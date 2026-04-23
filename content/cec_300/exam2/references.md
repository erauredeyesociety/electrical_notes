# CEC 300 Exam 2 — Research & References

Evidence collected by parallel research agents from the course content (all PDFs extracted to `extracted/`) and, for Q15, from authoritative outside sources.

---

## Q1 — Overlapping transponder replies (Mode S selective interrogation)

**Answer: B** — Replace broad Mode A/C-style interrogation with Mode S selective interrogation and lockout.

**Evidence from "CEC300 – ATCRBS and Mode S Transponders":**

- "Garble / Fruit [is] Wasteful of Spectrum [and requires] Repeated Interrogations" (p. 19)
- "Mode S Technology attempts to mitigate ATCRBS [through] Selective Interrogations (aka 'roll call' — once local aircraft are known, interrogate those aircraft. Lock out aircraft that have responded with updates to avoid unnecessary replies to all-call)." (p. 20)
- "After All-Call, Mode S radar will only interrogate the known aircraft with the SELECT (Roll Call) interrogation. Aircraft transponders lock out replies to the station's ALL Call interrogations until SELECT Message indicating lock out has ended." (p. 29)
- "Developed to provide more modern enhancements and reduce the amount of over-interrogation occurring. Built to be backward compatible with ATCRBS air/ground systems." (p. 21)

**Key concepts:** garbling/fruiting, ATCRBS limits, stochastic acquisition, Mode S all-call → roll-call, ICAO 24-bit address, lockout, backward compatibility.

**Why the distractors fail:**
- **A** — more power makes overlap worse, not better.
- **C** — more frequent interrogations multiply replies.
- **D** — dropping altitude requests barely shortens replies and loses mode-C information.

---

## Q2 — BVLOS UAS: ADS-B IN vs air-to-air radar

**Answer: B** — Radar still needed: ADS-B is cooperative-only and spoofable; radar finds non-cooperative intruders and cross-checks suspicious broadcasts.

**Evidence:**

- "Cooperative aircraft: Equipped with a form of cooperative technology such as: Transponder, ADS-B, TCAS/ACAS I or II. … Non-cooperative aircraft: Not equipped with a technology that aids in detection through traditional air traffic management system. … Non-cooperative aircraft are one of the great challenges of UAS integration." (Module 6b sensing, p. 28)
- "Radar (Primary): Most versatile non-cooperative sensor. Outputs: Range, range rate, azimuth, and elevation." (Module 6b sensing, p. 11)
- "4 — Malicious spoofing. Have backup surveillance systems such as Mode S." (CEC_300 ADS-B, p. 27)
- "Lack of privacy — ADS-B messages are not encrypted. … Easy to spoof." (CEC_300 ADS-B, p. 28)
- "Spoofing of ADS-B radio signals can present false aircraft information." (M7 Cybersecurity, p. 9)

**Why the distractors fail:**
- **A** — ADS-B never "guarantees" avoidance; it's cooperative-only.
- **C** — false; ADS-B broadcasts barometric *and* geodetic altitude.
- **D** — TCAS is independent of ground primary radar.

---

## Q3 — TCAS II Resolution Advisory trigger

**Answer: B** — A time-to-collision (tau) or time-to-co-altitude threshold was crossed.

**Evidence:**

- "Time to Co-altitude Threshold. (TVTHR)" (Module 6c TCAS II & ACAS-X, p. 7)
- "TA / RA times vs. altitude" — altitude-band-dependent tau thresholds (Module 6c TCAS II & ACAS-X, p. 8)
- "Systems like TCAS use some definition of tau (τ), an estimate of time to collision." (Module 6a DAA Overview, p. 9)
- "With TCAS II, a set of rules is used to determine given the states of ownship and intruder the type of traffic alert or resolution advisory to issue." (Module 6c TCAS II & ACAS-X, p. 21)

**Key concepts:** τ = slant-range / closure-rate as CPA estimate; separate TA and RA thresholds; thresholds vary by altitude band; RA can fire while aircraft are still measurably apart because τ is a *time* threshold, not a distance threshold.

**Why the distractors fail:**
- **A** — TCAS II runs on Mode S interrogation/reply, not ADS-B.
- **C** — ground primary radar doesn't drive airborne TCAS logic.
- **D** — pilot override silences advisories, doesn't create them.

---

## Q4 — Probabilistic collision avoidance (ACAS X)

**Answer: B** — Probabilistic decision-making and cost optimization, as used in the ACAS X family.

**Evidence:**

- "ACAS Xa combines a probabilistic dynamics model to determine where the aircrafts may go and a probabilistic sensor model to account for noise/error in sensor measurements." (Module 6c TCAS II & ACAS-X, p. 20)
- "ACAS Xa uses a look-up table to determine possible actions to take given the state. Considering the associated cost of the action, the system selects action with the lowest cost." (p. 21)
- "Explainer: Markov Decision Process" (p. 22) — the offline dynamic-programming method that generates the lookup table.
- TCAS II is contrasted: "a set of rules is used to determine … the type of traffic alert or resolution advisory to issue." (p. 21)

**Key concepts:** probabilistic dynamics + sensor models; offline MDP / dynamic programming → compiled lookup table; online selection of minimum-expected-cost maneuver; replaces TCAS II's deterministic rules.

**Why the distractors fail:** none of A, C, D captures probabilistic optimization.

---

## Q5 — ADS-B spoofability property

**Answer: B** — Lack of strong built-in encryption and authentication.

**Evidence:**

- "Unencrypted communication protocols, such as ADS-B, are susceptible to spoofing and manipulation and do not maintain confidentiality." (M7 Cybersecurity, p. 9)
- "Lack of (strong) authentication on critical data flows like data link can be exploited." (M7 Cybersecurity, p. 9)
- "ADS-B transmits flight positions without strong authentication." (M7 Cybersecurity, p. 34)
- "Lack of privacy — ADS-B messages are not encrypted. … Easy to spoof." (CEC_300 ADS-B, p. 28)
- "Cross-checking with additional sensors (e.g., radar, inertial navigation) is essential. Mitigation involves cryptographic signing of messages and anomaly detection." (M7 Cybersecurity, p. 34)

**Why the distractors fail:** ADS-B does not depend on air-ground radar (A), operates at all altitudes (C), and 1 Hz is adequate for surveillance (D).

---

## Q6 — Predictive-maintenance model generalization failure

**Answer: B** — Training data were biased, insufficiently diverse, or not representative of deployment conditions.

**Evidence from "AI+ML in Aviation and Aerospace":**

- "Insufficient data for a model can result in overfitting to only the cases given to it." (p. 5)
- "Challenge: Garbage In → Garbage Out … Missing data … Imbalanced Data … Outliers … Noisy data … Lack of Diversity … Poor data labeling." (p. 5)
- "Machine learning models largely are data-driven. … Data needs scale with model complexity." (p. 5)
- "Bias and Fairness" listed as a core ethical consideration (p. 13).
- "Proper data governance and quality are essential for the dependability and trustworthiness of AI systems in aerospace." (p. 53)

**Key concepts:** data-driven performance bound, distribution shift between training and deployment, overfitting/lack of diversity, bias.

**Why the distractors fail:**
- **A** — "too much data" isn't a failure mode the deck names; *insufficient* data is.
- **C** — number of sensors at deployment is a distractor; the deck treats more sensors as adding information.
- **D** — RL is defined on p. 9 as reward/penalty learning; it's not a remedy for generalization gaps in regression/classification.

---

## Q7 — Reward/penalty simulation agent

**Answer: C** — Reinforcement learning.

**Evidence:**

- "Reinforcement Learning — learns to respond to its state and stimuli through the reinforcement of which actions provided favorable results vs. which options provided less favorable results." (AI+ML, p. 9)
- "Agent must learn a policy, which dictates actions given state. Learning encourages maximization of rewards and/or minimization of penalties." (p. 17)
- "Reinforcement Learning Algorithms: Monte Carlo, Q-Learning, Markov Decision Modeling (MDM)." (p. 17)
- "Deep Q-Networks are used for controlling aircraft landing." (p. 47)
- "Explainable reinforcement learning contributes to fully automated and dependable autonomous aircraft." (p. 43)

**Why the distractors fail:**
- **A** — supervised needs labeled input/output pairs (p. 7); reward signals aren't labels.
- **B** — unsupervised discovers structure in unlabeled data (p. 8); no reward.
- **D** — static regression doesn't "improve through repeated episodes."

---

## Q8 — LEO Earth-observer pointing drift with larger solar panels

**Answer: B** — Solar-radiation pressure acting over a larger illuminated surface area.

**Evidence from "Module 6c — Spacecraft Attitude Determination and Control Systems":**

- "The solar illuminated surface of the aircraft influences the amount of force against it. So, large solar panels will receive more force than a magnetometer boom." (p. 11)
- "When striking the spacecraft's surface, momentum is transferred. … The moment arm is calculated by T = F × d where F is the force on the surface and d is the distance from the center of mass. If d = 1 m, then T = 9 × 10⁻¹⁵ Nm. While small, the accumulation of these disturbances over time will result in a gradual increase in pointing error." (p. 11)
- "Despite being massless, photons have momentum." (p. 11)

**Key concepts:** photons carry momentum; SRP torque scales with illuminated area and moment arm; growing panel ⇒ growing steady-state drift, specifically *daytime* because SRP is zero in eclipse.

**Why the distractors fail:**
- **A** — negligible aerodynamic drag above ~400 km; wouldn't scale with solar-panel area.
- **C** — launch friction is a one-time input, not a drift.
- **D** — satellites in orbit don't run engines continuously; no "cruise thrust."

---

## Q9 — UAS collision-avoidance logic

**Answer: B** — ACAS Xu.

**Evidence from "Module 6c TCAS II & ACAS-X":**

- "ACAS X standard for Uncrewed Aircraft Systems (normal category)." (p. 27)
- "Functions include ensuring Collision Avoidance (CA) [and] Remain Well Clear (RWC)." (p. 27)
- "Provides remain well clear function. Resolution advisories in both the vertical and horizontal planes. Non-cooperative surveillance can support the resolution advisory logic. Automation enables ACAS Xu vehicles to automatically respond to a RA and then return to course once resolved (optional)." (p. 31)
- "Works for cooperative intruders (with transponders or ADS-B) and non-cooperative intruders." (p. 27)

**Why the distractors fail:**
- **A** — no automation, no horizontal RAs, no RWC.
- **C** — TCAS II lacks horizontal RAs and isn't certified for UAS.
- **D** — primary radar is sensing only; it has no avoidance logic.

---

## Q10 — Mode S lockout

**Answer: B** — Lockout after selective interrogation.

**Evidence:**

- "After All-Call, Mode S radar will only interrogate the known aircraft with the SELECT (Roll Call) interrogation. Lockout message sent with the first SELECT Message. Aircraft transponders lock out replies to the station's ALL Call interrogations until SELECT Message indicating lock out has ended." (ATCRBS & Mode S, p. 29)
- "Mitigate garbling by not having each aircraft respond to every all call. With less aircraft responding, there is less likelihood of garble." (p. 30)
- "Lock out aircraft that have responded with updates to avoid unnecessary replies to all-call." (p. 20)
- "Aircraft replies that are received without garble are considered 'locked' or 'acquired'." (p. 26)

**Why the distractors fail:**
- **A** — Gillham is an altitude-encoding scheme, unrelated to reply suppression.
- **C** — extended-squitter parity is an integrity-check feature of ADS-B broadcasts, not a suppression mechanism.
- **D** — higher output power doesn't suppress replies.

---

## Q11 — DAA Sensor Architecture (evidence bank)

**Sensors named in Modules 6a/6b:**

| Sensor | Cooperative? | Outputs | Course limitations |
|---|---|---|---|
| ADS-B | Yes | Position, velocity, altitude, ID at 1 Hz | Cooperative only; spoofable; GPS-dependent |
| Mode S transponder / TCAS | Yes (active) | Range, bearing, altitude | Cooperative only |
| Primary radar | No | Range, range-rate, azimuth, elevation | Weather, SWaP, small/non-metallic targets, ground reflections (Sensing, p. 11–12) |
| EO (visible) | No | Bearing, classification | Daylight, haze, sun glare; range ≈ 20 km clear (Sensing, p. 14, 16) |
| IR (thermal) | No | Bearing, thermal classification | Works at night & through obscurants; range ≈ 35 km clear |
| LiDAR | No | Range, bearing, trajectory | Eye-safety; "typically not suitable for aviation applications" (Sensing, p. 13) |
| Acoustic (e.g., TASA) | No | Bearing, classification | Noisy environments; short range |

**Swiss-cheese quote (verbatim):**

> "Detect and avoid sensing has been described as working with 'swiss cheese'. Sensors and tracking software might have 'holes' in its safety function. Detection limits can include, but are not limited to: range, minimum target size, minimum target velocity, altitude of ownship, altitude of intruder, etc. A goal of DAA sensor selection is to find the right layers of 'cheese' such that when stacked together no holes remain." *(Module 6a DAA Overview, p. 36.)*

"Understanding the limits of sensor types and creating a complimentary suite of sensors" is listed as a DAA challenge (DAA Overview, p. 35).

**Complementary pairings for the coastline scenario (haze / sun glare / rain):**
- ADS-B covers beyond-radar-horizon cooperative traffic but fails against non-cooperative / spoofed intruders → radar backs it up.
- Radar sees non-cooperative metal traffic through rain/haze but has SWaP cost, ground clutter, and small-target limits → EO/IR provides passive classification and fine bearing in clear air.
- EO gets blinded by sun glare and haze → IR still registers heat signature; radar still registers range.

---

## Q12 — Cybersecurity Scenario (evidence bank)

**ATC-level impacts of false ADS-B injection:**
- "False data injection can alter flight paths and impact air traffic control." (M7, p. 35)
- Fabricated targets clutter controller displays, drive unnecessary vectors, and mask real traffic.
- "Simulated attacks expose the effectiveness of robust data validation methods." (M7, p. 35)

**Onboard DAA / ACAS impacts:**
- Phantom traffic triggers unwarranted RAs and climb/descend maneuvers into actual traffic.
- "Collision Avoidance System — a system that produces directive guidance in the form of Resolution Advisories to avoid mid-air collision." (DAA Overview, p. 8–9) — the system treats spoofed ADS-B as real.
- "GPS spoofing can create 'ghost' aircraft or falsify navigation data." (M7, p. 34)
- Repeated false alerts erode automation trust and desensitize pilots to genuine alerts. "Pilot can choose to justifiably disregard a resolution advisory." (DAA Overview, p. 25)

**Mitigations named in M7 Cybersecurity deck (layered defense):**
1. **Sensor fusion / cross-validation** — "Cross-checking with additional sensors (e.g., radar, inertial navigation) is essential." (M7, p. 34). Correlate ADS-B reports with primary/secondary radar and multilateration before trust.
2. **Anomaly detection (algorithmic)** — "Advanced machine learning algorithms monitor for abnormal data patterns. Statistical models establish baselines of normal network behavior. Continuous learning improves detection accuracy over time." (M7, p. 37). Flags impossible kinematics, duplicated ICAO addresses, out-of-service-volume reports.
3. **Cryptographic authentication** — "Mitigation involves cryptographic signing of messages and anomaly detection." (M7, p. 34); "Apply state-of-the-art encryption (TLS/SSL) to secure data in transit … Deployment of strong authentication mechanisms for all critical data flows." (M7, p. 37)
4. **Procedural / backup surveillance** — "ADS-B Challenges: Malicious spoofing — Have backup surveillance systems such as Mode S." (ADS-B, p. 27)

**Why two layers beat one:** An attacker who defeats one layer (e.g., a convincing radio broadcast) still has to evade a *different-class* check (radar return, MLAT TDOA, or signed-message check). The layers are independent — failures of one aren't correlated with failures of the other — so the joint probability of a successful spoof drops multiplicatively. This is the same Swiss-cheese logic used for DAA (DAA Overview, p. 36).

---

## Q13 — Reaction wheels + magnetorquers (evidence bank)

**Reaction-wheel saturation:**
- "If the counter rotation of the reaction wheel becomes saturated: Torque in opposing direction causes wheel rotation to slow, which allows it to store additional momentum and torque. External actuation (e.g. thruster or magnetic torquer)" is required to desaturate. (Module 2c GNC, p. 7)
- "Provides torque about an axis commonly used for small satellite ADCS and desaturation of reaction wheels." (Module 6c ADCS, p. 4)

**Magnetorquer physics and role:**
- "Provide control torque motion in the plane perpendicular to the local external magnetic field and magnetic dipole. Magnetometer needed to measure local [magnetic] field. Alternative to using thruster to desaturate spinning wheel for larger satellite systems." (Module 2c GNC, p. 9)
- "Typically, a space vehicle will have three magnetic torquers orthogonal to one another along the x, y, and z axis." (Module 2c GNC, p. 9)
- **Formula:** "T = M × B, where T is the torque vector (N·m), M is the magnetic dipole field (A·m²), B is the external magnetic field (Tesla)." (Module 2c GNC, p. 9)

**Magnetorquer limitations (pick one for Q13):**
- **No field, no torque:** "For interplanetary travel, they are less useful due to a lack of a local external magnetic field." (Module 2c GNC, p. 9) — also weak at higher orbits (GEO).
- **Torque only perpendicular to B** — cannot produce torque along the field direction; attitude control is 2-of-3 axes at any instant and requires orbital motion to fill in the missing axis.
- **Weak torques** vs. thrusters — magnetorquers provide only slow desaturation.
- **Magnetometer contamination** — "Need to avoid interference from local magnetic field sources such as magnetic torquers and reaction wheels. Placement on boom." (Module 2c GNC, p. 12)

---

## Q14 — ADS-B vs Radar comparison (evidence bank)

**ADS-B is clearly better when:**
- BVLOS UAS operating beyond primary-radar coverage (remote, low-altitude, over-water). ADS-B yields identity + GPS-precision position even where radar has no line of sight.
- Cost-constrained deployments: "ADS-B System at airport is at least an order of magnitude cheaper than [radar] (e.g. $400 k to $4 M). Less maintenance, Lower cost set up." (ADS-B, p. 4)

**Radar is clearly better when:**
- A non-cooperative intruder is present — unequipped drones, gliders, birds, stealth targets. "Radar (Primary): Most versatile non-cooperative sensor." (Sensing, p. 11)
- GPS is denied/jammed — radar derives range from round-trip echo, independent of GNSS.

**ADS-B failure modes unique to ADS-B:**
- Spoofing / injection of false targets (no message authentication). (ADS-B, p. 28; M7, p. 9, 34)
- GPS jamming / spoofing upstream of the ADS-B transmitter — "GPS spoofing can create 'ghost' aircraft or falsify navigation data." (M7, p. 34)
- Equipage gaps — ADS-B is blind to unequipped traffic (Sensing, p. 28).

**Radar failure modes / limitations unique to radar:**
- Line-of-sight / terrain masking.
- "Weather impacts some frequencies" (Sensing, p. 12) — rain, heavy clutter.
- SWaP on small UAS — "Antenna volume/mounting. Computer volume and power. TRL 3-4 for smaller systems." (Sensing, p. 12)
- Limited range and small-target discrimination — "Declaration Range 3–8 nm"; "difficulty discriminating between local aircraft and other airborne phenomena (e.g. Birds)." (Sensing, p. 12, 24)
- No target identity.

**Neither alone is sufficient — Swiss cheese:** Module 6a, p. 36 (see Q11 quote) and "backup surveillance systems such as Mode S" (ADS-B, p. 27). ADS-B's blindness to non-cooperative traffic and its spoofability perfectly line up with radar's holes (LOS, weather, small targets, SWaP) — each covers the other's gap. DAA requires a complementary suite.

---

## Q15 — AI/ML Current Event (primary candidate)

**Primary citation:**
> GE Aerospace. "GE Aerospace Deploys AI-Driven Inspection Tool to Maximize Narrowbody Engine Time on Wing." Press release, GE Aerospace Newsroom, **February 13, 2025**. https://www.geaerospace.com/news/press-releases/ge-aerospace-deploys-ai-driven-inspection-tool-maximize-narrowbody-engine-time-wing

**Source type & trust:** Manufacturer press release — first-hand on what GE is doing, but motivated to emphasize benefits. It offers no benchmark, no false-positive/false-negative rates, no training-set composition. Trust it for *existence and scope of the program*, not *measured performance*.

**Application & problem:** Blade borescope inspection on CFM LEAP high-pressure turbine blades. AI guides technicians to the frames most likely to contain defects and standardizes defect calls, reducing inter-inspector variability and boosting time-on-wing for narrowbody engines.

**Evidence the source actually provides:** A named Chief MRO Engineer quote, a deployment count ("over a dozen" MRO facilities), precedent (GEnx widebody ~3 years earlier), and two headline numbers: "cuts inspection time roughly in half" and "improved accuracy." No dataset description, no confusion matrix, no cert basis.

**Likely ML paradigm + data needed:** Supervised deep learning for image classification / object detection on borescope frames. Training requires thousands of expert-labeled frames per blade region, balanced across LEAP variants (-1A/-1B/-1C), operators, climates, and borescope hardware; hold-out sets from airlines outside training.

**Source-supported conclusion (exact wording):** "GE Aerospace *claims in its February 13 2025 press release* that an AI-assisted borescope-inspection tool is in use at more than a dozen of its MRO shops and among CFM LEAP customers, guiding technicians on which images to review."

**Engineering inference (your own):** "The tool is almost certainly a supervised convolutional image model whose field performance is bounded by how representative its training images are of each customer's wear patterns; operators in high-particulate environments (desert, coastal) could see higher miss rates than the aggregate press number implies."

**Technical limitation:** Distribution shift across operators — the same generalization failure mode as Q6 on this exam. If training is dominated by GE's own shop visits, a customer with a different duty cycle can see degraded accuracy.

**Safety / ethical / certification concern:** The FAA has not yet published a settled means of compliance for learning-enabled maintenance decision-support. Automation bias is the live safety risk: technicians may stop scrutinizing frames the AI did not flag, shifting — not raising — the inspection floor. Liability chains between technician, MRO, GE, and operator remain unsettled for AI-missed findings.

**Course connections:**
- The AI+ML deck lists **"GE Aviation Predictive Maintenance"** and **"AI-Enhanced Inspection"** on p. 22 and "Preventative Maintenance" on p. 14 — this example is a present-day instance of exactly that slide.
- Ties to the deck's "Garbage In → Garbage Out / Lack of Diversity" warning (p. 5) and the Bias/Accountability/Safety ethics triad (p. 13).

**Backup candidate:** Reliable Robotics FAA-accepted certification basis for an autonomous flight system (trade-press corroborated, e.g., Flight Global 2024; Aviation Week 2024). Ties to DAA, ACAS Xu, and certification of learning-enabled components.

---

## Q16 — UAM Integrated Collision-Avoidance (evidence bank)

**Cooperative surveillance backbone:**
- ADS-B: 1 Hz position/velocity/altitude/ID broadcast to ATC and other aircraft (ADS-B, p. 2, 4).
- Mode S transponder with ICAO 24-bit address, pressure altitude in 25-ft increments, TCAS/ADS-B compatible, supports air-to-air interrogation (ATCRBS & Mode S, p. 2, 35; Sensing, p. 7).

**Non-cooperative layer (pick one or combine):**
- **Primary radar** — most versatile non-cooperative sensor; outputs range, range-rate, azimuth, elevation (Sensing, p. 11).
- **EO/IR** — passive, classification-capable; IR works at night/through obscurants (Sensing, p. 14, 16).
- **Acoustic arrays (TASA)** — short-range classification, aimed explicitly at UAM (Sensing, p. 17).

**ACAS Xu as integration logic:**
- Standard for UAS, issues RAs (CA) plus Remain-Well-Clear, vertical *and* horizontal, accepts non-cooperative sensor inputs, hybrid ADS-B + active surveillance. (Module 6c TCAS II & ACAS-X, p. 16, 27, 31)
- "RAs can be issued based only on ADS-B input. Condition: active surveillance must confirm the ADS-B values for position, altitude, etc. Failure to verify ADS-B message results in only using the active sensing method." (p. 31)
- Decisions via probabilistic MDP lookup table: minimum-expected-cost maneuver (p. 20–22).

**Human oversight modes (DAA Overview, p. 25):**
- Human-in-the-loop: pilot processes sensor data and commands the maneuver.
- Human-on-the-loop: DAA detects, pilot approves/overrides.
- Automated: DAA detects and acts; PIC is notified (and can override).
- "Pilot in command has final legal authority." ACAS Xu automates the RA response with optional return-to-course.

**Failure cases to handle:**
1. **Spoofed / lost ADS-B** — active surveillance (radar or air-to-air Mode S) overrides before a maneuver is commanded ("backup surveillance systems such as Mode S," ADS-B p. 27).
2. **GPS denial** — ADS-B becomes unreliable; primary radar and inertial/IMU take over (M7, p. 34).
3. **Sensor occlusion (weather, haze, glare)** — IR + radar still work when EO is blinded; Swiss-cheese layering (DAA Overview, p. 36).
4. **Non-cooperative intruder (bird, unequipped drone)** — radar and/or EO/IR pick it up where ADS-B cannot.

**Tradeoffs to defend (pick one):**
- **SWaP vs. capability:** radar adds weight/power/cost; accept it because single-sensor DAA fails against non-cooperative traffic (Sensing, p. 12).
- **False-alert rate vs. missed detection:** MDP cost function tunes thresholds; err toward missed false alarms in dense UAM to avoid nuisance RAs eroding trust — compensate with tighter crew-station displays.
- **Automation authority:** leaving override with PIC costs response time but preserves legal authority and handles sensor-fusion edge cases (DAA Overview, p. 25).
- **Cost vs. redundancy:** ADS-B is ~10× cheaper than radar (ADS-B, p. 4), tempting to drop radar; don't, because cooperative-only surveillance fails to the exact threats UAM must tolerate.
