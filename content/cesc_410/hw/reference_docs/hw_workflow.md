# Homework workflow

## Two documents, different jobs

The single rule that shapes everything:

| | `pNN_<slug>.tex` | `hwNN_solutions.tex` |
| --- | --- | --- |
| One per | problem | assignment |
| Contains | **every step** | **answers only** |
| For | learning the method | checking the result |
| Built | standalone | once, at the end |

Mixing them ruins both. A solutions document with derivations is unusable for checking; a problem file without them is unusable for learning.

**The per-problem file is the graded artifact**, and that is not a style
preference: the course info requires *"Use correct approach and show all
necessary intermediate steps"* (§ 8.6). The solutions document is an internal
check aid — see
[`submission.md`](submission.md#what-this-settles-about-our-two-documents).

## Why one file per problem

- **It build-checks alone.** A LaTeX error is located at the problem, not somewhere in a 12-problem document.
- **Problems are independent.** They can be written, revised, and reviewed without touching each other.
- **The assignment can be partially done** without a broken document.

Each file inputs two preamble fragments — neither has a `\begin{document}`, which is what lets a fragment be a complete document:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}   % shared, every course
\input{../../reference_docs/cesc410_macros.tex}             % CESC 410 only
\begin{document}
```

The shared half carries the document class, the packages, `\answerbox`, the
`trap` callout, `\srcref` / `\extref`, `\problemheader` / `\problemheaderlo`
and the page style. The CESC 410 half carries `\coursename`, the DSP notation
and `\stemplot` — things that mean nothing outside a signals course. Four `..`
levels reach the repo root from `content/<course>/hw/hwNN/`.

## Naming

```text
hw01/
├── dsphw26-hw1.pdf              the assignment
├── README.md                    tracking: problems, LOs, points, status
├── p01_phasor_form.tex          one per problem
├── p02_phasor_arithmetic.tex
├── ...
└── hw01_solutions.tex           condensed answers
```

`pNN` is a **continuous internal index**, not necessarily the handout's label. HW1 numbers two different problems "Prob 1"; the file names run p01–p06 and each file states the handout's own label in its header.

## Grounding work in the course

⚠ **`course_text.py` is not at the repo root** — it is in `tools/` under
`content/cesc_410/hw/`, unlike `build_tex.sh`. Run it from there:

```sh
cd /home/devel/electrical_notes/content/cesc_410/hw
tools/course_text.py --grep "convolution"
tools/course_text.py --list
tools/course_text.py --dump /tmp/coursetext
```

Searches lectures, labs, handouts, and the `.md`/`.tex` alongside them in one
command. **`--list` prints the totals itself — read them off the command, not
off this page.** The number grows every time material lands. On 2026-09-08 it
printed `64 documents, 60 with a usable text layer`; the four `NO-TEXT` were
three handwritten lecture PDFs (`f26_lctr02` ×2, `f26_lctr03`) plus our own
near-empty `labs_and_projects/lab00/report.pdf`.

> Not being able to search a document is not permission to guess what it says. Read the PDF, or use `ocr_handler`, or state the gap in the problem file.

## Notation

Use the existing macros so every problem writes the same symbols:

| Macro | From | For |
| --- | --- | --- |
| `\answerbox` | shared | final answer — what the solutions document lifts |
| `\problemheaderlo{n}{LO}{pts}{title}` | shared | problem header; CESC 410 states an LO, so use the 4-arg `lo` form |
| `\problemheader{n}{pts}{title}` | shared | 3-arg form, for courses with no LO |
| `\srcref{...}` `\extref{...}` | shared | cite the slide a step came from / mark an outside step |
| `trap` environment | shared | callout for the trap in a problem |
| `\stemplot{xmin}{xmax}{coords}` | cesc410 | DT stem plot in the lecture's format |
| `\phasor{mag}{angle}` | cesc410 | phasor notation |
| `\conv` `\ustep` `\Real` `\Imag` `\dtft` `\ztr` `\sinc` | cesc410 | DSP notation |

Add a macro rather than redefining notation in one file — DSP notation to
`cesc410_macros.tex`, anything another course would also want to
`docs/latex/coursework_preamble.tex`.

## Building

The shared build-checker takes **repo-relative** paths and is run from the repo root:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/hw01/p01_phasor_form.tex   # one
docs/latex/build_tex.sh content/cesc_410/hw/hw01                        # all
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep                 # keep PDFs
```

`tools/build_tex.sh` still works for this folder and takes paths relative to
`content/cesc_410/hw/`, but `docs/latex/build_tex.sh` is the shared one — prefer it.
It is the same script every course runs, so a fix to it lands everywhere.

PDFs are deleted by default and gitignored — they are build products.

### ⚠ Pointing it at a `reference_docs/` reports one failure, by design

`build_tex.sh` builds **every** `.tex` at the top level of the folder it is
given. There are **two different `reference_docs/`** in play and each contains
exactly one fragment, so each reports exactly **one** FAIL — verified
2026-09-08:

| Folder | File | Standalone build | Why |
| --- | --- | --- | --- |
| `content/cesc_410/hw/reference_docs` | `problem_template.tex` | ✅ OK | a real document — it is the skeleton you copy |
| `content/cesc_410/hw/reference_docs` | `cesc410_preamble.tex` | ❌ `no legal \end found` | comment-only tombstone; superseded, do not `\input` it |
| `content/cesc_410/reference_docs` | `cesc410_macros.tex` | ❌ `Command \coursename undefined` | preamble fragment; `\renewcommand{\coursename}` needs the shared preamble loaded first, and there is no `\begin{document}` |

⚠ **`cesc410_macros.tex` is not under `hw/`.** It moved to the course level so
`new_tex.sh` could reach it from `qz/` and `exam/` too — see
[HW-11](findings.md#hw-11--new_texsh-could-not-reach-a-sibling-kinds-macros-file--fixed).
If you see two FAILs from one folder, or a doc claiming there should be, that
doc predates the move.

Both failures are correct behaviour, not bugs to fix — a fragment without
`\begin{document}` **cannot** compile, and that is exactly what lets it be
`\input` by a file that has one. Build the template by name instead:

```sh
cd /home/devel/electrical_notes
docs/latex/build_tex.sh content/cesc_410/hw/reference_docs/problem_template.tex
```

## Overleaf

**A source file cannot be pasted into Overleaf.** Its `\input` climbs above the
project root, which an Overleaf project cannot resolve — the compile dies with
`File '../../../../docs/latex/coursework_preamble.tex' not found`. Flatten to a
self-contained copy first:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
#   -> content/cesc_410/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

The flattened copy also has tooling-naming comments stripped, which is what the
no-tooling-references rule requires of anything submitted. **Edit the source, not
the copy.**

**Flattening successfully is not the same as the output compiling.** The script
only guarantees no `\input` survived; it does not build what it wrote. Check it:

```sh
cd /home/devel/electrical_notes && docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
cd /home/devel/electrical_notes/content/cesc_410/hw/hw01/overleaf
for f in *.tex; do tectonic "$f" >/dev/null && echo "$f OK" || echo "$f FAIL"; done
rm -f *.pdf     # the check is the exit status, not the output
```

Status, re-checked 2026-09-08: **all seven HW1 files flatten and compile
standalone**, and so does `reference_docs/problem_template.tex`.

Two caveats:

- The flattener stamps a two-line header into every output. It names the source
  **basename only** — no repository path; that was
  [fixed](findings.md#hw-10--the-flattener-used-to-stamp-a-repo-path-into-its-output--fixed)
  and re-checked 2026-09-08:

  ```text
  % Self-contained: preamble inlined, no external \input.
  % Generated copy of p01_phasor_form.tex -- edit the original, not this.
  ```

  A LaTeX comment never reaches the PDF, so this matters only if the `.tex`
  itself is handed in — in which case delete the two lines, since even a
  basename names one of our files.
- **The flattened copy is the one to hand over, not the source.** The source's
  first two lines are `\input{../../../../docs/latex/...}` and
  `\input{../../reference_docs/...}` — repository paths, inside the file. The
  flattened copy has none:
  `grep -nE 'docs/latex|reference_docs|/home/' overleaf/*.tex` returns nothing.
- `overleaf/` is gitignored at any depth, so `hw01/overleaf/` and
  `reference_docs/overleaf/` are both covered by the one rule.

## Starting a new file

Do not hand-write the two `\input` lines — the `../` count depends on depth.
**`new_tex.sh` refuses to create the folder** (`error: no such folder ...
(create it first)`), so `mkdir` first:

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/hw/hw02
docs/latex/new_tex.sh content/cesc_410/hw/hw02 1 phasors --pts "20 pts" --lo LO01
docs/latex/new_tex.sh content/cesc_410/hw/hw02 --solutions
```

CESC 410 states learning outcomes, so use `--lo`; the scaffold then emits
`\problemheaderlo`.

## Quizzes and exams

The doctrine covers `hw`, `qz` and `exam` with **identical** structure — same
two-document rule, same five-section problem file, same `answerbox`. Nothing
exists for quizzes yet; when a `qz01` appears it goes at
`content/cesc_410/qz/qz01/` alongside `hw/`.

**There is one macros file for CESC 410 and it is shared across all three
kinds.** Do *not* create `qz/reference_docs/cesc410_macros.tex`: a second
`*_macros.tex` for one course is the drift the doctrine exists to prevent, and
`new_tex.sh` warns about it explicitly —

```text
WARNING: 2 macros files for course 'cesc_410':
         Doctrine is ONE per course.
         Two files means hw/ and qz/ can silently diverge.
```

A quiz file therefore reaches the **course-level** `reference_docs/`, the same
folder `hw/` reaches — the two `..` land on `content/cesc_410/`, not on `hw/`:

```latex
\input{../../../../docs/latex/coursework_preamble.tex}   % 4 up: qz/qz01 -> root
\input{../../reference_docs/cesc410_macros.tex}          % 2 up: course level
\begin{document}
```

Absolute, so there is nothing to count:
`/home/devel/electrical_notes/content/cesc_410/reference_docs/cesc410_macros.tex`.

### ✅ `new_tex.sh` scaffolds a quiz correctly — re-verified 2026-09-08

**This section used to say the opposite. It was true, and it is no longer.** The
scaffolder walks **up** from the target folder looking for
`*/reference_docs/*_macros.tex`, two levels deep at each step. When the macros
file lived at `content/cesc_410/hw/reference_docs/`, that walk could not see it
from `content/cesc_410/qz/qz01` — a sibling kind is three levels down from the
common ancestor — and it exited without writing anything.

**The macros file has since moved up to the course level**, which is where the
walk *does* reach it. There is exactly one per current course:

```text
content/cesc_410/reference_docs/cesc410_macros.tex
content/cesc_470/reference_docs/cesc470_macros.tex
content/cpsc_462/reference_docs/cpsc462_macros.tex
```

**Verified end to end 2026-09-08** on a throwaway `content/cesc_410/qz/qz99/`
(created, exercised, deleted):

```sh
cd /home/devel/electrical_notes
mkdir -p content/cesc_410/qz/qz99
docs/latex/new_tex.sh   content/cesc_410/qz/qz99 1 phasors --pts "20 pts" --lo LO01
docs/latex/new_tex.sh   content/cesc_410/qz/qz99 --solutions
docs/latex/build_tex.sh content/cesc_410/qz/qz99
docs/latex/flatten_tex.sh content/cesc_410/qz/qz99
```

`new_tex.sh` reported the paths it resolved, and they are the right ones:

```text
created content/cesc_410/qz/qz99/p01_phasors.tex
  preamble: ../../../../docs/latex/coursework_preamble.tex  (4 levels up)
  macros:   ../../reference_docs/cesc410_macros.tex
```

Both files built (`All build.`), both flattened, and both flattened copies
compiled standalone under `tectonic`. **So scaffold a quiz; do not hand-copy the
template.** Copying still works if you prefer it, and the `\input` lines are the
same two shown above.

### One thing a new `qz/` still needs

`qz/` will need its own `.gitignore`, or `hw/`'s copied — the existing rules are
scoped to `hw/` and do not reach a sibling folder:

| Source (FROM) | Destination (TO) |
| --- | --- |
| `/home/devel/electrical_notes/content/cesc_410/hw/.gitignore` | `/home/devel/electrical_notes/content/cesc_410/qz/.gitignore` |

Then check it by rule number rather than by eye —
`git check-ignore -v content/cesc_410/qz/qz01/p01_slug.pdf` must name the line
that matched ([HW-07](findings.md#hw-07--build-products-vs-source-material-in-one-folder)).

### ✅ Resolved — the macros-file layout question

This document used to close on an open question: the doctrine put the macros
file at `content/<course>/<kind>/reference_docs/` while `new_tex.sh` looked at
`content/<course>/reference_docs/`, and moving it was *"flagged, not decided."*

**It was decided and done.** All three current courses now keep one macros file
at the course level, which is what the scaffolder expects:

```sh
find content -name '*_macros.tex'
#   content/cesc_410/reference_docs/cesc410_macros.tex
#   content/cesc_470/reference_docs/cesc470_macros.tex
#   content/cpsc_462/reference_docs/cpsc462_macros.tex
```

Nothing is open here and nobody needs to be asked. Recorded so it is not
re-raised — and so the *"copy the template, the scaffolder cannot help you"*
workaround above is not resurrected from an old copy of this file.

---

**Related:** [`findings.md`](findings.md) · [`../prompt.md`](../prompt.md) · [`submission.md`](submission.md) · [`problem_template.tex`](problem_template.tex) · [`../hw01/README.md`](../hw01/README.md)
