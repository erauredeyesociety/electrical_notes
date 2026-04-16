# CEC 315 — Exam 3 Official Study Guide (Instructor)

> **Source:** `StudyGuide_Exam3.pdf` (4 pages) — instructor-provided, authoritative.
> **Course:** CEC 315 — Signals and Systems, Spring 2026
> **Instructor:** Rogelio Gracia Otalvaro
> **Coverage:** Lectures 16–23

This file is a faithful transcription of the instructor's official Exam 3 study guide. **This is the authoritative source.** See `exam3_study_guide.md` for the student-compiled companion notes (tables of transform pairs, expanded pitfalls, worked explanations).

---

## Exam Format

- **Duration:** 50 minutes
- **Total points:** 100 pts
- **Part I:** 10 multiple-choice, $4 \times 10 = 40$ pts
- **Part II:** multi-part problems, 60 pts
- **Instructor emphasis:** *"Always state the ROC with every transform."*

---

## 1. The Laplace Transform (Lectures 16–17)

### 1.1 Definition and the $s$-Plane

**Bilateral Laplace Transform**
$$X(s) = \int_{-\infty}^{+\infty} x(t)\,e^{-st}\,dt, \qquad s = \sigma + j\omega$$

- $\sigma = 0 \Rightarrow X(j\omega)$ (the Fourier transform).
- LHP: $\sigma < 0$. RHP: $\sigma > 0$. $j\omega$-axis: FT lives here.

### 1.2 Region of Convergence Rules (Memorize)

1. ROC = vertical strip (depends only on $\sigma$).
2. ROC never contains poles.
3. Finite-duration, absolutely integrable $\Rightarrow$ ROC = all $s$.
4. Right-sided $\Rightarrow \operatorname{Re}\{s\} > \max_i \operatorname{Re}\{p_i\}$.
5. Left-sided $\Rightarrow \operatorname{Re}\{s\} < \min_i \operatorname{Re}\{p_i\}$.
6. Two-sided $\Rightarrow$ strip between consecutive poles.
7. $j\omega$-axis $\in$ ROC $\Rightarrow$ Fourier transform exists.

> **Warning (instructor highlight):** $\dfrac{1}{s+a}$ **is ambiguous without the ROC** — could be $e^{-at}u(t)$ or $-e^{-at}u(-t)$.

### 1.3 Laplace Transform Pairs

| $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $u(t)$ | $1/s$ | $\sigma > 0$ |
| $e^{-at}u(t)$ | $\dfrac{1}{s+a}$ | $\sigma > -\operatorname{Re}\{a\}$ |
| $-e^{-at}u(-t)$ | $\dfrac{1}{s+a}$ | $\sigma < -\operatorname{Re}\{a\}$ |
| $t e^{-at}u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\sigma > -\operatorname{Re}\{a\}$ |
| $\dfrac{t^{n-1}}{(n-1)!}e^{-at}u(t)$ | $\dfrac{1}{(s+a)^n}$ | $\sigma > -\operatorname{Re}\{a\}$ |
| $\delta(t - t_0)$ | $e^{-s t_0}$ | all $s$ |
| $e^{-at}\cos(\omega_0 t)u(t)$ | $\dfrac{s+a}{(s+a)^2+\omega_0^2}$ | $\sigma > -a$ |
| $e^{-at}\sin(\omega_0 t)u(t)$ | $\dfrac{\omega_0}{(s+a)^2+\omega_0^2}$ | $\sigma > -a$ |

### 1.4 Laplace Properties

| Property | Time | $s$-Domain |
|---|---|---|
| Linearity | $ax_1 + bx_2$ | $aX_1 + bX_2$ |
| Time shift | $x(t - t_0)$ | $e^{-s t_0} X(s)$ |
| $s$-shift | $e^{s_0 t} x(t)$ | $X(s - s_0)$ |
| Scaling | $x(at)$ | $\dfrac{1}{|a|} X(s/a)$ |
| Convolution | $x_1 * x_2$ | $X_1 X_2$ |
| Differentiation | $dx/dt$ | $sX(s)$ |
| Diff. in $s$ | $-tx(t)$ | $dX/ds$ |

### 1.5 Inverse Laplace: Partial Fractions

1. Decompose $X(s)$ into $\dfrac{A_i}{s - p_i}$ terms (use **cover-up method**).
2. Invert each term with the table.
3. **ROC decides direction:** ROC right of pole $\to u(t)$; ROC left of pole $\to u(-t)$.

**Three pole types:**
- **Distinct real:** each gives $A e^{p_i t} u(\cdot)$.
- **Repeated (order $n$):** need $n$ terms
$$\frac{B_1}{s - p} + \frac{B_2}{(s-p)^2} + \cdots + \frac{B_n}{(s-p)^n}, \qquad \frac{1}{(s+a)^k} \leftrightarrow \frac{t^{k-1}}{(k-1)!}e^{-at}u(t).$$
- **Complex conjugate:** complete the square, use $\cos / \sin$ pairs.

### 1.6 Initial-Value and Final-Value Theorems (Laplace)

$$x(0^+) = \lim_{s \to \infty} sX(s), \qquad x(\infty) = \lim_{s \to 0} sX(s).$$

**FVT valid only if** all poles of $sX(s)$ have $\operatorname{Re}\{p\} < 0$.

---

## 2. CT System Analysis (Lecture 18)

### 2.1 Transfer Function $H(s)$

From an ODE $\sum a_k \dfrac{d^k y}{dt^k} = \sum b_k \dfrac{d^k x}{dt^k}$, replace $d^k/dt^k \to s^k$:
$$H(s) = \frac{Y(s)}{X(s)} = \frac{b_M s^M + \cdots + b_0}{a_N s^N + \cdots + a_0}.$$

### 2.2 Stability (CT, Causal)

> **Golden Rule — CT:** Causal + BIBO stable $\iff$ all poles in the open LHP ($\operatorname{Re}\{p_i\} < 0 \ \forall i$).

| Pole location | Status |
|---|---|
| All $\operatorname{Re}\{p_i\} < 0$ (LHP) | Stable |
| Any $\operatorname{Re}\{p_i\} > 0$ (RHP) | Unstable |
| On $j\omega$-axis, none in RHP | Marginally stable |

### 2.3 Block Diagrams

- **Series:** $H = H_1 \cdot H_2$. **Parallel:** $H = H_1 + H_2$.
- **Negative feedback:** $Q = \dfrac{G}{1 + GF}$. **Positive feedback:** $Q = \dfrac{G}{1 - GF}$.

### 2.4 Unilateral Laplace Transform

Lower limit changes to $0^-$; captures ICs.

**Unilateral Differentiation Property:**
$$\frac{dy}{dt} \xrightarrow{\mathcal{L}_u} sY(s) - y(0^-)$$
$$\frac{d^2 y}{dt^2} \xrightarrow{\mathcal{L}_u} s^2 Y(s) - s y(0^-) - y'(0^-)$$

**Total response** = ZSR (input, zero ICs) + ZIR (ICs, zero input).

---

## 3. The $z$-Transform (Lectures 19–20)

### 3.1 Definition

$$X(z) = \sum_{n=-\infty}^{+\infty} x[n]\,z^{-n}, \qquad z = re^{j\omega}$$

- $|z| = 1 \Rightarrow X(e^{j\omega})$ (the DTFT).
- Unit circle replaces the $j\omega$-axis.

### 3.2 ROC Properties (DT)

Same logic as Laplace, with circles replacing lines:
- ROC = annular ring $r_1 < |z| < r_2$.
- **Right-sided:** $|z| > \max |d_i|$ (exterior).
- **Left-sided:** $|z| < \min |d_i|$ (interior).
- DTFT exists $\iff$ unit circle $\subset$ ROC.

### 3.3 $z$-Transform Pairs

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $u[n]$ | $\dfrac{1}{1 - z^{-1}}$ | $|z| > 1$ |
| $a^n u[n]$ | $\dfrac{1}{1 - a z^{-1}}$ | $|z| > |a|$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1 - a z^{-1}}$ | $|z| < |a|$ |
| $n a^n u[n]$ | $\dfrac{a z^{-1}}{(1 - a z^{-1})^2}$ | $|z| > |a|$ |
| $\delta[n - k]$ | $z^{-k}$ | $|z| > 0$ |
| $r^n \cos(\omega_0 n)u[n]$ | $\dfrac{1 - r\cos\omega_0\,z^{-1}}{1 - 2r\cos\omega_0\,z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |
| $r^n \sin(\omega_0 n)u[n]$ | $\dfrac{r\sin\omega_0\,z^{-1}}{1 - 2r\cos\omega_0\,z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |

### 3.4 $z$-Transform Properties

| Property | Sequence | $z$-Domain |
|---|---|---|
| Linearity | $ax_1 + bx_2$ | $aX_1 + bX_2$ |
| Time shift | $x[n - n_0]$ | $z^{-n_0}X(z)$ |
| $z$-scaling | $z_0^n x[n]$ | $X(z/z_0)$ |
| Convolution | $x_1 * x_2$ | $X_1 X_2$ |
| Diff. in $z$ | $n\,x[n]$ | $-z\,\dfrac{d}{dz}X(z)$ |

### 3.5 Inverse $z$-Transform

Same strategy as Laplace but in $z^{-1}$:
1. Make $X(z)$ proper in $z^{-1}$; long-divide if needed.
2. Partial fractions: $\dfrac{A_i}{1 - d_i z^{-1}}$.
3. ROC outside $|d_i| \to d_i^n u[n]$; inside $\to -d_i^n u[-n-1]$.

### 3.6 IVT / FVT ($z$-domain)

$$x[0] = \lim_{z \to \infty} X(z), \qquad \lim_{n \to \infty} x[n] = \lim_{z \to 1}(1 - z^{-1}) X(z).$$

**FVT valid only if** all poles of $(1 - z^{-1})X(z)$ are inside the unit circle.

---

## 4. DT System Analysis (Lecture 21)

### 4.1 Transfer Function $H(z)$

From a difference equation $\sum a_k y[n-k] = \sum b_k x[n-k]$, replace each delay $\to z^{-k}$:
$$H(z) = \frac{b_0 + b_1 z^{-1} + \cdots + b_M z^{-M}}{a_0 + a_1 z^{-1} + \cdots + a_N z^{-N}}.$$

### 4.2 Stability (DT, Causal)

> **Golden Rule — DT:** Causal + BIBO stable $\iff$ all poles strictly inside the unit circle ($|p_i| < 1\ \forall i$).

| Pole location | Status |
|---|---|
| All $|p_i| < 1$ | Stable |
| Any $|p_i| > 1$ | Unstable |
| On unit circle, none outside | Marginally stable |

### 4.3 Unilateral $z$-Transform

Sum starts at $n = 0$; initial conditions appear via the shift property.

**Unilateral $z$ Shift Property:**
$$y[n-1] \xrightarrow{\mathcal{Z}_u} z^{-1} Y(z) + y[-1]$$
$$y[n-2] \xrightarrow{\mathcal{Z}_u} z^{-2} Y(z) + y[-2] + y[-1] z^{-1}$$

> **Sign trap (instructor warning):** Laplace uses $-y(0^-)$; the $z$-transform uses $+y[-1]$.

**Pipeline:** difference eq. $\to \mathcal{Z}_u \to$ solve $Y(z) \to$ PFE $\to$ invert.
**Total response** = ZSR + ZIR.

---

## 5. Sampling (Lecture 22)

### 5.1 Impulse-Train Sampling

Multiply $x(t)$ by $p(t) = \sum \delta(t - nT)$. In frequency:

**Sampled Spectrum:**
$$X_p(j\omega) = \frac{1}{T} \sum_{k=-\infty}^{+\infty} X\bigl(j(\omega - k\omega_s)\bigr), \qquad \omega_s = \frac{2\pi}{T}.$$

Sampling = "copy-paste the spectrum at every multiple of $\omega_s$, scaled by $1/T$."

### 5.2 Sampling Theorem (Shannon / Nyquist)

Perfect reconstruction from $x(nT)$ requires $\omega_s > 2\omega_M$ (**strict inequality**).
$2\omega_M$ = Nyquist rate. Reconstruct with ideal LPF (gain $T$, cutoff $\omega_M < \omega_c < \omega_s - \omega_M$).

### 5.3 Key Sampling Formulas

| Concept | Formula |
|---|---|
| Sampling period | $T = 2\pi / \omega_s$ |
| Nyquist rate | $2\omega_M$ (must be exceeded) |
| Aliased frequency | $f_\text{alias} = |f_s - f_0|$ ($f_s/2 < f_0 < f_s$) |
| CT $\leftrightarrow$ DT freq. | $\Omega = \omega T$ |
| Reconstruction | $x_r(t) = \sum_n x(nT)\,\operatorname{sinc}\!\left(\dfrac{t - nT}{T}\right)$ |

### 5.4 Aliasing and Practical Notes

> **Aliasing is irreversible.** Overlapping replicas cannot be separated. Prevent with an **anti-aliasing LPF before** the sampler.

- Squaring a signal **doubles** its bandwidth.
- $\omega_s = 2\omega_M$ is **not** sufficient (e.g. $\sin(\omega_s t/2)$ sampled at $\omega_s$ gives all-zero samples).
- ZOH / FOH are practical but **inexact** approximations of sinc interpolation.

---

## 6. Linear Feedback Systems (Lecture 23)

### 6.1 Closed-Loop Transfer Function

**Feedback Formula:**
$$Q(s) = \frac{H(s)}{1 + G(s)H(s)} \qquad \text{(negative feedback)}$$

Positive feedback: replace $+$ with $-$ in the denominator.
$1 + GH = 0 \Rightarrow$ closed-loop poles (determines stability).

### 6.2 Block Diagram Rules

- Cascade $\to$ multiply. Parallel $\to$ add. Feedback $\to H/(1+GH)$.
- **Strategy:** simplify innermost loop first, work outward.

### 6.3 Stability via Closed-Loop Poles

All closed-loop poles in LHP (CT) or inside unit circle (DT) $\Rightarrow$ stable.

| Condition on $GH$ | $Q \approx$ | Meaning |
|---|---|---|
| $|GH| \gg 1$ | $1/G$ | Feedback dominates |
| $|GH| \ll 1$ | $H$ | Feedback negligible |
| $GH = -1$ | $\infty$ | **Instability** |

### 6.4 Nyquist Plot and Criterion

Plot $G(j\omega)H(j\omega)$ in the complex plane ($\omega : -\infty \to +\infty$).

> **Nyquist Criterion (simplified):** Open-loop stable $\Rightarrow$ closed-loop with gain $K$ is stable iff the Nyquist contour **does not encircle** $-1/K$.

### 6.5 Gain Margin and Phase Margin

Instability = $|GH| = 1$ (0 dB) and $\angle GH = -180°$ **simultaneously**.

**GM:** At $\omega_1$ where $\angle GH = -180°$: $\mathrm{GM}_\text{dB} = 0 - |GH(\omega_1)|_\text{dB}$.
**PM:** At $\omega_2$ where $|GH| = 0$ dB: $\mathrm{PM} = 180° + \angle GH(\omega_2)$.
Both positive $\Rightarrow$ stable. Max delay: $\tau_\text{max} = \mathrm{PM\,(rad)} / \omega_2$.

> **Reading Bode plots (instructor warning):** GM is read from the **magnitude** plot at the $-180°$ frequency. PM is read from the **phase** plot at the 0 dB frequency. **Don't mix them up!**

---

## 7. CT vs. DT Quick Reference

| | Laplace (CT) | $z$ (DT) |
|---|---|---|
| Variable | $s = \sigma + j\omega$ | $z = re^{j\omega}$ |
| FT on | $j\omega$-axis | unit circle |
| ROC shape | strip | ring |
| Right-sided | $\sigma > \sigma_\text{max}$ | $|z| > r_\text{max}$ |
| Stable (causal) | poles in LHP | poles $|p| < 1$ |
| Basic pair | $\dfrac{1}{s+a}$ | $\dfrac{1}{1-az^{-1}}$ |
| Delay | $e^{-s t_0}$ | $z^{-n_0}$ |
| Unil. IC | $sY - y(0^-)$ | $z^{-1}Y + y[-1]$ |
| IVT | $\lim_{s\to\infty} sX$ | $\lim_{z\to\infty} X$ |
| FVT | $\lim_{s\to 0} sX$ | $\lim_{z\to 1}(1 - z^{-1})X$ |
| Feedback | $H/(1+GH)$ | (same form) |

---

## 8. Common Mistakes to Avoid (Instructor's List)

1. **Omitting the ROC** — the transform is ambiguous without it.
2. **ROC direction:** right-sided $\to$ right/outside; left $\to$ left/inside.
3. Repeated pole of order $n$ needs $n$ partial-fraction terms.
4. Complex poles: complete the square, don't split conjugates.
5. FVT requires all poles of $sX(s)$ in LHP (or $(1 - z^{-1})X(z)$ inside unit circle).
6. DT stability: check $|a| < 1$, not $a < 1$ (pole at $z = -0.9$ is stable).
7. Unilateral sign: Laplace $-y(0^-)$; $z$-transform $+y[-1]$.
8. Don't mix Hz and rad/s ($\omega = 2\pi f$).
9. $\omega_s = 2\omega_M$ is **not enough**; need strict $>$.
10. Negative feedback $\to 1 + GH$; positive $\to 1 - GH$.
11. GM from magnitude plot; PM from phase plot.

---

## 9. Practice Questions (Instructor-Provided)

### 9.1 Lecture 22 — Sampling

1. $X(j\omega) = 0$ for $|\omega| > 5000\pi$. Find the Nyquist rate and the max allowable $T$.
2. True or false: $\omega_s = 2\omega_M$ guarantees perfect reconstruction.
3. In one sentence, why does sampling in time create copies of the spectrum?
4. Overlapping replicas appear in $X_p(j\omega)$. Can a filter undo this? Why or why not?
5. What is an anti-aliasing filter? Does it go before or after the sampler?
6. Nyquist rate of $x(t) = \cos(600\pi t) + \cos(1800\pi t)$?
7. $\omega_M = 3000\pi$, $T = 2 \times 10^{-4}$ s. Compute $\omega_s$; does aliasing occur?
8. $x(t) = \cos(2\pi \cdot 900\,t)$, $f_s = 1000$ Hz. Reconstructed frequency?
9. Same signal, $f_s = 1500$ Hz. Reconstructed frequency?
10. Signal has Nyquist rate $\omega_0$. Nyquist rate of $x(t - 5)$? Of $x(2t)$?
11. Why does the ideal reconstruction LPF have gain $T$?
12. Is ZOH reconstruction exact? What error does it introduce?
13. Camera at 24 fps, blade at 25 rev/s. What does the blade look like on film?
14. $X(j\omega) = 0$ for $|\omega| > 10{,}000\pi$; $f_s = 8000$ Hz. Is the theorem satisfied? Min $f_s$?
15. $x(t)$ is not band-limited. Can we ever sample it? What do real systems do?

### 9.2 Lecture 23 — Linear Feedback Systems

**Block Diagram Simplification**
1. Cascade + unity negative feedback: $H_1 = \dfrac{2}{s+1}$, $H_2 = \dfrac{1}{s+4}$. Find $Q(s)$.
2. Parallel forward path $\dfrac{3}{s+2} + \dfrac{1}{s+5}$, feedback $G = 4$. Find $Q(s)$.
3. Nested loops: inner forward $1/s$, inner feedback $3$; outer unity feedback. Find $Q(s)$.

**Closed-Loop Poles and Stability**

4. $H(s) = K/(s+5)$, $G = 1$.
   - (a) Closed-loop TF and pole?
   - (b) Stable for which $K$?
   - (c) $K$ for pole at $s = -10$?
5. $H(s) = K/[(s+1)(s+2)]$, $G = 1$.
   - (a) Characteristic equation?
   - (b) Range of $K$ for stability?
6. DT: $H(z) = Kz^{-1}/(1 - 0.8 z^{-1})$, $G = 1$.
   - (a) Closed-loop pole vs. $K$?
   - (b) $K > 0$ range for stability?

**Gain and Phase Margins**

7. Bode data: at $\omega_2 = 5$ ($|GH| = 0$ dB): $\angle GH = -150°$. At $\omega_1 = 20$ ($\angle GH = -180°$): $|GH| = -8$ dB.
   - (a) Phase margin?
   - (b) Gain margin?
   - (c) Stable?
   - (d) Max tolerable time delay?

**True / False**

8. Negative feedback always stabilizes a system.
9. Phase margin of $60°$ $\Rightarrow$ stable.
10. A Nyquist plot is $G(j\omega)H(j\omega)$ plotted in the complex plane.

---

*"Good luck on the exam!" — R. Gracia Otalvaro*
