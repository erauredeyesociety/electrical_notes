# Layout mode decides whether math survives — not OCR

**Found:** 2026-09-05, on a 47-page born-digital LaTeX PDF supplied by the
skytracker_v2 session as a candidate OCR test case.
**Fixture:** `~/skytracker_v2/docs/research/pixel2voxel/sources/dual_camera_3d_localization_tutorial.pdf`
(Creator `LaTeX with hyperref`, Producer `xdvipdfmx`).

---

## The claim, and what was actually true

It arrived as: *"`pdftotext -layout` got the prose but DROPPED all rendered
equations — which are the load-bearing content"*, offered as a case for
equation-OCR.

**The equations were never dropped.** `-layout` preserves them. Measured over
the whole document:

| Extractor | Chars | Equations |
| --- | ---: | --- |
| `pdftotext -layout` | **135,744** | ✅ preserved, 2D spatial alignment intact |
| `pdftotext` (plain) | 108,796 | ❌ scattered into unordered fragments |
| PyMuPDF `page.get_text()` | 106,531 | ❌ flattened into reading order |

Page 7, Eq. (3), under `-layout`:

```text
                       Xc                    Yc
               u = fx     + c x ,    v =  f y c + cy ,      (3)
                       Zc                    Z
```

Numerator above, denominator below, aligned — mechanically reconstructable as
$u = f_x\frac{X_c}{Z_c} + c_x$. The `\underbrace` under the $K$ matrix even
survives as `| {z } / K`.

The **same page**, plain `pdftotext`:

```text
Xc
Yc
,
v
=
f
(3)
+
```

That is the "equations were dropped" symptom, and it comes from the extraction
mode — not from the PDF.

---

## The rule

> **For a born-digital PDF, whether math survives is decided by the extraction
> MODE, not by the document and not by OCR.** The glyphs are present with
> correct coordinates in all three cases. Only `-layout` keeps the geometry that
> makes them readable.

This is the same failure family as
[HW-01](../../../content/cesc_410/hw/reference_docs/findings.md) (a stacked
fraction flattening to `cos( 6π n)`), seen from the other side: there, `-layout`
*caused* a misread by flattening a fraction onto one line; here, its absence
destroys the equation entirely. Neither mode is safe on its own — **both are
lossy in different directions, and neither raises an error.**

### Consequence for the roadmap

**OCR is the wrong tool for this document.** Reaching for a VLM here would spend
GPU on recovering information that is already in the file. The split worth
holding:

| Document kind | Right tool |
| --- | --- |
| Born-digital LaTeX (`xdvipdfmx`, `pdfTeX`) | **Layout-aware extraction**, then reconstruct 2D math |
| Scanned / handwritten (ps160 textbooks, cesc_410 `-plw` lectures) | **OCR** — there is no text layer to preserve |

Conflating them makes the cheap fix wait on the expensive one.

---

## ⚠ It exposed a false negative in `ocr-handler inspect`

Run against this PDF:

```text
47 pages, 106,484 chars (2266/page)
verdict: text-layer-sufficient
  ok 47   sparse 0   empty 0
```

**That verdict is wrong for this document**, and wrong in the dangerous
direction. `textlayer.py` classifies on **character count per page**, so a page
whose prose is intact but whose math is mangled scores `ok` and is routed *away*
from further processing. The load-bearing content is missing and the tool
reports health.

Character count cannot see structure. Measured signals that can:

- **21% of pages (10 of 47)** contain a run of ≥4 consecutive lines of ≤3
  characters — the signature of a flattened matrix or stacked fraction.
- A `-layout` vs no-`-layout` **character-count delta of 27k (25%)** on the same
  file. A large delta means geometry is carrying meaning.

Both are cheap, and neither needs a model.

### What this changes

`textlayer.py`'s `ok / sparse / empty` verdicts answer *"is there text?"*. They
do not answer *"is the text faithful?"* — and this project exists because of the
second question. The classifier needs a structural axis alongside the density
one.

---

## ✅ Closed, 2026-09-05 — the structural faithfulness axis

`textlayer.py` now carries **two orthogonal axes**, and the same command reports:

```text
47 pages, 106,484 chars (2266/page)
verdict: text-layer-sufficient
  ok 47   sparse 0   empty 0
  ! structure-suspect-partial: 12/47 pages  (letter-spaced 0  shredded-lines 12)
    pages: 7, 8, 10, 11, 12, 16, 19, 26, 27, 28, 40, 41
    shredded-lines: a 2-D layout flattened into a column of fragments — a matrix,
      a stacked fraction, a `cases` brace
    the characters are present and correct — OCR is NOT the repair; re-extract
      with layout awareness or read the page image
```

Design, the output contract, and the sweep behind every constant:
[../plans/structural-faithfulness.md](../plans/structural-faithfulness.md).
Implementation: `src/ocr_handler/structure.py` (new), wired into
`textlayer.PageText.structure` / `.signals` and `DocText.structure_verdict`.

**The density axis is untouched.** `verdict`, `ocr_pages` and `needs_ocr` still
mean exactly what they meant, and a `suspect` page is deliberately **not** routed
to OCR — this finding's own rule says why: the glyphs are already in the file
with correct coordinates, so a model would spend GPU recovering what is present.
Two failures, two repairs. `test_suspect_page_is_not_routed_to_ocr` holds that.

### Which of the two proposed signals survived

| Signal proposed above | Outcome |
| --- | --- |
| Run of ≥4 consecutive lines of ≤3 chars | **Shipped**, as `shredded-lines`, widened to ≤4 chars and qualified by symbolic content. |
| `-layout` vs no-`-layout` char delta (27k / 25%) | **Rejected — it does not discriminate.** |

The delta **inverts on real documents**: `content/cesc_470/cesc_470.pdf`, a
prose-only syllabus with no mathematics anywhere, measures **+44%**, and a
computer-architecture slide deck **+51%** — both *worse* than this fixture's
+25%. It measures how much horizontal whitespace a page has (tables,
indentation, headers), which is not structural loss. It is also poppler-only,
and [ADR-0001](../decisions/0001-pymupdf-is-the-only-pdf-library.md) excludes
poppler as a dependency. Kept as a terminal diagnostic; not in the classifier
and not behind a flag.

The raw run test needed one qualifier to be usable: **≥25% of the run's lines
must carry symbolic content, and a bare numeral does not count.** Unqualified it
fires on `\lstlisting` line-number gutters (`5 . 6 . 7 . 8 .`), on plot axis
ticks, and on a Lego ruler's number scale — 97 documents, mostly wrong.

### Measured, both directions

Whole corpus, 460 documents / 7,245 pages, one 17-second `nice`d pass, no model,
no GPU. **436 pages (6.0%) flagged, in 118 documents.**

*False negative — closed.* Fixture: `structure-suspect-partial`, 12 of 47 pages.
All 12 carry a numbered display equation, so precision on the fixture is 12/12;
recall over its 18 equation-bearing pages is 12/18. The six misses are fractions
whose numerator is long enough (`x = f Xc` / `Zc ,`) that no run of ≤4-character
lines forms — the deliberate precision setting, not an oversight.

*False positives — the direction that matters more.* Four control documents:

| Document | pages | flagged |
| --- | ---: | --- |
| `content/cesc_470/hw/hw01/HW1.pdf` (LaTeX we generated) | 3 | **0** |
| `content/cesc_470/cesc_470.pdf` (born-digital syllabus, prose only) | 12 | **0** |
| `content/cesc_470/Module 01 …ISA (1).pdf` | 88 | 1 — the *documented* `C o m p u t e r` artefact |
| `content/cec_320/cec320-course-info-spring2026.pdf` | 9 | **0** |

Widened to 1,559 control pages (all of `cesc_470`, `cec_320`, `stat_412`): **4
hard false positives, 0.26%**, all four inside one 248-page code-companion PDF.
Where it does fire it fires on mathematics — `ee_300` 29%, `cec_315` 28%,
`cesc_410` 11%, `ps160` 7%, `cec_320` 0.3%.

*Hand-labelled sample*, 40 flagged pages drawn at random weighted by
flagged-page count: **33 flattened equations or symbolic tables, 5 flattened
figure axes / traceability matrices, 2 hard misfires** — strict precision 83%,
broad precision 95%, hard false-positive rate **5%**. Both misfires are in the
two 700+ page systems-engineering handbooks (a table of contents and a code
gutter).

It independently rediscovered the HW-01 defect this finding cites as the same
failure family: in
`content/cesc_410/hw/hw01/overleaf/p03_signal_transformations.pdf` the run
` /  /  / cos / (π / 6 n / )` **is** the stacked `π/6` that flattened to
`cos( 6π n)`.

### ⚠ It exposed a second false positive on the way out

`is_letter_spaced()` existed already, fired on **51 documents**, and fed
*nothing* — a footnote wired to no verdict and no page. Folding it in as the
axis's first detector made it verdict-bearing, and that is when its pattern,
`(?:\b\w\s){6,}`, turned out to be wrong: **`\s` matches a newline.** A plot's
tick labels extracted one per line — `1\n2\n3\n4\n5\n6` — scored as a corrupt
text layer, and **46 of the 51 documents fired on nothing else.**

| Pattern | Documents | Pages |
| --- | ---: | ---: |
| `(?:\b\w\s){6,}` — as shipped since M1, and the [corpus census](./corpus-census-2026-09-04.md) number | 51 | 154 |
| `(?:\b\w[^\S\n]){6,}` — horizontal whitespace only | 5 | 11 |
| `(?:\b[^\W\d_][^\S\n]){6,}` — six consecutive **letters**, horizontally spaced | **3** | **9** |

The final nine pages are all genuine: `C o m p u t e r  O r g a n i z a t i o n`,
`L E A R N I N G  O B J E C T I V E`, `T A B L E`, `F I G U R E`, `I N  B R I E F`.
Tightened; all three of its existing regression tests pass unchanged.

**The corpus census's "51 documents carry a corrupt text layer" is therefore an
overcount by roughly 17×.** Recorded here rather than edited into
[corpus-census-2026-09-04.md](./corpus-census-2026-09-04.md), which is a dated
point-in-time measurement.

*Cost, stated plainly:* a rotated axis label extracted vertically
(`C\no\nn\nt\nr\no\nl`, real in the NASA SE handbook) is no longer caught.
Separating that from a tick sequence needs a detector that can tell a word from
a number — a new detector, not a wider regex. Open question 3 in the plan.

### Left on the table, with its measurement

An **unmapped-glyph** detector — Private-Use-Area and control characters, i.e.
glyphs the extractor could not map to Unicode — fires on 54 documents / 235
pages and its hits are real (U+F8F1–F8F4 are Computer Modern's `\left\{`
pieces, so a `cases` environment reaches the reader as an unreadable box). It is
**not shipped**: its single commonest corpus-wide trigger is **U+F0B7, the
Symbol-font bullet, 1,514 occurrences** — every PowerPoint bullet in the corpus.
It needs a benign-glyph list first. A geometric *tight-stacking* signal was also
measured and rejected: it fires on 100% of pages in five assembly-listing
homework sets, because a monospaced listing has a tighter line pitch than the
prose around it.

**Status: closed.** Fixture retained as the regression case; the regression
tests build their own PDFs in-process, so the floor holds on a machine that has
neither the fixture nor the course material.

---

**Related:** [`../plans/structural-faithfulness.md`](../plans/structural-faithfulness.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md) ·
[`../plans/text-layer-first.md`](../plans/text-layer-first.md) ·
[`../research/engine-landscape-2026-09.md`](../research/engine-landscape-2026-09.md)
