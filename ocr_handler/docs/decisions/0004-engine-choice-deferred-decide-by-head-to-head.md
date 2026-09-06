# ADR-0004 — The recognition engine is deliberately unresolved

**Date:** 2026-09-02, reaffirmed 2026-09-04 · **Status:** Accepted (a decision *about how to decide*)

## Context

Three candidates were measured running on this machine's RTX 3060 Laptop (6 GB) and **all three fit**:

| Candidate | Peak VRAM | Shape |
| --- | ---: | --- |
| UniMERNet-Base fp16 | 681 MiB | cropped equations only |
| SmolDocling-256M | 960 MiB | equations and whole pages |
| Unlimited-OCR NF4 | 4,199 MiB | whole pages, crops figures itself |

An earlier verdict picked UniMERNet-Base. It was then reopened when Unlimited-OCR — previously written
off as "does not fit" — was measured running successfully. The operator has since added:
*"the example repos it might be picking apart might not be the best solutions either."*

## Decision

**Do not choose yet.** Resolve by a head-to-head on the fixture page before `recognize.py` is written, and
treat the current landscape survey as unfinished — a separate research pass is re-examining it.

Build `recognize.py` behind **one swappable interface**, so the loser is cheap to replace.

## Rationale

The first verdict was wrong on the half that was argued rather than measured. A second argued verdict is
not better than the first. Three candidates that all fit is a measurement problem, not a debate.

## Consequences — adopt regardless of which wins

- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` — worth ~1.1 GiB of peak (5,321 → 4,199 MiB, identical work).
- `temperature=0` — determinism is what makes a regression test possible.
- **Always run the un-annotated twin as a control.** It is what proved the model reads the ink rather than
  guessing it: the twin returned `(\quad + j \quad)`.
- **Serialise GPU work.** A concurrent 1,318 MiB process caused an OOM mid-session.
- No `--engine` flag ships until this is closed; naming a model in the CLI would bake in the choice.

---

## Addendum — 2026-09-06: what is now known, and what is still an operator call

> **The decision above is unchanged and nothing in it is edited.** ADRs are immutable; this is an
> append, per [`../directives/documentation-discipline.md`](../directives/documentation-discipline.md)'s
> *"contradictions are recorded, not resolved by preference"* and the shared research doctrine's
> *append — don't replace*. It records evidence that arrived after the ADR, so the head-to-head can
> be run. **It does not choose the engine.**
>
> Full working: [`../research/stage2-slate-and-head-to-head-2026-09-06.md`](../research/stage2-slate-and-head-to-head-2026-09-06.md).

### The two blockers named in the ADR are both gone

1. **The scorer exists.** `ocr-handler check` ships eight engine-agnostic detectors
   ([`../plans/latex-repair-and-validity.md`](../plans/latex-repair-and-validity.md) § 7). ⚠ With
   one limit that must not be forgotten when the results are read: **it is a screen, not a score.**
   It proves a reading is degenerate; it cannot prove one is right. § 7.4 (b) of that plan is the
   standing counter-example — a reading with **zero** mathematical content passed seven of eight
   detectors. **Ground truth decides; the gate only eliminates.**
2. **The slate exists**, and it is five arms: UniMERNet-Base (the control), **`unimernet_base_2501`**
   and **`unimernet_hf_small_2503`** — two checkpoints newer than the one this project measured,
   the second being MinerU 3.4.5's actual shipping default, both at **identical or lower VRAM** —
   PaddleOCR-VL-1.6 on its **torch** path, and **`Uni-MuMER-Qwen3-VL-2B`**.

### The hardware premise of the ADR's table has changed

The ADR's three candidates were measured on a 6 GB RTX 3060 Laptop (Ampere). The deployment target
is the skytracker **Quadro RTX 5000: 16 GB, and Turing — compute capability 7.5**. Bigger card,
older silicon, and the second half is the one that matters:

- **PaddleX gates bf16 *and* SDPA at capability ≥ 8.0.** Verified in source
  (`paddle/fluid/pybind/place.cc:492-499`; `paddlex/…/_siglip.py:144-158`). On sm_75 the Paddle
  path therefore runs **fp32 with eager O(N²) vision attention**. The escape is one line: the HF
  **torch** implementation declares `_supports_sdpa` with no capability gate — load
  `dtype=torch.float16, attn_implementation="sdpa"`.
- **No FlashAttention-2 on Turing** (upstream README), so the sentence in
  `engine-landscape-2026-09.md` § 5 that resolved "does it fit" — *"flash-attention-2 supports
  Ampere, so it applies to our 3060"* — is true here and **false on the target**. SDPA covers ~95%
  of the saving, so the consequence is small; the reasoning does not transfer.
- **Every slate model ships `dtype: bfloat16`.** On this card each must be loaded with an explicit
  `float16`, or torch honours the config and runs an emulated path.
- **`from_pretrained` peaking at ~2× weights** — the constraint that decided the 6 GB analysis — is
  a *PaddlePaddle* behaviour and stops binding at 16 GB. On the torch path it is 1×.

### What the ADR's consequences look like now

Everything under *"Consequences — adopt regardless of which wins"* stands. Three gain force:
**serialise GPU work** (the target is a shared box already carrying a continuous YOLO watcher),
**`temperature=0`**, and **always run the un-annotated twin** — which is now reproduced by three
model families and, in this protocol, is 12 of the 84 inferences per arm.

Two additions the ADR could not have made:

- **Measure `max_memory_allocated` around `from_pretrained` separately from inference.** The peak
  is at load, and a post-warm-up `nvidia-smi` misses it by construction.
- **Fix the win condition before the run.** An arm displaces the incumbent iff, over 24
  hand-transcribed equations, it has (i) strictly more exact matches, (ii) no more suspect
  readings, and (iii) loses no symbol the incumbent recovered. **If (i) holds and (iii) fails, the
  answer is "route", not "swap."** Writing this down in advance is what stops the head-to-head
  ending in a fourth argued verdict — which is the failure this ADR exists to prevent.

### What the evidence supports, and what it does not

**Supports:** the incumbent is not obviously wrong, and the two cheapest arms have never been run —
`unimernet_base_2501` and `unimernet_hf_small_2503` cost the same VRAM as the checkpoint already
measured, so "is our checkpoint simply out of date?" is answerable in minutes. It also supports
putting `Uni-MuMER-Qwen3-VL-2B` on the slate: the objection that excluded it (4.4 GB of weights, a
vLLM-only path) fails on both halves.

**Does not support:** choosing. Two facts hold the decision open. **(a)** The single largest measured
accuracy win in this project is `ink.py`'s binary mask, and it needs separable ink — which **two
thirds of this corpus's handwriting does not have** (the OneNote export has no colour key and no
twin; the `ps160` scans have neither). **(b)** The two checkpoints that would be cheapest to adopt
live in `opendatalab/PDF-Extract-Kit-1.0`, whose `cardData.license` is **null**.

**Two one-line commands gate everything and neither runs a model:**

```sh
nvidia-smi --query-gpu=name,memory.total,memory.free,compute_cap --format=csv
nvidia-smi --query-compute-apps=pid,used_memory --format=csv
```

The first confirms or destroys the sm_75 premise above; the second says whether ~12.5 GB or ~7.9 GB
is actually free on a shared card. **Neither the engine choice nor `--engine` ships before the
head-to-head runs.** That part of the decision is unchanged.
