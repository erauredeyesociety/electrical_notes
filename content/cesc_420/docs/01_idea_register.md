# Idea Register

All project ideas raised, with status and reasoning. **Nothing is deleted.** Rules: [`00_meta_idea_register.md`](00_meta_idea_register.md). No cost figures — see [`../proposal/PROPOSAL_GAP_ANALYSIS.md`](../proposal/PROPOSAL_GAP_ANALYSIS.md) §Budget.

Source of entries IR-01 … IR-20: [`../init_transcript.md`](../init_transcript.md).

| Status | Count |
| --- | ---: |
| Selected | 5 |
| Stretch | 3 |
| Parked | 5 |
| Future work | 5 |
| Rejected | 4 |

---

## Selected — in current scope

### IR-01 · Heterogeneous air-ground formation control

**Problem:** A team of aerial and ground robots must hold a useful geometric formation while moving through a mission, but the two vehicle classes do not share mobility, endurance, sensing, or localization.
**Why it's a problem:** Aerial and ground agents are localized by *different* systems (Lighthouse base stations vs overhead-camera fiducials), so their position estimates live in different coordinate frames with different error characteristics and different latencies. Formation control assumes a common frame; getting one is an engineering problem in its own right. Asymmetric dynamics mean a formation law tuned for one class destabilizes the other.
**Concepts involved:** consensus / graph-Laplacian control, leader–follower, virtual structure, extrinsic frame calibration, ROS 2 TF trees, clock synchronization, formation-error metrics.
**Status:** **Selected** — this is the project. → [`findings/F02_formation_control.md`](findings/F02_formation_control.md), [`findings/F03_air_ground_integration.md`](findings/F03_air_ground_integration.md)

### IR-02 · Communication-constrained coordination

**Problem:** Coordination degrades as the radio link degrades, and the team's own problem statement names throughput, delay, and computational effort as the difficulty.
**Why it's a problem:** The Crazyradio link has a hard packet-rate ceiling shared across all drones on a dongle, so per-agent update rate falls as the swarm grows. Latency and loss enter the control loop directly. The 2.4 GHz band is shared with campus Wi-Fi, so interference is a lab reality, not a hypothetical.
**Concepts involved:** bandwidth budgeting per agent, centralized vs decentralized vs CTDE architectures, DDS/ROS 2 QoS, graceful degradation under loss, peer-to-peer messaging between agents.
**Status:** **Selected** — needs a measurable requirement in the SRS. → [`findings/F04_network_and_latency.md`](findings/F04_network_and_latency.md)

### IR-03 · Unified coordinate frame across two localization systems

**Problem:** Air uses Lighthouse; ground uses an overhead camera with ArUco tags. Neither knows about the other.
**Why it's a problem:** Any residual rotation or translation between the two frames appears as a constant formation bias that no controller can remove, because each agent is correctly tracking its own frame. Error is systematic, not noise, so averaging does not help.
**Concepts involved:** extrinsic calibration via a common fiducial, hand-eye style calibration, TF tree design, time synchronization, covariance-aware fusion.
**Status:** **Selected** — likely the first real integration milestone. → [`findings/F03_air_ground_integration.md`](findings/F03_air_ground_integration.md)

### IR-04 · Measurable mission and evaluation harness

**Problem:** Without defined metrics the project cannot show it worked, and the System Test Plan needs a traceability matrix mapping requirements to tests.
**Why it's a problem:** "The swarm flew in formation" is not a result. Formation error, convergence time, coverage completeness, message loss and control-loop jitter are, and they must be logged automatically or they will not be collected.
**Concepts involved:** RMS formation error, convergence/settling time, coverage percentage, mission completion time, automated logging and replay, repeatability across trials.
**Status:** **Selected** — build the harness early; it feeds midterm, final, poster and video evidence. → [`findings/F02_formation_control.md`](findings/F02_formation_control.md)

### IR-23 · Performance benchmarking and instrumentation harness

**Problem:** The team's own problem statement asserts that network throughput, delay and computational effort are what make heterogeneous coordination hard — but an assertion is not evidence. Nothing currently measures any of the three.

**Why it's a problem:** Benchmarking is **measurement, not prediction**, and it is the only way to compare implementations once they are past algorithmic differences. Big-O predicts the *shape* of a scaling curve; it says nothing about the constant, and the constant is where cache behavior, branch prediction and allocation live. Simulation cannot settle small deltas either, because a simulator's timing model carries more uncertainty than the difference being measured. Two optimized implementations of the same algorithm are therefore distinguishable *only* by running the real compiled code on the real hardware and measuring it.

**The symmetric caveats, recorded so we do not overclaim:** (a) a benchmark measures a *system* — this binary, these flags, this kernel, this CPU at this thermal state, this RF environment — not a *program*, so results are conditional and not portable; (b) measurement without bias control is not measurement, since repetitions shrink noise but not bias; and (c) **detecting a 1–2% difference needs 78–318 runs, which flight hours cannot supply** — so the methodology is a hybrid with simulation, not a rejection of it. See [DR-05](03_decision_record.md#dr-05--benchmarking-is-measurement-not-simulation).

**Concepts involved:** cycle-accurate timing on the MCU, control-loop period and jitter measurement, message latency percentiles rather than means, packet-rate and loss instrumentation on the radio link, profiling to separate CPU-bound from lock-bound from scheduler-delay, empirical scaling curves versus agent count, and regression tracking across the two semesters.

**Why it earns its place in *this* project specifically:**

1. It converts the Problem Statement from an assertion into an evidence-backed claim — directly worth points on a 24% section that currently has none.
2. The SRS requires measurable non-behavioral requirements; a threshold you cannot measure is not a requirement.
3. The System Test Plan's traceability matrix needs pass/fail criteria — performance benchmarks *are* the test cases for performance requirements.
4. It produces demonstrable prototype evidence for the midterm (15%) **without a single drone flying**, which de-risks the whole schedule against [C-11](02_constraints.md#c-11--schedule--shared-lab-and-shared-hardware) and [C-12](02_constraints.md#c-12--schedule--hardware-failure-stops-everything).

**Status:** **Selected** — and it is the answer to the simulation tension in [DR-05](03_decision_record.md#dr-05--benchmarking-is-measurement-not-simulation). → [`findings/F10_benchmarking_and_measurement.md`](findings/F10_benchmarking_and_measurement.md)

---

## Stretch — in scope only if the baseline lands early

### IR-05 · Cooperative coverage / survey mission

**Problem:** Sweeping a sensor field over an area while maintaining formation, rather than just holding formation in place.
**Why it's a problem:** Coverage and formation-keeping pull against each other — the geometry that maximizes sensor overlap is not the geometry that is easiest to hold. Adds a planning layer above the control layer.
**Concepts involved:** boustrophedon/lawnmower decomposition, Voronoi coverage control, task allocation, sensor footprint modeling.
**Status:** **Stretch** — the natural extension of the mentor's mission sequence, and scores against the Functionality rubric's advanced tier.

### IR-06 · Aerial agent as communication relay for ground agents

**Problem:** Ground agents lose line-of-sight links; an aerial agent repositions to restore connectivity.
**Why it's a problem:** The relay's optimal position is a function of link quality, which changes as the ground agents move — so it is a coupled control-and-communication problem, not a fixed waypoint. Published UAV-relay measurements show link quality varying with height as well as distance.
**Concepts involved:** connectivity maintenance, algebraic connectivity (Fiedler value) as a control objective, RSSI-driven positioning.
**Status:** **Stretch** — strong demo, defensible scope. Depends on IR-02.

### IR-07 · Aerial agent as overhead perception for ground agents

**Problem:** A ground robot cannot see past the obstacle in front of it; an aerial agent can.
**Why it's a problem:** Transferring an aerial observation into a ground agent's action requires the shared frame from IR-03 plus a shared map representation, and the aerial view's usefulness decays with altitude and tilt.
**Concepts involved:** occupancy grids, view planning, cross-agent map merging.
**Status:** **Stretch** — depends on IR-03 landing cleanly.

---

## Parked — sound, wrong semester or wrong hardware

### IR-08 · ML-enhanced single-drone navigation (the original preference)

**Problem:** Learning a navigation policy for cluttered space from range sensing.
**Why it's a problem:** No labels exist — only a reward and experience — so training needs millions of collisions, which is only affordable in simulation. That makes sim-to-real gap analysis the actual deliverable.
**Concepts involved:** RL over range-sensor observations, domain randomization (obstacle density, sensor noise, latency, mass, thrust), Multi-ranger deck as the real-world observation space.
**Status:** **Parked** — this was the alternative project ([DR-01](03_decision_record.md#dr-01--project-selected-heterogeneous-drone-swarm)). Retained because the Functionality rubric credits advanced features "listed or not in SRS or proposal." Trigger to revive: baseline formation control demonstrated by midterm.

### IR-09 · Two-level hierarchy — learned swarm layer over learned agent layer

**Problem:** Coordinating a swarm and controlling an individual agent are different timescales and different information sets.
**Why it's a problem:** The hard part is not the models but the **interface** between them — whether the swarm layer emits formation slots, virtual-leader poses, or per-agent waypoints. That choice defines the action space above and the goal input below, and changing it later invalidates both. Joint end-to-end training of a hierarchy has a notoriously bad debugging story.
**Concepts involved:** hierarchical RL, CTDE (centralized training, decentralized execution), freezing the lower policy and training the upper one against it.
**Status:** **Parked** — depends on IR-08. If revived, train the levels separately.

### IR-10 · ML at the edge, onboard the drone

**Problem:** Running inference onboard rather than streaming to a ground station.
**Why it's a problem:** The available onboard accelerator is very small, which bounds model size hard; anything larger must run on the ground station and cross the radio, adding the latency IR-02 is about.
**Concepts involved:** AI-deck / GAP8 class accelerators, quantization, tiny CNNs, latency budgeting across the radio link.
**Blocker found 2026-08-31:** the **AI-deck and the Lighthouse deck conflict on UART1** (Bitcraze deck-compatibility matrix, note 4 — the GAP8 module is on UART1). Since all indoor positioning is Lighthouse, onboard vision on a Lighthouse-localized Crazyflie is blocked until this is resolved. No alternate positioning deck dodges it. **Check in the first lab visit.**
**Status:** **Parked** — the team has prior research here. Only relevant if a perception task enters scope, and gated on the UART1 conflict. → [`findings/F07_edge_ml.md`](findings/F07_edge_ml.md)

### IR-11 · Lidar disambiguation for glass and chain-link fence

**Problem:** Lidar returns near glass and mesh structures are wrong in structured, repeatable ways, and downstream mapping treats them as real geometry.
**Why it's a problem:** Three distinct mechanisms, often conflated. (a) *Mixed pixels* — the beam is a diverging cone, so when its footprint straddles an edge or a thin structure the reported range blends multiple surfaces. (b) *Specular behavior at glass* — depending on incidence angle, material and thickness, you get no return at all or a mirrored ghost of the scene. (c) *Internal glare* in compact solid-state arrays — light from bright or retroreflective surfaces scatters inside the sensor and spreads across the pixel array, producing phantom objects. Labeling is the real obstacle: to label glass you must already know where the glass is.
**Concepts involved:** return-intensity gating, multi-echo/full-waveform returns, plane fitting from surveyed control points as a free auto-labeling scheme, polarization imaging as a complementary modality at large incidence angles.
**Status:** **Parked** — genuinely interesting, and there is a workable labeling strategy, but no lidar flies on the current platform. → [`findings/F08_lidar_and_sensors.md`](findings/F08_lidar_and_sensors.md)

### IR-12 · Cross-view geo-localization against pre-cached satellite tiles

**Problem:** A drone with a downward camera determines its position by matching against pre-cached overhead imagery, without GPS.
**Why it's a problem:** Viewpoint, scale, season and time-of-day all differ between the drone view and the cached tile, so naive image matching fails. It is a named research area with public benchmarks, which is unusual and useful.
**Concepts involved:** cross-view retrieval, public orthoimagery as training data, GPS logs as free labels, published datasets (CVUSA, CVACT, University-1652, VIGOR) as baselines.
**Status:** **Rejected (scope)** — *downgraded from Parked on 2026-08-31.* The "labels are free when you fly with GPS" argument, which was the entire reason this looked well-de-risked, **does not hold on this hardware: Bitcraze offers no GPS deck for the Crazyflie 2.x**, and the lab's positioning is indoor Lighthouse. There is no satellite tile to pair a frame against, so there is no free label — and the AI-deck camera is monochrome. Pursuing it needs a different airframe, outdoor flight authorization and a different camera: an entire second platform. Recorded as **structurally inapplicable to the available hardware**, not merely out of scope. → [`findings/F07_edge_ml.md`](findings/F07_edge_ml.md)

### IR-13 · Mutual interference between lidars in a swarm

**Problem:** Multiple lidars operating in the same volume can trigger on each other's pulses.
**Why it's a problem:** It is a swarm-specific failure that does not appear in single-robot testing, so it would be discovered late.
**Concepts involved:** pulse coding, time-division scheduling, per-unit timing dither.
**Status:** **Parked** — only relevant if IR-11 or a lidar-carrying swarm is revived. → [`findings/F08_lidar_and_sensors.md`](findings/F08_lidar_and_sensors.md)

---

## Future work — proposal §Future Work, not the build

### IR-14 · Topographic mapping by UAV with sensor fusion

**Problem:** Producing georeferenced terrain models from a flying platform.
**Why it's a problem:** Requires a payload class, an outdoor localization regime and an accuracy standard that none of the current lab infrastructure provides.
**Concepts involved:** photogrammetry, structure-from-motion, GNSS/INS fusion, mapping accuracy standards.
**Status:** **Future work** — the "pie in the sky" framing. Good for the proposal's motivation section.

### IR-15 · 3D interior capture with an overlapping multi-camera rig

**Problem:** Capturing building interiors — the real-estate case — where the vehicle genuinely moves in 3D rather than a 2D plane at fixed altitude.
**Why it's a problem:** Flying a lawnmower pattern at constant altitude is a 2.5D problem; traversing rooms and doorways is true 3D with no GNSS and no consistent sky view. A rig covering all directions with overlapping fields of view is a payload and calibration problem before it is an algorithms problem.
**Concepts involved:** multi-camera extrinsic calibration, overlap and baseline planning, visual-inertial odometry indoors.
**Status:** **Future work.**

### IR-16 · Subterranean mapping

**Problem:** Mapping tunnels, mines and voids where GNSS is unavailable.
**Why it's a problem:** The GPS-denied case is the hardest localization regime and also the most interesting one; drift accumulates with no global correction, and comms attenuate.
**Concepts involved:** lidar/visual-inertial SLAM, loop closure, tethered or relayed comms.
**Status:** **Future work.**

### IR-17 · 4D mapping — change detection over time

**Problem:** "4D" is time-series mapping, which is really *change detection* between repeat surveys.
**Why it's a problem:** Distinguishing real change from registration error is the whole problem. The standard method assumes locally planar surfaces and uniform registration error; on natural surfaces that overestimates what can be detected. The error-propagation variant matters here specifically because it allows combining datasets of *different* accuracies — multiple platforms, multiple sensors — without degrading the detection limit, which is exactly the heterogeneous-swarm case.
**Concepts involved:** M3C2 and M3C2-PM, level of detection, registration error propagation.
**Status:** **Future work** — but naming change detection out loud is what makes "4D" sound rigorous instead of vague. Worth one sentence in the proposal.

### IR-18 · Ground-penetrating radar for subsurface sensing

**Problem:** Seeing *through* soil, which is what "subterranean mapping" sometimes actually means.
**Why it's a problem:** It is a completely different sensor modality with its own airframe, power and processing requirements.
**Concepts involved:** GPR, radargram interpretation, ground coupling.
**Status:** **Future work** — recorded as the correct answer to the question sonar was wrongly asked ([DR-03](03_decision_record.md#dr-03--sonar-removed-from-the-concept)).

### IR-19 · Under-canopy vs above-canopy heterogeneous operation

**Problem:** Forest operations need sensing under the canopy and communications above it.
**Why it's a problem:** Dense-forest networks are limited by signal attenuation as a first-order effect, and the position that is good for sensing is not the position that is good for relaying. That incompatibility is a stronger argument for heterogeneity than "air and ground are complementary."
**Concepts involved:** attenuation modeling, relay placement, role specialization within a swarm.
**Status:** **Future work** — the outdoor version of IR-06.

---

## Rejected

### IR-20 · Sonar for aerial mapping — **Rejected (physics)**

In air, "sonar" is an ultrasonic rangefinder: metres of range, a wide cone, effectively no bearing resolution. It is an altimeter, not a mapping sensor. Real sonar mapping (side-scan, multibeam) means an underwater vehicle. If the goal was seeing through dirt, the sensor is GPR — see IR-18. → [DR-03](03_decision_record.md#dr-03--sonar-removed-from-the-concept)

### IR-21 · Learned lidar denoising as a headline contribution — **Rejected (scope)**

Statistical and radius outlier removal, voxel filtering and intensity gating handle most general lidar noise, and a learned denoiser needs labeled ground truth the team would not have. The honest baseline comparison would likely show the classical filter is fine.
**Note the split:** this is *general* denoising. The *structured* failures — glass, mesh, grass — are a different problem with a real labeling strategy, kept alive as IR-11.

### IR-22 · Cascadeur in the toolchain — **Rejected (scope)**

Character animation package for humanoids and creatures. Nothing in it applies to this domain.

---

## Open slots

Add new ideas here with the next free `IR-##`. Constraints are not ideas — they go in [`02_constraints.md`](02_constraints.md).

---

**Related:** [`00_meta_idea_register.md`](00_meta_idea_register.md) · [`02_constraints.md`](02_constraints.md) · [`03_decision_record.md`](03_decision_record.md) · [`findings/`](findings/) · [`../INDEX.md`](../INDEX.md)
