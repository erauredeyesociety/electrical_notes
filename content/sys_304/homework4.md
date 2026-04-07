# SYS 304 Homework 4

## Question 1 – Linear Programming (30 points)

A company produces two types of unmanned aerial vehicle components:

- x1: navigation units
- x2: communication units

Each unit requires labor, testing time, and raw material as shown below.

| Resource     | x1 per unit | x2 per unit | Available |
|---|---|---|---|
| Labor hours  | 4 | 3 | 240 |
| Testing hours| 2 | 5 | 200 |
| Material units| 3 | 2 | 180 |

Profit contribution:
- Navigation unit: $60 each
- Communication unit: $50 each

### (a) Formulation (10 points)

Formulate this as a linear programming model. Clearly define:
- decision variables
- objective function
- all constraints
- nonnegativity conditions

### (b) Solution by algebraic/solver method (10 points)

Solve the model using an algebraic method or optimization software. Report:
- optimal values of x1 and x2
- maximum profit

### (c) Constraint analysis (5 points)

Identify which constraints are binding at the optimum and explain what that means operationally.

### (d) Engineering interpretation (5 points)

Explain how this model supports decision making in an engineering production environment.

---

## Question 2 – Dynamic Programming (30 points)

A vehicle must travel from Node 1 to Node 8 through a sequence of stages. Travel costs between connected nodes are given below.

### Stage structure

- Stage 1: Node 1
- Stage 2: Nodes 2, 3
- Stage 3: Nodes 4, 5
- Stage 4: Node 8

### Travel costs

| From | To | Cost |
|---|---|---|
| 1 | 2 | 7 |
| 1 | 3 | 5 |
| 2 | 4 | 6 |
| 2 | 5 | 4 |
| 3 | 4 | 3 |
| 3 | 5 | 8 |
| 4 | 8 | 6 |
| 5 | 8 | 2 |

### (a) Stages and states (5 points)

Identify the stages and the states in each stage.

### (b) Backward recursion (15 points)

Use dynamic programming and work backward from the last stage to compute the cost-to-go functions. Show each step clearly.

### (c) Optimal path (5 points)

Determine the minimum total cost and the optimal path from Node 1 to Node 8.

### (d) Explanation (5 points)

Briefly explain why dynamic programming is appropriate for this problem.

---

## Question 3 – Goal Programming (40 points)

A manufacturer produces two products:

- x: Product 1
- y: Product 2

The weekly processing requirements are:

| Resource  | Constraint |
|---|---|
| Machine 1 | 0.2x + 0.5y <= 50 |
| Machine 2 | 0.4x + 0.2y <= 40 |
| Machine 3 | 0.3x + 0.3y <= 45 |

Profit contribution:
- Product 1: $12 per unit
- Product 2: $18 per unit

Demand limits:
- x <= 90
- y <= 90

Management has established the following goals:

1. Priority 1: Achieve at least $1,400 profit
2. Priority 2: Minimize total unused machine capacity

### (a) Goal programming formulation (15 points)

Formulate the problem as a goal programming model. Include:
- decision variables
- deviation variables
- goal constraints
- system constraints
- preemptive priority objective function

### (b) Deviation variables (10 points)

Explain the meaning of each deviation variable in the model. Indicate which deviations are undesirable and why.

### (c) Solution logic (10 points)

Describe the sequence used to solve the goal programming model under preemptive priorities. You do not need to fully solve numerically, but you must explain the process clearly.

### (d) Interpretation (5 points)

Explain why goal programming is more suitable than standard linear programming for this problem.

---

## Optional Bonus (5 points)

Compare linear programming, dynamic programming, and goal programming in terms of:
- type of problem each addresses
- main advantage
- main limitation
