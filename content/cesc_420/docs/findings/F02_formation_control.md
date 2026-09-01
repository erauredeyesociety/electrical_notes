# F02 · Formation Control and Evaluation Metrics

Coordination approaches ranked by *capstone defensibility*, plus the measurable metrics the System Test Plan needs. The metrics half is the more valuable half.

Related: [IR-01](../01_idea_register.md#ir-01--heterogeneous-air-ground-formation-control) · [IR-04](../01_idea_register.md#ir-04--measurable-mission-and-evaluation-harness) · [F01](F01_crazyflie_platform.md) · [F04](F04_network_and_latency.md)

---

## Recommended baseline

**Consensus-with-offsets** for formation shape (one-slide proof, measurable convergence rate) + **a ground robot or virtual structure supplying the group objective** (prevents fragmentation — see below) + **the stock Crazyflie BVCA** for inter-agent safety (already in firmware, position-only, hardware-validated).

Every component is either already implemented in the lab's firmware or has a one-slide proof. MPC and RL become explicit Semester 2 stretch goals.

---

## Approach comparison

| Approach | Needs | Failure mode | Defensibility |
| --- | --- | --- | --- |
| **Consensus / Laplacian** | neighbor-relative states | none intrinsic; rate set by λ₂ | **Provable, 3-line proof** |
| **Virtual structure** | global state (have it) | rate-limited by slowest member; no obstacle avoidance | **Provable, high precision** |
| Leader–follower | leader's state only | disturbance amplification; total loss on leader failure | Provable *with* caveat |
| Artificial potential fields | relative positions only | local minima, oscillation | Local minimum only |
| Behavior-based | varies by scheme | behaviors cancel → stall; oscillation | **Empirical only** |
| Distributed MPC | neighbors' *predicted trajectories* | four coupled preconditions | Research project |

### Things worth citing verbatim

**String instability is unavoidable.** Seiler, Pant & Hedrick proved a homogeneous predecessor-following string with constant spacing and two integrators necessarily has ‖T(s)‖∞ > 1 — *no compensator choice removes it*. One-line justification for capping chain depth: every follower references the leader or a virtual structure, never the robot in front.

**Pure potential fields fragment.** Olfati-Saber proved gradient-based flocking without navigational feedback *generically leads to fragmentation*; adding a group-objective term yields cohesive flocking. This is the citable proof that **a group objective is mandatory** — direct justification for keeping a leader or virtual-structure reference.

**Don't claim global stability for distance-based control.** Krick, Broucke & Francis give only *local* asymptotic stability with known undesired equilibria. Claiming global stability here is the most common overclaim in student formation reports and is trivially challenged at a defense.

**One codebase covers three families.** Wei Ren showed leader-follower, behavioral and virtual-structure approaches all unify under consensus by choosing the information state appropriately. One citation lets a single consensus codebase cover three literature families — a strong SDD architecture argument that avoids writing three controllers.

**A free ablation axis.** Balch & Arkin's three reference schemes — unit-center-referenced (all teammates), leader-referenced (one leader), neighbor-referenced (one assigned neighbor) — are the same controller under three information topologies. That's a real comparison table for the final report at almost no implementation cost.

**MPC won't close a fast loop onboard.** Embedded NMPC on Cortex-M class hardware reports solve times of single-to-tens of milliseconds (Cortex-M7 runtimes ≈ 40× an i7). The STM32F405 is a 168 MHz M4. Any MPC must be an **offboard outer loop at 10–100 Hz**. Its deeper problem: MPC requires exchanging whole predicted trajectories, which does not fit a 60-byte P2P packet.

---

## Graph theory — the whole prerequisite

**L = D − A** (degree − adjacency). For an undirected graph L is symmetric PSD with eigenvalues 0 = λ₁ ≤ λ₂ ≤ … ≤ λₙ. **The graph is connected iff λ₂ > 0**, with rank(L) = n−1. That is a computable precondition to assert in the SRS as a system assumption.

**λ₂ (the Fiedler value) predicts convergence rate.** The Lyapunov derivative satisfies V̇ ≤ −2λ₂V, so disagreement decays no slower than exp(−λ₂t):

> ‖δ(t)‖ ≤ ‖δ(0)‖ exp(−κt)

**This converts an eigenvalue into a testable prediction: the slope of a semilog plot of measured formation error must be at least λ₂.** That single figure demonstrates theory, measurement, and their agreement simultaneously — disproportionately valuable on a poster or midterm slide.

Two corrections that matter in practice:

- **Directed graphs:** if link quality is asymmetric, compute λ₂ of the *mirror* graph L̂ = (L + Lᵀ)/2, not of L. Otherwise the predicted rate is wrong.
- **Switching topology:** radio dropouts change the graph every cycle. Report the **worst-case λ₂ over observed graphs**, not the nominal all-to-all value. The guaranteed rate is κ* = minₖ λ₂(L(Ĝₖ)).

Sanity check: Olfati-Saber & Murray's n=10 sparse digraphs had λ₂ as low as 0.191. **A sparse 4–8 agent swarm settles in tens of seconds, not milliseconds.**

### The delay bound — turn "network delay" into a number

For a fixed undirected graph with uniform delay τ, consensus is reached **iff**:

> τ < τ* = π / (2·λ_max(L))

At τ = τ* the system oscillates stably at frequency λ_max. **This converts the proposal's vague "network delay" risk into a computable pass/fail requirement:** measure λ_max of the comm graph, compute τ*, require measured one-way delay below it. Put that in the SRS.

**The tuning trade-off, written down.** Scaling all edge weights by k scales λ_max by k — so any delay can be tolerated by shrinking the consensus gain. But it scales λ₂ by k too. **Robustness to delay is bought one-for-one with convergence speed.** One knob, an explicit trade curve — exactly the design-decision table the SDD template asks for.

Consequence: **do not naively broadcast all-to-all.** Denser graphs raise λ₂ (converge faster) but also raise λ_max (tighter delay budget). Both effects must be measured.

---

## Collision avoidance

| Algorithm | Needs | Complexity | Note |
| --- | --- | --- | --- |
| **BVC** | **position only** | O(k) geometric, O(k³) QP | **Already in Crazyflie firmware** |
| ORCA | position + **velocity** + radius | O(n) LP | Assumes holonomic; needs *all* agents running it |
| CBF-QP | model + safe-set function | small QP | Strongest safety language |

### BVCA ships in the firmware — this is the most actionable finding here

`src/modules/src/collision_avoidance.c` implements Buffered Voronoi Cell avoidance. **Enable it with one parameter (`colAv.enable`) instead of implementing anything**, and spend the time on formation control.

Defaults: `ellipsoidRadii` = (0.3, 0.3, 0.9) m, `horizonSecs` = 1.0 s, `maxSpeed` = 0.5 m/s, `sidestepThreshold` = 0.25 m, `voronoiProjectionMaxIters` = 100. Neighbor positions come from `peer_localization.h` for all Crazyflies **on the same radio channel**.

Three caveats from the source itself:

1. **It does not smooth modified setpoints** — output may be discontinuous. Only the **PID controller is confirmed to work**; high-gain controllers like Mellinger may become unstable. *Aggressive trajectories + Mellinger + onboard collision avoidance is a documented conflict and a crash waiting to happen in a demo.*
2. Suitable only for **low-to-medium spatial contention**.
3. **`maxPeerLocAgeMillis` defaults to 5000 ms**, with an in-source comment that this is "probably longer than desired in most applications." A 5-second-stale peer position at 0.5 m/s is a **2.5 m error**. Tighten it and justify the new value numerically in the test plan.

**Free instrumentation:** the `colAv` log group exposes `colAv.latency` — a per-agent compute-time measurement already wired up, reportable as a control-loop timing metric with zero instrumentation code. Useful input to [F10](F10_benchmarking_and_measurement.md).

### Why position-only matters

BVC needs only sensed relative **position**; ORCA needs **velocity** too. On Crazyflies, position comes from Lighthouse but velocity is differentiated and noisy — so BVC's information requirement is the decisive practical advantage, not merely its availability. BVC is also competitive with ORCA on path quality (569/355/704 steps vs 612/361/509 on three 100-robot benchmarks).

ORCA's half-plane construction encodes *each agent taking half the responsibility* — **which breaks the moment the heterogeneous ground robots don't run ORCA.** Critical for this project.

**Deadlock is an open problem, not a bug.** Zhou et al. state that to their knowledge no algorithm provably avoids deadlock without central computation or global coordination, and note residual livelock risk even with their perturbation heuristic. **The honest deliverable is a measured deadlock rate over N trials plus a timeout-and-replan mitigation** — not a claim of freedom from it.

**Copyable protocol:** Zhou et al. validated BVC on 5 quadrotors in OptiTrack with r_s = 0.2 m (0.4 m minimum separation), horizon T = 30, dt = 0.25 s, over **79 trials** without collision or deadlock. That is a directly transferable sample size and protocol.

**Downwash — measured, citable spacing:** Preiss et al. measured on real Crazyflies that **r_z = 0.3 m vertical** is safe while **r_x = r_y = 0.12 m** suffices horizontally (tested on 32 Crazyflies). The tall ellipsoid in the firmware defaults encodes exactly this. Vertical spacing is the constraint most likely to be violated in a stacked air/ground demo.

**CBF caveat:** the base formulation requires relative degree one. **Quadrotor position has relative degree 2 with respect to thrust**, so a naive position-based CBF on a Crazyflie is already outside the base theory and needs the HOCBF form. The Georgia Tech Robotarium is the existence proof that CBFs work on a student-accessible ground testbed.

---

## Metrics for the System Test Plan

### Formation error — define on *distances*, not positions

> e_RMS(t) = √( (1/|E|) · Σ_(i,j)∈E ( ‖pᵢ(t) − pⱼ(t)‖ − d_ij^desired )² )

**Defining it on inter-agent distances rather than absolute positions is not a stylistic choice — it is what makes the metric measurable at all.** Lighthouse gives <1 mm *relative* precision but only 2–10 cm *absolute* accuracy. An absolute-waypoint metric is dominated by calibration error; a distance metric is invariant to formation translation and rotation and measurable at millimetre precision.

If the formation is specified as a *shape*, use an orthogonal Procrustes fit (optimize over rotation and translation first). Otherwise a perfectly correct but rotated formation reports large error.

**Reporting format that makes a row pass/fail rather than descriptive:**

> `e_RMS = 0.043 ± 0.011 m, max 0.092 m, over t ∈ [20 s, 60 s], N = 20 trials; PASS (threshold 0.10 m)`

Mean + max + threshold + window + trial count. Missing any of these is the specific weakness graders flag.

### Convergence vs settling — they are different

- **Convergence time:** first t after the command at which e_RMS(τ) ≤ ε for all τ ∈ [t, t+T_hold]. **Publish both ε and T_hold** (e.g. ε = 0.10 m, T_hold = 5 s) or the number is meaningless.
- **Settling time:** time for error to enter and remain within ±2% or ±5% of its *final value* after a step. State which band (IEEE Std 181-2011).

Conflating them will be challenged at the defense.

### Standards-based network metrics

Citing IETF definitions converts hand-waved percentages into auditable measurements:

- **Message loss** — RFC 7680 / STD 82: a packet is lost if not received within a stated waiting time **Tmax**; corrupted counts as lost, duplicates count as received. Report the Type-P-One-way-Packet-Loss-Ratio.
- **Jitter** — RFC 3393 *ipdv*: difference in one-way delay between a selected packet pair. **Report percentiles and peak-to-peak, not a mean** — a mean hides the tail that actually destabilizes the loop, and it's the p95/p99 that determine whether τ* is respected.

### Onboard loop jitter — already instrumented

Firmware constants: `RATE_MAIN_LOOP` = 1000 Hz, `ATTITUDE_RATE` = 500 Hz, `POSITION_RATE` = 100 Hz, `RATE_HL_COMMANDER` = 100 Hz. The `rateSupervisor` accepts **997–1003 iterations per 1000 ms** and prints a warning otherwise.

**Report onboard jitter as a ±0.3% bound citing the built-in supervisor, rather than building a timing rig.**

### Coverage and mission time

- **Coverage:** CP = (|Θₑ|/|Θ|) × 100%. **Undefined without a stated grid cell size** — report resolution alongside every number (e.g. 0.25 m cells over 5×5 m = 400 cells).
- **Mission completion time:** wall-clock from arm/takeoff to the last agent satisfying a written terminal condition, reported **alongside the completion fraction**: *"completed 18/20 trials, mean 42.6 ± 5.1 s over the 18 successes."* Reporting mean-over-successes alone is the classic way a swarm result looks good while hiding a 10% failure rate — and a grader looking for pass/fail criteria will look for the denominator.

---

## Benchmark numbers to calibrate against

From Crazyswarm (Preiss et al., ICRA 2017) — 49 Crazyflies, 6×6×3 m Vicon, 3 Crazyradio PAs, 100 Hz pose broadcast, 500 Hz onboard control:

| Quantity | Value |
| --- | --- |
| Mean Euclidean tracking error | **<2 cm** even at 7×7 grid, 0.5 m spacing |
| End-to-end latency | 8→23 ms estimated (26 ms actual) growing linearly with N |
| Largest latency contributor | **motion capture, up to 14 ms** |

**Hover error vs position update rate (Table II) — the anchor for a degradation requirement:**

| Update rate | 100 Hz | 10 Hz | 5 Hz | 3.33 Hz | 2.5 Hz | 2 Hz |
| --- | --- | --- | --- | --- | --- | --- |
| Mean hover error | 0.58 cm | 0.68 cm | 0.91 cm | 1.48 cm | 1.95 cm | 2.18 cm |

Remained stable throughout. This supports a defensible requirement like *"formation error shall remain below X cm with position update rate degraded to 10 Hz"* — then tested by deliberately throttling the broadcast.

**Report packet loss as a histogram of consecutive drops, not a single percentage.** Crazyswarm Table I: of ~55,000 packets at 3 ms repeat delay — 54,458 with zero consecutive drops, 2 with one, 280 with two, 1174 with three. Consecutive-drop count is what predicts control-loop impact.

**Calibration:** a capstone hitting **<5 cm at 4–8 agents is credible; claiming <1 cm is not.**

### Air-ground specifically

- ArUco marker localization: position error <40 mm within 10 m, angle error <5° within ±60°. **~4 cm ground uncertainty vs ~1 mm relative drone precision means the heterogeneous formation error metric is dominated by the ground side** — set thresholds accordingly.
- A reported Crazyflie-tracking-ground-vehicle experiment showed centimetre accuracy static, but **8–11 cm RMSE while the ground vehicle moved**. Expect roughly an order of magnitude worse dynamic performance, and write separate static and dynamic pass thresholds.

---

## Open questions

- Does the mentor expect a **formal stability proof** in the SDD, or only empirical validation? This decides consensus (provable) vs behavior-based (empirical only).
- Do the ground robots accept **continuous velocity commands** (required for consensus, CBF and BVC) or only discrete waypoints? If waypoints only, the consensus formulation must be restructured as an outer loop.
- What is the **measured λ₂** of the actual lab communication graph? The theory-vs-measurement figure requires on-site RSSI and per-link loss data.
- Balch & Arkin's exact numeric formation-error formula was not retrievable open-access — pull from IEEE Xplore via the ERAU library before citing a specific number.

---

## References

1. R. Olfati-Saber, R. M. Murray, "Consensus Problems in Networks of Agents with Switching Topology and Time-Delays," *IEEE TAC* 49(9):1520–1533, 2004. — λ₂ convergence rate (Thm 8), delay bound τ* (Thm 10)
2. W. Ren, "Consensus strategies for cooperative control of vehicle formations," *IET Control Theory & Appl.* 1(2):505–512, 2007. — unification argument
3. K.-K. Oh, M.-C. Park, H.-S. Ahn, "A survey of multi-agent formation control," *Automatica* 53:424–440, 2015. — position/displacement/distance taxonomy
4. M. A. Lewis, K.-H. Tan, "High Precision Formation Control of Mobile Robots Using Virtual Structures," *Autonomous Robots* 4:387–403, 1997.
5. T. Balch, R. C. Arkin, "Behavior-Based Formation Control for Multirobot Teams," *IEEE T-RA* 14(6):926–939, 1998.
6. J. P. Desai, J. P. Ostrowski, V. Kumar, "Modeling and Control of Formations of Nonholonomic Mobile Robots," *IEEE T-RA* 17(6):905–908, 2001.
7. P. Seiler, A. Pant, K. Hedrick, "Disturbance Propagation in Vehicle Strings," *IEEE TAC* 49(10):1835–1842, 2004. — string instability
8. L. Krick, M. E. Broucke, B. A. Francis, "Stabilisation of infinitesimally rigid formations," *Int. J. Control* 82(3):423–439, 2009. — local-only caveat
9. Y. Koren, J. Borenstein, "Potential Field Methods and Their Inherent Limitations," *IEEE ICRA* 1991, 1398–1404.
10. R. Olfati-Saber, "Flocking for Multi-Agent Dynamic Systems," *IEEE TAC* 51(3):401–420, 2006. — fragmentation proof
11. W. B. Dunbar, R. M. Murray, "Distributed receding horizon control for multi-vehicle formation stabilization," *Automatica* 42(4):549–558, 2006.
12. J. van den Berg, S. J. Guy, M. Lin, D. Manocha, "Reciprocal n-Body Collision Avoidance," *ISRR 2009*, STAR 70:3–19, 2011.
13. D. Zhou, Z. Wang, S. Bandyopadhyay, M. Schwager, "Fast, On-Line Collision Avoidance for Dynamic Vehicles Using Buffered Voronoi Cells," *IEEE RA-L* 2(2):1047–1054, 2017. — **the algorithm in the firmware**
14. A. D. Ames, X. Xu, J. W. Grizzle, P. Tabuada, "Control Barrier Function Based Quadratic Programs for Safety Critical Systems," *IEEE TAC* 62(8):3861–3876, 2017.
15. D. Pickem et al., "The Robotarium: A remotely accessible swarm robotics research testbed," *IEEE ICRA* 2017, 1699–1706.
16. J. A. Preiss, W. Hönig, G. S. Sukhatme, N. Ayanian, "Crazyswarm: A Large Nano-Quadcopter Swarm," *IEEE ICRA* 2017, 3299–3304. — **the benchmark table**
17. J. A. Preiss et al., "Downwash-Aware Trajectory Planning for Large Quadrotor Teams," *IROS* 2017, arXiv:1704.04852. — r_z = 0.3 m
18. Bitcraze AB, `collision_avoidance.c`, crazyflie-firmware master. <https://github.com/bitcraze/crazyflie-firmware/blob/master/src/modules/src/collision_avoidance.c>
19. Bitcraze AB, `stabilizer.c`, `stabilizer_types.h` — loop rates and `rateSupervisor`
20. RFC 7680 / STD 82, "A One-Way Loss Metric for IP Performance Metrics (IPPM)," IETF, Jan 2016.
21. RFC 3393, "IP Packet Delay Variation Metric for IPPM," IETF, Nov 2002.
22. IEEE Std 181-2011, "IEEE Standard for Transitions, Pulses, and Related Waveforms."

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F03_air_ground_integration.md`](F03_air_ground_integration.md) · [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`F10_benchmarking_and_measurement.md`](F10_benchmarking_and_measurement.md) · [`../../INDEX.md`](../../INDEX.md)
