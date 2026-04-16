# CEC 315 — Master Homework Problem Collection

**Course:** CEC 315 Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro / Jianhua Liu
**Scope:** Every assigned / practice homework problem from the course, grouped by exam coverage and lecture topic, with solutions where available.

This document is assembled from the PDFs in `hw_practice_problems/` plus existing student-prepared solution notes in `homework/` and `exam2/`. Each problem is tagged with its source file. Part III (Exam 3, lectures 16-23) is the most thorough since the student is prepping for Exam 3.

---

## Table of Contents

- [Part I — Exam 1 Homework (Chapter 1, Lectures 3-8)](#part-i--exam-1-homework)
  - [HW Chapter 1 — Signals, Systems, Complex Numbers](#hw-chapter-1--signals-systems-complex-numbers)
  - [Lecture 3 Exercise — Euler Derivations](#lecture-3-exercise--euler-derivations)
  - [Lecture 4 Exercise — Fundamental Functions and Systems](#lecture-4-exercise--fundamental-functions-and-systems)
  - [Lecture 5 Exercise — Basic System Properties](#lecture-5-exercise--basic-system-properties)
  - [Lecture 6 Problems — DT Convolution Practice](#lecture-6-problems--dt-convolution-practice)
  - [Lecture 7 Problems — CT LTI Sifting / Convolution](#lecture-7-problems--ct-lti-sifting--convolution)
  - [Lecture 8 Problems — Differential / Difference Equations](#lecture-8-problems--differential--difference-equations)
- [Part II — Exam 2 Homework (Lectures 9-15)](#part-ii--exam-2-homework)
  - [HW Lectures 9-11 — Fourier Series, DTFS, Frequency Response](#hw-lectures-9-11--fourier-series-dtfs-frequency-response)
  - [HW Lectures 12-15 — Fourier Transforms, Properties, Filters, Bode](#hw-lectures-12-15--fourier-transforms-properties-filters-bode)
- [Part III — Exam 3 Homework (Lectures 16-23)](#part-iii--exam-3-homework)
  - [HW Lectures 16-18 — Laplace Transform: Definition, Inversion, Properties, System Analysis](#hw-lectures-16-18--laplace-transform)
  - [HW Lectures 19-21 — z-Transform: Definition, Inversion, Properties, System Analysis](#hw-lectures-19-21--z-transform)
  - [Lecture 22 Exercise — Sampling](#lecture-22-exercise--sampling)
  - [Lecture 23 Exercise — Feedback Systems](#lecture-23-exercise--feedback-systems)

---

# Part I — Exam 1 Homework

## HW Chapter 1 — Signals, Systems, Complex Numbers

**Lecture tag:** Lectures 2-5 (preliminary material)
**Source:** `hw_practice_problems/hw-chapter01.pdf` (also `homework/hw1/Homework_Chapter_1_CEC-315-rev1 (2).pdf`)
**Solutions available:** No dedicated solutions PDF; students work through book Chapter 1.

### Problem 1 — Power and Energy

Determine the values of $P_\infty$ and $E_\infty$ for each of the following signals:

1. $x_1(t) = e^{-2t}\,u(t)$
2. $x_2(t) = e^{j(2t+\pi/4)}$
3. $x_3(t) = \cos(t)$
4. $x_1[n] = (1/2)^n\,u[n]$
5. $x_2[n] = e^{j(\pi n/2 + \pi/8)}$
6. $x_3[n] = \cos(\pi n/4)$

### Problem 2 — Periodicity

Determine whether or not each of the following signals is periodic. If periodic, specify the fundamental period.

1. $x_1(t) = j\,e^{j10 t}$
2. $x_2(t) = e^{(-1+j)t}$
3. $x_3[n] = e^{j 7\pi n}$
4. $x_4[n] = 3\,e^{j 3\pi(n+1/2)/5}$
5. $x_5[n] = 3\,e^{j(3/5)(n+1/2)}$

### Problem 3 — System Properties

For each continuous-time system, determine which of the following hold: (1) Memoryless, (2) Time invariant, (3) Linear, (4) Causal, (5) Stable. Justify.

1. $y(t) = x(t-2) + x(2-t)$
2. $y(t) = [\cos(3t)]\,x(t)$
3. $y(t) = \int_{-\infty}^{2t} x(\tau)\,d\tau$
4. $y(t) = 0$ for $t<0$; $y(t) = x(t)+x(t-2)$ for $t\ge 0$
5. $y(t) = 0$ for $x(t)<0$; $y(t) = x(t)+x(t-2)$ for $x(t)\ge 0$
6. $y(t) = x(t/3)$
7. $y(t) = dx(t)/dt$

### Problem 4 — Signal Transformations

A CT signal $x(t)$ is given by a piecewise plot (trapezoid: value 2 on $-1\le t<0$, then a line from 2 at $t=0$ down to 0 at $t=2$; zero outside). Sketch and label:

1. $x(t-1)$
2. $x(2-t)$
3. $x(2t+1)$
4. $x(4 - t/2)$
5. $[x(t) + x(-t)]\,u(t)$
6. $x(t)\,[\delta(t+3/2) - \delta(t-3/2)]$

### Problem 5 — Complex Numbers in Polar Form

Express each complex number in polar form and plot:

1. $1 + j\sqrt{3}$
2. $-5$
3. $-5 - 5j$
4. $3 + 4j$
5. $(1 - j\sqrt{3})^3$
6. $(1+j)^5$
7. $(\sqrt{3} + j3)(1-j)$
8. $\dfrac{2 - j(6/\sqrt{3})}{2 + j(6/\sqrt{3})}$
9. $\dfrac{1+j\sqrt{3}}{\sqrt{3}+j}$
10. $j(1+j)\,e^{j\pi/6}$
11. $(\sqrt{3}+j)\,2\sqrt{2}\,e^{-j\pi/4}$
12. $\dfrac{e^{j\pi/3}-1}{1+j\sqrt{3}}$

---

## Lecture 3 Exercise — Euler Derivations

**Lecture tag:** Lecture 3 (Complex numbers, exponential and sinusoidal signals)
**Source:** `hw_practice_problems/lctr03-exercise-euler-derivations.pdf`
**Solutions available:** No written solutions; derivations are standard.

### Exercise

Derive the following identities starting from Euler's formula $e^{j\theta}=\cos\theta+j\sin\theta$:

1. $\cos(\alpha+\beta) = ?$
2. $\cos(\alpha-\beta) = ?$
3. $\sin(\alpha+\beta) = ?$
4. $\sin(\alpha-\beta) = ?$
5. $\cos(\alpha)\cos(\beta) = ?$
6. $\cos(\alpha)\sin(\beta) = ?$
7. $\sin(\alpha)\sin(\beta) = ?$

**Standard results (for reference):**
- $\cos(\alpha\pm\beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$
- $\sin(\alpha\pm\beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$
- $\cos\alpha\cos\beta = \tfrac{1}{2}[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$
- $\cos\alpha\sin\beta = \tfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)]$
- $\sin\alpha\sin\beta = \tfrac{1}{2}[\cos(\alpha-\beta)-\cos(\alpha+\beta)]$

---

## Lecture 4 Exercise — Fundamental Functions and Systems

**Lecture tag:** Lecture 4
**Source:** `hw_practice_problems/lctr04-exercise.pdf`
**Solutions available:** No written solutions.

### Exercise 1 — CT integrator with impulse train input

A CT integration system has input-output relation
$$y(t) = \int_0^t x(\tau)\,d\tau.$$
Assume $x(t) = \delta(t+1) + \delta(t-1) + \delta(t-3)$.

- Determine $y(t)$ in terms of shifted/scaled fundamental functions.
- Sketch both input and output.

### Exercise 2 — CT differentiator with rectangular input

A CT differentiation system has $y(t) = dx(t)/dt$. Assume
$$x(t) = \begin{cases}1, & 0 < t < 2\\ 0, & \text{otherwise}\end{cases}.$$

- Determine $y(t)$ in terms of shifted/scaled fundamental functions.
- Sketch both input and output.

---

## Lecture 5 Exercise — Basic System Properties

**Lecture tag:** Lecture 5
**Source:** `hw_practice_problems/lctr05-exercise.pdf`
**Solutions available:** No written solutions.

### Exercise 1 — Classify two DT systems

Consider
$$T_1(x[n]) = \frac{1}{x[n+1]}, \qquad T_2(x[n]) = x[n] + 0.5\,x[n+1].$$
Determine if each system is: invertible, causal, BIBO stable, time invariant, linear, memoryless.

### Exercise 2 — Waveform sketching (convolution prep)

Sketch:
1. $x_1[n] = 0.5^n\,u[n]$
2. $x_2[n] = x_1[n-2]$
3. $x_3[n] = x_2[-n]$

---

## Lecture 6 Problems — DT Convolution Practice

**Lecture tag:** Lecture 6
**Source:** `hw_practice_problems/lctr06-convolution-problems.pdf`
**Solutions available:** No solutions PDF.

For each problem, compute $y[n] = x[n]*h[n]$.

### Problem 1 (Easy)
$x[n] = \{2,1\}$ for $n=0,1$; $h[n] = \{1,3\}$ for $n=0,1$.

### Problem 2 (Easy-Medium)
$x[n] = \{1,2,1\}$ for $n=0,1,2$; $h[n] = \{1,-1\}$ for $n=0,1$.

### Problem 3 (Medium)
$x[n] = \{1,0,2\}$ for $n=0,1,2$; $h[n] = \{2,1,1\}$ for $n=0,1,2$.

### Problem 4 (Medium)
$x[n] = \{1,2,3,4\}$ for $n=0,1,2,3$; $h[n] = \{1,1\}$ for $n=0,1$.

### Problem 5 (Medium)
$x[-1]=1, x[0]=2, x[1]=-1$ (zero elsewhere); $h[n]=\{3,1\}$ for $n=0,1$.

---

## Lecture 7 Problems — CT LTI Sifting / Convolution

**Lecture tag:** Lecture 7
**Source:** `hw_practice_problems/lctr07-convolution-problems.pdf`
**Solutions available:** No solutions PDF.

### Problem 1 — Sifting property (unbounded limits)

Evaluate:
1. $\int_{-\infty}^{\infty} (3t^2 - 2t + 5)\,\delta(t-1)\,dt$
2. $\int_{-\infty}^{\infty} \cos(\pi t)\,\delta(t+0.5)\,dt$
3. $\int_{-\infty}^{\infty} e^{-2t}\,\delta(t-3)\,dt$

### Problem 2 — Sifting property (finite limits)

1. $\int_0^{10} t^3\,\delta(t-2)\,dt$
2. $\int_0^{5} e^{t}\,\delta(t+3)\,dt$
3. $\int_{-2}^{2} (t+1)^2\,\delta(t+1)\,dt$

### Problem 3 — System properties from impulse responses

For each $h(t)$, determine memory, causality, BIBO stability (show the stability integral):
1. $h(t) = 3\delta(t)$
2. $h(t) = e^{-3t}u(t)$
3. $h(t) = e^{2t}u(-t)$
4. $h(t) = e^{t}u(t)$

### Problem 4 — Convolution with a shifted impulse

Use $x(t)*\delta(t-t_0) = x(t-t_0)$ to compute:
1. $e^{-2t}u(t) * \delta(t-3)$
2. $\cos(2\pi t) * \delta(t+1)$
3. $[u(t) - u(t-2)] * \delta(t-4)$

### Problem 5 — Convolution integral

With $x(t) = u(t)-u(t-2)$ (pulse of height 1) and $h(t) = e^{-t}u(t)$, compute $y(t) = x(t)*h(t)$, splitting into cases on $t$.

---

## Lecture 8 Problems — Differential / Difference Equations

**Lecture tag:** Lecture 8
**Source:** `hw_practice_problems/lctr08-problems.pdf`
**Solutions available:** No solutions PDF (standard formulas).

### Problem 1 — CT first-order system

$$\frac{dy(t)}{dt} + 3\,y(t) = 6\,x(t), \quad \text{causal, initial rest.}$$
(a) Find the impulse response $h(t)$.
(b) Is the system stable? Why?
(c) Find $h(0)$ and $h(1)$.

### Problem 2 — DT first-order system

$$y[n] = \tfrac{1}{3}\,y[n-1] + 2\,x[n], \quad \text{causal, initial rest.}$$
(a) Use iteration with $x[n]=\delta[n]$ to find $h[0], h[1], h[2], h[3]$.
(b) Write the general formula for $h[n]$.
(c) Is the system stable? Why?

---

# Part II — Exam 2 Homework

## HW Lectures 9-11 — Fourier Series, DTFS, Frequency Response

**Source:** `hw_practice_problems/hw-lctr09-11.pdf`
**Solutions:** `hw_practice_problems/hw-lctr09-11-solutions.pdf` (complete, 17 pages); also summarized in `exam2/hw_lctr9_11_solutions_summary.md`.

### Problem 1 — Eigenfunction Property and CT FS Coefficients (Lecture 9)

LTI system with $h(t) = e^{-4t}u(t)$.

**(a) Eigenfunction property.** Input $x(t) = \cos(3t)$. Compute $H(j3) = \int_0^\infty e^{-4\tau}e^{-j3\tau}d\tau$ in rectangular and polar form. Write the output $y(t)$.

**(b) Fourier series coefficients.** Periodic $x(t)$, $T=4\text{ s}$, with $x(t) = 3$ for $0\le t<1$ and $x(t)=0$ for $1\le t<4$.
  1. Find $\omega_0$ (rad/s).
  2. Compute $a_0$ using the average-value formula; explain.
  3. Derive $a_k$ ($k\ne 0$) via the analysis integral.
  4. Compute $a_1, a_2$ in polar form.

**(c) Conjugate symmetry.** Verify $a_{-1} = a_1^*$ and state what this requires of $x(t)$.

**Solution summary** (from solutions PDF):
- $H(j3) = \dfrac{1}{4+j3} = \dfrac{4}{25} - j\dfrac{3}{25}$; $|H(j3)| = 1/5 = 0.2$; $\angle H(j3) = -\arctan(3/4) = -36.87^\circ$. $\boxed{y(t) = 0.2\cos(3t - 36.87^\circ)}$.
- $\omega_0 = 2\pi/4 = \pi/2$ rad/s.
- $a_0 = \tfrac{1}{4}\int_0^1 3\,dt = 3/4 = 0.75$.
- $a_k = \dfrac{3}{2jk\pi}(1-e^{-jk\pi/2})$ for $k\ne 0$.
- $a_1 = \dfrac{3(1-j)}{2\pi} \approx 0.477 - 0.477j$, $|a_1| = \dfrac{3\sqrt 2}{2\pi}\approx 0.675$, $\angle a_1 = -45^\circ$.
- $a_2 = -\dfrac{3j}{2\pi}$, $|a_2| = 3/(2\pi) \approx 0.477$, $\angle a_2 = -90^\circ$.
- $a_{-1} = \dfrac{3(1+j)}{2\pi} = a_1^*$. Holds for any real-valued signal.

### Problem 2 — CT FS Convergence and Gibbs (Lecture 10)

Odd square wave, period $T=2\pi$, $x(t)=+1$ on $(0,\pi)$ and $-1$ on $(-\pi,0)$, Fourier series
$x(t) = \tfrac{4}{\pi}\sum_{k\text{ odd}}^\infty \tfrac{1}{k}\sin(kt)$.

**(a) Dirichlet conditions.** State the three conditions and verify for this signal. Discuss $t=0$ and $t=\pm\pi$.

**(b) Convergence at specific points.** What does the series converge to at $t=0$? At $t=\pi/2$? Evaluate the three-term partial sum at $t=\pi/2$ and compare with $x(\pi/2)$.

**(c) Partial sums and Gibbs.**
  1. Write $x_1(t)$ and $x_3(t)$ explicitly.
  2. State the ~9% Gibbs overshoot rule; does it vanish as $N\to\infty$?
  3. Why can a finite sum of harmonics never reconstruct a jump discontinuity?

**(d) Smoothness and spectral decay.** Square wave has $a_k\sim 1/k$; triangular wave has $a_k\sim 1/k^2$. Connect spectral decay to smoothness.

**Solution summary:**
- All three Dirichlet conditions hold: $\int_{-\pi}^{\pi}|x|\,dt=2\pi<\infty$, zero extrema, two finite-jump discontinuities per period.
- FS at $t=0$ converges to $(x(0^-)+x(0^+))/2 = 0$. At $t=\pi/2$, continuity gives $x(\pi/2)=1$. Three-term sum: $\tfrac{4}{\pi}[1 - 1/3 + 1/5] = \tfrac{52}{15\pi}\approx 1.103$ (overshoots by ~10.3%).
- $x_1(t) = \tfrac{4}{\pi}\sin t$; $x_3(t) = \tfrac{4}{\pi}[\sin t + \tfrac{\sin 3t}{3} + \tfrac{\sin 5t}{5}]$.
- Gibbs overshoot ≈ 8.9% of jump height, does NOT vanish as $N\to\infty$; ripple narrows but peak persists.
- Triangular wave is smoother. General rule: if the first discontinuous derivative is the $m$-th, coefficients decay as $1/k^{m+1}$.

### Problem 3 — CT FS Properties (Lecture 10)

Real $x(t)$, $T=\pi$, $\omega_0 = 2$, coefficients $a_0 = 2$, $a_{\pm 1}=1$, $a_{\pm 2}=1/4$, $a_{\pm 3}=1/9$, $a_k=0$ for $|k|>3$.

**(a) Linearity.** $w(t) = 4x(t) + 6\sin(2t)$. Find FS coefficients of $\sin(2t)$, then $c_k$ for $w(t)$.

**(b) Time shifting.** $y(t) = x(t-\pi/4)$. Find $b_k$; verify $|b_k|=|a_k|$ for $k=1,2$. What does this say about power spectral density?

**(c) Differentiation.** $g(t) = dx/dt$; find $d_k = jk\omega_0 a_k$. Compute $|d_1|, |d_2|, |d_3|$.

**(d) Parseval.** $P_x = \sum_{k}|a_k|^2$. Compute numerically; what fraction of power is DC?

**Solution summary:**
- $\sin(2t)$: $b_1 = -j/2$, $b_{-1}=j/2$, else 0.
- $c_0 = 8$, $c_1 = 4-3j$, $c_{-1} = 4+3j$, $c_{\pm 2}=1$, $c_{\pm 3}=4/9$.
- Time shift: $b_k = a_k e^{-jk\pi/2}$; magnitudes unchanged. Same power spectrum; time shift only redistributes phase.
- $|d_1|=2, |d_2|=1, |d_3|=2/3$. $|d_k|/|a_k| = 2|k|$: differentiation amplifies high frequencies.
- $P_x = 4 + 2(1 + 1/16 + 1/81) = 6 + 97/648 \approx 6.1497$. DC fraction $= 4/6.1497 \approx 65\%$.

### Problem 4 — Discrete-Time Fourier Series (Lecture 10)

$x[n]$ periodic with $N=6$, $x[n]=1$ for $n=0,1,2$ and $x[n]=0$ for $n=3,4,5$.

**(a)** State DTFS analysis/synthesis equations; how many distinct coefficients for period $N$, and why finite?
**(b)** Compute $a_0, a_1, a_2, a_3$ via the analysis sum.
**(c)** Use periodicity $a_{k+N}=a_k$ to state $a_4, a_5$.
**(d)** Verify Parseval's: $\tfrac{1}{N}\sum|x[n]|^2 = \sum|a_k|^2$.

**Solution summary:**
- $\omega_0 = \pi/3$.
- $a_0 = 1/2$; $a_1 = (1-j\sqrt 3)/6$, $|a_1|=1/3$, $\angle = -60^\circ$; $a_2 = 0$; $a_3 = 1/6$.
- By periodicity: $a_4 = a_{-2} = a_2^* = 0$; $a_5 = a_{-1} = a_1^* = (1+j\sqrt 3)/6$.
- Parseval LHS: $\tfrac{1}{6}(1+1+1+0+0+0) = 1/2$. RHS: $(1/2)^2 + (1/3)^2 + 0 + (1/6)^2 + 0 + (1/3)^2 = 9/36+4/36+1/36+4/36 = 18/36 = 1/2$. ✓

### Problem 5 — Frequency Response and Filtering (Lecture 11)

$h(t) = e^{-3t}u(t)$, input $x(t) = 2 + 4\cos(3t) + 2\cos(9t)$.

**(a)** Compute $H(j\omega) = \int h(\tau)e^{-j\omega\tau}d\tau$; write as $1/(a+j\omega)$.
**(b)** Build the table of $H(j\omega), |H|, \angle H$ at $\omega = 0, 3, 9$.
**(c)** Write the output $y(t)$ via the eigenfunction property.
**(d)** Filtering interpretation: is the higher harmonic more attenuated? Lowpass vs highpass? Sketch $|H|$ and mark $\omega_c$.
**(e)** If $h'(t)=e^{-10t}u(t)$, how does the cutoff change? Is $y'$ more/less similar to $x$?

**Solution summary:**
- $H(j\omega) = \dfrac{1}{3+j\omega}$, so $a = 3$.
- $\omega=0$: $H=1/3$, $|H|=1/3\approx 0.333$, $\angle=0^\circ$.
- $\omega=3$: $H=1/(3(1+j)) = \tfrac{1}{3\sqrt 2}\,e^{-j45^\circ}$, $|H|\approx 0.236$, $\angle = -45^\circ$.
- $\omega=9$: $|H|=1/(3\sqrt{10})\approx 0.105$, $\angle = -\arctan 3 \approx -71.57^\circ$.
- $y(t) = \tfrac{2}{3} + \tfrac{2\sqrt 2}{3}\cos(3t-45^\circ) + \tfrac{2}{3\sqrt{10}}\cos(9t-71.57^\circ)$.
- Ratio $|H(j9)|/|H(j3)| = 1/\sqrt 5 \approx 0.447$: high harmonic more attenuated. Lowpass. $\omega_c = 3$ rad/s.
- For $a=10$: $\omega_c' = 10$ rad/s; wider bandwidth; $y'$ more similar to $x$.

---

## HW Lectures 12-15 — Fourier Transforms, Properties, Filters, Bode

**Source:** `hw_practice_problems/hw-lctr12-15.pdf`
**Solutions:** `hw_practice_problems/hw-lctr12-15-solutions.pdf`; also full worked solutions in `homework/hw4/hw4_solutions.md` and summary in `exam2/hw_lctr12_15_solutions_summary.md`.

### Problem 1 — CT Fourier Transform Basic Pairs (Lecture 12)

**(a) One-sided exponential.** $x(t) = 3e^{-5t}u(t)$. Compute $X(j\omega)$ from the definition; express as $A/(a+j\omega)$; find $|X|$ and $\angle X$.

**(b) Two-sided exponential.** $g(t) = 4e^{-2|t|}$. Split the integral; show real result; explain via symmetry.

**(c) Rectangular pulse.** $p(t)=2$ for $|t|\le 3$, else 0.
  1. $P(j\omega)$ from the definition.
  2. $P(0)$ as area.
  3. First two positive zeros of $P(j\omega)$.

**(d) Sanity check.** Verify $X(0) = \int x(t)\,dt$ for each.

**Solution summary** (from `hw4_solutions.md`):
- $X(j\omega) = 3/(5+j\omega)$; $|X| = 3/\sqrt{25+\omega^2}$; $\angle X = -\arctan(\omega/5)$; $X(0) = 0.6$ ✓.
- $G(j\omega) = 16/(4+\omega^2)$ (real & even, zero phase); $G(0) = 4$ ✓.
- $P(j\omega) = 4\sin(3\omega)/\omega = 12\,\text{sinc}(3\omega/\pi)$; $P(0) = 12$. First zeros at $\omega = \pi/3, 2\pi/3$.

### Problem 2 — DTFT Basic Pairs (Lecture 12)

**(a)** $x[n] = (0.6)^n u[n]$. DTFT via geometric series.
**(b)** Evaluate $|X(e^{j0})|, |X(e^{j\pi})|$. Lowpass or highpass? Over what interval is $X$ completely specified?
**(c) Finite-length.** $h[n]=\{1,2,3,2,1\}$ for $n=0..4$. Compute $H(e^{j\omega})$ and $H(e^{j0})$. Show $H(e^{j\omega}) = e^{-j2\omega}R(\omega)$ with $R$ real.

**Solution summary:**
- $X(e^{j\omega}) = 1/(1 - 0.6 e^{-j\omega})$.
- $X(e^{j0}) = 1/0.4 = 2.5$; $X(e^{j\pi}) = 1/1.6 = 0.625$. Lowpass. Period $2\pi$, so specified on any $2\pi$-interval.
- $H(e^{j0}) = 9$; factoring out $e^{-j2\omega}$: $H(e^{j\omega}) = e^{-j2\omega}[3 + 4\cos\omega + 2\cos 2\omega]$. The $e^{-j2\omega}$ is a linear phase (delay of 2 samples) — symmetric FIR filters have linear phase.

### Problem 3 — FT Properties and Convolution (Lecture 13)

Let $x(t) = e^{-3t}u(t)$, $X(j\omega) = 1/(3+j\omega)$.

**(a) Time shift.** $y(t) = e^{-3(t-2)}u(t-2)$. Find $Y$; verify $|Y| = |X|$.
**(b) Frequency shift.** $z(t) = e^{-3t}u(t)\cos(10 t)$.
**(c) Differentiation.** Verify the differentiation property on $w(t) = -3e^{-3t}u(t)+\delta(t)$.
**(d) Convolution property.** $h(t) = 2e^{-4t}u(t)$. Find $Y = XH$ via partial fractions, then $y(t)$; verify $y(0), y(\infty)$.

**Solution summary:**
- $Y(j\omega) = e^{-j2\omega}/(3+j\omega)$; magnitude unchanged.
- $Z(j\omega) = \tfrac{1}{2}[1/(3+j(\omega-10)) + 1/(3+j(\omega+10))]$.
- $W(j\omega) = j\omega/(3+j\omega) = j\omega X(j\omega)$ ✓.
- $Y = 2/[(3+j\omega)(4+j\omega)]$; PF: $A=2$, $B=-2$. $y(t) = 2(e^{-3t}-e^{-4t})u(t)$; $y(0)=0$, $y(\infty)=0$.

### Problem 4 — Systems from Differential / Difference Equations (Lectures 13, 15)

**(a) CT.** $y'' + 7y' + 10y = 3x$.
  1. $H(j\omega)$ via $d/dt\to j\omega$.
  2. Poles; stable?
  3. Partial fractions.
  4. $h(t)$.
  5. $|H|$ at $\omega=0,1,10$. Lowpass or highpass?

**(b) DT.** $y[n] - 0.5\,y[n-1] - 0.06\,y[n-2] = x[n]$.
  1. $H(e^{j\omega})$ via $y[n-k]\to e^{-jk\omega}Y$.
  2. Poles; stable?
  3. Partial fractions.
  4. $h[n]$.
  5. $|H(e^{j0})|, |H(e^{j\pi})|$. Lowpass or highpass?

**Solution summary:**
- CT: $H(j\omega) = 3/[(j\omega+2)(j\omega+5)]$, poles at $-2,-5$ (stable). $H = 1/(j\omega+2)-1/(j\omega+5)$. $h(t)=(e^{-2t}-e^{-5t})u(t)$. Lowpass; $|H(0)|=0.3$.
- DT: Poles at $z=0.6$ and $z=-0.1$ (both inside unit circle → stable). PF: $A=6/7, B=1/7$; $h[n] = (6/7)(0.6)^n u[n] + (1/7)(-0.1)^n u[n]$. $|H(e^{j0})| \approx 2.273$, $|H(e^{j\pi})|\approx 0.694$ — lowpass.

### Problem 5 — Magnitude, Phase, Group Delay (Lecture 14)

$H(j\omega) = 1/(1+j\omega/5)$, cutoff $\omega_c = 5$.

**(a)** Fill the table of $|H|, |H|_{\mathrm{dB}}, \angle H$ at $\omega \in \{0, 0.5, 1, 5, 10, 50, 500\}$.
**(b)** Derive $\tau(\omega) = -\tfrac{d}{d\omega}\angle H$. Evaluate $\tau(0), \tau(5)$. Constant?
**(c)** Linear-phase test at $\omega=5$.
**(d)** Two-tone input $x(t)=\cos t + \cos(50 t)$. Find $y(t)$ and the attenuation ratio in dB.

**Solution summary:**
- $|H(0)|=1$ (0 dB, 0°); $|H(1)|\approx 0.981$ (−0.17 dB, −11.3°); $|H(5)|=1/\sqrt 2$ (−3.01 dB, −45°); $|H(10)|\approx 0.447$ (−6.99 dB, −63.4°); $|H(50)|\approx 0.0995$ (−20.04 dB, −84.3°).
- $\tau(\omega) = (1/5)/(1+(\omega/5)^2) = 5/(25+\omega^2)$; $\tau(0)=0.2$, $\tau(5)=0.1$ — not constant → nonlinear phase.
- At $\omega=5$ linear-phase prediction is $-\omega/\omega_c = -1$ rad $=-57.3^\circ$ vs actual $-45^\circ$ (deviation ~12°).
- $y(t) \approx 0.981\cos(t-11.3^\circ) + 0.0995\cos(50t-84.3^\circ)$; attenuation ~20 dB.

### Problem 6 — Second-Order Systems and Bode Plots (Lecture 15)

$H(j\omega) = \dfrac{\omega_n^2}{(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2}$, $\omega_n = 20$, $\zeta=0.25$.

**(a)** Underdamped/critically damped/overdamped? Is there a resonance peak?
**(b)** $|H(0)|$; $|H(j\omega_n)|$ in dB; $\omega_r = \omega_n\sqrt{1-2\zeta^2}$ and $|H|_{\max} = 1/(2\zeta\sqrt{1-\zeta^2})$.
**(c)** Step response: %OS, $t_s$, $\omega_d$.
**(d)** Bode asymptotes: low-frequency, high-frequency slope (dB/dec), break frequency, actual-vs-asymptote gap at $\omega=\omega_n$.

**Solution summary:**
- Underdamped ($\zeta<1$); resonance exists ($\zeta < 1/\sqrt 2$).
- $|H(0)| = 1$ (0 dB); $|H(j\omega_n)| = 1/(2\zeta) = 2$ (≈6.02 dB); $\omega_r = 20\sqrt{0.875}\approx 18.71$; $|H|_{\max}=1/(2\cdot 0.25\cdot\sqrt{0.9375})\approx 2.065$ (≈6.30 dB).
- %OS $= 100 e^{-\pi(0.25)/\sqrt{0.9375}} \approx 44.4\%$; $t_s \approx 4/(0.25\cdot 20) = 0.8$ s; $\omega_d = 20\sqrt{0.9375}\approx 19.36$.
- Bode: 0 dB flat at low freq; −40 dB/decade high freq slope; break at $\omega_n = 20$; peak excess ≈6 dB over asymptote.

---

# Part III — Exam 3 Homework

## HW Lectures 16-18 — Laplace Transform

**Source:** `hw_practice_problems/hw-lctr16-18.pdf` (extracted text `hw-lctr16-18.md`)
**Solutions available:** **Yes — full official solutions in [`homework/hw5/hw5_solutions.md`](../homework/hw5/hw5_solutions.md)** (transcribed from `hw-lctr16-18-solutions.pdf`).

### Solutions Summary

Full official solutions with all algebra: [`hw5_solutions.md`](../homework/hw5/hw5_solutions.md).

- **P1(a)** — $\boxed{X_1(s) = \dfrac{4}{s+2},\; \Re\{s\}>-2}$ — standard causal $e^{-at}u(t)$ pair.
- **P1(b)** — $\boxed{X_2(s) = \dfrac{3}{s-5},\; \Re\{s\}<5}$ — anti-causal pair $-e^{-at}u(-t)\!\leftrightarrow\!1/(s+a)$.
- **P1(c)** — $\boxed{X_3(s) = 7e^{-3s},\; \text{all } s}$ — time-shifted impulse pair.
- **P1(d)** — $\boxed{X_4(s) = \dfrac{1}{(s+4)^2},\; \Re\{s\}>-4}$ — $t\,e^{-at}u(t)$ pair.
- **P1(e)** — $\boxed{X_5(s) = \dfrac{-3s+1}{(s+1)(s+3)},\; \Re\{s\}>-1}$ — linearity, common denominator; poles $-1,-3$, zero $1/3$.
- **P1(f)** — $\boxed{X_6(s) = \dfrac{-2(s+5)}{(s+2)(s-4)},\; -2<\Re\{s\}<4}$ — two-sided strip ROC contains $j\omega$-axis, so FT exists.
- **P2(a)** — $\boxed{x(t) = \tfrac{2}{3}e^{-t}u(t) + \tfrac{7}{3}e^{-4t}u(t)}$ — partial fractions, distinct real poles, right-sided.
- **P2(b)** — $\boxed{x(t) = \tfrac{8}{5}e^{-2t}u(t) - \tfrac{2}{5}e^{3t}u(-t)}$ — strip ROC splits into right- and left-sided terms.
- **P2(c)** — $\boxed{x(t) = [-\tfrac{2}{3}e^{-2t} + 2te^{-2t} + \tfrac{2}{3}e^{-5t}]u(t)}$ — repeated pole at $-2$; cover-up + $s^2$-coefficient matching.
- **P2(d)** — $\boxed{x(t) = e^{-3t}\cos(4t)u(t)}$ — complete the square $(s+3)^2+4^2$; damped cosine pair.
- **P3(a)** — $\boxed{F(s) = \dfrac{s+2}{(s+2)^2+25},\; \Re\{s\}>-2}$ — $s$-domain shift $s\!\to\!s+2$.
- **P3(b)** — $\boxed{Y(s) = s/(s+3) = 1 - 3/(s+3)}$ — differentiation property; $y(t)=\delta(t)-3e^{-3t}u(t)$.
- **P3(c)** — $\boxed{h(t) = \tfrac{3}{5}(e^{-t}-e^{-6t})u(t)}$ — convolution property, PFE.
- **P3(d)** — $\boxed{x(0^+)=0,\; x(\infty)=1,\; x(t) = [1 + 2e^{-2t} - 3e^{-4t}]u(t)}$ — IVT/FVT + full PFE.
- **P4(a)** — $\boxed{H(s) = \dfrac{2}{(s+2)(s+4)}}$ — substitute $d/dt\!\to\!s$.
- **P4(b)** — **BIBO stable** (both poles in open LHP, causal).
- **P4(c)** — $\boxed{h(t) = (e^{-2t}-e^{-4t})u(t)}$ — PFE of $H$.
- **P4(d)** — $\boxed{y(t) = [\tfrac{2}{3}e^{-t} - e^{-2t} + \tfrac{1}{3}e^{-4t}]u(t)}$ — convolve with $e^{-t}u(t)$; three-pole PFE.
- **P4(e)** — Causal $G=3/(s-1)$: **unstable** ($j\omega$-axis not in ROC). Anti-causal: **stable**.
- **P5(a)** — $\boxed{y(t) = (e^{-t}+e^{-4t})u(t)}$ — unilateral transform, $y(0^-)=2$.
- **P5(b)** — $\boxed{y(t) = e^{-t}u(t)}$ — pole-zero cancellation suppresses $e^{-2t}$ mode; pure ZIR.
- **P5(c)** — $\boxed{y_{\text{ZS}} = (e^{-t}-e^{-4t})u(t),\; y_{\text{ZI}} = 2e^{-4t}u(t)}$ — ZSR/ZIR sum = P5(a).

---

### Problem 1 — Computing Laplace Transforms and ROCs (Lecture 16)

Compute $X(s)$ and ROC.

**(a)** $x_1(t) = 4\,e^{-2t}u(t)$

*Solution.* From the pair $e^{-at}u(t)\leftrightarrow 1/(s+a)$ with $a=2$, linearity gives
$$X_1(s) = \frac{4}{s+2}, \qquad \text{ROC: } \Re\{s\} > -2.$$

**(b)** $x_2(t) = -3\,e^{5t}u(-t)$

*Solution.* Using $-e^{-at}u(-t)\leftrightarrow 1/(s+a)$ with $a=-5$ and coefficient 3:
$$X_2(s) = \frac{3}{s-5}, \qquad \text{ROC: } \Re\{s\} < 5.$$

**(c)** $x_3(t) = 7\,\delta(t-3)$

*Solution.* Time-shift of $\delta$: $\delta(t-t_0)\leftrightarrow e^{-st_0}$. So
$$X_3(s) = 7\,e^{-3s}, \qquad \text{ROC: all } s.$$

**(d)** $x_4(t) = t\,e^{-4t}u(t)$

*Solution.* Pair $t\,e^{-at}u(t)\leftrightarrow 1/(s+a)^2$ with $a=4$:
$$X_4(s) = \frac{1}{(s+4)^2}, \qquad \text{ROC: } \Re\{s\} > -4.$$

**(e)** $x_5(t) = 2e^{-t}u(t) - 5e^{-3t}u(t)$, single rational form, poles and zeros.

*Solution.*
$$X_5(s) = \frac{2}{s+1} - \frac{5}{s+3} = \frac{2(s+3) - 5(s+1)}{(s+1)(s+3)} = \frac{-3s + 1}{(s+1)(s+3)}.$$
Poles: $s=-1, -3$. Zero: $s = 1/3$. ROC: $\Re\{s\}>-1$ (intersection of $\Re\{s\}>-1$ and $\Re\{s\}>-3$).

**(f)** $x_6(t) = e^{-2t}u(t) + 3e^{4t}u(-t)$; two-sided. Does the FT exist?

*Solution.* Rewrite $3e^{4t}u(-t) = -(-3)e^{-(-4)t}u(-t)$ so its Laplace pair gives $-3/(s-4)$ with ROC $\Re\{s\} < 4$. Together:
$$X_6(s) = \frac{1}{s+2} - \frac{3}{s-4}, \qquad \text{ROC: } -2 < \Re\{s\} < 4.$$
Since the ROC contains the $j\omega$-axis ($\Re\{s\}=0$), the Fourier transform of $x_6(t)$ exists.

### Problem 2 — Inverse Laplace via Partial Fractions (Lecture 17)

**(a) Distinct real poles.** $X(s) = \dfrac{3s+5}{(s+1)(s+4)}$, $\Re\{s\}>-1$.

*Solution.* Let $X = \dfrac{A}{s+1} + \dfrac{B}{s+4}$. Solve $3s+5 = A(s+4) + B(s+1)$:
- $s=-1$: $2 = 3A \Rightarrow A = 2/3$.
- $s=-4$: $-7 = -3B \Rightarrow B = 7/3$.

Both terms right-sided (ROC is right of both poles):
$$x(t) = \left(\tfrac{2}{3}e^{-t} + \tfrac{7}{3}e^{-4t}\right)u(t).$$

**(b) Distinct real poles, two-sided.** $X(s) = \dfrac{2s-4}{(s+2)(s-3)}$, $-2<\Re\{s\}<3$.

*Solution.* $A = \dfrac{2(-2)-4}{(-2-3)} = \dfrac{-8}{-5} = 8/5$; $B = \dfrac{2(3)-4}{(3+2)} = \dfrac{2}{5}$.
- Pole $s=-2$: ROC is to the **right** of it → right-sided term: $\tfrac{8}{5}e^{-2t}u(t)$.
- Pole $s=3$: ROC is to the **left** of it → left-sided term: $-\tfrac{2}{5}e^{3t}u(-t)$.

$$x(t) = \tfrac{8}{5}e^{-2t}u(t) - \tfrac{2}{5}e^{3t}u(-t).$$

**(c) Repeated poles.** $X(s) = \dfrac{6}{(s+2)^2(s+5)}$, $\Re\{s\}>-2$.

*Solution.* $X = \dfrac{A}{s+2} + \dfrac{B}{(s+2)^2} + \dfrac{C}{s+5}$.
- $C$: multiply by $(s+5)$, set $s=-5$: $C = 6/((-5+2)^2) = 6/9 = 2/3$.
- $B$: multiply by $(s+2)^2$, set $s=-2$: $B = 6/(-2+5) = 2$.
- $A$: cover-up / equating constants gives $A = -2/3$.

$$x(t) = \left(-\tfrac{2}{3}e^{-2t} + 2t\,e^{-2t} + \tfrac{2}{3}e^{-5t}\right)u(t).$$

**(d) Complex conjugate poles.** $X(s) = \dfrac{s+3}{s^2+6s+25}$, $\Re\{s\}>-3$.

*Solution.* Complete the square: $s^2+6s+25 = (s+3)^2+16 = (s+3)^2 + 4^2$. So
$$X(s) = \frac{s+3}{(s+3)^2+4^2}.$$
This matches $e^{-at}\cos(\omega_d t)u(t) \leftrightarrow (s+a)/((s+a)^2+\omega_d^2)$ with $a=3$, $\omega_d = 4$:
$$x(t) = e^{-3t}\cos(4t)\,u(t).$$
Damping rate $a=3$, oscillation frequency $\omega_d = 4$ rad/s.

### Problem 3 — Laplace Transform Properties (Lectures 16-17)

**(a) $s$-domain shift.** $\cos(5t)u(t)\leftrightarrow s/(s^2+25)$, ROC $\Re\{s\}>0$. Find the transform of $f(t) = e^{-2t}\cos(5t)u(t)$.

*Solution.* Shift $s\to s+2$:
$$F(s) = \frac{s+2}{(s+2)^2 + 25}, \qquad \text{ROC: }\Re\{s\}>-2.$$

**(b) Differentiation in time.** $X(s) = 1/(s+3)$. Find $Y(s)$ of $y(t)=dx/dt$ and verify.

*Solution.* $Y(s) = sX(s) = s/(s+3) = 1 - 3/(s+3)$. Inverse: $y(t) = \delta(t) - 3e^{-3t}u(t)$. Direct differentiation: $x(t) = e^{-3t}u(t)$ gives $dx/dt = -3e^{-3t}u(t) + \delta(t)$ ✓.

**(c) Convolution property.** $h_1 = e^{-t}u(t)$, $h_2 = 3e^{-6t}u(t)$.

*Solution.*
- $H_1(s) = 1/(s+1)$, $H_2(s) = 3/(s+6)$.
- $H(s) = 3/[(s+1)(s+6)]$.
- PFE: $\dfrac{3}{(s+1)(s+6)} = \dfrac{3/5}{s+1} - \dfrac{3/5}{s+6}$.
- $h(t) = \tfrac{3}{5}(e^{-t} - e^{-6t})u(t)$.

**(d) Initial and final value theorems.** $X(s) = \dfrac{8(s+1)}{s(s+2)(s+4)}$, $\Re\{s\}>0$.

*Solution.*
- Initial: $x(0^+) = \lim_{s\to\infty} sX(s) = \lim 8(s+1)/((s+2)(s+4)) = 0$.
- Final: $sX$ has poles at $s=-2,-4$ (both LHP), so FVT applies. $x(\infty) = \lim_{s\to 0} sX(s) = 8(1)/((2)(4)) = 1$.
- PFE: $X(s) = A/s + B/(s+2) + C/(s+4)$. $A = 8(1)/(2\cdot 4) = 1$; $B = 8(-1)/((-2)(2)) = 8/(-4) \cdot (-1) = 2$; actually $B = 8(-2+1)/((-2)(-2+4)) = 8(-1)/(-4) = 2$; $C = 8(-3)/((-4)(-2)) = -24/8 = -3$.
- $x(t) = (1 + 2e^{-2t} - 3e^{-4t})u(t)$. At $t=0^+$: $1+2-3 = 0$ ✓. At $t\to\infty$: $1$ ✓.

### Problem 4 — System Analysis with $H(s)$ (Lecture 18)

Causal LTI: $y'' + 6y' + 8y = 2x$.

**(a)** $H(s) = \dfrac{2}{s^2+6s+8} = \dfrac{2}{(s+2)(s+4)}$. Poles: $s=-2,-4$. No finite zeros.

**(b)** Poles strictly in LHP; causal → **BIBO stable**.

**(c)** PFE: $H(s) = \dfrac{1}{s+2} - \dfrac{1}{s+4}$. So $h(t) = (e^{-2t}-e^{-4t})u(t)$.

**(d)** Input $x(t)=e^{-t}u(t)$, $X(s)=1/(s+1)$.
- $Y(s) = \dfrac{2}{(s+1)(s+2)(s+4)}$.
- PFE: $\dfrac{A}{s+1}+\dfrac{B}{s+2}+\dfrac{C}{s+4}$ with $A = 2/((1)(3))=2/3$; $B = 2/((-1)(2)) = -1$; $C = 2/((-3)(-2)) = 1/3$.
- $y(t) = (\tfrac{2}{3}e^{-t} - e^{-2t} + \tfrac{1}{3}e^{-4t})u(t)$.
- $y(0^+) = 2/3 - 1 + 1/3 = 0$; $y(\infty) = 0$. IVT: $\lim_{s\to\infty} sY = 0$ ✓. FVT: $\lim_{s\to 0} sY = 0$ ✓.

**(e)** $G(s) = 3/(s-1)$. Pole at $s=1$ (RHP).
- Causal (ROC $\Re\{s\}>1$): $g(t) = 3e^{t}u(t)$, unbounded → **not stable**. $j\omega$-axis not in ROC.
- Anti-causal (ROC $\Re\{s\}<1$): $g(t) = -3e^{t}u(-t)$, bounded; ROC contains $j\omega$-axis → **stable**.

### Problem 5 — Unilateral Laplace (Lecture 18)

**(a)** $y' + 4y = 3e^{-t}u(t)$, $y(0^-) = 2$.

*Solution.*
- Transform: $sY(s) - y(0^-) + 4Y(s) = 3/(s+1)$ → $(s+4)Y(s) = 3/(s+1) + 2$.
- $Y(s) = \dfrac{3}{(s+1)(s+4)} + \dfrac{2}{s+4} = \dfrac{3 + 2(s+1)}{(s+1)(s+4)} = \dfrac{2s+5}{(s+1)(s+4)}$.
- PFE: $A/(s+1)+B/(s+4)$ with $A=(2(-1)+5)/((-1+4))=3/3=1$; $B=(2(-4)+5)/((-4+1))=(-3)/(-3)=1$.
- $y(t) = (e^{-t} + e^{-4t})u(t)$. Check $y(0) = 2$ ✓; $y(\infty)=0$ ✓.

**(b)** $y'' + 3y' + 2y = 0$, $y(0^-)=1$, $y'(0^-)=-1$.

*Solution.*
- Transform: $[s^2 Y - s(1) - (-1)] + 3[sY - 1] + 2Y = 0$ → $(s^2+3s+2)Y = s - 1 + 3 = s + 2$.
- $Y(s) = \dfrac{s+2}{(s+1)(s+2)} = \dfrac{1}{s+1}$.
- $y(t) = e^{-t}u(t)$.
- Response is **zero-input** (ZIR): input is zero, response driven entirely by ICs.

**(c) ZSR/ZIR decomposition for (a).**
- ZSR: ICs=0, same input. $(s+4)Y_{\text{ZS}} = 3/(s+1)$ → $Y_{\text{ZS}} = 3/((s+1)(s+4))$. PFE: $1/(s+1) - 1/(s+4)$. So $y_{\text{ZS}}(t) = (e^{-t} - e^{-4t})u(t)$.
- ZIR: input=0, $y(0^-)=2$. $(s+4)Y_{\text{ZI}} = 2$ → $Y_{\text{ZI}} = 2/(s+4)$, $y_{\text{ZI}}(t) = 2e^{-4t}u(t)$.
- Sum: $e^{-t} - e^{-4t} + 2e^{-4t} = e^{-t} + e^{-4t}$ ✓ (matches part (a)).

---

## HW Lectures 19-21 — z-Transform

**Source:** `hw_practice_problems/hw-lctr19-21.pdf` (extracted text `hw-lctr19-21.md`)
**Solutions available:** **Yes — full official solutions in [`homework/hw6/hw6_official_solutions.md`](../homework/hw6/hw6_official_solutions.md)** (transcribed from `hw-lctr19-21-solutions.pdf`); student-made alternative in [`homework/hw6/hw6_solutions.md`](../homework/hw6/hw6_solutions.md).

### Solutions Summary

Full official solutions: [`hw6_official_solutions.md`](../homework/hw6/hw6_official_solutions.md).

- **P1(a)** — $\boxed{X_1(z) = \dfrac{5}{1-0.7z^{-1}},\; |z|>0.7}$ — causal geometric pair.
- **P1(b)** — $\boxed{X_2(z) = \dfrac{1}{1-4z^{-1}},\; |z|<4}$ — anti-causal pair $-a^n u[-n-1]$.
- **P1(c)** — $\boxed{X_3(z) = 3 - 2z^{-1} + z^{-4},\; |z|>0}$ — finite-length polynomial.
- **P1(d)** — $\boxed{X_4(z) = \dfrac{0.5z^{-1}}{(1-0.5z^{-1})^2},\; |z|>0.5}$ — $n\,a^n u[n]$ pair.
- **P1(e)** — $\boxed{X_5(z) = \dfrac{6-3z^{-1}}{(1-0.3z^{-1})(1-0.9z^{-1})},\; |z|>0.9}$ — linearity + common denom.
- **P1(f)** — $\boxed{X_6(z) = \dfrac{1}{1-0.6z^{-1}} + \dfrac{3}{1-2z^{-1}},\; 0.6<|z|<2}$ — annular ROC contains unit circle; DTFT exists.
- **P1(g)** — $\boxed{X_7(z) = \dfrac{1-0.5657 z^{-1}}{1 - 1.1314 z^{-1} + 0.64 z^{-2}},\; |z|>0.8}$ — damped cosine pair, poles $0.8e^{\pm j\pi/4}$.
- **P2(a)** — $\boxed{x[n] = [-8(0.2)^n + 9(0.6)^n]u[n]}$ — PFE with distinct real poles, right-sided.
- **P2(b)** — $\boxed{x[n] = -0.8(0.5)^n u[n] - 4.8(3)^n u[-n-1]}$ — annular ROC: right/left split.
- **P2(c)** — $\boxed{x[n] = 2n(0.5)^n u[n]}$ — double-pole pair, rewrite factor 2.
- **P2(d)** — $\boxed{x[n] = (0.9)^n \cos(0.3\pi n)u[n]}$ — damped-cosine table lookup, $r=0.9$.
- **P3(a)** — $\boxed{Y(z) = \dfrac{z^{-2}}{1-0.8z^{-1}},\; |z|>0.8}$ — time shift by 2 adds $z^{-2}$.
- **P3(b)** — $\boxed{F(z) = \dfrac{1}{1-0.5z^{-1}},\; |z|>0.5}$ — z-domain scaling $z_0=0.5$.
- **P3(c)** — $\boxed{h[n] = [-\tfrac{3}{4}(0.3)^n + \tfrac{7}{4}(0.7)^n]u[n]}$ — convolution via $H_1 H_2$ + PFE.
- **P3(d)** — $\boxed{x[0]=3,\; x[n] = \tfrac{2}{9}(0.4)^n u[n] + \tfrac{25}{9}(-0.5)^n u[n]}$ — IVT + PFE.
- **P4(a)** — $\boxed{H(z) = \dfrac{1}{(1-0.3z^{-1})(1-0.6z^{-1})}}$ — factor $z^2-0.9z+0.18$; poles $0.3, 0.6$.
- **P4(b)** — **BIBO stable** (both poles inside unit circle).
- **P4(c)** — $\boxed{h[n] = [2(0.6)^n - (0.3)^n]u[n]}$ — PFE of $H$.
- **P4(d)** — $\boxed{y[n] = [12(0.6)^n + 1.5(0.3)^n - 12.5(0.5)^n]u[n]}$ — three-pole PFE from $Y=HX$.
- **P4(e)** — Causal $G=1/(1-1.5z^{-1})$: **unstable**, DTFT DNE. Anti-causal: **stable**, DTFT exists.
- **P5(a)** — $\boxed{y[n] = [-\tfrac{5}{3}(0.5)^n + \tfrac{76}{15}(0.8)^n]u[n]}$ — unilateral $y[-1]=3$; $y[0]=3.4$ ✓.
- **P5(b)** — $\boxed{y[n] = [\tfrac{18}{7}(0.6)^n - \tfrac{1}{14}(-0.1)^n]u[n]}$ — pure ZIR with poles $0.6, -0.1$.
- **P5(c)** — $\boxed{y_{\text{ZS}}[n] = [-\tfrac{5}{3}(0.5)^n + \tfrac{8}{3}(0.8)^n]u[n],\; y_{\text{ZI}}[n] = 2.4(0.8)^n u[n]}$ — sum matches P5(a).

---

### Problem 1 — Computing z-Transforms and ROCs (Lecture 19)

Compute $X(z)$ and ROC for each.

**(a)** $x_1[n] = 5(0.7)^n u[n]$.
$$X_1(z) = \frac{5}{1 - 0.7 z^{-1}}, \qquad |z|>0.7.$$

**(b)** $x_2[n] = -(4)^n u[-n-1]$.
$$X_2(z) = \frac{1}{1 - 4 z^{-1}}, \qquad |z|<4.$$

**(c)** $x_3[n] = 3\delta[n] - 2\delta[n-1] + \delta[n-4]$.
$$X_3(z) = 3 - 2z^{-1} + z^{-4}, \qquad |z|>0.$$

**(d)** $x_4[n] = n(0.5)^n u[n]$.
$$X_4(z) = \frac{0.5 z^{-1}}{(1 - 0.5 z^{-1})^2}, \qquad |z|>0.5.$$

**(e)** $x_5[n] = 2(0.3)^n u[n] + 4(0.9)^n u[n]$. Combine:
$$X_5(z) = \frac{6 - 3 z^{-1}}{(1 - 0.3 z^{-1})(1 - 0.9 z^{-1})}, \qquad |z|>0.9.$$
Poles $z=0.3, 0.9$. Zero at $z=0.5$ and a zero at $z=0$ from the $z^{-1}$.

**(f)** $x_6[n] = (0.6)^n u[n] - 3(2)^n u[-n-1]$.
- Term 1: $1/(1-0.6z^{-1})$, $|z|>0.6$.
- Term 2: $3/(1 - 2z^{-1})$, $|z|<2$.
$$X_6(z) = \frac{4 - 3.8 z^{-1}}{(1 - 0.6 z^{-1})(1 - 2 z^{-1})}, \qquad 0.6<|z|<2.$$
ROC contains unit circle ($0.6 < 1 < 2$), so the DTFT **exists**.

**(g)** $x_7[n] = (0.8)^n\cos(0.25\pi n)u[n]$. With $r=0.8$, $\omega_0 = 0.25\pi$, $r\cos\omega_0 = 0.8(\sqrt 2/2)\approx 0.5657$, $r^2=0.64$:
$$X_7(z) = \frac{1 - 0.5657\,z^{-1}}{1 - 1.1314\,z^{-1} + 0.64\,z^{-2}}, \qquad |z|>0.8.$$
Poles at $z = 0.8\,e^{\pm j\pi/4}$: radius $0.8$, angle $\pm 45^\circ$. DTFT exists (poles inside unit circle).

**(h)** Verify $X(1) = \sum x[n]$ for each: (a) $5/0.3 \approx 16.667$; (b) $1/(1-4) = -1/3$; (c) $3-2+1 = 2$; (d) $0.5/0.25 = 2$; (e) $3/0.07\approx 42.857$; (f) $0.2/(-0.4) = -0.5$; (g) $\approx 0.854$.

### Problem 2 — Inverse z-Transform via Partial Fractions (Lecture 20)

**(a)** $X(z) = \dfrac{1+3z^{-1}}{(1-0.2z^{-1})(1-0.6z^{-1})}$, $|z|>0.6$.

PF: $A/(1-0.2z^{-1}) + B/(1-0.6z^{-1})$; solve $1+3z^{-1} = A(1-0.6z^{-1}) + B(1-0.2z^{-1})$.
- $z^{-1}=1/0.2 = 5$: $1+15 = -2A$ → $A = -8$.
- $z^{-1}=1/0.6 = 5/3$: $1+5 = B(2/3)$ → $B = 9$.

$$x[n] = -8(0.2)^n u[n] + 9(0.6)^n u[n].$$
Both right-sided since ROC is outside both poles.

**(b)** $X(z) = \dfrac{4}{(1-0.5z^{-1})(1-3z^{-1})}$, $0.5<|z|<3$.

PF: $A = -4/5 = -0.8$, $B = 24/5 = 4.8$.
- Pole $z=0.5$: ROC outside → right-sided: $-0.8(0.5)^n u[n]$.
- Pole $z=3$: ROC inside → left-sided: $-4.8(3)^n u[-n-1]$.

$$x[n] = -0.8(0.5)^n u[n] - 4.8(3)^n u[-n-1].$$

**(c)** $X(z) = \dfrac{z^{-1}}{(1-0.5z^{-1})^2}$, $|z|>0.5$.

Recognize $n a^n u[n]\leftrightarrow a z^{-1}/(1-az^{-1})^2$ with $a=0.5$: the table pair gives $0.5 z^{-1}/(1-0.5z^{-1})^2$, so $X(z) = 2 \cdot [\text{pair}]$:
$$x[n] = 2 n (0.5)^n u[n].$$

**(d)** $X(z) = \dfrac{1 - 0.9\cos(0.3\pi)z^{-1}}{1 - 2(0.9)\cos(0.3\pi)z^{-1} + 0.81 z^{-2}}$, $|z|>0.9$.

Matches the damped-cosine pair $r^n\cos(\omega_0 n)u[n]$ with $r=0.9$ and $\omega_0 = 0.3\pi$:
$$x[n] = (0.9)^n \cos(0.3\pi n)u[n].$$
Pole locations: $z = 0.9 e^{\pm j 0.3\pi}$ (magnitude 0.9, angle $\pm 54^\circ$).

### Problem 3 — z-Transform Properties (Lectures 19-20)

**(a) Time shifting.** $y[n] = (0.8)^{n-2}u[n-2]$.
$$Y(z) = z^{-2}\cdot \frac{1}{1-0.8 z^{-1}} = \frac{z^{-2}}{1 - 0.8 z^{-1}}, \qquad |z|>0.8.$$
Two zeros at $z=0$ from the $z^{-2}$ factor; one pole at $z=0.8$.

**(b) z-domain scaling.** Given $u[n]\leftrightarrow 1/(1-z^{-1})$, $z_0 = 0.5$:
$$F(z) = X(z/z_0) = \frac{1}{1 - (z/0.5)^{-1}} = \frac{1}{1-0.5 z^{-1}}, \qquad |z|>0.5,$$
which matches the standard pair $a^n u[n]\leftrightarrow 1/(1-az^{-1})$.

**(c) Convolution.** $h_1[n]=(0.3)^n u[n]$, $h_2[n]=(0.7)^n u[n]$.
- $H_1(z)=1/(1-0.3z^{-1})$, $H_2(z)=1/(1-0.7z^{-1})$.
- $H(z) = 1/[(1-0.3z^{-1})(1-0.7z^{-1})]$, $|z|>0.7$.
- PFE: $A = -0.75$, $B = 1.75$. So $h[n] = -0.75(0.3)^n u[n] + 1.75(0.7)^n u[n]$.
- Verify: $h[0]=1$, $h[1] = -0.225 + 1.225 = 1.0$. Direct convolution matches.

**(d) Initial-value theorem.** $X(z) = (3 - z^{-1})/[(1-0.4z^{-1})(1+0.5z^{-1})]$.
- $x[0] = \lim_{z\to\infty} X(z) = 3/(1\cdot 1) = 3$.
- PFE: $A = 2/9$, $B = 25/9$. $x[n] = (2/9)(0.4)^n u[n] + (25/9)(-0.5)^n u[n]$.
- $x[0] = 2/9 + 25/9 = 3$ ✓.
- $x[1] = (2/9)(0.4) + (25/9)(-0.5) \approx -1.3$; $x[2] = (2/9)(0.16) + (25/9)(0.25) \approx 0.73$.

### Problem 4 — System Analysis with $H(z)$ (Lecture 21)

$y[n] - 0.9 y[n-1] + 0.18 y[n-2] = x[n]$.

**(a)** $H(z) = \dfrac{1}{1 - 0.9 z^{-1} + 0.18 z^{-2}} = \dfrac{1}{(1 - 0.3 z^{-1})(1 - 0.6 z^{-1})}$. Poles $z=0.3, 0.6$. No finite zeros.

**(b)** Both poles inside unit circle → causal system is **BIBO stable**.

**(c)** PFE: $A/(1-0.3z^{-1}) + B/(1-0.6z^{-1})$ with $A=-1$, $B=2$.
$$h[n] = [-\,(0.3)^n + 2(0.6)^n]\,u[n].$$

**(d)** Input $x[n] = (0.5)^n u[n]$, $X(z) = 1/(1-0.5z^{-1})$.
- $Y(z) = 1/[(1-0.3z^{-1})(1-0.6z^{-1})(1-0.5z^{-1})]$.
- PFE coefficients: $A = 1.5$, $B = 12$, $C = -12.5$.
- $y[n] = 1.5(0.3)^n u[n] + 12(0.6)^n u[n] - 12.5(0.5)^n u[n]$.
- Verify $y[0] = 1.5 + 12 - 12.5 = 1$ (direct: $y[0] = x[0] = 1$ ✓); $y[1] = 0.45 + 7.2 - 6.25 = 1.4$ (direct: $0.9(1) + 0.5 = 1.4$ ✓).

**(e)** $G(z) = 1/(1 - 1.5 z^{-1})$, pole $z=1.5$.
- Causal (ROC $|z|>1.5$): $g[n] = (1.5)^n u[n]$, grows → NOT stable. DTFT does not exist.
- Anti-causal (ROC $|z|<1.5$): $g[n] = -(1.5)^n u[-n-1]$. ROC includes unit circle → stable. DTFT exists.

### Problem 5 — Unilateral z-Transform (Lecture 21)

**(a)** $y[n] - 0.8 y[n-1] = (0.5)^n u[n]$, $y[-1]=3$.

*Solution.*
- Transform using $y[n-1]\leftrightarrow z^{-1}Y + y[-1]$:
  $$Y - 0.8(z^{-1}Y + 3) = 1/(1 - 0.5 z^{-1}) \Rightarrow (1 - 0.8 z^{-1})Y = \dfrac{1}{1-0.5z^{-1}} + 2.4.$$
- $Y(z) = \dfrac{3.4 - 1.2 z^{-1}}{(1-0.5z^{-1})(1-0.8z^{-1})}$.
- PFE: $A = -5/3$, $B = 76/15$.
- $y[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{76}{15}(0.8)^n u[n]$.
- Check $y[0] = -5/3 + 76/15 = 51/15 = 3.4$; from DE: $y[0] = 0.8(3) + 1 = 3.4$ ✓.
- $y[1] = -5/6 + (76/15)(0.8) \approx 3.22$; from DE: $0.8(3.4) + 0.5 = 3.22$ ✓.

**(b)** $y[n] - 0.5 y[n-1] - 0.06 y[n-2] = 0$, $y[-1]=5$, $y[-2]=0$.

*Solution.*
- $y[n-1]\leftrightarrow z^{-1}Y + 5$; $y[n-2]\leftrightarrow z^{-2}Y + 0 + 5 z^{-1}$.
- $(1 - 0.5 z^{-1} - 0.06 z^{-2})Y = 2.5 + 0.3 z^{-1}$.
- Factor denominator: $(1-0.6z^{-1})(1+0.1z^{-1})$.
- PFE: $A = 18/7$, $B = -1/14$.
- $y[n] = \tfrac{18}{7}(0.6)^n u[n] - \tfrac{1}{14}(-0.1)^n u[n]$.
- This is **zero-input response** (ZIR): input is zero; response comes entirely from ICs.

**(c) ZSR/ZIR decomposition for (a).**
- $Y_{\text{ZS}} = 1/[(1-0.5z^{-1})(1-0.8z^{-1})]$, PF: $A=-5/3$, $B=8/3$.
  $$y_{\text{ZS}}[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{8}{3}(0.8)^n u[n].$$
- $Y_{\text{ZI}} = 2.4/(1-0.8z^{-1})$, $y_{\text{ZI}}[n] = 2.4(0.8)^n u[n]$.
- Sum: $-\tfrac{5}{3}(0.5)^n u[n] + (\tfrac{8}{3}+\tfrac{12}{5})(0.8)^n u[n] = -\tfrac{5}{3}(0.5)^n u[n] + \tfrac{76}{15}(0.8)^n u[n]$ ✓.

---

## Lecture 22 Exercise — Sampling

**Source:** `hw_practice_problems/lctr22-exercise.pdf` (extracted text `lctr22-exercise.md`)
**Solutions available:** **Yes — full official solutions in [`hw_practice_problems/lctr22-exercise-solutions.md`](../hw_practice_problems/lctr22-exercise-solutions.md)** (transcribed from `lctr22-exercise-solutions.pdf`).

### Solutions Summary

Full solutions with reasoning: [`lctr22-exercise-solutions.md`](../hw_practice_problems/lctr22-exercise-solutions.md).

- **P1** — $\boxed{\text{Nyquist rate} = 10{,}000\pi \text{ rad/s} = 5\text{ kHz};\; T_{\max}<0.2\text{ ms}}$ — $\omega_s > 2\omega_M$.
- **P2** — $\boxed{\text{False}}$ — strict inequality $\omega_s>2\omega_M$ required (sine sampled at $2\omega_M$ hits zeros).
- **P3** — Time-domain multiplication by impulse train ↔ frequency-domain convolution with impulse train → replicas.
- **P4** — $\boxed{\text{No}}$ — overlapped spectra add irreversibly; aliasing cannot be undone.
- **P5** — Anti-aliasing filter: analog LPF with cutoff $\le\omega_s/2$ placed **before** the sampler.
- **P6** — $\boxed{\text{Nyquist rate} = 3600\pi \text{ rad/s} = 1800\text{ Hz}}$ — $\omega_M = 1800\pi$.
- **P7** — $\boxed{\omega_s = 10{,}000\pi > 2\omega_M = 6000\pi;\; \text{no aliasing}}$.
- **P8** — $\boxed{f_{\text{alias}} = |1000-900| = 100\text{ Hz}}$ — fold-down via $f_s/2 = 500<900$.
- **P9** — $\boxed{f_{\text{alias}} = |1500-900| = 600\text{ Hz}}$ — still aliases at $f_s=1500$.
- **P10** — $\boxed{x(t-5)\!:\omega_0;\quad x(2t)\!:2\omega_0}$ — shift preserves spectrum magnitude; compression stretches it.
- **P11** — Each replica is scaled by $1/T$ from the sampling operation; reconstruction filter multiplies by $T$ to undo this.
- **P12** — ZOH is **not exact**: $H_0(j\omega) = e^{-j\omega T/2}\cdot 2\sin(\omega T/2)/\omega$ — sinc-droop in passband + residual images.
- **P13** — $\boxed{\text{Blade appears to rotate slowly backward at 1 rev/s}}$ — alias $= f_s-f_0 = 24-25 = -1$ Hz.
- **P14** — $\boxed{\text{Not satisfied};\; f_s>10\text{ kHz required}}$ — $f_s=8$ kHz $<2f_M=10$ kHz.
- **P15** — $\boxed{\text{Yes, with anti-aliasing LPF}}$ — trade high-frequency loss for aliasing-free passband.

---

### Problem 1
A signal $x(t)$ has $X(j\omega)=0$ for $|\omega|>5000\pi$. Nyquist rate? Max sampling period $T$?

**Answer.** $\omega_M = 5000\pi$ → Nyquist rate $\omega_s = 2\omega_M = 10000\pi$ rad/s (i.e. $f_s = 5000$ Hz). Max $T = 2\pi/\omega_s = 1/5000 = 0.2$ ms.

### Problem 2
True or false: if $\omega_s = 2\omega_M$, the sampling theorem guarantees perfect reconstruction.

**Answer.** False in general — the theorem requires $\omega_s > 2\omega_M$ **strictly**, or if $\omega_s = 2\omega_M$ the spectrum must have no content exactly at $\omega_M$. (The strict inequality avoids replicas touching at $\omega_M$.)

### Problem 3
Explain in one sentence why time-domain sampling produces spectral copies.

**Answer.** Multiplying $x(t)$ by an impulse train in time corresponds to convolving $X(j\omega)$ with a frequency-domain impulse train, producing periodic replicas of $X$ at multiples of $\omega_s$.

### Problem 4
Can overlapping replicas be undone with a clever filter? Why or why not?

**Answer.** No. Once replicas overlap the spectra add linearly, and a linear filter cannot separate sums of spectral content occupying the same frequency bins — aliasing is irreversible.

### Problem 5
What is an anti-aliasing filter and where does it go?

**Answer.** An analog low-pass filter placed **before** the sampler that band-limits $x(t)$ to $|\omega|<\omega_s/2$ to prevent replicas from overlapping.

### Problem 6
Nyquist rate for $x(t) = \cos(600\pi t) + \cos(1800\pi t)$.

**Answer.** Max frequency component $\omega_M = 1800\pi$. Nyquist rate $= 2\omega_M = 3600\pi$ rad/s = $1800$ Hz.

### Problem 7
$\omega_M = 3000\pi$, $T = 2\times 10^{-4}$ s. Compute $\omega_s$; aliasing?

**Answer.** $\omega_s = 2\pi/T = 2\pi/(2\times 10^{-4}) = 10000\pi$ rad/s. Need $\omega_s > 2\omega_M = 6000\pi$. $10000\pi > 6000\pi$ ✓, **no aliasing**.

### Problem 8
Sample $\cos(2\pi\cdot 900\,t)$ at $f_s = 1000$ Hz. Reconstructed frequency?

**Answer.** $f_s = 1000 < 2\cdot 900 = 1800$, so aliasing occurs. Alias frequency: $|900 - 1000| = 100$ Hz.

### Problem 9
Repeat with $f_s = 1500$ Hz.

**Answer.** $1500 < 1800$; alias $= |900 - 1500| = 600$ Hz.

### Problem 10
$x(t)$ has Nyquist rate $\omega_0$. Rates of $x(t-5)$ and $x(2t)$?

**Answer.** $x(t-5)$ has the same spectrum magnitude (phase shift only) → same Nyquist rate $\omega_0$. $x(2t)$ has spectrum $\tfrac{1}{2}X(j\omega/2)$ — bandwidth **doubles**, so Nyquist rate doubles to $2\omega_0$.

### Problem 11
Why the factor $T$ in the ideal reconstruction filter's passband?

**Answer.** The impulse-train sampling scales each replica by $1/T$; the reconstruction filter compensates by multiplying by $T$ to recover the original amplitude.

### Problem 12
ZOH reconstruction: exact? What kind of error?

**Answer.** Not exact. The ZOH has frequency response $\mathrm{sinc}(\omega T/2)$ plus a linear phase delay — it introduces a sinc-droop in the passband and spectral images at multiples of $f_s$ that must be removed with a second anti-imaging filter.

### Problem 13
Movie camera 24 fps, blade 25 rev/s — qualitative description?

**Answer.** The sampling frequency is below twice the blade rate, so the blade aliases. Since blade rate (25) is just above frame rate (24), the apparent rotation is $25-24 = 1$ rev/s (very slow) and because blades are typically symmetric and the alias is positive, the blade appears to **rotate slowly forward**.

### Problem 14
$|\omega|>10000\pi$ bandwidth, $f_s = 8000$ Hz. Sampling theorem satisfied? Min $f_s$?

**Answer.** $\omega_s = 16000\pi < 20000\pi$, so violated — aliasing. Need $\omega_s > 20000\pi$ → $f_s > 10000$ Hz. Minimum $f_s > 10$ kHz (strictly).

### Problem 15
Non-band-limited signals: can we sample in practice?

**Answer.** Yes — in real systems an analog anti-aliasing (low-pass) filter band-limits the signal before the ADC, trading some aliasing-free bandwidth against acceptable distortion of the original.

---

## Lecture 23 Exercise — Feedback Systems

**Source:** `hw_practice_problems/lctr23-exercise.pdf` (extracted text `lctr23-exercise.md`)
**Solutions available:** **Yes — full official solutions in [`hw_practice_problems/lctr23-exercise-solutions.md`](../hw_practice_problems/lctr23-exercise-solutions.md)** (transcribed from `lctr23-exercise-solutions.pdf`).

### Solutions Summary

Full solutions with block-diagram algebra: [`lctr23-exercise-solutions.md`](../hw_practice_problems/lctr23-exercise-solutions.md).

- **P1** — $\boxed{Q(s) = \dfrac{2}{(s+2)(s+3)}}$ — cascade $\times$ unity feedback; stable (poles $-2, -3$).
- **P2** — $\boxed{Q(s) = \dfrac{4s+17}{s^2+23s+78}}$ — parallel sum then feedback $G=4$; stable (roots $\approx-4.14, -18.87$).
- **P3** — $\boxed{Q(s) = \dfrac{1}{s+4}}$ — collapse inner loop to $1/(s+3)$ then outer unity feedback.
- **P4(a)** — $\boxed{Q(s) = \dfrac{K}{s+5+K},\; s_{\text{cl}} = -(5+K)}$; **(b)** $\boxed{K>-5}$; **(c)** $\boxed{K=5}$ gives pole at $-10$.
- **P5(a)** — Characteristic equation $\boxed{s^2 + 3s + (2+K) = 0}$; **(b)** $\boxed{K>-2}$ (Routh: all coeffs positive).
- **P6(a)** — DT closed-loop pole $\boxed{z_{\text{cl}} = 0.8-K}$; **(b)** stable range $\boxed{0<K<1.8}$ for $|z|<1$.
- **P7(a)** — $\boxed{\text{PM} = 30^\circ}$ at $\omega_{gc}=5$; **(b)** $\boxed{\text{GM}=8\text{ dB}}$ at $\omega_{pc}=20$; **(c)** both positive → **stable**; **(d)** $\boxed{\tau_{\max} = \text{PM(rad)}/\omega_{gc} \approx 0.105\text{ s}}$.
- **P8** — $\boxed{\text{FALSE}}$ — negative feedback with high loop gain can destabilize (audio squeal example).
- **P9** — $\boxed{\text{TRUE}}$ — positive PM $=60^\circ$ with positive GM ⇒ stable (well-damped design target).
- **P10** — $\boxed{\text{TRUE}}$ — Nyquist plot is locus of $GH(j\omega)$ in the complex plane; encirclements of $-1$ diagnose instability.

---

### Problem 1 — Cascade + Unity Feedback

Cascade of $\frac{2}{s+1}$ and $\frac{1}{s+4}$ with unity negative feedback.

*Solution.* Forward gain $G = \dfrac{2}{(s+1)(s+4)}$. Unity feedback: $Q(s) = \dfrac{G}{1+G} = \dfrac{2/[(s+1)(s+4)]}{1 + 2/[(s+1)(s+4)]} = \dfrac{2}{(s+1)(s+4) + 2} = \dfrac{2}{s^2 + 5s + 6} = \dfrac{2}{(s+2)(s+3)}$.

### Problem 2 — Parallel + Feedback Gain 4

Parallel paths $\frac{3}{s+2}$ and $\frac{1}{s+5}$, feedback gain $H=4$.

*Solution.* Parallel sum: $G(s) = \dfrac{3}{s+2} + \dfrac{1}{s+5} = \dfrac{3(s+5)+(s+2)}{(s+2)(s+5)} = \dfrac{4s+17}{(s+2)(s+5)}$.

Closed loop: $Q = \dfrac{G}{1+4G} = \dfrac{(4s+17)/[(s+2)(s+5)]}{1 + 4(4s+17)/[(s+2)(s+5)]} = \dfrac{4s+17}{(s+2)(s+5) + 4(4s+17)} = \dfrac{4s+17}{s^2 + 7s + 10 + 16 s + 68} = \dfrac{4s + 17}{s^2 + 23 s + 78}$.

### Problem 3 — Nested Loops

Forward block $1/s$; inner feedback gain 3; outer unity feedback.

*Solution.* Inner loop: $Q_{\text{inner}} = \dfrac{1/s}{1 + 3/s} = \dfrac{1}{s+3}$. Outer unity feedback:
$$Q(s) = \dfrac{Q_{\text{inner}}}{1 + Q_{\text{inner}}} = \dfrac{1/(s+3)}{1 + 1/(s+3)} = \dfrac{1}{s+4}.$$

### Problem 4 — Unity Feedback $H(s) = K/(s+5)$

**(a)** Closed-loop: $Q(s) = \dfrac{K/(s+5)}{1 + K/(s+5)} = \dfrac{K}{s+5+K}$. Pole at $s = -(5+K)$.

**(b)** Stable when $5 + K > 0$, i.e. $K > -5$.

**(c)** Pole at $s=-10$ requires $5+K = 10$ → $K = 5$.

### Problem 5 — $H(s) = K/[(s+1)(s+2)]$

**(a)** Characteristic equation: $(s+1)(s+2) + K = 0 \Rightarrow s^2 + 3s + 2 + K = 0$.

**(b)** By Routh-Hurwitz (or inspection of a quadratic with positive $a_2$): stable iff all coefficients positive, i.e. $2 + K > 0$ → $K > -2$.

### Problem 6 — DT: $H(z) = K z^{-1}/(1 - 0.8 z^{-1})$

**(a)** Unity feedback. Closed loop denominator: $1 + H(z) = 1 + \dfrac{K z^{-1}}{1 - 0.8 z^{-1}} = \dfrac{(1-0.8 z^{-1}) + K z^{-1}}{1-0.8 z^{-1}} = \dfrac{1 + (K - 0.8) z^{-1}}{1 - 0.8 z^{-1}}$.

Closed-loop system has pole where $1 + (K-0.8)z^{-1} = 0$, i.e. $z = -(K-0.8) = 0.8 - K$.

**(b)** For $K>0$, stability ($|z|<1$) requires $|0.8 - K| < 1$ → $-0.2 < K < 1.8$. Combined with $K>0$: $0 < K < 1.8$.

### Problem 7 — Bode Plot Margins

Readings: at $\omega_2 = 5$ (0 dB gain crossover), $\angle GH = -150^\circ$. At $\omega_1 = 20$ ($-180^\circ$ phase crossover), $|GH| = -8$ dB.

**(a) Phase margin** = $180^\circ + \angle GH(\omega_2) = 180 - 150 = 30^\circ$.

**(b) Gain margin** = $0 - (-8) = 8$ dB.

**(c) Stable?** Both margins positive → yes, closed-loop stable (assuming open-loop stable).

**(d) Max added delay.** $\Delta\phi_{\max} = \text{PM} = 30^\circ = 30\pi/180 = \pi/6$ rad. Additional delay $\tau_d$ causes extra phase $-\omega_2 \tau_d$ at the 0-dB crossover. Set $|\omega_2 \tau_d| = \pi/6$: $\tau_d = \pi/(6\cdot 5) = \pi/30 \approx 0.105$ s.

### Problem 8 — True/False: Negative feedback always stabilizes.

**False.** Negative feedback can destabilize if excess phase or gain at the 0-dB crossover makes the closed loop meet the $GH = -1$ condition. E.g., three stacked first-order lags with high loop gain.

### Problem 9 — True/False: PM $= 60^\circ$ implies stability.

**True** for open-loop stable systems. A positive phase margin with positive gain margin indicates closed-loop stability (standard Nyquist criterion for minimum-phase open-loop systems). 60° is a typical design target for good transient response.

### Problem 10 — True/False: Nyquist plot is $G(j\omega)H(j\omega)$ in complex plane.

**True.** The Nyquist plot is the locus of the complex number $G(j\omega)H(j\omega)$ as $\omega$ sweeps from $-\infty$ to $\infty$. Encirclements of $-1$ (times $-1$) count closed-loop RHP poles.

---

*End of master document.*
