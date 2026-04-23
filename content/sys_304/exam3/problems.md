# SYS 304 Exam 3 Problems

Source images:
- `original_photos/1.jpg`
- `original_photos/2.jpg`
- `original_photos/3.jpg`
- `original_photos/4.jpg`
- `original_photos/5.jpg`

Helpful derived crops are stored in `cropped_photos/`.

This is a cleaner transcription of the exam. Where the original used diagrams or partial photos, I rewrote the figure content in plain English instead of trying to redraw it.

## Question 1 (20 pts): Multiple Choice

### 1.1 (2 pts)
In a two-person, zero-sum game, what does "zero-sum" mean?

A. Both players always win the same amount  
B. One player's gain is exactly equal to the other player's loss  
C. The total payoff to both players is always positive  
D. Each player must use mixed strategies

### 1.2 (2 pts)
A dominated strategy is defined as a strategy that:

A. Always results in a saddle point  
B. Guarantees the highest possible payoff  
C. Is always at least as bad as another strategy, regardless of the opponent's choice  
D. Can only be used in mixed-strategy games

### 1.3 (2 pts)
The minimax criterion states that Player 1 should choose the strategy that:

A. Maximizes the maximum payoff  
B. Minimizes the opponent's payoff  
C. Maximizes the minimum payoff they can guarantee  
D. Randomizes all strategies equally

### 1.4 (2 pts)
A game lacks a saddle point when:

A. Both players have dominated strategies  
B. Maximin value equals the minimax value  
C. Maximin value is less than the minimax value  
D. The payoff table contains only zeros

### 1.5 (3 pts)
Given the following information from a QFD House of Quality:

- Customer Requirement `CR1` has importance `5`
- The relationship between `CR1` and Technical Requirement `TR1` is strong (value `9`)
- The relationship between `CR2` (importance `4`) and `TR1` is medium (value `3`)
- The relationship between `CR3` (importance `3`) and `TR1` is weak (value `1`)

What is the technical importance of `TR1`?

A. `15`  
B. `45`  
C. `54`  
D. `57`

Note: the visible numbers in the photo imply `5*9 + 4*3 + 3*1 = 60`, but `60` does not appear among the printed answer choices.

### 1.6 (3 pts)
A QFD analysis produces the following technical importance values:

- `TR1: 57`
- `TR2: 69`
- `TR3: 30`
- `TR4: 48`

If the engineering team can focus on only two technical requirements, which ones should they prioritize?

A. `TR1` and `TR3`  
B. `TR3` and `TR4`  
C. `TR2` and `TR1`  
D. `TR2` and `TR4`

### 1.7 (2 pts)
What is the primary purpose of the House of Quality in QFD?

A. To identify the least expensive components in a system  
B. To translate customer requirements into measurable technical requirements  
C. To optimize product cost without considering customer input  
D. To compare competitor products only

### 1.8 (2 pts)
According to the Systems Analysis process, why does the client not fully understand their own problem?

A. Clients focus only on the technical details  
B. Clients are typically new to their domain  
C. Clients are part of the problem and may hide or misunderstand aspects of it  
D. Analysts have more authority and thus know the problem better

### 1.9 (2 pts)
Why is simulation often preferred over analytical solutions in problems like the Newsvendor model?

A. Analytical solutions are always incorrect  
B. Simulation allows estimation of performance when analytical solutions are difficult or impossible due to randomness  
C. Simulation removes all randomness from the system  
D. Simulation guarantees the optimal solution every time

## Question 2 (25 pts = 10 + 10 + 5)

Consider the following payoff matrix for Player 1 in a two-person, zero-sum game. Player 1 chooses a row (`R1`-`R4`) and Player 2 chooses a column (`C1`-`C4`). The entry in the table is the payoff to Player 1.

| Player 1 \\ Player 2 | C1 | C2 | C3 | C4 |
| --- | ---: | ---: | ---: | ---: |
| R1 | 2 | 3 | 1 | 4 |
| R2 | 3 | 4 | 3 | 5 |
| R3 | 1 | 3 | 0 | 3 |
| R4 | 2 | 5 | 2 | 3 |

Answer:

a) Determine Player 1's maximin value and corresponding strategy.  
b) Determine Player 2's minimax value and corresponding strategy.  
c) Determine whether a saddle point exists.

Figure description:
The page shows a standard payoff table with rows `R1`-`R4` for Player 1 and columns `C1`-`C4` for Player 2. No extra annotations appear beyond the numeric payoffs.

## Question 3 (20 pts)

Create a Quality Function Deployment (QFD) example based on your own experience. Describe the product or service being designed and then complete its House of Quality. Limit the number of customer requirements and design features/attributes to a maximum of eight each. Include at least three competitors for benchmarking.

Scoring criteria:
- Roof: `5` points
- Requirements and design features: `5` points
- Technical importance: `15` points
- Benchmarking and target features: `5` points

Figure description:
The exam includes a blank House of Quality worksheet. In paragraph form, it contains:
- a triangular roof / tradeoff matrix at the top
- customer requirements down the left side
- "importance" columns to the right of the customer requirements but to the left of the design characteristics
- design characteristics across the top just under the tradeoff matrix
- a relationship matrix in the center between the customer requirements and design characteristics (importance is sandwiched between the customer requirements and the relationship matrix)
- objective measures / targets along the bottom underneath the customer requirements and their rows intersect with the design characteristics
- a competitive assessment block to the direct right of the relationship matrix

Step-by-step worksheet fill guide:

1. Choose the product or service.
- Write a short description of what you are designing.
- Keep it concrete enough that customer needs and measurable design features are easy to define.

2. Fill in the customer requirements block on the left.
- List the customer requirements down the far-left side, one per row.
- Keep the number of customer requirements to at most eight.
- Phrase them as user needs or "what the customer wants."

3. Fill in the importance area next to the customer requirements.
- Assign an importance rating to each customer requirement.
- Put those importance values in the narrow columns just to the right of the customer-requirements list.
- These values sit before the main relationship matrix begins.

4. Fill in the design characteristics across the top.
- Write the technical requirements / engineering attributes across the top of the matrix.
- These go directly under the roof.
- Keep the number of design characteristics to at most eight.
- Phrase them as measurable technical features or "how the design will meet the need."

5. Fill in the roof / tradeoff matrix.
- Use the triangular roof at the top to show how design characteristics interact with each other.
- Mark positive relationships where improving one characteristic helps another.
- Mark negative relationships where improving one characteristic hurts another.
- This is where you show tradeoffs among the technical features.

6. Fill in the central relationship matrix.
- At each intersection of a customer requirement row and a design characteristic column, enter the relationship strength.
- Use the class QFD relationship scale such as strong, medium, weak, or the matching numbers.
- Leave cells blank where there is no meaningful relationship.

7. Compute and fill in technical importance.
- For each design characteristic column, calculate the weighted sum using customer importance times relationship value.
- Record those technical-importance totals in the section associated with the technical columns.
- These values help identify which design characteristics should be prioritized.

8. Fill in the competitive assessment block on the right.
- Compare at least three competitors.
- Place the competitor ratings in the block to the right of the main relationship matrix.
- These ratings are tied to the customer-requirement side of the worksheet and help show where competitors are strong or weak.

9. Fill in the bottom objective / target area.
- Under the technical columns, write objective measures, units, direction of improvement, and target values as needed.
- This bottom area connects the design characteristics to measurable goals.
- Use it to show what final performance level the design should aim for.

10. Review the whole House of Quality as one system.
- Check that the most important customer requirements are strongly connected to at least some technical features.
- Check that the roof reflects the biggest technical tradeoffs.
- Make sure the technical-importance totals, benchmarking, and targets all support the same design story.

## Question 4 (35 points)

A cart can move on a `40`-foot-long track and can be moved in either direction. The goal is to push or pull the cart so that it returns to the center of the track.

Variables:
- position `x` in feet
- velocity `v` in feet per second
- control force `F` in newtons

The cart's position is described using the fuzzy set:
- `Left`
- `Middle`
- `Right`

The cart's velocity is described using the fuzzy set:
- `Moving Left`
- `Standing Still`
- `Moving Right`

The control force is described using the fuzzy set:
- `Pull`
- `None`
- `Push`

Interpretation:
- `Pull` means applying force to move the cart to the left
- `Push` means applying force to move the cart to the right

Figure description:
The page shows a cart slightly left of the track center, at about the `-10 ft` location, on a horizontal track whose left edge is `-20 ft` and right edge is `20 ft`. Two arrows above the cart indicate that the cart can move either left or right.

### Fuzzy ranges given in the photo

#### Position of cart

| Fuzzy set | Range (ft) |
| --- | --- |
| Left | `-20` to `0` |
| Middle | `-10` to `10` |
| Right | `0` to `20` |

#### Velocity of cart

| Fuzzy set | Range (ft/s) |
| --- | --- |
| Moving Left | `-1` to `0` |
| Standing Still | `-0.5` to `1` |
| Moving Right | `0` to `2` |

#### Control force

| Fuzzy set | Range (N) |
| --- | --- |
| Pull | `-1` to `0` |
| None | `-0.5` to `0.5` |
| Push | `0` to `1` |

### Fuzzy rule base shown in the photos

1. If Position of Cart is `Left` and Velocity of Cart is `Moving Left`, then Control Force is `Push`.  
2. If Position of Cart is `Left` and Velocity of Cart is `Standing Still`, then Control Force is `Push`.  
3. If Position of Cart is `Left` and Velocity of Cart is `Moving Right`, then Control Force is `None`.  
4. If Position of Cart is `Middle` and Velocity of Cart is `Moving Left`, then Control Force is `Push`.  
5. If Position of Cart is `Middle` and Velocity of Cart is `Standing Still`, then Control Force is `None`.  
6. If Position of Cart is `Middle` and Velocity of Cart is `Moving Right`, then Control Force is `Pull`.  
7. If Position of Cart is `Right` and Velocity of Cart is `Moving Right`, then Control Force is `Pull`.  
8. If Position of Cart is `Right` and Velocity of Cart is `Standing Still`, then Control Force is `Pull`.  
9. If Position of Cart is `Right` and Velocity of Cart is `Moving Left`, then Control Force is `None`.

Answer the following:

a) Develop the fuzzy membership functions for the fuzzy variables `Position of Cart`, `Velocity of Cart`, and `Control Force`.  
b) Let the cart be positioned at `Position of Cart = 5 ft`, and have a velocity of `Velocity of Cart = 0.8 ft/s`. Eliminate the rules that do not apply to this scenario.  
c) After eliminating the rules that do not apply, use the Sup-Min Operation Method to develop the control action rules for controlling the cart. Please use the similar approach as the one followed in slides 39-40 of the `Fuzzy Theory in Decision Analysis` PPT.
