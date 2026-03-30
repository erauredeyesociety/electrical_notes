# CEC 300 Exam 1 -- Consolidated Study Summary

## Module 2b: Satellite Navigation (GNSS)

### GPS Overview

- GNSS (Global Navigation Satellite System) enables navigational positioning and timing solutions synchronized with UTC.
- Examples: US Navstar GPS, GLONASS.
- GPS constellation: 24 satellites in Medium Earth Orbit (MEO).
- GPS orbit period: 1/2 sidereal day (11h 58m 2s = 43,082 s).
- Orbital radius: approximately 26,562 km.
- Operational since Dec 1993; full 24-satellite constellation online Jan 17, 1994.
- Satellites transmit on UHF-band (line-of-sight only).
- At least 4 satellites needed for a position fix; more satellites improve accuracy and enable integrity monitoring.

### GPS Segments

| Segment | Role |
|---------|------|
| Space | Satellites broadcasting PRN codes and ephemeris data |
| User | Receivers (aircraft, ships, ground vehicles, fixed stations, suborbital) |
| Ground/Control | Monitors health, adjusts satellite orbits, synchronizes atomic clocks |

### GPS Signal Structure

| Signal | Frequency | Notes |
|--------|-----------|-------|
| L1 | 1575.42 MHz (154 f0) | C/A code and P(Y) code |
| L2 | 1227.60 MHz (120 f0) | P(Y) code only |
| L1C | 1575.42 MHz | Backward-compatible with L1; pilot code, overlay code, CNAV-2 format |
| L2C | 1227.60 MHz | Civil moderate (CM) and civil long (CL) codes, multiplexed at 1023 kHz |
| L5 | 1176.45 MHz (115 f0) | Safety-of-life; ranging code (I5/Q5 in quadrature), CNAV format |

Where f0 = 1023.00 MHz (fundamental frequency from high-stability quartz oscillator).

### C/A Code (Coarse Acquisition)

- Pseudorandom number (PRN) code unique to each satellite.
- Generated from two 10-bit polynomials (Gold Codes).
- Length: 1,023 chips.
- Data rate: 1.023 Mb/s.
- Period: 1 ms.
- Each of 32 satellites has a unique C/A code.

### P(Y) Code (Precision Code)

- Much longer than C/A code: 2.35 x 10^14 chips.
- Rate: 10.23 Mb/s.
- Period: 7 days.
- Available on both L1 and L2.
- Called P-code when unencrypted; Y-code when encrypted (selective availability).
- Selective availability encryption was turned off by presidential order.

### Gold Code Generation (C/A Code via LFSRs)

Gold codes are generated using two 10-bit Linear Feedback Shift Registers (LFSRs):

**Stage 1 (G1 register):**
- Polynomial: 1 + X^3 + X^10.
- All 10 bits initialized to 1.
- Each iteration: XOR bits 3 and 10, feed result into bit 1; shift all bits right.
- Bit 10 output is sent to the final XOR with Stage 2.

**Stage 2 (G2 register):**
- Polynomial: 1 + X^2 + X^3 + X^6 + X^8 + X^9 + X^10.
- All 10 bits initialized to 1.
- Each iteration: XOR bits 2, 3, 6, 8, 9, 10 to produce feedback; shift right.
- Each satellite (SV) has a unique pair of "tap" bits from Stage 2 (e.g., SV1 uses taps [2,6], SV2 uses [3,7], etc.).
- The PRN chip output = XOR(Stage 2 tap bits) XOR (Stage 1 output bit).

**XOR / Modulo-2 Addition:**
- XOR(A, B, C, ...) = (A + B + C + ...) mod 2.
- If the count of high bits is even, result = 0; if odd, result = 1.

**SV-to-Tap Mapping (Stage 2):**
SV1:[2,6], SV2:[3,7], SV3:[4,8], SV4:[5,9], SV5:[1,9], SV6:[2,10], SV7:[1,8], SV8:[2,9], SV9:[3,10], SV10:[2,3], SV11:[3,4], SV12:[5,6], SV13:[6,7], SV14:[7,8], SV15:[8,9], SV16:[9,10], SV17:[1,4], SV18:[2,5], SV19:[3,6], SV20:[4,7], SV21:[5,8], SV22:[6,9], SV23:[1,3], SV24:[4,6], SV25:[5,7], SV26:[6,8], SV27:[7,9], SV28:[8,10], SV29:[1,6], SV30:[2,7], SV31:[3,8], SV32:[4,9].

Process repeats for 1,023 iterations to produce the full C/A code sequence for a given SV.

### GPS Ranging Process

1. Both the GPS satellite and receiver generate the same PRN code (C/A or P) at a given time.
2. **Autocorrelation**: the receiver correlates its locally generated code against the received signal to determine the phase shift (time delay).
3. The phase shift represents the **time-of-flight** of the signal from satellite to receiver.
4. **Pseudorange** = speed of light x time-of-flight. This gives the distance from the satellite.
5. Using the satellite's broadcast **ephemeris** (orbital parameters), the receiver knows the satellite's position, so the receiver lies on the surface of a sphere of radius = pseudorange centered on that satellite.
6. With 3 satellites: intersection narrows to two points. With 4 satellites: resolves position uniquely and solves for the receiver clock bias.

**Why "pseudorange"?** The receiver clock is not an atomic clock, so the measured range contains a clock-bias error. The 4th satellite measurement allows solving for the clock offset.

### Navigation Message

- Master frame: 25 subframes, 30 seconds each, total 12.5 minutes to transmit.
- Each frame: 5 subframes, each with 10 words of 30 bits.
- First two words of each subframe: TLM (telemetry -- status, age of ephemeris) and HOW (handover word -- time of GPS week, aids P-code acquisition).
- Contains ephemeris data: semi-major axis (A), semi-minor axis (B), right ascension (Omega_0), inclination (I_0), ellipticity (e), argument of perigee (omega).

### Atomic Clocks

- Each satellite carries 4 atomic clocks: 2 cesium (primary), 2 rubidium (secondary).
- Synchronized across constellation as "GPS Time," which is synchronized with UTC.
- A quartz clock is insufficient: 1 microsecond offset produces approximately 300 m error.
- Ground stations send periodic corrections.

### GPS Quality Metrics

**Position Dilution of Precision (PDOP):**
- Indicates quality of satellite geometry relative to the receiver.
- Higher PDOP = worse accuracy.
- 1-2: Excellent. 3-5: Good to moderate. 6+: Poor.
- Factors: satellite geometry (spread across sky), number of satellites, receiver quality, environment (solar storms).

**Other DOP metrics:**
- HDOP: horizontal. VDOP: vertical. TDOP: time.

**Estimated Position Uncertainty (EPU):**
- Radius (in NM) around current position with >95% confidence.
- Used in performance-based navigation / RNAV.

### GPS Error Sources

| Error Source | Description |
|-------------|-------------|
| Ionospheric delay | Signal slows passing through ionosphere; varies with solar activity |
| Tropospheric delay | Lower atmosphere effects on signal propagation |
| Satellite clock error | Drift in onboard atomic clocks (corrected by ground segment) |
| Ephemeris error | Inaccuracies in broadcast orbital parameters |
| Multipath | Signal reflections off buildings, terrain before reaching receiver |
| Receiver noise | Internal noise and processing limitations of the GPS receiver |
| Geometric dilution (PDOP) | Poor satellite geometry amplifies position error |
| Selective availability | Intentional degradation (historically; now turned off) |

### GPS Augmentation Systems

**Standard GPS accuracy:** Horizontal +/-13 m, Vertical +/-22 m, Time +/-40 ns.

**Differential GPS (DGPS):**
- Base station at a surveyed location identifies corrections (mainly ionospheric noise).
- Corrections shared with nearby equipped receivers.

**WAAS (Wide Area Augmentation System):**
- 38 receiver sites forward signals to a master site.
- Master site computes corrections, transmits via 2 GEO satellites.
- Improves accuracy to within 5 m.
- International equivalents: EGNOS (Europe), MSAS (Japan), GAGAN (India).

**LAAS (Local Area Augmentation System):**
- For CAT II/III precision approaches.
- Differential GPS with corrections transmitted on VOR band (108-118 MHz).
- Addresses ionospheric and tropospheric errors.

---

## Module 2c: Spacecraft GNC Elements

### Satellite Classification by Size

| Category | Typical Mass |
|----------|-------------|
| Large orbiter | >1000 kg (e.g., Europa Clipper) |
| Small satellite | 100-500 kg |
| Microsatellite | 10-100 kg |
| Nanosatellite / CubeSat | 1-10 kg |
| Picosatellite | <1 kg |

### GNC Components Overview

A spacecraft GNC system must determine:
- **Position**: orbital (ECI frame for Earth orbit; ICRF for deep space / beyond cislunar).
- **Attitude and spin rate**: orientation about its axes.
- **Actuators**: change attitude or adjust velocity.

### Actuators

#### Reaction Wheels
- Enable 3-axis precision pointing.
- Store torque/momentum by spinning; conservation of momentum causes counter-rotation of spacecraft.
- Common configuration: 3 orthogonal wheels + backup(s).
  - Large satellites: 3 primary + 3 backups.
  - Small/SWAP-limited satellites: 4-wheel config (1 backup, often misaligned).
- High failure rate is a known issue.
- **Saturation problem**: when a wheel reaches max spin, it can no longer absorb torque. Must be desaturated using an external actuator (thruster or magnetorquer).

#### Magnetorquers
- Provide control torque perpendicular to local magnetic field and magnetic dipole.
- Formula: T = M x B (T = torque vector, M = magnetic dipole = N*I*A, B = external magnetic field).
- Require a magnetometer to measure the local magnetic field.
- Types: air coils, torquer bars/rods.
- Typically 3 units orthogonally placed (x, y, z).
- Used as alternative to thrusters for desaturating reaction wheels.
- **Not useful for interplanetary travel** (no local external magnetic field).
- Common on CubeSats and small satellites.

#### Thrusters
- Enable both attitude and translational control.
- Expendable fuel source.
- Not typically used for SmallSats and smaller (magnetorquers preferred).
- Provide large external torque for: quick reactions, wheel desaturation, spin stabilization, proximity operations.
- Higher precision for translational and attitude controls.

**When to use each actuator:**

| Actuator | Best For | Limitations |
|----------|----------|-------------|
| Reaction Wheels | Fine 3-axis pointing, continuous attitude control | Saturation; high failure rate |
| Magnetorquers | Reaction wheel desaturation; coarse attitude control in LEO; low-cost small sats | Useless without local magnetic field (deep space); coarse only |
| Thrusters | Orbit maneuvers, quick attitude changes, desaturation, proximity ops | Expendable fuel; heavy; not for small sats |

### Sensors

#### Star Trackers
- Determine attitude by comparing positions of celestial bodies in an image against a catalog of 50-60 navigational stars.
- Components: optical assembly, imaging sensor, processing unit + software.
- Process: image capture, star identification, attitude calculation, continuous update.
- **Arcsecond-level precision** attitude determination.
- Applicable to deep space exploration, comms satellite pointing, large and small satellites.
- Often combined with gyroscopes and accelerometers in hybrid navigation.

#### Magnetometers
- Detect and measure local magnetic field.
- Provide real-time 2-axis attitude.
- With time-history data and Kalman filters: can provide attitude + rotational rates.
- Needed for magnetorquer control (must know local field).
- Challenges: interference from onboard magnetic sources (torquers, reaction wheels) -- often placed on a boom. May need on-orbit recalibration.
- Used to correct yaw drift (provides "North" reference).

#### Sun Sensors
- Determine attitude based on direction of the Sun relative to spacecraft body frame.
- 3-axis attitude requires an additional reference (e.g., nadir vector).
- Useful for fault detection and recovery.
- Error sources: glint from other spacecraft, Earth/Moon albedo (Earth albedo avg ~30%).

**Types:**
| Type | Description | Pros/Cons |
|------|-------------|-----------|
| Coarse (cosine/photocell) | Current proportional to cosine of angle to sun | Cheap, low mass; few-degree accuracy; albedo-sensitive |
| Quadrant detector | 2x2 photodiode array | Moderate accuracy; albedo-sensitive |
| Digital sun sensor | Narrow slit + coded bit mask | Higher accuracy |
| Sun camera | Camera image, finds centroid | High accuracy, albedo rejection |

- LEO coarse sun sensors: reduced accuracy up to 10 degrees due to albedo.

#### Horizon Sensors
- Types: Infrared Horizon Crossing Indicators (HCI), Thermopile sensors.
- Determine horizon and nadir vector.
- Enable attitude determination and guidance.

#### Inertial Sensors (IMU)
- **Gyroscopes**: measure angular velocity. Types:
  - Fiber Optic Gyros (FOGs): exploit Sagnac Effect; superior performance, higher SWAP.
  - Ring Laser Gyroscopes.
  - MEMS Gyros: more susceptible to radiation / single event upsets.
- **Accelerometers**: measure velocity change.
- Packaging: single instruments or Inertial Reference Unit (3 orthogonal gyros + 3 accelerometers).
- Stability characterized by: bias stability, angle random walk, dynamic range, output resolution.
- Sensor fusion needed to mitigate drift:
  - Accelerometer corrects roll/pitch drift (using "down" reference).
  - Magnetometer corrects yaw (using "North" reference).
- Angle integration: theta(t) = theta_0 + integral(omega(t) dt).

#### GPS Receivers
- Useful for Low Earth Orbit.
- Progress being made toward GEO and cislunar applications.

### Deep Space Navigation

- Requires Deep Space Network (DSN) radio transponders since GPS is not available beyond LEO/cislunar.
- **Small Deep Space Transponder (SDST)**: designed by JPL, manufactured by General Dynamics. Used with DSN.
- **IRIS V2**: deep space transponder for smaller form-factor spacecraft (CubeSats).

### LiDAR
- Time-of-flight laser sensor.
- Used for proximity operations on larger satellites.
- Also viable for smaller satellites and CubeSats.
- Additionally used for remote sensing (surface, atmosphere, oceans).

### Small Satellite Challenges
- Miniaturized INS suffers from: angular drift, EMI susceptibility, coarse navigation.
- Navigation accuracy limited by latency in communication links.
- GPS-denied environments require alternative solutions: optical stereo vision, star tracking.
- Data fusion and fast-response data links (e.g., laser comms) help mitigate issues.

---

## Module 3e: Spacecraft Avionics -- Architectures and Buses

### Core Concepts

- Spacecraft avionics = the "brain" and "nervous system": Command and Data Handling (C&DH), GNC, Payload Management.
- Key difference from aircraft avionics: spacecraft avionics must be autonomous, radiation-hardened, and thermally managed in vacuum (vs. maintainable and atmosphere-cooled for aircraft).

### Radiation Effects and Mitigation

| Effect | Description |
|--------|-------------|
| Total Ionizing Dose (TID) | Cumulative damage causing gradual degradation |
| Single Event Effects (SEE) | Instantaneous effects from particle strikes |

**Mitigation:** redundant systems (TMR), scrubbing, watchdogs, physical shielding, RAD hardening, component testing for voltage/current thresholds.

### Avionics Architectures

#### Federated (Classical)
- "One function, one box." Each subsystem (AOCS, Thermal, Power) is physically and functionally distinct.
- Topology: bus or star. Remote terminals connected to centralized processing.
- Each RT has exclusive processor, I/O, drivers. No resource sharing.

#### Integrated Modular Avionics (IMA) -- Centralized
- Functions combined on shared computing resources.
- Software partitions isolate functions on common processors.
- Data Interface Unit (DIU) or Remote Interface Unit (RIU) for sensor data, processed centrally.
- High functional density; reduces SWaP.

#### Distributed Integrated Modular Avionics (DIMA)
- Combines IMA functional integration with physical distribution.
- Computing nodes distributed near sensors/actuators on standardized software tasks, connected by high-speed backbone.
- Less cabling, high scalability.
- Real-world example: NASA Lunar Gateway.

**IMA vs. DIMA Comparison:**

| Feature | IMA | DIMA |
|---------|-----|------|
| Physical layout | Centralized | Distributed |
| Primary goal | Resource sharing (SWaP reduction) | Flexibility and scalability |
| Cable weight | Low (vs. federated) | Very low |
| Fault isolation | Logical partitioning | Physical and logical partitioning |
| Upgradeability | Moderate | High |

#### Open Architectures

**SAVOIR (ESA):**
- Open reference architecture standardizing HW/SW platforms, modules, and interfaces.
- Uses CCSDS and ECSS standards.
- Leverages MIL-STD-1553B, SpaceWire, TTE buses.
- Layered software architecture with time-space partitioning OS.
- Best for large, complex multi-collaborator missions. Enables reusability, decreases design time.

**SPA (US AFRL -- Space Plug-and-Play Avionics):**
- Modeled after USB: rapid detection and configuration.
- Self-organizing network, plug-and-play middleware.
- Dual-star topology with routers/switches.
- Unified mechanical, electrical, and thermal interfaces.
- Enables rapid assembly and hot-plugging.

**OMAC4S:**
- IMA-like approach using a commercial backplane (e.g., CPCI-E).
- Line Replaceable Units (LRUs) for fast hardware replacement/upgrade.
- TTE as network backbone.
- Initiated by Airbus and TTTech (2013).
- Real-world example: Orion spacecraft.

### Databuses

#### MIL-STD-1553B
- **Type:** Legacy command/response bus.
- **Topology:** Linear bus with Bus Controller.
- **Protocol:** Bus Controller polls Remote Terminals; RTs only respond to commands.
- **Speed:** Up to 1 Mbps, half-duplex.
- **Pros:** Deterministic, reliable, well-proven.
- **Cons:** Heavy cabling, low bandwidth.
- **Use when:** Reliability and determinism required; bandwidth needs are low; heritage/legacy systems.

#### CAN Bus (Controller Area Network)
- **Type:** Adapted from automotive.
- **Topology:** Linear with differential signaling (noise immunity).
- **Protocol:** Multi-master, event-triggered. CSMA/CD + AMP for arbitration.
- **Speed:** Up to 1 Mbps (classical), up to 5 Mbps (CAN-FD).
- **Pros:** Low SWaP, simple wiring, lighter than 1553B.
- **Cons:** High overhead limits effective throughput to ~40%.
- **Use when:** Small satellites / CubeSats; low SWaP is critical; moderate data rates sufficient.

#### SpaceWire / SpaceFibre
- **Type:** High-speed, point-to-point switched network (not a bus).
- **Topology:** Switched fabric / point-to-point, full-duplex with flow control.
- **Protocol:** "Wormhole" routing (packets forwarded before full message received).
- **Speed:** SpaceWire: 2-400 Mbps. SpaceFibre: up to 6.25 Gbps.
- SpaceFibre adds: longer cable distances, QoS, built-in FDIR.
- **Use when:** High data rates needed (remote sensing, SAR, hyperspectral imaging); payload data transport.
- **Real-world:** James Webb Space Telescope (SpaceWire).

#### Time-Triggered Ethernet (TTE / TTEthernet)
- **Type:** Mixed-criticality Ethernet network built on IEEE 802.3.
- **Traffic classes:**
  - Time-Triggered: critical control commands, guaranteed bandwidth.
  - Rate-Constrained: audio/video streams, guaranteed bandwidth.
  - Best-Effort: file transfers, no bandwidth guarantee.
- **Use when:** Mixed command/control and payload traffic on a common network; deterministic timing required alongside high throughput.
- **Real-world:** Orion spacecraft, NASA Lunar Gateway.

### Databus Comparison Summary

| Bus | Speed | Topology | Weight | Best For |
|-----|-------|----------|--------|----------|
| MIL-STD-1553B | 1 Mbps | Linear bus | Heavy | Legacy, reliable C&DH |
| CAN | 1-5 Mbps | Linear | Light | Small sats, CubeSats |
| SpaceWire | 2-400 Mbps | Switched fabric | Moderate | High-bandwidth payloads |
| SpaceFibre | Up to 6.25 Gbps | Switched fabric | Moderate | Next-gen high-bandwidth + FDIR |
| TTE | Ethernet speeds | Switched | Moderate | Mixed-criticality networks |

### Onboard Computers

| Type | Pros | Cons | Examples |
|------|------|------|----------|
| Rad-Hard | Radiation immune | Expensive, low performance | RAD750, LEON |
| COTS | High performance, cheap, low power | Radiation susceptible | ARM Cortex, Snapdragon |
| Hybrid/Heterogeneous | Fast + reliable | Complex integration | NASA SpaceCube (FPGA + rad-tolerant supervisor) |

Real-world: Ingenuity Mars Helicopter used Snapdragon (no radiation hardening) for autonomous flight.

### Software and Autonomy

- Software-Defined Systems: decoupling HW from SW; reconfigurable radios (SDR) and satellites.
- **FDIR hierarchy:** Device level (EDAC corrects bit flips) -> Subsystem level (switch to backup) -> System level (enter Safe Mode).
- Autonomy levels: from simple survival (power/thermal management) to autonomous scientific discovery (onboard data filtering).
- Examples: ESA OPS-SAT ("flying laboratory" for uploading new apps in orbit), Lockheed Martin SmartSat (smartphone-like reconfiguration).

### Trends

- Mega-constellations: batch production using automotive manufacturing techniques.
- Inter-Satellite Links (ISL): laser/RF links forming space mesh networks.
- Cloud-Edge Collaboration: satellites as edge nodes, processing data before downlinking insights.
