# SYS 304 Test 2 — Reference Material

This document maps each question to the relevant class material.

---

## Q1: Trade Study Selection

Source: "02 Decision Making with Multiple Objectives 1" slides

Key concepts:
- Systematic elimination methods (slides on "Compare alternatives against each other", "Compare alternatives against a standard")
- Dominance: A dominates B if A is at least as good on all criteria and strictly better on at least one
- Hard constraint (Z): the alternative MUST meet the threshold — any alternative failing Z is eliminated regardless of other performance
- Soft constraints (X, Y, V): desirable but not mandatory — used for trade-off comparison among surviving alternatives
- Equivalent cost: the primary selection criterion among alternatives that pass all hard constraints and are competitive on soft constraints
- The trade study chart plots each alternative's performance vs thresholds for each criterion

## Q2a: Linear Programming

Source: standard LP formulation (complements "02 Decision Making with Multiple Objectives 1" Slide 2 on single-objective optimization)

LP formulation steps:
1. Define decision variables (what we control)
2. Write objective function (what we optimize — here, maximize profit)
3. Write constraints (resource limits — here, available days for each process)
4. Add nonnegativity

## Q2b: Goal Programming

Source: "02 Decision Making with Multiple Objectives 1" and "02 Decision Making with Multiple Objectives 2" slides

Key concepts:
- GP extends LP for multiple conflicting objectives
- Deviation variables: d_plus (overachievement) and d_minus (underachievement) for each goal
- Goal constraints: activity + d_minus - d_plus = target
- The problem states which deviations are undesirable:
  - "concerned about underachievement of profit" -> minimize d_profit_minus
  - "concerned about idle time" -> minimize d_process1_minus and d_process2_minus (slack = idle time)
  - "NOT concerned about overachievement of profit" -> d_profit_plus is OK
  - "NOT concerned about overtime" -> d_process1_plus and d_process2_plus are OK

## Q3: Dynamic Programming

Source: standard DP backward recursion (Bellman's principle of optimality)

Key concepts:
- Stages = columns (f1 through f4)
- States = nodes within each stage
- Backward recursion: start at destination (LA), compute cost-to-go at each node working backward
- f(s) = min over all next nodes j of { cost(s->j) + f(j) }
- Optimal path traced forward after all f values computed

## Q4: AHP

Source: "03 The Analytic Hierarchy Process" lecture slides AND "03 Analytic Hierarchy Process_Handout" (Module 1)

Key concepts:
- Saaty scale: 1=equal, 3=moderate, 5=strong, 7=very strong, 9=extreme (Slide 11, Handout p.M1-5)
- Pairwise comparison matrix: diagonal=1, lower=reciprocal of upper (Handout p.M1-6)
- Normalization: divide each element by its column sum (Handout p.M1-7)
- Priority weights: row averages of normalized matrix (Handout p.M1-7)
- Consistency Index: CI = (lambda_max - n) / (n - 1) where n = matrix size (Handout eq. M1-1, p.M1-8)
- lambda_max: average of the consistency vector (weighted sum vector / priority weights)
- CR = CI / RI; RI for n=4 is 0.90 (Handout p.M1-8)
- CR <= 0.10 is acceptable
- Interpreting the matrix: read off which criteria are preferred over which and by how much
