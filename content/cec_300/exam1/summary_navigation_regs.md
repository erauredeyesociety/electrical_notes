# CEC 300 Exam 1 -- Navigation Systems, Regulations, and DAA Summary

## 1. RF Fundamentals

- **Wavelength formula:** Wavelength = Speed of light / Frequency (c / f)
  - Example: 300 kHz -> wavelength = 3e8 / 3e5 = 1000 m
- **Antenna sizing:**
  - Optimal dipole antenna length is approximately half-wavelength (lambda/2)
  - Optimal loop antenna perimeter is approximately one wavelength (lambda)
  - With a ground plane, a quarter-wavelength (lambda/4) antenna can be used
  - Capacitive "hats" can make an antenna electrically longer when physical length is impractical
- **Polarization:** Antennas work best when designed for the signal's wavelength and correct polarization. NDB uses vertical polarization.

---

## 2. Non-Directional Beacon (NDB)

- **Definition:** A ground-based radio transmitter that emits a non-directional signal for aircraft direction-finding.
- **Propagation:** Uses **ground waves** that follow the curvature of the earth.
- **Frequency range:**
  - ICAO allows 190 kHz -- 1750 kHz
  - US NDBs operate 190 kHz -- 435 kHz and 510 kHz -- 530 kHz
  - 500 kHz was formerly a distress frequency (now unused)
  - 540 -- 1610 kHz is commercial AM radio in many countries
- **Band:** LF/MF (Low Frequency / Medium Frequency)
- **Identification:** Morse code
- **Receiver:** Automatic Direction Finder (ADF) with loop + sense antenna
  - Loop antenna alone has 180-degree ambiguity
  - Adding a sense antenna resolves ambiguity -- receive power goes to zero when pointed away from beacon; beacon is at that angle + 180 degrees
- **Errors/Interference:**
  - **Shore effect** -- signal bending at coastlines
  - **Precipitation static** -- static buildup on aircraft in precipitation
  - **Skywave** -- at night, signals can refract off the ionosphere causing erroneous bearings (implied from NDB ground-wave operation context)
- **Indicator:** Radio Magnetic Indicator (RMI) -- dual pointer display showing bearing to NDB stations

---

## 3. VOR -- VHF Omnidirectional Range

- **Principle:** Two signals are transmitted:
  1. A **reference signal** whose phase is constant regardless of bearing
  2. A **variable signal** whose phase varies with bearing from the station
- The **phase difference** between reference and variable signals equals the VOR bearing (radial).
- **Variable signal:** Produced by a limacon-pattern antenna rotating clockwise at **30 Hz**.
- **Lighthouse analogy:** A synchronized flash (reference) plus a rotating beam (variable). The time between seeing the sync flash and the rotating beam indicates your bearing.
- **Radials vs. Bearings:**
  - VOR indicates which **radial** the aircraft is on relative to the station
  - Radials are defined as emanating FROM the station
- **TO/FROM flag:**
  - If the selected radial leads **toward** the station -> **TO** flag
  - If the selected radial leads **away** from the station -> **FROM** flag
  - **Heading of the aircraft is irrelevant** to TO/FROM indication
  - If you are on a TO radial but flying away from the station, it still reads TO, but the pilot must reverse CDI interpretation
- **CDI (Course Deviation Indicator):**
  - Standard sensitivity: **2 degrees per dot** (tick)
  - Full-scale deflection at the maximum deviation from the selected course
- **Airways:** Victor airways (V-routes) are based on VOR radials

---

## 4. Distance Measuring Equipment (DME)

- **Principle:** Aircraft interrogates a ground transponder; distance is calculated from round-trip time.
- **Frequencies:**
  - Airborne transmit: 1025 MHz -- 1150 MHz
  - Ground reply offset: 63 MHz above or below the airborne frequency
- **Pulse pair spacing by channel:**

  | Channel | Ground Reply Spacing | Air Interrogation Spacing |
  |---------|---------------------|--------------------------|
  | X       | 12 us               | 12 us                    |
  | Y       | 30 us               | 36 us                    |
  | W       | 24 us               | 24 us                    |
  | Z       | 15 us               | 21 us                    |

- **Radar mile:** Time for signal to travel 1 NM and return = 2 x 1852 m / 3e8 m/s = **12.3 microseconds**
- **DME distance formula (X channel):**
  - Ground station adds a fixed delay of **50 microseconds** before replying
  - **Distance (NM) = (round-trip time - 50 us) / 12.3 us**
- **Maximum range:** 200 NM per FARs; line-of-sight can extend to 300 NM
- **Slant range:** DME measures slant range (hypotenuse), not ground range
  - **Slant range^2 = ground range^2 + altitude^2**
  - Error is greatest when close to the station at high altitude

### DME Interference Terms

- **FRUIT (Friendly Replies Unsynchronized in Time):**
  - Replies from the ground station meant for OTHER aircraft that your receiver picks up
  - Removed by a **deFRUITer** circuit
- **GARBLE:**
  - Interference that scrambles signals and prevents correct output
  - Occurs when pulse pairs from different aircraft overlap and create invalid pulse spacing
  - If two aircraft's pulses garble, they retransmit -- could garble again indefinitely
  - Solved by **random interrogation timing** (average rate: 15 pulse pairs/second)
- **SQUITTER:**
  - Responses to no one; DME guarantees **2700 pulse pairs/second** output
  - Some squitter pulses carry Morse code identifier; some support TACAN
- **Capacity:** 2700 total pps, ~2000 available for aircraft; at 15 pps per aircraft, DME supports approximately **133 aircraft**

---

## 5. Instrument Landing System (ILS)

### Localizer (LOC)
- Provides **horizontal alignment** with the runway centerline
- Transmitter located at the **far end** of the runway
- Frequency: **108 -- 112 MHz** (VHF), 20 channels
- Range: **40 km**
- Maximum deviation: **+/- 2 degrees** (4 degrees total)
- Uses two modulation frequencies:
  - **90 Hz** modulation -- points to the **left** side of the runway
  - **150 Hz** modulation -- points to the **right** side of the runway
- Two signal types combined:
  - **CSB (Carrier with Side Band)** -- carries the carrier reference
  - **SBO (Side Bands Only)** -- provides directional information
- The difference in depth of modulation (DDM) between 90 Hz and 150 Hz indicates offset from centerline

### Glideslope (GS)
- Provides **vertical angle** information for a fixed descent rate
- One glideslope transmitter per runway
- Frequency: **329 -- 335 MHz** (UHF), 20 channels
- Vertical range: **1 km**
- Typical inclination: **3 degrees**
- Typical deviation: **+/- 0.7 degrees** (1.4 degrees total)
- Affected by: terrain profile, moving vehicles, terrain moisture, snow

### ILS Categories

| Category | Decision Height | Visibility / RVR |
|----------|----------------|-------------------|
| CAT I    | 200 ft         | RVR 2400 ft (1800 ft with certain lighting) |
| CAT II   | 100 ft         | RVR 1200 ft |
| CAT IIIA | 50 ft (or none) | RVR 700 ft |
| CAT IIIB | 50 ft (or none) | RVR 150 ft |

- **Back course:** Localizer signal behind the runway; CDI deflection is **reversed** (left/right swapped)

---

## 6. FAA Regulatory Hierarchy and Definitions

### Key Document Types

| Document | Definition | Binding? |
|----------|-----------|----------|
| **Regulation (14 CFR)** | Legally enforceable rules established by the FAA under delegated authority from Congress. Published in the Code of Federal Regulations. | Yes |
| **Airworthiness Directive (AD)** | Legally enforceable rules issued per 14 CFR Part 39 to correct an unsafe condition in a product (aircraft, engine, propeller, or appliance). Owner/operator must take action. Types: NPRM, Final Rule -- Public Comment, Emergency NPRM. | Yes |
| **Advisory Circular (AC)** | FAA documents providing guidance on acceptable means of compliance. Not binding and not the sole means of compliance. May reference industry standards (RTCA, ASTM, etc.). | No (guidance only) |
| **Technical Standard Order (TSO)** | Minimum performance standard for materials, parts, and appliances on civil aircraft. Receiving TSO authorization is both design and production approval. Equipment marked with TSO number. | Yes (for authorization holders) |
| **Orders** | Documents defining FAA policy and procedures for FAA personnel. Can provide guidance on how regulation is interpreted and compliance is assessed. | Internal to FAA |

### Certification Terminology

- **Airworthiness Certificate:** States an aircraft is airworthy, conforming to its type certificate and maintained properly
  - **Standard** -- normal airworthiness
  - **Special** -- primary, restricted, limited, light-sport, experimental (R&D, crew training, exhibition, marketing)
- **Type Certificate (TC):** Certifies the aircraft design is airworthy. Entire aircraft certified; does not certify individual components. Onboard equipment cannot be modified under a TC.
- **Supplemental Type Certificate (STC):** Issued for modifications to an existing TC'd aircraft. Approves airworthiness and operational limits of the modified aircraft.
- **Production Certificate:** Authorizes production of aircraft based on a type certificate.
- **Special Conditions:** Designated by FAA for aircraft with novel/unique design features not covered by existing 14 CFR standards.
- **AMOC (Alternative Methods of Compliance):** Required when following a different approach to address an AD's unsafe condition.

### CFR Structure

- Title 14 -> Aeronautics and Space
  - Chapter 1 -> FAA regulations
    - Subchapters -> Parts -> Subparts -> Sections -> Paragraphs
- Citation format: **14 CFR SS 23.2105(b)** = Title 14, Part 23, Section 2105, Paragraph b

### Key 14 CFR Parts

| Part | Scope |
|------|-------|
| Part 21 | Foundational standard for airworthiness; type certificates, production certificates |
| Part 23 | General aviation aircraft airworthiness (updated 2017 to performance-based standards) |
| Part 25 | Transport category aircraft |
| Part 27 | General aviation rotorcraft |
| Part 29 | Transport category rotorcraft |
| Part 39 | Airworthiness directives |
| Part 91 | General operating and flight rules |
| Part 107 | Small UAS operations |
| Part 108 | BVLOS operations (pending) |

### Rulemaking Process

1. Aviation Rulemaking Committees (ARCs) assist in development
2. Draft rule vetted by FAA and DOT
3. Notice of Public Rulemaking (NPRM) issued
4. Public comment period
5. FAA addresses all comments
6. Revision toward final regulation
7. Approval through FAA and DOT -> becomes regulatory law

### Other Agencies and Bodies

- **ICAO:** UN organization coordinating international aviation standards (e.g., Annex 10 for telecommunications)
- **EASA:** European Aviation Safety Agency (European CAA)
- **CASA:** Civil Aviation Safety Authority (Australia)
- **ITU:** International Telecommunication Union -- establishes RF frequency allocations
- **FCC:** Federal Communications Commission -- oversees radio transmission standards in the US

### Standards Development Organizations (SDOs)

- **RTCA:** Produces MOPS and MASPS for aviation equipment
  - DO-178C: Airborne software certification
  - DO-254: Electronic hardware assurance
  - DO-160G: Environmental test procedures for airborne equipment
  - DO-365: MOPS for DAA systems
  - DO-386: Airborne radar for DAA
- **MASPS** (Minimum Aviation System Performance Standards): System-level specs for designers, manufacturers, service providers
- **MOPS** (Minimum Operational Performance Standards): Equipment-level specs including test procedures
- **SAE:** ARP4754A/B (system development), ARP4761/A (safety assessment)
- **ARINC/AEEC:** ARINC 429 (data bus), ARINC 664 (AFDX network), ARINC 653 (partitioned RTOS), ARINC 661 (cockpit displays)
- **ASTM F38:** Standards for small UAS (e.g., F3002 for C2 systems)

---

## 7. Detect and Avoid (DAA)

### Definition and Purpose

- DAA ensures a UAS remains well clear of other aircraft and performs collision avoidance maneuvers when a well-clear violation occurs or is imminent.
- Official FAA terminology is **"Detect and Avoid" (DAA)** -- replaces earlier terms like "sense and avoid," "detect, sense, and avoid," etc.
- DAA is a **safety-critical function**.

### Layered Approach

1. **Conflict Avoidance** (procedural/ATC)
   - ATC provides heading/altitude changes
2. **Remain Well Clear (RWC)** -- course adjustments to prevent conflict from becoming a collision hazard
   - Self-separation: UA maneuvers within sufficient timeframe to remain well clear
3. **Collision Avoidance** -- last-resort maneuver to prevent mid-air collision
   - Systems: TCAS II, ACAS X, ACAS Xu (for UAS)

### Key DAA Terminology (from RTCA DO-365)

- **Ownship:** The aircraft performing DAA functions
- **Intruder:** Another aircraft being tracked for potential avoidance
- **DAA Well Clear (DWC):** A temporal and/or spatial boundary around the aircraft; electronic means of avoiding conflicting traffic
- **Remain Well Clear (RWC):** Ability to detect, analyze, and maneuver to avoid conflict
  - Two aspects: Maintain DWC and Regain DWC
- **Collision Avoidance (upper case):** Last-resort method directed by a Collision Avoidance System
- **Collision Avoidance (lower case):** General act of maneuvering to prevent mid-air collision
- **Resolution Advisory (RA):** Directive guidance from a collision avoidance system
- **Tau (tau):** Estimate of time to collision used by systems like TCAS
- **Near Mid-Air Collision (NMAC):** The condition most collision avoidance systems seek to prevent

### Regulatory Basis

- **14 CFR 91.111:** Forbids operating in close proximity to other aircraft if collision hazard exists
- **14 CFR 91.113:** Requires vigilance to see and avoid; defines right-of-way rules
- **14 CFR 91.115:** Right-of-way for water operations
- **14 CFR 91.181:** Permits pilot to maneuver to pass "well clear" of other traffic in controlled airspace
- For UAS, "see and avoid" must be reallocated from onboard pilot to automation or remote pilot with equivalent level of safety

### Pilot's Role in DAA

- **Human-in-the-loop:** Pilot processes sensor inputs and commands avoidance
- **Human-on-the-loop:** System detects threat and notifies pilot; pilot approves action
- **Automated:** System detects and takes corrective action; pilot notified afterward
- PIC has **final legal authority** over aircraft actions
- Visual observers may substitute for sensors under Part 107

### Cooperative vs. Non-Cooperative Detection

- **Cooperative aircraft:** Equipped with transponder, ADS-B, TCAS/ACAS, IFF, etc.
  - Required for controlled airspace / IFR
- **Non-cooperative aircraft:** No cooperative technology; detection relies solely on sensor capabilities
  - Permissible in some airspace (e.g., Class E, G)
  - One of the greatest challenges for UAS integration

### Types of Collisions Addressed

- **Mid-Air Collision (MAC)** -- primary focus
- Terrain collision (see TAWS)
- Runway incursion
- Collision with objects on ground

### "Swiss Cheese" Analogy

- Each sensor type has "holes" in its detection capability (range limits, minimum target size, velocity, altitude, etc.)
- Goal: layer sensors so that no holes remain when stacked together

---

## 8. Sensing Technologies for DAA

### Transponder Types Summary

| Type | Data | Notes |
|------|------|-------|
| Mode 3/A | Squawk code (ident) | Replies to all interrogations |
| Mode C | Pressure altitude | Often used with Mode 3/A |
| Mode S | Altitude (25 ft increments), callsign, ICAO address | Supports TCAS and ADS-B; selective interrogation |
| Mode 5 | Encrypted Mode S + encrypted ADS-B position | Military use |
| ADS-B | Callsign, ICAO address, GPS position, altitude, velocity | Two standards: 1090 MHz ES and 978 MHz UAT |
| TCAS/ACAS | Traffic Advisories, Resolution Advisories | Works with Mode S transponder |

### Airborne Non-Cooperative Sensors

- **Primary Radar:** Most versatile non-cooperative sensor. Outputs: range, range rate, azimuth, elevation. RTCA DO-386 standard.
  - Limitations: frequency band availability, small/non-metallic targets hard to detect, ground reflections, weather effects, SWAP constraints
- **LIDAR / Laser Systems:** Time-of-flight measurement. Can determine distance, bearing, trajectory. Eye safety concerns for aviation.
- **EO/IR Cameras:** Passive, non-cooperative. Factors: contrast, target temperature, visual range, altitude, optics, detector.
  - **Johnson's Criteria:** Estimates number of pixels needed for detection/recognition/identification
  - EO: daylight/well-lit; IR: thermal spectrum, works in darkness/through fog/smoke
  - Ground-based IR range: ~35 km clear weather; Visual: ~20 km
- **Acoustic Sensors:** Microphone arrays analyzing airspace sounds. High signal-to-noise ratio concern.

### Ground-Based Detection

- **Primary Radar:** Detects cooperative and non-cooperative traffic; limited range vs. secondary
- **Secondary Radar:** Detects transponder-equipped (cooperative) aircraft; greater range than primary
- **TIS-B (Traffic Information Service -- Broadcast):** Uses ground radar to detect local traffic, uplinks via 1090 MHz ES or 978 MHz UAT to ADS-B-equipped aircraft. Can detect Mode S/Mode C transponder aircraft.
- **Visual Observers:** Ground-based or airborne (chase aircraft). Required for Part 107. PIC retains legal authority; observers assist with situational awareness.
- **FLARM:** Designed for gliders; similar to ADS-B; encrypted channel; range 10 km; supports up to 50 targets.

### Airspace Classes and DAA Implications

| Class | Key Rules |
|-------|-----------|
| A | IFR only (unless authorized) |
| B | IFR and VFR with clearance; requires two-way radio + transponder |
| C | IFR and VFR with clearance; requires two-way radio + Mode C transponder |
| D | Requires two-way radio; no VFR separation services |
| E | No specified equipment |
| G | Uncontrolled; supports IFR and VFR |

### Part 108 (Pending BVLOS Rules)

- Expects equipage with ADS-B or TABS (Traffic Awareness Beacon System)
- **Shielded operations:** Aircraft shielded from others by environment (e.g., urban canyons)
- **Non-shielded operations:** Typical operations requiring full DAA capability

---

## 9. GPS-Denied Navigation (Key Facts)

- Traditional navigation aids (VOR, DME, NDB) remain relevant for GPS-denied environments
- NDB uses ground waves independent of GPS
- VOR/DME provide bearing and distance without satellite dependency
- ILS provides precision approach guidance without GPS
- DAA systems must account for GPS-denied scenarios -- cooperative sensors like ADS-B depend on GPS position data, so non-cooperative sensors (radar, EO/IR, acoustic) become critical when GPS is unavailable

---

## Quick Reference: Key Formulas

| Formula | Expression |
|---------|-----------|
| Wavelength | lambda = c / f |
| Radar Mile | 2 x 1852 m / 3e8 m/s = 12.3 us |
| DME Distance (X ch.) | D(NM) = (t - 50 us) / 12.3 us |
| Slant Range | SR^2 = GR^2 + Alt^2 |
| DME Capacity | ~2000 pps / 15 pps per aircraft = ~133 aircraft |
| VOR Variable Signal | Limacon pattern rotating at 30 Hz |
| CDI Sensitivity (VOR) | 2 degrees per dot |
| ILS LOC Deviation | +/- 2 degrees from centerline |
| ILS GS Typical Angle | 3 degrees, +/- 0.7 degrees deviation |

## Quick Reference: Key Acronyms

| Acronym | Meaning |
|---------|---------|
| NDB | Non-Directional Beacon |
| ADF | Automatic Direction Finder |
| VOR | VHF Omnidirectional Range |
| DME | Distance Measuring Equipment |
| ILS | Instrument Landing System |
| LOC | Localizer |
| GS | Glideslope |
| CDI | Course Deviation Indicator |
| RMI | Radio Magnetic Indicator |
| FRUIT | Friendly Replies Unsynchronized in Time |
| GARBLE | Interference scrambling signals preventing correct output |
| SQUITTER | DME responses to no interrogation (filler pulses) |
| DAA | Detect and Avoid |
| DWC | DAA Well Clear |
| RWC | Remain Well Clear |
| NMAC | Near Mid-Air Collision |
| MAC | Mid-Air Collision |
| AD | Airworthiness Directive |
| AC | Advisory Circular |
| TSO | Technical Standard Order |
| TC | Type Certificate |
| STC | Supplemental Type Certificate |
| MOPS | Minimum Operational Performance Standards |
| MASPS | Minimum Aviation System Performance Standards |
| ADS-B | Automatic Dependent Surveillance -- Broadcast |
| TCAS | Traffic Collision Avoidance System |
| ACAS | Airborne Collision Avoidance System |
| TIS-B | Traffic Information Service -- Broadcast |
| BVLOS | Beyond Visual Line of Sight |
| TABS | Traffic Awareness Beacon System |
| SWAP | Size, Weight, and Power |
| AMOC | Alternative Methods of Compliance |
