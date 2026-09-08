# Claude entry point — CESC 410L labs

**Trigger:** *"`labNN/` now exists with the lab material in it, get it all done."*

Read this file, then the docs it points at, then work. Stop only for the things listed under [Human-only](#human-only).

---

## Read first (in order)

1. This file.
2. [`README.md`](README.md) — layout, conventions, environment.
3. [`reference_docs/known_issues.md`](reference_docs/known_issues.md) — **check before debugging anything.** Recurring traps live here.
4. [`reference_docs/code_separation.md`](reference_docs/code_separation.md) — **which code is submitted and which is not.** Read before writing anything.
5. [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md) — how to comment what you write.
6. [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md) — **what this lab actually has to hand in. Largely unconfirmed; surface it.**
7. The lab's own handout in `labNN/` (`.md` preferred over `.pdf` — the `.md` is the source and has the code in copyable form).
8. [`reference_docs/py-pkg-1c-uv-cs.md`](reference_docs/py-pkg-1c-uv-cs.md) — the instructor's `uv` cheatsheet. Only if the lab does something new with packaging.

---

## Procedure

### 1. Inventory the lab folder

List what is in `labNN/`. Then read the handout and build the expected-inputs list — every file the handout names or links to. Run:

```sh
uv run --project dsp26 python tools/check_inputs.py
```

**One entry is permanent and is not yours to fix: `py-pkg-1c-uv-qg.md`.** The whole-tree run therefore
**exits 1 every time**, and a `PRESENT ELSEWHERE` section for `py-pkg-1c-uv-cs.md` is also expected and
harmless. Both are already written up in [`README.md`](README.md#status) § *Open across the course* —
**do not re-report either as a new blocker.** Anything *else* under `NOT ON DISK` is real.

**Report anything missing before starting work.** Handouts commonly reference a `.zip` of starter code, a dataset, or a sibling document that was not downloaded. Missing inputs are the single most common reason a lab stalls, and they need a human to fetch them from Canvas.

⚠ **A clean `check_inputs.py` does not mean nothing is missing.** It scans *Markdown links*; a path built in Python is structurally invisible to it — [KI-12](reference_docs/known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python). Read the handout's code for hard-coded paths yourself:

```sh
grep -rnE '"[^"]*\.(wav|csv|npz|zip|mat)"' dsp26/src/
```

Record the result as the **Inputs** table in the lab README (see the template), and give each missing file a **Blocks** entry — what stops, and what does not.

**A missing input is not a sentence, it is a block.** Write it as H1 in [Human-only](#human-only): WHERE to look, WHAT to do, how to VERIFY it landed, what to do IF it is absent, and what it BLOCKS. Do the searching first and quote the commands you ran, so the human does not repeat them.

### 2. Extract the work

From the handout, separate:

- **Code to write** — usually into `dsp26/src/dsp26/labN_<topic>/`, plus a command in `app_cli.py`. This is **lab code**: it gets submitted, so it must stand alone and read like a student's solution.
- **Runs to perform** — the CLI invocations that produce output.
- **Artifacts to produce** — figures, numbers, tables. These are the deliverable.
- **Questions to answer** — handouts often bury prose questions between code blocks. They are graded. Collect them explicitly.

### 3. Do it

Write the code, run it, save artifacts into `labNN/figs/` (or `labNN/out/` for non-figures). Verify:

```sh
uv run --project dsp26 python tools/check_artifacts.py labNN/figs
```

**Keep lab code and automation separate** — [`reference_docs/code_separation.md`](reference_docs/code_separation.md). `dsp26/` is submitted and must work with `tools/` deleted; `tools/` is ours and never ships. Anything that exists only because we drive the lab from a terminal is automation.

**Comment as you write** — [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md). One comment per logical step, naming the operation ("take the DFT and shift zero frequency to the centre"), never restating syntax. Put the governing equation in the docstring; it becomes the report's equation block.

**Transcribe handout code faithfully first, then fix.** If handout code is wrong, keep the structure and mark the change with a `DEVIATION FROM HANDOUT:` comment saying what the handout had, what broke, and why. The TA sees this code — an unexplained rewrite looks like the student didn't follow the lab. A marked, justified fix looks like engineering. Log every deviation in the lab README and, if it could recur, in `known_issues.md`.

### 4. Write `labNN/README.md`

Copy [`reference_docs/lab_template.md`](reference_docs/lab_template.md) and fill it. It is a **reproduction log**, not a summary: someone should be able to reproduce the lab from it without opening the handout. Every command verbatim, in order, with what it printed.

### 5. Report, if the lab needs one

Copy [`reference_docs/report_template.tex`](reference_docs/report_template.tex) to `labNN/report.tex` and fill the four sections. Verify it builds:

```sh
tools/render_reports.sh labNN
```

Expected: `labNN/report.tex   OK  -> labNN/report.pdf`, then `All rendered. PDFs kept (gitignored).`

The `.tex` is the artifact — the human pastes it into Overleaf. **The PDF is kept** (gitignored as `report*.pdf`), so the built report is on hand without a rebuild.

### 6. Report back

Tell the human:

- What is done and verified.
- What is blocked, and on what.
- **Everything from [Human-only](#human-only) that this lab needs — as blocks, not as a list of nouns.**

Then run the hand-off checklist in
[`human-task-instructions.md`](../../../docs/directives/human-task-instructions.md) against your own
*Needs a human* section. The short form:

- [ ] Every human task names a reason from the six.
- [ ] Nothing on the list is actually automatable — including the automatable *half* of a split task.
- [ ] Every path is absolute, from `/`. Every file move is a Source (FROM) → Destination (TO) table.
- [ ] Every task states WHERE, WHAT, VERIFY, IF ABSENT, BLOCKS — all five.
- [ ] No WHERE is a category noun. "Canvas" is a category; "Canvas → CESC 410L → the Lab 1 module, the page the handout came from" is a place.
- [ ] Every VERIFY is a command you have run, with the output you saw.
- [ ] Every blocking input has a fallback attached to it, with its cost stated.
- [ ] Anything learned goes in [`reference_docs/known_issues.md`](reference_docs/known_issues.md).

---

## Human-only

Do not attempt these. **Surface them to the standard** — a vague hand-off spends the human twice, once
on the task and once on working out what the task was. Every human task you write states **WHERE,
WHAT, VERIFY, IF ABSENT, BLOCKS**, and every "this needs a human" claim names a *reason*.

The rule, and the failure that produced it:
[`human-task-instructions.md`](../../../docs/directives/human-task-instructions.md).
The ready-made blocks: [`reference_docs/lab_template.md`](reference_docs/lab_template.md) § *Needs a
human* — **copy them, do not re-derive them.**

### Before you put anything on this list

**AUTOMATABLE is the default.** HUMAN-REQUIRED is a claim, and it needs one of six reasons:

| Reason | Means | In this course |
| --- | --- | --- |
| `GUI-only` | no command-line path exists at all | nothing yet — matplotlib, LaTeX and the CLI are all scriptable |
| `Hardware` | a physical device, cable or live recording | the microphone (`card 1: PCH [HDA Intel PCH]`) |
| `Credentialed` | behind a login this agent holds no session for | Canvas download, Canvas submission |
| `Capture` | a screenshot, a recording, a live demo | screenshots of the figure and player windows |
| `Judgment` | two defensible answers and the wrong one is graded | is this deviation acceptable; what does this lab submit |
| `Policy` | a course or repo rule reserves it for a person | the live demo; git commits |

Anything else is AUTOMATABLE. **"It's fiddly" and "I'd rather not" are not reasons.**

**Split the task at the real boundary before handing the whole thing over.** Plotting *looks* human
because `plt.show()` opens windows. It is not: `MPLBACKEND=Agg` saves every figure headlessly
([KI-02](reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless)), and only the
*screenshots of those windows* are `Capture`. Handing over "make the figures" instead of "screenshot
these five windows" moves an hour of automatable work onto the human.

**Do the human's homework first, and show it.** Before writing "download X":

- Search the machine for it by name and by extension — and **quote the command** in the task.
- Read the handout for where it is supposed to come from, and say what the handout does or does not say.
- **Ask the human to check Canvas Announcements**, and say that is what you are asking for. The TA
  posts a supplemental reference document for every lab, and Lab 1's answered four questions this repo
  had recorded as open — including where the default `.wav` came from. A "handout gap" is often a gap
  in what has been read, not in what exists.
- Look for a substitute on disk or one you can generate, and name it.
- Check the sibling `labNN/` folders and `reference_docs/`.
- Say what the filename **looks like**, if that is knowable — **as a lead, never as an answer.**
  `2086-149220-0033.wav` parses as a LibriSpeech utterance id (speaker 2086 / chapter 149220 /
  utterance 0033), which is worth one line because it tells the human what to search for. ⚠ **In Lab 1
  that lead was correct about the name and wrong about the file.** The TA supplied their own 10 s
  synthetic clip under that name; the LibriSpeech audio is 7.4 s of speech, and five hours of figures
  and captions were written about the wrong signal before a TA screenshot exposed it. Write *"the name
  looks like X"*, never *"the file is X"*, and never treat a public copy as the graded input —
  [KI-19](reference_docs/known_issues.md#ki-19--a-filename-that-parses-as-a-public-dataset-id-is-not-proof-of-provenance).

"Not downloadable from here" is a conclusion. Show the work that reached it.

**Every blocking input gets a fallback, attached to the task.** Say what the fallback costs — a
synthetic stand-in is a **deviation** and belongs in the report's Narrative, which is graded. And never
let a missing input stall work it does not gate: run everything that does not need it, then list only
the genuinely blocked step. **Keep a substitute under a name that cannot be loaded by accident** — park
it as `<name>.notused` rather than installing it at the path the real input will occupy, so that when
the real file arrives the two can be compared instead of one silently having overwritten the other.

### The recurring list

Nine tasks recur. The first six have ready-written blocks in the lab template; copy the block, do not
write a one-line summary of it.

| # | Task | Why human | What it blocks | Block |
| --- | --- | --- | --- | --- |
| H1 | Fetch a missing input (starter zip, dataset, audio) | `Credentialed` | usually one run or one figure — **say which** | [template](reference_docs/lab_template.md) |
| H2 | Screenshots of the GUI windows | `Capture` | the report's Artifacts section only | [template](reference_docs/lab_template.md) |
| H3 | Live demo — **in person to Ryle, by the next lab section**; early checkout allowed | `Policy` | grading of the report, not its writing | [template](reference_docs/lab_template.md) |
| H4 | Approve / finish the report | `Judgment` | submission | [template](reference_docs/lab_template.md) |
| H5 | Upload to Canvas — **due 1 week after the lab is assigned** | `Credentialed` | the grade — late is a zero | [template](reference_docs/lab_template.md) |
| H6 | Confirm what this lab must submit | `Judgment` | which command H5 runs | [template](reference_docs/lab_template.md) |
| H7 | Team membership for this lab | `Policy` | who submits, and how many times | below |
| H8 | Judging whether a deviation is acceptable | `Judgment` | nothing — work continues either way | below |
| H9 | Supply a self-made input (recording, photo, measurement) | `Hardware` | the experimental task that needs it | below |

**H3 and H5 are two different deadlines.** The Canvas upload is due *1 week after the lab is
assigned*; the demo is due *by the next lab section*. For a lab that spans a no-lab week they are
different dates — never write one block that conflates them. Both rules, with the TA's own wording:
[`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md).

**Who to name when a block says "ask the TA".** **Ryle** — Discord `ryletraub_30890`, Canvas
**Inbox**, or in person at either section's meeting (the TA invites students to attend the other
section too). ⚠ **Email is invited but no address is published — never invent one.** Recorded in
[`README.md`](README.md#course-facts-that-drive-the-workflow) § *Course facts*. Before Lab 1 this row
was blank, and every human block in the repo had to say *"the meeting is the only route to a TA"*;
that phrasing is now stale wherever it survives.

**Not on this list any more — do not hand it back:**

| Was human | Now | Why |
| --- | --- | --- |
| **ERAU ID digits** | **AUTOMATABLE** | The value is on file — `2636127`, `myID = 6127`, in [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md#student-id). Set it yourself with `grep -rn "myID" dsp26/src/`, then verify the figures regenerate. Ask only if a lab introduces a *different* personal field, and then ask for that field by name. |
| **Generating figures** | **AUTOMATABLE** | `MPLBACKEND=Agg` — [KI-02](reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless). Only the screenshots are human. |
| **Converting a downloaded clip to lab shape** | **AUTOMATABLE** | `librosa` + `soundfile` resample and downmix without `ffmpeg` — [KI-16](reference_docs/known_issues.md#ki-16--no-ffmpeg-on-this-machine-yt-dlp--x-fails-convert-with-librosa). The human supplies the raw file; you shape it. |

---

### H7 · Team membership for this lab · Why human: **Policy**

**WHERE.** The TA, at the start of the lab meeting (LB 373, Sec 1 Tue / Sec 2 Fri, 5:15–8:15 pm).

**WHAT.** Confirm two things and write both into `labNN/README.md` and the report header block:
who the partner is for **this** lab, and whether this lab collects an **ABET artifact**.

**VERIFY.** The report header names the team (or `individual`), and the *Per-lab requirements* row in
[`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md#per-lab-requirements)
records how many submissions this lab expects.

**IF YOU CANNOT CONFIRM.** **Submit individually.** One submission per team is the rule *except* on
ABET-artifact labs, where every student submits independently — so an extra individual submission is
never wrong, and a missing one is a zero.

**BLOCKS.** How many times H5 runs, and the name in the report header. Nothing about the code.

*Teams are two students, rebuilt every two labs from Lab 3.* Re-confirm at the start of Labs 3, 5, 7.

---

### H8 · Judging whether a deviation is acceptable · Why human: **Judgment**

You do **not** hold this back and wait. Fix the handout code, mark it, and keep going — the judgment
call is about whether to *keep* the fix, not whether to make it.

**WHERE.** `labNN/README.md` § *Deviations from the handout*, and the `DEVIATION FROM HANDOUT:` comment
in the source file.

**WHAT.** For each deviation, present three things and let the human choose: what the handout had, what
broke, and what you changed it to. Say whether the handout's version *runs at all* — a deviation that
fixes a crash is a different decision from one that changes a figure's appearance.

**VERIFY.** Every row in the Deviations table has a matching `DEVIATION FROM HANDOUT:` comment in the
source, and the count survives packaging:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
tools/make_submission.sh labNN nelson-gatlin
```

Expected (verified 2026-09-08 on `lab01`): a `Stripping comments...` block with a `N -> M lines` row
per file, then `Wrote /home/devel/.../labNN/dsp26-labNN-nelson-gatlin.zip`, a `Contents:` file list,
and a size. **Exit 0 and a printed file list is the pass.** It aborts with
`error: stripping failed -- aborting rather than shipping bad code` if stripping loses a disclosure —
[KI-14](reference_docs/known_issues.md#ki-14--naming-deviation-from-handout-in-a-docstring-aborts-packaging).

**IF THE HUMAN DOES NOT DECIDE.** **Keep the marked fix.** A marked, justified fix reads as
engineering; reverting to code that does not run reads as not having done the lab.

**BLOCKS.** Nothing. The report's Narrative section is *better* for having the story in it either way.

---

### H9 · Supply a self-made input · Why human: **Hardware**

Some labs need a recording, photo or measurement that does not exist yet. **Only the raw capture is
human** — shaping it into what the lab wants is yours.

**WHERE.** This machine can do it — no laptop, no phone. It has a microphone (`arecord -l` →
`card 1: PCH [HDA Intel PCH], device 0: ALC294 Analog`) and a PulseAudio monitor source that captures
whatever the speakers are playing (`pactl list short sources` →
`alsa_output.pci-0000_00_1f.3.analog-stereo.monitor`).

**WHAT.** Pick one. Both were run end-to-end on this machine on 2026-09-08 and both produced a valid
WAV; substitute a real lab folder for `labNN`:

```sh
# (a) record 10 s from the microphone
arecord -f S16_LE -r 16000 -c 1 -d 10 \
  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/raw.wav

# (b) capture 10 s of whatever is playing through the speakers.
#     PULSE_SOURCE is REQUIRED. Without it, -D pulse records the DEFAULT source,
#     which on this machine is the microphone -- you get room noise, not the audio.
PULSE_SOURCE=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor \
arecord -D pulse -f S16_LE -r 16000 -c 1 -d 10 \
  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/raw.wav
```

Both print `Recording WAVE '<path>' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono` and return
after the `-d` seconds. `pactl info | grep 'Default Source'` shows why (b) needs the override —
today it prints `alsa_input.pci-0000_00_1f.3.analog-stereo`, the microphone.

Or hand over any `.mp3` / `.ogg` / `.flac` / `.wav` file and stop there — **the agent converts it.**
`ffmpeg` is not installed; `librosa` + `soundfile` do it without one
([KI-16](reference_docs/known_issues.md#ki-16--no-ffmpeg-on-this-machine-yt-dlp--x-fails-convert-with-librosa)).

**VERIFY.**

From `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
uv run --project dsp26 python -c "import wave,sys; w=wave.open(sys.argv[1]); print(f'{w.getnchannels()} ch  {w.getframerate()} Hz  {w.getnframes()/w.getframerate():.2f} s')" \
  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/raw.wav
```

Expected for a Lab 1-shaped clip: `1 ch  16000 Hz  10.00 s`. A file of `0.00 s` means the device was
busy or muted. **Duration alone does not prove there is sound in it** — a muted mic and a suspended
monitor both write a full-length file of silence. Check the level too:

```sh
uv run --project dsp26 python -c "import soundfile as sf,sys,numpy as np; y,_=sf.read(sys.argv[1]); print('peak', float(np.abs(y).max()))" \
  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/raw.wav
```

Expected: `peak` well above `0.0` (`dsp26/audio_files/2086-149220-0033.wav` reads `peak 0.7818`).
Anything at or near `0.0` is a silent file — go to the next block. **Verified 2026-09-08: a monitor
capture taken with nothing playing reads exactly `peak 0.0`,** which is how this check earns its place.

**IF NO SOUND IS CAPTURED** — i.e. `peak 0.0`, or a duration of `0.00 s`.

1. **Route (b), silent.** The monitor source sits `SUSPENDED` until something plays — `pactl list
   short sources` shows the state. **Start the playback first, leave it playing, then run the record
   command in a second terminal.** Ten seconds of silence at the top of a clip is the usual cause.
2. **Route (a), silent or very faint.** `pactl list short sources` lists the microphone whether or not
   it is usable, so its presence proves nothing. Diagnose, then fix:

   ```sh
   pactl get-source-mute   alsa_input.pci-0000_00_1f.3.analog-stereo   # want: Mute: no
   pactl get-source-volume alsa_input.pci-0000_00_1f.3.analog-stereo   # 2026-09-08: 24% / -37.70 dB
   ```

   **24% is low enough to look like silence on a quiet source** — that is the machine's current
   setting, not a fault. Raise it and unmute:

   ```sh
   pactl set-source-mute   alsa_input.pci-0000_00_1f.3.analog-stereo 0
   pactl set-source-volume alsa_input.pci-0000_00_1f.3.analog-stereo 70%
   ```

   Re-record and re-check `peak`. The GUI route is the system Sound settings → Input.
3. **Device busy.** `arecord` exits immediately with `Device or resource busy` if something else holds
   the card — close any browser tab or meeting app that has the microphone, then retry.
4. **Still nothing:** hand over any existing `.mp3` / `.ogg` / `.flac` / `.wav` from anywhere instead.
   That is a fully equivalent answer to this task — the agent shapes it — so do not spend more than a
   few minutes here.

**BLOCKS.** Only the experimental task that needs the file. Everything driven by the handout's default
input is unaffected — **say so in the lab README rather than leaving it implied.**

---

## Rules

- **Never commit `.venv/`.** It is ~250 MB. It is gitignored; keep it that way. If a lab makes a venv under a different name, add it to `.gitignore` and say why in the lab README.
- **Commit `uv.lock`.** It is what makes the environment reproducible.
- **One package, many labs.** `dsp26` is shared for the whole semester — each lab adds a subpackage and a CLI command, not a new project. This is the handout's design, not ours.
- **Documentation lives in `labNN/`; lab code in `dsp26/`; automation in `tools/`.** Deliberate — see [`README.md`](README.md#why-code-and-docs-are-split) and [`reference_docs/code_separation.md`](reference_docs/code_separation.md).
- **Figures: save PNG and SVG.** The report needs PNG; handouts save SVG only, so this is a marked deviation.
- **`figs/` is gitignored** — regenerable, and images bloat git. Never `git add` it without `-f` and a reason.
- **Comment every file so it stands alone** ([`reference_docs/code_commenting.md`](reference_docs/code_commenting.md)). Comments are stripped at submission time by `tools/make_submission.sh`, so write them for us, not for the TA — but **never strip a `DEVIATION FROM HANDOUT` block**, which is disclosure.
- **Never put tooling references in a deliverable.** No script names, flags or repo paths in a report `.tex`/`.md`. Packaging blocks on it.
- **Never hand-edit code for submission.** `make_submission.sh` strips into a staging copy; the working tree keeps its comments.
- **Verify, don't assume.** Run it. Check the output is what the handout describes. Two identically-sized output files are a bug, not a coincidence.
- **Publishing and git are not a concern for this project.** The parent repo has a remote and a Hugo `baseURL`, but that does not apply here — see [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md#publishing-and-git--not-a-concern-here). Do not raise it, do not add redaction steps.
- **Prefer the `.md` handout over the `.pdf`.** Same content, copyable code, and it shows the instructor's build commands.

---

**Related:** [`README.md`](README.md) · [`reference_docs/known_issues.md`](reference_docs/known_issues.md) · [`reference_docs/code_separation.md`](reference_docs/code_separation.md) · [`reference_docs/code_commenting.md`](reference_docs/code_commenting.md) · [`reference_docs/report_guide.md`](reference_docs/report_guide.md) · [`reference_docs/lab_template.md`](reference_docs/lab_template.md)
