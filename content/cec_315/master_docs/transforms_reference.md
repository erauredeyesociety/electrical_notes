# CEC 315 — Master Transforms Reference

**Comprehensive reference for all transforms and properties covered in CEC 315 (Signals and Systems), with emphasis on Exam 3 material (Laplace, $z$-transform, sampling).**

Notation: $u(t)$ = unit step, $u[n]$ = DT unit step, $\delta(t)$ = CT impulse, $\delta[n]$ = Kronecker delta, ROC = region of convergence. All transforms listed with the bilateral convention except where unilateral is explicitly indicated.

---

## Table of Contents

1. [CT Fourier Series (CTFS)](#section-1-ct-fourier-series-ctfs)
2. [DT Fourier Series (DTFS)](#section-2-dt-fourier-series-dtfs)
3. [CT Fourier Transform (CTFT)](#section-3-ct-fourier-transform-ctft)
4. [DT Fourier Transform (DTFT)](#section-4-dt-fourier-transform-dtft)
5. [Laplace Transform (Bilateral and Unilateral)](#section-5-laplace-transform)
6. [$z$-Transform (Bilateral and Unilateral)](#section-6-z-transform)
7. [Connections Between Transforms](#section-7-connections-between-transforms)
8. [PFE Cookbook (Partial Fraction Expansion)](#section-8-pfe-cookbook-partial-fraction-expansion)
9. [Common Signal Definitions](#section-9-common-signal-definitions)
10. [Sampling and Reconstruction](#section-10-sampling-and-reconstruction)
11. [Feedback Systems](#section-11-feedback-systems)

---

## Section 1: CT Fourier Series (CTFS)

### 1.1 Definition (periodic $x(t)$ with period $T$, $\omega_0 = 2\pi/T$)

**Synthesis (frequency $\to$ time):**

$$x(t) = \sum_{k=-\infty}^{\infty} a_k \, e^{jk\omega_0 t}$$

**Analysis (time $\to$ frequency):**

$$a_k = \frac{1}{T}\int_{T} x(t)\, e^{-jk\omega_0 t}\, dt \qquad a_0 = \frac{1}{T}\int_T x(t)\,dt\ (\text{DC average})$$

### 1.2 Common CTFS Pairs

| Signal $x(t)$ (period $T$) | $a_k$ |
|---|---|
| $1$ (DC) | $a_0 = 1$, $a_k = 0$ for $k \ne 0$ |
| $\cos(\omega_0 t)$ | $a_1 = a_{-1} = \tfrac{1}{2}$, else $0$ |
| $\sin(\omega_0 t)$ | $a_1 = \tfrac{1}{2j}$, $a_{-1} = -\tfrac{1}{2j}$, else $0$ |
| $e^{jN\omega_0 t}$ | $a_N = 1$, else $0$ |
| Square wave (amp $\pm 1$, duty 50%) | $a_k = \dfrac{2}{jk\pi}$, $k$ odd; $0$ for $k$ even |
| Impulse train $\sum_n \delta(t - nT)$ | $a_k = \dfrac{1}{T}$ for all $k$ |
| Rect pulse width $2T_1$ in period $T$ | $a_k = \dfrac{\sin(k\omega_0 T_1)}{k\pi} = \dfrac{2 T_1}{T}\,\mathrm{sinc}\!\left(\tfrac{k\omega_0 T_1}{\pi}\right)$ |

### 1.3 CTFS Properties

| Property | Time domain | FS coefficients |
|---|---|---|
| Linearity | $A x(t) + B y(t)$ | $A a_k + B b_k$ |
| Time shift | $x(t - t_0)$ | $a_k\, e^{-jk\omega_0 t_0}$ |
| Frequency shift | $e^{jM\omega_0 t} x(t)$ | $a_{k-M}$ |
| Conjugation | $x^*(t)$ | $a_{-k}^*$ |
| Time reversal | $x(-t)$ | $a_{-k}$ |
| Time scaling | $x(\alpha t)$ (period $T/\alpha$) | $a_k$ unchanged; $\omega_0 \to \alpha\omega_0$ |
| Multiplication | $x(t)\, y(t)$ | $\sum_{\ell} a_\ell\, b_{k-\ell}$ (discrete convolution) |
| Periodic convolution | $\int_T x(\tau) y(t - \tau)\, d\tau$ | $T\, a_k\, b_k$ |
| Differentiation | $dx/dt$ | $jk\omega_0\, a_k$ |
| Integration (if $a_0 = 0$) | $\int_{-\infty}^t x(\tau)\,d\tau$ | $\dfrac{a_k}{jk\omega_0}$ |
| Real $x(t)$ symmetry | $x(t)$ real | $a_{-k} = a_k^*$ |
| Real, even $x(t)$ | even | $a_k$ real and even |
| Real, odd $x(t)$ | odd | $a_k$ purely imaginary and odd |

### 1.4 Parseval's Relation for CTFS

$$\frac{1}{T}\int_T |x(t)|^2\,dt = \sum_{k=-\infty}^{\infty} |a_k|^2$$

Average power equals the sum of power in every harmonic.

### 1.5 Dirichlet Conditions

For convergence: absolutely integrable over one period, finite number of maxima/minima per period, finite number of finite jump discontinuities per period. At jumps, the series converges to the midpoint $\tfrac{1}{2}[x(t_0^-) + x(t_0^+)]$. Gibbs overshoot is ~9% regardless of $N$.

---

## Section 2: DT Fourier Series (DTFS)

### 2.1 Definition (periodic $x[n]$ with period $N$, $\omega_0 = 2\pi/N$)

**Synthesis:**

$$x[n] = \sum_{k=\langle N\rangle} a_k\, e^{jk(2\pi/N)n}$$

**Analysis:**

$$a_k = \frac{1}{N}\sum_{n=\langle N\rangle} x[n]\, e^{-jk(2\pi/N)n}$$

Coefficients are themselves periodic with period $N$: $a_{k+N} = a_k$. Only $N$ distinct coefficients exist.

### 2.2 Common DTFS Pairs

| $x[n]$ | $a_k$ (one period of length $N$) |
|---|---|
| $1$ | $a_0 = 1$, $a_k = 0$ otherwise |
| $e^{jM(2\pi/N) n}$ | $a_M = 1$ (mod $N$), else $0$ |
| $\cos\bigl((2\pi/N) M n\bigr)$ | $a_M = a_{-M} = \tfrac{1}{2}$ |
| $\sin\bigl((2\pi/N) M n\bigr)$ | $a_M = \tfrac{1}{2j}$, $a_{-M} = -\tfrac{1}{2j}$ |
| Impulse train $\sum_r \delta[n - rN]$ | $a_k = \tfrac{1}{N}$ all $k$ |

### 2.3 DTFS Properties

| Property | Sequence | Coefficients |
|---|---|---|
| Linearity | $A x[n] + B y[n]$ | $A a_k + B b_k$ |
| Time shift | $x[n - n_0]$ | $a_k\, e^{-jk(2\pi/N)n_0}$ |
| Frequency shift | $e^{jM(2\pi/N)n} x[n]$ | $a_{k-M}$ |
| Conjugation | $x^*[n]$ | $a_{-k}^*$ |
| Time reversal | $x[-n]$ | $a_{-k}$ |
| Multiplication | $x[n]\,y[n]$ | $\sum_{\ell=\langle N\rangle} a_\ell\, b_{k-\ell}$ (periodic conv.) |
| Periodic convolution | $\sum_{r=\langle N\rangle} x[r] y[n-r]$ | $N\, a_k\, b_k$ |
| First difference | $x[n] - x[n-1]$ | $(1 - e^{-jk(2\pi/N)}) a_k$ |
| Real $x[n]$ | — | $a_{-k} = a_k^*$ |

### 2.4 Parseval's Relation for DTFS

$$\frac{1}{N}\sum_{n=\langle N\rangle} |x[n]|^2 = \sum_{k=\langle N\rangle} |a_k|^2$$

---

## Section 3: CT Fourier Transform (CTFT)

### 3.1 Definition

**Analysis (forward):**

$$X(j\omega) = \int_{-\infty}^{\infty} x(t)\, e^{-j\omega t}\, dt$$

**Synthesis (inverse):**

$$x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(j\omega)\, e^{j\omega t}\, d\omega$$

### 3.2 Common CTFT Pairs

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $\delta(t)$ | $1$ |
| $\delta(t - t_0)$ | $e^{-j\omega t_0}$ |
| $1$ | $2\pi\,\delta(\omega)$ |
| $u(t)$ | $\dfrac{1}{j\omega} + \pi\,\delta(\omega)$ |
| $\mathrm{sgn}(t)$ | $\dfrac{2}{j\omega}$ |
| $e^{-at}u(t),\ \Re\{a\}>0$ | $\dfrac{1}{a + j\omega}$ |
| $t\,e^{-at}u(t),\ \Re\{a\}>0$ | $\dfrac{1}{(a + j\omega)^2}$ |
| $e^{-a|t|},\ a > 0$ | $\dfrac{2a}{a^2 + \omega^2}$ |
| $e^{j\omega_0 t}$ | $2\pi\,\delta(\omega - \omega_0)$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega - \omega_0) + \delta(\omega + \omega_0)]$ |
| $\sin(\omega_0 t)$ | $\dfrac{\pi}{j}[\delta(\omega - \omega_0) - \delta(\omega + \omega_0)]$ |
| Rect pulse: $1$ for $|t|<T_1$ | $\dfrac{2\sin(\omega T_1)}{\omega} = 2T_1\,\mathrm{sinc}\!\left(\tfrac{\omega T_1}{\pi}\right)$ |
| $\dfrac{\sin(Wt)}{\pi t}$ (ideal LPF) | $1$ for $|\omega|<W$, $0$ else |
| Triangular pulse width $2T_1$ | $T_1\,\mathrm{sinc}^2\!\left(\tfrac{\omega T_1}{2\pi}\right)$ |
| $e^{-t^2/(2\sigma^2)}$ (Gaussian) | $\sigma\sqrt{2\pi}\, e^{-\sigma^2\omega^2/2}$ |
| Impulse train $\sum_n \delta(t - nT)$ | $\dfrac{2\pi}{T}\sum_k \delta(\omega - k\tfrac{2\pi}{T})$ |
| Periodic $x(t) = \sum a_k e^{jk\omega_0 t}$ | $\sum_k 2\pi a_k\,\delta(\omega - k\omega_0)$ |

### 3.3 CTFT Properties

| Property | Time | Frequency |
|---|---|---|
| Linearity | $a x(t) + b y(t)$ | $a X(j\omega) + b Y(j\omega)$ |
| Time shift | $x(t - t_0)$ | $e^{-j\omega t_0}\, X(j\omega)$ |
| Frequency shift | $e^{j\omega_0 t} x(t)$ | $X(j(\omega - \omega_0))$ |
| Conjugation | $x^*(t)$ | $X^*(-j\omega)$ |
| Time reversal | $x(-t)$ | $X(-j\omega)$ |
| Time scaling | $x(\alpha t)$ | $\dfrac{1}{|\alpha|} X\!\left(\dfrac{j\omega}{\alpha}\right)$ |
| Duality | $X(jt)$ | $2\pi\, x(-\omega)$ |
| Differentiation in $t$ | $\dfrac{d^n x}{dt^n}$ | $(j\omega)^n X(j\omega)$ |
| Differentiation in $\omega$ | $-jt\, x(t)$ | $\dfrac{d}{d\omega} X(j\omega)$ |
| Integration | $\displaystyle\int_{-\infty}^t x(\tau)\,d\tau$ | $\dfrac{1}{j\omega} X(j\omega) + \pi X(0)\,\delta(\omega)$ |
| Convolution | $x(t) * y(t)$ | $X(j\omega)\, Y(j\omega)$ |
| Multiplication | $x(t)\, y(t)$ | $\dfrac{1}{2\pi}\, X(j\omega) * Y(j\omega)$ |
| Parseval | $\displaystyle\int |x(t)|^2 dt$ | $= \dfrac{1}{2\pi}\displaystyle\int |X(j\omega)|^2 d\omega$ |
| Real $x(t)$ | — | $X(-j\omega) = X^*(j\omega)$; $\|X\|$ even, $\angle X$ odd |

---

## Section 4: DT Fourier Transform (DTFT)

### 4.1 Definition

**Analysis:**

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n]\, e^{-j\omega n}$$

**Synthesis:**

$$x[n] = \frac{1}{2\pi}\int_{2\pi} X(e^{j\omega})\, e^{j\omega n}\, d\omega$$

$X(e^{j\omega})$ is always periodic in $\omega$ with period $2\pi$.

### 4.2 Common DTFT Pairs

| $x[n]$ | $X(e^{j\omega})$ |
|---|---|
| $\delta[n]$ | $1$ |
| $\delta[n - n_0]$ | $e^{-j\omega n_0}$ |
| $1$ | $2\pi\sum_k \delta(\omega - 2\pi k)$ |
| $u[n]$ | $\dfrac{1}{1 - e^{-j\omega}} + \sum_k \pi\delta(\omega - 2\pi k)$ |
| $a^n u[n],\ |a|<1$ | $\dfrac{1}{1 - a e^{-j\omega}}$ |
| $(n+1) a^n u[n],\ |a|<1$ | $\dfrac{1}{(1 - a e^{-j\omega})^2}$ |
| $a^{|n|},\ |a|<1$ | $\dfrac{1 - a^2}{1 - 2a\cos\omega + a^2}$ |
| $e^{j\omega_0 n}$ | $2\pi\sum_k \delta(\omega - \omega_0 - 2\pi k)$ |
| $\cos(\omega_0 n)$ | $\pi\sum_k[\delta(\omega - \omega_0 - 2\pi k) + \delta(\omega + \omega_0 - 2\pi k)]$ |
| Rect $x[n] = 1$ for $|n|\le N_1$ | $\dfrac{\sin[\omega(N_1 + 1/2)]}{\sin(\omega/2)}$ |
| $\dfrac{\sin(W n)}{\pi n}$ | $1$ for $|\omega|<W$ (in $[-\pi,\pi]$), else $0$ |

### 4.3 DTFT Properties

| Property | Sequence | Transform |
|---|---|---|
| Linearity | $a x[n] + b y[n]$ | $a X(e^{j\omega}) + b Y(e^{j\omega})$ |
| Time shift | $x[n - n_0]$ | $e^{-j\omega n_0} X(e^{j\omega})$ |
| Frequency shift | $e^{j\omega_0 n} x[n]$ | $X(e^{j(\omega - \omega_0)})$ |
| Conjugation | $x^*[n]$ | $X^*(e^{-j\omega})$ |
| Time reversal | $x[-n]$ | $X(e^{-j\omega})$ |
| Upsample by $k$ | $x_{(k)}[n]$ (zeros between) | $X(e^{jk\omega})$ |
| Convolution | $x[n]*y[n]$ | $X(e^{j\omega}) Y(e^{j\omega})$ |
| Multiplication | $x[n] y[n]$ | $\dfrac{1}{2\pi}\int_{2\pi} X(e^{j\theta}) Y(e^{j(\omega-\theta)})\,d\theta$ |
| Differencing | $x[n] - x[n-1]$ | $(1 - e^{-j\omega}) X(e^{j\omega})$ |
| Accumulation | $\sum_{m=-\infty}^n x[m]$ | $\dfrac{X(e^{j\omega})}{1 - e^{-j\omega}} + \pi X(e^{j0})\sum_k \delta(\omega - 2\pi k)$ |
| Frequency differentiation | $n x[n]$ | $j\dfrac{d}{d\omega} X(e^{j\omega})$ |
| Parseval | $\sum_n |x[n]|^2$ | $=\dfrac{1}{2\pi}\int_{2\pi}|X(e^{j\omega})|^2 d\omega$ |
| Real $x[n]$ | — | $X(e^{-j\omega}) = X^*(e^{j\omega})$ |

---

## Section 5: Laplace Transform

### 5.1 Definitions

**Bilateral:**

$$X(s) = \int_{-\infty}^{\infty} x(t)\, e^{-st}\,dt, \qquad s = \sigma + j\omega$$

**Unilateral:**

$$\mathcal{X}(s) = \int_{0^-}^{\infty} x(t)\, e^{-st}\,dt$$

**Inverse (formal):**

$$x(t) = \frac{1}{2\pi j}\int_{\sigma - j\infty}^{\sigma + j\infty} X(s)\, e^{st}\,ds \quad(\sigma \in \text{ROC})$$

In practice, invert via **partial fraction expansion** (Section 8).

### 5.2 Common Laplace Pairs

| $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $\delta(t - t_0)$ | $e^{-s t_0}$ | all $s$ |
| $u(t)$ | $\dfrac{1}{s}$ | $\Re\{s\} > 0$ |
| $-u(-t)$ | $\dfrac{1}{s}$ | $\Re\{s\} < 0$ |
| $t\, u(t)$ | $\dfrac{1}{s^2}$ | $\Re\{s\} > 0$ |
| $\dfrac{t^{n-1}}{(n-1)!}\,u(t)$ | $\dfrac{1}{s^n}$ | $\Re\{s\} > 0$ |
| $e^{-at}u(t)$ | $\dfrac{1}{s+a}$ | $\Re\{s\} > -\Re\{a\}$ |
| $-e^{-at}u(-t)$ | $\dfrac{1}{s+a}$ | $\Re\{s\} < -\Re\{a\}$ |
| $t\, e^{-at}u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\Re\{s\} > -\Re\{a\}$ |
| $\dfrac{t^{n-1}}{(n-1)!}\,e^{-at}u(t)$ | $\dfrac{1}{(s+a)^n}$ | $\Re\{s\} > -\Re\{a\}$ |
| $\cos(\omega_0 t)\,u(t)$ | $\dfrac{s}{s^2 + \omega_0^2}$ | $\Re\{s\} > 0$ |
| $\sin(\omega_0 t)\,u(t)$ | $\dfrac{\omega_0}{s^2 + \omega_0^2}$ | $\Re\{s\} > 0$ |
| $e^{-at}\cos(\omega_d t)\,u(t)$ | $\dfrac{s+a}{(s+a)^2 + \omega_d^2}$ | $\Re\{s\} > -a$ |
| $e^{-at}\sin(\omega_d t)\,u(t)$ | $\dfrac{\omega_d}{(s+a)^2 + \omega_d^2}$ | $\Re\{s\} > -a$ |
| $t\cos(\omega_0 t)\,u(t)$ | $\dfrac{s^2 - \omega_0^2}{(s^2 + \omega_0^2)^2}$ | $\Re\{s\} > 0$ |
| $t\sin(\omega_0 t)\,u(t)$ | $\dfrac{2\omega_0 s}{(s^2 + \omega_0^2)^2}$ | $\Re\{s\} > 0$ |
| $\cosh(at)\,u(t)$ | $\dfrac{s}{s^2 - a^2}$ | $\Re\{s\} > |a|$ |
| $\sinh(at)\,u(t)$ | $\dfrac{a}{s^2 - a^2}$ | $\Re\{s\} > |a|$ |

### 5.3 Laplace Properties (Bilateral)

Let $x(t)\leftrightarrow X(s)$ with ROC $R_x$.

| Property | Time | $s$-domain / ROC |
|---|---|---|
| Linearity | $a x(t) + b y(t)$ | $a X(s) + b Y(s)$, ROC $\supseteq R_x \cap R_y$ |
| Time shift | $x(t - t_0)$ | $e^{-s t_0} X(s)$, ROC $= R_x$ |
| $s$-shift | $e^{s_0 t} x(t)$ | $X(s - s_0)$, ROC $= R_x + \Re\{s_0\}$ |
| Time scaling | $x(\alpha t)$, $\alpha\ne 0$ | $\dfrac{1}{|\alpha|} X\!\left(\dfrac{s}{\alpha}\right)$, ROC $= \alpha R_x$ |
| Conjugation | $x^*(t)$ | $X^*(s^*)$, ROC $= R_x$ |
| Time reversal | $x(-t)$ | $X(-s)$, ROC $= -R_x$ |
| Convolution | $x(t) * y(t)$ | $X(s)\, Y(s)$, ROC $\supseteq R_x \cap R_y$ |
| Differentiation in $t$ | $\dfrac{dx}{dt}$ | $s X(s)$, ROC $\supseteq R_x$ |
| $n$-th derivative | $\dfrac{d^n x}{dt^n}$ | $s^n X(s)$, ROC $\supseteq R_x$ |
| Differentiation in $s$ | $-t\, x(t)$ | $\dfrac{d}{ds} X(s)$, ROC $= R_x$ |
| Integration | $\displaystyle\int_{-\infty}^t x(\tau)\,d\tau$ | $\dfrac{1}{s} X(s)$, ROC $\supseteq R_x \cap \{\Re\{s\}>0\}$ |

**Initial-Value Theorem** (causal $x$, no impulse at $0$):

$$x(0^+) = \lim_{s\to\infty} s\, X(s)$$

**Final-Value Theorem** (all poles of $sX(s)$ in open LHP):

$$\lim_{t\to\infty} x(t) = \lim_{s\to 0} s\, X(s)$$

### 5.4 Unilateral Laplace: Differentiation Property (incorporates ICs)

$$\frac{dx}{dt}\ \xleftrightarrow{\mathcal{L}_u}\ s\mathcal{X}(s) - x(0^-)$$

$$\frac{d^2 x}{dt^2}\ \xleftrightarrow{\mathcal{L}_u}\ s^2\mathcal{X}(s) - s x(0^-) - x'(0^-)$$

$$\frac{d^n x}{dt^n}\ \xleftrightarrow{\mathcal{L}_u}\ s^n\mathcal{X}(s) - \sum_{k=0}^{n-1} s^{n-1-k} x^{(k)}(0^-)$$

**Total response decomposition:** $y(t) = y_{\text{ZS}}(t) + y_{\text{ZI}}(t)$ where ZSR comes from $H(s)X(s)$ (zero ICs) and ZIR comes from ICs alone (zero input).

### 5.5 ROC Rules (bilateral)

1. ROC is a union of strips parallel to the $j\omega$-axis.
2. ROC never contains a pole.
3. Finite-duration $x(t)$: ROC is entire $s$-plane (possibly excluding $\infty$).
4. **Right-sided** signal, rational $X(s)$: ROC is $\Re\{s\} > \sigma_{\max}$ (right of rightmost pole).
5. **Left-sided** signal: ROC is $\Re\{s\} < \sigma_{\min}$ (left of leftmost pole).
6. **Two-sided** signal: ROC is a vertical strip between two consecutive poles (or empty).
7. ROC includes $j\omega$-axis $\iff$ Fourier transform exists and $X(j\omega) = X(s)|_{s=j\omega}$.

**Causal + BIBO stable** (rational, causal system) $\iff$ all poles have $\Re\{p_i\} < 0$ (open LHP).

---

## Section 6: $z$-Transform

### 6.1 Definitions

**Bilateral:**

$$X(z) = \sum_{n=-\infty}^{\infty} x[n]\, z^{-n}, \qquad z = r e^{j\omega}$$

**Unilateral:**

$$\mathcal{X}(z) = \sum_{n=0}^{\infty} x[n]\, z^{-n}$$

**Inverse (formal):**

$$x[n] = \frac{1}{2\pi j}\oint_C X(z)\, z^{n-1}\, dz$$

In practice: partial fractions in $z^{-1}$, then look up each term in the table and use the ROC to assign right-sided ($|z|>|d|$) vs. left-sided ($|z|<|d|$).

### 6.2 Common $z$-Transform Pairs

| $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n - k],\ k\ge 0$ | $z^{-k}$ | $|z| > 0$ |
| $\delta[n + k],\ k > 0$ | $z^{k}$ | $|z| < \infty$ |
| $u[n]$ | $\dfrac{1}{1 - z^{-1}} = \dfrac{z}{z-1}$ | $|z| > 1$ |
| $-u[-n-1]$ | $\dfrac{1}{1 - z^{-1}}$ | $|z| < 1$ |
| $a^n u[n]$ | $\dfrac{1}{1 - a z^{-1}} = \dfrac{z}{z - a}$ | $|z| > |a|$ |
| $-a^n u[-n-1]$ | $\dfrac{1}{1 - a z^{-1}}$ | $|z| < |a|$ |
| $n\, a^n u[n]$ | $\dfrac{a z^{-1}}{(1 - a z^{-1})^2}$ | $|z| > |a|$ |
| $(n+1)\, a^n u[n]$ | $\dfrac{1}{(1 - a z^{-1})^2}$ | $|z| > |a|$ |
| $-n a^n u[-n-1]$ | $\dfrac{a z^{-1}}{(1 - a z^{-1})^2}$ | $|z| < |a|$ |
| $\cos(\omega_0 n)\,u[n]$ | $\dfrac{1 - \cos\omega_0\, z^{-1}}{1 - 2\cos\omega_0\, z^{-1} + z^{-2}}$ | $|z| > 1$ |
| $\sin(\omega_0 n)\,u[n]$ | $\dfrac{\sin\omega_0\, z^{-1}}{1 - 2\cos\omega_0\, z^{-1} + z^{-2}}$ | $|z| > 1$ |
| $r^n\cos(\omega_0 n)\,u[n]$ | $\dfrac{1 - r\cos\omega_0\, z^{-1}}{1 - 2r\cos\omega_0\, z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |
| $r^n\sin(\omega_0 n)\,u[n]$ | $\dfrac{r\sin\omega_0\, z^{-1}}{1 - 2r\cos\omega_0\, z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |
| $n u[n]$ | $\dfrac{z^{-1}}{(1 - z^{-1})^2}$ | $|z| > 1$ |
| $n^2 u[n]$ | $\dfrac{z^{-1}(1 + z^{-1})}{(1 - z^{-1})^3}$ | $|z| > 1$ |
| $\binom{n + k - 1}{k - 1} a^n u[n]$ | $\dfrac{1}{(1 - a z^{-1})^k}$ | $|z| > |a|$ |
| Finite $\{x[0],\dots,x[N]\}$ | $\sum_{n=0}^N x[n] z^{-n}$ | all $z$ except possibly $0,\infty$ |

### 6.3 $z$-Transform Properties (Bilateral)

Let $x[n]\leftrightarrow X(z)$ with ROC $R_x$.

| Property | Sequence | $z$-domain / ROC |
|---|---|---|
| Linearity | $a x_1[n] + b x_2[n]$ | $a X_1(z) + b X_2(z)$, ROC $\supseteq R_1 \cap R_2$ |
| Time shift | $x[n - n_0]$ | $z^{-n_0} X(z)$, ROC $= R_x$ (possibly $\pm \{0,\infty\}$) |
| $z$-scaling | $z_0^n\, x[n]$ | $X(z/z_0)$, ROC $= |z_0|\cdot R_x$ |
| Time reversal | $x[-n]$ | $X(z^{-1})$, ROC $= 1/R_x$ |
| Conjugation | $x^*[n]$ | $X^*(z^*)$, ROC $= R_x$ |
| Convolution | $x_1[n] * x_2[n]$ | $X_1(z) X_2(z)$, ROC $\supseteq R_1 \cap R_2$ |
| Differentiation in $z$ | $n\, x[n]$ | $-z\,\dfrac{d}{dz} X(z)$, ROC $= R_x$ |
| First difference | $x[n] - x[n-1]$ | $(1 - z^{-1}) X(z)$ |
| Accumulation | $\displaystyle\sum_{k=-\infty}^{n} x[k]$ | $\dfrac{1}{1 - z^{-1}} X(z)$, ROC $\supseteq R_x \cap\{|z|>1\}$ |
| Parseval | $\sum_n x_1[n] x_2^*[n]$ | $\dfrac{1}{2\pi j}\oint X_1(v) X_2^*(1/v^*)v^{-1}\,dv$ |

### 6.4 Unilateral $z$-Transform: Time-Shift Property (incorporates ICs)

Delays (the common case for causal difference equations):

$$x[n-1]\ \xleftrightarrow{\mathcal{Z}_u}\ z^{-1}\mathcal{X}(z) + x[-1]$$

$$x[n-2]\ \xleftrightarrow{\mathcal{Z}_u}\ z^{-2}\mathcal{X}(z) + z^{-1} x[-1] + x[-2]$$

$$x[n-m]\ \xleftrightarrow{\mathcal{Z}_u}\ z^{-m}\mathcal{X}(z) + \sum_{k=1}^{m} z^{-(m-k)} x[-k]$$

Advances:

$$x[n+1]\ \xleftrightarrow{\mathcal{Z}_u}\ z\mathcal{X}(z) - z x[0]$$

$$x[n+m]\ \xleftrightarrow{\mathcal{Z}_u}\ z^m\mathcal{X}(z) - \sum_{k=0}^{m-1} z^{m-k} x[k]$$

### 6.5 Initial- and Final-Value Theorems (Unilateral, Causal)

**Initial value** (causal $x[n]$):

$$x[0] = \lim_{z\to\infty} X(z)$$

**Final value** (all poles of $(1 - z^{-1})X(z)$ strictly inside unit circle):

$$\lim_{n\to\infty} x[n] = \lim_{z\to 1}\,(1 - z^{-1})\, X(z)$$

### 6.6 ROC Rules

1. ROC is an annular ring centered at the origin: $r_1 < |z| < r_2$.
2. ROC never contains a pole.
3. Finite-duration $x[n]$: ROC is all $z$ except possibly $0$ and/or $\infty$.
4. **Right-sided** $x[n]$, rational $X(z)$: ROC is $|z| > r_{\max}$ (exterior of outermost pole circle). If additionally causal, $\infty$ is in ROC.
5. **Left-sided** $x[n]$: ROC is $|z| < r_{\min}$ (interior of innermost pole circle). If anticausal ($x[n]=0$ for $n>0$), $0$ is in ROC.
6. **Two-sided** $x[n]$: ROC is an annular ring between two consecutive pole circles (or empty).
7. ROC includes unit circle $\iff$ DTFT exists and $X(e^{j\omega}) = X(z)|_{z=e^{j\omega}}$.

**Causal + BIBO stable** (rational, causal) $\iff$ all poles strictly inside unit circle ($|p_i| < 1$).

---

## Section 7: Connections Between Transforms

### 7.1 Laplace $\leftrightarrow$ Fourier (CT)

The CTFT is the Laplace transform evaluated on the $j\omega$-axis, **provided** the ROC of $X(s)$ contains that axis:

$$X(j\omega) = X(s)\big|_{s = j\omega} \qquad \text{iff } \{s:\Re\{s\}=0\} \subset \text{ROC}$$

Counterexample: $e^{2t}u(t)\leftrightarrow \tfrac{1}{s-2}$, ROC $\Re\{s\}>2$. The $j\omega$-axis is not in the ROC, so the CTFT does not exist.

### 7.2 $z$-Transform $\leftrightarrow$ DTFT

The DTFT is the $z$-transform evaluated on the unit circle, **provided** the ROC contains that circle:

$$X(e^{j\omega}) = X(z)\big|_{z = e^{j\omega}} \qquad \text{iff } \{z:|z|=1\}\subset \text{ROC}$$

### 7.3 Laplace $\leftrightarrow$ $z$ (CT/DT parallel)

| | Laplace | $z$-transform |
|---|---|---|
| Variable | $s = \sigma + j\omega$ | $z = r e^{j\omega}$ |
| Fourier lives on | $j\omega$-axis | unit circle $|z|=1$ |
| ROC shape | vertical strip | annular ring |
| Causal+stable | all poles in LHP | all poles inside unit circle |
| Convolution $\to$ | multiplication | multiplication |
| Diff/Delay operator | $s \leftrightarrow d/dt$ | $z^{-1}\leftrightarrow$ unit delay |

Approximate mappings between $s$ and $z$ used for designing DT systems from CT prototypes:

**Impulse invariance:** Sample $h(t)$ to get $h[n] = T h(nT)$. Preserves time-domain shape but can alias if $H(j\omega)$ is not band-limited.

**Bilinear transform:**
$$s = \frac{2}{T}\,\frac{1 - z^{-1}}{1 + z^{-1}} \qquad\Longleftrightarrow\qquad z = \frac{1 + (T/2)s}{1 - (T/2)s}$$
Maps the entire $j\omega$-axis (CT) onto the unit circle (DT) with frequency warping $\omega_{\text{CT}} = \tfrac{2}{T}\tan(\omega_{\text{DT}}/2)$. LHP maps to interior of unit circle; stable $\to$ stable.

### 7.4 CT $\leftrightarrow$ DT via Sampling (Spectrum Replication)

Sampling $x_c(t)$ at period $T$ with $\omega_s = 2\pi/T$:

$$\boxed{\,X_p(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X_c\bigl(j(\omega - k\omega_s)\bigr)\,}$$

The CT spectrum is copy-pasted at every integer multiple of $\omega_s$ and scaled by $1/T$. The DTFT of the sample sequence $x[n] = x_c(nT)$ is related to this replicated spectrum by the frequency warp $\Omega = \omega T$:

$$X(e^{j\Omega}) = \frac{1}{T}\sum_{k} X_c\!\left(j\,\tfrac{\Omega - 2\pi k}{T}\right)$$

**Sampling theorem (Nyquist/Shannon):** If $X_c(j\omega)=0$ for $|\omega|>\omega_M$ and $\omega_s > 2\omega_M$, then $x_c(t)$ is recoverable from its samples via an ideal LPF of cutoff $\omega_c\in(\omega_M, \omega_s - \omega_M)$ and passband gain $T$. **Nyquist rate** = $2\omega_M$ (strict inequality).

**Sinc interpolation (band-limited reconstruction):**

$$x_r(t) = \sum_{n=-\infty}^{\infty} x(nT)\,\frac{\sin[\pi(t - nT)/T]}{\pi(t - nT)/T}$$

---

## Section 8: PFE Cookbook (Partial Fraction Expansion)

Given a proper rational $X(s)$ (or $X(z)$) with numerator degree $<$ denominator degree. If improper, long-divide first.

### 8.1 Distinct Poles

$$X(s) = \frac{N(s)}{(s-p_1)(s-p_2)\cdots(s-p_n)} = \sum_{k=1}^{n}\frac{A_k}{s - p_k}$$

**Cover-up (Heaviside) method:**

$$A_k = \bigl[(s - p_k)\, X(s)\bigr]_{s = p_k}$$

Then for each pole (using the ROC to assign direction):

- ROC to the **right** of $p_k$ $\Rightarrow$ right-sided term $A_k\, e^{p_k t}\, u(t)$.
- ROC to the **left** of $p_k$ $\Rightarrow$ left-sided term $-A_k\, e^{p_k t}\, u(-t)$.

### 8.2 Repeated Poles

If $p$ has multiplicity $m$, include all $m$ terms:

$$X(s) = \cdots + \frac{B_1}{s - p} + \frac{B_2}{(s - p)^2} + \cdots + \frac{B_m}{(s - p)^m} + \cdots$$

**Cover-up generalization:**

$$B_{m-k} = \frac{1}{k!}\left.\frac{d^k}{ds^k}\bigl[(s - p)^m X(s)\bigr]\right|_{s=p}, \quad k = 0,1,\ldots,m-1$$

Inversion uses the pair

$$\frac{1}{(s + a)^n}\ \longleftrightarrow\ \frac{t^{n-1}}{(n-1)!}\,e^{-at}u(t)$$

### 8.3 Complex Conjugate Poles (Quadratic Factor)

For a factor $s^2 + bs + c$ with complex roots, **complete the square**:

$$s^2 + b s + c = (s + a)^2 + \omega_d^2,\qquad a = b/2,\ \omega_d = \sqrt{c - a^2}$$

Express the numerator in the form $\alpha(s+a) + \beta\omega_d$ and invert via

$$\frac{s+a}{(s+a)^2 + \omega_d^2}\ \leftrightarrow\ e^{-at}\cos(\omega_d t) u(t),\qquad \frac{\omega_d}{(s+a)^2+\omega_d^2}\ \leftrightarrow\ e^{-at}\sin(\omega_d t) u(t)$$

Never split complex-conjugate poles into separate first-order terms with complex coefficients.

### 8.4 $z$-Transform PFE (Work in $z^{-1}$)

Write $X(z)$ as a rational function of $z^{-1}$, then

$$X(z) = \sum_k \frac{A_k}{1 - d_k z^{-1}}\quad\text{(distinct poles)}$$

- $A_k = \bigl[(1 - d_k z^{-1}) X(z)\bigr]_{z = d_k}$.
- ROC **outside** $|d_k|$ $\Rightarrow$ right-sided term $A_k\, d_k^n\, u[n]$.
- ROC **inside** $|d_k|$ $\Rightarrow$ left-sided term $-A_k\, d_k^n\, u[-n-1]$.

For repeated poles of order $m$ at $d$, include $\frac{B_1}{1 - d z^{-1}}+ \frac{B_2}{(1 - d z^{-1})^2}+\cdots$ and invert using

$$\frac{1}{(1 - d z^{-1})^k}\ \leftrightarrow\ \binom{n + k - 1}{k - 1} d^n u[n]$$

If the numerator degree (in $z^{-1}$) exceeds the denominator degree, long-divide to pull out a polynomial in $z^{-1}$ (which inverts to weighted impulses).

---

## Section 9: Common Signal Definitions

**Unit step (CT):**
$$u(t) = \begin{cases} 1, & t > 0 \\ 1/2, & t = 0 \\ 0, & t < 0 \end{cases}$$

**Unit step (DT):**
$$u[n] = \begin{cases} 1, & n \ge 0 \\ 0, & n < 0\end{cases}$$

**Dirac delta (CT):** defined by $\int_{-\infty}^{\infty} \delta(t)\phi(t)\,dt = \phi(0)$ for test functions $\phi$. Sifting: $\int x(\tau)\delta(t - \tau)\,d\tau = x(t)$. Relationship: $\delta(t) = \dfrac{d}{dt} u(t)$, and $u(t) = \int_{-\infty}^t \delta(\tau)\,d\tau$.

**Kronecker delta (DT):**
$$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \ne 0\end{cases}\qquad\text{Sifting: }x[n]=\sum_k x[k]\,\delta[n-k]$$
Relationship: $\delta[n] = u[n] - u[n-1]$ and $u[n] = \sum_{k=-\infty}^n \delta[k]$.

**Rectangular pulse (CT):**
$$\mathrm{rect}(t/T_1) = \begin{cases} 1, & |t| \le T_1/2 \\ 0, & |t| > T_1/2\end{cases}$$

**Normalized sinc:** $\mathrm{sinc}(x) = \dfrac{\sin(\pi x)}{\pi x}$, with $\mathrm{sinc}(0) = 1$. Zeros at nonzero integers.

**Unnormalized sinc:** Some texts write $\mathrm{sinc}(x) = \dfrac{\sin x}{x}$; this document uses the normalized convention except where the source material explicitly differs.

**Signum:**
$$\mathrm{sgn}(t) = \begin{cases} +1, & t > 0 \\ 0, & t = 0 \\ -1, & t < 0\end{cases}\qquad u(t) = \tfrac{1}{2}[1 + \mathrm{sgn}(t)]$$

**Triangular pulse width $2T_1$:**
$$\mathrm{tri}(t/T_1) = \begin{cases} 1 - |t|/T_1, & |t| \le T_1 \\ 0, & |t| > T_1\end{cases}$$

**Impulse train (CT):** $\displaystyle p(t) = \sum_{n=-\infty}^{\infty}\delta(t - nT)$, period $T$.

**Complex exponential (eigenfunctions of LTI systems):** $e^{st}$ (CT) and $z^n$ (DT) pass through LTI systems unchanged up to scaling by $H(s)$ or $H(z)$ respectively.

---

## Section 10: Sampling and Reconstruction

### 10.1 Impulse-Train Sampling Model

Model sampling as multiplication by a periodic impulse train $p(t) = \sum_{n=-\infty}^{\infty}\delta(t - nT)$:

$$x_p(t) = x(t)\,p(t) = \sum_{n=-\infty}^{\infty} x(nT)\,\delta(t - nT)$$

The sampling period is $T$; the sampling frequency is $\omega_s = 2\pi/T$ (rad/s) or $f_s = 1/T$ (Hz).

### 10.2 Spectrum of the Sampled Signal

Since $P(j\omega) = \dfrac{2\pi}{T}\sum_k \delta(\omega - k\omega_s)$, multiplication in time becomes convolution in frequency:

$$\boxed{\,X_p(j\omega) = \frac{1}{T}\sum_{k=-\infty}^{\infty} X\!\bigl(j(\omega - k\omega_s)\bigr)\,}$$

Sampling creates **periodic replicas** of $X(j\omega)$ at every multiple of $\omega_s$, each scaled by $1/T$. The sampling theorem boils down to whether these replicas overlap.

### 10.3 Sampling Theorem (Shannon / Nyquist)

If $X(j\omega) = 0$ for $|\omega| > \omega_M$ (band-limited), then $x(t)$ is uniquely determined by its samples $x(nT)$ provided

$$\boxed{\,\omega_s > 2\omega_M\,}$$

- **Nyquist rate:** $2\omega_M$ (minimum sampling frequency; must be *strictly* exceeded).
- **Nyquist frequency:** $\omega_M = \omega_s/2$.
- Sampling at exactly $\omega_s = 2\omega_M$ is **not** sufficient (counterexample: $\sin(\omega_s t/2)$ samples to zero).

### 10.4 Ideal Reconstruction (Sinc Interpolation)

Pass $x_p(t)$ through an ideal LPF $H(j\omega)$ with gain $T$ in passband and cutoff $\omega_c$ satisfying $\omega_M < \omega_c < \omega_s - \omega_M$. With $\omega_c = \pi/T$, the impulse response is

$$h(t) = \frac{\sin(\pi t/T)}{\pi t/T}$$

**Sinc interpolation formula:**

$$\boxed{\,x_r(t) = \sum_{n=-\infty}^{\infty} x(nT)\,\frac{\sin[\pi(t - nT)/T]}{\pi(t - nT)/T}\,}$$

Each sinc equals 1 at its own sample instant and 0 at every other sample instant.

### 10.5 Aliasing

If $\omega_s < 2\omega_M$, the replicas overlap and the original $X(j\omega)$ cannot be recovered by any linear filter: this is **aliasing** (irreversible). For a sinusoid $\cos(2\pi f_0 t)$ sampled at $f_s$ with $f_s/2 < f_0 < f_s$, the aliased frequency is

$$f_{\text{alias}} = |f_s - f_0|$$

Mitigation: use an **anti-aliasing LPF** with cutoff $\omega_s/2$ **before** sampling.

### 10.6 Practical Reconstruction Filters

| Method | Impulse response | Accuracy |
|---|---|---|
| Ideal LPF (sinc interpolation) | $h(t) = \sin(\pi t/T)/(\pi t/T)$ | Exact, non-causal, infinite support |
| Zero-order hold (ZOH) | Rectangular pulse, width $T$ | Staircase approximation |
| First-order hold (FOH) | Triangular pulse, base $2T$ | Piecewise-linear "connect-the-dots" |

### 10.7 DT Processing of CT Signals

A cascade C/D $\to$ DT system $\to$ D/C acts as a CT LTI system provided the sampling theorem is met. The CT angular frequency $\omega$ and the DT angular frequency $\Omega$ are related by

$$\Omega = \omega T$$

Thus $|\omega| < \omega_s/2 = \pi/T$ maps to $|\Omega| < \pi$.

### 10.8 Summary of Sampling Formulas

| Concept | Formula |
|---|---|
| Sampling period / frequency | $T = 2\pi/\omega_s$; $f_s = 1/T$ |
| Nyquist rate | $2\omega_M$ (must be strictly exceeded) |
| Sampling condition | $\omega_s > 2\omega_M$ |
| Sampled spectrum | $X_p(j\omega) = \dfrac{1}{T}\sum_k X(j(\omega - k\omega_s))$ |
| Sinc interpolation | $x_r(t) = \sum_n x(nT)\,\operatorname{sinc}((t - nT)/T)$ |
| Aliased frequency | $f_{\text{alias}} = |f_s - f_0|$ for $f_s/2 < f_0 < f_s$ |
| CT $\leftrightarrow$ DT frequency | $\Omega = \omega T$ |

---

## Section 11: Feedback Systems

### 11.1 Block-Diagram Building Blocks

| Interconnection | Equivalent Transfer Function |
|---|---|
| Cascade (series) $H_1 \to H_2$ | $H(s) = H_1(s)\,H_2(s)$ |
| Parallel $H_1 + H_2$ | $H(s) = H_1(s) + H_2(s)$ |
| Negative feedback (forward $H$, feedback $G$) | $Q(s) = \dfrac{H(s)}{1 + G(s)H(s)}$ |
| Positive feedback | $Q(s) = \dfrac{H(s)}{1 - G(s)H(s)}$ |
| Unity feedback ($G = 1$) | $Q(s) = \dfrac{H(s)}{1 + H(s)}$ |

### 11.2 Closed-Loop Transfer Function

For the standard negative-feedback loop:

$$\boxed{\,Q(s) = \frac{Y(s)}{X(s)} = \frac{H(s)}{1 + G(s)H(s)}\,}$$

The product $L(s) = G(s)H(s)$ is the **loop gain**. The **characteristic equation** is

$$1 + G(s)H(s) = 0$$

whose roots are the **closed-loop poles**. Stability of the closed-loop system is determined by these roots, not by the poles of $G$ or $H$ individually.

### 11.3 Limiting Behavior of $Q = H/(1+GH)$

| Regime | Approximation | Interpretation |
|---|---|---|
| $|GH| \gg 1$ | $Q \approx 1/G$ | Closed-loop depends on feedback path only; plant variations are rejected |
| $|GH| \ll 1$ | $Q \approx H$ | Feedback barely affects the system |
| $GH = -1$ at some $\omega$ | $Q \to \infty$ | Instability |

### 11.4 Sensitivity

Sensitivity of the closed-loop transfer function to variations in the plant $H$ (unity feedback):

$$S_H^Q = \frac{\partial Q/Q}{\partial H/H} = \frac{1}{1 + H(s)}$$

Large loop gain $\Rightarrow$ small sensitivity to plant parameter variations.

### 11.5 Stability Criteria

**Pole test.** A CT feedback system is stable iff all roots of $1 + G(s)H(s) = 0$ lie in the open LHP ($\Re\{s\} < 0$). A DT feedback system is stable iff all roots of $1 + G(z)H(z) = 0$ lie strictly inside the unit circle ($|z| < 1$).

**Nyquist criterion (simplified, stable open-loop $GH$).** Plot the loop gain $GH(j\omega)$ in the complex plane as $\omega$ runs from $-\infty$ to $+\infty$. The closed-loop system with gain $K$ is stable iff the Nyquist contour does **not encircle** the critical point $-1/K$. The curve for $\omega < 0$ is the mirror image (across the real axis) of the $\omega > 0$ half.

**Instability condition.** $GH(j\omega) = -1$, i.e. $|GH(j\omega)| = 1$ (0 dB) **and** $\angle GH(j\omega) = -180^\circ$ **simultaneously**.

### 11.6 Gain Margin and Phase Margin

Let $\omega_1$ be the **phase crossover** ($\angle GH(j\omega_1) = -180^\circ$) and $\omega_2$ the **gain crossover** ($|GH(j\omega_2)| = 1$, i.e. 0 dB). Then:

| Margin | Definition | Reading from Bode plot |
|---|---|---|
| Phase margin (PM) | $\mathrm{PM} = 180^\circ + \angle GH(j\omega_2)$ | Phase plot value at 0-dB crossover, relative to $-180^\circ$ |
| Gain margin (GM) | $\mathrm{GM} = \dfrac{1}{|GH(j\omega_1)|}$ | Magnitude plot value at the $-180^\circ$ phase crossover, below 0 dB |
| Gain margin (dB) | $\mathrm{GM}_{\text{dB}} = -20\log_{10}|GH(j\omega_1)|$ | How many dB you can increase gain before instability |

Both margins positive $\Rightarrow$ closed-loop system is stable with margin. Either margin zero or negative $\Rightarrow$ unstable (or on the boundary).

**Maximum tolerable extra time delay** at the gain crossover:

$$\tau_{\max} = \frac{\mathrm{PM\ (rad)}}{\omega_2}$$

A pure delay $\tau$ contributes phase $-\omega\tau$, which eats into the phase margin as frequency increases.

### 11.7 CT vs. DT Feedback Summary

| | Continuous-time | Discrete-time |
|---|---|---|
| Closed-loop formula | $H(s)/[1 + G(s)H(s)]$ | $H(z)/[1 + G(z)H(z)]$ |
| Stability boundary | $j\omega$-axis | unit circle $|z| = 1$ |
| Stable closed-loop poles | $\Re\{s\} < 0$ (open LHP) | $|z| < 1$ (strictly inside unit circle) |
| Delay operator | $e^{-st_0}$ | $z^{-1}$ (unit delay) |

### 11.8 Common Pitfalls

- Sign error at the summer: negative feedback $\to 1 + GH$; positive feedback $\to 1 - GH$.
- Open-loop poles (roots of $GH$) are **not** the closed-loop poles (roots of $1 + KGH$).
- Gain margin is read from the magnitude plot at the frequency located on the phase plot; phase margin is read from the phase plot at the frequency located on the magnitude plot. Do not mix them up.
- RHP zeros do not cause instability (only RHP poles do for causal CT systems); they produce non-minimum-phase behavior.
- CT stability $\neq$ DT stability: LHP vs. inside-the-unit-circle. A DT pole at $z = -0.9$ is stable.

---

*End of Master Transforms Reference.*
