# Claude entry point — CESC 470 homework

**Trigger:** *"`hwNN/` now exists with the assignment in it, work it."*

**Read [`docs/directives/coursework-solutions.md`](../../../docs/directives/coursework-solutions.md) first.**
That is the doctrine — the two-document rule, the citation rule, the verification
rule, the per-assignment checklist. It is shared by every course under the
doctrine and is not repeated here.

This file carries **only what is specific to CESC 470.**

---

## The course

**Computer Architecture** · Fall 2026 · Siyao Li · MWF 11:00–11:50, Lehman 369
Textbook: Hennessy & Patterson, Elsevier S&T, 2016, 1st ed.

Syllabus: [`../cesc_470.pdf`](../cesc_470.pdf) →
transcript at [`../pdf_transcripts/cesc_470.md`](../pdf_transcripts/cesc_470.md)

**Homework must be typed and submitted as PDF** (syllabus). Attendance is not
recorded but is *"factored into the quizzes"*.

---

## What to cite

Lecture decks live in [`../`](../) and are transcribed in
[`../pdf_transcripts/`](../pdf_transcripts/). Cite by **PDF page** and the deck's
own printed slide number, which differ — title slides are unnumbered:

```latex
The performance equation \srcref{Module 01, PDF p55, slide 32}
```

⚠ **Module 01 is 62 of 88 pages image-only.** The text layer carries the
quantitative material almost intact but not the diagrams. Check before citing a
page you have not seen:

```sh
cd ocr_handler && uv run ocr-handler inspect \
  "../content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf"
```

Study notes with worked examples: [`../md_notes/`](../md_notes/).

---

## Macros

Shared preamble plus [`reference_docs/cesc470_macros.tex`](reference_docs/cesc470_macros.tex):

| Macro | For |
| --- | --- |
| `\CPUtime` `\IC` `\CPI` `\cycletime` `\clockrate` `\cycles` `\speedup` | the performance equation |
| `\amdahl{unaffected}{affected}{n}` | Amdahl's law in the slides' form |

CESC 470 assignments state **no learning outcomes**, so use the three-argument
`\problemheader{n}{pts}{title}` — not `\problemheaderlo`.

---

## Assignments

| | Points | Status |
| --- | ---: | --- |
| [`hw01/`](hw01/) — five components, ISA, performance, Amdahl | 100 | ✅ complete |

---

## Human-only

Everything in the directive's Human-only table, plus:

| Task | Why |
| --- | --- |
| **Confirming submission form** | The syllabus says "typed, converted to PDF". Whether that means the solutions document alone or the per-problem files too is **unconfirmed**. |
