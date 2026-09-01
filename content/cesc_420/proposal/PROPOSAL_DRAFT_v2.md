# Project Proposal — Draft v2

> **Working document, not the submission.** Rewrite of [`../MOCK_PROPOSAL.pdf`](../MOCK_PROPOSAL.pdf) against the rubric in [`../canvas_materials/Project Proposal Template_rubric.pdf`](../canvas_materials/Project%20Proposal%20Template_rubric.pdf).
>
> **`⟦MENTOR⟧`** = needs Dr. Calderon Chavez. **`⟦COUNT⟧`** = needs a lab inventory. **`⟦TEAM⟧`** = team decision.
> Both classes of marker must be resolved before submission — see [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md). Every technical number traces to [`../docs/findings/`](../docs/findings/).

---

## Project Name (2%)

**⟦TEAM⟧ `HALO` — Heterogeneous Air-Ground Localization and Orchestration**

*(`X_swarm` is a placeholder. Alternatives: `TANDEM`, `SwarmBridge`, `CoFly`. Pick one and use it consistently across all four documents.)*

---

## Project Team Members (4%)

| Member | Role |
| --- | --- |
| Emmett Gilbert | ⟦TEAM⟧ |
| Gatlin Nelson | ⟦TEAM⟧ |
| DeAndre Johnney | ⟦TEAM⟧ |
| Nicholas Schultz | ⟦TEAM⟧ |

Roles per the Day-1 slides: Project Manager/Scrum Lead · Systems & Technical Lead · Design/Implementation Lead · Testing & Validation Lead · Documentation & Communication Lead. Roles define ownership, not boundaries — every member does engineering work.

*Verify spellings against the roster before submission.*

---

## Problem Statement (24%)

### What is the problem?

Aerial and ground robots have complementary capabilities, but making them operate as **one coordinated team** requires reconciling vehicles that do not share mobility, endurance, sensing, or — critically — a common notion of where they are. We are building and characterizing a heterogeneous air-ground robot team that holds a commanded formation while executing a mission, and we are quantifying the communication and localization limits that bound how well it can be done.

### Why is it a problem?

Four reasons, each structural rather than an implementation difficulty:

**1. The two vehicle classes do not share a state space.** A ground robot is a nonholonomic SE(2) system with two controllable degrees of freedom; a quadrotor is an underactuated SE(3) system. A single formation law cannot be written across both without an explicit mapping between them [1], [2].

**2. They do not share a coordinate frame.** Aerial agents are localized by infrared base-station tracking computed onboard; ground agents by an overhead camera detecting fiducial markers, computed off-board. Each system's origin is defined arbitrarily by its own calibration procedure, with no intrinsic relationship to the other. Any residual misalignment appears as a **systematic** formation bias that no controller can remove, because each agent is correctly tracking its own frame. One degree of residual yaw misalignment produces 52 mm of lateral error at 3 m and 87 mm at 5 m — already larger than the aerial positioning system's own 2–4 cm accuracy [3]. Cross-modal registration between air and ground sensing is treated as an open problem in the literature [4].

**3. Pose freshness differs architecturally, not by tuning.** The aerial estimate is computed onboard and needs no radio link to arrive; the ground estimate must traverse detection and network transport before any controller sees it. At 30 fps the overhead pose is already one frame interval (33.3 ms) stale before transport, during which an agent at 1 m/s travels 33 mm. This asymmetry cannot be removed by buying a faster camera.

**4. Communication is a hard, quantifiable ceiling — not a vague concern.** The radio serving the aerial agents has a firmware-limited packet rate shared across every drone on it, so per-agent update rate falls as the swarm grows [5], [6]. Published measurements on comparable hardware show end-to-end latency growing linearly with swarm size to 26 ms at 49 vehicles [6]. Consensus theory gives an exact bound: for a fixed communication graph, agreement is reached **if and only if** delay τ < π/(2·λ_max(L)), where λ_max is the largest Laplacian eigenvalue of the communication graph [7]. And loss statistics matter more than loss rates — simulation of formation control under *bursty* (Gilbert) loss showed maximum agent error rising from 0.41 m to 0.83 m in an easy scenario and to complete formation collapse with collisions in a cluttered one, while i.i.d. loss at the same average rate was nearly harmless [8]. **Average packet loss is the wrong requirement; burst length is what breaks formation control.**

Recent surveys identify disparities in communication protocols, sensor interoperability, and autonomy frameworks — rather than the coordination control law itself — as the persistent integration challenge in heterogeneous UAV-UGV systems [9]. Notably, **no published work fuses these two specific localization modalities into a single common frame**, so the residual calibration error of this pairing is unmeasured. The closest published system to ours was validated only in simulation [10].

### Constraints

**Physical.** Aerial payload margin is 15 g (40 g on the brushless airframe) against a 29–34 g takeoff weight; flight endurance is 7–10 minutes against a 40–60 minute recharge; the tracked flight volume is approximately 8 × 8 × 3 m ⟦COUNT⟧ [11]. Downwash requires ~0.3 m vertical separation between aerial agents against 0.12 m horizontally [12], and the whole formation's speed ceiling is set by the ground platform ⟦COUNT⟧.

**Technical.** Two independently-calibrated localization frames must be reconciled. The shared radio ceiling is approximately 1000–1200 packets/s divided among all connected aerial agents [5], and 30 bytes is the maximum payload of a single command packet. Onboard compute is a 168 MHz microcontroller with 192 kB of RAM. The 2.4 GHz band is shared with campus Wi-Fi, and the drone radio has no true RSSI — only a 1-bit power detector — so interference must be characterized externally.

**Schedule.** Two semesters, with the proposal, SRS, System Design Document, System Test Plan, midterm presentation and video all falling in the first. Flight hardware is departmental, shared, and cannot leave the lab, so lab access gates testing and a single unrecoverable crash halts flight work.

---

## Stakeholders (10%)

A stakeholder is an *"individual or organization having a right, share, claim, or interest in a system or in its possession of characteristics that meet their needs and expectations"* (ISO/IEC/IEEE 15288) [13]. We apply one rule consistently: **a primary stakeholder interacts with the system or its direct outputs as part of their own work, or the project cannot proceed without their continuing participation; a secondary stakeholder never touches the system but constrains it, governs it, or inherits its consequences** [14], [15]. Stakeholders were enumerated by walking the system life-cycle stages [16] and will be re-reviewed each sprint.

*"Primary" does not mean "most important"* — a regulator is secondary yet can veto a system [17].

**Approving authorities are plural and named separately:** the course instructor accepts deliverables for grade, the faculty mentor accepts the system technically, and the lab manager authorizes flight in the volume.

### Primary

| Stakeholder | Role | Need | Verified by |
| --- | --- | --- | --- |
| Dr. Juan Calderon Chavez | Customer / acquirer | A working, documented heterogeneous coordination capability on lab hardware | Acceptance demo, SDD review |
| Dr. Fan Yang | Approving authority, grader | Deliverables meeting the published templates | Document submissions |
| Team (4 members) | Developers; graduating students | A demonstrable system and a defensible design record | Final demo, decision record |
| Lab manager / equipment custodian ⟦MENTOR⟧ | Operator of shared resource | Safe, scheduled, accountable use of the flight volume and fleet | Lab procedures, incident log |

⟦MENTOR⟧ *If this work carries external grant funding, the sponsoring agency is also primary and may impose publication or export-control obligations.*

### Secondary

- **ABET** — the capstone is the accreditation-mandated *"culminating major engineering design experience that incorporates appropriate engineering standards and multiple constraints"* (Criterion 5) [18]. This is why the proposal cites standards at all.
- **The EECS department and its assessment process** — Criterion 2 requires periodic program review involving constituencies [18]; capstone artifacts are that evidence.
- **Future capstone teams and lab researchers** who inherit the codebase, hardware configuration and calibration procedures. Their need is a reproducible setup procedure — which makes documentation quality a traceable requirement, not a courtesy.
- **Other users of the lab** — they share the 2.4 GHz band and the physical flight volume, making their operations and ours mutually interfering. This is simultaneously a stakeholder relationship and a channel-allocation constraint.
- **University EH&S / risk management** — indoor flight safety and lithium-polymer charging and storage policy.
- **The FCC** — the 2.4 GHz links operate under 47 CFR Part 15.

**The FAA is not a stakeholder for the baseline system**, because 14 CFR Part 107 governs operations in the National Airspace System and the FAA has stated its rules do not apply to operations conducted indoors [19]. This holds only because we commit to indoor-only flight in the scope below.

### Application-domain stakeholders

Two domains that the indoor, GPS-denied, fiducial-assisted testbed genuinely models:

**GPS-denied interior and subterranean search** — FEMA and state urban search-and-rescue task forces, mine rescue teams and inspectors. Aerial agents reach spaces ground systems cannot while ground agents provide endurance and communications anchoring; this division was validated by the CERBERUS team in the DARPA Subterranean Challenge [20]. NIST's Standard Test Methods for Response Robots, standardized through ASTM Committee E54.09, cover exactly this ground-and-aerial combination.

**Warehouse inventory** — operations managers and third-party logistics providers. Drones read high-rack labels that otherwise require a lift truck while floor robots supply docking, charging and a localization anchor. Indoor, GPS-denied and infrastructure-assisted — the closest commercial analog to our testbed.

---

## Proposed Solution (45%)

### Scope — what we will cover

A heterogeneous team of **N aerial and M ground agents ⟦COUNT⟧** operating in a single shared indoor volume, delivering:

1. A **unified coordinate frame** across the two localization systems, with the residual calibration error measured and reported.
2. **Formation control** holding a commanded geometry, with formation error, convergence time and message loss logged automatically every trial.
3. A **performance measurement harness** quantifying control-loop timing, end-to-end command latency, and radio throughput and loss — converting this proposal's communication claims into measured evidence.
4. **Characterized degradation**: how formation error responds as update rate, latency and loss are deliberately varied.

### Scope — what is explicitly out

| Excluded | Why |
| --- | --- |
| Outdoor flight | Positioning infrastructure is indoor-only; keeps the system outside FAA jurisdiction |
| GPS-denied autonomous localization (SLAM) | The lab provides external positioning; SLAM is a separate capstone |
| Lidar, photogrammetry, mapping, 3D reconstruction | Excluded by payload: a 15 g margin cannot carry the sensors |
| Learned control policies (RL / multi-agent RL) | Classical consensus control is provably stable and demonstrably sufficient at this scale [7]; MARL sim-to-real on nano-drones is an open research problem [21] |
| Onboard vision | Blocked by a documented deck pin conflict with the positioning hardware, and by endurance cost |
| More than one mission type | One well-characterized mission beats three demonstrated once |

*This list is deliberate. Each exclusion has a stated reason and a corresponding entry in our idea register, so nothing was dropped silently.*

### Standards driving the solution

| Standard | How it drives the design |
| --- | --- |
| **14 CFR §107.35** | Prohibits one pilot operating multiple aircraft — **the regulatory justification for the autonomy architecture.** Waivable under §107.205, so the design targets the evidence such a waiver requires |
| **14 CFR Part 107 (jurisdiction)** | Does not apply indoors; the FAA has stated its rules govern outdoor NAS operations [19]. Scoping flight indoors is therefore a deliberate regulatory decision |
| **47 CFR §15.247** | Bounds 2.4 GHz operation: 1 W conducted, 36 dBm EIRP. The aerial platform holds FCC ID 2AUV3CF21KIT |
| **ISO/IEC/IEEE 29148:2018** | Requirements structure and the characteristics of a good requirement — governs the SRS |
| **ISO/IEC/IEEE 42010:2022** | Architecture description and stakeholder viewpoints — governs the SDD |
| **ISO/IEC/IEEE 29119-3:2021** | Test documentation — governs the System Test Plan |
| **ISO/IEC/IEEE 15288:2023** | Life-cycle process framing for the two-semester sequence |
| **OMG DDSI-RTPS v2.5** | The wire protocol underlying ROS 2, used for the ground segment |
| **IEC 62133-2 / UN 38.3** | Lithium-polymer handling, charging and storage for a multi-aircraft fleet |
| **IEC 60825-1:2014** | The positioning base stations are certified Class 1 laser products; governs operating procedure (never operate with the housing open) |
| **RFC 7680, RFC 3393** | Standards-based definitions of packet loss and delay variation, so our reported metrics are auditable rather than hand-defined |

Indoor research flight has **no consensus standard**; safety is governed by ERAU institutional policy ⟦MENTOR⟧, which we cite rather than substituting an invented standards reference.

### Approach

**Architecture.** Position estimation and attitude control run **onboard** each aerial agent; the ground station broadcasts low-rate setpoints rather than unicasting per-agent state. This is the published pattern that makes swarms of this scale feasible on a bandwidth-limited link [6], and analysis of the packet budget shows broadcast versus per-agent unicast is worth roughly a 4× difference in achievable swarm size on identical hardware.

**Control.** Consensus with constant offsets over a fixed communication graph, chosen because it has a short Lyapunov stability proof, an explicit convergence rate given by the graph's algebraic connectivity λ₂, and an exact delay bound [7] — all three independently measurable from flight data. A ground agent or virtual structure supplies the group objective, which is required: gradient-based flocking without navigational feedback provably fragments [22]. Inter-agent safety uses buffered Voronoi cells, which need only relative *position* — not velocity — and are already implemented in the platform firmware [23].

**Frame unification.** An aerial agent carrying a ground-detectable fiducial is moved through the shared volume, collecting corresponding measurement pairs; the rigid transform is solved in closed form [24]. This yields a measurable residual, and it is a hardware experiment rather than a simulation.

**Data: real, with a bounded simulation role.** Hardware measurement is the primary evidence base. **Software-in-the-loop is used to unit-test coordination logic before flight** — the platform's ROS 2 stack provides a simulation backend exposing an identical API, so the same flight scripts run unchanged. This is a pre-flight safety check, not a research artifact. It is also the honest answer to a real constraint: no available simulator models either of our localization systems, so the part of the system we most need to characterize is precisely the part that cannot be simulated.

**Measurement is a deliverable, not an afterthought.** Benchmarking is measurement, not prediction: a simulator's timing model carries more uncertainty than the differences we need to resolve, and algorithmic complexity predicts the shape of a scaling curve but not its constant. Every performance claim in this proposal will be replaced by a measured number with its measurement conditions attached.

### Functionality complete by end of Semester 1

| # | Deliverable | Acceptance criterion |
| --- | --- | --- |
| S1-1 | Development environment reproduced by all four members | Each member independently builds, flies and lands one aerial agent |
| S1-2 | **Measurement harness operational** | Logged, repeatable measurement of control-loop period and jitter, command latency (p50/p95/p99), and radio packet rate and loss |
| S1-3 | Radio and RF baseline characterized | Measured maximum packet rate; channel-occupancy survey at the flight volume during quiet and busy hours |
| S1-4 | Aerial-only formation, N = 3 | Commanded geometry held; RMS formation error and convergence time reported over ≥5 trials with conditions logged |
| S1-5 | **Unified coordinate frame** | Transform calibrated; **residual error measured and reported**, not tuned away |
| S1-6 | One heterogeneous agent pair coordinating | An aerial and a ground agent hold a commanded relative geometry |
| S1-7 | SRS, System Design Document, System Test Plan | Every performance requirement carries a number, a percentile and a measurement condition; every requirement traces to a test case |

### Functionality complete by end of the year

| # | Deliverable | Acceptance criterion |
| --- | --- | --- |
| S2-1 | Full heterogeneous formation, N aerial + M ground ⟦COUNT⟧ | Formation held through a commanded mission; error within the SRS threshold |
| S2-2 | Mission execution | Formation traverses a defined path or covers a defined area; completion time reported **with completion fraction** |
| S2-3 | Degradation characterized | Formation error measured against deliberately degraded update rate, injected latency and injected loss — including **burst** loss, not only average |
| S2-4 | Theory-vs-measurement validation | Measured convergence rate compared against the λ₂ prediction; measured latency knee compared against the analytic delay bound |
| S2-5 | Fault tolerance | Behavior measured under mid-mission agent loss and positioning occlusion |
| S2-6 | Handover package | Repository, calibration procedure and known-good configuration reproducible by a future team |

**Stretch, only if the baseline lands early:** aerial agent as communication relay; cooperative area coverage; learned residual dynamics for close-proximity flight, which has a published single-number value proposition (reducing safe vertical separation from ~60 cm to 24 cm on comparable hardware [25]) and keeps the classical controller as a fallback.

---

## Proposed Project Budget (10%)

⟦COUNT⟧ **Choose one before submission — the section must not be left blank.**

**Option A — no budget required.** *"This project requires no budget. All aerial and ground platforms, positioning infrastructure, radios and computing are existing departmental laboratory equipment [itemize]. All software is open-source: ROS 2, the platform firmware and client libraries (MIT/GPL), and standard Linux tooling. No commercial software licences are required. Per the proposal template, the 10% weighting for this section is redistributed to Problem Statement (+3%), Stakeholders (+3%) and Proposed Solution (+4%)."*

**Option B — spares requested.** Itemize consumables and spares: airframes, propellers, batteries, expansion decks, ground-platform parts. **⟦TEAM⟧ Even under Option A, ask what spares the lab holds** — a single unrecoverable crash with no replacement halts all flight work, which is the highest-scoring risk in our risk register.

---

## References (5%)

⟦TEAM⟧ *Confirm the required citation style with the instructor. Numbers verified against primary sources; several claims in an earlier draft were corrected or removed after checking — see [`../docs/findings/`](../docs/findings/).*

[1] J. P. Desai, J. P. Ostrowski, V. Kumar, "Modeling and Control of Formations of Nonholonomic Mobile Robots," *IEEE Trans. Robotics and Automation*, 17(6):905–908, 2001.

[2] K.-K. Oh, M.-C. Park, H.-S. Ahn, "A survey of multi-agent formation control," *Automatica*, 53:424–440, 2015.

[3] A. Taffanel et al., "Lighthouse Positioning System: Dataset, Accuracy, and Precision for UAV Research," arXiv:2104.11523, 2021.

[4] A. Gawel, R. Dubé, H. Surmann, J. Nieto, R. Siegwart, C. Cadena, "3D Registration of Aerial and Ground Robots for Disaster Response," arXiv:1709.00587, 2017.

[5] Bitcraze AB, "New Crazyradio 2.0 Swarm-optimized firmware 5.1," Dec. 2025.

[6] J. A. Preiss, W. Hönig, G. S. Sukhatme, N. Ayanian, "Crazyswarm: A Large Nano-Quadcopter Swarm," *IEEE ICRA*, pp. 3299–3304, 2017.

[7] R. Olfati-Saber, R. M. Murray, "Consensus Problems in Networks of Agents with Switching Topology and Time-Delays," *IEEE Trans. Automatic Control*, 49(9):1520–1533, 2004.

[8] L. R. Buonocore, V. Lippiello, S. Manfredi, F. Ruggiero, B. Siciliano, "Effects of Packet Losses on Formation Control of Unmanned Aerial Vehicles," *IFAC World Congress*, 2014.

[9] "UGV-UAV Integration Advancements for Coordinated Missions: A Review," *J. Intelligent & Robotic Systems*, 2025. doi:10.1007/s10846-025-02273-w

[10] "Leader-Follower Based Formation Control of a Heterogeneous Robot Swarm," *European Journal of Technique*, 13(2), 2023.

[11] Bitcraze AB, "Datasheet Crazyflie 2.1+ Rev 1," 2024; "Lighthouse Positioning System," system documentation.

[12] J. A. Preiss, W. Hönig, G. S. Sukhatme, N. Ayanian, "Downwash-Aware Trajectory Planning for Large Quadrotor Teams," *IEEE/RSJ IROS*, 2017. arXiv:1704.04852

[13] ISO/IEC/IEEE 15288:2023, *Systems and software engineering — System life cycle processes*.

[14] M. B. E. Clarkson, "A Stakeholder Framework for Analyzing and Evaluating Corporate Social Performance," *Academy of Management Review*, 20(1):92–117, 1995.

[15] K. D. Eason, *Information Technology and Organisational Change*, Taylor & Francis, 1988.

[16] SEBoK Editorial Board, "Stakeholder Needs Definition," *Guide to the Systems Engineering Body of Knowledge*, v2.14, Stevens Institute of Technology, 2026.

[17] R. K. Mitchell, B. R. Agle, D. J. Wood, "Toward a Theory of Stakeholder Identification and Salience," *Academy of Management Review*, 22(4):853–886, 1997.

[18] ABET Engineering Accreditation Commission, *Criteria for Accrediting Engineering Programs, 2025–2026*.

[19] Federal Aviation Administration, "Do the FAA rules and regulations apply to … drone operations conducted indoors ONLY?" FAA Frequently Asked Questions.

[20] M. Tranzatto et al., "CERBERUS: Autonomous Legged and Aerial Robotic Exploration in the Tunnel and Urban Circuits of the DARPA Subterranean Challenge," *Field Robotics*, 2022. arXiv:2201.07067

[21] "Autonomous Navigation at the Nano-Scale: Algorithms, Architectures, and Constraints," arXiv:2601.13252, 2026. *(preprint)*

[22] R. Olfati-Saber, "Flocking for Multi-Agent Dynamic Systems: Algorithms and Theory," *IEEE Trans. Automatic Control*, 51(3):401–420, 2006.

[23] D. Zhou, Z. Wang, S. Bandyopadhyay, M. Schwager, "Fast, On-Line Collision Avoidance for Dynamic Vehicles Using Buffered Voronoi Cells," *IEEE Robotics and Automation Letters*, 2(2):1047–1054, 2017.

[24] S. Umeyama, "Least-Squares Estimation of Transformation Parameters Between Two Point Patterns," *IEEE Trans. Pattern Analysis and Machine Intelligence*, 13(4):376–380, 1991.

[25] G. Shi, W. Hönig, X. Shi, Y. Yue, S.-J. Chung, "Neural-Swarm2: Planning and Control of Heterogeneous Multirotor Swarms Using Learned Interactions," *IEEE Trans. Robotics*, 2021. arXiv:2012.05457

---

## Pre-submission checklist

- [ ] Project name chosen and used consistently ⟦TEAM⟧
- [ ] Roles assigned ⟦TEAM⟧; name spellings verified against the roster
- [ ] Every ⟦MENTOR⟧ / ⟦COUNT⟧ / ⟦TEAM⟧ marker resolved and removed
- [ ] **Budget option chosen and stated** — blank forfeits 10%
- [ ] ERAU lab flight-safety policy cited by title and revision date
- [ ] Agent counts (N, M) filled in and derivable from the bandwidth budget
- [ ] Citation style confirmed with the instructor
- [ ] Read aloud once for the typo in the original draft: "heterogen**e**ous"

---

**Related:** [`PROPOSAL_GAP_ANALYSIS.md`](PROPOSAL_GAP_ANALYSIS.md) · [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) · [`../docs/findings/`](../docs/findings/) · [`../INDEX.md`](../INDEX.md)
