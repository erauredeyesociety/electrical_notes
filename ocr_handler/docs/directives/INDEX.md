# Project Directives — INDEX

Condensed, project-local rules for **ocr_handler**, phrased for *this* stack (Python 3.12 + `uv` +
PyMuPDF, a 6 GB RTX 3060 Laptop) and *this* job (one text extractor for every course in
`electrical_notes`).

Three tiers — load down only when the tier above lacks the depth you need:
**project directive (here)** → `~/llm-project-bootstrap/directives/<name>.md` → `~/llm-project-bootstrap/guides/<GUIDE>.md`

| File | Governs |
| --- | --- |
| [scope-discipline.md](./scope-discipline.md) | One scope file; the blacklist is enforced; the CLI verb count is fixed |
| [roadmap-and-plans.md](./roadmap-and-plans.md) | Lean roadmap; tactical detail in `docs/plans/`; re-sequence by leverage and say why |
| [code-discipline.md](./code-discipline.md) | Write less code; module size cap; measured constants; the reading-order rule |
| [testing-discipline.md](./testing-discipline.md) | Tiny behaviour-level floor — **and it must cover the path the CLI uses** |
| [documentation-discipline.md](./documentation-discipline.md) | Right doc, right folder; INTERNAL vs EXTERNAL; supersede in place |
| [question-discipline.md](./question-discipline.md) | Batch the operator's open calls; never guess; git is human-only |

Referenced from [../scope.md](../scope.md) and [../roadmap.md](../roadmap.md) so every session loads them
just-in-time.

**Not yet distilled** (see [../plans/doctrine-compliance.md](../plans/doctrine-compliance.md)):
`automation-first`, `wiki`, `honest-instrumentation`, `plan-first`, `map-before-act`,
`knowledge-retrieval`, `research-docs`. Add them when they start costing something, not pre-emptively.
