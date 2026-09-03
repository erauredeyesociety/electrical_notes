# Baidu Unlimited-OCR — teardown

The project's stated inspiration. Cloned to `~/tmp/Unlimited-OCR`. MIT licence, Baidu 2026, arXiv 2606.23050.

> **This document was rewritten after a 14-agent teardown that actually ran the model on this GPU. The first pass concluded "does not fit, wrong shape." That was wrong on the first half.** Corrections are marked ⚠ throughout.

---

## Verdict

**It runs, and on our own fixture page it meets `scope.md`'s success criterion in a single 8.5 s pass.**

| | measured on this RTX 3060 |
| --- | --- |
| bf16 | **OOM** — dies at 5.51 GiB of 6.214 GiB during `.cuda()` |
| **NF4 4-bit** | **2684 MiB weights, 4199 MiB peak of 6144, 8.5–9.5 s/page** |
| int8 (experts only) | 5423 MiB, 24.6 s — fits but tight |
| CPU offload | works below ~3000 MiB budget, **10–13× slower** (97–117 s) |
| Determinism | 6 repeat runs **byte-identical** (greedy, temp 0) |

On our page 5 it produced `= |\alpha|^{n} (\cos(\omega_{0} n) + j \sin(\omega_{0} n)).` — correct `\cos`, `\sin`, and the `\omega_0` subscripts — plus both stem plots as separate cropped JPEGs and the exact header and footer.

### The control experiment that settles it

Run on the **un-annotated twin**, the same equation comes out as:

```
= |\alpha|^{n} (\quad + j \quad).
```

**The model emits `\quad` spacing exactly where the deliberately-left blanks are.** With ink, it returns the filled content. Same model, same process, back to back.

That is decisive: it is *reading the red ink*, not confabulating plausible DSP from context. It is the strongest single result of the whole exercise, and it is a methodology worth reusing — **always run the base twin as a control.**

---

## ⚠ Corrections to the first pass

| First pass said | Actually |
| --- | --- |
| "Does not fit — quantisation mandatory, accuracy cost unmeasured" | Fits at NF4 with **1945 MiB to spare**, and **no measurable accuracy loss** versus a bf16 CPU-offload reference. If anything 4-bit read *better* on this page (n=1, so call it "no loss"). |
| "`fa3` hardcoding is a hard blocker" | Only for the **sglang** path. The transformers path needs no flash-attn at all: `use_mla=false` routes to `mha_eager`, and both vision encoders use torch SDPA. |
| "torch 2.7.0 vs their 2.10.0 is a version problem" | **No problem.** Every imported symbol resolves on torch 2.7.0 + transformers 4.57.1; the remote code carries explicit forward-compat shims. |
| "MoE sparsity buys no memory" | True but misleading — **72.6% of the model is routed experts**, and almost everything is Linear-shaped, which is *why* 4-bit works so well here. |
| "Re-test DPI at 300" | **Answered, and the question was wrong.** See below. |

---

## The five things that actually matter for using it

**1. `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` is worth ~1.1 GiB.** 5321 MiB without, 4199 MiB with, identical work. For int8 it is the difference between OOM and success. Highest-leverage single line in the setup.

**2. The memory ceiling is not the weights — it is one tensor.** The SAM windowed relative-position attention bias (`deepencoder.py:837`) materialises **704–750 MiB in one allocation**. That is what kills int8-without-the-flag and offload-at-5000MiB. Design around it, not around weight size.

**3. Quantising `model.projector` breaks the model.** It returns Float while `inputs_embeds` is BFloat16 → `masked_scatter_: expected self and source to have same dtypes`. It must go in `llm_int8_skip_modules`. The two vision encoders quantise safely.

**4. `crop_mode` (gundam) is mandatory for handwriting.** The `base` profile read `e^{jw_0}` as `e^{iu\theta}` and `\alpha` as `x` on the same page gundam read correctly. Measured cause: base squashes the page to a padded 1024², dropping our handwriting to **10.6 px glyphs / 1.24 px strokes** and the red ink to **11.8 px / 0.62 px — sub-pixel**. Gundam keeps the same content at 25.6/3.0 and 28.6/1.5 px.

> **This disqualifies their PDF path for our material.** `infer_multi` and the PDF helper are **forced to base**. One-shot 10-page parsing did run — 165.9 s, peak 5199 MiB — but was **slower *and* worse**: "complex" became "lowplex", ω₀n became ω_n, and it emitted 12 `<PAGE>` markers for 10 pages. The long-horizon headline feature is for clean printed documents.

**5. It is not instruction-followable.** Only trained prompts produce output; everything else returns an empty string after 1.0 s. `'<image>document parsing.'` works; `'Transcribe only the red handwriting.'` returns nothing. **You cannot ask it to isolate the ink** — that stays our structural extraction's job.

---

## ⚠ The rasteriser matters more than the DPI

The most surprising finding, and it invalidates the open question I logged last pass.

| Render | Result on the same page |
| --- | --- |
| **poppler** `pdftoppm` @ 200 dpi | `c o s (w o n)` — spaced-out, wrong |
| **PyMuPDF** @ 150, 200, 300 dpi | `\cos (\omega_{0} n)` — all three correct |
| PyMuPDF @ 400 dpi | `c o s (w o n)` — degrades again |

The two 200 dpi renders differ on **6.66% of pixels** purely from antialiasing, and that is enough to change the answer. **Switch the renderer to PyMuPDF** — which we were already going to do for other reasons — and DPI between 150 and 300 stops mattering.

**DPI is free in cost terms:** peak VRAM was 3941 MiB and wall time ~8.5 s at *every* DPI from 150 to 400, because everything is resampled to one 1024 global view plus 640-px crops. Only accuracy varies, never cost.

Separately, for the ink path the DPI question is moot: **PDF Annotator stores the red ink as embedded PNGs at a fixed native resolution** (uniformly 150 dpi in these Ghostscript exports), so rendering the page higher cannot add ink detail that was never captured.

---

## What the papers say, and why it does not decide this

**The papers make no handwriting claim whatsoever.** `grep -ci handwrit` over the full Unlimited-OCR paper returns **0**. Its 2 M continued-training samples are PaddleOCR-pseudo-labelled PDFs — a *printed*-text engine as annotator. DeepSeek-OCR's formula competence traces explicitly to 3 M **Word documents**: *"This data mainly brings benefits to formulas and HTML-formatted tables."* That is typeset-formula ability.

**And yet it read our handwriting correctly.** When documentation and measurement disagree, measurement wins — but honestly: this is **n = 1 page**, on handwriting that is unusually neat, and the papers give no reason to expect it to generalise. Treat the capability as *observed*, not *supported*.

---

## Architecture notes worth keeping

- `infer.py` (329 lines) contains **no image preprocessing at all** — it is an HTTP client for an sglang server it launches. All preprocessing lives in the HF remote code.
- **gundam tiling:** a 2550×3300 page resolves to `crop_ratio (3,4)` → resized to 1920×2560, cut into **12 non-overlapping 640² tiles**, plus the whole page padded into 1024² with grey bars. Cost: 273 global + 1240 local = **1513 image tokens**.
- **Tiles are re-woven, not fed independently.** A `permute` reassembles the per-tile 10×10 token grids into one 30×40 raster in reading order with a learned newline embedding per row (`modeling_unlimitedocr.py:534`). A glyph split across a tile edge has its halves adjacent in the sequence — which matters, because the grid **cuts through 12–22% of ink marks** on our pages (page 5: 19.5%).
- Two bugs found: `infer()` never forwards `image_size` into `dynamic_preprocess`, so crops are always 640 px regardless of the argument; and `config.json`'s `global_view_pos: "head"` is a **dead key** — the code concatenates local first.
- NF4 weights can be **cached to disk at 2.62 GiB**, reloading in 5.8 s instead of 11–14 s, byte-identical output. Two gotchas: `llm_int8_skip_modules` is not written into the saved config, and reload **must** pass `dtype=torch.bfloat16` or unquantised modules come back fp16 and hit the same `masked_scatter_` error.

---

## Where this leaves the plan

**Routing is confirmed, emphatically.** On a born-digital page the model spent **19.6 s to produce a *worse* answer** than PyMuPDF's text layer gives for free — mangling TOC dot-leaders. Never send a type-A page to a model.

**Structural ink extraction survives and gains a second job.** Intersecting PDF Annotator's exact ink rectangles with the model's `<|det|>` boxes tells you *which recognised blocks are annotation* — something the model cannot tell you itself, since it is not instruction-followable.

**Adopt their output format as our intermediate representation** (`scope.md` open decision 3):

```
<|det|>CATEGORY [x1,y1,x2,y2]<|/det|>CONTENT
```

with 0–1000 normalised page coordinates. It says what a block is, where it is, and what it contains, resolution-independently — and figures as a bbox with *empty* content plus a separate caption block is exactly our "equations as text, figures as cropped images" contract in wire form.

**Open question this raises:** a sibling agent found **SmolDocling-256M** running at **960 MiB peak** on a full page, reading `\cos(\omega_0 n)` *with* the ω₀ subscript that UniMERNet-Tiny missed, and recovering both the subscript and the `^n` in region 3 that UniMERNet Base and Tiny both missed. At 256 M against 3.3 B that deserves a head-to-head before the engine is fixed.

---

## Practical footnote

Peak 4199 MiB leaves 1945 MiB — real headroom, but not generous, and it assumes the display is not on this GPU (it is on the iGPU here). **A concurrent GPU process cost a run mid-session**: another agent's 1318 MiB benchmark caused an OOM. Serialise GPU work.

---

**Cloned:** `~/tmp/Unlimited-OCR` · **Runs:** `~/tmp/uocr_run` · **See:** [`INDEX.md`](INDEX.md) · [`../scope.md`](../scope.md)
