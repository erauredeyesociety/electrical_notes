Name: Gatlin Nelson
Student ID: 2636127

CEC 300 Exam 1

---

Multiple Choice

1. (b) Electromagnetic waves that reflect back from the ionosphere, therefore, they can reach further distances than the line-of-sight.

2. (b) The bearing of the airplane from a given point (ground station), referenced to Magnetic North.

---

Short Answer

3. DME reports slant range, forming the hypotenuse of a right triangle with altitude and horizontal distance as legs. Converting altitude: 30,000 ft / 6,076.12 ft/nmi = 4.937 nmi. By the Pythagorean theorem: b = sqrt(5^2 - 4.937^2) = sqrt(0.63) = 0.79 nmi.

4. Radio multipath occurs when electromagnetic waves reach a receiver via two or more paths, with reflected copies bouncing off ground, buildings, or terrain arriving later than the direct signal. This causes errors in distance or position measurements because receivers interpret the delayed signals as different ranges. For example, in GPS navigation, signals reflecting off nearby buildings cause the receiver to overestimate pseudorange, degrading position accuracy [1].

5. The TO/FROM indicator would show FROM. The flag depends on the aircraft's position relative to the station and the selected OBS course, not heading. After passing the station onto the 270 radial (now west of the station), following course 270 leads away from the station, so the flag flips to FROM. For the CDI, the pilot should turn right by 6 degrees. Each tick represents 2 degrees of deviation, so three ticks equals 6 degrees.

6. Standards are technical specifications from organizations like ICAO and RTCA ensuring global interoperability; they are not legally enforceable alone but become so when adopted by regulation. Regulations are legally enforceable FAA rules under 14 CFR dictating safety requirements for aircraft design and operation. Orders are internal FAA documents defining policies for FAA personnel. Technical Standard Orders (TSOs) set minimum performance standards for interchangeable parts, serving as both design and production approval. Airworthiness Directives (ADs) are legally enforceable rules correcting specific unsafe conditions — owners must comply. Advisory Circulars (ACs) are non-binding guidance describing acceptable means of regulatory compliance.

---

Essay 1: Uncrewed Automated Aircraft Navigation (GPS-Denied)

In a GPS-denied environment, the autonomous Cessna 182 relies exclusively on terrestrial NAS infrastructure for full-mission automation.

For departure and climb-to-altitude, the system prioritizes VOR and DME. VOR provides magnetic bearing from a ground station by measuring the phase difference between a reference signal and a variable signal from a rotating 30 Hz limacon antenna [1]. This allows the automation to track departure radials. DME measures slant range via pulse-pair timing at 12.36 microseconds per nautical mile, identifying distance-based turn or step-climb points. Together, VOR bearing and DME distance provide a complete rho-theta position fix [1].

For en route navigation, VOR and DME remain primary. Victor Airways are defined by VOR radials, so the system tracks a radial FROM one station, then retunes TO the next. The TO/FROM flag confirms position relative to each station based on the OBS setting, independent of heading. Continuous DME identifies intersections and waypoints along the airway [1].

For airport arrival, the system prioritizes NDB/ADF supplemented by VOR/DME. Unlike VOR, the ADF pointer always indicates direct relative bearing to the beacon regardless of heading, simplifying the automation's ability to home toward an arrival fix. The loop and sense antenna combination resolves the 180-degree ambiguity inherent in loop-only receivers. VOR/DME provides cross-fixes for terminal area awareness [1].

For final approach and landing, the system prioritizes ILS and DME. The localizer (108-112 MHz) provides horizontal alignment using differential 90/150 Hz modulation — equal signal indicates centerline. The glideslope (329-335 MHz) provides a 3-degree vertical descent path. DME identifies the final approach fix and monitors distance to threshold for triggering the flare. CAT I decision height is 200 feet [1][2].

References:
[1] CEC 300. "Module 2a - Navigation Systems," Florida Institute of Technology, 2025.
[2] CEC 300. "CEC 300 - Module 2 Homework," Florida Institute of Technology, 2025.

---

Essay 2: Spacecraft Localization and Attitude Control

LEO Minisatellite

For a LEO minisatellite (10-100 kg class, similar to NASA's TROPICS CubeSat constellation), the sensor suite must minimize size, weight, and power while providing 3-axis attitude determination and localization. I recommend MEMS inertial measurement units, magnetometers, sun sensors, and a GPS receiver. Since the satellite operates in LEO, a GPS receiver serves as the primary localization tool, providing accurate orbital position and timing data. The Deep Space Network is not needed for this mission — standard ground stations and the existing GPS constellation provide sufficient navigation and communication coverage for LEO operations. For attitude determination, magnetometers measure Earth's local magnetic field vector, providing one reference direction. Sun sensors provide a second reference vector toward the sun, and horizon sensors identify the nadir direction toward Earth's center. Together, these three external references allow the onboard processor to resolve full 3-axis attitude (roll, pitch, yaw). MEMS gyroscopes within the IMU provide angular rate data for attitude propagation between external sensor updates, but they exhibit drift over time and require periodic correction from the external references [3].

For actuation, I recommend magnetorquers supplemented by small reaction wheels. Magnetorquers generate control torque by passing current through coils that interact with Earth's magnetic field, arranged in three orthogonal axes for roll, pitch, and yaw. They are lightweight, have no moving parts, and require no expendable propellant, making them ideal for mass-constrained small satellites. Reaction wheels provide finer pointing control by exchanging angular momentum with the spacecraft body through spinning flywheels — as the wheel spins faster in one direction, the satellite rotates in the opposite direction. When reaction wheels accumulate excess stored momentum over time (saturation), magnetorquers can desaturate them by dumping that momentum into Earth's magnetic field. This approach is feasible in LEO because the geomagnetic field is strong enough to generate meaningful control torque [3].

For the databus, I recommend the Controller Area Network (CAN) bus. CAN provides up to 1 Mbit/s bandwidth with a simple linear topology and differential signaling for noise immunity, all at very low SWaP-C. This bandwidth is sufficient for the modest data requirements of a minisatellite — housekeeping telemetry, attitude sensor data, and actuator commands. Compared to legacy alternatives like MIL-STD-1553B, CAN is significantly lighter and less complex, which is critical for a mass-constrained CubeSat platform. CAN has proven space heritage on ESA's Galileo GIOVE-A satellite and China's Beijing III satellite, where adopting CAN reduced satellite mass by approximately 60% and power consumption by 20% [4][5].

Large Europa Orbiter

A science mission to Jupiter's moon Europa faces high radiation from Jupiter's intense magnetosphere, extreme distance from Earth (628-928 million km), and demanding pointing requirements for science instruments like cameras and spectrometers. I recommend star trackers, high-grade fiber-optic gyroscopes (FOGs), and Deep Space Network transponders. Star trackers are the primary attitude sensor, providing arcsecond-level absolute 3-axis attitude by capturing images of star fields and matching them against an onboard star catalog. This precision is required for pointing science instruments at specific surface features on Europa. Fiber-optic gyroscopes provide angular rate data with significantly lower drift than MEMS sensors, which is critical for maintaining accurate attitude knowledge during the multi-year interplanetary cruise and during orbital maneuvers when star trackers may be temporarily blinded by thruster plumes or planetary bodies. The Deep Space Network IS essential for this mission — at Europa's distance, GPS is completely unavailable. Interplanetary navigation relies on DSN-linked transponders such as the Small Deep Space Transponder for two-way ranging and Doppler velocity measurements to determine the spacecraft's position. The one-way communication latency to Europa is approximately 33-53 minutes, making autonomous onboard decision-making critical for time-sensitive operations [3].

For actuation, I recommend large reaction wheels in an orthogonal four-wheel configuration (three primary axes plus one skewed backup for redundancy) and an integrated thruster suite. Reaction wheels manage fine roll, pitch, and yaw control for science pointing by exchanging angular momentum with the spacecraft body. The four-wheel configuration provides single-fault tolerance — if one wheel fails, the remaining three can still control all three axes. However, there is no significant magnetic field at Europa to leverage for magnetorquer-based desaturation, so thrusters are required to periodically dump accumulated angular momentum from the reaction wheels. Thrusters also perform translational maneuvers: Jupiter orbit insertion, Europa orbit capture, orbit maintenance, and trajectory correction maneuvers during the interplanetary cruise phase. The expendable propellant adds significant mass to the spacecraft, but this tradeoff is unavoidable given the lack of an ambient magnetic field and the need for substantial delta-V capability [3].

For the databus, I recommend Time-Triggered Ethernet (TTE), developed by TTTech. A large science orbiter demands high bandwidth (up to 1 Gbps) for payload data — imaging, spectroscopy, and radar sounding — alongside spacecraft command and control. TTE supports mixed-criticality traffic on a single physical network through three traffic classes: time-triggered (deterministic, for critical flight control commands), rate-constrained (bounded latency, for telemetry), and best-effort (for bulk payload data downloads). These coexist without interference, eliminating the need for separate bus networks. TTE has direct space heritage as the backbone of NASA's Orion spacecraft and the Lunar Gateway, both part of the Artemis program. Its deterministic latency guarantees are vital for autonomous operations at Europa, where the 33-53 minute communication delay precludes any real-time ground intervention during critical events [4][5].

References:
[3] CEC 300. "Module 2c - Spacecraft GNC Elements," Florida Institute of Technology, 2025.
[4] CEC 300. "Module 3e - spacecraft-avionics," Florida Institute of Technology, 2025.
[5] C. Chen et al., "Research status and prospect of avionics system technology for spacecraft," Chinese Journal of Aeronautics, 2025.

---

Essay 3: Gold Codes and PRN Ranging in GPS

Gold Codes are the mathematical foundation for the pseudorandom number (PRN) codes transmitted by GPS satellites. A PRN code is a deterministic binary sequence that appears random but is repeatable, allowing a receiver to generate its own local replica.

Receivers determine range through autocorrelation: the receiver generates a local copy of a satellite's PRN code and slides it in time against the incoming signal. The phase shift required for alignment corresponds to the signal's time-of-flight. Since signals travel at the speed of light, this yields a pseudorange — the estimated satellite-to-receiver distance. This places the receiver on a sphere centered on the satellite's known position (from ephemeris data). Four or more pseudoranges solve for 3D position and receiver clock bias. The term "pseudorange" reflects errors from ionospheric/tropospheric delay, clock offsets, ephemeris errors, multipath, and receiver noise [6][7].

Gold Codes are generated using two 10-bit Linear Feedback Shift Registers (LFSRs) and XOR (modulo-2 addition). The C/A code produces a 1023-chip sequence repeating every millisecond at 1.023 MHz. Two polynomials drive the process: G1 (1 + x^3 + x^10) and G2 (1 + x^2 + x^3 + x^6 + x^8 + x^9 + x^10). Both registers initialize to all ones. Each clock cycle, designated bits are XORed for feedback and shifted right. G1 uses bits 3 and 10; G2 uses bits 2, 3, 6, 8, 9, and 10 [6].

Each satellite is assigned unique tap positions from G2 — for example, SV #1 uses bits 2 and 6, SV #2 uses bits 3 and 7. The final PRN chip is produced by XORing the G2 taps together, then XORing with the G1 output. This creates a unique Gold Code per satellite with excellent cross-correlation properties — near zero correlation between different codes. This enables CDMA, allowing all satellites to broadcast on the same L1 frequency (1575.42 MHz) without interference [6].

References:
[6] CEC 300. "Module 2b - Satellite Navigation (GNSS)," Florida Institute of Technology, 2025.
[7] CEC 300. "CEC 300 - Module 2 Homework," Florida Institute of Technology, 2025.
