# SYS 304 Homework 5 — Solutions

---

## I. Problem M1-9 (25 pts) — Gina Fox University Selection using AHP

Gina Fox must choose among three universities (A, B, C) based on three factors: cost (weight 0.6), reputation (weight 0.2), and quality of life (weight 0.2). Her direct ratings are:

    Cost:       A=4, B=8, C=7
    Reputation: A=9, B=5, C=6
    Quality:    A=7, B=7, C=3

Using MFEP, we compute the total weighted evaluation for each university:

    University A: 0.6(4) + 0.2(9) + 0.2(7) = 2.4 + 1.8 + 1.4 = 5.6
    University B: 0.6(8) + 0.2(5) + 0.2(7) = 4.8 + 1.0 + 1.4 = 7.2
    University C: 0.6(7) + 0.2(6) + 0.2(3) = 4.2 + 1.2 + 0.6 = 6.0

University B has the highest total weighted evaluation (7.2), so Gina should select University B.

---

## II. Problem M1-10 (25 pts) — Gina Fox Revisited with AHP

Gina is not comfortable with her direct ratings, so she uses AHP pairwise comparisons instead. We are given:

On cost: B strongly preferred to A (5), B moderately preferred to C (3), C moderately preferred to A (3).
On reputation: A very strongly preferred to B (7), C moderately preferred to B (3), A strongly preferred to C (5).
On quality of life: A and B equally preferred (1), A strongly preferred to C (5), B very strongly preferred to C (7).

On the three factors: cost very strongly preferred to quality of life (7), cost moderately preferred to reputation (3), reputation equally to moderately preferred to quality of life (2).

Step 1 — Build pairwise comparison matrices and compute priority weights for each.

Criteria comparison matrix:

              Cost    Rep    QoL
    Cost       1       3      7
    Rep       1/3      1      2
    QoL       1/7     1/2     1

Column sums: 1 + 0.333 + 0.143 = 1.476; 3 + 1 + 0.5 = 4.5; 7 + 2 + 1 = 10

Normalized matrix:
    Cost: 0.677, 0.667, 0.700 -> average = 0.681
    Rep:  0.226, 0.222, 0.200 -> average = 0.216
    QoL:  0.097, 0.111, 0.100 -> average = 0.103

Criteria weights: Cost = 0.681, Reputation = 0.216, Quality of Life = 0.103

Consistency check:
    [A]*[B] = [1,3,7; 1/3,1,2; 1/7,1/2,1] * [0.681; 0.216; 0.103] = [2.069; 0.665; 0.311]
    [D] = [2.069/0.681, 0.665/0.216, 0.311/0.103] = [3.038, 3.079, 3.019]
    lambda_max = (3.038 + 3.079 + 3.019)/3 = 3.045
    CI = (3.045 - 3)/(3 - 1) = 0.023
    CR = 0.023/0.58 = 0.039 < 0.10 -- acceptable

Cost comparison matrix (universities):

              A      B      C
    A         1     1/5    1/3
    B         5      1      3
    C         3     1/3     1

Column sums: 9, 1.533, 4.333

Normalized and averaged:
    A: 0.111, 0.130, 0.077 -> 0.106
    B: 0.556, 0.652, 0.692 -> 0.633
    C: 0.333, 0.217, 0.231 -> 0.260

Cost priorities: A=0.106, B=0.633, C=0.260

Consistency: lambda_max approx 3.04, CI=0.02, CR=0.03 -- acceptable

Reputation comparison matrix:

              A      B      C
    A         1      7      5
    B        1/7     1     1/3
    C        1/5     3      1

Column sums: 1.343, 11, 6.333

Normalized and averaged:
    A: 0.745, 0.636, 0.789 -> 0.723
    B: 0.106, 0.091, 0.053 -> 0.083
    C: 0.149, 0.273, 0.158 -> 0.193

Reputation priorities: A=0.723, B=0.083, C=0.193

Consistency: lambda_max approx 3.07, CI=0.03, CR=0.06 -- acceptable

Quality of Life comparison matrix:

              A      B      C
    A         1      1      5
    B         1      1      7
    C        1/5    1/7     1

Column sums: 2.2, 2.143, 13

Normalized and averaged:
    A: 0.455, 0.467, 0.385 -> 0.435
    B: 0.455, 0.467, 0.538 -> 0.487
    C: 0.091, 0.067, 0.077 -> 0.078

QoL priorities: A=0.435, B=0.487, C=0.078

Consistency: lambda_max approx 3.01, CI=0.005, CR=0.009 -- acceptable

Step 2 — Compute overall priority weights.

    A: 0.681(0.106) + 0.216(0.723) + 0.103(0.435) = 0.072 + 0.156 + 0.045 = 0.273
    B: 0.681(0.633) + 0.216(0.083) + 0.103(0.487) = 0.431 + 0.018 + 0.050 = 0.499
    C: 0.681(0.260) + 0.216(0.193) + 0.103(0.078) = 0.177 + 0.042 + 0.008 = 0.227

University B has the highest overall priority weight (0.499). Gina should select University B.

This result is consistent with the MFEP answer from M1-9, confirming that B is the best choice. The AHP approach gives more confidence because it uses structured pairwise comparisons rather than direct subjective ratings.

---

## III. AHP Python Program (50 pts)

See the file ahp_program.py in this folder. The program:
- Uses the decision problem from Slide 8 (manufacturing modernization: 5 criteria, 3 alternatives)
- Accepts Saaty pairwise comparison values as input arrays
- Computes normalized matrices, priority weight vectors, consistency ratios
- Shows Level II (criteria) and Level III (alternative) weights
- Shows overall priority weights and selects the best alternative
- Computes local CRs for each matrix and the global CRH
- Flags any CR > 0.10 as inconsistent

---

## IV. Systematic Elimination Methods

We are given three alternatives (A, B, C) against four criteria (higher is better):

    Criterion | A   | B   | C   | Ideal | Min Standard
    1         | 6   | 5   | 8   | 10    | 7
    2         | 90  | 80  | 75  | 100   | 70
    3         | 40  | 35  | 50  | 50    | 30
    4         | G   | P   | VG  | E     | F

For criterion 4, we use the ordinal scale: P < F < G < VG < E.

### 1. Dominance (comparing alternatives against each other)

Alternative X dominates alternative Y if X is at least as good as Y on all criteria and strictly better on at least one.

Compare A vs B:
    Crit 1: A=6 > B=5
    Crit 2: A=90 > B=80
    Crit 3: A=40 > B=35
    Crit 4: A=G > B=P
    A is better on all four criteria. A dominates B.

Compare A vs C:
    Crit 1: A=6 < C=8
    Crit 2: A=90 > C=75
    Crit 3: A=40 < C=50
    Crit 4: A=G < C=VG
    Neither dominates the other (mixed results).

Compare B vs C:
    Crit 1: B=5 < C=8
    Crit 2: B=80 > C=75
    Crit 3: B=35 < C=50
    Crit 4: B=P < C=VG
    Neither dominates the other.

Conclusion: B is dominated by A and can be eliminated. A and C remain — neither dominates the other, so further analysis is needed.

### 2. Comparing against a standard (Rules 1 and 2)

Rule 1 (conjunctive screening): An alternative must meet the minimum standard on ALL criteria to remain feasible.

    Alternative A: Crit 1: 6 < 7 (FAILS). A does not meet the minimum standard.
    Alternative B: Crit 1: 5 < 7 (FAILS). B does not meet the minimum standard.
    Alternative C: Crit 1: 8 >= 7, Crit 2: 75 >= 70, Crit 3: 50 >= 30, Crit 4: VG >= F. All pass.

Under Rule 1 (conjunctive), only C survives. A and B fail criterion 1.

Rule 2 (disjunctive screening): An alternative is acceptable if it meets the ideal on at least one criterion.

    Alternative A: No criterion meets the ideal (6<10, 90<100, 40<50, G<E). Fails.
    Alternative B: No criterion meets the ideal. Fails.
    Alternative C: Crit 3: 50 = 50 (MEETS ideal). Passes.

Under Rule 2 (disjunctive), only C survives.

Conclusion: C is the only alternative that passes both screening methods.

### 3. Comparing criteria across alternatives (criteria ranked 2 > 3 > 1 > 4)

When criteria have different importance levels, we compare alternatives starting with the most important criterion first.

Most important: Criterion 2
    A=90, B=80, C=75. A is best on criterion 2.

Second most important: Criterion 3
    A=40, B=35, C=50. C is best on criterion 3.

Third: Criterion 1
    A=6, B=5, C=8. C is best on criterion 1.

Least important: Criterion 4
    A=G, B=P, C=VG. C is best on criterion 4.

Using lexicographic ordering (decide by most important criterion first): A wins on criterion 2 (the most important), so A would be selected under strict lexicographic ordering.

However, if we consider the overall picture: C is best on 3 out of 4 criteria (criteria 1, 3, and 4), while A is only best on criterion 2. Also from the screening analysis, A fails the minimum standard on criterion 1. So while A wins on the highest-priority criterion, C is the stronger overall candidate.

Conclusion: Under strict lexicographic ordering by importance, A is selected (best on criterion 2). But considering that A fails the minimum standard on criterion 1, C is the more practical choice.
