# SYS 304: Trade Studies, Risk, and Decision Analysis

## Test 1: Fall 2026

**Name:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Question 1 [5×2 = 10 points]

Define the following terms and give one engineering-related example for each. Use first line for definition and second to provide an example.

A. Risk

B. Uncertainty

C. Conditional Probability

D. Prior Probability

E. Perfect Information

---

## Question 2 [30 points]: Multiple Choice Questions

**A. [1 point]** In a payoff table, the rows typically represent:

- a. States of nature
- b. Decision alternatives
- c. Probabilities
- d. Regret values

**B. [2 points]** The Maximin rule selects the alternative with:

- a. Largest maximum payoff
- b. Largest minimum payoff
- c. Smallest regret
- d. Largest EMV

**C. [2 points]** A dominated alternative should:

- a. Always be selected
- b. Be eliminated from consideration
- c. Be averaged with others
- d. Be evaluated using Bayes

**D. [2 points]** In a probability tree, the joint probability along a path is found by:

- a. Adding branch probabilities
- b. Multiplying branch probabilities
- c. Subtracting conditional probabilities
- d. Dividing by prior probability

**E. [2 points]** The denominator in Bayes' theorem is computed using:

- a. EMV (Expected Monetary Value or Expected Value)
- b. Maximax
- c. Law of Total Probability
- d. Minimax regret

**F. [2 points]** EMV is calculated as:

- a. Maximum payoff
- b. Minimum payoff
- c. Probability-weighted average payoff
- d. Difference between best and worst payoff

**G. [2 points]** If the probability of success increases, the EMV of a high-profit project will:

- a. Decrease
- b. Remain constant
- c. Increase
- d. Become zero

**H. [2 points]** The Minimax Regret rule selects the alternative that:

- a. Minimizes the maximum regret
- b. Maximizes expected value
- c. Maximizes minimum payoff
- d. Eliminates uncertainty

**I. [2 points]** EVPI is always:

- a. Negative
- b. Zero
- c. Greater than or equal to zero
- d. Equal to study cost

**J. [2 points]** A rational decision maker should purchase sample information if:

- a. EVSI > Cost of study
- b. EVSI < Cost of study
- c. EMV decreases
- d. EVPI = 0

**K. [3 points]** A project yields $100 if successful and -$40 if it fails. Probability of success = 0.6. EMV equals:

- a. $36
- b. $40
- c. $44
- d. $60

**L. [2 points]** When solving a decision tree, the correct procedure is to:

- a. Start at first decision node
- b. Evaluate probabilities only
- c. Roll back from terminal nodes
- d. Compare maximum payoffs directly

**M. [2 points]** If a test has 90% sensitivity and 10% false positive rate, and prior defect rate is 5%, the posterior probability after a positive test will be:

- a. Less than 5%
- b. Equal to 5%
- c. Greater than 5%
- d. Equal to 90%

**N. [2 points]** If one alternative has higher payoffs in every state of nature than another, then:

- a. Compare EMV
- b. Compare regret
- c. The weaker alternative is dominated
- d. Compute EVPI

**O. [2 points]** If probabilities are unknown and cannot be reasonably estimated, EMV should:

- a. Be used normally
- b. Be replaced with Bayes' theorem
- c. Not be used; use uncertainty criteria instead
- d. Equal zero

---

## Question 3 [10 points]

Explain the concept of the *Fallacy of Expected Value*. Provide an example that was not discussed in class or included in the lecture notes.


---

## Question 4 [20 points = 4Q × 5pts]

A renewable energy company must choose one of three project alternatives. Market demand next year can be High, Moderate, or Low. The projected profits (in $ thousands) are shown below:

| Alternative        | High | Moderate | Low  |
|--------------------|------|----------|------|
| Solar Farm (A1)    | 300  | 150      | -50  |
| Wind Farm (A2)     | 250  | 200      | 0    |
| Hybrid System (A3) | 400  | 100      | -150 |

Assume the probabilities of demand levels are unknown.

Apply the following decision analysis models:

1. Aspiration level criterion with an assumed aspiration level of $100,000
2. Expected value criterion. Assume probabilities P(High) = 0.3, P(Moderate) = 0.5, and P(Low) = 0.2
3. Laplace criterion
4. Hurwicz with a optimism coefficient α = 0.6

---

## Question 5 [30 points]

The systems engineering project manager for ENG company is currently faced with the question of whether to award a $100,000 contract to SW software company. The project manager has three internal ratings (poor risk, average risk, and good risk) for evaluation of a contractor, but does not know which category fits the SW software company. Internal ratings indicate that 20% of similar companies are poor risks, 50% are average risks, and 30% are good risks. If contract is awarded, the expected profit for poor risk is -$15,000, for average risk $10,000, and for good risk $20,000. If contract is not awarded, the ENG company expected payoff is $0.

| Alternatives                          | Poor Risk (20%) | Average Risk (50%) | Good Risk (30%) |
|---------------------------------------|-----------------|--------------------|-----------------| 
| Award Contract to SW software         | -$15,000        | $10,000            | $20,000         |
| Do not Award Contract to SW software  | $0              | $0                 | $0              |

The project manager can consult an external rating organization for a fee of $5,000. For each of the three internal ratings, the following table shows the percentages given through external ratings as poor, average, and good risks.

| External Rating (Findings) | Poor Risk (20%) | Average Risk (50%) | Good Risk (30%) |
|----------------------------|-----------------|--------------------|-----------------| 
| Poor Risk                  | 50%             | 40%                | 20%             |
| Average Risk               | 40%             | 50%                | 40%             |
| Good Risk                  | 10%             | 10%                | 40%             |

a) **[5 points]** Assuming the external rating is not used, determine which alternative should be chosen.

b) **[10 points]** Assume the external rating organization is used. Develop a probability tree diagram to find the posterior probabilities of the respective states of nature for each of the three possible ratings of the potential SW software company.

Consider:

- PF = Poor Finding, AF = Average Finding, GF = Good Finding
- PS = Poor State, AS = Average State, GS = Good State

c) **[15 points]** Build the decision tree and identify the resulting optimal policy for ENG Company.