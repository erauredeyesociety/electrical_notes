# GLM-OCR — source teardown, 2026-09-05

Static analysis of `github.com/zai-org/GLM-OCR` at `cef4d0e` (HEAD, pushed 2026-04-21),
cloned at `~/tmp/ocr_repos/GLM-OCR`. **No weights downloaded, no inference run, no GPU
touched, nothing installed.** Everything below is read from source, from the repo's own
example outputs, or from small text artifacts on Hugging Face (`config.json`,
`preprocessor_config.json`, the model's own `.eval_results/*.yaml`, the file manifest).
Behavioural claims cite `file:line`.

> Companion to [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md). That document is
> **not edited here**. Where this teardown corrects it, the correction is called out in
> [§10](#10-corrections-to-the-landscape-review).

---

## Verdict up front

**No. GLM-OCR should not displace PaddleOCR-VL as the recommended page engine.**

The single fact that reframes everything: **this repository contains no model code.** It is an
HTTP client and a two-stage orchestration pipeline. The 0.9B VLM never runs in this process —
it runs in vLLM, SGLang, Ollama or mlx-vlm, and the shipped default (`glmocr/config.yaml:35`)
is Zhipu's **cloud API**. What the repo *does* run locally is PP-DocLayoutV3, a 127 MiB
Apache-2.0 object detector. Every bounding box GLM-OCR emits comes from that detector; the
VLM emits none.

Five findings drive the verdict:

1. **It is a two-model pipeline too** — `Pipeline.__init__` unconditionally constructs
   PP-DocLayoutV3 (`glmocr/pipeline/pipeline.py:87-97`; module docstring line 6: *"Stages (all
   always enabled)"*). The "fewer moving parts" argument the landscape review raised against
   PaddleOCR-VL (§8.1) applies to GLM-OCR identically.
2. **ParseBench Text Formatting 2.3** (model card). That is the metric that disqualified
   Unlimited-OCR at 0.97. PaddleOCR-VL-1.6 scores 54.64. Our deliverable is Markdown/LaTeX.
3. **Old Scans 37.6** on the vendor's own olmOCR-Bench artifact — statistically the same as
   PaddleOCR-VL's 37.8 and only 2.2 above Unlimited-OCR's 35.4. It is **not** better on
   degraded scans, which is the category closest to our material.
4. **The handwriting evidence is weaker than the landscape review assumed.** 87.0 is an
   *in-house, unreleased* benchmark (paper Table 5). The one *public* handwriting number,
   Handwritten-KIE 86.1, has an **open, unanswered reproduction failure at "64+"**
   (issue #226, filed 2026-06-19, zero comments).
5. **Weights are 2.47 GiB, not 1.8 GB.** The "0.9B" headline excludes token embeddings, the
   LM head and the MTP module. It still fits 4.3 GB — but with less margin than assumed.

The strongest argument against this verdict is in [§11](#11-the-strongest-argument-against-my-own-answer)
and it is genuinely strong.

---

## 1. What this repository actually is

| Component | Where it runs | Source |
| --- | --- | --- |
| `PageLoader` | in-process, CPU | PyMuPDF render + PIL resize |
| `PPDocLayoutDetector` | in-process, **torch**, GPU or CPU | `glmocr/layout/layout_detector.py` |
| `OCRClient` | **HTTP client only** | `glmocr/ocr_client.py` |
| `ResultFormatter` | in-process, CPU, pure Python | `glmocr/postprocess/result_formatter.py` |

`OCRClient` is `requests.Session.post` and nothing else (`glmocr/ocr_client.py:289-295`). The
class docstring is explicit: *"Calls a remote API for recognition without requiring local
deployment of services"* (`glmocr/ocr_client.py:24-27`).

**The flow is: render page → detect regions → crop each region → POST each crop separately →
reassemble.** The VLM never sees a whole page. `glmocr/pipeline/_workers.py:364-370` builds one
request per region and submits it to a `ThreadPoolExecutor`; `max_workers: 32`
(`glmocr/config.yaml:109`).

Three prompts exist, and they are plain English strings (`glmocr/config.yaml:132-135`):

```yaml
task_prompt_mapping:
  text: "Text Recognition:"
  table: "Table Recognition:"
  formula: "Formula Recognition:"
```

The model's `chat_template.jinja` on Hugging Face contains role and image delimiters
(`<|user|>`, `<|begin_of_image|>`, …) and a tool-call block, but **no OCR-, layout- or
grounding-specific tokens** — nothing analogous to Unlimited-OCR's `<|det|>CATEGORY [bbox]`.

---

## 2. Q1 — Does it fit ~4.3 GB free?

### 2.1 Weights: 2.47 GiB, measured from the manifest

`huggingface.co/api/models/zai-org/GLM-OCR?blobs=true` reports a single shard:

```
model.safetensors    2,650,579,464 bytes  =  2.4685 GiB  =  2.65 GB
```

At bf16 (`config.json` → `text_config.dtype: "bfloat16"`) that is **1.325B stored tensor
elements**, not 0.9B.

Reconstructed from `config.json` (derived; the shard has no per-tensor index published):

| Block | Params |
| --- | ---: |
| Text decoder body — 16 layers, hidden 1536, GQA 16q/8kv × head_dim 128, SwiGLU 4608 | 490.8 M |
| `embed_tokens` (59,392 × 1536) | 91.2 M |
| `lm_head` (untied — `tie_word_embeddings: false`) | 91.2 M |
| CogViT — 24 layers, hidden 1024, intermediate 4096, patch 14 | ~403 M |
| Patch embed + spatial-merge connector (1024·4 → 1536) | ~24 M |
| MTP module (`num_nextn_predict_layers: 1`) + its head/embed copy | ~218 M |
| **Total** | **~1.32 B** |

That lands within 0.5% of the 1.325B implied by the file size, so the accounting is sound.
**The advertised 0.9B = decoder body (0.5B) + vision tower (0.4B), excluding embeddings, the
LM head and MTP.** Budget 2.47 GiB of resident weights.

### 2.2 What drives the activation peak

**KV cache dominates, and it is unusually expensive for a 0.9B model.** GQA is only 2:1
(16 query heads, 8 KV heads) at head_dim 128:

```
16 layers × 8 kv-heads × 128 dim × 2 (K+V) × 2 bytes = 65,536 B  =  64 KiB per token
```

| Context | KV cache |
| ---: | ---: |
| 4,096 | 256 MiB |
| 8,192 | 512 MiB |
| 16,384 | 1.00 GiB |
| **131,072** (`max_position_embeddings`) | **8.0 GiB** |

**A vLLM/SGLang launch that inherits the native 131 K context will not fit on this card.**
`--max-model-len` is the single most important flag.

**Input resolution.** `preprocessor_config.json` caps images at `longest_edge: 9,633,792` px,
which after patch 14 and spatial-merge 2 is **12,288 vision tokens** — the per-image ceiling.
The SDK's own client-side cap is *larger* and therefore never binds:
`max_pixels: 71,372,800` (`glmocr/config.yaml:129`, `glmocr/config.py:162`); the comment
`# 14 * 14 * 4 * 1280` does not equal that value, so the constant is stale. Actual downscaling
comes from the PDF rasteriser: PyMuPDF at 200 dpi with the long side capped at 3500 px
(`glmocr/utils/image_utils.py:262-281`) — the same rasteriser and roughly the same DPI this
project already standardised on.

**But the crop architecture makes this mostly moot.** A 200 dpi 1700×2200 page is 3.74 M px
≈ 4,770 tokens *if it were sent whole*. It is not. A typical text region (1500×250) is
~478 tokens. **Per-request activation is small; per-server concurrency is the risk.**
`max_workers: 32` will drive the server to its `--max-num-seqs` limit and multiply the KV
cache by that factor.

### 2.3 A budget that should fit — UNVERIFIED, not run

vLLM's `--gpu-memory-utilization` is a fraction of **total**, not free, VRAM. With 4.3 GB
free of 6144 MiB, the ceiling is ~0.70.

| Item | MiB |
| --- | ---: |
| Weights (bf16) | 2,528 |
| CUDA context + cuBLAS/cuDNN workspaces | ~350 |
| KV cache @ 8,192 ctx × 2 seqs | 1,024 |
| Vision activations, one crop | ~150 |
| **Total** | **~4,050** |

Suggested starting flags: `--max-model-len 8192 --max-num-seqs 2 --gpu-memory-utilization 0.70
--enforce-eager`, **omitting** the README's `--speculative-config '{"method":"mtp",...}'`
(the MTP draft layer and its own KV are ~220 M params plus buffers you cannot afford), and
running the layout model on CPU with `--layout-device cpu`. Set
`pipeline.max_workers: 2` to match `--max-num-seqs`.

This is corroborated indirectly: the landscape review's like-for-like consumer table
(§1.7) records **GLM-OCR at 4.67 GB** on an RTX 4070 Laptop 8 GB — a default-ish
configuration, i.e. ~600 MB above our free budget, closable by the flags above.

**UNVERIFIED.** What would settle it: `vllm serve zai-org/GLM-OCR` with those flags and
`nvidia-smi --query-gpu=memory.used` sampled during a page. That requires downloading 2.65 GB
of weights and starting a server — explicitly out of bounds for this pass.

**Measured on this machine today (read-only probe):** RTX 3060 Laptop, 6144 MiB total,
**5792 MiB free at rest**, 8 CPU cores, 15.7 GB RAM of which only **3.6 GB available** with
4.9 GB of swap already in use. The brief's "~4.3 GB typically free" is conservative for VRAM;
**host RAM is the tighter constraint right now.**

### 2.4 Host-RAM risk the repo creates on its own

`PipelineState` holds full-resolution PIL pages and cropped regions in bounded queues sized
`page_maxsize: 100` / `region_maxsize: 2000` (`glmocr/config.yaml:111-112`,
`glmocr/pipeline/_state.py:30-37`). A hundred 1700×2200 RGB pages is ~1.1 GB of RSS before a
single crop exists, and `skip` regions (figures) are retained as PIL images until the unit
completes (`glmocr/pipeline/_workers.py:355-362`). **On 3.6 GB of available RAM, lower both
queue bounds before running a long PDF.**

---

## 3. Q2 — Model loading cost

**The dangerous load is not in this repository.** The 2.47 GiB checkpoint is deserialised by
vLLM / SGLang / Ollama / mlx-vlm in a separate process. Nothing in `glmocr/` loads it.

What `glmocr` loads locally is PP-DocLayoutV3:

```python
# glmocr/layout/layout_detector.py:80-95
self._image_processor = PPDocLayoutV3ImageProcessor.from_pretrained(self.model_dir)
self._model = PPDocLayoutV3ForObjectDetection.from_pretrained(self.model_dir)
self._model.eval()
...
self._model = self._model.to(self._device)
```

**Yes, it deserialises on CPU and then moves to GPU** — `from_pretrained` at line 83 with no
`device_map`, no `dtype`, no explicit `low_cpu_mem_usage`, followed by a separate `.to()` at
line 95. A repo-wide grep finds **zero** occurrences of `device_map`, `torch_dtype`, `dtype=`
(on a model call), or any quantisation argument.

Materially, though, this is cheap: `PP-DocLayoutV3_safetensors/model.safetensors` is
**133,270,468 bytes (127 MiB)** and its `config.json` declares `"torch_dtype": "float32"`, so
~33 M fp32 params. Under `transformers>=5.3` the `from_pretrained` default dtype is `"auto"`
(a v5.0 breaking change), so it loads at fp32 as saved. CPU spike ≈ 133 MB. Not a hazard.

**Thread capping: none, anywhere.** Grepping the whole tree for `set_num_threads`,
`OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `num_threads`, `cpu_count` or `nproc` returns **zero
hits**.

**This matters, because the repo's own advice for a single-GPU box is to run the detector on
CPU.** From `README.md`:

```
# Run layout detection on CPU (keep GPU free for OCR model)
glmocr parse examples/source/code.png --layout-device cpu
```

An HGNetV2-L detector forward at full page resolution under `torch.no_grad()`
(`glmocr/layout/layout_detector.py:246, 327`) with default intra-op parallelism will use all
8 cores, inside a process that is simultaneously running a 32-thread HTTP pool. **That is
structurally the same failure mode as today's incident: a correctly GPU-pinned design whose
CPU-side stage saturates the box.** The repo offers no knob; cap it externally:

```bash
OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 glmocr parse ... --layout-device cpu
```

`batch_size: 1` in the shipped YAML (`glmocr/config.yaml:192`) limits it to one page at a time,
which helps. Note the Pydantic default is `8` (`glmocr/config.py:205`) — if you build a
`LayoutConfig` programmatically rather than from the YAML, you get 8× the peak.

---

## 4. Q3 — Silent CPU fallback? **Yes, and at DEBUG level**

```python
# glmocr/layout/layout_detector.py:89-94
if self._config_device is not None:
    self._device = self._config_device
elif torch.cuda.is_available() and self.cuda_visible_devices:
    self._device = f"cuda:{self.cuda_visible_devices}"
else:
    self._device = "cpu"
```

`device` defaults to `None` (`glmocr/config.py:214`) and is commented out in the shipped YAML
(`glmocr/config.yaml:202`). So on a machine where CUDA is unavailable — driver hiccup, wrong
container, `CUDA_VISIBLE_DEVICES=""`, a torch build without CUDA — **the layout model silently
runs on CPU.** The only announcement is `logger.debug` (line 156), and the default log level
is `INFO` (`glmocr/config.yaml:16`). Nothing is printed.

This is not incidental: it is **tested as intended behaviour** —
`glmocr/tests/test_unit.py:175-194`, `test_detector_device_selection_auto_fallback_cpu`,
docstring *"When config.device=None and CUDA unavailable, auto-selects CPU."*

**There is no OOM fallback path at all.** A CUDA OOM inside `layout_detector.process()`
propagates to `_flush_layout_batch`, which catches **`Exception`** and degrades the page to
zero regions with a `logger.warning` (`glmocr/pipeline/_workers.py:273-281`):

```python
except Exception as e:
    logger.warning("Layout detection failed for pages %s, skipping batch: %s", ...)
    for page_idx in batch_page_indices:
        state.layout_results_dict[page_idx] = []
    return
```

**A page that OOMs comes back empty and the run reports success.** The same shape appears in
recognition: a failed HTTP call sets `region["content"] = None` and warns
(`glmocr/pipeline/_workers.py:415-428`), and `ResultFormatter.process` then drops empty
non-image regions entirely (`glmocr/postprocess/result_formatter.py:191-199`). **Missing
content is indistinguishable from a blank region in the output JSON.**

For `ocr_handler`, whose objective **O3** is *"Say honestly what was and was not recovered"*,
this is a real integration hazard. It is mitigable — `Pipeline.process` re-raises collected
exceptions at the end (`glmocr/pipeline/pipeline.py:193`, `state.raise_if_exceptions()`), and
the OCR-server preflight *does* fail loudly (`glmocr/ocr_client.py:254-256` raises
`TimeoutError` after `connect_timeout`) — but per-page silent loss requires our own
region-count assertion on top.

**Disqualifying?** For the layout model, mitigable in one line (`layout_device="cuda"` forces
it, and an invalid value raises via the Pydantic validator at `glmocr/config.py:223-248`).
For the empty-page-on-error path, it needs a wrapper. Neither is fatal, but the brief's bar
("silent fallback is disqualifying") **is met by the device selection as shipped**.

---

## 5. Q4 — The PP-DocLayoutV3 dependency

**Required, not optional — but it does not pull in PaddleOCR or PaddlePaddle.**

**Required.** `Pipeline.__init__` builds it whenever one is not injected
(`glmocr/pipeline/pipeline.py:87-97`), and raises `ImportError` if the extra is missing
(`glmocr/layout/__init__.py:24-38`). The module docstring says *"Stages (all always enabled)"*
(`glmocr/pipeline/pipeline.py:6`). The only bypass is `_process_passthrough`
(`glmocr/pipeline/pipeline.py:289-307`), reachable **only when the request contains no image
sources** — it is a raw-message forwarder, not a layout-free page mode. Passing a custom
`layout_detector` is a documented extension point, so a null detector returning one
full-page region is trivially writable, but nothing ships.

**No Paddle.** The `selfhosted` extra (`pyproject.toml:53-62`) is:

```
opencv-python-headless>=4.10.0, torch>=2.10.0, torchvision>=0.25.0,
transformers>=5.3.0, sentencepiece>=0.2.0, accelerate>=1.13.0, pypdfium2>=5.6.0
```

Zero `paddlepaddle`, zero `paddleocr`. The detector is imported straight from `transformers`
(`glmocr/layout/layout_detector.py:11-14`) as `PPDocLayoutV3ForObjectDetection` /
`PPDocLayoutV3ImageProcessor` — upstreamed classes. The HF repo
`PaddlePaddle/PP-DocLayoutV3_safetensors` contains only `config.json`, `inference.yml`,
`preprocessor_config.json` and a 127 MiB `model.safetensors`: **no `.pdmodel`, no
`.pdiparams`.** It is a pure transformers port.

**Licence story:** clean and unchanged. Apache-2.0 detector alongside MIT weights; both permit
commercial use with attribution. The README states it plainly.

**Install footprint:** torch 2.10 + torchvision + transformers 5.3 + accelerate + opencv +
sentencepiece + pypdfium2 — several GB of wheels and CUDA libs. `ocr_handler`'s own venv
currently has **none** of this (`pyproject.toml`: typer, pillow, numpy, scipy, pymupdf). Note
`transformers>=5.3.0` and `torch>=2.10.0` are aggressive floors; the system python here has
transformers 4.52.3 / torch 2.7.0, so this is a fresh, heavy environment, not an upgrade to an
existing one. **UNVERIFIED:** whether transformers 5.3 co-installs cleanly with UniMERNet-B,
which historically pins the 4.x line — that is the concrete integration risk to test first,
and it is testable with `uv pip install --dry-run` at zero GPU cost.

One soft dependency worth knowing: `wordfreq` is imported opportunistically for hyphen-merge
validation and is **not declared anywhere** (`glmocr/postprocess/result_formatter.py:20-23`).
Without it a regex heuristic is used, so English de-hyphenation quality differs silently
between machines.

---

## 6. Q5 — Handwriting

**The repository substantiates nothing.** `grep -ril "handwrit\|手写"` over the whole tree
returns exactly three files:

| File | Hits | What it is |
| --- | ---: | --- |
| `skills/glmocr-handwriting/SKILL.md` | 22 | marketing copy for a **cloud-API** skill |
| `skills/glmocr/SKILL.md` | 3 | one bullet listing handwriting as a use case |
| `apps/frontend/src/routes/_ocr/testData.ts` | 2 | demo fixture strings in the web UI |

Zero in `glmocr/`. No handwriting prompt, no handwriting preprocessing, no benchmark script,
no eval harness of any kind (`find` for `*eval*` / `*bench*` / `*omnidoc*`: no matches).

**The "handwriting skill" is the same file as the others.** The four skill scripts:

```
skills/glmocr/scripts/glm_ocr_cli.py             62593a0d…  429 lines
skills/glmocr-handwriting/scripts/glm_ocr_cli.py 24e5140f…  405 lines
skills/glmocr-formula/scripts/glm_ocr_cli.py     24e5140f…  405 lines   ← identical
skills/glmocr-table/scripts/glm_ocr_cli.py       24e5140f…  405 lines   ← identical
```

Handwriting, formula and table are **byte-identical**. They hard-code
`OFFICIAL_API_URL = "https://open.bigmodel.cn/api/paas/v4/layout_parsing"`
(`skills/glmocr-handwriting/scripts/glm_ocr_cli.py:48`) with no local path and no
task-specific prompt. `SKILL.md` even forbids local alternatives: *"NEVER parse handwriting
yourself… NO fallback methods."* **The handwriting skill is a cloud router with a different
front-matter description.** For a project whose blacklist bars cloud OCR on the shipped path,
it is unusable as-is and tells us nothing about the weights.

**The only handwritten example in the repo is Chinese prose.**
`examples/result/handwritten/handwritten.json` is four `text` regions of Chinese
essay prose. No handwritten mathematics, no English handwriting, no annotated-slide case,
nothing resembling our fixture.

### 6.1 Where the 87.0 actually comes from

The arXiv HTML (`2603.10910`) places **Handwritten Text 87.0** in **Table 5, "In-House
Benchmarks"** — an unreleased vendor test set, alongside PaddleOCR-VL-1.5's 87.4,
DeepSeek-OCR2 73.8, dots.ocr 71.7, MinerU2.5 54.2. The paper's own framing: *"While
PaddleOCR-VL-1.5 holds a marginal lead in Handwritten Text (87.4 vs. GLM-OCR's 87.0),
GLM-OCR remains highly effective."*

**Both numbers in that comparison are ZAI's private measurement.** The landscape review
treats the 87.4 as usefully independent — a competitor's table is better evidence than a
self-report, which is fair — but it is n=1 source on an unreleased set, and it is **not**
reproducible by anyone.

The **public** handwriting number is Table 3's **Handwritten-KIE 86.1**. And:

> **Issue #226 — "Handwritten-KIE评测集复现时得分仅64+，和论文中差异较大"**
> ("reproducing the Handwritten-KIE eval set yields only 64+, a large gap from the paper —
> are there optimisation strategies?"). Opened 2026-06-19. **Zero comments. Still open.**

A ~22-point unanswered reproduction failure on the model's only public handwriting benchmark.
That is the same shape of evidence — an open, unrebutted third-party reproduction failure —
that the landscape review used to discount Unlimited-OCR's headline (§1.2), and it should
carry the same weight here.

**Also note what `scope.md` actually needs.** Handwriting recognition *for prose* is on the
blacklist; only **mathematics** must survive as text, and that is Stage 2b's job
(UniMERNet-B on cropped expressions). GLM-OCR's relevant number is therefore UniMER-Test
**HWE 95.10 CDM** (MinerU2.5-Pro's independent table, per the landscape review §2b) — above
PaddleOCR-VL's 94.45, below MinerU2.5-Pro's 95.38, and **below UniMERNet-B's own 0.941 CDM
which we already have running locally at 681 MiB.** The handwriting headline that made
GLM-OCR interesting is largely aimed at a job this project has already assigned elsewhere.

---

## 7. Q6 — Output format

**Markdown + a structured per-page JSON. Bounding boxes exist and are normalised 0–1000.
None of them come from the VLM.**

### 7.1 The JSON

`json_result` is `List[page][region]`, each region:

```json
{ "index": 4, "label": "formula",
  "content": "$$\n\\frac {q l}{2 t _ {1}} \\leqslant f _ {1}\n$$",
  "bbox_2d": [230, 248, 285, 290] }
```

Verified against `examples/result/page/page.json`, `paper.json`, `GLM-4.5V.json` (41 pages).
`label` is one of **four** mapped classes — `text` / `table` / `formula` / `image` — collapsed
from 25 native PP-DocLayout classes by `_map_label`
(`glmocr/postprocess/result_formatter.py:365-375`). The native class survives as
`native_label`, and `polygon` is carried in the raw snapshot
(`glmocr/pipeline/pipeline.py:265-287`) when `use_polygon: true`
(off by default, `glmocr/config.yaml:211`).

### 7.2 Coordinate space

**Integers normalised to 0–1000, relative to the rendered page image** (not PDF points, not
pixels):

```python
# glmocr/layout/layout_detector.py:390-393
x1_norm = int(float(x1) / image_width  * 1000)
y1_norm = int(float(y1) / image_height * 1000)
```

Round-tripped back to pixels in `crop_image_region` (`glmocr/utils/image_utils.py:200-205`).
The MaaS path returns absolute pixels plus markdown refs of the form
`![](page=0,bbox=[431, 1762, 1061, 2189])` and the SDK normalises them to the same 0–1000
space (`glmocr/api.py:363-412`), so **both backends agree**. The page image is PyMuPDF at
`pdf_dpi: 200` with the long side capped at 3500 px, so mapping 0–1000 back to PDF
coordinates needs the render scale, which `_render_page_to_pil` computes but does not return
to the caller (`glmocr/utils/image_utils.py:262-281`). **Integer 0–1000 on a 2200 px page is
2.2 px of quantisation** — fine for figure crops, marginal for tight equation boxes.

### 7.3 What each element type gives us

| `ocr_handler` needs | GLM-OCR gives | Where |
| --- | --- | --- |
| Text | Markdown, `#`/`##` from `doc_title`/`paragraph_title` | `result_formatter.py:307-315` |
| LaTeX equations | `$$\n…\n$$` block, inline `$…$` normalised | `result_formatter.py:318-331` |
| Figure regions + coords | `label:"image"`, `content:""`, `bbox_2d`, **and the crop saved to `imgs/cropped_page{N}_idx{M}.jpg`** with a `![](imgs/…)` ref | `_workers.py:355-362`, `result_formatter.py:233-249` |
| Tables | **HTML `<table>…</table>`, not Markdown tables** | `examples/result/table/table.json` |

The figure handling is genuinely good and is the best single fit with our contract: `chart`
and `image` are mapped to `task_type: skip` (`glmocr/config.yaml:271-273`), which keeps the
region and its pixels without spending a VLM call on it.

**Two caveats.**

*Tables are HTML.* `skills/glmocr/references/output_schema.md` claims *"Tables are formatted
as Markdown tables"*; the actual local output is HTML. The doc is wrong about its own tool.

*Headers, footers and page numbers are deleted by default.* `label_task_mapping.abandon`
(`glmocr/config.yaml:274-282`) lists `header, footer, number, footnote, aside_text, reference,
footer_image, header_image`, and `layout_detector.py:387-388` drops them before OCR:

```python
if task_type is None or task_type == "abandon":
    continue
```

For lecture slides this deletes the slide footer and page number — which our fixture page's
ground truth (`"DT signals and systems Page 5"`) contains. Move `footer`/`number` into the
`text` bucket if you want them. **This is also the key to the olmOCR conflict — see §9.**

---

## 8. Q7 — Licence

**Split, and the split is stated correctly by upstream.**

| Artifact | Licence | Evidence |
| --- | --- | --- |
| Repository **code** | **Apache-2.0** | `LICENSE` (full Apache text, *"Copyright 2026 Zhipu AI"*), `pyproject.toml:14`, GitHub API `license.spdx_id: "Apache-2.0"` |
| **Weights** | **MIT** | HF card front-matter `license: mit`; README: *"The GLM-OCR model is released under the MIT License."* |
| PP-DocLayoutV3 | Apache-2.0 | HF card; required by the pipeline |

**No acceptable-use rider, and not gated.** The HF API returns `gated: false` with **no**
`extra_gated_prompt`, `extra_gated_fields`, `license_name` or `license_link`. Unlike dots.ocr
there is no separate use-restriction agreement. Nothing in the repo, the card, or the paper
adds a field-of-use or non-commercial clause.

**One precision worth recording:** the weights repo contains **no `LICENSE` file** — the
manifest is `.eval_results/*`, `.gitattributes`, `README.md`, `chat_template.jinja`,
`config.json`, `generation_config.json`, `model.safetensors`, `preprocessor_config.json`,
`tokenizer.json`, `tokenizer_config.json`. The MIT claim rests on the card's `license:` tag
plus the GitHub README sentence. That is HF's standard mechanism and is normally sufficient,
but it is an assertion in metadata rather than a distributed licence text.

**Net: the landscape review's "MIT on the weights, the most permissive in the field" is
correct.** The correction is that the **code** is Apache-2.0, not MIT — which changes nothing
practical, since we would be consuming the weights and probably writing our own thin client.

---

## 9. The olmOCR-Bench conflict, resolved

The landscape review flags 75.2 (model card, *"via the ZAI API, excluding headers/footers"*)
against 68.4 on a third-party leaderboard. **The repo, plus the model's own eval artifact,
settles what each number is — and the received explanation is wrong.**

The weights repo ships `.eval_results/olmocrbench.yaml`. Full contents:

| Category | ZAI (`.eval_results`) | Nanonets IDP leaderboard | Δ |
| --- | ---: | ---: | ---: |
| ArXiv Math | 80.7 | 67.3 | −13.4 |
| **Old Scans Math** | 68.3 | 75.5 | **+7.2** |
| Tables | 77.6 | 59.0 | −18.6 |
| **Old Scans** | **37.6** | **41.3** | **+3.7** |
| **Multi Column** | 76.7 | 80.3 | **+3.6** |
| **Long Tiny Text** | **86.9** | **35.7** | **−51.2** |
| Headers & Footers | 95.8 | 89.2 | −6.6 |
| Baseline | 98.8 | (≈99, implied) | — |
| **Overall** | **75.2** *(7 cats, excl. H&F)* | **68.4** *(8 cats)* | |

Both means check out arithmetically: ZAI's seven excluding H&F is 526.6/7 = **75.23**;
Nanonets' eight including H&F and Baseline is 547.3/8 = **68.41**.

**Finding 1 — the "excluding headers/footers" caveat is conservative, not flattering.**
olmOCR-Bench's `headers_footers` category is an *absence* test: it rewards a parser for
**omitting** running headers, footers and page numbers (olmOCR-2, arXiv 2510.19817;
the tests were built by masking header/footer regions and asserting the text does **not**
appear). GLM-OCR scores **95.8** there — precisely because the repo's default config
*abandons* those classes (§7.3). **Including that category would raise the score to 77.8,
not lower it.** The submitter dropped their best category. The landscape review's implication
that the exclusion inflates 75.2 is backwards.

**Finding 2 — the 9.4-point gap is therefore not a category-set artefact.** On identical
category sets, ZAI measures 77.8 and Nanonets measures 68.4.

**Finding 3 — the divergence is concentrated exactly where a two-stage pipeline is fragile.**
Long Tiny Text collapses from 86.9 to 35.7 and Tables from 77.6 to 59.0, while Nanonets is
*better* on Old Scans, Old Scans Math and Multi-Column. That pattern is the signature of a
**different layout configuration**, not a different model: small-text regions being missed at
`threshold: 0.3`, merged by `layout_nms`, or clipped by `layout_unclip_ratio: [1.0, 1.0]` —
all knobs the shipped `config.yaml` exposes (lines 183-246) and which the ZAI cloud is free to
tune differently. It is corroborated by three open, unanswered issues reporting that
**cropped-region OCR is worse than full-page OCR**:

- **#241** (2026-08-28): decimal commas vanish in isolated table crops — `10,72 → 1072`,
  `2,300 → 2300`, *"for every numeric cell"* — but are correct in full-page OCR.
- **#240**: table footer/summary rows missing from output.
- **#228**: *"用红框crop部分图像做推理，结果有点差"* — cropped-region inference gives poor results.

**What the repo supports, stated plainly:** *neither published number is a measurement of the
open weights under a documented local configuration.* The `.eval_results` artifact says
verbatim **"Using ZAI API"** — it measures Zhipu's cloud pipeline, whose layout settings are
not the ones in this repository. The repo contains no evaluation harness at all with which to
reproduce either. **Treat 75.2 as a cloud-service number and 68.4 as the more honest proxy for
what a self-hosted run produces**, and note that the categories most relevant to us —
Old Scans 37.6/41.3, Old Scans Math 68.3/75.5 — are the ones where the two agree best and
where GLM-OCR is **level with PaddleOCR-VL (37.8), not ahead of it.**

---

## 10. Repository health

| | |
| --- | --- |
| Stars / forks | 7,402 / 669 |
| Created | 2026-02-02 |
| **Last push** | **2026-04-21** — 4.5 months stale |
| Open issues | 55 |
| Archived | no |
| SDK version | 0.1.5, *"Development Status :: 3 - Alpha"* (`pyproject.toml:17`) |

Open and unanswered, all directly relevant:

- **#226** — Handwritten-KIE reproduces at 64+ vs 86.1 (§6.1). 0 comments since 2026-06-19.
- **#241 / #240 / #228** — crop-vs-full-page degradation (§9).
- **#220** — *"GLM-OCR repeats OCR output unless a stop sequence is configured"*: a phrase
  repeated 75+ times, **417 s for one image** on Ollama, workaround `"stop": ["```"]` which
  *"still resulted in repetition for some images."* Same failure class as Unlimited-OCR #55.
  Note the shipped config already sets `repetition_penalty: 1.1` and greedy decoding
  (`temperature: 0.0, top_k: 1`) — `glmocr/config.yaml:118-121` — and it still loops.
- **#231 / #227 / #232 / #233** — vLLM segfault on WSL2, aarch64, Ascend.

### Corrections to the landscape review

Recorded for the record; that file is not edited.

| Landscape claim | This teardown |
| --- | --- |
| §2a: GLM-OCR **MIT** (HF card) | Correct for **weights**; the **code** is Apache-2.0 (`LICENSE`, GitHub SPDX). |
| §8.1: PaddleOCR-VL is a two-model pipeline, *"against a project whose stack is deliberately minimal"* | **GLM-OCR is too** — PP-DocLayoutV3 is unconditional (`pipeline.py:87-97`). The argument does not distinguish them. |
| olmOCR 75.2 vs 68.4, exclusion of H&F implied as flattering | **Backwards.** H&F is an *absence* test GLM-OCR wins at 95.8; including it gives 77.8. The real gap is a layout-configuration difference (§9). |
| §1.6: GLM-OCR's Table 5 as an independent handwriting comparison | It is **ZAI's own in-house, unreleased** benchmark. Both 87.0 and 87.4 are unreproducible; the public number (Handwritten-KIE 86.1) has an open reproduction failure at 64+. |
| §2a table: GLM-OCR ParseBench Text Formatting "—" | The model card gives **2.3**. |
| Brief's premise: "0.9B at bf16 ≈ 1.8 GB of weights" | **2.47 GiB** measured from the manifest; 0.9B excludes embeddings, LM head and MTP. |

**Standing and confirmed by this teardown:** GLM-OCR is 0.9B-class and small; MIT weights with
no rider; it renders PDFs with **PyMuPDF at 200 dpi** (the same rasteriser this project already
chose, `image_utils.py:262-281`); and it emits figure regions with coordinates and saved crops,
which is a genuine fit with our contract.

---

## 11. The strongest argument against my own answer

**It is that GLM-OCR is the only candidate on the slate with a documented, zero-Python-dependency
local serving path on hardware we already run — and my case against it leans on a metric I
cannot show applies to the local pipeline.**

Four points, in descending strength.

1. **`ollama pull glm-ocr:latest` needs nothing from this repository.** A single 2.47 GiB
   checkpoint, one process, an OpenAI-compatible endpoint, no torch 2.10, no transformers 5.3,
   no PP-DocLayoutV3, no new venv. Against that, **PaddleOCR-VL's entire 6 GB story is one
   user's comment in a GitHub discussion** (§7 of the landscape review admits this), its
   flash-attn-2 path is unmeasured here, and it too needs a layout model. If the deciding
   question is *"what can I actually run on this laptop this week,"* GLM-OCR is ahead and I am
   ranking it below on benchmarks the landscape review itself argues are saturated.

2. **The ParseBench Text Formatting 2.3 may not measure the local pipeline at all.** In the
   self-hosted path, headings, formula delimiters, bullets and list markers are produced
   **deterministically in Python** from PP-DocLayoutV3's class labels —
   `# ` from `doc_title`, `## ` from `paragraph_title`, `$$…$$` from `display_formula`
   (`result_formatter.py:307-331`). The VLM contributes plain text per crop. Whatever
   ParseBench scored — almost certainly the ZAI cloud API's markdown, as with every other
   published GLM-OCR number — **it is not obviously the same artefact the SDK produces.**
   I am using a number from one pipeline to condemn another. **UNVERIFIED**, and it is the
   single cheapest thing to settle: run both engines on our fixture page and diff the heading
   and equation structure.

3. **On the two categories that actually match our corpus, GLM-OCR is not behind.** Old Scans
   37.6–41.3 vs PaddleOCR-VL's 37.8; Old Scans Math 68.3–75.5. The landscape review's own
   §5 decision procedure says *choose by handwriting sub-score, semantic formatting and Old
   Scans* — and on Old Scans these two are a coin flip.

4. **My §9 resolution cuts both ways.** I argued the local pipeline is worse than the cloud
   because the layout stage is misconfigured. But that is a **configuration** claim, and every
   knob is in a YAML file we control: `threshold`, `threshold_by_class`, `layout_nms`,
   `layout_unclip_ratio`, `use_polygon`, the `abandon` list. If the 9.4-point gap really is
   layout tuning, it is recoverable by us, not intrinsic to the weights.

**What does not move, whatever those tests say:** issue #226 (an unrebutted 22-point
reproduction failure on the only public handwriting benchmark), the 4.5-month-stale repo with
55 open issues and unanswered correctness reports, and the fact that the shipped default is
a cloud API that `scope.md` permanently blacklists on the shipped path.

### The recommendation

**Keep PaddleOCR-VL-1.6 as the recommended page engine. Add GLM-OCR to the head-to-head slate
as the strongest challenger, ahead of Unlimited-OCR.** It has earned a run on the fixture page;
it has not earned the default.

If it is run, run it in this order, and stop at the first failure:

1. `uv pip install --dry-run "glmocr[selfhosted]"` alongside the existing pins. **Free.**
   If transformers 5.3 / torch 2.10 cannot coexist with UniMERNet-B, the question is settled
   without a single byte of weights.
2. `ollama pull glm-ocr:latest` and check the quantisation it ships. The landscape review's
   §1.7 GGUF ladder — 0.78 % CER at Q5_K_M, **15.64 %** at Q4_K_M — is the cautionary tale.
   Refuse anything below Q5_K_M.
3. Single page, `--layout-device cpu`, `OMP_NUM_THREADS=2`, `max_workers: 2`, and
   `nvidia-smi` sampled throughout. Move `footer`/`number` out of `abandon` first, or the
   ground-truth footer will read as a miss.
4. The un-annotated-twin control, unchanged. It has now reproduced on two model families.
5. A region-count assertion, because §4 shows an OOM'd or failed page returns **empty and
   successful**.

---

## Sources

**Read locally (no execution):** `~/tmp/ocr_repos/GLM-OCR` @ `cef4d0e` — all files cited by
`file:line` above.

**Small text artifacts fetched (no weights):**
`huggingface.co/zai-org/GLM-OCR` — model card, `config.json`, `preprocessor_config.json`,
`chat_template.jinja`, `.eval_results/olmocrbench.yaml`, and the `?blobs=true` file manifest ·
`huggingface.co/PaddlePaddle/PP-DocLayoutV3_safetensors` — `config.json` + manifest ·
`arxiv.org/abs/2603.10910` and its HTML rendering (Tables 3 and 5) ·
`api.github.com/repos/zai-org/GLM-OCR` — repo metadata and issues #220, #226, #241 ·
`benchmarking.nanonets.com/benchmarks/olmocr` — the 68.4 row and its per-category breakdown ·
olmOCR-2, arXiv 2510.19817 — `headers_footers` absence-test semantics.

**Measured on this machine, read-only, 2026-09-05:** `nvidia-smi` (RTX 3060 Laptop,
6144 MiB total / 5792 MiB free), `nproc` (8), `free -m` (15.7 GB total / 3.6 GB available /
4.9 GB swap used).

**Not done, by instruction:** no weights downloaded, no inference, no GPU work, no installs,
no builds, no test suites. Everything marked **UNVERIFIED** names what would settle it.

---

**See:** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) ·
[`INDEX.md`](INDEX.md) · [`../scope.md`](../scope.md)
