"""
ALPHAMIX - Alphabet Letters Phonetic Harmonizer and Mixer
by Zee Weasel

This tool generates unique and customizable audio files that mimic dialogue sounds found in
video games like Okami and Animal Crossing. By utilizing Google TTS and PyDub, it creates
modified versions of alphabet letter sounds with adjustable pitch, playback speed, and other
effects to create a diverse range of phonetic-based sounds.

Users can control various settings, such as using short or long versions of letters, fade duration,
and more. The output is saved as a WAV file with a name that includes the user's arguments, making it
easy to identify and reuse different combinations of settings.
"""

import argparse
import os
import random
import gtts
import string
from pydub import AudioSegment
from pydub.playback import play

# Define variables
alphabet = string.ascii_lowercase
original_audio_dir = "original_audio"
modified_audio_dir = "modified_audio"

def generate_alphabet_audio(args):
    if not os.path.exists(original_audio_dir):
        os.makedirs(original_audio_dir)
        print("Generating alphabet audio files with Google TTS...")
        
        for letter in alphabet:
            for version, num_letters in [('short', args.short_version_length), ('long', args.long_version_length)]:
                random_letters = ''.join(random.choices(alphabet, k=num_letters))
                tts = gtts.gTTS(random_letters, lang="en")
                output_file = os.path.join(original_audio_dir, f"{letter}_{version}.mp3")
                tts.save(output_file)
                print(f"Generated audio for letter '{letter}' with '{version}' version.")
    else:
        print("Alphabet audio files already exist, skipping generation.")

def modify_alphabet_audio(args):
    if not os.path.exists(modified_audio_dir):
        os.makedirs(modified_audio_dir)

    modified_files_exist = all(
        os.path.exists(os.path.join(modified_audio_dir, f"{letter}_modified_{version}.mp3"))
        for letter in alphabet for version in ['short', 'long']
    )
    
    if not modified_files_exist:
        print("Applying modifications to alphabet audio files...")
        for letter in alphabet:
            for version in ['short', 'long']:
                input_file = os.path.join(original_audio_dir, f"{letter}_{version}.mp3")
                output_file = os.path.join(modified_audio_dir, f"{letter}_modified_{version}.mp3")

                audio = AudioSegment.from_file(input_file)

                # Apply pitch shift
                audio = audio._spawn(audio.raw_data, overrides={'frame_rate': int(audio.frame_rate * (2.0 ** (args.pitch / 1200.0)))})

                # Apply reverse audio
                if args.reverse:
                    audio = audio.reverse()

                # Apply playback speed modification
                audio = audio.speedup(args.playback_speed)

                audio.export(output_file, format="mp3")
                print(f"Applied modifications to letter '{letter}' with '{version}' version.")
    else:
        print("Modified alphabet audio files already exist, skipping modifications.")

def play_modified_string(args):
    print("Generating user-defined string...")
    combined_audio = None
    fade_duration = args.fade_duration

    for word in args.user_string.split():
        first_letter = word[0].lower()
        if first_letter in alphabet:
            version = "long" if len(word) >= args.short_version_length else "short"
            file_path = os.path.join(modified_audio_dir, f"{first_letter}_modified_{version}.mp3")
            audio = AudioSegment.from_file(file_path)

            # Apply fade-in and fade-out to reduce clicking
            audio = audio.fade_in(fade_duration).fade_out(fade_duration)

            if combined_audio is None:
                combined_audio = audio
            else:
                combined_audio = combined_audio.append(audio, crossfade=args.crossfade_duration)

            print(f"Added sound for letter '{first_letter}' to the output file.")

    if combined_audio is not None:
        output_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), f"output-{args.pitch}-{args.playback_speed}-{args.crossfade_duration}-{args.reverse}-{args.short_version_length}-{args.long_version_length}-{args.fade_duration}.wav")
        combined_audio.export(output_file, format="wav")
        print(f"Saved combined audio to '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_string", help="User-defined string of words.")
    parser.add_argument("--pitch", type=int, default=400, help="Pitch shift in cents (100 cents = 1 semitone).")
    parser.add_argument("--playback_speed", type=float, default=1.0, help="Playback speed (1.0 for normal, > 1 for faster, < 1 for slower).")
    parser.add_argument("--reverse", action="store_true", help="Whether to reverse the audio.")
    parser.add_argument("--crossfade_duration", type=int, default=50, help="Crossfade duration in milliseconds.")
    parser.add_argument("--short_version_length", type=int, default=2, help="Number of different letters for short version audio.")
    parser.add_argument("--long_version_length", type=int, default=6, help="Number of different letters for long version audio.")
    parser.add_argument("--use_long_version", type=int, default=3, help="Minimum word length to use the long version audio.")
    parser.add_argument("--fade_duration", type=int, default=50, help="Duration of fade-in and fade-out in milliseconds.")
    args = parser.parse_args()

    generate_alphabet_audio(args)
    modify_alphabet_audio(args)
    play_modified_string(args)
