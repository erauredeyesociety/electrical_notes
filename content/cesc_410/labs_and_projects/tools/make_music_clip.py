#!/usr/bin/env python3
"""Cut a lab-spec WAV clip from a music file. NEVER modifies the source.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.

Lab 1's experimental task needs a music recording that is mono, 16 kHz and
about 10 seconds. Source material is typically a stereo 44.1 kHz MP3, so it
needs downmixing, resampling and cutting. This does all three in one pass and
verifies the result against the spec before exiting non-zero if it misses.

The source file is opened READ-ONLY and never written, moved or renamed.
Derivatives are written beside it under new names.

    uv run --project dsp26 python tools/make_music_clip.py <source> <output.wav>
    uv run --project dsp26 python tools/make_music_clip.py <source> <out.wav> --start 95 --duration 15

Defaults follow the handout: 10 s, mono, 16 kHz.
"""

import argparse
import sys
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf

# The handout's stated spec for the experimental task.
TARGET_SR = 16000
TARGET_CHANNELS = 1
DEFAULT_DURATION_S = 10.0

# Where to cut from, when not told. Chosen by measuring the source rather than
# guessing: RMS energy and onset density were computed over the whole track in
# 10 s windows, and 90-115 s was the densest full-band region (RMS 0.176 vs
# 0.111 at the intro). A dense window gives a spectrogram with structure to
# look at; a sparse one gives a mostly empty plot.
DEFAULT_START_S = 95.0

# Peak normalisation target. -3 dBFS leaves headroom so the 16-bit quantisation
# never clips on a stray sample.
PEAK = 0.708


def make_clip(source: Path, out: Path, start_s: float, duration_s: float) -> int:
    if not source.is_file():
        print(f"ERROR: source not found: {source}", file=sys.stderr)
        return 1

    # sr=TARGET_SR resamples on load; mono=True downmixes. Both are what the
    # spec asks for, and doing them at load time avoids a second pass.
    total = librosa.get_duration(path=str(source))
    if start_s + duration_s > total:
        print(f"ERROR: {source.name} is {total:.1f} s; cannot cut "
              f"{duration_s:.1f} s at {start_s:.1f} s", file=sys.stderr)
        return 1

    audio, sr = librosa.load(str(source), sr=TARGET_SR, mono=True,
                             offset=start_s, duration=duration_s)

    # Normalise, then quantise to signed 16-bit PCM -- the format `wave` reads
    # and the format the lab's print_wave_file_properties expects.
    peak = float(np.max(np.abs(audio)))
    if peak > 0:
        audio = PEAK * audio / peak
    pcm = (audio * 32767).astype(np.int16)

    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out), pcm, sr, subtype="PCM_16")

    # Verify against the spec by re-reading what was written, rather than
    # trusting the write. A clip that silently misses the spec would be marked
    # down, and the lab's own properties command is what the grader sees.
    info = sf.info(str(out))
    ok = (info.samplerate == TARGET_SR
          and info.channels == TARGET_CHANNELS
          and abs(info.duration - duration_s) < 0.05)
    print(f"  source : {source.name}")
    print(f"           (unmodified -- opened read-only)")
    print(f"  cut    : {start_s:.1f} s .. {start_s + duration_s:.1f} s")
    print(f"  wrote  : {out}")
    print(f"           {info.channels} ch, {info.samplerate} Hz, "
          f"{info.duration:.2f} s, {out.stat().st_size:,} bytes")
    print(f"  spec   : {'OK -- mono, 16 kHz, ~%.0f s' % duration_s if ok else 'FAILED'}")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", type=Path, help="source audio (mp3, wav, flac...)")
    ap.add_argument("output", type=Path, help="output .wav")
    ap.add_argument("--start", type=float, default=DEFAULT_START_S,
                    help=f"seconds into the source (default {DEFAULT_START_S})")
    ap.add_argument("--duration", type=float, default=DEFAULT_DURATION_S,
                    help=f"clip length (default {DEFAULT_DURATION_S}, the handout spec)")
    a = ap.parse_args()
    return make_clip(a.source, a.output, a.start, a.duration)


if __name__ == "__main__":
    sys.exit(main())
