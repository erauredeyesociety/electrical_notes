# What each homework requires

> ⚠ **Unconfirmed and expected to vary.** Unlike the labs — which have a stated report+code rule — homework submission format has not been established. Fill this in per assignment; ask rather than assume.

## What is known

- Homework **usually involves no code and no zip**, unlike the labs.
- The CESC 410 (lecture course) info governs, not the 410L lab info. They are different courses with different rules.
- HW1 is worth **130 points** across 6 problems.

## Per-assignment

| HW | Due | Format | Confirmed? | Notes |
| --- | --- | --- | --- | --- |
| 01 | ? | ? | ❌ | 6 problems, 130 pts. Handout labels two of them "Prob 1" |

## Questions to ask

1. Is a single PDF expected, or per-problem files?
2. Is the detailed working submitted, or only final answers? **This decides which of our two documents is the deliverable** — and we produce both, so it is cheap either way.
3. Handwritten or typeset? Some courses require handwritten work.
4. Is there a required cover sheet or naming convention?

## Producing the PDF

```sh
tools/build_tex.sh hw01 --keep      # keeps the PDFs
```

For a single combined document, build `hw01_solutions.tex`, or make a wrapper that `\include`s each problem file.

**Check any submitted `.tex` or PDF carries no tooling references** — no script names, flags, or repository paths. Same rule as the labs ([`../../labs_and_projects/reference_docs/code_separation.md`](../../labs_and_projects/reference_docs/code_separation.md)).

---

**Related:** [`../prompt.md`](../prompt.md) · [`hw_workflow.md`](hw_workflow.md)
