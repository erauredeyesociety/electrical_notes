# Lecture 19: The z-Transform -- Definition and Region of Convergence

**CEC 315 -- Signals and Systems**
Rogelio Gracia Otalvaro, Spring 2026
Focus: Sections 10.0-10.2 (Pages 741-757)

---

## 19.1 The Big Picture: DT Counterpart of the Laplace Transform

The z-transform is the discrete-time analog of the Laplace transform. It generalizes the DTFT by introducing a complex variable z, just as s generalizes the CT Fourier transform.

### CT/DT Parallel

| Laplace (CT) | z-Transform (DT) |
|---|---|
| Complex variable s = sigma + j omega | Complex variable z = r e^{j omega} |
| j omega-axis (sigma = 0) | Unit circle (\|z\| = 1) |
| Left/Right half-plane | Inside/outside the unit circle |
| ROC: vertical strip | ROC: annular ring |
| Differential equations -> algebra | Difference equations -> algebra |

---

## 19.2 From the DTFT to the z-Transform

### 19.2.1 The Convergence Problem

The DTFT requires absolute convergence: sum |x[n]| < inf. Many important sequences violate this (e.g., x[n] = 2^n u[n] diverges).

### 19.2.2 The Fix: Geometric Damping Factor

Multiply x[n] by r^{-n} (analogous to multiplying by e^{-sigma t} in the Laplace case). Define the complex variable:

**z = r e^{j omega}**

where r = |z| is the magnitude and omega = angle(z) is the angle.

### 19.2.3 The z-Plane

Key facts:
1. Points on the unit circle have |z| = 1, so z = e^{j omega}. This is where the DTFT lives.
2. z = 1 corresponds to omega = 0 (DC). z = -1 corresponds to omega = pi (Nyquist frequency).
3. Points inside the unit circle have |z| < 1; points outside have |z| > 1.

---

## 19.3 Formal Definition

### The z-Transform Pair

**Analysis (forward transform):**

X(z) = sum_{n=-inf}^{+inf} x[n] z^{-n}

**Synthesis (inverse transform):**

x[n] = (1 / (2 pi j)) contour_integral X(z) z^{n-1} dz

where the contour integral is along a closed path in the ROC that encircles the origin.

**Notation:** x[n] <-Z-> X(z)

### Key Insight

The z-transform is the DTFT of x[n] r^{-n}. When r = 1 (i.e., |z| = 1), the damping disappears and the z-transform reduces exactly to the DTFT:

X(z)|_{z=e^{j omega}} = X(e^{j omega})  (the DTFT)

### Critical Warning

X(z) alone does **not** uniquely determine x[n]. The ROC must also be specified. Different signals can share the same X(z) but have different ROCs.

---

## 19.4 Fundamental z-Transform Pairs

### 19.4.1 Right-Sided Exponential: x[n] = a^n u[n]

Derivation uses the geometric series sum_{n=0}^{inf} w^n = 1/(1-w) for |w| < 1.

**Result:**

a^n u[n] <-Z-> 1 / (1 - a z^{-1}) = z / (z - a),  ROC: |z| > |a|

- Pole at z = a, zero at z = 0
- ROC is the exterior of a circle of radius |a|

**Numerical examples:**
- a = 0.5 (decaying): (0.5)^n u[n] <-Z-> 1/(1 - 0.5 z^{-1}), |z| > 0.5. Unit circle is in ROC, so DTFT exists.
- a = 2 (growing): 2^n u[n] <-Z-> 1/(1 - 2 z^{-1}), |z| > 2. Unit circle is NOT in ROC, so DTFT does not exist.

### 19.4.2 Left-Sided Exponential: x[n] = -a^n u[-n - 1]

**Result:**

-a^n u[-n - 1] <-Z-> 1 / (1 - a z^{-1}),  ROC: |z| < |a|

**Critical observation:** The right-sided pair a^n u[n] and the left-sided pair -a^n u[-n-1] produce the **same** algebraic expression 1/(1 - a z^{-1}). The ROC is the **only** difference:

| Signal | X(z) | ROC |
|--------|-------|-----|
| a^n u[n] | 1 / (1 - a z^{-1}) | \|z\| > \|a\| (exterior) |
| -a^n u[-n - 1] | 1 / (1 - a z^{-1}) | \|z\| < \|a\| (interior) |

Without the ROC, the transform is ambiguous. **Always state the ROC.**

**Numerical example:** x[n] = -(3)^n u[-n - 1], a = 3. X(z) = 1/(1 - 3 z^{-1}), |z| < 3. Pole at z = 3 (outside unit circle). ROC includes unit circle, so DTFT exists.

### 19.4.3 ROC Diagrams: Right-Sided vs. Left-Sided

- **Right-sided:** ROC is |z| > |a| (exterior of the pole circle)
- **Left-sided:** ROC is |z| < |a| (interior of the pole circle)

### 19.4.4 Unit Impulse and Unit Step

**Unit impulse:** delta[n] <-Z-> 1, ROC: all z.

**Delayed impulse:** delta[n - k] <-Z-> z^{-k}, ROC: |z| > 0 (for k >= 1).
Each unit of delay contributes a factor of z^{-1}. A delay of k samples gives z^{-k}, which has k zeros at z = 0.

**Unit step:** u[n] is the special case a^n u[n] with a = 1:

u[n] <-Z-> 1 / (1 - z^{-1}) = z / (z - 1),  ROC: |z| > 1

The pole is at z = 1, which sits exactly on the unit circle. The ROC does not include the unit circle, so the DTFT of u[n] cannot be obtained by simply setting z = e^{j omega}.

### 19.4.5 Two-Sided Signals

**Example:** x[n] = (0.5)^n u[n] + 2 * (3)^n u[-n - 1]

Transform each piece separately, then add and intersect ROCs:

X(z) = 1/(1 - 0.5 z^{-1}) - 2/(1 - 3 z^{-1}),  ROC: 0.5 < |z| < 3

The ROC is an annular ring. Since 0.5 < 1 < 3, the unit circle lies inside this ring, so the DTFT exists.

**Key insight:** The ROC for a two-sided signal is a ring r_1 < |z| < r_2 between two pole circles. If the inner pole has a larger radius than the outer pole, the intersection is empty and the z-transform does not exist.

### 19.4.6 Sum of Two Right-Sided Exponentials

**Example:** x[n] = 3(0.4)^n u[n] - 2(0.8)^n u[n]

Step 1: Transform each term: 3/(1 - 0.4 z^{-1}) and -2/(1 - 0.8 z^{-1})

Step 2: Common denominator:

X(z) = (1 - 1.6 z^{-1}) / ((1 - 0.4 z^{-1})(1 - 0.8 z^{-1}))

ROC: |z| > 0.8 (intersection of |z| > 0.4 and |z| > 0.8).
Poles: z = 0.4 and z = 0.8. Zero: z = 1.6 (from 1 - 1.6 z^{-1} = 0).

**Sanity check:** X(1) = (1-1.6)/((1-0.4)(1-0.8)) = -0.6/(0.6*0.2) = -5. Direct: 3/0.6 - 2/0.2 = 5 - 10 = -5. Checks out.

### 19.4.7 Finite-Duration Sequence

**Example:** x[n] = {2, -1, 3, 0, 4} for n = 0, 1, 2, 3, 4

X(z) = 2 - z^{-1} + 3 z^{-2} + 4 z^{-4}

This is a polynomial in z^{-1}. No poles except at z = 0. ROC is all z != 0 (ROC Property P3 for finite-duration sequences).

**Sanity check:** X(1) = 2 - 1 + 3 + 0 + 4 = 8 = sum_n x[n]. The sum of all samples always equals the z-transform evaluated at z = 1.

---

## 19.5 Poles, Zeros, and the ROC

For rational X(z), the ROC is bounded by circles passing through pole locations. The ROC can never contain a pole.

**Reading a pole-zero plot:**
- Poles (x): values where X(z) -> inf. ROC boundaries are circles through the poles.
- Zeros (o): values where X(z) = 0. Zeros do not affect the ROC.
- In the z^{-1} form X(z) = 1/(1 - a z^{-1}), the pole is at z = a (not at z = 1/a).
- If X(z) has N poles and M < N finite zeros, there are also N - M zeros at z = 0.

---

## 19.6 Properties of the ROC

**P1:** The ROC is a ring (annulus) centered at the origin: r_1 < |z| < r_2.

**P2:** The ROC does not contain any poles.

**P3:** **Finite-duration** sequences have ROC = entire z-plane (possibly excluding z = 0 or z = inf).

**P4:** **Right-sided** signals with rational X(z): ROC is exterior, |z| > max_i |d_i|.

**P5:** **Left-sided** signals with rational X(z): ROC is interior, |z| < min_i |d_i|.

**P6:** **Two-sided** signals: ROC is an annular ring between consecutive pole circles.

**P7:** If the ROC includes the unit circle (|z| = 1), the DTFT exists.

---

## 19.7 The Complete CT/DT Parallel

| | Laplace (s-domain) | z-Transform (z-domain) |
|---|---|---|
| Variable | s = sigma + j omega | z = r e^{j omega} |
| Transform | integral x(t) e^{-st} dt | sum x[n] z^{-n} |
| FT lives on | j omega-axis (sigma = 0) | unit circle (\|z\| = 1) |
| ROC shape | vertical strip | annular ring |
| Right-sided ROC | Re{s} > sigma_max | \|z\| > r_max |
| Left-sided ROC | Re{s} < sigma_min | \|z\| < r_min |
| Causal + Stable | all poles in LHP | all poles inside unit circle |
| Basic pair | e^{-at} u(t) <-> 1/(s+a) | a^n u[n] <-> 1/(1 - a z^{-1}) |

---

## 19.8 Table of Basic z-Transform Pairs

| Signal x[n] | X(z) | ROC |
|---|---|---|
| delta[n] | 1 | all z |
| delta[n - k], k >= 0 | z^{-k} | \|z\| > 0 |
| u[n] | 1 / (1 - z^{-1}) | \|z\| > 1 |
| a^n u[n] | 1 / (1 - a z^{-1}) | \|z\| > \|a\| |
| -a^n u[-n - 1] | 1 / (1 - a z^{-1}) | \|z\| < \|a\| |
| n a^n u[n] | a z^{-1} / (1 - a z^{-1})^2 | \|z\| > \|a\| |
| (n+1) a^n u[n] | 1 / (1 - a z^{-1})^2 | \|z\| > \|a\| |
| r^n cos(omega_0 n) u[n] | (1 - r cos(omega_0) z^{-1}) / (1 - 2r cos(omega_0) z^{-1} + r^2 z^{-2}) | \|z\| > r |
| r^n sin(omega_0 n) u[n] | r sin(omega_0) z^{-1} / (1 - 2r cos(omega_0) z^{-1} + r^2 z^{-2}) | \|z\| > r |

---

## 19.9 Summary

1. The z-transform X(z) = sum x[n] z^{-n} generalizes the DTFT via z = r e^{j omega}. Setting r = 1 recovers the DTFT.
2. The ROC is essential: without it, X(z) does not uniquely determine x[n].
3. Right-sided => ROC outside the outermost pole. Left-sided => ROC inside the innermost pole. Two-sided => annular ring between pole circles.
4. The **unit circle** (|z| = 1) plays the role of the j omega-axis. DTFT exists iff the unit circle is in the ROC.
5. The structure parallels the Laplace transform exactly, with circles replacing lines and |z| replacing Re{s}.

---

## 19.10 Common Mistakes to Avoid

1. **Omitting the ROC:** 1/(1 - 0.5 z^{-1}) with |z| > 0.5 means (0.5)^n u[n], but with |z| < 0.5 it means -(0.5)^n u[-n - 1].
2. **Confusing "outside" and "inside":** Right-sided signals have ROC *outside* the outermost pole circle. This is different from the Laplace convention ("to the right" of the rightmost pole).
3. **Forgetting that the unit circle replaces the j omega-axis:** The DTFT exists iff the unit circle is in the ROC.
4. **Misidentifying poles:** In 1/(1 - a z^{-1}), the pole is at z = a, *not* at z = 1/a.
5. **Geometric series convergence:** sum w^n converges iff |w| < 1, not just w < 1. For complex w, the magnitude |w| is what matters.
