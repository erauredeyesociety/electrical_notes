# Semester 1 Schedule — Fall 2026

Term: **Aug 24 – Dec 9, 2026**. Class Tue/Thu 2:15–3:30, IC 101. Weekly in-class progress checks; backlog must be current with per-sprint estimates.

> ⚠ **Deliverable due dates below are estimates, not confirmed.** The syllabus gives no dates. Confirm with Dr. Yang and replace — question 13 in [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md).

**Today is week 2.** Weeks 1–2 are already spent on project selection.

---

## Week map

| Wk | Dates | Focus | Milestone |
| --- | --- | --- | --- |
| 1 | Aug 24–30 | Project options introduced | — |
| 2 | **Aug 31–Sep 6** | **Proposal + mentor meeting** | Roles assigned; mentor Q&A done |
| 3 | Sep 7–13 | Proposal submitted; repo + backlog live | **M1 — Proposal** |
| 4 | Sep 14–20 | Bring-up: build, fly one drone, land it | **M2 — Hello Drone** |
| 5 | Sep 21–27 | Instrumentation: logging + benchmark harness v0 | **M3 — First numbers** |
| 6 | Sep 28–Oct 4 | SRS drafting; two-drone coordination | — |
| 7 | Oct 5–11 | SRS submitted; frame calibration begins | **M4 — SRS** |
| 8 | Oct 12–18 | **Midterm presentation** | **M5 — Midterm** |
| 9 | Oct 19–25 | Air-only formation, N=3 | **M6 — Formation** |
| 10 | Oct 26–Nov 1 | SDD drafting; air↔ground frame unified | **M7 — Common frame** |
| 11 | Nov 2–8 | SDD submitted; integration checkpoint | **M8 — SDD** |
| 12 | Nov 9–15 | Test Plan; scaling measurements vs N | — |
| 13 | Nov 16–22 | Test Plan submitted; baseline demo rehearsal | **M9 — Test Plan** |
| 14 | Nov 23–29 | *Thanksgiving (Nov 26) — assume ~half a week* | Buffer |
| 15 | Nov 30–Dec 6 | Final presentation, poster, 10-min video | **M10 — Final** |
| 16 | Dec 7–9 | Term ends Dec 9 | Handover notes |

---

## Milestones with acceptance criteria

A milestone is done when the criterion is *measured*, not when it feels done.

### M1 · Proposal submitted — week 3

Every rubric section answered, budget statement present, ≥8 references. Gate: [`../proposal/PROPOSAL_GAP_ANALYSIS.md`](../proposal/PROPOSAL_GAP_ANALYSIS.md) shows no ✗ rows.

### M2 · Hello Drone — week 4

Clone the inherited repo, build it, take off, hover, land — by every team member, on their own machine. **This is deliberately the first engineering milestone** ([R-08](05_risk_register.md#r-08--inherited-codebase)); if it takes longer than a week that is information for the mentor, not a private struggle.

### M3 · First numbers — week 5

Benchmark harness v0 produces a logged, reproducible measurement of at least: control-loop period and jitter, ground-station→drone command latency (p50/p95/p99), and radio packet rate and loss. **No flight required beyond a tethered hover.** This is [IR-23](01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness) and it is the hedge against [R-13](05_risk_register.md#r-13--nothing-to-show-at-midterm).

### M4 · SRS — week 7

Every performance requirement has a number, a percentile and a measurement condition. If a requirement cannot be traced to a test case, it is not a requirement.

### M5 · Midterm — week 8

5 minutes, all four members speak. Carries prototyping evidence at 15% — M3's latency histograms are the slide.

### M6 · Formation, air-only, N=3 — week 9

Three drones hold a commanded geometry. Report RMS formation error and convergence time over ≥5 trials, with the RF environment and battery state logged per trial.

### M7 · Common frame — week 10

Air and ground frames calibrated; residual offset **measured and reported**, not tuned away ([R-04](05_risk_register.md#r-04--frame-calibration)).

### M8 · SDD + integration checkpoint — week 11

Architecture documented, and every subsystem interface exercised end-to-end at least once — even with stubs. Guards against [R-12](05_risk_register.md#r-12--late-integration).

### M9 · Test Plan — week 13

Traceability matrix complete: every SRS requirement maps to a test case with pass/fail criteria.

### M10 · Final, poster, video — week 15

Rehearse against the clock; the video rubric gives 10% for time management alone.

---

## Sprint mechanics

Two-week sprints aligned to the week map (S1 = wk 3–4, S2 = wk 5–6, …). Required by the syllabus: a current backlog, with each task estimated in a consistent unit before the sprint starts. Backlog tool is [PD](03_decision_record.md#pending-decisions)-pending — GitHub Projects is the low-friction choice if Dr. Yang accepts it (question 15).

Per sprint: pick tasks, estimate, review at the boundary, re-score [`05_risk_register.md`](05_risk_register.md), append anything decided to [`03_decision_record.md`](03_decision_record.md).

---

## Parallel workstreams

Four people, and these run concurrently rather than in sequence — sequencing them is how a semester disappears.

| Stream | Weeks | Depends on hardware? |
| --- | --- | --- |
| Flight bring-up and formation control | 4–13 | Yes — lab-bound |
| Benchmarking and instrumentation | 5–13 | **No** — survives a grounded fleet |
| Frame calibration and integration | 7–11 | Partly |
| Documentation (SRS, SDD, Test Plan) | 3–13 | No |

The second and fourth streams are what keep the project moving through [R-01](05_risk_register.md#r-01--hardware-loss) and [R-06](05_risk_register.md#r-06--lab-access).

---

## Scheduling notes

- **The draft's "Semester 2: Implementation" does not survive this calendar.** Midterm is week 8 and needs prototype evidence; implementation starts week 4. See [DR-02](03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation).
- **Week 14 is Thanksgiving.** Do not schedule a milestone into it; treat it as the buffer that absorbs one slipped milestone.
- **Four major documents land in Semester 1** — proposal, SRS, SDD, Test Plan — all written outside class. That is the real workload, and it is why documentation needs a named owner.

---

**Related:** [`05_risk_register.md`](05_risk_register.md) · [`04_course_requirements.md`](04_course_requirements.md) · [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md) · [`../INDEX.md`](../INDEX.md)
