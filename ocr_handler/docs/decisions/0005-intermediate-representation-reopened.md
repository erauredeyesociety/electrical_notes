# ADR-0005 — Intermediate representation: adopted from Unlimited-OCR, now reopened

**Date:** 2026-09-02, reopened 2026-09-04 · **Status:** **Under review** — do not build against it yet

## Context

The M1 session adopted Baidu Unlimited-OCR's output format,
`<|det|>CATEGORY [bbox]<|/det|>CONTENT`, as this project's intermediate representation, on the grounds
that it is "the same shape as our contract — what a block is, where, and what it contains,
resolution-independently."

## Why it is reopened

That adoption inherits its justification from a source now under re-examination. The operator's steer:
*"the example repos it might be picking apart might not be the best solutions either."* A format chosen
because an inspiration used it has not been chosen on its merits.

It also predates a requirement it was never tested against: **side-by-side comparison**. The intermediate
now has to hold *two* variants of the same page plus the evidence for preferring one.

## Options

| Option | For | Against |
| --- | --- | --- |
| `<|det|>` tagged string | matches one candidate engine's native output; resolution-independent bboxes | a string format needing a parser; owes its selection to an unvetted source; no obvious place for two variants + agreement metrics |
| **JSONL, one record per page** | greppable, streamable, trivially holds both variants, `chosen` and `reason`; no parser | not any engine's native output — needs a small adapter per engine |

Recommended: **JSONL**, schema proposed in [plans/text-layer-first.md](../plans/text-layer-first.md) § 4.
If a page-level engine emits `<|det|>`, parse it into the JSONL record rather than adopting it wholesale.

## Status

Open — [scope.md](../scope.md) § Open decisions #5. Supersede this ADR with a new one when settled;
do not edit it.
