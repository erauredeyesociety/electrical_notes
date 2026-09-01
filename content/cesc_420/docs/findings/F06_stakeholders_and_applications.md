# F06 · Stakeholders and Applications

Fixes the proposal's weakest section. Stakeholders is **10% of the proposal, rising to 13%** if the budget clause is invoked — for about three-quarters of a page, **the highest points-per-effort section in the document**. It currently scores near zero.

Related: [`../../proposal/PROPOSAL_GAP_ANALYSIS.md`](../../proposal/PROPOSAL_GAP_ANALYSIS.md) · [F05](F05_standards_and_regulations.md) · [F03](F03_air_ground_integration.md)

---

## What went wrong, and where the content should go

The draft says *"Primary stakeholders: Equal share amongst all stakeholders, 25%."* That is a **responsibility/ownership split**, not a stakeholder list.

**The content isn't wasted — it just has the wrong home.** Move it to a RACI or work-package table in the project-management portion of the proposal. It is the evidence for ABET outcome (5) (*function effectively on a team … plan tasks, meet objectives*), and the peer-evaluation deliverable will ask about it anyway. Relocating recovers the 10% while keeping the record.

---

## The definitions — and a trap

**Open the section with this**, quoted from ISO/IEC/IEEE 15288:

> A stakeholder is an *"individual or organization having a right, share, claim, or interest in a system or in its possession of characteristics that meet their needs and expectations."*

Quoting it immediately signals the team knows "stakeholder" is a systems-engineering term of art, not a division of team ownership.

> ⚠ **The trap:** neither ISO/IEC/IEEE 15288 nor 29148 defines "primary stakeholder" or "secondary stakeholder." That split comes from **management stakeholder theory (Clarkson 1995)** and **HCI/requirements classification (Eason 1988)**. Do not claim an ISO source for it. Citing Clarkson or Eason is both honest and more impressive than a fake standards citation.

| Source | Test |
| --- | --- |
| **Clarkson (1995)** | Primary = *"one without whose continuing participation the corporation cannot survive as a going concern."* → **If this party withdrew tomorrow, would X_swarm stop?** |
| **Eason (1988)** | primary (use it directly) / secondary (receive outputs or supply inputs) / tertiary (affected by its introduction) / **facilitating** (design, build, maintain it) — defined by interaction with the artifact, so best suited to a design project |
| **Freeman (1984)** | *"can affect or is affected by"* — the two-way sweep test for finding stakeholders you'd otherwise miss |

**The one rule to state and apply consistently:**

> A **primary** stakeholder interacts with the system or its direct outputs as part of their own work, or the project cannot proceed without their continuing participation. A **secondary** stakeholder never touches the system but constrains it, governs it, funds the environment it runs in, or inherits its consequences.

*One stated rule applied consistently beats a longer list applied inconsistently.*

**Pre-empt the obvious objection:** "primary" does not mean "most important." A regulator is usually secondary yet can veto the entire system — which is why Mitchell, Agle & Wood (1997) score stakeholders on power, legitimacy and urgency instead. Add one clause noting this when listing the FCC or a safety officer as secondary.

**Why the section is worth 10%,** in SEBoK's words: *"Stakeholders are the primary source of needs and requirements"* and *"leaving out a relevant stakeholder often results in missing needs and requirements and a failure to pass system validation."* It is the input to the SRS and Test Plan — the next two graded deliverables.

---

## Recommended structure

Five blocks, in this order:

1. **Two-line framing** — the ISO 15288 definition + the primary/secondary rule being applied.
2. **Stakeholder register table** (below).
3. **Primary** subsection — 3–6 entries.
4. **Secondary** subsection — 4–8 one-line entries.
5. **Application-domain stakeholders** of the technology itself.

Headings that match the rubric prompts mean the grader can find both required lists without hunting.

### The register table — five columns

| Stakeholder | Class | Role (ISO terms) | What they need | How we verify |
| --- | --- | --- | --- | --- |
| … | primary/secondary | acquirer, user, operator, regulator, approving authority, inheritor | … | forward ref to a requirement or test ID |

**The fifth column is the highest-value trick in the section.** It makes the stakeholder table the documented seed of the SRS and System Test Plan — exactly the traceability those later rubrics reward.

Add one sentence naming the **identification method** (a SEBoK life-cycle-stage walk, or Sharp et al.'s four-baseline seed of *users / developers / legislators / decision-makers*) and one committing to **periodic re-review**. Method plus cadence is process evidence, and process is what separates a well-graded capstone document from a list.

**Name the approving authorities explicitly in one labelled sentence.** SEBoK singles these out as the class teams most often collapse into "the customer," and warns *"it cannot be assumed that the only stakeholder that has this authority is the 'customer.'"* Here there are three: **the instructor** (grade acceptance), **the mentor** (technical acceptance), **the lab manager** (flight authorization).

**Length:** ¾–1 page plus the table. Every entry carries a stated need; entries with a name but no need should be deleted. A 10–13% section that runs three pages steals time from the 45% Proposed Solution.

---

## The stakeholder set

### Primary

| Stakeholder | Role | Need |
| --- | --- | --- |
| **Dr. Juan Calderon Chavez** | customer / acquirer | Defines the technical need, owns the hardware, accepts the delivered system |
| **Dr. Fan Yang** | approving authority, grader | Deliverables satisfying the published templates |
| **The four team members** | developers (Eason "facilitating") + graduating students | A demonstrable system and a defensible design record |
| **Lab manager / equipment custodian** | operator of the shared resource | Safe, scheduled, accountable use of the flight volume |

Naming a **single customer** is the strongest signal the team has a real requirements source rather than a self-invented project.

The lab manager is primary under Clarkson's test: **withdrawal of access halts the project outright.** Given the hardware-first Semester 1 preference, lab access is the largest schedule risk ([R-06](../05_risk_register.md)), and naming it as a stakeholder makes that risk visible in the proposal.

**Conditional:** if the mentor's swarm work carries external grant funding, **the sponsoring agency is primary** under Clarkson, and may impose publication, data-sharing or export-control obligations. An unnamed sponsor is a classic source of surprise constraints mid-project. **One email to ask** — this is the highest-value unknown in the section.

### Secondary

- **ABET** — the capstone is the accreditation-mandated *"culminating major engineering design experience that 1) incorporates appropriate engineering standards and multiple constraints, and 2) is based on the knowledge and skills acquired in earlier course work"* (Criterion 5). **Quoting Criterion 5 verbatim explains to the grader why the proposal must cite standards at all** — tying this section to the Proposed Solution's standards prompt.
- **The EECS department and its assessment process** — Criterion 2 requires a documented periodic-review process involving program constituencies. This is the precise reason capstone artifacts are archived.
- **Future capstone teams and lab researchers** who inherit the codebase, hardware configuration and calibration procedures. Their need is reproducible documentation, a working repository, and a known-good setup procedure. **Naming inheritors converts "write good documentation" from a nice-to-have into a traceable stakeholder requirement the Test Plan can verify.**
- **Other users of the same lab** — they share the 2.4 GHz band and the physical flight volume, so operations are mutually interfering. This is simultaneously a stakeholder relationship and a hard technical constraint on channel allocation and scheduling ([F04](F04_network_and_latency.md)), so it strengthens two sections at once.
- **University EH&S / risk management** — indoor flight safety (netting, standoff, eye protection) and LiPo charging/storage policy. **The cheapest available evidence for ABET outcome (2)'s "public health, safety, and welfare" clause.**
- **The FCC** — for the 2.4 GHz links ([F05](F05_standards_and_regulations.md)).

> **The FAA is *not* a stakeholder if all flight is indoors**, because Part 107 governs operations in the National Airspace System and indoor flight sits outside it. **Explicitly stating why the FAA does not apply is a more sophisticated move than reflexively listing it** — but it is only correct if the scope section commits to indoor-only flight.

ABET Criterion 3 outcome (2) requires design *"with consideration of public health, safety, and welfare, as well as global, cultural, social, environmental, and economic factors"* — a list that is itself a stakeholder taxonomy, and one the application-domain stakeholders below map onto directly.

### Failure modes to avoid

Listing "society" or "the public" with no stated need · listing a stakeholder without saying what they need · **conflating the team's internal work split with the stakeholder list** (already committed) · omitting the inheritors · omitting the approving authorities.

---

## Why a heterogeneous team beats a single robot

**Name the mechanism per domain rather than asserting "swarms are better."** Five separately citable mechanisms — this also serves the Problem Statement's 24%:

| # | Mechanism | Evidence |
| --- | --- | --- |
| 1 | **Complementary mobility and viewpoint** | CERBERUS (DARPA SubT winner) deployed aerial robots specifically to *"explore spaces too narrow or otherwise unreachable by ground systems"*, alongside ANYmal legged robots chosen for endurance and terrain |
| 2 | **Endurance sharing** | UGVs as mobile recharging stations rendezvousing with battery-limited UAVs, converting short flight time into persistent coverage |
| 3 | **Communications relay** | A 2025 mine-inspection deployment used a mobile Wi-Fi mesh for multi-agent operation with minimal fixed infrastructure |
| 4 | **Sensing/compute asymmetry** — *with a documented cost* | Globally registering UGV lidar clouds against UAV vision-derived maps is itself an open research problem in disaster response |
| 5 | Parallel coverage with graceful degradation | — |

**Mechanism 2 is the most concrete stakeholder-visible reason the ground robots must be in the architecture at all**, given a 7-minute Crazyflie flight time.

**Mechanism 4 is worth citing carefully:** it makes the team's "differing localization frames" constraint a *literature-backed difficulty* rather than a guess, and justifies scoping frame unification as explicit Semester 1 work ([IR-03](../01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems)).

---

## Application domains

**Claim only two or three.** Claiming ten reads as padding; claiming two the testbed actually models reads as engineering judgment — and protects the Proposed Solution's scope statement from contradicting itself.

**Recommended two**, because every other domain requires outdoor flight that has been scoped out:

### 1. GPS-denied interior search — USAR and subterranean

Operators: FEMA/state urban search-and-rescue task forces, local heavy-rescue teams, mine rescue teams, mine operators, MSHA/NIOSH.

Advantage: parallel void search inside a collapse under a time-critical survival window — aerial agents map the rubble exterior for entry points while ground agents penetrate voids; in mines, ground robots anchor the relay while aerial agents penetrate shafts.

**This is the domain with the strongest published evidence for heterogeneous air-ground teaming** (CERBERUS, the mine deployment), and it is GPS-denied and indoor-like — so it most honestly analogizes to a Lighthouse-positioned indoor Crazyflie testbed.

Standards hook: **NIST Standard Test Methods for Response Robots**, standardized through **ASTM Committee E54.09**, cover ground *and* aerial platforms across mobility, sensors, energy, communications and safety, sponsored by DHS S&T, DOJ, ARL and DARPA. A named standards body with named agency stakeholders for exactly this technology — **and it also answers the Proposed Solution's "what standards drive the solution?" prompt.**

### 2. Warehouse and inventory

Operators: warehouse operations managers, third-party logistics providers.

Advantage: full-facility cycle counting overnight instead of sampled manual counts — drones read high-rack labels that otherwise need a lift truck, while floor AMRs provide docking, charging, and a localization anchor.

**Indoor, GPS-denied, fiducial-marked, infrastructure-assisted — the closest commercial analog to a Lighthouse-plus-ArUco testbed.** The demo maps onto it with the least hand-waving.

### Others — one line each, as motivation only

| Domain | Sizing figure | Note |
| --- | --- | --- |
| Infrastructure / bridge inspection | FHWA 2024 NBI: **623,218 bridges; 42,080 (6.8%) Poor, 306,279 (49.1%) Fair** | Simultaneous underside (air) + deck (ground) capture in one closure window |
| Wildland fire | NIFC 2024: **64,897 fires, 8,924,884 acres** (10-yr avg 64,979 / 7,657,589) | **Outdoor — frame as motivation, not a deliverable** |
| Disaster damage assessment | — | Its unsolved core (cross-modal map registration) *is* the team's Semester 1 frame-unification problem |
| Precision agriculture | — | Aerial scouting + ground in-canopy verification |
| Military / defense ISR | DARPA OFFSET targeted swarms of **250+ UAS/UGS** | ⚠ Check export control (ITAR/EAR) and institutional policy before leaning on this |
| Construction progress monitoring | — | Weakest quantitative evidence; one line at most |

---

## ⚠ Unverified — do not cite until checked

The research pass flagged these as retrieved-but-unconfirmed or blocked. **Verify before any appears in the proposal:**

- **FEMA National US&R task force count** — believed 28 federal task forces, **not verified** (fema.gov returned HTTP 403).
- **National Bridge Inspection Standards routine interval** — believed up to 24 months under 23 CFR 650 Subpart C, **not verified**.
- **Commercial warehouse-drone performance figures** (Verity, Corvus Robotics) — scans/night, count accuracy. No extractable vendor numbers found.
- **USDA precision-agriculture adoption percentages** — ERS page 404'd.
- **USFS / DOI UAS mission counts and fleet size** — agency pages returned no statistics.

The FHWA bridge figures and NIFC wildfire figures *were* verified against primary sources and are safe to cite.

---

## Open questions

1. **Does the mentor's swarm research carry external grant or sponsor funding?** Highest-value unknown here — changes the primary stakeholder list and may add publication or export-control constraints.
2. Who is the lab manager / equipment custodian, and what is the actual flight-volume booking procedure?
3. **Does CESC capstone have an industry advisory board, external poster-showcase reviewers, or a formal design-review panel?** Any of these are stakeholders unknowable from the rubric. Ask Dr. Yang.
4. ERAU's program-specific ABET outcome mapping — which deliverable is evidence for which outcome?
5. Is there a written departmental policy on capstone code, hardware return, and inheritance by future teams?
6. **Will any part of the project fly outdoors?** If yes, the FAA becomes a regulator stakeholder and this analysis changes. If no, **say so explicitly in the scope section.**
7. Any institutional position on framing the project in defense/ISR terms?

---

## References

1. ISO/IEC/IEEE 15288:2023, *System life cycle processes* — the stakeholder definition.
2. ISO/IEC/IEEE 29148:2018, *Requirements engineering* — linking stakeholders forward to the SRS.
3. SEBoK Editorial Board, *"Stakeholder Needs Definition"* and *"Stakeholder (glossary),"* SEBoK v2.14, Stevens Institute of Technology, 2026.
4. M. B. E. Clarkson, "A Stakeholder Framework for Analyzing and Evaluating Corporate Social Performance," *Academy of Management Review* 20(1):92–117, 1995. — **the primary/secondary split**
5. K. D. Eason, *Information Technology and Organisational Change*, Taylor & Francis, 1988. — primary/secondary/tertiary/facilitating
6. R. K. Mitchell, B. R. Agle, D. J. Wood, "Toward a Theory of Stakeholder Identification and Salience," *AMR* 22(4):853–886, 1997.
7. H. Sharp, A. Finkelstein, G. Galal, "Stakeholder Identification in the Requirements Engineering Process," *DEXA'99*, 387–391.
8. R. E. Freeman, *Strategic Management: A Stakeholder Approach*, Pitman, 1984.
9. ABET EAC, *Criteria for Accrediting Engineering Programs, 2025–2026* — Criterion 5, Criterion 3 outcomes (2)/(5), Criterion 2.
10. NIST, *Standard Test Methods for Response Robots*; ASTM Committee E54.09.
11. M. Tranzatto et al., "CERBERUS: Autonomous Legged and Aerial Robotic Exploration … DARPA Subterranean Challenge," *Field Robotics*, 2022. arXiv:2201.07067.
12. DARPA, *OFFensive Swarm-Enabled Tactics (OFFSET)* program page.
13. A. Gawel et al., "3D Registration of Aerial and Ground Robots for Disaster Response," arXiv:1709.00587, 2017.
14. "Deployment of an Aerial Multi-agent System … Underground Mining Environments," arXiv:2501.10262, 2025.
15. "Risk-aware Resource Allocation for Multiple UAVs-UGVs Recharging Rendezvous," arXiv:2209.06308, 2022.
16. "Air-Ground Collaborative Robots for Fire and Rescue Missions," arXiv:2412.20699, 2024.
17. FHWA, *Bridge Condition by Highway System 2024*, National Bridge Inventory. ✅ verified
18. NIFC, *Wildfires and Acres*, Fire Information Statistics. ✅ verified

---

**Related:** [`F05_standards_and_regulations.md`](F05_standards_and_regulations.md) · [`F03_air_ground_integration.md`](F03_air_ground_integration.md) · [`../../proposal/PROPOSAL_GAP_ANALYSIS.md`](../../proposal/PROPOSAL_GAP_ANALYSIS.md) · [`../../INDEX.md`](../../INDEX.md)
