# F05 · Standards and Regulations

The proposal rubric asks: *"What standards drive the solution? [eg, IEEE standard, FAA, FCC, ISO, etc.]"* — worth part of the 45% Proposed Solution section.

**This page is organized around one distinction: what the team can honestly cite versus what would be name-dropping.** Graders catch scope errors, and several obvious-looking citations here are outright wrong for this project.

Related: [C-15](../02_constraints.md#c-15--safety-and-regulatory) · [`../../proposal/PROPOSAL_GAP_ANALYSIS.md`](../../proposal/PROPOSAL_GAP_ANALYSIS.md)

---

## Tier 1 — cite these, they genuinely apply

### The document-structure standards — highest value

These map **one-to-one onto the graded deliverables**, which makes them the most honestly citable standards available:

| Standard | Governs | Deliverable |
| --- | --- | --- |
| **ISO/IEC/IEEE 29148:2018** | Requirements engineering; characteristics of a good requirement; SRS content structure | SRS |
| **ISO/IEC/IEEE 42010:2022** | Architecture description, stakeholder viewpoints | System Design Document |
| **ISO/IEC/IEEE 29119-3:2021** | Test documentation | System Test Plan |
| **ISO/IEC/IEEE 15288:2023** | System life cycle processes | The two-semester sequence as a whole |

29148's "characteristics of a good requirement" is directly useful, not decorative — see [F10](F10_benchmarking_and_measurement.md) on writing measurable requirements.

### FAA — the honest framing

**Indoor flight is outside FAA jurisdiction.** The FAA states directly that *"Part 107 would not apply to operations conducted indoors"* because *"FAA rules and regulations apply to operations conducted outdoors in the National Airspace System (NAS)."*

Be precise about *why*: **there is no explicit "indoor" carve-out written into §107.1.** The carve-out is jurisdictional (NAS) and comes from FAA interpretation. State it that way to be accurate.

**§107.35 is the strongest genuine regulatory driver in this project:**

> *"A person may not manipulate flight controls or act as a remote pilot in command or visual observer in the operation of more than one unmanned aircraft at the same time."*

Any swarm larger than one aircraft is unlawful outdoors without a waiver. **That single sentence is the regulatory justification for the entire autonomy architecture.**

§107.205 lists §107.35 among waivable sections, so a waiver path legally exists. The honest phrasing is: *"our design targets the evidence a §107.35 waiver would require"* — not the vaguer *"we comply with Part 107."* **Precedent exists, but cite it by waiver number, not by statistics.** The FAA does grant Part 107 certificates of waiver combining §107.35 with §107.29(a)(2) and (b) for drone light shows — **Sky Elements LLC, Waiver 107W-2021-02474**, and **Verge Aero, Waiver 107W-2024-01105** (issued 15 May 2024). That is a solid one-pilot-many-aircraft precedent.

> ⚠ An earlier draft of this page cited "200+ shows of 50–650 drones with zero safety incidents." **Those numbers are not in the source and must not be used** — the cited document is FAA Grant of Exemption No. 22551 (Docket FAA-2023-2047), a decision letter containing no such figures, and the operator's own track record was withheld as proprietary. The only operator statistics present are Sky Elements': an average show is *"250 drones and lasts 10 minutes,"* with *"over 200,000 drones into the sky"* and *"over 30,000 flights."*

**Remote ID does not trigger here, and the reason is a chain, not a weight:**

1. §89.101 applies Remote ID to aircraft **registered or required to be registered** under Parts 47/48 — keyed to registration status, not weight directly.
2. §48.15 exempts from registration an sUAS operated exclusively under 49 U.S.C. §44809 weighing **≤0.55 lb (250 g)** at takeoff including everything attached.
3. A 29 g Crazyflie is **~8.6× under** that line.

So the registration-and-therefore-Remote-ID chain never starts. Stating the chain is much stronger than asserting a weight threshold that does not actually appear in Part 89.

**49 U.S.C. §44809** (limited recreational operations) covers educational users — but note the mechanism: **the educational extension is not in §44809 and was not made by the FAA.** Congress made it in an uncodified note, **Sec. 350 of the FAA Reauthorization Act of 2018 (Pub. L. 115-254)**, later amended by Pub. L. 116-283 §10002 (2021) and Pub. L. 118-63 §928(b) (2024) to four categories. ERAU qualifies as an institution of higher education under 20 U.S.C. §1001(a).

> ⚠ **Correction to an earlier framing.** "§44809 is more defensible than Part 107 for a class project" is **wrong twice over.** Part 107 is *not* commercial status — it has no business-purpose test, expressly covers education, and the FAA advises *"when in doubt, assume Part 107."* And **§44809 has no waiver mechanism**, whereas §107.205 makes §107.31 (VLOS) and **§107.35 (one aircraft per operator) waivable.** For a multi-vehicle swarm, Part 107 plus a waiver is the *only* path — §44809 offers none. All eight §44809(a) limitations remain absolute regardless (recreational purpose, CBO safety programming, VLOS, give way to manned aircraft, LAANC authorization, 400 ft in Class G, TRUST, registration and Remote ID).

### FCC — and a genuinely interesting finding

**47 CFR §15.247** caps 2400–2483.5 MHz digitally modulated systems at **1 W (30 dBm) conducted**, antennas up to 6 dBi (**36 dBm EIRP**), PSD ≤8 dBm in any 3 kHz band. These are the hard ceilings for any link-budget analysis.

**The Crazyflie 2.1 is certified: FCC ID 2AUV3CF21KIT** (Bitcraze AB, 2402–2480 MHz, Part 15C Digital Transmission System). Citing the FCC ID by number is far stronger than a generic "we comply with FCC Part 15."

> ⚠ **But the Crazyradio dongles are not.** Bitcraze states on its own GitHub discussions that *"only the Crazyflie 2.1 is certified by FCC/CE/MIC"* — the Crazyradio PA holds only Korean KC and limited Japanese test certification. §15.1(c) prohibits operating intentional radiators lacking prior equipment authorization, and §15.23's home-built exemption (≤5 units, not from a kit, not marketed) **does not cover a purchased dongle**.
>
> This is a real, specific, honest compliance finding — unusually good material for a proposal. **Route it to ERAU rather than asserting an exemption**; see open questions below.

**Unresolved discrepancy:** the Crazyflie 2.1 datasheet advertises a "20 dBm radio amplifier" while the FCC grant listing shows conducted output of 0.0005 W (≈ −3 dBm). **Read the actual FCC test report exhibit before making any link-budget claim in the SRS.**

### Safety — with an honesty caveat

**IEC 60825-1:2014** — the SteamVR Base Station 2.0 (HTC 2QCJ100, FCC ID NM82QCJ100) is **certified as a Class 1 laser product**. Its safety guide states it *"contains Class 3B laser, which can produce hazardous level of Class 3B and 4 laser radiations. However, the design of this product incorporates optics, a protective housing and a scanning safeguard such that there is no access to levels of laser radiation above Class 1."*

> ⚠ **Downgraded from "strongest non-obvious citation."** IEC 60825-1 **binds the manufacturer, not the capstone team.** Because the unit ships as a Class 1 product, the standard imposes essentially no user-side control measures — **it does not "drive" the design.** The only genuine operational constraints it yields are: never operate a base station with the housing open or damaged, and don't defeat the scanning safeguard. Cite it as an operating-procedure basis, not a design driver.
>
> Also cite it correctly: the source is the FCC exhibit *"User Manual 2 (Safety and regulatory guide)"* under FCC ID NM82QCJ100 — **not the Bitcraze docs page, which says nothing about laser classes or IEC 60825-1.**

**IEC 62133-2:2017+AMD1:2021** (portable sealed lithium cells) plus **UN 38.3** (transport) — a fleet of 250 mAh LiPo packs in a shared lab is a real hazard, and these support charging, storage and handling procedures. Recall the Day-1 lab policy: *don't leave chargers unsupervised.*

### Communications

**OMG DDSI-RTPS v2.5** (April 2022) — if the ground robots run ROS 2, this is a genuine, named, version-pinned communications standard the team actually uses.

> ⚠ **Do not cite IEEE 802.15.4 for the Crazyflie link.** The Crazyflie-to-Crazyradio link uses Nordic's proprietary **Enhanced ShockBurst (ESB)** — not 802.15.4, not standard BLE. (The onboard nRF51822 separately supports BLE for phone clients.) **This is the single most likely name-dropping error this team could make.**

### If a learned or complex controller enters scope

**ASTM F3269-21** — run-time assurance as an alternative to design-time assurance, explicitly to bound nondeterministic behavior from unassured or algorithmically complex functions, and to permit COTS hardware/software. The one ASTM F38 standard that genuinely fits a learned swarm controller wrapped in a safety monitor. Citing it signals the team understands *why* an autonomy safety architecture is needed.

---

## Tier 2 — honest but low value

| Standard | Honest use | Limit |
| --- | --- | --- |
| **ISO 8373:2021** (Robotics vocabulary) | Consistent air/ground terminology across all four documents | That's all it does |
| **ISO 21384-2:2021 / -3:2026 / -4:2025** | Voluntary best-practice reference | ⚠ **-3 is now edition 3 (2026-08-07)**, superseding the :2023 edition — the older catalogue entry points to a withdrawn edition. Applies to **commercial** UAS ops; a capstone flying indoors is not one. Series retitled "Unmanned" → "Uncrewed" |
| **ISO 15964:2025**, **ISO 23629** UTM series | Detect-and-avoid; UTM functional structure (-5), remote ID (-8), provider/user interface (-9) | Omitted from earlier drafts, and **more relevant to a heterogeneous swarm than 21384** if the project ever goes outdoors |
| **ISO 23665:2026** | UAS personnel training | Edition 3, released 2026-08-18 |
| **IEEE 1936.1-2021** (Drone Applications Framework) | Element decomposition for the SDD — flight platform, flight control system, ground control station, payload, control/data link, **takeoff and landing system** | Generic; adds little unless architecture is actually **mapped** onto it. ⚠ Quote the **abstract**, not the Scope clause — the formal Scope is much narrower than the decomposition people cite it for |

---

## Tier 3 — do NOT cite these

Each of these looks topically relevant and is wrong. A reviewer could catch any of them immediately.

| Standard | Why it fails here |
| --- | --- |
| **ISO 21384-1** | **Never published.** The DIS was deleted as a project on 5 July 2019 at stage 40.98. Citing it references a standard that does not exist. |
| **ANSI/A3 R15.08** | Explicitly places *"airborne systems (drones, for example)"* **outside its scope**. Outright scope error for the aerial half. |
| **ASTM F3442/F3442M** | Scope is detect-and-avoid **in the NAS**. Citing it for indoor inter-agent collision avoidance is a scope error despite the surface-level match. |
| **ASTM F3389/F3389M-21** | ⚠ **Moved here from Tier 1.** It exists to support Civil Aviation Authority approval for **flight over people**, as a means of compliance for 14 CFR Part 107 Subpart D Category 2 (§107.120) and Category 3 (§107.130). It does not reach a 29 g indoor drone: Part 107 does not apply indoors at all, and even outdoors a 29 g aircraft is Category 1 (§107.110, ≤250 g). *(If ever cited: the **-21** edition defines four methods A–D; the superseded **-20** has only three. Method A's gate is an **energy** threshold — impact KE never exceeding 73 J — not a weight class.)* |
| **ANSI/CAN/UL 3030** | Two of three conditions fail — commercial, and certified pilot. ⚠ **"Intended for outdoor operation" is an *inclusion* condition, not an exclusion**, so an outdoor swarm would satisfy it. The stronger honest argument is **clause 1.3**, which excludes autonomy/flight-control efficacy, UAS handling, and loss-of-communication effects — i.e. almost everything a swarm-coordination capstone actually does. |
| **IEEE 1873-2015** (2D map data) | **2D-only by its own scope statement** — explicitly excludes 3D, dynamic and semantic maps. Cannot represent the aerial half. Honest only if applied *solely* to the ground robots. |
| **IEEE 1872 / 1872.2** (robotics ontology) | Real standards, but nothing in a Crazyflie/ArUco/ROS stack consumes them. Honest only if the team actually authors an OWL ontology as a deliverable. |
| **IEEE 2941-2021** (AI model interoperability) | Only honest if models are actually trained on the H100 cluster and shipped to onboard inference targets — which would be a real interoperability problem worth citing. |
| **IEEE 7000-2021** (ethical value elicitation) | Defensible **only if the team runs the process and produces its artifacts.** Cited without the work, pure name-dropping. |

**On IEEE 7000 specifically:** there *is* a genuine hook. An overhead camera watching a lab raises a real privacy question ([SLO 4](../04_course_requirements.md#student-learning-outcomes-map-deliverables-to-these) requires considering ethical and societal constraints). If the team does the analysis, the citation becomes honest — and it covers an SLO. But do the work first.

**On Remote ID citations:** if cited at all, **F3411-22a alone is technically wrong for compliance purposes.** ASTM **F3586-22** is the FAA-facing Means of Compliance document; the FAA accepted it "with additions," adding a tamper-resistance requirement because *"Section 7.5.2 of ASTM F3586-22 does not adequately ensure compliance with tamper resistance requirements."* **That quote is in the original acceptance notice — 87 Fed. Reg. 49576, 11 Aug 2022 — not in the 14 Nov 2023 correction.** Cite the original. Citing that Federal Register record shows the team read the regulatory record, not a standard's title page.

---

## Where no standard exists — say so

**No consensus standard exists for indoor research-lab drone flight.** University documents filling the gap (e.g. Princeton's Indoor Safety Guidelines) are informal best-practice lists sourced from hobbyist blog articles, not standards bodies.

**Say this plainly in the proposal: indoor lab safety is governed by institutional policy, not by a standard.** That is more credible than inventing a standards citation for netting. Then cite ERAU's actual policy (see open questions).

For containment, typical practice cited by netting vendors uses ~1¾ inch knotted nylon mesh with impact eyewear as PPE — a concrete specification to propose to the mentor, carrying no standards number behind it, and it should be presented that way.

---

## Open questions

1. **ERAU's own campus/lab UAS operating policy is the single most binding document governing these flights**, and it is not publicly locatable. Obtain it from Dr. Calderon Chavez, the department, or ERAU Environmental Health & Safety, and **cite it by title and revision date** in the proposal.
2. **How does ERAU handle the uncertified Crazyradio dongles?** Institutional experimental authorization, a Part 5 experimental license, or unexamined practice? Direct question to the mentor, possibly to ERAU's spectrum or research-compliance office.
3. Is there a flight cage or netting — mesh spec, dimensions, ceiling clearance? Indoor containment has no governing standard, so the constraint is purely physical.
4. **Does the overhead ArUco camera record or retain imagery of people entering the lab?** Determines whether IRB review or a privacy analysis is warranted — and therefore whether IEEE 7000 is an honest citation. Only the mentor can answer.
5. What radio do the ground robots use — campus Wi-Fi, a dedicated AP, something else? Determines whether IEEE 802.11 and ERAU IT policy are genuine drivers.
6. **Does the CESC 420 rubric expect standards cited as binding requirements or as design references?** This changes how aggressively to claim applicability. Confirm with Dr. Yang rather than infer.
7. Has any university been granted a §107.35 waiver for swarm *research* (as opposed to commercial light shows)? Would need a direct FAA waiver-database search. Only matters if the project goes outdoors.
8. ASTM work item WK91742 is an active revision of F3411-22a — verify the current version against the FAA's published MOC list at <https://uasdoc.faa.gov/listMOC> before citing a version number. Again, only matters outdoors.

---

## Suggested proposal wording

> The baseline system operates indoors, where the FAA has stated Part 107 does not apply because its rules govern operations in the National Airspace System. Flight safety is therefore governed by ERAU institutional policy [cite by title/date] rather than by a consensus standard, as none exists for indoor research flight. The design nonetheless targets 14 CFR §107.35 — which prohibits one pilot operating multiple aircraft — as the regulatory driver for autonomy, since it is the constraint any outdoor scaling would face and is waivable under §107.205. Radio operation is bounded by 47 CFR §15.247; the Crazyflie 2.1 airframe holds FCC ID 2AUV3CF21KIT. Document structure follows ISO/IEC/IEEE 29148 (requirements), 42010 (architecture) and 29119-3 (test documentation) under the 15288 life-cycle framework. Lighthouse base-station operating procedures follow IEC 60825-1 (the units are certified Class 1), and battery handling follows IEC 62133-2.

That paragraph cites nine standards, every one of which the team can defend.

---

## References

1. FAA, *"Do the FAA rules and regulations apply to … drone operations conducted indoors ONLY?"* FAA FAQ. <https://www.faa.gov/faq/do-faa-rules-and-regulations-apply-commercial-uas-or-drone-operations-conducted-indoors-only>
2. 14 C.F.R. Part 107, esp. §107.1, **§107.35**, §107.205. Waiver precedent: Sky Elements 107W-2021-02474; Verge Aero 107W-2024-01105.
3. 14 C.F.R. Part 89, esp. §89.101; 14 C.F.R. §48.15; 49 U.S.C. §44809 **plus Sec. 350, Pub. L. 115-254** (the educational extension — it is not in §44809 itself).
4. ASTM F3411-22a and **ASTM F3586-22**; FAA, *Accepted Means of Compliance; Remote Identification of Unmanned Aircraft*, 87 Fed. Reg. 49576 (11 Aug 2022), correction 14 Nov 2023.
5. 47 C.F.R. Part 15, esp. §15.1, §15.23, **§15.247**.
6. FCC Grant of Equipment Authorization, **FCC ID 2AUV3CF21KIT**, Bitcraze AB, Crazyflie 2.1.
7. Bitcraze AB, GitHub discussion #249 — certification status of Crazyradio.
8. IEC 60825-1:2014, *Safety of laser products — Part 1*. Source for the base-station classification: FCC exhibit *User Manual 2 (Safety and regulatory guide)*, FCC ID NM82QCJ100.
9. **IEC 62133-2:2017+AMD1:2021**, lithium cells and batteries; UN 38.3.
10. **ASTM F3269-21**, run-time assurance for complex functions.
11. ASTM F3389/F3389M-21 — *listed for completeness only; see Tier 3, it does not apply here.*
12. **OMG DDSI-RTPS v2.5**, April 2022.
13. **ISO/IEC/IEEE 29148:2018**, requirements engineering.
14. **ISO/IEC/IEEE 42010:2022**, architecture description.
15. **ISO/IEC/IEEE 29119-3:2021**, test documentation.
16. **ISO/IEC/IEEE 15288:2023**, system life cycle processes.
17. ISO 8373:2021, robotics vocabulary; ISO 21384-2:2021, **-3:2026 (ed. 3)**, -4:2025; ISO 23665:2026; ISO 15964:2025; ISO 23629 UTM series.
18. IEEE Std 1936.1-2021, Drone Applications Framework.
19. Bitcraze AB, "Crazyflie radio communication," Aug 2020 — **ESB, not 802.15.4**.
20. Princeton University, *Indoor Safety Guidelines* — example of the institutional-policy gap.

---

**Related:** [`F04_network_and_latency.md`](F04_network_and_latency.md) · [`F06_stakeholders_and_applications.md`](F06_stakeholders_and_applications.md) · [`../02_constraints.md`](../02_constraints.md) · [`../../INDEX.md`](../../INDEX.md)
