# Converging the two page classifiers — what it actually changed

> Date: 2026-09-06 · Status: **Reference** (re-run when the corpus changes)
> Keywords: classifier convergence, poppler, PyMuPDF, ADR-0001, page kind, blank pages, vector drawings,
> get_cdrawings, get_image_info, Form XObject, must-not-break

## Summary

`pdfops.py` classified pages with poppler (`pdftotext` + `pdfimages` behind `subprocess`) and
`textlayer.py` classified them with PyMuPDF. Same 400-char rule, two libraries,
[ADR-0001](../decisions/0001-pymupdf-is-the-only-pdf-library.md) unsatisfied since 2026-09-02.

Converging them onto PyMuPDF **changes 428 of 7,187 corpus pages (5.95%)** — and the two causes are of
very different sizes and very different kinds:

| Cause | Pages | Verdict |
| --- | ---: | --- |
| Swapping the library (poppler → PyMuPDF) | **35** | Threshold noise. 24 of the 35 sit within 20 characters of the 400 gate. Neither library is "right". |
| Adding the vector-drawing term the plan already required | **406** | **A correction.** These pages were being called `blank` and they are full of content. |

**No page moves toward `blank`.** The converged classifier only ever discovers content the old one
missed, which is the only direction that is safe to change unattended.

**The `482 blank pages` figure quoted throughout the docs is a conflation, and the census itself said so.**
It counts pages with no text and *no images*. Once the drawing count the plan requires is applied, the
true skip set is **24 pages**, not 482.

⚠ **`ocr-handler inspect` output did not change on any page.** The user-facing verdicts
(`ok`/`sparse`/`empty`, `text-layer-sufficient`/`ocr-partial`/`ocr-required`) always came from PyMuPDF via
`textlayer`. The 428 pages are `pdfops.PageInfo.kind`, a routing label whose only consumers are the M4
ink path and the regression floor.

---

## Method

448 PDFs / 7,187 pages under `content/` — the corpus has grown since the
[census](./corpus-census-2026-09-04.md)'s 430/7,146. Both classifiers were run **per page**, faithfully:
the poppler side used the exact shipped code path (`pdfinfo`, then `pdftotext -f p -l p` and
`pdfimages -list -f p -l p`, one invocation per page), not a faster whole-document approximation.
Nothing failed to open on either side, and the two agreed on the page count of all 448 documents.

Three classifiers are compared:

| | chars from | images from | drawings |
| --- | --- | --- | --- |
| **A** old shipped | `pdftotext` | `pdfimages -list` | — |
| **B** library swap only | `page.get_text()` | `page.get_images(full=True)` | — |
| **C** shipped now | `page.get_text()` | `page.get_images(full=True)` | `get_cdrawings` + `get_image_info` |

---

## A → B · the library swap: 35 pages, and it is threshold noise

35 pages of 7,187 (0.49%) across 24 documents change `kind`:

| | pages |
| --- | ---: |
| `text` → `image` | 10 |
| `text` → `blank` | 9 |
| `image` → `text` | 7 |
| `blank` → `text` | 6 |
| `image` → `blank` | 2 |
| `blank` → `image` | 1 |

**24 of the 35 have the two character counts within 20 of each other.** They are pages sitting on the
400-character gate, e.g. `cpsc_462/class_materials/Introduction CPSC 462.pdf` page 24 — poppler 400,
PyMuPDF 399. Nothing is wrong with either count; the gate is a heuristic and 400 is
[still an open decision](../scope.md) (#3).

Across all 7,187 pages the two libraries agree exactly on 891, are within 5 characters on 3,053 and
within 20 on 5,215. Median difference −1, mean −0.9.

### The 11 larger disagreements are a whitespace policy difference

PyMuPDF preserves trailing spaces and blank lines between text objects; poppler collapses them and
reflows columns. Neither is more content. Two verbatim examples:

- `sys_304/.../02 Decision Making with Multiple Objectives 2.pdf` page 41 — poppler 263 chars, PyMuPDF
  404. The extra 141 characters are the layout whitespace inside a goal-programming constraint block.
- `ps160/midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf` page 3 — poppler 437, PyMuPDF 383. Here
  poppler's extra characters are *newlines from a column reflow*, and its reading order is the worse of
  the two: poppler yields `CV =\n\nf\nR\n2` where PyMuPDF yields `CV = f\n2R`. This is the same effect
  ADR-0001 was written about.

### Image counts differ on 1,773 pages, and that is definitional

Poppler counts more on 1,767 pages, PyMuPDF on 6. `pdfimages -list` enumerates image *placements* and
lists a soft mask as its own row; `get_images(full=True)` enumerates unique image XObjects in the page's
resources. On `sys_304/.../SYS 304 Test 1 Fall 2026 - Key.pdf` page 4 one 56×40 logo appears as two
poppler rows (`image` + `smask`). This almost never reaches `kind`, because the count is only consulted
when the text layer has already failed.

---

## B → C · the drawings term: 406 pages, and it is a correction

The [census](./corpus-census-2026-09-04.md) already flagged this as a caveat:

> *The census does not count vector drawings, only embedded images. A page of pure vector figure with no
> raster image and no text would land in the "482 blank" bucket incorrectly.*

**It does, and here is how often.** Of the 483 non-`ok` pages with zero images:

| drawings on the page | pages |
| ---: | ---: |
| 0 | 78 |
| 1 | 31 |
| 2–3 | 57 |
| 4–10 | 175 |
| more than 10 | 142 |

**405 of 483 carry vector content.** Rendered at 72 dpi to check they are not empty:

| page | chars | images | drawings | non-white pixels |
| --- | ---: | ---: | ---: | ---: |
| `cec_315/hw_practice_problems/lctr22-exercise.pdf` p1 | 0 | 0 | **1,837** | **8.93%** |
| `ps160/m14/M14_textbook_chapter.pdf` p33 | 0 | 0 | 883 | **20.61%** |
| `cec_315/all_lectures/cec315-lctr06-dt-lti-convolution.pdf` p9 | 17 | 0 | 0 | 0.05% |

The first two are full pages of content — a whole exercise sheet and a whole textbook page, drawn as
vector paths. Under the images-only rule both were `blank`: never rendered, never recognised, silently
absent from the output. The third is what a genuinely blank page looks like.

This is consistent with, and independent of, [ground-truth-sample.md](./ground-truth-sample.md), which
found the same class from the other end (idx 115, a full textbook page, image area 0.00, 502 drawings).
That finding proposes `drawings ≥ 40` as part of a *routing* predicate — "is OCR worth running here?".
The rule here answers a different and prior question — "is there anything on this page at all?" — and so
its threshold is simply *any*.

### One page needed more than a drawing count

`get_images(full=True)` misses an image **painted from inside a Form XObject**. Measured: 14 such pages,
of which one — `sys_304/.../SYS 304 Test 1 Fall 2026 - Key.pdf` page 6, a 56×40 logo — also has zero
drawings and was therefore routed `blank`. That was the only `image → blank` transition left in A → C,
i.e. the only page the convergence would have *lost*. `get_image_info()` finds it, and
`PageText.drawn_images` now carries it. Zero `empty`-verdict pages are affected, so the skip rule was
never at risk; `kind` was.

---

## The corrected blank-page number

| | pages |
| --- | ---: |
| Non-`ok` pages with no images — **the 482/483 figure** | 483 |
| …of those, also no drawings and no painted images | 78 |
| `empty`-verdict pages that are the actual skip set (`blank_pages`) | **24** |
| Pages OCR would be aimed at (`ocr_candidates`) | 2,329 |

**24, not 482.** Every doc that quotes 482 as "pages that must never be sent to a model" has been
corrected.

---

## Cost — why the counts are lazy

`drawings` is measured with `get_cdrawings()`, not `get_drawings()`: over all 7,187 pages the two return
an **identical count on every page**, and `get_cdrawings` costs 18.4 s against 83.4 s.

It is also measured **only where it can change an answer** — `verdict != "ok" and images == 0`, which is
483 of 7,187 pages. Eager `get_drawings()` on every page adds 83.4 s to a text pass that takes 15.8 s.
Lazy `get_cdrawings()` + `get_image_info()` on the 483 adds about 5 s to a ~26 s
`textlayer.extract` corpus pass (20–30% across four alternating runs; machine noise dominates the
spread). `inspect` is advertised as free and has to stay that way.

Where a count was not taken the field is `None`, never `0`. A measurement that was not made and one that
came back zero are different facts, and this project already has a lesson about detectors that report a
bare boolean.

---

## Must-not-break, checked rather than asserted

[roadmap.md](../roadmap.md) § M2 names four invariants.

| Invariant | How it was checked | Result |
| --- | --- | --- |
| **Text-layer output bytes** | SHA-256 of `to_markdown()` and `to_text()` for all 448 documents, before and after | **0 differ** |
| **Document verdict** | `verdict`, `structure_verdict`, `ocr_pages`, `suspect_pages`, per-page `verdict` and `images`, all 448 documents | **0 differ** |
| **Page classification** | per-page `kind`, all 7,187 pages, against the poppler baseline | **428 differ** — this document |
| **Reading order** | `ink.py` untouched; the floor test still passes | unchanged |

The CLI was checked too: 48 captured stdout/stderr runs and 6 output directories from
`ocr-handler text` are byte-identical to `ocr-handler extract --mode text`.

---

## What is still poppler

`pdfops.render()`, and deliberately. The two renderers differ on 6.66% of pixels from antialiasing
alone, and the ink path's constants are calibrated against poppler's pixels — `ink.red_mask` on the
fixture page yields a count the floor pins to 7,000–9,500, and `merge_px = 64` is a pixel distance
measured at 200 dpi. Swapping the renderer without re-sweeping both would move numbers the regression
floor is guarding. That is [roadmap.md](../roadmap.md) **M4**, which serves the 2-document ink path.

---

## Reproduce

```sh
cd /home/devel/electrical_notes/ocr_handler
uv run python - <<'PY'
import collections, pathlib
from ocr_handler import textlayer
root = pathlib.Path("/home/devel/electrical_notes/content")
docs, pages, blank, cand = collections.Counter(), collections.Counter(), 0, 0
for p in sorted(root.rglob("*.pdf")):
    if ".venv" in str(p) or "site-packages" in str(p): continue
    d = textlayer.extract(p)
    if not d.pages: continue
    docs[d.verdict] += 1
    blank += len(d.blank_pages); cand += len(d.ocr_candidates)
    for pg in d.pages: pages[pg.verdict] += 1
print(dict(docs), dict(pages), "blank", blank, "candidates", cand)
PY
```

---

**Related:** [corpus-census-2026-09-04.md](./corpus-census-2026-09-04.md) ·
[ground-truth-sample.md](./ground-truth-sample.md) ·
[../decisions/0001-pymupdf-is-the-only-pdf-library.md](../decisions/0001-pymupdf-is-the-only-pdf-library.md) ·
[../plans/text-layer-first.md](../plans/text-layer-first.md) · [../roadmap.md](../roadmap.md) ·
`src/ocr_handler/{pdfops,textlayer}.py`
