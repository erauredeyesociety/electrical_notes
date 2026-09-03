# Research — external teardowns

Studied before building. Numbers marked **measured** were run on this machine's RTX 3060 Laptop (6 GB); everything else is from primary sources.

---

## Verdict

**Three stages, two small models, one PDF library.**

| Stage | Tool | Cost |
| --- | --- | --- |
| 0 · route | **PyMuPDF** — no model | free |
| 1 · locate ink | **PyMuPDF structural extraction** — no model | free |
| 2 · read math | **contested — see below** | 681 MiB / 960 MiB / 4199 MiB |

**Stage 2 is now a three-way question, not a settled choice.** All three fit and all three were measured on this GPU:

| Candidate | Peak | Reads a cropped equation | Reads a whole page |
| --- | --- | --- | --- |
| UniMERNet-Base | **681 MiB** | yes — its only job | no |
| SmolDocling-256M | 960 MiB | yes, and got the `ω₀` subscript UniMERNet-Tiny missed | yes |
| Unlimited-OCR NF4 | 4199 MiB | overkill | **yes — and crops figures for you** |

Resolve with a head-to-head on the fixture page before writing `recognize.py`.

---

## The finding that changes the design

**PDF Annotator stores the red ink as separate embedded images with exact page coordinates.** The ink does not have to be recovered from pixels at all — it can be pulled out structurally.

Verified here on page 5:

| | base PDF | annotated PDF |
| --- | --- | --- |
| images on page 5 | 1 | **3** |

The two extra images *are* the annotation layer. Extracting `xref 178` yields a clean red-on-white `cos(ω₀n)   sin(ω₀n)` — the two filled-in blanks — with **no rendering, no colour thresholding, no dilation tuning.**

```python
import pymupdf
doc = pymupdf.open(annotated)
page = doc[4]
for xref, *_ in page.get_images(full=True):
    for rect in page.get_image_rects(xref):
        ...        # exact page coordinates
```

> ⚠ **Correction to the source claim.** The research reported the discriminator as a `/OC`-tagged **DeviceRGB** colourspace. That is not reliable: `get_images(full=True)` reports the base image as `Indexed` and the ink as `DeviceRGB`, but converting any of them through `Pixmap` normalises all three to DeviceRGB. **Discriminate by image-count difference against the base file**, which is exact and colour-agnostic, not by the colourspace of a converted Pixmap.

**This does not delete `ink.py`.** Structural extraction says *where the ink is*, exactly. Region grouping then subdivides it into one-expression crops, which is what a recogniser needs — structural gave 2 images on page 5, pixel grouping gave 5 logical items. They compose; neither replaces the other. Colour separation also stays as the fallback for annotated files with no available base.

---

## Models

### Equation → LaTeX: **UniMERNet-Base** (`wanderkid/unimernet_base`, Apache-2.0)

**Measured on this GPU against our own page 5:** 622 MiB weights, **681 MiB peak**, ~0.5 s per expression.

Keep `unimernet_tiny` (410 MB, 580 MiB peak) installed as a second opinion — on our handwriting the two fail on *different* symbols: Tiny read `\cos(\omega_0 n)` where Base did not; Base recovered the subscript in `(e^{jw_0})^n` where Tiny did not. Cheap disagreement signal.

### Ruled out, with reasons

| Tool | Why not |
| --- | --- |
| **Qwen2.5-VL-7B** | fp16 ~16.6 GB; int4 ~5.2–5.6 GB *weights alone* before ViT activations on a page. Blog claims of "runs in 6–8 GB" are **false for page-sized input**. olmOCR, a 7B finetune, states a 12 GB floor. |
| **MiniCPM-V 4.5** | Strongest candidate we cannot run. int4 ~5.5–6 GB leaves nothing for a 1.8 MP page. |
| **Qwen2.5-VL-3B** | Qwen **Research Licence — non-commercial only**. Verification also corrected params to 4.07B, not 3.75B. |
| **Stock generalist VLMs** | ~38% expression-rate on cropped handwritten math. Uni-MuMER's finetune gains **+41.79 points** over stock — the gap is the whole problem. |
| **CROHME specialists** (CoMER, BTTR, PosFormer) | Trained on isolated clean expressions; no usable path for real lecture annotation. |
| **OpenCV / scikit-image** | Both installed and benchmarked; both lost on merit. Hough needed the same collinear-merge post-processing as plain morphology, and `regionprops` is ergonomics over `find_objects`. numpy + scipy + Pillow suffice. |
| **pdfplumber / pypdf / pdfminer / Camelot** | pdfplumber duplicates PyMuPDF, pypdf cannot render, pdfminer is a subset of pdfplumber, poppler is ~10× slower, Camelot would corrupt output. |

### Corrections the adversarial pass produced

- **PaddleOCR-VL** — "fits comfortably" **refuted**. Fits *conditionally*; the vendor's own documented floor exceeds 6 GB.
- **SmolDocling** — licence is **CDLA-Permissive-2.0**, not Apache-2.0.
- **InternVL3.5-2B** — 2.35B params, not 2.1B, and **weights are not the fit criterion; activations are.**
- **Uni-MuMER-Qwen3-VL-2B** — claim stands and is *conservative*. 2.128B, Apache-2.0 clean chain. A viable alternative to UniMERNet if a second engine is wanted.

---

## The "besu" thread — resolved

Not an OCR project by that name; the earlier survey guessed Hyperledger Besu. **The actual referent was Baidu Unlimited-OCR** — `github.com/baidu/Unlimited-OCR`, the stated inspiration for this project.

Torn down separately: [`unlimited-ocr.md`](unlimited-ocr.md) — **and the first summary here was wrong.**

**It runs.** NF4 4-bit: 2684 MiB weights, **4199 MiB peak of 6144**, 8.5 s/page, deterministic. On our fixture page it met `scope.md`'s success criterion in one pass, recovering `\cos(\omega_0 n) + j\sin(\omega_0 n)` — and a **control run on the un-annotated twin returned `(\quad + j \quad)`**, proving it reads the ink rather than confabulating.

bf16 genuinely OOMs, and the `fa3` blocker is real but applies only to the **sglang** path — the transformers path needs no flash-attn. The torch-version concern was unfounded.

---

## Frontier models don't use OCR

Neither Claude nor ChatGPT runs a classical OCR engine — both rasterise and read pixels with the vision transformer. The local analogue is therefore a **VLM, not an OCR engine** — but *not* a single general VLM, which is the one configuration this research rules out.

---

## Consequence for the code

Current `pdfops.py` shells out to poppler (`pdftotext`, `pdftoppm`, `pdfimages`). **PyMuPDF replaces all of it**, is ~10× faster, and unlocks structural ink extraction. That is a rewrite of one 120-line module — logged in [`../todo.md`](../todo.md).

---

**Raw survey:** 22 agents, 8 topics, 14 adversarial verifications. Several measured on this exact GPU.
