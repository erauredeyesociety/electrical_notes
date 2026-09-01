# Decision Record

Chronological log of decisions and their reasons. Append only. Format rules in [`00_meta_idea_register.md`](00_meta_idea_register.md).

---

## DR-01 — Project selected: heterogeneous drone swarm

**Date:** 2026-08 (pre-proposal)
**Decision:** Team takes the **drone swarm** project (Dr. Juan Calderon Chavez), not the reinforcement-learning drone project (Dr. Ilhan Akbas).
**Decided by:** team consensus.

**Alternative considered:** ML/RL single-drone navigation in Isaac Sim, with sim-to-real transfer to a Crazyflie.

**Why swarm won:** inherits working lab infrastructure (Crazyflie + Lighthouse for air, overhead camera + ArUco for ground), so Semester 1 is not consumed by procurement and bring-up.

**Recorded dissent:** the log's author preferred the ML project. Per team-decision policy, that preference is noted and the swarm direction is supported. The ML ideas are not discarded — they are registered as `Parked` / `Stretch` in [`01_idea_register.md`](01_idea_register.md) so they remain available as enhancements, which the [Project Functionality Rubric](04_course_requirements.md#project-functionality) rewards at 20% for advanced/innovative features.

**Consequence:** the grand mapping vision (topographic mapping, photogrammetry, subterranean SLAM, 4D change detection) becomes *problem-domain framing and future work*, not the build. See [`01_idea_register.md`](01_idea_register.md) §Future work.

---

## DR-02 — Semester 1 favors real hardware over simulation

**Date:** 2026-08 (stated in draft proposal)
**Decision:** "Testing and research, avoiding simulations as much as possible to gain real time experience."

**Risk this creates:** hardware-only iteration is slow, and a crashed Crazyflie stops all work. See [`02_constraints.md`](02_constraints.md).
**Mitigation to write into the proposal:** a minimal software-in-the-loop path for the coordination logic only, so algorithm bugs are found off-hardware. This is not "doing simulation" — it is unit-testing the control stack.

**Open:** needs mentor confirmation. See [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md).

---

## DR-03 — Sonar removed from the concept

**Date:** 2026-08
**Decision:** `Rejected (physics)`. In air, "sonar" is an ultrasonic rangefinder: metre-scale range, wide cone, effectively no bearing resolution. It is an altimeter, not a mapping sensor.
**If the real goal was subsurface sensing,** the sensor is ground-penetrating radar, which is its own project. Recorded as `Future work`.

---

## DR-05 — Benchmarking is measurement, not simulation

**Date:** 2026-08-31
**Decision:** Build a performance benchmarking and instrumentation harness as a first-class deliverable ([IR-23](01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness)).

**The distinction that motivates it:** simulation *predicts* behavior from a model; benchmarking *measures* real compiled code on real hardware. They are different epistemic activities, and conflating them is what made [DR-02](#dr-02--semester-1-favors-real-hardware-over-simulation) look like it conflicted with SLO 6.

**Why simulation cannot substitute here:** a simulator's timing model carries uncertainty larger than the performance differences worth optimizing. Simulation can reveal an order-of-magnitude improvement; it cannot adjudicate between two hyper-optimized implementations, because the difference is smaller than the model error. Once two implementations share an algorithm, they differ only in constant factors — cache behavior, branch prediction, allocation, instruction-level parallelism — none of which are visible in source code, in complexity analysis, or in a simulator's timing approximation.

**What each method is actually good for:**

| Method | Answers | Cannot answer |
| --- | --- | --- |
| Complexity analysis | How does cost *scale* with N? | What is the constant? Where does the curve bite? |
| Simulation | Does the logic behave correctly? Large-scale feasibility? | Small timing deltas on real hardware |
| **Benchmarking** | What does *this build* cost on *this hardware*? | Whether the result transfers to other hardware |

**Consequence — this resolves DR-02 cleanly.** The proposal should not say "we avoid simulation." It should say: *hardware measurement is the primary evidence base; software-in-the-loop is used to unit-test coordination logic before flight; and a benchmarking harness quantifies the throughput, latency and computational-effort claims made in the problem statement.* That satisfies SLO 6 honestly, without retreating from the team's stated preference for real experience.

**Three constraints that come with it,** recorded so we do not overclaim in the final report:

1. **A benchmark measures a *system*, not a *program*.** Every number must carry its measurement conditions — build flags, kernel, CPU governor, agent count, RF environment, battery state — or it is not reproducible. Measured evidence: an *unused* environment variable moved a benchmark result by 11.7% on 2026 hardware.
2. **Measurement without bias control is not measurement.** More repetitions shrink *noise* as 1/√n but do not shrink *bias* at all — a tight confidence interval is fully compatible with a wrong answer.
3. ⚠ **This forces a hybrid methodology, and it partially reverses [DR-02](#dr-02--semester-1-favors-real-hardware-over-simulation).** Detecting a 1–2% difference at the measured coefficient of variation requires **78–318 runs**. **You cannot fly a swarm 300 times; you can simulate it 300 times.** Simulation wins on repeatability, observability and sample size, so it is not an inferior substitute for hardware — it answers a different question. The honest position is *fidelity versus control*, not *predict versus measure*: a cycle-accurate simulator measures a model and inherits its biases (demonstrated by Mytkowicz et al., whose measurement bias appeared inside the m5 simulator itself).

**Revised statement for the proposal:** hardware measurement is the primary evidence base for end-to-end system claims; software-in-the-loop unit-tests coordination logic before flight; and where a claim needs a sample size that flight hours cannot supply, that is stated explicitly rather than papered over with too few trials. → [`findings/F10_benchmarking_and_measurement.md`](findings/F10_benchmarking_and_measurement.md)

---

## DR-04 — Documentation set rebuilt in this repository

**Date:** 2026-08-31
**Decision:** The register and findings documents referenced in [`../init_transcript.md`](../init_transcript.md) were produced in a prior session and did not persist to disk. They are rebuilt here under `content/cesc_420/docs/`, in Markdown, as the single source of truth.

---

## Pending decisions

| ID | Decision needed | Blocks |
| --- | --- | --- |
| PD-01 | Project name — `X_swarm` is a placeholder | Proposal §Project Name (2%) |
| PD-02 | Team roles (PM, systems, implementation, test, documentation) | Proposal, and weekly progress checks |
| PD-03 | Air-only vs air+ground for the graded baseline | Proposal §Proposed Solution (45%) |
| PD-04 | Swarm size target — N drones, M ground vehicles | SRS requirements table |
| PD-05 | Whether ground vehicles exist in the lab or must be built | Budget (10%) |

Details and the questions to ask in [`../proposal/OPEN_QUESTIONS.md`](../proposal/OPEN_QUESTIONS.md).

---

**Related:** [`01_idea_register.md`](01_idea_register.md) · [`02_constraints.md`](02_constraints.md) · [`../INDEX.md`](../INDEX.md)
