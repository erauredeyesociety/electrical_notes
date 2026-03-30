# CEC 300 Exam 1 Solutions

**Total: 100 points**

---

## Part I: Multiple Choice (5 pts)

### 1. Answer: **(b)** — Electromagnetic waves that reflect back from the ionosphere

The **Gibbs** — sorry, **Skywaves** are electromagnetic waves that reflect back from the ionosphere, therefore, they can reach further distances than the line-of-sight. This is distinct from ground waves (which follow the earth's curvature, used by NDB) and space waves (which pass through the ionosphere). Option (a) is wrong because skywaves reflect, not travel within the ionosphere. Option (c) is wrong because they don't pass through to space. Option (d) is wrong because they reflect from the ionosphere, not clouds.

> *Ref: Module 2a - Navigation Systems, RF propagation fundamentals.*

### 2. Answer: **(b)** — The bearing of the airplane from a given point (ground station), referenced to Magnetic North

VOR transmits two signals: a reference signal (constant phase) and a variable signal (phase varies with bearing, produced by a rotating 30 Hz limacon antenna pattern). The **phase difference** between these two signals equals the magnetic bearing of the aircraft from the station. VOR is referenced to **Magnetic North**, not True North (geodetic north), which eliminates option (a). Option (d) describes DME, not VOR. Option (c) is unrelated to VOR functionality.

> *Ref: Module 2a - Navigation Systems.*

---

## Part II: Short Answer (20 pts)

### 3. DME Horizontal Distance Calculation (5 pts)

**Given:** Aircraft at 30,000 ft altitude, DME reports 5 nmi. (1 nmi = 6076.12 ft)

**Step 1 — Convert altitude to nautical miles:**

    30,000 ft / 6,076.12 ft/nmi = 4.937 nmi

**Step 2 — Recognize DME reports slant range:**
DME measures the direct line-of-sight distance (slant range), which forms the hypotenuse of a right triangle where altitude and horizontal distance are the other two sides.

**Step 3 — Apply Pythagorean theorem:**

    a^2 + b^2 = c^2
    (4.937)^2 + b^2 = (5)^2
    24.37 + b^2 = 25
    b^2 = 0.63
    b = sqrt(0.63) = 0.794

**Answer:** The aircraft is approximately **0.79 nmi** horizontally from the DME station.

> *Ref: Module 2a - Navigation Systems. DME slant range vs. horizontal distance, radar mile = 12.36 us/nmi.*

### 4. Radio Multipath (5 pts)

**Definition:** Radio multipath occurs when electromagnetic waves reach a receiving antenna via two or more paths, often reflecting off the ground, terrain, buildings, or moving vehicles.

**Why it is a problem:** Reflected signals arrive slightly later than the direct signal, causing interference or "garble" that leads to errors in measuring distance or position. Receivers that rely on precise timing (like GPS or DME) interpret the delayed reflected signal as a different range, producing calculation errors.

**Example:** In GPS navigation, multipath interference from nearby buildings or terrain is a significant source of error for the receiver. The GPS error budget lists multipath as contributing approximately 0.6 meters of ranging error. Signals reflecting off tall structures arrive later than the direct line-of-sight signal, causing the receiver to overestimate the pseudorange to that satellite.

> *Ref: Module 2b - Satellite Navigation (GNSS), "Sources of GPS Errors" table. Module 6b - sensing.*

### 5. VOR Indicator — TO/FROM and CDI (5 pts)

**Setup:** Aircraft heading 270 degrees, on VOR radial 270, TO flag displayed, CDI centered.

**Part 1 — If the pilot turns to heading 090 while returning to the 270 radial, what does the TO/FROM indicator show?**

**Answer: FROM.** The TO/FROM flag depends on the aircraft's **position** relative to the station and the selected OBS course — **not** on the aircraft's heading. After the aircraft passes the station and is now on the 270 radial (west of the station), the OBS is still set to 270. Since following course 270 from this position leads **away** from the station, the flag flips to FROM.

**Part 2 — CDI is three ticks to the right. What direction should the pilot turn, and by how many degrees?**

**Answer: Turn right by 6 degrees.** Each tick (dot) on a standard VOR CDI represents **2 degrees** of angular deviation from the selected course. Three ticks to the right = 3 x 2 = **6 degrees**. The pilot should turn right to intercept the desired radial.

> *Ref: Module 2a - Navigation Systems. TO/FROM flag logic; CDI sensitivity = 2 degrees per dot.*

### 6. Differentiate: Standards, Regulations, Orders, TSO, AD, AC (5 pts)

**Standards:** Technical characteristics used by designers and manufacturers to ensure global interoperability, coordinated by organizations like ICAO, RTCA, and SAE. Standards are not legally enforceable by themselves but become so when adopted into regulation. Example: RTCA DO-178C for software assurance.

**Regulations:** Legally enforceable rules established by the FAA under Title 14 of the Code of Federal Regulations (14 CFR), dictating safety requirements for aircraft design, manufacture, and operation. Example: 14 CFR Part 91 (general operating rules), Part 25 (transport aircraft airworthiness).

**Orders:** Internal FAA documents that define policies and procedures for FAA personnel, providing compliance guidance and defining how the agency enforces regulations. Example: FAA Order 8900.1.

**Technical Standard Orders (TSO):** Minimum performance standards for specific interchangeable parts (like altimeters or TAWS); TSO authorization constitutes both **design and production approval**. TSO'd parts are interchangeable across aircraft that require that article.

**Airworthiness Directives (AD):** Legally enforceable rules issued to correct a specific **unsafe condition** in an aircraft, engine, or appliance. Aircraft owners are **legally required** to comply — non-compliance makes the aircraft unairworthy.

**Advisory Circulars (AC):** Non-binding FAA guidance documents that provide recommendations and **acceptable means of compliance** with existing regulations. Following an AC is one way (but not the only way) to demonstrate regulatory compliance.

**Role in Safety:** Together, these form a layered framework — standards define technical benchmarks, regulations make requirements mandatory, orders ensure consistent enforcement, TSOs guarantee minimum part performance, ADs force correction of known hazards, and ACs guide compliance.

> *Ref: Module 1b - Regulations (TSO, AD, AC definitions). Module 1d - Regulations (FAA hierarchy, CFR structure).*

---

## Part III: Essays (75 pts)

---

### Essay 1 (25 pts): Uncrewed Automated Aircraft Navigation — GPS-Denied Environment

#### Given

Design the navigational suite for an autonomous Cessna 182 in a GPS-denied environment. The system relies exclusively on terrestrial NAS infrastructure: NDB/ADF, VOR, DME, and ILS. Identify which NAVAIDs to prioritize for each flight phase with justification.

#### 1. Departure & Climb-to-Altitude

**Prioritized NAVAIDs: VOR and DME**

This phase focuses on transitioning from the terminal area to the airway. **VOR (VHF Omnidirectional Range)** provides the autonomous system with a magnetic bearing from a ground station by measuring the phase difference between a reference signal and a variable signal (rotating limacon pattern at 30 Hz). This allows the logic to track a specific **radial** leading to the departure airway. The system sets the OBS to the assigned departure radial and monitors the CDI (2 degrees per dot) to maintain course.

**DME (Distance Measurement Equipment)** is essential for determining position along the radial. DME measures **slant range** by timing the round trip of paired pulses (at 12.36 microseconds per nautical mile). This allows the autonomous logic to identify precise distance markers for step-climbs, turns, or altitude level-offs required by the Standard Instrument Departure (SID) procedure. Together, VOR bearing + DME distance = complete 2D position fix (rho-theta navigation).

#### 2. En Route (Route Following)

**Prioritized NAVAIDs: VOR and DME**

En route navigation relies on long-distance station-to-station tracking. Victor Airways are defined by VOR radials. The autonomous system tracks a radial **FROM** a departing VOR station, then retunes to track a radial **TO** the next station. The TO/FROM indicator confirms position relative to each station — it depends on position and OBS setting, not heading. Continuous **DME** data identifies intersections and waypoints along the airway. A VOR/DME fix from one station combined with a cross-bearing from another provides redundant 2D position.

#### 3. Airport Arrival / Terminal Area

**Prioritized NAVAIDs: NDB/ADF (supplemented by VOR/DME)**

During the transition from high-altitude airways to the approach environment, the **NDB (Non-Directional Beacon)** is prioritized. Unlike VOR (which requires selecting a specific course via OBS), the **ADF pointer** always indicates the direct relative bearing to the NDB station regardless of aircraft heading. This simplicity makes it well-suited for the autonomous system to home directly toward an arrival fix or airfield without pre-selecting a radial. NDB operates on ground waves in the LF/MF band (190-530 kHz in the US), providing coverage not strictly limited to line-of-sight. The loop and sense antenna combination resolves the 180-degree ambiguity inherent in loop-only receivers. VOR/DME provides supplementary cross-fixes for terminal area position awareness.

#### 4. Final Approach & Landing

**Prioritized NAVAIDs: ILS (Localizer and Glideslope) and DME**

This phase requires high-precision vertical and lateral guidance. The **Instrument Landing System (ILS)** provides both:

- **Localizer (LOC):** Operates at 108-112 MHz, provides horizontal alignment with the runway centerline using differential modulation of 90 Hz (left) and 150 Hz (right) tones. Equal signal = centerline. Full-scale beam width approx. +/-2.5 degrees.
- **Glideslope (GS):** Operates at 329-335 MHz, provides vertical descent path at approximately 3 degrees (+/-0.7 degrees full scale).

**DME** identifies the Final Approach Fix (FAF) and monitors distance to threshold for triggering the landing flare. For a CAT I approach, decision height is 200 feet with 2400 ft RVR minimum.

#### Resources Used

- CEC 300. "Module 2a - Navigation Systems," Florida Institute of Technology, 2025.
- CEC 300. "CEC 300 - Module 2 Homework," Florida Institute of Technology, 2025.
- CEC 300. "Module 6a - DAA Overview," Florida Institute of Technology, 2025.

---

### Essay 2 (25 pts): Spacecraft Localization and Attitude Control

#### Given

Design localization and attitude control systems for two spacecraft: a LEO minisatellite (CubeSat-class) and a large Europa orbiter. Address sensor selection, actuator selection, and databus recommendation for each. Minimum 350 words per spacecraft.

---

#### Spacecraft 1: LEO Minisatellite (CubeSat Style)

**Sensor Selection:**

For a LEO minisatellite (typically 10-100 kg, similar to NASA's TROPICS CubeSat constellation), the sensor suite must minimize Size, Weight, and Power (SWaP) while providing 3-axis attitude determination and localization.

I recommend **MEMS IMUs**, **Magnetometers**, **Sun Sensors**, and a **GPS receiver**.

- **Localization:** A **GPS receiver** is the primary position determination tool in LEO, providing accurate coordinates and timing. The **Deep Space Network (DSN) is NOT needed** — standard ground stations and GPS provide sufficient coverage.
- **Attitude (Roll, Pitch, Yaw):** **Magnetometers** measure the Earth's local magnetic field vector (one reference direction). **Sun Sensors** provide a vector toward the sun. **Horizon Sensors** identify the nadir vector. Together, these resolve full 3-axis attitude. **MEMS gyroscopes** provide angular rate data but exhibit drift, requiring periodic correction from the external references.
- **SWaP justification:** MEMS IMUs and magnetometers are low-mass, low-power. Star trackers would be oversized for modest pointing requirements.

**Actuator Selection:**

I recommend **Magnetorquers** supplemented by small **Reaction Wheels**.

- **Magnetorquers** create control torque via current-carrying coils interacting with Earth's magnetic field. Three-axis orthogonal configuration provides roll, pitch, and yaw control. Lightweight, no moving parts, no propellant.
- **Reaction Wheels** provide finer pointing via angular momentum exchange with the spacecraft body (conservation of angular momentum). When wheels accumulate excess momentum (saturation), **magnetorquers desaturate them** by dumping momentum into the Earth's magnetic field — feasible in LEO where the field is strong enough.
- **SWaP justification:** Avoids mass and complexity of a thruster system. Miniature reaction wheels are commercially available for CubeSat platforms.

**Databus: CAN (Controller Area Network)**

CAN provides up to 1 Mbit/s bandwidth with simple linear topology and differential signaling for noise immunity, all at very low SWaP-C. This is sufficient for a minisatellite's modest data requirements (housekeeping, sensor data, actuator commands). Compared to MIL-STD-1553B, CAN is significantly lighter and less complex. CAN supports up to 128 nodes with priority-based arbitration. Space heritage: ESA's Galileo GIOVE-A and China's Beijing III (where CAN reduced mass by ~60% and power by ~20%).

---

#### Spacecraft 2: Large Europa Orbiter (Deep Space)

**Sensor Selection:**

A Europa orbiter faces high radiation (Jupiter's magnetosphere), extreme distance (628-928 million km from Earth), and demanding science pointing requirements. I recommend **Star Trackers**, **Fiber-Optic Gyroscopes (FOGs)**, and **Deep Space Transponders**.

- **Attitude (Roll, Pitch, Yaw):** **Star Trackers** provide arcsecond-level absolute 3-axis attitude by matching star field images against an onboard catalog. Required for precision science instrument pointing. **FOGs** provide superior angular rate data with lower drift than MEMS — critical during multi-year transit and orbital maneuvers when star trackers may be temporarily blinded.
- **Localization & DSN:** The **Deep Space Network (DSN) IS essential**. GPS is unavailable at Europa. Navigation relies on DSN-linked transponders (Small Deep Space Transponder) for two-way ranging and Doppler tracking, calculating position relative to the ICRF. Communication latency: ~33-53 minutes one-way, making autonomous operations critical.
- **SWaP justification:** Star trackers and FOGs consume more mass/power than MEMS suites, but they are necessary for the accuracy and drift performance required by a flagship orbiter.

**Actuator Selection:**

I recommend **Large Reaction Wheels** (four-wheel orthogonal configuration: three primary + one skewed backup) and an **integrated Thruster (RCS) suite**.

- **Reaction Wheels** manage fine roll, pitch, and yaw control for science pointing. Four-wheel config provides redundancy.
- **Thrusters** are required because there is **no significant magnetic field** at Europa — magnetorquers are useless here. Thrusters perform momentum dumping (desaturation of reaction wheels), orbital insertion, orbit maintenance, and trajectory corrections during cruise. Expendable propellant adds mass, but this is unavoidable.

**Databus: TTE (Time-Triggered Ethernet)**

A large orbiter demands high bandwidth (up to 1 Gbps) for science payload data (imaging, spectroscopy, radar sounding) plus command/control. TTE supports **mixed-criticality traffic** on a single network: time-triggered (deterministic, for flight control), rate-constrained (bounded latency, for telemetry), and best-effort (for bulk payload data). These coexist without interference. TTE is the backbone of NASA's **Orion spacecraft** and the **Lunar Gateway** (Artemis program). Deterministic latency is vital where 33-53 min communication lag precludes real-time ground control.

#### Resources Used

- CEC 300. "Module 2c - Spacecraft GNC Elements," Florida Institute of Technology, 2025.
- CEC 300. "Module 3e - spacecraft-avionics," Florida Institute of Technology, 2025.
- C. Chen, Y. Yin, K. Huang, and X. He, "Research status and prospect of avionics system technology for spacecraft," *Chinese Journal of Aeronautics*, 2025.
- CEC 300. "Stansbury ADS-B for RLV," Space Congress 2018. (Deep space latency context.)

---

### Essay 3 (25 pts): Gold Codes and PRN Ranging in GPS

#### Given

Explain Gold Codes in GPS. Describe the purpose of PRNs for determining range. Describe the algorithm behind Gold Code generation, including LFSRs and generating polynomials.

#### The Purpose of PRNs for Ranging

Within the Global Positioning System (GPS), **Gold Codes** serve as the mathematical foundation for the **Pseudorandom Number (PRN)** codes transmitted by each satellite. A PRN code is a sequence of binary chips that appears random but is actually a deterministic, repeatable signal generated by a known algorithm. This is critical — because the code is deterministic, a GPS receiver can generate its own local replica of any satellite's PRN code.

GPS receivers determine position through **autocorrelation**. The receiver generates an internal copy of a specific satellite's PRN code and compares it to the incoming signal. By sliding the local replica in time and measuring the **phase shift** (time delay) required to align the two sequences, the receiver estimates the **time-of-flight** of the signal from satellite to receiver.

Because radio signals travel at the speed of light (~3 x 10^8 m/s), this time-of-flight yields a **pseudorange** — the estimated distance between satellite and receiver. This places the receiver on the surface of an imaginary sphere centered on the satellite's known orbital position (provided via ephemeris data in the navigation message). With measurements from **four or more satellites**, the receiver solves for four unknowns: three-dimensional position (x, y, z) and clock bias (offset between the receiver's oscillator and the satellites' atomic clocks).

The term "pseudorange" reflects that the measurement contains errors from the receiver clock bias, ionospheric delay, tropospheric delay, satellite clock/ephemeris errors, multipath, and receiver noise.

#### The Algorithm: LFSRs and Polynomials

Gold Codes are generated using a pair of **Linear Feedback Shift Registers (LFSRs)** and **modulo-2 addition** (XOR gates). The C/A code uses two 10-bit shift registers to produce a sequence exactly **1023 chips** long, repeating every millisecond at a chipping rate of 1.023 MHz.

Two generating polynomials drive the process:

1. **Polynomial G1:** 1 + x^3 + x^10
2. **Polynomial G2:** 1 + x^2 + x^3 + x^6 + x^8 + x^9 + x^10

**Stage 1 (G1):** The register is initialized to all ones. At each clock cycle, bits 3 and 10 are XORed together, and the feedback result shifts into position 1 as all bits shift right. The output (bit 10) feeds the final combination stage.

**Stage 2 (G2):** Operates with the more complex polynomial — bits 2, 3, 6, 8, 9, and 10 are XORed for feedback. Also initialized to all ones. The key difference is that each GPS satellite is assigned a **unique pair of "taps"** — specific bit positions from the G2 register whose outputs are XORed together. For example:

- SV #1 uses taps at bits 2 and 6
- SV #2 uses taps at bits 3 and 7
- SV #3 uses taps at bits 4 and 8

#### Final Code Generation

The output from G1 (bit 10) is XORed with the satellite-specific G2 tap output. This combination produces a unique 1023-chip Gold Code for each satellite with excellent **cross-correlation properties** — when two different satellites' codes are correlated, the result is near zero. This enables **Code Division Multiple Access (CDMA)**, allowing all GPS satellites to broadcast simultaneously on the same L1 frequency (1575.42 MHz) without mutual interference. Each satellite's unique PRN code acts as an identifying signature that the receiver isolates through correlation.

#### Resources Used

- CEC 300. "Module 2b - Satellite Navigation (GNSS)," Florida Institute of Technology, 2025.
- CEC 300. "CEC 300 - Module 2 Homework," Florida Institute of Technology, 2025.
