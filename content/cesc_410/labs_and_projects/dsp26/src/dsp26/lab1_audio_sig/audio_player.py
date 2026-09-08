"""Simple Audio Player using simpleaudio and tkinter.

Transcribed verbatim from the Lab 1 handout, which states the file needs no
modification. It opens a Tk window with play/pause controls and streams the
WAV through simpleaudio; `play()` blocks in `mainloop()` until the window is
closed, which is what makes the five figures appear one after the other.

This file itself is unmodified -- every change Lab 1 needed is in recipes.py
and is marked there. Note that `play()` needs a real display and does not
return until the window is closed, which is why recipes.py does not call it
during an unattended run.
"""

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
