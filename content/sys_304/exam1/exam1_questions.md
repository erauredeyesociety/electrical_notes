# SYS 304 — Trade Studies, Risk, and Decision Analysis — Test 2

---

## Question 1 (20 points) — Trade Study Selection

Referring to the figure below, there are four alternative configurations and several selection criteria. The equivalent cost is used as the main criterion for selection. Out of the other four (X, Y, Z, V), criterion Z is critical (hard constraint) and must be respected by the selected alternative configuration. The other three criteria can be considered in trade studies (soft constraints).

Which alternative would you select? Why?

**Figure notes (from pg1.jpg):**
- The figure labels the four alternatives as A, B, C, D (read from the figure columns)
- The criteria rows from top to bottom appear to be: Y, X, Z, V, and Equivalent cost
- Each criterion has a threshold line (vertical dashed line labeled "Criteria threshold")
- Dots represent each alternative's performance on each criterion relative to the threshold
- The bottom row shows "Equivalent cost" with arrows

---

## Question 2 (25 points) — LP and Goal Programming

An engineering design and manufacturing company produces two systems to address the needs of their market niche. Both systems require the same two main processes performed at different assembly lines.

- Process 1 is usually completed in 3 days for System 1 and in 5 days for System 2.
- Process 2 requires 6 days for System 1 and 9 days for System 2.
- The company has 25 days available for Process 1 and 40 days available for Process 2.
- System 1 is sold for $200, while System 2 is sold for $350.

### (a) [10 points]
Formulate the problem as a linear programming model (Solving the model is not required).

### (b) [15 points]
As a result of current business, the company is moving to a new location. Management now considers that maximizing profit is not a realistic goal, and it sets a profit level of $1500 for a certain time interval of initial adjustment. Also, management attempts to obtain an improved utilization of the assembly lines for the two processes (Process 1 and Process 2).

While management is concerned about the underachievement of the profit level and the idle time for the two assembly lines, it is NOT concerned about overachievement of the profit target and overtime for the two assembly lines.

Re-formulate the problem as a goal programming model (Solving the model is not required).

---

## Question 3 (25 points) — Dynamic Programming

How to drive from NYC to LA on the shortest path?

Stages: f1, f2, f3, f4

Nodes:
- f1: NYC (1)
- f2: C (2), N (3), L (4)
- f3: KC (5), OC (6), Dal (7)
- f4: LA (10)

Edge costs:

    NYC(1) -> C(2):   550
    NYC(1) -> N(3):   900
    NYC(1) -> L(4):   770

    C(2) -> KC(5):    680
    C(2) -> OC(6):    790
    C(2) -> Dal(7):  1050

    N(3) -> KC(5):    580
    N(3) -> OC(6):    760
    N(3) -> Dal(7):   660

    L(4) -> KC(5):    510
    L(4) -> OC(6):    700
    L(4) -> Dal(7):   830

    KC(5) -> LA(10): 1030
    OC(6) -> LA(10):  940
    Dal(7) -> LA(10): 1390

---

## Question 4 (30 points) — AHP

You are part of a team evaluating three drone platforms for surveillance missions:
- (i) AeroMax (A)
- (ii) SkyLite (B)
- (iii) FalconPro (C)

Evaluation criteria: Cost (C1), Payload Capacity (C2), Endurance (C3), and Ease of Integration (C4).

Pairwise comparison matrix for criteria:

         C1    C2    C3    C4
    C1    1    1/3   1/2    2
    C2    3     1     2     4
    C3    2    1/2    1     3
    C4   1/2   1/4   1/3    1

Tasks:
1. [10 points] Briefly interpret the matrix by stating what it says about the relative importance of the criteria.
2. [10 points] Compute the normalized weights and priority weights.
3. [5 points] Interpret priority weights.
4. [5 points] Define Consistency Index.
