# Risk Register

Capstone risks with owners, triggers and mitigations. The Midterm rubric awards 20% for *"Technical Feasibility & Planning — major technical challenges; identifies mitigation steps"*, and the System Test Plan template has a Testing Risks and Contingencies section. This file feeds both.

**Scoring:** Likelihood (L) and Impact (I) each 1–5; Score = L × I. Anything ≥ 12 needs an active mitigation now, not a plan to mitigate later.

---

## Active risks

| ID | Risk | L | I | Score | Owner |
| --- | --- | ---: | ---: | ---: | --- |
| R-01 | Drone destroyed with no spare → all flight work stops | 4 | 5 | **20** | TBD |
| R-02 | Scope is too large; nothing is finished well | 4 | 5 | **20** | PM |
| R-03 | Ground vehicles don't exist / aren't working | 3 | 5 | **15** | Systems |
| R-04 | Frame calibration between air and ground is harder than expected | 4 | 4 | **16** | Systems |
| R-05 | Radio bandwidth caps swarm size below what we promised | 3 | 4 | **12** | Systems |
| R-06 | Lab access is the bottleneck, not engineering | 4 | 3 | **12** | PM |
| R-07 | Documentation slips because it's "outside class" work | 4 | 3 | **12** | Docs lead |
| R-08 | Inherited codebase is undocumented or broken | 3 | 4 | **12** | Impl. lead |
| R-09 | Mentor availability / requirement drift | 2 | 4 | 8 | PM |
| R-10 | 2.4 GHz interference makes results non-repeatable | 3 | 3 | 9 | Test lead |
| R-11 | Team member unavailable (illness, workload, withdrawal) | 2 | 4 | 8 | PM |
| R-12 | Integration deferred to the end; subsystems never meet | 3 | 5 | **15** | Systems |
| R-13 | No measurable results to show at midterm | 3 | 4 | **12** | Test lead |
| R-14 | Battery logistics throttle the experiment rate | 4 | 2 | 8 | Test lead |

---

## Mitigations for score ≥ 12

### R-01 · Hardware loss

**Trigger:** any unrecoverable crash.
**Mitigate:** confirm what spares the lab holds *before* the proposal ([PD-05](03_decision_record.md#pending-decisions)); fly inside a net or over a soft surface; cap altitude and speed during development; keep one airframe designated as the known-good reference and never fly it during algorithm bring-up. Keep the benchmarking and ground-station work ([IR-23](01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness)) genuinely independent of flight so a grounded fleet does not idle the team.

### R-02 · Scope

**Trigger:** the proposal promises more than one demonstrable mission.
**Mitigate:** the proposal's *out-of-scope* list is the mitigation, and it is graded. Commit to one baseline mission; everything else is a stretch goal explicitly labelled as such. Recommendation in [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md) [PD-03]: air-only formation as the Semester 1 baseline, air+ground as the Semester 2 target.

### R-03 · Ground vehicles

**Trigger:** first mentor meeting reveals nothing usable exists.
**Mitigate:** ask in week 1, not week 8 — question 2 in [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md). **Contingency:** if no ground platform exists, the project becomes air-only formation with a *simulated* or *teleoperated* ground agent standing in at the interface, so the coordination work still lands. Decide this before the proposal, because it changes the Problem Statement.

### R-04 · Frame calibration

**Trigger:** persistent constant offset in formation error that tuning does not remove.
**Mitigate:** treat it as its own milestone with its own acceptance test, scheduled early ([IR-03](01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems)). Measure and report the residual explicitly rather than hiding it in controller gains — a characterized bias is a result; an unexplained one is a bug. Ask whether prior teams already did this.

### R-05 · Bandwidth ceiling

**Trigger:** per-agent update rate falls below the control requirement as agents are added.
**Mitigate:** derive swarm size from a measured bandwidth budget rather than picking a number ([`findings/F04_network_and_latency.md`](findings/F04_network_and_latency.md)). Measure the ceiling early with the benchmarking harness — this is exactly the kind of claim [IR-23](01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness) exists to settle. State the measured maximum in the SRS as a derived constraint, so the project is *characterizing* a limit rather than *failing* to meet an arbitrary target.

### R-06 · Lab access

**Mitigate:** book lab time as a recurring team commitment. Do everything that does not need hardware off-hardware — this is the practical argument for software-in-the-loop and for the benchmark harness, independent of [SLO 6](04_course_requirements.md#student-learning-outcomes-map-deliverables-to-these). Arrive at the lab with a written test script; never debug design questions during flight time.

### R-07 · Documentation slip

**Trigger:** a deliverable is started the week it is due.
**Mitigate:** documentation is a graded stream with a named owner, and the SRS/SDD/Test Plan are largely writable *before* implementation is finished. The decision record and engineering notebook must be written as events happen — the Final rubric awards 20 of 50 points for Lessons Learned and Future Plans, which cannot be reconstructed in December.

### R-08 · Inherited codebase

**Trigger:** the handover repository does not build.
**Mitigate:** make "clone, build, fly one drone, land it" the *first* milestone, before any design work. If it takes more than a week, that is data for the mentor, not a private struggle.

### R-12 · Late integration

**Trigger:** week 10 with subsystems that have never run together.
**Mitigate:** define subsystem interfaces in the SDD and stub every one of them from day one, so an end-to-end path exists early even if each stage is trivial. Schedule an integration checkpoint before the midterm, not after.

### R-13 · Nothing to show at midterm

**Trigger:** week 7 with no measurements.
**Mitigate:** the benchmarking harness produces reportable numbers without flight, and the Midterm rubric explicitly accepts *"clear requirements if the project is still in very early stage"* as prototyping evidence. Both are hedges — but a measured latency histogram is a far better slide than a requirements table.

---

## Review cadence

Re-score at each sprint boundary. Add new risks as they surface; keep closed risks with their outcome, since realized risks and how the team adapted are worth 10 points on the Final presentation.

---

**Related:** [`02_constraints.md`](02_constraints.md) · [`06_semester1_schedule.md`](06_semester1_schedule.md) · [`03_decision_record.md`](03_decision_record.md) · [`../INDEX.md`](../INDEX.md)
