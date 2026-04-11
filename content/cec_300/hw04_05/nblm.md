please answer the following questions and reference your resources for your answers:

"""
Problem 1: [10 points] Contrast the interrogation and response approach for Mode A, Mode C, and Mode S transponders. What information does each provide? Note: For Mode s, please be sure to discuss all-call vs. roll-call interrogations. You should reply with 1-2 paragraphs for each transponder type.
"""



### **Problem 1: Transponder Interrogation and Response Comparison**

#### **Mode A Transponders**
Mode A (often referred to as Mode 3/A) uses a standard secondary radar interrogation approach where a ground station transmits pulses at 1030 MHz and the aircraft replies at 1090 MHz. The interrogation pulse sequence for Mode A consists of two pulses, P1 and P3, spaced exactly **8 microseconds ($\mu s$)** apart. Any aircraft receiving this valid timing sequence will trigger a response.

The primary information provided by a Mode A response is the **IDENT**, commonly known as the "Squawk Code". This is a four-digit octal identification code assigned by Air Traffic Control (ATC) to identify a specific flight on a radar display. Because Mode A responds to all valid interrogations, it is susceptible to "Fruit" and "Garble," which occur when multiple aircraft replies overlap or are received by unintended stations.

#### **Mode C Transponders**
Mode C transponders utilize the same 1030/1090 MHz frequency pair as Mode A but are interrogated with a different timing sequence to request different data. A Mode C interrogation is defined by a **21 $\mu s$ delay** between the P1 and P3 pulses. Like Mode A, it is a non-selective protocol, meaning every aircraft within the radar's beam that receives the signal will reply, regardless of its identity.

The information provided by Mode C is the aircraft's **Pressure Altitude**. This data is captured by an encoding altimeter and transmitted in **100-foot increments** using a 11-bit sequence known as **Gillham Code** (a type of Gray code). Mode C is almost always used in conjunction with Mode A to provide controllers with both the identity and the vertical position of the aircraft.

#### **Mode S Transponders**
Mode S (Select) was developed to address the spectrum congestion and interference limitations of Mode A and C by utilizing a unique **24-bit ICAO aircraft address**. While it remains backward compatible with legacy systems, Mode S uses a two-step interrogation approach: **All-Call** and **Roll-Call**. In an **All-Call** interrogation, the ground station identifies all aircraft in its vicinity. To prevent signal "Garble" from dozens of aircraft responding at once, Mode S uses **stochastic acquisition**, where aircraft are told to respond with a specific probability (e.g., a 1/2 or 1/4 chance) until they are acquired and "locked out" from further All-Calls.

Once an aircraft's unique address is known, the station transitions to **Roll-Call (Selective Interrogations)**, where it interrogates that specific aircraft individually for data. Mode S provides significantly more information than its predecessors, including the unique ICAO address, callsign, and high-resolution pressure altitude in **25-foot increments**. Additionally, Mode S supports **air-to-air interrogations**, which is the foundational technology for the Traffic Collision Avoidance System (TCAS) and Automatic Dependent Surveillance-Broadcast (ADS-B).

***

### **Resources Used**
*   **CEC300 - ATCRBS and Mode S Transponders.pdf:** [Slides 11, 12, 13, 15, 16, 17, 18, 21, 23].
*   **module 6b - sensing.pdf:** [Slide 58, 59].
*   **CEC 300 - Module 2 Homework.pdf:** [Page 20].


please answer the following questions and reference your resources for your answers:

"""


Problem 2: [10 points] Fill in the blanks on the description of side lobe suppression. Then, in your own words, explain why this approach works.
a.
[6 points] Fill in the blanks
•
The Side Lobe Suppression (SLS) mechanism in ATCRBS transponders prevents unwanted responses to ground radar interrogations transmitted through the radar antenna's ________________by using a two-pulse interrogation technique involving pulses P1 and P2.
•
The ground radar transmits the main interrogation pulse (P1) using a ________________antenna.
•
Simultaneously, the ground radar transmits a second pulse (P2) from an ________________antenna.
•
The aircraft transponder is designed to compare the received ________________of the P1 and P2 pulses.
•
The transponder will only respond to the interrogation if the received ________________signal strength is greater than the ________________ signal strength.
Options: P1, P2, omnidirectional, directional, amplitudes, sidelobe
b.
[4 points] Why does this approach mitigate the impact of sidelobes? i.e. how does the comparison of the two pulses help us determine if it is a sidelobe pulse or not?

"""




Based on the provided sources, here are the answers for Problem 2 regarding Side Lobe Suppression (SLS).

### **a. Fill in the Blanks**

*   The Side Lobe Suppression (SLS) mechanism in ATCRBS transponders prevents unwanted responses to ground radar interrogations transmitted through the radar antenna's **sidelobe** by using a two-pulse interrogation technique involving pulses P1 and P2.
*   The ground radar transmits the main interrogation pulse (P1) using a **directional** antenna.
*   Simultaneously, the ground radar transmits a second pulse (P2) from an **omnidirectional** antenna.
*   The aircraft transponder is designed to compare the received **amplitudes** of the P1 and P2 pulses.
*   The transponder will only respond to the interrogation if the received **P1** signal strength is greater than the **P2** signal strength.

---

### **b. Why this approach works**

This approach mitigates the impact of sidelobes by leveraging the difference in power distribution between directional and omnidirectional antennas. 

A directional radar antenna concentrates the majority of its energy into a narrow **main beam**, but it inevitably radiates a smaller amount of energy in other directions, known as **sidelobes**. The omnidirectional antenna is calibrated to transmit the **P2 pulse** at a power level that is **stronger than any of the directional antenna's sidelobes** but significantly **weaker than its main beam**. 

When the transponder compares the two pulses:
1.  **In the Main Beam:** The directional P1 pulse is much stronger than the omnidirectional P2 pulse ($P1 > P2$). The transponder recognizes this as a valid interrogation and responds.
2.  **In a Sidelobe:** The aircraft is hit by a weak P1 pulse from a sidelobe. Because the omnidirectional P2 pulse was sent at a power level higher than the sidelobes, the transponder receives a stronger P2 signal ($P2 > P1$). It then correctly identifies the interrogation as a sidelobe and ignores it to prevent "Garble" or unnecessary interference.

***

### **Resources Used**
*   **CEC300 - ATCRBS and Mode S Transponders.pdf**: [Slide 14] "Sidelobe Suppression Pulse," [Slide 15] "When Reply to Interrogation."










please answer the following questions and reference your resources for your answers:

"""


Problem 3: [10 points] Compare and contrast 1090 ES ADS-B vs. UAT ADS-B. Describe the type of users for each, vehicle state data transmitted, integration with the aircraft’s systems.

"1090 ES ADS-B" vs "UAT ADS-B"

- What information about the aircraft is communicated with each update?

- Carrier Frequency (Hz)

- Integrated with the onboard transponder (yes or no)

- Recommend for which aircraft type (general aviation or transport category aircraft)

- Other

"""



Based on the provided sources, here is a comparison between **1090 ES ADS-B** and **UAT ADS-B**:

### **1090 ES ADS-B (Extended Squitter)**
*   **Information Communicated:** Periodically broadcasts identity (24-bit ICAO address), vehicle state (position and velocity), and other aircraft status information. Specifically, it uses "Extended Squitter" messages (112-bit data blocks) for airborne position, surface position, airborne velocity, and aircraft identification/callsign.
*   **Carrier Frequency:** **1090 MHz**.
*   **Integrated with Onboard Transponder:** **Yes**. It is an extension of Mode S technology and utilizes the aircraft's existing Mode S transponder to broadcast messages.
*   **Recommended Aircraft Type:** **Transport Category Aircraft**. It is internationally coordinated as the globally harmonized data link and is required for aircraft flying at or above **FL180** (18,000 ft) in the U.S. and throughout most of the world (including Europe, Asia, and the Pacific).
*   **Other:** 1090 ES is subject to spectrum congestion because it shares the 1090 MHz frequency with Mode A/C and Mode S transponder replies. It **does not support FIS-B** (weather/aeronautical data) services.

---

### **978 MHz UAT ADS-B (Universal Access Transceiver)**
*   **Information Communicated:** Broadcasts identical state data to the 1090 ES link, including identity (24-bit ICAO address), position, altitude, horizontal/vertical velocity, and status information. The UAT payload also includes specific navigation quality values like NACp (Position Accuracy) and NIC (Integrity Category).
*   **Carrier Frequency:** **978 MHz**.
*   **Integrated with Onboard Transponder:** **No**. It utilizes a dedicated Universal Access Transceiver rather than the primary Mode S transponder used for radar interrogations.
*   **Recommended Aircraft Type:** **General Aviation**. It is primarily intended for general aviation aircraft flying in the U.S. national airspace **below FL180**.
*   **Other:** UAT is unique in that it supports **FIS-B (Flight Information Services – Broadcast)**, allowing suitably equipped aircraft to receive free ground-based weather data, SIGMETs, and NOTAMs. It also supports **ADS-R (Re-broadcast)**, which allows UAT users to see 1090 ES traffic updates relayed by ground stations.

***

### **Resources Used**
*   **CEC_300_ADS-B.pdf:** [Slides 17, 18, 22, 23, 24, 25, 26]
*   **module 6b - sensing.pdf:** [Slide 52, 53]
*   **CEC300 - ATCRBS and Mode S Transponders.pdf:** [Slide 15] (Mode S messaging context)




please answer the following questions and reference your resources for your answers:

"""

Problem 4: [10 points] Explain the "layered approach" to avoiding potential collisions as it pertains to both traditional manned aircraft and Unmanned Aircraft Systems (UAS), drawing on the concepts of Self-Separation and Collision Avoidance. Cite specific examples of how these layers are implemented in each type of aviation. Your response should be 200+ words.

"""




The "layered approach" to avoiding potential collisions in aviation is a hierarchical safety framework composed of two primary functional layers: **Conflict Avoidance (Self-Separation)** and **Collision Avoidance**. This architecture is designed to provide multiple opportunities to resolve a threat before it results in a Mid-Air Collision (MAC).

### **Layer 1: Conflict Avoidance and Self-Separation**
Conflict avoidance is the proactive layer, focusing on maintaining a **"Remain Well Clear" (RWC)** status. The objective is to detect potential conflicts early and apply adjustments to the flight path to prevent them from developing into an immediate hazard.

*   **Manned Aviation Example:** This layer relies on **Air Traffic Management (ATM)** instructions and the pilot's visual vigilance, governed by the regulatory principle of **"see and avoid"**. Pilots use ground-based radar instructions and visual scanning to stay well clear of other aircraft.
*   **UAS Example:** Since the pilot is physically separated from the aircraft, UAS utilize **automated self-separation mechanisms**. These systems use sensors like **ADS-B** or **Ground-based Radar** to identify ownship and intruder locations, allowing the automation (or a remote pilot) to maneuver within a sufficient timeframe to maintain **DAA Well Clear (DWC)** boundaries.

### **Layer 2: Collision Avoidance (CA)**
The final safety layer is **Collision Avoidance**, acting as a "last-resort" method to prevent a collision when the RWC layer has been violated. This layer requires highly deterministic, rapid maneuvers.

*   **Manned Aviation Example:** The primary implementation is **TCAS II**. It interrogates the transponders of nearby aircraft and, if a collision is imminent, provides a **Resolution Advisory (RA)** directing the pilot to execute a specific vertical maneuver (e.g., "Climb, Climb").
*   **UAS Example:** The specialized system **ACAS Xu** is designed for UAS. Unlike the vertical-only rules of TCAS II, ACAS Xu can provide **Resolution Advisories in both vertical and horizontal planes**. Furthermore, it supports **automated responses**, where the flight control system executes the evasive maneuver autonomously without requiring remote pilot input, ensuring safety even during a lost-link scenario.

***

### **Resources Used**
*   **module 6a - DAA Overview.pdf:** Definitions of DAA, layered approach, and "Well Clear" [Slides 50, 51, 53, 54, 59, 60].
*   **module 6b - sensing.pdf:** Role of transponders and ground-based detection [Slides 72, 75].
*   **module 6c - TCAS II and ACAS-X.pdf:** Comparison of TCAS II and ACAS Xu, RA logic, and automated responses [Slides 80, 81, 82, 84, 85, 86].




please answer the following questions and reference your resources for your answers:

"""

Problem 5: [2 points] According to the provided materials, which of the following is the official terminology recognized by the FAA for the "equivalent" capability to manned aviation's "see and avoid" for UAS?
a.
See and Avoid (SAA)
b.
Detect, Sense, and Avoid (DSA)
c.
Sense and Avoid (SAA)
d.
Detect and Avoid (DAA)
Problem 6: [2 points] Which of the following is considered a characteristic of a cooperative aircraft in the context of DAA?
a.
It is small and non-metallic
b.
It is equipped with a transponder or ADS-B
c.
It does not utilize air traffic management systems
d.
It relies solely on being visually detected
Problem 7: [2 points] What is "Remain Well Clear (RWC)" defined as in the context of DAA?
a.
A last-resort method of preventing mid-air collisions directed by a Collision Avoidance System
b.
The ability of a human operator to harness their five senses to detect aircraft
c.
The ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path
d.
A temporal and/or spatial boundary around the aircraft intended to be an electronic means of avoiding conflicting traffic

"""


Based on the provided sources, here are the answers for Problems 5, 6, and 7:

**Problem 5: [2 points] According to the provided materials, which of the following is the official terminology recognized by the FAA for the "equivalent" capability to manned aviation's "see and avoid" for UAS?**
*   **Correct Answer: d. Detect and Avoid (DAA)**
*   **Source Reference:** According to the "Notes on Terminology" slide in the DAA Overview, while several terms like "sense and avoid" or "detect, sense, and avoid" have evolved over time, **"DAA is the official terminology recognized by the FAA"** for UAS.

**Problem 6: [2 points] Which of the following is considered a characteristic of a cooperative aircraft in the context of DAA?**
*   **Correct Answer: b. It is equipped with a transponder or ADS-B**
*   **Source Reference:** The sources distinguish between cooperative and non-cooperative aircraft, stating that a **cooperative aircraft** is **"equipped with a form of cooperative technology such as: Transponder, ADS-B, TCAS / ACAS I or II"**.

**Problem 7: [2 points] What is "Remain Well Clear (RWC)" defined as in the context of DAA?**
*   **Correct Answer: c. The ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path**
*   **Source Reference:** Drawing from RTCA DO-365 definitions, the sources define **Remain Well Clear (RWC)** as **"the ability to detect, analyze and maneuver to avoid potential conflicting traffic by applying adjustments to the current flight path in order to prevent the conflict from developing into a collision hazard"**. (Note: Option D describes "DAA Well Clear (DWC)", which is the temporal or spatial boundary itself).