# Lecture 21: DT System Analysis and the Unilateral z-Transform

**Textbook Reference:** Sections 10.7--10.9 (Pages 774--796)

---

## Part I: System Analysis with H(z)

### 1. Finding H(z) from a Difference Equation

Given a constant-coefficient difference equation:

```
sum_{k=0}^{N} a_k y[n-k] = sum_{k=0}^{M} b_k x[n-k]
```

Take the bilateral z-transform (zero initial conditions), replacing each delay y[n-k] with z^{-k} Y(z):

```
H(z) = Y(z)/X(z) = (b0 + b1 z^{-1} + ... + bM z^{-M}) / (a0 + a1 z^{-1} + ... + aN z^{-N})
```

### Worked Example: Difference Equation to H(z)

**System:** y[n] - 0.8 y[n-1] + 0.15 y[n-2] = x[n] + 2x[n-1]

**Step 1:** Replace delays with z^{-k}:
(1 - 0.8z^{-1} + 0.15z^{-2}) Y(z) = (1 + 2z^{-1}) X(z)

**Step 2:** Form H(z):
H(z) = (1 + 2z^{-1}) / (1 - 0.8z^{-1} + 0.15z^{-2})

**Step 3:** Factor denominator. Solve z^2 - 0.8z + 0.15 = 0:
z = (0.8 +/- 0.2)/2 => z1 = 0.5, z2 = 0.3

**Result:** H(z) = (1 + 2z^{-1}) / [(1 - 0.5z^{-1})(1 - 0.3z^{-1})]

Poles: z = 0.5, 0.3 (both inside unit circle). Zero: z = -2.

---

### 2. Causality and Stability Criteria

#### Causality Criterion
- h[n] = 0 for n < 0
- ROC must be the **exterior of a circle:** |z| > r_max (outside the outermost pole)
- For rational H(z): requires M <= N (numerator degree <= denominator degree in z^{-1})

#### Stability Criterion (BIBO)
- sum |h[n]| < inf
- ROC must **include the unit circle** (|z| = 1)

#### The Golden Rule: Causal + Stable

```
Causal + Stable  <==>  |p_i| < 1 for ALL poles p_i
```

**All poles must lie strictly inside the unit circle.**

Why: For a causal system, ROC is |z| > |p_max|. For the unit circle to be in the ROC, we need |p_max| < 1.

#### Stability Classification Table

| H(z) | Poles | \|p_i\| | Causal + Stable? |
|---|---|---|---|
| 1 / (1 - 0.5z^{-1}) | z = 0.5 | 0.5 < 1 | **Yes** |
| 1 / (1 - 1.2z^{-1}) | z = 1.2 | 1.2 > 1 | **No (unstable)** |
| 1 / (1 - z^{-1}) | z = 1 | 1 = 1 | **Marginally stable** |
| 1 / [(1 - 0.3z^{-1})(1 + 0.7z^{-1})] | z = 0.3, -0.7 | 0.3, 0.7 < 1 | **Yes** |

---

### 3. Complete System Analysis Pipeline (Worked Example)

**System:** y[n] - 0.5 y[n-1] = x[n], **Input:** x[n] = (0.8)^n u[n]

**Step 1: Find H(z).**
H(z) = 1 / (1 - 0.5z^{-1}), |z| > 0.5
Pole at z = 0.5 (inside unit circle => causal and stable).

**Step 2: Find X(z).**
X(z) = 1 / (1 - 0.8z^{-1}), |z| > 0.8

**Step 3: Y(z) = H(z) X(z).**
Y(z) = 1 / [(1 - 0.5z^{-1})(1 - 0.8z^{-1})], |z| > 0.8

**Step 4: Partial fractions.**
- Set z^{-1} = 2: A = -5/3
- Set z^{-1} = 1.25: B = 8/3

**Step 5: Invert.** Both poles inside ROC => both right-sided:

```
y[n] = [-5/3 (0.5)^n + 8/3 (0.8)^n] u[n]
```

**Step 6: Verify.**
- y[0] = -5/3 + 8/3 = 1 = x[0] (with y[-1] = 0)
- y[1] = 0.5(1) + 0.8 = 1.3 matches formula

---

### 4. Block Diagram Representations

Three basic building blocks in the z-domain:
- **z^{-1}**: Unit delay (one sample memory)
- **a**: Gain (scalar multiplier)
- **+**: Adder

A difference equation of order N requires exactly N memory elements (z^{-1} blocks).

---

## Part II: The Unilateral z-Transform

### 5. Definition

```
X_u(z) = sum_{n=0}^{inf} x[n] z^{-n}
```

Sum starts at n = 0 (not n = -inf). For causal signals, unilateral = bilateral.

---

### 6. The Key Property: Unilateral Time-Shift

This is where initial conditions enter the picture:

```
x[n - 1]  --Z_u-->  z^{-1} X_u(z) + x[-1]

x[n - 2]  --Z_u-->  z^{-2} X_u(z) + x[-2] + x[-1] z^{-1}
```

**General pattern for delay by m:**

```
x[n - m]  --Z_u-->  z^{-m} X_u(z) + x[-m] + x[-m+1] z^{-1} + ... + x[-1] z^{-(m-1)}
```

> **Key difference from Laplace:** The IC terms have a **plus** sign (not minus). Compare: y'(t) -> sY - y(0^-) has a minus sign, but z-domain y[n-1] -> z^{-1}Y **+** y[-1] has a plus sign.

---

### 7. Solving Difference Equations with Initial Conditions

#### Example 1: First-Order with IC

**Solve:** y[n] - 0.6 y[n-1] = (0.5)^n u[n], y[-1] = 4

**Step 1: Unilateral z-transform.**

Left side: Y(z) - 0.6[z^{-1}Y(z) + y[-1]] = (1 - 0.6z^{-1})Y(z) - 2.4

Right side: 1/(1 - 0.5z^{-1})

**Step 2: Solve for Y(z).**

(1 - 0.6z^{-1})Y(z) = 1/(1 - 0.5z^{-1}) + 2.4

Y(z) = 1/[(1 - 0.5z^{-1})(1 - 0.6z^{-1})] + 2.4/(1 - 0.6z^{-1})

**Step 3: Partial fractions on first term.**
- Set z^{-1} = 2: A = -5
- Set z^{-1} = 5/3: B = 6

**Step 4: Combine and invert.**

Y(z) = -5/(1 - 0.5z^{-1}) + 8.4/(1 - 0.6z^{-1})

```
y[n] = [-5(0.5)^n + 8.4(0.6)^n] u[n]
```

**Verify:** y[0] = -5 + 8.4 = 3.4. From ODE: 0.6(4) + 1 = 3.4. Matches.

#### Example 2: Second-Order (Zero-Input Response)

**Solve:** y[n] - 0.7 y[n-1] + 0.1 y[n-2] = 0, y[-1] = 1, y[-2] = 0

**Step 1: Unilateral z-transform.**
- Z_u{y[n-1]} = z^{-1}Y + y[-1] = z^{-1}Y + 1
- Z_u{y[n-2]} = z^{-2}Y + y[-2] + y[-1]z^{-1} = z^{-2}Y + z^{-1}

Substitute: Y - 0.7(z^{-1}Y + 1) + 0.1(z^{-2}Y + z^{-1}) = 0

(1 - 0.7z^{-1} + 0.1z^{-2})Y = 0.7 - 0.1z^{-1}

**Step 2: Factor.** z^2 - 0.7z + 0.1 = 0 => z = (0.7 +/- 0.3)/2 => poles at z = 0.5, z = 0.2

Y(z) = (0.7 - 0.1z^{-1}) / [(1 - 0.5z^{-1})(1 - 0.2z^{-1})]

**Step 3: Partial fractions.**
- Set z^{-1} = 2: A = 5/6
- Set z^{-1} = 5: B = -2/15

**Step 4: Invert.**

```
y[n] = [5/6 (0.5)^n - 2/15 (0.2)^n] u[n]
```

This is a **pure zero-input response** (no external input -- output entirely from initial conditions). Both modes decay since both poles are inside the unit circle.

**Verify:** y[0] = 5/6 - 2/15 = 21/30 = 0.7. From ODE: 0.7(1) - 0.1(0) = 0.7. Matches.

---

### 8. ZSR + ZIR Decomposition

```
y[n] = y_ZS[n] + y_ZI[n]
```

- **y_ZS[n] (zero-state response):** Output due to input alone, all initial conditions = 0
- **y_ZI[n] (zero-input response):** Output due to initial conditions alone, zero input

---

## 9. Laplace vs. z-Transform Comparison Table

| | Laplace (Lctrs 16--18) | z-Transform (Lctrs 19--21) |
|---|---|---|
| Converts | differential eqs -> algebra | difference eqs -> algebra |
| Delay operator | e^{-st0} | z^{-1} |
| Causal + Stable | poles in LHP (Re{p} < 0) | **poles inside \|z\| = 1 (\|p\| < 1)** |
| Unilateral IC property | y'(t) -> sY - y(0^-) | y[n-1] -> z^{-1}Y + y[-1] |
| FT exists | jw-axis in ROC | unit circle in ROC |

---

## 10. Procedure Checklist for Homework Problems

### To find the output of a DT system (zero initial conditions):
1. Write the difference equation
2. Take z-transform: replace delays with z^{-k}, form H(z) = Y(z)/X(z)
3. Factor denominator, find poles; check stability (all |p_i| < 1?)
4. Find X(z) of the input
5. Y(z) = H(z) X(z)
6. Partial fractions in z^{-1}
7. Invert each term using table pairs and ROC
8. Verify with initial-value theorem or by plugging n=0 back into ODE

### To solve with nonzero initial conditions:
1. Take the **unilateral** z-transform of the difference equation
2. Apply the shift property: y[n-m] -> z^{-m}Y + x[-m] + x[-m+1]z^{-1} + ... + x[-1]z^{-(m-1)}
3. Substitute known initial conditions (y[-1], y[-2], etc.)
4. Solve algebraically for Y(z)
5. Partial fractions and invert
6. Verify by plugging y[0] back into the original equation

---

## 11. Common Mistakes to Avoid

1. **"Inside unit circle" is NOT the same as "LHP":** z = -0.9 is stable (|z| = 0.9 < 1) even though it is on the negative real axis.
2. **Unilateral shift has a PLUS sign:** y[n-1] -> z^{-1}Y **+** y[-1]. (Laplace has a minus: sY **-** y(0^-).)
3. **z^{-1} means delay, not advance:** x[n-1] <-> z^{-1}X(z). For advance: x[n+1] <-> zX(z) - zx[0] (unilateral).
4. **Pole location from z^{-1} form:** In H(z) = 1/(1 - az^{-1}), the pole is at **z = a** (not z = 1/a or z = -a).
5. **Stability check uses |a| < 1**, not a < 1. A pole at z = -0.9 has |z| = 0.9 < 1 and IS stable.
