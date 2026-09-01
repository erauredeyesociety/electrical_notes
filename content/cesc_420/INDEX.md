# CESC 420 — Capstone Documentation Index

**Project:** heterogeneous air-ground drone swarm (working name `X_swarm`)
**Team:** Emmett Gilbert · Gatlin Nelson · DeAndre Johnney · Nicholas Schultz
**Term:** Fall 2026 (CESC 420) → Spring 2027
**Mentor / customer:** Dr. Juan Calderon Chavez · **Instructor:** Dr. Fan Yang

---

## Start here

| If you want to… | Read |
| --- | --- |
| Finish the proposal | [`proposal/PROPOSAL_GAP_ANALYSIS.md`](proposal/PROPOSAL_GAP_ANALYSIS.md) → [`proposal/PROPOSAL_DRAFT_v2.md`](proposal/PROPOSAL_DRAFT_v2.md) |
| Know what's blocking us | [`proposal/OPEN_QUESTIONS.md`](proposal/OPEN_QUESTIONS.md) |
| Know what's due and how it's graded | [`docs/04_course_requirements.md`](docs/04_course_requirements.md) |
| Know why we're doing this and not that | [`docs/03_decision_record.md`](docs/03_decision_record.md) |
| Find an idea we discussed | [`docs/01_idea_register.md`](docs/01_idea_register.md) |
| Check a technical claim | [`docs/findings/`](docs/findings/) |

---

## Documentation

### Registers and decisions

- [`docs/00_meta_idea_register.md`](docs/00_meta_idea_register.md) — how the register is built: entry shape, status taxonomy, the no-deletion rule
- [`docs/01_idea_register.md`](docs/01_idea_register.md) — **every idea raised**, IR-01…IR-23, with status and reasoning
- [`docs/02_constraints.md`](docs/02_constraints.md) — what is true regardless of what we pick
- [`docs/03_decision_record.md`](docs/03_decision_record.md) — decisions DR-01…DR-05, and pending decisions PD-01…PD-05
- [`docs/04_course_requirements.md`](docs/04_course_requirements.md) — deliverables, rubric weights, SLOs, lab policy

### Planning

- [`docs/05_risk_register.md`](docs/05_risk_register.md) — R-01…R-14 scored, with mitigations for everything ≥ 12
- [`docs/06_semester1_schedule.md`](docs/06_semester1_schedule.md) — week map Aug 24–Dec 9, milestones M1…M10, parallel workstreams

### Findings

- [`docs/findings/F01_crazyflie_platform.md`](docs/findings/F01_crazyflie_platform.md) — airframe, positioning, radio, decks, swarm limits
- [`docs/findings/F02_formation_control.md`](docs/findings/F02_formation_control.md) — coordination approaches and **evaluation metrics**
- [`docs/findings/F03_air_ground_integration.md`](docs/findings/F03_air_ground_integration.md) — fiducial localization, frame unification, time sync
- [`docs/findings/F04_network_and_latency.md`](docs/findings/F04_network_and_latency.md) — bandwidth budget, ROS 2/DDS, 2.4 GHz coexistence
- [`docs/findings/F05_standards_and_regulations.md`](docs/findings/F05_standards_and_regulations.md) — FAA, FCC, IEEE, ISO — what we can honestly cite
- [`docs/findings/F06_stakeholders_and_applications.md`](docs/findings/F06_stakeholders_and_applications.md) — primary vs secondary, application domains
- [`docs/findings/F07_edge_ml.md`](docs/findings/F07_edge_ml.md) — onboard inference limits, CTDE, cross-view geo-localization
- [`docs/findings/F08_lidar_and_sensors.md`](docs/findings/F08_lidar_and_sensors.md) — verification of the five transcript lidar claims (3 needed correction); complementary sensors vs the 15 g / 7.9 W budget
- [`docs/findings/F09_simulation_and_compute.md`](docs/findings/F09_simulation_and_compute.md) — what simulation is worth building; what the 8× H100 can honestly be claimed to do
- [`docs/findings/F10_benchmarking_and_measurement.md`](docs/findings/F10_benchmarking_and_measurement.md) — **benchmarking as measurement, not simulation**; embedded timing, ROS 2/DDS latency, profiling, statistical rigor, measurable requirements

### Proposal

- [`proposal/PROPOSAL_GAP_ANALYSIS.md`](proposal/PROPOSAL_GAP_ANALYSIS.md) — draft vs rubric, section by section, with a scoring estimate
- [`proposal/PROPOSAL_DRAFT_v2.md`](proposal/PROPOSAL_DRAFT_v2.md) — the rewrite
- [`proposal/OPEN_QUESTIONS.md`](proposal/OPEN_QUESTIONS.md) — what to ask the mentor, the instructor, and each other

---

## Source material

| File | What it is |
| --- | --- |
| [`init_transcript.md`](init_transcript.md) | The project-selection conversation. Source for IR-01…IR-22. |
| [`MOCK_PROPOSAL.pdf`](MOCK_PROPOSAL.pdf) | First proposal draft |
| [`cesc420.pdf`](cesc420.pdf) | Syllabus |
| [`canvas_materials/`](canvas_materials/) | All templates and rubrics |

**Known missing:** the two mentor project-description PDFs (Calderon swarm, Akbas RL). Referenced in the transcript, not on disk. Check Canvas — the swarm one likely contains the mission sequence we need.

---

## Conventions

- Everything is Markdown; relative links between files.
- Register entries are `IR-##`, decisions `DR-##`, pending decisions `PD-##`, findings `F##`.
- Nothing is deleted — rejected ideas keep their reason ([`docs/00_meta_idea_register.md`](docs/00_meta_idea_register.md)).
- No cost figures outside the proposal's Budget section.

_Last updated: 2026-08-31_
