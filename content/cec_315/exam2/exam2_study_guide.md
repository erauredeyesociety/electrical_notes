# CEC 315 — Exam 2 Study Guide (Lectures 9–15)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Lectures 9–15 (Fourier series, Fourier transforms, filters, Bode plots)
**Based on:** lecture PDFs in `all_lectures/`, lecture summaries in `lecture_summaries/`, and existing exam2 notes (`cheatsheet.md`, `equations.md`, `exam2_solutions.md`, `study_guide_summary.md`, `hw_lctr9_11_solutions_summary.md`, `hw_lctr12_15_solutions_summary.md`).

---

## Table of Contents

1. [Topic Overview by Lecture](#1-topic-overview-by-lecture)
2. [Key Equations Reference](#2-key-equations-reference)
3. [Fourier Transform Properties and Pairs](#3-fourier-transform-properties-and-pairs)
4. [Filter Design Basics (Magnitude/Phase, Ideal Filters, Bode)](#4-filter-design-basics)
5. [Second-Order Systems](#5-second-order-systems)
6. [What to Memorize](#6-what-to-memorize)
7. [Common Pitfalls](#7-common-pitfalls)

---

## 1. Topic Overview by Lecture

### Lecture 9 — Continuous-Time Fourier Series (Oppenheim §3.0–3.5)
- Complex exponentials $e^{st}$ are **eigenfunctions** of LTI systems: $e^{st}\to H(s)e^{st}$, where $H(s)=\int h(\tau)e^{-s\tau}d\tau$. Frequency is preserved.
- Periodic signal: $x(t)=x(t+T)$, fundamental frequency $\omega_0=2\pi/T$.
- CTFS synthesis/analysis:
$$x(t)=\sum_{k=-\infty}^\infty a_k e^{jk\omega_0 t},\qquad a_k=\frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}dt.$$
- $a_0=\frac{1}{T}\int_T x(t)dt$ is the DC/average value.
- Conjugate symmetry for real signals: $a_{-k}=a_k^*$.
- **Inspection trick:** expand $\cos/\sin$ via Euler, read off coefficients directly without integrating.

### Lecture 10 — Convergence, Properties, DTFS (§3.4, §3.6–3.8)
- **Dirichlet conditions:** $\int_T|x|dt<\infty$, bounded variation, finite number of finite-jump discontinuities per period. At a discontinuity the FS converges to the midpoint $(x(t_0^-)+x(t_0^+))/2$.
- **Gibbs phenomenon:** ~9% overshoot near jumps, persists for all $N$; ripple narrows but peak amplitude is fixed.
- **Spectral decay vs. smoothness:** jump $\sim 1/k$, continuous with jump derivative $\sim 1/k^2$; in general if the $m$th derivative is the first discontinuous one, $|a_k|\sim 1/k^{m+1}$.
- **CTFS properties:** linearity, time shift $a_k e^{-jk\omega_0 t_0}$, time reversal $a_{-k}$, conjugation $a_{-k}^*$, differentiation $jk\omega_0 a_k$, Parseval.
- **DTFS:** $x[n]=\sum_{k=\langle N\rangle} a_k e^{jk(2\pi/N)n}$, $a_k=\frac{1}{N}\sum_{n=\langle N\rangle} x[n]e^{-jk(2\pi/N)n}$, only $N$ distinct coefficients (periodic $a_{k+N}=a_k$), no convergence issues, Parseval $\frac{1}{N}\sum|x[n]|^2=\sum_{k=\langle N\rangle}|a_k|^2$.

### Lecture 11 — Frequency Response and Filtering (§3.9–3.12)
- Output of LTI system for periodic input: $y(t)=\sum a_k H(jk\omega_0)e^{jk\omega_0 t}$, i.e. $b_k=a_k\cdot H(jk\omega_0)$.
- CT frequency response: $H(j\omega)=\int h(\tau)e^{-j\omega\tau}d\tau$; for $h(t)=e^{-at}u(t)$, $H(j\omega)=1/(a+j\omega)$.
- DT frequency response: $H(e^{j\omega})=\sum_n h[n]e^{-j\omega n}$; for $h[n]=a^n u[n]$, $H(e^{j\omega})=1/(1-ae^{-j\omega})$.
- **Ideal filter types:** LP, HP, BP, BS — rectangular magnitude, zero phase.
- **RC lowpass:** $H(j\omega)=1/(1+j\omega RC)$, $\omega_c=1/RC$ (−3 dB), phase $=-45°$ at $\omega_c$.
- **General first-order LP:** $H(j\omega)=1/(a+j\omega)$, $\omega_c=a$.
- Bandwidth / rise-time trade-off: $\omega_c\cdot t_r\approx\text{constant}$.

### Lecture 12 — Fourier Transforms (Ch. 4–5)
- CTFT pair: $X(j\omega)=\int x(t)e^{-j\omega t}dt$, $x(t)=\frac{1}{2\pi}\int X(j\omega)e^{j\omega t}d\omega$.
- Convergence: Dirichlet + $\int|x|dt<\infty$ (absolutely integrable).
- **FT of periodic signal:** $X(j\omega)=\sum_k 2\pi a_k\delta(\omega-k\omega_0)$.
- DTFT pair: $X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$, $x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}d\omega$. DTFT is $2\pi$-periodic in $\omega$.
- **Four Fourier representations** (discrete $\leftrightarrow$ periodic in the other domain): CTFS (CT periodic), CTFT (CT aperiodic), DTFS (DT periodic), DTFT (DT aperiodic).

### Lecture 13 — FT Properties and Convolution (Ch. 4 §4.3–4.7)
- **Convolution property** (the key payoff): $y=x*h\Leftrightarrow Y=XH$. Analysis pipeline: transform → multiply → partial fractions → inverse.
- **Multiplication property:** $xy\Leftrightarrow\frac{1}{2\pi}X*Y$.
- Other properties: linearity, time shift ($e^{-j\omega t_0}X$), frequency shift ($X(j(\omega-\omega_0))$), scaling ($\frac{1}{|a|}X(j\omega/a)$), duality ($X(jt)\leftrightarrow 2\pi x(-\omega)$), differentiation ($j\omega X$), integration ($X/(j\omega)+\pi X(0)\delta(\omega)$), Parseval ($\int|x|^2dt=\frac{1}{2\pi}\int|X|^2d\omega$).
- **Systems from differential equations:** $\sum b_k y^{(k)}=\sum c_k x^{(k)}\Rightarrow H(j\omega)=\frac{\sum c_k(j\omega)^k}{\sum b_k(j\omega)^k}$. For DT: $y[n-k]\to e^{-j\omega k}Y(e^{j\omega})$.

### Lecture 14 — Magnitude/Phase and Ideal Filters (Ch. 6 §6.1–6.5)
- Polar form: $X(j\omega)=|X(j\omega)|e^{j\angle X(j\omega)}$; decibels $|H|_\text{dB}=20\log_{10}|H|$ (−3 dB ≈ $1/\sqrt{2}$).
- Energy: $E=\int|x|^2dt=\frac{1}{2\pi}\int|X|^2 d\omega$; $|X|^2$ is energy spectral density (phase has no effect on energy).
- **Linear phase** $\angle H=-\omega t_0\Rightarrow$ pure delay, no distortion. Nonlinear phase $\Rightarrow$ phase distortion.
- **Group delay:** $\tau(\omega)=-\frac{d}{d\omega}\angle H(j\omega)$; constant $\tau$ $\Leftrightarrow$ linear phase.
- **Ideal LPF:** $H(j\omega)=1$ on $|\omega|\le\omega_c$, $0$ elsewhere; $h(t)=\frac{\sin(\omega_c t)}{\pi t}$ — noncausal (unrealizable). Delayed version still noncausal (sinc extends to $-\infty$).
- **Real filter specs:** passband edge $\omega_p$, stopband edge $\omega_s$, transition band, passband ripple $\delta_1$, stopband attenuation $\delta_2$.
- Bandwidth–rise-time trade-off: $\omega_c t_r\approx\text{const}$.

### Lecture 15 — First/Second-Order Systems, Bode Plots (Ch. 6 §6.6)
- **First-order LP** standard form: $H(j\omega)=1/(1+j\omega/\omega_c)$. DC gain 1; at $\omega_c$, $|H|=1/\sqrt{2}$ (−3 dB), phase $-45°$; phase $0°\to-90°$ across $[\omega_c/10,10\omega_c]$. Magnitude slope $0$ dB $\to -20$ dB/dec past $\omega_c$.
- **Bode building blocks:** pole $\to -20$ dB/dec, $0\to-90°$; zero $\to +20$ dB/dec, $0\to+90°$; $(j\omega)^{\pm1}$ $\to\pm20$ dB/dec through all $\omega$. Cascade $\to$ add dB magnitudes and phases.
- **Second-order** standard form: $H(j\omega)=\omega_n^2/[(j\omega)^2+2\zeta\omega_n(j\omega)+\omega_n^2]$. DC gain 1; at $\omega_n$: $|H|=1/(2\zeta)$ and $\angle H=-90°$ (always); HF slope $-40$ dB/dec, phase $0°\to-180°$.
- Damping: $\zeta<1$ underdamped, $=1$ critically, $>1$ over.
- **Resonance:** $\omega_r=\omega_n\sqrt{1-2\zeta^2}$ exists iff $\zeta<1/\sqrt{2}$; peak $|H|_\max=1/(2\zeta\sqrt{1-\zeta^2})$.
- **Step response (underdamped):** %OS $=100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$, $t_p=\pi/\omega_d$ with $\omega_d=\omega_n\sqrt{1-\zeta^2}$, $t_s\approx 4/(\zeta\omega_n)$, $t_r\approx 1.8/\omega_n$.
- **DT analog:** first-order pole at $z=a$ with $|a|<1$ stable; second-order poles at $re^{\pm j\theta_0}$, $r$ = damping, $\theta_0$ = resonance.

---

## 2. Key Equations Reference

### 2.1 Fourier Series (CT)

| Quantity | Formula |
|---|---|
| Synthesis | $\displaystyle x(t)=\sum_{k=-\infty}^\infty a_k e^{jk\omega_0 t}$ |
| Analysis | $\displaystyle a_k=\frac{1}{T}\int_T x(t)e^{-jk\omega_0 t}dt$ |
| Fundamental freq | $\omega_0=2\pi/T$ |
| DC component | $\displaystyle a_0=\frac{1}{T}\int_T x(t)dt$ |
| Parseval (avg power) | $\displaystyle\frac{1}{T}\int_T|x|^2dt=\sum_k|a_k|^2$ |

### 2.2 Fourier Series (DT, length $N$)

| Quantity | Formula |
|---|---|
| Synthesis | $\displaystyle x[n]=\sum_{k=\langle N\rangle} a_k e^{jk(2\pi/N)n}$ |
| Analysis | $\displaystyle a_k=\frac{1}{N}\sum_{n=\langle N\rangle} x[n]e^{-jk(2\pi/N)n}$ |
| Fund. freq | $\omega_0=2\pi/N$ |
| Parseval | $\displaystyle\frac{1}{N}\sum_{n=\langle N\rangle}|x[n]|^2=\sum_{k=\langle N\rangle}|a_k|^2$ |
| Periodicity | $a_{k+N}=a_k$ |

### 2.3 Fourier Transform (CT)

| Quantity | Formula |
|---|---|
| Forward (analysis) | $\displaystyle X(j\omega)=\int_{-\infty}^\infty x(t)e^{-j\omega t}dt$ |
| Inverse (synthesis) | $\displaystyle x(t)=\frac{1}{2\pi}\int_{-\infty}^\infty X(j\omega)e^{j\omega t}d\omega$ |
| Parseval | $\displaystyle\int|x(t)|^2dt=\frac{1}{2\pi}\int|X(j\omega)|^2d\omega$ |

### 2.4 Fourier Transform (DT)

| Quantity | Formula |
|---|---|
| Forward | $\displaystyle X(e^{j\omega})=\sum_n x[n]e^{-j\omega n}$ |
| Inverse | $\displaystyle x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\omega})e^{j\omega n}d\omega$ |
| Parseval | $\displaystyle\sum_n|x[n]|^2=\frac{1}{2\pi}\int_{2\pi}|X(e^{j\omega})|^2d\omega$ |
| Periodicity | $X(e^{j(\omega+2\pi)})=X(e^{j\omega})$ |

### 2.5 Frequency Response

| Quantity | CT | DT |
|---|---|---|
| $H$ from $h$ | $H(j\omega)=\int h(\tau)e^{-j\omega\tau}d\tau$ | $H(e^{j\omega})=\sum_n h[n]e^{-j\omega n}$ |
| Causal first-order | $\dfrac{1}{a+j\omega}$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| Output (periodic) | $b_k=a_k H(jk\omega_0)$ | $b_k=a_k H(e^{jk\omega_0})$ |

---

## 3. Fourier Transform Properties and Pairs

### 3.1 CT FT Properties

| Property | Time | Frequency |
|---|---|---|
| Linearity | $ax+by$ | $aX+bY$ |
| Time shift | $x(t-t_0)$ | $e^{-j\omega t_0}X(j\omega)$ |
| Frequency shift | $e^{j\omega_0 t}x(t)$ | $X(j(\omega-\omega_0))$ |
| Scaling | $x(at)$, $a\ne0$ | $\dfrac{1}{|a|}X(j\omega/a)$ |
| Time reversal | $x(-t)$ | $X(-j\omega)$ (real $x\Rightarrow X^*$) |
| Conjugation | $x^*(t)$ | $X^*(-j\omega)$ |
| Differentiation (time) | $dx/dt$ | $j\omega X(j\omega)$ |
| Integration | $\displaystyle\int_{-\infty}^t x(\tau)d\tau$ | $\dfrac{X(j\omega)}{j\omega}+\pi X(0)\delta(\omega)$ |
| Differentiation (freq) | $-jtx(t)$ | $dX/d\omega$ |
| Convolution | $x*h$ | $X\cdot H$ |
| Multiplication | $x\cdot y$ | $\dfrac{1}{2\pi}X*Y$ |
| Duality | $X(jt)$ | $2\pi x(-\omega)$ |
| Parseval | $\int|x|^2dt$ | $\dfrac{1}{2\pi}\int|X|^2d\omega$ |

### 3.2 CT FS Properties (summary)

| Property | Time | Coefficient |
|---|---|---|
| Linearity | $Ax+By$ | $Aa_k+Bb_k$ |
| Time shift | $x(t-t_0)$ | $a_k e^{-jk\omega_0 t_0}$ |
| Time reversal | $x(-t)$ | $a_{-k}$ |
| Conjugation | $x^*(t)$ | $a_{-k}^*$ |
| Differentiation | $dx/dt$ | $jk\omega_0 a_k$ |
| Real signal | $x(t)\in\mathbb{R}$ | $a_{-k}=a_k^*$ |

### 3.3 Common CT FT Pairs

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $u(t)$ | $\dfrac{1}{j\omega}+\pi\delta(\omega)$ |
| $e^{-at}u(t)$, $a>0$ | $\dfrac{1}{a+j\omega}$ |
| $te^{-at}u(t)$, $a>0$ | $\dfrac{1}{(a+j\omega)^2}$ |
| $e^{-a|t|}$, $a>0$ | $\dfrac{2a}{a^2+\omega^2}$ |
| $e^{j\omega_0 t}$ | $2\pi\delta(\omega-\omega_0)$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| $\sin(\omega_0 t)$ | $\dfrac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)]$ |
| $\text{rect}(t/T_1)$ (width $2T_1$) | $\dfrac{2\sin(\omega T_1)}{\omega}=2T_1\,\text{sinc}(\omega T_1/\pi)$ |
| $\dfrac{\sin(Wt)}{\pi t}$ | $\text{rect}(\omega/(2W))$ (ideal LPF) |
| Periodic $x$ | $\displaystyle\sum_k 2\pi a_k\delta(\omega-k\omega_0)$ |

### 3.4 Common DT FT Pairs

| $x[n]$ | $X(e^{j\omega})$ |
|---|---|
| $\delta[n]$ | $1$ |
| $\delta[n-n_0]$ | $e^{-j\omega n_0}$ |
| $1$ | $\displaystyle 2\pi\sum_k\delta(\omega-2\pi k)$ |
| $a^n u[n]$, $|a|<1$ | $\dfrac{1}{1-ae^{-j\omega}}$ |
| $(n+1)a^n u[n]$, $|a|<1$ | $\dfrac{1}{(1-ae^{-j\omega})^2}$ |
| $e^{j\omega_0 n}$ | $\displaystyle 2\pi\sum_k\delta(\omega-\omega_0-2\pi k)$ |

---

## 4. Filter Design Basics

### 4.1 Magnitude, Phase, dB

- Polar form: $H(j\omega)=|H|e^{j\angle H}$.
- $|H|_\text{dB}=20\log_{10}|H|$; $-3$ dB $\Leftrightarrow|H|=1/\sqrt{2}\Leftrightarrow$ half power.
- Linear phase $\angle H=-\omega t_0\Rightarrow$ pure delay $t_0$.
- Group delay $\tau(\omega)=-d(\angle H)/d\omega$; constant iff phase is linear.

### 4.2 Ideal Filters

| Filter | $H(j\omega)$ |
|---|---|
| Ideal LPF | $1$ for $|\omega|\le\omega_c$, $0$ else |
| Ideal HPF | $1-\text{ideal LPF}$ |
| Ideal BPF | $1$ for $\omega_1\le|\omega|\le\omega_2$, $0$ else |

Impulse response of ideal LPF: $h(t)=\dfrac{\sin(\omega_c t)}{\pi t}$. **Noncausal → unrealizable.**

### 4.3 Bode Plot Rules

- Plot $|H|_\text{dB}$ vs $\log_{10}\omega$ and $\angle H$ vs $\log_{10}\omega$.
- Cascades add magnitudes (dB) and phases.
- **First-order pole** $(1+j\omega/\omega_c)^{-1}$: flat at 0 dB below $\omega_c$, $-20$ dB/dec above; phase $0°\to-45°$ at $\omega_c\to-90°$.
- **First-order zero** $(1+j\omega/\omega_c)$: flat 0 dB → $+20$ dB/dec; phase $0\to+45°\to+90°$.
- **$(j\omega)^{\pm1}$:** constant $\pm 20$ dB/dec through all frequencies; phase fixed at $\pm 90°$.
- **Second-order** with $\omega_n$ and $\zeta<1/\sqrt2$: 0 dB flat $\to$ $-40$ dB/dec past $\omega_n$, phase $0°\to -90°$ at $\omega_n\to -180°$; peak at $\omega_r=\omega_n\sqrt{1-2\zeta^2}$ of height $|H|_\max=1/(2\zeta\sqrt{1-\zeta^2})$.

---

## 5. Second-Order Systems

**Standard form:** $H(j\omega)=\dfrac{\omega_n^2}{(j\omega)^2+2\zeta\omega_n(j\omega)+\omega_n^2}$.

| Quantity | Formula | Notes |
|---|---|---|
| DC gain | $1$ | always |
| $|H(j\omega_n)|$ | $1/(2\zeta)$ | always |
| $\angle H(j\omega_n)$ | $-90°$ | always |
| Resonance freq | $\omega_r=\omega_n\sqrt{1-2\zeta^2}$ | only if $\zeta<1/\sqrt2$ |
| Peak magnitude | $1/(2\zeta\sqrt{1-\zeta^2})$ | only if $\zeta<1/\sqrt2$ |
| Damped freq | $\omega_d=\omega_n\sqrt{1-\zeta^2}$ | $\zeta<1$ |
| %OS (step) | $100\,e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ | $\zeta<1$ |
| Peak time | $t_p=\pi/\omega_d$ | $\zeta<1$ |
| Settling 2% | $t_s\approx 4/(\zeta\omega_n)$ | $\zeta<1$ |
| Rise time | $t_r\approx 1.8/\omega_n$ | $\zeta<1$ |
| HF Bode slope | $-40$ dB/dec | always |

**Damping classification:** $\zeta<1$ underdamped (complex poles), $\zeta=1$ critically damped (repeated real pole), $\zeta>1$ overdamped (distinct real poles).

---

## 6. What to Memorize

**Must-know pairs:**
$$\delta(t)\leftrightarrow 1,\quad 1\leftrightarrow 2\pi\delta(\omega),\quad e^{-at}u(t)\leftrightarrow\frac{1}{a+j\omega},\quad e^{-a|t|}\leftrightarrow\frac{2a}{a^2+\omega^2},$$
$$\cos\omega_0 t\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)],\quad \text{rect}_{T_1}\leftrightarrow 2T_1\text{sinc}(\omega T_1/\pi).$$

**Must-know identities:**
- $\omega_0=2\pi/T$ and $a_0=\frac{1}{T}\int_T x\,dt$.
- Conjugate symmetry: real $x\Rightarrow a_{-k}=a_k^*$ and $X(-j\omega)=X^*(j\omega)$.
- Parseval (CTFS vs CTFT differ by factor $1/(2\pi)$!): $\int|x|^2dt=\frac{1}{2\pi}\int|X|^2d\omega$.
- Differentiation: $dx/dt\leftrightarrow j\omega X$; kills DC since $(j0)X(0)=0$.
- Convolution $\leftrightarrow$ multiplication (the workhorse).
- Gibbs ~9% (invariant in $N$).
- Spectral decay $\sim 1/k^{m+1}$ where $m$ counts continuous derivatives.

**Must-know frequency response anchors:**
- First-order LP $1/(1+j\omega/\omega_c)$: 0 dB, $-45°$ at $\omega_c$, $-20$ dB/dec.
- Second-order standard form: DC gain 1, $|H(j\omega_n)|=1/(2\zeta)$, phase $-90°$ at $\omega_n$, HF slope $-40$ dB/dec.
- Cutoff of $1/(a+j\omega)$ is $\omega_c=a$.

**Must-know procedures:**
1. **Find CTFS coefficients:** identify $T,\omega_0$; compute $a_0$; set up $a_k$ integral over one period; simplify with Euler.
2. **LTI output from periodic input:** compute FS coefficients $a_k$, compute $H(jk\omega_0)$, form $b_k=a_k H(jk\omega_0)$, reassemble $y$.
3. **Convolution pipeline:** $X,H\Rightarrow Y=XH$; partial fractions $\Rightarrow$ inverse FT term by term.
4. **ODE $\to H(j\omega)$:** replace $d^k/dt^k\to (j\omega)^k$; $H=\frac{\sum c_k(j\omega)^k}{\sum b_k(j\omega)^k}$.
5. **Second-order parameter extraction:** read $\omega_n^2$ and $2\zeta\omega_n$; compute $\zeta,\omega_n$; decide damping/resonance; evaluate %OS, $t_s$, $|H|_\max$.

---

## 7. Common Pitfalls

1. **Forgetting to kill DC when differentiating.** Always: $d_0=j(0)\omega_0 a_0=0$.
2. **Gibbs misconception:** the overshoot is ~9% of the jump height and does NOT vanish as $N\to\infty$ — only the ripple width does.
3. **Conflating CTFS and CTFT Parseval constants.** CTFS: $\sum|a_k|^2$ equals the average power; CTFT: the integral of $|X|^2$ carries a $1/(2\pi)$.
4. **Wrong sign of $e^{j\omega_0 t}$:** frequency shift multiplies time by $e^{j\omega_0 t}$, which shifts the spectrum to $\omega-\omega_0$ (not $\omega+\omega_0$).
5. **Ideal filter $\ne$ causal.** Sinc impulse response extends to $-\infty$; any delayed version is still noncausal. You cannot implement an ideal filter.
6. **DTFS has only $N$ coefficients**, not infinitely many; summing more produces the same $N$ harmonics.
7. **Mixing up cutoff forms:** $H(j\omega)=1/(a+j\omega)\Rightarrow\omega_c=a$; but $H(j\omega)=1/(1+j\omega/\omega_c)$ already has $\omega_c$ explicit.
8. **Magnitude at $\omega_n$ confusion:** the standard second-order form gives $|H(j\omega_n)|=1/(2\zeta)$ (not 1). DC gain is 1.
9. **Resonance exists only if $\zeta<1/\sqrt{2}\approx 0.707$.** Smaller $\zeta$ = higher peak. Above $1/\sqrt2$ the magnitude is monotone.
10. **Time shift preserves $|a_k|$ and $|X|$** — only phase changes; power and energy unchanged.
11. **Cover-up method pitfall:** for FT partial fractions use the $j\omega$-domain variables; plug $j\omega=-a$ (not $s=-a$) when inverting to time with $e^{-at}u(t)$.
12. **Conjugate symmetry only applies to real signals.** Complex $x(t)$ does not satisfy $a_{-k}=a_k^*$.
13. **DC gain vs peak magnitude** in Bode plots: asymptote is $0$ dB at low frequency; the actual curve at a corner frequency differs (up to 3 dB for a first-order pole; the second-order deviation depends on $\zeta$).
14. **Hz vs rad/s:** $\omega=2\pi f$; formulas involving $\omega_c$ assume rad/s unless stated.
15. **Linear phase vs zero phase:** linear phase still gives distortion-free output (just delayed); zero phase is an idealization used in ideal filters.

---

*Prepared for CEC 315 Exam 2 — Spring 2026.*
