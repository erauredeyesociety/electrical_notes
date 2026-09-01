# Meta: How the Idea Register Works

**Purpose:** rules for [`01_idea_register.md`](01_idea_register.md). This file is *about* the register, not part of it.

**Why it exists:** ideas get re-litigated. When someone asks in November "why aren't we doing sonar?", the answer must already be written down with its reasoning, not re-argued.

---

## Core rule

**Nothing is deleted.** An idea that is rejected gets a `Rejected` status and a recorded reason. Silent removal is what causes re-litigation.

Only the humans on the team can reject an idea. Research can produce evidence; it cannot cast the vote.

---

## Entry shape

Every entry uses the same six fields. No solution is committed to — the register captures *problems and concepts*, not designs.

| Field | Contents |
| --- | --- |
| **ID** | `IR-##`, never reused |
| **Idea** | One sentence |
| **Problem** | What real-world thing is broken |
| **Why it's a problem** | The physics / economics / operational reason it isn't already solved |
| **Concepts involved** | Techniques, sensors, algorithms that *bear on* it — not a chosen solution |
| **Status** | See taxonomy below |

Plus, where useful: `Depends on`, `Data needed`, `Related` (cross-links to other IDs and to findings docs).

---

## Status taxonomy

| Status | Meaning | Can it come back? |
| --- | --- | --- |
| **Selected** | In the current project scope | — |
| **Stretch** | In scope only if the baseline lands early | Yes |
| **Parked** | Sound idea, wrong semester or wrong hardware | Yes, needs a trigger |
| **Future work** | Belongs in the proposal's *future work* section, not the build | No, by design |
| **Rejected** | Ruled out; reason recorded | Only with new evidence |

`Rejected` splits into two kinds, and the distinction matters:

- **Rejected (physics)** — cannot work as described. New evidence would have to overturn the physics.
- **Rejected (scope)** — could work, doesn't fit two semesters or this hardware. New evidence = a schedule or budget change.

---

## Cost is excluded

Per team direction, no cost figures appear in the register. Budget lives only in the proposal's Budget section — see [`../proposal/PROPOSAL_GAP_ANALYSIS.md`](../proposal/PROPOSAL_GAP_ANALYSIS.md).

---

## Cross-referencing

Register entries link to findings documents in [`findings/`](findings/); findings documents link back by `IR-##`. Any claim with a number in it should point at the findings doc that sources it.

---

## Maintenance

- Add entries as they come up; do not batch.
- When status changes, record the date and the reason on the same line.
- Constraints are **not** ideas. They live in [`02_constraints.md`](02_constraints.md) because they are true regardless of which ideas get picked.

**Related:** [`01_idea_register.md`](01_idea_register.md) · [`02_constraints.md`](02_constraints.md) · [`03_decision_record.md`](03_decision_record.md) · [`../INDEX.md`](../INDEX.md)
