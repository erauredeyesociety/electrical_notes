# Homework: Lectures 19-21

## The z-Transform: Definition, Inversion, Properties, and System Analysis

**CEC 315 -- Signals and Systems**
Rogelio Gracia Otalvaro
Spring 2026

**Instructions:** Show all work clearly and in an organized manner. Box your final answers. For every z-transform you compute, you **must** state the Region of Convergence (ROC). Unless stated otherwise, assume all systems are causal and initially at rest.

---

## Problem 1: Computing z-Transforms and ROCs (Lecture 19)

Compute the z-transform X(z) and specify the ROC for each of the following signals.

**(a)** x_1[n] = 5 (0.7)^n u[n]

**(b)** x_2[n] = -(4)^n u[-n - 1]

**(c)** x_3[n] = 3 delta[n] - 2 delta[n - 1] + delta[n - 4]

**(d)** x_4[n] = n (0.5)^n u[n]

**(e)** x_5[n] = 2 (0.3)^n u[n] + 4 (0.9)^n u[n]. Express X_5(z) as a single rational function and identify all poles and zeros.

**(f)** x_6[n] = (0.6)^n u[n] - 3 (2)^n u[-n - 1]. This is a two-sided signal. Find X_6(z), state the ROC, and determine whether the DTFT of x_6[n] exists.

**(g)** x_7[n] = (0.8)^n cos(0.25 pi n) u[n]. Use the table pair for r^n cos(omega_0 n) u[n] to find X_7(z). Identify the pole locations (express them in polar form), the pole radius, and the oscillation frequency. Does this signal have a DTFT?

**(h)** For each signal in (a)-(g), evaluate X(z) at z = 1 and verify that this equals sum_n x[n].

### Recall -- Key z-transform pairs:

| Signal | X(z) | ROC |
|--------|-------|-----|
| a^n u[n] | 1 / (1 - a z^{-1}) | \|z\| > \|a\| |
| -a^n u[-n - 1] | 1 / (1 - a z^{-1}) | \|z\| < \|a\| |
| n a^n u[n] | a z^{-1} / (1 - a z^{-1})^2 | \|z\| > \|a\| |
| delta[n - k] | z^{-k} | \|z\| > 0 for k >= 1 |
| r^n cos(omega_0 n) u[n] | (1 - r cos(omega_0) z^{-1}) / (1 - 2r cos(omega_0) z^{-1} + r^2 z^{-2}) | \|z\| > r |

---

## Problem 2: Inverse z-Transform via Partial Fractions (Lecture 20)

Find x[n] for each of the following z-transforms with the given ROC.

**(a) Distinct real poles, causal signal.**

X(z) = (1 + 3 z^{-1}) / ((1 - 0.2 z^{-1})(1 - 0.6 z^{-1})),  |z| > 0.6

**(b) Distinct real poles, two-sided signal.**

X(z) = 4 / ((1 - 0.5 z^{-1})(1 - 3 z^{-1})),  0.5 < |z| < 3

For each pole, state whether the corresponding term is right-sided or left-sided, and explain why.

**(c) Repeated poles.**

X(z) = z^{-1} / (1 - 0.5 z^{-1})^2,  |z| > 0.5

**(d) Complex conjugate poles.**

X(z) = (1 - 0.9 cos(0.3 pi) z^{-1}) / (1 - 2(0.9) cos(0.3 pi) z^{-1} + 0.81 z^{-2}),  |z| > 0.9

Identify the pole radius r, the oscillation frequency omega_0, and write x[n] using the damped-cosine pair from the table.

### Hint

For part (c), use the pair n a^n u[n] <-Z-> a z^{-1} / (1 - a z^{-1})^2 with a = 0.5. For part (b), the annular ROC tells you one term is right-sided and the other is left-sided.

---

## Problem 3: z-Transform Properties (Lectures 19-20)

**(a) Time shifting.** Given that (0.8)^n u[n] <-Z-> 1 / (1 - 0.8 z^{-1}) with ROC |z| > 0.8, find the z-transform and ROC of:

y[n] = (0.8)^{n-2} u[n - 2]

How many zeros does Y(z) have at z = 0? Explain.

**(b) z-domain scaling.** Given that u[n] <-Z-> 1 / (1 - z^{-1}) with ROC |z| > 1, use the scaling property (z_0^n x[n] <-Z-> X(z/z_0)) to find the z-transform of:

f[n] = (0.5)^n u[n]

Verify that your answer matches the standard pair.

**(c) Convolution property.** Two causal systems are connected in cascade. The first has impulse response h_1[n] = (0.3)^n u[n] and the second has h_2[n] = (0.7)^n u[n]. Find the overall impulse response h[n] = h_1[n] * h_2[n] by:

- (i) Computing H_1(z) and H_2(z).
- (ii) Forming H(z) = H_1(z) * H_2(z).
- (iii) Performing partial fractions and inverting.
- (iv) Verifying h[0] and h[1] by direct convolution.

**(d) Initial-value theorem.** For the signal with z-transform

X(z) = (3 - z^{-1}) / ((1 - 0.4 z^{-1})(1 + 0.5 z^{-1})),  |z| > 0.5

- (i) Use the initial-value theorem x[0] = lim_{z->inf} X(z) to find x[0].
- (ii) Invert X(z) fully using partial fractions and verify x[0].
- (iii) Compute x[1] and x[2].

### Recall

- **Time shift:** x[n - n_0] <-Z-> z^{-n_0} X(z)
- **z-domain scaling:** z_0^n x[n] <-Z-> X(z/z_0), ROC = |z_0| * R_x
- **Convolution:** x_1[n] * x_2[n] <-Z-> X_1(z) * X_2(z)
- **Initial value (causal):** x[0] = lim_{z->inf} X(z)

---

## Problem 4: System Analysis with H(z) (Lecture 21)

A causal LTI system is described by:

y[n] - 0.9 y[n - 1] + 0.18 y[n - 2] = x[n]

**(a)** Find the system function H(z) = Y(z)/X(z). Factor the denominator and identify the poles. Are there any finite zeros?

**(b)** Is the system BIBO stable? Justify using the pole locations and the unit circle.

**(c)** Find the impulse response h[n] via partial fractions.

**(d)** The input is x[n] = (0.5)^n u[n].

- (i) Find X(z) and compute Y(z) = H(z) * X(z).
- (ii) Find y[n] via partial fractions.
- (iii) Verify: compute y[0] and y[1] both from your formula and directly from the difference equation.

**(e)** A second system has G(z) = 1 / (1 - 1.5 z^{-1}). Is this system BIBO stable if it is causal? What if it has a left-sided (anti-causal) impulse response? For each case, state the ROC and whether the DTFT of the impulse response exists.

### Common Mistake

For a **causal** DT system, BIBO stability requires all poles strictly inside the unit circle (|p_i| < 1). A pole at |p_i| = 1 makes the system marginally stable, and a pole at |p_i| > 1 makes it unstable. But for a **non-causal** system, stability depends on whether the unit circle is in the ROC, which can hold even if poles are outside the unit circle.

---

## Problem 5: The Unilateral z-Transform (Lecture 21)

**(a) First-order difference equation with IC.** Solve using the unilateral z-transform:

y[n] - 0.8 y[n - 1] = (0.5)^n u[n],  y[-1] = 3

- (i) Transform both sides, incorporating the initial condition.
- (ii) Solve for Y(z).
- (iii) Find y[n] via partial fractions.
- (iv) Verify: check y[0] and y[1] from both the formula and the difference equation.

**(b) Second-order, zero-input response.** Solve:

y[n] - 0.5 y[n - 1] - 0.06 y[n - 2] = 0,  y[-1] = 5, y[-2] = 0

- (i) Transform both sides and solve for Y(z).
- (ii) Factor the denominator and find y[n].
- (iii) What type of response is this (zero-state, zero-input, or both)? Explain.

**(c) ZSR/ZIR decomposition.** For the system in part (a), decompose Y(z) into:

Y(z) = Y_ZS(z) + Y_ZI(z)

where Y_ZS(z) is from input only (ICs = 0) and Y_ZI(z) is from ICs only (input = 0).

Find y_ZS[n] and y_ZI[n] separately and verify they sum to the total y[n] from part (a).

### Recall

Unilateral z-transform time-shift property:

- y[n - 1] <-Z_u-> z^{-1} Y(z) + y[-1]
- y[n - 2] <-Z_u-> z^{-2} Y(z) + y[-2] + y[-1] z^{-1}

Note the **plus** sign on the initial condition terms (contrast with the minus sign in the unilateral Laplace differentiation property).
