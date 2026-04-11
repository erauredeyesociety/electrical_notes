# CEC 300 - Module 4 & 5 Homework Solutions (Concise)

---

## Problem 1: Mode A vs. Mode C vs. Mode S Transponders

**Mode A:** Ground station interrogates at 1030 MHz, aircraft replies at 1090 MHz. Mode A interrogation uses P1-to-P3 spacing of 8 microseconds. Every aircraft in range replies (non-selective). The reply provides the aircraft's **IDENT (squawk code)** — a four-digit octal code assigned by ATC. This non-selective approach causes garble and fruit when multiple aircraft respond simultaneously.

**Mode C:** Same 1030/1090 MHz frequencies, but P1-to-P3 spacing is 21 microseconds. Still non-selective. The reply provides the aircraft's **pressure altitude** in 100-foot increments, encoded using Gillham code (a gray code) via an encoding altimeter. Typically used alongside Mode A so ATC gets both identity and altitude.

**Mode S:** Uses a unique 24-bit ICAO address per aircraft to enable selective interrogation. Two-phase process: (1) **All-Call** — ground station broadcasts to discover nearby aircraft; uses stochastic acquisition (aircraft reply with probability 100%/50%/25%/6.25%) to reduce garble, then locks out acquired aircraft from future All-Calls. (2) **Roll-Call** — ground station interrogates known aircraft individually by their ICAO address for specific data. Mode S provides the ICAO address, callsign, altitude in 25-foot increments, and supports CRC error detection. It also enables **air-to-air interrogation**, which is the basis for TCAS and ADS-B.

---

## Problem 2: Side Lobe Suppression

### a. Fill in the Blanks

1. **sidelobe**
2. **directional**
3. **omnidirectional**
4. **amplitudes**
5. **P1**
6. **P2**

### b. Why It Works

The omnidirectional P2 antenna is set to a power level stronger than the directional antenna's sidelobes but weaker than its main beam. So if the aircraft is in the main beam, P1 > P2 and it responds. If the aircraft is in a sidelobe, the weak sidelobe P1 is less than P2, so the transponder suppresses its reply. This prevents false interrogations from sidelobes.

---

## Problem 3: 1090 ES vs. UAT ADS-B

|                              | **1090 ES**                                  | **UAT ADS-B**                                |
| ---------------------------- | -------------------------------------------- | -------------------------------------------- |
| **Info communicated**        | ICAO address, position, velocity, callsign, altitude (112-bit Extended Squitter) | ICAO address, position, velocity, altitude, callsign, plus quality values (NACp, NACv, NIC, SDA, SIL) |
| **Carrier Frequency**        | 1090 MHz                                     | 978 MHz                                      |
| **Integrated w/ transponder**| Yes (uses Mode S transponder)                | No (separate Universal Access Transceiver)   |
| **Recommended aircraft**     | Transport category (required at/above FL180) | General aviation (below FL180, U.S. only)    |
| **Other**                    | Shares congested 1090 MHz band; no FIS-B support | Supports FIS-B (free weather/NOTAMs) and ADS-R (rebroadcasts 1090 ES traffic to UAT users) |

---

## Problem 4: Layered Approach to Collision Avoidance

Aviation uses a two-layer safety framework to prevent mid-air collisions, applicable to both manned and unmanned aircraft.

**Layer 1 — Self-Separation (Remain Well Clear):** The proactive layer. The goal is to detect conflicts early and adjust the flight path before a collision threat develops. For manned aircraft, this is accomplished through ATC instructions and the pilot's "see and avoid" responsibility (14 CFR 91.113). For UAS, the remote pilot or onboard automation performs self-separation using sensors like ADS-B or ground-based radar to track nearby traffic and maintain DAA Well Clear (DWC) boundaries.

**Layer 2 — Collision Avoidance (Last Resort):** Activates when self-separation fails. For manned aircraft, **TCAS II** interrogates nearby transponders and issues vertical-only Resolution Advisories (e.g., "Climb" or "Descend"). For UAS, **ACAS Xu** serves the same function but with key differences: it provides RAs in both the vertical and horizontal planes, it can use non-cooperative sensor data (radar), and it supports fully automated execution of evasive maneuvers with return-to-course — critical for lost-link scenarios where no remote pilot is available.

Together these layers ensure multiple opportunities to resolve a conflict before it becomes a collision.

---

## Problem 5

**d. Detect and Avoid (DAA)**

---

## Problem 6

**b. It is equipped with a transponder or ADS-B**

---

## Problem 7

**c. The ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path**

(Option d describes DAA Well Clear (DWC), which is the boundary itself, not the capability.)
