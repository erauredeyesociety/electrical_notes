# Scope

> **Draft — needs operator confirmation.** Per bootstrap doctrine the human defines in/out. Everything below is a proposal from the brief; the Out-of-Scope section is the load-bearing part.

**Kind:** Implementation project (deliverable is working code).

---

## Problem

Lecture PDFs are unusable as source material. Some are born-digital with a clean text layer; some are handwritten notes exported to PDF; some of those then carry red ink an instructor added live during class. The red ink often carries the actual content — worked steps, and answers filled into blanks deliberately left in the prepared notes.

The goal is to turn any of them into **Markdown or LaTeX with equations as text and figures as cropped images**, running locally.

---

## In scope

1. **Classify a page** before spending anything on it — text layer, handwriting, or blank.
2. **Extract the text layer** where one exists, without recognition.
3. **Separate annotation ink** from prepared content, by colour and by differencing against the un-annotated twin.
4. **Group ink into regions** and crop each to its own image, in reading order.
5. **Recognise handwritten mathematics** into LaTeX. *Model choice pending research.*
6. **Emit Markdown or LaTeX**, selected by flag.
7. **Assemble a final PDF** with equations as text and figures embedded, after which the intermediate crops can be deleted.

## Out of scope — the blacklist

Deliberate exclusions. Re-opening one needs a reason recorded in `docs/decisions/`.

| Excluded | Why |
| --- | --- |
| **Cloud OCR APIs on the core path** | Must run locally. A cloud model may be used to *evaluate* a local one, never as the shipped dependency. |
| **Full-page OCR on born-digital PDFs** | They already have a perfect text layer. Running a model over them is pure waste and *loses* fidelity. |
| **Re-typesetting whole documents** | The aim is extraction, not reproducing the instructor's layout. |
| **Training or fine-tuning a model** | Off-the-shelf weights only. Data collection and training is a different project. |
| **Handwriting recognition for prose** | Only *mathematics* has to survive as text. Prose annotation can stay an image. |
| **Anything over ~300 lines in one module** | A module past 300 lines is doing two jobs; split it. |
| **A rich CLI** | `file`, `page`, procedure, output format. Nothing else. |
| **Generic OCR for arbitrary documents** | Scoped to lecture material from this course family. Generalising is a later decision, not a design goal. |
| **GUI** | Command line only. |

### Distractions to name explicitly

Things that will look attractive mid-build and are not the job:

- Perfecting figure-crop boundaries beyond "a human can read it."
- Supporting every PDF producer in existence. Three kinds are known; handle those.
- Chasing state-of-the-art accuracy. **Good enough to check against the original** is the bar.
- Building a document database, search index, or web viewer.

---

## Constraints

| | |
| --- | --- |
| GPU | **RTX 3060 Laptop, 6 GB VRAM** — the hard limit on model choice |
| Stack | torch 2.7.0+cu126, CUDA available, Python 3.12, `uv` |
| Module size | under ~300 lines each |
| Determinism | `pdfops` and `ink` must never require a GPU |
| Source PDFs | never modified; all output to a chosen directory |

---

## Success

The tool reproduces, unattended, the transcript of one known page — two stem plots cropped, and three equations recovered as LaTeX including the two filled-in blanks. That page is the regression fixture: [`../../tmp/page5_transcript.md`](../../tmp/page5_transcript.md), verified against four independent readings.

---

## Open decisions

1. **Recognition model** — pending [`research/INDEX.md`](research/INDEX.md).
2. **Where output lands.** `tmp/` for now; real destination undecided.
3. **Whether the intermediate representation is a file format or just in-memory.** Matters if Markdown and LaTeX are both first-class.
4. **Whether this stays inside `electrical_notes` or becomes a bootstrap child.** Currently a subfolder.

---

**See:** [`roadmap.md`](roadmap.md) · [`todo.md`](todo.md) · [`README.md`](README.md)
