Name: Gatlin Nelson
Student ID: 2636127

CEC 300 – Exam 2

---

Multiple Choice

1. **B.** Replace broad Mode A/C-style interrogation with Mode S selective interrogation and lockout. Overlapping replies ("garbling" or "fruit") come from many transponders answering the same all-call simultaneously; Mode S acquires each aircraft once, then addresses it individually by its 24-bit ICAO address via roll-call, and locks out further all-call replies from acquired aircraft. This attacks the root cause — reply simultaneity — while remaining backward-compatible with ATCRBS air/ground signaling [1].

2. **B.** Radar is still needed because ADS-B only reveals cooperative traffic, while radar can also detect non-cooperative intruders and help validate suspicious broadcasts. ADS-B depends on the intruder being equipped and truthfully broadcasting; an unequipped aircraft, bird, or spoofed target is invisible or misleading to ADS-B. A primary air-to-air radar is a non-cooperative sensor whose return can both reveal unequipped traffic and cross-check ADS-B reports before they drive a maneuver [2][3].

3. **B.** A time-to-collision or time-to-co-altitude threshold. TCAS II alerts on tau (τ), an estimate of time to closest point of approach rather than instantaneous distance, and uses separate tau thresholds for TA and RA that vary by altitude band. A geometry change (closure rate rising, vertical rate increasing) can push τ below the RA threshold even while measurable slant range remains [4].

4. **B.** Probabilistic decision-making and cost optimization, as used in the ACAS X family. ACAS X replaces TCAS II's deterministic rules with a probabilistic dynamics model, a probabilistic sensor model, and an offline-optimized lookup table (generated via a Markov decision process) that selects the minimum-expected-cost maneuver online [4].

5. **B.** It lacks strong built-in encryption and authentication for the broadcast message. ADS-B is an unauthenticated, unencrypted broadcast over a known waveform; anyone with a compatible transmitter can inject plausible traffic, and receivers (ATC and airborne) cannot intrinsically distinguish genuine reports from fabricated ones [3][5].

6. **B.** The model generalized poorly because the training data were biased, insufficiently diverse, or not representative of deployment conditions. ML performance is bounded by the distribution of the training set; a model trained on one airline's sensor quality and maintenance practices is not automatically valid on a heterogeneous fleet — this is the canonical distribution-shift / overfitting failure the course lists under "Lack of Diversity" and "Garbage In → Garbage Out" [6].

7. **C.** Reinforcement learning. The agent improves a policy through repeated simulation episodes, using penalties and rewards as the learning signal — exactly the paradigm defined in the course ("maximization of rewards and/or minimization of penalties," policy over states) [6].

8. **B.** Solar-radiation pressure acting over a larger illuminated surface area. Photons carry momentum; solar pressure produces a torque T = F·d whose magnitude scales with illuminated area (F) and moment arm (d). Adding larger solar panels increases both, and the disturbance accumulates specifically during daylight — precisely the observed symptom. There is no meaningful atmosphere, runway, or engine thrust in LEO cruise [7].

9. **B.** ACAS Xu. ACAS Xu is the ACAS X variant for UAS; it provides Remain-Well-Clear in addition to Collision Avoidance, issues Resolution Advisories in both vertical and horizontal planes, accepts non-cooperative sensor inputs (e.g., air-to-air radar per RTCA DO-360), and can automatically execute an RA and return to course [4].

10. **B.** Lockout after selective interrogation. Once the ground station has acquired an aircraft via a Mode S roll-call, the transponder is locked out from replying to that station's all-calls; only the addressed SELECT messages elicit further replies. This directly removes the redundant follow-on all-call replies from already-known aircraft [1].

---

Short Answer

### 11. DAA Sensor Architecture — BVLOS UAS near a hazy, glaring, rainy coastline

I propose a three-layer airborne architecture: (1) ADS-B IN, (2) a small air-to-air primary radar, and (3) an EO/IR dual-band camera.

**ADS-B IN** receives 1 Hz position, velocity, altitude, and ID from cooperative traffic — equipped manned aircraft and other ADS-B-Out UAS — at ranges well beyond the horizon [2]. Its limitation here is that it is blind to non-cooperative intruders (unequipped drones, gliders, birds) and to spoofed broadcasts. The **radar** fills both gaps: as a non-cooperative sensor it returns range, range-rate, and bearing regardless of target equipage [8], and independent radar tracks can corroborate or discredit suspicious ADS-B reports before they drive a maneuver.

**Radar** in turn struggles against small, low-RCS targets, suffers ground-return clutter over a coastline, and carries a real SWaP cost on a small UAS [8]. The **EO/IR camera** compensates: EO provides high angular resolution for classification in clear daylight (~20 km), and IR sees through haze and persists at night via thermal contrast (~35 km) [8].

**EO/IR** itself is defeated by direct sun glare in the visible band and heavy rain in both; in those conditions the radar's RF return is unaffected by optical obscurants, and ADS-B remains weather-agnostic.

Each sensor has holes; the holes are offset. Stacking three dissimilar detection physics (cooperative RF broadcast, active RF echo, passive optical) is the Swiss-cheese principle applied to DAA — no single environmental or adversarial failure blinds the whole system [9].

### 12. Cybersecurity Scenario — False ADS-B targets near a busy airport

**ATC-level impact.** Injected ghost tracks populate the controller display as if they were legitimate aircraft. The controller must either issue vectors around phantoms — wasting airspace and time — or risk masking a real converging aircraft among the chaff. Either response degrades situational awareness and raises workload during the peak period the attack was timed to exploit [5].

**Onboard DAA / ACAS impact.** Airborne TCAS/ACAS systems treat a spoofed extended-squitter as real traffic; a well-placed ghost can trigger an unnecessary Resolution Advisory, forcing a climb or descent into airspace that was clear. Even when the spoof is eventually unmasked, the cumulative false-alarm rate erodes pilot trust in the automation and desensitizes crews to the next genuine RA [4][5].

**Mitigation 1 — Sensor cross-validation (physical layer).** ATC and airborne systems correlate each ADS-B report against independent measurements: secondary radar range/azimuth, multilateration (TDOA on the 1090 MHz signal across ≥3 ground receivers), and — onboard — air-to-air primary radar. A spoofer would have to simultaneously fake an RF echo and a geometrically consistent TDOA fingerprint, which is far harder than broadcasting a message [5].

**Mitigation 2 — Anomaly detection and authentication (algorithmic / protocol layer).** Statistical monitors flag kinematically impossible tracks, duplicated ICAO addresses, out-of-service-volume reports, and sudden position jumps; the longer-term fix is cryptographically signed squitters so receivers can reject unsigned or wrongly signed messages outright [5].

The two mitigations are at different layers and fail independently. A spoofer who defeats the physical check (somehow syncing a fake return) still has to defeat signed-message validation; an attacker who forges signatures still has to produce a consistent physical echo. Combined, they drop attack success multiplicatively — the same layered-defense logic the course applies to DAA [9].

### 13. Spacecraft Control — Reaction wheels + magnetorquers on a small satellite

Reaction wheels produce fine pointing by exchanging angular momentum with the spacecraft body, but external disturbance torques (solar-radiation pressure, atmospheric drag, gravity gradient) continuously pump momentum *into* the wheels. Each time the wheel spins up to counteract a disturbance, it stores a little more angular momentum. Eventually it hits its maximum speed and saturates — it can no longer absorb additional torque in that direction, and pointing authority is lost [10].

Magnetorquers provide the off-loading path. A current-carrying coil inside the satellite generates a magnetic dipole **M**; interacting with Earth's local magnetic field **B** produces a torque **T = M × B**. By driving **M** in the right direction, the ADCS can bleed stored momentum out of the reaction wheels over an orbit or two — "momentum dumping" — without spending propellant. Three orthogonal coils give 3-axis capability. This works in LEO precisely because Earth's B-field is strong enough there to deliver useful torque [7][10].

The key operational limitation is that **T = M × B** is always perpendicular to **B**: you cannot produce torque along the field direction at a given instant, so the ADCS must wait for orbital motion to rotate **B** through all axes. Torque is also weak compared to thrusters, so desaturation is slow, and the method fails entirely where no ambient field exists (interplanetary cruise, deep space) [10].

### 14. Surveillance-System Comparison — ADS-B vs radar around a BVLOS UAS

**Where ADS-B is clearly better:** Long-range, beyond-radar-horizon encounters at low altitudes over remote terrain. ADS-B delivers identity, GPS-precision position, and velocity at 1 Hz from any equipped aircraft within radio line of sight, long before a small air-to-air radar could detect it, and at roughly an order of magnitude lower equipment cost [2].

**Where radar is clearly better:** Any encounter with a non-cooperative intruder — an unequipped drone, a glider, a transponder failure, or a malicious target. Radar derives range and bearing directly from the reflected echo and does not depend on the intruder broadcasting anything [8].

**Failure mode unique to ADS-B:** Spoofing. ADS-B messages are unauthenticated and unencrypted; a commodity transmitter can inject plausible ghost traffic that receivers cannot tell from real broadcasts. Upstream GPS jamming or spoofing also corrupts ADS-B position reports without the broadcaster being aware [3][5].

**Failure mode unique to radar:** Line-of-sight and weather. Terrain masking hides targets below the horizon or behind obstructions; rain and ground clutter degrade some frequency bands; and SWaP constraints on a small UAS limit antenna aperture, range (typically 3–8 nmi declaration), and small-target discrimination (e.g., birds) [8].

Neither system alone is sufficient for robust DAA. The course's Swiss-cheese principle explicitly requires complementary sensors so that one's detection holes are covered by another's [9]. ADS-B's blind spots (non-cooperative, spoofed) align precisely with radar's strengths, and radar's blind spots (beyond-LOS, SWaP-limited range) align with ADS-B's strengths. A layered ADS-B + radar architecture is the minimum viable DAA sensor suite.

---

### 15. AI/ML Current Event — AI-driven borescope inspection on CFM LEAP engines

**Citation.** GE Aerospace, "GE Aerospace Deploys AI-Driven Inspection Tool to Maximize Narrowbody Engine Time on Wing," press release, 13 February 2025 [11].

**Source type and trust.** This is a manufacturer press release. GE is both the technology vendor and a beneficiary of the narrative, so the source is reliable for *what program exists* and unreliable for *how well it performs*. It offers no benchmark, no false-positive/false-negative rates, no training-set description, and no third-party validation. I treat its existence claims as factual and its performance claims ("cuts inspection time roughly in half," "improved accuracy") as marketing headlines, not evidence.

**Application and problem.** The tool assists borescope technicians inspecting the hot section of CFM LEAP narrowbody engines. It flags which frames to review and standardizes defect calls, targeting the inter-inspector variability that drives both missed findings and unnecessary teardowns. The business driver is time-on-wing: every avoided shop visit matters for an airline on a LEAP.

**Evidence the source actually provides.** A named executive (Chief MRO Engineer) quote, a deployment count ("over a dozen" MRO facilities plus CFM customers), a precedent on the GEnx widebody, and two unverified numbers (≈50% inspection time reduction; "improved accuracy"). No dataset composition, no confusion matrix, no cert basis, no independent benchmark.

**ML paradigm and data needed.** Almost certainly supervised deep learning for image classification and/or object detection on borescope frames — the exact aviation-CV use case flagged in the AI/ML module [6]. Adequate training data would include tens of thousands of expert-labeled frames per blade region, balanced across LEAP variants (-1A/-1B/-1C), climates, duty cycles, borescope operators, and imaging hardware, with hold-out validation on airlines not in training.

**Source-supported conclusion vs. my engineering inference.** *Supported by the source:* GE has deployed an AI-assisted borescope-inspection tool to more than a dozen MRO shops and CFM LEAP customers as of Feb 2025 [11]. *My inference (going beyond the source):* The tool is a supervised CV model whose field accuracy is bounded by how representative its training images are; an operator in a high-particulate environment (desert, coastal) could see worse miss rates than the aggregate number implies, because the training pool is almost certainly skewed toward GE's own shop visits.

**Technical limitation.** Distribution shift across operators — the same generalization failure mode tested in Question 6. "Excellent on historical data, worse on the real fleet" is the default CV failure when the training distribution doesn't cover the deployment distribution [6].

**Safety / certification concern.** The FAA has not yet published mature means-of-compliance guidance for learning-enabled maintenance decision-support; the live FAA posture is bounded, monitored, auditable use. The concrete safety risk is automation bias: a technician who trusts the tool may stop scrutinizing the 99% of frames it did *not* flag, shifting the inspection floor rather than raising its ceiling. The accountability chain between technician, MRO, GE, and the operator is not settled for an AI-missed finding.

**Course connection.** The AI/ML module names GE Aviation predictive maintenance and AI-enhanced inspection as exemplar aviation use cases and lists preventative maintenance as a core application [6]. This deployment is a present-day instance of that slide, and it exercises the deck's warnings about data diversity, generalization, and the bias/accountability/safety ethics triad.

---

### 16. Integrated System Design — Layered Collision Avoidance for Urban Air Mobility

**Architecture.** A UAM aircraft operating near conventional traffic carries four concentric layers: cooperative surveillance (ADS-B IN/OUT plus a Mode S transponder with 1090ES extended squitter), non-cooperative sensing (a compact air-to-air primary radar as the primary, backed by an EO/IR dual-band camera for classification), an ACAS Xu avoidance-logic core, and a human oversight interface for the remote pilot.

**Information flow.** ADS-B IN supplies cooperative tracks with identity and GPS-precision state at 1 Hz, out to radio line of sight [2]. The Mode S transponder broadcasts ownship state for ATC, for nearby TCAS/ACAS, and for air-to-air interrogation, and can itself perform air-to-air Mode S for redundancy [1]. The radar generates non-cooperative tracks (range, range-rate, azimuth, elevation) that the fusion engine correlates with ADS-B; EO/IR narrows bearing and classifies ambiguous returns [8]. All tracks feed ACAS Xu, which uses its probabilistic dynamics and sensor models, along with an offline-optimized MDP lookup table, to compute both a Remain-Well-Clear guidance cue and, if the encounter escalates, a vertical or horizontal Resolution Advisory [4].

**Human oversight.** The remote pilot runs human-on-the-loop for routine Remain-Well-Clear events — the system displays the recommended maneuver and the pilot approves (or amends) before it executes. Inside the CA threshold, ACAS Xu switches to automated mode: it issues and begins executing the RA within the TA-to-RA tau budget and notifies the pilot concurrently, who retains override authority consistent with PIC responsibility [4][9].

**Failure case 1 — Spoofed or lost ADS-B.** ACAS Xu is configured so that an RA may be issued from ADS-B alone only if active surveillance (radar or air-to-air Mode S) corroborates the report; otherwise it falls back to active sensing [4]. A spoofer who injects a ghost track sees no radar echo and no Mode S reply, so the logic discards the track rather than maneuvering. If ADS-B is lost entirely (jamming), the radar + Mode S + EO/IR stack continues to provide separation [3].

**Failure case 2 — GPS denial.** Ownship GPS loss degrades ADS-B outputs across the entire cooperative layer. The design mitigates this by navigating on INS/altimeter for short-term state, continuing to transmit Mode S without ADS-B position validity flags, and relying on radar-derived relative geometry for avoidance. Remain-Well-Clear margins are automatically widened in degraded-mode, reflecting increased state-estimate uncertainty [5].

**Tradeoff I intentionally accept.** I carry the SWaP, cost, and integration burden of a small radar on a UAM vehicle even though ADS-B would be ~10× cheaper to equip [2] and is adequate in fully-equipped airspace. The reason is structural: the attack surface and equipage gap the course explicitly warns about — non-cooperative intruders, ADS-B spoofing, GPS denial — all fail in the direction ADS-B *alone* cannot recover from [3][5][9]. Saving radar cost buys a sensor suite whose holes are all correlated (everything downstream of a single RF broadcast chain). Paying the radar cost buys uncorrelated failure modes — the only architecture that preserves separation in the two most plausible UAM failure cases. The SWaP penalty is a predictable engineering cost; the correlated-failure alternative is not.

---

References

[1] CEC 300. "CEC 300 – ATCRBS and Mode S Transponders," Florida Institute of Technology, 2025.
[2] CEC 300. "CEC 300 – ADS-B," Florida Institute of Technology, 2025.
[3] CEC 300. "CEC 300 – M7 – Cybersecurity in Aviation and Aerospace," Florida Institute of Technology, 2025.
[4] CEC 300. "Module 6c – TCAS II and ACAS-X," Florida Institute of Technology, 2025.
[5] CEC 300. "CEC 300 – M7 – Cybersecurity in Aviation and Aerospace," Florida Institute of Technology, 2025. (ADS-B spoofing, authentication, anomaly-detection discussion.)
[6] CEC 300. "AI + ML in Aviation and Aerospace," Florida Institute of Technology, 2025.
[7] CEC 300. "Module 6c – Spacecraft Attitude Determination and Control Systems," Florida Institute of Technology, 2025.
[8] CEC 300. "Module 6b – Sensing," Florida Institute of Technology, 2025.
[9] CEC 300. "Module 6a – DAA Overview," Florida Institute of Technology, 2025.
[10] CEC 300. "Module 2c – Spacecraft GNC Elements," Florida Institute of Technology, 2025.
[11] GE Aerospace, "GE Aerospace Deploys AI-Driven Inspection Tool to Maximize Narrowbody Engine Time on Wing," press release, GE Aerospace Newsroom, 13 Feb. 2025. URL: https://www.geaerospace.com/news/press-releases/ge-aerospace-deploys-ai-driven-inspection-tool-maximize-narrowbody-engine-time-wing (accessed 2026-04-22).
