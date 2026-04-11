# CEC 300 - Module 4 and 5 Homework Solutions

## Transponders, ADS-B, and DAA

---

## Problem 1: Transponder Interrogation and Response Comparison

### Mode A Transponders

Mode A (often referred to as Mode 3/A) uses the ATCRBS (Air Traffic Control Radar Beacon System) secondary radar approach where a ground station transmits interrogation pulses at 1030 MHz and the aircraft replies at 1090 MHz. The interrogation consists of three pulses: P1, P2, and P3. To trigger a Mode A reply, the P1-to-P3 spacing must be exactly **8 microseconds**. Additionally, the transponder validates that P1 > P2 (sidelobe suppression check) and that P1-to-P2 spacing is 2 microseconds [1, Slides 8-9].

The primary information provided by a Mode A response is the **IDENT**, commonly known as the "Squawk Code." This is a four-digit octal identification code assigned by Air Traffic Control (ATC) to identify a specific flight on a radar display. Mode A replies consist of 12 data pulses with no error detection capability. Because Mode A responds to all valid interrogations without selectivity, it is susceptible to **"Fruit"** (replies from unintended stations) and **"Garble"** (overlapping replies from multiple aircraft), which wastes spectrum and requires repeated interrogations [1, Slides 2, 9, 19].

### Mode C Transponders

Mode C transponders utilize the same 1030/1090 MHz frequency pair as Mode A but are interrogated with a different timing sequence to request different data. A Mode C interrogation is defined by a **21 microsecond delay** between the P1 and P3 pulses (compared to 8 microseconds for Mode A). Like Mode A, it is a non-selective protocol, meaning every aircraft within the radar's beam that receives the signal will reply, regardless of its identity [1, Slides 9, 15].

The information provided by Mode C is the aircraft's **Pressure Altitude**. This data is captured by an encoding altimeter and transmitted in **100-foot increments** using an 11-bit sequence known as **Gillham Code** (a type of Gray code), covering a range from -1,200 ft to 126,700 ft. The altitude transmitted is uncorrected barometric (pressure) altitude, not corrected for local altimeter settings, which is necessary for consistent separation references. Mode C is almost always used in conjunction with Mode A to provide controllers with both the identity and the vertical position of the aircraft [1, Slides 15-18], [2, Slides 58-59].

### Mode S Transponders

Mode S (Select) was developed to address the spectrum congestion, garble/fruit interference, and limited information capabilities of Mode A and C. Each registered aircraft is assigned a unique **24-bit ICAO aircraft address** (supporting approximately 16.7 million unique addresses). Mode S remains backward compatible with ATCRBS, operating on the same 1030/1090 MHz frequencies at the same signal levels [1, Slides 19-21, 23].

Mode S uses a two-step interrogation approach: **All-Call** and **Roll-Call**. In an **All-Call** interrogation (approximately 1/3 of interrogations), the ground station broadcasts to identify all aircraft in its vicinity. To mitigate garble from simultaneous replies, Mode S employs **stochastic acquisition**, where aircraft are instructed to respond with a set probability (100%, 50%, 25%, 6.25%, or 0%) until acquired. Aircraft that successfully respond are then **"locked out"** from further All-Call replies to that station [1, Slides 25, 29-30].

Once an aircraft is acquired, the station transitions to **Roll-Call (Selective Interrogations)** (approximately 2/3 of interrogations), where it addresses that specific aircraft individually using its 24-bit ICAO address within a 56-bit or 112-bit data word. Mode S replies use **pulse position modulation** and include **CRC (Cyclic Redundancy Check)** parity bits for error detection, allowing the system to re-interrogate aircraft that produce error messages. Mode S provides significantly more information than its predecessors, including the unique ICAO address, callsign, and high-resolution pressure altitude in **25-foot increments**. Additionally, Mode S supports **air-to-air interrogations** (aircraft can send All-Call and Select messages to other aircraft), which is the foundational technology for TCAS and ADS-B [1, Slides 25, 27, 32-35].

---

## Problem 2: Side Lobe Suppression

### a. Fill in the Blanks

- The Side Lobe Suppression (SLS) mechanism in ATCRBS transponders prevents unwanted responses to ground radar interrogations transmitted through the radar antenna's **sidelobe** by using a two-pulse interrogation technique involving pulses P1 and P2.
- The ground radar transmits the main interrogation pulse (P1) using a **directional** antenna.
- Simultaneously, the ground radar transmits a second pulse (P2) from an **omnidirectional** antenna.
- The aircraft transponder is designed to compare the received **amplitudes** of the P1 and P2 pulses.
- The transponder will only respond to the interrogation if the received **P1** signal strength is greater than the **P2** signal strength.

### b. Why This Approach Works

This approach mitigates the impact of sidelobes by leveraging the difference in power distribution between directional and omnidirectional antennas.

A directional radar antenna concentrates the majority of its energy into a narrow **main beam**, but it inevitably radiates a smaller amount of energy in other directions, known as **sidelobes**. The omnidirectional antenna is calibrated to transmit the P2 pulse at a power level that is **stronger than the energy of any of the directional antenna's sidelobes** but significantly **weaker than its main beam** [1, Slide 8].

When the transponder compares the two pulses:

1. **In the Main Beam:** The directional P1 pulse is much stronger than the omnidirectional P2 pulse (P1 > P2). The transponder recognizes this as a valid interrogation and responds.
2. **In a Sidelobe:** The aircraft is hit by a weak P1 pulse from a sidelobe. Because the omnidirectional P2 pulse was sent at a power level higher than the sidelobes, the transponder receives a stronger P2 signal (P2 > P1). It then correctly identifies the interrogation as originating from a sidelobe and suppresses its reply, preventing unnecessary garble and interference [1, Slides 8-9].

---

## Problem 3: 1090 ES ADS-B vs. UAT ADS-B

Both ADS-B links are **Automatic** (broadcast without requiring an interrogation), **Dependent** (rely on onboard GNSS for position), and used for **Surveillance** via **Broadcast** to ground stations and other aircraft. Both provide position and velocity updates at approximately **1 Hz** [3, Slides 2-3].

|                                                                            | **1090 ES**                                                                                                                                                                                    | **UAT ADS-B (978 MHz)**                                                                                                                                                                     |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| What information about the aircraft is communicated with each update?      | Identity (24-bit ICAO address), airborne position, surface position, airborne velocity, and aircraft identification/callsign. Uses 112-bit Extended Squitter data blocks containing a 56-bit ADS-B message payload [3, Slide 20]. | Identity (24-bit ICAO address), latitude, longitude, altitude, horizontal velocity, vertical velocity, emitter category, callsign, and status information. Includes navigation quality values such as NACp (Position Accuracy), NACv (Velocity Accuracy), NIC (Navigation Integrity Category), SDA (System Design Assurance), and SIL (Surveillance Integrity Level) [3, Slides 22-23]. |
| Carrier Frequency (Hz)                                                     | **1090 MHz**                                                                                                                                                                                   | **978 MHz**                                                                                                                                                                                 |
| Integrated with the onboard transponder (yes or no)                        | **Yes** — it is an extension of Mode S technology and uses the aircraft's existing Mode S transponder to broadcast Extended Squitter messages (DF17/DF18). Governed by RTCA DO-260B [3, Slides 13, 17-18]. | **No** — it uses a dedicated Universal Access Transceiver, separate from the primary transponder. Governed by RTCA DO-282B [3, Slide 13]. |
| Recommend for which aircraft type (general aviation or transport category) | **Transport Category Aircraft** — internationally harmonized as the globally coordinated data link (used in the U.S., Europe, Asia, Pacific). **Required** for aircraft operating at or above **FL180** (Class A airspace) in the U.S. per FAR 91.225 [3, Slides 11-13]. | **General Aviation** — primarily intended for aircraft operating in U.S. national airspace **below FL180**. UAT is a U.S.-only link not used internationally [3, Slides 11, 13]. |
| Other                                                                      | Subject to spectrum congestion since it shares 1090 MHz with Mode A/C and Mode S transponder replies. **Does not** support FIS-B weather/aeronautical data services. Supports **TIS-B** (Traffic Information System - Broadcast) for traffic from non-ADS-B aircraft [3, Slides 9, 28-29]. | Supports **FIS-B** (Flight Information Services - Broadcast), providing free ground-based aeronautical data, weather (METAR, TAF), SIGMETs, and NOTAMs to suitably equipped aircraft. Also supports **ADS-R** (Re-broadcast) to relay 1090 ES traffic updates to UAT users and vice versa via ground stations [3, Slides 9, 21-22, 27]. |

---

## Problem 4: Layered Approach to Collision Avoidance

The "layered approach" to avoiding potential collisions in aviation is a hierarchical safety framework composed of two primary functional layers: **Conflict Avoidance (Self-Separation)** and **Collision Avoidance**. This architecture is designed to provide multiple opportunities to resolve a threat before it results in a Mid-Air Collision (MAC). Detect and Avoid (DAA) for UAS addresses both cooperative and non-cooperative collision avoidance through these layers [4, Slide 5].

### Layer 1: Conflict Avoidance and Self-Separation

Conflict avoidance is the proactive layer, focusing on maintaining a **"Remain Well Clear" (RWC)** status. As defined by RTCA DO-365, RWC is "the ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path in order to prevent the conflict from developing into a collision hazard." This layer includes procedural measures (ATC-controlled airspace procedures), Air Traffic Management instructions (heading or altitude changes), and pilot or automation-driven well-clear maintenance [4, Slides 5, 9].

- **Manned Aviation:** This layer relies on **Air Traffic Management (ATM)** instructions and the pilot's visual vigilance, governed by the regulatory principle of **"see and avoid"** under 14 CFR 91.113, which addresses the necessary vigilance required to see and avoid other aircraft. Pilots use ground-based radar instructions and visual scanning to stay well clear of other aircraft [4, Slides 15-17].
- **UAS:** Since the pilot is physically separated from the aircraft, UAS utilize **automated self-separation mechanisms**. These systems use sensors like **ADS-B** or **Ground-based Radar** to identify ownship and intruder locations, allowing the automation (or a remote pilot) to maneuver within a sufficient timeframe to maintain **DAA Well Clear (DWC)** boundaries. The function can be implemented as human-in-the-loop, human-on-the-loop, or fully automated depending on the system architecture [4, Slides 5, 25].

### Layer 2: Collision Avoidance (CA)

The final safety layer is **Collision Avoidance**, acting as a "last-resort method of preventing mid-air collisions between aircraft, as directed by a Collision Avoidance System" (per RTCA DO-365). This layer activates when the self-separation layer has been violated, requiring highly deterministic, rapid maneuvers [4, Slide 8], [6, Slides 1-2].

- **Manned Aviation:** The primary implementation is **TCAS II**. It interrogates the transponders of nearby aircraft using Mode C and Mode S signals and, if a collision is imminent (based on time-to-co-altitude thresholds), provides a **Resolution Advisory (RA)** directing the pilot to execute a specific **vertical-only** maneuver (e.g., "Climb, Climb" or "Descend, Descend"). TCAS II uses a rules-based deterministic logic system to issue Traffic Advisories (TAs) and RAs [6, Slides 7-14].
- **UAS:** The specialized system **ACAS Xu** (defined in RTCA DO-385) is the ACAS X standard for Uncrewed Aircraft Systems. Unlike TCAS II, ACAS Xu provides several key enhancements: (1) it issues **Resolution Advisories in both vertical and horizontal planes**, including blended RAs specifying both heading and altitude changes; (2) it supports **non-cooperative surveillance** inputs (e.g., air-to-air radar per RTCA DO-360) in addition to transponder and ADS-B data; (3) it enables **automated responses**, where the flight control system executes the evasive maneuver and then performs a return-to-course behavior autonomously without requiring remote pilot input, ensuring safety even during a lost-link scenario. When both aircraft are ACAS-equipped, they coordinate their RAs through interrogation messages to ensure compatible maneuvers [6, Slides 27, 31, 34, 36].

---

## Problem 5

**Answer: d. Detect and Avoid (DAA)**

According to the DAA Overview notes on terminology (Slide 7), while several terms like "see and avoid (SAA)," "detect, sense, and avoid (DSA)," "sense and avoid (SAA)," and "sense & avoid (S&A)" have evolved over time, **"DAA is the official terminology recognized by the FAA"** for the UAS equivalent of manned aviation's "see and avoid" capability [4, Slide 7].

---

## Problem 6

**Answer: b. It is equipped with a transponder or ADS-B**

The course materials explicitly distinguish between cooperative and non-cooperative aircraft: a **cooperative aircraft** is one that is "equipped with a form of cooperative technology such as: Transponder, ADS-B, TCAS / ACAS I or II, Identify Friend or Foe System." Non-cooperative aircraft are not equipped with such technologies and represent one of the great challenges of UAS integration [4, Slide 28].

---

## Problem 7

**Answer: c. The ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path**

Drawing from RTCA DO-365 definitions, the sources define Remain Well Clear (RWC) as "the ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path in order to prevent the conflict from developing into a collision hazard." RWC includes two aspects: maintaining DWC and regaining DWC. Note that option (d) describes **DAA Well Clear (DWC)**, which is "a temporal and/or spatial boundary around the aircraft intended to be an electronic means of avoiding conflicting traffic" — a related but distinct concept [4, Slide 9].
