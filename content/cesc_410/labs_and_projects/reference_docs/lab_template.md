# Lab NN — <title>

<!--
Copy to labNN/README.md and fill in as you work, not afterwards.

This is a REPRODUCTION LOG. Someone should redo the lab from this file without
opening the handout. Commands verbatim, in order, with what they printed.

The report is a different document -- see reference_docs/report_guide.md.
Delete these comments.
-->

**Handout:** [`<file>.md`](<file>.md) · **Started:** YYYY-MM-DD · **Status:** in progress / done / submitted

**Goal:** one or two sentences.

---

## Inputs

Every file the handout names or links to. **Check this before starting** — a missing starter zip or dataset is the most common reason a lab stalls, and only a human can fetch it from Canvas.

Each missing input gets a row in **Needs a human** below, and the *Blocks* column here must match what that block says. A missing input with no stated consequence is a defect — see [`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md) Rule 3.

| File | Purpose | Status | If missing, blocks |
| --- | --- | --- | --- |
| `<name>.md` / `.pdf` | handout | ✅ present | — |
| `<name>.zip` | starter code | ❌ **missing — see H1** | the whole lab / one figure / nothing |

⚠ **Do not trust a clean `check_inputs.py` on its own.** It scans *Markdown links*; a path built in Python (`project_root / "audio_files" / "x.wav"`) is structurally invisible to it — [KI-12](../reference_docs/known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python). Read the handout's code for hard-coded paths and add them to this table by hand. Run from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
grep -rnE '"[^"]*\.(wav|csv|npz|zip|mat)"' dsp26/src/
```

---

## Code

Lab code lives in the shared package, not here — see [`../README.md`](../README.md#why-code-and-docs-are-split).

| File | What it does |
| --- | --- |
| `dsp26/src/dsp26/labN_<topic>/<file>.py` | … |
| `dsp26/src/dsp26/app_cli.py` | adds the `<command-name>` command |

---

## Reproduce

Every command, in order, exactly as run. **Every one starts from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`** unless a `cd` says otherwise —
say so here too, so nobody has to guess a working directory.

```sh
export PATH="$HOME/.local/bin:$PATH"    # if uv is not already on PATH
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26
uv sync
```

```sh
# headless: plt.show() is a no-op, so save instead
MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

Output:

```
<paste actual output>
```

Verify:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 python tools/check_artifacts.py labNN/figs
```

Expected: a file listing, then `OK    artifacts present, non-trivial, and distinct` (exit 0).

---

## Artifacts

`figs/` is gitignored — regenerate with the command above.

| # | File | Shows |
| --- | --- | --- |
| 1 | `figs/<name>.png` | … |

---

## Deviations from the handout

Anything changed from the handout code, and why. Each one is also marked in the source with a `DEVIATION FROM HANDOUT:` comment. **This section feeds the report's Narrative — a graded section.** If it could recur, add it to [`../reference_docs/known_issues.md`](../reference_docs/known_issues.md).

| # | Change | Why |
| --- | --- | --- |
| 1 | … | … |

*None* — if the handout code worked as written.

---

## Handout questions

Handouts bury questions between code blocks and they are graded. Collect them while reading.

1. **Q:** …
   **A:** …

---

## Needs a human

<!--
=========================== HOW TO FILL THIS IN ============================
STANDARD: ../../../../docs/directives/human-task-instructions.md

Every block below states all FIVE elements. A block missing one is not ready
to hand over:

  WHERE      exactly where to go. A named app, page or absolute path.
             "Canvas" is a category, not a place. Name the module.
  WHAT       exactly what to do there. Commands, clicks, or a
             Source (FROM) -> Destination (TO) table. Never a bare list.
  VERIFY     a command with its expected output, or an observable state.
             Not "check it worked."
  IF ABSENT  what to do when it is not there. At least one next step, then
             a named person to ask. This is the element that actually fires.
  BLOCKS     what stays stuck until this is done -- AND what does not.
             Stated per task. A footnote at the bottom is attached to nothing.

Before writing any block, do the human's homework and show it (Rule 4):
search for the file, read the handout for where it should come from, look for
a substitute, and say what the filename IS if that is knowable.

AUTOMATABLE is the default. HUMAN-REQUIRED needs one of six reasons:
GUI-only / Hardware / Credentialed / Capture / Judgment / Policy.
"It's fiddly" is not a reason. Split a task at the real boundary before
handing the whole thing over -- generating figures is automatable even when
screenshotting the windows is not (KI-02).

Delete the blocks this lab does not need. Keep every element of the ones you
keep. Paths ABSOLUTE, from /. Replace `labNN` and `<command>` throughout.
============================================================================
-->

**Every row expands into a block below. Read the block before acting on the row.**

| # | Task | Why human | Blocks | Status |
| --- | --- | --- | --- | --- |
| H1 | Fetch `<missing input>` | Credentialed | *(name it — or "nothing")* | ⬜ |
| H2 | Screenshots of the GUI windows | Capture | the report's Artifacts section | ⬜ |
| H3 | Live demo — **to Ryle, in person, by the next lab section** | Policy | grading of the report | ⬜ |
| H4 | Approve / finish the report | Judgment | submission | ⬜ |
| H5 | Upload to Canvas — **due 1 week after this lab was assigned** | Credentialed | the grade | ⬜ |
| H6 | Confirm what this lab must submit | Judgment | what H5 uploads | ⬜ |

Three more blocks exist and are **not** copied in by default, because most labs do not need them.
Copy them from [`../prompt.md`](../prompt.md#human-only) when they apply, and add the row here:

| # | Task | Why human | Copy from |
| --- | --- | --- | --- |
| H7 | Team membership for this lab | Policy | [`../prompt.md`](../prompt.md#h7--team-membership-for-this-lab--why-human-policy) — re-confirm at Labs 3, 5, 7 |
| H8 | Judging whether a deviation is acceptable | Judgment | [`../prompt.md`](../prompt.md#h8--judging-whether-a-deviation-is-acceptable--why-human-judgment) — add a row whenever *Deviations* above is not empty |
| H9 | Supply a self-made input (recording, photo, measurement) | Hardware | [`../prompt.md`](../prompt.md#h9--supply-a-self-made-input--why-human-hardware) — the human gives you the raw file; **you** shape it |

**Not on this list, and do not put it back:** setting the ERAU ID. The value is on file — `6127`,
[`submission_requirements.md`](../reference_docs/submission_requirements.md#student-id) — so the agent
sets it. Add a row only if a lab introduces a *second* personal field, and then name that field.

**Nothing that a tool can do belongs here.** Generating figures, converting audio, rendering the report
and building the zip are all agent work — [`code_separation.md`](../reference_docs/code_separation.md#who-runs-what)
lists who runs what. If a row here maps to a command, delete the row and run the command.

---

### H1 · Fetch `<missing input>` · Why human: **Credentialed** (Canvas login)

**Already tried — do not repeat.** *(Fill this in with the commands actually run. If it is empty, the block is not ready.)*

```sh
find /home/devel -iname '<name>' 2>/dev/null        # -> not on this machine
grep -n '<name>' labNN/<handout>.md                 # -> named only inside code, line NNN
```

- What the handout says about where it comes from: *(quote it, or say "the handout never says")*.
- What the filename **looks like**, if that is knowable — e.g. `2086-149220-0033.wav` parses as a LibriSpeech utterance id (speaker 2086 / chapter 149220 / utterance 0033). One line, and it tells the human what to search for. ⚠ **Write it as a lead, never as an answer.** In Lab 1 the parse was right about the name and wrong about the file: the TA supplied their own clip under that name — [KI-19](known_issues.md#ki-19--a-filename-that-parses-as-a-public-dataset-id-is-not-proof-of-provenance).
- Substitute found on disk / generatable: *(name it, or "none")*.

**WHERE.** Canvas → **CESC 410L** → the **Lab NN** module — the same page `<handout>.pdf` came from. If that page has no attachment list, in order: the course-level **Files** area → the **Lab 0** module (shared assets are often posted once) → the **Announcements** tab.

> ⚠ **The Canvas course URL and the exact module titles are not recorded in this repo.** The *tab* is known — the TA posts each lab's material under **Modules**, on that lab's own page — but not the titles, so this WHERE is as specific as it can currently be made. **You are already logged in — spend three extra minutes and close the gap permanently:** [`../README.md`](../README.md#how-to-fill-in-the-last-two--three-minutes-once--why-human-credentialed) § *How to fill in the last two* lists where each blank lives and the one `grep` that says you are done. Every later block gets specific for free.

**WHAT.**

```sh
mkdir -p /home/devel/electrical_notes/content/cesc_410/labs_and_projects/<dest folder>
```

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/Downloads/<name>` | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/<dest folder>/<name>` |

`/home/devel/Downloads/` is where course downloads have actually landed on this machine — the Lab 1
handout and the instructor's uv cheatsheet are both still sitting there. Say the path; do not write
"wherever the browser put it".

The destination folder may not exist. **The `mkdir -p` is part of this step, not a suggestion.**

**VERIFY.** Three checks, in this order. Run from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`.

**1 — the file is where it belongs.** This is the check that actually proves the fetch worked:

```sh
ls -l /home/devel/electrical_notes/content/cesc_410/labs_and_projects/<dest folder>/<name>
```

Expected: one line, non-zero size. `No such file or directory` means the copy did not happen — most
often because the download landed under a browser-mangled name (`file (1).wav`, `file.wav.part`);
`ls -lt /home/devel/Downloads/ | head` shows what actually arrived.

**2 — for a WAV, the shape the lab assumes.** A wrong sample rate means the wrong file:

```sh
uv run --project dsp26 python -c "import wave,sys; w=wave.open(sys.argv[1]); print(f'{w.getnchannels()} ch  {w.getframerate()} Hz  {w.getnframes()/w.getframerate():.2f} s')" /home/devel/electrical_notes/content/cesc_410/labs_and_projects/<dest folder>/<name>
```

Expected for a Lab 1-shaped clip: `1 ch  16000 Hz  7.43 s`. A `wave.Error` means it is not PCM WAV —
hand it over as-is and let the agent convert it
([KI-16](../reference_docs/known_issues.md#ki-16--no-ffmpeg-on-this-machine-yt-dlp--x-fails-convert-with-librosa)).

**3 — optional, and it does NOT replace check 1:**

```sh
uv run --project dsp26 python tools/check_inputs.py labNN
```

⚠ **Two ways this one lies, both verified on 2026-09-08 — do not treat its `OK` as proof:**

- It reads **Markdown links only**. A file the handout loads from Python
  (`project_root / "audio_files" / "x.wav"`) is invisible to it, so fetching that file changes its
  output not at all — [KI-12](../reference_docs/known_issues.md#ki-12--check_inputspy-cannot-see-an-input-referenced-from-python).
- Given a folder argument it only looks for files **inside that folder**, so a file that exists
  elsewhere in the repo is reported as missing. `... check_inputs.py lab00` prints
  `NOT ON DISK ... py-pkg-1c-uv-cs.md` even though that file is sitting in `reference_docs/`. **That
  is a false alarm, not your fetch failing.** Re-run with no argument to see the truth.

**IF IT IS NOT THERE.**

1. Course **Files** area, then the Lab 0 module, then Announcements.
2. **Ask the TA at the start of the next lab meeting, or message the instructor (Dr. Jianhua Liu),
   quoting the exact filename.** *(This is not a formality — for Lab 1 the file genuinely was not on
   Canvas on 2026-09-08. "Not posted yet" is a real answer.)*

   ⚠ **Name the TA: Ryle.** Reachable on **Discord `ryletraub_30890`**, by Canvas **Inbox**, or in
   person at either section's meeting — the TA invites students to attend the other section too.
   **Email is invited but no address is published; do not construct one.** Recorded in
   [`../README.md`](../README.md#course-facts-that-drive-the-workflow) § *Course facts*. If you do get
   an email address, write it into that row on the same trip.
3. **Fallback:** *(name the stand-in, say how it was generated, and say what it costs)*. A synthetic or substituted input is a **deviation** and must be stated in the report's Narrative — a graded section. Never a silent substitution.

**BLOCKS.** *(Be exact. "Only the run against the default input; the package code, the figures and the report are complete and do not wait on this" is a useful answer. "Everything" is also a useful answer. Silence is not.)*

---

### H2 · Screenshots of the GUI windows · Why human: **Capture**

Only the *capture* is human. **Generating the figures is not** — `MPLBACKEND=Agg` saves every one headlessly ([KI-02](../reference_docs/known_issues.md#ki-02--pltshow-does-nothing-headless)), and they are already in `labNN/figs/`. Hand over the screenshots, never the plotting.

**WHERE.** A desktop session with a display. This machine has one (`DISPLAY=:1`, 1920×1080, X11), so it can be done here — you do not need a laptop.

**WHAT — you need TWO terminals. Read this before you start, or you will get stuck.** Run the
command **without** `MPLBACKEND=Agg` so windows actually open — and that run then **blocks** until you
close them. Any lab that opens the audio player waits in `mainloop()` for you to click **Exit**
([KI-13](../reference_docs/known_issues.md#ki-13--a-gui-window-opened-during-an-unattended-run-and-blocked-it-forever)),
so the terminal you launched from is busy and cannot take the `import` command. That is expected
behaviour, not a hang.

**Terminal 1 — open the windows and leave it sitting there:**

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 dsp26 <command> --folder-name labNN
```

**Terminal 2 — capture, while the windows from Terminal 1 are still up.** ImageMagick's `import` is
installed (6.9.11-60); no screenshot GUI is (`gnome-screenshot`, `scrot`, `flameshot` and `spectacle`
are all absent, verified 2026-09-08), so do not go looking for a menu item:

```sh
mkdir -p /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/shots
import -window root /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/shots/NN_whole_screen.png
import              /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/shots/NN_one_window.png
```

**Then go back to Terminal 1 and close the windows** (click **Exit** on the player) so the run
finishes. If you only have one terminal, append `&` to the Terminal 1 command instead.

`import -window root` grabs the whole screen immediately. `import` with no `-window` turns the cursor into a crosshair and captures the **window you click** — better for a single figure.

Shots normally needed: `dsp26 --help`, each figure window, and any player/dialog the lab opens.

**Avoid dark backgrounds** — reports get printed, and the CEC 320 template asked for this explicitly ([`report_guide.md`](../reference_docs/report_guide.md#3-artifacts--code-snippets-and-screenshots)).

**VERIFY.**

```sh
ls -l /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/shots/
file  /home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/shots/*.png
```

Expected: `PNG image data, 1920 x 1080` (or the window's size), and **not** `1-bit grayscale` — that is what an empty desktop captures as, and it means you grabbed the screen before the window opened.

**IF IT DOES NOT WORK.** No window appears → check `MPLBACKEND` is unset (`echo $MPLBACKEND` should print nothing) and `echo $DISPLAY` prints `:1`. A run that produces no output *and never exits* is a blocked GUI window, not a slow computation — [KI-13](../reference_docs/known_issues.md#ki-13--a-gui-window-opened-during-an-unattended-run-and-blocked-it-forever). If the lab does not actually require screenshots (confirm via H6), skip this and say so here.

**BLOCKS.** The report's **Artifacts** section only. Code, figures and packaging do not wait on it.

---

### H3 · Live demo — by the next lab section · Why human: **Policy**

Course policy: the student shows their own working code to the TA. Nothing about it is automatable.

**WHEN.** **By the next lab section** — the TA's own wording, not "at the start of the meeting".
**Early checkout is allowed:** *"If you complete your lab before class, you are welcome to show up,
demo it to me, and leave early."* Lab NN's dates are in [`../README.md`](../README.md#schedule)
§ *Schedule*.

**WHO.** **Ryle** — in person, or Discord `ryletraub_30890` / Canvas **Inbox** to arrange it. The TA
also invites students to attend **the other section's** meeting, which is a second slot for both help
and a demo.

**WHERE.** LB 373. **Sec 1 Tue, Sec 2 Fri, 5:15–8:15 pm.**

**WHAT.** Have the code running before you walk in:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
uv run --project dsp26 dsp26 --help
uv run --project dsp26 dsp26 <command>          # no MPLBACKEND -- let the windows open
```

The second command **does not return until you close the windows it opens** — that is the demo, not a
hang ([KI-13](../reference_docs/known_issues.md#ki-13--a-gui-window-opened-during-an-unattended-run-and-blocked-it-forever)). Click **Exit** on the player when you are done.

**VERIFY.** Both commands run clean on this machine *before* the meeting, and `dsp26 --help` lists this lab's command — verified 2026-09-08: the help screen shows `plot-sinusoids-td-fd` and `play-plot-audio`, each with its description. Rehearse it — a demo that fails at the bench is the same as no demo.

**IF YOU CANNOT ATTEND.** Send a **video demo before the meeting**. **Two are allowed all semester** — spend them deliberately.

**BLOCKS.** Grading of the report. *"The report will not be assessed before the ATs can see your live demo of the lab."* The report can still be written and submitted first; it just is not read yet.

---

### H4 · Approve / finish the report · Why human: **Judgment**

The agent drafts it. The report is the student's account of their own work, and the Narrative is graded on the debugging story — only the student can say which parts are theirs.

**WHERE.** `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/report.tex`

**WHAT.** Read all four sections against [`report_guide.md`](../reference_docs/report_guide.md). Confirm the **Narrative** matches what actually happened, including every row of *Deviations from the handout* above. Then rebuild:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects
tools/render_reports.sh labNN
```

Expected: `labNN/report.tex   OK  -> labNN/report.pdf` then `All rendered. PDFs kept (gitignored).`

**VERIFY.** The PDF exists and opens, and every figure it references is present. Do **not** eyeball
the `.tex` for tooling references — run the same guard packaging runs, from
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
uv run --project dsp26 python tools/strip_comments.py labNN/report.tex -o /tmp/report-guardcheck.tex
uv run --project dsp26 python -c "
import sys; sys.path.insert(0,'tools')
from pathlib import Path
from strip_comments import find_tooling_refs
hits = list(find_tooling_refs(Path('/tmp/report-guardcheck.tex').read_text(errors='replace')))
print('\n'.join(f'line {ln}: {t.strip()[:80]}' for ln, t in hits) or 'clean -- nothing that would block packaging')
"
```

Expected: `clean -- nothing that would block packaging` — verified against `lab00/report.tex` and
`lab01/report.tex` on 2026-09-08. **The strip step is not optional:** packaging removes comment-only
`%` lines *before* guarding, so guarding the raw file flags the template's own `%` header and sends you
deleting something harmless. Anything the two-step check reports is a real line that will make
packaging refuse to build the zip
([KI-09](../reference_docs/known_issues.md#ki-09--tooling-references-leaked-into-a-submitted-report)) — delete it before H5.

**IF IT FAILS TO RENDER.** `Unable to load picture` means `figs/` is empty — it is gitignored. Regenerate first:

```sh
cd /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26
MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

**BLOCKS.** H5. Nothing else.

---

### H5 · Upload to Canvas — due 1 week after the lab is assigned · Why human: **Credentialed**

**WHEN.** *"Lab write-ups/deliverables are due on Canvas **1 week** after they are assigned."* Work the
date from [`../README.md`](../README.md#schedule) § *Schedule* — assigned date + 7 days. ⚠ **This is a
different rule from H3's demo deadline**, and on a lab spanning a no-lab week (10/2–10/6, 10/16–10/20,
11/6–11/10) the two dates are not the same day.

**WHERE.** Canvas → **the course site** → **Modules** → the **Lab NN** page, then the assignment.
The TA posts each lab's material on that lab's Modules page. *(Course URL and exact module titles not
recorded — see the warning in H1.)*

**WHAT.** Build the package first, then upload exactly what it printed. Run **only the mode this lab
wants** — H6 settles which; if H6 is unanswered, run both and upload both. From
`/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

```sh
tools/make_submission.sh labNN nelson-gatlin              # code
tools/make_submission.sh labNN nelson-gatlin --figures    # report + figures
```

Each command prints `Wrote <absolute path>` — that path is the file to upload. **The two modes write
differently-named zips, and it is easy to upload the wrong one:**

| Source (FROM) — produced by | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/dsp26-labNN-nelson-gatlin.zip` — the plain command (**code**) | the Canvas **Lab NN** assignment upload box |
| `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/labNN-figures-nelson-gatlin.zip` — the `--figures` command (**report `.pdf` + `.tex` + the PNGs**, no code) | same |
| `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/labNN/report.pdf` — rendered by `--figures`; upload it loose as well if the assignment wants the PDF visible without unzipping | same |

*(`--figures` already contains `report.pdf` inside the zip, so uploading the loose PDF too is
belt-and-braces, never wrong.)*

⚠ **`--figures` re-renders the report first and refuses to build the zip if it does not compile**
(`error: report failed to render -- fix it before packaging`). That is not an upload problem — go fix
the render, usually a figure the `.tex` names that is not in `labNN/figs/`
([KI-17](../reference_docs/known_issues.md#ki-17--a-report-can-reference-a-figure-that-moved-to-a-sibling-folder-render_reportssh-blames-the-wrong-thing)).
**An existing `report.pdf` on disk does not mean the source still builds** — it is gitignored and kept,
so it can be arbitrarily stale.

**VERIFY.** `make_submission.sh` prints its file list — **read it before uploading.** No `.venv`, no `tools/`, no `__pycache__`. Then, on Canvas, reopen the submission and confirm the attachment names match. Canvas shows a submission timestamp; check it is before **assigned date + 7 days**, not merely before the next meeting.

**IF THE ASSIGNMENT IS NOT THERE.** Check the course **Modules** and **Assignments** tabs, then message **Ryle the same day** — Discord `ryletraub_30890` or Canvas **Inbox**. Waiting for the next meeting is already too late.

**BLOCKS.** The grade. **Late is a zero. No resubmission.**

---

### H6 · Confirm what this lab must submit · Why human: **Judgment**

The course info and the handouts disagree, and only a TA can settle it — [`submission_requirements.md`](../reference_docs/submission_requirements.md).

**WHERE.** The TA, at the **start** of the lab meeting (the same slot as H3), or by Canvas message.

**WHAT.** Ask, in this order: figures / code / report — which of the three, and in what form (zip of the package, individual `.py`, or pasted into the report)? Then fill in this lab's row in the *Per-lab requirements* table in [`submission_requirements.md`](../reference_docs/submission_requirements.md#per-lab-requirements) and set *Confirmed with TA?* to ✅.

**VERIFY.** The row is filled in and marked confirmed, with the TA's wording quoted.

**IF YOU CANNOT ASK IN TIME.** Produce **everything** — figures, code zip and report — and submit all of it. Over-submitting has no stated penalty; under-submitting is a zero with no resubmission.

**BLOCKS.** Which command H5 runs. Nothing before that.

---

**BLOCKED / NOT BLOCKED — state it here explicitly.** *(e.g. "All code is written, runs clean, and every figure is generated and checked. Only H2 and H5 remain.")*

---

## Notes

Anything that would otherwise be lost — a surprise, a wrong turn, something to check next time.
