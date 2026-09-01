# F07 · Edge ML and Learning

What machine learning is physically possible on this hardware, what a reviewer would say about each idea, and the three that survive. Supports the Parked entries [IR-08](../01_idea_register.md#ir-08--ml-enhanced-single-drone-navigation-the-original-preference)–[IR-12](../01_idea_register.md#ir-12--cross-view-geo-localization-against-pre-cached-satellite-tiles).

Related: [C-08](../02_constraints.md#c-08--technical--onboard-compute-is-very-small) · [F01](F01_crazyflie_platform.md) · [F09](F09_simulation_and_compute.md)

---

## ⚠ Two findings that change the register

### 1. The AI-deck and the Lighthouse deck conflict on UART1

Bitcraze's own deck-compatibility matrix marks them **not plainly compatible** — footnote 4: *"The GAP8 module is connected to UART1, so if that is enabled there will be conflicts."* The pin table confirms both claim RX1/TX1.

**The team's entire indoor positioning is Lighthouse.** So "onboard vision ML on a Lighthouse-localized Crazyflie" is blocked by a pin conflict that must be resolved in **week 1, not discovered in Semester 2.**

There is no drop-in alternative either: the matrix also flags AI-deck against the Loco deck (note 6, *"with a patch or workaround it is possible"*), the Micro-SD deck (note 5, both use IO4 for chip select), and BigQuad/Buzzer (note 7). The fallback is motion capture or a Lighthouse/GAP8 UART workaround.

### 2. Cross-view geo-localization is structurally inapplicable

The "labels are free when you fly with GPS" argument — the reason [IR-12](../01_idea_register.md#ir-12--cross-view-geo-localization-against-pre-cached-satellite-tiles) looked like the best-de-risked ML idea — **does not hold here. Bitcraze offers no GPS deck for the Crazyflie 2.x**, and the lab's positioning is indoor Lighthouse. There is no satellite tile to pair a frame with and therefore no free label.

Pursuing it would require a different airframe, outdoor flight authorization, and a camera other than the monochrome HM01B0 — an entire second platform. **The register should record "structurally inapplicable to available hardware," not merely "out of scope."**

*(Benchmarks retained for reference: CVUSA 35,532 train pairs; CVACT same + 9,280 test; University-1652 covers 1,652 buildings but its drone views are **rendered from 3D models, not flown**; VIGOR 90,618 satellite / 105,214 street-view across four US cities, built specifically to break the unrealistic centered-pair assumption. Sample4Geo Recall@1: CVUSA 98.68, CVACT val/test 90.81/71.51, **VIGOR same-area 77.86 → cross-area 61.70**, University-1652 92.65/95.14. That same-to-cross-area drop is what generalizing to an unseen city actually costs.)*

---

## The hardware ceiling

### AI-deck 1.1 / GAP8

4.4 g, up to 300 mA at VCOM 3–5 V. GAP8 rev-C (8+1 core RISC-V), 512 Mbit HyperFlash + 64 Mbit HyperRAM, Himax HM01B0 **320×320 monochrome** camera.

**Memory hierarchy — this is what matters:** 16 kB L1 (fabric controller), 64 kB L1 TCDM (8-core cluster), **512 kB L2 on-chip**. Anything larger must be tiled from off-chip HyperRAM over uDMA. **512 kB L2 is the hard ceiling on weights plus activations, and crossing it collapses throughput.**

Operating points (peer-reviewed): max performance FC@250 MHz / cluster@175 MHz / 1.2 V; energy-efficient FC@50 MHz / cluster@100 MHz / 1.0 V. **Any onboard inference-rate claim must state which point it assumes, or it is unfalsifiable.**

**Cite 5.4 GOps/s** at ~100 mW — the peer-reviewed figure. Vendor claims 10 GOPS and a 2026 preprint claims 20.0 GOPS; those are marketing or unverified and a reviewer can challenge them.

**The camera is never the bottleneck** — HM01B0 does QVGA@60 fps or binned QQVGA@120 fps at <4 mW. All frame-rate arguments reduce to GAP8 inference time.

**It is monochrome.** Anything depending on color — colored robot markers, color-based ground-robot ID, RGB-pretrained backbones without adaptation — is dead on arrival onboard. (ArUco is fine.)

### The accuracy-vs-rate menu

| Model | Params | Footprint | Rate | Energy |
| --- | ---: | ---: | ---: | ---: |
| PULP-DroNet v2 | — | 320 kB int8, ~41 MMAC | 19 fps | — |
| PULP-DroNet v3 (γ=1) | 204 k | — | 34 fps | 1.1 mJ/frame |
| PULP-DroNet v3 (γ=2) | 69 k | 14 kB | 61 fps | — |
| PULP-DroNet v3 (γ=4) | 26 k | 4.7 kB | 101 fps | — |
| **Tiny-PULP-DroNet v3 (γ=8)** | **1.9 k** | **1.9 kB**, 1.1 MMAC | **139 fps** | 0.4 mJ/frame |

**A 2 kB network at 139 fps is the existence proof that useful onboard vision on this exact hardware is real, not aspirational.**

The two published **failure markers** that define the ceiling: a 534 MMAC network exceeded L2, forced off-chip traffic, and managed **1.6 fps**; a 310 k-parameter depth network ran at **0.2 fps** on QVGA.

**Design rule for the SRS** — a single falsifiable requirement to hold every ML idea against:

> ≤40 MMAC/frame and ≤320 kB int8 → ~20 fps. ≤15 MMAC and ≤65 kB → 40–140 fps. Over ~500 MMAC or over 512 kB → below 2 fps.

**Honest speed envelope:** in-field at 0.5 m/s, PULP-DroNet v3 completed a static-obstacle corridor with a 180° turn 80% of the time and Tiny-PULP-DroNet v3 100%. Success degrades at 1.0 m/s and **neither is reliable at 1.5 m/s.** Don't promise more in the test plan.

> ⚠ **Citation care:** the Tiny-PULP-DroNet v3 paper is internally inconsistent — abstract and conclusion say 2.9 k params / 2.9 kB, the results section says 1.9 k / 1.9 kB. **Only 1.9 kB is consistent with the stated 168× reduction from 320 kB.** Quote the results-section number.

**Free, format-matched training data:** the PULP-DroNet v3 dataset is **66 k labeled grayscale QVGA images** collected with the nano-drone itself, released open-source — because the authors found *the dataset, not the network,* was the limiting factor. Direct evidence that data collection is where a capstone would actually spend its time.

Other networks demonstrated fully onboard: PULP-Frontnet human pose (14.7 MMAC, 48 fps, 96 mW), NanoFlowNet dense optical flow (5.5–9.3 fps), and **an FCNN for drone-to-drone relative localization at 39 Hz, 101 mW** — the single most directly reusable prior result for a swarm capstone.

**Endurance cost:** AI-deck (4.4 g) + Lighthouse deck (2.7 g) = 7.1 g of 15 g — mass fits. But a 2026 survey reports the AI-deck cuts endurance ~22% (≈440 s → 340 s). **A vision-equipped Crazyflie gets under 6 minutes per battery**, which sets how many trials fit in a lab session.

### STM32-resident ML — the other option

192 kB SRAM is the entire budget for the EKF, controller, *and* any learned component combined.

**Neural-Swarm2** (Shi et al., IEEE T-RO 2021) ran a spectrally-normalized deep-set DNN (φ: 6→25→40→40→20, ρ: 20→40→40→40→1, ReLU) **onboard the STM32 alongside the nonlinear controller and EKF in real time.** That is the demonstrated ceiling: roughly four 40-unit dense layers at control rate — enough for residual dynamics, nothing like enough for vision.

### The compute-boundary ladder

**This sentence belongs verbatim in the System Design Document:**

> STM32 dense-net inference adds essentially zero latency inside the existing control loop; GAP8 inference adds **6.3–29 ms** (139–34 fps) plus a UART hop to the STM32; ground-station-over-radio adds at least one radio round trip plus host scheduling, and for images additionally WiFi encode, transport and decode.

Per-drone command rate is ~1200/N Hz per radio — an 8-drone swarm on one radio gets **~150 Hz of setpoints: ample for trajectory commands, nowhere near enough to close a vision loop over the link.** Ground-station-over-radio is a **command channel, not a perception channel.**

AI-deck WiFi image streaming through the ESP32 is a debug path with **no vendor-specified frame rate**. Community reports say RAW works more reliably than the default JPEG encoder at >15× the bandwidth. **Any "stream images and infer on the ground" idea cannot be specified in the SRS until the team measures it.**

---

## The reviewer's counter-arguments — and where they're right

**Every ML idea kept in the register needs a paired classical baseline and one agreed metric in the System Test Plan**, because the reviewer question with no ML-only answer is *"does the swarm work measurably better with it than without it?"* That converts ML from a risk into a graded, falsifiable deliverable.

| Idea | The counter-argument | Verdict |
| --- | --- | --- |
| RL for formation keeping | Consensus/virtual-structure + Crazyswarm's high-level commander with minimum-snap trajectories **already flies 49 Crazyflies in tight formation**. For the nominal case, RL adds nothing. | **Reviewer is right** unless scoped to a regime where the classical controller demonstrably fails |
| **Inter-drone collision avoidance** | Classical answer is conservative ellipsoidal separation (~60 cm vertical for a 9 cm-span Crazyflie). | **The one place the classical method is provably not good enough** — see below |
| Onboard obstacle avoidance | Multi-ranger gives direct range in 5 directions at 2.3 g; the Swarm Gradient Bug Algorithm navigates complex environments with four single-pixel rangers, negligible memory, **and no inter-agent communication at all**. | Reviewer is right — a CNN must be justified by something ToF *cannot* do (semantics, identity, long range), not by avoidance itself |
| Ground-robot localization / frame registration | ArUco + overhead camera already yields pose; the Lighthouse-to-camera transform is a **one-time rigid calibration**. | Reviewer is right — record these as **classical by choice** in the SDD so the team isn't asked at the defense why they weren't learned |

### The strongest ML pitch available to this team

**Neural-Swarm2 closes vertical separation from ~60 cm to 24 cm** on a heterogeneous 16-robot Crazyflie-based team, cutting worst-case tracking error up to 3×.

That is:

- the closest published precedent to X_swarm's own premise (heterogeneous, close-proximity, Crazyflie-based),
- a **single-number value proposition** a grader can grasp instantly,
- **STM32-resident**, so it keeps the classical controller as a fallback,
- and reducible to one scalar metric: tracking error at a given separation.

---

## The three ML ideas that survive

1. **Learned residual aerodynamics for close-proximity heterogeneous flight** — the Neural-Swarm2 pattern. STM32-resident, classical fallback intact, single metric.
2. **Onboard vision-based drone-to-drone relative localization** at ~39 Hz on GAP8 — a Lighthouse-independent fallback. *(Blocked by the UART1 conflict until resolved.)*
3. **A tiny onboard CNN for a vision task the ToF decks physically cannot do** — semantics, identity, or long range.

Everything else either exceeds the hardware or is beaten by a classical baseline.

### On MARL specifically

**Reject it, and say why.** The canonical algorithms and their traps:

- **MADDPG** — the original CTDE formulation; per-agent actor + centralized critic seeing all observations and actions *at training time only*.
- **QMIX** — monotonic mixing of per-agent values. **By construction cannot represent joint value functions non-monotonic in per-agent values** — which is exactly what happens in close-proximity formation flight, where one agent's contribution flips sign.
- **MAPPO** — matches or beats both, *but only under five specific implementation choices*: value normalization, agent-specific global state as critic input, ≤10 (hard) / 15 (easy) epochs with no minibatch splitting, PPO clip ε ≤ 0.2, and large batches. **These five are the difference between it working and silently not working — which is where capstone weeks disappear.**

**The underlying instability CTDE only partly fixes is non-stationarity:** each agent's effective environment changes as co-agents update, breaking the Markov assumption. That is why MARL runs diverge for reasons that look like bugs, and why debugging time is *unbounded* rather than merely large.

**The H100s buy less than they look like here.** MAPPO's own SMAC experiments used up to 10M (40M on some maps) environment steps on a desktop with a **64-core CPU**, 256 GB RAM and one RTX 3090. **Reference MARL runs are environment-stepping bound on CPU, not GPU bound** — the cluster is far better spent on vision-model training or GPU-parallel single-agent sim ([F09](F09_simulation_and_compute.md)).

**The citation that makes "we chose not to pursue MARL" sound rigorous rather than unambitious:** Gorsane et al. (NeurIPS 2022) meta-analyzed 75 cooperative-MARL papers 2016–2022 and found evaluation trends that *"put into question the true rate of progress"* in the field. A 2026 nano-UAV survey separately names RL sim-to-real transfer as one of three persistent unsolved limitations, attributing failures to *"the stochastic nonlinearities of nano-scale physics."*

**The counterweight, for fairness:** Batra et al. (CoRL 2021) trained decentralized end-to-end neural swarm policies in simulation and **zero-shot transferred them to physical quadrotors** — flocking, tight formations, station keeping, goal swapping. Cite it in the register even though the idea is deferred.

**Single-agent RL is now cheap, though:** "Learning to Fly in Seconds" trained an RPM-level policy in **18 seconds on a consumer laptop** (~0.3M interactions) and deployed it on a real Crazyflie microcontroller under real-time guarantees. Single-agent RL is a days-scale fallback; **multi-agent RL is the only genuinely risky learning idea.**

### On learned SLAM front-ends

The classical baseline is strong: **ORB-SLAM3 reports 3.6 cm** average accuracy on EuRoC in stereo-inertial mode, real time — already comparable to the **2–4 cm the team gets free from Lighthouse.**

If proposing a learned front-end, the three names a reviewer expects are **NetVLAD** (place recognition), **SuperPoint** (detector/descriptor) and **SuperGlue/LightGlue** (matcher). But **LightGlue runs 150 fps at 1024 keypoints on an RTX 3080 and only 20 fps at 512 keypoints on an i7-10700K CPU** — so a learned matcher cannot run on a 168 MHz Cortex-M4 or at useful rates on GAP8. **Any learned SLAM front-end is necessarily a ground-station component and inherits the radio/WiFi latency.**

Even the tiny result worth reproducing needs newer silicon: NanoSLAM fits a 10 cm-resolution map in 10 kB of the Crazyflie's 192 kB RAM, but its pose-graph solver is constrained to **GAP9's 128 kB L1 — which the AI-deck 1.1 does not have.**

---

## Open

1. **Does the AI-deck / Lighthouse UART1 conflict have a workaround on this lab's Crazyflies?** Gates every onboard-vision idea. **First lab visit, not later.**
2. **Does the course or Dr. Calderon require an ML component at all?** If optional, recommend learned-residual-dynamics with a classical fallback. If mandatory, the scoping changes — ask explicitly.
3. Exact counts of Crazyflies, AI-decks, Lighthouse decks, base stations, ground robots, Crazyradios. No swarm-size claim can be written without them.
4. Does the lab have motion capture in addition to Lighthouse? **Both Neural-Swarm2 and Crazyswarm's tightest results used mocap at 100 Hz** — reproducing them may need capability the lab lacks.
5. Do the ground robots have onboard compute, or are they purely camera-localized and radio-commanded? Determines whether "heterogeneous" means heterogeneous *compute* or only heterogeneous *dynamics*.
6. AI-deck WiFi throughput and end-to-end latency — **no vendor figure exists; must be measured** if any ground-station-inference idea is kept.
7. Measured end-to-end Crazyradio command latency **in milliseconds** (not packets/s) — not found in any Bitcraze source. Needed to substantiate the "delay" term in the team's own problem statement. See [F04](F04_network_and_latency.md).
8. Are the H100 nodes usable for **CPU-heavy environment stepping** (core count, queue limits, job duration caps)? That, not GPU count, decides whether MARL training is even schedulable.
9. Is a GAP9-based AI-deck successor announced? Several attractive results need GAP9.

**Unresolved in sources:** GAP8 peak throughput is contested (5.4 GOps/s peer-reviewed vs 10 vendor vs 20.0 in a preprint) and was not settled against the GreenWaves reference manual. PULP-Frontnet throughput is reported inconsistently across sources. No direct capstone-scale datapoint exists for MARL formation-keeping wall-clock training time on Crazyflies — the "time sink" judgment rests on indirect evidence.

---

## References

1. L. Lamberti, L. Bellone, L. Macan, E. Natalizio, F. Conti, D. Palossi, L. Benini, "Distilling Tiny and Ultrafast Deep Neural Networks for Autonomous Navigation on Nano-UAVs," *IEEE IoT-J* 11(20):33269–33281, 2024. arXiv:2407.12675 — **the accuracy/rate menu**
2. G. Shi, W. Hönig, X. Shi, Y. Yue, S.-J. Chung, "Neural-Swarm2: Planning and Control of Heterogeneous Multirotor Swarms Using Learned Interactions," *IEEE T-RO*, 2021. arXiv:2012.05457 — **60 cm → 24 cm**
3. J. Eschmann, D. Albani, G. Loianno, "Learning to Fly in Seconds," *IEEE RA-L*, 2024. arXiv:2311.13081
4. S. Batra, Z. Huang, A. Petrenko, T. Kumar, A. Molchanov, G. S. Sukhatme, "Decentralized Control of Quadrotor Swarms with End-to-end Deep Reinforcement Learning," *CoRL* 2021. arXiv:2109.07735
5. R. Lowe et al., "Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments," *NeurIPS* 2017. arXiv:1706.02275 — MADDPG / CTDE
6. T. Rashid et al., "QMIX: Monotonic Value Function Factorisation…," *ICML* 2018. arXiv:1803.11485
7. C. Yu et al., "The Surprising Effectiveness of PPO in Cooperative Multi-Agent Games," *NeurIPS* 2022 D&B. arXiv:2103.01955 — **the five settings**
8. R. Gorsane et al., "Towards a Standardised Performance Evaluation Protocol for Cooperative MARL," *NeurIPS* 2022. arXiv:2209.10485
9. C. Campos et al., "ORB-SLAM3," *IEEE T-RO* 37(6), 2021. arXiv:2007.11898
10. R. Arandjelović et al., "NetVLAD," *CVPR* 2016; D. DeTone et al., "SuperPoint," *CVPRW* 2018; P.-E. Sarlin et al., "SuperGlue," *CVPR* 2020; P. Lindenberger et al., "LightGlue," *ICCV* 2023.
11. Z. Zheng, Y. Wei, Y. Yang, "University-1652," *ACM MM* 2020; S. Zhu, T. Yang, C. Chen, "VIGOR," *CVPR* 2021; F. Deuser, K. Habel, N. Oswald, "Sample4Geo," *ICCV* 2023.
12. Bitcraze AB, *Datasheet AI-deck 1.1 Rev 2*; *Crazyflie 2.X expansion decks* — **the deck-conflict matrix and the absence of a GPS deck**
13. Himax, *HM01B0* product page.
14. GreenWaves, *GAP8 Hardware Reference Manual* v1.5.5; WikiChip GAP8.
15. "Autonomous Navigation at the Nano-Scale: Algorithms, Architectures, and Constraints," arXiv:2601.13252, Jan 2026 *(preprint, not peer reviewed)*.
16. `pulp-platform/pulp-dronet` repository.

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F02_formation_control.md`](F02_formation_control.md) · [`F09_simulation_and_compute.md`](F09_simulation_and_compute.md) · [`../../INDEX.md`](../../INDEX.md)
