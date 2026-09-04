# Scope

> **Status: Draft → needs operator confirmation on the six calls in § Open decisions.**
> Per bootstrap doctrine the human defines in/out. Everything here is a proposal; the
> Out-of-Scope blacklist is the load-bearing part.
> Rules that govern work here: [directives/INDEX.md](./directives/INDEX.md)
> Revised 2026-09-04 to reflect the **centralized-extractor** role and the **still-open engine question**.

**Kind:** Implementation project (deliverable is working code).

---

## Overview

`ocr_handler` is the **one text extractor for every course** in `electrical_notes`.
It turns a PDF into text — Markdown, plain text, or LaTeX — and it decides, per page,
whether that text can be read straight out of the file or has to be recognised from pixels.

It exists because the alternative already happened: three divergent per-course extractors
were written independently, disagreeing about what counts as a usable text layer
(`content/cesc_410/hw/tools/course_text.py` on poppler, `content/cpsc_462/tools/extract_notes.py`
on PyMuPDF, `content/cec_300/exam*/extract_pdfs.py` on PyMuPDF with no verdict at all).
One tool, one threshold, one honest verdict.

## Objectives

- **O1 — One extractor.** Every course calls `ocr-handler`; no course grows its own PDF reader.
- **O2 — Text-layer first, always.** Never spend a GPU second on a page whose bytes are already correct.
- **O3 — Say honestly what was and was not recovered.** A gap is reported, never silently skipped.
- **O4 — Recover the hard pages.** Handwritten lecture maths and scanned textbook pages become text.
- **O5 — Stay runnable with no GPU.** Everything except recognition is deterministic and cheap.

---

## The two problems, and their true sizes

They are different problems with different leverage. Measured 2026-09-04 across
`content/` — 430 PDFs, 7,146 pages, full census in
[findings/corpus-census-2026-09-04.md](./findings/corpus-census-2026-09-04.md):

| Problem | Serves | Status |
| --- | --- | --- |
| **A · Centralized text extraction** — read the text layer, classify each page, report the gaps | **430 documents / 7,146 pages** | backbone works (`textlayer.py` + `cli.py`) |
| **B · Annotated-lecture ink** — separate an instructor's live red ink and recognise the maths | **2 documents** (`content/cesc_410/lectures/*-plw.pdf`) | backbone works (`ink.py`), recognition unbuilt |

Problem B is where the project started and is still the technically interesting half.
Problem A is where the value is. **B must not be allowed to block A** — that inversion is
the main thing this revision fixes. See [roadmap.md](./roadmap.md) for the re-sequencing.

### The load-bearing insight

**Most pages need no recognition at all.** Measured: 4,790 of 7,146 pages (67%) carry an
adequate text layer today, and 214 of 430 documents (50%) need no OCR anywhere.
Routing on that before touching a GPU is the difference between a fast tool and a slow one.

**Two `-plw` files are not the same thing.** One producer means live ink was added; a matching
producer on both means the source was merely recompiled and the "annotation" is typed text
already in the text layer. Check the producer before assuming.

---

## In scope

1. **Classify a page** before spending anything on it — `ok` / `sparse` / `empty`, and a
   document-level verdict of `text-layer-sufficient` / `ocr-partial` / `ocr-required`.
2. **Extract the text layer** where one exists, without recognition.
3. **Four extraction modes** — text-layer only, OCR only, both side by side, and auto
   (OCR aimed only at the pages the text layer failed on). Contract:
   [plans/text-layer-first.md](./plans/text-layer-first.md).
4. **Report the gaps honestly** — which pages carry nothing, and which carry corrupted text
   (the letter-spacing artefact fires on 51 documents; a present text layer is not a correct one).
5. **Separate annotation ink** from prepared content, by colour and by differencing against
   the un-annotated twin.
6. **Group ink into regions** and crop each to its own image, in reading order.
7. **Recognise handwritten mathematics** into LaTeX. *Engine unresolved — see § Open decisions.*
8. **Emit Markdown, plain text, or LaTeX** from one intermediate, selected by flag.
9. **Assemble a final document** with equations as text and figures embedded, after which the
   intermediate crops can be deleted.
10. **Batch a directory** — only after one document works end to end.

## Out of scope — the blacklist

Deliberate exclusions. Re-opening one needs an ADR in [decisions/](./decisions/INDEX.md).

| Excluded | Tier | Why |
| --- | --- | --- |
| **Cloud OCR APIs on the shipped path** | permanent | Must run locally. A cloud model may *evaluate* a local one, never be depended on. |
| **Running a model over a page with a good text layer** | permanent | The bytes are already exact; recognition is lossy. This is the project's founding rule. |
| **Silently repairing extracted text** | permanent | Collapsing letter-spacing, de-hyphenating, re-flowing — all guesswork. Detect and report; never rewrite. |
| **Modifying a source PDF** | permanent | Everything writes to an output directory. |
| **Training or fine-tuning a model** | permanent | Off-the-shelf weights only. |
| **A GUI** | permanent | Command line only. |
| **Re-typesetting whole documents** | yes | The aim is extraction, not reproducing the instructor's layout. |
| **Handwriting recognition for prose** | yes | Only *mathematics* has to survive as text. Prose annotation can stay an image. |
| **Anything over ~300 lines in one module** | yes | Past that it is doing two jobs; split it. |
| **More than five CLI verbs** | yes | `inspect`, `extract`, `version` today. New capability arrives as a *mode or format value*, not a new verb. See § A note on the CLI. |
| **A document database, search index, or web viewer** | maybe later | Out of the extractor's job. The notes site consumes the output; it is not this tool. |
| **Non-PDF inputs** (`.docx`, `.pptx`) | maybe later | `content/cpsc_462/tools/extract_notes.py` handles `.docx` via pandoc. Absorbing that is a real question, not a design goal — see § Open decisions #6. |

### A note on the CLI — this replaces the old "no rich CLI" rule

The previous blacklist said "a rich CLI" was out of scope, listing `file`, `page`, procedure,
format. That rule now conflicts with an explicit requirement (four modes), so it is restated
rather than quietly broken: **the surface stays small by keeping the verb count fixed and
pushing variation into enumerated values of a few orthogonal flags.** A new capability that
needs a new verb is a scope question, not a coding task.

### Distractions to name explicitly

Attractive mid-build, and not the job:

- Perfecting figure-crop boundaries beyond "a human can read it."
- Supporting every PDF producer in existence. Three kinds are known; handle those.
- Chasing state-of-the-art accuracy. **Good enough to check against the original** is the bar.
- Tuning the `sparse` threshold on intuition. It gates 24% of all pages; move it only against a
  labelled sample (§ Open decisions #3).
- Building the ink/recognition half further while the 430-document text path is unfinished.

---

## Constraints

| | |
| --- | --- |
| GPU | **RTX 3060 Laptop, 6 GB VRAM** — the hard limit on model choice |
| Stack | torch 2.7.0+cu126, CUDA available, Python 3.12, `uv` |
| Module size | under ~300 lines each |
| Determinism | everything except recognition must run with no GPU; recognition runs at `temperature=0` |
| Source PDFs | never modified; all output to a chosen directory |
| Git | **human-only.** Agents propose commands; the operator runs them. |

---

## Success

Two criteria, because there are two problems.

**S1 — the extractor (Problem A).** `ocr-handler extract` reproduces, unattended, the output that
the three per-course scripts produce today, for every document each of them handles, and those
scripts are deleted. The verdict it reports agrees with a human's reading on a labelled sample.
*Currently unmet: no test covers `textlayer.py`, and no labelled sample exists.*

**S2 — the annotated lecture (Problem B).** The tool reproduces, unattended, the transcript of one
known page — two stem plots cropped, and three equations recovered as LaTeX including the two
filled-in blanks — verified against four independent readings.

⚠ **S2's ground truth is not in the repository.** It lives at
`/home/devel/electrical_notes/tmp/page5_transcript.md`, and `tmp/` is gitignored. The success
criterion is one `rm -rf` from being unverifiable. Fixing this is a roadmap item.

---

## Open decisions — operator input needed

These are named rather than invented. Each blocks or re-shapes something concrete.

1. **Recognition engine — deliberately unresolved.** Three candidates were measured on this GPU
   and all three fit. A separate research pass is re-examining the landscape and will land
   [research/engine-landscape-2026-09.md](./research/INDEX.md); assume nothing until it does.
   The operator's own steer stands: *"the example repos it might be picking apart might not be the
   best solutions either."* Decide by head-to-head on the fixture page, not by argument.
   → [decisions/0004-engine-choice-deferred-decide-by-head-to-head.md](./decisions/0004-engine-choice-deferred-decide-by-head-to-head.md)
2. **Where output lands.** `tmp/` today. Options: require `--out` always (no implicit destination);
   or a per-course `_extracted/` convention next to the source. **Recommend: require `--out`**, so
   nothing is ever written where it was not asked for.
3. **Is 400 chars/page the right `sparse` gate?** It classifies 1,736 pages (24%) as sparse. A
   diagram-heavy slide with 200 real characters is not broken. Needs a labelled sample of ~50 pages
   before the number is trusted or moved.
4. **Does `ocr_handler` physically leave `electrical_notes`?** The operator has settled that it is a
   child project under bootstrap doctrine. Whether it *moves* is separate — the tests reach into
   `../content/` for fixtures, and the parent repo is 625 MB.
5. **Is the structured intermediate a file format or in-memory only?** It becomes user-visible the
   moment `--mode both` writes a comparison. Proposal in
   [plans/text-layer-first.md](./plans/text-layer-first.md) § Intermediate.
6. **Does this absorb non-PDF inputs?** `.docx` via pandoc is what `cpsc_462` needs. If "the ONE
   text extractor for every course" means *every source type*, that is a larger project than the
   blacklist currently allows.

---

**See:** [roadmap.md](./roadmap.md) · [todo.md](./todo.md) · [README.md](./README.md) · [directives/INDEX.md](./directives/INDEX.md)
