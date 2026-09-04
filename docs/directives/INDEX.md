# Project Directives — INDEX

Condensed, project-local rules for **electrical_notes**, phrased for *this* repo (a Hugo-published
university coursework corpus, 15 course folders, two child projects) rather than for software in general.

Three tiers — load down only when the tier above lacks the depth you need:
**project directive (here)** → `~/llm-project-bootstrap/directives/<name>.md` → `~/llm-project-bootstrap/guides/<GUIDE>.md`

| File | Governs |
| --- | --- |
| [scope-discipline.md](./scope-discipline.md) | One scope file; **older courses are not retrofitted**; child projects own their own scope; `content/` is public |
| [coursework-solutions.md](./coursework-solutions.md) | **The coursework workflow.** Two-document rule, standalone per-problem `.tex`, citations, verification, what is human-only |
| [documentation-discipline.md](./documentation-discipline.md) | Right doc, right folder; three separate doc trees; nothing durable in the repo root |
| [roadmap-and-plans.md](./roadmap-and-plans.md) | Lean roadmap about the *repo*, not the coursework; tactical detail in `docs/plans/` |
| [testing-discipline.md](./testing-discipline.md) | The floor here is **three build checks**, not a unit-test suite; child-project floors are real and protected |
| [question-discipline.md](./question-discipline.md) | Batch the operator's calls; never retrofit or move coursework unasked; git is human-only |

Referenced from [../scope.md](../scope.md) and [../roadmap.md](../roadmap.md) so every session loads them
just-in-time.

**Deliberately not distilled yet** — add one when it starts costing something, not pre-emptively:
`code-discipline` (the root repo ships no application code; `ocr_handler` has its own —
[`../../ocr_handler/docs/directives/code-discipline.md`](../../ocr_handler/docs/directives/code-discipline.md)),
`automation-first`, `wiki`, `plan-first`, `map-before-act`, `knowledge-retrieval`,
`honest-instrumentation`, `research-docs`.

**Child projects carry their own directives** and are not governed by this folder:
[`ocr_handler/docs/directives/INDEX.md`](../../ocr_handler/docs/directives/INDEX.md).
