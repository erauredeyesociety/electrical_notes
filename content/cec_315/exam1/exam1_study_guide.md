# CEC 315 — Exam 1 Study Guide (Lectures 2–8)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Jianhua Liu / Rogelio Gracia Otalvaro
**Coverage:** Chapters 1–2 of Oppenheim & Willsky (Lectures 2–8)
**Exam topics:** Signal definitions & transformations, complex numbers / Euler / phasors, fundamental functions (impulse, step, ramp), basic system properties, DT LTI convolution, CT LTI convolution, difference / differential equations, singularity functions.

---

## Table of Contents

1. [Topic Overview by Lecture](#1-topic-overview-by-lecture)
2. [Key Equations Reference](#2-key-equations-reference)
3. [Signal Transformations and Classification](#3-signal-transformations-and-classification)
4. [Complex Exponentials and Euler](#4-complex-exponentials-and-euler)
5. [Fundamental Functions](#5-fundamental-functions)
6. [System Properties Checklist](#6-system-properties-checklist)
7. [LTI Convolution (DT and CT)](#7-lti-convolution-dt-and-ct)
8. [First-Order Equations and Impulse Responses](#8-first-order-equations-and-impulse-responses)
9. [Singularity Functions](#9-singularity-functions)
10. [What to Memorize](#10-what-to-memorize)
11. [Common Pitfalls](#11-common-pitfalls)

---

## 1. Topic Overview by Lecture

### Lecture 2 — Signal Definitions and Transformations (§1.1–1.2)
- CT vs. DT signals: notation $x(t)$ vs. $x[n]$; sampling relation $x[n] = x(nT_s)$.
- Signal energy $E_\infty$ and power $P_\infty$ (see §3 below); classification into finite-energy, finite-power, or neither.
- Transformations of the independent variable: time shift $x(t-t_0)$, reversal $x(-t)$, scaling $x(at)$.
- Order for $x(at-b)$: rewrite as $x\!\left(a(t-b/a)\right)$; shift first by $b/a$, then scale by $a$.
- Periodicity: CT $x(t)=x(t+T)$ (fundamental period $T_0$); DT $x[n]=x[n+N]$ (fundamental period $N_0$).
- Even/odd decomposition: $x_e(t)=\tfrac12[x(t)+x(-t)]$, $x_o(t)=\tfrac12[x(t)-x(-t)]$.

### Lecture 3 — Complex Numbers, Exponentials, Sinusoids (§1.3)
- Rectangular $c=a+jb$ and polar $c=re^{j\theta}=r\angle\theta$; $r=\sqrt{a^2+b^2}$, $\theta=\mathrm{atan2}(b,a)$.
- Euler's formula: $e^{j\phi}=\cos\phi+j\sin\phi$; inverse Euler:
  $\cos\phi=\tfrac12(e^{j\phi}+e^{-j\phi})$, $\sin\phi=\tfrac{1}{2j}(e^{j\phi}-e^{-j\phi})$.
- Polar products: multiplication $\to$ magnitudes multiply, angles add; division $\to$ magnitudes divide, angles subtract.
- CT complex sinusoid $x_C(t)=Ae^{j(\omega_0 t+\theta)}$; real sinusoid $x(t)=A\cos(\omega_0 t+\theta)$; $T_0=2\pi/|\omega_0|$.
- Real exponentials $Ce^{at}$: grow for $a>0$, decay for $a<0$.
- DT sinusoid quirks: $e^{j(\omega_0+2\pi)n}=e^{j\omega_0 n}$; $e^{j\omega_0 n}$ periodic only if $\omega_0/(2\pi)$ is rational.
- Special values: $1=e^{j0}$, $j=e^{j\pi/2}$, $-1=e^{j\pi}$, $-j=e^{-j\pi/2}$.

### Lecture 4 — Key Functions and System Basics (§1.4–1.5)
- DT unit impulse $\delta[n]=1$ if $n=0$, else $0$; DT unit step $u[n]=1$ if $n\ge 0$, else $0$.
- Relations: $\delta[n]=u[n]-u[n-1]$ and $u[n]=\sum_{m=-\infty}^{n}\delta[m]$.
- CT Dirac delta $\delta(t)$: zero for $t\ne 0$, $\int\delta\,dt=1$; $\delta(t)=du/dt$; $u(t)=\int_{-\infty}^t\delta(\tau)d\tau$.
- Impulse decompositions:
  $x[n]=\sum_k x[k]\delta[n-k]$ and $x(t)=\int x(\tau)\delta(t-\tau)d\tau$.
- Impulse multiplication ("sampling"): $x[n]\delta[n-k]=x[k]\delta[n-k]$ and $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$.
- System notation, impulse response $h$, interconnections: series (cascade), parallel, feedback.

### Lecture 5 — Basic System Properties (§1.6)
- **Memoryless:** $y$ at time $t$ depends only on $x$ at time $t$. E.g., $y(t)=5x(t)$, ReLU $y[n]=\max(x[n],0)$.
- **Invertible:** distinct inputs give distinct outputs; inverse system $T_2$ with $T_2\circ T_1=$ identity.
- **Causal:** no dependence on future input. LTI test: $h(t)=0$ for $t<0$ (or $h[n]=0$ for $n<0$).
- **BIBO stable:** bounded input $\Rightarrow$ bounded output. LTI test: $\int|h|\,dt<\infty$ or $\sum|h[n]|<\infty$.
- **Time-invariant:** input shift $\to$ identical output shift. Red flag: explicit $t$ or $n$ coefficient (e.g., $y(t)=tx(t)$).
- **Linear:** superposition (additivity + homogeneity). Zero-in/zero-out is a necessary check.

### Lecture 6 — DT LTI Convolution Sum (§2.1)
- Derivation: decompose $x[n]=\sum_k x[k]\delta[n-k]$, apply linearity then time-invariance $\Rightarrow$
  $y[n]=\sum_{k=-\infty}^{\infty}x[k]\,h[n-k]=x[n]*h[n]$.
- Flip-and-slide: flip $h[k]\to h[-k]$, shift by $n$, multiply by $x[k]$, sum.
- Length: if $x$ has $N$ samples and $h$ has $M$, output has $N+M-1$ samples.
- Properties: commutative, associative (cascade $\Rightarrow h_1*h_2$), distributive (parallel $\Rightarrow h_1+h_2$), identity $x*\delta=x$, shift $x*\delta[n-n_0]=x[n-n_0]$.
- Sanity check: $\sum_n y[n]=(\sum_n x[n])(\sum_n h[n])$.

### Lecture 7 — CT LTI Convolution Integral (§2.2–2.3)
- Sifting: $\int x(\tau)\delta(\tau-t_0)\,d\tau=x(t_0)$ (delta must lie inside the limits!).
- Convolution integral: $y(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)d\tau=x(t)*h(t)$.
- Graphical procedure: sketch $x(\tau)$, flip-shift $h(t-\tau)$, identify overlap, integrate piecewise.
- LTI properties from $h$:
  - Memoryless $\iff h(t)=K\delta(t)$.
  - Causal $\iff h(t)=0$ for $t<0$.
  - BIBO stable $\iff \int|h(t)|\,dt<\infty$.
  - Invertible $\iff$ exists $h_i$ with $h*h_i=\delta$.
- Step response $s(t)=\int_{-\infty}^{t}h(\tau)\,d\tau$; $h(t)=ds/dt$.

### Lecture 8 — Differential / Difference Equations and Singularity Functions (§2.4–2.5)
- CT first order: $\dfrac{dy}{dt}+ay=bx$. Impulse response (initial rest, causal): $h(t)=be^{-at}u(t)$. Stable iff $a>0$.
- DT first order: $y[n]=\alpha y[n-1]+bx[n]$. Impulse response: $h[n]=b\alpha^n u[n]$. Stable iff $|\alpha|<1$.
- Solution method: homogeneous + particular, or iterate from initial rest; jump condition at $t=0$ from impulse.
- Singularity chain: $r(t)=tu(t)\xrightarrow{d/dt}u(t)\xrightarrow{d/dt}\delta(t)\xrightarrow{d/dt}\delta'(t)$; integrals reverse arrows.
- Impulse scaling: $\delta(at)=\delta(t)/|a|$. Impulse multiplication: $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$.
- Doublet: $x(t)*\delta'(t)=dx/dt$.

---

## 2. Key Equations Reference

### 2.1 Signal Energy and Power

| Quantity | CT | DT |
|---|---|---|
| Instantaneous energy | $\lvert x(t)\rvert^2$ | $\lvert x[n]\rvert^2$ |
| Total energy $E_\infty$ | $\displaystyle\int_{-\infty}^{\infty}\lvert x(t)\rvert^2\,dt$ | $\displaystyle\sum_{n=-\infty}^{\infty}\lvert x[n]\rvert^2$ |
| Average power $P_\infty$ | $\displaystyle\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}\lvert x(t)\rvert^2dt$ | $\displaystyle\lim_{N\to\infty}\frac{1}{2N+1}\sum_{n=-N}^{N}\lvert x[n]\rvert^2$ |

Classification: **finite energy** ($E_\infty<\infty$, $P_\infty=0$); **finite power** ($P_\infty$ finite, $E_\infty=\infty$, e.g., sinusoids); neither.

### 2.2 Signal Transformations

| Operation | CT | DT |
|---|---|---|
| Time shift | $x(t-t_0)$ (delay if $t_0>0$) | $x[n-n_0]$ |
| Time reversal | $x(-t)$ | $x[-n]$ |
| Time scaling | $x(at)$ (compress if $|a|>1$) | — (limited to integer) |
| Combined | $x(at-b)=x(a(t-b/a))$: shift by $b/a$ first, then scale | — |
| Even part | $x_e(t)=\tfrac12[x(t)+x(-t)]$ | $x_e[n]=\tfrac12[x[n]+x[-n]]$ |
| Odd part | $x_o(t)=\tfrac12[x(t)-x(-t)]$ | $x_o[n]=\tfrac12[x[n]-x[-n]]$ |

### 2.3 Complex Exponentials and Euler

| Identity | Formula |
|---|---|
| Euler | $e^{j\phi}=\cos\phi+j\sin\phi$ |
| Inverse Euler (cos) | $\cos\phi=\tfrac12(e^{j\phi}+e^{-j\phi})$ |
| Inverse Euler (sin) | $\sin\phi=\tfrac{1}{2j}(e^{j\phi}-e^{-j\phi})$ |
| Polar / rect | $re^{j\theta}=r\cos\theta+jr\sin\theta$ |
| Magnitude | $r=\sqrt{a^2+b^2}$ |
| Angle | $\theta=\mathrm{atan2}(b,a)$ |
| Conjugate | $(re^{j\theta})^*=re^{-j\theta}$ |
| Multiplication | $r_1e^{j\theta_1}\cdot r_2e^{j\theta_2}=r_1r_2 e^{j(\theta_1+\theta_2)}$ |
| Division | $\dfrac{r_1 e^{j\theta_1}}{r_2 e^{j\theta_2}}=\dfrac{r_1}{r_2}e^{j(\theta_1-\theta_2)}$ |
| CT complex sinusoid | $x_C(t)=Ae^{j(\omega_0 t+\theta)}$ |
| CT real sinusoid | $x(t)=A\cos(\omega_0 t+\theta)$ |
| Fundamental period | $T_0=2\pi/|\omega_0|$ (CT) |
| Complex amplitude (phasor) | $X_C=Ae^{j\theta}$ |

### 2.4 Fundamental Functions

| Function | CT | DT |
|---|---|---|
| Unit impulse | $\delta(t)$: $\int\delta(t)dt=1$ | $\delta[n]=1$ if $n=0$, else $0$ |
| Unit step | $u(t)=1$ for $t>0$, $0$ for $t<0$ | $u[n]=1$ for $n\ge0$, else $0$ |
| Ramp | $r(t)=tu(t)$ | $r[n]=nu[n]$ |
| $\delta$–$u$ relation | $\delta(t)=du/dt$; $u(t)=\int_{-\infty}^t\delta(\tau)d\tau$ | $\delta[n]=u[n]-u[n-1]$; $u[n]=\sum_{m\le n}\delta[m]$ |
| Sifting | $\int x(\tau)\delta(\tau-t_0)d\tau=x(t_0)$ | $\sum_k x[k]\delta[k-n_0]=x[n_0]$ |
| Sampling mul. | $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$ | $x[n]\delta[n-k]=x[k]\delta[n-k]$ |
| Impulse scaling | $\delta(at)=\delta(t)/|a|$ | — |
| Doublet | $\delta'(t)=d\delta/dt$; $x(t)*\delta'(t)=dx/dt$ | — |

### 2.5 LTI Systems and Convolution

| Concept | CT | DT |
|---|---|---|
| Signal decomposition | $x(t)=\int x(\tau)\delta(t-\tau)d\tau$ | $x[n]=\sum_k x[k]\delta[n-k]$ |
| Impulse response | $h(t)=T\{\delta(t)\}$ | $h[n]=T\{\delta[n]\}$ |
| Convolution | $y(t)=\int x(\tau)h(t-\tau)d\tau$ | $y[n]=\sum_k x[k]h[n-k]$ |
| Identity | $x*\delta=x$ | $x*\delta=x$ |
| Delay | $x(t)*\delta(t-t_0)=x(t-t_0)$ | $x[n]*\delta[n-n_0]=x[n-n_0]$ |
| Commutativity | $x*h=h*x$ | $x*h=h*x$ |
| Associativity | $(x*h_1)*h_2=x*(h_1*h_2)$ | same |
| Distributivity | $x*(h_1+h_2)=x*h_1+x*h_2$ | same |
| Output length (finite) | — | $N+M-1$ samples |
| Step response | $s(t)=\int_{-\infty}^t h(\tau)d\tau$; $h=ds/dt$ | $s[n]=\sum_{k\le n}h[k]$; $h[n]=s[n]-s[n-1]$ |
| Memoryless | $h(t)=K\delta(t)$ | $h[n]=K\delta[n]$ |
| Causal | $h(t)=0$ for $t<0$ | $h[n]=0$ for $n<0$ |
| BIBO stable | $\int|h|dt<\infty$ | $\sum|h[n]|<\infty$ |

### 2.6 First-Order Equations

| Quantity | CT | DT |
|---|---|---|
| Standard form | $\dfrac{dy}{dt}+ay=bx$ | $y[n]=\alpha y[n-1]+bx[n]$ |
| Impulse response | $h(t)=be^{-at}u(t)$ | $h[n]=b\alpha^n u[n]$ |
| Stability | $a>0$ | $|\alpha|<1$ |
| Step response | $s(t)=\dfrac{b}{a}(1-e^{-at})u(t)$ | $s[n]=b\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$ |

---

## 3. Signal Transformations and Classification

### 3.1 Order of Transformations

For $x(at-b)$, **algebraically factor** out $a$:
$$x(at-b)=x\!\left(a\!\left(t-\tfrac{b}{a}\right)\right).$$
Read this as: shift by $b/a$, then scale by $a$. Equivalently, plug numerical values of $t$ and check.

**Example.** $x(2t-4)=x(2(t-2))$: shift right by 2, compress by 2.

### 3.2 Periodicity

- CT: $x(t)=x(t+T_0)$ for fundamental (smallest positive) $T_0$.
- DT: $x[n]=x[n+N_0]$ for smallest positive *integer* $N_0$.
- CT $\cos(\omega_0 t)$ is always periodic with $T_0=2\pi/\omega_0$.
- DT $\cos(\omega_0 n)$ is periodic **only** when $\omega_0/(2\pi)$ is rational $p/q$; then $N_0=q$ (smallest).

### 3.3 Energy vs. Power

- Sinusoids, constants $\Rightarrow$ finite power, infinite energy.
- Decaying exponentials, finite-duration pulses $\Rightarrow$ finite energy, zero power.
- Growing exponentials $\Rightarrow$ neither.

### 3.4 Even/Odd Decomposition

Any signal decomposes uniquely as $x = x_e + x_o$:
$$x_e(t)=\tfrac12[x(t)+x(-t)],\qquad x_o(t)=\tfrac12[x(t)-x(-t)].$$
- Cosine is even; sine is odd.
- Product: even $\times$ even $=$ even, odd $\times$ odd $=$ even, even $\times$ odd $=$ odd.

---

## 4. Complex Exponentials and Euler

### 4.1 Converting Between Rectangular and Polar

$$c = a + jb = re^{j\theta}, \quad r = \sqrt{a^2+b^2}, \quad \theta = \mathrm{atan2}(b,a).$$

### 4.2 Euler Identities

$$e^{j\phi} = \cos\phi + j\sin\phi,\quad \cos\phi = \frac{e^{j\phi}+e^{-j\phi}}{2},\quad \sin\phi = \frac{e^{j\phi}-e^{-j\phi}}{2j}.$$

### 4.3 Phasor Form

A single-frequency real sinusoid $A\cos(\omega_0 t + \theta)$ has complex amplitude $X_C = A e^{j\theta}$; full signal is $\mathrm{Re}\{X_C e^{j\omega_0 t}\}$. Linear combinations of same-frequency sinusoids reduce to algebra on complex amplitudes.

### 4.4 Useful Identities Derivable from Euler

- $\cos(\alpha\pm\beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$.
- $\sin(\alpha\pm\beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$.
- $\cos\alpha\cos\beta = \tfrac12[\cos(\alpha-\beta)+\cos(\alpha+\beta)]$.
- $\sin\alpha\sin\beta = \tfrac12[\cos(\alpha-\beta)-\cos(\alpha+\beta)]$.
- $\cos\alpha\sin\beta = \tfrac12[\sin(\alpha+\beta)-\sin(\alpha-\beta)]$.

### 4.5 DT Sinusoid Quirks

- $e^{j(\omega_0+2\pi)n}=e^{j\omega_0 n}$: frequencies differing by $2\pi$ are identical. Effective range: $\omega_0\in[-\pi,\pi]$ or $[0,2\pi)$.
- Periodic iff $\omega_0/(2\pi)$ is rational.
- Highest DT frequency is at $\omega_0=\pm\pi$ (oscillates every sample); **not** at large $\omega_0$.

---

## 5. Fundamental Functions

### 5.1 DT Impulse / Step

$$\delta[n]=\begin{cases}1,& n=0\\0,& \text{else}\end{cases},\qquad u[n]=\begin{cases}1,& n\ge 0\\0,& \text{else}\end{cases}.$$

- $\delta[n]=u[n]-u[n-1]$ (first difference).
- $u[n]=\sum_{m=-\infty}^{n}\delta[m]$ (running sum).
- Decomposition: $x[n]=\sum_k x[k]\delta[n-k]$.

### 5.2 CT Impulse / Step

Dirac delta $\delta(t)$: "infinitely tall, infinitely narrow" spike with unit area. Realistically, the limit of any unit-area pulse (rectangular, triangular, Gaussian) as the width $\to 0$.

$$\int_{-\infty}^\infty\delta(t)\,dt=1,\qquad \delta(t)=\frac{du(t)}{dt},\qquad u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau.$$

### 5.3 Key Rules

- **Sifting (integral, yields a number):** $\int x(\tau)\delta(\tau-t_0)d\tau = x(t_0)$, provided $t_0$ is inside the integration interval.
- **Sampling (multiplication, yields a scaled impulse):** $x(t)\delta(t-t_0) = x(t_0)\delta(t-t_0)$.
- **Scaling:** $\delta(at)=\delta(t)/|a|$.

### 5.4 Ramp Function and the Singularity Chain

$$r(t) = tu(t), \quad \int_{-\infty}^t u(\tau)d\tau = r(t), \quad \int_{-\infty}^t \delta(\tau)d\tau = u(t).$$

Family chain: $r(t) \to u(t) \to \delta(t) \to \delta'(t)$ via $d/dt$; integration reverses.

---

## 6. System Properties Checklist

Walk through all six for any system you see. A worked example follows.

1. **Memoryless?** Does the equation reference $x$ at any time other than the output time? Past output $\Rightarrow$ memory.
2. **Causal?** Does the equation reference any future value ($x[n+1]$, $x(t+1)$)? Non-causal if yes. LTI shortcut: $h(t)=0$ for $t<0$.
3. **Stable (BIBO)?** Bound $|y|$ given $|x|\le B_x$. LTI shortcut: $\int|h|<\infty$ or $\sum|h[n]|<\infty$.
4. **Time-invariant?** Compute $y_2(t)$ from $x_2(t)=x_1(t-t_0)$ and compare with $y_1(t-t_0)$. Explicit $t$/$n$ or time-scaling = time-varying.
5. **Linear?** Check $a x_1 + b x_2 \to a y_1 + b y_2$. Quick sanity check: zero-in / zero-out test.
6. **Invertible?** Can you recover $x$ from $y$? LTI: does $h_i$ exist with $h*h_i=\delta$?

### Worked example — $y(t)=tx(t)$

- **Memoryless:** yes.
- **Causal:** yes.
- **Stable:** **no** (let $x=1$; $y=t$ unbounded).
- **Time-invariant:** **no**. $y_2(t)=tx_1(t-t_0)$ vs. $y_1(t-t_0)=(t-t_0)x_1(t-t_0)$ — explicit $t$.
- **Linear:** yes ($t$ is a scalar at each fixed $t$).
- **Invertible:** yes away from $t=0$.

### Worked example — $y(t)=3x(t)+2$

Memoryless, causal, stable, time-invariant, **nonlinear** (zero input $\to y=2\ne 0$). It is *affine*, not linear.

### Worked example — $y[n]=x[n]-\beta x[n+1]$

Has memory; **non-causal** (uses $x[n+1]$); BIBO stable ($|y|\le (1+|\beta|)B_x$); time-invariant; linear.

---

## 7. LTI Convolution (DT and CT)

### 7.1 DT Convolution Cookbook

1. List nonzero samples of $x[k]$ and $h[k]$.
2. Output range: first nonzero at sum of earliest indices; last nonzero at sum of latest indices. Total length $N+M-1$.
3. For each $n$, $y[n]=\sum_k x[k]h[n-k]$. Only $k$ values where both are nonzero contribute.
4. Polynomial trick: treat $x[n]$, $h[n]$ as polynomials in $z^{-1}$; convolution = polynomial multiplication.
5. Sanity check: $\left(\sum x\right)\left(\sum h\right) = \sum y$.

**Standard results:**
- $x[n]*\delta[n-n_0]=x[n-n_0]$.
- $\alpha^n u[n]*u[n] = \dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$.
- $u[n]*u[n] = (n+1)u[n]$.

### 7.2 CT Convolution Cookbook

1. Sketch $x(\tau)$ and $h(\tau)$. Identify supports $[a,b]$ and $[c,d]$.
2. Flip: $h(-\tau)$ has support $[-d,-c]$.
3. Shift by $t$: $h(t-\tau)$ has support $[t-d,t-c]$.
4. Critical $t$-values (boundary events): $a+c$, $a+d$, $b+c$, $b+d$. Sort them.
5. For each interval between critical values,
   $$y(t)=\int_{\max(a,\,t-d)}^{\min(b,\,t-c)}x(\tau)h(t-\tau)\,d\tau$$
   if the overlap is nonempty; else $y(t)=0$.
6. Continuity: $y(t)$ must match at each boundary.
7. Sanity: total area $\int y\,dt = \int x\,dt\cdot\int h\,dt$.

**Standard results:**
- Rect $*$ rect $=$ trapezoid (triangle if widths equal).
- $e^{-at}u(t)*u(t)=\tfrac{1}{a}(1-e^{-at})u(t)$.
- $e^{-at}u(t)*e^{-bt}u(t)=\tfrac{1}{b-a}(e^{-at}-e^{-bt})u(t)$ for $a\ne b$.
- $u(t)*u(t)=tu(t)=r(t)$.

### 7.3 LTI Properties from the Impulse Response

| Property | CT test on $h(t)$ | DT test on $h[n]$ |
|---|---|---|
| Memoryless | $h(t)=K\delta(t)$ | $h[n]=K\delta[n]$ |
| Causal | $h(t)=0$ for $t<0$ | $h[n]=0$ for $n<0$ |
| BIBO stable | $\int|h(t)|dt<\infty$ | $\sum|h[n]|<\infty$ |
| Invertible | $\exists\,h_i: h*h_i=\delta$ | same |

---

## 8. First-Order Equations and Impulse Responses

### 8.1 CT First Order

$$\frac{dy}{dt}+ay=bx.$$

Under initial rest ($y(0^-)=0$) and causal operation, solve by either:

1. **Impulse + jump condition:** for $t>0$ the homogeneous solution is $Ce^{-at}$. Integrate across $t=0$: $h(0^+)-h(0^-)=b$, so $C=b$. Combined with $u(t)$ for causality:
   $$h(t)=be^{-at}u(t).$$
2. **Homogeneous + particular:** e.g., for a step input $x(t)=u(t)$, try $y_p=K$ (constant), get $K=b/a$; then $y(t)=(b/a)(1-e^{-at})u(t)$.

Stability: $a>0$ (exponential decays). $a<0$ is unstable.

### 8.2 DT First Order

$$y[n]=\alpha y[n-1]+bx[n].$$

Iterate from initial rest ($y[n]=0$ for $n<0$):
- $h[0]=b$
- $h[1]=\alpha b$
- $h[2]=\alpha^2 b$, ... $\Rightarrow h[n]=b\alpha^n u[n]$.

Stability: $|\alpha|<1$.

### 8.3 Step Responses

- CT: $s(t)=(b/a)(1-e^{-at})u(t)$.
- DT: $s[n]=b\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$; steady state $b/(1-\alpha)$.

---

## 9. Singularity Functions

Family chain by differentiation (right) / integration (left):

$$\cdots \;\xrightarrow{\int}\; r(t)=tu(t) \;\xrightarrow{d/dt}\; u(t) \;\xrightarrow{d/dt}\; \delta(t) \;\xrightarrow{d/dt}\; \delta'(t) \;\xrightarrow{d/dt}\; \cdots$$

**Key rules:**
- $\delta(at)=\delta(t)/|a|$.
- $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$ (multiplication).
- $\int x(\tau)\delta(\tau-t_0)d\tau=x(t_0)$ (sifting).
- $x(t)*\delta'(t)=dx/dt$ (doublet convolution).

**Derivative of $(t+1)u(t)$:** Apply product rule:
$$\frac{d}{dt}[(t+1)u(t)] = 1\cdot u(t) + (t+1)\delta(t) = u(t)+\delta(t),$$
where $(t+1)\delta(t)=\delta(t)$ (multiplication rule at $t=0$).

---

## 10. What to Memorize

**Must-know identities**
- Euler: $e^{j\phi}=\cos\phi+j\sin\phi$; inverse Euler for cos / sin.
- Polar product: magnitudes multiply, angles add.
- $\delta(t)=du/dt$; $u(t)=\int_{-\infty}^t\delta(\tau)d\tau$; same for DT with sums.
- $\delta[n]=u[n]-u[n-1]$; $u[n]=\sum_{m\le n}\delta[m]$.

**Must-know convolution facts**
- $x*\delta=x$, $x*\delta(t-t_0)=x(t-t_0)$.
- Convolution of two rects = trapezoid (or triangle if equal width).
- $e^{-at}u(t)*u(t)=\tfrac{1}{a}(1-e^{-at})u(t)$.
- $u(t)*u(t)=r(t)=tu(t)$.
- DT: $\alpha^n u[n]*u[n]=\tfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$; $u[n]*u[n]=(n+1)u[n]$.
- Output length (finite): $N+M-1$.
- Sanity: $\sum y = (\sum x)(\sum h)$ / $\int y = (\int x)(\int h)$.

**Must-know LTI tests**
- Causal: $h(t)=0$ for $t<0$.
- Stable: $\int|h|dt<\infty$ (CT) or $\sum|h[n]|<\infty$ (DT).
- Memoryless: $h(t)=K\delta(t)$.
- Step response = integral/cumulative sum of impulse response.

**Must-know first-order formulas**
- CT: $\dfrac{dy}{dt}+ay=bx \Rightarrow h(t)=be^{-at}u(t)$; stable iff $a>0$.
- DT: $y[n]-\alpha y[n-1]=bx[n]\Rightarrow h[n]=b\alpha^n u[n]$; stable iff $|\alpha|<1$.

**Must-know singularity relations**
- $r\to u\to\delta\to\delta'$ by $d/dt$.
- $\delta(at)=\delta(t)/|a|$.
- $x(t)\delta(t-t_0)=x(t_0)\delta(t-t_0)$.
- $x(t)*\delta'(t)=dx/dt$.

---

## 11. Common Pitfalls

1. **Affine $\ne$ linear.** $y=mx+b$ with $b\ne 0$ fails zero-in / zero-out. *Always* check.
2. **Forgetting to flip before shifting.** $h(t-\tau)$ = flip $h(\tau)$ first, then shift by $t$.
3. **Wrong integration/summation limits.** Only include $\tau$ (or $k$) where *both* $x$ and $h$ are nonzero. Sketch!
4. **Confusing sifting with sampling.** Sifting is an integral yielding a number $x(t_0)$. Sampling is multiplication yielding a scaled impulse $x(t_0)\delta(t-t_0)$.
5. **Missing $u(t)$ in impulse responses.** Causal system $\Rightarrow$ multiply by $u(t)$ or $u[n]$ to force zero for $t<0$.
6. **Sign error in first-order exponent.** $\dfrac{dy}{dt}+ay=bx$ yields $e^{-at}$, not $e^{+at}$. Stability wants $a>0$.
7. **Mistaking $|a|<1$ for $a<0$.** DT stability is magnitude-based: $\alpha=-0.9$ is stable ($|\alpha|=0.9$).
8. **DT periodicity assumption.** $\cos(\omega_0 n)$ is periodic only when $\omega_0/(2\pi)$ is rational. $\cos(n)$ is **not** periodic.
9. **Explicit $t$ / $n$ = time-varying.** $y(t)=tx(t)$, $y[n]=nx[n]$, $y(t)=x(2t)$ are all time-varying.
10. **BIBO requires absolute value.** Stability test uses $\int|h|dt$, not $\int h\,dt$. Alternating impulse responses are easy to get wrong.
11. **Transformation ordering.** For $x(at-b)$ write $x(a(t-b/a))$: shift by $b/a$, then scale by $a$. Doing it in the wrong order shifts by $b$ instead of $b/a$.
12. **Initial rest convention.** For diff-eqn problems, assume $y(0^-)=0$ (and $y[n]=0$ for $n<0$) unless stated otherwise.
13. **Delta limits.** $\int_0^5 x(t)\delta(t+2)dt = 0$, because the impulse at $t=-2$ is outside the interval.
14. **Sifting vs. product rule.** $(t+1)\delta(t)=\delta(t)$ (set $t=0$ in the smooth factor), whereas $\int(t+1)\delta(t)dt=1$. Don't mix up the two.
15. **Causality and stability independence.** A causal system can be unstable (e.g., $e^{2t}u(t)$); a non-causal system can be stable (e.g., $e^{t}u(-t)$).

---

*Prepared for CEC 315 Exam 1 — Spring 2026.*
