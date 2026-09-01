# CESC 420 — Course Requirements Digest

Compiled from [`../cesc420.pdf`](../cesc420.pdf) (syllabus) and [`../canvas_materials/`](../canvas_materials/). Rubric weights are quoted verbatim so we can target them.

---

## Course facts

| | |
| --- | --- |
| Course | DB-CESC 420 01DB — Computer Systems Design I, 3 cr |
| Term | Daytona Beach Fall 2026 · **Aug 24 – Dec 9, 2026** |
| Meets | Tue/Thu 2:15–3:30 PM, Instructional Center 101 (in person) |
| Instructor | Fan Yang · yangf1@erau.edu · office hours MWF 11–12, 3–4 |
| Capstone faculty | Dr. Ilhan Akbas, Dr. Juan Calderon Chavez, Dr. Fan Yang |
| Structure | Two-semester sequence — CESC 420 (Fall 2026) → Semester 2 (Spring 2027) |
| Grading | A 90+, B 80–89, C 70–79, D 60–69, F <60 |
| Required tooling | A backlog system — Jira, Scrumwise, GitHub, etc. |

**Course policy (verbatim):** class time is for discussing the project and executing plans; documentation is treated as homework and done outside class; meet regularly with project customers for feedback.

**Weekly:** attendance is checked; instructors/TAs do in-class progress checks; the backlog must be current, with per-sprint task estimates in a consistent unit (points or hours).

---

## Deliverables and their rubrics

### 1. Project Proposal — *current task*

| Section | Weight |
| --- | ---: |
| Project Name | 2% |
| Project Team Members | 4% |
| Problem Statement | 24% |
| Stakeholders | 10% |
| Proposed Solution | 45% |
| Proposed Project Budget | 10% |
| References | 5% |

**Budget clause:** if no budget is required, state that explicitly — the 10% redistributes as +3% Problem Statement, +3% Stakeholders, +4% Proposed Solution. *Redistribution requires the statement; leaving the section blank forfeits the points.*

**Problem Statement explicitly requires a literature review.** Template text: *"To fill out this section, do a review of the relevant literature in the project area. References can be placed at the end of this proposal."* This is the single largest scoring gap in the current draft.

Full section-by-section analysis: [`../proposal/PROPOSAL_GAP_ANALYSIS.md`](../proposal/PROPOSAL_GAP_ANALYSIS.md)

### 2. System Requirements Specification (SRS)

Template sections: Introduction (7%), General Description, External Interface Requirements, Behavioral Requirements, Non-behavioral Requirements (performance, safety, availability, security, maintainability, portability), Other Requirements, **Analysis Models** (data flow L0/L1/L2, class model, state model), Impact Analysis.

Note the diagram load — context diagram plus two data-flow levels, a class model and a state model.

### 3. System Design Document (SDD)

Sections: Introduction, **System Architecture** (hardware / software / internal communications), Human-Machine Interface (inputs, outputs), **Detailed Design** (hardware, software, internal comms), External Interfaces.

### 4. System Test Plan

Sections: Introduction (10%), Testing Approach (usability, functionality; suspension/resumption criteria; environment; assumptions; risks), Test Schedule, **Traceability Matrix** and defect severity definitions, Test Cases and Results.

The traceability matrix maps every SRS requirement to a test case — so SRS requirements must be written measurably from the start.

### 5. Midterm presentation — 5 minutes, all members contribute

| Criterion | Weight |
| --- | ---: |
| Technical Concept & System Overview | 20% |
| Design Approach & Rationale (incl. alternatives) | 20% |
| Technical Feasibility & Planning (subsystems, challenges, mitigation) | 20% |
| Early Progress & Prototyping Evidence | 15% |
| Presentation & Communication | 10% |
| Visual Aids (block diagrams, flowcharts, 3D model, animation) | 10% |
| Engineering Insight & Next Steps | 5% |

*Early Progress accepts "clear requirements if the project is still in very early stage" — a fallback worth knowing.*

### 6. Final presentation — 50 pts

Problem Statement & Motivation 5 · Project Design & Technical Content 15 · Results/Progress/Demos 5 · **Lessons Learned 10** · **Future Plans & Next Steps 10** · Presentation Quality 5.

Lessons Learned and Future Plans together are 40% — failed approaches and requirement shifts are worth points, so record them as they happen ([`03_decision_record.md`](03_decision_record.md) feeds this directly).

### 7. Poster

Project Execution & Outcomes 20% · Understanding & Critical Thinking 20% · Content & Clarity 20% · Visual Appeal 15% · Oral Presentation 15% · Professionalism 10%.
Examples on display in the department hallway and at <https://commons.erau.edu/db-srs/>.

### 8. Ten-minute video

Content 65% — Introduction 10 (elevator pitch, problem, customer/origin, purpose, importance), Design Considerations 20 (assumptions, dependencies, constraints, standards, safety), System Architecture 20, Subsystem/Detailed Design 15.
Effectiveness 35% — Lessons Learned 4, Timeline 4, Participation 4, Verbal Quality 5, Visual Aids 8, **Time Management 10**.

Budget is required in the video even for a 100%-software project (state open-source vs commercial).

### 9. Project Functionality {#project-functionality}

Basic Requirements 60% (core functionality 40, usability & reliability 20) · Intermediate Enhancements 20% (extended features 10, efficiency & optimization 10) · **Advanced/Innovative Features 20%** (advanced functionality 15, creativity & impact 5).

The advanced tier says *"listed or not in SRS or proposal documents"* — this is where parked ML ideas can score without being promised in the proposal.

### 10. Engineering notebook

See [`../canvas_materials/engineering notebook example.docx`](../canvas_materials/engineering%20notebook%20example.docx). The example is a dated, literal command-by-command log — every command typed, every error, every setting changed. Keep it at that granularity.

### 11. Peer evaluation

Template in canvas_materials. Individual grades are affected.

---

## Student Learning Outcomes (map deliverables to these)

1. Apply the engineering design process to complex, open-ended problems.
2. Integrate interdisciplinary knowledge to assess feasibility and effectiveness.
3. Communicate technical information through reports, presentations, demonstrations.
4. Create solutions considering **ethical, societal, and sustainability** constraints.
5. **Prototype an embedded computing system** using computer engineering principles.
6. Examine designs through physical experiments, prototypes, **and computer simulations**.

Two of these bite:

- **SLO 5** requires embedded prototyping. A pure ground-station orchestration project does not satisfy it — some work must land on the Crazyflie firmware or a deck.
- **SLO 6** names simulation explicitly. [DR-02](03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation) ("avoid simulation") is in tension with this. The proposal should not say *no* simulation; it should say simulation is used for X and hardware for Y.

---

## Team roles (from Day 1 slides — "ownership, not boundaries")

Project Manager/Scrum Lead · Systems & Technical Lead · Design/Implementation Lead · Testing & Validation Lead · Documentation & Communication Lead. Everyone still does engineering work.

## Lab and materials policy

Safety first; check wiring/limits before energizing; work within your training; protect people before hardware; report problems immediately. **All materials built, purchased, or modified belong to the EECS Department or the customer** — nothing goes home. Don't leave chargers unsupervised.

---

**Related:** [`../proposal/PROPOSAL_GAP_ANALYSIS.md`](../proposal/PROPOSAL_GAP_ANALYSIS.md) · [`02_constraints.md`](02_constraints.md) · [`../INDEX.md`](../INDEX.md)
