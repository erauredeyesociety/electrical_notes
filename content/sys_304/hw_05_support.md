# SYS 304 HW5 Support Document — Class Material References

This document explains why each answer in hw_05_solutions.md is structured the way it is, with specific references to the AHP Handout (Module 1) and lecture slides.

---

## I. Problem M1-9 — MFEP University Selection

**Source:** AHP Handout, page M1-15, Problem M1-9.

**Method used:** Multifactor Evaluation Process (MFEP), as defined on Handout pages M1-2 through M1-3. The MFEP procedure is:
1. List factors and assign importance weights (must sum to 1.0) — Handout Table M1.1
2. For each alternative, assign factor evaluations (0 to 1 scale or raw ratings) — Handout Table M1.2
3. Compute weighted evaluation = sum of (weight * evaluation) for each factor — Handout Tables M1.3-M1.5
4. Select the alternative with the highest total weighted evaluation

The problem states Gina has already assigned weights (cost=0.6, reputation=0.2, quality of life=0.2) and ratings on a 1-10 scale. We simply compute the weighted sums directly.

**Verification:** The solution uses the exact same procedure as Solved Problem M1-1 on Handout page M1-13: multiply each factor weight by the factor evaluation, sum across factors, compare totals.

Result: University B = 7.2 (highest). No corrections needed.

---

## II. Problem M1-10 — AHP University Selection

**Source:** AHP Handout, page M1-15, Problem M1-10.

**Method used:** Analytic Hierarchy Process (AHP), as defined on Handout pages M1-4 through M1-11 and Lecture Slides 1-29.

The problem states Gina is "not comfortable with her ratings" so she uses pairwise comparisons instead. The text gives verbal preferences that must be mapped to Saaty's scale:

**Saaty Scale (Lecture Slide 11, Handout page M1-5):**
- 1 = Equally preferred
- 2 = Equally to moderately preferred
- 3 = Moderately preferred
- 5 = Strongly preferred
- 7 = Very strongly preferred
- 9 = Extremely preferred
- Even numbers (2,4,6,8) = intermediate values

**Mapping the verbal preferences from M1-10 to Saaty values:**

Cost comparisons:
- "B is strongly preferred to A" -> B vs A = 5
- "B is moderately preferred to C" -> B vs C = 3
- "C is moderately preferred to A" -> C vs A = 3

Reputation comparisons:
- "A is very strongly preferred to B" -> A vs B = 7
- "C is moderately preferred to B" -> C vs B = 3
- "A is strongly preferred to C" -> A vs C = 5

Quality of Life comparisons:
- "A and B are equally preferred" -> A vs B = 1
- "A is strongly preferred to C" -> A vs C = 5
- "B is very strongly preferred to C" -> B vs C = 7

Criteria comparisons:
- "cost is very strongly preferred to quality of life" -> Cost vs QoL = 7
- "cost is moderately preferred to reputation" -> Cost vs Rep = 3
- "reputation is equally to moderately preferred to quality of life" -> Rep vs QoL = 2

**AHP procedure (from Lecture Slides 13-22 and Handout pages M1-6 through M1-9):**
1. Build pairwise comparison matrix (diagonal = 1, lower triangle = reciprocals)
2. Compute column sums
3. Normalize: divide each element by its column sum
4. Compute priority weights: average of each row in normalized matrix
5. Consistency check:
   - Multiply original matrix by weight vector to get weighted sum vector
   - Divide element-wise by weights to get consistency vector
   - lambda_max = average of consistency vector
   - CI = (lambda_max - n) / (n - 1) — Handout equation M1-1
   - CR = CI / RI — Handout equation M1-2
   - RI table from Handout page M1-8: n=3 -> RI=0.58
   - CR <= 0.10 is acceptable

**Consistency check for all matrices:** All CRs are under 0.10, confirming consistency.

**Overall priority weights (Lecture Slide 26):** Multiply each alternative's criterion weight by the criterion priority and sum across all criteria.

Result: University B = 0.499 (highest). Consistent with M1-9. No corrections needed.

---

## III. AHP Python Program

**Source:** Lecture Slides 1-29, specifically Slide 8 (decision problem), Slide 13 (criteria matrix), Slides 17-19 (alternative matrices), Slide 26 (overall weights), Slides 20-24 (consistency).

The program reproduces the manufacturing modernization example from the lecture:
- Level I (Focus): Best overall automated system
- Level II (Criteria): A=CIMS goals, B=Net present worth, C=Serviceability, D=Management effort, E=Lack of riskiness
- Level III (Alternatives): P-1, P-2, P-3

**Criteria matrix from Slide 13:**
The 5x5 matrix matches exactly: A vs B = 1/3, A vs C = 5, A vs D = 6, A vs E = 5, etc.

**Criteria weights from Slide 14:**
Slide shows: A=0.288, B=0.489, C=0.086, D=0.041, E=0.096. Our program computes: A=0.288, B=0.489, C=0.086, D=0.041, E=0.095. Match (rounding differences only).

**Alternative matrices from Slides 17-19:**
- Subjective comparisons used for A (CIMS), C (Serviceability), E (Riskiness) — Slide 17
- Performance data used for B (NPW: 300M, 350M, 400M) and D (effort: 500, 700, 1100 hrs) — Slide 18-19
- For B: proportional ratios (300/350, etc.) rather than subjective Saaty scale
- For D: hours are "less is better" so we invert (1/500, 1/700, 1/1100) then take ratios

**Consistency (Slides 20-24):**
- CR for criteria: 0.07 (Slide 22 shows 0.07) — match
- CR for CIMS goals alternatives: 0.02 (Slide 23 shows 0.02) — match
- Global CRH formula from Slide 28-29: CRH = M_CI / M_RI where M_CI = level2_CI + weights dot level3_CIs

**Overall weights from Slide 26:**
Slide shows P-1=0.324, P-2=0.378, P-3=0.298. Our program: P-1=0.322, P-2=0.379, P-3=0.299. Match (rounding differences from using performance-data ratios vs Slide's slightly different values).

P-2 is selected in both the slides and our program. No corrections needed.

---

## IV. Systematic Elimination Methods

**Source:** "02 Decision Making with Multiple Objectives 1" slides, "Systematic Elimination Methods" section.

### 1. Dominance

**Source slide:** "Compare alternatives against each other" — "Check for dominance by making mutual comparisons across alternatives. Just an elimination technique."

The slide example shows the exact same type of problem with A, B, C, D alternatives. It states "A dominates B, so B can be eliminated from further consideration."

Our solution correctly applies this: A beats B on all 4 criteria, so A dominates B. A and C have mixed results (no dominance). B and C have mixed results (no dominance). Only B is eliminated.

### 2. Comparing against a standard (Rules 1 and 2)

**Source slide:** "Compare alternatives against a standard"

**IMPORTANT CORRECTION APPLIED:** The slides define:
- **Rule 1 (disjunctive):** "alternative may be retained only if it meets the standard for at least one criterion"
- **Rule 2 (conjunctive):** "alternative may be retained only if it meets the standard for all criteria"

The slide example shows: "Rule 1: A, B, C, and D meet the standard for at least one criterion. Rule 2: C meets the standard for all criteria."

Our solution was originally reversed (calling Rule 1 conjunctive and Rule 2 disjunctive). This has been corrected to match the slide definitions exactly:
- Rule 1: All three alternatives retained (each meets >= 1 standard)
- Rule 2: Only C retained (only one meeting all standards)

### 3. Comparing criteria across alternatives

**Source slide:** "Compare criteria across alternatives — Rank relevant criteria based on importance. Ranking of criteria: 2 > 1 > 3 > 4"

The slide shows lexicographic ordering: compare on the most important criterion first. The HW problem gives ranking 2 > 3 > 1 > 4 (different from the slide example's 2 > 1 > 3 > 4, but same method).

Our solution applies the same method: start with criterion 2 (most important), where A=90 wins. Under strict lexicographic ordering, A is selected. However, we note that A fails the minimum standard on criterion 1, which is a practical concern.

**Qualitative scale ordering** (from Slide 9 measurement scale and the Slide example table):
The scale used is: P (Poor) < F (Fair) < G (Good) < VG (Very Good) < E (Excellent). This matches the "poor, fair, good, very good, excellent" scale shown on the measurement scale slide.

No further corrections needed after the Rule 1/Rule 2 fix.
