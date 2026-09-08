# Lab code vs. automation code

**Rule: `dsp26/` is the lab. `tools/` is how we drive it. Only `dsp26/` is ever submitted.**

This boundary exists for two reasons — one practical, one about honesty — and they point the same way.

---

## The two kinds of code

| | **Lab code** | **Automation code** |
| --- | --- | --- |
| Lives in | `dsp26/src/dsp26/` | `tools/` |
| Submitted? | **Yes** | **Never** |
| Written by | the student, following the handout | us, to drive and check the lab |
| Must run | standalone, on a clean machine, with only `uv sync` | only here |
| May depend on | the handout and the course's own package | anything |
| Reads like | a student's lab solution | a build script |

### Lab code must be standalone

`dsp26` has to work for someone who clones it, runs `uv sync`, and runs the CLI. **No import from `tools/`, no path assumption about this repo, no dependency on any wrapper.** If lab code stops working when `tools/` is deleted, the boundary has been crossed.

A TA opening the submission should see a package that does what the handout asked, in the shape the handout described.

### Automation code may do anything

`tools/` exists so we do not re-type the same commands, and so mistakes get caught mechanically. It runs the lab code from the outside, the same way a person would — **it calls the CLI, it does not reach inside the package.**

---

## Why this matters beyond tidiness

Submitting the automation alongside the lab would misrepresent the work. The lab is meant to demonstrate that the student can write and run the code; a harness that regenerates everything on demand is a *different* artifact, and shipping the two together invites a reader to conclude the lab was produced by a script.

It also isn't what was asked for. The deliverable is the lab code plus a report. Extra tooling in the submission is noise at best.

**So: the automation is real, it is committed here, and it stays here.** It speeds up *our* loop — running headless, catching identical-output bugs, packaging a clean zip. What gets turned in is the lab, and the report describes what the student actually did, including problems hit and how they were resolved.

**None of this makes the tooling secret.** It lives in the repo in plain sight. It just isn't part of the coursework deliverable, the same way a Makefile you wrote for your own convenience isn't part of an essay.

---

## Where the line sits in practice

| Situation | Which side |
| --- | --- |
| A function the handout tells you to write | Lab code |
| A CLI command exposing that function | Lab code — the handout's whole design is one CLI |
| Setting `MPLBACKEND=Agg` so a headless run saves instead of blocking | Automation |
| Checking two saved figures aren't accidentally identical | Automation |
| Fixing a genuine bug in handout code | **Lab code**, with a `DEVIATION FROM HANDOUT:` comment |
| Adding PNG output next to SVG | **Lab code** — it changes the deliverable, so mark it as a deviation |
| Building the submission zip | Automation |
| Verifying every file the handout references was downloaded | Automation |
| Checking a report `.tex` compiles | Automation |
| The report `.tex` itself | Neither — a **deliverable**, written by the student |
| Comments explaining what the code does | **Lab code** — see [`code_commenting.md`](code_commenting.md) |
| A build instruction written into a report `.tex` | **Neither — it does not belong anywhere in a deliverable.** [KI-09](known_issues.md#ki-09--tooling-references-leaked-into-a-submitted-report) |
| Stripping those comments for submission | Automation — [`submission_requirements.md`](submission_requirements.md) |

The test: **would a student who did this lab by hand have written it?** If yes, it is lab code. If it only exists because we are driving the lab from a terminal, it is automation.

---

## Deviations from the handout

Sometimes handout code is wrong (see [`known_issues.md`](known_issues.md) KI-01). Fix it, but:

1. Keep the handout's structure — do not rewrite it in your own style.
2. Mark the change in the source:

   ```python
   # DEVIATION FROM HANDOUT: handout has `plt.figure(1)` here.
   # <what broke, and why this fixes it>
   ```

3. Log it in the lab README under **Deviations**.
4. If it could recur, add it to [`known_issues.md`](known_issues.md).

A marked, justified fix reads as engineering. An unexplained rewrite reads as not having followed the lab. **The comment is what makes the difference,** and it is also what you talk about in the report's Narrative section — problems hit and how they were resolved is a graded section.

---

## Tools

Run from `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`.

### Who runs what

**Every tool here is the agent's to run.** None of them needs a human, and none of them should ever
appear in a *Needs a human* list — if one does, the hand-off is wrong. The human's jobs — fetching from
Canvas, screenshots, the live demo, approving the report, uploading, and confirming what the lab wants
(H1–H6 in [`lab_template.md`](lab_template.md)) — sit *around* the tools, not inside them.

| Step | Who | Why |
| --- | --- | --- |
| `check_inputs.py`, `check_artifacts.py` | **LLM** | plain commands |
| `strip_comments.py`, `make_submission.sh` | **LLM** | plain commands; the printed manifest is the check |
| `render_reports.sh` | **LLM** | tectonic is installed and needs no display |
| Generating figures (`MPLBACKEND=Agg`) | **LLM** | headless save is a supported path, not a workaround |
| Converting a supplied audio file to the shape a lab wants | **LLM** | [KI-16](known_issues.md#ki-16--no-ffmpeg-on-this-machine-yt-dlp--x-fails-convert-with-librosa) |
| Setting `myID` | **LLM** | the value is on file — [`submission_requirements.md`](submission_requirements.md#student-id) |
| Downloading from Canvas | **HUMAN** | `Credentialed` |
| Screenshotting a running window | **HUMAN** | `Capture` — but only the capture; the figures are already generated |
| Live demo | **HUMAN** | `Policy` |
| Uploading to Canvas | **HUMAN** | `Credentialed` |

Full reason vocabulary and the block format each human row expands into:
[`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md), with the
recurring blocks pre-written in [`lab_template.md`](lab_template.md).

### `tools/check_artifacts.py`

Verifies a lab's output files are present, non-trivial, and **actually distinct**. Catches the KI-01 class of bug, where a figure-numbering mistake makes two saved figures the same image.

```sh
uv run --project dsp26 python tools/check_artifacts.py lab00/figs
```

Exit code 0 if clean, 1 if anything is suspicious.

### `tools/check_inputs.py`

Scans every markdown file for links to files that are not on disk, and separates *never downloaded* (needs a human on Canvas) from *moved* (stale link, harmless). **Run before starting a lab.**

⚠ **A clean result does not mean nothing is missing.** It reads *Markdown links* only; a path built in Python is invisible to it — [KI-12](known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python). Grep the lab code for hard-coded paths as well, and put anything you find in the lab README's **Inputs** table by hand with its own *Blocks* entry.

```sh
uv run --project dsp26 python tools/check_inputs.py         # whole tree
uv run --project dsp26 python tools/check_inputs.py lab01   # one folder
```

Exit code 1 only when something is genuinely absent.

⚠ **The folder form produces false alarms, so never use it as a human's proof that a download
landed.** With a folder argument the tool builds its "what is on disk" index from that folder alone,
so a file living elsewhere in the repo is reported as never downloaded. Verified 2026-09-08:
`check_inputs.py lab00` reports `py-pkg-1c-uv-cs.md` as `NOT ON DISK` and exits 1, while the whole-tree
run correctly files it under `PRESENT ELSEWHERE` and exits 0. To prove a specific file arrived, check
that file: `ls -l <absolute path>`.

### `tools/make_submission.sh`

Builds a zip containing **only** lab code — `dsp26/` without `.venv/`, caches, or `tools/`.

```sh
tools/make_submission.sh lab00 nelson-gatlin
# -> lab00/dsp26-lab00-nelson-gatlin.zip
```

It prints what it included. **Check that list before submitting.**

### `tools/strip_comments.py`

Removes comments and docstrings for submission, keeping `DEVIATION FROM HANDOUT` blocks. Uses `tokenize`, not regex, so a `#` inside a string is safe. Verifies its own output by AST comparison and refuses to emit code it changed. Normally invoked via `make_submission.sh` rather than directly — see [`submission_requirements.md`](submission_requirements.md).

**It is not executable and not on `PATH`.** To run it by hand, go through the project interpreter;
`tools/strip_comments.py <file>` on its own gives `Permission denied`:

```sh
uv run --project dsp26 python tools/strip_comments.py <file>.py
```

Same for `check_inputs.py`, `check_artifacts.py` and `make_test_audio.py`. The two `.sh` scripts *are*
executable and run directly.

### `tools/render_reports.sh`

**The only script that renders PDFs.** `make_submission.sh --figures` delegates to it, so there is one place rendering behaviour lives.

```sh
tools/render_reports.sh          # all labs
tools/render_reports.sh lab00    # one
```

PDFs are **kept** and gitignored (`report*.pdf`). Fails if a referenced figure is missing — regenerate figures first.

### Headless run

Not worth a script — one environment variable:

```sh
cd dsp26 && MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

---

**Related:** [`../prompt.md`](../prompt.md) · [`known_issues.md`](known_issues.md) · [`report_guide.md`](report_guide.md)
