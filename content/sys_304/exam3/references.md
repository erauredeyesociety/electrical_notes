# SYS 304 Exam 3 References and Verification Notes

## Source Set

### Exam artifacts

- Original photos:
  - [1.jpg](/home/devel/electrical_notes/content/sys_304/exam3/original_photos/1.jpg)
  - [2.jpg](/home/devel/electrical_notes/content/sys_304/exam3/original_photos/2.jpg)
  - [3.jpg](/home/devel/electrical_notes/content/sys_304/exam3/original_photos/3.jpg)
  - [4.jpg](/home/devel/electrical_notes/content/sys_304/exam3/original_photos/4.jpg)
  - [5.jpg](/home/devel/electrical_notes/content/sys_304/exam3/original_photos/5.jpg)
- Derived crops:
  - [cropped_photos](/home/devel/electrical_notes/content/sys_304/exam3/cropped_photos)

### Solution diagrams (Python-generated)

Scripts and images live in [python_photos/](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/). Each script uses matplotlib with `Agg` backend and writes its output next to itself. Rerun any script with `python3 <script>` to regenerate the PNG.

| Script | Image(s) | Purpose |
| --- | --- | --- |
| [01_membership_functions.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/01_membership_functions.py) | [01a_position_membership.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/01a_position_membership.png), [01b_velocity_membership.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/01b_velocity_membership.png), [01c_force_membership.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/01c_force_membership.png) | Q4(a) — triangular/shoulder membership functions for position, velocity, and control force; position and velocity plots are annotated at the exam inputs `x = 5 ft` and `v = 0.8 ft/s`. |
| [02_sup_min_rules.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/02_sup_min_rules.py) | [02_sup_min_rule_grid.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/02_sup_min_rule_grid.png) | Q4(c) — 4 × 3 grid of the four active rules showing antecedent evaluation, min firing strength, and clipped consequent for each rule. |
| [03_aggregation.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/03_aggregation.py) | [03a_output_aggregation.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/03a_output_aggregation.png) | Q4(c) — clipped consequent sets, max-aggregated output `μ_agg(F)`, and numerically computed centroid `F* ≈ -0.40 N`. |
| [04_qfd_house_of_quality.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/04_qfd_house_of_quality.py) | [04_qfd_house_of_quality.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/04_qfd_house_of_quality.png) | Q3 — full House of Quality for the commuter-backpack example with roof, relationship matrix, technical importance, competitive assessment, and target row. |
| [05_game_theory_saddle.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/05_game_theory_saddle.py) | [05_game_theory_payoff_saddle.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/05_game_theory_payoff_saddle.png) | Q2 — payoff matrix with row minima, column maxima, and the `(R2, C1)` / `(R2, C3)` saddle points highlighted. |
| [06_rule_activation_grid.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/06_rule_activation_grid.py) | [06_rule_activation_grid.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/06_rule_activation_grid.png) | Q4(b) — 3 × 3 rule grid with rules 5, 6, 7, 8 highlighted by consequent and the other five rules struck through. |
| [07_sup_min_slide_style.py](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/07_sup_min_slide_style.py) | [07_sup_min_slide_style.png](/home/devel/electrical_notes/content/sys_304/exam3/python_photos/07_sup_min_slide_style.png) | Q4(c) — slide 39-40 layout: three clipped-consequent panels (Pull, None, Push) plus a wide union-envelope panel with centroid marker. Keeps our `α = 0.4 / 0.2` values. |

All diagrams are solution-side artifacts — they render what a student would produce as their answer, not what the exam page shows as the problem.

### Q4(c) membership-function interpretation note

A TA reference shared by the student (`tmp.webp` in this directory, converted to `tmp_ref.png`) uses a slide 39-40 layout with `α = 0.5` for Pull and `α ≈ 0.267` for None. Those values come from interpreting `Standing Still` as a symmetric triangle over `[-0.5, 1]` peaked at `v = 0.25` (giving `μ_StandingStill(0.8) = (1 − 0.8) / (1 − 0.25) = 4/15 ≈ 0.267`) and placing the `Moving Right` peak at `v = 1.6` rather than at the bound `v = 2`. Our solutions use the simpler textbook convention with each "middle" set peaked at the center of its numeric sense (`Standing Still` at `v = 0`, `Moving Right` as a shoulder ramp over `[0, 2]`), giving `α = 0.4 / 0.2`. Both interpretations produce the same qualitative result: `Pull` dominates and `F* ≈ -0.40 N`.

### Saved course-material text extracts

- [04 Fuzzy Theory in Decision Analysis.txt](/home/devel/electrical_notes/content/sys_304/exam3/pdf_text_notes/04%20Fuzzy%20Theory%20in%20Decision%20Analysis.txt)
- [05 Game Theory.txt](/home/devel/electrical_notes/content/sys_304/exam3/pdf_text_notes/05%20Game%20Theory.txt)
- [06 Quality Function Deployment.txt](/home/devel/electrical_notes/content/sys_304/exam3/pdf_text_notes/06%20Quality%20Function%20Deployment.txt)
- [07 Simulation Approaches 1.txt](/home/devel/electrical_notes/content/sys_304/exam3/pdf_text_notes/07%20Simulation%20Approaches%201.txt)
- [08 Systems Analysis Process.txt](/home/devel/electrical_notes/content/sys_304/exam3/pdf_text_notes/08%20Systems%20Analysis%20Process.txt)

### Primary lecture decks

- [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf)
- [06 Quality Function Deployment.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/06%20Quality%20Function%20Deployment.pdf)
- [07 Simulation Approaches 1.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/07%20Simulation%20Approaches%201.pdf)
- [08 Systems Analysis Process.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/08%20Systems%20Analysis%20Process.pdf)
- [04 Fuzzy Theory in Decision Analysis.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/04%20Fuzzy%20Theory%20in%20Decision%20Analysis.pdf)

### Supporting course notes already in repo

- [hw06.md](/home/devel/electrical_notes/content/sys_304/hw06/hw06.md:1)
- [hw07.md](/home/devel/electrical_notes/content/sys_304/hw07/hw07.md:1)
- [topics_list.md](/home/devel/electrical_notes/content/sys_304/topics_list.md:26)

## Verification Summary

I re-checked the Exam 3 answers against the actual SYS 304 lecture decks most directly tied to these topics:

- Game Theory for Q1.1-Q1.4 and Q2
- Quality Function Deployment for Q1.5-Q1.7 and Q3
- Systems Analysis Process for Q1.8
- Simulation Approaches 1 for Q1.9
- Fuzzy Theory in Decision Analysis for Q4

The result:

- Q1.1, Q1.2, Q1.3, Q1.4, Q1.6, Q1.7, Q1.8, Q1.9 are well supported by lecture material.
- Q2 is fully supported by the Game Theory lecture treatment of maximin, minimax, and saddle points.
- Q3 is structurally supported by the QFD lecture deck; the specific backpack example is my own constructed example, as the exam requires.
- Q4 methodology is supported by the Fuzzy Theory lecture deck, especially the Sup-Min procedure on slides 39-40.
- Q1.5 remains the one unresolved item: the visible exam numbers produce `60`, but the printed choices do not include `60`.

Additional review-pass note:

- Q3 and Q4 were rechecked against the updated diagram descriptions in [problems.md](/home/devel/electrical_notes/content/sys_304/exam3/problems.md:124).
- Q3 now uses the more accurate worksheet-layout interpretation: customer requirements on the far left, importance immediately to their right, design characteristics across the top under the roof, relationship matrix in the center, competitive assessment to the right of that matrix, and objective / target information along the bottom.
- Q4 wording now consistently uses the corrected cart position description near `-10 ft`.

## Per-Question Verification

### Q1.1 Zero-sum game

Verified against [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf), slide 3.

Relevant lecture language:

> "Called zero-sum games because one player wins whatever the other one loses"

That directly supports answer `B`.

### Q1.2 Dominated strategy

Verified against [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf), slide 11.

Relevant lecture language:

> "always at least as good (and sometimes better)"

This matches answer `C`: a dominated strategy is always at least as bad as another strategy regardless of opponent choice.

### Q1.3 Minimax / maximin criterion for Player 1

Verified against [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf), slide 23.

Relevant lecture language:

> "Player 1 should select the strategy whose minimum payoff is largest."

That is exactly answer `C`.

Note:
The exam says "minimax criterion" for Player 1, but the lecture slide describes the Player 1 rule as choosing the largest row minimum, i.e. the usual maximin step for Player 1. The answer choice `C` still matches the course treatment.

### Q1.4 When a game lacks a saddle point

Verified against [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf):

- slide 24: saddle point is the same entry giving both maximin and minimax values
- slide 26: lecture example explicitly says "No saddle point"

Relevant lecture language from slide 24:

> "Same entry in the payoff table yields both the maximin and the minimax values."

Therefore, if those values are not equal, there is no saddle point. In the exam choices, that corresponds to answer `C`:

```text
maximin < minimax
```

### Q1.5 Technical importance of TR1

Verified against [06 Quality Function Deployment.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/06%20Quality%20Function%20Deployment.pdf), slide 9.

Relevant lecture language:

> "Technical Importance... weighted sum"

More specifically, slide 9 says technical importance is estimated as a weighted sum of relationship values, weighted by customer importance ratings.

Applying that to the visible exam data:

```text
TR1 = 5*9 + 4*3 + 3*1 = 45 + 12 + 3 = 60
```

But the answer choices in the photo are:

- `15`
- `45`
- `54`
- `57`

Conclusion:

- the lecture method supports the calculation
- the visible exam numbers support `60`
- the printed choices do not

This is still the main ambiguity in the exam set.

Additional note:
Because Q1.6 later lists `TR1 = 57`, `57` may have been the instructor's intended carry-over value, but that is not what the photographed Q1.5 data produce.

### Q1.6 Which technical requirements should be prioritized

Verified against [06 Quality Function Deployment.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/06%20Quality%20Function%20Deployment.pdf), slide 9.

Once technical importance values are available, the lecture logic is to prioritize the highest values first.

Given:

- `TR1 = 57`
- `TR2 = 69`
- `TR3 = 30`
- `TR4 = 48`

The top two are:

- `TR2`
- `TR1`

So answer `C` is supported.

### Q1.7 Purpose of the House of Quality

Verified against [06 Quality Function Deployment.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/06%20Quality%20Function%20Deployment.pdf), slide 4.

Relevant lecture language:

> "translating customer needs into specific system or product characteristics"

and

> "house of quality to translate the needs or requirements into the necessary technical requirements"

That directly supports answer `B`.

### Q1.8 Why the client does not fully understand the problem

Verified against [08 Systems Analysis Process.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/08%20Systems%20Analysis%20Process.pdf), slide 4.

Relevant lecture language:

> "Rule 2: Your client does not understand his own problem."

and

> "Client is part of the problem"

This supports answer `C`.

### Q1.9 Why simulation is often preferred

Verified against [07 Simulation Approaches 1.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/07%20Simulation%20Approaches%201.pdf):

- slide 4: classic newsvendor problem has exact-solution literature, but it is still easy to simulate
- slide 5: simulation gives `E(W(q))`, confidence interval, `P(loss)`, and histogram

Relevant lecture language from slide 4:

> "Much research on exact solution in certain cases. But easy to simulate"

Relevant lecture language from slide 5:

> "estimate E(W(q))"

and

> "confidence interval, estimate of P(loss), histogram"

That supports answer `B`: simulation is attractive because it lets us estimate performance under randomness.

## Question 2 Verification

Verified against [05 Game Theory.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/05%20Game%20Theory.pdf), slides 23-24.

### Course rule used

Slide 23:

> "Player 1 should select the strategy whose minimum payoff is largest."

and

> "Player 2 should select the strategy whose maximum payoff to Player 1 is the smallest."

Slide 24:

> "Same entry in the payoff table yields both the maximin and the minimax values."

### Scratch work

Payoff matrix:

| Row | Values | Row minimum |
| --- | --- | ---: |
| R1 | `2, 3, 1, 4` | `1` |
| R2 | `3, 4, 3, 5` | `3` |
| R3 | `1, 3, 0, 3` | `0` |
| R4 | `2, 5, 2, 3` | `2` |

So Player 1 maximin value is:

```text
max(1, 3, 0, 2) = 3
```

and Player 1 chooses `R2`.

Column maxima:

| Column | Values | Column maximum |
| --- | --- | ---: |
| C1 | `2, 3, 1, 2` | `3` |
| C2 | `3, 4, 3, 5` | `5` |
| C3 | `1, 3, 0, 2` | `3` |
| C4 | `4, 5, 3, 3` | `5` |

So Player 2 minimax value is:

```text
min(3, 5, 3, 5) = 3
```

and Player 2 can choose `C1` or `C3`.

Because:

```text
maximin = minimax = 3
```

a saddle point exists.

## Question 3 Verification

The exam asks for a student-created QFD example, so there is no single lecture-correct product choice. What can be verified is whether the structure of the solution matches the House of Quality taught in class.

Verified against [06 Quality Function Deployment.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/06%20Quality%20Function%20Deployment.pdf):

- slide 4: translation from customer needs to technical requirements
- slide 8: customer requirements and optional greenhouse / correlation area
- slide 9: system requirements and technical importance
- slide 18: rows are customer requirements, columns are technical requirements
- slide 24: competitive evaluation / benchmarking

### What in the current Q3 solution is course-aligned

- customer requirements on the left
- importance values immediately to the right of the customer requirements
- technical requirements across the top
- relationship matrix between them
- technical-importance calculations
- roof / tradeoff discussion
- competitor benchmarking
- target values

### Q3 worksheet-fill logic

This interpretation is consistent with the updated problem description and with the lecture deck:

- slide 8 of the QFD deck covers customer requirements and the importance side of the HoQ
- slide 9 covers technical requirements and technical importance
- slide 24 covers competitive evaluation

So the current solution structure matches the intended worksheet flow:

1. customer requirements
2. importance
3. technical requirements
4. roof / tradeoffs
5. relationship matrix
6. technical importance
7. competitive assessment
8. objective measures / targets

### Q3 note on point total

The exam image says `Question 3 (20 pts)`, but the visible scoring breakdown on the page sums to `30`:

- Roof `5`
- Requirements and design features `5`
- Technical importance `15`
- Benchmarking and target features `5`

So the printed point breakdown appears internally inconsistent.

## Question 4 Verification

Verified against [04 Fuzzy Theory in Decision Analysis.pdf](/home/devel/electrical_notes/content/sys_304/class_materials/04%20Fuzzy%20Theory%20in%20Decision%20Analysis.pdf):

- slide 38: fuzzy control rules setup
- slide 39: Sup-Min operation method graphical setup
- slide 40: Sup-Min control-action aggregation

Relevant lecture language on slide 38:

> "Sup-min method defuzzification scheme."

The exam itself explicitly says to use the same style as slides 39-40, so those are the correct lecture references for methodology.

### Important limitation

The lecture slides support the inference method, but the exact membership-function geometry for the cart problem is not fully visible in the exam photos. The photos clearly give fuzzy ranges, but not fully drawn triangles / shoulders for every set.

So:

- the rule elimination work is strongly supported
- the Sup-Min aggregation logic is strongly supported
- the exact crisp output depends on a reasonable modeling assumption about the membership-function shapes

### Assumptions used in the current solution

- `Left` and `Right` treated as ramp / shoulder sets over their printed ranges
- `Middle`, `Standing Still`, and `None` treated as overlapping triangular sets

At `x = 5`, `v = 0.8`, this gives:

```text
mu_Middle(5) = 0.5
mu_Right(5) = 0.25
mu_StandingStill(0.8) = 0.2
mu_MovingRight(0.8) = 0.4
```

Active rules:

- Rule 5 -> `None` at `0.2`
- Rule 6 -> `Pull` at `0.4`
- Rule 8 -> `Pull` at `0.2`
- Rule 7 -> `Pull` at `0.25`

So the qualitative result is robust:

```text
dominant output = Pull
```

That interpretation is consistent with the physics of the problem as well: the cart is to the right of center and moving right, so a leftward corrective force is appropriate.

## Most Useful Slide References

If you want the shortest high-confidence review list while checking my work against the course materials yourself, these are the best slides to inspect:

- Game Theory:
  - slide 3: zero-sum definition
  - slide 11: dominated strategy definition
  - slide 23: maximin / minimax criterion
  - slide 24: saddle point definition
- QFD:
  - slide 4: purpose of House of Quality
  - slide 8: customer requirements / tradeoff structure
  - slide 9: technical importance formula
  - slide 18: rows vs columns structure
  - slide 24: competitive evaluation
- Systems Analysis:
  - slide 4: client does not understand own problem
  - slide 9: goal-centered approach
- Simulation:
  - slide 4: newsvendor formulation and why simulation is useful
  - slide 5: `E(W(q))`, confidence intervals, and `P(loss)`
  - slide 7: spreadsheet outputs
- Fuzzy Theory:
  - slide 38: rule setup
  - slides 39-40: Sup-Min procedure

## Outstanding Uncertainties

### 1.5 Multiple-choice mismatch

This is still the only major unresolved issue.

What is solid:

- the QFD lecture formula
- the photographed values

What is not solid:

- the match between those values and the printed choices

### Q4 exact crisp value

The qualitative control action `Pull` is well supported.

The exact numerical output, such as `F ≈ -0.40 N`, is assumption-dependent because the exam photos do not fully specify the membership-function graph shapes, only the ranges.
