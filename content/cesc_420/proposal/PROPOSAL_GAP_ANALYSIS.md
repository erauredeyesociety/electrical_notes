# Proposal Gap Analysis

Draft under review: [`../MOCK_PROPOSAL.pdf`](../MOCK_PROPOSAL.pdf). Rubric: [`../canvas_materials/Project Proposal Template_rubric.pdf`](../canvas_materials/Project%20Proposal%20Template_rubric.pdf), digested in [`../docs/04_course_requirements.md`](../docs/04_course_requirements.md).

---

## Scoring estimate

| Section | Weight | Draft state | Est. earned |
| --- | ---: | --- | ---: |
| Project Name | 2% | `X_swarm` — present, placeholder | 1–2% |
| Team Members | 4% | Four names listed | 4% |
| Problem Statement | 24% | Three sentences, **no literature review** | ~8% |
| Stakeholders | 10% | Answers the wrong question | ~1% |
| Proposed Solution | 45% | **Template prompts left unanswered**; two words of plan | ~4% |
| Budget | 10% | **Empty** — forfeits the redistribution clause | 0% |
| References | 5% | **Empty** | 0% |
| | | | **≈18 / 100** |

The draft is a skeleton, which is fine for a first pass. The two cheapest large gains are Budget (10% for one honest sentence) and References (5%), and they are also what unlock the Problem Statement's missing 16%.

---

## Section-by-section

### Project Name — 2%

`X_swarm` reads as a placeholder. Cheap fix; pick something that names the *capability*.

Candidates: `HALO` (Heterogeneous Air-Ground Localization & Orchestration) · `TANDEM` · `SwarmBridge` · `CoFly`. Decision pending — [PD-01](../docs/03_decision_record.md#pending-decisions).

### Team Members — 4%

Emmett Gilbert · Gatlin Nelson · DeAndre Johnney · Nicholas Schultz. Full marks already.

**Improve:** add the Day-1 role assignments (PM/Scrum, Systems & Technical, Design/Implementation, Testing & Validation, Documentation & Communication). Costs nothing, and the roles are needed for weekly progress checks anyway. Verify the spelling of every name against the roster before submission.

### Problem Statement — 24% ⚠ largest gap

Draft:
> *We are trying to solve the issue of heterogenous aerial swarm formations with ground vehicles.* … *Coordinating flying vehicles with ground vehicles is difficult because of network throughput, delay, computational effort, and other software/hardware inaccuracies.*

The instincts are right. Three problems:

1. **No literature review.** The template says so explicitly, and it is the single largest source of lost points. Every difficulty claimed — throughput, delay, computation — needs a citation.
2. **"Difficult" is not a problem statement.** It says the engineering is hard; it does not say who suffers when it isn't done. Name the operational gap first, then the technical difficulty.
3. **Constraints are circular.** *"software and testing constraints, which ultimately lead to time constraints"* — every project has time constraints. The template names physical and cost constraints as examples; the real ones here are payload, flight time, positioning-volume, radio bandwidth, and shared lab access.
4. Typo: "heterogenous" → **heterogeneous**.

**Rewrite in three moves:** (a) the real-world gap that a heterogeneous air-ground team solves and a single robot doesn't; (b) *why it stays unsolved* — differing localization frames, clock skew, bandwidth ceiling, asymmetric mobility and endurance — each cited; (c) constraints, split into physical / technical / schedule with actual numbers.

### Stakeholders — 10% ⚠ wrong question answered

Draft: *"Primary stakeholders: Equal share amongst all stakeholders, 25%."*

That is a team ownership split, not a stakeholder list. Near-zero as written.

**The distinction:** *primary* stakeholders are directly affected by the system's operation or outcome — they use it, fund it, or are graded on it. *Secondary* stakeholders are affected indirectly or govern it.

Structure to use — three tiers:

- **Course/customer:** faculty mentor as customer (Dr. Calderon Chavez), course instructors and TAs, the team, the EECS department and lab manager.
- **Inheritors:** future capstone teams and lab researchers who build on the codebase — this is real, given the department materials policy.
- **Application-domain:** the operators who would use the technology. Pick two or three and say what a swarm gives them that one robot does not.

Sourced list: [`../docs/findings/F06_stakeholders_and_applications.md`](../docs/findings/F06_stakeholders_and_applications.md).

### Proposed Solution — 45% ⚠ effectively unwritten

The draft leaves the template's own prompts in place as body text and answers with *"Semester 1: Testing and research, avoiding simulations as much as possible… Semester 2: Implementation."*

Every prompt needs an explicit answer:

| Template prompt | Status | What it needs |
| --- | --- | --- |
| Scope: what's covered | ✗ | Baseline mission, agent counts, environment |
| Scope: **what's out of scope** | ✗ | Explicit exclusions — outdoor flight, GPS-denied mapping, lidar, learned control |
| Standards that drive it | ✗ | FAA, FCC, IEEE, ISO — see [`F05`](../docs/findings/F05_standards_and_regulations.md) |
| Functionality by end of Semester 1 | ✗ | Demonstrable milestones, not "research" |
| Functionality by end of the year | ✗ | The final demo, defined |
| Approach: real vs simulated data | Partial | Says "avoid simulation" — needs nuance ([SLO 6](../docs/04_course_requirements.md#student-learning-outcomes-map-deliverables-to-these) requires simulation) |
| Approach: technical detail | ✗ | Architecture sketch, positioning, comms, control |

Three specific risks:

- **"Semester 2: Implementation" is a scheduling error.** A whole semester with no implementation means no midterm prototype evidence (15% of the midterm rubric) and nothing to de-risk against. Implementation must start in Semester 1.
- **"Avoiding simulations as much as possible"** contradicts SLO 6 and removes the only cheap way to debug coordination logic. Reframe rather than reverse: *hardware is the primary validation environment; software-in-the-loop is used to unit-test coordination logic before flight.*
- **The out-of-scope list is where the 45% is defended.** It is the cheapest way to look deliberate rather than vague.

### Budget — 10% ⚠ free points, currently zero

Section is empty. The clause is explicit: state that no budget is required and the 10% redistributes to +3 Problem Statement, +3 Stakeholders, +4 Proposed Solution. **The statement is required; blank forfeits it.**

Two paths:

- **Zero-budget:** all lab hardware exists → say so, itemize what is being borrowed, state that all software is open-source, claim the redistribution.
- **Non-zero:** spare Crazyflie airframes, propellers, batteries, decks, ground-robot parts. Spares deserve real consideration — a broken drone with no replacement stops the project.

Either way it must be stated. Depends on [PD-05](../docs/03_decision_record.md#pending-decisions) — do the ground vehicles exist?

### References — 5% ⚠ empty

Zero as written, and it is what makes the Problem Statement's 24% reachable. Target 8–12 references: Crazyflie/Crazyswarm2 documentation and papers, formation-control literature, air-ground cooperation papers, the standards cited by number, and the mentor's own publications (worth doing regardless of citation value).

Starting set: [`../docs/findings/`](../docs/findings/), and pick one citation style, consistently.

---

## Priority order

1. **Budget statement** — one sentence, 10%.
2. **Proposed Solution** — the 45%, and the most work. Scope in/out, standards, per-semester functionality.
3. **Problem Statement literature review** — unlocks ~16%.
4. **Stakeholders rewrite** — 30 minutes for ~9%.
5. **References** — falls out of 3 and 4.
6. **Project name + roles** — 15 minutes.

Working rewrite: [`PROPOSAL_DRAFT_v2.md`](PROPOSAL_DRAFT_v2.md). Blocking unknowns: [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md).

---

**Related:** [`../docs/04_course_requirements.md`](../docs/04_course_requirements.md) · [`../docs/03_decision_record.md`](../docs/03_decision_record.md) · [`../INDEX.md`](../INDEX.md)
