# Lab 1 — Exploring Audio Signals in Python

**Handout:** [`dsp-bc--lab1-audio-signal.md`](dsp-bc--lab1-audio-signal.md) · **Started:** 2026-09-08 · **Status:** **DONE.** Demo signed off by the TA 2026-09-08. All 12 required artifacts verified present in `lab01-artifacts-nelson-gatlin.pdf`. Only the Canvas upload remains.

> **Updated 2026-09-08 (evening) — the TA published answers.** A Canvas announcement and a one-page
> supplemental PDF closed several questions this file used to carry as open, and **superseded one
> conclusion that was wrong**: the default `.wav` is the TA's own file, not the LibriSpeech utterance
> its filename names. Both documents are transcribed here —
> [`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md) and
> [`ta_supplement_lab1_reference.md`](ta_supplement_lab1_reference.md) — and every affected section
> below has been rewritten. What changed, in one table:
>
> | Was | Now |
> | --- | --- |
> | *"The default `.wav` is a LibriSpeech utterance; it is not on Canvas and did not need to be."* | **Wrong conclusion.** The TA uploaded a `.wav` with that name; it is a 10 s synthetic tone pair, not speech. It is installed and is what `figs/` was regenerated from |
> | *"No TA name or contact is recorded anywhere in this repo."* | **Ryle**, Discord `ryletraub_30890` (email offered, address not stated) |
> | *"When is the deliverable due?"* — unrecorded | **1 week after the lab is assigned**, on Canvas |
> | *"Demo at the start of the meeting"* — inferred from the course info | **Demo by the next lab section**; early checkout allowed |
> | *"Is our `app_cli.py` right?"* — untested against anything | **Confirmed.** The TA's reference file is Lab 0's plus the Lab 1 snippet; ours is that plus the graded programming task |
> | H3's Audio Player window — described from our own code | **Described from the TA's screenshot**, element by element |

**Goal:** add a `play-plot-audio` command to the shared `dsp26` package that plays a WAV, prints its
header properties, and plots it five ways — waveform (full and zoomed) plus spectrogram on linear,
log and mel frequency axes — then extend the command with arbitrary start/end times.

---

## Inputs

Each missing input has a block in **Needs a human** below, and the *If missing, blocks* column here
says the same thing that block says.

| File | Purpose | Status | If missing, blocks |
| --- | --- | --- | --- |
| `dsp-bc--lab1-audio-signal.md` + `dsp-bc--lab1-audio-signal-26.pdf` | handout — **note the `-26` in the PDF name**; there is no `dsp-bc--lab1-audio-signal.pdf` | ✅ present | — |
| `dsp26/audio_files/2086-149220-0033.wav` | the default file `recipes.py` loads when `--path-name` is omitted. **This is the TA's uploaded file** — see below | ✅ **installed and verified against the TA's own output** | — (nothing; it is here) |
| [`ta_supplied_2086-149220-0033.wav`](ta_supplied_2086-149220-0033.wav) | the as-downloaded copy of that file, kept in this folder as the provenance record. Byte-identical to the installed one (`md5 b8c6e2fc5147d4c627efa0f443c82102`) | ✅ present | — |
| `dsp26/audio_files/librispeech_2086-149220-0033.wav.notused` | the **superseded** LibriSpeech decode, parked beside the real one under a `.notused` name so nothing loads it by accident. Kept only as evidence for the provenance note below | ✅ parked, unused | — |
| [`ta_announcement_lab1_and_future_labs.html`](ta_announcement_lab1_and_future_labs.html) + [`.md`](ta_announcement_lab1_and_future_labs.md) | the TA's Canvas announcement *"Lab 1 and Future Labs"* — saved page fragment plus a greppable transcript. **Source of the demo/submission policy and the TA's contact** | ✅ present, retrieved 2026-09-08 | — |
| [`ta_supplement_lab1_reference.pdf`](ta_supplement_lab1_reference.pdf) + [`.md`](ta_supplement_lab1_reference.md) | the TA's one-page supplemental reference (Canvas name `CESC410L_Lab1.pdf`) — `app_cli.py` guidance, the Windows build-tools fix, where the `.wav` goes, and **the screenshot of the expected terminal + Audio Player output**. The PDF holds the screenshot; the `.md` transcribes it | ✅ present, retrieved 2026-09-08 | — |
| [`ta_reference_app_cli.py`](ta_reference_app_cli.py) | the TA's complete reference `app_cli.py` — 58 lines, **CRLF**, no trailing newline, exactly as Canvas served it. **Reference only — never imported, never packaged.** Compared against ours under *Code* below | ✅ present | — |
| `Rick Astley - Never Gonna Give You Up ….mp3` | source supplied by the operator 2026-09-08 for the experimental task. **Kept unmodified**; opened read-only | ✅ present | — |
| `music_clip.wav` | the ~10 s mono 16 kHz clip the experimental task requires, cut from that source | ✅ **generated and spec-verified** | — |
| `test_tone.wav` | synthetic stand-in used before any supplied file existed. **No longer used for any artifact** — kept only so the lab can be re-run with no audio at all | ✅ generated | — |

⚠ **Four files in this folder are now 10.00 s / 16 kHz / mono / 320,044 bytes** — the TA's `.wav`,
its `ta_supplied_` copy, `music_clip.wav` and `test_tone.wav`. **Size and duration no longer tell them
apart; only `md5sum` and the printed path do.** That matters twice below: for the stale
`out/run_log.txt` and for anything that screenshots a header block.

| File | md5 |
| --- | --- |
| `dsp26/audio_files/2086-149220-0033.wav` and `ta_supplied_2086-149220-0033.wav` | `b8c6e2fc5147d4c627efa0f443c82102` |
| `music_clip.wav` | `e50f63f797773f6626c261dd90c21f72` |
| `test_tone.wav` | `04cbca2fa719db68e81c73a986b5b478` |
| `dsp26/audio_files/librispeech_2086-149220-0033.wav.notused` | `1617f1812d3abbc25b41ef855aa09eb1` (237,964 bytes, 7.435 s — the odd one out) |

### Provenance of `2086-149220-0033.wav` — settled 2026-09-08

**The TA supplied this file, and the TA's copy is the one that counts.** It is the file installed at

    /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files/2086-149220-0033.wav

and every figure in `lab01/figs/` was regenerated from it.

**Why the TA's copy and not any other:** a grader comparing our figures against theirs is looking at
*their* audio. The TA's supplemental PDF prints the header block their run produces, and ours matches
it line for line ([`ta_supplement_lab1_reference.md`](ta_supplement_lab1_reference.md)). Any other
file with the same name would put a different waveform under the same figure caption — which is
exactly what almost happened here.

Verified shape:

```
Number of channels: 1
Sample width (bytes): 2
Frame rate (sample rate): 16000
Number of frames: 160000
Duration (seconds): 10.0
```

`md5sum` → `b8c6e2fc5147d4c627efa0f443c82102`, 320,044 bytes.

**What the audio actually is.** Not speech. A steady two-tone dyad held for the whole 10 s — **440.0 Hz
(A4) and 554.4 Hz (C♯5)**, each at half scale, summing to a full-scale ±1.0 waveform whose per-100 ms
RMS never moves outside 0.494–0.506. That is why `figs/lab1_audio_fig1_waveform_full.png` is a solid
blue block and why figures 3–5 are two flat horizontal bands. **Both are correct.** Re-derive it with:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 python -c "
import numpy as np, wave
w = wave.open('dsp26/audio_files/2086-149220-0033.wav')
y = np.frombuffer(w.readframes(w.getnframes()), dtype='<i2').astype(float) / 32768
Y = np.abs(np.fft.rfft(y * np.hanning(len(y))))
f = np.fft.rfftfreq(len(y), 1 / w.getframerate())
print(' '.join(f'{f[i]:.1f} Hz' for i in np.argsort(Y)[::-1][:2]))
"
```

Expected, exactly: `440.0 Hz 554.4 Hz` — verified 2026-09-08. The TA's own terminal shows a `Generated WAV file at: …` line just before
the run, so the file was synthesised, not recorded — consistent with the announcement's *"You are
welcome to generate your own .wav file, but for simplicity, I've uploaded a ready-to-use sample."*

#### Historical note — the LibriSpeech reading, and why it was superseded

This is kept because it is **still a correct observation about the filename**, and because it is the
reason a wrong file sat in `audio_files/` for five hours.

`2086-149220-0033` **is** a LibriSpeech utterance id — speaker `2086`, chapter `149220`, utterance
`0033` — from a public, freely redistributable corpus ([openslr.org/12](https://www.openslr.org/12/),
CC BY 4.0), and speaker 2086 really is in the `dev-clean` subset. The handout names the file exactly
once, at line 459, inside a code block:

```python
audio_file_path = project_root / "audio_files" / "2086-149220-0033.wav"
```

— with no prose sentence, no link and no "download from" anywhere in its 19 KB. With no other lead,
the corpus original was fetched, decoded to WAV, and used. **That reasoning was sound. The conclusion
was wrong**, and the announcement is what proved it:

| | TA's file (authoritative) | LibriSpeech `dev-clean/2086/149220/2086-149220-0033.flac` |
| --- | --- | --- |
| Duration | 10.00 s | 7.435 s |
| Frames | 160000 | 118960 |
| Size | 320,044 bytes | 237,964 bytes |
| md5 (as WAV) | `b8c6e2fc5147d4c627efa0f443c82102` | `1617f1812d3abbc25b41ef855aa09eb1` |
| Content | synthetic 440 + 554.4 Hz dyad | read speech, with silences and pauses |

Same name, different audio, and **the samples differ** — this is not a re-encode of the same clip. The
LibriSpeech decode is parked at
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files/librispeech_2086-149220-0033.wav.notused`
so the evidence survives and nothing loads it. **Do not restore it**; the only thing it is good for is
re-checking the table above.

**The lesson, filed as a known issue:** a filename that decodes cleanly as a public-dataset id is a
*hypothesis about the filename*, never proof of what the bytes are —
[KI-19](../reference_docs/known_issues.md#ki-19--a-filename-that-parses-as-a-public-dataset-id-is-not-proof-of-provenance).
The handout gap is real and is still worth mentioning to the TA, but it is now a documentation nit,
not a blocker: the answer was posted in Announcements.

⚠ **`tools/check_inputs.py` reported this lab as clean the whole time, including when the file was
absent and when it was the wrong file.** The checker scans *Markdown links*; this path is built in
**Python**, so it is structurally invisible to the tool — and no checker anywhere compares file
*contents* to an expectation. Logged as [KI-12](../reference_docs/known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python).

---

## Code

Lab code lives in the shared package, not here — see [`../README.md`](../README.md#why-code-and-docs-are-split).

| File | What it does |
| --- | --- |
| `dsp26/src/dsp26/lab1_audio_sig/audio_player.py` | Tk + simpleaudio player, transcribed verbatim; handout says no modification needed |
| `dsp26/src/dsp26/lab1_audio_sig/audio_sig.py` | `print_wave_file_properties`, `plot_audio_sig_in_td`, `plot_audio_sig_in_fd` |
| `dsp26/src/dsp26/lab1_audio_sig/recipes.py` | orchestrates player → properties → five figures |
| `dsp26/src/dsp26/app_cli.py` | adds the `play-plot-audio` command and its four options |

New dependencies: `librosa` (load, STFT, display) and `simpleaudio` (playback).

### Our `app_cli.py` vs the TA's reference — checked, and **nothing needs to change**

The announcement says *"You should append the provided code snippet to your `app_cli.py` file from
Lab 0. The complete reference file has been uploaded as well"*, and the supplement adds *"make sure
you leave everything in there alone – simply copy and paste the new content."* That reference file is
[`ta_reference_app_cli.py`](ta_reference_app_cli.py) — 58 lines (`wc -l` reports 57; the last one has
no trailing newline). **Posting it does not mean we diverged** — read this before "fixing" anything.

| Piece | TA's reference | Ours (`dsp26/src/dsp26/app_cli.py`) | Verdict |
| --- | --- | --- | --- |
| Lab 0's file, untouched | `--version` callback, `plot-sinusoids-td-fd` with `--folder-name` | identical in behaviour and option names | ✅ *"leave everything in there alone"* is satisfied |
| The Lab 1 snippet | `play_plot_audio` with `--path-name` only | present, same name, same option, same default `""` | ✅ appended as instructed |
| `--start-s` / `--end-s` | **absent** | present | ✅ **this is the graded programming task**, handout § *Programming task*. The reference file is the *starting* point students extend; a submission that matched it exactly would be missing the task |
| `--folder-name` on `play-plot-audio` | absent | present | ✅ ours, deviation 3 below — headless figure saving. It is how `figs/` exists at all without a human closing six windows |
| Comments / docstrings | terse | fuller, per [`../reference_docs/code_commenting.md`](../reference_docs/code_commenting.md) | ✅ style, not behaviour |

So the relationship is: **TA's reference = Lab 0 + the snippet. Ours = that + the programming task +
one saving option.** Confirm it yourself — the diff is short and every line of it is expected:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
diff -u <(sed 's/\r$//' lab01/ta_reference_app_cli.py) dsp26/src/dsp26/app_cli.py
```

⚠ **The `sed` is not optional.** The TA's file has **CRLF** line endings (`file` says so), so a plain
`diff -u lab01/ta_reference_app_cli.py …` reports *every* line as changed and tells you nothing.
Normalised, the diff is exactly four hunks: our module docstring, our fuller `--version` comments,
the three added options, and the multi-line call that passes them on. Nothing else.

**`ta_reference_app_cli.py` is reference material only.** It is never imported, never on `sys.path`,
and `make_submission.sh` packages from `dsp26/src/`, not from `lab01/` — so it cannot leak into a
submission. Do not copy it over `dsp26/src/dsp26/app_cli.py`; that would delete the programming task.

---

## Reproduce

Every block below starts from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`, and each one says so with its own
`cd` — no block assumes you are already there.

```sh
export PATH="$HOME/.local/bin:$PATH"    # if uv is not already on PATH
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26
uv add librosa simpleaudio
uv sync
```

> **`.venv/` already exists and is in sync**, so this is a no-op today. It is here so the lab can be
> rebuilt from a clean checkout.

### What every `dsp26` command prints that this README's outputs would otherwise hide

Two things appear on **every** `dsp26` invocation, including `dsp26 --help`. Both are expected. They
are reproduced in the output blocks below so that you can compare what you see against what should be
there, rather than wondering whether your run went wrong.

1. **`The basic frequency is 4.0 Hz.` is always the first line of stdout.** It is a module-level
   `print` in `dsp26/src/dsp26/lab0_sinusoids/recipes.py` line 36, which runs at import time, so
   every Lab 1 command inherits it. It is Lab 0's line, it is harmless, and it is *also* in
   `lab01/out/dsp26_help.txt` and in the `dsp26 --help` screenshot H3 asks for — so that screenshot
   is not wrong when it shows it.
2. **Three `UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown` lines go to
   stderr** whenever `MPLBACKEND=Agg` is set. That is `plt.show()` being a no-op headless
   ([KI-02](../reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless)) — exactly the
   condition deviation 1 exists to work around. Figures are still saved. Add `2>/dev/null` if they
   are in your way.

**The five figures from the handout's default input** — no `--path-name`, so `recipes.py` resolves
`dsp26/audio_files/2086-149220-0033.wav` itself. **This is the one command that regenerates `figs/`:**

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name lab01
```

Output — **stdout, in full, including the Lab 0 line noted above**:

```
The basic frequency is 4.0 Hz.
MPLBACKEND=Agg -- batch run, skipping the audio player window. Run without it under a desktop session to hear the file.

Detailed properties of /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files/2086-149220-0033.wav ------------------
Number of channels: 1
Sample width (bytes): 2
Frame rate (sample rate): 16000
Number of frames: 160000
Duration (seconds): 10.0
Figures Saved in lab01
```

…plus, on stderr, the three `FigureCanvasAgg is non-interactive` warnings. **You have succeeded when
`Figures Saved in lab01` is the last line of stdout and `lab01/figs/` holds 10 files** (5 PNG + 5 SVG).

> **This block is the TA's reference output, and it matches theirs field for field.** The supplemental
> PDF's screenshot shows `1` channel, sample width `2`, `16000` Hz, `160000` frames, `10.0` s — the same
> five values, transcribed in
> [`ta_supplement_lab1_reference.md`](ta_supplement_lab1_reference.md). Verified 2026-09-08.
>
> **The one line that differs is supposed to differ.** Theirs says `The basic frequency is 5.0 Hz.`,
> ours says `4.0 Hz.` That number comes from the per-student `myID` seed carried over from Lab 0 —
> ours is `6127` ([`../reference_docs/submission_requirements.md`](../reference_docs/submission_requirements.md#student-id)),
> theirs is theirs. **`4.0` is correct here and must not be "fixed" to match the screenshot**; a run
> that printed `5.0` on this machine would mean someone had overwritten our seed with the TA's
> ([KI-03](../reference_docs/known_issues.md#ki-03--myid-is-a-per-student-seed-and-must-be-set-every-lab)).
> Theirs also carries two lines ours does not — a `Generated WAV file at: …` from a WAV-generator
> script that is not in the handout and not in our package, and a first-run `Built simpleaudio==1.0.4`.
> Neither is expected here.

**Cut the music clip from the operator's source.** The source MP3 is **never modified** — it is opened
read-only and the clip written beside it. `--start 95` is not a default; it is the offset the clip on
disk was actually cut at, and omitting it produces a different clip:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 python tools/make_music_clip.py \
  "lab01/Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp3" \
  lab01/music_clip.wav --start 95
```

Ends with `spec   : OK -- mono, 16 kHz, ~10 s`, and `md5sum lab01/music_clip.wav` →
`e50f63f797773f6626c261dd90c21f72`. Verified 2026-09-08.

*(`tools/make_test_audio.py lab01/test_tone.wav` is a different tool for a different file — the
synthetic no-audio fallback, which no artifact uses. Do not run it expecting the music clip.)*

**The experimental set, from the music clip.** `--folder-name X` always writes to `X/figs`, so this
generates into a scratch folder and moves the files up — that is why there is no one-liner:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
T=$(mktemp -d)
mkdir -p lab01/figs_music
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio \
  --path-name lab01/music_clip.wav --folder-name "$T/a"
mv "$T"/a/figs/* lab01/figs_music/
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio \
  --path-name lab01/music_clip.wav --start-s 0.5 --end-s 1.5 --folder-name "$T/b"
for e in png svg; do
  mv "$T/b/figs/lab1_audio_fig2_waveform_zoom.$e" "lab01/figs_music/lab1_audio_prog_zoom_0.5_1.5.$e"
done
rm -rf "$T"
```

Twelve files land in `lab01/figs_music/`. **Re-run 2026-09-08: all six PNGs came back byte-for-byte
identical to the ones on disk** (the SVGs differ only in their embedded creation date, which matplotlib
stamps).

⚠ **Earlier versions of this block said `--path-name lab01/test_tone.wav` here. That was wrong** — the
figures on disk are from `music_clip.wav`, and running it with `test_tone.wav` silently produces a
*different* set of pictures under the same filenames. Checked by regenerating from both and comparing
md5s.

Verify:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 python tools/check_artifacts.py lab01/figs
uv run --project dsp26 python tools/check_artifacts.py lab01/figs_music
```

Each run prints a size-and-checksum table (10 rows for `figs`, 12 for `figs_music`) and **ends** with:

```
OK    artifacts present, non-trivial, and distinct
```

Both exit `0`. `tools/check_inputs.py` is a different tool and **exits `1` course-wide** for an
unrelated missing file (`py-pkg-1c-uv-qg.md`, tracked in
[`../README.md`](../README.md#open-across-the-course--py-pkg-1c-uv-qgmd--why-human-credentialed)); that is not a Lab 1 failure.

---

## Artifacts

`figs/` is gitignored (the `figs/` pattern in [`../.gitignore`](../.gitignore) line 58). **`figs_music/`
is not** — the pattern does not match it. Both regenerate with the commands above; nothing here is
precious.

**Two figure sets, and they are not interchangeable.** `figs/` is the handout's default input — **the
TA's supplied `.wav`, a steady 440 + 554.4 Hz dyad, not speech**; `figs_music/` is the experimental
task's music clip. The handout asks for the programming task's 0.5–1.5 s screenshot *"of your music
file"*, so that figure belongs to `figs_music/`.

⚠ **`figs/` was regenerated from the TA's file at 17:00 on 2026-09-08 and every description below is
of that run.** If a caption anywhere still describes silences, pauses or speech bursts, it is left over
from the superseded LibriSpeech decode — that audio is gone from `audio_files/` and no figure on disk
comes from it any more.

| # | File | Shows |
| --- | --- | --- |
| 1 | `figs/lab1_audio_fig1_waveform_full.png` | title `Waveform from 0.0s to 10.0s`, x-ticks `0.0` and `10.0` only. **A solid blue block filling ±1.0 for the whole 10 s** — no silences, no pauses, no envelope. That is what a constant full-scale dyad looks like at this zoom, and it is correct |
| 2 | `figs/lab1_audio_fig2_waveform_zoom.png` | title `Waveform from 0.4s to 1.4s`, the handout's zoom window. At 1 s across, the two tones resolve into a **regular beat pattern** — the 114.4 Hz difference between 440 and 554.4 Hz — with an unbroken dense band through the middle. Uniform across the window; there is nothing to "start in" |
| 3 | `figs/lab1_audio_fig3_spec_linear.png` | spectrogram, linear frequency axis. **Two bright bands crushed together just below 1000 Hz**, and blackness from ~1200 Hz to 8000 Hz — the linear axis spends 90 % of its height on empty spectrum |
| 4 | `figs/lab1_audio_fig4_spec_log.png` | spectrogram, log axis. The same two bands, now **spread open around 512 Hz and individually visible** — this is the figure that shows why the axis choice matters |
| 5 | `figs/lab1_audio_fig5_spec_mel.png` | spectrogram, mel axis. Bands sit low, below 512 Hz, with the near-linear low end giving them more room than the linear plot but less than the log one |

All five run flat left-to-right: **the signal does not change over the 10 s**, so every spectrogram is
horizontal stripes. A time-varying spectrogram here would mean the wrong file was loaded.
| E1 | `figs_music/lab1_audio_fig2_waveform_zoom.png` | experimental task, artifact 1 of 2: the zoomed waveform of the music clip |
| E2 | `figs_music/lab1_audio_fig5_spec_mel.png` | experimental task, artifact 2 of 2: the last (mel) spectrum of the music clip |
| P | `figs_music/lab1_audio_prog_zoom_0.5_1.5.png` | programming task: 0.5–1.5 s window of the music clip |
| — | `out/dsp26_help.txt`, `out/play_plot_audio_help.txt` | terminal output the handout wants screenshotted. Both begin with the Lab 0 `The basic frequency is 4.0 Hz.` line — expected, see *Reproduce* |
| — | `out/run_log.txt` | ⚠ **stale.** It is the `test_tone.wav` run from 12:03. **Its numbers are now identical to a correct run** — `test_tone.wav` is also 16 kHz mono, 160000 frames, 10.0 s — so the *only* thing that gives it away is the path it prints: `Detailed properties of lab01/test_tone.wav`. **Do not screenshot it for the report**; regenerating it is agent work, see *Open, and not human work* |
| — | `report.tex` / `report.pdf` | 5-page report, 3 figures embedded. ⚠ **`report.tex` no longer renders**, and the `report.pdf` on disk is the stale 12:07 build (`pdfinfo` → `Pages: 5`, `CreationDate: Sep 8 12:07:38 2026`) — see *Open, and not human work* below |
| — | `dsp26-lab01-nelson-gatlin.zip` | stripped code, 96 KB. Carries **7 `DEVIATION FROM HANDOUT` comment blocks** — 5 in the Lab 1 sources (`recipes.py` ×2, `audio_sig.py` ×3) and 2 inherited from Lab 0. They map to deviations 1–4 below; deviation 5 is prose-only and deviation 6 is not a code change at all |

All five PNGs in each set have distinct md5s and distinct byte sizes — the [KI-01](../reference_docs/known_issues.md#ki-01--repeated-pltfiguren-silently-overplots--figures-come-out-identical) overplot check.

---

## Open, and not human work

**Do not put this on the human's list. An agent finishes it.**

`tools/render_reports.sh lab01` fails as of 2026-09-08 12:24. Tracked as [KI-17](../reference_docs/known_issues.md#ki-17--a-report-can-reference-a-figure-that-moved-to-a-sibling-folder-render_reportssh-blames-the-wrong-thing) — **read that
first: its whole point is that the renderer's "regenerate `figs/`" hint is wrong here.**

```
lab01/report.tex                             FAIL
    error: report.tex:190: Unable to load picture or PDF file 'figs/lab1_audio_prog_zoom_0.5_1.5.png'
```

**Cause.** `figs/` was regenerated once a real default input arrived, and the music-derived figures
moved to `figs_music/`. `report.tex` still points the programming-task figure at `figs/`, and the
captions for `fig2` and `fig4` still describe the synthetic chord progression (*"four segments
separated at 2.5, 5.0 and 7.5 s"*) rather than what is plotted there now.

**Fix — two edits, both in `lab01/report.tex`:** repoint line 190 at
`figs_music/lab1_audio_prog_zoom_0.5_1.5.png`, and rewrite the `fig:zoom` (line 176) and `fig:speclog`
(line 185) captions — line 183 still says *"separated at 2.5, 5.0 and 7.5\,s"*, which describes the
synthetic chords. Then `tools/render_reports.sh lab01` must print `OK`. Left undone here only because
`report.tex` is being edited elsewhere in this session and two writers would collide.

> ⚠ **Whoever fixes those captions: `figs/` changed again at 17:00.** It is no longer speech either.
> The default input is now the TA's supplied `.wav` — a **constant 440 + 554.4 Hz dyad, 10.0 s**. Any
> caption describing silences, pauses, formants or speech bursts is as wrong as the chord-progression
> ones. The *Artifacts* table above describes what each of the five figures actually shows now.

**Second agent-side item: `lab01/out/run_log.txt` is stale.** It records a `test_tone.wav` run from
12:03. **Reading the numbers will not catch it** — `test_tone.wav` is also 16 kHz mono / 160000 frames
/ 10.0 s, so the stale log's header block is digit-for-digit what a correct run prints. Only the path
on the `Detailed properties of …` line differs. Regenerate it from the default input so the report
does not screenshot the stand-in:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name lab01 > lab01/out/run_log.txt
```

Correct when `grep -c test_tone lab01/out/run_log.txt` prints `0` and the file names
`2086-149220-0033.wav`.

---

**Submission deliverable:** `artifacts.pdf` — 5 pages, 8 of 9 required artifacts embedded. The
ninth (Audio Player window) is a placeholder until H3; drop the screenshot at
`lab01/figs_player/audio_player_window.png` and re-render.

## Deviations from the handout

| # | Change | Why |
| --- | --- | --- |
| 1 | `plot_audio_sig_in_td` and `plot_audio_sig_in_fd` **return** their `Figure`; the handout returns nothing | The only way to save headless. `plt.show()` is a no-op with no display ([KI-02](../reference_docs/known_issues.md)), so without a handle there is no artifact. |
| 2 | `play_audio` is **skipped when `MPLBACKEND=Agg`**; the handout calls it unconditionally | It opens a Tk window and blocks in `mainloop()` until a human closes it, so an unattended run hangs forever. Under a desktop with `MPLBACKEND` unset the behaviour is exactly the handout's. |
| 3 | `--folder-name` option added, writing the five figures to `<folder>/figs` | Not in the handout, which relies on a screenshot. Matches what Lab 0 already does. |
| 4 | Figures saved as **PNG and SVG** | The report needs PNG; SVG is the handout's choice elsewhere in the course. |
| 5 | `HANDOUT_ZOOM_S = (0.4, 1.4)` fallback when neither `--start-s` nor `--end-s` is given | ⚠ **Judgment call — please review.** See the note below. |
| 6 | ~~The experimental task's clip is synthetic~~ **RESOLVED 2026-09-08** | The operator supplied a real music source and `music_clip.wav` was cut from it (mono, 16 kHz, 10.00 s, spec-verified). No longer a deviation and no longer belongs in the Narrative. `test_tone.wav` is retained only as a no-audio fallback. |

**On deviation 5.** The programming task says to give the new options *"the same default values as those
defined in the `plot_audio_sig_in_td` function"* — that is `start_s=0.0, end_s=None`, which means
"the whole file". Taken literally and with no fallback, a no-argument run makes Figure 2 an exact
duplicate of Figure 1, and the handout's own Figure 2 (0.4–1.4 s) becomes unreachable without
arguments. The options are declared with the required defaults; the fallback only applies when
*neither* is supplied, so any explicit window is honoured and the default output still matches the
handout. Reverting is one `if` — say the word if the TA wants it literal.

Deviation 2 was found the hard way: the guard first tested `DISPLAY`, this machine has one
(`DISPLAY=:1`), and a batch run opened a window and waited for a click. Logged as
[KI-13](../reference_docs/known_issues.md).

---

## Handout questions

The handout asks for artifacts rather than prose answers, but two points are worth recording:

1. **Q:** What do the three frequency-axis formats show that the others do not?
   **A:** All three are the same STFT — `n_fft=512`, `win_length=400`, `hop_length=160` — differing
   only in how the axis is mapped. **Linear** spaces bins evenly, so the harmonics of a low note
   crowd into the bottom of the plot. **Log** spaces them by octave, which makes a harmonic stack
   evenly spaced and is why the vibrato is legible there. **Mel** warps to approximate human pitch
   perception: near-linear below ~1 kHz, logarithmic above.

2. **Q:** Why `sr=None` in `librosa.load`?
   **A:** Without it librosa resamples to its 22050 Hz default, and the sample rate printed by
   `print_wave_file_properties` (read from the WAV header) would disagree with the spectrogram axes.

At 16 kHz the handout's 400/160-sample settings are a 25 ms window advanced every 10 ms — the standard
speech framing, and it is why the same numbers suit both a 16 kHz music clip and the TA's tone pair.
**The default input makes point 1 unusually easy to see**: a constant 440 + 554.4 Hz dyad has nothing
but two lines to draw, so the three axes differ *only* in where those two lines land — crushed together
under 1 kHz on the linear axis, spread apart around 512 Hz on the log axis, low-but-legible on mel.
The music clip in `figs_music/` is the figure to point at for harmonic stacks and vibrato; the default
input has neither.

---

## Needs a human

Standard: [`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md).
Block shapes: [`../reference_docs/lab_template.md`](../reference_docs/lab_template.md) § *Needs a human*.

**Every row expands into a block below. Read the block before acting on the row.**

| # | Task | Why human | Blocks | Status |
| --- | --- | --- | --- | --- |
| H1 | ~~Fetch / confirm the default WAV~~ | Credentialed | — | ✅ **done 2026-09-08** — the TA's file is downloaded, installed and verified |
| H2 | ~~Supply the music clip~~ | Judgment | — | ✅ **done 2026-09-08** — source supplied, clip cut and verified |
| H3 | ~~Screenshots of the player and the 5 figure windows ~~ | Capture | the report's Artifacts section | ✅ **done 2026-09-08** — captured and embedded |
| H4 | ~~Live demo — **by the next lab section**, early checkout allowed ~~ | Policy | grading of the report | ✅ **done 2026-09-08 — TA signed off** |
| H5 | ~~Approve / finish the report ~~ | Judgment | H6 | ✅ **done** — `lab01-artifacts-nelson-gatlin.pdf`, 12/12 artifacts verified |
| H6 | Upload to Canvas — **due 1 week after the lab was assigned** | Credentialed | the grade | ⬜ |
| H7 | ~~Confirm what Lab 1 must submit~~ | Judgment | — | ✅ **answered by the handout itself** — § Submission: *"Submit a single PDF file containing all the artifacts."* One PDF, nothing else. The general course-wide ambiguity stays open for future labs |

**Two deadlines, not one, and they are different dates.** The TA's announcement separates them: the
**Canvas deliverable is due 1 week after the lab is assigned** (H6), and the **in-person demo is due by
the next lab section** (H4). Lab 1 started Sec 2 **9/4**, Sec 1 **9/8**, so for Sec 1 the upload is due
**9/15** and the demo by the **9/15** meeting; for Sec 2, upload **9/11** and demo by the **9/11**
meeting. Those coincide this time *because the sections meet weekly* — do not assume they always will.
Source: [`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md);
schedule from [`../README.md`](../README.md#schedule).

*(Not on this list: setting the ERAU ID. It is on file — `6127`,
[`../reference_docs/submission_requirements.md`](../reference_docs/submission_requirements.md#student-id) — the agent
sets it, and Lab 1 has no RNG seed of its own anyway.)*

---

### H1 · ~~Fetch / confirm the default WAV~~ — ✅ DONE 2026-09-08 · Why human was: **Credentialed**

> **Closed. Nothing to do here, and nothing waits on it.** The TA posted the file to Canvas along with
> the announcement *"Lab 1 and Future Labs"*; you downloaded it on 2026-09-08 and it is installed at
> `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files/2086-149220-0033.wav`.
> All five figures in `lab01/figs/` were regenerated from it, and the printed header block matches the
> TA's own screenshot field for field. The block below is kept as the record of how this went wrong
> first, because the way it went wrong is the useful part.

**What happened, in order.**

| When | What | Outcome |
| --- | --- | --- |
| 2026-09-08 morning | Handout named the file once, in code, with no source. Machine searched (`find /home/devel -iname '*2086*'`) → nothing | Correctly identified as a missing input |
| " | Filename parsed as a **LibriSpeech utterance id** (speaker 2086 / chapter 149220 / utterance 0033); the corpus original was fetched from openslr.org and decoded to WAV | **Plausible, and wrong.** 7.435 s of read speech |
| " | You checked Canvas and reported no `.wav` on the Lab 1 page | Correct *at that moment* |
| 2026-09-08 evening | TA posted the announcement **and the `.wav`**, plus a supplemental PDF | The real file arrived |
| " | Downloaded, installed, `figs/` regenerated, output compared against the TA's screenshot | ✅ settled |

**The two files are not the same audio.** 10.00 s / 320,044 bytes / a synthetic 440 + 554.4 Hz dyad
versus 7.43 s / 237,964 bytes / read speech; the samples differ. Full comparison and the commands that
established it: *Provenance of `2086-149220-0033.wav`* above.

**Where it came from, for the record** — worth having, because this is the first Canvas location this
repo can name concretely:

| | |
| --- | --- |
| Announcement | Canvas → the CESC 410/510 course site → **Announcements** → *"Lab 1 and Future Labs"*, by **Ryle** |
| The `.wav`, the supplemental PDF and the reference `app_cli.py` | uploaded alongside it. Going forward the TA has said the **Lab PDF is posted in the Modules tab under each lab's page** |
| Saved here | [`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md), [`ta_supplement_lab1_reference.md`](ta_supplement_lab1_reference.md), [`ta_supplied_2086-149220-0033.wav`](ta_supplied_2086-149220-0033.wav), [`ta_reference_app_cli.py`](ta_reference_app_cli.py) |

**IF THE TA REPLACES THE FILE.** They said future labs get a supplemental doc each time, so a re-upload
is realistic. Do not overwrite blind — download to a scratch path and compare:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/2086-149220-0033.wav` *(wherever the browser put it)* | `/tmp/canvas-2086.wav` — **a scratch path, not `audio_files/`** |

```sh
md5sum /tmp/canvas-2086.wav
```

`b8c6e2fc5147d4c627efa0f443c82102` → same file, delete the download, nothing to do. Anything else →
replace both copies and regenerate, then re-check the header:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
cp /tmp/canvas-2086.wav dsp26/audio_files/2086-149220-0033.wav
cp /tmp/canvas-2086.wav lab01/ta_supplied_2086-149220-0033.wav
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name lab01
```

Then say so here — the *Artifacts* table's descriptions of figures 1–5 are written against the current
audio and would need rewriting too.

**VERIFY (30 seconds, any time).**

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
md5sum dsp26/audio_files/2086-149220-0033.wav
uv run --project dsp26 python -c "import wave,sys; w=wave.open(sys.argv[1]); print(f'{w.getnchannels()} ch  {w.getframerate()} Hz  {w.getnframes()} frames  {w.getnframes()/w.getframerate():.2f} s')" dsp26/audio_files/2086-149220-0033.wav
```

Expected, exactly:

```
b8c6e2fc5147d4c627efa0f443c82102  dsp26/audio_files/2086-149220-0033.wav
1 ch  16000 Hz  160000 frames  10.00 s
```

⚠ **The second line alone is not enough.** `test_tone.wav` and `music_clip.wav` print the same thing —
see the md5 table under *Inputs*. **The md5 is the check.**

**IF SOMETHING IS OFF.** Ryle is now reachable outside the meeting: **Discord `ryletraub_30890`**, or
Canvas **Inbox** on the course site. (*The announcement invites email but does not give an address —
do not guess one.*) Failing that, Dr. Liu — `jianhua.liu@erau.edu` and `liu620@erau.edu`, copy both;
office LB 349, MWF 1:30–3:50 pm, or Zoom by appointment
([`../../hw/reference_docs/submission.md`](../../hw/reference_docs/submission.md) § *Who to ask, and when*).

**BLOCKS.** **Nothing.** The input is present, verified, and every figure is regenerated from it.

---

### H2 · ~~Supply the music clip~~ — ✅ DONE 2026-09-08 · Why human was: **Judgment**

> **Closed. Nothing to do here.** The operator supplied
> `Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster).mp3` on 2026-09-08.
> `music_clip.wav` was cut from it — **mono, 16000 Hz, 10.00 s**, matching the handout spec, with the
> source left byte-for-byte unmodified. All three experimental/programming figures are regenerated
> from it. The block below is kept as the record of how the clip was chosen and how to re-cut it.

**Choosing the music is yours; shaping the file is not.** Give any readable audio file and an agent
produces the exact spec — do **not** spend your time on sample rates
([KI-16](../reference_docs/known_issues.md), *No ffmpeg on this machine*).

**Already tried — do not repeat.** `find /home/devel -iname '*.wav'` finds only library test assets
(`simpleaudio`, `pygame`, `scipy`) and an STM32 demo clip — nothing usable as "your music". A
synthetic stand-in was built instead (`lab01/test_tone.wav`, a four-chord progression) so the code
could be exercised; it is **not** a submission, and using it is deviation 6 above.

**The exact spec, from the handout** (§ *Experimental task*, 20 pts):

| Property | Required value |
| --- | --- |
| Channels | 1 (mono) |
| Sample rate | 16 kHz (16000) |
| Duration | approximately 10 s |
| Format | WAV |

**WHERE — what counts as a good source.** Anything you can legally play and that reads on this
machine. In order of least effort:

1. **A music file you already own** — `.mp3`, `.flac`, `.ogg`, `.wav`, `.aiff` all read directly
   (libsndfile 1.2.2 in the `dsp26` venv). Put it anywhere; `/home/devel/Downloads/` is fine.
2. **A free-licence download** — the Free Music Archive, ccMixter, or Wikimedia Commons audio. Pick
   something with a clear melody and a few instruments; a spectrogram of solo spoken word or a beat
   with no pitch content makes a dull Figure 5.
3. **Record 10 s through the microphone** — mic verified present (`arecord -l` → `card 1: PCH [HDA
   Intel PCH]`). Needs no conversion at all; it writes the spec directly:

```sh
arecord -f S16_LE -r 16000 -c 1 -d 10 /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/music_clip.wav
```

4. **Record 10 s of whatever this machine is playing — including a YouTube tab — with no microphone
   and no `ffmpeg`.** This is the route to use if you want the handout's own suggested source.
   PulseAudio exposes the speaker output as a capture device
   (`pactl list short sources` → `alsa_output.pci-0000_00_1f.3.analog-stereo.monitor`), and
   `parecord` records from it. **Start the music playing first, then run this**; it captures ~12 s
   and the next command trims it to exactly 10 s:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
timeout 14 parecord --device=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor \
  --rate=16000 --channels=1 --format=s16le --file-format=wav /tmp/raw_capture.wav
```

   `timeout` ends it — that is not an error, and `parecord` still writes a valid header. Verified on
   this machine: a `timeout 14` capture yields 12.07 s. Then run the conversion in **WHAT** below with
   `/tmp/raw_capture.wav` as the source. If the result is silent, the browser tab was muted or paused.

⚠ **`yt-dlp` alone will not get you there.** It is installed (2026.06.09) but its `-x` audio
extraction needs `ffmpeg`, and **`ffmpeg` is not on this machine** (`command -v ffmpeg` prints
nothing; installing it needs root — [KI-16](../reference_docs/known_issues.md)). Nor is there a `-f`
that rescues it: YouTube's audio-only streams are `m4a`/AAC or `webm`/Opus, and this venv's
libsndfile 1.2.2 reads **none** of those. Its full list, checked with `soundfile.available_formats()`,
is AIFF, AU, AVR, CAF, **FLAC**, HTK, IRCAM, MAT4, MAT5, **MP3**, MPC2K, NIST, **OGG**, PAF, PVF, RAW,
RF64, SD2, SDS, SVX, VOC, W64, **WAV**, WAVEX, WVE, XI — and there is no `audioread` fallback
installed. **So: use route 1, 3 or 4. Do not spend time on `yt-dlp` flags.**

**WHAT.** Hand over the raw file — any format, any length, any rate. The conversion is one command,
already verified on a stereo 44.1 kHz MP3, a stereo 32 kHz WAV, and a `parecord` monitor capture.
**Edit only the first line**, then paste the rest unchanged:

```sh
SRC=/home/devel/Downloads/my-song.mp3          # <-- put YOUR file's real path here
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 python -c "
import librosa, soundfile as sf, sys
y, sr = librosa.load(sys.argv[1], sr=16000, mono=True, offset=0.0, duration=10.0)
sf.write(sys.argv[2], y, sr, subtype='PCM_16')
print(f'wrote {sys.argv[2]}  mono  {sr} Hz  {len(y)/sr:.1f} s')
" "$SRC" lab01/music_clip.wav
```

```
wrote lab01/music_clip.wav  mono  16000 Hz  10.0 s
```

`offset=` picks which 10 seconds — raise it to skip an intro. `duration=` sets the length.

> The `SRC=` line exists because a literal `<your file>` placeholder is a **redirect** in bash and
> fails with a confusing `No such file or directory`. Set the variable; do not paste angle brackets.

| Source (FROM) | Destination (TO) |
| --- | --- |
| Your file — e.g. `/home/devel/Downloads/my-song.mp3`, or `/tmp/raw_capture.wav` from route 4 *(any format in the libsndfile list above)* | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/music_clip.wav` |

**VERIFY — do this *before* running the lab.** Two checks; the first needs nothing installed:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
python3 -c "
import sys, wave
p = sys.argv[1]
with wave.open(p) as w:
    ch, sr, n = w.getnchannels(), w.getframerate(), w.getnframes()
print(f'{p}: channels={ch} rate={sr} duration={n/sr:.2f}s')
print('SPEC OK' if (ch == 1 and sr == 16000 and 8 <= n/sr <= 12) else 'SPEC FAIL')
" lab01/music_clip.wav
```

Expected:

```
lab01/music_clip.wav: channels=1 rate=16000 duration=10.00s
SPEC OK
```

A file that is still stereo/44.1 kHz prints, for example,
`channels=2 rate=44100 duration=3.50s` and `SPEC FAIL` — rerun the conversion, do not proceed.

The second is the lab's own reader, which prints the same header fields the handout asks you to
identify (it is also the fastest end-to-end smoke test):

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --path-name lab01/music_clip.wav
```

Expected tail (the first stdout line is still Lab 0's `The basic frequency is 4.0 Hz.` — see
*Reproduce*):

```
Number of channels: 1
Sample width (bytes): 2
Frame rate (sample rate): 16000
Number of frames: 160000
Duration (seconds): 10.0
```

**Then stop — you are done, and the figures are not yet rebuilt.** This smoke test has no
`--folder-name`, so it saves nothing; `lab01/figs_music/` still holds the `test_tone.wav` set. Say the
clip has landed and an agent reruns the *Reproduce* experimental block with
`--path-name lab01/music_clip.wav`, regenerates E1/E2/P, and drops deviation 6 from the report. If you
want to do it yourself, it is that one block with the filename swapped.

**IF THE SPEC CHECK FAILS.** `SPEC FAIL` with `channels=2` or `rate=44100` means the conversion did
not run — you copied the file instead. Rerun **WHAT**. `SPEC FAIL` with a duration under 8 s means the
source was shorter than `offset + 10 s`; lower `offset=0.0` or pick a longer file. A
`FileNotFoundError` naming `lab01/music_clip.wav` means the conversion never wrote it — check `$SRC`.

**IF YOU CANNOT GET ONE.** Say so and the stand-in ships:
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/test_tone.wav` is on disk (not
yet committed — `lab01/` is still untracked, and git is human-only here), mono / 16 kHz / 10.0 s,
deliberately *music-shaped* (four chords, six harmonics per note, per-note decay,
slight vibrato), and every figure in `figs_music/` was generated from it. **This is a graded deviation**
— it is already written up as deviation 6 above and must stay in the report's Narrative. It costs
credibility on a 20-point task whose whole point is real audio, so it is a last resort, not a plan.

**BLOCKS.** The two experimental-task figures (E1, E2) and the programming task's 0.5–1.5 s figure (P)
being *your music*. It does **not** block the package code, the five `figs/` figures, `dsp26 --help`,
the zip, or H1/H4/H7.

---

### H3 · Screenshots of the player and the 5 figure windows · Why human: **Capture**

Only the *capture* is human. **Generating the figures is not** — `MPLBACKEND=Agg` saves every one
headlessly ([KI-02](../reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless)) and they
are already in `lab01/figs/` and `lab01/figs_music/`.

**WHERE.** A desktop session with a display. **This machine has one** — `DISPLAY=:1`, 1920×1080, X11
(`xdpyinfo` confirms). You do not need a laptop.

**WHAT.** Three runs, and the environment matters more than anything else on this page.

**Step 0 — check the environment first. `MPLBACKEND` must be unset or nothing opens:**

```sh
echo "MPLBACKEND=[$MPLBACKEND]"     # must print MPLBACKEND=[]
echo "DISPLAY=[$DISPLAY]"           # must print DISPLAY=[:1]
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
```

If `MPLBACKEND` prints `[Agg]`, run `unset MPLBACKEND` in that shell. **Every command in this block is
run *without* the `MPLBACKEND=Agg` prefix used everywhere else in this README** — that prefix is
exactly what suppresses the player and the windows.

**Step 1 — `dsp26 --help`, one screenshot of the terminal:**

```sh
uv run --project dsp26 dsp26 --help
```

**Step 2 — the player and the five figures, from the handout's default input:**

```sh
uv run --project dsp26 dsp26 play-plot-audio
```

The terminal first prints `Loading: .../2086-149220-0033.wav` and `Duration: 10.00 seconds`, then
**six windows appear one at a time, and each must be closed to reveal the next.** What to expect, in
order:

| Order | Window | How to recognise it |
| --- | --- | --- |
| 1 | **Audio Player** | Tk window, title bar `Audio Player`, 500×300. See the element-by-element table below — **this one is confirmed against the TA's own screenshot.** |
| 2 | Figure 1 — waveform, whole file | Title `Waveform from 0.0s to 10.0s`. Only two x-tick labels, `0.0` and `10.0`. **A solid blue block filling ±1.0 edge to edge** — no gaps, no envelope. That is correct; the default input is a constant tone pair, not speech. |
| 3 | Figure 2 — waveform, zoomed | Title `Waveform from 0.4s to 1.4s`. X-ticks `0.4` and `1.4` only. A regular beat pattern across the full second — evenly spaced peaks, no quiet stretch anywhere. |
| 4 | Figure 3 — spectrogram, **linear** | Title `Spectrogram of an Audio Signal`, y-label `Hz`. **Y-ticks evenly spaced: 0, 1000, 2000 … 8000.** Two bright bands squeezed together just under 1000 Hz; everything above is black. |
| 5 | Figure 4 — spectrogram, **log** | Same title and y-label. **Y-ticks double: 0, 64, 128, 256, 512, 1024, 2048, 4096** — eight labels, crowded near the bottom. The two bands are widest apart here. |
| 6 | Figure 5 — spectrogram, **mel** | Same title and y-label. **Y-ticks 0, 512, 1024, 2048, 4096** — five labels, wide gap between 0 and 512. Bands sit below the 512 tick. |

⚠ **Figures 3, 4 and 5 all carry the identical title `Spectrogram of an Audio Signal`.** The **y-axis
tick labels in the table above are the only reliable way to tell them apart** — name your screenshots
as you take them, in the order they appear, or you will not be able to sort them afterwards. With this
input they are *also* three very similar-looking pictures of two flat stripes, which makes the tick
labels the only difference visible at a glance.

**The Audio Player window, element by element.** The TA's supplemental PDF contains a screenshot of
this exact window, so for once there is no guessing about what you are capturing. Ours is the same Tk
code and lays out identically (`audio_player.py` lines 186–232 — `geometry("500x300")`, two `pack`ed
labels, then a 3-column button grid with `Exit` at row 1, column 1):

| Where | Exact text | Note |
| --- | --- | --- |
| Title bar | `Audio Player` | plus the window-manager's own minimise/maximise/close buttons |
| First label | `Playing: 2086-149220-0033.wav` | filename only, never a path |
| Second label | `Duration: 10.00 seconds` | **two decimals** — this is the player's own print, `f"{duration:.2f}"`, not the `10.0` the properties block shows |
| Buttons, row 1 | **Play** · **Pause** · **Resume** | three across, left to right |
| Button, row 2 | **Exit** | centred, directly under **Pause** |

⚠ **Take the screenshot before the clip finishes, or press nothing at all.** When playback reaches the
end, `audio_player.py` relabels the first button from **Play** to **Replay** (lines 116 and 124). A
shot showing `Replay` is still a valid screenshot of a working player, but it no longer matches the
TA's reference. Ten seconds is not much time — the safe order is: **capture first, then click Play.**

⚠ **The TA's screenshot is theirs, and cannot be submitted as ours.** It lives inside
[`ta_supplement_lab1_reference.pdf`](ta_supplement_lab1_reference.pdf); its window shows the TA's
Windows title bar and its terminal half shows `C:\Users\rylet\…` paths and `The basic frequency is
5.0 Hz.` (their seed, not ours). Use it as the target to compare against — never as an artifact. For
the same reason it has deliberately **not** been extracted into `figs_player/`, which is where our own
capture goes.

**Step 3 — the experimental task's two figures, from your music clip** (already generated;
`lab01/test_tone.wav` is available to rehearse the click-through, but is **not** what you capture):

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 dsp26 play-plot-audio --path-name lab01/music_clip.wav
```

**Each of the two Step-3 runs replays the whole sequence** — player, then five figures, six windows to
close, exactly as in the table above. The player now says `Playing: music_clip.wav`, and **the figures
are the ones that look different**: the music clip has real harmonic structure and a visible envelope
where the default input is flat. Both files are 10.0 s, so **the titles are identical between Step 2
and Step 3** (`Waveform from 0.0s to 10.0s` either way) — the title is not how you tell these
screenshots apart; the player's filename label and the picture itself are.
Screenshot **Figure 2** (the zoomed waveform) and **Figure 5** (the mel spectrum) — those are the two
the handout names; close the rest. Then the programming task's figure:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 dsp26 play-plot-audio --path-name lab01/music_clip.wav --start-s 0.5 --end-s 1.5
```

and screenshot **Figure 2**, which is now titled `Waveform from 0.5s to 1.5s`.

**Capturing.** No screenshot GUI is installed; ImageMagick's `import` is (6.9.11-60):

```sh
mkdir -p /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots
import        /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots/01_player.png
import -window root /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots/00_help.png
```

`import` with no `-window` turns the cursor into a crosshair and captures **the window you click** —
use it for each figure. `import -window root` grabs the whole screen immediately — use it for the
terminal. Avoid dark terminal themes; reports get printed
([`../reference_docs/report_guide.md`](../reference_docs/report_guide.md#3-artifacts--code-snippets-and-screenshots)).

**VERIFY.**

```sh
ls -l /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots/
file  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots/*.png
```

Expected: `PNG image data, 1920 x 1080` (or the window's own size) and **not** `1-bit grayscale` —
that is what an empty desktop captures as, and it means the shot was taken before the window drew.
Count them: 1 help + 1 player + 5 figures + 2 experimental + 1 programming = **10**.

**Then put the player shot where the report expects it.** `artifacts.tex` embeds a placeholder for it
at a fixed path, so this move is part of the task, not a tidy-up:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/shots/01_player.png` | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/figs_player/audio_player_window.png` |

`figs_player/` already exists and is empty — verified 2026-09-08. Compare your shot against the
element table above (and, if you want, against the TA's screenshot in the supplemental PDF) before
moving it: `Playing:` must read `2086-149220-0033.wav`, and `Duration:` must read `10.00 seconds`.

**IF IT DOES NOT WORK.** `FileNotFoundError: File not found: lab01/music_clip.wav` → re-cut it with
`tools/make_music_clip.py … --start 95` (exact command under *Reproduce*); rehearsing with
`--path-name lab01/test_tone.wav` is fine, but **never screenshot a `test_tone.wav` run as the
experimental task** — it is the synthetic fallback, and using it is a deviation that must be disclosed. No window appears → `MPLBACKEND` is
still set; recheck step 0. A run that prints nothing **and never exits** is a blocked GUI window, not
slow maths —
[KI-13](../reference_docs/known_issues.md). No sound from the player but the window is fine → the
figures still work; note it and move on, the handout only asks for a screenshot of the player, not
proof of audio.

**BLOCKS.** The report's **Artifacts** section only — one placeholder in `artifacts.tex` stays a
placeholder until the player shot lands. Code, figures, packaging, H4 and H6 do not wait on it.

---

### H4 · Demo Lab 1 to Ryle, in person, by the next lab section · Why human: **Policy**

Course policy: the student shows their own working code to the TA. Nothing about it is automatable.

**The deadline is now stated, not inferred.** From the TA's announcement, quoted in full at
[`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md):

| Rule | Wording | What it means here |
| --- | --- | --- |
| **In-Person Demos** | *"You must demo your completed lab to me by the next lab section."* | Lab 1 started Sec 1 **9/8** / Sec 2 **9/4**, so the demo is due at the **9/15** (Sec 1) or **9/11** (Sec 2) meeting |
| **Early Checkouts** | *"If you complete your lab before class, you are welcome to show up, demo it to me, and leave early."* | **You do not have to sit the session.** Lab 1 is finished apart from H3 and H5 — showing up, demoing and leaving is explicitly sanctioned |
| **Extra Support** | *"If you need supplemental instruction or extra help, you are welcome to show up and attend the other lab section as well."* | The **other section's** meeting is a second slot for both help and, in practice, catching Ryle |

**This supersedes the old note that the demo happens "at the **start** of the meeting."** That came
from the course info's general wording; the TA's own rule is *by the next lab section*, and early
checkout is offered. Arriving early is still the sensible play — it is what makes leaving early
possible.

**WHO.** **Ryle**, the lab TA. Outside the meeting: Discord `ryletraub_30890`, or Canvas **Inbox**.
The announcement invites email but gives no address, so do not guess one.

**WHERE.** LB 373. **Sec 1 Tue, Sec 2 Fri, 5:15–8:15 pm** — [`../README.md`](../README.md#schedule)
§ *Schedule* for the full calendar.

**WHAT.** Have it running before you walk in:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 dsp26 --help
uv run --project dsp26 dsp26 play-plot-audio          # no MPLBACKEND -- let the windows open
```

**VERIFY.** Both run clean on this machine *before* the meeting, and `dsp26 --help` lists
`play-plot-audio`. Rehearse the click-through — six windows, each closed in turn (see H3). If you
intend to check out early, have the answer to *"show me the start/end options"* ready too: that is the
graded programming task, and it is the one thing in this lab the TA's reference `app_cli.py` does not
contain.

**IF YOU CANNOT ATTEND.** Two routes, in order:

1. **The other section's meeting.** The TA explicitly invites students to attend the other section —
   Sec 1 Tue / Sec 2 Fri, same room and time. This costs nothing and is not a make-up request.
2. **A video demo before the meeting.** **Two are allowed all semester** — spend them deliberately,
   and only after route 1 is genuinely impossible.

**BLOCKS.** Grading of the report. The report can still be written and **uploaded** first — the Canvas
deadline (H6) and this one are separate rules with separate dates; it just is not read until Ryle has
seen the demo.

---

### H5 · Approve / finish the report · Why human: **Judgment**

The agent drafts it. The **Narrative** is graded on the debugging story, and only you can say which
parts are yours.

**WHERE.** `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/report.tex`

**WHAT.** Read all four sections against
[`../reference_docs/report_guide.md`](../reference_docs/report_guide.md). Confirm the Narrative matches
what actually happened, including **every row** of *Deviations from the handout* above — deviation 5
is an open judgment call you may want to revert, and deviation 6 (synthetic music) must be disclosed
unless H2 lands first. Then rebuild:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
tools/render_reports.sh lab01
```

Expected: `lab01/report.tex   OK  -> lab01/report.pdf` then `All rendered. PDFs kept (gitignored).`

**VERIFY.** The PDF opens, every figure it references exists, and no line in the `.tex` names a script,
a flag or a repo path ([KI-09](../reference_docs/known_issues.md) — packaging refuses to build if one
survives).

**IF IT FAILS TO RENDER.** As of 2026-09-08 it **does** fail, with
`Unable to load picture or PDF file 'figs/lab1_audio_prog_zoom_0.5_1.5.png'`. **That is a known
agent-side defect, not yours** — [KI-17](../reference_docs/known_issues.md#ki-17--a-report-can-reference-a-figure-that-moved-to-a-sibling-folder-render_reportssh-blames-the-wrong-thing), and *Open, and not human work* above. The
renderer's own advice (*"Missing figures? figs/ is gitignored -- generate them first"*) **is wrong for
this one error**: the file exists, in `figs_music/`. If it is still failing when you get here, say so
rather than editing `.tex` paths by hand. A plain `Unable to load picture` for any
*other* figure just means `figs/` is empty (it is gitignored); regenerate:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name lab01
```

**BLOCKS.** H6. Nothing else.

---

### H6 · Upload to Canvas — due 1 week after Lab 1 was assigned · Why human: **Credentialed**

**WHEN — now a stated rule, not an inference.** The TA's announcement
([`ta_announcement_lab1_and_future_labs.md`](ta_announcement_lab1_and_future_labs.md)):
*"Lab write-ups/deliverables are due on Canvas **1 week** after they are assigned."*

| Section | Lab 1 assigned | Canvas deliverable due |
| --- | --- | --- |
| Sec 1 (Tue) | 9/8 | **9/15** |
| Sec 2 (Fri) | 9/4 | **9/11** |

Dates from [`../README.md`](../README.md#schedule) § *Schedule*. **This is a different rule from the
demo deadline in H4**, even though for Lab 1 the two dates land on the same day. Do not merge them in
your head; a lab that spans a no-lab week will separate them.

**WHERE.** ERAU Canvas → **the `CESC 510` course site** (the site the lab handouts are posted on — see
H1 for why it is probably not called "CESC 410L", and why nobody here can be certain) → the **Lab 1**
assignment. Check **Modules** and **Assignments**; a separate CESC 410/410L site, if your roster has
one, is the second place to look.

> The TA has said that from now on *"I will copy over and post the Lab PDF directly inside the
> **Modules** tab under the respective lab pages"* — so **Modules** is the tab to open first, and each
> lab has its own page there. That is also where the Lab 1 `.wav`, the supplemental PDF and the
> reference `app_cli.py` came from.

**WHAT.** Build the package first, then upload exactly what it printed:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
tools/render_reports.sh lab01                             # -> lab01/report.pdf   <- always needed
# tools/make_submission.sh lab01 nelson-gatlin            # NOT NEEDED for Lab 1 -- the handout
#                                                        # wants one PDF, not a code zip. Kept
#                                                        # commented because a later lab may ask.
```

**You do not need `--figures` for Lab 1.** That mode packages *report + figures and no code*, writing
`lab01/lab01-figures-nelson-gatlin.zip` — a file the upload table below never asks for. It is Lab 0's
shape. Run it only if H7 comes back saying Lab 1 wants figures rather than code. Either way it calls
`tools/render_reports.sh` first and **exits 1 with `error: report failed to render -- fix it before
packaging`** while the failure in *Open, and not human work* stands — verified 2026-09-08. So does
`render_reports.sh` on its own. **Both must print `OK` before you upload anything.**

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/lab01/report.pdf` | the Canvas **Lab 1** assignment upload box — the handout asks for **a single PDF containing all the artifacts** |
| ~~`.../lab01/dsp26-lab01-nelson-gatlin.zip`~~ | ❌ **DO NOT UPLOAD.** H7 is answered: the handout wants one PDF. The code is already in it as the Programming task's *Code Snippet*. The zip is 93% `uv.lock` and 1.8% Lab 0 code |

**VERIFY.** `make_submission.sh` prints its file list — **read it before uploading.** No `.venv`, no
`tools/`, no `__pycache__`. Then reopen the Canvas submission and confirm the attachment names match,
and that the timestamp is **before the 1-week deadline in the table above** — not merely before the
next meeting.

**IF THE ASSIGNMENT IS NOT THERE.** In order, and **the same day** — the next meeting is already too
late:

1. Check **Modules** first — the TA posts each lab's material on that lab's page — then
   **Announcements** and **Assignments** on the CESC 510 site. A late-posted assignment usually shows
   up as an announcement first.
2. Check any separate CESC 410 / 410L site on your roster.
3. **Message Ryle.** Discord **`ryletraub_30890`**, or Canvas **Inbox** on the course site. The
   announcement invites email but never gives an address — **do not invent one.** This is a change
   from earlier versions of this file, which said no TA contact existed.
4. Ask a classmate. One line, answered in minutes.
5. **Email Dr. Liu — `jianhua.liu@erau.edu` and `liu620@erau.edu`, copy both** — if Ryle has not
   replied and the deadline is close.

**BLOCKS.** The grade. **Late is a zero. No resubmission.**

---

### H7 · Confirm what Lab 1 must submit · Why human: **Judgment**

The course info and the handout disagree, and only a TA can settle it —
[`../reference_docs/submission_requirements.md`](../reference_docs/submission_requirements.md).

**WHERE.** **Ryle**, the lab TA. Three routes, and — unlike every earlier version of this block — the
meeting is no longer the only one:

| Route | Address | When to use it |
| --- | --- | --- |
| In person | LB 373, at the lab meeting — the same slot as H4 | Best. Costs no extra trip, and you are demoing anyway |
| Discord | **`ryletraub_30890`** | The TA's own first suggestion for questions between meetings |
| Canvas **Inbox** | on the CESC 510 course site | If you would rather keep it on the course record |

⚠ **The announcement says "email me" but does not give an address. Do not construct one** from the
Discord handle or from an ERAU pattern — a bounced or misdirected email is worse than a Discord
message that lands. If a question genuinely needs email, ask Ryle at the meeting for the address and
record it in [`../README.md`](../README.md#course-facts-that-drive-the-workflow) § *Course facts*.

The other lab section's meeting is also open to you — the TA invites students to attend either — so a
missed Tuesday can be asked on Friday. Failing all of that, Dr. Liu: `jianhua.liu@erau.edu` and
`liu620@erau.edu`, copy both.

**WHAT.** The handout says *"Submit a single PDF file containing all the artifacts"* and says nothing
about a code zip, while the course info says report + code generally. Ask which, and in what form
(zip of the package, individual `.py`, or code pasted into the report). Then fill in Lab 1's row in
the *Per-lab requirements* table in
[`../reference_docs/submission_requirements.md`](../reference_docs/submission_requirements.md#per-lab-requirements)
and set *Confirmed with TA?* to ✅.

**VERIFY.** The row is filled in and marked confirmed, with the TA's wording quoted.

**No longer applies to Lab 1.** That fallback existed while it was unknown what this lab wanted. The handout answers it directly — *"Submit a single PDF file containing all the artifacts"* — so submit **only** `lab01-artifacts-nelson-gatlin.pdf`. Sending the code zip as well is not a safe hedge here: it is 93% `uv.lock` and 1.8% Lab 0 code, none of which the handout asked for.
Over-submitting has no stated penalty; under-submitting is a zero with no resubmission.

**BLOCKS.** Which files H6 uploads. Nothing before that.

---

**BLOCKED / NOT BLOCKED.** The code is written, runs clean against **the TA's own default input**, and
all five `figs/` figures plus the experimental set in `figs_music/` are generated and checked against
the TA's published output. **Nothing is blocked by a missing download — H1 and H2 are both closed.**
What is left for you is H3 (screenshots), H4 (the demo), H5 (approve the report), H6 (upload) and H7
(confirm what to submit). The report build failure is an agent's job, not yours (*Open, and not human
work*, above).

---

## Notes

- `simpleaudio` compiled from source without extra system packages, so no ALSA headers were needed.
- The synthetic stand-in is deliberately *music-shaped* — a four-chord progression with six harmonics
  per note, per-note decay envelopes and slight vibrato. A pure sine would give a spectrogram with one
  flat line, which would hide exactly the bugs the spectral figures exist to expose. The chord
  boundaries at 2.5 / 5.0 / 7.5 s are visible in `figs_music/` figures 3–5 and are a quick correctness
  check.
- To hear the file and see the player, drop `MPLBACKEND=Agg`. Full click-through in **H3**.
- The default input is **not** speech, despite a filename that says it should be. It is the TA's
  synthetic 440 + 554.4 Hz dyad, so `figs/` is flat and featureless where `figs_music/` has real
  harmonic structure. Both are correct; they are different signals. The provenance section above
  has the measurement and the one-liner that reproduces it.
- Packaging caught a real defect on the first run: a docstring that *mentioned* the deviation marker
  looked like a lost disclosure once docstrings were stripped. Logged as
  [KI-14](../reference_docs/known_issues.md). Run `make_submission.sh` as soon as code works, not at
  submission time.
- Lab 0 was re-run after these changes and still produces its four figures unchanged.
- The lesson from this README's first version — a human task that names no place costs a round trip —
  is logged as [KI-15](../reference_docs/known_issues.md) and is now repo doctrine in
  [`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md).
- The lesson from its **second** version — a filename that parses as a public-dataset id is a
  hypothesis, not provenance, and a checker that only looks at *links* will never catch a file whose
  *contents* are wrong — is logged as
  [KI-19](../reference_docs/known_issues.md#ki-19--a-filename-that-parses-as-a-public-dataset-id-is-not-proof-of-provenance).
- **Read the TA's announcements.** Four things this file used to carry as open questions were answered
  in one Canvas post: the `.wav`, the TA's name and contact, the submission deadline and the demo
  deadline. The TA has said a supplemental reference document will follow **every** future lab —
  checking Announcements before starting a lab is now part of the routine, not an afterthought.
