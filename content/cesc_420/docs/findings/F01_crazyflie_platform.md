# F01 · Crazyflie Platform

Hardware facts for the SRS and SDD. Every number below is from a primary source; citations at the bottom.

**The one-line design driver:** what breaks first as a Crazyflie swarm scales is **shared radio airtime** — the ~1200 packets/s per Crazyradio 2.0 is divided equally among all connected drones. So: push autonomy onboard, broadcast rather than unicast, and treat telemetry as a debug-only luxury. Everything else on this page follows from that.

Related: [IR-02](../01_idea_register.md#ir-02--communication-constrained-coordination) · [C-01](../02_constraints.md#c-01--physical--payload) · [C-06](../02_constraints.md#c-06--technical--radio-bandwidth-ceiling) · [F04](F04_network_and_latency.md)

---

## Airframes

| | 2.1 / 2.1+ | 2.1 Brushless |
| --- | --- | --- |
| Takeoff weight | 29 g | 34 g (37 g w/ guards) |
| **Max payload** | **15 g** | **40 g** |
| Flight time | 7 min | 10 min |
| Charge time | 40 min | 60 min |
| Battery | 250 mAh 1S | 350 mAh 1S |
| Frame | 92×92×29 mm | 100 mm diagonal |
| Thrust | — | 4 × 30 g ≈ 3.5:1 T/W |

2.1 and 2.1+ have identical flight numbers, so one set of platform requirements covers both. Brushless is deck-compatible **except the LED-ring deck**.

**Mixed swarms of 2.1+ and Brushless are explicitly supported by Bitcraze** — which directly supports a heterogeneous architecture using Brushless units as sensor-carrying "heavy" nodes and 2.1+ units as light nodes. Worth noting in the proposal: heterogeneity need not mean air-vs-ground alone.

**Compute:** STM32F405 (Cortex-M4, 168 MHz, 192 kB SRAM, 1 MB flash) for the application, plus nRF51822 (Cortex-M0, 32 MHz) for radio/power, linked by syslink. **192 kB SRAM is the hard ceiling on any onboard algorithm** and rules out learned policies of meaningful size.

**IMU:** BMI088 accel/gyro + BMP388 barometer.

**Expansion connector:** VCC 3.0 V @ 100 mA max, VCOM (unregulated VBAT) @ 1 A max, I²C 400 kHz, SPI, 2× UART, 1-wire deck auto-identification.

---

## Payload budget — the architecture trade

| Deck | Mass | Notes |
| --- | ---: | --- |
| Lighthouse positioning | 2.7 g | 4× TS4231 IR receivers, ~30 mA |
| Multi-ranger | 2.3 g | 5× VL53L1x ToF, 4 m range |
| Micro-SD | 1.7 g | SPI, FAT32 only, **1 kHz logging** |
| AI-deck 1.1 | 4.4 g | GAP8 + HM01B0 camera, **up to 300 mA** |

Lighthouse + Multi-ranger + SD = **6.7 g of 15 g** on a 2.1+. Add the AI-deck and it's 11.1 g. **A full sensing + logging stack fits on a 2.1+ only if vision is dropped.** If vision is in scope, it's a Brushless-only payload.

The AI-deck's 300 mA draw against a 250 mAh battery is a material hit to the 7-minute flight time — flag as a risk if vision enters scope. No published measurement of the actual cost.

---

## Positioning

| System | Accuracy | Coverage | Swarm-capable? |
| --- | --- | --- | --- |
| **Lighthouse** | 2–4 cm absolute, <1 mm precision | 8×8×3 m, max 4 base stations | Yes — onboard compute |
| LPS TWR | ~10 cm | 4–8 anchors | **No — one drone at a time** |
| LPS TDoA2 | ~10 cm | 8 anchors, ~8×8 m | Yes — unlimited tags |
| LPS TDoA3 | ~10 cm | up to 255 anchors, multi-room | Yes — unlimited tags |
| Motion capture | <1 mm | unlimited | Yes, but offboard compute |
| Flow deck v2 | **relative only** | 4 m | **No — drifts, no global frame** |

**Write formation requirements against 2–4 cm absolute accuracy, not the <1 mm precision figure**, or the test plan will fail its own acceptance criteria. This is the most common way a swarm SRS becomes untestable.

**Lighthouse V1 vs V2 — audit the lab's stock in week 1:**

| | V1 | V2 |
| --- | --- | --- |
| Update rate | ~30 Hz | ~50 Hz (independent of station count) |
| Max stations | **2 (hard)** | 4 (firmware default, raisable to 16) |
| FOV | 120°×120° | 150°H × 110°V |

**V1 and V2 cannot be mixed in one system.** A mixed inventory means half the hardware is dead weight — this is a blocking Semester 1 task ([R-03](../05_risk_register.md)).

Measured onboard (Taffanel et al., against a 300 Hz Qualisys reference): update rate 30 ± 2.4 Hz (LH1) and 34 ± **18** Hz (LH2). **That 18 Hz standard deviation — caused by periodic interference between base stations — is a real jitter source the control loop must tolerate**, and it is exactly the kind of thing the benchmarking harness ([IR-23](../01_idea_register.md#ir-23--performance-benchmarking-and-instrumentation-harness)) should measure locally rather than assume.

RMS position jitter: 0.6 mm (LH1 crossing-beam), 3.9 mm (LH1 EKF), 0.3 mm (LH2 crossing-beam), 0.7 mm (LH2 EKF); mocap 0.1 mm.

**Lighthouse limitations:** infrared, indoor-only, degrades in direct sunlight, needs line of sight to ≥1 base station, requires a geometry calibration step. **Occlusion by ground robots or by other drones in a dense formation is a first-order failure mode** and needs its own test case.

LPS TDoA3 measured ~400 packets/s system rate → ~340 TDoA measurements/s into the Kalman filter, at ~15% packet loss. That budget is shared across the whole system.

---

## Radio — the ceiling

| | Crazyradio PA | Crazyradio 2.0 |
| --- | --- | --- |
| MCU | nRF24LU1+ (8051, 16 MHz) | nRF52840 (M4F, 64 MHz) |
| Rates | 250 k / 1 M / 2 Mbps | + BLE, 802.15.4 |
| Payload | 32 bytes | 32 bytes |
| Throughput | ~800 pkt/s shared | **~1200 pkt/s shared** (fw 5.1 inline mode) |

**CRTP packet = 4-bit port + 2-bit channel + up to 30 bytes payload.** 30 bytes is the atomic unit every bandwidth calculation must build from.

Before firmware 5.1, you got ~1200 pkt/s to a *single* Crazyflie but only ~600 once two or more connected. Inline mode shares ~1200 equally. **With 10 drones that's ~120 pkt/s each, for commands and telemetry combined.** Bitcraze states the remaining bottleneck is USB/radio synchronization — so **buying more dongles beats tuning the radio**.

Firmware limit is 1 packet per millisecond per radio (recently relaxed to 2 broadcast packets), which is why the ceiling sits where it does.

CRTP link latency measured 360 µs – 1.26 ms. BLE minimum is 7.5 ms, typically ~20 ms — **BLE is disqualified for swarm control.**

### Published swarm sizes

| Result | Drones | Radios | Notes |
| --- | ---: | ---: | --- |
| Preiss et al. 2017 (Crazyswarm) | 49 | 3 | ~16/radio; required pose compression |
| Bitcraze, July 2026 | 49 | **1** | Brushless, Lighthouse, 5×5×2 m, 0.4 m spacing |
| Bitcraze, March 2025 | 9 | — | **Fully decentralized**, onboard Lighthouse + P2P, ~9 min |
| Bitcraze guidance | 3–4 | 1 | Nominal; ~10 with minimal logging; ~15 ideal |

**Write 3–4 drones per dongle into the SRS as the nominal design point.** Ten requires giving up telemetry.

How the big numbers were achieved, and the pattern to copy:

- Crazyswarm compressed position to 24-bit fixed-point and quaternions to 32 bits, fitting **two poses per 32-byte packet** and two packets per USB request.
- Crazyswarm broadcast pose at **100 Hz** while planning, state estimation and control ran **onboard at 500 Hz**.
- The 2026 single-radio 49-drone demo used the onboard **High-Level Commander**, receiving only `go_to`/spiral commands.

Crazyswarm measured end-to-end latency 8–23 ms (software estimate; actual +3 ms), growing linearly with swarm size — **26 ms at 49 vehicles**. That is a hard, published number for the "network delay" the proposal names as a core difficulty. Tracking error was <2 cm RMS on figure-8s at 0.76 m/s mean, 1.5 m/s max.

Packet loss handling: repeating swarm commands **5× every 3 ms** made dropping more than five consecutive updates very unlikely. Directly citable justification for an **idempotent repeat-N protocol** instead of a reliable transport.

The 9-drone decentralized demo is the most realistic scale reference for a 4-person capstone, and its source is published (`crazyflie-firmware-experimental`, `arena-demo` branch).

### Peer-to-peer

- `P2P_MAX_DATA_SIZE` = **60 bytes** — the hard constraint on any decentralized consensus or collision-avoidance message format.
- **Broadcast-only**; unicast still in development. Every drone hears every message, so addressing must live inside the 60-byte payload.
- P2P shares airtime with CRTP. Without the `rate_limit=100` URI option, a ground-station CRTP link will **starve** P2P traffic. Concrete SRS configuration requirement.
- P2P receive callbacks run inside the radio task and must return fast — push to a queue. Real processing there destabilizes the link.

---

## Crazyswarm2

MIT-licensed ROS 2 stack; supports 2.1(+), 2.1 Brushless, Flapper Nimble+, Bolt-based customs. Tested on **Ubuntu 22.04 / Python 3.10 / ROS 2 Humble** and **Ubuntu 24.04 / Python 3.12 / ROS 2 Jazzy**. Pin one across all four laptops in week 1 — this is a classic capstone time sink.

**Three backends, and the choice matters more than anything else in this section:**

| Backend | Broadcast? | Notes |
| --- | --- | --- |
| **C++** (crazyflie-link-cpp) | **Yes** | The only one that broadcasts |
| CFlib (Python) | **No** | Caps the swarm at a few drones per radio |
| Simulator (firmware SIL) | No | Identical ROS interfaces |

**Choosing the Python backend caps the swarm.** This is the single most consequential Crazyswarm2 fact for this project.

Services: `takeoff`, `land`, `go_to`, trajectory upload/start, emergency stop. Topics: pose, odometry, IMU, scan. Addressable to `/all` or per-drone namespace — **this list maps almost one-to-one onto the SRS functional requirements.**

Default `firmware_logging` gives 10 Hz pose per drone. Multiply by swarm size against the ~1200 pkt/s ceiling.

**The simulator backend does not support** parameters, logging, motion capture, Flow deck, Lighthouse, or LPS. That is a hard boundary on what can be validated before touching hardware — relevant given the hardware-first preference ([DR-02](../03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation)).

Known open defect, documented by the project: *"Sometimes unicast packets get lost, which is a known firmware bug."* Design around it with idempotent repeated commands.

Priority queues allow **trajectory upload during flight** — a dynamic-reassignment demo could be built on this.

---

## Safety features already in firmware

Citable in the SRS safety section rather than built:

| Mechanism | Value | Effect |
| --- | --- | --- |
| Emergency-stop watchdog | **1000 ms** | Timeout latches a locked state requiring reboot |
| `COMMANDER_WDT_TIMEOUT_STABILIZE` | 500 ms | Attitude angles reset to zero |
| `COMMANDER_WDT_TIMEOUT_SHUTDOWN` | 2000 ms | Motors shut down |
| Tumble detection | — | Motors stop, free-fall to crashed state |

The ground station must sustain **≥1 Hz per drone even when idle**. Combined with the ~1200 pkt/s ceiling, the commander timeouts give a defensible upper bound on swarm size — which is how [PD-04](../03_decision_record.md#pending-decisions) should be answered.

---

## Logging

- Firmware log block payload capped at **26 bytes** (`LOG_MAX_LEN`), 16 blocks (`LOG_MAX_BLOCKS`), 128 total operations (`LOG_MAX_OPS`).
- Micro-SD deck supports **1 kHz** logging — roughly 100× what the radio can deliver per drone in a swarm.

Taffanel et al. confirm: Crazyflie radio bandwidth is insufficient to transfer raw Lighthouse data in real time, so they logged onboard and used the radio only for start/stop. **Any high-rate data the team wants to analyze must go to the SD deck, not over the radio.** This directly shapes the benchmarking harness design ([F10](F10_benchmarking_and_measurement.md)).

---

## Open — needs a lab inventory

These are blocking and belong in the first mentor meeting ([`../../proposal/OPEN_QUESTIONS.md`](../../proposal/OPEN_QUESTIONS.md)):

1. Which airframe variant, and how many? Decides 15 g vs 40 g payload budget.
2. Lighthouse V1 or V2, how many stations? V1 caps at 2 stations / 30 Hz; they cannot be mixed.
3. Crazyradio PA or 2.0, how many? ~800 vs ~1200 pkt/s. **Is 2.0 flashed with firmware ≥5.1?** Inline mode is a firmware feature.
4. Calibrated flight volume in metres, and **does it overlap the ArUco ground-robot workspace?**
5. Ground robot platform, its compute, its ROS 2 status, and whether it consumes Crazyswarm2 message types.
6. Does the department own motion capture? Without it there is **no independent ground truth** to validate Lighthouse against in the test plan.

Two gaps worth stating plainly:

- **No Bitcraze- or Crazyswarm2-supported bridge exists between the Crazyflie stack and an overhead-camera/ArUco ground-robot system.** The team must write the coordinate-frame alignment and message bridge themselves. Difficulty is unknown without seeing the ground robots' software. This is [IR-03](../01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems) and it is the project's real technical core.
- **Nothing in the Crazyflie stack needs GPU compute.** The 8× H100 cluster is currently unmotivated by the chosen architecture — ask the mentor what he intends it for rather than assuming it has a role.

Also unresolved: practical P2P throughput at scale (unpublished), Multi-ranger update rate as configured in firmware (unpublished), and whether Crazyswarm2's broadcast advantage applies to a pure-Lighthouse swarm or only the mocap pose-streaming case.

---

## References

1. Bitcraze AB, *Datasheet Crazyflie 2.1+ Rev 1*, 2024. <https://www.bitcraze.io/documentation/hardware/crazyflie_2_1_plus/crazyflie_2_1_plus-datasheet.pdf>
2. Bitcraze AB, *Datasheet Crazyflie 2.1 Brushless Rev 3*, 2025. <https://www.bitcraze.io/documentation/hardware/crazyflie_2_1_brushless/crazyflie_2_1_brushless-datasheet.pdf>
3. J. A. Preiss, W. Hönig, G. S. Sukhatme, N. Ayanian, "Crazyswarm: A Large Nano-Quadcopter Swarm," *IEEE ICRA*, pp. 3299–3304, 2017. <https://whoenig.github.io/publications/2017_ICRA_Preiss_Hoenig.pdf>
4. A. Taffanel et al., "Lighthouse Positioning System: Dataset, Accuracy, and Precision for UAV Research," arXiv:2104.11523, 2021. <https://arxiv.org/abs/2104.11523>
5. Bitcraze AB, *Lighthouse Positioning System* documentation. <https://www.bitcraze.io/documentation/system/positioning/ligthouse-positioning-system/>
6. Bitcraze AB, *Loco Positioning System* documentation. <https://www.bitcraze.io/documentation/system/positioning/loco-positioning-system/>
7. Bitcraze AB, "New Crazyradio 2.0 Swarm-optimized firmware 5.1," Dec 2025. <https://www.bitcraze.io/2025/12/new-crazyradio-2-0-swarm-optimized-firmware-5-1/>
8. Bitcraze AB, "49 Crazyflies, 1 Crazyradio, and cflib2," Jul 2026. <https://www.bitcraze.io/2026/07/49-crazyflies-1-crazyradio-and-cflib2/>
9. Bitcraze AB, "Decentralized Brushless Swarm Demo," Mar 2025. <https://www.bitcraze.io/2025/03/decentralized-brushless-swarm-demo/>
10. W. Hönig et al., *Crazyswarm2: A ROS 2 testbed for Aerial Robot Teams*. <https://imrclab.github.io/crazyswarm2/>
11. Bitcraze AB, *CRTP* and *Peer to Peer API*, crazyflie-firmware documentation.
12. Bitcraze AB, *Crazyflie 2.X architecture*. <https://www.bitcraze.io/documentation/system/platform/cf2-architecture/>
13. STMicroelectronics, *VL53L1X Datasheet DS11054*. <https://www.st.com/resource/en/datasheet/vl53l1x.pdf>
14. Bitcraze AB, "Exploring the Swarming Potential of the Crazyflie," Jun 2025. <https://www.bitcraze.io/2025/06/exploring-the-swarming-potential-of-the-crazyflie/>

---

**Related:** [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`F02_formation_control.md`](F02_formation_control.md) · [`F10_benchmarking_and_measurement.md`](F10_benchmarking_and_measurement.md) · [`../../INDEX.md`](../../INDEX.md)
