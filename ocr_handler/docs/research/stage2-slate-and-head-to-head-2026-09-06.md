# Stage 2 — the candidate slate for the RTX 5000, and the head-to-head protocol

**Date:** 2026-09-06. Closes the *slate* and the *protocol* halves of
[ADR-0004](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md). It does **not**
choose the engine — that is an operator call, and the point of ADR-0004 is that it is settled by
measurement rather than by a third argued verdict.

**Nothing was executed.** No model, no GPU, no ollama, no install. Every number below is either
(a) a prior measurement from this repo, cited to its file, (b) read out of a primary source today —
safetensors manifests via the HF API, upstream source via `raw.githubusercontent.com` — or (c)
arithmetic, **which is labelled as arithmetic**, because this project has already caught one
GPU-recommender page whose VRAM table was arithmetic on a parameter count and was wrong for
exactly that reason.

> **What changed since the incumbent research.** Every VRAM figure in
> [`equation-ocr-specialists.md`](equation-ocr-specialists.md),
> [`paddleocr-vl-teardown.md`](paddleocr-vl-teardown.md) and
> [`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) was taken on a **6 GB RTX 3060
> Laptop (Ampere, sm_86)**. The deployment target is the **skytracker Quadro RTX 5000**. Those
> documents are **not edited**; where this one contradicts them, [§7](#7-inherited-claims-that-changed-or-failed)
> says so.

---

## Verdict up front

| # | Question | Answer |
| --- | --- | --- |
| 1 | Does the bigger card unblock the incumbent's binding constraint? | **Yes — and it replaces it with a different, larger one.** PaddleOCR-VL's ~2× -weights load spike is a **PaddlePaddle** defect and it stops mattering at 16 GB. But the target is **Turing (sm_75)**, and PaddleX gates *both* bf16 **and** SDPA at compute capability **≥ 8.0** — verified in source today. On the Paddle path the model therefore runs **fp32 with eager O(N²) attention** |
| 2 | Is there an escape from that? | **Yes, and it is one line.** The HF weights ship a **torch** implementation whose `_supports_sdpa = True` carries **no capability gate**. `dtype=float16, attn_implementation="sdpa"` via `trust_remote_code` sidesteps the whole problem |
| 3 | Is Uni-MuMER in? | **Yes — `Uni-MuMER-Qwen3-VL-2B`, and not the 3B.** 3.963 GiB of weights, Apache-2.0 base *and* derivative (both verified today). Its class is stock `Qwen3VLForConditionalGeneration`, so **no serving stack is required** — the inherited objection is wrong. The real cost is `transformers ≥ 5`, which this project does not run |
| 4 | Are sub-5B models any good here? | **They are the entire open field, and the big ones are worse.** UniMERNet-**B** is 325M and scores UniMER-Test HWE 0.94 CDM; Qwen2.5-VL-**72B** scores 0.863 on the same subset. Size is not the axis |
| 5 | What settles the head-to-head? | **Ground truth, not the validity gate.** `ocr-handler check` is a *screen* — it proves a reading is degenerate, never that it is right. §7.4(b) of [the repair plan](../plans/latex-repair-and-validity.md) is the standing proof |
| 6 | Biggest unknown? | **Whether the mask trick survives.** The best of 84 measured outputs came from `ink.py`'s binary mask — which needs separable ink. **Two thirds of this corpus's handwriting has none** |

**The one command that must run first** (no model, no GPU load, ~0 s), on skytracker:

```sh
nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv
```

It settles §1 and §2's entire premise. Everything below is written so that a `compute_cap` of
`8.x` invalidates §2 loudly rather than silently.

---

## 1. The target card — what the evidence actually supports

No first-party measurement of this GPU exists in any repo on this machine. What exists:

| Claim | Source | Rank |
| --- | --- | --- |
| **Quadro RTX 5000, 16 GB VRAM, 3072 CUDA cores** | `skytracker_algo/docs/detection-roadmap.md:77`, `.../archive/gpu-batch-inference.md:13` | Named part + two independent specs |
| 16 GB, corroborated | `postproc/docs/scope.md:184`, `postproc/docs/ARCHITECTURE.md:390`, `yolo_retraining/docs/scope.md:29,147`, `yolo_retraining/docs/ARCHITECTURE.md:20` | Five more docs |
| 16 GB, corroborated **by a budget that only works at 16** | `postproc/docs/findings/gpu-inference-service.md:17` — *"3 × 2.3 GB … on the Quadro RTX 5000 (16 GB), this leaves little room for the `./live/` Rust daemon (1.2 GB)"* | Strongest: an arithmetic that would be nonsense at 24 GB |
| **"Quadro RTX 5000 (24GB)"**, *"Available for next image: 20.9 GB"* | `postproc/docs/findings/SAHI-INTEGRATION.md:313,350` | ⚠ **FAILS** — see [§7](#7-inherited-claims-that-changed-or-failed) |

**Part identification is unambiguous.** 16 GB **and** 3072 CUDA cores is the Quadro RTX 5000
(TU104) and nothing else: RTX A5000 is 8192 cores / 24 GB (sm_86), RTX 5000 Ada is 12800 cores /
32 GB (sm_89). TU104 is **Turing, compute capability 7.5**.

> ⚠ **UNVERIFIED on the target: the compute capability.** The three "Compute Capability 7.5
> (Turing)" lines in `yolo_retraining/` belong to an **RTX 2060** on a different host, not to
> skytracker. The 7.5 above is inferred from the part number, not read off the card. It is a
> strong inference — but this project's own rule is that a spec-sheet inference is not a
> measurement, and the command in the verdict box settles it in one line.

**Free VRAM is not 16 GB.** The GPU is shared with a continuous YOLO watcher and a Rust live
daemon. Per `gpu-inference-service.md`, the two live states are:

| State | Resident | Free (of ~16 GB) |
| --- | ---: | ---: |
| Centralised inference service deployed (1 × YOLO + live) | ~3.5 GB | **~12.5 GB** |
| Not deployed (3 × YOLO + live) | ~8.1 GB | **~7.9 GB** |

That document is marked *"Implemented, pending deployment"* as of 2026-03-06 and nothing here
knows which state is current. **Plan against ~7.9 GB; verify with
`nvidia-smi --query-compute-apps=pid,used_memory --format=csv`.**
[`gpu-discipline.md`](../directives/gpu-discipline.md) applies unchanged: the box is not idle,
and its lesson — *"it's on the GPU" describes the compute, not the load* — is if anything
sharper on a 52-core shared server than it was here.

---

## 2. What Turing changes, verified in source

This is the finding the 6 GB work could not have made, because it never ran on sm_75.

### 2.1 PaddleX gates bf16 at capability ≥ 80

`paddlex/inference/models/doc_vlm/predictor.py` (v3.7.2, fetched today):

```python
if is_bfloat16_available(self.device):
    self.dtype = "bfloat16"
else:
    self.dtype = "float32"
```

`paddlex/inference/utils/misc.py:27-35` routes that to `paddle.amp.is_bfloat16_supported()`,
which is `core.is_bfloat16_supported(place)`, which is C++
(`paddle/fluid/pybind/place.cc:492-499`, fetched today):

```cpp
m.def("is_bfloat16_supported", [](const GPUPlace &place) -> bool {
// Only GPUs with Compute Capability >= 80 support bfloat16
  return platform::GetGPUComputeCapability(place.device) >= 80;
});
```

**75 < 80. On the Quadro RTX 5000 the Paddle path selects `float32`** — 3.571 GiB of weights
instead of 1.786 GiB, and every activation doubled.

### 2.2 PaddleX also gates SDPA at capability ≥ 80 — explicitly

`paddlex/…/paddleocr_vl/_siglip.py:144-158`, fetched today:

```python
cap = get_gpu_compute_capability()
self._supports_sdpa = False
if (cap is not None and cap >= (8, 0) and cuda_ver >= (11, 4)
        and platform.system() == "Linux"):
    self._supports_sdpa = True
```

and `:185` — `if not self._supports_sdpa or q.dtype == paddle.float32:` → `eager_attention_forward`.

**Both arms fire on Turing.** So the vision tower runs the dense fp32 `16·N²·4`-byte softmax that
[`paddleocr-vl-teardown.md`](paddleocr-vl-teardown.md) §2.2 identified as the source of every
reported OOM. That teardown's own table, applied to the target:

| Input | N (raw patches) | one fp32 buffer | realistic peak |
| --- | ---: | ---: | ---: |
| an `ink.py` equation crop (upscaled to `min_pixels`) | 576 | 20 MiB | **~50 MiB** |
| a mid-size block | 2,048 | 256 MiB | ~0.6 GiB |
| a **full page** at the 1.6 default `max_pixels` | 5,120 | 1.56 GiB | **~3.1–3.9 GiB** |

> **The mitigation is already the architecture.** `ocr_handler` does not hand a page to a model;
> `ink.py` hands it one equation. At crop scale the quadratic term is 50 MiB and the eager path
> is irrelevant. **The Turing penalty is a full-page problem, and we do not have a full-page
> problem** — which is the same reason `mineru-teardown.md`'s 36.56 was the wrong column.

### 2.3 The torch implementation has no such gate

`huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/modeling_paddleocr_vl.py` (2,487 lines, fetched
today) declares `_supports_flash_attn = True` and `_supports_sdpa = True` at `:530` and `:1266-1267`,
selects at `:1089-1140`, and **nowhere queries the compute capability**. torch's SDPA
memory-efficient backend runs on sm_75. So:

```python
# the Turing-safe path
AutoModelForImageTextToText.from_pretrained(
    "PaddlePaddle/PaddleOCR-VL-1.6", trust_remote_code=True,
    dtype=torch.float16, attn_implementation="sdpa",
).to("cuda:0")
```

fp16 weights (1.786 GiB), O(N) attention, and — per the same teardown at `:425` — a torch
`from_pretrained` peak of **1× weights, not 2×**.

### 2.4 What is *not* available on Turing, and where it bites

Verified against flash-attention's own README today: *"Ampere, Ada, or Hopper GPUs… For Turing
GPUs (T4, RTX 2080), see the separate `flash-attention-turing` repo"* and *"bf16 requires
Ampere, Ada, or Hopper."*

- **No FlashAttention-2.** SDPA gets ~95% of its saving anyway (2.95 GB vs 2.84 GB in the
  ablation the teardown reproduces), so this costs almost nothing here.
- **No TF32, no bf16 tensor cores, no FP8.** fp16 tensor cores *are* present (Turing's headline
  feature). **The rule for this card is: load everything as fp16, never bf16.**
- Every model on the slate ships `dtype: bfloat16` in `config.json`. **Each one must be loaded
  with an explicit `dtype=torch.float16`**, or torch will honour the config and run a bf16 path
  that is emulated and slow. This is a one-line change per engine and a silent 2–5× if forgotten.

---

## 3. The slate

Weight bytes are read from the HF API `?blobs=true` manifest. "Alloc/reserved" figures marked
**measured** are this repo's, on the 6 GB card — they are architecture-level and transfer;
"est." figures are arithmetic and are marked as such.

### 3.1 In the head-to-head

| # | Candidate | Weights (bytes → GiB) | Peak on the RTX 5000 | Licence (verified today) | Why it is in |
| --- | --- | ---: | --- | --- | --- |
| **A** | **UniMERNet-Base** fp16 `wanderkid/unimernet_base` | 1,300,760,949 → 1.211 (fp32 on disk) | **686 MiB alloc / 1290 MiB reserved — measured** | Apache-2.0 | The incumbent. The control arm |
| **B** | **UniMERNet-Base-2501** `opendatalab/PDF-Extract-Kit-1.0` | 1,300,749,558 → 1.211 | **identical to A** — same architecture, 11 KB smaller | ⚠ **repo has no licence tag** | **A Jan-2025 retrain of the exact checkpoint we measured, and nobody here had noticed it.** Zero VRAM cost to try |
| **C** | **UniMERNet-small-2503** `…/unimernet_hf_small_2503` | 810,036,696 → 0.754 | ~450 MiB alloc / ~900 MiB reserved *(est., size ratio)* | ⚠ **no licence tag** | **MinerU 3.4.5's actual shipping default.** We measured Base and Tiny and never this |
| **D** | **PaddleOCR-VL-1.6, torch path** fp16 + sdpa | 1,917,177,472 → **1.786** | **1767 MiB alloc / 1786 MiB reserved — measured**; load 1× weights | Apache-2.0 code **and** weights | The challenger that read `expo` **exactly right** where A failed at every padding and every DPI |
| **E** | **Uni-MuMER-Qwen3-VL-2B** fp16 `phxember/Uni-MuMER-Qwen3-VL-2B` | 4,255,140,312 → **3.963** | ~4.0 GiB weights + KV + vision; **est. 4.5–6.0 GiB** on crop-sized input | Apache-2.0, base `Qwen/Qwen3-VL-2B-Instruct` **also Apache-2.0** | The only purpose-built HMER model with clean weights, a clean base, and a **stock transformers class** |

**On E, the correction that puts it in the slate.** `engine-landscape-2026-09.md` listed
`Uni-MuMER-Qwen3.5-2B` first and `equation-ocr-specialists.md` §2.6 rejected the family because
*"2.2B fp16 ≈ 4.4 GB against 4.3 GB of headroom, and the repo's inference path is
`scripts/vllm_infer.py`."* Both halves are now wrong: 3.963 GiB is unremarkable at 16 GB, and
`config.json` declares `Qwen3VLForConditionalGeneration` — a class transformers ships, so vLLM is
the repo's convenience, not a requirement. **Prefer the Qwen3-VL variant over the Qwen3.5 one**:
`Uni-MuMER-Qwen3.5-2B` is a hybrid model (18 of 24 layers `linear_attention`,
`mamba_ssm_dtype: float32`) whose kernels are the least likely thing on this slate to have a
working sm_75 path, and it buys **0.6 ExpRate points** (73.09 vs 72.49) for that risk.

**The dependency cost of E, stated plainly.** Both 2B configs declare
`transformers_version: 5.2.0`. This project runs **4.52.3**, on which the vendored UniMERNet path
is verified working, and on which `handwriting-ocr-systems.md` §3.2 recorded that transformers 5
*breaks* TrOCR. **Arm E is the only one that costs a framework upgrade**, and that is a scope
question, not a benchmark result.

### 3.2 Adjacent, and why each is not in round one

| Candidate | Weights | Status on this card | Blocker |
| --- | ---: | --- | --- |
| **UniMERNet-Tiny** | 430,075,701 (0.401 GiB) | 232/478 MiB **measured** | Not excluded — **carry it as a free second opinion**, it beat Base on `cos_only` |
| **PaddleOCR-VL-1.6, Paddle path** | 3.571 GiB **as fp32 on Turing** | load ≈ 7.1–8.1 GiB, steady 4.0–4.6 GiB on crops | Not a blocker, a **price**. Run it once to measure the fp32/eager penalty, then use the torch path |
| **GLM-OCR** `zai-org/GLM-OCR` | 2,650,579,464 (**2.469 GiB**) | fits easily | `model_type: glm_ocr`, `transformers_version: 5.0.1dev0`, **no `.py` files and no `custom_code` tag** → needs native transformers-5 support. Cheap to check, not cheap to assume |
| **PP-FormulaNet_plus-M** via MinerU's torch code | `PP-FormulaNet_plus-M.pth` 617,338,934 (0.575 GiB) | trivial | ⚠ weights live in `opendatalab/PDF-Extract-Kit-1.0`, **`cardData.license` is null** |
| **Texo** `alephpi/FormulaNet` | 80,238,928 safetensors; **ONNX encoder 54 MB + decoder 26 MB** | trivial; the ONNX pair needs **no torch at all** | **AGPL-3.0** — operator call. Also *loses* to UniMERNet-Tiny on HWE (0.902 vs 0.9328) |
| **dots.mocr** `dots-studio/dots.mocr` | 6,078,431,736 = **5,797 MiB** (matches the teardown exactly) | **fits — the VRAM exclusion is void on this card** | The `dots.mocr LICENSE AGREEMENT` §3.3(c) bars *"unauthorized digitization of publications/document scanning."* Hardware-independent, and now the **only** reason it is out |
| **Uni-MuMER-Qwen2.5-VL-3B** | 8,131,668,008 (7.573 GiB) | fits | Base `Qwen/Qwen2.5-VL-3B-Instruct` licence is **`qwen-research`, non-commercial** — confirmed today. Also *scores lower* than both 2Bs |
| **Uni-MuMER-Qwen3.5-4B / Qwen3-VL-4B** | 8.455 / — GiB | fits | Same transformers-5 cost, larger, unmeasured. Escalate only if the 2B wins |

### 3.3 Excluded, and the exclusion is not about VRAM

`GryphOne` (2602.03370) and `InkFM` (2503.23081) both surfaced from ResearchHub and both have
**zero HuggingFace hits and no source repository** — searched today. The UniMERNet **CVPR-2026**
redesign is still unreleased: GitHub releases stop at **0.2.3 (2024-12-26)** and
`wanderkid/unimernet_base` `lastModified` is **2024-09-13**. `PaddlePaddle/PP-FormulaNet_plus-L_onnx`
**exists and is empty** — a 28-byte README, zero downloads. TrOCR, the classical HTR family,
pix2tex, texify/surya, TexTeller and the CROHME specialists are excluded by
[`handwriting-ocr-systems.md`](handwriting-ocr-systems.md) and
[`equation-ocr-specialists.md`](equation-ocr-specialists.md) on grounds the card does not touch.

### 3.4 The operator's sub-5B question, answered from the record

**Every open model that is any good at this is under 5B, and the large ones are worse on the
subset that matters.** UniMER-Test HWE, in CDM:

| Model | Params | HWE CDM | Table it comes from |
| --- | ---: | ---: | --- |
| **UniMERNet-Base** | **0.325B** | **0.94** | CDM paper `2409.03643` Table 4 (released checkpoints) |
| PaddleOCR-VL | 0.9B | 0.9445 | MinerU2.5-Pro `2604.04771` Table 5 |
| GLM-OCR | 0.9B | 0.9510 | same |
| Qwen3-VL-235B | 235B | 0.9423 | same |
| Qwen2.5-VL-72B | 72B | **0.863** | UniMERNet CVPR-2026 table (a **different** evaluation) |

⚠ **Provenance is not uniform and the last row is from a different table** — the same warning
`equation-ocr-specialists.md` § 2.1 attaches to its own comparison, repeated here rather than
quietly dropped. It does not change the ranking: the 72B row is 8 points below a 325M model on
*any* of these tables, and the 235B row is within 0.2 of it on the *same* table.

A 325M specialist beats a 72B generalist by 8 points, and is within 0.2 of a 235B one. The
~20B ceiling the operator set is not binding on this problem; **nothing worth running is near
it.** The reason is in `handwriting-ocr-systems.md` §4: WildHandBench traces 87–98% of model
formula errors to a **language prior overriding the pixels**, and a bigger prior is a bigger
version of that failure — TrOCR reading `\sin` as the word *"simultaneously"* is the same
mechanism at 558M.

---

## 4. The head-to-head protocol

### 4.1 Pages — three strata, because there are three shapes of handwriting

n=2 equations on one page is what every current conclusion rests on. The corpus supports far
better, and the strata are not interchangeable:

| | Source | Pages | Ink separable? | Twin control? |
| --- | --- | ---: | --- | --- |
| **P1** | `cesc_410/lectures/f26_lctr02_DT signals and systems-plw.pdf` + `dsp-lctr1-analog-signal-in-td-n-fd-26-08-26-plw.pdf` | 10 + 12 | **yes** — coloured ink, `red_mask` | **yes** — both have an un-annotated twin |
| **P2** | `cesc_410/lectures/f26_lctr03_LTI_systems_conv.pdf` — a OneNote export, dark ink on graph paper | 8 | `dark_mask` only | **no** |
| **P3** | `ps160/midterm_01/Worked Problems.pdf` — flatbed scan, **blue** handwriting over print | (labelled idx 129, 130) | neither `red_mask` nor a twin | **no** |

P2 and P3 are labelled `handwritten-math` / `scan-handwritten-math`, `math_state: absent` in
[`../findings/ground-truth-sample.md`](../findings/ground-truth-sample.md) (rows 96, 97, 98, 129,
130). **Neither has ever been fed to a model in this project.** Including them is the whole point:
P1 is where the mask trick works and it is *two documents*; P2 and P3 are where the answer has to
generalise.

### 4.2 Crops — 24, and how they are cut

**24 equation crops: 12 from P1, 8 from P2, 4 from P3.** That is a budget, not a power
calculation, and it should be stated as one: with 24 items, a difference of fewer than about
four wins between two engines is noise. It is chosen because it is the smallest number that
gives ≥ 8 per stratum on the two strata that matter most and is hand-transcribable in one sitting.

Cutting uses the shipped code and no new constants:

- `ink.regions(mask, merge_px=64, min_pixels=120)` locates them; `min_pixels` **is** the
  blank-crop guard that catches the one hallucination no output-side test does.
- `crops.prepare(page, regions, paint=red|dark, binary=…)` pads via `clamp`, which is already
  gap-aware. **Do not pad to a constant.** Padding is free inside the gap to the nearest
  neighbour and catastrophic one pixel past it (measured: `eqline` broke at +48 px with a 6 px
  gap; `expo` held to +96 with a 141 px gap). **Record the measured gap for every one of the 24
  boxes** — that re-tests the padding-cliff rule at n=24 instead of n=2, for free.
- Render at **200 dpi** and do not tune it. Mid-band of UniMERNet's 80–350 dpi training range,
  already past its 192×672 input ceiling, and the response was measured **non-monotonic**.
- Flag `Crop.contested` — an overlapping region is a *grouping* failure that no padding rule
  fixes, and such a crop must be excluded from scoring rather than counted as a model error.

### 4.3 Renderings — the mask variants, and one that is already known to be wrong

`crops.prepare` returns both renderings today, so **this needs no new code**:

| Arm | How | Why |
| --- | --- | --- |
| `raw` | `Crop.raw` | The control. PaddleOCR-VL's exact `expo` reading came from a raw crop |
| `inkmask` | `Crop.composite`, `paint = red\|dark`, `binary=True` | **The best of 84 measured UniMERNet outputs.** Recovered `\|\alpha\|^n` and the `\omega_0` subscripts and deleted a `\frac{1}{2}` that was the slide's graph-paper grid read as a fraction bar |
| `flatten` | `Crop.composite`, same paint, `binary=False` | Keeps true greys. Between the two on the recorded sweep; cheap to carry |

> ⚠ **Do not add a `diff_mask` paint arm.** It is the obvious fourth variant and
> `crops.prepare`'s own docstring records it as already measured and **destructive**: painting
> the annotation ink alone made the fixture's printed skeleton `= |a|^n( … + j … )` vanish and
> the reading collapse. `diff_mask` is a **locator**, not a paint. This is exactly the kind of
> re-attempt the append-don't-delete rule exists to prevent.

**Totals per engine:** 24 crops × 3 renderings = **72**, plus the 12 P1 crops re-run on their
un-annotated twin as the standing control = **84 inferences per arm**. Five arms → 420. At
UniMERNet's measured 0.23–0.36 s and PaddleOCR-VL's 2.37–3.97 s per crop, the whole matrix is
minutes of GPU time, serialised.

### 4.4 What counts as a win — two axes, and only one of them decides

**Axis 1 — validity. Free, automatic, and it is a screen, not a score.**

Write one `results.json` per arm in a shape `ocr-handler check` already reads — `{name, task,
size:[w,h], text}` or `{case, w, h, raw}`. **Do not invent a fifth alias.** Then:

```sh
ocr-handler check tmp/h2h/<arm>/results.json
```

Report, per arm, the suspect rate and the per-detector roll-call. `--crop` comes from the record,
so `length-vs-crop` — the measured best single detector, 8/10 pathologies at 0 false positives —
is live on every reading.

**What Axis 1 can decide:** an arm that emits degenerate output is out; a crop that trips
`length-vs-crop` across *every* arm is a bad crop, not a bad model; `content-free` and
`empty-reading` catch a broken harness before anyone reads a number.

**What Axis 1 cannot decide — and this is load-bearing.** It has no idea whether a reading is
*correct*. The repair plan §7.4(b) is the proof: `\[\begin{aligned}\begin{aligned}\\ &\end{aligned}\\ \end{aligned}\]`
passed **seven of eight** detectors and contains zero mathematics. And in the other direction,
`control/expo_base_twin` is counted as a false positive while arguably being a true one. **A
"plausible" verdict is the absence of a specific alarm, not evidence of a right answer.**
Choosing on suspect-rate alone would repeat the compile-checking mistake in a new place.

**Axis 2 — correctness against ground truth. This is the decision.**

1. **Transcribe all 24 equations to LaTeX by hand, before any model runs.** Writing a key after
   seeing model output is how a benchmark gets contaminated, and this project already carries the
   labelled-sample debt that `scope.md` § Open decisions #3 records.
2. Score each reading three ways:
   - **exact match** after normalisation (the ExpRate analogue) — the headline;
   - **token edit distance ÷ ground-truth token count**, using `validity.tokens()` —
     **the same tokeniser the detectors use**, so the two axes are commensurable and no third
     tokenisation enters the project. (A fourth definition is precisely what halved the
     token-variety headline.)
   - **a symbol roll-call** per equation: the symbols that *must* appear (`\alpha`, `\omega_0`,
     `^{n}`, `\cos`, `j`, …), scored present/absent. This is what actually separates the recorded
     readings — "one subscript short" is invisible to exact match and is the difference between
     every pair of outputs in the record.
3. **Do not use CDM.** It needs a renderer and a spatial matcher this project does not have, and
   compile-checking — the cheap thing it is often confused with — is already dead here at 83/84.

**The win condition, fixed before the run.** An arm displaces the incumbent iff, over the 24
ground-truth equations, it has **(i)** strictly more exact matches, **(ii)** no more suspect
readings under `ocr-handler check`, and **(iii)** it loses no symbol the incumbent recovered.

If (i) holds but (iii) fails, the answer is **not** "swap" — it is **"route"**, and the routing
key is already in the per-crop record: the stratum (P1/P2/P3) or the aspect ratio (UniMERNet's
input is 1:3.5 and wastes ~90% of its canvas on a stacked derivation; PP-FormulaNet's is square).
Fixing this in advance is the whole purpose of ADR-0004: *"a second argued verdict is not better
than the first."*

**Tie-break, in order:** peak VRAM at load → seconds per crop → dependency footprint. A
transformers-5 upgrade is a real, unpaid cost and it breaks the arm that loses ties.

### 4.5 Rig discipline — the four that are not optional

1. **One engine resident at a time**, through [`tools/gpu_lock.py`](../../tools/gpu_lock.py).
   The box is shared with a YOLO watcher; ADR-0004 already records an OOM caused by a concurrent
   1,318 MiB process on a card with *less* competition than this one.
2. **Measure `max_memory_allocated()` and `max_memory_reserved()` around `from_pretrained`
   separately from inference.** The whole PaddleOCR-VL teardown turns on the peak being at load;
   a post-warm-up `nvidia-smi` misses it by design.
3. **`temperature=0`**, and record `eos_reached` plus token count against the cap. Hitting the cap
   is the classic loop signature and costs nothing to log. Note the cap is **VRAM-dependent** in
   MinerU's wrapper — 1152 tokens ≤ 6 GB, 1344 above — so **it will differ on this card** and any
   length heuristic must be expressed relative to it.
4. **Explicit `dtype=torch.float16` on every torch arm**, and explicit `device="gpu:0"` on any
   Paddle arm (three silent CPU fallbacks, all closed by naming the device).

### 4.6 Order of operations — each step can stop the next

| # | Step | GPU? | What it settles |
| --- | --- | --- | --- |
| 0 | `nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv` | no | §1 and §2's premise. **Do this first** |
| 1 | Hand-transcribe the 24 equations | no | Axis 2 exists at all |
| 2 | Cut 84 inputs with `ink.py` + `crops.py`, record gaps | no | The crops, and the padding rule at n=24 |
| 3 | Arms A, B, C (UniMERNet family, ~1.3 GiB, one process) | yes, small | Whether the 2501/2503 refreshes beat what we measured — **the cheapest possible win** |
| 4 | Arm D (PaddleOCR-VL, **torch** path, fp16+sdpa) | yes | The real challenger, on masked crops for the first time |
| 4b | Arm D again, Paddle path, once | yes | Prices the fp32/eager Turing penalty. Optional |
| 5 | Arm E (Uni-MuMER-Qwen3-VL-2B) | yes | Only after transformers 5 is agreed |

---

## 5. What this does **not** change

- **Two thirds of the corpus still needs no model.** Born-digital reconstruction and the
  no-GPU scanned-prose path are untouched; a bigger card is not a reason to point a VLM at pages
  that already have a text layer.
- **`ink.py` is still exact where a detector is approximate.** OmniDocBench's component-vs-
  end-to-end gap (85.0 → 57.3) is ~28 CDM points lost *upstream* of the recogniser. We do not pay
  it on P1/P2. **We do pay it on P3 and on the 430-document scanned path**, and no amount of VRAM
  helps there.
- **The blank-region guard, the un-annotated twin, and serialised GPU work** all stand, and all
  three were reproduced independently by two model families.
- **The ~20B ceiling is not binding** (§3.4), so it never enters the protocol.

---

## 6. Which ResearchHub queries were productive

Recorded so the next session does not re-pay for the noise. The calibration in the brief holds
exactly: **strong on models and papers, useless on tooling and on short/ambiguous queries.**

| Query | Result |
| --- | --- |
| `Uni-MuMER unified multi-task fine-tuning handwritten mathematical expression recognition` | ✅ **Best.** arXiv 2505.23566 with abstract + the official GitHub repo, first two hits |
| `handwritten mathematical expression recognition open weights vision language model 2B 3B parameters LaTeX output` | ✅ **Productive.** Uni-MuMER, **OmniHandwritingOCR 2608.18586**, 2412.03853, 2310.16809 — 4 real papers before the noise |
| `MathWriting dataset handwritten mathematical expressions PaLIGemma baseline Google` | ✅ **Productive, and it surfaced two candidates the existing docs do not name**: **GryphOne 2602.03370** and **InkFM 2503.23081** (both then found to have no released weights) |
| `offline handwritten mathematical expression recognition model 2026 released weights lightweight encoder decoder LaTeX` | ◐ Mixed — 6 real HMER papers, all pre-2024 or unreleased. Useful as a **negative**: the field has nothing new and runnable |
| `CROHME ExpRate state of the art 2025 2026 HMER benchmark comparison` | ❌ Noise (forums, an unrelated side-channel paper). Benchmark-name queries do badly |
| `Qwen2.5-VL formula recognition LaTeX document OCR benchmark` | ❌ Mostly Qwen2 release pages. Vendor-name queries do badly |
| `GOT-OCR 2.0 unified end-to-end OCR model formula` | ❌ Returned *Game of Thrones*. Found the right paper (2409.01704) at rank 1 and then collapsed |
| `binarization image preprocessing effect handwritten formula recognition accuracy background removal` | ❌ Noise (Spanish templates, quantum ML). **The mask-vs-raw question has no corpus support and stays a measurement** |

**Rule that falls out:** query with a *paper's own title words*, and it works. Query with a
benchmark name, a vendor name, or a technique phrase, and it returns SEO. `--json` is worth using —
it carries abstracts and arXiv IDs that the title view drops.

---

## 7. Inherited claims that changed or failed

| Claim | Source | Verdict |
| --- | --- | --- |
| *"Quadro RTX 5000 (24GB)"*, *"Available for next image: 20.9 GB (RTX 5000)"* | `skytracker…/findings/SAHI-INTEGRATION.md:313,350` | ❌ **FAILS.** Eight other skytracker docs say 16 GB, including a VRAM budget that is arithmetically incoherent at 24 GB. It sits inside a hand-built "Memory Profile" block — spec-sheet arithmetic presented as a measurement, the exact pattern this project has already caught once |
| *"Flash-attention-2 supports Ampere, so it applies to our 3060"* | `engine-landscape-2026-09.md` §5 | ◐ **True locally, false on the target.** FA2's own README excludes Turing. SDPA covers ~95% of the saving, so the consequence is small — but the *reasoning* does not transfer, and it was the sentence that resolved "does it fit" |
| *"Loading peaks ≈2× weights … loading is the binding constraint"* | `paddleocr-vl-teardown.md` verdict | ◐ **Still true, no longer binding — and replaced.** It is a PaddlePaddle behaviour on a 6 GB card. At 16 GB it is noise; on **Turing** a larger constraint takes its place (fp32 + eager, §2), which the 6 GB analysis could not see because it never ran on sm_75. The teardown's *method* is what found it |
| *"Uni-MuMER … 2.2B fp16 ≈ 4.4 GB against 4.3 GB of headroom, and the repo's inference path is `scripts/vllm_infer.py`. Fails the operator's constraint twice"* | `equation-ocr-specialists.md` §2.6 | ❌ **Both halves fail.** 3.963 GiB (measured from the manifest) is unremarkable at 16 GB, and `Qwen3VLForConditionalGeneration` is a stock transformers class. The surviving objection is different: **transformers ≥ 5** |
| *"PP-FormulaNet … costs a whole second DL framework (`paddlex` + PaddlePaddle) beside torch"* | `equation-ocr-specialists.md` §2.6, §7 | ❌ **False for plus-M.** MinerU ships a **pure-torch** `FormulaRecognizer` (`mfr/pp_formulanet_plus_m/predict_formula.py`, `import torch`, `BaseOCRV20`) reading `PP-FormulaNet_plus-M.pth` — the same vendoring shape already chosen for UniMERNet. The real objection is that the `.pth` lives in an **unlicensed** repo |
| *"GLM-OCR — not a local model — the repo is a cloud-API client"* | [`INDEX.md`](INDEX.md) | ◐ **Imprecise, and the compression is what broke it.** The *teardown* is careful; the INDEX row is not. `zai-org/GLM-OCR` is **MIT, 2.469 GiB, ~2M downloads/month**. The blocker is that it ships **no modeling code and no `custom_code` tag**, so it needs native transformers-5 support — availability is not the issue |
| *"dots.mocr — ruled out — exceeds the card"* | [`INDEX.md`](INDEX.md) | ◐ **Void on this card.** 6,078,431,736 B = **5,797 MiB**, which reproduces the teardown's figure exactly and **fits 16 GB**. The exclusion survives only on the `dots.mocr LICENSE AGREEMENT` §3.3(c) digitisation clause — which was always the stronger reason and should now be the recorded one |
| *"The CVPR-2026 UniMERNet checkpoint does not exist on the hub"* | `equation-ocr-specialists.md` §2.2 | ✅ **Holds, re-checked today.** Releases stop at 0.2.3 (2024-12-26); `wanderkid/unimernet_base` lastModified 2024-09-13. **But the same check found two checkpoints nobody here had noticed** — `unimernet_base_2501` and `unimernet_hf_small_2503` — and the second is MinerU's shipping default |
| `PaddlePaddle/PP-FormulaNet_plus-L_onnx` | its own name | ❌ **The repo is empty** — `.gitattributes` and a 28-byte README, zero downloads. A name is not an artifact |

---

## 7b. Three of § 8's unknowns — SETTLED by querying the box, 2026-09-06

This section was queried directly over SSH rather than inferred. Read-only commands only.

### ✅ The card is Turing. Confirmed by PCI device ID, not by part number.

```
0000:d5:00.0 VGA compatible controller: NVIDIA Corporation TU104GL [Quadro RTX 5000] [10de:1eb0]
Model: Quadro RTX 5000     (/proc/driver/nvidia/gpus/0000:d5:00.0/information)
```

**TU104 ⇒ Turing ⇒ compute capability 7.5.** Not `RTX A5000` (Ampere, sm_86, 24 GB), not
`RTX 5000 Ada` (sm_89, 32 GB) — the two cards whose names collide with this one and whose
capabilities would have made § 2's whole finding moot. **§ 2 stands: both `cap >= 8.0` gates fire.**

⚠ **Source attribution corrected 2026-09-06, by the skytracker_v2 session.** The `24GB` /
`20.9 GB available` block is **not** in the maintained `skytracker_v2` repo. It is at
`~/skytracker_data_analysis/postproc/docs/findings/SAHI-INTEGRATION.md:313,350` — the **legacy
archive**, which that team treats as a fabrication-riddled source rather than a maintained repo.
`skytracker_v2` already records the card correctly as 16 GB, and independently catalogs the same class
of error: `engine/docs/research/v1-demo-findings.md` verified-fabrication **#9**, *"describes a machine
that does not exist"*, citing five other files in its own repo that state 16 GB consistently.

Two notes on that, for whoever reads this next:

- #9 names a **different file** — `PERFORMANCE_BASELINES_2026_05_19.md`, not `SAHI-INTEGRATION.md`. So
  the archive instance at `:313,350` looks like a *second, uncatalogued* occurrence of the same
  fabrication rather than the one already logged. Minor, and theirs to decide.
- The direction of evidence is worth keeping: our `lspci` read is a **third-party confirmation of a
  conclusion they had already reached by a different route** (cross-referencing their own repo). Two
  independent methods, same answer — which is why 16 GB is now treated here as settled rather than
  merely well-sourced.

### ⚠ NEW — `nvidia-smi` is BROKEN on the target, and it is the tool § 8 wanted

```
Failed to initialize NVML: Driver/library version mismatch
NVML library version: 580.173
NVRM version: NVIDIA UNIX Open Kernel Module ... 580.159.03     (loaded kernel module)
nvidia-utils-580  580.173.02                                    (installed userspace)
```

Kernel module and userspace library disagree, so **every `nvidia-smi` query fails** — including the
free-VRAM and compute-capability queries § 8 proposed as its one-line settlements. The mismatch is
userspace-only: `/dev/nvidia{0,ctl,uvm,...}` are all present and the CUDA path is unaffected
(evidence below). **A reboot or a matching `nvidia-utils` install fixes it. Not our machine — this is
a request to the skytracker developers, not a change to make.**

Consequence for § 4.5 (rig discipline): the head-to-head **cannot record per-arm peak VRAM on the
target** until this is fixed. Either fix it first, or measure peaks on err0r's RTX 3060 and treat the
target as a headroom check only — and say which was done.

### ✅ Ollama on the target IS GPU-resident — the mismatch did not silently demote it

```json
{"model":"nomic-embed-text:latest","size":595142656,"size_vram":595142656,...}
```

`size_vram == size`: **100% of the model is on the card.** This matters beyond this project — the
operator's standing constraint is that Ollama runs on a GPU or not at all
([../../docs/decisions/0002-no-local-ollama-on-err0r.md](../../../docs/decisions/0002-no-local-ollama-on-err0r.md)),
and a broken NVML is exactly the failure that would have demoted it to CPU without saying so. It did not.

### ⚠ The GPU is SHARED — § 8's "12.5 or 7.9 GB" question is answered "neither is guaranteed"

```
/dev/nvidia0:   skytracker-dev  7399  F...m  python3
                skytracker-dev  7402  F...m  skytracker
```

Two resident processes besides Ollama, one of them the skytracker application itself. So free VRAM is
**not** a fixed number to look up — it depends on what that application is doing at the time, and with
`nvidia-smi` broken there is currently **no way to measure it**. Every arm in § 3 fits 16 GB with room
to spare, so this does not change the slate; it changes the **protocol**, which must now either
serialise against the other consumers or record what else was resident during each run.

---

## 8. What is still unknown, and the measurement that settles each

| # | Unknown | What settles it | Cost |
| --- | --- | --- | ---: |
| 1 | **The card's identity and capability.** Inferred from 16 GB + 3072 cores; never queried | `nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv` | one line |
| 2 | **Free VRAM in practice.** 12.5 GB or 7.9 GB depending on whether the centralised inference service shipped | `nvidia-smi --query-compute-apps=pid,used_memory --format=csv` | one line |
| 3 | **Whether Paddle really picks fp32+eager on this card.** Source-verified as a gate; not observed | `python -c "import paddle; print(paddle.amp.is_bfloat16_supported())"` | one line, no model |
| 4 | **The size of the fp32/eager penalty.** Arithmetic says several×; nobody has timed it | Arm 4b, once | one run |
| 5 | **Whether `unimernet_base_2501` / `…_small_2503` beat the Sept-2024 base.** No published comparison exists anywhere | Arms B and C. **Same architecture, same VRAM — the cheapest experiment on this page** | minutes |
| 6 | **The licence of `opendatalab/PDF-Extract-Kit-1.0`.** `cardData.license` is null; arms B, C and PP-FormulaNet all inherit the hole | Read the repo's `LICENSE`/README, or route through `wanderkid/*` (Apache-2.0) instead | metadata |
| 7 | **Whether `glm_ocr` has native support in a released transformers 5.x** | `grep` the installed transformers for `glm_ocr`, or read its release notes | metadata |
| 8 | **Whether the mask win survives P2 and P3.** ⚠ **The biggest one.** The best measured result in this project depends on separable ink — **P2 has no colour key and no twin; P3 has neither and is a scan.** Two thirds of the handwriting corpus | The protocol's strata. It is designed around this question and nothing else answers it | the run |
| 9 | **Uni-MuMER on *this* material.** Its numbers are CROHME / HME100K / MathWriting — clean isolated handwriting. §4.4 of the equation doc stands: **no benchmark measures handwriting over printed slides on graph paper** | Arm E on P1–P3 | the run |
| 10 | **Whether 24 equations is enough.** It is not, for a 1-point difference. It is, for the 3–4 point differences the recorded data actually shows | Nothing — this is a stated limit, not a question. Say it in the result | — |
| 11 | **fp16 numerical safety.** Every slate config declares `bfloat16`; Turing forces fp16, whose range is narrower. Overflow in a vision tower is usually benign and occasionally is not | Compare arm A's fp16 output against its recorded 6 GB fp16 output — **identical inputs already exist** in `tmp/eqocr/sweep.json` | free |

---

## 9. The strongest argument against this document

**It re-opens a slate on a machine none of its measurements came from.**

Every VRAM number here is either a 6 GB measurement asserted to transfer, or arithmetic over a
safetensors manifest. The one genuinely new mechanism — §2's fp32+eager cascade — is a *source
reading*, and source readings in this project have a mixed record: `mfr/utils.py` looked
adoptable until it was run against real outputs. §2 could be wrong in the way that matters most,
which is that it never fires because nobody uses the Paddle path anyway.

Four more:

1. **A bigger card is an invitation to stop thinking.** The best result in this project's
   equation work cost **zero** VRAM — it was a binary mask computed by existing code. Nothing
   about 16 GB improves that, and a slate with a 2B model on it makes it easier to reach for
   parameters instead of preprocessing. The ranking in §3.4 exists to keep that visible.
2. **Arm E costs a framework upgrade that could break the arm that wins.** transformers 5 already
   breaks TrOCR here; the vendored UniMERNet path is verified on 4.52.3 and on nothing else. It
   is entirely possible that the head-to-head selects a model the project then cannot ship
   alongside its incumbent.
3. **The protocol trusts a hand transcription by one reader.** That is the same single-reader
   limitation `ground-truth-sample.md` §0 states about its own 161 rows, and this key is 24 rows
   with no second opinion. On a 3-win margin, one misread ground truth flips the result.
4. **Three strata at n=8/12/4 is three underpowered experiments, not one adequate one.**
   Stratifying is right — P2 and P3 are the generalisation test — but it buys coverage with
   power, and P3 at n=4 can support "it failed completely" and nothing finer.

**The resolution is the same one ADR-0004 already chose:** fix the win condition before the run,
publish the per-crop record with the verdicts, and let a 3-win margin be reported as a 3-win
margin rather than as a decision.

---

## Sources

**Read from primary sources today** (read-only HTTP; no weights fetched, nothing installed):

- `paddle/fluid/pybind/place.cc:485-499` and `python/paddle/amp/{__init__,auto_cast}.py` —
  the bf16 ≥ sm_80 gate, from `PaddlePaddle/Paddle@develop`
- `paddlex/inference/models/doc_vlm/predictor.py:61-66`, `paddlex/inference/utils/misc.py:27-35`,
  `paddlex/…/paddleocr_vl/_siglip.py:144-158,185-191` — from `PaddlePaddle/PaddleX@v3.7.2`
- `huggingface.co/PaddlePaddle/PaddleOCR-VL-1.6/modeling_paddleocr_vl.py` (2,487 lines) —
  `_supports_sdpa` at `:530`, `:1266-1267`, selection at `:1089-1140`, no capability gate
- `github.com/Dao-AILab/flash-attention/README.md:145-146` — Turing exclusion, bf16 requirement
- HF API `?blobs=true` manifests and `cardData`: `phxember/Uni-MuMER-Qwen{3.5-2B,3-VL-2B,2.5-VL-3B,3.5-4B}`,
  `Qwen/Qwen{3.5-2B,3-VL-2B-Instruct,2.5-VL-3B-Instruct}`, `zai-org/GLM-OCR`,
  `dots-studio/dots.mocr`, `alephpi/FormulaNet`, `PaddlePaddle/PP-FormulaNet_plus-{M,L,L_onnx,L_safetensors}`,
  `opendatalab/PDF-Extract-Kit-1.0`, `wanderkid/unimernet_*`
- GitHub API: `opendatalab/UniMERNet` (releases, licence), `BFlameSwift/Uni-MuMER` (Apache-2.0);
  HF + GitHub search for `GryphOne` and `InkFM` — **zero released weights for either**
- Local clone: `~/tmp/ocr_repos/MinerU/mineru/model/mfr/pp_formulanet_plus_m/predict_formula.py`
  — pure torch, `PP-FormulaNet_plus-M.pth`

**ResearchHub** — the four productive queries in [§6](#6-which-researchhub-queries-were-productive).
New papers it surfaced that the existing research does not name: **GryphOne** `2602.03370`,
**InkFM** `2503.23081`, **OmniHandwritingOCR** `2608.18586`.

**Internal, cited not recopied:** [`equation-ocr-specialists.md`](equation-ocr-specialists.md) ·
[`paddleocr-vl-teardown.md`](paddleocr-vl-teardown.md) ·
[`handwriting-ocr-systems.md`](handwriting-ocr-systems.md) ·
[`engine-landscape-2026-09.md`](engine-landscape-2026-09.md) ·
[`mineru-teardown.md`](mineru-teardown.md) · [`dots-mocr-teardown.md`](dots-mocr-teardown.md) ·
[`glm-ocr-teardown.md`](glm-ocr-teardown.md) ·
[`../plans/latex-repair-and-validity.md`](../plans/latex-repair-and-validity.md) ·
[`../findings/ground-truth-sample.md`](../findings/ground-truth-sample.md) ·
[`../findings/corpus-census-2026-09-04.md`](../findings/corpus-census-2026-09-04.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md) ·
`src/ocr_handler/{ink,crops,validity}.py` (read only; nothing under `src/` or `tests/` was modified)

**Outside this repo:** `skytracker_data_analysis/postproc/docs/findings/{gpu-inference-service,
SAHI-INTEGRATION,gpu-driver-mismatch}.md`, `skytracker_algo/docs/detection-roadmap.md`,
`postproc/docs/{scope,ARCHITECTURE}.md`.

---

**Related:** [`INDEX.md`](INDEX.md) ·
[`../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md`](../decisions/0004-engine-choice-deferred-decide-by-head-to-head.md) ·
[`../directives/gpu-discipline.md`](../directives/gpu-discipline.md)
