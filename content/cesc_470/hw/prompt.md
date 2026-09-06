# Claude entry point — CESC 470 homework

**Trigger:** *"`hwNN/` now exists with the assignment in it, work it."*

**Read [`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) first.**
That is the doctrine — the two-document rule, the citation rule, the verification
rule, the per-assignment checklist. It is shared by every course under the
doctrine and is not repeated here.

This file carries **only what is specific to CESC 470.** Traps that have already
cost time are in [`../reference_docs/findings.md`](../reference_docs/findings.md);
read it before the first citation and before the first table.

---

## The course

**Computer Architecture** · Fall 2026 · Siyao Li · MWF 11:00–11:50, Lehman 369
Textbook: Hennessy & Patterson, Elsevier S&T, 2016, 1st ed.

Syllabus: [`../cesc_470.pdf`](../cesc_470.pdf) →
transcript at [`../pdf_transcripts/cesc_470.md`](../pdf_transcripts/cesc_470.md)

**Homework must be typed and submitted as PDF** (syllabus). Attendance is not
recorded but is *"factored into the quizzes"*.

⚠ The HW1 handout heads itself **"CEC 470"**. The syllabus says **CESC 470**
throughout, and `\coursename` follows the syllabus. Do not "fix" it the other
way.

---

## What to cite

Lecture decks live in [`../`](../) and are transcribed in
[`../pdf_transcripts/`](../pdf_transcripts/). Cite by **PDF page** and the deck's
own printed slide number, which differ — title slides are unnumbered:

```latex
The performance equation \srcref{Module 01, PDF p55, slide 32}
```

For Module 01 the offset is **PDF page − 7 = printed slide**, verified across six
citations. Re-derive it per deck; it is not a course-wide constant.

⚠ **Module 01's text layer is partial.** `ocr-handler inspect` grades it
`ok 26 / sparse 48 / empty 14` — so **62 of 88 pages are flagged sparse or
empty**, of which only 7 have essentially no text at all. Most "sparse" pages
still carry their diagram labels, so the flag is a prompt to look, not proof the
page is unreadable. The deck also has **letter-spacing artefacts** (one glyph per
text run), which break word-boundary greps. Check before citing a page you have
not seen:

```sh
cd ocr_handler && uv run ocr-handler inspect \
  "../content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf"
```

Study notes with worked examples: [`../md_notes/`](../md_notes/).

---

## Macros

Shared preamble plus [`../reference_docs/cesc470_macros.tex`](../reference_docs/cesc470_macros.tex):

| Macro | For |
| --- | --- |
| `\CPUtime` `\IC` `\CPI` `\cycletime` `\clockrate` `\cycles` `\speedup` | the performance equation |
| `\amdahl{unaffected}{affected}{n}` | Amdahl's law in the slides' form |

CESC 470 assignments state **no learning outcomes**, so use the three-argument
`\problemheader{n}{pts}{title}` — not `\problemheaderlo`.

**One macros file for the whole course**, at
`content/cesc_470/reference_docs/`, shared by `hw`, `qz` and `exam` — notation is
a property of the subject, not of the assignment kind. Every problem file
resolves it as `../../reference_docs/cesc470_macros.tex`. Never add a second copy
under a `<kind>/`: `new_tex.sh` takes the *nearest* hit, so `hw` and `qz` would
compile against different notation with no error anywhere.

---

## Assignments

| | Points | Status |
| --- | ---: | --- |
| [`hw01/`](hw01/) — five components, ISA, performance, Amdahl | 100 | ✅ complete, verified |

---

## Quizzes and exams

Nothing exists yet, but the tree is ready: [`../qz/`](../qz/) carries a
[`README.md`](../qz/README.md) with the recipe, and the doctrine treats `qz` and
`exam` exactly like `hw`.

```sh
mkdir -p content/cesc_470/qz/qz01
docs/latex/new_tex.sh content/cesc_470/qz/qz01 1 some-slug --pts "5 pts"
docs/latex/new_tex.sh content/cesc_470/qz/qz01 --solutions
```

`new_tex.sh` computes `../../reference_docs/cesc470_macros.tex` on its own —
**verified end to end on a throwaway `qz99/`**: scaffolded with no warning,
built, flattened, and the flattened copies compiled standalone with `CESC 470`
in the running head.

This only works because the macros sit at **course level**. While they lived
under `hw/reference_docs/` the scaffolder could not see them from `qz/qzNN/`
(`-maxdepth 2` misses a file three levels down) and exited without writing a
file. Moved 2026-09-05; the eleven HW1 sources were repointed from
`../reference_docs/` to `../../reference_docs/` in the same change. See
[`../reference_docs/findings.md`](../reference_docs/findings.md) § HW-08.

Build products for every kind are handled by one course-level
[`../.gitignore`](../.gitignore).

---

## Build, flatten, and *look*

```sh
docs/latex/build_tex.sh   content/cesc_470/hw/hw01           # build-check all
docs/latex/build_tex.sh   content/cesc_470/hw/hw01 --keep    # ...and keep the PDFs
docs/latex/flatten_tex.sh content/cesc_470/hw/hw01           # -> hw01/overleaf/
```

**Never paste a source file into Overleaf** — its relative `\input` climbs above
the project root and cannot resolve there. Flatten first.

A build that succeeds is not a document that is correct, and a file that flattens
is not a file that compiles. Three checks, none of which `build_tex.sh` performs:

```sh
# 1. the flattened copies actually compile standalone
cd content/cesc_470/hw/hw01/overleaf && for f in *.tex; do tectonic "$f" || echo "FAIL $f"; done

# 2. no overfull/underfull boxes (build_tex.sh deletes the log that holds them)
for f in *.tex; do tectonic -o /tmp/o "$f" 2>&1 | grep -E 'Overfull|Underfull'; done

# 3. no Markdown emphasis leaked into the LaTeX — this compiles clean and prints
#    literal asterisks
grep -nE '\*\*?[A-Za-z]' content/cesc_470/hw/hw01/*.tex
```

Then render a page and look at it:

```python
import pymupdf
pymupdf.open("p04_architecture_vs_organization.pdf")[1].get_pixmap(dpi=110).save("/tmp/p.png")
```

Scaffold new `hw` files rather than hand-writing the `\input` lines:

```sh
docs/latex/new_tex.sh content/cesc_470/hw/hw02 3 some-slug --pts "10 pts"
docs/latex/new_tex.sh content/cesc_470/hw/hw02 --solutions
```

Detail: [`docs/latex/INDEX.md`](../../../docs/latex/INDEX.md)

---

## Human-only

Everything in the directive's Human-only table, plus:

| Task | Why |
| --- | --- |
| **Confirming submission form** | The syllabus says "typed, converted to PDF". Whether that means the solutions document alone or the per-problem files too is **unconfirmed**. |
| **Confirming the quiz PDF naming** | The course-level `.gitignore` whitelists *our* build products rather than guessing the instructor's filenames, so nothing needs adjusting — but confirm with `git check-ignore -v` the first time a real quiz handout lands. |
