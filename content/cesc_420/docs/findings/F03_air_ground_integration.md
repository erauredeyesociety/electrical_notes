# F03 · Air-Ground Integration

The two-frame problem, fiducial localization, time synchronization, and why air+ground is *structurally* harder than air-only. This is the project's technical core.

Related: [IR-01](../01_idea_register.md#ir-01--heterogeneous-air-ground-formation-control) · [IR-03](../01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems) · [C-05](../02_constraints.md#c-05--technical--two-frames-one-formation) · [F01](F01_crazyflie_platform.md) · [F02](F02_formation_control.md)

---

## Why air+ground is genuinely harder — for the Problem Statement

Four reasons, all structural rather than implementation complaints. The proposal template wants exactly this kind of argument.

**1. Different state spaces.** The ground robot is a **nonholonomic SE(2)** system with two controllable DOF (v, ω); the Crazyflie is an **underactuated SE(3)** system. A single formation law cannot be written in one shared state space without an explicit mapping. This is the cleanest one-sentence articulation of the difficulty, and it is control-theoretic, not a complaint about wiring.

**2. Pose freshness differs architecturally, not by tuning.** Lighthouse position is computed **onboard** the Crazyflie and needs no radio link to arrive. The ground robot's pose is computed **off-board** in the camera pipeline and must traverse detection plus network before any controller sees it. **You cannot fix this by buying a faster camera** — the SDD should show the two latency paths explicitly.

**3. The altitude band is the worst one.** The Crazyflie suffers ground effect below a few decimetres, and its downward ToF has a 4 cm minimum range. Flying alongside a ~19 cm TurtleBot3 places the drone precisely where its flight model is least valid. **Air-only swarms simply fly above this band; air-ground formations cannot.** A physical, non-software reason the problem is harder.

**4. Occlusion is one-directional.** A drone hovering over a ground robot **occludes that robot's overhead ArUco tag**, while the ground robot cannot occlude the Crazyflie's upward Lighthouse line of sight. Predictable, and therefore designable-around: lateral formation offset, or multiple tags spread across the rover deck.

Downwash compounds #4: Crazyswarm models the collision volume as a **tall** ellipsoid because safe vertical separation far exceeds horizontal (60 cm vertical vs 24 cm horizontal in prior Crazyflie work). **Hovering an aerial agent directly over a ground agent — the most natural air-ground formation — is the single worst geometry.** Design formations offset, not stacked.

**Inverted architecture, worth stating explicitly.** The 15 g payload budget rules out the camera and companion computer that every published "aerial-as-eye-in-the-sky" mission assumes. X_swarm's aerial eye must be the *ceiling* camera — inverting the standard architecture. Say so in the proposal rather than letting a reviewer notice it.

**Scoping support:** recent surveys identify *disparities in communication protocols, sensor interoperability and autonomy frameworks* — not the coordination control law — as the persistent integration challenge in heterogeneous UAV-UGV systems. That directly supports scoping Semester 1 around **integration and calibration deliverables**, which is both honest and far more achievable than promising a novel control algorithm.

---

## The two-frame problem

**The mechanical root:** the Lighthouse coordinate frame's origin and axes are defined by the cfclient geometry-estimation procedure — **the air frame's origin is wherever the calibration drone was placed** and has no intrinsic relationship to the camera's frame. The two systems don't merely disagree numerically; they have independently and arbitrarily defined origins that must be tied together deliberately.

### Calibration procedure — a one-afternoon hardware experiment

1. Rigidly mount an ArUco tag on a Lighthouse-equipped Crazyflie.
2. Move it through the shared volume, collecting corresponding (Lighthouse, camera) point pairs.
3. Solve the closed-form **Kabsch–Umeyama** least-squares rigid transform.

Umeyama (1991) proved this always returns a *proper* rotation rather than a reflection, even with badly corrupted data. This satisfies the hardware-first Semester 1 preference exactly, and produces a **measurable residual** for the test plan. It is [M7](../06_semester1_schedule.md) on the schedule.

### Why 1° of sloppiness matters

A residual yaw misalignment θ produces lateral error r·sin(θ) growing with distance from the shared origin:

| Misalignment | Error at 3 m | Error at 5 m |
| --- | --- | --- |
| 1° | 52 mm | 87 mm |

**1° of calibration sloppiness already exceeds Lighthouse's own 2–4 cm error at arena scale.** That is the numeric argument for treating extrinsic calibration as a first-class engineering task rather than a setup step.

### The diagnostic that saves a week

- **Translation offset** → common-mode bias every agent inherits equally → formation is uniformly *shifted*.
- **Rotation offset** → different error vector per agent depending on position → formation is *sheared or twisted*.

So: a uniformly offset formation is a translation bug; a sheared one is a rotation bug. Spend the effort on rotation.

**Don't forget z.** The overhead camera observes only the floor plane, so calibration constrains the vertical axis weakly. The drone's Lighthouse z must be reconciled against the camera's assumed z=0 plane by **explicitly measuring the floor**. An unmeasured floor-plane offset appears as a constant altitude bias in every air-ground relative measurement — easy to miss because the ground robots never expose it.

### Composed error budget

| Source | Contribution |
| --- | --- |
| Lighthouse (air) | 2–4 cm |
| Multi-marker overhead ArUco (ground) | 3–5 cm |
| Extrinsic calibration residual | a few cm |
| **Composed air-ground relative uncertainty** | **≈5–10 cm** |

**5–10 cm is therefore the minimum honest inter-agent clearance.** Quoting a composed budget rather than a single sensor spec is exactly what the SDD template rewards.

### ROS 2 conventions to conform to

**REP-105** fixes the strict chain `earth → map → odom → base_link` with **exactly one parent per frame**. Designate one system as the shared world frame and publish the other as a static SE(3) transform. The single-parent rule forces the team to decide up front which system is authoritative — decide it, don't discover it.

Two REP-105 details that bite:

- **`odom` is continuous but drifts without bound; `map` is drift-free but jumps discretely** when localization updates. A formation controller fed map-frame poses sees step discontinuities and **commands a velocity spike**. Either filter the jumps or run the inner formation loop in a continuous frame.
- Multi-robot guidance: remap frame ids to disambiguate origin (`cf1/base_link`, `tb3/base_link`). Write this convention into the SDD **before anyone writes a node**.

**REP-103** fixes units and the right-handed x-forward/y-left/z-up body convention with ENU world convention — needed to state the transform unambiguously.

---

## Overhead ArUco localization

### The finding that should shape the risk register

Georgia Tech's Robotarium originally tracked robots with ArUco tags and a single webcam (1280×720, 30 Hz, 130×90 cm arena, up to 20 robots). **They later abandoned it for Vicon motion capture** because:

- the camera required **recalibration through the day as ambient light changed**,
- tracks were lost to **obstruction and reflections**,
- it grew **computationally expensive as agent count rose**.

**The best-known overhead-ArUco swarm testbed in the world gave up on the approach for exactly the failure modes this team is about to inherit.** Name these as known risks with mitigations in the proposal — doing so reads as diligence, not weakness.

### Accuracy is dominated by marker count

Controlled study, Logitech C920 at 2.991 m height, 15 cm DICT_6X6_1000 markers:

| Markers visible | Position RMSE (x / y) | Rotation error |
| --- | --- | --- |
| 1 | **45.3 / 31.4 cm** | 1.04° |
| 5 | 3.7 / 4.6 cm | 0.08° |
| 7 | 3.0 / 4.0 cm | 0.07° |

**Single-tag overhead localization is a ~30–45 cm system; multi-tag is a ~3–5 cm system.** Put multiple tags on each ground robot or accept decimetre-class ground pose. The study concludes **five or more markers must be visible from every reachable robot position** — a concrete, testable acceptance criterion: *verify 5-marker visibility across the full arena footprint before any formation experiment.*

At a reduced 1.334 m camera height: 2.75 / 5.16 cm RMSE.

### Failure modes to design against

**Pose ambiguity — the phantom bug.** Four coplanar corners admit **two** pose solutions with near-identical reprojection error. IPPE returns both and picks the lower-error one, but at long range or oblique viewing they become indistinguishable and **the estimated pose flips randomly between them**. This produces sudden large yaw/pitch jumps that look exactly like a control fault. Filter explicitly (temporal consistency check or multi-marker constraint) or debug a phantom controller bug for weeks.

**Motion blur** = velocity × exposure. A 10 ms exposure smears a 0.22 m/s TurtleBot3 tag by **2.2 mm** but a 1 m/s Crazyflie tag by **10 mm**.

**Staleness at 30 fps:** the pose is already one frame interval (33.3 ms) old before detection and transport. In that time a TurtleBot3 at 0.22 m/s moves **7.3 mm**; a Crazyflie at 1 m/s moves **33 mm**.

Together those two numbers are the technical argument for **keeping air localization onboard via Lighthouse** — the overhead camera is a viable ground sensor and a poor air sensor.

**Rolling shutter:** readout takes ~30 ms first row to last on a 30 fps webcam, geometrically skewing a moving marker's square. If yaw bias grows with ground-robot speed, rolling shutter is the first suspect; a global-shutter USB camera is a cheap fix worth budgeting.

**ArUco vs AprilTag:** ArUco is competitive on detection rate and cheapest computationally, but has higher mean and standard-deviation pose error; AprilTag's edge refinement wins at viewing angles ≤30°. Worth a documented trade study in the SRS — ArUco for throughput across many agents, AprilTag for accuracy — rather than an unexplained choice of whatever the lab already has.

---

## Time synchronization

**ROS 2 performs no automatic cross-machine clock synchronization** and uses each host's system clock. chrony or PTP must be configured *outside* ROS. Assuming ROS 2 timestamps are comparable across machines is a common and expensive team mistake — naming chrony explicitly in the SDD prevents a whole class of unexplained state-estimation errors.

| Method | Achievable sync |
| --- | --- |
| PTP (IEEE 1588) + NIC hardware timestamping | sub-microsecond |
| NTP / chrony, software timestamping, wired LAN | ~1 ms |
| chrony over Wi-Fi | worse, and jittery |

~1 ms on a wired chrony setup is adequate. **Wi-Fi-only sync is the weak link that will need measuring and reporting.**

### Why clock skew corrupts formation control

A **100 ms** offset between the camera pipeline and the Lighthouse pipeline maps to a **10 cm** apparent position error for an agent at 1 m/s — exceeding either sensor's own error. The controller sees a phantom formation error and **actively drives the swarm to correct something that is not there.**

**The diagnostic test to write into the System Test Plan:** clock skew produces a velocity-multiplied error that is **exactly zero at rest and grows linearly with speed**. So a swarm that holds formation perfectly in hover but oscillates or lags in transit has a **time-sync fault, not a control-gain fault**. Static-hold vs moving-hold isolates timing from tuning.

**Air-side timestamps are structurally less trustworthy.** The Crazyflie runs no NTP client and its firmware tick is independent of the host, so air-side timestamps are effectively applied *on arrival at the host* — folding radio latency into the timestamp itself. Measure this offset rather than assuming it away.

Use `message_filters` `ApproximateTimeSynchronizer` (with its `slop` parameter) to pair streams that are only approximately aligned — but only *after* host clocks are synchronized.

---

## Ground platforms

| Platform | Max speed | ROS 2 native? | Note |
| --- | --- | --- | --- |
| **TurtleBot3 Burger** | **0.22 m/s** | Yes | 138×178×192 mm; the common Crazyflie partner |
| Pololu 3pi+ | ~0.4 m/s | **No** | Cheapest path to 4+ agents; write the whole bridge |
| Bitcraze "Crazyrat" | — | — | Bolt 1.1 + DRV8833 + 3pi+ chassis; **prototype only, no positioning** |

**The ground robot's top speed is the hard speed ceiling of the entire formation** — every aerial trajectory must be planned at ground-robot pace. At 0.22 m/s that is a significant constraint on any mission design.

Precedent exists: published distributed-optimization work used heterogeneous teams of **3 Crazyflies + 4 TurtleBots**, so the pairing is citable rather than novel-and-unjustified.

---

## Calibrating expectations

| Result | Reported performance |
| --- | --- |
| Published UAV-UGV formation framework | **~60 cm horizontal, 20 cm vertical** tracking error |
| ArUco-guided UAV precision landing | ~21 mm (real flight), ~20 mm (sim) |
| Generic vision-based landing | 5–10 cm |
| ColAG (1 UAV guiding 3 blind UGVs) | 40.83 s mean reach, 0.53 s waiting, 12.50 m path |

**Decimetre-class formation error is the published state of practice for air-ground teams.** Promising centimetre accuracy in the proposal sets up a failed acceptance test. ColAG's metrics — reach time, waiting time, path length — are adoptable verbatim.

---

## The contribution angle

**No published work was found that fuses Bitcraze Lighthouse (air) with overhead ArUco (ground) into a single common frame.** There is therefore no literature value for the residual extrinsic calibration error of that specific pairing — **the team must measure it themselves, which is arguably a genuine contribution worth highlighting in the proposal.**

Reinforcing this: the closest published prior work to the X_swarm concept — a ROS 2 leader-follower V-formation with a TurtleBot3 leader and Crazyflie followers using Hungarian assignment — was **validated only in the Webots simulator**. The team's genuine contribution, and their pitch to Dr. Calderon Chavez, is **the hardware realization**. That aligns exactly with their stated real-hardware preference.

---

## Open — needs a lab visit with a tape measure

1. **Do the overhead camera's ground footprint and the Lighthouse tracked volume actually overlap?** If not substantially, there is no shared workspace to calibrate and the project premise needs rework. *Highest-priority unknown on this page.*
2. Overhead camera: model, resolution, frame rate, **rolling vs global shutter**, lens FOV, mounting height. Every ArUco accuracy number scales with these.
3. Current tag configuration — one tag per robot or several? This is the difference between ~30–45 cm and ~3–5 cm, and it may be cheap to fix.
4. Ground platform, count, ROS 2 status, top speed → sets the formation speed ceiling.
5. Wired Ethernet or Wi-Fi only? Any NIC with hardware timestamping? Decides µs-PTP vs ms-chrony.
6. Does Crazyswarm2 expose a clean insertion point for externally-localized non-Crazyflie agents, or must a parallel ground stack be written alongside it? Requires reading the `crazyswarm2` and `motion_capture_tracking` source.
7. Measured end-to-end (glass-to-controller) camera latency. **Vendor latency claims found in search were not primary sources and should not be cited** — measure it with an LED-flash or moving-target experiment.
8. Any means of ground-truthing the combined system (mocap elsewhere on campus)? Without an independent reference the team can measure **repeatability but not accuracy**.

---

## References

1. S. Umeyama, "Least-Squares Estimation of Transformation Parameters Between Two Point Patterns," *IEEE TPAMI* 13(4):376–380, 1991. — the calibration solver
2. W. Meeussen, "REP 105: Coordinate Frames for Mobile Platforms," ROS Enhancement Proposal, 2010.
3. T. Foote, M. Purvis, "REP 103: Standard Units of Measure and Coordinate Conventions," 2010.
4. S. Hinderer, M. Scheffler, B. Yang, "Investigation of ArUco Marker Placement for Planar Indoor Localization," arXiv:2509.17345, 2025. — the marker-count table
5. D. Pickem et al., "The Robotarium: A remotely accessible swarm robotics research testbed," *IEEE ICRA* 2017, arXiv:1609.04730.
6. S. Wilson et al., "The Robotarium: Globally Impactful Opportunities, Challenges, and Lessons Learned," *IEEE Control Systems Magazine* 40(1):26–44, 2020. — **why ArUco+webcam was abandoned**
7. M. Kalaitzakis et al., "Fiducial Markers for Pose Estimation: … ARTag, AprilTag, ArUco and STag," *J. Intell. Robot. Syst.* 101(4), 2021.
8. S. Garrido-Jurado et al., "Automatic generation and detection of highly reliable fiducial markers under occlusion," *Pattern Recognition* 47(6):2280–2292, 2014.
9. T. Collins, A. Bartoli, "Infinitesimal Plane-Based Pose Estimation," *IJCV* 109:252–286, 2014. — IPPE and the two-solution ambiguity
10. B. Wang et al., "STag: A Stable Fiducial Marker System," arXiv:1707.06292 / *Image and Vision Computing*, 2019.
11. E. Olson, "AprilTag: A robust and flexible visual fiducial system," *IEEE ICRA* 2011, 3400–3407.
12. A. Taffanel et al., "Lighthouse Positioning System: Dataset, Accuracy, and Precision for UAV Research," arXiv:2104.11523, 2021.
13. N. Michael et al., "Collaborative mapping of an earthquake-damaged building via ground and aerial robots," *J. Field Robotics* 29(5):832–841, 2012. — canonical motivating citation
14. C. Peterson et al., "Online Aerial Terrain Mapping for Ground Robot Navigation," *Sensors* 18(2):630, 2018.
15. P. Zhang, Y. Chen et al., "ColAG: A Collaborative Air-Ground Framework for Perception-Limited UGVs' Navigation," arXiv:2310.13324.
16. IEEE Std 1588-2019, "Precision Clock Synchronization Protocol for Networked Measurement and Control Systems."
17. chrony Project FAQ. <https://chrony-project.org/faq.html>
18. "UGV-UAV Integration Advancements for Coordinated Missions: A Review," *J. Intell. Robot. Syst.*, 2025. doi:10.1007/s10846-025-02273-w
19. ROBOTIS, *TurtleBot3 Features and Specifications*. <https://emanual.robotis.com/docs/en/platform/turtlebot3/features/>
20. Bitcraze AB, "Turning a Crazyflie into a ground robot," Apr 2026. <https://www.bitcraze.io/2026/04/turning-a-crazyflie-into-a-ground-robot/>

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F02_formation_control.md`](F02_formation_control.md) · [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`../../INDEX.md`](../../INDEX.md)
