# Lessons Learned — INDEX

**PRESCRIPTIVE** rules distilled from this project's own experience, in WHEN → DON'T → BECAUSE form, each
carrying the discovery that produced it.

**EMPTY — and that is a gap, not a state of nature.** Three earned lessons already exist and are currently
misfiled as *directives* in [../directives/code-discipline.md](../directives/code-discipline.md):

| Lesson owed | Discovery behind it |
| --- | --- |
| Don't sort spatial items by `(y, x)` | Two side-by-side equations came back swapped because their tops differed by three pixels — a silently reversed equation. Band by vertical overlap first. |
| Don't run a model over a page that already has a text layer | Extraction is exact; recognition is lossy. Measured: 67% of pages need no model. |
| Don't guess a tuned constant | `merge_px = 64` came from a 16→96 sweep with a stable plateau at 56–80. A swept and documented value survives review. |

The distinction that keeps them apart: **a directive is a standing rule for how to work; a lesson is a
rule plus the specific failure that earned it.** Splitting them is tracked in
[../plans/doctrine-compliance.md](../plans/doctrine-compliance.md) § C.
