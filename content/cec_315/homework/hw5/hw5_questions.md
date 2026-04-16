# CEC 315 — Homework 5: Lectures 16–18 — Laplace Transform: Definition, Inversion, Properties, and System Analysis

**Source PDF:** `hw_practice_problems/hw-lctr16-18.pdf`
**Lectures covered:** Lectures 16–18: Laplace transform definition and ROC, inverse Laplace via partial fractions, properties, system analysis with $H(s)$, unilateral Laplace
**Exam coverage:** Exam 3

CEC 315 – Signals and Systems
Rogelio Gracia Otalvaro
Spring 2026

**Instructions:** Show all work clearly and in an organized manner. Box your final answers. For every Laplace transform you compute, you **must** state the Region of Convergence (ROC). Unless stated otherwise, assume all systems are causal and initially at rest.

---

## Problem 1

**Computing Laplace Transforms and ROCs (Lecture 16)**

Compute the Laplace transform $X(s)$ and specify the ROC for each of the following signals.

### Part (a)
$x_1(t) = 4 e^{-2t}\,u(t)$

### Part (b)
$x_2(t) = -3 e^{5t}\,u(-t)$

### Part (c)
$x_3(t) = 7\,\delta(t - 3)$

### Part (d)
$x_4(t) = t\,e^{-4t}\,u(t)$

### Part (e)
$x_5(t) = 2 e^{-t}\,u(t) - 5 e^{-3t}\,u(t)$. Express $X_5(s)$ as a single rational function and identify all poles and zeros.

### Part (f)
$x_6(t) = e^{-2t}\,u(t) + 3 e^{4t}\,u(-t)$. This is a two-sided signal. Find $X_6(s)$ and determine whether the Fourier transform of $x_6(t)$ exists.

**Recall:**
$$X(s) = \int_{-\infty}^{+\infty} x(t)\,e^{-st}\,dt, \qquad s = \sigma + j\omega$$

Key pairs:
$$e^{-at}\,u(t) \;\xleftrightarrow{\mathcal{L}}\; \frac{1}{s+a}, \quad \text{ROC: } \mathrm{Re}\{s\} > -\mathrm{Re}\{a\}$$
$$-e^{-at}\,u(-t) \;\xleftrightarrow{\mathcal{L}}\; \frac{1}{s+a}, \quad \text{ROC: } \mathrm{Re}\{s\} < -\mathrm{Re}\{a\}$$

---

## Problem 2

**Inverse Laplace Transform via Partial Fractions (Lecture 17)**

Find $x(t)$ for each of the following Laplace transforms with the given ROC.

### Part (a)
**Distinct real poles.**
$$X(s) = \frac{3s + 5}{(s + 1)(s + 4)}, \quad \mathrm{Re}\{s\} > -1$$

### Part (b)
**Distinct real poles, two-sided signal.**
$$X(s) = \frac{2s - 4}{(s + 2)(s - 3)}, \quad -2 < \mathrm{Re}\{s\} < 3$$

For each pole, state whether the corresponding term is right-sided or left-sided, and explain why.

### Part (c)
**Repeated poles.**
$$X(s) = \frac{6}{(s + 2)^2(s + 5)}, \quad \mathrm{Re}\{s\} > -2$$

### Part (d)
**Complex conjugate poles.**
$$X(s) = \frac{s + 3}{s^2 + 6s + 25}, \quad \mathrm{Re}\{s\} > -3$$

Complete the square in the denominator, identify the damping rate and oscillation frequency, then invert.

**Hint:** For part (d), write $s^2 + 6s + 25 = (s + 3)^2 + 16 = (s + 3)^2 + 4^2$. Then rewrite the numerator in terms of $(s + 3)$ and use the pairs for $e^{-at}\cos(\omega_d t)\,u(t)$ and $e^{-at}\sin(\omega_d t)\,u(t)$.

---

## Problem 3

**Laplace Transform Properties (Lectures 16–17)**

### Part (a)
**s-domain shift.** Given that $\cos(5t)\,u(t) \xleftrightarrow{\mathcal{L}} \frac{s}{s^2 + 25}$ with ROC $\mathrm{Re}\{s\} > 0$, find the Laplace transform and ROC of:
$$f(t) = e^{-2t}\cos(5t)\,u(t)$$

### Part (b)
**Differentiation in time.** A signal $x(t)$ has Laplace transform $X(s) = \frac{1}{s + 3}$ with ROC $\mathrm{Re}\{s\} > -3$. Find the Laplace transform of $y(t) = \frac{dx}{dt}$ and verify by computing $y(t)$ explicitly.

### Part (c)
**Convolution property.** Two causal systems are connected in series (cascade). The first has impulse response $h_1(t) = e^{-t}\,u(t)$ and the second has $h_2(t) = 3 e^{-6t}\,u(t)$. Find the overall impulse response $h(t) = h_1(t) * h_2(t)$ by:

(i) Computing $H_1(s)$ and $H_2(s)$.
(ii) Forming $H(s) = H_1(s)\cdot H_2(s)$.
(iii) Performing partial fractions and inverting.

### Part (d)
**Initial and final value theorems.** For the signal with Laplace transform
$$X(s) = \frac{8(s + 1)}{s(s + 2)(s + 4)}, \quad \mathrm{Re}\{s\} > 0$$

(i) Use the initial-value theorem to find $x(0^+)$.
(ii) Check that the final-value theorem applies, then compute $x(\infty)$.
(iii) Invert $X(s)$ fully using partial fractions and verify both values.

**Recall:**
- $s$-domain shift: $e^{s_0 t} x(t) \xleftrightarrow{\mathcal{L}} X(s - s_0)$, ROC shifted by $\mathrm{Re}\{s_0\}$.
- Differentiation: $\frac{dx}{dt} \xleftrightarrow{\mathcal{L}} s X(s)$, ROC $\supseteq R_x$.
- Convolution: $x(t) * h(t) \xleftrightarrow{\mathcal{L}} X(s)\cdot H(s)$, ROC $\supseteq R_x \cap R_h$.
- Initial value: $x(0^+) = \lim_{s \to \infty} s X(s)$. Final value: $x(\infty) = \lim_{s \to 0} s X(s)$ (if $sX(s)$ has all poles in LHP).

---

## Problem 4

**System Analysis with $H(s)$ (Lecture 18)**

A causal LTI system is described by:
$$\frac{d^2 y}{dt^2} + 6\frac{dy}{dt} + 8 y(t) = 2 x(t)$$

### Part (a)
Find the system function $H(s) = Y(s)/X(s)$. Factor the denominator and identify the poles and any finite zeros.

### Part (b)
Draw the pole-zero plot. Is the system BIBO stable? Justify using the pole locations.

### Part (c)
Find the impulse response $h(t)$ via partial fractions.

### Part (d)
The input is $x(t) = e^{-t}\,u(t)$.

(i) Find $X(s)$ and compute $Y(s) = H(s)\cdot X(s)$.
(ii) Find $y(t)$ via partial fractions.
(iii) Verify: compute $y(0^+)$ and $y(\infty)$.

### Part (e)
A second system has $G(s) = \frac{3}{s - 1}$. Is this system BIBO stable if it is causal? What if it is anti-causal (left-sided impulse response)? State the ROC for each case and explain.

**Common Mistake:** When determining stability, remember: for a **causal** system, stability requires all poles in the open LHP. But if the system is **not** specified as causal, you must check whether the $j\omega$-axis is in the ROC, which depends on whether the impulse response is right-sided, left-sided, or two-sided.

---

## Problem 5

**The Unilateral Laplace Transform (Lecture 18)**

### Part (a)
**First-order IVP.** Solve using the unilateral Laplace transform:
$$\frac{dy}{dt} + 4 y(t) = 3 e^{-t}\,u(t), \quad y(0^-) = 2$$

(i) Transform both sides, incorporating the initial condition.
(ii) Solve for $Y(s)$.
(iii) Find $y(t)$ via partial fractions.
(iv) Verify: check $y(0)$ and $y(\infty)$.

### Part (b)
**Second-order IVP.** Solve:
$$\frac{d^2 y}{dt^2} + 3\frac{dy}{dt} + 2 y(t) = 0, \quad y(0^-) = 1,\; y'(0^-) = -1$$

(i) Transform both sides.
(ii) Find $y(t)$.
(iii) What type of response is this (zero-state, zero-input, or both)? Explain.

### Part (c)
**ZSR/ZIR decomposition.** For the system in part (a), decompose $Y(s)$ into:
$$Y(s) = \underbrace{Y_{\text{ZS}}(s)}_{\text{due to input only}} + \underbrace{Y_{\text{ZI}}(s)}_{\text{due to ICs only}}$$
Find $y_{\text{ZS}}(t)$ and $y_{\text{ZI}}(t)$ separately and verify they sum to the total $y(t)$ from part (a).

**Recall — Unilateral Laplace transform differentiation property:**
$$\frac{dy}{dt} \;\xleftrightarrow{\mathcal{L}_u}\; s Y(s) - y(0^-)$$
$$\frac{d^2 y}{dt^2} \;\xleftrightarrow{\mathcal{L}_u}\; s^2 Y(s) - s\, y(0^-) - y'(0^-)$$

*Rogelio Gracia Otalvaro*

---

## Problem Index

- **Problem 1:** Compute Laplace transforms and ROCs of six signals: causal exponential, anti-causal exponential, shifted delta, $t\,e^{-at}$, sum of two causal exponentials as a rational function, and a two-sided signal.
- **Problem 2:** Inverse Laplace transforms via partial fractions for four cases: distinct real poles causal, distinct real poles two-sided, repeated poles, and complex conjugate poles (completing the square).
- **Problem 3:** Laplace transform properties — $s$-domain shift (damped cosine), differentiation in time, convolution (cascade of two causal exponentials), and initial/final value theorems.
- **Problem 4:** System analysis of a second-order causal LTI ODE: find $H(s)$, plot poles/zeros, check stability, compute $h(t)$, drive with $e^{-t}u(t)$, and analyze a second system $G(s) = 3/(s-1)$ causal vs anti-causal.
- **Problem 5:** Unilateral Laplace transform: first-order IVP, second-order zero-input IVP, and ZSR/ZIR decomposition.
