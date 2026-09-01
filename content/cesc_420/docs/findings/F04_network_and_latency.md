# F04 · Network, Latency and Computational Effort

This is the evidence base for the proposal's own problem statement — *"network throughput, delay, computational effort."* Right now that claim is unsupported. Everything here exists to support it with numbers.

Related: [IR-02](../01_idea_register.md#ir-02--communication-constrained-coordination) · [IR-23](../01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness) · [C-06](../02_constraints.md#c-06--technical--radio-bandwidth-ceiling) · [C-07](../02_constraints.md#c-07--technical--24-ghz-is-a-shared-band) · [F01](F01_crazyflie_platform.md) · [F10](F10_benchmarking_and_measurement.md)

---

## The bandwidth budget — put this equation in the SRS

Packets per second on one Crazyradio:

> **pkt/s = ⌈N/4⌉ · f_pos  +  N · f_cmd  <  ~1000**

where the first term is packed-position **broadcast** (4 agents per packet) and the second is per-drone **unicast** setpoints.

Derived from firmware, not estimated:

| Constant | Value | Source |
| --- | --- | --- |
| `CRTP_MAX_DATA_SIZE` | **30 bytes** | `crtp.h` |
| `extPositionPackedItem` | 7 B → **4 per packet** | `crtp_localization_service.c` |
| `extPosePackedItem` | 11 B → **2 per packet** | same |
| `fullStatePacket_s` | 28 B → 30 B on wire | `crtp_commander_generic.c` |
| Crazyradio firmware ceiling | ~1000 pkt/s (1/ms) | Bitcraze forum |

### The result that justifies the architecture

| Architecture | Agents | Rate | Radio load |
| --- | ---: | ---: | ---: |
| Per-drone **unicast** full-state | 8 | 100 Hz | **1000 pkt/s = 100%** |
| Packed-position **broadcast** | **30** | 100 Hz | 800 pkt/s = 80% |

**Roughly a 4× swarm-size multiplier on identical hardware, purely from the architecture choice.** Position-only broadcast doubles drones-per-packet versus pose broadcast (4 items vs 2) — that alone is the lever that decides how many Crazyflies fit on one radio.

**The ceiling is USB/firmware, not radio physics.** From the nRF24L01+ on-air frame (1 B preamble + 5 B address + 9-bit packet control + payload + 2 B CRC), a 32-byte packet occupies 329 bits = **164.5 µs** at 2 Mbps. Uplink + ACK = 329 µs → an air-limited ceiling of **~3040 pkt/s**. The observed ~1000 pkt/s is therefore a software bottleneck. That "where does the limit actually come from" analysis is exactly what the SDD wants — and it says **buying dongles beats tuning the radio**.

**Vendor-primary latency floor:** CRTP round trip is **360 µs** (1-byte packet) to **1.26 ms** (32-byte) at 2 Mbps with no retries. BLE is ~20 ms — **disqualified for closed-loop formation control.**

**Ground segment (Wi-Fi):** bytes/s = N · f_update · (payload + **44 B RTPS** + 28 B UDP/IP), before 802.11 framing and discovery. Four ground robots publishing a 28-byte state at 50 Hz costs ~20 kB/s of payload and **~20 kB/s more of pure protocol overhead** — for small messages, overhead exceeds payload. That is the quantitative basis for **aggregating agent states into one message rather than one topic per agent**.

**Lighthouse removes position streaming from the radio budget entirely**, because the estimate is computed onboard. That is a decisive architectural advantage over the mocap-style setups whose bandwidth numbers dominate the Crazyswarm literature — and it's worth saying explicitly in the proposal.

---

## Latency and loss thresholds

### The single best argument in this document

Buonocore et al. simulated 6 UAVs under a centralized formation controller at 10 Hz:

| Loss model | Max agent error (easy scenario) | Hard scenario (corridor + obstacles) |
| --- | --- | --- |
| Ideal | 0.41 m | 0.47 m |
| i.i.d. Bernoulli | 0.42 m | — |
| **Gilbert (bursty)** | 0.67 m | **197.06 m, with collisions** |
| Extended Gilbert | 0.83 m | — |

**Average packet-loss rate is the wrong requirement. Burst length is what breaks formation control.** And it does not degrade gracefully — it falls off a cliff once obstacle-avoidance and formation tasks compete. Write the requirement against burst length, and write the cliff into the test plan as a named failure mode.

*Caveat for honesty:* the paper inherits its Gilbert parameters from Jiang & Schulzrinne (2000) without restating them, so the result is qualitatively decisive but **cannot be quoted as "at X% loss."** Pull the original if a numeric loss requirement is needed.

### Published delay tolerance

A 2026 *Drones* study gives the only tabulated τ_max values found:

| Formation | τ_max |
| --- | --- |
| 3 UAVs, 3 m separation | 270.4 ms |
| 5 UAVs, 5 m | 300.4 ms |
| 10 UAVs, 3 m | 308.3 ms |
| 25 UAVs, 25 m | 6248.3 ms |

(under 15% allowed formation-error degradation, 0.99 reliability). Measured per-hop delay was **7.78 ± 2.94 ms, skewness 4.72, kurtosis 43.9, P(delay > 15 ms) ≈ 1.8%** — a **heavy-tailed** distribution, not Gaussian. That justifies specifying a **p99 latency** in the SRS rather than a mean.

**Extrapolate with care.** That study is outdoor, 3–25 m separation, 5 m/s. Its own trend is *tighter spacing → lower tolerance*, so indoor Crazyflie numbers at 0.3–0.5 m spacing are likely **far below** its 270 ms floor. **No published latency- or loss-tolerance threshold exists for an indoor nano-quadcopter formation at that spacing.** Measuring it — inject delay, report the formation-error knee — is a strong Semester 1 hardware experiment that fits the team's stated preference exactly, and it's a genuine result.

Cross-check with theory: [F02](F02_formation_control.md) gives τ* = π/(2λ_max) as an analytic bound. Measured knee vs analytic bound in one figure is a strong midterm slide.

### Standards anchor

**3GPP TS 22.104** Table 5.2-1 specifies **cooperative robotic motion control** at a 1–50 ms transfer interval with end-to-end latency below the transfer interval and service availability >99.9999%. Factory motion control rows go to 500 µs–2 ms at up to 99.999999%.

This lets the team argue their **100 Hz / 10 ms budget is deliberately two orders of magnitude looser** than industrial hard real-time and therefore achievable on 2.4 GHz — a citable justification for a chosen number rather than an invented one.

### Graceful degradation, with a citation

Kar & Moura prove almost-sure convergence of average consensus under random link failures and channel noise using decaying weights — at the explicit cost of a **slower rate**, not divergence. Consensus degrades in *speed*, not stability.

Quantified: for i.i.d. link failure probability p, the expected Laplacian is (1−p)L, so λ₂ scales by (1−p) and time-to-consensus inflates by ~1/(1−p).

| Link loss | Iteration cost |
| --- | --- |
| 10% | ~+11% |
| 50% | ~2× |

That turns "graceful degradation" into a requirements-table row: *"consensus shall converge within 2× nominal iterations at 50% link loss."*

---

## ROS 2 / DDS over Wi-Fi

### Do not run DDS multicast over the lab Wi-Fi

**RFC 9119** (IETF): Wi-Fi multicast frames are **not acknowledged**, are sent at the **slowest rate of all connected devices** (a >3 orders of magnitude penalty vs optimal unicast), and *"it is not uncommon for there to be a packet loss rate of 5% or more."* IETF-primary, and a citable 5% baseline for the requirements table.

### Discovery scales quadratically

> discovery traffic ∝ **n · (n−1) · (r + w)**

n = participants, r = readers each, w = writers each. **Node count, not message rate, is what makes ROS 2 fall over.** Put this formula in the SDD.

Measured (TurtleBot3, ROS 2 Foxy, SLAM over Wi-Fi to RViz2):

| Stack | Discovery cost |
| --- | --- |
| DDS | 686 packets / 251,576 B |
| Zenoh | 31 packets / 6,617 B (**−97.4%**) |
| Zenoh + generalization + warm start | 1 packet / 82 B (**−99.97%**) |

### The three QoS pathologies, with one-line fixes

| Pathology | Effect | Fix |
| --- | --- | --- |
| Default 64 KB `maxMessageSize` | 44 IP fragments; losing one kills the sample. Delivery fell **77% → 9%** at 1% PER as payload grew 33 KB → 330 KB | set to **1472 B** |
| Default 3 s (0.33 Hz) heartbeat/AckNack | burst traffic **>160 Mb/s** for 65 KB msgs at 30 Hz; 512 KB latency 56 ms ideal → **477 ms** at 1% PER | heartbeat = **2× publish rate** |
| Default 400-sample HistoryCache | after a 10 s outage, reception recovers at only **5 Hz vs 30 Hz** — backlog saturates the channel on reconnect | size the cache |

That third one is the **congestive buffer burst** a swarm hits *every time a robot walks out of Wi-Fi coverage and back* — trivially testable in the System Test Plan.

### Middleware trade study

Real multi-robot mesh measurements (Chovet et al.), Zenoh vs the DDS options:

| Metric | vs FastDDS | vs CycloneDDS |
| --- | --- | --- |
| Delay | **−76%** | −69.9% |
| Reachability | **+146.9%** | +58.2% |
| CPU | −41.3% | −39.8% |
| RAM | 54.6 MB vs 34 MB | vs 29.3 MB |

FastDDS showed delays **exceeding 50 seconds** in some 32–64 KB runs — a concrete worst case to design a watchdog and fallback against. Independent work confirms CycloneDDS wins on Ethernet but **Zenoh wins on Wi-Fi**.

`rmw_zenoh_cpp` reached **Tier 1 in ROS 2 Kilted Kaiju (May 2025)** — it is a supported first-class RMW, not an experiment, which removes the maturity risk from choosing it.

**Lower-effort mitigations if staying on DDS:**

- **Fast DDS Discovery Server** — unicast client-server discovery, no application code change. v2 also filters discovery data to topics a node actually uses.
- **CycloneDDS** — `<AllowMulticast>false</AllowMulticast>` + explicit `<Peers>`, or `<AllowMulticast>spdp</AllowMulticast>`; pin the interface with `<NetworkInterfaceAddress>`. Static peers also eliminate startup discovery storms.

### QoS choice, with rationale

For periodic state broadcast at 50–100 Hz: **BEST_EFFORT + KEEP_LAST(1)**. A retransmitted stale pose is worse than a dropped one. The ROS 2 QoS design article explicitly cites *"inexpensive robots using unreliable wireless networks"* and notes TCP is unsuitable for lossy links — so this is a documented design decision, not a default.

---

## 2.4 GHz coexistence

**Two different channel numbering schemes — confusing them is a classic lab mistake:**

- Wi-Fi channel n → **2407 + 5n MHz**, ~22 MHz occupied. Non-overlapping in the US: **1 (2412), 6 (2437), 11 (2462)**.
- Crazyradio channel k → **2400 + k MHz**, range 0–125.

Nordic's guidance is to sit in the gaps between Wi-Fi 1/6/11:

| Frequency gap | Crazyradio channels |
| --- | --- |
| 2420–2427 MHz | 20–27 |
| 2445–2454 MHz | 45–54 |
| 2472–2480 MHz | 72–80 |

> ⚠ **Corrected 2026-08-31 after adversarial verification.** An earlier draft claimed users report spacing radios "≥20 channels apart" and proposed channels 25/50/75. **The ≥20 figure is unsourced** — it does not appear in any Bitcraze document. The only documented figures are:
>
> - Bitcraze client user guide: at **2M datarate, copter channels should be 2 apart (2 MHz)**.
> - *"In most countries channel 0 to 80 is OK to use but this should be checked with your local regulations."*
> - The Crazyswarm example splits a fleet by *Crazyflie number modulo the number of channels* — cf1→80, cf2→90, cf3→100 — **a spacing of 10, motivated by the ~15-per-radio limit, not by Wi-Fi.**
>
> **A much more important architectural fact surfaced in the same check:** Bitcraze states that **all Crazyflies on a given radio must share ONE channel**, because *"the use of broadcast packet to send the position of multiple Crazyflie at the same time … only works if all Crazyflie connected to each radio have the same channel."* Channel diversity is therefore *between* radios, never within one.

**The defensible plan:** one channel per radio, ≥2 apart at 2M datarate, all inside 0–80, positioned in the Nordic gaps between whichever 802.11 channels the campus actually uses — which requires the RF survey below. State the survey as the input to the channel decision rather than picking numbers in advance.

> ⚠ **Config-review item.** Bitcraze says channels 0–80 (2400–2480 MHz) are acceptable in most countries, but the **Crazyswarm configuration documentation's worked example assigns channels 80, 90 and 100** — i.e. 2480, 2490 and 2500 MHz. **The latter two are above the 2400–2483.5 MHz ISM band edge.** Copying the Crazyswarm example channel plan would put the team out of band. Worth a risk-register entry.

**The swarm hardware is blind to interference.** The nRF24L01+ has no true RSSI — only a **1-bit Received Power Detector** indicating whether channel power exceeds −64 dBm. Interference must be characterized with an external tool (Wi-Fi scanner or spectrum analyzer) as a documented pre-flight procedure.

**But the retry counter is free instrumentation.** The Crazyradio protocol returns a **retransmission count in bits 4–7 of the ACK status byte** (auto-retry count 0–15, default 3; delay 250–4000 µs in 250 µs steps). Log it per packet and plot it — evidence for the test plan and the final presentation at zero cost.

**Objective pre-flight criterion:** enterprise Wi-Fi practice treats **~50% channel airtime utilization** as the degradation threshold, with capacity problems appearing above **70% channel-busy** plus high retry rates from clients that still have good RSSI. That is a measurable pass/fail for an RF survey, rather than "the Wi-Fi seemed busy."

---

## Computational effort

**The honest version of the claim:** the STM32F405 is a Cortex-M4 at ~160–168 MHz with ~192–196 kB RAM. Anything running onboard must fit in that and complete in a few milliseconds.

**GLAS is the existence proof** that it can be done: a fully decentralized neural policy runs onboard a Crazyflie 2.0 at **40 Hz** using only relative states of nearby neighbours and obstacles, with policy evaluation taking **3.4 ms (1 neighbour) to 5.0 ms (3 neighbours)** — and **zero inter-agent radio traffic**. That is both a compute budget and an architecture argument.

**CTDE's defining bandwidth property:** the centralized critic and global state are used **only during training**, so execution needs only each agent's local observation. Run-time communication cost is strictly lower than a fully centralized architecture.

**This is the argument that gives the H100 cluster a role.** Train offline on the HPC; execute onboard with zero inter-agent messages during flight. If the design is CTDE, the cluster **does not appear in the run-time latency budget at all** — and that distinction should be stated explicitly in the proposal rather than left ambiguous. (If any part of the control loop *does* touch the cluster at run time, that hop must be measured; no numbers were found for HPC-to-lab-floor inference latency.)

ArUco detection costs ~10 ms/frame on one core — the floor for the ground localization loop, to which ROS 2 transport latency must be added.

---

## Open — and three are cheap experiments worth doing

1. **Which Crazyradio does the lab own?** PA (nRF24LU1) or 2.0 (nRF52840)? Re-derive the swarm-size table once known. Also: **the ~1000 pkt/s limit is forum-sourced, not datasheet-sourced.** Verify empirically by ramping broadcast rate until loss counters rise — which also produces a nice measured figure for the report.
2. **Lab 2.4 GHz occupancy** — unresearchable remotely. Needs a site survey (channel utilization at the flight volume, at quiet *and* class hours) before any channel plan is committed.
3. **End-to-end camera + ArUco pipeline latency** — almost certainly unmeasured. Detection alone is ~10 ms; exposure, capture, USB/GigE transfer and the ROS 2 hop are all unaccounted for. **A one-afternoon timestamp round-trip measurement.**
4. **Do the ground robots run ROS 2 at all**, and on which RMW and distro? Every mitigation above is vendor- and distro-specific.
5. **Crazyradio packet-error rate vs co-channel Wi-Fi airtime** — no published measurement exists. The team can generate it by logging the ACK retransmission counter against a Wi-Fi channel-utilization reading. **Genuinely novel, cheap, and a good poster figure.**
6. **Regulatory check:** whether the Crazyradio 2.0's 20 dBm PA with the supplied 2 dBi antenna complies with the applicable EIRP limit at the intended power setting. Likely fine under 47 CFR §15.247 in the US, but confirm the operating power setting rather than assume — see [F05](F05_standards_and_regulations.md).

---

## References

1. J. A. Preiss, W. Hönig, G. S. Sukhatme, N. Ayanian, "Crazyswarm: A Large Nano-Quadcopter Swarm," *IEEE ICRA* 2017, 3299–3304.
2. B. Rivière, W. Hönig, Y. Yue, S.-J. Chung, "GLAS: Global-to-Local Safe Autonomy Synthesis…," *IEEE RA-L* 5(3):4249–4256, 2020. arXiv:2002.11807.
3. L. R. Buonocore, V. Lippiello, S. Manfredi, F. Ruggiero, B. Siciliano, "Effects of Packet Losses on Formation Control of Unmanned Aerial Vehicles," *IFAC World Congress* 2014. — **burst vs average loss**
4. "Measurement-Informed Latency Limits for Real-Time UAV Swarm Coordination," *Drones* 10(4):310, 2026. doi:10.3390/drones10040310 — τ_max table
5. S. Kar, J. M. F. Moura, "Distributed Consensus Algorithms in Sensor Networks With Imperfect Communication," *IEEE T-SP* 57(1):355–369, 2009. arXiv:0711.3915.
6. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, "Randomized Gossip Algorithms," *IEEE T-IT* 52(6):2508–2530, 2006.
7. RFC 9119, "Multicast Considerations over IEEE 802 Wireless Media," IETF, Oct 2021.
8. S. Lee, T. Kim, J. Chae, K.-J. Park, "Optimizing ROS 2 Communication for Wireless Robotic Systems," arXiv:2508.11366, 2025. — the three QoS pathologies
9. L. P. Chovet et al., "Performance Comparison of ROS2 Middlewares for Multi-robot Mesh Networks in Planetary Exploration," arXiv:2407.03091, 2024.
10. J. Zhang et al., "Comparison of Middlewares in Edge-to-Edge and Edge-to-Cloud Communication for Distributed ROS 2 Systems," *JINT*, 2024. arXiv:2309.07496.
11. D. P. Klüner, S. Kowalewski, A. Kampmann, "StreamRTPS: Increasing DDS Bandwidth Efficiency by Reducing Protocol Overhead," arXiv:2606.14214. — 44 B RTPS overhead
12. A. Corsaro et al., "Minimizing Discovery Overhead in ROS 2," ZettaScale, Mar 2021. <https://zenoh.io/blog/2021-03-23-discovery/>
13. 3GPP TS 22.104 / ETSI TS 122 104 V17.7.0, "Service requirements for cyber-physical control applications in vertical domains," May 2022.
14. Bitcraze AB, *Crazyflie 2.x Architecture*. <https://www.bitcraze.io/documentation/system/platform/cf2-architecture/>
15. Bitcraze AB, *USB and Radio protocol of the Crazyradio dongle*. — channel map, ARD/ARC, retransmission counter
16. Nordic Semiconductor, *nRF24L01+ Product Specification v1.0*, 2008. — on-air frame
17. Nordic DevZone Q&A #38005 — Wi-Fi channel gaps; 1-bit RPD
18. Open Robotics, *ROS 2 QoS Design Article*. <https://design.ros2.org/articles/qos.html>
19. eProsima, *Fast DDS Discovery Server* documentation.
20. Eclipse Foundation, *Cyclone DDS discovery* documentation.
21. Open Robotics, *Kilted Kaiju Release Notes*, May 2025; `ros2/rmw_zenoh`.
22. IEEE Std 802.11-2020 — 2.4 GHz channel plan.
23. `bitcraze/crazyflie-firmware`: `crtp.h`, `crtp_localization_service.c`, `crtp_commander_generic.c` — **the packet sizes behind every calculation here**

---

**Related:** [`F01_crazyflie_platform.md`](F01_crazyflie_platform.md) · [`F02_formation_control.md`](F02_formation_control.md) · [`F03_air_ground_integration.md`](F03_air_ground_integration.md) · [`F10_benchmarking_and_measurement.md`](F10_benchmarking_and_measurement.md) · [`../../INDEX.md`](../../INDEX.md)
