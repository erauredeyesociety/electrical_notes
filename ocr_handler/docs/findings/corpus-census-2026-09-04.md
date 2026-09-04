# Corpus census — what `electrical_notes` actually contains

> Date: 2026-09-04 · Status: **Reference** (re-run when the corpus changes)
> Keywords: text layer, sparse, ocr-required, letter-spacing, corpus size, routing, leverage

## Summary

Ran `ocr_handler.textlayer.extract` over every PDF in `/home/devel/electrical_notes/content/`.
**430 documents, 7,146 pages.** Two thirds of pages already carry an adequate text layer; half of all
documents need no OCR anywhere. The annotated-ink path that the project was designed around serves
**2 documents**. This is the measurement that re-sequenced [../roadmap.md](../roadmap.md).

---

## Method

No new code. The census used the shipped `textlayer` module and its shipped thresholds
(`SPARSE_CHARS = 400`, `EMPTY_CHARS = 30`), so the numbers are exactly what `ocr-handler inspect`
reports today. Reproduce:

```python
import pathlib, collections
from ocr_handler import textlayer
root = pathlib.Path("/home/devel/electrical_notes/content")
docs, pages = collections.Counter(), collections.Counter()
for p in sorted(root.rglob("*.pdf")):
    if ".venv" in str(p) or "site-packages" in str(p): continue
    d = textlayer.extract(p)
    if not d.pages: continue
    docs[d.verdict] += 1
    for pg in d.pages: pages[pg.verdict] += 1
```

---

## Results

### Document verdicts — 430 documents

| Verdict | Count | Share |
| --- | ---: | ---: |
| `text-layer-sufficient` | 214 | 50% |
| `ocr-partial` | 188 | 44% |
| `ocr-required` | 28 | 6.5% |

Zero documents failed to open.

### Page verdicts — 7,146 pages

| Verdict | Count | Share |
| --- | ---: | ---: |
| `ok` | 4,790 | 67% |
| `sparse` | 1,736 | 24% |
| `empty` | 620 | 8.7% |

Of the 2,356 non-`ok` pages: **1,874 have embedded images** (content is present, in pixels — OCR can
recover it) and **482 have none** (nothing to recover; OCR would return nothing).

### By course

| Course | sufficient | partial | required |
| --- | ---: | ---: | ---: |
| cec_320 | 88 | 25 | — |
| stat_412 | 52 | 2 | 1 |
| cec_315 | 20 | 51 | 5 |
| ps160 | 10 | 23 | **15** |
| cesc_410 | 10 | 6 | 4 |
| cec_300 | 6 | 35 | 1 |
| syse_301 | 7 | 5 | — |
| ee_300 | 7 | — | — |
| cesc_420 | 7 | 6 | — |
| sys_304 | 5 | 15 | — |
| ae318 | — | 16 | 1 |
| cpsc_462 | 1 | 3 | 1 |
| cesc_470 | 1 | 1 | — |

### The 28 `ocr-required` documents — 400 pages

Dominated by **ps160** (scanned textbook chapters, review worksheets, worked problems) and the two
**cesc_410** handwriting decks. Largest:

| Pages | Document |
| ---: | --- |
| 95 | `ps160/m12/12_Lecture_Outline.pdf` |
| 60 | `ae318/AE318_export/AE318_Chapter 5_Textbook_Pages.pdf` |
| 35 | `ps160/m14/M14_textbook_chapter.pdf` |
| 33 | `ps160/m16/M16_textbook_chapter.pdf` |
| 29 | `ps160/m15/M15_textbook_chapter.pdf`, `ps160/m12/M12_textbook_chapter.pdf` |
| 10 | `cesc_410/lectures/f26_lctr02_DT signals and systems.pdf` **+ its `-plw` twin** |

### Letter-spacing artefacts — 51 documents

`textlayer.is_letter_spaced` fires on 51 documents — a text layer that is *present but corrupt*
(one glyph per text run: `C o m p u t e r`). Concentrated in **cec_315 lecture PDFs** (10 of the
`all_lectures/` set) and **cec_300 course content**.

**This is the only measured case where OCR should be preferred over a dense text layer**, and it is
therefore the natural evaluation set for `--mode both`.

---

## What this changes

1. **Leverage inverts the roadmap.** The extractor serves 430 documents; the annotated-ink path serves
   2 (`content/cesc_410/lectures/*-plw.pdf` — the only `-plw` files in the entire repository). Ink work
   was sequenced first; it is now sequenced after. → [../roadmap.md](../roadmap.md)
2. **The blank-page rule is measurable, not a guess.** 482 pages have no text and no images. `--mode auto`
   must skip them before rendering. → [../plans/text-layer-first.md](../plans/text-layer-first.md) § 2
3. **The genuine OCR need is ps160, not cesc_410.** An earlier scoping note asked whether courses other
   than cesc_410 had material that truly needs OCR. Answer: **yes — ps160 scanned textbook chapters**,
   plus `ae318` and parts of `cec_315`.
4. **44% `ocr-partial` is an upper bound on OCR need, not a measurement of it.** `sparse` is a 400-char
   heuristic; a diagram-heavy slide with 200 real characters is not broken. The threshold routes 1,736
   pages and has never been validated against a labelled sample. → [../scope.md](../scope.md) § Open decisions #3

## Caveats

- Thresholds are the shipped heuristics, unvalidated. Every "needs OCR" number inherits that.
- `content/` includes exam folders that duplicate lecture PDFs, so document counts contain duplicates.
  Page-level shares are unaffected in kind.
- The census does not count vector drawings, only embedded images. A page of pure vector figure with no
  raster image and no text would land in the "482 blank" bucket incorrectly.
  **`--mode auto` must count drawings as well as images before it trusts that rule.**

---

**Related:** [../plans/text-layer-first.md](../plans/text-layer-first.md) · [../roadmap.md](../roadmap.md) ·
[../scope.md](../scope.md) · `src/ocr_handler/textlayer.py` · `/home/devel/electrical_notes/tmp_ocr_child.md`
