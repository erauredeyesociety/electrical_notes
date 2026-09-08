#!/usr/bin/env python3
"""Synthesise a mono 16 kHz WAV so Lab 1 can be run and verified offline.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.

WHY THIS EXISTS. Lab 1 needs two audio files we do not have:

  1. `dsp26/audio_files/2086-149220-0033.wav`, the default in the handout's
     recipes.py. It is a LibriSpeech utterance the handout never says where to
     get -- a Canvas download, i.e. human work.
  2. A ~10 s mono 16 kHz music recording for the experimental task, which the
     handout says to capture from a real source such as YouTube. Also human
     work, and a synthetic tone is NOT a substitute for the submission.

This generator exists so the CODE can be exercised and the figures checked
without either. It writes something deliberately music-shaped -- a four-chord
progression with harmonics, per-note envelopes and a little vibrato -- because
a pure sine gives a spectrogram with one flat line, which would hide exactly
the bugs the spectral figures are meant to reveal.

    uv run --project dsp26 python tools/make_test_audio.py lab01/test_tone.wav
"""

import sys
import wave
from pathlib import Path

import numpy as np

SAMPLE_RATE = 16000      # the rate the experimental task specifies
DURATION_S = 10.0        # "approximately 10 seconds"
# A ii-V-I-vi progression in C, as MIDI note numbers. Musical enough that the
# spectrogram shows moving harmonic stacks rather than a static comb.
CHORDS = [
    [62, 65, 69],   # Dm
    [67, 71, 74],   # G
    [60, 64, 67],   # C
    [57, 60, 64],   # Am
]


def midi_to_hz(note: int) -> float:
    """Equal-tempered pitch: A4 = MIDI 69 = 440 Hz."""
    return 440.0 * 2 ** ((note - 69) / 12.0)


def main(out_path: str) -> int:
    rng = np.random.default_rng(6127)          # ERAU ID, so runs are repeatable
    n_total = int(SAMPLE_RATE * DURATION_S)
    audio = np.zeros(n_total, dtype=np.float64)

    seconds_per_chord = DURATION_S / len(CHORDS)
    n_chord = int(SAMPLE_RATE * seconds_per_chord)

    for c, chord in enumerate(CHORDS):
        start = c * n_chord
        t = np.arange(n_chord) / SAMPLE_RATE
        # Plucked-string envelope: fast attack, exponential decay. Gives clear
        # note onsets, which is what makes the spectrogram legible.
        env = np.exp(-2.5 * t) * (1 - np.exp(-200 * t))
        for note in chord:
            f0 = midi_to_hz(note)
            # Six harmonics with 1/k amplitude -- a sawtooth-ish timbre that
            # puts real energy across the band instead of one bin.
            for k in range(1, 7):
                fk = f0 * k
                if fk >= SAMPLE_RATE / 2:      # never synthesise above Nyquist
                    break
                vibrato = 1 + 0.002 * np.sin(2 * np.pi * 5.0 * t)
                audio[start:start + n_chord] += (
                    (1.0 / k) * env * np.sin(2 * np.pi * fk * vibrato * t)
                )

    # A little noise so the spectrogram floor is not digital silence.
    audio += 0.001 * rng.standard_normal(n_total)
    # Normalise to -3 dBFS, then quantise to signed 16-bit PCM.
    audio = 0.708 * audio / np.max(np.abs(audio))
    pcm = (audio * 32767).astype(np.int16)

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(1)        # mono, per the experimental task
        w.setsampwidth(2)        # 16-bit
        w.setframerate(SAMPLE_RATE)
        w.writeframes(pcm.tobytes())

    print(f"wrote {out}  mono  {SAMPLE_RATE} Hz  {n_total/SAMPLE_RATE:.1f} s  "
          f"{out.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "lab01/test_tone.wav"))
