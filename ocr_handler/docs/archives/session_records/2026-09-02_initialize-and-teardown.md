# 2026-09-02 — Initialize, build backbone, tear down the inspiration

**Seat:** PM2 Project-Lead · **Mode:** discovery → development · **Outcome:** M1 complete, engine choice reopened

---

## What was done

**Initialized the project** per the bootstrap Initialize directive. Kind: **Implementation** (deliverable is working code). Full `docs/` tree, project-local directives, lean scope/roadmap/todo, regression floor.

**Built the non-ML backbone** and verified it on real course material:

| Module | Lines | Does |
| --- | ---: | --- |
| `pdfops.py` | 120 | classify / producer / render / pair |
| `ink.py` | 162 | colour + diff masks, region grouping, crop |

Verified end to end: routing separated all three PDF kinds correctly (born-digital → 11 text pages; annotated → 9 image pages), pairing found the un-annotated twin, red separation reproduced a manual check **to the pixel (8,090)**, and region grouping returned **5 regions matching the page's logical content**.

**Ran two research efforts.** An 8-topic OCR landscape survey with 14 adversarial verifications, then — after the operator identified the real inspiration — a **14-agent teardown of Baidu Unlimited-OCR**, which cloned it, read the remote code, and ran the model on this GPU.

**Wrote a 7-test regression floor.** All passing.

---

## Decisions made

| Decision | Rationale |
| --- | --- |
| **PyMuPDF as the only PDF library** | pdfplumber duplicates it, pypdf cannot render, pdfminer is a subset, poppler ~10× slower, Camelot would corrupt output |
| **No OpenCV, no scikit-image** | Both installed and benchmarked by an agent; both lost to numpy + scipy + Pillow on merit |
| **No single general VLM** | Stock models ~38% expression-rate on cropped handwritten math; specialist finetunes gain +41.79 points |
| **`merge_px = 64`** | Swept 16→96; stable plateau of 5 regions across 56–80 matching actual content. Pixel distance, so re-sweep if DPI changes |
| **Adopt `<\|det\|>CATEGORY [bbox]<\|/det\|>CONTENT`** as the intermediate representation | Unlimited-OCR's output format is the same shape as our contract — what a block is, where, and what it contains, resolution-independently |
| **Engine choice deferred** | Three candidates all fit and all were measured; decide by head-to-head, not by argument |

---

## Discoveries

### Structural ink extraction — the design-changing one

**PDF Annotator stores the red ink as separate embedded images with exact page coordinates.** Base page 5 has 1 image; annotated has 3. Extracting the extras yields a clean red-on-white `cos(ω₀n)  sin(ω₀n)` — **no rendering, no thresholding, no tuning.**

Corrected the source claim while verifying it: the discriminator is **not** a DeviceRGB colourspace (converting through `Pixmap` normalises everything to DeviceRGB). It is **image-count difference against the base file** — exact and colour-agnostic.

This does not replace `ink.py`; structural extraction says *where* ink is, region grouping subdivides into one-expression crops. They compose.

### Unlimited-OCR runs — and the first verdict was wrong

| First pass | Measured |
| --- | --- |
| "Does not fit unquantised" | ✅ correct — bf16 OOMs at 5.51 of 6.214 GiB |
| "Quantisation cost unmeasured" | ❌ **NF4: 4199 MiB peak, 8.5 s/page, no measurable loss vs a bf16 offload reference** |
| "`fa3` is a hard blocker" | ❌ only for the **sglang** path; transformers needs no flash-attn |
| "torch 2.7 vs 2.10 is a problem" | ❌ unfounded — the remote code carries forward-compat shims |

On the fixture page it met `scope.md`'s success criterion in one pass, and a **control run on the un-annotated twin returned `(\quad + j \quad)`** — proving it reads the ink rather than confabulating. That control is now a standing methodology.

### Operational findings worth more than the model choice

- **`PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` is worth ~1.1 GiB of peak** (5321 → 4199 MiB, identical work).
- **The memory ceiling is one tensor**, not the weights — a 704–750 MiB SAM attention bias allocated in one go.
- **The rasteriser changes answers more than DPI does.** poppler @200 dpi → `c o s (w o n)`; PyMuPDF @150/200/300 → `\cos(\omega_0 n)`. The renders differ on 6.66% of pixels from antialiasing alone. DPI is *free in cost* — same peak and wall time from 150 to 400.
- **Serialise GPU work.** A concurrent 1318 MiB process caused an OOM mid-session.

### Bug found in our own code

Sorting regions by `(y0, x0)` returned `cos(ω₀n)` and `sin(ω₀n)` **swapped**, because their tops differ by three pixels — which would have silently reversed an equation. Fixed by banding on vertical overlap first; now a named regression test and a project directive.

### "besu" resolved

Not an OCR project. The operator identified the real referent: **Baidu Unlimited-OCR**.

---

## Blockers

None hard. One decision outstanding and three operator confirmations.

**Engine head-to-head** — run on the fixture page before writing `recognize.py`:

| Candidate | Peak | Notes |
| --- | --- | --- |
| UniMERNet-Base | 681 MiB | cropped equations only |
| SmolDocling-256M | 960 MiB | got the `ω₀` subscript UniMERNet-Tiny missed |
| Unlimited-OCR NF4 | 4199 MiB | whole pages, crops figures itself |

**Awaiting operator:** confirm `scope.md` (especially the Out-of-Scope blacklist), output destination, and whether this becomes a bootstrap child project or stays a subfolder of `electrical_notes`.

---

## Next

1. `pdfops.py` → PyMuPDF. Changes *answers*, not just speed. Keep the `PageInfo`/`kind` interface so tests and routing are untouched.
2. `ink.structural_regions()` — annotation images by count-difference against the base.
3. Engine head-to-head, then `recognize.py` behind one swappable interface.
4. `emit.py` + `cli.py` (M2).

---

**Detail:** [`../../research/unlimited-ocr.md`](../../research/unlimited-ocr.md) · [`../../research/INDEX.md`](../../research/INDEX.md) · [`../../todo.md`](../../todo.md)
