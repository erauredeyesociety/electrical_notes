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

Run from the **repo root**; paths are repo-relative:

```sh
docs/latex/build_tex.sh content/cesc_410/hw/hw01 --keep     # keeps the PDFs
```

`../tools/build_tex.sh hw01 --keep` still works and takes paths relative to
`content/cesc_410/hw/`, but the shared checker is the one to prefer — it is the
same script every course uses, so a fix lands everywhere at once.

For a single combined document, build `hw01_solutions.tex`, or make a wrapper that `\include`s each problem file.

## If the deliverable goes through Overleaf

**Never paste a source file in.** Its `\input` climbs above the project root and
cannot resolve there. Flatten first:

```sh
docs/latex/flatten_tex.sh content/cesc_410/hw/hw01
#   -> content/cesc_410/hw/hw01/overleaf/*.tex   (gitignored, regenerable)
```

Each output is self-contained: paste or upload one and it needs no other file.
Verified for HW1 — all seven flattened copies compile on their own.

Two things to know before handing a flattened copy to anyone:

- The flattener writes a two-line header naming the **source path it came
  from**. That is a repository path in a document that may be submitted. Delete
  those two comment lines from anything you hand in. (It never renders — a
  LaTeX comment does not reach the PDF — so this only matters if the `.tex`
  itself is the deliverable.)
- **Edit the source, never the flattened copy.** `overleaf/` is overwritten on
  the next run.

**Check any submitted `.tex` or PDF carries no tooling references** — no script names, flags, or repository paths. Same rule as the labs ([`../../labs_and_projects/reference_docs/code_separation.md`](../../labs_and_projects/reference_docs/code_separation.md)).

---

**Related:** [`../prompt.md`](../prompt.md) · [`hw_workflow.md`](hw_workflow.md)
