# CEC 315 — Exam 2 Sample Problems (Lectures 9–15)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Exam 2 — Lectures 9–15
**Source:** Worked examples from lecture PDFs, lecture summaries, and existing exam2 notes (`exam2_solutions.md`, `hw_lctr9_11_solutions_summary.md`, `hw_lctr12_15_solutions_summary.md`, `examples/hw_problem*.md`).

Each problem lists: statement, lecture reference, topic, concepts tested, full step-by-step solution.

---

## Table of Contents

- [Lecture 9 — CT Fourier Series](#lecture-9--ct-fourier-series)
- [Lecture 10 — Convergence, Gibbs, DTFS](#lecture-10--convergence-gibbs-dtfs)
- [Lecture 11 — Frequency Response and Filtering](#lecture-11--frequency-response-and-filtering)
- [Lecture 12 — Fourier Transforms](#lecture-12--fourier-transforms)
- [Lecture 13 — FT Properties and Convolution](#lecture-13--ft-properties-and-convolution)
- [Lecture 14 — Magnitude, Phase, and Ideal Filters](#lecture-14--magnitude-phase-and-ideal-filters)
- [Lecture 15 — First/Second-Order Systems and Bode](#lecture-15--firstsecond-order-systems-and-bode)

---

## Lecture 9 — CT Fourier Series

### Problem 9.1 — Eigenfunction Property
**Reference:** Lecture 9; `examples/hw_problem1_eigenfunction_fs_coefficients.md`.
**Topic:** Eigenfunctions of LTI systems.
**Concepts tested:** $H(j\omega)=\int h(\tau)e^{-j\omega\tau}d\tau$; frequency preservation.

**Statement.** Let $h(t)=e^{-4t}u(t)$ and $x(t)=\cos(3t)$. Find the output $y(t)$.

**Solution.**

**Step 1.** Because $h$ is causal,
$$H(j3)=\int_0^\infty e^{-4\tau}e^{-j3\tau}d\tau=\frac{1}{4+j3}.$$

**Step 2.** Convert to polar form:
$$|H(j3)|=\frac{1}{\sqrt{4^2+3^2}}=\frac{1}{5}=0.2,\quad \angle H(j3)=-\arctan(3/4)\approx-36.87°.$$

**Step 3.** By the eigenfunction property, $\cos(3t)$ passes through with the same frequency, scaled by $|H|$ and phase-shifted by $\angle H$:
$$\boxed{y(t)=0.2\cos(3t-36.87°).}$$

---

### Problem 9.2 — CTFS of a Pulse Train
**Reference:** Lecture 9; `examples/hw_problem1_eigenfunction_fs_coefficients.md`, Part (b).
**Topic:** Analysis integral for a rectangular-pulse periodic signal.
**Concepts tested:** Computing $a_k$ directly; DC value; integration only over nonzero intervals.

**Statement.** $x(t)$ is periodic with $T=4$, and on one period $x(t)=3$ for $0\le t<1$, $x(t)=0$ for $1\le t<4$. Find $\omega_0$, $a_0$, and $a_k$ for $k\ne 0$.

**Solution.**

**Step 1.** $\omega_0=2\pi/T=\pi/2$ rad/s.

**Step 2.** DC value:
$$a_0=\frac{1}{4}\int_0^1 3\,dt=\frac{3}{4}=0.75.$$

**Step 3.** For $k\ne 0$, integrate only where $x\ne 0$:
$$a_k=\frac{1}{4}\int_0^1 3 e^{-jk(\pi/2)t}dt=\frac{3}{4}\cdot\frac{1-e^{-jk\pi/2}}{jk\pi/2}=\frac{3}{2jk\pi}(1-e^{-jk\pi/2}).$$

**Step 4.** Check conjugate symmetry: $a_{-1}=\frac{3(1+j)}{2\pi}=a_1^*$. Holds for any real signal.

$$\boxed{\omega_0=\pi/2,\quad a_0=3/4,\quad a_k=\frac{3}{2jk\pi}(1-e^{-jk\pi/2}).}$$

---

### Problem 9.3 — Square Wave FS Coefficients
**Reference:** Lecture 9; `exam2_solutions.md`, Problem 1.
**Topic:** Odd-symmetric square wave.
**Concepts tested:** $a_0=0$ from symmetry; simplification $e^{-jk\pi}=(-1)^k$.

**Statement.** $x(t)$ is periodic with $T=2$, $x(t)=+1$ on $[0,1)$ and $x(t)=-1$ on $[1,2)$. Find $a_0$ and $a_k$ for $k\ne 0$.

**Solution.**

**Step 1.** $\omega_0=2\pi/T=\pi$, and the signed areas cancel over one period, so
$$a_0=\frac{1}{2}\left[\int_0^1 1\,dt+\int_1^2(-1)dt\right]=0.$$

**Step 2.** For $k\ne 0$:
$$a_k=\frac{1}{2}\left[\int_0^1 e^{-jk\pi t}dt-\int_1^2 e^{-jk\pi t}dt\right].$$

Evaluating each integral:
$$\int_0^1 e^{-jk\pi t}dt=\frac{1-e^{-jk\pi}}{jk\pi},\qquad -\int_1^2 e^{-jk\pi t}dt=\frac{e^{-j2k\pi}-e^{-jk\pi}}{jk\pi}=\frac{1-e^{-jk\pi}}{jk\pi}.$$

**Step 3.** Combine (both terms are equal):
$$a_k=\frac{1-e^{-jk\pi}}{jk\pi}=\frac{1-(-1)^k}{jk\pi}.$$

So $a_k=0$ for even $k$ and $a_k=2/(jk\pi)=-2j/(k\pi)$ for odd $k$.

**Step 4.** Verify power via Parseval:
$$P=\frac{1}{2}\int_0^2 1\,dt=1=\sum_k|a_k|^2=\frac{8}{\pi^2}\sum_{n=0}^\infty\frac{1}{(2n+1)^2}=\frac{8}{\pi^2}\cdot\frac{\pi^2}{8}=1.\ \checkmark$$

$$\boxed{a_0=0,\quad a_k=\frac{1-(-1)^k}{jk\pi}\text{ (nonzero for odd $k$).}}$$

---

## Lecture 10 — Convergence, Gibbs, DTFS

### Problem 10.1 — Convergence at a Discontinuity
**Reference:** Lecture 10; `examples/hw_problem2_convergence_gibbs.md`.
**Topic:** Dirichlet convergence at jumps.
**Concepts tested:** Value at a jump = midpoint of left/right limits.

**Statement.** Let $x(t)$ be an odd square wave on $[-\pi,\pi)$ with $x(t)=-1$ on $(-\pi,0)$ and $x(t)=+1$ on $(0,\pi)$. Find the value the Fourier series converges to at $t=0$ and $t=\pi/2$.

**Solution.**

**Step 1.** At $t=0$, a jump occurs: $x(0^-)=-1$, $x(0^+)=+1$. The FS converges to the midpoint:
$$x_\text{FS}(0)=\frac{-1+1}{2}=0.$$

**Step 2.** At $t=\pi/2$, $x$ is continuous, so $x_\text{FS}(\pi/2)=x(\pi/2)=+1$.

$$\boxed{x_\text{FS}(0)=0,\quad x_\text{FS}(\pi/2)=1.}$$

---

### Problem 10.2 — Gibbs Partial Sum
**Reference:** Lecture 10; `examples/hw_problem2_convergence_gibbs.md`, Part (c).
**Topic:** Gibbs overshoot in a 3-term partial sum.
**Concepts tested:** Square-wave coefficients $4/(k\pi)$ for odd $k$; overshoot ≈ 9%.

**Statement.** For the square wave above, compute the three-term partial sum $x_3(t)=(4/\pi)[\sin t+\sin(3t)/3+\sin(5t)/5]$ at $t=\pi/2$. Compare to the true value 1.

**Solution.**

**Step 1.** $\sin(\pi/2)=1$, $\sin(3\pi/2)=-1$, $\sin(5\pi/2)=1$, so
$$x_3(\pi/2)=\frac{4}{\pi}\left(1-\frac{1}{3}+\frac{1}{5}\right)=\frac{4}{\pi}\cdot\frac{13}{15}\approx 1.103.$$

**Step 2.** Percent overshoot relative to the jump height $|+1-(-1)|=2$:
$$\frac{1.103-1}{2}\times 100\%\approx 5.2\%\text{ for 3 terms}.$$

As $N$ increases, the overshoot approaches the asymptotic Gibbs value ≈ 9% of the jump height and does **not** vanish.

$$\boxed{x_3(\pi/2)\approx 1.103\text{ (approaches $\sim$9\% overshoot as $N\to\infty$).}}$$

---

### Problem 10.3 — DTFS of a Rectangular Pulse
**Reference:** Lecture 10; `examples/hw_problem4_dtfs.md`; `hw_lctr9_11_solutions_summary.md`, Problem 4.
**Topic:** DTFS analysis equation.
**Concepts tested:** Finite sum, periodicity $a_{k+N}=a_k$, Parseval.

**Statement.** $x[n]$ is periodic with $N=6$: one period is $x[0]=x[1]=x[2]=1$, $x[3]=x[4]=x[5]=0$. Find $a_0$, $a_1$, and verify Parseval.

**Solution.**

**Step 1.** $\omega_0=2\pi/6=\pi/3$, and
$$a_k=\frac{1}{6}\sum_{n=0}^5 x[n]e^{-jk(\pi/3)n}=\frac{1}{6}\sum_{n=0}^2 e^{-jk(\pi/3)n}.$$

**Step 2.** $a_0=\frac{1}{6}(1+1+1)=\frac{1}{2}$.

**Step 3.** $a_1=\frac{1}{6}(1+e^{-j\pi/3}+e^{-j2\pi/3})$.

Numerically:
$$e^{-j\pi/3}=\tfrac{1}{2}-j\tfrac{\sqrt 3}{2},\ e^{-j2\pi/3}=-\tfrac12-j\tfrac{\sqrt3}{2},$$
so $a_1=\frac{1}{6}(1+0-j\sqrt3)=\frac{1}{6}-j\frac{\sqrt3}{6}=\frac{1-j\sqrt3}{6}$.

**Step 4.** Parseval:
$$\frac{1}{6}\sum_{n=0}^5|x[n]|^2=\frac{3}{6}=\frac{1}{2}.$$

Summing $|a_k|^2$ over $k=0,\ldots,5$ gives $1/2$ as well (periodicity $a_{k+6}=a_k$).

$$\boxed{a_0=\tfrac12,\ a_1=\tfrac{1-j\sqrt3}{6},\ \text{Parseval: }1/2=1/2.\ \checkmark}$$

---

## Lecture 11 — Frequency Response and Filtering

### Problem 11.1 — LTI System with Multi-Tone Input
**Reference:** Lecture 11; `exam2_solutions.md`, Problem 3.
**Topic:** Frequency response of a first-order lowpass.
**Concepts tested:** Evaluating $H(j\omega)$ at multiple frequencies; recognizing lowpass behavior.

**Statement.** Let $h(t)=4e^{-4t}u(t)$ and $x(t)=3+2\cos(4t)+\cos(20t)$. Find $y(t)$.

**Solution.**

**Step 1.** $H(j\omega)=\dfrac{4}{4+j\omega}=\dfrac{1}{1+j\omega/4}$, so $\omega_c=4$ rad/s (−3 dB).

**Step 2.** Evaluate at the three input frequencies:

| $\omega$ | $H(j\omega)$ | $|H|$ | $\angle H$ |
|---|---|---|---|
| 0 | 1 | 1 | $0°$ |
| 4 | $\frac{1}{1+j}$ | $1/\sqrt2\approx 0.707$ | $-45°$ |
| 20 | $\frac{1}{1+j5}$ | $1/\sqrt{26}\approx 0.196$ | $-\arctan5\approx-78.69°$ |

**Step 3.** Apply $A\cos(\omega t+\phi)\to A|H|\cos(\omega t+\phi+\angle H)$:
$$\boxed{y(t)=3+\sqrt{2}\cos(4t-45°)+\frac{1}{\sqrt{26}}\cos(20t-78.69°).}$$

**Step 4.** Interpretation: $|H|$ decreases with $\omega$, so this is a **lowpass filter**. The ratio of output magnitudes $|H(j20)|/|H(j4)|=1/\sqrt{13}\approx 0.277$ ≈ $-11.14$ dB of relative attenuation.

---

### Problem 11.2 — RC Lowpass Cutoff
**Reference:** Lecture 11; `lctr11_frequency_response_filtering.md`.
**Topic:** First-order RC lowpass.
**Concepts tested:** Deriving $\omega_c$ from $H$.

**Statement.** Find the cutoff frequency of $H(j\omega)=1/(1+j\omega RC)$ with $R=10\,\text{k}\Omega$ and $C=1\,\mu\text{F}$.

**Solution.**

**Step 1.** Standard form $1/(1+j\omega/\omega_c)$, so $\omega_c=1/(RC)$.

**Step 2.** $\omega_c=1/(10^4\cdot 10^{-6})=100$ rad/s.

**Step 3.** $f_c=\omega_c/(2\pi)\approx 15.9$ Hz; at $\omega_c$, $|H|=1/\sqrt2$, $\angle H=-45°$.

$$\boxed{\omega_c=100\text{ rad/s},\ f_c\approx 15.9\text{ Hz}.}$$

---

## Lecture 12 — Fourier Transforms

### Problem 12.1 — One-Sided Exponential
**Reference:** Lecture 12; `hw_lctr12_15_solutions_summary.md`, Problem 1(a).
**Topic:** FT from definition.
**Concepts tested:** Integral from 0 to $\infty$; magnitude/phase; sanity check $X(0)=\int x\,dt$.

**Statement.** Compute $X(j\omega)$ for $x(t)=3e^{-5t}u(t)$, then give $|X|$ and $\angle X$.

**Solution.**

**Step 1.** $X(j\omega)=\int_0^\infty 3 e^{-5t}e^{-j\omega t}dt=\dfrac{3}{5+j\omega}$.

**Step 2.** $|X|=3/\sqrt{25+\omega^2}$, $\angle X=-\arctan(\omega/5)$.

**Step 3.** Sanity: $X(0)=3/5=0.6=\int_0^\infty 3e^{-5t}dt$. ✓

$$\boxed{X(j\omega)=\dfrac{3}{5+j\omega}.}$$

---

### Problem 12.2 — Two-Sided Exponential
**Reference:** Lecture 12; `hw_lctr12_15_solutions_summary.md`, Problem 1(b).
**Topic:** Real-even signal $\to$ real-even transform.
**Concepts tested:** Splitting integrals; recognizing $\text{FT}(e^{-a|t|})=2a/(a^2+\omega^2)$.

**Statement.** Compute $G(j\omega)$ for $g(t)=4e^{-2|t|}$.

**Solution.**

**Step 1.** Split at $t=0$:
$$G(j\omega)=4\int_0^\infty e^{-2t}e^{-j\omega t}dt+4\int_{-\infty}^0 e^{2t}e^{-j\omega t}dt=\frac{4}{2+j\omega}+\frac{4}{2-j\omega}.$$

**Step 2.** Combine:
$$G(j\omega)=\frac{4(2-j\omega)+4(2+j\omega)}{(2+j\omega)(2-j\omega)}=\frac{16}{4+\omega^2}.$$

**Step 3.** Purely real (real even $\Rightarrow$ real even transform, phase zero). Sanity: $G(0)=4$, matches $\int_{-\infty}^\infty 4 e^{-2|t|}dt=4$. ✓

$$\boxed{G(j\omega)=\dfrac{16}{4+\omega^2}.}$$

---

### Problem 12.3 — Rectangular Pulse
**Reference:** Lecture 12; `hw_lctr12_15_solutions_summary.md`, Problem 1(c).
**Topic:** rect $\to$ sinc.

**Statement.** $p(t)$ equals 2 on $|t|\le 3$ and 0 otherwise. Compute $P(j\omega)$.

**Solution.**

**Step 1.** $P(j\omega)=\int_{-3}^3 2 e^{-j\omega t}dt=2\left[\frac{e^{-j\omega t}}{-j\omega}\right]_{-3}^3=\frac{2(e^{j3\omega}-e^{-j3\omega})}{j\omega}=\frac{4\sin(3\omega)}{\omega}.$

**Step 2.** Sanity: $P(0)=12$ matches $\int 2\,dt=12$. First zero at $\omega=\pi/3$.

$$\boxed{P(j\omega)=\dfrac{4\sin(3\omega)}{\omega}=12\,\text{sinc}(3\omega/\pi).}$$

---

### Problem 12.4 — DTFT of Causal Exponential
**Reference:** Lecture 12; `hw_lctr12_15_solutions_summary.md`, Problem 2(a).
**Topic:** Geometric series for DTFT.

**Statement.** Compute $X(e^{j\omega})$ for $x[n]=(0.6)^n u[n]$.

**Solution.**

**Step 1.** $X(e^{j\omega})=\sum_{n=0}^\infty (0.6 e^{-j\omega})^n=\frac{1}{1-0.6 e^{-j\omega}}$, valid because $|0.6|<1$.

**Step 2.** DC and Nyquist: $X(e^{j0})=1/0.4=2.5$, $X(e^{j\pi})=1/1.6=0.625$. Larger at DC $\Rightarrow$ lowpass.

$$\boxed{X(e^{j\omega})=\dfrac{1}{1-0.6 e^{-j\omega}}.}$$

---

## Lecture 13 — FT Properties and Convolution

### Problem 13.1 — Time Shift
**Reference:** Lecture 13; `exam2_solutions.md`, Problem 2(a).
**Topic:** Time-shift property.

**Statement.** $x(t)=e^{-3t}u(t)$ with $X(j\omega)=1/(3+j\omega)$. Find $Y(j\omega)$ for $y(t)=e^{-3(t-4)}u(t-4)$.

**Solution.**

**Step 1.** Recognize $y(t)=x(t-4)$, $t_0=4$.

**Step 2.** Apply time-shift: $Y(j\omega)=e^{-j4\omega}X(j\omega)=\dfrac{e^{-j4\omega}}{3+j\omega}$.

**Step 3.** $|Y|=|X|$ (magnitude unchanged); only a linear phase $-4\omega$ is added.

$$\boxed{Y(j\omega)=\dfrac{e^{-j4\omega}}{3+j\omega}.}$$

---

### Problem 13.2 — Frequency Shift (Modulation)
**Reference:** Lecture 13; `exam2_solutions.md`, Problem 2(b).
**Topic:** Frequency shift via Euler.

**Statement.** For the same $x(t)$, let $z(t)=x(t)\cos(8t)$. Find $Z(j\omega)$.

**Solution.**

**Step 1.** $\cos(8t)=\frac{1}{2}(e^{j8t}+e^{-j8t})$.

**Step 2.** Apply the frequency-shift property to each term:
$$Z(j\omega)=\frac{1}{2}\left[\frac{1}{3+j(\omega-8)}+\frac{1}{3+j(\omega+8)}\right].$$

$$\boxed{Z(j\omega)=\tfrac12\left[\tfrac{1}{3+j(\omega-8)}+\tfrac{1}{3+j(\omega+8)}\right].}$$

---

### Problem 13.3 — Convolution via FT + Partial Fractions
**Reference:** Lecture 13; `exam2_solutions.md`, Problem 2(c)-(d).
**Topic:** Convolution property + PFE pipeline.
**Concepts tested:** Computing $Y=XH$, PFE, inverse FT.

**Statement.** $x(t)=e^{-3t}u(t)$, $h(t)=6e^{-5t}u(t)$. Find $y(t)=x*h$.

**Solution.**

**Step 1.** Transform: $X(j\omega)=\frac{1}{3+j\omega}$, $H(j\omega)=\frac{6}{5+j\omega}$.

**Step 2.** Multiply: $Y(j\omega)=\frac{6}{(3+j\omega)(5+j\omega)}$.

**Step 3.** PFE. Write $Y=\frac{A}{3+j\omega}+\frac{B}{5+j\omega}$; cover-up:
- At $j\omega=-3$: $A=6/(5-3)=3$.
- At $j\omega=-5$: $B=6/(3-5)=-3$.

So $Y(j\omega)=\frac{3}{3+j\omega}-\frac{3}{5+j\omega}$.

**Step 4.** Inverse-transform each term with $e^{-at}u(t)\leftrightarrow 1/(a+j\omega)$:
$$\boxed{y(t)=3(e^{-3t}-e^{-5t})u(t).}$$

**Step 5.** Verify $y(0)=0$ ✓; $\lim_{t\to\infty}y(t)=0$ ✓.

---

### Problem 13.4 — CT System from an ODE
**Reference:** Lecture 13; `hw_lctr12_15_solutions_summary.md`, Problem 4(a).
**Topic:** $d^k/dt^k\to(j\omega)^k$.
**Concepts tested:** Converting ODE to $H(j\omega)$, stability check via poles.

**Statement.** Find $H(j\omega)$ and $h(t)$ for $y''+7y'+10y=3x$. Classify the filter.

**Solution.**

**Step 1.** Replace derivatives:
$$[(j\omega)^2+7(j\omega)+10]Y(j\omega)=3X(j\omega)\Rightarrow H(j\omega)=\frac{3}{(j\omega)^2+7(j\omega)+10}=\frac{3}{(j\omega+2)(j\omega+5)}.$$

Poles at $j\omega=-2,-5$, both in LHP $\Rightarrow$ stable.

**Step 2.** PFE:
$$H=\frac{A}{j\omega+2}+\frac{B}{j\omega+5},\quad A=3/3=1,\ B=3/(-3)=-1.$$

**Step 3.** Inverse transform:
$$h(t)=(e^{-2t}-e^{-5t})u(t).$$

**Step 4.** DC gain $|H(0)|=3/10=0.3$; decreasing with $\omega$ $\Rightarrow$ lowpass.

$$\boxed{H(j\omega)=\dfrac{3}{(j\omega+2)(j\omega+5)},\ h(t)=(e^{-2t}-e^{-5t})u(t).}$$

---

## Lecture 14 — Magnitude, Phase, and Ideal Filters

### Problem 14.1 — Magnitude, Phase, Group Delay
**Reference:** Lecture 14; `hw_lctr12_15_solutions_summary.md`, Problem 5.
**Topic:** Polar form and group delay.
**Concepts tested:** $|H|$, $\angle H$ at sample frequencies; $\tau=-d\angle H/d\omega$.

**Statement.** $H(j\omega)=1/(1+j\omega/5)$. Compute $|H|$ and $\angle H$ at $\omega=0,1,5,10,50$; find the group delay $\tau(\omega)$.

**Solution.**

**Step 1.** $|H(j\omega)|=1/\sqrt{1+\omega^2/25}$, $\angle H(j\omega)=-\arctan(\omega/5)$.

**Step 2.** Values:

| $\omega$ | $|H|$ | dB | $\angle H$ |
|---|---|---|---|
| 0 | 1 | 0 | $0°$ |
| 1 | 0.981 | −0.17 | $-11.3°$ |
| 5 | 0.707 | −3.01 | $-45°$ |
| 10 | 0.447 | −6.99 | $-63.4°$ |
| 50 | 0.0995 | −20.04 | $-84.3°$ |

**Step 3.** Group delay:
$$\tau(\omega)=-\frac{d}{d\omega}(-\arctan(\omega/5))=\frac{1/5}{1+(\omega/5)^2}=\frac{5}{25+\omega^2}.$$

$\tau(0)=0.2$ s, $\tau(5)=0.1$ s. Not constant $\Rightarrow$ nonlinear phase; mild phase distortion.

$$\boxed{\tau(\omega)=\dfrac{5}{25+\omega^2}.}$$

---

### Problem 14.2 — Ideal Lowpass Impulse Response
**Reference:** Lecture 14; `lctr14_magnitude_phase_filters.md`.
**Topic:** Inverse FT of a rectangular $H(j\omega)$.
**Concepts tested:** Duality / sinc; noncausality of ideal filters.

**Statement.** Find the impulse response $h(t)$ of an ideal LPF with cutoff $\omega_c$, $H(j\omega)=1$ on $|\omega|\le\omega_c$ and 0 otherwise.

**Solution.**

**Step 1.** Inverse FT:
$$h(t)=\frac{1}{2\pi}\int_{-\omega_c}^{\omega_c}e^{j\omega t}d\omega=\frac{1}{2\pi}\cdot\frac{e^{j\omega_c t}-e^{-j\omega_c t}}{jt}=\frac{\sin(\omega_c t)}{\pi t}.$$

**Step 2.** Observation: $h(t)\ne 0$ for $t<0$, so the ideal LPF is **noncausal** and hence physically unrealizable.

$$\boxed{h(t)=\dfrac{\sin(\omega_c t)}{\pi t}=\dfrac{\omega_c}{\pi}\text{sinc}\!\left(\dfrac{\omega_c t}{\pi}\right).}$$

---

## Lecture 15 — First/Second-Order Systems and Bode

### Problem 15.1 — First-Order Bode Plot
**Reference:** Lecture 15; `lctr15_systems_bode.md`.
**Topic:** First-order LP Bode asymptotes.

**Statement.** Sketch the Bode magnitude asymptote of $H(j\omega)=1/(1+j\omega/10)$ and give the phase at $\omega=1,10,100$.

**Solution.**

**Step 1.** DC gain 1 (0 dB). Corner at $\omega_c=10$. Below $\omega_c$: 0 dB flat. Above $\omega_c$: $-20$ dB/decade.

**Step 2.** Magnitude asymptote levels:
- At $\omega=10$: 0 dB (asymptote); actual $-3$ dB.
- At $\omega=100$: $-20$ dB.
- At $\omega=1000$: $-40$ dB.

**Step 3.** Phase: $\angle H=-\arctan(\omega/10)$.
- $\omega=1$: $-5.7°$ (≈ $0°$).
- $\omega=10$: $-45°$.
- $\omega=100$: $-84.3°$ (≈ $-90°$).

$$\boxed{\text{0 dB flat to }\omega_c=10,\ \text{then }-20\text{ dB/dec; phase }0°\to-45°@\omega_c\to-90°.}$$

---

### Problem 15.2 — Second-Order System Analysis
**Reference:** Lecture 15; `exam2_solutions.md`, Problem 4.
**Topic:** Standard second-order form; classification; Bode; step response.
**Concepts tested:** Computing $\omega_n$, $\zeta$, resonance, %OS, $t_s$, corner frequency.

**Statement.** $H(j\omega)=\dfrac{100}{(j\omega)^2+10(j\omega)+100}$. Classify, compute DC gain, $|H(j\omega_n)|$, resonance, %OS, $t_s$, and Bode asymptotes.

**Solution.**

**Step 1.** Match standard form $\omega_n^2/[(j\omega)^2+2\zeta\omega_n(j\omega)+\omega_n^2]$:
$$\omega_n^2=100\Rightarrow\omega_n=10,\ 2\zeta\omega_n=10\Rightarrow\zeta=0.5.$$

**Step 2.** $\zeta=0.5<1$ $\Rightarrow$ **underdamped** (complex poles). Since $\zeta<1/\sqrt2\approx0.707$, a resonance peak exists:
$$\omega_r=\omega_n\sqrt{1-2\zeta^2}=10\sqrt{0.5}\approx 7.07\text{ rad/s}.$$

**Step 3.** DC gain: $|H(0)|=100/100=1$ (0 dB). At $\omega_n$:
$$H(j10)=\frac{100}{-100+j100+100}=\frac{100}{j100}=-j,\ |H(j10)|=1,\ \angle H=-90°.$$

Consistent with $|H(j\omega_n)|=1/(2\zeta)=1$.

**Step 4.** Peak magnitude:
$$|H|_\max=\frac{1}{2\zeta\sqrt{1-\zeta^2}}=\frac{1}{2(0.5)\sqrt{0.75}}=\frac{2}{\sqrt3}\approx 1.155\ (\approx 1.25\text{ dB}).$$

**Step 5.** Step-response metrics:
$$\%\text{OS}=100 e^{-\pi(0.5)/\sqrt{0.75}}\approx 16.3\%,\quad t_s\approx\frac{4}{0.5\cdot 10}=0.8\text{ s}.$$

**Step 6.** Bode asymptotes: 0 dB flat below $\omega_n=10$, then $-40$ dB/dec. Phase: $0°\to-90°$ at $\omega_n\to-180°$.

$$\boxed{\omega_n=10,\ \zeta=0.5,\ \omega_r\approx 7.07,\ \%\text{OS}\approx 16.3\%,\ t_s=0.8\text{ s},\ \text{HF slope }-40\text{ dB/dec}.}$$

---

### Problem 15.3 — Cascade of Two First-Order Sections
**Reference:** Lecture 15; `lctr15_systems_bode.md` (Bode cascade rule).
**Topic:** Cascading Bode plots.

**Statement.** Sketch the Bode magnitude asymptote of $H(j\omega)=\dfrac{1}{(1+j\omega)(1+j\omega/100)}$.

**Solution.**

**Step 1.** Two poles at $\omega=1$ and $\omega=100$. DC gain 1 (0 dB).

**Step 2.** Magnitude asymptotes:
- $\omega<1$: 0 dB (flat).
- $1<\omega<100$: $-20$ dB/dec (one pole active).
- $\omega>100$: $-40$ dB/dec (both poles active).

**Step 3.** Phase: starts at $0°$; by $\omega=1000$ approaches $-180°$. Each pole contributes $-90°$ above its corner by a factor of 10.

$$\boxed{\text{Asymptotes: 0 dB, then $-20$ dB/dec at $\omega=1$, then $-40$ dB/dec at $\omega=100$.}}$$

---

*Prepared for CEC 315 Exam 2 — Spring 2026.*
