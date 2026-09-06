# Classical OCR engines and PDF→Markdown pipelines

> Date: 2026-09-05 · Status: **Research** · Scope: **no VLM, no model server**
> Systems that install as an ordinary Python package or CLI tool. Fetching weights from a hub
> is fine; standing up ollama / vLLM / an HF serving stack is not.
> Numbers marked **measured** were run today on this machine (RTX 3060 Laptop 6 GB, 8 cores,
> single-process, `nice -n 10`, `OMP_NUM_THREADS=3`). Everything else is cited.
> Companion to [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md), which covers the
> VLM half. This document **does not contradict** it; it covers the ground it excluded.
>
> It also pairs with [`../plans/structural-faithfulness.md`](../plans/structural-faithfulness.md),
> landed in parallel today. That plan builds the **detector** — which pages have text that is present
> but not faithful. This document supplies the **remedy** it names: §1.1 identifies the layout-aware
> re-extraction mode, and §1.4 shows the shredded equations can be reassembled rather than merely
> flagged.

---

## Verdict up front

**Yes for the born-digital half — decisively, and with more upside than expected.
No for the scanned half's mathematics, but the prose is recoverable cheaply.**

| Corpus need | Pages | No-VLM answer | Confidence |
| --- | ---: | --- | --- |
| **Born-digital LaTeX** (pdfTeX / xdvipdfmx) | 2,594 | **Geometry-based extraction. No model, no OCR.** 4,202 fractions already recovered mechanically at ~92% precision. | **high — measured** |
| **Scanned textbook chapters** (ps160 etc.) | ~400 | **OCRmyPDF for the prose.** Verdict flips `ocr-required` → `text-layer-sufficient`, 6/6 pages, 3,729 chars/page. | **high — measured** |
| **The equations on those scanned pages** | — | **No. Nothing classical reads them.** Tesseract destroys every 2-D expression and emits confident Latin garbage in its place. | **high — measured** |

The load-bearing result is §1: **the fraction bars, radicals and matrix delimiters in a LaTeX
PDF are vector rectangles and CMEX glyphs, sitting in the file with exact coordinates.** Nothing
has to be recognised. A ~90-line probe pulled 4,202 fractions out of the real corpus in one
single-threaded pass. That is a bigger, cheaper win than any engine in this document.

The honest counterweight is also in §1: **MaxTract built exactly this in 2012 and scored 37% on
full formula structure.** The gap between our 92% and their 37% is real and explainable — we are
measuring one relation on one document class, they measured whole-formula reconstruction on
arbitrary papers — and §1.6 says precisely where the remaining 55 points go.

---

## 0. What was run, and what it cost

| | |
| --- | --- |
| Corpus scan v1 (fonts + rules, 430 PDFs / 7,144 pages) | **182 s**, one process, load 2.8–5.1 |
| Corpus scan v3 (with discriminators, 430 PDFs) | **~300 s**, one process |
| `pdftotext -layout`, 47-page doc | **0.08 s** |
| `pymupdf gettext -mode layout`, same doc | **0.35 s** |
| Tesseract 4.1.1, one 2550×3300 (300 dpi) scan | **3.7–4.4 s**, **133 MB** peak RSS, 1 thread |
| OCRmyPDF `--redo-ocr --jobs 2`, 6 scanned pages | **61 s** (10.2 s/pg), **561 MB** peak RSS |
| OCRmyPDF `--force-ocr --jobs 2`, same | **21 s** (3.5 s/pg), **319 MB** peak RSS |

Load average never exceeded 5.7 and was ~5.0 before this work started (another session held a
python process at 262% CPU throughout). Nothing here approached the failure mode.

> ⚠ **Two installs were made. Both are removable; one is outside `tmp/`.**
>
> - `tmp/classicalvenv/` (106 MB, gitignored) — `ocrmypdf` 16.13.0 and deps.
> - **System packages via `apt`:** `tesseract-ocr` 4.1.1, `tesseract-ocr-eng`, `tesseract-ocr-osd`.
>   Tesseract has no pip distribution, and OCRmyPDF cannot run without the binary. `libtesseract4`
>   was already present; only the CLI and two data files were added.
>   Undo: `sudo apt-get remove tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd`.
> - Probe scripts and fixtures live in `tmp/classical/` (33 MB, gitignored).
> - **No git commands were run.**

---

## 1. Layout-preserving extraction — the highest-value finding

### 1.1 Correction: PyMuPDF has a layout mode, and it beats `pdftotext -layout`

[`findings/layout-mode-decides-whether-math-survives.md`](../findings/layout-mode-decides-whether-math-survives.md)
compared `pdftotext -layout` against **PyMuPDF `page.get_text()`** and concluded poppler won.
That comparison was mode-mismatched: `get_text()` is PyMuPDF's *simple* mode. Re-measured on the
same 47-page fixture:

| Extractor | Chars | Time | Equation geometry |
| --- | ---: | ---: | --- |
| **`pymupdf gettext -mode layout`** | **170,105** | 0.35 s | ✅ preserved, superscripts on their own line |
| `pdftotext -layout` | 135,744 | 0.08 s | ✅ preserved |
| `pdftotext` (plain) | 108,796 | 0.08 s | ❌ |
| `pymupdf gettext -mode blocks` | 108,275 | 0.18 s | ❌ |
| `pymupdf gettext -mode simple` (= `get_text()`) | 108,275 | 0.16 s | ❌ |

Page 7, Eq. (3), under `pymupdf -mode layout` — note the superscript `c` is on a separate row,
which `pdftotext -layout` merged into `Xc`:

```text
                             c                        c
                          X                        Y
                u = fx           + cx,     v = fy          + cy,          (3)
                             c                        c
                          Z                        Z
```

**Consequence: [ADR 0001 (PyMuPDF is the only PDF library)](../decisions/0001-pymupdf-is-the-only-pdf-library.md)
survives intact.** There is no reason to shell out to poppler for layout mode. The implementation
is `page_layout()` in `pymupdf/__main__.py` — a module-level pure-Python function, importable
today, ~225 lines over `rawdict`. It is not a documented public API; either call it or
reimplement it, but do not add a poppler dependency for it.

`pdfops.py` still shells out to `pdftotext`/`pdftoppm`/`pdfinfo`/`pdfimages`. This finding
removes the last argument for keeping that.

### 1.2 The signals that are actually in the file

Measured on the fixture page (47-page LaTeX tutorial, `xdvipdfmx`):

```text
chars=2439   math-font chars=428 (18%)
distinct (font,size) pairs=15
   1738  LMRoman10-Regular  10.91     <- prose
    162  CMMI10             10.91     <- math italic
    134  CMR10              10.91
     55  CMMI8               7.97
     24  CMEX10             10.91     <- extensible delimiters, braces
     15  CMSY10             10.91     <- math symbols
```

Three signals, all free, all deterministic:

1. **Font family separates math from prose with no ambiguity.** `CMMI`/`CMSY`/`CMEX`/`CMMIB` are
   TeX math fonts; `LMRoman`/`LMSans` are the prose. Available per span in `rawdict`.
2. **Fraction bars are vector rectangles, not glyphs.** `page.get_drawings()` returns them; better,
   **`get_text("rawdict", flags=TEXT_COLLECT_VECTORS)` returns them inline in the block sequence**
   as `type: 3` blocks with `stroked: True, isrect: True`. Verified present in the pinned
   pymupdf 1.28.2 (`TEXT_COLLECT_VECTORS = 1024`):

   ```text
   block types with COLLECT_VECTORS: {0: 57, 3: 15}
     bbox=(245.14, 99.66, 259.64, 100.10)  stroked=True  isrect=True   <- \frac bar, Eq (3) left
     bbox=(342.11, 99.66, 355.47, 100.10)  stroked=True  isrect=True   <- \frac bar, Eq (3) right
   ```

   One pass, one call. Cheaper than a separate `get_drawings()`.
3. **Matrix delimiters are CMEX10 glyphs in the private-use area.** Eq. (4)'s 3×3 matrix appears as
   `U+F8EE`/`U+F8F0` (upper/lower left bracket) and `U+F8F9`/`U+F8FB` (right), in three matched
   pairs at x = (203.8, 217.3), (239.1, 297.2), (306.3, 327.6) — exactly the three bracketed groups.

### 1.3 ⚠ The default character bboxes are wrong

PyMuPDF, PDFMiner and PDFBox all compute character boxes from *font metrics*, not glyph outlines.
Shah, Dey & Zanibbi (ICDAR 2021) name this explicitly: the PDF baseline coordinate *"does not take
character kerning, font-weight, ascent, descent, etc., into account"*, and they had to intercept the
rendering pipeline to fix it ([SymbolScraper paper](https://shahayush.com/files/Shah2021_MathSeer.pdf)).

**PyMuPDF now fixes this natively and the flag is in our pinned version.** Measured on the fixture page:

```text
TEXT_ACCURATE_BBOXES:  2044 of 2439 chars change bbox  (84%)
  'D' (68.03, 38.28, 74.69, 47.25) -> (68.03, 39.28, 74.69, 45.51)
  'u' (74.69, 38.28, 79.45, 47.25) -> (74.69, 41.53, 79.45, 45.61)
  '-' (86.08, 38.28, 89.16, 47.25) -> (86.08, 43.24, 89.16, 43.79)
```

Default boxes are the full em height for every glyph. **Every vertical-relation test — is this
above the bar, is this raised enough to be a superscript — is unreliable without
`TEXT_ACCURATE_BBOXES`.** This is non-negotiable for any reconstruction work.

### 1.4 Mechanical reconstruction — it works, and here is the code path

`tmp/classical/frac_recon3.py`, ~90 lines, numpy-free, model-free:

```python
rules      = [b for b in blocks if b["type"] == 3 and b["isrect"] and b["stroked"]]
numerator  = glyphs centred on the bar, 0.5–13 pt ABOVE it
denominator= glyphs centred on the bar, 0.5–13 pt BELOW it
superscript= size < 0.82 × prev AND baseline lifted > 0.9 pt AND x-adjacent
subscript  = size < 0.82 × prev AND baseline dropped > 0.4 pt AND x-adjacent
```

Fixture page 7, all four display fractions recovered exactly:

```text
  \frac{Xc}{Zc}        \frac{Yc}{Zc}        \frac{∂θ}{∂u}        \frac{1}{fpx}
  superscripts: X^c  Z^c  r^2  r^4  r^6  x^2  y^2
  subscripts:   f_x  c_x  f_y  c_y  P_i  K_i  R_i  C_i
```

**`\underbrace` is the first false-positive family, and it is cleanly discriminable.** TeX draws it
as CMEX brace pieces *plus* a rule at the same y. A real `\frac` bar never has a CMEX glyph sitting
on it:

```text
bar y=196.8:  '|' CMEX10 dy=-2.58   '{' CMEX10 dy=-2.58   '{z}' CMEX10   -> brace, suppress
bar y= 99.9:  no CMEX glyph within ±3.5 pt                              -> genuine \frac
```

With that one test the fixture page goes to **4 fractions, 6 brace rules suppressed, 0 errors.**

### 1.5 Corpus scale — measured over all 430 documents

One process, 300 s, no threads, no GPU:

| Producer class | Docs | Pages | Fractions recovered | Est. precision |
| --- | ---: | ---: | ---: | ---: |
| **TeX** (`pdfTeX`, `xdvipdfmx`, `XeTeX`, `LuaTeX`, `dvips`) | 275 | 2,594 | **4,202** | **~92%** |
| Everything else (Word, InDesign, PowerPoint, scanners) | 155 | 4,550 | 672 | **~8%** |

212 of 430 documents (49%) carry TeX math fonts. Fractions land on 1,015 distinct pages.

Precision estimated by eye on a seeded random sample of 25 from each bucket (`random.seed(11)`).
Criterion: *is the numerator/denominator split structurally correct?* — not *is every glyph perfect*.

**TeX bucket — 23/25 correct, 1 false positive, 1 glyph defect:**

```text
✓ \frac{TC}{1−η}                          ps160/m20/M20_Review.pdf
✓ \frac{(n1−1)s21+(n2−1)s22}{n1+n2−2}     stat_412/QZ08/solutions/q08.pdf   (pooled variance)
✓ \frac{ejθ−e−jθ}{2j}                     cec_315/…lctr09-ct-fourier-series.pdf
✓ \frac{2s+6}{(s+1)(s+3)}                 cec_315/…lctr17-inverse-laplace.pdf
✓ \frac{ωd}{(s+a)2+ωd2}                   cec_315/exam3/…lctr17
✓ \frac{1}{1−1.2z−1}                      cec_315/…lctr21-unilateral-z.pdf
~ \frac{QMi=1(s−zi)}{QNi=1(s−pi)}         structure right, ∏ extracted as 'Q'  (ToUnicode defect)
✗ \frac{HeightclassOProbabilityE}{<156.05320.225633.17}   stat_412/QZ08/solutions/q02.pdf — a TABLE
```

**Non-TeX bucket — 2/25 correct.** Essentially all table borders and TOC dot leaders:

```text
✗ \frac{NPR7123.1Process}{TheCenterDirectorsordesigneesestab­}   NASA SE Handbook p238
✗ \frac{References}{Appendices}                                   NASA SE Handbook p220
✗ \frac{6.6}{66..78}                                              NASA SE Handbook p24 (TOC leaders)
✓ \frac{P}{tb}                                                    NASA SE Handbook p301
```

**The discriminator is the producer, and `pdfops.producer()` already reads it.** A geometric
centering-and-containment test was tried and did *not* rescue the non-TeX documents — table rules
have centred short text above and below just like fractions do. Gate on the producer; do not tune
geometry against Word output.

### 1.6 What this does *not* solve — the MaxTract number

**MaxTract** (Baker, Sexton & Sorge, CICM 2012) is the direct precedent and it is worth reading before
over-committing. It did exactly this — glyph name + TeX font name + size → linear grammar → LaTeX —
and against InftyReader on 5 papers × 2 pages:

| | Infty | **MaxTract** |
| --- | ---: | ---: |
| Characters misrecognised | 53/5/5/1/3 | **0 / 0 / 0 / 0 / 0** |
| Formula structures correct (of 628) | 550 (~88%) | **235 (~37%)** |
| — expression split | 40 | **172** |
| — space differences | 2 | **103** |
| — additional characters | 10 | **102** |

*Perfect at the symbol layer, 37% at the structure layer.* Their own slide: "Layout analysis still
naive." The three failure families, and how they map onto us:

1. **Segmentation — where does a formula start and stop?** 172/628. This information is genuinely not
   in the PDF. Both labs that went furthest (Birmingham, RIT) ended up rendering the page to an image
   and running a detector for exactly this step. **Our 92% number does not measure this at all** —
   it measures one relation given a bar. This is the single biggest gap between the two numbers.
2. **Spacing semantics.** 103/628. TeX emits `\,` `\;` `\quad` as pure kerning. From coordinates you
   see a gap; you cannot recover whether it meant `f(x)`, `f x`, or `f\,x`. Destroyed at typesetting
   time; unrecoverable in principle.
3. **ToUnicode.** TeX PDFs are the worst case — CM subsets often carry no usable CMap. We observed
   exactly one instance in the sample (`∏` → `Q`) and correct extraction of `∂ θ ω √ η ⊤ σ`, so our
   corpus is mostly healthy — but this must be spot-checked per document class, not assumed.

MaxTract is **not usable**: [`zorkow/MaxTract`](https://github.com/zorkow/MaxTract) is an OCaml stub
with **no licence file**, and the Birmingham binary download page now 307-redirects to the department
homepage. UNVERIFIED whether [`trenta3/maxtract-docker`](https://github.com/trenta3/maxtract-docker)
still builds; its own README warns the LaTeX "needs some tuning by hand."

**SymbolScraper** (RIT, Apache-2.0, Java/PDFBox) is the only other published work that uses PDF rules
as a math signal, and it flags the same thing we hit: *"Some additional work is needed to improve the
discrimination between different line types."* Its pipeline then renders at 600 dpi and runs a CNN for
region and structure — i.e. the leading born-digital math lab uses mechanical extraction for symbols
**only**.

**ChemScraper** (same lab, IJDAR 2024) is the encouraging counter-example: fully mechanical born-digital
parsing, no GPU/OCR/vectorisation, **98.4%** on USPTO — *for chemistry*, a far more constrained visual
language than mathematics. It proves the technique is sound; it does not prove it transfers.

### 1.7 The 2026 bar this has to clear

Horn & Keuper, *Benchmarking Document Parsers on Mathematical Formula Extraction from PDFs*
([arXiv:2512.09874](https://arxiv.org/abs/2512.09874), Best Scientific Paper ICPR 2026), 100 synthetic
LaTeX PDFs, 1,411 inline + 641 display formulas, LLM-as-judge (r=0.78 with 30 human raters):

| Rank | Parser | Score /10 |
| ---: | --- | ---: |
| 3 | **PaddleOCR-VL (0.9B)** | **9.65** |
| 6 | **PP-StructureV3 (<0.3B)** | **9.34** |
| 17 | PyPDF | 7.69 |
| 19 | PyMuPDF4LLM | 6.67 |
| 21 | GROBID | 5.70 |

Read this carefully, because it cuts both ways. Their own note: *"Rule-based tools such as pypdf and
pymupdf4llm output Unicode symbols exclusively."* **Those scores measure the absence of a
reconstructor, not a bad one.** No entry in that table attempts what §1.4 does. But the bar is real:
a sub-0.3B CPU-runnable model already scores 9.34, so mechanical reconstruction has to be *good*, not
merely *free*, to justify itself. Its advantages are that it is exact where it fires, deterministic,
and produces no hallucination — which the blacklist's "silently repairing extracted text" rule values
more than a benchmark does.

### 1.8 Everything else in this category

| Tool | Licence | Per-char bbox | Font/size | Vectors | Verdict |
| --- | --- | :-: | :-: | :-: | --- |
| **PyMuPDF `rawdict`/`xml`** | AGPL-3.0 | ✅ | ✅ | ✅ `COLLECT_VECTORS` | **already the project's dependency; nothing beats it** |
| pdfplumber | MIT | ✅ | ✅ | ✅ `.rects`/`.lines` | duplicates PyMuPDF; `layout=True` is documented-experimental |
| pdfminer.six | MIT | ✅ `LTChar` | ✅ | ✗ | subset of pdfplumber; open bug "Math formula position detected wrongly" (#490) |
| `pdftotext -bbox-layout` | GPL-2 | ✗ **word only** | ✗ **none** | ✗ | **cannot support this work** — the bbox output drops fonts entirely |
| pdfalto | GPL-2 | ✗ token | ✅ + sup/sub flags | ✅ SVG | good geometry source; GPL, C++ binary |
| pdftext (datalab) | Apache-2.0 | ✅ | ✅ | ✗ | best-*licensed* base layer if AGPL ever bites |
| pymupdf4llm | AGPL-3.0 | — | — | — | **no math handling at all**; headers by font size. Scored 6.67 |
| markitdown (MS) | MIT | — | — | — | no equation extraction for PDF |
| docling (IBM) | MIT | — | — | — | **uses models**; formula→LaTeX needs `do_formula_enrichment` (off by default) |
| unstructured | Apache-2.0 + paid | — | — | — | no math |

> **Note on `pdftotext -bbox-layout`.** It emits `<word xMin=… yMin=… xMax=… yMax=…>`. Poppler's
> internal `TextWord` exposes `getFontName()`/`getFontSize()`, but `pdftotext` does not serialise
> them. So the 135,744-char `-layout` output is **a rendering, not a data structure** — it has
> already thrown away the single most valuable signal. UNVERIFIED at the printf level (freedesktop
> GitLab is behind a bot wall); inferred from the header + man page.

---

## 2. Surya + Marker (datalab)

### 2.1 ⚠ The licence premise in the brief is stale — and the answer is better than feared

The reported README-vs-LICENSE `$5M`-vs-`$2M` contradiction **does not exist today**. Both say $5M.
Raw files fetched:

| Source | Figure |
| --- | --- |
| `marker/LICENSE`, `surya/LICENSE` | **plain Apache-2.0**, 11,358 / 9,135 bytes. Zero dollar thresholds. |
| `marker/MODEL_LICENSE`, `surya/MODEL_LICENSE` | byte-identical (md5 `377611a1c22328e4dc2fb13bd7d04e4d`), AI Pubs OpenRAIL-M (Modified), **$5,000,000** |
| marker README L65, surya README L69 | **$5M** |
| **`datalab.to/pricing`** | **$2M** ← stale marketing, contradicts their own licence |

**The `$2M` was real, historically.** Commit archaeology:

| Date | What happened |
| --- | --- |
| 2023-11-17 → 2025-08-20 | code **GPL-3.0** |
| 2025-08-20 | `LICENSE` replaced with OpenRAIL-M **$2,000,000** while the README still said GPL — genuinely contradictory for two months |
| 2025-10-20 | `LICENSE` reverted to GPL-3.0; `MODEL_LICENSE` added separately the next day |
| 2026-05-14 / 2026-07-17 | code relicensed **GPL-3.0 → Apache-2.0** |
| 2026-07-20 | threshold **$2M → $5M**, in a commit titled **"Swap to uv"**, no release note |

**Terms that actually apply** (`MODEL_LICENSE`, Attachment A §2, verbatim):

> (a) … generated more than five million US Dollars ($5,000,000) in gross revenue in the prior year,
> except where Your Use is limited to personal use or research purposes;
> (b) … has raised more than five million US dollars ($5,000,000) in total equity or debt funding …
> (c) … provides or otherwise makes available any product or service that **competes** with any
> product or service offered by … Licensor or any of its affiliates.

- Clause (c) has **no threshold and no research carve-out**.
- The restrictions attach to **Output**, not just weights — clause 1(k) defines Output as
  *"the results of operating a Model"*. A >$5M entity is restricted from commercial use of the
  converted Markdown.
- Clause 1(e) forbids distillation / training on Surya output.
- Personal and academic coursework use, which is this project, is **unambiguously permitted**.

### 2.2 The disqualifier is architectural, not legal

**Surya 2 is a 650M-parameter Qwen3.5 VLM.** From `surya/settings.py`:
`# ---- Surya2 inference (VLM-backed: vllm | llamacpp) ----`. README: *"Layout / OCR / table_rec all
share one VLM, served either by `vllm` (GPU) or `llama.cpp` (CPU / Apple Silicon)."*

**That is precisely the shape this brief excludes.** Standing up `vllm` or `llama-server` is a model
server. The only classical components left are a 76.9 MB EfficientViT line detector and a 134.9 MB
rf-detr layout model.

| Model | Role | Size |
| --- | --- | ---: |
| `datalab-to/surya-ocr-2` | OCR + layout + tables (one VLM) | 1,372 MB bf16 |
| `surya-ocr-2-gguf` | same, llama.cpp | 1,266 MB + 205 MB mmproj |
| `surya_layout2` (rf-detr-large) | fast layout + reading order | 134.9 MB + 7.1 MB |
| text detection (EfficientViT) | line detection | 76.9 MB |
| ocr error detection (DistilBERT) | garbled-text classifier | 270.7 MB |

`VLLM_GPU_MEMORY_UTILIZATION = 0.85` — vLLM grabs 85% of the card regardless of the 1.4 GB of
weights. On a 6 GB laptop card shared with a desktop, that is hostile. bf16 needs compute ≥ 8.0
(our 3060 clears it).

### 2.3 Math without a VLM: 23.4, and with `--disable_ocr`: 0.0

Marker's own olmocr-bench table (vendor-run, AI2's benchmark, official checker):

| Category | balanced (GPU VLM) | fast (CPU-ish) | **no OCR (pure CPU)** |
| --- | ---: | ---: | ---: |
| **arXiv math** | 83.9 | **23.4** | **0.0** |
| Old scans math | 63.8 | 59.8 | **0.0** |
| Multi column | 76.6 | 76.0 | 67.0 |
| Overall | 76.0 | 66.6 | 43.6 |

Their own caveat: *"`--disable_ocr` never calls the VLM: math scores zero (equations have no
text-layer LaTeX)."* **The only Marker configuration that satisfies our constraints scores 0.0 on
mathematics.** CPU VLM throughput on Metal is 0.108 pages/s (~9.3 s/page sustained, 129 s p95);
no x86 CPU figure is published — **UNVERIFIED**.

`texify` is dead — `datalab-to/texify` 404s, `VikParuchuri/texify` is archived (GPL-3.0, last push
2025-01-29), and marker 2.0.0 has no texify dependency. Math is native to the VLM now.

### 2.4 Composition

**Marker duplicates region detection.** `LayoutBuilder` runs either the VLM layout model or rf-detr
and imposes its own 24-type block taxonomy (`Equation`, `Figure`, `Handwriting`, `TextInlineMath`, …).
The only bypass is `force_layout_block`, which is all-or-nothing per document. **Adopting Marker means
adopting a second, disagreeing layout opinion alongside `ink.py`.**

Status: marker v2.0.0 and surya v0.22.1, both 2026-07-20. No code commits since (CLA bot only,
through 2026-09-05).

---

## 3. docTR (Mindee)

**Code Apache-2.0.** Weights: **no licence statement exists anywhere in the project** — they are served
from `doctr-static.mindee.com` and GitHub release assets, not an HF org with a card. UNVERIFIED.
Open issue #1730 argues docTR is not usable as Apache-2.0 because it pulls **GPLv2+ dependencies**
(`Unidecode` directly, `Pyphen` via weasyprint); no maintainer resolution.

**Math: structurally impossible, and this is the sharpest finding in this section.** Every pretrained
recognition model ships `VOCABS["french"]`, verified across `crnn_vgg16_bn`, `crnn_mobilenet_v3_*`,
`master`, `parseq`, `sar_resnet31`, `vitstr_*`:

```python
VOCABS["latin"]   = digits + ascii_letters + punctuation
VOCABS["english"] = VOCABS["latin"] + "°" + "£€¥¢฿"
VOCABS["french"]  = VOCABS["english"] + "àâéèêëîïôùûüçÀÂÉÈÊËÎÏÔÙÛÜÇ"
```

**126 characters. No Greek. No `∫ ∑ ∏ ∂ ∇ √ ± × ÷ ≤ ≥ ≠ ≈ ∞`.** A CTC/attention decoder cannot emit a
character outside its charset. An `ancient_greek` vocab and a `latex` vocab exist in `vocabs.py`, but
**no released checkpoint uses either** — and issue #591 notes you cannot fine-tune onto a different
vocabulary because the head shape changes.

Worse: **v1.1.0 (2026-08-21) added a layout model that boxes formulas but cannot read them.**
`lw_detr_s/m` predict the 11 DocLayNet classes including `Formula`. So docTR can now locate an equation
and hand it to a 126-character Latin word recogniser. **That combination is worse than nothing — it
produces confident-looking garbage where a gap would have been honest**, which is exactly what
[`scope.md`](../scope.md)'s "report the gaps honestly" rule exists to prevent.

Sizes and CPU speed (official benchmarks, i7-11800H CPU):

| Model | Params | ≈ fp32 | CPU |
| --- | ---: | ---: | --- |
| db_resnet50 (detect) | 25.4 M | ~102 MB | 1.1 s/page |
| crnn_vgg16_bn (recog) | 15.8 M | ~63 MB | 0.6 s / batch-64 crops |
| db_mobilenet_v3_large + crnn_mobilenet_v3_small | 4.2 + 2.1 M | ~25 MB | fastest CPU combo |
| master | 58.7 M | ~235 MB | **17.6 s / batch-64 — unusable on CPU** |

Document accuracy is published only on FUNSD (scanned forms) and CORD (receipts), neither remotely
like a textbook page: end-to-end db_resnet50+crnn_vgg16_bn = 73.4 R / 76.1 P on FUNSD.
**OnnxTR** (Apache-2.0, no torch) is the right CPU route if docTR is ever wanted: ~0.15 s/page with
OpenVINO.

**Verdict: excellent for making prose searchable, disqualified for this corpus by its charset.**

---

## 4. Tesseract — measured on our own scans, and precisely why it is not enough

Apache-2.0, current release 5.5.3 (2026-07-24). Installed here: **4.1.1** (Ubuntu 22.04 archive).

### 4.1 Why math is structurally impossible, from the source

1. **The LSTM engine is a *line* recogniser.** Official doc: *"The Tesseract 4.00 neural network
   subsystem is integrated into Tesseract as a line recognizer."*
2. **Decoding is CTC over a 1-D sequence** — *"a line graph of strength of output against image
   x-coordinate."* A fraction bar, a summation limit, an exponent's baseline offset: **none of these
   are functions of x.**
3. **Superscript detection exists and never reaches any output.** `LTRResultIterator` declares
   `SymbolIsSuperscript()`; it reads a field set by `SubAndSuperscriptFix()`; and
   `classify_word_pass2()` in `src/ccmain/control.cpp` does:

   ```cpp
   if (tessedit_ocr_engine_mode == OEM_LSTM_ONLY) { return; }   // before SubAndSuperscriptFix
   ```

   Even in legacy mode it goes nowhere — `src/api/hocrrenderer.cpp` emits `<strong>`/`<em>` and has
   **no `<sup>`/`<sub>` handling at all.** So `x²` → `x2`, and no output channel records otherwise.
4. **`equ.traineddata` is a region detector, not a recogniser.** `src/ccmain/equationdetect.cpp`
   labels blobs `BSTT_MATH`, groups partitions as `PT_EQUATION`, and does no syntactic analysis. It is
   `false` by default, and its declaration and both call sites sit inside `#ifndef DISABLED_LEGACY_ENGINE`.
   Issue #3028 (a request for LaTeX support) was closed **wontfix**. It is not in the Ubuntu archive
   as a separate package.

### 4.2 Measured on `content/ps160/m14/M14_textbook_chapter.pdf`

Rendered at 300 dpi (2550×3300), `--psm 3`, `OMP_THREAD_LIMIT=1`: **3.7–4.4 s/page, 133 MB RSS.**

**Prose is genuinely good.** Verbatim from page 6, unedited:

> *"When you start an object oscillating in SHM, the value of w is not yours to choose; it is
> predetermined by the values of k and m."*

**Every 2-D expression is destroyed, and 1-D ones survive.** That split is exact and follows from the
CTC-over-x architecture:

| Source | Tesseract output | |
| --- | --- | :-: |
| `x = (0.025 m) cos[(20 rad/s)t − 0.93 rad]` | `x = (0.025 m) cos[(20 rad/s)t — 0.93 rad]` | ✅ 1-D |
| `x₀` | `x)` / `xo,` / `xg,` | ❌ |
| `v₀ₓ` | `vg,` / `Up,` / `UV,` | ❌ |
| `a_x = −(10 m/s²)…` | `a, = —(10 m/s”)…` | ❌ superscript 2 → `”` |
| `kg/s²`, `s⁻²`, `s⁻¹` | `kg/s”`, `s *`, `s \|` | ❌ |
| `A = √(x₀² + v₀ₓ²/ω²)` | `A =/x¢ + = ,\| (0.015 m)` … `> , (0.40 m/s)?` … `(20 rad/s)”` | ❌ **shattered across the page** |
| `φ = arctan(−v₀ₓ/ωx₀)` | `d= arctan( —` … `OY _) = _53° = 0.93 rad` | ❌ |
| Eq. (14.11), boxed with leader lines | `f —- i Se Of restoring force` | ❌ |
| `Eqs.` | `Eggs.` | ❌ |

**Reading order also breaks on the two-column page** — the equation for `A` comes back interleaved
with EVALUATE prose from the other column. Tesseract's own documented limits confirm this is expected:
*"it might fail to recognize two columns … and attempt to join text across columns"*, and *"Tesseract
does not divide text into paragraphs or headings."* No `--psm` fixes it: `3` is the only mode that
attempts columns, `6` destroys them by assumption, `11`/`12` give no ordering guarantee at all.

**The dangerous property is not the errors — it is the confidence.** `aaafae = [coors m)? +` is
emitted as ordinary text with no marker. Under
[`scope.md`](../scope.md)'s "report the gaps honestly" objective, **a silently plausible wrong answer
is worse than an empty page.**

Published CER for context (no math benchmark for Tesseract exists — none of the math-OCR benchmarks
include it, presumably because a flat-string engine cannot be scored on a 2-D target):
BLN600 clean 19th-c. newsprint **5.71% CER / 18.18% WER**; Jacob corpus early-modern print
**20.90% / 43.73%**.

---

## 5. OCRmyPDF — **yes, this is the pragmatic answer for ps160's prose**

**MPL-2.0** since **v11.0.0, 2020-08-12** (previously GPL-3; the version bump existed only for the
relicensing). Latest 17.11.0; **16.13.0** installed here. Core MPL-2.0, misc code MIT, docs CC-BY-SA-4.0.

### 5.1 Measured: the verdict flips

Six scanned pages of `M14_textbook_chapter.pdf` (8.5 MB slice), scored with **our own
`textlayer.extract`**:

| | verdict | chars | per page |
| --- | --- | ---: | --- |
| **before** | `ocr-required` | 37 (6/pg) | `empty ×6` |
| `--skip-text` | `ocr-partial` | 10,744 | `ok, empty, empty, ok, ok, empty` |
| **`--redo-ocr`** | **`text-layer-sufficient`** | **22,372 (3,729/pg)** | **`ok ×6`** |
| `--force-ocr` | `text-layer-sufficient` | 22,363 (3,727/pg) | `ok ×6` |

Cost, `--jobs 2`, `nice -n 10`: `--redo-ocr` **61.4 s / 6 pages = 10.2 s/pg, 561 MB peak RSS**;
`--force-ocr` **21.0 s = 3.5 s/pg, 319 MB**. Extrapolated over the census's 400 `ocr-required`
pages: **~68 min at `--jobs 2`**, entirely on CPU. That is cheap.

### 5.2 ⚠ `--skip-text` silently skipped 3 of 6 pages — and would have on the real corpus

The two pages profiled had **8 and 19 characters** of text layer (page furniture on a scan).
`--skip-text` skips a page if it has *any* text, so those pages got **no OCR and no warning**.

**This is a routing decision `ocr_handler` already makes better.** Our per-page verdict
(`ok`/`sparse`/`empty`, threshold 400 chars) correctly called all six `empty`. OCRmyPDF's test is
binary and cruder.

> **Rule:** never let OCRmyPDF decide which pages to OCR. Use `--redo-ocr` (which strips prior
> invisible OCR text, masks *visible* text out of the raster, and OCRs only the remainder — so
> genuine born-digital text is preserved), or drive it page-by-page from our own verdict.
> `--force-ocr` is faster but rasterises vector content; the slice shrank 8.5 MB → 5.4 MB, i.e. the
> images were re-encoded. On a mixed document that is irreversible damage.

### 5.3 Threading — this is the 8-core saturation mechanism

From `builtin_plugins/tesseract_ocr.py`:

```python
jobs = options.jobs or available_cpu_count()
tess_threads = clamp(jobs // len(pdfinfo), 1, 3)
```

with the comment *"Performance testing shows we're better off parallelizing ocrmypdf and forcing
Tesseract to be single threaded."* On 8 cores with a multi-page PDF: `8 // n_pages` → 0 → clamped to
1, so each Tesseract is single-threaded and **OCRmyPDF spawns 8 page workers.** `--jobs N` is the
only throttle — there is no nice level or percentage option. **Memory is ~15 bytes per pixel of the
largest page per job**; a 600 dpi letter page is ~500 MB at `--jobs 1`. Add
`--max-ocr-image-mpixels 8` — Tesseract is tuned for ~300 dpi and gains little above 400, so this is
nearly free.

### 5.4 Ceiling and pluggability

**Its math ceiling is Tesseract's, and §4.2 quantified it on our own pages.** Verified in the
OCRmyPDF output of the same slice — `A = √(x₀² + v₀ₓ²/ω²) = 0.025 m` comes back as:

```bash
aaafae = [coors m)? +
```

Engines *are* pluggable (`get_ocr_engine()` hook): **OCRmyPDF-EasyOCR** (MIT, maintained by the
ocrmypdf org), `ocrmypdf-paddleocr`, `ocrmypdf-rapidocr`, OCRmyPDF-AppleOCR. **No Surya plugin
exists** — request #1330 closed unimplemented, blocked because Surya emits JSON not hOCR.

**Recommended invocation for this corpus:**

```
ocrmypdf --jobs 4 --redo-ocr --max-ocr-image-mpixels 8 --deskew \
         --optimize 1 --output-type pdf in.pdf out.pdf
```

---

## 6. GROBID — orthogonal, and the wrong shape

Code **Apache-2.0**, v0.9.1 (2026-08-04). Model weights carry no separate statement — they are
committed under the repo licence, but that this is *intended* to cover them is inference (**UNVERIFIED**).
Note `pdfalto`, which it ships and shells out to, is **GPL**.

**It is a Java Dropwizard REST service on port 8070.** `grobid-client-python` is purely an HTTP client
("Prerequisites: a running GROBID service instance"). There is **no Python library binding**. Batch
mode exists but the docs say *"We do not recommend to use the batch mode"*; the Java library API is
**deprecated**. CRF-only Docker image ~500 MB; full DL image ~8 GB. **Whether that violates "no server
stacks" is the operator's call** — the CRF image is small, CPU-only, and has no ML runtime, which is
meaningfully unlike ollama — but it is a supervised second process with a JDK 21 dependency.

Three hard disqualifiers regardless:

1. **No OCR, ever.** *"`NO_BLOCKS` means the PDF does not contain any text, and should be processed
   with OCR first."* On the ps160 half it returns nothing.
2. **Math is discarded.** `<formula>` contains the raw glyph sequence with `<lb/>` breaks — no LaTeX,
   no MathML — and issue #829 confirms it *"does not currently serialize superscript/subscript
   information to the TEI XML output."* It ranks **last of 21 parsers (5.70/10)** on the formula
   benchmark. `grobid-quantities` is about physical units, not formulas.
3. **Scholarly articles only.** *"GROBID is designed for scholarly articles."* The `article/light`
   flavor that works on arbitrary documents is exactly the one that gives no structure — *"All noise
   … references, page numbers, head notes, and footnotes are also included in the body. No tables or
   figures recognition."* Lecture slides and homework sets are out of scope. **UNVERIFIED as a
   measurement** — no benchmark on slides exists; this is documented scope plus corpus-builder practice.

Even where it works you get a **flat list of `<head>`** — hierarchy detection is documented as
unreliable (#377, #526 open). Cost is genuinely low: 0.24–0.31 s/PDF on 4 CPU / 8 threads, CRF-only,
4 GB RAM. And the DL path is moot: *"There are currently no neural model for the fulltext models"* —
body structure and section detection are CRF-only no matter what.

**What is worth taking from GROBID is `pdfalto`**, the GPL C++ binary that does the column detection
and text ordering. GROBID's own FAQ points there. Plain CLI, no server, no JVM.
**Secondary lead:** `sciencebeam-parser` (eLife, 0.1.18, Linux-only, licence **UNVERIFIED**) is a
Python reimplementation reusing GROBID's models — it removes the Java objection and **none** of the
content objections.

---

## 7. Composition vs duplication — the two-layout-opinions risk

`ink.py` owns colour/diff masking, dilate-and-label region grouping, band-based reading order, and
cropping. `pdfops.py` owns classify/render/pair. The named risk is real: **adopting a system that
re-does region detection differently creates two disagreeing layout opinions, and nothing arbitrates
between them.**

| System | Composes | Duplicates | Net |
| --- | --- | --- | --- |
| **PyMuPDF geometry** (`rawdict` + `ACCURATE_BBOXES` + `COLLECT_VECTORS`) | *is* the existing dependency; `_reading_order()` and `regions()` already speak in bboxes | nothing | **adopt — free** |
| **`pymupdf.__main__.page_layout`** | drop-in second extraction mode beside `textlayer.extract` | replaces the `pdftotext` shell-out in `pdfops.py` — a deletion, not a duplication | **adopt** |
| **OCRmyPDF** | operates on *whole PDFs* and writes an invisible text layer, which `textlayer.extract` then reads unchanged. **Zero region-detection overlap.** Our per-page verdict drives which pages it touches. | its `--skip-text` page-skip logic duplicates and is *worse than* our verdict (§5.2) | **adopt, but drive it — never let it route** |
| **Tesseract** (direct) | line-level engine; consumes crops `ink.py` already produces | its own page segmentation (`--psm 3`) would compete with `ink.py` if given whole pages | **use only via OCRmyPDF, or on our own crops with `--psm 6/7`** |
| **docTR** | — | **full detect + group + reading order + (v1.1.0) DocLayNet layout.** A complete second opinion. | **reject — duplication plus a 126-char charset** |
| **Marker / Surya** | — | `LayoutBuilder` + a 24-type block taxonomy; `force_layout_block` is the only bypass and is all-or-nothing | **reject — duplication, and a VLM behind a server** |
| **GROBID** | — | its own segmentation model, its own TEI structure | **reject — wrong document class, no OCR, no math** |
| **pdfplumber / pdfminer** | — | duplicates PyMuPDF's geometry, as ADR-era analysis already found | **reject — unchanged** |

---

## 8. The direct answer

> **For the two real corpus needs — scanned textbook chapters (ps160) and born-digital LaTeX PDFs —
> is there a no-VLM path that is good enough?**

**Born-digital LaTeX: yes, and it is better than "good enough" — it is *exact* where it fires.**
2,594 pages across 275 documents. The equations are not images; they are glyphs with font identities
and stroked rectangles at known coordinates. 4,202 fractions came out mechanically at ~92% precision
in 300 s of one CPU core, using only a library the project already depends on. Superscripts and
subscripts are ~99.89% recoverable from relative size and position (Suzuki et al. 2008), and MuPDF
flags superscript spans for free. **No model here would be an improvement; it would be a
regression** — that is the founding rule in [`scope.md`](../scope.md), applied to structure rather
than to characters.

The realistic target is **not** end-to-end LaTeX. MaxTract's 37% and the 172/628 expression-split
errors say formula *segmentation* — where an expression begins and ends — is genuinely not in the
PDF, and both labs that pushed hardest ended up rendering to pixels for exactly that step.
**The mechanically achievable deliverable is a faithful, font-and-geometry-annotated intermediate:**
glyph, accurate bbox, math-font class, size, baseline offset, sup/sub flag, plus rule rectangles.
That is strictly better structured than `-layout`'s ASCII art while preserving everything it
preserves, and fractions, radicals, matrices and limits fall out of it with a few hundred lines of
rules on a corpus that is one document class, not arXiv-at-large. Where it is ambiguous, **say so** —
which is what this project's honesty rule wants anyway.

**Scanned chapters: yes for the prose, no for the mathematics, and the distinction must be visible in
the output.** OCRmyPDF + Tesseract turns `ocr-required` into `text-layer-sufficient` at ~10 s/page on
CPU, and ps160's ~400 pages become searchable in about an hour. Today those chapters extract to a
436-byte stub that says *"see source PDF"* — so this is a large gain over the status quo. But
**every displayed equation is destroyed**, measured on our own pages: no `∫ ∑ √ ∂`, no Greek,
superscripts silently flattened, radicals shattered across the page, two-column reading order broken.
And Tesseract emits that as ordinary confident text. **Recording the prose and marking the equation
regions as unrecovered is honest; shipping `aaafae = [coors m)? +` as content is not.**

So the roadmap change this supports is a **re-sequencing, not a substitution**:

1. **Do the geometry work first.** It is free, deterministic, needs no GPU, serves 2,594 pages, and
   nothing in the VLM landscape does it better. It also fixes the false negative recorded in
   [`layout-mode-decides-whether-math-survives.md`](../findings/layout-mode-decides-whether-math-survives.md)
   — a structural axis for the classifier falls straight out of the rule and math-font counts.
2. **Ship OCRmyPDF for ps160 prose immediately**, driven by our own per-page verdict, with equation
   regions flagged rather than transcribed.
3. **The VLM question narrows to one thing: reading mathematics off pixels.** That is where
   [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md)'s candidates earn their VRAM — on
   scanned and handwritten math, ~400 pages plus 2 annotated lectures. It is a much smaller and much
   better-defined problem than "the OCR engine for this project", and neither of the above waits on it.

---

## Caveats and open questions

- **The ~92% precision is a 25-sample eyeball, not a labelled evaluation.** The criterion was
  structural correctness of the num/den split, not glyph perfection. A real number needs a labelled
  fixture set. It is also *conditional on a bar being found* — it says nothing about recall, and
  nothing about whole-formula assembly, which is where MaxTract lost.
- **Recall is entirely unmeasured.** How many fractions in those 275 documents were *missed*? Unknown.
- **Non-TeX born-digital (Word / PowerPoint / Cambria Math) is not solved and may not be solvable this
  way.** 155 documents, 4,550 pages, ~8% precision. The `ee_300` cheat sheets use Word's equation
  editor and produced both real fractions and table-row garbage from the same detector.
- **`--redo-ocr` at 10.2 s/page was measured at `--jobs 2` on a machine already at load ~5.** On an
  idle machine at `--jobs 4` it will be faster; that number is a ceiling, not a benchmark.
- **Tesseract here is 4.1.1** (Ubuntu 22.04 archive), not the current 5.5.3. 5.x prose accuracy is
  better; **the math ceiling is architectural and identical** — the CTC-over-x-axis limit and the
  `OEM_LSTM_ONLY` early return are both still in `main`.
- **UNVERIFIED:** docTR weight licensing (no statement exists); `pdftotext`'s bbox printf formats;
  whether `maxtract-docker` still builds; GROBID model-weight licensing; GROBID on slides (inference
  from documented scope, not a measurement); Surya CPU throughput on x86 (only Metal is published);
  marker's "20M layout model" claim (the shipped rf-detr-large checkpoint is 134.9 MB ≈ 34M params).
- **Contradiction with the brief, recorded not resolved by preference:** the brief stated Marker's
  README says $5M while its LICENSE says $2M, with the file governing. **Today both say $5M**; the
  $2M survives only on `datalab.to/pricing`. The $2M/GPL era was real (2025-08-20 → 2026-07-20) and
  the source of the confusion. Anyone between $2M and $5M should get it in writing.

---

## Reproduce

```bash
cd ~/electrical_notes/ocr_handler
export OMP_NUM_THREADS=3 MKL_NUM_THREADS=3

# fraction reconstruction, one document
nice -n 10 .venv/bin/python tmp/classical/frac_recon3.py <pdf> 20

# whole corpus, producer-split, with random precision sample
nice -n 10 .venv/bin/python tmp/classical/corpus_scan3.py

# layout-mode comparison
nice -n 10 .venv/bin/python -m pymupdf gettext -mode layout -output out.txt <pdf>

# OCRmyPDF on a slice, throttled  (NEVER omit --jobs)
OMP_THREAD_LIMIT=1 nice -n 10 tmp/classicalvenv/bin/ocrmypdf \
    --jobs 2 --redo-ocr --optimize 1 --output-type pdf in.pdf out.pdf
```

Probes: `tmp/classical/{probe_geom,frac_recon,frac_recon2,frac_recon3,corpus_scan,corpus_scan3,report,inspect_bar,dump_fracs}.py`
(gitignored; ~90 lines each, no dependency beyond `pymupdf`).

---

**Related:** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) ·
[`../findings/layout-mode-decides-whether-math-survives.md`](../findings/layout-mode-decides-whether-math-survives.md) ·
[`../findings/corpus-census-2026-09-04.md`](../findings/corpus-census-2026-09-04.md) ·
[`../decisions/0001-pymupdf-is-the-only-pdf-library.md`](../decisions/0001-pymupdf-is-the-only-pdf-library.md) ·
[`../scope.md`](../scope.md) · `src/ocr_handler/{textlayer,pdfops,ink}.py`

**Primary sources:**
[marker LICENSE](https://raw.githubusercontent.com/datalab-to/marker/master/LICENSE) ·
[marker MODEL_LICENSE](https://raw.githubusercontent.com/datalab-to/marker/master/MODEL_LICENSE) ·
[surya README](https://raw.githubusercontent.com/datalab-to/surya/master/README.md) ·
[surya settings.py](https://raw.githubusercontent.com/datalab-to/surya/master/surya/settings.py) ·
[datalab.to/pricing](https://www.datalab.to/pricing) ·
[docTR vocabs.py](https://raw.githubusercontent.com/mindee/doctr/main/doctr/datasets/vocabs.py) ·
[docTR issue #1730](https://github.com/mindee/doctr/issues/1730) ·
[OnnxTR](https://github.com/felixdittrich92/OnnxTR) ·
[Tesseract control.cpp](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/src/ccmain/control.cpp) ·
[Tesseract hocrrenderer.cpp](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/src/api/hocrrenderer.cpp) ·
[Tesseract equationdetect.cpp](https://raw.githubusercontent.com/tesseract-ocr/tesseract/main/src/ccmain/equationdetect.cpp) ·
[Tesseract NeuralNets doc](https://tesseract-ocr.github.io/tessdoc/tess4/NeuralNetsInTesseract4.00.html) ·
[OCRmyPDF introduction](https://raw.githubusercontent.com/ocrmypdf/OCRmyPDF/main/docs/introduction.md) ·
[OCRmyPDF tesseract plugin](https://raw.githubusercontent.com/ocrmypdf/OCRmyPDF/main/src/ocrmypdf/builtin_plugins/tesseract_ocr.py) ·
[OCRmyPDF performance](https://raw.githubusercontent.com/ocrmypdf/OCRmyPDF/main/docs/performance.md) ·
[GROBID FAQ](https://github.com/kermitt2/grobid/blob/master/doc/Frequently-asked-questions.md) ·
[GROBID fulltext training](https://grobid.readthedocs.io/en/latest/training/fulltext/) ·
[pdfalto](https://github.com/kermitt2/pdfalto) ·
[MaxTract, CICM 2012](https://link.springer.com/chapter/10.1007/978-3-642-31374-5_29) ·
[MaxTract DML 2011 slides](https://www.fi.muni.cz/~sojka/dml-2011-baker-sexton-sorge.pdf) ·
[SymbolScraper](https://github.com/zanibbi/SymbolScraper) ·
[MathSeer / SymbolScraper paper](https://shahayush.com/files/Shah2021_MathSeer.pdf) ·
[ChemScraper](https://arxiv.org/abs/2311.12161) ·
[Suzuki, sub/superscripts](http://www.inftyproject.org/articles/2008_MCS-51.pdf) ·
[Horn & Keuper, arXiv:2512.09874](https://arxiv.org/abs/2512.09874) ·
[PyMuPDF constants](https://pymupdf.readthedocs.io/en/latest/vars.html) ·
[PyMuPDF text extraction](https://pymupdf.readthedocs.io/en/latest/app1.html)
