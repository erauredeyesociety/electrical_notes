# CEC 300 - Module 4 and 5 Homework References

## Course Materials

### [1] CEC300 - ATCRBS and Mode S Transponders.pdf
CEC 300 lecture slides (38 slides) covering Air Traffic Control Radar Beacon System (ATCRBS), Mode A/C/S transponder interrogation and response protocols, sidelobe suppression (SLS), Gillham code, encoding altimeters, stochastic acquisition, Mode S selective addressing, lockout, squitter/extended squitter, CRC error detection, and air-to-air Mode S.
- **Key Slides:** 2 (ATCRBS overview), 8 (SLS pulse), 9 (reply conditions), 15-18 (encoding altimeter / Gillham code), 19 (ATCRBS issues), 20-21 (Mode S overview), 23 (ICAO 24-bit address), 25 (All-Call vs Roll-Call), 27 (selective call format), 29-30 (lockout and stochastic acquisition), 32-34 (Mode S reply, squitter, CRC), 35 (air-to-air Mode S)
- **Used in:** Problems 1, 2

### [2] module 6b - sensing.pdf
CEC 300 lecture slides (31 slides) on sensing technologies for aviation surveillance, including transponder operations, radar-based detection, cooperative vs. non-cooperative aircraft classification, and sensor modalities for DAA.
- **Used in:** Problems 1, 6

### [3] CEC_300_ADS-B.pdf
CEC 300 lecture slides (29 slides) on Automatic Dependent Surveillance-Broadcast (ADS-B). Covers ADS-B fundamentals (Automatic, Dependent, Surveillance, Broadcast), benefits over radar, ADS-B OUT vs. ADS-B IN, 1090 ES and 978 UAT data links, Extended Squitter message format (112-bit), UAT message payload, FIS-B/TIS-B/ADS-R services, ADS-B airspace requirements (FAR 91.225), quality/integrity values (NACp, NACv, NIC, SDA, SIL), and ADS-B IN applications.
- **Key Slides:** 2-3 (what is ADS-B), 8 (ADS-B In vs Out), 9 (ADS-R, TIS-B, FIS-B), 10-11 (airspace requirements), 13 (ADS-B OUT data links table: DO-260B / DO-282B), 14 (ADS-B OUT system diagram), 20 (1090ES message specification), 21-22 (UAT message format and payload), 23 (quality values), 27 (ADS-R/TIS-B architecture), 28-29 (challenges and current issues)
- **Used in:** Problem 3

### [4] module 6a - DAA Overview.pdf
CEC 300 lecture slides (40 slides) providing an overview of Detect and Avoid (DAA) for Unmanned Aircraft Systems. Covers FAA terminology evolution, the layered approach to collision avoidance (conflict avoidance + collision avoidance), self-separation, Remain Well Clear (RWC), DAA Well Clear (DWC), ownship/intruder terminology, cooperative vs. non-cooperative targets, regulatory basis (14 CFR Part 91 sections 91.111, 91.113, 91.115, 91.181), pilot's role in DAA (human-in-the-loop, human-on-the-loop, automated), DAA sensing (airborne vs. ground-based), and system architecture challenges.
- **Key Slides:** 5 (layered approach diagram), 7 (DAA terminology), 8-9 (RTCA DO-365 definitions: Collision Avoidance, RWC, DWC), 10 (ownship/intruder), 15-17 (14 CFR Part 91 regulatory basis), 25 (pilot's role), 28 (cooperative vs. non-cooperative)
- **Used in:** Problems 4, 5, 6, 7

### [5] CEC 300 - Module 2 Homework (2).pdf
Prior CEC 300 homework covering navigation and transponder fundamentals, referenced for supplementary context on Mode A/C behavior.
- **Used in:** Problem 1 (supplementary)

### [6] module 6c - TCAS II and ACAS-X.pdf
CEC 300 lecture slides (37 slides) on Traffic Collision Avoidance System (TCAS II) and ACAS-X family. Covers TCAS II operation (TA/RA thresholds, time-to-co-altitude, hazard zones, single-threat encounters), ACAS Xa (probabilistic dynamics model, Markov Decision Process lookup table approach, hybrid ADS-B surveillance), ACAS Xo (special cases: CSPO, DNA), and ACAS Xu (UAS-specific: rule-based advisories, vertical + horizontal RAs, cooperative and non-cooperative intruder support, automated responses, return-to-course, RA compliance performance requirements, coordination with ACAS-equipped intruders).
- **Key Slides:** 7-8 (TA/RA thresholds), 16 (ACAS X overview, RTCA DO-385), 17 (self-separation vs collision avoidance), 21 (TCAS II vs ACAS Xa), 27 (ACAS Xu overview), 31 (ACAS Xu differences from Xa/Xo), 33 (horizontal RAs), 34 (handling alerts: remote PIC vs automated), 35 (RA compliance performance), 36 (coordination with ACAS-equipped intruders)
- **Used in:** Problem 4

---

## Standards Referenced in Course Materials

| Standard | Title | Relevance |
| -------- | ----- | --------- |
| **RTCA DO-365** | Minimum Operational Performance Standards (MOPS) for Detect and Avoid (DAA) Systems | Definitions of RWC, DWC, Collision Avoidance terminology (Problems 4, 7) |
| **RTCA DO-385** | MOPS for ACAS Xu | ACAS Xu standard for UAS collision avoidance (Problem 4) |
| **RTCA DO-260B** | MOPS for 1090 MHz Extended Squitter ADS-B and TIS-B | 1090 ES ADS-B message standard (Problem 3) |
| **RTCA DO-282B** | MOPS for Universal Access Transceiver (UAT) ADS-B | UAT ADS-B message standard (Problem 3) |
| **RTCA DO-360** | MOPS for Air-to-Air Radar for UAS DAA | Non-cooperative surveillance for ACAS Xu (Problem 4) |
| **14 CFR Part 91** | General Operating and Flight Rules | Regulatory basis for see-and-avoid (91.113) and ADS-B equipage (91.225) (Problems 3, 4) |
| **14 CFR Part 107** | Small UAS Rules | Visual observer requirements and BVLOS waivers (Problem 4) |

---

## Textbook References

- **Spitzer, Ferrell, and Ferrell** — *Digital Avionics Handbook*. Referenced in the ADS-B lecture slides for ADS-B OUT data link tables and ADS-B IN application tables.
- **Helfrick (2010)** — Referenced in the ATCRBS lecture for transponder block diagram.
- **Binns** — *Aircraft Systems* (5 Primary and Secondary Radar). Referenced throughout ATCRBS and TCAS lectures for interrogation timing diagrams and system architecture figures.
- **Bodart (2019)** — Referenced in ATCRBS lecture for Mode S signal format diagrams.
