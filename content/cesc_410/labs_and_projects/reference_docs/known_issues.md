# Known issues

**Check here before debugging.** Traps that have already cost time, and things in the handouts that are wrong.

Add an entry when something takes more than ~15 minutes to work out, or when handout code does not do what it says.

---

## KI-01 · Repeated `plt.figure(N)` silently overplots — figures come out identical

**Seen in:** Lab 0, `sinusoids.py` · **Status:** fixed, deviation marked in source

**Symptom.** Four figures saved, but two were the same image. `lab0_sinusoids_fig1.svg` and `fig2.svg` both came out at exactly 95410 bytes.

**Cause.** `plot_one_sinusoid_td_fd()` opens its figure with `plt.figure(1)` and the recipe calls it twice. **pyplot returns the *existing* Figure for a repeated number** — so `fig1 is fig2` is `True`, the second call draws on top of the first (4 lines on the axes instead of 2), and both `savefig` calls write the same overplotted figure.

**Why it looks fine in class.** Interactively, `plt.show()` *blocks*, and closing the window destroys figure 1 — so the next `plt.figure(1)` gets a fresh one. The bug only appears when saving to file, because headless `plt.show()` is a no-op and nothing is ever closed. **The broken path is the one the handout recommends for submission.**

**Fix.** Bare `plt.figure()` auto-numbers (1, then 2), matching the handout's intent and leaving the explicit `figure(3)` / `figure(4)` calls alone.

```python
fig_plot = plt.figure()     # was: plt.figure(1)
```

**How to catch it.** Two output files with the *same byte size* are a bug, not a coincidence:

```sh
ls -l figs/ | awk '{print $5, $9}'
md5sum figs/*
```

Note that identical size with *different* md5 still means overplotted — matplotlib writes randomized element ids into SVG, so the bytes differ even when the picture is the same.

**Generalize:** any handout helper that hard-codes a figure number and gets called more than once has this bug.

---

## KI-02 · `plt.show()` does nothing headless

**Seen in:** Lab 0 · **Status:** expected, not a bug

`UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown`. Expected whenever the Agg
backend is selected. Save instead — from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26`:

```sh
MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

The handouts sanction saving to file, so this is a supported path, not a workaround.

⚠ **This machine is not headless, and that distinction matters.** It has a real display
(`DISPLAY=:1`, X11, 1920×1080) and nobody watching it. `MPLBACKEND=Agg` is *this project's* deliberate
"no windows" signal, not a consequence of there being no display —
[KI-13](#ki-13--a-gui-window-opened-during-an-unattended-run-and-blocked-it-forever) is the bug you get
from confusing the two. **Screenshots for submission need windows, so drop `MPLBACKEND` for those** —
they can be taken right here, no laptop needed
([`lab_template.md`](lab_template.md) block H2), and only the capture itself is human work.

---

## KI-03 · `myID` is a per-student seed and must be set every lab

**Seen in:** Lab 0, `recipes.py` · **Status:** resolved for Lab 0 (`myID = 6127`)

```python
myID = 6127                 # last 4 digits of the ERAU ID
np.random.seed(seed=myID)
Freq_1 = np.floor((10 + np.random.randint(0, 10)) / 3)
```

Handouts ship the placeholder `1234`. Expect this pattern in every lab, and set it before generating anything you intend to submit:

```sh
grep -rn "myID" dsp26/src/
```

**But do not expect the output to change visibly** — see [KI-06](#ki-06--setting-your-erau-id-may-not-change-the-figures-at-all). In Lab 0 the real ID and the placeholder both yield 4.0 Hz. Set it because the handout asks for it, not because you can see the difference.

---

## KI-04 · `uv` is not in the system package manager

**Status:** resolved

Not in apt. Install standalone (no root, lands in `~/.local/bin`):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
```

Installed here: **uv 0.12.8**. Add the `PATH` line to your shell profile or every new terminal will report `uv: command not found`.

---

## KI-05 · ImageMagick renders matplotlib SVG almost blank

**Seen in:** verifying Lab 0 figures · **Status:** avoid the tool

`convert file.svg out.png` on a matplotlib SVG produced axes and text but **no data** — plots looked empty. ImageMagick's built-in SVG renderer does not handle matplotlib's paths and clip paths.

**This can make correct output look broken.** To check a figure, save PNG directly from matplotlib rather than converting:

```python
fig.savefig("out.png", dpi=60)
```

Or open the SVG in a real renderer. **`rsvg-convert` and Inkscape are NOT installed here** (verified
2026-09-08) — do not go and install them. What *is* installed is a browser, and this machine has a
display (`DISPLAY=:1`), so:

```sh
firefox        /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/figs/<name>.svg
# or: google-chrome <same path>
```

Both are at `/usr/bin/`. The PNG route above is still the better check because it needs no window.

---

## KI-06 · Setting your ERAU ID may not change the figures at all

**Seen in:** Lab 0, `recipes.py` · **Status:** expected, not a bug

Changing `myID` from the placeholder `1234` to a real ID `6127` produced **byte-identical figures**. It looks like the change did not take effect. It did.

```python
Freq_1 = np.floor((10 + np.random.randint(0, 10)) / 3)
```

The draw genuinely changed — seed 1234 gives 3, seed 6127 gives 4 — but `floor((10+v)/3)` collapses ten possible draws onto **four** frequencies:

| `Freq_1` | Draws that produce it | Share of seeds |
| --- | --- | ---: |
| 3 Hz | 0, 1 | 20% |
| **4 Hz** | 2, 3, 4 | **30%** |
| **5 Hz** | 5, 6, 7 | **30%** |
| 6 Hz | 8, 9 | 20% |

Both 1234 and 6127 land in the 4 Hz bucket.

**Consequences worth knowing:**

- **Do not debug this.** Verify the seed changed the *draw*, not the frequency. Run from
  `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:
  ```sh
  uv run --project dsp26 python -c "import numpy as np; np.random.seed(6127); print(np.random.randint(0,10))"
  ```
  Prints `4`; swap in `1234` and it prints `3` — different draws, same `floor((10+v)/3) == 4`.
  **`--project dsp26` is required.** Without it, `uv run python -c ...` from this folder finds no
  project and fails with `ModuleNotFoundError: No module named 'numpy'` — verified 2026-09-08.
- Roughly **30% of the class will produce the same figures as each other**, and 30% will match the handout's placeholder output. Identical figures between two students are not evidence of anything.
- It also means "leaving the placeholder = submitting the instructor's plots" is only *sometimes* true. Set your real ID anyway — it is what the handout asks, and the seed is what is being checked.

---

## KI-07 · `splitlines()` vs `tokenize` desync silently corrupted stripped output

**Seen in:** `tools/strip_comments.py` · **Status:** fixed · **Found by:** adversarial testing, not by use

**Symptom.** Comments survived a strip; a `DEVIATION FROM HANDOUT` disclosure was deleted or truncated to a bare `#`; a string constant was silently truncated. **All exiting 0.**

**Cause.** Cut positions were keyed by *tokenize* line numbers, which break only on `\n`. The emit loop iterated `source.splitlines()` — which **also** breaks on U+000B, **U+000C (form feed)**, U+001C–1E, U+0085, **U+2028** and U+2029. One of those anywhere in the file shifts every subsequent line number, so cuts land on the wrong lines.

**Why it mattered here.** Form feeds are used as section separators in real source (several stdlib modules have them), and **U+2028 rides along in copy-paste from PDFs — which is exactly how handout code reaches us.**

**Why the safety net missed it.** `_verify` compared ASTs, and **comments carry no AST**. In the docstring case it was worse: `norm()` deleted `body[0]` from *both* trees, hiding a genuinely different string constant.

**Fix.** Split on `"\n"` everywhere, matching tokenize:

```python
src_lines = source.split("\n")            # was: source.splitlines()
for i, line in enumerate(source.split("\n"), start=1):
```

Plus a second check in `_verify`: every kept-pattern comment present in the input must still be present in the output. Comments have no AST, so this has to be explicit.

**Generalize:** `str.splitlines()` and every tokenizer disagree about what a line break is. **Never mix them.** If you index one by the other's line numbers, you have this bug.

---

## KI-08 · Stripping docstrings removes Typer's `--help` text

**Seen in:** `app_cli.py` · **Status:** fixed

**Symptom.** After stripping, `dsp26 --help` listed the command with **no description**.

**Cause.** Typer and Click build help text *from the function docstring*. To a stripper it looks like commentary; to the CLI it is user-visible output. The Lab 0 handout tells students to run `dsp26 --help`, so that text is part of what the lab demonstrates.

**Fix.** `strip_comments.py` keeps docstrings on functions whose decorators include `command` or `callback`:

```python
FUNCTIONAL_DOCSTRING_DECORATORS = ("command", "callback")
```

`--keep-docstrings` is the blunt escape hatch if some other decorator turns out to be functional too.

**Generalize:** a docstring is not always commentary — `argparse`, `pytest` ids, `doctest` and anything reading `__doc__` at runtime all make it functional. **Check `--help` still works after any strip.**

---

## KI-09 · Tooling references leaked into a submitted report

**Seen in:** `lab00/report.tex` · **Status:** fixed, and now blocked automatically

**Symptom.** The packaged `report.tex` carried a header naming our automation:

```latex
% Render:  tools/render_reports.sh lab00 --keep
% Package: tools/make_submission.sh lab00 nelson-gatlin --figures
```

One of those flags no longer even existed. The submitted document was advertising a build harness that is not part of the coursework — the same boundary [`code_separation.md`](code_separation.md) draws for code, crossed in a document instead.

**Cause.** Build instructions were written into the file they build, because that felt convenient.

**Fix, three layers:**

1. `report_template.tex` carries no tooling references, and says so in its own header, so new reports start clean.
2. `make_submission.sh --figures` strips **comment-only lines** from `.tex` before packaging.
3. A **hard guard** scans every packaged `.tex`/`.md`/`.txt`/`.py` for tooling references and **refuses to build the zip** if any survive, naming file and line.

Layer 3 is the one that actually enforces it; 1 and 2 just keep it tidy.

**Why only comment-only lines are stripped.** In LaTeX a trailing `%` suppresses the following space, so removing it changes the rendering. Deleting a whole comment-only line is safe — TeX consumes such lines entirely, and deleting one does not introduce the blank line that would start a new paragraph. Verified: PDF still 4 pages with identical text after stripping.

**Generalize:** build instructions belong with the build tooling, never in the artifact. If a file is going to be handed to someone else, nothing in it should describe how your repo works.

---

## KI-10 · `report_template.tex` did not build — it pointed at a figure that is never there

**Seen in:** `reference_docs/report_template.tex` · **Status:** fixed

**Symptom.** Build-checking the template failed outright:

```
Unable to load picture or PDF file 'figs/lab0_sinusoids_fig1.png'
```

**Cause.** The template's example figure named a real path from `lab00` — but
the template does not live in `lab00`, and `figs/` is gitignored everywhere, so
the file is absent on any fresh checkout regardless of folder. A template that
cannot be build-checked is a template nobody notices has rotted.

**Fix.** The example figure is wrapped in `\IfFileExists` with a visible
placeholder box as the fallback, so the skeleton compiles with no figures at
all and uses your figure once it exists. Both report files also gained
`\graphicspath{{./}{../}}` so a copy of the document one folder down still
resolves `figs/`.

**How to catch it.** Build the template itself, not only the reports written
from it. It is a document; treat it like one.

---

## KI-11 · A flattened report must never be packaged

**Seen in:** auditing the Overleaf outputs, 2026-09-05 · **Status:** expected — documented, not fixable here

**Symptom.** A report flattened for Overleaf opens with:

```latex
% Generated from content/cesc_410/labs_and_projects/lab00/report.tex -- edit that, not this.
```

That line matches both `reference_docs` and `labs_and_projects` in the
submission guard's pattern, so packaging a flattened copy is refused —
[KI-09](#ki-09--tooling-references-leaked-into-a-submitted-report) firing
exactly as designed, on a file the flattener wrote itself.

**Cause.** The flattener stamps its source path into every output. It lives
under the shared `docs/` tree, which this course does not own.

**Fix.** None needed. A report has no `\input` and needs no flattening. The
`overleaf/` copies exist only for pasting into Overleaf and are gitignored;
**the submission path is always `labNN/report.tex`.**

**How to catch it.** The guard already catches it, before the zip exists. That
is the point of having it.

---

## KI-12 · `check_inputs.py` cannot see an input referenced from Python

**Seen in:** Lab 1 · **Status:** expected, but the report is misleading

**Symptom.** `uv run --project dsp26 python tools/check_inputs.py lab01` prints
`OK    every referenced file is present`, while the lab's default input is absent:
`recipes.py` loads `project_root / "audio_files" / "2086-149220-0033.wav"`, and there is no
`audio_files/` directory at all.

*(Since resolved for Lab 1 specifically — `dsp26/audio_files/2086-149220-0033.wav` is now on disk,
provenance in `lab01/README.md`. **The checker's blind spot is unchanged**, and would report the same
`OK` if the file were deleted right now. Do not read the resolution as a fix.)*

**Cause.** The checker scans **Markdown links** (`LINK = re.compile(r"\[[^\]]*\]\(...")`). A path
built in Python is not a Markdown link, so it is structurally invisible. The tool is not broken — it
answers a narrower question than its `OK` line suggests.

**Fix.** None in the tool yet. **Read the handout's code for hard-coded paths yourself** and put them
in the lab README's Inputs table by hand. A `grep` for path-joins is a start:

```sh
grep -rnE '"[^"]*\.(wav|csv|npz|zip|mat)"' dsp26/src/
```

**How to catch it.** Run the command with no arguments before trusting the default: a missing default
input fails immediately with `FileNotFoundError`, which is the honest answer the checker did not give.

**Second blind spot — a folder argument produces false alarms.** `check_inputs.py <folder>` builds its
"what is on disk" index from that folder only, so a file that exists *elsewhere in the repo* is
reported as never downloaded. Verified 2026-09-08:

```sh
uv run --project dsp26 python tools/check_inputs.py lab00
#   -> NOT ON DISK ... py-pkg-1c-uv-cs.md   (it is in reference_docs/, exit 1)
uv run --project dsp26 python tools/check_inputs.py
#   -> PRESENT ELSEWHERE ... py-pkg-1c-uv-cs.md -> reference_docs/py-pkg-1c-uv-cs.md  (exit 0 for it)
```

**So: never hand a human a scoped run as the proof that their download landed.** Verify the file
directly with `ls -l <absolute path>`, and use the whole-tree run for the repo-wide picture.

---

## KI-13 · A GUI window opened during an unattended run and blocked it forever

**Seen in:** Lab 1, `recipes.py` · **Status:** fixed

**Symptom.** `MPLBACKEND=Agg uv run dsp26 play-plot-audio ... --folder-name lab01` produced **no
output and never exited**. An audio-player window had opened on the desktop, waiting for a click.

**Cause.** The handout calls `play_audio()` unconditionally; it opens Tk and blocks in `mainloop()`
until a human closes the window. The first guard skipped it only when `DISPLAY` was unset — but this
machine **has** a display (`DISPLAY=:1`), so the guard passed and the batch run hung.

**Fix.** Key the skip on the batch signal, not on display availability:

```python
batch = os.environ.get("MPLBACKEND", "").lower() == "agg"
```

`MPLBACKEND=Agg` is already this project's "no windows" convention ([KI-02](#ki-02--pltshow-does-nothing-headless)). Interactively the player still opens, which is what the graded screenshot needs.

**How to catch it.** `timeout` every unattended run that touches a GUI library. A command that
produces no output *and* does not exit is a blocked window, not a slow computation.

**Generalize:** `DISPLAY` answers "could a window open?", never "should one?". For any handout code
that opens a window, gate on how *you* are running it.

---

## KI-14 · Naming `DEVIATION FROM HANDOUT` in a docstring aborts packaging

**Seen in:** Lab 1, `audio_player.py` · **Status:** fixed

**Symptom.** `tools/make_submission.sh lab01 nelson-gatlin` refused to build:

```
ERROR .../lab1_audio_sig/audio_player.py: stripping lost a 'DEVIATION FROM HANDOUT' comment (1 -> 0)
error: stripping failed -- aborting rather than shipping bad code
```

**Cause.** The file has **no deviation**; it is transcribed verbatim. Its module docstring merely
*pointed at* a deviation in another file, using the marker phrase. Docstrings are stripped
([KI-08](#ki-08--stripping-docstrings-removes-typers---help-text)), so the count went 1 → 0 and the
guard correctly refused. The guard is right --- a disclosure that vanishes from submitted code is
exactly what it exists to prevent; it simply cannot tell a marker from a mention of one.

**Fix.** Keep the marker phrase for real deviations, in `#` comments, in the file that deviates.
Refer to one elsewhere without quoting the phrase:

```python
# was: "... -- see the DEVIATION FROM HANDOUT block there."
# now: "This file itself is unmodified -- every change Lab 1 needed is in recipes.py
#       and is marked there."
```

**How to catch it.** Run `make_submission.sh` as soon as the code works, not at submission time. It
is a two-second check that reads the code the TA will actually receive.

---

## KI-15 · A human task that names no place costs a round trip

**Seen in:** `lab01/README.md` § *Needs a human*, 2026-09-08 · **Status:** fixed as doctrine, [`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md)

**Symptom.** The lab README told the human:

> **Fetch `2086-149220-0033.wav` from Canvas** into `dsp26/audio_files/` — the handout's default input, not downloadable from here

The operator went to Canvas, could not find it, and had to come back and ask. Nothing in the sentence
is false, and it still cost a round trip.

**Cause.** Six omissions in one line:

| Missing | What it said | What was needed |
| --- | --- | --- |
| **WHERE** | "from Canvas" | Canvas is an entire LMS. Which course, which module, which page? |
| **WHAT** | "into `dsp26/audio_files/`" | a *relative* path, to a folder that **did not exist on disk**; no `mkdir` |
| **VERIFY** | — | a command proving the right file landed in the right place |
| **IF ABSENT** | — | the case that actually happened, unhandled |
| **BLOCKS** | — | "Nothing else is blocked" sat three lines later, attached to nothing |
| **HOMEWORK** | "not downloadable from here" | no evidence anything was searched, and no substitute named |

There was even a good fallback — `lab01/test_tone.wav`, which every figure was generated from — but it
was described in a *different section*, so the connection was never made.

**Fix.** Every human task states **WHERE, WHAT, VERIFY, IF ABSENT, BLOCKS**, and every
HUMAN-REQUIRED claim names a reason. The blocks are pre-written in
[`lab_template.md`](lab_template.md) § *Needs a human* — copy them rather than re-deriving them, and
never delete an element from a block you keep.

**Second-order finding.** The Canvas course URL, the module names and the TA's contact details were
**not recorded anywhere in this repo**, which is why "Canvas" kept appearing unqualified. That is a
one-time fix worth more than any individual task: put them in
[`../README.md`](../README.md#course-facts-that-drive-the-workflow) § *Course facts* the first time
anyone has them.

**Update 2026-09-08 — two of the three are filled in, and the source was a surprise.** The TA's name
and contact (**Ryle**, Discord `ryletraub_30890`) came from a **course Announcement**, not the People
tab this repo had been pointing at; the same post also fixed the submission and demo deadlines, and
confirmed that lab material lives on each lab's page under the **Modules** tab. **Read Announcements
before recording a Canvas fact as unknowable.** The remaining two blanks — the course URL and the
exact module titles — have a three-minute procedure at
[`../README.md`](../README.md#how-to-fill-in-the-last-two--three-minutes-once--why-human-credentialed)
§ *How to fill in the last two*. Until they are filled, say so in the task — *"nobody here knows which
module; ask Ryle"* is a specific instruction. Vagueness is not.

**How to catch it.** Read your own *Needs a human* section as the person who has to act on it. If any
row leaves them a choice about where to go, it is not finished. The checklist is at the bottom of
[`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md).

---

## KI-16 · No ffmpeg on this machine: yt-dlp -x fails; convert with librosa

**Seen in:** Lab 1, preparing the experimental music clip · **Status:** expected — use Solution A

**Symptom.** A lab wants a specific audio shape (Lab 1: ~10 s, mono, 16 kHz WAV) and the human has a
download in some other format. The obvious tooling is absent:

```sh
command -v ffmpeg      # -> nothing
command -v sox         # -> nothing
```

`yt-dlp` **is** installed (`2026.06.09`, `~/.local/bin/yt-dlp`), but its `-x` / `--extract-audio`
post-processing needs `ffmpeg`, so the usual one-liner cannot work here.

**Cause.** Neither `ffmpeg` nor `sox` is packaged on this machine, and installing either needs root.

**Solution A: command-line, no root, no ffmpeg.** `soundfile` in the `dsp26` venv is libsndfile
**1.2.2**, which reads **MP3, OGG, FLAC, WAV, AIFF, CAF** directly; `librosa.load` resamples and
downmixes in the same call. Run from `/home/devel/electrical_notes/content/cesc_410/labs_and_projects`:

```sh
uv run --project dsp26 python -c "
import librosa, soundfile as sf, sys
y, sr = librosa.load(sys.argv[1], sr=16000, mono=True, offset=0.0, duration=10.0)
sf.write(sys.argv[2], y, sr, subtype='PCM_16')
print(f'wrote {sys.argv[2]}  mono  {sr} Hz  {len(y)/sr:.1f} s')
" /home/devel/Downloads/whatever.mp3 labNN/music_clip.wav
```

Verified on a stereo 44.1 kHz MP3 → `wrote labNN/music_clip.wav  mono  16000 Hz  10.0 s`, and the
result reads back as `channels 1 rate 16000 frames 160000 width 2`. `offset` picks the start second;
`duration` sets the length.

**Solution B: install ffmpeg.** `sudo apt install ffmpeg`, then `yt-dlp -x --audio-format wav` and
`ffmpeg -i in -ac 1 -ar 16000 -t 10 out.wav` behave as documented. **Needs root, so it is a human
step** — and Solution A already covers every format the labs have needed, so prefer A.

**This splits a human task in half.** The human supplies a raw file in *any* readable format — or none
at all, if a recording will do (`arecord -f S16_LE -r 16000 -c 1 -d 10 out.wav`, microphone verified as
`card 1: PCH [HDA Intel PCH]`). **Shaping it is automatable**, so never hand over "produce a 10 s mono
16 kHz WAV"; hand over "give me the audio" and do the rest.

**How to catch it.** Check the format support you actually have before assuming a converter exists:

```sh
uv run --project dsp26 python -c "import soundfile as sf; print(sf.__libsndfile_version__); print(sorted(sf.available_formats()))"
```

---

## KI-17 · A report can reference a figure that moved to a sibling folder; `render_reports.sh` blames the wrong thing

**Seen in:** `lab01/report.tex`, 2026-09-08 · **Status:** open — needs a one-line decision, see below

**Symptom.** `tools/render_reports.sh lab01` fails:

```
lab01/report.tex                             FAIL
    error: report.tex:190: Unable to load picture or PDF file 'figs/lab1_audio_prog_zoom_0.5_1.5.png'
1 file(s) failed to render.
Missing figures? figs/ is gitignored -- generate them first:
```

**The hint is wrong here, and that is the trap.** Regenerating `figs/` will not help — the file is
already on disk, in the *other* figure folder:

```sh
ls lab01/figs/lab1_audio_prog_zoom_0.5_1.5.png       # -> No such file
ls lab01/figs_music/lab1_audio_prog_zoom_0.5_1.5.png  # -> 70151 bytes, present
```

**Cause.** Lab 1 keeps two figure sets — `figs/` from the handout's default input and `figs_music/`
from the experimental clip. The report's third `\includegraphics` names a **`figs_music/` figure with a
`figs/` prefix.** `\graphicspath{{./}{../}}` does not rescue it: graphicspath prepends *directories*,
so the engine looks for `./figs/<name>` and `../figs/<name>`, never `figs_music/`.

`lab01/report.pdf` is still on disk and looks fine — it is a **stale build from 12:07**, made while
that figure was still in `figs/`. A stale PDF next to a `.tex` that no longer builds is the worst
version of this: nothing looks broken until packaging runs.

**Fix — pick one, both one line, from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:**

```sh
# (a) point the report at where the figure actually lives  -- keeps the two sets separate
sed -i 's#figs/lab1_audio_prog_zoom#figs_music/lab1_audio_prog_zoom#' lab01/report.tex

# (b) or copy the experimental figure in beside the others -- keeps every \includegraphics uniform
cp lab01/figs_music/lab1_audio_prog_zoom_0.5_1.5.png lab01/figs/
```

**(a) is the better default** — `figs/` is gitignored and regenerated by the *default-input* command,
which does not produce this figure, so a copy placed there is silently destroyed by the next
regeneration. Either way, re-render and confirm:

```sh
tools/render_reports.sh lab01
#   -> lab01/report.tex   OK  -> lab01/report.pdf
#   -> All rendered. PDFs kept (gitignored).
```

**How to catch it.** **Re-render before trusting any `report.pdf` you did not just build.** The PDF is
gitignored and kept, so its presence proves nothing about whether the source still compiles. Cheap
check for the whole class of problem:

```sh
for f in $(grep -o 'figs[^}]*\.png' labNN/report.tex | sort -u); do
  [ -e "labNN/$f" ] || echo "MISSING: $f"
done
```

**Generalize:** the moment a lab grows a second figure directory, `\includegraphics` prefixes stop
being interchangeable, and `render_reports.sh`'s "regenerate figures first" advice becomes actively
misleading. Check *where* the file is before believing it is absent.

---

## KI-18 · A stale flattened copy hid a tooling-reference leak for three days

**Seen in:** `reference_docs/overleaf/report_template.tex` · **Status:** fixed; check added

**Symptom.** None. That is the point. The copy compiled, looked correct, and its
first two lines read:

```latex
% Self-contained for Overleaf: preamble inlined, no external \input.
% Generated from content/cesc_410/labs_and_projects/reference_docs/report_template.tex -- edit that, not this.
```

A repo path inside a document meant for submission — the same class of leak as
[KI-09](#ki-09--tooling-references-leaked-into-a-submitted-report).

**Cause.** Two failures compounding. `flatten_tex.sh`'s header used to stamp the
full repo-relative source path; that was fixed, but **the already-generated
copies were never regenerated**, and nothing compared them against what the
flattener would produce today. Re-flattening is manual, and forgetting it is
silent — a stale copy is indistinguishable from a current one by inspection.

**Fix.** Regenerate (`docs/latex/flatten_tex.sh <assignment>`), and use the check
that now exists:

```sh
docs/latex/flatten_tex.sh --check          # whole corpus, exit 3 if anything is stale
```

It compares **content**, not timestamps, so `touch` cannot mask a stale copy. It
reports `STALE`, `MISSING` and `ORPHAN` (a copy whose source was renamed or
deleted, which would otherwise sit there looking uploadable forever).

**How to catch it.** `build_tex.sh` now runs the check automatically for any
directory with an `overleaf/` beside it. Before this existed, nothing did — the
leak was found only because someone went looking for a *different* problem.

**Generalize:** any generated artifact that is committed and regenerated by hand
needs a freshness check, or it drifts from its source in silence. The build
passing says nothing about the artifact you actually ship.

## KI-19 · A filename that parses as a public-dataset id is not proof of provenance

**Seen in:** `lab01/` — `dsp26/audio_files/2086-149220-0033.wav` · **Status:** fixed; superseded file parked

**Symptom.** Everything looked right and nothing complained. `check_inputs.py`
said the lab was clean, five figures generated, the report built, and the audio
file had the exact name the handout asks for. It was **the wrong audio** — 7.435 s
of read speech where the graded default input is a 10.00 s synthetic tone pair.
Every figure in `lab01/figs/` was a picture of the wrong signal, and the only
reason it was caught is that the TA later posted a screenshot of their own output.

**Cause.** The handout names the file exactly once, inside a code block, with no
link and no "download from". `2086-149220-0033` parses cleanly as a **LibriSpeech
utterance id** — speaker 2086 / chapter 149220 / utterance 0033 — and speaker 2086
really is in `dev-clean`. The corpus copy was fetched, verified sample-for-sample
against the corpus original, and installed. **The verification was rigorous and
verified the wrong thing:** it proved the file matched *LibriSpeech*, when the
question was whether it matched *the instructor's file*. A confident id parse
became a provenance claim without anything ever testing that step.

**Fix.** Two parts.

**A — treat a parsed filename as a hypothesis, and say so in writing.** It is
worth recording (it tells a human what to look for), but the note must read
*"the name looks like X"*, never *"the file is X"*, until something external
confirms it. Where a stand-in has to be used, mark it a **deviation** and keep it
under a name that cannot be loaded by accident:

```sh
# not: overwrite the real path and hope
mv dsp26/audio_files/2086-149220-0033.wav \
   dsp26/audio_files/librispeech_2086-149220-0033.wav.notused
```

**B — check the *content*, not the link.** `check_inputs.py` scans Markdown links
for missing files; it cannot see a path built in Python
([KI-12](#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python)) and,
more importantly, **no checker in this repo compares a file's contents to an
expectation**. A present-but-wrong file passes every gate. When the instructor
publishes reference output, diff against it:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
md5sum dsp26/audio_files/2086-149220-0033.wav
# -> b8c6e2fc5147d4c627efa0f443c82102
MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name /tmp/chk 2>/dev/null
# compare channels / sample width / frame rate / frames / duration against the
# instructor's published run before trusting any figure
```

**How to catch it.** **Read the course Announcements before concluding an input
is unobtainable.** The answer here was posted to Canvas, with the file attached,
by the TA — while this repo was reasoning its way to a substitute. The cost was
not the wrong download; it was five hours of figures, captions and README prose
written about audio nobody was going to grade.

Three cheap habits, in order of how much they would have saved:

1. **Announcements first.** A "handout gap" is often a gap in *what you read*, not
   in what exists. The TA has since said a supplemental reference document will
   accompany every future lab.
2. **Ask before substituting a graded input**, even when a public copy verifies
   perfectly. Verification against the wrong reference is still wrong.
3. **Never let two candidate files share the loadable name.** Park the loser under
   `.notused` and record both checksums, so the comparison survives.

**Generalize:** *provenance is a claim about where bytes came from, and only the
source can settle it.* An id that decodes, a checksum that matches a public
mirror, and a file that loads without error are all compatible with having the
wrong file. Ask what would be true if this were wrong — here, the duration would
differ, and it did.

---

---

## Template

```markdown
## KI-NN · One-line symptom

**Seen in:** where · **Status:** open / fixed / expected

**Symptom.** What you observe.
**Cause.** Why.
**Fix.** Code or command.
**How to catch it.** The check that would have caught it sooner.
```

---

**Related:** [`../prompt.md`](../prompt.md) · [`../README.md`](../README.md)
