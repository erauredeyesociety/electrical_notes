# PaddleOCR-VL — source teardown, 2026-09-05

A static read of the code that would actually run on this machine, prompted by an evaluation
attempt that saturated the CPU during weight loading and was killed before it reached the GPU.

**Nothing was executed.** No weights downloaded, no inference, no GPU touched, no ML framework
installed. Every behavioural claim below is cited to a file and line. Claims I could not settle
from source are marked **UNVERIFIED** with a note on what would settle them.

> This document **contradicts** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) in
> three places and **strengthens** it in two. See [§9](#9-where-this-contradicts-the-landscape-review).
> That file and `INDEX.md` are not edited.

---

## Verdict up front

| # | Question | Answer |
| --- | --- | --- |
| 1 | Fits in ~4.3 GB free? | **Steady-state yes (~3.0–3.5 GiB). Loading is the binding constraint, at ~3.6–4.6 GiB peak, and it is marginal.** The failure mode is `from_pretrained`, not inference |
| 2 | What does loading cost? | **Two full copies of the weights on the target device, plus a full random-init of 958 M parameters.** No `low_cpu_mem_usage`, no meta-device init, no thread cap anywhere |
| 3 | Silent CPU fallback? | **Yes — three of them.** Device selection, dtype selection, and flash-attention detection all degrade silently. The dtype one doubles memory to fp32 |
| 4 | Quantization? | **None in the repo. Zero.** The only quantized path is an out-of-process llama.cpp server, and the *official* GGUF is an F16 conversion, not a quantization |
| 5 | Input contract? | **Two-stage: a layout model crops, the VLM reads crops one at a time.** It duplicates `ink.py`'s grouping job on *content*; `ink.py` groups on *ink*. They compose, but only via `use_layout_detection=False` |
| 6 | Licence | **Code Apache-2.0, weights Apache-2.0, stated separately and both clean.** Confirmed from the LICENSE files, not the badges |

**The single most useful number in this document:** the model is **958,588,736 parameters, every
tensor BF16, 1,917,177,472 bytes = 1.786 GiB**, computed from the safetensors header manifest, not
from anybody's blog. Everything else follows from that.

**The single most useful behavioural finding:** the 40 GB OOM reports and the 3.3 GB success report
are *both true* and describe *different code*. The blow-up is an `O(N²)` fp32 attention buffer in the
vision tower, and between the version those reports were filed against and the version you would run
today, `N` fell 2.8× and an SDPA path was added. See [§3](#3-resolving-45-gb-vs-33-gb-vs-8-gb-vs-12-gb).

---

## 0. What was read, and where it lives

The clone at `~/tmp/ocr_repos/PaddleOCR` is at commit `2661c7c` (2026-07-22). **It does not contain
the model.** `paddleocr` is a thin CLI/pipeline wrapper; the implementation lives in its pinned
dependency:

- `/home/devel/tmp/ocr_repos/PaddleOCR/pyproject.toml:50` — `"paddlex[ocr-core]>=3.7.0,<3.8.0"`

So the teardown covers three source sets:

| Source | How cited below | Where |
| --- | --- | --- |
| The clone | `PaddleOCR/<path>:<line>` | `/home/devel/tmp/ocr_repos/PaddleOCR/` |
| PaddleX **v3.7.2** (the newest tag satisfying the pin) | `paddlex/<path>:<line>` | fetched read-only from `raw.githubusercontent.com/PaddlePaddle/PaddleX/v3.7.2/`, copies under the session scratchpad at `…/scratchpad/px/` |
| The HF weights repo's `trust_remote_code` files | `hf:<file>:<line>` | fetched read-only from `huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6`, copies under `…/scratchpad/hf_pvl16/` |

Only text files were fetched. The one binary touched was a **78,488-byte HTTP range read of the
safetensors JSON header** (`bytes 8–78495`) to get the tensor manifest. No tensor data was read; the
1.917 GB payload was never requested.

**Version note that saves confusion:** `config.json`, `configuration_paddleocr_vl.py` and
`image_processing_paddleocr_vl.py` are byte-identical across PaddleOCR-VL, -1.5 and -1.6, and
`modeling_paddleocr_vl.py` is identical between 1.5 and 1.6. 1.5→1.6 is a pure weight refresh. The
one thing that *did* change between 1.0 and 1.5 is `preprocessor_config.json`, and it is the change
that matters most for VRAM (§3).

---

## 1. The exact weight footprint

Computed from the safetensors header (620 tensors), not from a parameter count in a paper.

```
total params   958,588,736
total bytes  1,917,177,472   = 1.786 GiB = 1.917 GB
dtypes       BF16 only — every one of the 620 tensors
```

| Component | Params | % | bf16 | fp32 |
| --- | ---: | ---: | ---: | ---: |
| `visual.*` (SigLIP-so400m-shaped tower, 27 layers) | 465,974,336 | 48.6% | 0.868 GiB | 1.736 GiB |
| `model.layers.*` (ERNIE-4.5 decoder, 18 layers) | 254,840,832 | 26.6% | 0.475 GiB | 0.949 GiB |
| `lm_head.weight` `[103424, 1024]` | 105,906,176 | 11.0% | 0.197 GiB | 0.395 GiB |
| `model.embed_tokens.weight` `[103424, 1024]` | 105,906,176 | 11.0% | 0.197 GiB | 0.395 GiB |
| `mlp_AR.*` (2-layer projector, 4608→4608→1024) | 25,960,192 | 2.7% | 0.048 GiB | 0.097 GiB |
| `model.norm.weight` | 1,024 | — | — | — |
| **total** | **958,588,736** | | **1.786 GiB** | **3.571 GiB** |

Two things worth internalising:

1. **The vision tower is as large as the language model.** 466 M vs 467 M (LM incl. both untied
   embedding matrices). "0.9B" is not "a 0.3B LM with a small ViT bolted on" — it is half encoder.
   Anything that shrinks only the LM (most GGUF quant schemes, most serving optimisations) leaves
   half the model untouched.
2. **`tie_word_embeddings: false`.** The two 103,424 × 1,024 matrices are separate — 212 M params,
   22% of the model, spent on a 103 k vocabulary.

Architecture, from `config.json` (all three versions):

```
LM     hidden 1024 · layers 18 · heads 16 · kv_heads 2 (GQA 8:1) · head_dim 128
       intermediate 3072 · vocab 103424 · max_position_embeddings 131072
       rope_theta 500000 · mrope_section [16,24,24] · torch_dtype bfloat16
vision hidden 1152 · layers 27 · heads 16 · intermediate 4304
       patch 14 · image_size 384 · spatial_merge_size 2
```

Plus one tensor the config does not mention and that governs the input ceiling:

```
visual.vision_model.embeddings.packing_position_embedding.weight   [32768, 1152]   37.7 M params
```

A NaViT-style packed position table for **32,768 visual patches**. That is the architectural hard cap
on one vision forward pass — 8,192 LM tokens after the 2×2 merge. Nothing in the pipeline gets near
it (§7).

---

## 2. Where the memory actually goes at run time

Weights are the easy part. Three other terms matter, and one of them is quadratic.

### 2.1 Visual sequence length is bounded, and the bound is set in two places

`smart_resize` (`hf:image_processing_paddleocr_vl.py:128-173`) is the standard Qwen2-VL rescale:
snap both dimensions to a multiple of `factor = 28` (patch 14 × merge 2), then scale so total pixels
land in `[min_pixels, max_pixels]`. Note it scales **both** ways — a crop *smaller* than `min_pixels`
is bicubically **upscaled**, not padded (`:169-172`).

| | min_pixels | max_pixels | raw patches (÷196) | LM visual tokens (÷784) |
| --- | ---: | ---: | ---: | ---: |
| `preprocessor_config.json`, PaddleOCR-VL **1.0** | 147,384 | **2,822,400** | 752 – **14,400** | 188 – 3,600 |
| `preprocessor_config.json`, **1.5 / 1.6** | 112,896 | **1,003,520** | 576 – **5,120** | 144 – **1,280** |
| PaddleX pipeline defaults (used by `paddleocr`) | 112,896 | 1,003,520 | 576 – 5,120 | 144 – 1,280 |
| `spotting` blocks only | 112,896 | 1,605,632 | 576 – 8,192 | 144 – 2,048 |

The pipeline defaults are hardcoded in PaddleX and do **not** read the preprocessor JSON:

- `paddlex/inference/pipelines/paddleocr_vl/pipeline.py:664` — `default_min_pixels = … else 112896`
- `paddlex/inference/pipelines/paddleocr_vl/pipeline.py:666` — `default_max_pixels = … else 1003520`
- `paddlex/inference/pipelines/paddleocr_vl/pipeline.py:338-339` — spotting overrides to `1605632`

They are also per-block-type overridable (`ocr_max_pixels`, `table_max_pixels`, `formula_max_pixels`,
`chart_max_pixels`, `seal_max_pixels` — `pipeline.py:675-701`). **`max_pixels` is the dominant VRAM
knob and it is a first-class argument**, exposed all the way up to the CLI
(`PaddleOCR/paddleocr/_pipelines/paddleocr_vl.py:485-492`).

### 2.2 The quadratic term: vision attention

The vision tower runs **dense bidirectional attention over the whole packed patch sequence**, with no
windowing and no mask. Both are verifiable:

- `hf:modeling_paddleocr_vl.py:2203` passes `window_size=-1` from the top-level forward, and
  `:1417` gates windowing on `window_size > 0` — so window attention is **off** on the generation path.
- The top-level forward (`hf:modeling_paddleocr_vl.py:2193-2205`) never passes `attention_mask` into
  `self.visual(...)`, so it is `None` all the way down to the attention kernel.

Which kernel runs decides everything.

**Torch path** (`hf:modeling_paddleocr_vl.py:1089-1091, 1126-1140`):

```python
use_flash_attn = (cu_seqlens is not None) and self.config._attn_implementation == "flash_attention_2"
...
if not use_flash_attn:
    attention_interface = eager_attention_forward          # line 1127
    ...
    elif self.config._attn_implementation == "sdpa":
        attention_interface = sdpa_attention_forward       # line 1135
```

and `eager_attention_forward` (`:1043`) does
`softmax(attn_weights, dim=-1, dtype=torch.float32)` — a materialised `[1, 16, N, N]` **fp32** tensor.

**Paddle path** (`paddlex/…/modeling/paddleocr_vl/_siglip.py`), and this one has a hardware gate:

```python
cap = get_gpu_compute_capability()          # :146
self._supports_sdpa = False                 # :148
if cap is not None and cap >= (8, 0) and cuda_ver >= (11, 4) and platform.system() == "Linux":
    self._supports_sdpa = True              # :156
...
if not self._supports_sdpa or q.dtype == paddle.float32:   # :185
    attn_output, _ = eager_attention_forward(...)          # :191
else:
    attn_output = paddle.nn.functional.scaled_dot_product_attention(...)  # :203
```

with `eager_attention_forward` at `_siglip.py:99-125` doing bf16 matmul → `.cast(float32)` →
`softmax` → `.cast(bf16)`.

Cost of that fp32 buffer, `16 · N² · 4` bytes for one copy:

| N (raw patches) | Corresponds to | one fp32 buffer | realistic peak (2–3 copies live) |
| ---: | --- | ---: | ---: |
| 576 | `min_pixels`, a small crop | 20 MiB | ~50 MiB |
| 2,048 | a mid-size text block | 256 MiB | ~0.6 GiB |
| **5,120** | **1.6 `max_pixels`, a full-page crop** | **1.56 GiB** | **~3.1–3.9 GiB** |
| 8,192 | a `spotting` block | 4.0 GiB | ~8–10 GiB |
| 14,400 | **1.0 `max_pixels`** | **12.36 GiB** | ~25–40 GiB |

With SDPA or flash-attention the same workload costs `O(N)` — at N = 5,120 the whole vision
activation set is about **90 MiB**.

**On an RTX 3060 Laptop (CC 8.6, Linux, CUDA ≥ 11.4) the paddle gate passes and SDPA is used.**
That is the difference between fitting and not fitting, and it is decided by three environment
checks with no logging on either branch.

### 2.3 The language model always uses eager attention

```python
def set_attn_func(self):                                  # paddlex/…/_ernie.py:657
    if config.use_flash_attention:
        self.attn_func = self._flash_attention_wrapper     # :665
    else:
        self.attn_func = self.core_attn                    # :667
```

`config.json` ships `"use_flash_attention": false`, and **nothing in PaddleX ever overrides it** —
`grep -rn use_flash_attention paddlex/` returns only the definition (`_config.py:106,147`) and the two
read sites. So `core_attn` (`_ernie.py:822-900`) always runs, materialising `[1, 16, L, L]` and casting
it to fp32 at `:870`.

This is survivable because `L` is small: 1,280 visual tokens + ~20 text tokens ≈ 1,300 at prefill.
`16 · 1300² · 4 ≈ 108 MiB` per buffer, ~0.3 GiB peak. It is *not* survivable if you ever feed the LM a
long sequence, which the architecture would otherwise allow (`max_position_embeddings: 131072`).

Two smaller LM terms:

- **Prefill logits.** Paddle's generate computes logits for every position, then slices
  (`paddlex/…/generation/utils.py:1421` — `logits = logits[:, -1, :]`). At L = 1,300 that is
  `1300 × 103424 × 2 B = 269 MiB` of bf16 logits, allocated then discarded. No fp32 upcast — the LM
  head has no cast (checked `_ernie.py:1519-1600`).
- **KV cache is negligible.** GQA with 2 KV heads: `18 layers × 2 × 2 heads × 128 dim × 2 B =
  18,432 B/token`. A full 4,096-token generation on a 1,300-token prompt is **99 MiB**. This is one
  place the architecture is genuinely frugal.

  (`core_attn` does `paddle.repeat_interleave(k, 8, axis=1)` at `_ernie.py:861-862` — it re-expands the
  whole cache from 2 heads to 16 on **every decode step**. 44 MiB allocated and freed 4,096 times.
  That is a throughput cost, not a capacity one, and it is a large part of why the naive local path
  is slow.)

### 2.4 Budget, RTX 3060 Laptop, 4.3 GB free = 4.005 GiB

Assuming the default `paddleocr` path: paddle native backend, bf16, SDPA active, layout detection on,
one page at `max_pixels = 1,003,520`.

| Term | GiB | Source |
| --- | ---: | --- |
| VLM weights, bf16 | 1.79 | safetensors manifest, §1 |
| PP-DocLayout weights | ~0.20 | `PaddleOCR/docs/version3.x/module_usage/layout_analysis.en.md:71` — V2 is 203.8 MB. **V3 size UNVERIFIED** |
| CUDA context + cuBLAS/cuDNN workspaces + allocator slack | 0.3–0.8 | **UNVERIFIED** — not measurable from source |
| Vision activations, SDPA, N = 5,120 | ~0.09 | §2.2 |
| LM prefill attention + logits | ~0.55 | §2.3 |
| KV cache @ 5.4 k tokens | ~0.10 | §2.3 |
| **steady-state total** | **≈ 3.0–3.5** | |
| **`from_pretrained` peak** (§4) | **≈ 3.6–4.6** | 2 × weights + layout model + context |

**Conclusion: inference fits with headroom; loading does not reliably fit.** That is the opposite of
what everyone assumes, and it matches the symptom that prompted this teardown.

Three things would push it over: eager attention instead of SDPA (+3 GiB), fp32 instead of bf16
(+1.8 GiB of weights and +2× on every activation), or `max_pixels` left at the 1.0 value. All three
are silent (§5).

---

## 3. Resolving 45 GB vs 3.3 GB vs 8 GB vs 12 GB

The landscape review flagged this as the open question. It is resolvable, and the resolution is that
**all four numbers are correct about different things**.

| Claim | What it actually is | Verdict |
| --- | --- | --- |
| **45 GB** | HF `PaddleOCR-VL/discussions/59`, one user on a Colab **A100**, Nov 2025, official model-card snippet, **PaddleOCR-VL 1.0**, `max_pixels = 2,822,400`, eager attention. `16 · 14400² · 4 = 12.36 GiB` per softmax buffer × ~3 live × reservation ≈ 40–45 GB | **Real, reproducible from the arithmetic, and obsolete.** Fixed by 1.5's `max_pixels` cut and by SDPA |
| **3.3 GB** | Same thread, same user, same page, with `attn_implementation="flash_attention_2"` | **Real.** 1.92 GB weights + ~1.4 GB of everything else |
| **8 GB** | FastDeploy best-practices page, *"Recommended Hardware Configuration: GPU Memory: 8GB or more"*, immediately followed by `api_server` launch commands with `--gpu-memory-utilization 0.7–0.8` | **Serving preallocation, not a model floor.** The landscape review is right about this |
| **12 GB** | `PaddlePaddle/PaddleOCR` issue **#16823**, the pinned maintainer FAQ: *"the minimum supported configuration that successfully runs is an **RTX 3060 (12 GB)**"* | **The vendor's own stated floor, and the landscape review missed it.** But it is stated for the default paddle dynamic-graph path, and the same FAQ concedes that path *"exhibits significant fluctuations in memory usage"* |

The `inference_mode` half of the landscape review's claim does not survive contact with the source.
A second user in the same discussion posted a 2×2 ablation on an RTX 5060 Ti: inference_mode moved
VRAM by **0.02 GB** (and was marginally *worse* with FA2), while sdpa cost only 0.11 GB over FA2.
That is exactly what the source predicts — `GenerationMixin.generate` is already decorated
`@torch.no_grad()`, so wrapping the call adds nothing. **The flash-attn/sdpa choice is the whole
effect; `inference_mode` is noise.**

The strongest single piece of evidence is arithmetic: **every OOM allocation size reported in the
PaddleOCR and HF issue trackers is exactly `16 · N² · 4` bytes** (or `× 2` for the bf16 copy) for an
`N` at or just under the 14,400-patch cap:

| Reported failed allocation | Implied N | Implied Mpx | Issue |
| ---: | ---: | ---: | --- |
| 11.809693 GB | 14,076 | 2.76 | HF #47, #33; PaddleOCR #16852 |
| 11.351109 GB | 13,800 | 2.70 | PaddleOCR #16788 |
| 6.067032 GB | 10,089 | 1.98 | PaddleOCR #16852 (4090) |
| 2.843554 GB (bf16) | 9,768 | 1.91 | PaddleOCR #17064 |

and the Paddle C++ tracebacks in those issues name `SoftmaxGPUDNNKernel<float, ...>` and
`CastCUDAKernelImpl<bfloat16, float>` — the fp32 softmax over the attention matrix, exactly the two
lines at `_siglip.py:116-118`. HF #47's reporter closed his own issue with *"The size of the image was
too big. Making it smaller fixed the issue."*

**And the code those reports describe no longer exists.** In PaddleX **v3.3.0 and v3.3.5** — the tags
current when PaddleOCR-VL 1.0 shipped — `_siglip.py` calls `eager_attention_forward` unconditionally;
there is no `_supports_sdpa` at all (verified by fetching `_siglip.py` at tags v3.3.0, v3.3.5,
v3.3.13, v3.4.0, v3.5.0, v3.6.0, v3.7.0: the gate first appears in v3.3.13). Combined with the 2.8×
`max_pixels` cut, the worst-case vision attention buffer went from **12.36 GiB to 1.56 GiB, and then
to ~0** on any CC ≥ 8.0 card.

The one first-hand 6 GB data point that exists: `ggml-org/llama.cpp` issue **#25339** — *"Ryzen 7640HS
+ RTX 3050 6gb"*, *"paddleocr vl 1.6 gguf q8"*, `-ngl 999 -c 20000 -np 4 -fa on`, fully offloaded and
serving. The issue is about a chat-template parsing bug, not memory. **UNVERIFIED for the transformers
and paddle paths — no first-hand 6 GB report exists for either.**

---

## 4. What loading costs — the thing that bit us

Reconstructed from `paddlex/inference/models/common/transformers/transformers/model_utils.py`.

### 4.1 The model is fully materialised *and randomly initialised* before any weight is read

```python
init_contexts = []                                   # :1781
if dtype:
    init_contexts.append(dtype_guard(dtype))         # :1784
...
with ContextManagers(init_contexts):
    model = cls(config, *init_args, **model_kwargs)  # :1807
```

`init_contexts` contains **only** a dtype guard. There is no meta-device init and — although the file
defines `no_init_weights()` at `:94` — **it is never used by `from_pretrained`**. In Paddle's dynamic
mode `nn.Linear`/`nn.Embedding` allocate and run their default initializer at construction. So
constructing the model allocates the full 1.786 GiB (bf16) or 3.571 GiB (fp32) **and generates
958,588,736 random values** on the current device before the checkpoint is opened.

On GPU that is fast. On CPU — which is where you land after the silent fallback in §5 — it is
958 M gaussian samples into 3.57 GiB of host memory, on whatever thread pool Paddle's CPU ops use.

### 4.2 Then a second full copy is loaded onto the same device

```python
state_dict, scale_dict = _load_part_state_dict_from_safetensors(
    keys, checkpoint_file, tensor_parallel_split_mapping, fliter_dict_keys,
    "expected",                                       # :266  ← hardcoded, ignores the device= arg at :243
    ...)
```

and inside, per tensor:

```python
if not return_numpy and device == "expected":
    weight = weight._copy_to(paddle.framework._current_expected_place(), True)   # :212-215
```

The predictor wraps the whole call in `with TemporaryDeviceChanger(self.device):`
(`paddlex/inference/models/doc_vlm/predictor.py:161-165`), so `_current_expected_place()` is
`CUDAPlace(0)`. **The entire state dict is copied to the GPU** — 1.786 GiB, on top of the 1.786 GiB
of already-allocated parameters.

Both are live at the same time. `_load_state_dict_into_model` calls
`model_to_load.set_state_dict(state_dict)` (`:306`), which *copies into* the existing parameters, and
only then does `del state_dict` (`:309`).

```
peak device allocation during from_pretrained  ≈  2 × 1.786 GiB  =  3.57 GiB
```

`low_cpu_mem_usage` — which would take the meta-device path at `:1584` and avoid this — defaults to
**`False`** (`:1732`) and is not plumbed through PaddleX's predictor.

### 4.3 The layout model is loaded first, so it is resident during that peak

`paddlex/inference/pipelines/paddleocr_vl/pipeline.py:110-142` creates `self.layout_det_model`,
**then** `:152` creates `self.vl_rec_model`. So the ~0.2 GiB layout model plus its Paddle Inference
workspace are already on the card when the 3.57 GiB spike happens.

### 4.4 Thread and CPU behaviour

Searched for `set_num_threads`, `OMP_NUM_THREADS`, `MKL_NUM_THREADS`, `cpu_count`, `multiprocessing`
across the clone and every PaddleX file involved in this path.

| Finding | Where |
| --- | --- |
| **Nothing sets `OMP_NUM_THREADS` or `paddle.set_num_threads` anywhere.** `set_env_for_device_type` sets device flags for NPU/XPU/MLU/DCU/GCU and **nothing at all for `gpu` or `cpu`** | `paddlex/utils/device.py:117-160` |
| `DEFAULT_CPU_THREADS = 10` exists but is only wired into the **Paddle Inference static engine** (`config.set_cpu_math_library_num_threads`), i.e. the layout/orientation models, never the VL model | `PaddleOCR/paddleocr/_constants.py:20`; `PaddleOCR/paddleocr/_common_args.py:95` |
| Download is single-threaded, `requests`-based, no parallel chunks | `paddlex/utils/download.py:47-79` |
| Layout-prep thread pool defaults to **0 workers** (disabled) | `pipeline.py:177` — `lp = config.get("layout_prep_cpu_workers", 0)` |
| **`use_queues: True` by default, with three long-lived threads and very large queues** | `paddlex/configs/pipelines/PaddleOCR-VL-1.6.yaml`; `pipeline.py:1019-1023, 1157-1164` |

That last row is the CPU-side hazard. The default v1.6 pipeline YAML ships `batch_size: 64` and
`use_queues: True`. `ImageBatchSampler` is built with that batch size (`pipeline.py:156-158`), and:

```python
max_num_batches_in_process = 64                       # :1019
queue_input = queue.Queue(maxsize=max_num_batches_in_process)   # :1020
queue_cv    = queue.Queue(maxsize=max_num_batches_in_process)   # :1021
queue_vlm   = queue.Queue(maxsize=self.batch_sampler.batch_size * max_num_batches_in_process)  # :1022-1023
```

`_worker_input` (`:1029-1042`) rasterises pages as fast as it can and pushes batches; `_worker_cv`
runs layout detection; `_worker_vlm` consumes. But for the local backend
`MAX_NUM_BOXES = self.vl_rec_model.batch_sampler.batch_size` (`:1076`) and that is **forced to 1**:

- `paddlex/inference/models/doc_vlm/constants.py:36` — `PADDLEOCR_VL_LOCAL_BATCH_SIZE = 1`
- `predictor.py:70-78` — warns and clamps any larger batch size

So the producer can buffer up to **64 batches × 64 decoded page images** in host RAM while the
consumer processes one crop at a time. At 200 dpi a page is ~11 MB of BGR uint8. That is a
producer-outruns-consumer memory ramp running concurrently with GPU work, on a laptop, and it is on
by default. **On a single-page input it is irrelevant; on a directory or a long PDF it is not.**

### 4.5 The transformers backend loads differently, and better for VRAM

`engine="transformers"` is a supported value (`PaddleOCR/paddleocr/_common_args.py:29-35`) and routes
to `DocVLMTransformersPredictor`. Its loader:

```python
model = model_cls.from_pretrained(self._require_model_dir(), **self._build_pretrained_model_kwargs())
torch_device = self._get_manual_torch_device()
if torch_device is not None:
    model = model.to(torch_device)                    # paddlex/…/predictors/transformers_predictor.py:88-94
model.eval()
```

This is *deserialize on CPU, then move to GPU* — **peak GPU allocation is 1× weights, not 2×**, at
the cost of host RAM. It also already wraps generation in `torch.inference_mode()` (`:202-203`) and
exposes `attn_implementation` as a config key (`:75-77`,
`paddlex/inference/models/engines/transformers.py:36`).

Two catches, both from source:

- `dtype` is only passed if `engine_config["dtype"]` is set (`transformers_predictor.py:78-80`).
  **There is no default.** What `from_pretrained` does with no dtype depends on the transformers
  version — v4 defaults to fp32 regardless of the checkpoint; v5 defaults to the checkpoint's dtype.
  The HF card requires `transformers>=5.0.0` (`hf:README.md:164`). **UNVERIFIED which applies to a
  given install — set `dtype: bfloat16` explicitly.**
- The HF card's own example is `from_pretrained(..., torch_dtype=torch.bfloat16).to(DEVICE)`
  (`hf:README.md:206`) — the same CPU-then-move pattern.

---

## 5. Silent CPU fallback — three of them, all disqualifying

### 5.1 Device selection falls back to CPU with no warning

```python
def get_default_device():                                 # paddlex/utils/device.py:55
    if is_dep_available("paddlepaddle"):
        paddle = import_paddle()
        if paddle.device.is_compiled_with_cuda() and paddle.device.cuda.device_count() > 0:
            return constr_device("gpu", [0])
        return "cpu"                                      # :63   ← no log, no warning
    ...
    return "cpu"                                          # :75   ← no log, no warning
```

`DEFAULT_DEVICE = None` (`PaddleOCR/paddleocr/_constants.py:15`), and
`PaddleOCR/paddleocr/_common_args.py:104-105` resolves `None` through `get_default_device()`. So the
out-of-the-box behaviour is a silent CPU fallback. It is *documented* — the CLI help string at
`_common_args.py:131,133` and the pipeline doc at
`PaddleOCR/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md:723` both say *"By default, GPU 0 will be
used if available; otherwise, the CPU will be used"* — but nothing is emitted at run time.

**Mitigation, and it is complete:** pass `device="gpu:0"` explicitly. `TemporaryDeviceChanger.__enter__`
then calls `paddle.device.set_device("gpu:0")` (`device.py:220`), which raises if there is no GPU. An
explicit device is loud; only the default is silent.

### 5.2 The dtype silently doubles on CPU

```python
if is_bfloat16_available(self.device):    # predictor.py:63
    self.dtype = "bfloat16"
else:
    self.dtype = "float32"                # :66
```

```python
def is_bfloat16_available(device):                        # paddlex/inference/utils/misc.py:27
    ...
    return ("npu" in get_device_type() or paddle_amp.is_bfloat16_supported()) and (
        device_type in ("gpu", "npu", "xpu", "mlu", "metax_gpu", "iluvatar_gpu"))   # :33-35
```

`"cpu"` is not in that tuple. **A CPU fallback therefore also silently selects fp32** — 3.571 GiB of
weights, doubled activations, and (via `_siglip.py:185`, `q.dtype == paddle.float32`) it *also*
forces eager attention. There is no fp16 option for this model on any path.

That compound is the most plausible reading of the incident that prompted this teardown: fp32 model
construction (958 M random values, 3.57 GiB), plus a second 3.57 GiB state dict, plus an fp32 eager
attention buffer, all on 8 CPU cores with no thread cap.

### 5.3 Flash-attention detection swallows every exception

```python
def is_flash_attn_available():                            # paddlex/…/flash_attn_utils.py:19
    try:
        ...
        q = paddle.rand((1, 4, 2, 8)).astype("bfloat16")
        _ = paddle.nn.functional.flash_attention.flash_attention(q, q, q, 0.9, False, False)
        return True
    except:                                               # :94   ← bare except, no log
        return False

HAS_FLASH_ATTN = is_flash_attn_available()                # :98   ← runs at import time
```

A bare `except:` returning `False`, evaluated at **module import**, which also allocates a tensor and
therefore initialises the CUDA context as a side effect of importing paddlex. Any failure —
missing kernel, wrong CUDA, transient OOM — silently degrades to the fp32 eager path with no
diagnostic. (For this model it is moot on the LM side, since `use_flash_attention: false` in the
config means `core_attn` runs regardless — §2.3.)

### 5.4 What *is* loud

OOM during inference is **not** silently caught. `_worker_vlm` catches and forwards, and the consumer
re-raises:

```python
raise RuntimeError(f"Exception from the '{item[1]}' worker: {item[2]}")   # pipeline.py:1179-1181
```

Loud, but **the original exception type is stringified** — you cannot `except` on Paddle's memory
error, only pattern-match the message. There is no OOM→CPU retry path anywhere in
`pipeline.py`, `predictor.py`, or `predictors/*.py`.

---

## 6. Quantization — the repo implements none

Searched `paddleocr/`, `deploy/paddleocr_vl_docker/`, `mcp_server/` for
`quantiz|quantize|int8|int4|wint8|weight_only|nf4|awq|gptq`. **Zero hits.**

| Path | Precision options available |
| --- | --- |
| Paddle native (default) | `bfloat16` or `float32`. That is the entire set (`predictor.py:63-66`) |
| `precision: fp32\|fp16` CLI flag | **Applies only to the TensorRT subgraph engine for the static Paddle models** — the layout and orientation models. `SUPPORTED_PRECISION_LIST = ["fp32", "fp16"]` (`PaddleOCR/paddleocr/_constants.py:21`); the help text says *"Precision for TensorRT"* (`_common_args.py:160-163`). It does not touch the VLM |
| transformers engine | Whatever you pass as `dtype`. No `BitsAndBytesConfig`, no `quantization_config` plumbing (`transformers_predictor.py:70-81`) |
| vLLM / SGLang / FastDeploy servers | The bundled configs set only `gpu-memory-utilization`, `max-model-len`, `max-num-seqs`, `workers`. No quantization key (`paddlex/inference/genai/configs/paddleocr_vl_09b.py:23-74`) |
| **llama.cpp server** | The only quantized route, and it is out-of-process |
| Static-graph quantization code | Present in the repo but for the **v2 CNN OCR models** (`test_tipc/test_ptq_inference_python.sh`), unrelated to the VLM |

`llama-cpp-server` is a first-class backend
(`PaddleOCR/paddleocr/_pipelines/paddleocr_vl.py:27-34`) and is documented with a working
`llama-server` invocation (`PaddleOCR/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md:1842-1856`).

**But the official GGUF is not a quantization.** `PaddlePaddle/PaddleOCR-VL-1.6-GGUF` contains:

```
PaddleOCR-VL-1.6-GGUF.gguf          935,769,056 B   (LM)
PaddleOCR-VL-1.6-GGUF-mmproj.gguf   881,770,560 B   (vision tower + projector)
                                  ─────────────
                                  1,817,539,616 B = 1.69 GiB
```

Dividing by the exact parameter counts from §1: `935,769,056 / 466,654,208 = 2.005 bytes/param` and
`881,770,560 / 491,934,528 = 1.79 bytes/param`. **That is F16, not a quant.** Baidu's "GGUF" release
is a format conversion — same footprint as bf16, ~100 MB saved. There is **no official INT8, W8A8,
INT4, AWQ or GPTQ release of this model in any form.**

Third-party quantized GGUFs do exist (`mradermacher/…-i1-GGUF`, `LunarOilRig/…-GGUF-Q4`,
`cstr/…`, `Mungert/…`, plus MLX 4/5/6/8-bit, ONNX, and OpenVINO INT4 conversions). **None publishes an
accuracy measurement.** HF search for `PaddleOCR-VL awq` and `PaddleOCR-VL int8` returns zero results.

Given the landscape review's own quantisation ladder — Q4_K_M at 15.64% CER vs BF16's 0.78% on a
*different* model, and 45% on dense text — going below 8-bit on an unmeasured third-party conversion
of a model whose *vision half* would also be quantized is not a defensible move. And the arithmetic in
§2.4 says you do not need to: bf16 fits.

---

## 7. Input contract, and whether it composes with `ink.py`

### 7.1 It is a two-model pipeline, and the docs are emphatic about it

> *"the first stage is layout analysis: the model takes the entire image as input, detects and
> localizes various layout elements … and **crops the corresponding element-level sub-images** based on
> the detection results. The second stage is VLM-based recognition: **each sub-image is independently
> fed into the VLM** … Therefore, **to fully leverage the capabilities of PaddleOCR-VL, it is necessary
> to adopt the complete pipeline** … rather than using the VLM component alone."*
> — `PaddleOCR/docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md:20`

and, directly relevant to the hallucination hazard already recorded in the landscape review:

> *"If issues arise during usage — such as failure to reproduce the performance reported in the paper
> …, or the **generation of excessive hallucinated text** — the first step is to verify whether the
> complete PaddleOCR-VL pipeline is being used, rather than only the VLM component."*
> — same file, `:24`

Default v1.6 pipeline (`paddlex/configs/pipelines/PaddleOCR-VL-1.6.yaml`):

```yaml
batch_size: 64                  # pages per batch — see §4.4
use_queues: True
use_doc_preprocessor: False      # orientation + unwarping off by default
use_layout_detection: True
use_chart_recognition: False
use_seal_recognition: False
merge_layout_blocks: True
SubModules:
  LayoutDetection:  { model_name: PP-DocLayoutV3, threshold: 0.3, layout_nms: True,
                      layout_unclip_ratio: [1.0, 1.0] }
  VLRecognition:    { model_name: PaddleOCR-VL-1.6-0.9B, batch_size: -1,
                      genai_config: { backend: native } }
```

Note `layout_unclip_ratio: [1.0, 1.0]` — **crops get no padding by default**, and the layout model is
`PP-DocLayoutV3` (V2 for the v1 pipeline; both accepted, `pipeline.py:117-120`).

The layout model is RT-DETR-L plus a 6-layer pointer network that recovers **reading order** as an
N×N pairwise-order matrix (`PaddleOCR/docs/version3.x/module_usage/layout_analysis.en.md:25,37`), over
**25 classes**. Per crop, the class picks the prompt and the pixel budget
(`pipeline.py:288-355`):

| Block label | Prompt | Extra handling |
| --- | --- | --- |
| default | `OCR:` | — |
| `table` | `Table Recognition:` | embedded figures tokenised out first |
| `chart` | `Chart Recognition:` | only if `use_chart_recognition` |
| `*formula*` (not `formula_number`) | `Formula Recognition:` | **`crop_margin()` applied first** (`:328-331`) |
| `spotting` | `Spotting:` | `pre_process_for_spotting()`, budget raised to 1,605,632 |
| `seal` | `Seal Recognition:` | only if `use_seal_recognition` |
| anything in `image_labels` | — | **skipped entirely** — no VLM call (`:302-305`) |

Generation is greedy and deterministic on the local path: `generation_config.json` sets no sampling
params, and `repetition_penalty` / `temperature` / `top_p` are **explicitly rejected with a warning**
by the local predictor (`predictor.py:229-243`) — they only work against a server backend.
`max_new_tokens` is 4,096 in the pipeline (`pipeline.py:505`), 8,192 at the predictor default
(`constants.py:35`).

### 7.2 Composition with `ink.py`

`src/ocr_handler/ink.py` and PaddleOCR-VL's stage 1 solve the *same shape of problem on different
signals*:

| | `ink.py` | PP-DocLayoutV2/V3 |
| --- | --- | --- |
| Signal | **ink** — red-channel threshold (`ink.py:54-59`) or base/annotated diff (`:67-77`) | **content** — RT-DETR over the rendered page |
| Grouping | binary dilation at `merge_px=64`, swept on a real 200 dpi page (`:80-110`) | NMS + `layout_merge_bboxes_mode` per class |
| Reading order | vertical-overlap banding, then left-to-right (`:112-143`) | learned pointer network, N×N order matrix |
| Output | untyped boxes + pixel counts | 25 semantic classes + order |
| Padding | `pad=12` px (`:145-155`) | `layout_unclip_ratio: [1.0, 1.0]` — none |

They are **complementary, not redundant** — but only one of them can drive the crop, and running both
duplicates work and disagrees about boundaries.

Two ways to compose, both supported:

**(a) Feed `ink.py` crops directly, `use_layout_detection=False`.** Then you must supply
`prompt_label`, and the pipeline asserts it is one of `['ocr', 'formula', 'table', 'chart']`
(`pipeline.py:855-868`; `'chart'`/`'seal'` additionally require their feature flags). You keep your own
reading order, you skip loading the layout model entirely (**−0.2 GiB VRAM and one fewer model to
load during the 3.57 GiB spike**), and every crop is ink-only — which is exactly what the
un-annotated-twin control protocol needs. The cost is the vendor's explicit warning at `:24` that
VLM-only usage is where the hallucination reports come from.

**(b) Run the full pipeline and use `ink.py` as a gate.** Layout drives the crops; `ink.py`'s pixel
count decides which of the resulting boxes actually contain annotation. This directly implements the
landscape review's §5 recommendation ("add a blank-region guard") and keeps the vendor-blessed path.

**One concrete interaction worth knowing:** `smart_resize` upscales anything under `min_pixels =
112,896` (`hf:image_processing_paddleocr_vl.py:169-172`). A typical `ink.py` equation crop —
say 800 × 150 = 120,000 px — sits right at that boundary; the 480 × 140 = 67,200 px crop from the
prior session's fixture work would be **bicubically upscaled ~1.3× before the model sees it**. That
is probably helpful for thin handwritten strokes, and it is definitely not what a naive reading of
"feed it a crop" would predict. Worth measuring rather than assuming.

---

## 8. Licence — code and weights, stated separately

| Artifact | Licence | Evidence |
| --- | --- | --- |
| **Code** — `PaddlePaddle/PaddleOCR` | **Apache-2.0** | `PaddleOCR/LICENSE` (11,376 B, stock Apache 2.0); `PaddleOCR/pyproject.toml:37` — `license = {text = "Apache License 2.0"}`; every source header carries the Apache notice |
| **Code** — `PaddlePaddle/PaddleX` (the actual implementation) | **Apache-2.0** | Apache header on every file fetched, e.g. `paddlex/utils/device.py:1-13` |
| **Weights** — `PaddlePaddle/PaddleOCR-VL-1.6` | **Apache-2.0** | HF API `cardData.license: apache-2.0`; README frontmatter `license: apache-2.0`; `LICENSE` in the weights repo is stock Apache 2.0 text, appendix `Copyright (c) 2025 PaddlePaddle Authors` |
| **Weights** — `PaddlePaddle/PaddleOCR-VL-1.6-GGUF` | **Apache-2.0** | README frontmatter `license: apache-2.0` |
| **Layout model** — `PaddlePaddle/PP-DocLayoutV2` / V3 | **UNVERIFIED** — separate HF repo, licence not checked in this pass | linked from `layout_analysis.en.md:71` |

No RAIL clause, no non-commercial rider, no upstream-base trap of the kind found on Uni-MuMER. The
vision tower is SigLIP-shaped and the LM is ERNIE-4.5-0.3B-derived; both upstreams are Apache-2.0.
**The last item is the only open one and it matters — the pipeline does not run without the layout
model.**

---

## 9. Where this contradicts the landscape review

| `engine-landscape-2026-09.md` | This document | Stronger evidence |
| --- | --- | --- |
| §5 / §7: *"The 8 GB figure … is FastDeploy's serving recommendation, not a transformers single-image floor"* | **Correct, and it under-sells the case.** But the review missed the vendor's *actual* stated floor: PaddleOCR issue #16823, the pinned maintainer FAQ, says *"the minimum supported configuration that successfully runs is an RTX 3060 (12 GB)"* | **This document.** The review defended PaddleOCR-VL against a number that was not the vendor's floor, while a worse vendor number existed unquoted. The 12 GB figure is nonetheless *also* wrong for our case — it is stated for the paddle dynamic-graph path, whose instability the same FAQ concedes |
| §5: *"A user … reported 45 GB → 3.3 GB … purely by passing `attn_implementation="flash_attention_2"` and wrapping in `torch.inference_mode()`"* | **The flash-attn half is right and now has a mechanism. The `inference_mode` half is wrong.** `generate()` is already `@torch.no_grad()`; a 2×2 ablation in the same discussion shows inference_mode moving VRAM by 0.02 GB. Also: **sdpa gets you 95% of flash-attn's saving** (2.95 GB vs 2.84 GB in that ablation), so flash-attn-2 is not a prerequisite | **This document.** `hf:modeling_paddleocr_vl.py:1043,1089-1140` + `_siglip.py:146-203` give the mechanism; the OOM allocation sizes reproduce as `16·N²·4` to four significant figures |
| §5: *"UNVERIFIED on this machine — measure it before committing"* | **Still true, but the thing to measure has changed.** Steady-state inference is not the risk; **`from_pretrained` is**, at ~2× weights on-device (`model_utils.py:1781-1807`, `:212-215`, `:266`, `:306-309`). A measurement that only samples `nvidia-smi` after warm-up will miss it | **This document.** The review framed VRAM as an inference question. The source says the peak is at load |
| §8: *"PaddleOCR-VL is a two-model pipeline … More moving parts, more VRAM"* | **Right, and quantifiable: ~0.2 GiB for PP-DocLayoutV2, loaded first and therefore resident during the 3.57 GiB load spike.** But it is also *skippable* — `use_layout_detection=False` is supported and is exactly the shape that composes with `ink.py` (§7.2) | **Both.** The review's concern is real; the source shows the escape hatch and its cost (the vendor's hallucination warning at `PaddleOCR-VL.en.md:24`) |
| §8: *"Its handwriting evidence is thinner than it looks … Its HF model card makes no handwriting claim at all"* | **Confirmed** — the 1.6 model card's Performance section is OmniDocBench + Real5-OmniDocBench only. No handwriting dimension | **Both agree.** Nothing here changes it |
| §1.7 table: *"PaddleOCR-VL (raw transformers) — 273 s/page"* | **Now explained, not just observed.** The LM runs `core_attn` unconditionally (`use_flash_attention: false` in config, never overridden — `_ernie.py:657-667`), and re-expands the entire GQA KV cache from 2 heads to 16 on **every decode step** (`_ernie.py:861-862`) | **This document** supplies the mechanism the review only had a number for |
| §5: *"Recommendation: PaddleOCR-VL-1.6 … as the page engine"* | **Not overturned. Materially strengthened on fit, materially complicated on operation.** Apache-2.0 on both code and weights is now confirmed from LICENSE files rather than badges; the memory arithmetic now closes; but three silent degradations (§5) and a default 64-page prefetch queue (§4.4) mean it needs configuring, not just installing | **Unchanged verdict, better grounded** |

---

## 10. What is still UNVERIFIED, and what would settle it

Ordered by how much the answer would move the decision.

1. **Paddle's CUDA context + workspace overhead on this card.** The 0.3–0.8 GiB band in §2.4 is a
   guess, and it is the difference between the load peak fitting and not.
   *Settles it:* `import paddle; paddle.set_device("gpu:0"); paddle.zeros([1])` then read
   `nvidia-smi` — no model, no weights, seconds.
2. **Whether the ~3.57 GiB load peak actually materialises.** The source says both copies are live;
   the allocator's `auto_growth` strategy might partly hide it.
   *Settles it:* run `from_pretrained` alone with `nvidia-smi --query-gpu=memory.used
   --format=csv -l 1` logging in a second terminal, and **kill it at the peak** — you do not need to
   run inference to answer this.
3. **`PP-DocLayoutV3`'s size and licence.** V2 is 203.8 MB and its licence was not checked. V3 has no
   published size in the clone. *Settles it:* the HF repo file listing + LICENSE, no download.
4. **What `dtype=None` means for the installed transformers.** v4 → fp32 (disaster); v5 → bf16.
   *Settles it:* `python -c "import transformers; print(transformers.__version__)"`.
   Or simply always pass `dtype` explicitly, which is the right move regardless.
5. **Whether PaddleX actually routes `PaddleOCR-VL-1.6-0.9B` to `DocVLMTransformersPredictor` when
   `engine="transformers"`.** The engine advertises `("safetensors",)` and the HF repo ships
   `model.safetensors`, so it should — but the dispatch table was not read.
6. **Whether SDPA is genuinely selected on this card at run time.** The gate at `_siglip.py:146-156`
   should pass for CC 8.6 on Linux, but `get_gpu_compute_capability()` and
   `get_paddle_cuda_version()` were not read. *Settles it:* a two-line check of those two functions'
   return values — no model needed.
7. **The transformers/paddle path on a 6 GB card, first-hand.** No such report exists anywhere. The
   only verified 6 GB success is llama.cpp + GGUF on an RTX 3050 (`ggml-org/llama.cpp#25339`).

### A safe first experiment

If and when someone runs this, the configuration the source argues for:

```
device="gpu:0"                    # explicit — kills the silent CPU fallback (§5.1) and the fp32 one (§5.2)
use_layout_detection=False        # −0.2 GiB, and lets ink.py drive the crops (§7.2)
prompt_label="formula" | "ocr"    # required when layout is off (pipeline.py:855-868)
max_pixels=1003520 or lower       # the dominant knob (§2.1)
use_queues=False                  # kills the 64×64-page prefetch ramp (§4.4)
batch_size=1
```

and, separately, the same page through `--vl_rec_backend llama-cpp-server` against the official
F16 GGUF, which is the only configuration anyone has confirmed on 6 GB.

Watch `nvidia-smi` **during load**, not after. That is where the source says it breaks.

---

## Sources

**Read locally (the clone, commit `2661c7c`, 2026-07-22)**
- `paddleocr/_pipelines/paddleocr_vl.py`, `paddleocr/_models/_doc_vlm.py`, `paddleocr/_common_args.py`,
  `paddleocr/_constants.py`, `paddleocr/_env.py`, `pyproject.toml`, `LICENSE`
- `docs/version3.x/pipeline_usage/PaddleOCR-VL.en.md` (3,369 lines),
  `docs/version3.x/algorithm/PaddleOCR-VL/PaddleOCR-VL-1.6.en.md`,
  `docs/version3.x/module_usage/layout_analysis.en.md`
- `deploy/paddleocr_vl_docker/pipeline_config_{vllm,fastdeploy}.yaml`,
  `mcp_server/paddleocr_mcp/inference/paddleocr_vl/local.py`

**Fetched read-only — PaddleX v3.7.2** (`raw.githubusercontent.com/PaddlePaddle/PaddleX/v3.7.2/`)
- `paddlex/utils/{device,download,env,flags}.py`
- `paddlex/inference/models/doc_vlm/{predictor,constants,utils}.py`
- `paddlex/inference/models/doc_vlm/modeling/paddleocr_vl/{_config,_paddleocr_vl,_siglip,_ernie,_projector}.py`
- `paddlex/inference/models/doc_vlm/processors/paddleocr_vl/_paddleocr_vl.py`
- `paddlex/inference/models/common/transformers/transformers/model_utils.py`,
  `.../{flash_attn_utils,fusion_ops}.py`, `.../generation/utils.py`
- `paddlex/inference/models/predictors/{base,local_model,transformers}_predictor.py`,
  `paddlex/inference/models/engines/{_base,paddle,transformers}.py`,
  `paddlex/inference/utils/misc.py`, `paddlex/inference/models/common/genai.py`
- `paddlex/inference/pipelines/paddleocr_vl/pipeline.py`,
  `paddlex/inference/genai/configs/paddleocr_vl_{09b,15_09b,16_09b}.py`,
  `paddlex/configs/pipelines/PaddleOCR-VL-1.6.yaml`,
  `paddlex/configs/modules/doc_vlm/PaddleOCR-VL-0.9B.yaml`
- `_siglip.py` additionally fetched at tags **v3.3.0, v3.3.5, v3.3.13, v3.4.0, v3.5.0, v3.6.0, v3.7.0**
  to date the SDPA gate

**Fetched read-only — `huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6`**
- `config.json`, `preprocessor_config.json`, `generation_config.json`, `inference.yml`,
  `processor_config.json`, `chat_template.jinja`, `README.md`, `LICENSE`
- `modeling_paddleocr_vl.py` (103,889 B), `configuration_paddleocr_vl.py`,
  `image_processing_paddleocr_vl.py`, `processing_paddleocr_vl.py`
- `model.safetensors` **header only** — HTTP range `bytes=0-7` then `bytes=8-78495`, 78,488 B of JSON.
  No tensor data transferred.
- Same file set diffed against `PaddleOCR-VL` and `PaddleOCR-VL-1.5`
- File listings + sizes + licence via `huggingface.co/api/models/…/tree/main`, incl.
  `PaddlePaddle/PaddleOCR-VL-1.6-GGUF`

**Web, secondary**
- `huggingface.co/PaddlePaddle/PaddleOCR-VL/discussions/{33,38,47,59}`
- `github.com/PaddlePaddle/PaddleOCR/issues/{16788,16823,16852,17064,17371}`
- `github.com/ggml-org/llama.cpp/issues/25339`
- `paddlepaddle.github.io/FastDeploy/best_practices/PaddleOCR-VL-0.9B/`

**Not done, deliberately:** no weights downloaded, no inference, no GPU access, no framework
installed, no builds, no test suites, no git mutations in `electrical_notes`.

---

**See:** [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) · [`INDEX.md`](INDEX.md) ·
[`../scope.md`](../scope.md)
