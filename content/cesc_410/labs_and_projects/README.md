# CESC 410L — Labs and Projects

DSP lab work for Fall 2026. Instructor **Dr. Jianhua Liu**; labs taught by TAs.

Claude's entry point is [`prompt.md`](prompt.md). This file is orientation for a person.

---

## Layout

```
labs_and_projects/
├── prompt.md              # "get lab N done" — Claude reads this first
├── README.md              # you are here
├── .gitignore             # .venv, __pycache__, caches
├── reference_docs/        # course-wide, not lab-specific
│   ├── py-pkg-1c-uv-cs.md # instructor's uv cheatsheet
│   ├── known_issues.md    # recurring traps — check before debugging
│   ├── code_separation.md # what gets submitted and what does not
│   ├── code_commenting.md # how source files explain themselves
│   ├── submission_requirements.md  # WHAT EACH LAB ACTUALLY WANTS (open)
│   ├── report_guide.md    # lab report structure
│   ├── report_template.tex# Overleaf-ready report skeleton
│   ├── lab_template.md    # copy this to start a lab README
│   ├── py-pkg-1c-uv-cs.pdf# same document as the .md; prefer the .md
│   └── overleaf/          # flattened copies for pasting — GITIGNORED, never packaged (KI-11)
├── tools/                 # AUTOMATION — never submitted
│   ├── check_inputs.py    # finds referenced-but-missing files
│   ├── check_artifacts.py # catches identical/empty output files
│   ├── render_reports.sh  # THE renderer — .tex -> PDF (kept, gitignored)
│   ├── strip_comments.py  # comment/docstring removal (tokenize-based)
│   ├── make_test_audio.py # synthesises a music-shaped stand-in WAV
│   └── make_submission.sh # strips, headers, zips lab code only
├── dsp26/                 # LAB CODE — shared by every lab, submitted
│   ├── pyproject.toml
│   ├── uv.lock            # committed
│   ├── .venv/             # ~250 MB, gitignored
│   └── src/dsp26/
│   │   ├── __init__.py
│   │   ├── app_cli.py     # one Typer command per lab
│   │   ├── lab0_sinusoids/
│   │   └── lab1_audio_sig/
│   └── audio_files/       # handout-default inputs loaded from Python, NOT
│                          #   Markdown — invisible to check_inputs.py (KI-12)
├── lab00/                 # one folder per lab: docs + artifacts
│   ├── README.md          # reproduction log
│   ├── report.tex         # submission report (Overleaf-ready)
│   ├── report.pdf         # built — kept, gitignored
│   ├── figs/              # output figures — GITIGNORED, regenerated
│   └── dsp-ba--lab0-*.md/pdf
└── lab01/                 # same shape; also out/ (text captures) and
                           #   figs_expt/ (the experimental-input figure set)
```

### Three kinds of content

| | Where | Submitted |
| --- | --- | --- |
| **Lab code** — what the handout asks you to write | `dsp26/src/dsp26/` | **yes** |
| **Automation** — how we drive and check it | `tools/` | **never** |
| **Documentation and artifacts** | `labNN/` | report + figures |

`dsp26/` must work standalone with `tools/` deleted. Anything that exists only because we run the lab from a terminal is automation, not lab code. Full rule and rationale: [`reference_docs/code_separation.md`](reference_docs/code_separation.md).

### Why code and docs are split

Each lab gets its own `labNN/` folder, but the **code** for every lab lives in one shared package under `dsp26/src/dsp26/`.

That is the handout's design, not a choice we made: the instructor wants *all* lab and class projects in a single virtual environment, exposed through one CLI app, so you never activate a venv to run anything. Later labs are expected to import from earlier ones.

The consequence is that `labNN/` holds **documentation and artifacts**, while the code it describes sits elsewhere. That is a little unusual, and it is deliberate — in this course the code *is* the subject being studied, so it earns commentary that would be redundant in a normal project. Each lab README names the exact source files it covers.

---

## Environment

`uv` manages Python. It is not in the system package manager; install with:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

It lands in `~/.local/bin`. Add that to `PATH` if your shell doesn't already:

```sh
export PATH="$HOME/.local/bin:$PATH"
```

Then:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26
uv sync                 # create .venv and install everything from uv.lock
uv run dsp26 --help     # list every lab command
```

`uv run dsp26 --help` prints a `Commands` panel — today `plot-sinusoids-td-fd` and `play-plot-audio`,
each with a description. From anywhere else, the same thing is
`uv run --project dsp26 dsp26 --help`; both forms are used in these docs and both work.

`uv run` resolves the environment itself — **you never activate the venv.**

| | |
| --- | --- |
| Python | 3.12 (two behind current, per the handout, for dependency stability) |
| Runtime deps | `typer`, `matplotlib`, `numpy`, `scipy` |
| Dev deps | `pytest` |
| Installed as | editable — edit `src/` and rerun, no reinstall |

**LaTeX:** `tectonic` is installed (0.16.9) — self-contained, no TeX Live, no root. **`tools/render_reports.sh` is the only script that renders**; `make_submission.sh --figures` calls it. PDFs are kept and gitignored, so the built report is always on hand without entering the repo. `pandoc` **is** installed too (2.9.2.1, `/usr/bin/pandoc`, a system package since 2022) — an earlier note here said it was not, which was wrong; verified 2026-09-08. Nothing needs installing to write Markdown and convert, but `.tex` is still preferred because it skips the conversion step.

**All `*.zip` and all `report*.pdf` are gitignored** — every one is a build product. The `report*.pdf` rule is deliberately narrow so it can never match an instructor handout.

**Generated figures are gitignored.** `figs/` is regenerated by one command and would otherwise add roughly half a megabyte per lab per run for simple plots, and several megabytes once spectrograms are involved (Lab 1's set is ~5 MB). Regeneration is deterministic because `myID` is committed and `uv.lock` pins matplotlib. To keep a specific set — the exact figures you submitted — `git add -f labNN/figs/`.

> ⚠ **The rule is the literal directory name `figs/`, not "figures".** `.gitignore` ignores `figs/`
> (line 58) and `overleaf/` (line 85); **`lab01/figs_expt/` matches neither and is currently NOT
> ignored** — that is
> ~5 MB of regenerable PNG/SVG a commit would pick up. Verified 2026-09-08 with
> `git check-ignore -v lab01/figs_expt/lab1_audio_fig1_waveform_full.png` (no match). **Any new
> figure directory needs its own line**; for this one, add `figs_expt/` next to `figs/` in
> `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/.gitignore`, then confirm with the
> same `git check-ignore -v` command — it should print the matching rule instead of nothing. Left for
> a person because editing `.gitignore` changes what future commits carry, and git here is human-only.

**Headless note — read this carefully, the obvious version of it is wrong.** This machine **does** have
a display (`DISPLAY=:1`, X11, 1920×1080). What it does not have is anyone watching it. So:

- Unattended runs set `MPLBACKEND=Agg`. `plt.show()` then does nothing and warns, and each command's
  `--folder-name` option saves the figures instead ([KI-02](reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless)).
- **Never gate window-opening code on `DISPLAY`.** It is set, so the guard passes and an unattended run
  hangs on a window nobody will click — this happened, and cost a run that produced no output and never
  exited ([KI-13](reference_docs/known_issues.md#ki-13--a-gui-window-opened-during-an-unattended-run-and-blocked-it-forever)).
  Gate on `MPLBACKEND`, which is this project's "no windows" signal.
- Because the display is real, **screenshots can be taken here** — no laptop needed. See the table below.

### What this machine actually has

Verified 2026-09-08. Check here before telling a human to install something or go and find a GUI.

| Need | Have | Command |
| --- | --- | --- |
| Screenshot | ImageMagick `import` 6.9.11-60. **No** `gnome-screenshot`, `scrot`, `flameshot`, `spectacle` | `import -window root out.png`, or `import out.png` to click a window |
| Record audio — **mic** | `arecord`; mic is `card 1: PCH [HDA Intel PCH]`, currently at 24% input volume | `arecord -f S16_LE -r 16000 -c 1 -d 10 out.wav` |
| Record audio — **what the speakers play** | the PulseAudio `...analog-stereo.monitor` source. **`-D pulse` alone records the MIC** — the default source is the input device, so the override is not optional | `PULSE_SOURCE=alsa_output.pci-0000_00_1f.3.analog-stereo.monitor arecord -D pulse -f S16_LE -r 16000 -c 1 -d 10 out.wav` |
| Convert audio | `librosa` + `soundfile` (libsndfile 1.2.2 — reads MP3, OGG, FLAC, WAV). **No `ffmpeg`, no `sox`** | [KI-16](reference_docs/known_issues.md#ki-16--no-ffmpeg-on-this-machine-yt-dlp--x-fails-convert-with-librosa) |
| Download media | `yt-dlp` 2026.06.09. Its `-x` needs `ffmpeg`, so **it cannot extract audio here** — download, then convert as above | — |
| Render LaTeX | `tectonic` 0.16.9 | `tools/render_reports.sh labNN` |
| Convert Markdown | `pandoc` 2.9.2.1 | — |
| Window ids | `xwininfo`, `xrandr`. **No** `xdotool`, `wmctrl` | — |

**When an instruction would say "install X" or "use the screenshot tool", check this table first.** Most
of the time the capability is already here under a different name, and the human step disappears.

---

## Working a lab

Who acts is marked on every step. **Almost all of it is the agent's** — the human appears in two rows
of the table below but **five times** in practice, because step 10 bundles four separate jobs. Each of
the five, plus a sixth (confirming what the lab submits), is written out as a ready-made block in
[`reference_docs/lab_template.md`](reference_docs/lab_template.md) § *Needs a human* — H1 fetch,
H2 screenshots, H3 demo, H4 approve report, H5 upload, H6 confirm requirements. **Copy the block; do
not re-derive it.**

| # | Who | Step |
| --- | --- | --- |
| 1 | **HUMAN** | Download the handout from Canvas and drop it into `labNN/` (`Credentialed` — a login the agent has no session for) |
| 2 | **LLM** | Check nothing is missing: `uv run --project dsp26 python tools/check_inputs.py` — then read the handout's *code* for hard-coded paths, which the checker cannot see ([KI-12](reference_docs/known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python)) |
| 3 | **LLM** | Follow [`prompt.md`](prompt.md) |
| 4 | **LLM** | Code into `dsp26/src/dsp26/labN_<topic>/`, with a command added to `app_cli.py` |
| 5 | **LLM** | Artifacts into `labNN/figs/` — both PNG and SVG; **use PNG in the report** |
| 6 | **LLM** | Verify: `uv run --project dsp26 python tools/check_artifacts.py labNN/figs` |
| 7 | **LLM** | Fill in `labNN/README.md` from [`reference_docs/lab_template.md`](reference_docs/lab_template.md) as you go, not afterwards |
| 8 | **LLM** | Package: `tools/make_submission.sh labNN lastname-firstname` — strips comments, adds a header, zips. Check the printed file list |
| 9 | **LLM** | Draft the report from [`reference_docs/report_template.tex`](reference_docs/report_template.tex); check it builds with `tools/render_reports.sh labNN`. See [`reference_docs/report_guide.md`](reference_docs/report_guide.md) |
| 10 | **HUMAN** | Screenshots of the running program (`Capture`), the live demo (`Policy`), approving the report (`Judgment`), and the Canvas upload (`Credentialed`) |

**Whatever the agent hands back must state WHERE, WHAT, VERIFY, IF ABSENT and BLOCKS** — the standard is
[`docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md), and
it exists because this repo once shipped *"fetch the .wav from Canvas"* and cost a wasted hunt
([KI-15](reference_docs/known_issues.md#ki-15--a-human-task-that-names-no-place-costs-a-round-trip)).

**The ERAU ID is already set — this is no longer a human step.** Labs seed an RNG with the last four
digits of the student ID; handouts ship the placeholder `1234`, and the real value is on file
(`2636127` → `myID = 6127`, [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md#student-id)).
The agent sets it and checks it:

```sh
grep -rn "myID" dsp26/src/          # currently: lab0_sinusoids/recipes.py:27, myID = 6127
```

Leaving it at `1234` means submitting the instructor's example output instead of your own. Expect a new
lab to add its own `myID` line. **Ask a human only if a lab wants a *different* personal field** — and
then ask for that field by name, not for "your details".

---

## Course facts that drive the workflow

| | |
| --- | --- |
| Meetings | Sec 1 Tue, Sec 2 Fri, 5:15–8:15 pm, LB 373 |
| Grading | Weekly labs 60 pts + final lab exam 40 pts |
| **Live demo** | **By the next lab section**, in person, to the TA. The report is not graded until the TA sees the demo. **Early checkout is allowed** — demo it and leave |
| **Canvas deadline** | **1 week after a lab is assigned**, for the write-up/deliverables. **A separate rule from the demo deadline**, and on a lab that spans a no-lab week the two dates differ |
| Submission | Report + code for the *previous* lab. *What* each lab wants is still unconfirmed — [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md) |
| Late policy | **No late reports. Missing report = 0. No resubmission.** |
| Missed lab | **Attend the other section's meeting** — the TA invites it, for extra help or to demo. Failing that, a video demo before the meeting; **two allowed all semester** |
| Teams | Two students; rebuilt every two labs from Lab 3. One submission per team — **except ABET-artifact labs, where everyone submits independently** |
| **TA name** | **Ryle** (signs announcements "- Ryle"; Windows user `rylet`) |
| **TA contact** | **Discord `ryletraub_30890`** — the TA's own suggestion — or Canvas **Inbox**. ⚠ **Email is offered but no address is given**; ask at a meeting rather than constructing one |
| **Where lab material is posted** | Canvas **Modules** tab, on each lab's own page. The TA: *"I will copy over and post the Lab PDF directly inside the Modules tab under the respective lab pages"* |
| **Supplemental docs** | **Expect one per lab from Lab 1 on** — *"a reference document addressing common edge cases, setup quirks, or potential issues"*. **Check Announcements before starting a lab** |
| **Canvas course URL** | **NOT RECORDED — fill this in.** Every "fetch it from Canvas" instruction is vague until it is |
| **Canvas module names** | **NOT RECORDED.** The *tab* is known (Modules) and each lab has its own page there, but the exact titles are not recorded |

**Source for the TA rows and the two deadline rows:** a Canvas announcement, *"Lab 1 and Future
Labs"*, retrieved 2026-09-08 and transcribed at
[`lab01/ta_announcement_lab1_and_future_labs.md`](lab01/ta_announcement_lab1_and_future_labs.md)
(saved page: [`lab01/ta_announcement_lab1_and_future_labs.html`](lab01/ta_announcement_lab1_and_future_labs.html)).

> **Two blanks left, and they are still the highest-value thing a human can add to this repo.** The TA
> rows above were blank until 2026-09-08 and their being blank is exactly why
> [`lab01/README.md`](lab01/README.md) had to hedge for a whole lab —
> [KI-15](reference_docs/known_issues.md#ki-15--a-human-task-that-names-no-place-costs-a-round-trip).
> The remaining two are the course URL and the module titles; filling them makes every future
> hand-off name a page instead of a category.

#### How to fill in the last two — three minutes, once · Why human: **Credentialed**

Neither is guessable from this machine; both live behind the Canvas login.

> **The third blank — TA name / contact — was filled on 2026-09-08** from the announcement
> *"Lab 1 and Future Labs"*, not from the People tab. Worth remembering: **course Announcements
> answered a question the People tab was supposed to.** If the two remaining rows resist the lookups
> below, read the announcements.

**WHERE.** Canvas, logged in as yourself, on the course the lab handouts are posted on. The repo's
homework notes call that the **CESC 510** site
([`../hw/reference_docs/submission.md`](../hw/reference_docs/submission.md)) and the handouts are
titled *"CESC 410/510"*, so start there; if your roster also shows a separate CESC 410 or 410L site,
check that too — **and record which one it actually is**, because that ambiguity is itself one of the
things these rows exist to kill.

**WHAT.** Two lookups, then one edit:

| # | Blank | Where it is on Canvas | What to copy |
| --- | --- | --- | --- |
| 1 | Course URL | Open the course from the **Dashboard** or **Courses** menu | The address bar, up to and including the course number — Canvas course URLs end `/courses/<NNNNNN>`. Copy it verbatim; **do not reconstruct the hostname from memory** |
| 2 | Module names | The course's **Modules** tab — the TA has confirmed each lab has its own page there | The module and page titles verbatim, at least the one holding each lab's handout (e.g. *"Lab 1 — Audio Signal"*) |

Then edit the two **NOT RECORDED** rows in the table above, in
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/README.md`, replacing the placeholder
text with what you copied.

**While you are in there — one optional extra.** If you get Ryle's email address at a meeting, add it
to the **TA contact** row. Right now that row says the address is not published, and every human block
in the repo that mentions email says so too; **nobody should be guessing an address from the Discord
handle.**

**VERIFY.** No table row in this file still says `NOT RECORDED`:

```sh
grep -c '^|.*NOT RECORDED' /home/devel/electrical_notes/content/cesc_410/labs_and_projects/README.md
```

Expected after the edit: `0`. Today — verified 2026-09-08 — it prints `2`, the two rows above. It
printed `3` before the TA rows were filled in. *(The pattern is anchored to `^|` on purpose, so it
matches only the table and not this instruction, which names the phrase too.)*

**IF IT IS NOT THERE.** A course whose **Modules** tab is hidden usually still exposes **Files** and
**Syllabus**; try those, then the course **Announcements**, which is where the TA has been posting.
If something genuinely is not published, record that fact in the row (*"not published on Canvas as of
&lt;date&gt;; ask at the meeting"*) rather than leaving it blank. **A recorded dead end is worth more
than an open question**, because it stops the next person repeating the hunt.

**BLOCKS.** *Nothing.* No lab waits on this. It makes every future Canvas hand-off name a page instead
of a category, which is why it is worth the three minutes.

### Schedule

| Lab | Sec 2 (Fri) | Sec 1 (Tue) |
| --- | --- | --- |
| 0 | 8/28 | 9/1 |
| 1 | 9/4 | 9/8 |
| 2 | 9/11 | 9/15 |
| 3 | 9/18 | 9/22 |
| 4 | 9/25 | 9/29 |
| 5 | 10/9 | 10/13 |
| 6 | 10/23 | 10/27 |
| 7 | 10/30 | 11/3 |
| 8 | 11/13 | 11/17 |
| Final | 11/20 | 12/1 |

Dates are when a lab **starts**, not when it is due. No lab: 10/2–10/6, 10/16–10/20, 11/6–11/10.

---

## Status

| Lab | Topic | Code | Artifacts | Report | Submitted |
| --- | --- | --- | --- | --- | --- |
| [00](lab00/README.md) | Getting started — sinusoids in TD/FD | ✅ | ✅ 4 PNGs + 4 SVGs | ✅ builds | ⬜ needs live demo |
| [01](lab01/README.md) | Audio signal — waveform, spectra, player | ✅ | ✅ 5 figs, plus an experimental set in `figs_expt/` | ❌ **does not render — [KI-17](reference_docs/known_issues.md#ki-17--a-report-can-reference-a-figure-that-moved-to-a-sibling-folder-render_reportssh-blames-the-wrong-thing)** | ⬜ see `lab01/README.md` § *Needs a human* |

`lab01/report.pdf` on disk is a **stale build** from before the experimental figure moved out of
`figs/` — it renders no longer. Fix it before H4/H5; KI-17 has both one-line options.

**Read the lab's own README before acting on this row** — it carries the per-lab *Needs a human*
blocks and any open substitutions. Lab 1's inputs are both real and both closed as of 2026-09-08: the
TA's supplied `.wav` for the default figures, and a clip cut from an operator-supplied source for the
experimental task. `lab01/test_tone.wav` is retained only as a no-audio fallback and feeds no artifact.

**When each lab is due is now known; *what* it wants still is not.** The TA's announcement fixes the
two deadlines — Canvas deliverable **1 week after the lab is assigned**, in-person demo **by the next
lab section** (both in *Course facts* above). It says nothing about which of figures/code/report a
given lab expects. **Lab 0 submits four PNGs only** — the handout is explicit that the figures are the
submission. From Lab 1 on it is still unconfirmed (course info says report + code generally). Track it
in [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md), which also
records the student ID and the decision that **publishing/git concerns do not apply to this project.**

### Open across the course · `py-pkg-1c-uv-qg.md` · Why human: **Credentialed**

The instructor's uv **quick guide**. Referenced by the cheatsheet we do have, never downloaded.

**Already tried — do not repeat.**

```sh
find /home/devel -iname '*uv-qg*'          # -> nothing, anywhere on this machine
grep -n "uv-qg" reference_docs/py-pkg-1c-uv-cs.md
```

The cheatsheet names it exactly twice: line 3, *"This is the cheatsheet for using uv. The quick guide
version is at py-pkg-1c-uv-qg"*, and line 384, pointing at its **Installing a local app** section. It
never says where to download it from.

**WHERE.** Wherever `py-pkg-1c-uv-cs` came from — they are a pair, same four-character document code.
That download is still on disk: `/home/devel/Downloads/py-pkg-1c-uv-cs.pdf` and `.md`, both dated
**2026-09-01 16:37**. Go back to that page on Canvas and look for the `-qg` sibling next to the `-cs`
file. If the page is gone from your history, check the course **Files** area and the **Lab 0** module.

**WHAT.**

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/py-pkg-1c-uv-qg.md` | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/reference_docs/py-pkg-1c-uv-qg.md` |
| `/home/devel/Downloads/py-pkg-1c-uv-qg.pdf` *(if posted)* | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/reference_docs/py-pkg-1c-uv-qg.pdf` |

`reference_docs/` already exists — no `mkdir` needed. Prefer the `.md`; it is the source and has copyable code.

**VERIFY.** From `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
uv run --project dsp26 python tools/check_inputs.py
```

Expected once it lands: the `NOT ON DISK` section **disappears entirely** and the command **exits 0**
(`echo $?`). Today — re-verified 2026-09-08 — it exits **1** and prints exactly one entry there:

```
NOT ON DISK -- needs downloading from Canvas (human):

  py-pkg-1c-uv-qg.md
      referenced by reference_docs/py-pkg-1c-uv-cs.md
```

**A second section, `PRESENT ELSEWHERE`, will still be printed and that is fine** — it lists
`py-pkg-1c-uv-cs.md`, a stale link inside the Lab 0 handout pointing at a file we moved into
`reference_docs/`. It does not affect the exit code and it is not something to fix. **Exit 0 is the
pass; `PRESENT ELSEWHERE` alone still exits 0.**

**IF IT IS NOT THERE.** It may simply never have been posted — the cheatsheet is a standalone document
and the labs have not needed the quick guide once. Ask the TA, quoting the filename, or **leave it
open**: this is the correct outcome, not a failure.

**BLOCKS.** *Nothing.* Every lab so far has run without it. It is a nice-to-have reference; it is on
this list only so that `check_inputs.py` exiting 1 is explained rather than mysterious.

---

## Relationship to CEC 320

Same instructor, and the document toolchain is identical — pandoc with `eagle.tex`, `select-blocks.lua`, four-character document codes (`dsp-ba`, `py-pkg-1c`, matching CEC 320's `de5d`, `ca4b`). The handout `.md` files carry the build command in a comment block at the top.

What carried over from [`../../cec_320/labs_and_projects/`](../../cec_320/labs_and_projects/): the per-lab folder pattern, a known-issues file checked before debugging, an LLM entry-point prompt, and tracking artifacts as first-class deliverables. What did not: everything CubeIDE, STM32 and Renode. This course is Python.

---

**Related:** [`prompt.md`](prompt.md) · [`reference_docs/submission_requirements.md`](reference_docs/submission_requirements.md) · [`reference_docs/code_separation.md`](reference_docs/code_separation.md) · [`reference_docs/known_issues.md`](reference_docs/known_issues.md) · [`reference_docs/report_guide.md`](reference_docs/report_guide.md)
