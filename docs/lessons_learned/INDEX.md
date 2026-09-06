# Lessons Learned — INDEX

**PRESCRIPTIVE** rules future sessions must obey, in `WHEN → DON'T → BECAUSE` form, each carrying the
specific failure that earned it. A [finding](../findings/INDEX.md) that hardens into a rule graduates here.

| File | Covers |
| --- | --- |
| [lessons.md](./lessons.md) | 14 lessons in four groups — **Coursework and LaTeX** (never read maths from a text layer; no tooling references in a submission; Overleaf cannot resolve paths above its root; ignore what you generate, not what you predict) · **docs-rag** (a silent success; re-ingest is not idempotent; exclusions are not retroactive; the search parameter differs by endpoint) · **Shell and operations** (`grep -q` under pipefail; bind the docker bridge too; check the base image's user) · **Repo governance** (write the ADR; report git state, never resolve it) |

This file tracks the **repo and its toolchain**. Lessons about the OCR pipeline live in the child
project: [`ocr_handler/docs/lessons_learned/`](../../ocr_handler/docs/lessons_learned/INDEX.md).

## The distinction that keeps this folder from becoming a second directives folder

A **directive** is a standing rule for how to work here. A **lesson** is a rule *plus the specific
failure that earned it*. If you cannot name the incident, it is a directive, not a lesson.

## Format

```
- **WHEN <situation>, DON'T <action> — <do this instead> — BECAUSE <consequence>.** <The concrete
  failure, with its measurement.> (YYYY-MM-DD) Source: <path>
```

Split at ~400 lines into `lessons_2.md` and index the parts.

---

**The three lessons this folder was opened owing** — never read mathematics out of a PDF text layer
(HW-01), never let a tooling reference into a submitted document (KI-09), and a silent success is worse
than a failure (docs-rag F-01) — are now written, with their measurements, in [lessons.md](./lessons.md).
[../roadmap.md](../roadmap.md) § M6 tracked this as the distillation step.
