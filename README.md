# ALPHAMIX - Alphabet Letters Phonetic Harmonizer and Mixer
> Generate unique and customizable audio files that mimic dialogue sounds

This tool generates unique and customizable audio files that mimic dialogue sounds found in
video games like Okami and Animal Crossing. By utilizing Google TTS and PyDub, it creates
modified versions of alphabet letter sounds with adjustable pitch, playback speed, and other
effects to create a diverse range of phonetic-based sounds.

Users can control various settings, such as using short or long versions of letters, fade duration,
and more. The output is saved as a WAV file with a name that includes the user's arguments, making it
easy to identify and reuse different combinations of settings.

## Features

* Generates alphabet audio files with Google Text-to-Speech (TTS)
* Applies modifications to alphabet audio files:
** Pitch shift
** Reverse audio
** Playback speed modification
* Creates a combined audio file from a user-defined string with the following features:
** Uses short and long versions of the alphabet letters
** Applies fade-in and fade-out effects to reduce clicking
* Supports user-defined values for the following arguments:
** User-defined string of words
** Pitch shift in cents (100 cents = 1 semitone)
** Playback speed (1.0 for normal, > 1 for faster, < 1 for slower)
** Whether to reverse the audio
** Crossfade duration in milliseconds
** Duration of fade-in and fade-out in milliseconds
** Number of letters to use for the short and long versions of the alphabet letters
* Saves the combined audio file as a .wav file with the user-defined argument values in the filename

## Installing / Getting started

1. Clone this repository.
2. Install the required Python packages: pip install gtts pydub argparse
3. Run the script with the desired arguments: python alphamix.py --user_string "hello world" --pitch 600 --playback_speed 1.5 --reverse --crossfade_duration 200 --short_version_length 2 --long_version_length 4 --fade_duration 50

## List of Arguments

- `--pitch`: Pitch shift in cents (100 cents = 1 semitone). Default is 600.
- `--playback_speed`: Playback speed (1.0 for normal, > 1 for faster, < 1 for slower). Default is 1.0.
- `--reverse`: Whether to reverse the audio. Default is False.
- `--crossfade_duration`: Crossfade duration in milliseconds. Default is 100.
- `--short_version_letters`: Number of different letters to use to generate the short version of each letter's audio file. Default is 2.
- `--long_version_letters`: Number of different letters to use to generate the long version of each letter's audio file. Default is 4.
- `--min_word_length`: Minimum length of words to use the long version of the audio files. Default is 3.
- `--fade_duration`: Duration of fade-in and fade-out in milliseconds. Default is 50.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
