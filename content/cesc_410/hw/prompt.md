# Claude entry point — CESC 410 homework

**Trigger:** *"`hwNN/` now exists with the assignment in it, work it."*

Same file governs **quizzes and exams** — `qz/qzNN/` and `exam/examN/` use an
identical structure. One extra step applies to them: see
[Quizzes and exams](#quizzes-and-exams).

Read this, then the docs it points at, then work. Stop only for [Human-only](#human-only).

Sibling setup for the lab course: [`../labs_and_projects/prompt.md`](../labs_and_projects/prompt.md). Same instructor, same conventions — but **homework is LaTeX, not Markdown**, and usually involves no code and no zip.

---

## Read first

1. This file.
2. [`reference_docs/findings.md`](reference_docs/findings.md) — **what silently produces wrong answers.** Read before transcribing anything.
3. [`reference_docs/hw_workflow.md`](reference_docs/hw_workflow.md) — the two-document rule, and how a problem file is built.
4. [`reference_docs/submission.md`](reference_docs/submission.md) — **what the course actually requires of a submission**, quoted from the course-info PDF: PDF only, Letter, 1-inch margins, every intermediate step, AI use disclosed, no late work. It also holds the questions still open and the exact words to ask them with.
5. The assignment PDF in `hwNN/`.
6. [`../../../docs/latex/coursework_preamble.tex`](../../../docs/latex/coursework_preamble.tex) — the SHARED preamble: `\answerbox`, `trap`, `\srcref`, `\extref`, `\problemheader` / `\problemheaderlo`, page style, packages.
7. [`../reference_docs/cesc410_macros.tex`](../reference_docs/cesc410_macros.tex) — the CESC 410 half: DSP notation and `\stemplot`. Do not redefine either set per problem.

---

## ⚠ Never transcribe an equation from a PDF text layer

`pdftotext` flattens stacked fractions into valid-looking text that means
something else. On HW1 it turned $\cos(\frac{\pi}{6}n)$ into `cos( 6π n)` — a
constant signal — and dropped a $\sqrt{\ }$ onto the wrong line, which would have
flipped an aperiodic signal into a periodic one. Neither raises an error.

**Render the region and look at it.** Absolute path, and the handout's real
filename — the instructor names it, so it is never `assignment.pdf`
(HW 1's is `dsphw26-hw1.pdf`; `ls` the folder to get yours):

```python
import fitz
d = fitz.open("/home/devel/electrical_notes/content/cesc_410/hw/hw01/dsphw26-hw1.pdf")
d[0].get_pixmap(clip=fitz.Rect(180, 270, 420, 320), dpi=400).save("/tmp/x.png")
```

Then open `/tmp/x.png` and read it. 400 dpi resolves a $\sqrt{\ }$ from a `/`.

`course_text.py --grep` reads that same broken layer. It is for finding *which
document* covers a topic — never for reading the maths inside one.
Full detail: [HW-01](reference_docs/findings.md#hw-01--pdftotext-silently-corrupts-fractions--wrong-answers-no-error).

---

## The two-document rule

This is the whole shape of the work, and it is not negotiable:

| | Per-problem files | Solutions document |
| --- | --- | --- |
| `hwNN/pNN_<slug>.tex` | one per problem | `hwNN/hwNN_solutions.tex` |
| **Every step, shown** | ✅ full working | ❌ **answers only** |
| Audience | someone learning it | someone checking it |
| Length | as long as it takes | as short as possible |

**Detailed work lives in the per-problem files. The solutions document is the condensed version — final answers, nothing else.** Do not put derivations in the solutions document; do not omit them from the problem files.

Each problem file is **standalone** — it inputs the shared repo preamble and the
CESC 410 macros, then builds by itself, so a broken problem is found where it broke:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}
\input{../../reference_docs/cesc410_macros.tex}
\begin{document}
```

```sh
# from the repo root; paths are REPO-RELATIVE
docs/latex/build_tex.sh content/cesc_410/hw/hw01/p01_phasor_form.tex
```

---

## Procedure

### 1. Inventory

List `hwNN/`. Read the assignment PDF. **Extract every problem, its stated LO, and its points.** Record them in `hwNN/README.md` before writing any LaTeX.

**Sum the points and compare against the handout's stated total.** It is the only cheap check that catches a dropped problem — HW1 states 130, and $20+10+20+20+40+20=130$ confirms it.

Watch for handout numbering errors. HW1 labels two different problems "Prob 1" and has no Prob 6; files use a continuous internal index and state the discrepancy on the face of the document.

### 2. Ground it in the course materials — do not guess

The lectures and labs are the authority on notation and method. **Search them before searching the internet.**

⚠ **`course_text.py` is NOT at the repo root.** It lives in `tools/` under
`content/cesc_410/hw/`, so unlike `build_tex.sh` it is not run from the repo
root — `cd` first or it fails with `No such file or directory`:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw
tools/course_text.py --grep "periodic"      # find where the course covers it
tools/course_text.py --list                 # what is available, with a text-layer verdict
```

⚠ **Some documents have no usable text layer.** `--list` flags each one
`NO-TEXT` and prints the totals on its first and last lines — **read the count
off `--list`, do not trust a number written in prose here.** It moves every time
material is added, and the tool indexes `.md`/`.tex` as well as PDFs. On
2026-09-08 it printed `64 documents, 60 with a usable text layer`, and the four
were:

```text
lectures/f26_lctr02_DT signals and systems-plw.pdf
lectures/f26_lctr02_DT signals and systems.pdf
lectures/f26_lctr03_LTI_systems_conv.pdf
labs_and_projects/lab00/report.pdf          <- ours, and near-empty; not a lecture
```

Three are the handwritten lecture PDFs. They are not searchable this way, and
inventing what they contain is worse than admitting the gap. Use
[`../../../ocr_handler`](../../../ocr_handler) or read the PDF directly.

If the course materials genuinely do not cover something, say so in the problem file rather than silently importing a convention from elsewhere.

### 3. Write one file per problem

**Scaffold it** — `new_tex.sh` computes the two `\input` paths from the target's depth instead of trusting a `../` count, and writes the same five sections:

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/hw/hwNN          # new_tex.sh will not create the folder
docs/latex/new_tex.sh content/cesc_410/hw/hwNN 1 <slug> --pts "20 pts" --lo LO01
```

Copying [`reference_docs/problem_template.tex`](reference_docs/problem_template.tex) by hand also works — its `\input` lines are already right for `hwNN/` depth. Either way: fill in the header, restate the problem, then work it.

**Show every step.** The reader is someone learning the method, not someone confirming an answer they already have. State which lecture or LO a technique comes from where it is not obvious.

End with the result in an `answerbox`. That is what the solutions document lifts.

### 4. Assemble the solutions document

`hwNN/hwNN_solutions.tex` — one entry per problem, the final answer only. If it takes more than a few lines per problem, it is the wrong document.

### 5. Build-check everything — then *look* at it

⚠ **`build_tex.sh` DELETES the PDF it made unless you pass `--keep`.** If the
next thing you do is render that PDF, build with `--keep` or there is nothing
to render:

```sh
docs/latex/build_tex.sh content/cesc_410/hw/hw01           # check only, PDFs removed
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep    # check AND keep the PDFs
```

**One expected failure per `reference_docs/`, and they are different files.**
Both are preamble fragments with no `\begin{document}`, so they cannot compile
alone — that is what makes them fragments. Do not "fix" them:

| Folder | Expected FAIL | Expected OK |
| --- | --- | --- |
| `content/cesc_410/hw/reference_docs` | `cesc410_preamble.tex` — `no legal \end found` | `problem_template.tex` |
| `content/cesc_410/reference_docs` | `cesc410_macros.tex` — `Command \coursename undefined` | *(nothing else there)* |

`cesc410_macros.tex` is **not** under `hw/` — it moved to the course level
([HW-11](reference_docs/findings.md#hw-11--new_texsh-could-not-reach-a-sibling-kinds-macros-file--fixed)).
Anything still claiming two failures in one folder is stale.

**A document that compiles is not a document that is correct.** `OK` says
nothing about layout: it did not catch the y-label being drawn straight through
the tallest stem, or `\angle -75°` rendering as a subtraction. Render to PNG and
actually look, at least once per new visual element:

```python
import fitz
d = fitz.open("/home/devel/electrical_notes/content/cesc_410/hw/hw01/p03_signal_transformations.pdf")
d[0].get_pixmap(dpi=110).save("/tmp/p.png")
```

If that raises `no such file`, the build ran without `--keep`. Re-run it with
`--keep`.

### 5b. Verify the numbers computationally

Do not submit an answer that was only re-read. Check it by an independent route —
and for any "not periodic" / "no solution" claim, **run the search** rather than
asserting it. Evaluating at a single point is usually too weak: $x(0)=A\cos\phi$
agrees for both $+\phi$ and $-\phi$. See [HW-04](reference_docs/findings.md#hw-04--verify-numerics-computationally-and-prefer-two-independent-routes).

### 6. Report

What is done, what is blocked, and everything from [Human-only](#human-only).

**Every hand-off gets WHERE / WHAT / VERIFY / IF ABSENT / BLOCKS** — all five, per
task, absolute paths, with the search you already ran quoted so the human does not
repeat it. Run the checklist at the end of
[`human-task-instructions.md`](../../../docs/directives/human-task-instructions.md#hand-off-checklist)
against your own list before you report. A vague hand-off spends the human twice:
once on the task, once on working out what the task was.

---

## Overleaf

**Never paste a source file into Overleaf** — its relative `\input` climbs above
the project root and cannot resolve there. Flatten first:

```sh
cd /home/devel/electrical_notes
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
#   -> content/cesc_410/hw/hw01/overleaf/*.tex   (self-contained, gitignored)
```

**Then compile what it wrote.** Flattening only proves no `\input` survived; it
does not build the output, so those are two different claims:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf
for f in *.tex; do tectonic "$f"; done
```

The output carries a two-line header naming the source **basename** — no
repository path; that was fixed and re-checked 2026-09-08
([HW-10](reference_docs/findings.md#hw-10--the-flattener-used-to-stamp-a-repo-path-into-its-output--fixed)).
It never reaches the PDF, but delete it if the `.tex` itself is the deliverable.
**Hand over the flattened copy, never the source** — the source's first two
lines are `\input` paths into this repository.

Scaffold new files rather than hand-writing the `\input` lines. **`new_tex.sh`
will not create the assignment folder** — it exits 1 with
`error: no such folder ... (create it first)`, so `mkdir` is step one:

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/hw/hw02
docs/latex/new_tex.sh content/cesc_410/hw/hw02 3 some-slug --pts "10 pts" --lo LO01
```

Detail: [`docs/latex/INDEX.md`](../../../docs/latex/INDEX.md)

---

## Quizzes and exams

Same doctrine, same two-document rule, same five-section problem file. A quiz
lives at `content/cesc_410/qz/qzNN/`, an exam at `content/cesc_410/exam/examN/`.

**CESC 410 has exactly one macros file and all three kinds share it.** Do not
create `qz/reference_docs/` — a second `*_macros.tex` for one course lets `hw/`
and `qz/` diverge silently, and `new_tex.sh` warns about it by name.

**`new_tex.sh` scaffolds a quiz correctly — use it.** An older version of this
file said it could not, and that was true while the macros file sat under `hw/`.
It has since moved to the course level, which is where the scaffolder looks:

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/qz/qz01          # new_tex.sh will not create it
docs/latex/new_tex.sh content/cesc_410/qz/qz01 1 some-slug --pts "20 pts" --lo LO01
docs/latex/new_tex.sh content/cesc_410/qz/qz01 --solutions
```

Re-verified 2026-09-08 on a throwaway `qz99/` — scaffolded, built, flattened, and
the flattened copies compiled standalone. The emitted `\input` lines are:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}
\input{../../reference_docs/cesc410_macros.tex}
```

A new `qz/` still needs its own `.gitignore` — `hw/`'s rules do not reach a
sibling folder. Full detail:
[`reference_docs/hw_workflow.md`](reference_docs/hw_workflow.md#quizzes-and-exams) ·
[HW-11](reference_docs/findings.md#hw-11--new_texsh-could-not-reach-a-sibling-kinds-macros-file--fixed).

---

## Human-only

**AUTOMATABLE is the default.** A task is on this list only with a reason from
[`human-task-instructions.md`](../../../docs/directives/human-task-instructions.md)
§ Rule 1 — `GUI-only`, `Hardware`, `Credentialed`, `Capture`, `Judgment`, `Policy`.
"It's fiddly" is not a reason. Split a task before handing over the whole of it:
building, checking, merging and flattening the PDFs are all automated, so only the
upload is human.

**H1–H4 are tasks**; their full **WHERE / WHAT / VERIFY / IF ABSENT / BLOCKS**
lives in [`reference_docs/submission.md`](reference_docs/submission.md#human-tasks)
— this table is the index, not the instruction. **The last two rows are standing
judgment calls, not to-dos**: they have no H-number and no five-element entry,
because there is nothing to go and do — their Detail column points at the
doctrine that governs the call when it comes up.

| Task | Why human | Detail | Blocks |
| --- | --- | --- | --- |
| **Submitting to Canvas** | `Credentialed` — no session, and the destination site is itself unconfirmed | [H1](reference_docs/submission.md#h1--confirm-where-homework-is-submitted-and-submit-it--why-human-credentialed) | Only the act of turning it in. Every artifact is built |
| **Deciding working vs. answers-only** | `Judgment` — settled by § 8.6 (*"show all necessary intermediate steps"*), so read before asking | [H2](reference_docs/submission.md#h2--decide-whether-the-working-or-the-answers-go-in--why-human-judgment) | Nothing. Both documents exist |
| **The AI-use disclosure** | `Judgment` — § 11.1 requires it (*"you should clearly indicate it"*), and a representation about your own work is not the agent's to write | [H3](reference_docs/submission.md#h3--decide-and-place-the-ai-use-disclosure--why-human-judgment) | Must be settled **before** H1 |
| **Asking the instructor Q1–Q5** | `Credentialed` — Dr. Liu is a person. Verbatim wording, address and office hours are in the doc | [H4](reference_docs/submission.md#h4--ask-q1q5--why-human-credentialed-they-are-a-person-not-a-file) | Nothing. Every assumption is already implemented |
| **Deciding whether an answer is right** | `Judgment` — where the course materials are silent and two conventions are defensible, flag it in the problem file; do not pick silently | [`coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) | The problem it affects, and only that problem |
| **Reading the handwritten lecture PDFs** | `Judgment` — three lecture PDFs have no text layer (`course_text.py --list` flags them `NO-TEXT`), and inventing their contents is worse than naming the gap | [HW-01](reference_docs/findings.md#hw-01--pdftotext-silently-corrupts-fractions--wrong-answers-no-error) | Only a claim that cites one of those three |

**Never write a human task without all five elements.** A line that says "fetch it
from Canvas" and stops has already cost this repo a failed hunt and a round-trip
— that failure is
[written up](../../../docs/directives/human-task-instructions.md#the-failure-this-exists-to-prevent).

---

## Rules

**"§ N" below means a section of the CESC 410 course-info PDF**,
[`../senior_design/cesc410-course-info-fall2026.pdf`](../senior_design/cesc410-course-info-fall2026.pdf)
— § 8.6 *Submission of Work*, § 11.1 *AI Use Policy*, § 11.3 *Missing Assignments*. It is the
authority on what a submission must look like, and it is quoted in
[`reference_docs/submission.md`](reference_docs/submission.md#confirmed--quoted-from-the-course-info-pdf)
so you rarely need to open it.

- **LaTeX only for homework content.** No Markdown solutions, no Markdown working. `README.md` per assignment is tracking metadata, not homework.
- **One problem, one file.** A file covering two problems cannot be build-checked independently.
- **Use the existing macros** rather than redefining notation per file. `\answerbox`, `\problemheaderlo`, `\srcref` come from the shared repo preamble; `\stemplot`, `\phasor` and the rest of the DSP notation from `../reference_docs/cesc410_macros.tex` — **course level, one per course**, not under `hw/`. A macro another course would also want belongs in the shared preamble, not in the course macros.
- **Never cite a lecture you have not read.** `course_text.py --grep` first; `NO-TEXT` documents are not searchable.
- **Homework rarely ships code or a zip** — unlike the labs, but the course info says assignments *"may include programming assignments."* Check the handout; if there is code, it is typed **1TBS with 4-space indentation** (§ 8.6 prints a worked example).
- **The submitted PDF must be Letter with 1-inch margins and show every intermediate step** (§ 8.6). Letter and the margins come free from `docs/latex/coursework_preamble.tex` — verified, every built PDF measures `612 x 792 pts` with text starting at 72.0 pt. Do not override `geometry` per file.
- **AI use must be disclosed** (§ 11.1). That sentence is the operator's to write, not the agent's — [H3](reference_docs/submission.md#h3--decide-and-place-the-ai-use-disclosure--why-human-judgment). Do not add it silently and do not decide it is unnecessary.
- **Late is a zero and there is no makeup** (§ 8.6, § 11.3). Deadline table: [`reference_docs/submission.md`](reference_docs/submission.md#deadlines--from--9-class-schedule).
- PDFs are build products: gitignored, rebuilt by `docs/latex/build_tex.sh`.
- `overleaf/` is generated output, gitignored at any depth. **Edit the source, never the flattened copy** — it is overwritten on the next run.

---

**Related:** [`reference_docs/findings.md`](reference_docs/findings.md) · [`reference_docs/hw_workflow.md`](reference_docs/hw_workflow.md) · [`reference_docs/submission.md`](reference_docs/submission.md) · [`../senior_design/cesc410-course-info-fall2026.pdf`](../senior_design/cesc410-course-info-fall2026.pdf) · [`../labs_and_projects/prompt.md`](../labs_and_projects/prompt.md) · [`../../../docs/directives/human-task-instructions.md`](../../../docs/directives/human-task-instructions.md)
