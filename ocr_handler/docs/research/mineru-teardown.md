# MinerU — static teardown, 2026-09-05

Static analysis of `opendatalab/MinerU` as cloned at `~/tmp/ocr_repos/MinerU`.
**Nothing was executed.** No weights downloaded, no inference, no GPU, no `pip install`.
Every behavioural claim below is cited to `file:line` in that clone; everything that would
need a run to settle is marked **UNVERIFIED** with the experiment that would settle it.

**Clone identity.** Commit `4fe4bde114a23ee5dd637eae99b767f4669bf58c`, authored 2026-08-14,
`mineru/version.py` → `__version__ = "3.4.5"`. Shallow clone, depth 1 (`git rev-list --count HEAD` = 1),
so LICENSE history is not recoverable locally — the licence timeline below comes from the
README's own release notes plus web research.

> Read with [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md), which nominated this
> repo for teardown on two grounds: it is the only project in the landscape publishing a
> minimum-VRAM table, and it is the cautionary tale on leaderboard rank
> (93–95.75 OmniDocBench, 54.2 handwriting). Both grounds hold up. The rest of this document
> is what the source says about them.

---

## Verdict up front

**One part of MinerU is worth adopting on a 6 GB card, and it is not a model.**

| Question | Answer |
| --- | --- |
| Is the 4 GB / 8 GB floor enforced? | **No. Advisory only.** No guard, no gate, no OOM handler anywhere in the repo |
| Can the pipeline backend run in 6 GB? | **Almost certainly yes** — `>= 6` is an explicit rung in its own batch ladder. But it scores **86.47**, not 95 |
| Does it fail loudly without a GPU? | **No. It degrades silently, on the default backend.** Disqualifying as an adopted runtime |
| Does it deserialize on CPU first? | **Yes, every model.** And it caps `OMP_NUM_THREADS` only on the VLM paths — *not* on the pipeline path |
| Is the handwriting claim backed? | **No.** The claim traces to a 2025 *layout-detection* patch. Independent benchmarks put MinerU2.5 second-to-last of 18 |
| Licence — code | **MinerU Open Source License** = Apache-2.0 + 4 additional terms. Not AGPL. Usable here |
| Licence — weights | VLM weights Apache-2.0; **the pipeline weights bundle is still declared AGPL-3.0**. See §6.3 |

**Adopt: `mineru/model/mfr/utils.py` — the LaTeX repair suite and the area-sorted dynamic
batching — as vendored source.** Both are directly applicable to the UniMERNet-B path this
project already runs, both are pure Python with no model dependency, and the code licence
permits vendoring with attribution. Being *code*, this is untouched by the weights problem.

**Do not adopt: MinerU as a runtime, or any MinerU model.** The pipeline backend's OCR is
PP-OCR-derived and its maintainer calls handwriting *"已知问题"* (a known issue) in writing.
The VLM backend needs 8 GB and scores 31.33 overall on in-the-wild handwriting.

---

## 1. The VRAM floors — where they come from, and what enforces them

### 1.1 What is published

The table is in three places, identical: `README.md:218-284`, `docs/en/quick_start/index.md:31-97`,
`docs/zh/quick_start/index.md` (Chinese mirror). Transcribed:

| | pipeline | hybrid-engine | vlm-engine | hybrid-http-client | vlm-http-client |
| --- | --- | --- | --- | --- | --- |
| **OmniDocBench v1.6 overall** | **86.47** | 95.39 high / 95.26 medium | 95.30 | 95.39 / 95.26 | 95.30 |
| **Pure CPU support** | **✅** | ❌ | ❌ | ✅ | ✅ |
| **GPU acceleration** | Volta+ or Apple Silicon | Volta+ | Volta+ | Volta+ | not required |
| **Min VRAM** | **4 GB** | 8 GB | 8 GB | 2 GB | 2 GB |
| **RAM** | min 16 GB, rec. 32 GB | " | " | min 16 GB | min 16 GB |
| **Disk** | min 20 GB, SSD rec. | " | " | min 2 GB | min 2 GB |

`README.md:241-246` (accuracy row) · `README.md:253` (CPU row) · `README.md:260` (GPU arch row) ·
`README.md:264-267` (VRAM row) · `README.md:271-272` (RAM) · `README.md:276-277` (disk).

**The single most important line in that table is the one the landscape review did not have:
the 4 GB configuration scores 86.47, not 95.** The 93–95.75 figures that put MinerU 2nd on
OmniDocBench belong to the VLM and hybrid backends, which are the **8 GB, GPU-mandatory,
no-CPU-fallback** rows. There is no configuration that is both cheap and top-of-leaderboard.
The footnote confirms the source: *"Accuracy metrics are the End-to-End Evaluation Overall
scores from OmniDocBench (v1.6), based on the latest version of `MinerU`"* (`README.md:280`).

*Table defect worth noting:* the Min VRAM row emits 4 `<td>`s (colspans 1+2+1) for a 5-column
table, so the `2GB` cell renders under `hybrid-http-client` and `vlm-http-client` is blank.
The RAM and disk rows below it use colspan 2 in that position. Read `2 GB` as covering both
http-client columns.

### 1.2 What enforces them: nothing

There is exactly one VRAM-reading function in the repo, `get_vram()` at
`mineru/utils/model_utils.py:217-253`. It:

- honours an override, `MINERU_VIRTUAL_VRAM_SIZE` (`model_utils.py:218-231`) — an integer in GB,
  no upper bound, warns and falls through only if unparseable or ≤ 0;
- otherwise returns `round(torch.cuda.get_device_properties(device).total_memory / 1024**3)`
  for CUDA, with parallel branches for npu/gcu/musa/mlu/sdaa (`model_utils.py:235-251`);
- **initialises `total_memory = 1` (`model_utils.py:234`) and returns that if no accelerator
  matched.** CPU is 1 GB as far as the rest of the codebase is concerned.

Its return value is used for exactly three things, all of them batch sizing:

| Consumer | File:line | Ladder |
| --- | --- | --- |
| pipeline batch ratio | `mineru/backend/pipeline/pipeline_analyze.py:353-365` | ≥32→16, ≥16→8, ≥8→4, **≥6→2**, else→1 |
| hybrid batch ratio | `mineru/backend/hybrid/hybrid_analyze.py:865-876` | ≥32→16, ≥16→8, **≥12→4**, else→1 |
| vLLM memory fraction | `mineru/backend/vlm/utils.py:83-92` | 0.5, or **0.7 if vllm ≥ 0.11.0 and gpu_memory ≤ 8** |
| transformers batch size | `mineru/backend/vlm/utils.py:96-110` | ≥16→8, ≥8→4, else→1 |

**Four findings follow, and they are the most valuable thing in this repo for us.**

**(a) The 4 GB and 8 GB numbers appear in no config, no constant, and no guard.** They are
documentation only. `grep -rniE "vram|total_memory|get_device_properties"` over `*.py`
returns the four consumers above and nothing else. There is no `if vram < 4: raise`, no
minimum check at model-init time, and — verified by grep for
`OutOfMemory|OOM|except.*Memory` across the whole tree — **no OOM handling of any kind,
anywhere.** A 3 GB card will attempt the pipeline, allocate, and die with a raw
`torch.cuda.OutOfMemoryError`.

**(b) 6 GB is a first-class rung in the pipeline ladder, and only in the pipeline ladder.**
`pipeline_analyze.py:360-361` is `elif gpu_memory >= 6: batch_ratio = 2`. The hybrid ladder
(`hybrid_analyze.py:870-873`) skips from 12 straight to 1. Upstream tuned the pipeline for
6 GB cards specifically and did not tune hybrid for them. That is corroborating structural
evidence that the pipeline backend is genuinely intended to run on hardware like ours, and
that hybrid is not.

**(c) `clean_vram(device, vram_threshold=8)` is the tell for what ≤ 8 GB costs.**
`model_utils.py:208-214`: if `get_vram(device) <= 8`, run `torch.cuda.empty_cache()` +
`gc.collect()`. It is called between every pipeline stage — after layout
(`batch_analyze.py:432`), after formula recognition (`batch_analyze.py:460`), after OCR
(`batch_analyze.py:798`). **On a 6 GB card the pipeline pays a full GC and cache-flush three
times per batch.** That is a real, unquantified latency cost that the 4 GB figure does not
disclose. Its magnitude is **UNVERIFIED** — settled by timing a run with
`MINERU_VIRTUAL_VRAM_SIZE=6` against `MINERU_VIRTUAL_VRAM_SIZE=16` on the same GPU, which
changes only this threshold and the batch ratio.

**(d) Nothing is ever offloaded, so 4 GB must cover every pipeline model simultaneously.**
`AtomModelSingleton._models` (`mineru/backend/pipeline/model_init.py:148-187`) is a
process-lifetime dict that is never cleared; grep for
`\.cpu\(\)|offload|_models\.clear|\.to\("cpu"\)` finds only output-tensor transfers and one
`self._models.clear()` in the *VLM* singleton (`vlm_analyze.py:257`). So with formulas and
tables enabled, the resident set is layout + UniMERNet + OCR-det + OCR-rec + two table ONNX
sessions + two classifier models, all at once, for the whole process.

**(e) `MINERU_VIRTUAL_VRAM_SIZE` is an undocumented escape hatch in 3.4.5.**
`grep -rn MINERU_VIRTUAL_VRAM_SIZE .` returns three hits, all inside `model_utils.py`. It is
**absent from `docs/en/usage/cli_tools.md`**, which documents 21 other `MINERU_*` variables
(`cli_tools.md:109-201`). Older MinerU documented it. Anyone tuning MinerU on a small card
in 3.4.5 has to read the source to find the one knob that matters.

### 1.3 Verdict on Q1

The published floors are **honest but soft**. They are a hardware recommendation with real
engineering behind them — the batch ladders and the ≤ 8 GB GC threshold prove upstream
actually thought about small cards — but they are enforced by nothing. Treat "4 GB" as
"upstream ran it in 4 GB with `batch_ratio=1` and it did not OOM on their documents," not as
a contract. **This is still more than any other project in the landscape publishes, and the
`>= 6` rung is worth more to us than the 4 GB headline.**

---

## 2. Pipeline vs VLM — what the pipeline backend actually is

### 2.1 Composition

From `mineru/backend/pipeline/model_init.py` (`MineruPipelineModel.__init__`, lines 231-291)
and the model paths in `mineru/utils/enum_class.py:96-107`:

| Stage | Model | Path in `opendatalab/PDF-Extract-Kit-1.0` | Runtime |
| --- | --- | --- | --- |
| Layout + reading order | **PP-DocLayoutV2** | `models/Layout/PP-DocLayoutV2` | torch |
| Formula recognition | **UniMERNet small** | `models/MFR/unimernet_hf_small_2503` | torch |
| Formula recognition (alt) | PP-FormulaNet-plus-M | `models/MFR/pp_formulanet_plus_m` | torch |
| Text detect + recognise | **PP-OCRv6** (PyTorch port) | `models/OCR/paddleocr_torch` | torch |
| Table structure (wireless) | SLANet-plus | `models/TabRec/SlanetPlus/slanet-plus.onnx` | **onnxruntime** |
| Table structure (wired) | UNet | `models/TabRec/UnetStructure/unet.onnx` | **onnxruntime** |
| Table wired/wireless class. | PP-LCNet_x1_0 | `models/TabCls/paddle_table_cls/...onnx` | **onnxruntime** |
| Table orientation class. | reuses the OCR engine | — | torch |

Selection logic: `model_init.py:189-228` (`atom_model_init`). The MFR choice is made by an
env var at import time — `MINERU_FORMULA_CH_SUPPORT` (`model_init.py:64-70`); default is
`unimernet_small`, and setting it true switches to PP-FormulaNet-plus-M for Chinese formula
support.

**There is no separate formula-detection (MFD) model.** `AtomicModel.MFD` is declared
(`mineru/backend/pipeline/model_list.py:5`) but never constructed — `atom_model_init` has no
branch for it. Formula regions come from PP-DocLayoutV2's own `display_formula` /
`inline_formula` labels, filtered at `batch_analyze.py:436-441`. That is a direct consequence
of the licence cleanup in §6: `mfd_yolov8` was AGPL and was deleted, so its job was folded
into the layout model.

**No PaddlePaddle dependency.** The `pipeline` extra is
`PyYAML, ftfy, shapely, pyclipper, torch, torchvision, transformers, safetensors, onnxruntime`
(`pyproject.toml`, `[project.optional-dependencies].pipeline`). `mineru/model/utils/pytorchocr/`
is a vendored PyTorch reimplementation of PaddleOCR (attributed in `README.md:361-362` to
PaddleOCR and PaddleOCR2Pytorch). This is a genuine advantage over PaddleOCR-VL, which the
landscape review is currently leaning toward: **MinerU's OCR stack is pure torch + ORT.**

Weights are individually downloadable: `_snapshot_download_cached` passes
`allow_patterns=[relative_path, relative_path + "/*"]` for `repo_mode='pipeline'`
(`mineru/utils/models_download_utils.py:249`). So one can fetch, e.g., only
`models/MFR/unimernet_hf_small_2503` from `opendatalab/PDF-Extract-Kit-1.0` without the rest.

### 2.2 Is the pipeline backend alone useful to `ocr_handler` at 4 GB?

**As a runtime: no. As a source of two specific components: partially. As a source of two
pieces of plain Python: yes, and that is the recommendation.**

Against adopting it as a runtime:

1. **86.47, and that is on printed documents.** The number that made MinerU interesting
   (95.75) belongs to a backend we cannot run. 86.47 sits below `Marker`-class in the
   landscape's own table and well below PaddleOCR-VL-1.6's 96.34.
2. **Handwriting is the pipeline's specific, maintainer-acknowledged weakness** — see §5.
   Its OCR is PP-OCR-derived, and a MinerU collaborator wrote that PP-OCR's poor handwriting
   support is a known issue with no model-swap option. `ocr_handler`'s hard problem is
   handwritten lecture maths. This is the wrong tool for it.
3. **The dependency footprint is disqualifying for this project's constraints.**
   `ocr_handler` currently declares five runtime dependencies (`typer, pillow, numpy, scipy,
   pymupdf`). The *base* `mineru` package declares 29 — including `fastapi`, `uvicorn`,
   `python-multipart`, `modelscope`, `openai`, `magika`, `mineru-vl-utils`, `python-docx`,
   `mammoth`, `openpyxl`, `pypptx-with-oxml`, `reportlab` — before the `pipeline` extra adds
   9 more. There is no "pipeline models only, no web server, no Office parsers" install.
4. **Different rasteriser.** MinerU moved off PyMuPDF to pypdfium2 at 2.0 *for licence
   reasons* (`docs/en/faq/index.md:48`), and its own FAQ documents text loss from missing CJK
   fonts as a consequence. `scope.md`'s standing finding is that the rasteriser changes
   answers. Adopting MinerU means adopting pypdfium2 alongside the PyMuPDF path already built.

In favour, and worth recording honestly:

- **PP-DocLayoutV2 is the most interesting model in the bundle for us.** It emits layout
  boxes *and* reading order from a single forward pass (`_get_order_seqs`,
  `pp_doclayoutv2.py:935-947`, a pairwise order-logit vote), and its label set includes
  `display_formula` / `inline_formula` — which is precisely the "find the equations, give me
  boxes" step `ocr_handler` needs before it can crop for UniMERNet. Its VRAM cost and its
  behaviour on handwritten regions are both **UNVERIFIED**; §5 gives strong reason to expect
  the second to be poor. Settled by fetching it from `PaddlePaddle/PP-DocLayoutV2` (Apache-2.0
  — *not* MinerU's AGPL-declared bundle, §6.3), running it on the `-plw` fixture page, and
  counting how many ink regions it labels `image` rather than `text`/`formula`.
- **The gradio label is a claim worth naming:** *"Traditional multi-model pipeline parsing,
  low resource usage, hallucination-free"* (`mineru/cli/gradio_app.py:1640`; Chinese
  *"无幻觉"* at `:1716`). The landscape review's §4.3 found a VLM inventing
  `\frac{1}{\sqrt x}` from blank graph paper. A deterministic detector + CTC recogniser
  genuinely cannot do that. **The claim is structurally sound for the OCR path and false for
  the formula path** — UniMERNet is an autoregressive encoder-decoder and hallucinates like
  one. Do not read "hallucination-free" as covering formulas.

---

## 3. CPU fallback — it degrades silently, on the default backend

This is the question with the cleanest answer and the worst one.

### 3.1 The code path

```
mineru/utils/config_reader.py:105-137   get_device()
```
`MINERU_DEVICE_MODE` if set; else `cuda` if available; else `mps`; else a chain of
`try: torch_npu/gcu/musa/mlu/sdaa` each swallowing its exception; else — `config_reader.py:137`
— **`return "cpu"`**. No log line, no warning, no exception. The function that decides whether
this machine has a GPU cannot report that it does not.

### 3.2 What the default backend does with that

- `mineru/cli/backend_options.py:11` — `DEFAULT_BACKEND = BACKEND_HYBRID_ENGINE`. The CLI
  option defaults to it (`mineru/cli/client.py:1082`) and the help text says so
  (`client.py:1092`). This changed in 2.7.0: *"Switched the default backend from `pipeline` to
  `hybrid-auto-engine` for better out-of-the-box consistency"* (`docs/en/reference/changelog.md:38`).
  **The default is the backend the README marks ❌ for CPU.**
- `mineru/utils/engine_utils.py:10-34` — `get_vlm_engine('auto')`. On Linux
  (`_select_linux_engine`, `:46-56`): `import vllm` → vllm; else `import lmdeploy` → lmdeploy;
  else **`return 'transformers'`**. Falling back to the slowest engine is logged only as
  `"Using transformers as the inference engine for VLM."` (`engine_utils.py:33`) — which reads
  as a normal selection, not a degradation.
- `mineru/backend/vlm/vlm_analyze.py:96-101` — the transformers path:
  ```python
  device = get_device()
  model = Qwen2VLForConditionalGeneration.from_pretrained(
      model_path, device_map={"": device}, **{dtype_key: "auto"})
  ```
  **`device_map={"": "cpu"}`. No assertion, no check, no warning.** A 1.2B VLM loads onto the
  CPU and runs.

### 3.3 Where guards *do* exist, which proves the omission is not stylistic

The codebase raises loudly in four analogous situations:

| Guard | File:line |
| --- | --- |
| mlx-engine on non-Apple-Silicon → `EnvironmentError` | `vlm_analyze.py:110-111` |
| lmdeploy with `device_type='cuda'` and no CUDA → `ValueError("CUDA is not available.")` | `mineru/backend/vlm/utils.py:66-68` |
| NPU selected but `torch_npu` unavailable → `RuntimeError` | `pipeline_analyze.py:342-352`, `model_init.py:348-357` |
| `hybrid-*` without the pipeline extra → `HybridDependencyError` | `mineru/cli/common.py:56-84` |

Upstream knows how to fail loudly and does so for four narrower cases. **The broad case —
"you asked for a GPU-only backend and there is no GPU" — is the one left unguarded.**

### 3.4 Consequence, and the verdict

Run `mineru -p x.pdf` on a machine with no usable CUDA and you get the hybrid backend,
resolved to transformers, running a 1.2B VLM plus the full pipeline model set on CPU, with
`get_vram()` returning `1` so `batch_ratio` is `1` and `clean_vram`'s ≤ 8 threshold fires on
every stage. It will produce correct output. It will take, per the landscape review's own
measurement of a comparable CPU-resident VLM, on the order of minutes per page. Nothing in
the logs distinguishes this from working normally.

**This is disqualifying as an adopted runtime for `ocr_handler`, whose O5 is "stay runnable
with no GPU" and whose O3 is "say honestly what was and was not recovered."** A component
that cannot tell you it fell off the GPU cannot be part of an honest verdict.

*One mitigation, for the record:* `MINERU_DEVICE_MODE=cuda` forces `get_device()` to return
`"cuda"` unconditionally (`config_reader.py:106-108`), so a missing GPU then surfaces as a
torch error at model-load rather than as silent CPU execution. That is the pattern to copy
if we ever wrap any of this: **make the device explicit and let it fail, never auto-detect
down.**

---

## 4. Model loading cost — CPU-first, and thread-capped only where we are not

This is the section the operator asked for by name, because a model-loading script nearly
took this machine down today. **The failure mode is not guarded against on the path that
matters.**

### 4.1 Every model deserializes on CPU, then moves

| Model | Load | Move |
| --- | --- | --- |
| UniMERNet | `torch.load(model_file_path, map_location="cpu", weights_only=True)` — `mineru/model/mfr/unimernet/unimernet_hf/modeling_unimernet.py:110` | `self.model.to(self.device)` — `mineru/model/mfr/unimernet/Unimernet.py:38` |
| PP-OCR det/rec/cls | `load_file(..., device="cpu")` (safetensors) or `torch.load(..., map_location="cpu")` — `mineru/model/utils/pytorchocr/base_ocr_v20.py:61-68` | `self.net.to(device)` — `base_ocr_v20.py:41` |
| PP-DocLayoutV2 | `PPDocLayoutV2ForObjectDetection.from_pretrained(...)` — `mineru/model/layout/pp_doclayoutv2.py:930` | `self.model.to(self.device)` — `:931` |

No `low_cpu_mem_usage=True`, no `device_map` on any pipeline model, no `init_empty_weights` /
meta-device construction. The full state dict is materialised in host RAM, the module is
constructed in host RAM, and only then does it move. **Peak host RAM during load is roughly
2× the weight size per model, and the models load sequentially into a singleton that never
releases them (§1.2d).** That is the honest explanation for the documented "RAM: min 16 GB,
recommended 32 GB" against a set of models that are individually small.

### 4.2 CPU runs at fp32; GPU runs at fp16

- UniMERNet: `if not _device_.startswith("cpu"): self.model = self.model.to(dtype=torch.float16)`
  — `Unimernet.py:39-40`.
- OCR: `_resolve_inference_dtype` returns `torch.float32` when `is_cpu`, else `float16`
  — `base_ocr_v20.py:25-43`, keyed off the module constant `OCR_INFERENCE_PRECISION = "auto"`
  (`base_ocr_v20.py:11`).

**So CPU mode costs 2× the resident weight memory of GPU mode**, on top of already needing
16 GB. The "pipeline supports CPU" row is real but not cheap.

### 4.3 Thread capping — present, and on the wrong path for us

`OMP_NUM_THREADS` is set to `1` in exactly three places, all VLM:

| File:line | Context |
| --- | --- |
| `mineru/backend/vlm/vlm_analyze.py:115-116` | before importing vllm / lmdeploy |
| `mineru/model/vlm/vllm_server.py:60-61` | before `vllm_main()` |
| `mineru/model/vlm/lmdeploy_server.py:83-84` | before the lmdeploy server |

All three are guarded `if os.getenv('OMP_NUM_THREADS') is None`, i.e. they respect a
pre-existing value.

**`grep -rn "set_num_threads" --include=*.py` over the whole tree returns nothing.** There is
no `torch.set_num_threads` anywhere. On the pipeline backend running on CPU, torch's intra-op
pool defaults to one thread per core and MinerU does not touch it. **That is precisely the
"775% CPU on `llama-server`" shape the landscape review measured on the remote host and the
shape the operator flagged this morning.**

ONNX Runtime threads *are* configurable but default to unbounded:
`get_op_num_threads()` returns `-1` unless the env var is set (`mineru/utils/os_env_config.py:5-7`,
`get_value_from_string(env_value, -1)`), and `-1` is left alone by the session-option builders
(`slanet_plus/table_structure_utils.py:56-63`, `unet_table/utils.py:49-56`). The two env vars
`MINERU_INTRA_OP_NUM_THREADS` / `MINERU_INTER_OP_NUM_THREADS` are documented
(`docs/en/usage/cli_tools.md:179-185`) and are wired only into the **two table models**
(`table_structure.py:33-34`, `table_structure_unet.py:34-35`). They do nothing for layout, OCR,
or formula recognition. The changelog says they were added "to reduce CPU resource contention
conflicts in high concurrency scenarios" (`changelog.md:63`) — a server concern, not a
don't-wedge-the-workstation concern.

### 4.4 What *is* bounded

Credit where due — the PDF rasterisation pool is properly capped:

- `MAX_PDF_RENDER_PROCESSES = 3`, `MIN_PAGES_PER_RENDER_PROCESS = 30`
  (`mineru/utils/pdf_image_tools.py:37-38`);
- worker count = `min(cpus, requested, 3, pages // 30)` (`pdf_image_tools.py:101-110`);
- default requested threads is 3 (`os_env_config.py:17-18`, `MINERU_PDF_RENDER_THREADS`);
- forced to the `spawn` start method on non-Windows (`pdf_image_tools.py:158-168`), which
  avoids fork-after-torch-import hazards;
- and a render timeout defaulting to 300 s (`os_env_config.py:12-14`, `MINERU_PDF_RENDER_TIMEOUT`),
  added in 2.6.4 explicitly "to prevent long blocking of the rendering process caused by some
  abnormal PDF files" (`changelog.md:62`).

All inference is under `torch.inference_mode()` or `torch.no_grad()` — verified across
`predict_rec.py`, `predict_det.py`, `predict_cls.py`, `base_ocr_v20.py:110`,
`Unimernet.py:173`, `pp_doclayoutv2.py:384,604,705,1604`.

### 4.5 Verdict on Q4

**Deserialization is CPU-first with no memory-efficient path, and torch thread count is
uncapped on the pipeline backend.** If MinerU's pipeline were ever run on this machine
without a GPU, it would allocate ~2× fp32 weights in host RAM across seven-plus
never-released models and then saturate every core. **Set `OMP_NUM_THREADS` and
`MINERU_INTRA_OP_NUM_THREADS`/`MINERU_INTER_OP_NUM_THREADS` yourself before importing
anything, and prefer `MINERU_DEVICE_MODE=cuda` so a missing GPU errors instead of
silently landing here.** Actual peak RSS is **UNVERIFIED** — settled by
`/usr/bin/time -v` on a single-page run with `MINERU_DEVICE_MODE=cpu`, which is a CPU-only
experiment and safe to run under a thread cap.

---

## 5. Handwriting — the claim is real, the backing is not

### 5.1 What the repo claims

`README.md:57`, in the Key Features list:

> Supports scanned docs, handwriting, multi-column layouts, cross-page table merging

No metric, no citation, no qualifier. `grep -ric handwrit` over the whole clone returns
**25 lines total**, listed exhaustively below. **Not one of them is a number.**

### 5.2 The repo contradicts itself 132 lines later

`README.md:189`, and identically `docs/en/quick_start/index.md:3`:

> Document parsing is a difficult and complex task. In scenarios such as complex layouts,
> scanned pages, and **handwritten content, the parsing results may fall short of
> expectations.** We recommend trying the online demo first…

**The same README advertises handwriting as a supported capability and warns that handwriting
may disappoint, 132 lines apart.** The warning is the honest one.

### 5.3 Where the capability claim actually comes from

`docs/en/reference/changelog.md:303-306`, release 1.3.12 (2025-05-24):

> **Added support for handwritten documents through optimized layout recognition of
> handwritten text areas**
> - This feature is supported by default, no additional configuration required
> - You can refer to the instructions above to manually select the PPOCRv5 model for better
>   handwritten document parsing results

**"Handwriting support" means the layout model stopped classifying handwritten regions as
figures.** It is a detection fix, not a recognition fix. The independent research below
confirms exactly this reading, from both OmniDocBench and a MinerU maintainer.

And the recogniser choice, `changelog.md:294-299`, same release:

> In testing, we found that PPOCRv5(server) has some improvement for handwritten documents,
> **but has slightly lower accuracy than v4_server_doc for other document types, so the
> default ch model remains unchanged as `PP-OCRv4_server_rec_doc`.**

**Upstream benchmarked a more handwriting-capable recogniser, found it better on handwriting
and worse on everything else, and shipped the worse-on-handwriting one as the default.** That
is a defensible product decision and a decisive one for us: the default configuration is
explicitly not the handwriting configuration.

In 3.4.5 the model set has moved on again — `mineru/model/utils/pytorchocr/utils/resources/models_config.yml`
now maps `ch` → `ch_PP-OCRv6_small_rec_infer.safetensors` and `ch_server` →
`ch_PP-OCRv6_medium_rec_infer.safetensors`, and the v1.3.12-era `ch_lite` / `ch_server_v4`
options are gone. **Whether PP-OCRv6 retained PP-OCRv5's handwriting training is stated
nowhere in the repo — UNVERIFIED.** Note also that `en` is not a model: it is an alias that
normalises to `ch` (`mineru/utils/ocr_language.py:52`, `_CH_LANG_ALIASES`), so English
handwritten lecture notes would be read by the Chinese/English/Japanese/Latin multilingual
model.

The only other handwriting mentions are a 2.1.6 bug fix — *"Fixed table parsing issues in
handwritten documents when using `vlm` backend"* (`changelog.md:186`) — a claim that the
MinerU 2.0 VLM covers "handwriting recognition" among seven tasks (`changelog.md:275`), and
one unrelated `\mathscr` comment in the DOCX OMML converter
(`mineru/model/docx/tools/math/omml.py:48`).

### 5.4 What independent sources say (web research, this session)

The landscape review's 54.2 figure is not only confirmed, it is the *charitable* number.

| Source | Metric | MinerU | Comparator |
| --- | --- | --- | --- |
| **WildHandBench** (arXiv 2608.22959, 500 wild handwritten docs, 18 models) | Overall ↑ | **MinerU2.5 = 31.33** (2nd-last of 18); MinerU2.5-Pro = 51.73 | PaddleOCR-VL-1.6 54.21 · Gemini 3.1 Pro 71.85 · human 77.09 |
| WildHandBench | Text edit dist. ↓ | **MinerU2.5 = 83.80**; Pro = 59.80 | PaddleOCR-VL-1.6 41.52 |
| WildHandBench | Formula CDM ↑ | **MinerU2.5 = 36.56** | vs its own 94.42 on *cropped* UniMER-HWE |
| **OmniDocBench v1.0** (arXiv 2412.07626) Table 3, `Notes` | edit dist. ↓ | **MinerU = 0.984** (near-total failure) | Marker 0.470 · GOT-OCR 0.388 · InternVL2 0.226 |
| **MinerU2.5's own paper** (2509.22186) Table 6, `Notes` | edit dist. ↓ | **0.1161 — its worst category** | Academic papers 0.0235; dots.ocr beats it at 0.1116 |
| GLM-OCR (2603.10910) Table 5 | handwritten text | MinerU2.5 = 54.2 | PaddleOCR-VL-1.5 87.4 |

Three things sharpen this:

1. **OmniDocBench's own diagnosis matches the changelog's fix, and names the mechanism:**
   *"MinerU detects all handwritten notes as figures, resulting in very low recognition
   accuracy in Notes."*
2. **A MinerU maintainer says so in writing.** Issue
   [#1746](https://github.com/opendatalab/MinerU/issues/1746), `myhloli` (`COLLABORATOR`),
   2025-02-22: *"目前的ocr使用了paddleocr，对手写体支持欠佳属于已知问题。目前没有做切换ocr模型的方案"* —
   "the current OCR uses PaddleOCR; poor handwriting support is **a known issue**; there is
   currently no scheme for swapping the OCR model." And issue
   [#648](https://github.com/opendatalab/MinerU/issues/648): *"because the layout model was
   never trained on this kind of sample, the layout model classifies this PDF page as an
   image."*
3. **The formula/text gap is really a cropped/full-page gap.** MinerU2.5 scores 94.42 CDM on
   UniMER-HWE (pre-cropped single handwritten formulas) and **36.56** on WildHandBench's
   in-the-wild handwritten formulas — the same nominal task, ~58 points apart. The high HWE
   number measures a recogniser given a perfect crop; it is not evidence of handwriting
   competence on a page. *(WildHandBench also reports MinerU2.5's formula Prior-Driven Error
   at 92.16, i.e. most of its handwritten-formula errors are language-prior hallucinations —
   the same failure the landscape review measured directly in §4.3.)*

One caveat kept in view: MinerU2.5's paper **modified OmniDocBench** — *"Enhanced resolution
for Notes and Newspapers from 72 to 200 DPI"* plus 374 added pages and a changed matching
algorithm — so its 0.1161 is not comparable to v1.0's 0.984. The direction is unambiguous
across five independent sources regardless.

### 5.5 Verdict on Q5

**The capability claim is backed by a layout-detection patch and nothing else.** No MinerU
paper publishes a handwritten-*text* metric; MinerU2.5-Pro's paper deleted the per-document-type
table that contained the closest proxy. The one handwriting number MinerU does publish
(UniMER-HWE CDM ~94–95) measures pre-cropped formulas and collapses by ~58 points on real
pages.

**This is the landscape review's methodological point, confirmed from a second direction.**
MinerU sits 2nd on OmniDocBench overall and 17th of 18 on wild handwriting. Rank on printed
documents does not transfer. Anyone choosing an engine for this project from the OmniDocBench
column would pick MinerU and be wrong.

---

## 6. Licence — the code is not AGPL; the pipeline weights still say they are

### 6.1 What this clone's LICENSE actually says

`LICENSE.md`, bilingual, titled **"MinerU Open Source License"**. Verbatim opening:

> MinerU is licensed under Apache License 2.0 and is subject to the additional terms below.
> Except to the extent expressly modified or supplemented by these additional terms, your
> other rights and obligations are governed by Apache License 2.0.

Four additional terms:

1. **Commercial thresholds.** Commercial use is permitted without a separate licence *unless*
   you and your affiliates, consolidated, exceed **100 million MAU** or **USD 20 million
   monthly revenue**, in which case a separate commercial licence is required first.
2. **Online service attribution.** If you provide online services to third parties based on
   MinerU, you must clearly and prominently indicate that MinerU is used, in the product/service
   interface or in public documentation.
3. **Termination.** Breach of 1 or 2 terminates the licence and all rights automatically,
   with no notice required.
4. **Definitions** of "Affiliates" and "Control".

`© 2026 [MinerU Team]` — the placeholder brackets are in the original.

`pyproject.toml` declares `license = "LicenseRef-MinerU-Open-Source-License"` with
`license-files = ["LICENSE.md"]`. `README.md:355` restates it.

**Assessment for this project.** This is an Apache-2.0 licence with a Llama-style scale
threshold and an attribution rider. `electrical_notes` is one person's coursework: the MAU
and revenue thresholds are not remotely in play, and no online service is provided to third
parties, so term 2 does not attach either. **Vendoring MinerU source into `ocr_handler` is
clean**, subject to Apache-2.0's ordinary obligations — retain the copyright notice, state
changes, include the licence text.

*The one thing to actually watch* is term 3's automatic, no-notice termination coupled with
term 2's attribution duty. If this ever became a hosted service, attribution stops being
optional politeness and becomes a licence condition whose breach is self-executing.

### 6.2 The licence timeline

From the repo's own release notes, plus the upstream `LICENSE.md` commit history
(web research this session; not recoverable from this depth-1 clone):

- **≤ 2.x — AGPLv3.** Confirmed by `README.md:123` in retrospect, and by
  `docs/en/faq/index.md:48`: *"MinerU uses `pypdfium2` instead of `pymupdf` as the PDF page
  rendering engine in versions >= 2.0 to resolve AGPLv3 license issues."* The reason was
  stated plainly by maintainer `myhloli` in GitHub Discussion #2863: *"Since we have not
  purchased a commercial license for YOLO, all code in the entire MinerU repository remains
  under the AGPL 3.0 license."* **The AGPL was inherited from Ultralytics YOLO, not chosen.**
- **3.0.0, 2026-03-28 — the model cleanup that made the relicence possible.**
  `README.md:154`: *"Completely removed the use of two AGPLv3 models (`doclayoutyolo` and
  `mfd_yolov8`) and one CC-BY-NC-SA 4.0 model (`layoutreader`)."* **MinerU switched away from
  YOLO rather than buying a commercial Ultralytics licence** — corroborated by the current
  `pyproject.toml`, which contains no `ultralytics`, no `doclayout-yolo`, no `layoutreader`
  and no `pymupdf`, and by `mineru/model/layout/` holding only `__init__.py` and
  `pp_doclayoutv2.py` with no `mfd/` module at all.
- **3.1.0, released 2026-04-17.** `README.md:122-124`: *"MinerU has officially moved from
  `AGPLv3` to the MinerU Open Source License, a custom license based on `Apache 2.0`."*

The `LICENSE.md` commit history shows the switch was not a single clean flip — worth knowing
if anyone ever has to date a fork:

| Commit | Date | Message |
| --- | --- | --- |
| `9fe8179` | 2024-03-04 | Create LICENSE.md (AGPL-3.0) |
| `7409e64` | 2026-03-20 | AGPL-3.0 → Apache-2.0 |
| `18d2606` | 2026-03-28 | **Apache-2.0 → AGPLv3 — reverted** |
| `e148afa` | 2026-04-14 | AGPL-3.0 → Apache-2.0 again |
| `2de3411` | 2026-04-17 | "include MinerU Open Source…" |
| `2f078fc` | 2026-04-17 | "clarify commercial use terms and attribution obligations" |

Release `mineru-3.1.0-released` was published 2026-04-17T17:55Z, ~17 minutes after the final
LICENSE.md commit. **A checkout between 2026-03-28 and 2026-04-14 is AGPL.**

**`README.md:154` is the answer to the DocLayout-YOLO/Ultralytics AGPL question, from the
source.** MinerU did not inherit an AGPL layout model — it *deleted* one. `doclayoutyolo` was
replaced by PP-DocLayoutV2, `mfd_yolov8` was deleted outright with its job folded into the
layout model's `display_formula`/`inline_formula` labels (§2.1), and `layoutreader` (CC-BY-NC-SA,
i.e. non-commercial) was replaced by PP-DocLayoutV2's built-in order head. The current 3.4.5
model set carries no YOLO and no non-commercial component.

### 6.3 Code vs weights — and the trap

**Code:** unambiguous. Every source file in the clone carries
`# Copyright (c) Opendatalab. All rights reserved.` — including the vendored PaddleOCR port
(`mineru/model/utils/pytorchocr/base_ocr_v20.py:1`) and the UniMERNet implementation
(`mineru/model/mfr/unimernet/unimernet_hf/modeling_unimernet.py:1`). Upstream attributions are
in `README.md:359-370` (UniMERNet, TableStructureRec, PaddleOCR, PaddleOCR2Pytorch, pypdfium2,
pdftext, pypdf, magika, fast-langdetect, vLLM, LMDeploy) but there are **no per-component
licence files in the tree**. One licence covers all the code. `LICENSE.md` says nothing about
weights, and neither does the README or the docs site.

**Weights:** the clone names only *where* they live — `opendatalab/PDF-Extract-Kit-1.0` for the
pipeline bundle and `opendatalab/MinerU2.5-Pro-2605-1.2B` for the VLM
(`mineru/utils/enum_class.py:97-100`; ModelScope mirrors under `OpenDataLab/`). It says nothing
about their licences. From the Hugging Face card metadata (web research this session):

| Weights repo | Declared licence | Used by 3.4.5? |
| --- | --- | --- |
| `opendatalab/MinerU2.5-Pro-2605-1.2B` | **apache-2.0** | **yes** — `enum_class.py:97` |
| `opendatalab/MinerU2.5-Pro-2604-1.2B` | apache-2.0 | no (shipped with 3.1.0) |
| `opendatalab/MinerU2.5-2509-1.2B` | **agpl-3.0** | no (pre-3.1 default) |
| `opendatalab/MinerU2.0-2505-0.9B` | **none declared** | no |
| **`opendatalab/PDF-Extract-Kit-1.0`** | **agpl-3.0** | **yes — the entire pipeline backend** |

**This is the trap, and it inverts the obvious reading.** The relicence covered the code and
the *VLM* weights. **The pipeline weights bundle — the one that makes the cheap, CPU-capable,
4 GB backend work — is still declared AGPL-3.0 on Hugging Face.**

Per-file provenance says every component MinerU 3.x actually fetches traces to an Apache-2.0
upstream: PP-DocLayoutV2 from `PaddlePaddle/PP-DocLayoutV2` (Apache-2.0), the OCR port from
PaddleOCR (Apache-2.0), UniMERNet from `opendatalab/UniMERNet` (Apache-2.0), and
`unet.onnx` from RapidAI/TableStructureRec (Apache-2.0). But `PDF-Extract-Kit-1.0` **also still
hosts the old `models/MFD/` YOLOv8 and YOLOv10 layout weights** that 3.x no longer fetches,
and its repo-level card has not been updated to match the code relicence.

So *"MinerU's pipeline is Apache-2.0-clean"* is a claim resting on per-file provenance against
the distributing repo's own contrary declaration. Upstream has been asked to resolve this and
has not: **issue #4060** (2025-11-25) asks verbatim *"If different components use different
licenses (e.g., model weights vs. code), could you specify which parts can be used in
production?"* and has **no maintainer reply**; an equivalent question on the
MinerU2.5-2509-1.2B HF discussion (#7, Oct 2025) also went unanswered.

**Consequences for us:**

1. **The §7.1 recommendation is unaffected.** Vendoring `mineru/model/mfr/utils.py` is a *code*
   action, governed by `LICENSE.md` (Apache-2.0 + terms). It touches no weights.
2. **Anything that downloads from `PDF-Extract-Kit-1.0` inherits a stated AGPL.** If
   PP-DocLayoutV2 is ever evaluated here (§7.3), **fetch it from `PaddlePaddle/PP-DocLayoutV2`
   (Apache-2.0), not from MinerU's bundle** — same model, unambiguous licence.
3. The ModelScope mirror `OpenDataLab/PDF-Extract-Kit-1.0` shows no licence string at all.
   **UNVERIFIED**; assume it matches the HF card.

## 7. What to take, and what to leave

### 7.1 Take this: `mineru/model/mfr/utils.py`

**The single most directly applicable artifact in the repo, and it is not a model.** 448 lines
of pure Python — `import re` is its only dependency — doing two jobs `ocr_handler` needs for
the UniMERNet-B path it has already chosen.

**(a) LaTeX repair for UniMERNet output.** `latex_rm_whitespace(s)` (`mfr/utils.py:317-340`) is
applied to every generated string at `modeling_unimernet.py:152`. It composes:

| Function | `mfr/utils.py` | What it fixes |
| --- | --- | --- |
| `fix_unbalanced_braces` | `:163-207` | drops `{`/`}` with no partner, escape-aware |
| `fix_latex_left_right` | `:10-49` | `\left`/`\right` without a valid delimiter get `.`; if counts differ, strips them all |
| `fix_left_right_pairs` | `:52-133` | moves a `\right` that ended up at the wrong brace depth |
| `fix_latex_environments` | `:254-277` | inserts a missing `\begin{array}`/`\end{...}` for 12 KaTeX-safe environments |
| `remove_up_commands` | `:300-306` | `\upalpha` → `\alpha`, keeping `\uparrow`/`\downarrow`/`\uplus`/`\upsilon` |
| `remove_unsupported_commands` | `:309-314` | strips `\lefteqn`, `\boldmath`, `\ensuremath`, `\centering`, `\emph`, … |
| `REPLACEMENTS_PATTERNS` | `:280-296` | 15 substitutions: `\underbar`→`\underline`, `\Bar`→`\hat`, `\vDash`→`\models`, `\sq \sqcup`→`\square`, … |
| `process_latex` | `:210-245` | inserts a space after a backslash where the next token would otherwise glue |

These are empirical fixes for the specific ways a Swin+mBART encoder-decoder emits malformed
LaTeX — which is the exact model family `ocr_handler` runs. **Reproducing this list by
observation would cost days.** It also normalises `\qquad` (`QQUAD_PATTERN`, `:297`, applied at
`:334`), which is directly relevant given the landscape review's finding that both model
families emit `\quad`/`\qquad` for deliberately-blank regions — that token is the ink control's
signal and must survive post-processing intact.

*Adoption note:* the aggressive branch of `fix_latex_left_right` deletes **all** `\left`/`\right`
when the counts disagree (`:45-49`) rather than repairing them. For lecture maths that is
usually right; for a genuinely unbalanced source it silently changes the meaning of the
delimiters. Port it with that branch behind a flag.

**(b) Area-sorted dynamic batching.** `build_mfr_batch_groups` (`mfr/utils.py:393-448`) with
`largest_power_of_two_leq` (`:343`), `get_mfr_effective_batch_size` (`:349`),
`get_mfr_min_dynamic_batch_size` (`:356`) and `finalize_mfr_batch_groups` (`:360`). The caller
(`Unimernet.py:152-176`) sorts every formula crop by pixel area, batches ascending, and
**halves the batch size each time the running mean crop area exceeds 4× / 8× / 16× the
baseline batch's mean**, with a floor of `max(16, requested // 4)`.

This is a memory-shaping strategy for exactly our constraint: a single wide display equation
can be 20× the area of an inline one, and a fixed batch size must be sized for the worst crop
or it OOMs. **On a 6 GB card feeding UniMERNet-B a page of mixed inline and display maths,
this is the difference between a fixed conservative batch and a filled one.** Its actual
benefit here is **UNVERIFIED** — settled by measuring peak `torch.cuda.max_memory_allocated()`
and wall time on the `-plw` fixture page's formula crops, fixed batch vs this grouping. That
experiment needs only UniMERNet-B, which this project already has at 681 MiB measured.

Both are Apache-2.0-plus-terms, both are `import re` / `torch` only, and vendoring them
avoids every objection in §2.2 — no 38 dependencies, no pypdfium2, no silent CPU fallback.

### 7.2 Take this too: three engineering patterns, free

1. **The explicit-device rule.** `MINERU_DEVICE_MODE` (`config_reader.py:106-108`) overrides
   detection entirely. Copy the *override*, not the *auto-detect* — `ocr_handler` should make
   the device explicit and let a missing GPU raise, never fall through to `"cpu"` unannounced.
   §3 is the worked example of why.
2. **Individually-addressable weight downloads.** `allow_patterns=[path, path + "/*"]`
   (`models_download_utils.py:249`) against a monorepo model bundle. If `ocr_handler` ever
   pulls PP-DocLayoutV2 or UniMERNet-small for a comparison, this is how to fetch one model
   from `opendatalab/PDF-Extract-Kit-1.0` without the other 20 GB.
3. **Bounded rasterisation.** `MAX_PDF_RENDER_PROCESSES = 3` + `spawn` + a 300 s per-render
   timeout (`pdf_image_tools.py:37,158-168`; `os_env_config.py:12-14`). `ocr_handler` renders
   pages too, and MinerU's caps are more conservative than the obvious `cpu_count()` default.

### 7.3 Leave this

- **The VLM backend (MinerU2.5-Pro-1.2B).** 8 GB floor, no CPU fallback, and 31.33 / 51.73
  overall on wild handwriting. The 95.75 that put it on the shortlist is a printed-document
  number.
- **The pipeline backend as a runtime.** 86.47 on printed documents, PP-OCR handwriting that
  its own maintainer calls a known issue, 38 direct dependencies against this project's 5,
  and a different rasteriser from the one `scope.md` standardised on.
- **The `mineru` package as a dependency, in any form.** There is no pipeline-only install;
  the base package alone pulls `fastapi`, `uvicorn`, `openai`, `modelscope`, `magika`,
  `python-docx`, `mammoth` and `openpyxl`.
- **PP-DocLayoutV2 — provisionally, not finally, and not from MinerU's bundle.** It is the one
  MinerU model with a plausible role here: layout + reading order + `display_formula` /
  `inline_formula` boxes in one forward pass, no YOLO. But MinerU's *entire* documented
  handwriting fix was making the layout model stop calling handwriting a figure, and
  OmniDocBench plus issue #648 say the layout stage is exactly where MinerU loses handwritten
  pages. **UNVERIFIED and worth 30 minutes:** fetch it from **`PaddlePaddle/PP-DocLayoutV2`
  (Apache-2.0)** — *not* from `opendatalab/PDF-Extract-Kit-1.0`, which is declared AGPL-3.0
  (§6.3) — run it on the `-plw` fixture page, and count how many ink regions come back
  labelled `image`. If it labels them `text`/`formula` with sane boxes it is a candidate for
  the crop-finding step; if it calls them figures it is disqualified for the same reason
  MinerU is.

### 7.4 The direct answer

**Is any part of MinerU worth adopting for a 6 GB card?**

**Yes — `mineru/model/mfr/utils.py`, vendored, for the UniMERNet post-processing and the
area-sorted dynamic batching.** That is a licence-clean, dependency-free, ~470-line file that
solves two problems this project will otherwise solve worse and slower, on the equation path
it has already committed to.

**No to everything that loads MinerU's weights.** The configuration that fits in 6 GB scores
86.47 and cannot read handwriting; the configuration that scores 95 needs 8 GB, mandates a
GPU, and still comes 17th of 18 on wild handwriting. And the cheap tier carries a licence
problem the expensive tier does not — its weights bundle is still declared AGPL-3.0 while the
code and the VLM weights moved to Apache-2.0.

MinerU's real contribution to this project is that it is the only vendor honest enough to
publish the table that shows the trade-off — and the table shows its own cheap tier is not
good enough for the job.

---

## Sources

**Primary — read in the clone, `~/tmp/ocr_repos/MinerU` @ `4fe4bde`, 3.4.5**
`LICENSE.md` · `pyproject.toml` · `README.md` · `mineru/version.py` · `mineru.template.json` ·
`mineru/utils/{model_utils,config_reader,engine_utils,os_env_config,enum_class,ocr_language,models_download_utils,pdf_image_tools}.py` ·
`mineru/backend/pipeline/{pipeline_analyze,batch_analyze,model_init,model_list}.py` ·
`mineru/backend/hybrid/hybrid_analyze.py` · `mineru/backend/vlm/{vlm_analyze,utils}.py` ·
`mineru/model/mfr/{utils.py,unimernet/Unimernet.py,unimernet/unimernet_hf/modeling_unimernet.py}` ·
`mineru/model/layout/pp_doclayoutv2.py` · `mineru/model/ocr/pytorch_paddle.py` ·
`mineru/model/utils/pytorchocr/{base_ocr_v20.py,utils/resources/models_config.yml}` ·
`mineru/model/table/rec/{slanet_plus,unet_table}/*` · `mineru/model/vlm/{vllm_server,lmdeploy_server}.py` ·
`mineru/cli/{backend_options,client,common,gradio_app}.py` ·
`docs/en/{quick_start/index.md,quick_start/extension_modules.md,quick_start/docker_deployment.md,usage/cli_tools.md,faq/index.md,reference/changelog.md}` ·
`docker/compose.yaml`

**Web, this session — handwriting**
WildHandBench arXiv 2608.22959 · MinerU2.5 arXiv 2509.22186 (Tables 6, 11) ·
MinerU2.5-Pro arXiv 2604.04771 (Table 5) · GLM-OCR arXiv 2603.10910 (Table 5) ·
OmniDocBench arXiv 2412.07626 (Table 3) ·
`github.com/opendatalab/MinerU/issues/{648,1746,3223,3818,5351}` ·
`opendatalab.github.io/MinerU/reference/changelog/`

**Web, this session — licensing**
`github.com/opendatalab/MinerU/blob/master/LICENSE.md` + its commit history via the GitHub API ·
release `mineru-3.1.0-released` (2026-04-17T17:55Z) · `pypi.org/project/mineru/` (3.4.5) ·
`github.com/opendatalab/MinerU/discussions/2863` (the YOLO/AGPL statement) ·
`github.com/opendatalab/MinerU/issues/4060` (weights-vs-code question, unanswered) ·
HF cards: `opendatalab/{PDF-Extract-Kit-1.0, MinerU2.5-2509-1.2B, MinerU2.5-Pro-2604-1.2B,
MinerU2.5-Pro-2605-1.2B, MinerU2.0-2505-0.9B}` · `PaddlePaddle/PP-DocLayoutV2` ·
`github.com/{PaddlePaddle/PaddleOCR, opendatalab/UniMERNet, RapidAI/TableStructureRec}`

**Not executed.** No model was downloaded, no inference run, no GPU touched, nothing installed.
Every `file:line` is from static reading; every claim needing a run is marked UNVERIFIED above.

---

**See:** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) · [`../scope.md`](../scope.md)
