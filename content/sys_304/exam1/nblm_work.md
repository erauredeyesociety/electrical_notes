## Question 2


Based on the sources provided, here is the formulation for both the Linear Programming (LP) and Goal Programming (GP) models for the engineering company.

### **(a) Linear Programming Model Formulation**
The objective of linear programming is to optimize a single evaluation function subject to linear constraints. In this case, the goal is to maximize total profit from selling the two systems.

**1. Define Decision Variables:**
*   $x_1$ = Number of units of System 1 to produce.
*   $x_2$ = Number of units of System 2 to produce.

**2. Objective Function:**
The objective is to maximize total profit based on the selling price of each system.
*   **Maximize $Z = 200x_1 + 350x_2$**

**3. Constraints:**
The constraints are based on the limited availability of days for each process.
*   **Process 1 Capacity:** $3x_1 + 5x_2 \leq 25$ days.
*   **Process 2 Capacity:** $6x_1 + 9x_2 \leq 40$ days.

**4. Non-negativity Constraints:**
The number of systems produced cannot be negative.
*   **$x_1, x_2 \geq 0$**

---

### **(b) Goal Programming Model Formulation**
Goal Programming is used when a decision maker faces multiple objectives and criteria. The formulation shifts from maximizing a single objective to **minimizing deviations** from set targets. Management has identified three goals: profit, Process 1 utilization, and Process 2 utilization.

**1. Define Decision and Deviational Variables:**
*   $x_1, x_2$ = Production quantities of Systems 1 and 2.
*   $d_i^-$ = Underachievement of goal $i$ (e.g., profit below target or idle time).
*   $d_i^+$ = Overachievement of goal $i$ (e.g., profit above target or overtime).

**2. Goal Constraints:**
The constraints are now equalities that incorporate the deviational variables to show how the actual production relates to the target.

*   **Goal 1 (Profit Target):** $200x_1 + 350x_2 + d_1^- - d_1^+ = 1500$
*   **Goal 2 (Process 1 Utilization):** $3x_1 + 5x_2 + d_2^- - d_2^+ = 25$
*   **Goal 3 (Process 2 Utilization):** $6x_1 + 9x_2 + d_3^- - d_3^+ = 40$

**3. Objective Function (Minimize Deviations):**
Management specifically states they are **only** concerned about underachievement of the profit level ($d_1^-$) and idle time on the assembly lines ($d_2^-, d_3^-$). They are **not** concerned about overachievement or overtime ($d_1^+, d_2^+, d_3^+$).

*   **Minimize $P = d_1^- + d_2^- + d_3^-$**

**4. Non-negativity Constraints:**
All decision and deviational variables must be greater than or equal to zero.
*   **$x_1, x_2, d_1^-, d_1^+, d_2^-, d_2^+, d_3^-, d_3^+ \geq 0$**


## Question 3

To find the shortest path from NYC to LA using **Dynamic Programming**, we employ the principle of **backward induction**, starting from the final destination (Stage 4) and working back to the origin (Stage 1).

### **Step 1: Stage 3 to Stage 4 (Final Destination)**
Calculate the cost to reach LA (Node 10) from each node in Stage 3.
*   $f_3(5) = \text{KC to LA} = \mathbf{1030}$
*   $f_3(6) = \text{OC to LA} = \mathbf{940}$
*   $f_3(7) = \text{Dal to LA} = \mathbf{1390}$

---

### **Step 2: Stage 2 to Stage 3**
Determine the minimum cost to reach LA from each node in Stage 2 by evaluating all paths through Stage 3.

**From C (Node 2):**
*   Path 2 $\to$ 5 $\to$ 10: $680 + 1030 = 1710$
*   Path 2 $\to$ 6 $\to$ 10: $790 + 940 = 1730$
*   Path 2 $\to$ 7 $\to$ 10: $1050 + 1390 = 2440$
*   **Minimum $f_2(2) = 1710$ (via Node 5)**

**From N (Node 3):**
*   Path 3 $\to$ 5 $\to$ 10: $580 + 1030 = 1610$
*   Path 3 $\to$ 6 $\to$ 10: $760 + 940 = 1700$
*   Path 3 $\to$ 7 $\to$ 10: $660 + 1390 = 2050$
*   **Minimum $f_2(3) = 1610$ (via Node 5)**

**From L (Node 4):**
*   Path 4 $\to$ 5 $\to$ 10: $510 + 1030 = 1540$
*   Path 4 $\to$ 6 $\to$ 10: $700 + 940 = 1640$
*   Path 4 $\to$ 7 $\to$ 10: $830 + 1390 = 2220$
*   **Minimum $f_2(4) = 1540$ (via Node 5)**

---

### **Step 3: Stage 1 to Stage 2**
Determine the absolute shortest path from NYC (Node 1) to LA by comparing paths through Stage 2.

*   Path 1 $\to$ 2 $\to$ LA: $550 + 1710 = \mathbf{2260}$
*   Path 1 $\to$ 3 $\to$ LA: $900 + 1610 = 2510$
*   Path 1 $\to$ 4 $\to$ LA: $770 + 1540 = 2310$

---

### **Final Recommendation**
The shortest path from NYC to LA is found by selecting the alternative with the **minimum total cost**.

*   **Optimal Path:** **NYC (1) $\to$ C (2) $\to$ KC (5) $\to$ LA (10)**
*   **Total Shortest Distance/Cost:** **2260**

**Rationale:** By using dynamic programming to evaluate sub-problems in a consistent manner, we identified that while node 4 has a very efficient connection to node 5, the high initial cost to get to node 4 from NYC makes the path through node 2 more efficient overall. This "error-embracing" iterative approach ensures that all potential "blind alleys" are avoided in favor of the mathematical optimum.


## Question 4

Based on the sources provided, here is the comprehensive evaluation of the drone surveillance platforms using the **Analytic Hierarchy Process (AHP)**.

### **1. Interpretation of the Pairwise Comparison Matrix**
The matrix uses a 1–9 scale where a value of **1 signifies equal importance** and higher values signify increasing strength of preference.
*   **Payload Capacity (C2)** is the most critical criterion. It is **moderately preferred (3)** over Cost (C1), **equally to moderately preferred (2)** over Endurance (C3), and **moderately to strongly preferred (4)** over Ease of Integration (C4).
*   **Endurance (C3)** is the second most important factor, being **equally to moderately preferred (2)** over Cost (C1) and **moderately preferred (3)** over Ease of Integration (C4).
*   **Cost (C1)** is **equally to moderately preferred (2)** specifically over Ease of Integration (C4).
*   **Ease of Integration (C4)** is the least important criterion, as shown by its reciprocal values (less than 1) when compared against all other factors.

### **2. Normalized Weights and Priority Weights**
To compute the weights, we first find the sum of each column, then divide each element by its column total (normalization), and finally average the rows.

**Step 1: Calculate Column Totals**
*   **C1 Sum:** $1 + 3 + 2 + 0.5 = \mathbf{6.5}$
*   **C2 Sum:** $0.333 + 1 + 0.5 + 0.25 = \mathbf{2.083}$
*   **C3 Sum:** $0.5 + 2 + 1 + 0.333 = \mathbf{3.833}$
*   **C4 Sum:** $2 + 4 + 3 + 1 = \mathbf{10.0}$

**Step 2: Normalized Matrix (Element / Column Total)**
| | C1 | C2 | C3 | C4 |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | 0.1538 | 0.1600 | 0.1304 | 0.2000 |
| **C2** | 0.4615 | 0.4800 | 0.5217 | 0.4000 |
| **C3** | 0.3077 | 0.2400 | 0.2609 | 0.3000 |
| ****C4**** | 0.0769 | 0.1200 | 0.0870 | 0.1000 |

**Step 3: Priority Weights (Average of each row)**
1.  **Cost (C1):** $(0.1538 + 0.1600 + 0.1304 + 0.2000) / 4 = \mathbf{0.161}$
2.  **Payload (C2):** $(0.4615 + 0.4800 + 0.5217 + 0.4000) / 4 = \mathbf{0.466}$
3.  **Endurance (C3):** $(0.3077 + 0.2400 + 0.2609 + 0.3000) / 4 = \mathbf{0.277}$
4.  **Integration (C4):** $(0.0769 + 0.1200 + 0.0870 + 0.1000) / 4 = \mathbf{0.096}$

### **3. Interpretation of Priority Weights**
The priority weights quantify the **relative importance of each factor** in the overall decision.
*   **Payload Capacity (46.6%)** is the dominant requirement for this mission, carrying nearly half the total decision weight.
*   **Endurance (27.7%)** follows as a significant second priority.
*   **Cost (16.1%)** is considered a secondary concern compared to technical capabilities.
*   **Ease of Integration (9.6%)** is a minor factor in selecting the drone platform.

### **4. Definition of Consistency Index (CI)**
The **Consistency Index (CI)** is a mathematical indicator used to measure the **magnitude of departure from perfect cardinal consistency** in a decision-maker's subjective judgments. It is calculated as:
$$CI = \frac{\lambda_{\text{max}} - N}{N - 1}$$
Where **$N$ is the size of the comparison matrix** and **$\lambda_{\text{max}}$ is the average of the consistency vector**. The CI is compared against a **Random Index (RI)** to determine the **Consistency Ratio (C.R.)**; if the C.R. is $\leq 0.10$, the judgments are considered acceptably consistent.