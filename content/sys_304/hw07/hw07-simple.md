Here is the simplified, cleaned-up version of the entire homework solution, with no extra notation, no "pts" labels, and no advanced equations — just straightforward answers.

---

# SYS 304 — Homework 7: QFD & Simulation

## Question 1 — QFD Calculations

### Given data

| Customer requirement (importance) | Battery capacity (E1) | Motor efficiency (E2) | Payload capacity (E3) |
|:--------------------------------|:---------------------:|:---------------------:|:---------------------:|
| Fast delivery (5)               |           3           |           9           |           3           |
| Low cost (4)                    |           9           |           3           |           3           |
| Reliability (5)                 |           3           |           9           |           1           |

Scale: 9 = strong, 3 = medium, 1 = weak

---

### a) Technical importance weights

Multiply each customer importance by the relationship score, then add across each column.

**E1 (Battery capacity):**  
(5 × 3) + (4 × 9) + (5 × 3) = 15 + 36 + 15 = 66

**E2 (Motor efficiency):**  
(5 × 9) + (4 × 3) + (5 × 9) = 45 + 12 + 45 = 102

**E3 (Payload capacity):**  
(5 × 3) + (4 × 3) + (5 × 1) = 15 + 12 + 5 = 32

---

### b) Normalized weights

Add up all weights: 66 + 102 + 32 = 200  
Divide each weight by this total.

| Engineering characteristic | Raw weight | Normalized weight |
|:--------------------------|:----------:|:-----------------:|
| E1 — Battery capacity     |     66     |       0.33        |
| E2 — Motor efficiency     |    102     |       0.51        |
| E3 — Payload capacity     |     32     |       0.16        |

---

### c) Most important engineering characteristic

**Motor efficiency (E2)** is most important because it has the highest normalized weight (0.51).

---

## Question 2 — Interpreting QFD

**Why motor efficiency ranks highest.**  
Motor efficiency has a strong relationship (score 9) with both fast delivery and reliability. These two customer requirements have the highest importance (5 each). So motor efficiency gets more total weighted points than any other engineering characteristic.

**One trade-off revealed by the QFD.**  
Increasing battery capacity usually adds weight, which reduces payload capacity. This is a trade-off: you cannot maximize both at the same time. The design team must decide which one matters more based on customer priorities.

---

## Question 3 — Integration of Simulation and QFD

Simulation results help improve QFD decisions by showing real numbers, not just rankings. For example, simulation can tell you how much profit changes if motor efficiency improves, or how often you lose money. If simulation shows that profit is too uncertain, you might raise the importance of reliability in the QFD.

**Example of a design change based on risk or uncertainty.**  
If simulation shows a high chance of losing money on low-demand days, you might reduce the number of delivery slots per day (q) to avoid paying for unused slots. This changes how you balance cost versus service level.

---

## Question 4 — Newsvendor Simulation Setup

### a) Profit function

Profit = (revenue per delivery × actual deliveries made) – (cost per slot × slots scheduled)

Actual deliveries made = the smaller of (demand) and (slots scheduled)

So:  
Profit = 12 × min(q, D) – 7 × q

Where:  
- q = slots scheduled per day  
- D = random daily demand

---

### b) How to simulate demand using a spreadsheet

You set up a spreadsheet with many rows, each row = one simulated day.

In the demand column, use a formula like `=NORM.INV(RAND(), mean, std_dev)` to generate random daily demand. This gives you a different demand value for each row.

Then, in the profit column, use:  
`=12 * MIN(scheduled_slots, demand) – 7 * scheduled_slots`

Copy these formulas down for many rows (like 50 or 100 rows).

Then take the **average** of all the profit numbers to see expected profit for that number of slots.

To find the best number of slots, try a few different values (like 20, 30, 40, 50, 60) and see which one gives the highest average profit.

No code needed — just basic spreadsheet formulas.

---

### c) What happens if q is too large vs. too small

**If q is too large (too many slots scheduled):**  
On days with low demand, you pay for slots that stay empty. Profit can become negative. You waste money on unused capacity.

**If q is too small (not enough slots scheduled):**  
On days with high demand, you turn away customers because you have no open slots. You miss out on extra revenue you could have earned.

The best q balances these two problems: enough slots to capture most demand, but not so many that you waste money on empty slots.