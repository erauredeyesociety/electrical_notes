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
