# Constraints

Things that are true **regardless of which ideas we pick**. Not ideas — those live in [`01_idea_register.md`](01_idea_register.md). Numbers are sourced in [`findings/`](findings/); this file is the summary.

The proposal's Problem Statement asks explicitly for constraints, and the draft's answer ("software and testing constraints, which ultimately lead to time constraints") is circular. This is the replacement.

---

## C-01 · Physical — payload

A Crazyflie-class microdrone has a payload margin measured in grams — **15 g on a 2.1/2.1+, 40 g on a Brushless**. That rules out lidar, GPR (0.9–1.2 kg minimum) and photogrammetry-grade optics *by mass alone*. Expansion decks are the practical sensing option.

> ⚠ **Corrected 2026-08-31.** An earlier version of this constraint also listed **thermal imaging** as ruled out by mass. **It is not** — a FLIR Lepton 3.5 is ~1 g and 140 mW (~1.8% of hover power), well inside the budget. Thermal's real limits are different: it does not range, is 160×120, is **opaque to glass**, and needs periodic flat-field shutter events that blank the image. Likewise **GNSS**: no GPS deck exists for the Crazyflie 2.x at all, so that one is an availability problem, not a mass problem. See [`findings/F08_lidar_and_sensors.md`](findings/F08_lidar_and_sensors.md).

**Power budget rule, to sit alongside the mass budget:** 250 mAh at 3.7 V over 7 min ⇒ ~7.9 W average. A 2 W sensor cuts endurance to ~5.6 min; a 0.1 W sensor costs essentially nothing.

**Consequence:** every mapping-flavored idea ([IR-11](01_idea_register.md#ir-11--lidar-disambiguation-for-glass-and-chain-link-fence), [IR-14](01_idea_register.md#ir-14--topographic-mapping-by-uav-with-sensor-fusion)–[IR-17](01_idea_register.md#ir-17--4d-mapping--change-detection-over-time)) is parked or future work purely because of this. Changing it means a different airframe, which means procurement and a semester of bring-up. → [`findings/F01_crazyflie_platform.md`](findings/F01_crazyflie_platform.md), [`findings/F08_lidar_and_sensors.md`](findings/F08_lidar_and_sensors.md)

## C-02 · Physical — flight time

Battery endurance bounds a single flight to minutes, and it is the hard limit on experiment design. Anything requiring a long continuous mission must be decomposed into repeatable short runs, or it cannot be tested.

**Consequence:** the evaluation harness ([IR-04](01_idea_register.md#ir-04--measurable-mission-and-evaluation-harness)) must support many short trials with automatic logging, not one long demo. Battery charging cycles, not compute, will set the iteration rate on flight-test days.

## C-03 · Physical — positioning volume

External positioning covers a bounded volume. Outside it, the drones have no usable position estimate.

**Consequence:** the mission must fit inside the tracked volume. "Fly to a distant waypoint" is not testable here. → [`findings/F01_crazyflie_platform.md`](findings/F01_crazyflie_platform.md)

## C-04 · Technical — localization regime

The lab's infrastructure is **indoor and external**: base-station tracking for the air, an overhead camera with fiducial markers for the ground. Neither works outdoors. GNSS works neither indoors nor underground.

**Consequence:** three regimes, and we must pick one deliberately because each implies a different sensor stack. We are in the indoor-external-tracking regime. Every idea premised on outdoors ([IR-19](01_idea_register.md#ir-19--under-canopy-vs-above-canopy-heterogeneous-operation)) or GPS-denied autonomy ([IR-12](01_idea_register.md#ir-12--cross-view-geo-localization-against-pre-cached-satellite-tiles), [IR-16](01_idea_register.md#ir-16--subterranean-mapping)) is out of regime.

## C-05 · Technical — two frames, one formation

Air and ground are tracked by *different* systems. Any residual misalignment between them is a **systematic** formation bias, not noise, so it does not average out and no controller can remove it.

**Consequence:** extrinsic calibration between the two frames is a prerequisite, not a nice-to-have. It is [IR-03](01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems) and likely the first integration milestone. → [`findings/F03_air_ground_integration.md`](findings/F03_air_ground_integration.md)

## C-06 · Technical — radio bandwidth ceiling

The radio link has a finite packet rate shared across the swarm, so per-agent update rate falls as agent count rises. This is the constraint that sets the maximum swarm size, and it is what the draft proposal was reaching for with "network throughput, delay."

**Consequence:** swarm size ([PD-04](03_decision_record.md#pending-decisions)) is a *derived* number, not a preference. Compute it from the required per-agent update rate. → [`findings/F04_network_and_latency.md`](findings/F04_network_and_latency.md)

## C-07 · Technical — 2.4 GHz is a shared band

The drone radio shares spectrum with campus Wi-Fi and everything else in the building. Interference is a lab reality and varies by time of day.

**Consequence:** test results are not repeatable unless the RF environment is recorded alongside them. Log link statistics with every trial. → [`findings/F04_network_and_latency.md`](findings/F04_network_and_latency.md)

## C-08 · Technical — onboard compute is very small

The flight controller is a microcontroller. The optional AI accelerator deck runs only tiny models. Anything larger runs on the ground station and crosses the radio, adding latency (C-06).

**Consequence:** "ML at the edge" is real but the edge is small, and that boundary is a design constraint to state up front rather than discover in Semester 2. → [`findings/F07_edge_ml.md`](findings/F07_edge_ml.md)

## C-09 · Compute — HPC GPUs are not rendering GPUs

The available H100 cluster is a compute part. Photoreal rendering and RTX-accelerated simulated sensors depend on ray-tracing hardware H100 lacks — NVIDIA states verbatim that *"GPUs without RT Cores (A100, H100) are not supported"* for Isaac Sim. **Precisely: this is a support boundary and a degradation, not a hardware lockout** — but on Hopper, Motion BVH is unavailable, which makes RTX-rendered lidar and radar not merely slow but *physically wrong*.

**Consequence:** if simulation ever enters scope, split it — render or generate data on RT-capable hardware, train on the H100s. Physics-only training over state and range observations needs no rendering and fits the cluster well. Verify what else the cluster has before assuming; many university clusters have a visualization partition. → [`findings/F09_simulation_and_compute.md`](findings/F09_simulation_and_compute.md)

## C-10 · Schedule — two semesters, and the first one is short

Fall 2026 runs **Aug 24 – Dec 9, 2026**. Proposal, SRS, System Design Document, System Test Plan, midterm presentation and a 10-minute video all land inside it, and documentation is homework done outside class.

**Consequence:** "Semester 2: Implementation" ([DR-02](03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation)) leaves no prototype for the midterm, which carries 15% for prototyping evidence. Implementation has to begin in Semester 1. → [`04_course_requirements.md`](04_course_requirements.md)

## C-11 · Schedule — shared lab and shared hardware

Flight hardware is departmental and shared. Lab access, other teams' setups and TA availability all gate testing. Materials cannot leave the lab, so no work happens at home on the hardware.

**Consequence:** software that can be developed and unit-tested off-hardware should be, so that lab time is spent on things that genuinely need the drones. This is the practical argument for a minimal software-in-the-loop path, independent of SLO 6.

## C-12 · Schedule — hardware failure stops everything

A crashed drone with no spare halts the project. This is the single most likely cause of a lost week.

**Consequence:** spares are a scope decision, not a shopping decision ([PD-05](03_decision_record.md#pending-decisions)). Even at zero budget, ask what spares the lab holds.

## C-13 · Team — four people, five roles, all still taking classes

Roles are ownership, not exclusive assignment. Everyone still does engineering work.

**Consequence:** parallelizable work must be identified early. Documentation is a graded deliverable stream in its own right and needs an owner.

## C-14 · Process — learning outcomes constrain the design

**SLO 5** requires prototyping an embedded computing system: a pure ground-station orchestrator does not satisfy it, so some work must land on the drone firmware or a deck. **SLO 6** names computer simulation explicitly alongside physical experiments, so the proposal should not claim to avoid simulation entirely — it should say what each is used for.

**Consequence:** both are design constraints, not paperwork. → [`04_course_requirements.md`](04_course_requirements.md#student-learning-outcomes-map-deliverables-to-these)

## C-15 · Safety and regulatory

Lab policy: check before energizing, work within training, protect people before hardware, report problems immediately. Indoor flight in a bounded volume is the safest regime available and is one more reason to stay in it. Regulatory applicability is genuinely different indoors versus outdoors and should be stated correctly rather than name-dropped. → [`findings/F05_standards_and_regulations.md`](findings/F05_standards_and_regulations.md)

---

## Summary for the proposal

The Problem Statement's constraints paragraph should say, in one sentence each:

- **Physical:** payload margin in grams, flight time in minutes, bounded tracking volume.
- **Technical:** two localization frames to reconcile, a shared-radio bandwidth ceiling that caps swarm size, microcontroller-class onboard compute.
- **Schedule:** two semesters with all major documentation in the first, shared lab access, and no work possible off-site.

---

**Related:** [`01_idea_register.md`](01_idea_register.md) · [`03_decision_record.md`](03_decision_record.md) · [`04_course_requirements.md`](04_course_requirements.md) · [`../INDEX.md`](../INDEX.md)
