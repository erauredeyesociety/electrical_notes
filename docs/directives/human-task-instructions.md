# Directive — human-task instructions

**Applies to:** `cesc_410`, `cesc_470`, `cpsc_462`, and every course added after them — the same
doctrine boundary as [coursework-solutions.md](./coursework-solutions.md).
Older courses are not retrofitted ([scope-discipline.md](./scope-discipline.md)).

**Source, frozen:** everything below is distilled from `content/cec_320/labs_and_projects/`
— [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../../content/cec_320/labs_and_projects/LAB_PROJECT_ANALYSIS_PROCEDURE.md),
[known_base_projects.md](../../content/cec_320/labs_and_projects/known_base_projects.md),
[known_issues.md](../../content/cec_320/labs_and_projects/known_issues.md),
[nucleo32_pinout_reference.md](../../content/cec_320/labs_and_projects/nucleo32_pinout_reference.md),
[analysis_prompt.md](../../content/cec_320/labs_and_projects/analysis_prompt.md).
**Read them; never edit them.** CEC 320 is a completed course.

---

**WHEN** you write a line that starts "the human needs to…" → **DON'T** ship it until it names a
place, a check, a fallback, and what it blocks → **BECAUSE** this repo already shipped one that
didn't, and it cost the operator a failed hunt through Canvas and a round-trip to ask.

The standing expectation, in the operator's words: *"Claude gets everything done that it can without
the human involved … get as much done without the human as needed and just tell the human what they
are needed for."* **The human is the scarce resource.** A vague hand-off spends it twice — once on
the task, once on working out what the task was.

---

## The failure this exists to prevent

[`content/cesc_410/labs_and_projects/lab01/README.md`](../../content/cesc_410/labs_and_projects/lab01/README.md)
§ *Needs a human* shipped this row:

> **Fetch `2086-149220-0033.wav` from Canvas** into `dsp26/audio_files/` — the handout's default
> input, not downloadable from here

Nothing in it is false. It is still a defect. The audit:

| Missing | What the row said | What was needed |
| --- | --- | --- |
| **WHERE** | "from Canvas" | Canvas is an entire LMS. Which course, which module, which page? |
| **WHAT** | "into `dsp26/audio_files/`" | a *relative* path, to a folder that **did not exist on disk**; no `mkdir` |
| **VERIFY** | — | a command proving the right file landed in the right place |
| **IF ABSENT** | — | the case that actually happened, unhandled |
| **BLOCKS** | — | "Nothing else is blocked" sits three lines later, unattached to the task |
| **HOMEWORK** | "not downloadable from here" | no evidence anything was searched, and no substitute named |

Six omissions in one sentence. Rules 1–6 are those six, generalised. Rule 7 is the fix, written out.

---

## Rule 1 — Classify every task, and name *why* it is human

CEC 320 never states a human step without a **Why Manual** column — every table under
*What Requires Human Interaction* is `Operation | Why Manual | Human Steps`. **Copy that shape.**
A human task with no stated reason invites the human to wonder whether the agent just gave up.

**AUTOMATABLE is the default. HUMAN-REQUIRED is a claim, and it needs one of these reasons:**

| Reason | Means | Evidence in CEC 320 |
| --- | --- | --- |
| `GUI-only` | no command-line path exists at all | *"Converting a `.ioc` file into a CubeIDE project ALWAYS requires CubeMX GUI. There is no command-line alternative."* |
| `Hardware` | a physical board, cable, jumper or pin bridge | *"Upload to board — Hardware + GUI — Connect USB, click download/debug"* |
| `Credentialed` | behind a login the agent holds no session for | Canvas download, Canvas submission |
| `Capture` | a screenshot, a recording, a live demo | *"Take screenshots — OS interaction — Use screenshot tool, save file"* |
| `Judgment` | two defensible answers and the wrong one is graded | [coursework-solutions.md](./coursework-solutions.md) § Human-only |
| `Policy` | the repo forbids the agent doing it | git mutations — [question-discipline.md](./question-discipline.md) |

Anything else is AUTOMATABLE. "It's fiddly" and "I'd rather not" are not reasons.

**Decision tree** (ported from CEC 320 § Task Classification):

```
File create / copy / rename / edit?
├── YES → AUTOMATABLE (note the regeneration risk if it is a generated file)
└── NO: needs a GUI window?
    ├── YES → HUMAN-REQUIRED, reason GUI-only
    └── NO: an interactive session (blocks on a person)?
        ├── YES → HUMAN-REQUIRED, but hand over copy-paste commands
        └── NO → AUTOMATABLE
```

**Split the task at the real boundary before handing the whole thing over.** In CESC 410, plotting
looked human — `plt.show()` opens windows. It is not: `MPLBACKEND=Agg` saves every figure headlessly,
and only the *screenshots of the windows* are `Capture`
([reference_docs/known_issues.md](../../content/cesc_410/labs_and_projects/reference_docs/known_issues.md)
KI-02). Handing over "make the figures" instead of "screenshot these five windows" would have moved
an hour of automatable work onto the operator.

**Mark ownership everywhere, not just in one section.** CEC 320 prefixes each step in a workflow list
with `**LLM:**` or `**HUMAN:**` (`known_base_projects.md` § Workflow for New Projects) and opens every
procedure with a TLDR sequence table whose `Who` column alternates `LLM` / `HUMAN`. A reader must
never have to infer who acts.

---

## Rule 2 — Absolute paths, always

CEC 320 states the rule and the reason under *Writing Guidelines for Human Tasks*: *"Humans may have
multiple terminal windows or file managers open. Relative paths are ambiguous without context. Full
paths can be copy-pasted directly into file managers."*

**Any file movement gets a Source (FROM) → Destination (TO) table.** Never a bare list.

Bad — CEC 320's own example of the anti-pattern:

```
Drag these files to the lib_src folder:
- lib/mp_uart_redirect.c
- src/_mp_main.c
```

Good:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/opt/proj_mp/project_name/lib/mp_uart_redirect.c` | `lib_src` folder in CubeIDE |
| `/opt/proj_mp/project_name/src/_mp_main.c` | `lib_src` folder in CubeIDE |

- **From the filesystem root, every time.** `~` is acceptable only inside a shell block; never in prose.
- **If the destination folder does not exist, the `mkdir -p` is part of the instruction.**
- **A GUI destination is named as the GUI names it** — "the `lib_src` folder in CubeIDE Project
  Explorer", not a guess at its on-disk path.

**The specificity bar for anything physical** is
[nucleo32_pinout_reference.md](../../content/cec_320/labs_and_projects/nucleo32_pinout_reference.md):

> **Right side, Pin 13** (AREF = ~3.3V) — 3rd from bottom (bottom pin=1st, +3V3=2nd, AREF=3rd)

Note what that does: side, pin number, signal name, expected voltage, position counted from a named
edge — **and the document defines its counting convention before using it** (*"'Nth from bottom'
counts the bottom-most pin as the 1st from bottom"*). It also warns that the G431KB has its CN3/CN4
labels swapped versus every other Nucleo-32, so it uses physical position instead. That is the
standard: leave no step where the human has to guess which of two readings you meant.

---

## Rule 3 — Five things, every time

Every human task states **all five**. A task missing any of them is not ready to hand over.

| # | Element | The question it answers |
| --- | --- | --- |
| 1 | **WHERE** | Exactly where do I go? Named application, named page, named path — no category nouns. |
| 2 | **WHAT** | Exactly what do I do there? Clicks, commands, FROM→TO table. |
| 3 | **VERIFY** | How do I know it worked? A command with expected output, or an observable state. |
| 4 | **IF ABSENT** | What if it is not there / does not work? At least one next step, then who to ask. |
| 5 | **BLOCKS** | What stays stuck until this is done — and, just as important, what does not. |

- **WHERE fails on category nouns.** "Canvas", "the course site", "the settings" are categories.
  "Canvas → CESC 410 → Lab 1 module, the page the handout PDF came from" is a place.
- **VERIFY is a command, not a feeling.** Prefer something already in the repo:
  [`tools/check_inputs.py`](../../content/cesc_410/labs_and_projects/tools/check_inputs.py) exists
  precisely because *"a link to a file that was never downloaded is the most common reason a lab
  stalls"*. If no checker fits, give a `ls -l`, an `md5sum`, or the exact line of program output.
- **IF ABSENT is the one that actually fires.** It fired on Lab 1. Write it first if it helps.
- **BLOCKS is stated per task, not once at the bottom.** "Nothing else is blocked" as a footnote is
  not attached to anything; the operator cannot tell which task it was excusing.

---

## Rule 4 — Do the human's homework first, and show it

Before writing "download X", the agent must have looked. **State what was already tried so the human
does not repeat it.** CEC 320 does this even for its own fixes — every dual-solution entry in
`known_issues.md` carries a *"How to diagnose"* block and a **"What the LLM actually ran"** block
listing the literal commands.

Minimum before any `Credentialed` hand-off:

- [ ] Searched the repo and the machine for the file, by name and by extension — and quote the command.
- [ ] Read the handout for where it is supposed to come from, and say what the handout does or does not say.
- [ ] Checked whether a substitute exists on disk or can be generated, and named it.
- [ ] Checked the sibling lab folders and any shared assets directory.
- [ ] Said what the filename *is*, if that is knowable. `2086-149220-0033.wav` is a LibriSpeech
      utterance id (speaker 2086 / chapter 149220 / utterance 0033) — worth one line, because it
      tells the operator what they are looking for.

"Not downloadable from here" is a conclusion. Show the work that reached it.

---

## Rule 5 — Every blocking input gets a fallback

Assume the file never arrives. **Say what still works without it, and what has already been done to
keep going.** CESC 410 Lab 1 in fact had a good fallback — `test_tone.wav`, synthesised by
`tools/make_test_audio.py`, deliberately music-shaped, and every figure in `lab01/figs/` was produced
from it. The defect was that the fallback was described in a different section from the blocking task,
so the connection was never made.

- **Attach the fallback to the task**, in the same row or the same block.
- **Say what the fallback costs.** A synthetic stand-in is a *deviation* and goes in the report's
  Narrative — a graded section. Never a silent substitution.
- **Never let a missing input stall work it does not gate.** Split the task: run everything that does
  not need it, then list only the genuinely blocked step.
- **If nothing can proceed, say that explicitly too.** "This blocks all remaining work" is a real and
  useful answer; silence is not.

---

## Rule 6 — Both methods where both exist

CEC 320's issue template is not one solution, it is two:

```markdown
**Solution A: LLM/Command-Line Fix**
[terminal / automation steps]

**Solution B: Human GUI Fix**
[step-by-step GUI steps]
```

The worked instance — *Folder-level include paths override project settings* — gives Solution A as
`sed -i` on `.cproject` plus `rm -rf Debug/`, and Solution B as eleven numbered CubeIDE clicks ending
at *"Apply and Close"*, then *"Project → Clean"*. Same fix, both routes.

- **Write both when both exist.** The operator may be at a desktop or at a terminal; they choose.
- **Prefer A, offer B.** If the agent can do it, it should already be done — B is then a repair route
  and a way for the human to verify.
- **GUI steps are numbered and literal.** Menu names in bold, exact labels, and the disambiguation
  when it matters: *"right-click the `lib_src` **folder** (NOT the project root!)"*.
- **When a route is known-unreliable, say so and give the working one.** CEC 320:
  *"Drag-and-drop file linking is unreliable on Linux — use **New → File → Link to file system**."*

---

## Rule 7 — Worked example: the Lab 1 WAV

### Before — what shipped

```markdown
| Task | Status |
| --- | --- |
| **Fetch `2086-149220-0033.wav` from Canvas** into `dsp26/audio_files/` — the handout's default input, not downloadable from here | ⬜ |
```

### After — what the standard requires

Written as it should have shipped, at the moment it shipped. (The file has since arrived —
`dsp26/audio_files/2086-149220-0033.wav`, mono / 16 kHz / 7.43 s. The example stands as the
form to copy, not as an open task.)

```markdown
### H1 · Fetch the handout's default audio file  ·  Why human: Credentialed (Canvas login)

**Already tried — do not repeat:**
- `find /home/devel -iname '*2086*' -o -iname '*.wav'` → not on this machine.
- Read `dsp-bc--lab1-audio-signal.md` end to end. It names the file **only** inside code
  (line 459, `project_root / "audio_files" / "2086-149220-0033.wav"`) and never says where to get it.
- The name is a LibriSpeech utterance id (speaker 2086 / chapter 149220 / utterance 0033), so a
  public copy of the same clip likely exists — but the graded default input should be the
  instructor's copy. Ask before substituting.

**WHERE.** Canvas → CESC 410 (DSP) → the **Lab 1** module — the same page
`dsp-bc--lab1-audio-signal-26.pdf` was downloaded from. If that page has no attachment list, check
the course-level **Files** area, then the **Lab 0** module (shared assets are often posted once).

**WHAT.**

    mkdir -p /home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files

| Source (FROM) | Destination (TO) |
| --- | --- |
| `~/Downloads/2086-149220-0033.wav` (wherever the browser put it) | `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/dsp26/audio_files/2086-149220-0033.wav` |

The folder does not exist yet — the `mkdir -p` above is part of this step, not a suggestion.

**VERIFY.** From `/home/devel/electrical_notes/content/cesc_410/labs_and_projects/`:

    uv run --project dsp26 python tools/check_inputs.py lab01
    MPLBACKEND=Agg uv run --project dsp26 dsp26 play-plot-audio --folder-name lab01

Expected: `check_inputs.py` reports nothing missing, and the run prints
`Detailed properties of .../2086-149220-0033.wav` with `Frame rate (sample rate): 16000` and
`Number of channels: 1`. A different sample rate means the wrong file.

**IF IT IS NOT THERE.**
1. Course **Files** area, then the Lab 0 module.
2. Ask the TA or instructor, quoting the exact filename.
3. **Fallback, already in place:** `lab01/test_tone.wav` (synthesised by
   `tools/make_test_audio.py`, mono / 16 kHz / 10 s) is committed, and all five figures in
   `lab01/figs/` were generated from it. Add `--path-name lab01/test_tone.wav`. This is a
   **deviation** and must be stated in the report's Narrative.

**BLOCKS.** Only the run against the *default* input. The package code, all five figures,
`report.tex`, and `dsp26-lab01-nelson-gatlin.zip` are complete and do not wait on this.
```

Longer, and that is the point: the operator reads it once and acts, instead of reading it once and
returning to ask.

---

## Hand-off checklist

Run this against your own *Needs a human* section before you report. Every box, every task.

- [ ] Every task is classified, and every HUMAN-REQUIRED one names a reason from Rule 1's table.
- [ ] Nothing on the human list is actually automatable — including the automatable *half* of a
      split task.
- [ ] Every path is absolute, from `/`. No bare relative paths in prose.
- [ ] Every file movement is a Source (FROM) → Destination (TO) table.
- [ ] Every destination folder either exists or the instruction creates it.
- [ ] Every task states **WHERE, WHAT, VERIFY, IF ABSENT, BLOCKS** — all five.
- [ ] No WHERE is a category noun ("Canvas", "the settings", "the course site").
- [ ] Every VERIFY is a runnable command or an observable state, with the expected result written out.
- [ ] Every `Credentialed` task shows the search that was already done, with the command.
- [ ] Every blocking input has a fallback, attached to the task, with its cost stated.
- [ ] Both methods given wherever a command-line route and a GUI route both exist.
- [ ] Physical steps name side, position, and counting convention — the pinout bar.
- [ ] Anything learned in the process is filed per
      [documentation-discipline.md](./documentation-discipline.md): a recurring trap goes in the
      course's `reference_docs/known_issues.md` with **both** solutions.

---

Hub: no counterpart upstream — this rule is specific to a coursework repo where the human is the
only route to hardware, a login, and a grade. Nearest:
`~/llm-project-bootstrap/directives/question-discipline.md` → guide `ASKING_QUESTIONS.md`.
