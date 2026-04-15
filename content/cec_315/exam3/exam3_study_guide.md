# CEC 315 — Exam 3 Study Guide (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Coverage:** Lectures 16–23 (Laplace, Z-Transform, Sampling, Feedback)

---

## Table of Contents

1. [Topic Overview by Lecture](#1-topic-overview-by-lecture)
2. [Key Equations Reference](#2-key-equations-reference)
3. [ROC Rules (Laplace and Z)](#3-roc-rules-laplace-and-z)
4. [Sampling Theorem](#4-sampling-theorem)
5. [Feedback System Analysis](#5-feedback-system-analysis)
6. [What to Memorize](#6-what-to-memorize)
7. [Common Pitfalls](#7-common-pitfalls)

---

## 1. Topic Overview by Lecture

### Lecture 16 — Laplace Transform and ROC (§9.0–9.2)
- Motivation: Fourier transform fails for growing signals (e.g., $e^{2t}u(t)$).
- Definition of the bilateral Laplace transform $X(s) = \int_{-\infty}^{\infty} x(t) e^{-st}\,dt$.
- The complex variable $s = \sigma + j\omega$ and the $s$-plane.
- Region of convergence (ROC): set of $s$ where the integral converges.
- Basic pairs: $e^{-at}u(t)$, $-e^{-at}u(-t)$, $\delta(t)$, $u(t)$, $t e^{-at}u(t)$.
- Poles, zeros, and pole-zero plots; ROC bounded by poles.
- Properties of the ROC (strip parallel to $j\omega$-axis, no poles, finite duration, right/left/two-sided rules).
- Fourier transform as a special case: $X(j\omega) = X(s)\big|_{s=j\omega}$ when the $j\omega$-axis lies in the ROC.

### Lecture 17 — Inverse Laplace and Properties (§9.3–9.6)
- Partial fraction expansion (distinct, repeated, and complex conjugate poles).
- Using ROC to assign right-sided vs. left-sided terms.
- Geometric evaluation of $|H(j\omega)|$ from the pole-zero plot.
- Laplace properties: linearity, time shift, $s$-domain shift, time scaling, conjugation, convolution, differentiation in $t$, integration in $t$, differentiation in $s$.
- Initial-value theorem: $x(0^+) = \lim_{s\to\infty} s X(s)$.
- Final-value theorem: $x(\infty) = \lim_{s\to 0} s X(s)$ (only when valid).

### Lecture 18 — System Analysis via Unilateral Laplace (§9.7–9.9)
- Deriving $H(s) = Y(s)/X(s)$ from a differential equation.
- Causality $\Leftrightarrow$ ROC is a right half-plane (and $M \le N$).
- BIBO stability $\Leftrightarrow$ ROC includes the $j\omega$-axis.
- "Golden Rule": causal + stable $\Leftrightarrow$ all poles strictly in the open LHP.
- Block diagrams: series ($H_1 H_2$), parallel ($H_1 + H_2$), feedback ($G/(1+GF)$).
- Unilateral Laplace: $\mathcal{X}(s) = \int_{0^-}^\infty x(t)e^{-st}dt$.
- Differentiation rule with ICs: $\mathcal{L}_u\{x'\} = sX(s) - x(0^-)$.
- Solving differential equations with nonzero initial conditions.
- Zero-state response (ZSR) + zero-input response (ZIR) decomposition.

### Lecture 19 — Z-Transform and ROC (§10.0–10.2)
- Motivation: DTFT fails for growing sequences (e.g., $2^n u[n]$).
- Definition: $X(z) = \sum_n x[n] z^{-n}$; $z = re^{j\omega}$.
- Unit circle $|z|=1$ plays the role of the $j\omega$-axis.
- Basic pairs: $a^n u[n]$, $-a^n u[-n-1]$, $\delta[n]$, $\delta[n-k]$, $u[n]$.
- Right-sided $\Rightarrow$ ROC outside outermost pole; left-sided $\Rightarrow$ ROC inside innermost pole; two-sided $\Rightarrow$ annular ring.
- Finite-duration $\Rightarrow$ entire $z$-plane (excluding possibly $z=0$ or $\infty$).
- DTFT exists $\Leftrightarrow$ unit circle in ROC.

### Lecture 20 — Inverse Z-Transform and Properties (§10.3–10.6)
- Partial fractions in $z^{-1}$ (crucial: not in $z$!).
- Right-sided vs. left-sided direction assignment from the ROC.
- Complex poles at $re^{\pm j\omega_0}$ give damped sinusoids $r^n\cos(\omega_0 n)$.
- Geometric evaluation of frequency response on the unit circle.
- Z properties: linearity, time shift, z-domain scaling, time reversal, convolution, differentiation in $z$, first difference, accumulation.
- Initial-value theorem: $x[0] = \lim_{z\to\infty} X(z)$.
- Final-value theorem: $x[\infty] = \lim_{z\to 1}(1-z^{-1})X(z)$.

### Lecture 21 — System Analysis via Unilateral Z (§10.7–10.9)
- Deriving $H(z) = Y(z)/X(z)$ from a difference equation (replace $y[n-k] \to z^{-k}Y(z)$).
- Causality $\Leftrightarrow$ ROC is exterior of a circle; $M \le N$.
- BIBO stability $\Leftrightarrow$ ROC includes the unit circle.
- "Golden Rule" (DT): causal + stable $\Leftrightarrow$ all poles strictly inside the unit circle ($|p_i|<1$).
- Block diagrams with $z^{-1}$ as the unit delay.
- Unilateral z-transform: $\mathcal{X}(z) = \sum_{n=0}^\infty x[n]z^{-n}$.
- Shift rule with ICs: $x[n-1] \leftrightarrow z^{-1}X(z) + x[-1]$ (note the "+", not "$-$" like Laplace).
- Solving difference equations with initial conditions; ZSR + ZIR.

### Lecture 22 — Sampling (Ch. 7)
- Impulse-train sampling: $x_p(t) = x(t) p(t)$, $p(t) = \sum_n \delta(t-nT)$.
- Frequency-domain effect: spectrum replicated at multiples of $\omega_s$, scaled by $1/T$.
- Sampling theorem: $\omega_s > 2\omega_M$ for perfect reconstruction (strict inequality!).
- Ideal reconstruction: lowpass filter with gain $T$, cutoff $\omega_c$ between $\omega_M$ and $\omega_s-\omega_M$.
- Band-limited interpolation (sinc interpolation formula).
- Practical interpolation: zero-order hold (staircase), first-order hold (linear).
- Aliasing: $f_\text{alias} = |f_s - f_0|$ when undersampled.
- Wagon-wheel effect, moiré patterns.
- Discrete-time processing of CT signals: $\Omega = \omega T$.

### Lecture 23 — Linear Feedback Systems (§11.0–11.5)
- Open-loop vs. closed-loop system structure.
- Closed-loop transfer function: $Q(s) = H/(1+GH)$ for negative feedback.
- Block diagram simplification: cascade, parallel, feedback.
- Closed-loop poles from the characteristic equation $1 + GH = 0$.
- Effect of feedback: disturbance rejection, sensitivity reduction, pole relocation.
- Nyquist plot: polar plot of $G(j\omega)H(j\omega)$.
- Nyquist stability criterion (simplified): closed-loop stable iff Nyquist plot does not encircle $-1/K$ (given open-loop is stable).
- Gain margin and phase margin from Bode plots.
- CT vs. DT feedback stability boundaries.

---

## 2. Key Equations Reference

### 2.1 Transform Definitions

| Transform | Formula |
|---|---|
| Bilateral Laplace | $\displaystyle X(s) = \int_{-\infty}^{\infty} x(t)e^{-st}\,dt$ |
| Unilateral Laplace | $\displaystyle \mathcal{X}(s) = \int_{0^-}^{\infty} x(t)e^{-st}\,dt$ |
| Inverse Laplace | $\displaystyle x(t) = \frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty} X(s)e^{st}\,ds$ |
| Bilateral Z | $\displaystyle X(z) = \sum_{n=-\infty}^{\infty} x[n]z^{-n}$ |
| Unilateral Z | $\displaystyle \mathcal{X}(z) = \sum_{n=0}^{\infty} x[n]z^{-n}$ |
| Inverse Z | $\displaystyle x[n] = \frac{1}{2\pi j}\oint X(z)z^{n-1}\,dz$ |

### 2.2 Common Laplace Pairs (all causal, ROC = right of rightmost pole)

| $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $\delta(t-t_0)$ | $e^{-st_0}$ | all $s$ |
| $u(t)$ | $\dfrac{1}{s}$ | $\operatorname{Re}\{s\}>0$ |
| $tu(t)$ | $\dfrac{1}{s^2}$ | $\operatorname{Re}\{s\}>0$ |
| $\dfrac{t^{n-1}}{(n-1)!}u(t)$ | $\dfrac{1}{s^n}$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}u(t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $t e^{-at}u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $\dfrac{t^{n-1}}{(n-1)!}e^{-at}u(t)$ | $\dfrac{1}{(s+a)^n}$ | $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$ |
| $\cos(\omega_0 t)u(t)$ | $\dfrac{s}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $\sin(\omega_0 t)u(t)$ | $\dfrac{\omega_0}{s^2+\omega_0^2}$ | $\operatorname{Re}\{s\}>0$ |
| $e^{-at}\cos(\omega_d t)u(t)$ | $\dfrac{s+a}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $e^{-at}\sin(\omega_d t)u(t)$ | $\dfrac{\omega_d}{(s+a)^2+\omega_d^2}$ | $\operatorname{Re}\{s\}>-a$ |
| $-e^{-at}u(-t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\}<-\operatorname{Re}\{a\}$ |

### 2.3 Common Z-Transform Pairs

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n-k]$, $k\ge 0$ | $z^{-k}$ | $|z|>0$ |
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $|z|>1$ |
| $a^n u[n]$ | $\dfrac{1}{1-az^{-1}}$ | $|z|>|a|$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $|z|<|a|$ |
| $na^n u[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $(n+1)a^n u[n]$ | $\dfrac{1}{(1-az^{-1})^2}$ | $|z|>|a|$ |
| $r^n \cos(\omega_0 n)u[n]$ | $\dfrac{1-r\cos\omega_0 z^{-1}}{1-2r\cos\omega_0 z^{-1}+r^2 z^{-2}}$ | $|z|>r$ |
| $r^n \sin(\omega_0 n)u[n]$ | $\dfrac{r\sin\omega_0 z^{-1}}{1-2r\cos\omega_0 z^{-1}+r^2 z^{-2}}$ | $|z|>r$ |

### 2.4 Laplace Properties

| Property | Time | $s$-Domain |
|---|---|---|
| Linearity | $ax(t)+by(t)$ | $aX(s)+bY(s)$, ROC $\supseteq R_x\cap R_y$ |
| Time shift | $x(t-t_0)$ | $e^{-st_0}X(s)$, ROC $=R_x$ |
| $s$-domain shift | $e^{s_0 t}x(t)$ | $X(s-s_0)$, ROC $=R_x+\operatorname{Re}\{s_0\}$ |
| Time scaling | $x(at)$, $a>0$ | $\dfrac{1}{a}X(s/a)$, ROC $=aR_x$ |
| Conjugation | $x^*(t)$ | $X^*(s^*)$, ROC $=R_x$ |
| Convolution | $x(t)*y(t)$ | $X(s)Y(s)$ |
| Differentiation in $t$ | $dx/dt$ | $sX(s)$ (bilateral, zero ICs) |
| Integration in $t$ | $\int_{-\infty}^t x(\tau)d\tau$ | $X(s)/s$ |
| Differentiation in $s$ | $-tx(t)$ | $dX/ds$ |
| **Unilateral diff.** | $dx/dt$ | $sX(s)-x(0^-)$ |
| Unilateral $d^2/dt^2$ | $d^2x/dt^2$ | $s^2X(s)-sx(0^-)-x'(0^-)$ |
| Initial-value theorem | $x(0^+)$ | $\lim_{s\to\infty} sX(s)$ |
| Final-value theorem | $x(\infty)$ | $\lim_{s\to 0} sX(s)$ (if valid) |

### 2.5 Z-Transform Properties

| Property | Sequence | z-Domain |
|---|---|---|
| Linearity | $ax_1+bx_2$ | $aX_1+bX_2$ |
| Time shift | $x[n-n_0]$ | $z^{-n_0}X(z)$ |
| z-domain scaling | $z_0^n x[n]$ | $X(z/z_0)$, ROC $=|z_0|R_x$ |
| Time reversal | $x[-n]$ | $X(z^{-1})$, ROC $=1/R_x$ |
| Convolution | $x_1*x_2$ | $X_1(z)X_2(z)$ |
| Differentiation in $z$ | $nx[n]$ | $-z\,dX/dz$ |
| First difference | $x[n]-x[n-1]$ | $(1-z^{-1})X(z)$ |
| Accumulation | $\sum_{k=-\infty}^n x[k]$ | $\dfrac{X(z)}{1-z^{-1}}$ |
| **Unilateral shift** | $x[n-1]$ | $z^{-1}X(z)+x[-1]$ |
| Unilateral shift-2 | $x[n-2]$ | $z^{-2}X(z)+x[-1]z^{-1}+x[-2]$ |
| Initial-value theorem | $x[0]$ | $\lim_{z\to\infty} X(z)$ |
| Final-value theorem | $x[\infty]$ | $\lim_{z\to 1}(1-z^{-1})X(z)$ |

---

## 3. ROC Rules (Laplace and Z)

### 3.1 Laplace ROC

| Signal type | ROC shape |
|---|---|
| Finite duration (absolutely integrable) | Entire $s$-plane |
| Right-sided ($x(t)=0$ for $t<T_0$) | $\operatorname{Re}\{s\} > \sigma_{\max}$ (right of rightmost pole) |
| Left-sided ($x(t)=0$ for $t>T_0$) | $\operatorname{Re}\{s\} < \sigma_{\min}$ (left of leftmost pole) |
| Two-sided | Vertical strip between consecutive poles |
| Causal and stable | Rightmost pole in LHP; $j\omega$-axis in ROC |

**ROC key facts:**
- ROC is always a **vertical strip** parallel to the $j\omega$-axis.
- ROC never contains poles.
- DTFT/Fourier transform exists iff ROC includes the $j\omega$-axis.

### 3.2 Z-Transform ROC

| Signal type | ROC shape |
|---|---|
| Finite duration | Entire $z$-plane (possibly excluding $z=0$ or $\infty$) |
| Right-sided (causal) | $|z| > r_{\max}$ (exterior of outermost pole) |
| Left-sided (anti-causal) | $|z| < r_{\min}$ (interior of innermost pole) |
| Two-sided | Annular ring $r_1 < |z| < r_2$ between pole circles |
| Causal and stable | All poles inside unit circle; unit circle in ROC |

**ROC key facts:**
- ROC is always an **annular ring** centered at the origin.
- ROC never contains poles.
- DTFT exists iff ROC includes the unit circle.

### 3.3 Causality and Stability Summary

| Criterion | Laplace (CT) | Z (DT) |
|---|---|---|
| Causal | ROC right half-plane, $M\le N$ | ROC exterior of circle, $M\le N$ |
| BIBO stable | ROC includes $j\omega$-axis | ROC includes unit circle |
| Causal + stable | All poles with $\operatorname{Re}\{p_i\}<0$ | All poles with $|p_i|<1$ |
| Marginally stable | Poles on $j\omega$-axis | Poles on unit circle |

---

## 4. Sampling Theorem

### 4.1 The Theorem

Let $x(t)$ be bandlimited with $X(j\omega)=0$ for $|\omega|>\omega_M$. Then $x(t)$ is uniquely determined by samples $x(nT)$ if and only if
$$\omega_s > 2\omega_M, \qquad \omega_s = \frac{2\pi}{T}.$$

- **Nyquist rate:** $2\omega_M$ (minimum sampling frequency).
- **Nyquist frequency:** $\omega_M$.
- The inequality is **strict**: $\omega_s = 2\omega_M$ is generally not sufficient.

### 4.2 Spectrum of Sampled Signal

$$X_p(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X(j(\omega - k\omega_s))$$

The spectrum is replicated every $\omega_s$ and scaled by $1/T$.

### 4.3 Ideal Reconstruction

Use LPF with gain $T$ and cutoff $\omega_c$ such that $\omega_M < \omega_c < \omega_s - \omega_M$. Typical choice: $\omega_c = \omega_s/2$.

Time-domain formula:
$$x_r(t) = \sum_{n=-\infty}^{\infty} x(nT)\,\frac{\sin[\pi(t-nT)/T]}{\pi(t-nT)/T}$$

### 4.4 Aliasing

When $\omega_s < 2\omega_M$, the replicas overlap. A sinusoid at $f_0$ (with $f_s/2 < f_0 < f_s$) aliases to
$$f_\text{alias} = |f_s - f_0|.$$

**Aliasing is irreversible.** Prevent it with an **anti-aliasing filter** before sampling.

### 4.5 DT Processing of CT Signals

$$\Omega = \omega T$$

Relates discrete-time frequency $\Omega$ (rad/sample) to continuous-time frequency $\omega$ (rad/s).

---

## 5. Feedback System Analysis

### 5.1 Closed-Loop Transfer Function

For standard negative feedback:
$$Q(s) = \frac{Y(s)}{X(s)} = \frac{H(s)}{1 + G(s)H(s)}$$

- **Forward path:** $H(s)$
- **Feedback path:** $G(s)$
- **Loop gain:** $L(s) = G(s)H(s)$
- **Characteristic equation:** $1 + G(s)H(s) = 0$ (closed-loop pole locations)
- Positive feedback variant: $Q = H/(1 - GH)$

### 5.2 Block Diagram Rules

| Configuration | Equivalent |
|---|---|
| Cascade (series) | $H_1 \cdot H_2$ |
| Parallel | $H_1 + H_2$ |
| Negative feedback | $H/(1+GH)$ |

### 5.3 Stability via Nyquist Criterion

For an **open-loop stable** plant $GH$ (no RHP poles), the closed-loop system with gain $K$ is stable iff the Nyquist plot of $G(j\omega)H(j\omega)$ does **not encircle** the critical point $-1/K$.

- Plot $GH$ for $\omega \in (-\infty, \infty)$.
- Locate $-1/K$ on the real axis.
- Critical point outside the closed contour $\Rightarrow$ stable.

### 5.4 Gain and Phase Margins

Instability occurs when $GH = -1$ (magnitude 1, phase $-180°$ simultaneously).

**Gain margin (GM):** At $\omega_1$ where $\angle GH(\omega_1) = -180°$,
$$\mathrm{GM}_{\mathrm{dB}} = -20\log_{10}|GH(\omega_1)|$$

**Phase margin (PM):** At $\omega_2$ where $|GH(\omega_2)| = 1$ (0 dB),
$$\mathrm{PM} = 180° + \angle GH(\omega_2)$$

Both positive $\Rightarrow$ stable. Max additional delay: $\tau_{\max} = \mathrm{PM (rad)}/\omega_2$.

### 5.5 CT vs. DT Stability

| | CT | DT |
|---|---|---|
| Closed-loop | $H(s)/[1+G(s)H(s)]$ | $H(z)/[1+G(z)H(z)]$ |
| Stable region | $\operatorname{Re}\{s\}<0$ (open LHP) | $|z|<1$ (inside unit circle) |

---

## 6. What to Memorize

**Must-know transform pairs:**
$$\delta(t)\leftrightarrow 1,\qquad u(t)\leftrightarrow \tfrac{1}{s},\qquad e^{-at}u(t)\leftrightarrow \tfrac{1}{s+a}$$
$$te^{-at}u(t)\leftrightarrow \tfrac{1}{(s+a)^2},\qquad \cos\omega_0 t\,u(t)\leftrightarrow \tfrac{s}{s^2+\omega_0^2},\qquad \sin\omega_0 t\,u(t)\leftrightarrow \tfrac{\omega_0}{s^2+\omega_0^2}$$

**Must-know Z pairs:**
$$\delta[n]\leftrightarrow 1,\qquad u[n]\leftrightarrow \tfrac{1}{1-z^{-1}},\qquad a^n u[n]\leftrightarrow \tfrac{1}{1-az^{-1}}\ (|z|>|a|)$$
$$(n+1)a^n u[n]\leftrightarrow \tfrac{1}{(1-az^{-1})^2}$$

**Must-know rules:**
- $dx/dt \leftrightarrow sX(s)-x(0^-)$ (unilateral).
- $x[n-1] \leftrightarrow z^{-1}X(z)+x[-1]$ (unilateral, note the **plus**).
- Convolution $\leftrightarrow$ multiplication.
- Causal + stable $\Leftrightarrow$ all poles in LHP (CT) or inside unit circle (DT).
- Sampling theorem: $\omega_s > 2\omega_M$.
- Closed-loop: $Q = H/(1+GH)$.
- Aliased frequency: $f_\text{alias} = |f_s - f_0|$.

**Must-know steps:**
1. **Solving an ODE with ICs:** (a) unilateral Laplace, (b) plug in IC terms, (c) solve for $Y(s)$, (d) partial fractions, (e) invert.
2. **Finding impulse response:** (a) compute $H(s)=Y/X$, (b) partial fractions, (c) use ROC to assign direction, (d) invert each term.
3. **Stability check:** (a) find poles, (b) causal + LHP $\Rightarrow$ stable (CT); causal + inside unit circle $\Rightarrow$ stable (DT).

---

## 7. Common Pitfalls

1. **Omitting the ROC.** $X(s)=1/(s+3)$ could be $e^{-3t}u(t)$ or $-e^{-3t}u(-t)$. Always state the ROC.
2. **Wrong direction in partial fractions.** Use the ROC, *not* the sign of the pole, to choose right- vs. left-sided.
3. **Incomplete partial fractions for repeated poles.** A pole of order $n$ requires $n$ terms: $\frac{B_1}{s-p},\ldots,\frac{B_n}{(s-p)^n}$.
4. **Mishandling complex poles in Laplace.** Don't split conjugate pairs; complete the square and use cos/sin pairs.
5. **Forgetting IC terms in unilateral differentiation.** $\mathcal{L}_u\{y'\} = sY - y(0^-)$, with **minus** in Laplace; unilateral Z shift is $z^{-1}Y + x[-1]$ with **plus**.
6. **Applying final-value theorem without checking.** Requires $sX(s)$ (or $(1-z^{-1})X(z)$) to have all poles strictly in LHP / inside unit circle.
7. **Mixing LHP with "inside the unit circle."** In CT stability is about $\operatorname{Re}\{s\}<0$. In DT it's about $|z|<1$. A DT pole at $z=-0.9$ is stable ($|-0.9|<1$) even though $z=-0.9$ is on the negative real axis.
8. **Pole at $z=a$, not $z=1/a$.** For $1/(1-az^{-1})$, the pole is at $z=a$.
9. **Working Z partial fractions in $z$, not $z^{-1}$.** All standard pairs are in $z^{-1}$ form. Use $z^{-1}$ as the variable.
10. **Sampling at exactly $2\omega_M$.** Strictly insufficient (Example 22.3: $\sin(\omega_s t/2)$ samples to all zeros).
11. **Confusing Hz and rad/s in sampling.** $f_s > 2f_M$ or $\omega_s > 2\omega_M$; $\omega = 2\pi f$.
12. **Aliased frequency formula.** $f_\text{alias} = |f_s - f_0|$ only for $f_s/2 < f_0 < f_s$. More generally, aliasing folds components back into $[-f_s/2, f_s/2]$.
13. **Sign error at the summer.** Negative feedback $\to 1+GH$; positive feedback $\to 1-GH$.
14. **Open-loop vs. closed-loop poles.** Poles of $GH$ are open-loop; roots of $1+KGH=0$ are closed-loop.
15. **Gain margin vs. phase margin confusion.** GM is read on magnitude plot at the frequency where phase $=-180°$. PM is read on phase plot at the frequency where magnitude $=0$ dB.
16. **Assuming feedback always stabilizes.** Too much gain can destabilize a stable plant. Feedback is a tool, not a panacea.
17. **Forgetting $1/T$ scaling** in the sampled spectrum. Replicas are scaled by $1/T$; reconstruction filter compensates with gain $T$.
18. **RHP zeros $\neq$ instability.** Only poles determine stability; RHP zeros give nonminimum-phase behavior but not instability.

---

*Prepared for CEC 315 Exam 3 — Spring 2026.*
