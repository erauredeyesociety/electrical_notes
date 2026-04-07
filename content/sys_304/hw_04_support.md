# SYS 304 HW4 Support Document — Class Material References

This document explains why each answer in hw_04_solutions.md is structured the way it is, referencing specific class materials.

---

## Q1: Linear Programming

The class materials ("02 Decision Making with Multiple Objectives 1") cover MCDM and establish the need for single-dimensioned analysis (collapsing multiple criteria into one metric) vs full-dimensioned analysis. LP is the foundational single-objective optimization method.

The LP formulation follows standard OR procedure:
- Decision variables represent quantities to be determined (Slide 2: "basic question: which alternative to select")
- Objective function is the single metric being optimized (profit)
- Constraints represent resource limits (labor, testing, material)
- The corner-point method is used because LP theory guarantees the optimum lies at a vertex of the feasible region

The constraint analysis (binding vs non-binding) connects to the "limiting factors" concept from "01 Trade Studies" (Slide 5): "Factors restricting accomplishment of desired objectives." Binding constraints are the limiting factors. The "strategic factors" are those that can be altered to make progress — here, increasing labor or testing capacity.

The engineering interpretation (part d) connects to "01 Trade Studies" Slide 4: "Comparing alternatives equivalently — need to be converted to a common measure. Use money flow models, economic optimization models." LP provides exactly this quantitative basis.

Note: The class materials do not include explicit LP lecture slides (the optimization topics appear to be supplementary to the main decision analysis curriculum). The LP, DP, and GP methods are standard operations research techniques that complement the MCDM framework taught in the course.

---

## Q2: Dynamic Programming

DP is appropriate for sequential/multi-stage decisions — this connects to the "01 Trade Studies" concept that "throughout a project there are several tradeoff studies performed" (Slide 3). Each stage in the DP represents a decision point.

The backward recursion method (Bellman's principle of optimality) is the standard DP solution approach: working from the terminal state back to the initial state, computing the optimal cost-to-go at each node. This is standard OR material.

The stage structure is given directly in the problem. The solution correctly identifies:
- 4 stages with the states at each stage
- Cost-to-go at each node computed backward
- Optimal path traced forward: 1->2->5->8, cost=13

No corrections needed. The DP solution follows standard textbook procedure.

---

## Q3: Goal Programming

Goal programming directly addresses the MCDM framework from "02 Decision Making with Multiple Objectives 1":
- Slide 2: "Single-objective models developed in 1960s and 1970s are considered by many to be unrealistic, too restrictive, and often inadequate for real-world problems"
- Slide 2: "Multiple-Criteria Decision Making (MCDM) — objectives: minimizing cost, maximizing benefits, and minimizing risks of various kinds"

GP extends LP by handling multiple objectives with priority ordering, which is exactly what the class material motivates. The preemptive priority method solves sequentially, ensuring higher-priority goals are never sacrificed for lower-priority ones.

The deviation variables (d_plus and d_minus) represent over- and under-achievement of each goal. The formulation correctly:
- Treats machine capacities as constraints with slack variables for Goal 2
- Uses d1_minus (profit shortfall) as the Priority 1 objective
- Uses total machine slack as the Priority 2 objective
- Applies preemptive sequential solving

The interpretation (part d) directly references the MCDM motivation from the class: GP is preferred when there are multiple conflicting objectives that cannot be meaningfully combined into a single weighted metric.

---

## Bonus

The comparison of LP, DP, and GP ties together three optimization paradigms:
- LP = single objective, foundational (from "01 Trade Studies" economic optimization models)
- DP = sequential decisions (from the concept of staged decision-making)
- GP = multiple objectives (from "02 Decision Making with Multiple Objectives" MCDM framework)

This comparison is well-supported by the class materials' progression from single-objective to multi-criteria decision making.

No corrections needed for HW4 solutions.
