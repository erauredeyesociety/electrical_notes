<!-- bgn hidden -->

-   #2026-08-31: Created based on last year's note and new project

<!-- end hidden -->

<!-- bgn cli -->

# Commands for doc creation:

## Notes for Fall 2026:

```sh
pandoc -N -V fontsize=11pt "dsp-bc--lab1-audio-signal.md" -o "dsp/dsp-bc--lab1-audio-signal-26.pdf" --data-dir=../../a5ar/pandoc -L include-files.lua -L select-blocks.lua -V blocks2select="notes" -L output2verbatim.lua --template=eagle.tex -V linestretch=1.1 -V verbatim-in-note -V codefontsize=9.5 -M geometry="top=2.7cm, bottom=2.8cm, left=2.5cm, right=2.4cm, headsep=0.3cm, footskip=0.9cm" --listings --filter pandoc-crossref -M listings -V float-placement-figure=htbp -M title="Lab 1: Exploring Audio Signals in Python" -M date="Fall 2026" -M author="Jianhua Liu" -V header-includes="\setcounter{section}{1}"

```
Note: will remove the sinusoidal signal part and only use the audio signal part.

<!-- end cli -->

<!-- bgn hidden -->

```toc
style: number
min_depth: 1
max_depth: 6
```

<!-- end hidden -->

<!-- bgn ch-title -->

# Lab 1: Exploring Audio Signals in Python

<!-- end ch-title -->

## Introduction

One of the best ways to build motivation for learning DSP concepts is to experiment with real audio signals. In this lab, we will read audio files and examine several important signal parameters. We will also explore both the time-domain and frequency-domain representations of the audio signal.


## Planning of the project

We will add new code to the existing dsp26 project. Specifically, we will:

-   Add code to `app_cli.py` so that we can execute the new lab functionality.
-   Add a new folder, `src/dsp26/lab1_audio_sig`, to host the core code for this lab.

Before proceeding, please ensure that Lab 0 works correctly. If you encounter any issues, please reach out to the TA or the instructor for assistance.


## Lab Task: Project Management (30 pts)

The project management task for Lab 1 is to:

-   Add the provided code to the project.
-   Add the required dependencies using `uv add <dependency_list>`.
-   Run the Lab 1 command of the application, as described below.

**Total points for this task: 30 pts**


### Adding code to `app_cli.py`

In the code section designated for Labs (see comments in the file), add the following code to enable the command:

```sh
dsp26 play-plot-audio --path-name <a_wave_file.wav>
```

This command can be executed from a terminal in any directory containing the specified WAV file.

`app_cli.py`:
```python
# Lab1-audio-sig
@app.command()
def play_plot_audio(
    path_name: str = typer.Option(
        "",
        "--path-name",
        help="Optional output path name for loading an audio file. " \
        "If set, the specified audio file will be loaded.",
    ),
):
    """Play and plot audio signal.
    Use --path-name to load audio file from."""
    play_plot_audio_(path_name=path_name)
```

### Adding Lab code under `src/dsp26/lab1_audio_sig`

The lab includes three files in this folder:

`audio_player.py`

This file contains a function that plays an audio file (in WAV format) through a GUI interface. The code was generated with the assistance of Kilo Code in VS Code. No modifications are needed---simply include it as provided.

```python
"""Simple Audio Player using simpleaudio and tkinter"""

import os
import tempfile
import time
import wave
from pathlib import Path
import tkinter as tk

import simpleaudio as sa

class AudioPlayer:
    _instance = None
    _play_obj = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self._root = None
        self._is_playing = False
        self._is_paused = False
        self._audio_file = None
        self._play_obj = None
        self._duration = 0
        self._pause_offset = 0.0
        self._play_started_at = 0.0
        self._current_file_path = None
        self._temp_wav_path = None
        self._play_button = None
        self._has_played_once = False

    def _get_duration(self, file_path):
        """Get audio duration from WAV file"""
        try:
            with wave.open(str(file_path), 'rb') as wav:
                frames = wav.getnframes()
                rate = wav.getframerate()
                duration = frames / float(rate)
                return duration
        except:
            return 30  # Default fallback

    def _cleanup_temp_file(self):
        if self._temp_wav_path and Path(self._temp_wav_path).exists():
            try:
                Path(self._temp_wav_path).unlink()
            except OSError:
                pass
        self._temp_wav_path = None

    def _play_from_offset(self, offset_seconds: float = 0.0):
        """Start playback from a specific offset in seconds."""
        if not self._current_file_path or not self._current_file_path.exists():
            return

        self._cleanup_temp_file()

        offset_seconds = max(0.0, float(offset_seconds))
        with wave.open(str(self._current_file_path), "rb") as wav_file:
            sample_rate = wav_file.getframerate()
            channels = wav_file.getnchannels()
            sampwidth = wav_file.getsampwidth()
            total_frames = wav_file.getnframes()
            start_frame = min(int(offset_seconds * sample_rate), total_frames)
            wav_file.setpos(start_frame)
            remaining = wav_file.readframes(total_frames - start_frame)

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            self._temp_wav_path = tmp.name

        with wave.open(self._temp_wav_path, "wb") as out_file:
            out_file.setnchannels(channels)
            out_file.setsampwidth(sampwidth)
            out_file.setframerate(sample_rate)
            out_file.writeframes(remaining)

        self._play_obj = sa.WaveObject.from_wave_file(
            self._temp_wav_path).play()
        self._is_playing = True
        self._is_paused = False
        self._play_started_at = time.time() - offset_seconds

    def _play(self):
        """Play audio or replay from the beginning after the first run."""
        try:
            if not self._audio_file:
                return

            if self._has_played_once:
                if self._play_obj:
                    self._play_obj.stop()
                self._cleanup_temp_file()
                self._pause_offset = 0.0
                self._is_playing = False
                self._is_paused = False
                self._play_from_offset(0.0)
                if self._play_button:
                    self._play_button.config(text="Replay")
                return

            if not self._is_playing:
                self._pause_offset = 0.0
                self._play_from_offset(0.0)
                self._has_played_once = True
                if self._play_button:
                    self._play_button.config(text="Replay")
        except Exception as e:
            print(f"Error playing: {e}")

    def _pause(self):
        """Pause audio by stopping current playback and storing offset."""
        if self._is_playing and self._play_obj:
            self._pause_offset = max(0.0, time.time() - self._play_started_at)
            self._play_obj.stop()
            self._is_playing = False
            self._is_paused = True

    def _resume(self):
        """Resume audio from the last paused offset."""
        if self._is_paused and self._current_file_path:
            self._play_from_offset(self._pause_offset)

    def _replay(self):
        """Replay audio from start and reset pause state."""
        if self._play_obj:
            self._play_obj.stop()
        self._cleanup_temp_file()
        self._pause_offset = 0.0
        self._is_playing = False
        self._is_paused = False
        if self._current_file_path:
            self._play_from_offset(0.0)

    def _exit(self):
        """Exit the player."""
        self._is_playing = False
        self._is_paused = False
        self._pause_offset = 0.0
        if self._play_obj:
            self._play_obj.stop()
        self._cleanup_temp_file()
        if self._root:
            self._root.destroy()
        self._instance = None

    def play(self, file_path):
        """Main method to play audio file"""
        if isinstance(file_path, str):
            file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        # Close any existing instance
        if self._root:
            self._exit()
            time.sleep(0.1)

        # Load audio file
        print(f"Loading: {file_path}")
        self._current_file_path = file_path
        self._audio_file = sa.WaveObject.from_wave_file(str(file_path))
        self._duration = self._get_duration(file_path)
        print(f"Duration: {self._duration:.2f} seconds")

        # Create GUI
        self._root = tk.Tk()
        self._root.title("Audio Player")
        self._root.geometry("500x300")

        # Label
        label = tk.Label(
            self._root,
            text=f"Playing: {file_path.name}",
            font=("Arial", 12)
        )
        label.pack(pady=10)

        # Duration label
        duration_label = tk.Label(
            self._root,
            text=f"Duration: {self._duration:.2f} seconds",
            font=("Arial", 10)
        )
        duration_label.pack(pady=5)

        # Button frame
        button_frame = tk.Frame(self._root)
        button_frame.pack(pady=10)

        # Buttons
        buttons = [
            ("Play", self._play),
            ("Pause", self._pause),
            ("Resume", self._resume),
            ("Exit", self._exit),
        ]

        self._play_button = None
        row = 0
        col = 0
        for text, cmd in buttons:
            btn = tk.Button(
                button_frame,
                text=text,
                width=10,
                height=2,
                command=cmd
            )
            if text == "Play":
                self._play_button = btn
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 1
                row += 1

        # Window close handler
        self._root.protocol("WM_DELETE_WINDOW", self._exit)

        # Start main loop
        self._root.mainloop()


# --------------------------------------------------
# Public API
# --------------------------------------------------

def play_audio(file_path):
    """Play an audio file with GUI."""
    os.environ['PYTHON_GIL'] = '0'
    player = AudioPlayer()
    player.play(file_path)
```

`audio_sig.py`

This file contains several utility functions for audio signal analysis, including:

-   Retrieving and displaying audio file metadata (e.g., sample rate, number of channels, bit depth, and duration).
-   Plotting the time-domain waveform of the audio signal.
-   Visualizing the frequency-domain spectrum using various representations (e.g., magnitude spectrum, power spectral density, and spectrogram).

These functions form the core analytical components of the lab and are called by the main CLI command.

```python
import wave

import librosa.display
import matplotlib.pyplot as plt
import numpy as np

## Print various parameters of an audio file
# Open the WAV file in read mode to access the properties
def print_wave_file_properties(wav_file_path):
    wav_file_path = str(wav_file_path)
    with wave.open(wav_file_path, 'r') as wav_file:
        print(f"\nDetailed properties of {wav_file_path} ------------------")
        # Number of audio channels
        n_channels = wav_file.getnchannels()
        print("Number of channels:", n_channels)

        # Sample width in bytes
        sample_width = wav_file.getsampwidth()
        print("Sample width (bytes):", sample_width)

        # Frame rate (sample rate)
        frame_rate = wav_file.getframerate()
        print("Frame rate (sample rate):", frame_rate)

        # Number of audio frames
        n_frames = wav_file.getnframes()
        print("Number of frames:", n_frames)

        # Duration of the audio in seconds
        duration = n_frames / float(frame_rate)
        print("Duration (seconds):", duration)
        # Other properties can be accessed similarly


# Display the waveform from start_s to end_s seconds
def plot_audio_sig_in_td(audio, sample_rate, start_s=0.0, end_s=None):
    start_idx = int(start_s * sample_rate)
    if end_s == None:
        end_idx = len(audio)
        end_s = end_idx / sample_rate
    else:
        end_idx = int(end_s * sample_rate)

    segment = audio[start_idx:end_idx]
    time_length = len(segment) / sample_rate

    plt.figure(figsize=(16, 9))
    librosa.display.waveshow(segment, sr=sample_rate, color="blue")

    ax = plt.gca()
    ax.set_xlim(0, time_length)          # keep the selected window visible
    ax.set_xticks([0, time_length])      # left and right edge only
    ax.set_xticklabels([f"{start_s}", f"{end_s}"])  # label as start_s/end_s

    plt.title(f"Waveform from {start_s:.1f}s to {end_s:.1f}s")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()


def plot_audio_sig_in_fd(audio, sample_rate, fd_format='linear'):
    spec = librosa.stft(audio, n_fft=512, hop_length=160, win_length=400)
    spec_db = librosa.amplitude_to_db(np.abs(spec), ref=np.max)

    plt.figure(figsize=(16, 9))
    librosa.display.specshow(spec_db, y_axis=fd_format, x_axis='time',
                             sr=sample_rate, hop_length=160)
    plt.colorbar()
    plt.title('Spectrogram of an Audio Signal')
    plt.show()
```

`recipes.py`

This file serves as the bridge between the CLI commands defined in `app_cli.py` and the core functionality implemented in the other module files. It contains the wrapper functions that:

-   Parse and validate inputs received from the command line.
-   Call the appropriate core functions from `audio_sig.py` and `audio_player.py`.
-   Handle any necessary data transformation or error handling.

This separation of concerns keeps the CLI layer clean and focused on command parsing, while the core logic remains modular and reusable.

`recipes.py`:
```python
from pathlib import Path

import librosa

from dsp26.lab1_audio_sig.audio_player import play_audio
from dsp26.lab1_audio_sig.audio_sig import (
    print_wave_file_properties,
    plot_audio_sig_in_td,
    plot_audio_sig_in_fd,
)


def play_plot_audio_(path_name: str = ""):
    if path_name:
        audio_file_path = path_name
    else:
        # Get the directory containing this Python file:
        # dsp26/src/dsp26/lab1_audio_sig/recipes.py
        current_dir = Path(__file__).resolve().parent
        # Go up:
        # lab1_audio_sig -> dsp26 -> src -> project root (dsp26)
        project_root = current_dir.parents[2]
        # Construct the audio file path
        audio_file_path = project_root / "audio_files" / "2086-149220-0033.wav"

    play_audio(audio_file_path)

    print_wave_file_properties(audio_file_path)

    audio, sample_rate = librosa.load(audio_file_path, sr=None)

    plot_audio_sig_in_td(audio, sample_rate)
    plot_audio_sig_in_td(audio, sample_rate, 0.4, 1.4)

    plot_audio_sig_in_fd(audio, sample_rate)
    plot_audio_sig_in_fd(audio, sample_rate, 'log')
    plot_audio_sig_in_fd(audio, sample_rate, 'mel')
```

### Adding dependencies

You may need to add new dependencies for this lab and future labs. We will not explicitly specify which dependencies are required. A common approach is to simply run the application; if a package named <a_package> is missing, you can add it using:

```sh
uv add <a_package>
```

Alternatively, you can proactively add any packages you anticipate needing.


### Running the provided code

This process may take a few steps if dependencies are not installed correctly. You may need to run the following commands iteratively until all dependencies are satisfied:

```sh
uv add <a_package>
dsp26 play-plot-audio
```

**Note**:

-   Once installed via uv, the app can be run from anywhere on your system.
-   If new dependencies are added, you may need to perform **a forced local installation**. Refer to the uv cheatsheet for the specific command if this becomes necessary.


### Artifacts for the project management task

To demonstrate that your code works correctly, take screenshots of the following:

-   The output of running `dsp26 --help`.
-   The Audio Player window when running `dsp26 play-plot-audio`.
-   Each of the **5 figures** displayed after closing the Audio Player window. (Note: You must close one figure to reveal the next.)


## Experimental task (20 pts)

Once the basic setup is complete, record a **short music audio file** with the following specifications:

-   Channels: Single channel (mono)
-   Sample rate: 16 kHz
-   Duration: Approximately 10 seconds

You may use any music source (e.g., YouTube). Save the file in **WAV format** in a folder of your choice. Then, run the app in that folder with the specified file name to:

-   Listen to the music.
-   View the waveform.
-   Examine the spectrum displays.


### Artifacts for the experimental task

Take screenshots of the following:

-   The second (zoomed-in) waveform figure.
-   The last spectrum figure.


## Programming tasks (40 pts)

**Total points for this task: 40 pts**

The `dsp26 play-plot-audio` command currently supports one option: `--path-name`, which we have already used.

In Figure 2, we displayed a zoomed-in waveform from 0.4 to 1.4 seconds. Now, we extend this functionality to support arbitrary start and end times. The good news is that the `plot_audio_sig_in_td` function already supports this feature. Therefore, we only need to:

-   Add two new options to the `dsp26 play-plot-audio` command.
-   Use the same default values as those defined in the `plot_audio_sig_in_td` function.

**AI-Assisted Coding Note:**

Without AI assistance, this coding task can be challenging due to the need to navigate multiple files and function signatures. With AI-assisted coding (e.g., using Kilo Code in VS Code), this becomes straightforward:

-   Simply describe the problem and requirements to the AI, and it will generate the necessary code.
-   You must still be able to read, understand, and integrate the code into the appropriate locations.

Kilo Code provides free LLM access for coding within VS Code, with no need to purchase tokens. While there is a token limit, it is more than sufficient for basic coding tasks.


### Artifacts for the programming task

Submit the following:

-   Code Snippet: The code added to `app_cli.py` and/or `lab1_audio_sig/recipes.py` for the new start and end time parameters.
-   Code Explanation: A concise summary of how the command-line options work. (This can be generated by an LLM, but you should condense it to the most relevant points.)
-   Screenshot of zoomed-in figure (of your music file) from 0.5 to 1.5 seconds.


## Submission (10 pts)

**Total points for submission: 10 pts**

Submit a single PDF file containing all the artifacts collected from the tasks above:

-   Project Management Task artifacts
-   Experimental Task artifacts
-   Programming Task artifacts

Important: The project will receive a grade only after you demonstrate the running results to the TA, in addition to submitting the collection of artifacts.
