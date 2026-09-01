# Open Questions

Things the proposal cannot be finished without. Grouped by who answers them. Tracked as `PD-##` in [`../docs/03_decision_record.md`](../docs/03_decision_record.md#pending-decisions).

---

## For the faculty mentor / customer (Dr. Calderon Chavez)

Ask these in one meeting; the course policy requires regular customer contact anyway.

1. **What exactly is the mission?** Is there a defined mission sequence we are inheriting, or do we define it? *Blocks the entire Proposed Solution section (45%).*
2. **What ground vehicles exist?** Platform, how many, current state, who maintains them. *Blocks Budget (10%) and scope.*
3. **How many Crazyflies are available**, and how many can fly simultaneously on the existing setup?
4. **Which positioning system is installed and working** — Lighthouse, Loco/UWB, or both? How many base stations, what volume does it cover?
5. **Has the air frame and the ground overhead-camera frame ever been calibrated to each other?** If prior work exists, we should not redo it. *This is [IR-03](../docs/01_idea_register.md#ir-03--unified-coordinate-frame-across-two-localization-systems), likely our first milestone.*
6. **What software stack is already running** — Crazyswarm2/ROS 2, or the team's own? Which ROS 2 distro? Is there a repository we inherit?
7. **What did previous teams leave behind**, and what broke? Department policy says materials stay, so something should exist.
8. **Is there a flight cage / netting**, and what is the lab access schedule?
9. **What does success look like to you?** Ask directly — the customer's definition is what the proposal should target.
10. **Your relevant publications** — for the literature review, and because citing the customer is good practice.

## For the course instructor (Dr. Yang)

11. **Does "avoiding simulation" conflict with SLO 6?** We plan to state that hardware is primary validation and software-in-the-loop is used to unit-test coordination logic. Confirm that satisfies the outcome. *See [DR-02](../docs/03_decision_record.md#dr-02--semester-1-favors-real-hardware-over-simulation).*
12. **Does SLO 5 (prototype an embedded computing system) require work on the drone firmware itself**, or does a ground-station orchestration system with embedded deck integration count?
13. **Proposal due date and length expectation** — the template gives no page target.
14. **Citation style** for references.
15. **Backlog tool** — is GitHub Projects acceptable, or is Jira/Scrumwise expected?

## For the team

16. **[PD-01] Project name.** `X_swarm` is a placeholder. Candidates in [`PROPOSAL_GAP_ANALYSIS.md`](PROPOSAL_GAP_ANALYSIS.md#project-name--2).
17. **[PD-02] Roles.** PM/Scrum · Systems & Technical · Design/Implementation · Testing & Validation · Documentation & Communication. Needed for the proposal and for weekly progress checks.
18. **[PD-03] Air-only or air+ground for the graded baseline?** Air-only is safer and still satisfies the project; air+ground is what the draft promises and is significantly harder. **Recommendation:** promise air-only formation as the Semester 1 baseline, air+ground as the Semester 2 target — so a delay on the ground platform does not sink the midterm.
19. **[PD-04] Swarm size.** N drones and M ground vehicles, as a number, in the proposal. Radio bandwidth sets the ceiling — [`../docs/findings/F04_network_and_latency.md`](../docs/findings/F04_network_and_latency.md).
20. **[PD-05] Spares.** Even at zero budget, decide whether to request spare propellers, batteries and an airframe. One unrecoverable crash without spares stops all work.
21. **Which two or three application domains** do we claim as stakeholders? — [`../docs/findings/F06_stakeholders_and_applications.md`](../docs/findings/F06_stakeholders_and_applications.md).
22. **Verify name spellings** against the roster before submission.

---

## Missing inputs

- **The two mentor project description PDFs** (Calderon swarm, Akbas RL) referenced in [`../init_transcript.md`](../init_transcript.md) are not in this repository. The swarm one is needed for the mission sequence — questions 1 and 9 above are partly redundant if we can just find that file. Check Canvas.

---

**Related:** [`PROPOSAL_GAP_ANALYSIS.md`](PROPOSAL_GAP_ANALYSIS.md) · [`../docs/03_decision_record.md`](../docs/03_decision_record.md) · [`../INDEX.md`](../INDEX.md)
