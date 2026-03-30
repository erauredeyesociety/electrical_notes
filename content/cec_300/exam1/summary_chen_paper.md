# Chen et al. 2025 -- Spacecraft Avionics System Technology: Research Status and Prospect

**Citation:** C. Chen, Y. Yin, K. Huang, X. He, "Research status and prospect of avionics system technology for spacecraft," *Chinese Journal of Aeronautics*, 2025. DOI: 10.1016/j.cja.2025.104048

---

## 1. Avionics Architecture Evolution (Section 2.1)

The paper traces spacecraft avionics from **Federated** (discrete, separate boxes per function) through **IMA** (Integrated Modular Avionics) to **DIMA** (Distributed Integrated Modular Avionics).

### Five Major Architectures Compared

| Architecture | Proposer | Year | Key Idea | Best For |
|---|---|---|---|---|
| **SPA** (Space Plug-and-play Avionics) | AFRL | 2004 | USB-like hot-plug, self-organizing network, middleware auto-discovers components | Rapid design / rapid response missions |
| **SAVOIR** (Space AVionics Open Interface aRchitecture) | ESA | 2007 | Open interfaces, interoperability, multi-standard (CCSDS + ECSS), uses 1553B + SpaceWire + TTE | Large missions requiring multi-vendor integration |
| **OMAC4S** (Open Modular Avionics for Space) | Airbus / TTTech | 2013 | TTE backbone, multi-core CPU, time-space partitioning OS, Line Replaceable Units (LRUs) | Highly modular / reusable projects |
| **DIMA** (Distributed Integrated Modular Avionics) | NASA | 2018 | Physical distribution + functional integration, TTE backbone, CCSDS protocols, advantageous in SWaP | High-reliability projects (Artemis / Lunar Gateway) |
| **MUSTANG** (Modular Unified Space Technology Avionics for Next Gen) | NASA | 2019 | Backplane-less modular design, maximum functionality in minimal size | Deep space exploration missions |

**Key takeaway:** SAVOIR and DIMA are the two most widely studied and adopted architectures (NASA and ESA mainstream). MUSTANG expected to see wider future use.

### Architecture Trend in China
- Evolved from centralized to distributed networked to distributed integrated modular.
- Small satellites trend toward **centralized** architectures (e.g., Beijing III satellite uses a single integrated computer with CAN bus, reducing mass 60% and power 20%).
- Large/complex spacecraft trend toward **DIMA** (physical distribution, functional integration).

---

## 2. Databus Technologies (Section 3.2)

### Bus Comparison Table (Table 3 from paper)

| Feature | CAN | 1553B | SpaceWire | Ethernet | TTE | TSN |
|---|---|---|---|---|---|---|
| **Topology** | Bus | Bus | Point-to-point / switched | Point-to-point / bus / switched | Point-to-point / switched | Point-to-point / bus / switched |
| **Max Nodes** | 128 | 32 | No limit | No limit | No limit | No limit |
| **Scalability** | No | No | Via switch | Via switch | Via switch | Via switch |
| **Data Rate** | Max 1 Mbit/s | 1-10 Mbit/s | 2-400 Mbit/s (1 Gbit/s w/ fiber) | 10/100/1000 Mbit/s | 100 Mbit/s / 1 Gbit/s | 10 Gbit/s / 25 Gbit/s |
| **Maturity** | Widely used | Widely used | Widely used | Widely used | Starting use | Starting use |
| **Application** | Automotive, electronics, spacecraft | Aviation, spacecraft | Aviation, spacecraft | Every field | Automotive, aviation, spacecraft | Automotive, electronics |

### Bus Details

- **CAN**: Low-speed (max 1 Mbit/s), simple, widely used in small satellites (Galileo GIOVE-A, Beijing III, NovaSAR-1). Good for low-SWaP platforms.
- **1553B**: Legacy standard backbone for spacecraft (1-10 Mbit/s). Used in Chinese space station system network, Asia-Pacific 6D, Dongfanghong V, BeiDou-3. Reliable but bandwidth-limited.
- **SpaceWire**: ESA-developed high-speed bus for spacecraft. Flexible topology, point-to-point full-duplex, good fault/error detection. **SpaceFibre** is next-gen (up to 1 Gbit/s). Used in SAVOIR architecture.
- **TTE (Time-Triggered Ethernet)**: Created by TTTech. Adds time-triggered modes to standard Ethernet for **deterministic latency**. Supports mixed high/low-speed data on single network. **Used in Orion spacecraft and Lunar Gateway backbone.** Key for missions demanding both high bandwidth and deterministic timing.
- **TSN (Time-Sensitive Networking)**: Based on AVB, IEEE 802.1 standard. Very high bandwidth (10-25 Gbit/s). Deterministic real-time via clock synchronization and bandwidth reservation. Forward-compatible with standard Ethernet. Standards still being refined; suitability for space still under evaluation.

### Bus Selection by Mission Type
- **Small satellites / CubeSats**: CAN bus preferred -- low SWaP, simple, sufficient for low data rates.
- **Traditional large spacecraft / constellations**: 1553B backbone with SpaceWire for high-speed payload data.
- **High-reliability crewed / deep space**: TTE backbone (Orion, Lunar Gateway) -- deterministic latency + high bandwidth on single network.
- **Future (2030+)**: TTE and TSN expected to become the standard spacecraft backbone buses.

---

## 3. SWaP-C Considerations: Small vs. Large Spacecraft

### Small Satellites
- Centralized architecture (single integrated computer).
- CAN bus for data management -- minimal wiring, low power.
- COTS components with radiation hardening to reduce cost.
- Beijing III: CAN bus reduced satellite mass by 60%, power by 20%.
- FPGA-based payload processing.

### Large / Complex Spacecraft (Orbiters, Space Stations, Deep Space)
- DIMA architecture: physical distribution, functional integration.
- TTE backbone network for deterministic mixed-rate data.
- Multiple redundant on-board computers with rad-hard processors (RAD5545, LEON4).
- DIMA is "advantageous in terms of size, weight, and power, allowing functional integration with less hardware."
- BeiDou-3 avionics: hierarchical distributed system reduced weight by 30%+.
- Chang'e-5 orbiter: resource sharing via modular power/info/RF modules reduced weight by ~40%.

---

## 4. Development Roadmap (Section 4)

### Stage 1: 2025-2030
- Architecture: Distributed integrated modular (functional integration + physical distribution)
- Bus: SpaceWire + Ethernet + TTE hybrid networks
- Computing: Multi-core hybrid heterogeneous processors
- Autonomy: Autonomous survival, mission, and health management
- Software: Software-defined payloads and networks

### Stage 2: 2030-2035
- Architecture: General open system (on-demand service, random access)
- Bus: TTE + TSN
- Computing: Commercial servers, many-core processors, brain-inspired and space supercomputing
- Autonomy: Autonomous scientific exploration, on-orbit decision-making
- Software: Full software-defined spacecraft with real on-orbit functional reconfiguration

---

## 5. Network Interconnection Protocols (Section 3.1)

| Protocol | Strength | Weakness |
|---|---|---|
| **TCP/IP** | Low cost, ubiquitous | "Best-effort" only, unsuitable for deep space |
| **CCSDS** | Refined for space, verified on 1000+ spacecraft | Cannot directly connect to terrestrial Internet |
| **DTN** (Delay/Disruption Tolerant Network) | Store-and-forward, ideal for deep space high-latency links | Newer, still developing |

**Future direction:** Integrated system combining CCSDS + TCP/IP + DTN for full interoperability from deep space to ground.

---

## 6. Key Points for Exam Relevance

- **Exam Essay 2c** asks to recommend a databus for a minisatellite (low SWaP) vs. a Europa orbiter (high bandwidth, deterministic). This paper directly supports:
  - **Minisatellite**: CAN bus -- low SWaP, simple, proven on small satellites.
  - **Europa orbiter**: TTE -- high bandwidth, deterministic latency, proven on Orion/Lunar Gateway, suitable for complex missions with many subsystems and payloads.
- The paper's Table 3 is an excellent reference for justifying bus selection.
- DIMA architecture (used for Lunar Gateway) is directly relevant to the orbiter design question.

---

## 7. ADS-B for Space Operations (Stansbury 2018 -- Supplementary)

The Stansbury paper covers adapting ADS-B (UAT, 978 MHz) for tracking suborbital reusable launch vehicles (sRLVs) through the NAS.

**Key points:**
- ADS-B uses GPS position (not radar) for surveillance -- broadcasts state vector once/second.
- Two standards: UAT (978 MHz, <18,000 ft GA) and 1090ES (>18,000 ft transport).
- UBR-ERAU payload upgraded GPS to handle altitudes >60,000 ft and velocities >1,000 knots (beyond COCOM limits).
- **Altitude limit of UAT standard: 101,337.5 ft MSL** -- implemented "roll-over" workaround.
- Flight tested on Near Space Corp balloon (94,025 ft), Up Aerospace SpaceLoft XL sounding rocket (384,100 ft apogee), and Terminal Velocity Aerospace RED-4U reentry vehicle.
- SL-8 rocket flight: 73.8% tracked overall, 95.9% on descent, position accuracy avg ~54 ft altitude error.
- GBT stations have 250-300 NM range; terrain impacts tracking at launch/recovery.
- Conclusion: ADS-B is a viable means for real-time tracking of commercial space vehicles to mitigate impact on routine NAS operations.

---

## 8. Homework 2 Grading Notes

- **Score: 78/100** (visible from graded submission).
- Grading comment on Page 3: "-3 Does not meet the length requirements. 10/15"
- Homework covered: DME pulse simulation (Problem 1, 50 pts), VOR indicator reading (Problem 2), ILS questions (Problem 3), GPS essay (Problem 4, 500-word min), satellite sensors/actuators (Problem 5).
