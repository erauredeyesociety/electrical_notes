# CEC 300 – Exam 2 (Verbatim)

**Instructions:** Answer each question to the best of your ability in your own words and without the use of online AI tools (e.g. ChatGPT). If you reference material outside of the course material, include the reference and provide an in-line citation within your text.

---

## Multiple Choice (2 pts each)

### 1. Overlapping transponder replies at a Class B airport
At a Class B airport, controllers report frequent overlapping transponder replies when many aircraft enter the terminal area at once. Which change most directly attacks the root cause while preserving compatibility with existing SSR operations?

- **A.** Increase interrogation power so valid replies dominate the overlap.
- **B.** Replace broad Mode A/C-style interrogation with Mode S selective interrogation and lockout.
- **C.** Increase interrogation frequency so missed replies are recovered more quickly.
- **D.** Stop requesting altitude during peak periods to shorten each reply.

### 2. BVLOS UAS radar vs ADS-B IN
A BVLOS UAS carries ADS-B IN and a small air-to-air radar. A teammate argues that the radar should be removed because ADS-B already provides traffic information. Which response is the strongest engineering rebuttal?

- **A.** Radar is unnecessary because ADS-B already guarantees collision avoidance.
- **B.** Radar is still needed because ADS-B only reveals cooperative traffic, while radar can also detect non-cooperative intruders and help validate suspicious broadcasts.
- **C.** Radar is still needed because ADS-B cannot provide altitude information.
- **D.** Radar is still needed because TCAS only works when primary radar is available.

### 3. TCAS II Resolution Advisory trigger
Two aircraft are converging. TCAS II remains quiet until the encounter geometry changes, after which a Resolution Advisory appears even though the aircraft are still separated by a measurable distance. What most likely crossed the decision boundary?

- **A.** Loss of ADS-B reception.
- **B.** A time-to-collision or time-to-co-altitude threshold.
- **C.** Loss of primary-radar tracking on the ground.
- **D.** Manual pilot override of the transponder.

### 4. Probabilistic collision-avoidance design
A design review describes a collision-avoidance system that evaluates several candidate maneuvers and selects the action with the lowest expected cost using probabilistic models of aircraft motion and sensor uncertainty. Which improvement over TCAS II does this most directly describe?

- **A.** Higher interrogation power.
- **B.** Probabilistic decision-making and cost optimization, as used in the ACAS X family.
- **C.** Removal of transponder dependence.
- **D.** Elimination of vertical advisories.

### 5. Spoofed ADS-B threat property
Which property of ADS-B most directly makes spoofed or fabricated traffic reports a believable threat to operators and automation?

- **A.** It depends on air-ground radar coverage.
- **B.** It lacks strong built-in encryption and authentication for the broadcast message.
- **C.** It can only operate above 18,000 feet.
- **D.** It transmits too slowly to support surveillance.

### 6. Predictive maintenance model failure
A predictive-maintenance model shows excellent performance on historical data from one airline but performs poorly after deployment across a mixed fleet with different sensor quality and maintenance practices. Which explanation is most convincing?

- **A.** The model had too much training data.
- **B.** The model generalized poorly because the training data were biased, insufficiently diverse, or not representative of deployment conditions.
- **C.** The aircraft used too many sensors during deployment.
- **D.** The system should have used reinforcement learning instead of any other ML method.

### 7. Reward/penalty learning paradigm
An autonomous flight agent improves through repeated simulation episodes by receiving penalties for unsafe choices and rewards for desirable trajectories. Which learning paradigm does this describe?

- **A.** Supervised learning from labeled examples.
- **B.** Unsupervised clustering.
- **C.** Reinforcement learning.
- **D.** Static regression only.

### 8. LEO Earth-observer pointing drift
A small Earth-observing satellite in low Earth orbit shows a gradual daytime pointing drift that grows when larger solar panels are installed. Which disturbance best explains that specific symptom?

- **A.** Wind gusts from the atmosphere.
- **B.** Solar-radiation pressure acting over a larger illuminated surface area.
- **C.** Runway-friction asymmetry from launch.
- **D.** Engine-thrust imbalance during cruise.

### 9. UAS collision-avoidance system choice
A UAS program needs collision-avoidance logic that can support horizontal guidance, automated response, and remain-well-clear functions in mixed encounters. Which system concept is the best fit?

- **A.** Mode C with manual ATC coordination only.
- **B.** ACAS Xu.
- **C.** TCAS II with no modifications.
- **D.** Primary radar alone.

### 10. Mode S feature reducing unnecessary replies
After a ground station has already acquired nearby aircraft, which Mode S feature most directly reduces unnecessary follow-on replies from those aircraft to future all-call interrogations?

- **A.** Gillham altitude encoding.
- **B.** Lockout after selective interrogation.
- **C.** Extended-squitter parity only.
- **D.** Higher transponder output power.

---

## Short Answer

### 11. [10 pts] DAA Sensor Architecture
*Recommended response: 175–250 words.*

A BVLOS UAS must operate in mixed airspace near a coastline where haze, sun glare, and occasional rain are common. Propose a three-sensor airborne or mixed architecture. For each sensor, explain what class of intruder it can detect, one limitation in this environment, and how another sensor in your design covers that limitation. End with one sentence explaining why your architecture reflects a layered 'Swiss cheese' approach.

### 12. [10 pts] Cybersecurity Scenario
*Recommended response: 175–250 words.*

An attacker injects false ADS-B targets near a busy airport. Explain two different ways the attack could distort human or automated decision-making—one at the ATC level and one at the onboard DAA or ACAS level. Then propose two mitigations that operate at different layers (for example, sensor validation, networking, procedures, or authentication) and explain why using both is stronger than using only one.

### 13. [10 pts] Spacecraft Control
*Recommended response: 125–200 words.*

A small satellite uses reaction wheels for fine pointing. Explain why magnetorquers are often added even when the wheels already provide precise control. Your answer must mention wheel saturation, the role of Earth's magnetic field, and one operational limitation of magnetorquers.

### 14. [10 pts] Surveillance-System Comparison
*Recommended response: 150–225 words.*

Compare ADS-B and radar for detecting traffic around a BVLOS UAS. Your answer must include one situation where ADS-B is clearly better, one situation where radar is clearly better, one failure mode unique to ADS-B, and one failure mode or limitation unique to radar. End by stating whether either system alone is sufficient for robust DAA and justify your answer.

---

## Essays

### 15. [20 pts] AI/ML Current Event Analysis
*Suggested response: 350–500 words.*

Find a real-world example from 2023 to the present involving AI or ML in aviation or aerospace. Use the source as evidence, not just as a topic. Your response must:

- provide a full citation and publication date;
- identify the type of source (for example, research paper, company press release, journalism, regulator notice, or technical report);
- explain how that source type affects how much trust you place in it;
- summarize the application and the problem it is trying to solve;
- identify what evidence the source actually provides;
- explain what ML paradigm is most likely involved and what data would be needed;
- clearly separate one conclusion supported directly by the source from one engineering inference of your own;
- evaluate one technical limitation and one safety, ethical, or certification concern;
- and connect the example to at least one concept from this course.

### 16. [20 pts] Integrated System Design
*Suggested response: 350–500 words.*

Design a layered collision-avoidance architecture for future urban air mobility operations near conventional traffic. Your response must integrate transponders, ADS-B, at least one non-cooperative sensing method, and ACAS Xu or equivalent UAS-oriented avoidance logic. Explain how information flows through the system, how human oversight interacts with automation, and how your design handles at least two failure cases. End by defending one tradeoff you intentionally accepted.
