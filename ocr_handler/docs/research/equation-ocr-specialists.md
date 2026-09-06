# Equation / formula OCR specialists — 2026-09-05

Does **UniMERNet-B** remain the right engine for turning a cropped equation into LaTeX?

**Scope set by the operator:** specialist models that install as ordinary Python packages.
No ollama, no vLLM, no HuggingFace model-serving stack. Fetching weights from the hub is fine;
standing up a server is not. Ceiling ~20B nominally, but the real ceiling is this machine —
**RTX 3060 Laptop, 6144 MiB, 5792 MiB free at the time of these runs.**

**Numbers marked *measured*** were run here today, in an isolated venv at `tmp/eqvenv/`
(gitignored), through [`tools/gpu_lock.py`](../../tools/gpu_lock.py), one model at a time.
Everything else is cited. Anything I could not settle from a primary source is marked
**UNVERIFIED**.

> Read with [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) (which chose
> UniMERNet-B and PaddleOCR-VL-1.6) and [`mineru-teardown.md`](mineru-teardown.md) (which
> nominated `mfr/utils.py` for vendoring). This document **does not edit either.** Where it
> contradicts them, [§8](#8-where-this-contradicts-the-earlier-research) says so explicitly.
>
> ⚠ **`INDEX.md` was deliberately not touched** (other agents are working in this folder), so
> this file is not yet linked from it. It needs one line added under *Models → Equation → LaTeX*.

---

## Verdict up front

**Keep UniMERNet-Base — but the reason it is right is not the reason it was chosen, and the
biggest accuracy win available is not the model at all.**

| Question | Answer |
| --- | --- |
| Is UniMERNet still the best open specialist? | **Yes on handwriting.** Nothing published since 2024 beats its UniMER-Test HWE score with releasable weights and a clean licence |
| Is `pip install unimernet` viable? | **No.** It hard-pins `transformers==4.42.4`, drags in Streamlit and ImageMagick, last released 2024-12-26. **Vendor MinerU's fork instead** — that is what MinerU itself does |
| Does the 94→36.56 collapse apply to us? | **No, and the earlier framing was wrong.** 36.56 is a *full-page detect-and-parse* score. We hand the model a crop we chose. The 94 column is ours |
| How crop-sensitive is it? | **Padding is free until it touches the neighbouring line — then it is catastrophic.** *Measured*: identical output across a ±16 px band, and across a 96 px band where the page is empty; total collapse at the distance to the nearest neighbour |
| Is DPI the bottleneck? | **No.** *Measured*: usable output from 400 dpi down to 50 dpi. The model's input is 192×672 px and its training band was 80–350 dpi; everything else is thrown away |
| What actually helps most? | **Removing the background.** *Measured*: feeding `ink.py`'s binary mask instead of raw pixels recovered `\omega_0` subscripts UniMERNet-B misses on the raw crop, and deleted a hallucinated `\frac{1}{2}` caused by graph-paper grid lines |
| Can bad LaTeX be detected by compiling it? | **Almost never. 83 of 84 outputs compiled under tectonic**, including 1113 tokens of garbage from a whole page — matching the CDM authors' published **99.71% render rate** for this model. Guard *before* inference and with a repetition test, not with a compiler |
| Is there published guidance on crops? | **No paper; five pipelines' worth of code constants**, spanning +0 px (MinerU) to +18% per side (docling). And one published ablation — DocTron's **0.919 → 0.644 → 0.009 CDM** as crop scope widens, which is the same cliff measured here |

**Recommendation and the strongest argument against it:** [§7](#7-recommendation) and
[§9](#9-the-strongest-argument-against-my-own-recommendation). The argument against is
measured, not rhetorical: **PaddleOCR-VL-1.6 in `Formula Recognition:` mode read one of the two
fixture equations exactly right, and UniMERNet-Base did not — at any padding, at any resolution.**

---

## 1. What was run here, and what it cost

| | |
| --- | --- |
| Venv | `tmp/eqvenv` — `python3 -m venv --system-site-packages`, plus `ftfy` and `loguru` only |
| Model code | **not** `pip install unimernet` — MinerU's vendored `mineru/model/mfr/unimernet/` on `sys.path` from `~/tmp/ocr_repos/MinerU` |
| Weights | `wanderkid/unimernet_base` (1.3 GB) and `wanderkid/unimernet_tiny` (430 MB), 23 s and 9 s to fetch |
| Guards | `OMP_NUM_THREADS=3 MKL_NUM_THREADS=3` before torch import, `nice -n 10`, `gpu_session()` lock |
| Runs | 44-case crop sweep (50 s), 40-case background sweep over both model sizes (39 s), 84-case tectonic validation (4 min, CPU) |

**Resource cost, honestly.** Load average went `2.78 → 4.97` across the first GPU run and
`5.66 → 7.28` across the second. **7.28 exceeds the ~6 ceiling I was given, so I stopped GPU
work at that point.** The GPU was released and idle (5792 MiB free) at 7.26; the load was
`tmp/htr/run_rapidocr.py` at 231% and `tmp/classical/corpus_scan3.py` at 93% — **other agents'
processes, not mine.** My own runs were 50 s and 39 s. The lesson is the one
[`gpu-discipline.md`](../directives/gpu-discipline.md) already states: the lock serialises the
*GPU*, and nothing serialises the *CPU* across agents.

*Measured footprint, this GPU, fp16, batch 1:*

| Model | Weights on disk | torch peak alloc | torch peak reserved | Load | Per crop |
| --- | ---: | ---: | ---: | ---: | ---: |
| **UniMERNet-Base** | 1300.8 MB | **685.9 MiB** | **1290.0 MiB** | 8.1–10.1 s | **0.23–0.36 s** |
| **UniMERNet-Tiny** | 430.1 MB | **232.1 MiB** | **478.0 MiB** | 3.2 s | 0.14–0.44 s |
| *PaddleOCR-VL-1.6* (prior session, `tmp/eval/out_crops/results.json`) | 1.8 GB | 1767 MiB | 1786 MiB | 4.6 s | 2.37–3.97 s |

The project's recorded "681 MiB" for UniMERNet-B reproduces (685.9 MiB). **But `reserved` is
what the card actually loses — 1290 MiB, nearly 2×.** Both fit with room to spare.

---

## 2. The systems

### 2.1 Per-system summary

Licence / size / **printed vs handwritten separately** / maintenance. Handwritten column is
UniMER-Test **HWE**; printed is **SPE** (simple) and **CPE** (complex). CDM where published,
else BLEU. CDM and BLEU are **not interchangeable** — CDM renders both strings and matches
spatially, and runs well above BLEU.

| System | Licence (code / weights) | Params | Weight file | SPE | CPE | **HWE** | Maintenance |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| **UniMERNet-B** | Apache-2.0 / **Apache-2.0** | 325M | 1300.8 MB | 0.9914 CDM | 0.9595 | **0.9400 CDM** | model code frozen since 2024-12 |
| UniMERNet-S | Apache-2.0 / Apache-2.0 | 202M | 810.3 MB | 0.9906 | 0.9588 | 0.9370 | ditto |
| UniMERNet-T | Apache-2.0 / Apache-2.0 | 107M | 430.1 MB | 0.9910 | 0.9491 | **0.9328** | ditto |
| **pix2tex** | MIT / **contested** | ~25M (derived) | 102 MB | 0.9619 | 0.6489 | **0.2453 CDM** | dormant since 2025-01-18 |
| **texify** | **GPL-3.0** / CC BY-SA 4.0 | 312M | 625 MB | 0.9852 | 0.7041 | **0.5269 CDM** | **archived 2025-01-29** |
| surya-ocr-2 | Apache-2.0 / **modified OpenRAIL-M, $5M** | 686M | 1.37 GB | — | — | **UNVERIFIED** | very active (0.22.1, 2026-07) |
| PP-FormulaNet_plus-M | Apache-2.0 / Apache-2.0 | — | 592 MB | — | — | UNVERIFIED (plus-L: 0.947) | active |
| PP-FormulaNet-S | Apache-2.0 / Apache-2.0 | 57M | 224 MB | 0.949 | 0.678 | **0.818 CDM** | active |
| **Texo** | **AGPL-3.0** | **20M** | — | 0.958 | 0.825 | **0.902 CDM** | new (2026-02) |
| TexTeller | Apache-2.0 / Apache-2.0 | 298M | 1.19 GB | — | — | **claimed, see §2.6** | weights unchanged since 2024-06 |
| Pix2Text MFR-1.5 | MIT / MIT | UNVERIFIED | 114 MB ONNX | — | — | **none published** | active (1.1.7, 2026-08) |
| Uni-MuMER-Qwen3.5-2B | Apache-2.0 / Apache-2.0 | 2.2B | ~4.4 GB fp16 | — | — | 73.09 avg ExpRate | active |

Sources: UniMERNet paper Table 5 (BLEU/EditDis) `arxiv.org/html/2404.15254v1`; CDM paper
Tables 2/4 `arxiv.org/html/2409.03643v2`; Texo Table `arxiv.org/html/2602.17189v1`;
PaddleOCR module docs; HF API `?blobs=true` for exact byte counts.

⚠ **Row provenance is not uniform, and it matters at the third digit.** The UniMERNet rows are
the CDM paper's *released-checkpoint* table (Table 4); the pix2tex and texify rows are its
*model-comparison* table (Table 2). The same paper gives UniMERNet HWE as **0.9530** in Table 2
and **0.9400** in Table 4. Both are as-printed and the difference does not change any ranking,
but do not quote a single UniMERNet HWE figure as if there were one.

### 2.2 UniMERNet — confirmed, with three corrections

**Sizes and licence are clean, and I verified them first-hand** against the HF API rather than
the model cards. `wanderkid/unimernet_{base,small,tiny}` are all `apache-2.0`; the training set
`wanderkid/UniMER_Dataset` is also `apache-2.0`. The parameter counts fall straight out of the
fp32 file sizes: 1300.8 MB ÷ 4 = **325M**, 810.3 MB ÷ 4 = **202M**, 430.1 MB ÷ 4 = **107M** —
matching the paper's Table 4/5.

*Verified from the checkpoints themselves:* Donut-Swin encoder (`depths [6,6,6,6]`, `window 5`,
`patch 4`; embed dim 128 / 96 / 64) + mBART decoder (8 layers, vocab 50000,
`max_position_embeddings 1536`; `d_model` 1024 / 768 / 512). Same family as Nougat and Donut.

**Correction 1 — Base is barely better than Tiny.** On CDM the released checkpoints span
SPE 0.9910→0.9914 and HWE 0.9328→0.9400 for a **3× parameter jump**. The gain is concentrated
in CPE ExpRate@CDM (0.699→0.805). *Measured here, the two are not even ordered:* on the
`cos_only` crop Tiny returned `(\cos(\omega_0 n) +` — **correct** — while Base returned
`(\cos(won) +`. Tiny costs 232 MiB and 3.2 s to load. **Tiny is a serious option, not just a
second opinion.**

**Correction 2 — "beats Mathpix on handwriting" is true but comes from the wrong paper.**
The 2024 UniMERNet paper contains **no Mathpix, GPT-4V or GPT-4o comparison at all**. The
Mathpix numbers are in the *CDM* paper (`2409.03643`): UniMERNet HWE **0.9530** vs Mathpix
0.9318. Note the CDM paper also reports a *released-checkpoint* HWE of 0.9400 for Base — the
two tables disagree slightly and both are as-printed.

**Correction 3 — the CVPR 2026 redesign has no weights.** The paper is real (Gu et al., poster
39595, Raster-Scan Attention + ConvE, 313M, HWE CDM 0.941 / 0.954 at 2× resolution). But the
GitHub News section stops at 2025-09-28, the last release is 0.2.3 from 2024-12-26, there is no
arXiv v3, and **no 313M checkpoint exists on the hub.** The `engine-landscape` line *"A 313M
Apache-2.0 model beats Mathpix on handwritten expressions"* is about a model you cannot
download. Its own caveat was right; this makes it definite.

**The pip package is a trap — verified directly from the PyPI JSON API:**

| Package | Version | Released | Killer detail |
| --- | --- | --- | --- |
| `unimernet` | 0.2.3 | **2024-12-26** | **`transformers==4.42.4`** exact pin; `[full]` pulls Streamlit + jupyterlab; `wand` needs system ImageMagick |
| `texteller` | 1.0.2 | 2025-04-21 | **`transformers==4.47`** exact pin |
| `pix2tex` | 0.1.4 | 2025-01-18 | **`x-transformers==0.15.0`** exact pin; `torchtext` (abandoned, will not build against torch 2.7) |
| `texify` | 0.2.1 | 2024-10-31 | `GPL-3.0-or-later` |
| `pix2text` | 1.1.7 | **2026-08-23** | `transformers>=4.37.0` — a **range**. Cleanest dependency shape of the set |
| `paddleocr` | 3.7.0 | 2026-06-11 | pulls `paddlex` — a second deep-learning framework beside torch |

There is also **no `AutoModel` + `trust_remote_code` path**: the HF `config.json` declares
`"architectures": ["UnimernetModel"]` with **no `auto_map`**, so `trust_remote_code` has nothing
to point at. This is precisely why MinerU vendors the model rather than depending on it — and
why the operator's "ordinary Python package" test has a nuanced answer: *the package exists and
is Apache-2.0, but installing it is the wrong move.* **Vendor the model code the way MinerU
does.** Confirmed working here: `transformers 4.52.3`, `torch 2.7.0+cu126`, plus `ftfy` and
`loguru`. No serving stack anywhere.

⚠ **The only distribution format is a pickle.** `wanderkid/*` ship `.pth`, not safetensors.
MinerU mitigates with `torch.load(..., weights_only=True)` at
`modeling_unimernet.py:110` — keep that if vendoring. A safetensors variant exists only inside
`opendatalab/PDF-Extract-Kit-1.0` at `models/MFR/unimernet_hf_small_2503/model.safetensors`
(810 MB) — and **that repo carries no licence tag at all**, so the Apache-2.0 on `wanderkid/*`
does not automatically extend to it. UNVERIFIED.

### 2.3 UniMERNet is still the default in the leading open pipeline

*Verified in the local clone:* MinerU 3.4.5 `mineru/backend/pipeline/model_init.py:61-68` sets
`MFR_MODEL = "unimernet_small"` unless `MINERU_FORMULA_CH_SUPPORT` is truthy, in which case it
switches to PP-FormulaNet-plus-M. `enum_class.py:102` resolves it to
`models/MFR/unimernet_hf_small_2503`. **As of a 2026-08-14 commit, the strongest open document
pipeline still routes every formula through UniMERNet, and only swaps it out for Chinese.**
That is the single best currency signal available, and it is worth more than the download
counts (855/month for `unimernet_base`, which look alarming until you realise nobody fetches
it directly — they fetch PDF-Extract-Kit).

### 2.4 pix2tex — disqualified for handwriting, and the number in the earlier doc is wrong

BLEU **0.012** on UniMER-Test HWE is verified in both the UniMERNet and CDM papers. The CDM
figure in [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) is **0.213; the published
value is 0.2453** — and the more damning statistic is **ExpRate@CDM 0.0060**, i.e. six
handwritten expressions in a thousand recognised exactly. The conclusion is unchanged and the
correction is minor, but cite 0.2453.

Root cause is in the repo's own TODO: trained on arXiv printed formulae, *"support handwritten
formulae (kinda done, see training colab notebook)"*. MIT repo badge, but an early release note
said the weights were CC BY-NC-SA because of the training data — **treat the weights licence as
contested, not MIT.** Dormant since 2025-01-18, 159 open issues, not archived.

### 2.5 texify — the licence is *not* the OpenRAIL trap, but it is GPL

The operator's suspicion was well-founded but lands on the wrong project. Checked separately:

| Artefact | Licence |
| --- | --- |
| `VikParuchuri/texify` code | **GPL-3.0** (verbatim GPLv3 LICENSE file) |
| `vikp/texify` weights (what the archived code loads) | **CC BY-SA 4.0** — commercial OK |
| `datalab-to/texify` weights (the surya-era model) | **CC BY-NC-SA 4.0 — non-commercial** |
| `datalab-to/surya` code | Apache-2.0 |
| `datalab-to/surya` **weights** | **modified AI Pubs OpenRAIL-M** |

**The threshold is $5,000,000, not $2M** — and it applies **twice, independently**:
Attachment A §2(a) *gross revenue in the prior year*, §2(b) *total equity **or debt** funding
raised, cumulative, from any source*. Either alone disqualifies. Web sources still quoting $2M
are citing a superseded revision; Datalab **raised** it, and nothing guarantees it stays there.

The competitor clause is §2(c) and it is the sharp one:

> *(c) for any purpose if You (your employer, or the entity you are affiliated with) provides or
> otherwise makes available any product or service that competes with any product or service
> offered by or made available by Licensor or any of its affiliates.*

**No revenue floor and no personal/research carve-out** — unlike (a) and (b), which both exempt
personal and research use. Datalab sells document OCR; anything shipping document extraction is
arguably caught at any size.

Practically it does not matter, because **surya has no crop-in → LaTeX-out entry point any
more.** The archived texify README points users at `surya_latex_ocr`; that console script no
longer exists in surya 0.22.1, and `surya/scripts/` has no `latex_ocr.py`. Surya returns
`<math>…</math>` inline in page-level HTML. **Different task shape. Not a drop-in.**

### 2.6 What is newer — searched, not assumed

| Candidate | Verdict for this project |
| --- | --- |
| **PP-FormulaNet_plus-M/L** (2025-03, `2503.18382`, Apache-2.0) | **The real alternative.** `pip install paddleocr`, three lines of Python, no server. plus-L reaches HWE CDM ~0.947 per MinerU2.5's Table 11 — parity with UniMERNet-B. **But it pulls `paddlex` + PaddlePaddle**, a second DL framework next to torch on a 6 GB card. And the small end is weak on handwriting: PP-FormulaNet-**S** is HWE CDM **0.818**, well below UniMERNet-Tiny's 0.9328 at a similar size |
| **Texo** (2026-02, `2602.17189`, 20M) | Genuinely impressive — HWE CDM **0.902** at 20M, 7× faster than UniMERNet-T. **But it does not beat UniMERNet** (0.902 < 0.9328 for Tiny; its own table says so), it is **AGPL-3.0**, and it is clone-and-`uv sync`, not a package |
| **TexTeller 3.0** (`2508.09220`, Apache-2.0, 298M) | Claims CROHME14 88.0 / HME100K 90.7 / MathWriting 81.0 ExpRate — which would be a landslide. **Do not act on it.** The HF weights' `lastModified` is **2024-06-22** and the paper is **August 2025**: the released checkpoint predates the paper by 14 months. Its own README and model card disagree on the training-set size (80M vs 7.5M). PyPI pins `transformers==4.47`. `engine-landscape-2026-09.md` already flagged this as self-inconsistent; the release dates confirm it. **UNVERIFIED and treated as unreleased** |
| **UniRec-0.1B** (2025-12, `2512.21095`, CC BY 4.0) | Claims −10.4% edit distance vs UniMERNet-B at 0.1B. **No CDM, no HWE number published.** Unproven for handwriting |
| **Uni-MuMER-Qwen3.5-2B** (Apache-2.0 base *and* derivative) | Licence chain is genuinely clean, unlike the Qwen2.5-VL-3B variant. **But 2.2B fp16 ≈ 4.4 GB of weights against 4.3 GB of headroom**, and the repo's inference path is `scripts/vllm_infer.py`. Fails the operator's constraint twice |
| **DocTron-Formula** (3B/7B), **GryphOne**, **MinerU2.5-Pro** | Too large, or vLLM-shaped, or unverifiable |

**Nothing published since 2024 has a releasable, permissively-licensed, sub-1B checkpoint with a
UniMER-Test HWE score above UniMERNet's.** The field moved on printed and Chinese formulae, not
on handwriting.

---

## 3. The 36.56 claim — verified, and the earlier framing of it was wrong

**Both numbers are real.** MinerU2.5 scores **94.42** Formula CDM on UniMER-HWE
(`2604.04771v1` Table 5; its own paper rounds to 94.4) and **36.56** on WildHandBench
(`2608.22959`, 2026-08-24), verbatim: *"MinerU-2.5 achieves a Formula CDM of 36.56."*

**But the 58-point gap is not a crop-quality effect, and neither paper draws the comparison —
it was our synthesis.** The two evaluations are different tasks:

| | UniMER-Test HWE | WildHandBench Formula |
| --- | --- | --- |
| Input | **6,332 pre-cropped single formulae** | **500 full handwritten document pages** |
| Task | recognition only | **detection + recognition + reading order + structure, one pass** |
| A formula the layout stage misses | cannot happen | **scores zero** |

WildHandBench also carries a human baseline (86.56 formula CDM) and reports that general VLMs
produce 63–79% *prior-driven* errors — fluent output unsupported by the image — against 49% for
humans.

**Consequence for this project: 94.42 is our column, not 36.56.** `ocr_handler` does not ask a
model to find the formulae; [`ink.py`](../../src/ocr_handler/ink.py) already does that
structurally, and structural extraction is *exact*. The pre-cropped number is the one that
describes our pipeline. `mineru-teardown.md` §"the formula/text gap is really a cropped/full-page
gap" reached the right conclusion for a slightly wrong reason — it is a *detection* gap, and we
do not have a detection problem.

**The caveat that does survive** is sharper and is in [§4.4](#44-the-benchmark-does-not-measure-our-task).

---

## 4. Crop quality — the integration risk, measured

Guidance exists, but not where you would look for it: **there is no paper on how tightly to crop
a formula, and five different production pipelines hard-code five different answers**
([§4.0](#40-what-other-pipelines-actually-do)). The one published *ablation* is on crop **scope**,
not padding ([§4.2](#42-padding--a-plateau-then-a-cliff)). So the rest was measured, on this
project's own fixture page
(`content/cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf` p.4, rendered 1700×2200
at 200 dpi) using boxes located by exact pixel match against the committed crops:

| Target | Box | Ground truth |
| --- | --- | --- |
| `eqline` | (500, 1370, 1220, 1500) | `= \|\alpha\|^{n}(\cos(\omega_0 n) + j\sin(\omega_0 n)).` |
| `expo` | (1080, 1050, 1580, 1210) | `(e^{j\omega_0})^{n} = e^{j\omega_0 n}` |

### 4.0 What other pipelines actually do

No paper states a padding rule. Five shipped pipelines state five different ones, in code:

| Pipeline | Expansion around the formula bbox | Where |
| --- | --- | --- |
| **MinerU → UniMERNet** | **zero** — `floor`/`ceil` and clamp only | `mfr/unimernet/Unimernet.py` `batch_predict` |
| MinerU → *text* regions (contrast) | **+50 px white every side** | `backend/pipeline/batch_analyze.py:713` |
| **surya** | **+4 px fixed** | `surya/recognition/__init__.py:47` `_crop_block(pad=4)` |
| **marker** (LLM equation redo) | **+5% of w/h per side** | `processors/llm/llm_equation.py`, commented *"Equations sometimes get bboxes that are too tight"* |
| **docling** `CodeFormulaModel` | **+18% of w/h per side** | `models/code_formula_model.py:69-71`, `expansion_factor = 0.18` |
| **PaddleX / PP-StructureV3** | 1.0 (none) by default, `layout_unclip_ratio` knob, per-class capable | `configs/pipelines/formula_recognition.yaml` |
| CDM's own renderer | +8 px at 200 dpi | `cdm/modules/latex2bbox_color.py:117` |

Rasterisation DPI: **MinerU 200** (`DEFAULT_PDF_IMAGE_DPI`, longest side ≤3500), **marker 192**
for equations specifically (96 for layout; `BlockTypes.Equation` is in `highres_block_types`),
**docling 120**, **CDM 200**. And the number that anchors all of them — **UniMERNet's own paper
says its training renders used "a DPI setting varying between 80 to 350."** Outside that band you
are extrapolating. `ocr_handler` renders at 200 dpi today; that is mid-range and correct.

**Its augmentation pipeline says what it tolerates** (`unimernet/processors/formula_processor.py`,
cross-checked against the paper's Data Augmentation section):

- Tolerated: JPEG artefacts (quality ≥95), Gaussian noise σ≈10, mild brightness/contrast shift,
  erosion/dilation of strokes, fog/frost/rain/snow/shadow, coloured backgrounds.
- **`rotate_limit=1` — one degree of skew, and that is all.** Same in pix2tex. **Deskew before
  cropping; the recogniser will not do it for you.**
- **`scale_limit=(-.15, 0)` — shrink only, never enlarge.**
- The whole geometric + degradation block is gated at **`p=.15`**: 85% of training samples were
  clean.

### 4.1 What the model actually sees — read from the source, not guessed

From `preprocessor_config.json` on the hub and MinerU's
`unimer_swin/image_processing_unimer_swin.py`:

1. **`crop_margin` runs first and re-tightens your crop.** It min-max normalises to grayscale,
   thresholds at `< 200`, takes the bounding rect of every dark pixel, and crops to it.
   **Padding you add is discarded** — unless it contains ink, in which case it is kept in full.
2. **Aspect ratio preserved**, `scale = min(192/h, 672/w)`, then centre-padded to **192×672**
   with **black** letterbox bars (`ImageOps.expand` default fill, `cv2.BORDER_CONSTANT value=0`).
3. Grayscale, normalised `(g − 0.7931·255) / (0.1738·255)`, then repeated to 3 channels.
4. **MinerU adds zero padding to the detected bbox** — `floor`/`ceil` and clamp, nothing more
   (`Unimernet.py:_normalize_bbox`). It relies entirely on the detector's box.
5. **PP-FormulaNet reuses the identical `crop_margin`**, at 384×384
   (`pp_formulanet_plus_m/processors.py:UniMERNetImgDecode`, `predict_formula.py:63`).
   **The crop findings below generalise to it.**

**192×672 is not arbitrary — it is 1:3.5**, and the CVPR-2026 paper says why: *"we analyze
common aspect ratios of formula images and find an average of 1:3.5."* Three consequences fall
out of the geometry before any run:

- **A single-line formula is width-bound.** A 1600×150 display equation scales by
  `min(1.28, 0.42) = 0.42` → 672×63. **The model never sees more than 672 px of horizontal
  detail**, so there is no benefit to rendering wider — and a *long* equation is squeezed
  harder than a short one. This is why CPE is a harder subset than SPE, and why the unreleased
  CVPR-2026 `†` variant gains most on CPE (+1.7 CDM) by doubling to 384×1344.
- **A tall, near-square multi-line equation wastes ~90% of the canvas.** At 1:1 it letterboxes
  into 192×192 of a 192×672 frame. **PP-FormulaNet's 384×384 has the opposite bias** and is the
  better shape for a stacked derivation — a genuine reason to route by aspect ratio rather than
  to pick one model for everything.
- **Two equations merged into one crop halve the resolution of both.** `ink.py`'s
  `regions(merge_px=64)` is the knob that decides this.

### 4.2 Padding — a plateau, then a cliff

*Measured*, UniMERNet-Base, fp16, greedy, one crop at a time:

| pad (px @200 dpi) | `eqline` output | `expo` output |
| ---: | --- | --- |
| −24 | `= 1 \times 1^{n}(\cos(\cos n)+j\sin(w_0,n)).` | `e^{iwo})^{n}=e^{\frac12 woh}` |
| −16 … +4 | `= 1\alpha\vert^{n}(\cos(\cos n)+j\sin(w\sin)).` **— identical across 5 settings** | *identical* |
| +12 | `= 1\alpha\vert^{n}(\cos(w_0 h)+j\sin(w_0 h)).` | *identical* |
| +24 | `= 1\times 1^{n}(\cos(\omega_0 h)+j\sin(w_0 h)).` | *identical* |
| +48 | **`\begin{array}{l}{{\displaystyle \chi(n)=\alpha^{n}=…`** ← reading the line above | *identical* |
| +96 | `\begin{array}{l}{ \chi[n]=\alpha^{n}=…` (150 tok) | **identical — still correct** |
| +160 | `\begin{array}{rl}&{\alpha=\vert\alpha\vert…` (222 tok) | **`({\ e \sp \prime \cos\theta})\sp n=…`** ← breaks |
| +300 | 423 tok of array garbage | 561 tok of array garbage |

**The rule, and it is predictive.** *Measured* distance from each box to the nearest
neighbouring content, over the box's full width:

| Target | gap above | gap below | plateau held to | broke at |
| --- | ---: | ---: | ---: | ---: |
| `eqline` | **6 px** | 675 px | +24 | **+48** |
| `expo` | **141 px** | 216 px | **+96** | **+160** |

> **Padding costs nothing until the crop touches the next thing on the page. Then it does not
> degrade — it switches the model into multi-line `\begin{array}` mode and the answer is lost.**

`expo` sits in white space and tolerates **8× more padding** than `eqline`, which sits 6 px
below a printed line. **Crop tolerance is a property of the page, not of the model.** So the
right integration is not a tuned constant — it is *"expand until you are within a few pixels of
the nearest other region, and no further"*, which `ink.py` can compute because it already has
every region's box.

`ink.py`'s current `crop(pad=12)` is inside the safe band on both targets. It is not obviously
optimal — on `eqline`, +12 changed the answer versus 0 (arguably improving it, from `\cos(\cos n)`
to `\cos(w_0 h)`), which is a reminder that **within the plateau the output is stable; at the
edges it is not.**

**This reproduces a published result, which matters because n=2.** DocTron-Formula
(`2508.00311` Table 3) feeds the same models line-, paragraph- and page-scoped crops of
CSFormula, CDM ↑:

| Model | line | paragraph | page |
| --- | ---: | ---: | ---: |
| **UniMERNet** | **0.919** | **0.644** | **0.009** |
| Qwen2.5-VL | 0.924 | 0.746 | 0.197 |
| GPT-4o | 0.879 | 0.569 | 0.161 |
| Mathpix | 0.926 | 0.696 | 0.579 |

**A line-level specialist fed an over-scoped crop does not degrade — it goes to zero**, and it
falls *further and faster than a general VLM or Mathpix.* My `\begin{array}` garbage at +48 px is
the small-scale version of that 0.919 → 0.009. It also sharpens
[§9](#9-the-strongest-argument-against-my-own-recommendation): **a page VLM is structurally more
forgiving of a bad crop than a formula specialist is**, and our crops come from a heuristic.

### 4.3 Resolution — far less important than expected

*Measured*, crop rescaled at pad=+12:

| effective dpi | crop px | `eqline` | `expo` |
| ---: | --- | --- | --- |
| 400 | 1488×308 | `\cos(w_0 h)+j\sin(w_0 h)` | `e^{iwo})^n=e^{\frac12 woh}` |
| 200 | 744×154 | *same* | *same* |
| 150 | 558×115 | `\cos(\cos n)+j\sin(w,n)` ← worse | `e^{iw_0})^n=e^{\frac12 w_0 r}` ← **better** |
| 100 | 372×77 | `\cos(w_0 h)+j\sin(w_0 h)` ← back | *same as 150* |
| 70 | 260×53 | `\cos(\cos n)+j\sin(w_1,t)` | `(e^{iw_0})^n=…` ← recovers the `(` |
| 50 | 186×38 | `\cos(\cos n)+j\sin(n\times1)` | `(e^{iw/2})^n=e^{\frac12 w/2 n}` |
| 30 | 111×23 | collapses | collapses |

Two things, and the second matters more than the first:

1. **Usable output survives a 4× downscale.** Structure holds to ~50 dpi, then collapses at 30 —
   and the training range is **80–350 dpi**, so the collapse happens exactly where the input
   leaves the distribution. Rendering above 200 dpi buys nothing anyway: the 192×672 input is the
   ceiling, and the published 2× -resolution ablation gains only **+0.1 CDM on SCE** (the
   degraded subset) against +1.7 on long printed formulae. **DPI is not the bottleneck.**
2. **The response is not monotonic.** 150 dpi was *worse* than both 200 and 100 on `eqline`,
   and *better* than both on `expo`; 70 dpi recovered a parenthesis that 200 dpi lost. **Do not
   tune DPI to fix a bad reading** — you are sampling resampling noise, and n=1 will mislead you.
   This is §1.7's quantisation-ladder lesson from `engine-landscape-2026-09.md` in a new place.

### 4.4 The benchmark does not measure our task

`expo` is read **wrong at every padding and every resolution**: `e^{iwo})^{n}=e^{\frac12 woh}`
against a ground truth of `(e^{j\omega_0})^{n}=e^{j\omega_0 n}` — the leading `(` dropped, `j`
read as `i`, and a **`\frac{1}{2}` invented**. Looking at the fixture explains it: the
handwriting sits on the **light-blue graph-paper grid** of the underlying slide. Grayscale
conversion turns the grid into mid-grey rules, and the model reads a horizontal rule as a
fraction bar.

**UniMER-Test HWE is clean isolated handwriting sourced from CROHME and HME100K.** Our task is
handwriting *over printed content*, on grid paper, mixed with printed glyphs in the same
expression. **No published benchmark measures that**, and the 0.94 HWE figure does not describe it.

### 4.5 The largest available accuracy win is not the model — it is the background

*Measured*, same crops, same model, five renderings. `flatten` keeps true greys and whitens
everything else; `inkmask` is `ink.py`'s own binary red∪dark mask.

| | UniMERNet-Base output |
| --- | --- |
| `eqline` / **raw** | `= 1\alpha\vert^{n}(\cos(w_0 h)+j\sin(w_0 h)).` |
| `eqline` / **flatten** | `= 1\alpha\vert n(\cos(`**`\omega_0 n`**`)+j\sin(`**`\omega_0 n`**`)).` |
| `eqline` / **inkmask** | **`= \vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).`** ← best of all 84 runs |
| `expo` / **raw** | `e^{iwo})^{n}=e^{`**`\frac12`**`woh}` ← grid read as a fraction |
| `expo` / **inkmask** | `e^{iw_0})^{n}=e^{iw_0 r}` ← **`\frac12` gone, subscript recovered** |

`eqline/inkmask` recovers `|\alpha|^{n}` (raw gives `1\alpha\vert`) *and* the `\omega_0`
subscript. **The `\frac{1}{2}` hallucination is entirely a background artefact** — it vanishes
under `redblack`, `inkmask` and `redmask` alike.

> **Feeding UniMERNet the mask that `ink.py` already computes is worth more than any padding,
> DPI or model-size change measured here.** It is free, deterministic, needs no GPU, and it is
> the project's existing code.

The catch: masking is only available where the ink is separable — the annotated `-plw` lectures.
For a scanned textbook page there is no red channel to key on, and the raw crop is all there is.

### 4.6 Tiny and Base disagree usefully

*Measured*, both sizes over all 20 renderings. They fail on **different** symbols, confirming
the note in `research/INDEX.md` with a bigger sample:

- `cos_only/raw` — Tiny `(\cos(\omega_0 n)+` **correct**; Base `(\cos(won)+` wrong.
- `expo/*` — Tiny keeps the leading `(` in every rendering; **Base drops it in every one.**
- `eqline/*` — Base is clearly better; Tiny loses `|\alpha|^n` and both subscripts.

At 232 MiB and 0.14–0.44 s, running Tiny alongside Base costs almost nothing and gives a real
disagreement signal. **Both fit simultaneously** (232 + 686 = 918 MiB allocated).

### 4.7 Everywhere else, finding the box is the whole problem

OmniDocBench (`2412.07626`) measures both halves separately, and the gap is enormous:

| | Formula CDM |
| --- | ---: |
| UniMERNet-B, **ground-truth crops** (component-level, Table 9) | **85.0** |
| MinerU **end-to-end**, its own detector's crops (Table 2, EN) | **57.3** |
| Best layout detector (DocLayout-YOLO), average mAP across doc types | **47.38** |

**~28 CDM points are lost upstream of the recogniser**, on a pipeline whose recogniser *is*
UniMERNet. (Two caveats: MinerU defaults to `unimernet_small` not `-B`, but that gap is 1–3
points, not 28; and end-to-end also folds in formula matching and inline formatting.)

> **At MinerU-class detection quality, effort spent on bbox quality beats effort spent swapping
> recognisers by roughly an order of magnitude.**

`ocr_handler` is in an unusually good position here **for the annotated-lecture path only**:
[`research/INDEX.md`](INDEX.md)'s structural extraction gives exact ink coordinates from the PDF,
so there is no detector to be wrong. **For the 430-document scanned/printed path there is no such
shortcut** — a formula detector would have to be added, and this table is what it would cost.
That is an argument for finishing the text-layer path before building the formula path at all,
which is what [`roadmap.md`](../roadmap.md) already says.

---

## 5. Validating the output — compiling it does not work

Every string both sweeps produced (84) was wrapped in a minimal `article` + `amsmath` document
and compiled with `tectonic 0.16.9`, the same binary
[`docs/latex/build_tex.sh`](../../../docs/latex/build_tex.sh) uses.

| Detector | Result |
| --- | --- |
| **tectonic compile-check, post-repair** | **83 / 84 compiled (99%)** |
| **tectonic compile-check, pre-repair (raw model output)** | **43 / 44 compiled (98%)** |
| **token-variety ratio < 0.20** | **8 / 10 pathologies caught, 0 false positives in 76** |

**Compile-checking is nearly useless as a hallucination detector.** 1113 tokens of array garbage
from a whole page compiles. A hallucinated fraction from blank paper compiles. Only
`expo/pad+300` failed. The obvious hypothesis — *MinerU's repair suite is destroying the signal*
— is **wrong**: raw output compiles at the same rate. UniMERNet's greedy decoder simply emits
syntactically valid LaTeX almost always, because it was trained on valid LaTeX.

**This is not a small-sample artefact.** The CDM authors ship a render-checker
(`cdm/modules/latex_render_percentage.py`: `pdflatex -interaction=nonstopmode`, 15 s timeout,
`item['renderable']`) and publish its rates on all 23,757 UniMER-Test expressions:

| Model | render success | + syntax errors caught by a KaTeX pass |
| --- | ---: | ---: |
| **UniMERNet** | **99.71%** | 1.05% total bad |
| Mathpix | 97.82% | 2.38% |
| Texify | 94.77% | 5.03% |
| Pix2tex | 96.63% | **13.83%** |

**My measured 98.8% sits right on their 99.71%.** Their §5.2.1 policy — a prediction that fails
to render scores CDM 0 — is right for *scoring* and useless as a *gate*, because for UniMERNet it
fires on 1 output in 350. Note the pix2tex row: **a KaTeX parse catches ~4× more bad output than
a compile does** (13.83% vs 3.37%). The two fail on disjoint sets, so if a syntax gate is wanted,
KaTeX is the better half of it and `pdflatex` is the expensive half.

**What does work is a token-variety ratio** — distinct token types ÷ total tokens, over a
`\\[a-zA-Z]+|.` tokenisation. *Measured separation:*

| Case | ntok | types | ratio |
| --- | ---: | ---: | ---: |
| `patho/whole_page` | 1113 | 37 | **0.021** |
| `patho/merged_two_equations` | 626 | 46 | **0.045** |
| `eqline/pad+300` | 423 | 43 | **0.063** |
| `eqline/pad+48` | 146 | 29 | **0.120** |
| `expo/pad+160` | 84 | 22 | **0.193** |
| — threshold 0.20 — | | | |
| `eqline/scale0.15` (bad but not degenerate) | 54 | 20 | 0.238 |
| every good crop | 39–64 | 12–21 | 0.245–0.44 |

A plain length threshold would miss `patho/blank_paper_pad96` (57 tokens). The ratio is strictly
better. Two rules cover almost everything, and neither needs a model or a TeX run:

```python
ratio < 0.20 and ntok > 40   ->  degenerate; the crop is wrong, not the reading
ntok < 5                     ->  nothing was there
```

**The one failure nothing catches is the important one.** `patho/blank_paper_pad96` — an empty
patch of paper — returned `\textstyle{\frac{1}{11110 \times 1111111111111}}` (57 tokens, ratio
0.254): a **confident, well-formed, compilable hallucination.** It compiles, it passes the
variety test, and it is entirely invented. This is `crop_margin`'s min-max normalisation
amplifying faint speckle to full contrast and the model dutifully reading it.

**It is already preventable structurally**, and that is the answer rather than a smarter
detector: `ink.py`'s `regions(min_pixels=120)` would never have emitted that box.
**Never send a crop that did not come from a region with real ink in it.** The smaller sibling
`patho/blank_paper` (no padding) returned `-`, 2 tokens — caught by the `ntok < 5` rule.

surya solves the same problem the same way and its constants are worth copying —
`surya/common/blank.py`, used to *"drop hallucinated layout blocks over empty space"*:
`BLANK_WHITE_THRESHOLD = 245`, `BLANK_PIXEL_FRACTION = 0.99`, `UNIFORM_COLOR_STD = 8.0`.
**A pre-inference blank check is cheaper and more reliable than any post-hoc test on the output.**

### 5.1 What MinerU does *not* ship, and what to borrow instead

MinerU's `generate()` (`modeling_unimernet.py:164-198`) is plain greedy with **no
`repetition_penalty`, no `no_repeat_ngram_size`, no `StoppingCriteria`, and no returned scores** —
and the checkpoints' own `config.json` confirms `num_beams: 1`, `repetition_penalty: 1.0`,
`no_repeat_ngram_size: 0`. Nothing prevents a loop, which is why `patho/whole_page` ran to 1113
of its 1152-token budget. Note also that the budget is **VRAM-dependent** — 1152 on ≤6 GB, 1344
above (`modeling_unimernet.py:183-187`) — so *the truncation point differs between machines* and
any length heuristic must be expressed relative to it, not as a constant.

Two production detectors exist and neither needs retraining:

- **surya `_detect_repeat_loop`** (`surya/recognition/__init__.py:88-113`) — string-level, ~20
  lines, no logits. Scans tail substrings up to a 500-char window; short repeats need many
  occurrences, long repeats only four. surya wires it to *recovery* (fall back to per-block OCR),
  not just a flag. **This is the one to lift** — my token-variety ratio is a cruder version of it.
- **nougat `StoppingCriteriaScores`** (`nougat/model.py:442-474`) — logit-level, stops generation
  when the variance-of-variance of the max logit falls below 0.015. Better, but requires
  `output_scores=True`, which MinerU's wrapper discards.

Also available for free: `eos_reached` — did generation stop on EOS or hit the cap? A run that
hit the cap is the classic loop signature, and it needs no heuristic at all.

**Recommended cascade, cheapest first** (each stage is independent and cheap enough to always run):

| Stage | Cost | Catches |
| --- | --- | --- |
| 1. blank-crop guard *before* inference (`min_pixels`, surya's constants) | µs | the confident hallucination nothing else catches |
| 2. `eos_reached == False` / token count near cap | free | truncation and loops |
| 3. repetition detector (surya's, or the variety ratio) | µs | degenerate output from an over-scoped crop |
| 4. `pylatexenc.LatexWalker(tolerant_parsing=False)` | µs | unbalanced braces, environment mismatch |
| 5. KaTeX `__parse` / `throwOnError` | ms | grammatical nonsense — ~4× the yield of a compile |
| 6. `tectonic` on a sample | ~1 s | the last 1%; **not** a per-expression gate |

`sympy.parsing.latex` / `latex2sympy2` are **not** suitable — SymPy's own docs call the parser
experimental, it does not support `\begin{env}…\end{env}` or matrices at all, and it can fail to
parse without raising. It would reject correct output constantly.

The other guard already recorded in this project stands and was reproduced twice today:
**always run the un-annotated twin.** `control/eqline_base_twin` → `= 1\alpha1^{n}( + j)).`,
`control/expo_base_twin` → `\mp` (3 tokens). The blanks come back empty. That is proof the model
is reading ink and not confabulating, and it costs one extra inference.

---

## 6. Vendoring `mineru/model/mfr/utils.py` — yes, with four caveats

Read in full (448 lines, `import re` only). The teardown's recommendation holds:
`latex_rm_whitespace` composes brace balancing, `\left`/`\right` repair and re-pairing,
environment `\begin`/`\end` completion, unsupported-command removal and `\qquad` spacing, and
`build_mfr_batch_groups` is a genuinely good area-sorted dynamic batcher. Four things the
teardown did not surface:

1. **⚠ The licence is not plain Apache-2.0.** `~/tmp/ocr_repos/MinerU/LICENSE.md` is
   *"Apache License 2.0 … subject to the additional terms below"*: a commercial licence is
   required above **100M MAU or USD 20M monthly revenue**, and §2 imposes an **attribution
   obligation** — *"If you provide online services to third parties based on MinerU, you must
   clearly and prominently indicate … that MinerU is used."* Irrelevant to coursework notes;
   record it anyway, because §3 terminates the licence automatically on non-compliance.
   `mineru-teardown.md` calls this file "licence-clean", which is true in effect and imprecise
   in fact.
2. **⚠ `\Bar` → `\hat` is a semantic corruption.** `REPLACEMENTS_PATTERNS` (`utils.py:281-284`)
   maps `\Hat→\hat`, `\Tilde→\tilde`, `\Dot→\dot` — all correct — and **`\Bar→\hat`**, which
   silently turns $\bar{x}$ into $\hat{x}$. Almost certainly a typo for `\bar`. In a maths
   transcription tool that is a wrong answer, not a formatting nit. **Fix on vendoring.**
3. **`remove_up_commands` over-reaches.** `\up([a-zA-Z]+)` strips `up` from anything not in
   `{arrow, downarrow, lus, silon}` — so `\upharpoonright` becomes `\harpoonright`. Rare, but
   it is a silent rewrite, which [`scope.md`](../scope.md)'s blacklist forbids on extracted text.
4. **Compile-checking will not audit it.** Per [§5](#5-validating-the-output--compiling-it-does-not-work),
   input and output both compile 98–99% of the time, so the repair suite's edits are invisible
   to a TeX run. Test it against fixtures, not against the compiler.

**The batcher does not apply yet.** `build_mfr_batch_groups` earns its keep on pages with dozens
of mixed inline and display formulae. Our fixture page has **five** regions. It is right for the
scanned-textbook path later; it is not today's work.

### 6.1 The preprocessor can be reimplemented without opencv

[ADR-0002](../decisions/0002-numpy-scipy-pillow-not-opencv.md) excludes opencv, and MinerU's
image processor uses `cv2` for four things: `cvtColor`, `findNonZero`+`boundingRect`, `resize`,
`copyMakeBorder`. All four have numpy/Pillow equivalents. *Measured*, a 25-line
numpy+Pillow reimplementation against MinerU's on four real crops:

| crop | max abs diff | mean abs diff |
| --- | ---: | ---: |
| `eqline`, `expo`, `cos` | **0.0226** | 0.00035–0.00047 |
| `wide` (1400×220, heavy downscale) | **0.8349** | 0.0065 |

Normalised units span roughly ±4.5 from paper to ink, so 0.0226 is ~0.5% of dynamic range —
irrelevant. **But the `wide` case is a real divergence**: Pillow's `BILINEAR` antialiases on
downscale and `cv2.INTER_LINEAR` does not. Pillow's is probably the *better* input for OCR, but
it is a different input, and this project's whole ethos is not to change things silently.
Script kept at `tmp/eqocr/nocv2.py`. **Either accept `cv2` for this one module or record the
resampler swap as a deliberate deviation. Do not do it by accident.**

---

## 7. Recommendation

**Keep UniMERNet-Base. Vendor it; do not `pip install` it. And spend the integration effort on
the crop, not on the model.**

| Decision | Why |
| --- | --- |
| **Engine: UniMERNet-Base**, 325M, Apache-2.0 | Highest releasable HWE score in the open field. 686 MiB / 1290 MiB reserved, **0.25 s per crop** — 10× faster than PaddleOCR-VL on the same crops. Still MinerU 3.4.5's default |
| **Ship Tiny alongside**, 107M | +232 MiB, +3.2 s load. *Measured* to be right where Base is wrong on this page's handwriting. Free disagreement signal |
| **Install shape: vendor MinerU's `mineru/model/mfr/unimernet/` + `mfr/utils.py`** | `pip install unimernet` hard-pins `transformers==4.42.4` and pulls Streamlit. There is no `trust_remote_code` path. Verified working here on `transformers 4.52.3` / `torch 2.7.0+cu126` + `ftfy` + `loguru` |
| **Feed it `ink.py`'s mask, not raw pixels**, wherever the ink is separable | The single largest measured accuracy gain. Free, deterministic, no GPU |
| **Pad to the nearest neighbour, not to a constant** | Padding is free inside the gap and catastrophic past it. `ink.py` knows every region's box, so it can compute the gap. As a floor, marker's +5% and docling's +18% are the shipped precedents; MinerU's zero is not |
| **Keep 200 dpi; do not tune it** | Mid-range of UniMERNet's own 80–350 dpi training band, already past the 192×672 ceiling, and the response is non-monotonic |
| **Deskew to within ~1°** | `rotate_limit=1` is literally all the rotation UniMERNet (or pix2tex) ever saw |
| **Guard *before* inference, not after** | Compile-checking catches 1 of 84 here and ~1 in 350 upstream. A blank-crop check plus `min_pixels` catches the only hallucination that survives every output-side test |
| **Add a repetition detector — MinerU ships none** | `generate()` is greedy with `repetition_penalty 1.0`, no n-gram blocking, no stopping criteria. Lift surya's `_detect_repeat_loop`, or use `ratio < 0.20 & ntok > 40` (8/10 caught, 0 false positives in 76) |
| **Keep the un-annotated-twin control** | Reproduced twice today. It is the only thing that catches a plausible hallucination *after* the fact |

**Deferred, deliberately:** PP-FormulaNet_plus-M is the one candidate that could displace this,
and there are now two reasons to keep it on the list rather than dismiss it — the Chinese/printed
side, and its **384×384 square input**, which suits a tall stacked derivation that UniMERNet's
1:3.5 frame wastes 90% of. It costs a whole second DL framework (`paddlex` + PaddlePaddle) beside
torch on a 6 GB card, so it is a *routing* option, not a replacement. Texo is 20M and AGPL and
*loses* to UniMERNet-Tiny on HWE. TexTeller's numbers describe a checkpoint that has not been
released.

---

## 8. Where this contradicts the earlier research

Those files are not edited. Contradictions are recorded here per
[`documentation-discipline.md`](../directives/documentation-discipline.md).

| Earlier claim | This document | Which is stronger |
| --- | --- | --- |
| `engine-landscape`: *"A 313M Apache-2.0 model beats Mathpix on handwritten expressions"* | True of a paper, **false of anything downloadable.** No CVPR-2026 checkpoint exists on the hub; last release 2024-12-26, no arXiv v3 | **This document.** The earlier doc's own parenthetical said UNVERIFIED; four independent checks now make it definite |
| `engine-landscape`: pix2tex HWE **CDM 0.213** | Published value is **0.2453** (CDM paper Table 2). ExpRate@CDM is **0.0060** | **This document.** Minor; conclusion unchanged |
| `mineru-teardown`: the 94.42/36.56 gap *"is really a cropped/full-page gap"* | Correct, and the reason is sharper: 36.56 is **detection + recognition + reading order**, where a missed formula scores zero. **We have no detection problem** — `ink.py` is exact. 94.42 is our column | **Both; this one is more precise.** It changes the number we should plan against |
| `mineru-teardown`: `mfr/utils.py` is *"licence-clean"* | MinerU is Apache-2.0 **plus additional terms** — 100M MAU / USD 20M monthly revenue thresholds and an online-service attribution obligation, with automatic termination | **This document.** True in effect for us, imprecise in fact |
| `research/INDEX.md`: Tiny is a *"cheap disagreement signal"* | Understated. On CDM, Tiny is within 0.7 points of Base on HWE at ⅓ the size, and *measured* here it is **outright better** on one of the two fixture equations | **This document.** Bigger sample, same direction |
| Implicit throughout: UniMERNet's ~0.94 HWE describes our task | **It does not.** UniMER-Test HWE is clean isolated handwriting from CROHME/HME100K. Ours is handwriting *over* printed slides and graph-paper grids, mixed with printed glyphs in one expression. **No benchmark measures that** | **This document.** Directly observed: a grid line became `\frac{1}{2}` |

**Standing and reinforced:** the un-annotated-twin control (reproduced twice today); serialising
GPU work; routing born-digital pages away from any model; structural ink extraction as *exact*
where a model is approximate. `ink.py`'s region grouping turned out to be the most valuable
thing in the pipeline for equation accuracy, not merely a cropper.

---

## 9. The strongest argument against my own recommendation

**PaddleOCR-VL-1.6 read one of the two fixture equations exactly right, and UniMERNet-Base did
not — at any padding, at any resolution, in any rendering.**

Both measured on this machine, on these crops. PaddleOCR-VL's numbers are the prior session's,
in `tmp/eval/out_crops/results.json`; UniMERNet's are today's.

| Crop | Ground truth | **PaddleOCR-VL-1.6** (`Formula Recognition:`) | **UniMERNet-Base**, best of 24 variants |
| --- | --- | --- | --- |
| `expo` | `(e^{j\omega_0})^{n}=e^{j\omega_0 n}` | **`(e^{j\omega_{0}})^{n}=e^{j\omega_{0}n}` — exact** | `e^{iw_0})^{n}=e^{iw_0 r}` — 3 errors |
| `eqline` | `=\|\alpha\|^{n}(\cos(\omega_0 n)+j\sin(\omega_0 n)).` | `=\|\alpha\|^{n}\left(\cos(\omega n)+j\sin(\omega n)\right).` — **subscripts dropped** | `=\vert\alpha\vert^{n}(\cos(\omega_0 n)+j\sin(w_0 n)).` — one subscript short |

On `eqline` UniMERNet-with-the-mask is arguably ahead. On `expo` it is not close. And there is a
process problem underneath: PaddleOCR-VL was given the **raw** crop, UniMERNet needed
`ink.py`'s mask to get as far as it did. A fair rematch would give both the mask.

Four more things that cut against me:

1. **A 325M special-purpose model is being kept for a job a 0.9B general page model already
   does better, on a card that fits the 0.9B model.** PaddleOCR-VL measured 1767 MiB allocated
   here — 1.4× UniMERNet-B's *reserved* figure, not 3×. The "cheapest thing that works"
   argument is weaker than it looks once `reserved` rather than `allocated` is the number.
2. **The benchmark I am relying on does not measure our task**, and I said so myself in
   [§4.4](#44-the-benchmark-does-not-measure-our-task). Recommending on UniMER-Test HWE while
   arguing that UniMER-Test HWE is unrepresentative is having it both ways. The honest position
   is that **the fixture page is the only evidence that counts, and on it the result is a split
   decision at best.**
3. **UniMERNet's model code has not changed in ~2 years.** The `unimernet` package is 20 months
   stale, the weights are from September 2024, the CVPR-2026 successor is unreleased, and the
   only reason it still looks current is that MinerU keeps vendoring it. PaddleOCR-VL shipped
   1.5 and 1.6 in that window.
4. **n=2.** Two equations, one page, one course, one instructor's handwriting. Every conclusion
   in [§4](#4-crop-quality--the-integration-risk-measured) rests on that.
   The padding-cliff rule was confirmed on two independent boxes with very different neighbour
   distances, which is the strongest of them; the model comparison is the weakest.

**The resolution is not to overturn the choice on this document.** It is that the head-to-head
[ADR-0004](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md) calls for should
now be run **with the mask variants in the slate**, on more than two equations, scoring
PaddleOCR-VL-1.6 and UniMERNet-Base on *identical* inputs. If PaddleOCR-VL wins on masked crops
too, then it is one model for the whole pipeline and the specialist is redundant — which would
be a better outcome than the current two-model plan, not a worse one.

---

## Sources

**Measured here, 2026-09-05** — scripts under `tmp/eqocr/` (gitignored; re-run to reproduce):
`crop_sweep.py` (44 cases), `bg_sweep.py` (40 cases × 2 model sizes), `validate.py` (84 tectonic
compiles), `nocv2.py`. Raw JSON alongside them. Fixture:
`tmp/eval/fixtures/F1_cesc410_plw_i04.png` and its base twin `F1c_cesc410_base_i04.png`.

**Read locally:** `~/tmp/ocr_repos/MinerU` @ `4fe4bde`, v3.4.5 — `mineru/model/mfr/utils.py`,
`mfr/unimernet/{Unimernet.py,unimernet_hf/…}`, `mfr/pp_formulanet_plus_m/{processors,predict_formula}.py`,
`backend/pipeline/model_init.py:61-68`, `utils/enum_class.py:96-107`, `LICENSE.md`.

**Primary, verified today:** HuggingFace API `?blobs=true` for exact byte counts and licence
tags on `wanderkid/unimernet_{base,small,tiny}` and `wanderkid/UniMER_Dataset`;
`config.json` / `preprocessor_config.json` for all three checkpoints; PyPI JSON API for
`unimernet`, `pix2tex`, `texteller`, `texify`, `pix2text`, `paddleocr`.

**Papers:** UniMERNet `2404.15254` (+ CVPR 2026, openaccess, poster 39595) · CDM metric
`2409.03643` · WildHandBench `2608.22959` · MinerU2.5 `2509.22186`, -Pro `2604.04771` ·
PP-FormulaNet `2503.18382` · Uni-MuMER `2505.23566` · Texo `2602.17189` · TexTeller `2508.09220` ·
UniRec `2512.21095` · **DocTron-Formula `2508.00311`** (the crop-scope ablation) ·
**OmniDocBench `2412.07626`** (component vs end-to-end) · MathWriting `2404.10690` ·
OmniHandwritingOCR `2608.18586`

**Repos / licence files:** `github.com/opendatalab/UniMERNet` (LICENSE, releases, commits,
`unimernet/processors/formula_processor.py`, `cdm/modules/{latex_render_percentage,
latex2bbox_color,tokenize_latex}.py`) · `github.com/lukas-blecher/LaTeX-OCR`
(`settings/config.yaml`, `dataset/transforms.py`, `cli.py`) · `github.com/VikParuchuri/texify`
(LICENSE, README, settings.py) · `github.com/datalab-to/surya` (LICENSE, **MODEL_LICENSE**,
pyproject.toml, `recognition/__init__.py`, **`common/blank.py`**) · `github.com/datalab-to/marker`
(MODEL_LICENSE, `processors/llm/llm_equation.py`, `builders/document.py`) ·
`github.com/docling-project/docling` (`models/code_formula_model.py`) ·
`github.com/PaddlePaddle/{PaddleOCR,PaddleX}` (formula configs, `layout_unclip_ratio`) ·
`github.com/facebookresearch/nougat` (`model.py`, `postprocessing.py`) ·
`github.com/breezedeus/Pix2Text` · `github.com/OleehyO/TexTeller` · `github.com/alephpi/Texo` ·
`datalab.to/pricing` · `pylatexenc` and `katex` docs

---

**Related:** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) ·
[`mineru-teardown.md`](mineru-teardown.md) ·
[`../findings/layout-mode-decides-whether-math-survives.md`](../findings/layout-mode-decides-whether-math-survives.md) ·
[`../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md`](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md)
