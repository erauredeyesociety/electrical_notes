# CEC 300 Exam 1

**Name:** Nelson Gatlin
**Student ID:** ___

---

**1. [MC 2.5 pts] Skywaves are:**

**(b)** Electromagnetic waves that reflect back from the ionosphere, therefore, they can reach further distances than the line-of-sight.

**2. [MC 2.5 pts] The VOR systems measure:**

**(b)** The bearing of the airplane from a given point (ground station), referenced to Magnetic North.

---

**3. [SA 5 pts] DME Horizontal Distance**

DME reports slant range (the direct line-of-sight distance), which forms the hypotenuse of a right triangle with altitude and horizontal distance as the legs. Converting altitude: 30,000 ft / 6,076.12 ft/nmi = 4.937 nmi. Applying the Pythagorean theorem: b = sqrt(5^2 - 4.937^2) = sqrt(25 - 24.37) = sqrt(0.63) = **0.79 nmi**.

---

**4. [SA 5 pts] Radio Multipath**

Radio multipath occurs when electromagnetic waves reach a receiving antenna via two or more paths, with reflected copies bouncing off the ground, buildings, or terrain arriving slightly later than the direct signal. This is a problem for avionics because the delayed signals interfere with the direct signal, causing errors in distance or position measurements. For example, in GPS navigation, signals reflecting off nearby buildings arrive later than the line-of-sight signal, causing the receiver to overestimate the pseudorange and degrade position accuracy [1].

---

**5. [SA 5 pts] VOR Indicator**

If the pilot turns to fly heading 090 (the opposite direction) while on the 270 radial, the TO/FROM indicator would show **FROM**. The TO/FROM flag depends on the aircraft's position relative to the station and the selected OBS course, not on heading. After passing the station to the 270 radial (now west of the station), following course 270 leads away from the station, so the flag flips to FROM.

If the CDI shows three ticks to the right, the pilot should turn **right by 6 degrees**. Each tick on a standard VOR CDI represents 2 degrees of deviation, so three ticks equals 6 degrees.

---

**6. [SA 5 pts] Standards, Regulations, Orders, TSO, AD, AC**

**Standards** are technical specifications developed by organizations like ICAO, RTCA, and SAE to ensure global interoperability. They are not legally enforceable on their own but become so when adopted by regulation. **Regulations** are legally enforceable rules under Title 14 CFR, established by the FAA, dictating safety requirements for aircraft design, manufacture, and operation. **Orders** are internal FAA documents defining policies and procedures for FAA personnel, guiding how the agency enforces regulations. **Technical Standard Orders (TSOs)** are minimum performance standards for specific interchangeable parts and appliances; a TSO authorization serves as both design and production approval. **Airworthiness Directives (ADs)** are legally enforceable rules correcting a specific unsafe condition in an aircraft, engine, or appliance — owners must comply or the aircraft is unairworthy. **Advisory Circulars (ACs)** are non-binding FAA guidance documents describing acceptable means of compliance with existing regulations. Together, these form a layered safety framework ensuring components meet standards, operations follow regulations, and known defects are corrected [2][3].

---

**Essay 1 [25 pts]: Uncrewed Automated Aircraft Navigation (GPS-Denied)**

In a GPS-denied environment, the autonomous Cessna 182 must rely exclusively on terrestrial NAS infrastructure to achieve full-mission automation. The following proposal identifies which NAVAIDs the autonomous logic will prioritize for each flight phase.

For **departure and climb-to-altitude**, the system prioritizes VOR and DME. VOR provides the magnetic bearing from a ground station by measuring the phase difference between a constant reference signal and a variable signal produced by a rotating 30 Hz limacon antenna pattern. This allows the automation to track the assigned departure radial. DME complements VOR by measuring slant range through pulse-pair timing at 12.36 microseconds per nautical mile, enabling the system to identify distance-based step-climb or turn points required by the departure procedure. Together, VOR bearing and DME distance provide a complete rho-theta position fix [4].

For **en route route-following**, VOR and DME remain the primary NAVAIDs. Victor Airways are defined by VOR radials, so the system tracks a radial FROM a departing station, then retunes to track a radial TO the next station. The TO/FROM flag confirms position relative to each station based on the selected OBS course and aircraft position, independent of heading. Continuous DME data identifies intersections and waypoints along the airway without GPS [4].

For **airport arrival and the terminal area**, the system prioritizes NDB/ADF supplemented by VOR/DME. Unlike VOR, which requires selecting a specific course, the ADF pointer always indicates the direct relative bearing to the NDB station regardless of aircraft heading. This makes NDB well-suited for the autonomous system to home directly toward an arrival fix or the airfield. The loop and sense antenna combination in the ADF resolves the 180-degree bearing ambiguity inherent in loop-only receivers. VOR/DME provides supplementary cross-fixes for terminal area position awareness [4].

For **final approach and landing**, the system prioritizes the Instrument Landing System (ILS) and DME. The localizer operates at 108-112 MHz and provides precise horizontal alignment with the runway centerline using differential modulation of 90 Hz and 150 Hz tones — equal signal strength indicates centerline. The glideslope operates at 329-335 MHz and provides a vertical descent path at approximately 3 degrees. Together, these give the automation the lateral and vertical guidance needed for a stabilized approach. DME identifies the final approach fix and monitors distance to threshold, enabling the system to trigger the landing flare at the correct point. For a CAT I approach, decision height is 200 feet [4][5].

**References:**
[4] CEC 300. "Module 2a - Navigation Systems"
[5] CEC 300. "CEC 300 - Module 2 Homework"

---

**Essay 2 [25 pts]: Spacecraft Localization and Attitude Control**

**LEO Minisatellite**

For a LEO minisatellite in the 10-100 kg class (similar to NASA's TROPICS CubeSat constellation), the sensor suite must minimize size, weight, and power (SWaP) while providing 3-axis attitude determination and localization. I recommend MEMS inertial measurement units, magnetometers, sun sensors, and a GPS receiver. Since the satellite operates in LEO, a GPS receiver serves as the primary localization tool, providing accurate position and timing. The Deep Space Network is not needed — standard ground stations and the GPS constellation provide sufficient coverage. For attitude determination, magnetometers measure the Earth's local magnetic field vector, sun sensors provide a vector toward the sun, and horizon sensors identify the nadir direction. Together these external references resolve 3-axis attitude (roll, pitch, yaw). MEMS gyroscopes provide angular rate data between external updates but exhibit drift requiring periodic correction [6].

For actuation, I recommend magnetorquers supplemented by small reaction wheels. Magnetorquers generate control torque by interacting with Earth's magnetic field through current-carrying coils arranged in three orthogonal axes. They are lightweight, have no moving parts, and require no expendable propellant, making them ideal for small satellites. Reaction wheels provide finer pointing control by exchanging angular momentum with the spacecraft body through spinning flywheels. When reaction wheels accumulate excess momentum (saturation), magnetorquers can desaturate them by dumping momentum into the Earth's magnetic field — this works in LEO because the field is strong enough to generate meaningful torque [6].

For the databus, I recommend the Controller Area Network (CAN) bus. CAN provides up to 1 Mbit/s bandwidth with a simple linear topology and differential signaling for noise immunity, all at very low SWaP-C (Size, Weight, Power, and Cost). This is sufficient for the modest data requirements of a minisatellite — housekeeping telemetry, sensor data, and actuator commands. Compared to legacy alternatives like MIL-STD-1553B, CAN is significantly lighter and less complex, which is critical for a mass-constrained CubeSat platform. CAN also supports up to 128 nodes and uses a priority-based arbitration scheme that ensures higher-priority messages (such as fault alerts) are transmitted first. CAN has proven space heritage on ESA's Galileo GIOVE-A and China's Beijing III satellite, where adopting CAN reduced satellite mass by approximately 60% and power consumption by 20% compared to traditional bus architectures [7][8].

**Large Europa Orbiter**

A science mission to Jupiter's moon Europa faces high radiation from Jupiter's magnetosphere, extreme distance from Earth (628-928 million km), and demanding pointing requirements for science instruments. I recommend star trackers, high-grade fiber-optic gyroscopes (FOGs), and Deep Space Network transponders. Star trackers are the primary attitude sensor, providing arcsecond-level precision by matching captured star field images against an onboard catalog. FOGs provide angular rate data with significantly lower drift than MEMS, which is critical during multi-year interplanetary transit. The Deep Space Network IS essential for this mission — at Europa's distance, GPS is unavailable. Navigation relies on DSN-linked transponders (such as the Small Deep Space Transponder) for two-way ranging and Doppler tracking to calculate position. Communication latency is approximately 33-53 minutes one-way, making autonomous onboard operations critical [6].

For actuation, I recommend large reaction wheels in an orthogonal four-wheel configuration (three primary plus one skewed backup for redundancy) and an integrated thruster suite. Reaction wheels manage fine pointing for science observations. However, there is no significant magnetic field at Europa to leverage for magnetorquer-based desaturation, so thrusters are required to dump accumulated angular momentum from the reaction wheels. Thrusters also perform orbital insertion, orbit maintenance, and trajectory correction maneuvers during cruise. The expendable propellant adds significant mass, but this is unavoidable given the operating environment [6].

For the databus, I recommend Time-Triggered Ethernet (TTE), developed by TTTech. A large orbiter demands high bandwidth (up to 1 Gbps) for scientific payload data — imaging, spectroscopy, and radar sounding — plus spacecraft command and control. TTE is superior to legacy buses like 1553B (limited to 1 Mbit/s) and CAN because it supports mixed-criticality traffic on a single physical network. It defines three traffic classes: time-triggered (deterministic, for critical flight control), rate-constrained (bounded latency, for telemetry), and best-effort (for bulk payload data). These coexist without interference, eliminating the need for separate networks. TTE has direct space heritage as the backbone network for NASA's Orion spacecraft and the Lunar Gateway, both part of the Artemis program. Its deterministic latency is vital for autonomous operations at Europa, where the 33-53 minute one-way communication delay to Earth precludes any real-time ground intervention [7][8].

**References:**
[6] CEC 300. "Module 2c - Spacecraft GNC Elements," Florida Institute of Technology, 2025.
[7] CEC 300. "Module 3e - spacecraft-avionics," Florida Institute of Technology, 2025.
[8] C. Chen, Y. Yin, K. Huang, and X. He, "Research status and prospect of avionics system technology for spacecraft," *Chinese Journal of Aeronautics*, 2025.

---

**Essay 3 [25 pts]: Gold Codes and PRN Ranging in GPS**

Within the Global Positioning System, Gold Codes serve as the mathematical foundation for the pseudorandom number (PRN) codes transmitted by each satellite. These codes are essential for identifying specific satellites and for calculating the precise distance between a satellite-based transmitter and a ground receiver.

A PRN code is a deterministic sequence of binary chips that appears random but is repeatable. Because the sequence is known, a GPS receiver can generate its own local replica of any satellite's PRN code. The receiver determines range through autocorrelation — it generates an internal copy of a specific satellite's code and slides it in time against the incoming signal until the two align. The time delay (phase shift) required for alignment corresponds to the signal's time-of-flight from the satellite. Since radio signals travel at the speed of light, this time-of-flight yields a pseudorange — the estimated distance between satellite and receiver. This places the receiver on the surface of an imaginary sphere centered on the satellite's known orbital position, provided via the navigation message's ephemeris data. With pseudorange measurements from four or more satellites, the receiver solves for its three-dimensional position and clock bias (the offset between the receiver's inexpensive oscillator and the satellites' atomic clocks). The measurement is called a "pseudorange" rather than true range because it contains errors from ionospheric delay, tropospheric delay, satellite clock and ephemeris errors, multipath, and receiver noise [9][10].

Gold Codes are generated using a pair of 10-bit Linear Feedback Shift Registers (LFSRs) and modulo-2 addition (XOR gates). The C/A code uses this structure to produce a sequence exactly 1023 chips long, repeating every millisecond at a chipping rate of 1.023 MHz. Two generating polynomials drive the process. The Stage 1 (G1) polynomial is 1 + x^3 + x^10, and the Stage 2 (G2) polynomial is 1 + x^2 + x^3 + x^6 + x^8 + x^9 + x^10. Both registers are initialized to an all-ones state. At each clock cycle, the designated bits are XORed to produce a feedback value that shifts into position 1 as all bits shift right. For G1, bits 3 and 10 are XORed for feedback; for G2, bits 2, 3, 6, 8, 9, and 10 are combined [9].

The critical feature is that each GPS satellite is assigned a unique pair of tap positions from the G2 register. For example, SV #1 uses taps at bits 2 and 6, SV #2 uses bits 3 and 7, and SV #3 uses bits 4 and 8. To produce the final PRN code, the two G2 tap outputs are XORed together, and that result is XORed with the G1 output (bit 10). This creates a unique 1023-chip Gold Code for each satellite with excellent cross-correlation properties — when two different satellites' codes are correlated, the result is near zero. This property enables Code Division Multiple Access (CDMA), allowing all GPS satellites to broadcast simultaneously on the same L1 frequency (1575.42 MHz) without mutual interference, because the receiver can isolate each satellite's signal through correlation with its unique PRN code [9].

**References:**
[9] CEC 300. "Module 2b - Satellite Navigation (GNSS)," Florida Institute of Technology, 2025.
[10] CEC 300. "CEC 300 - Module 2 Homework," Florida Institute of Technology, 2025.
