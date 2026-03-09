# CEC 315 Homework 4 Solutions (Lectures 12–15)

---

## Problem 1: CT Fourier Transform — Basic Pairs

### Part (a): $x(t) = 3e^{-5t}u(t)$

Using the one-sided exponential pair $e^{-at}u(t) \leftrightarrow \frac{1}{a+j\omega}$ with linearity:

$$X(j\omega) = 3 \cdot \frac{1}{5 + j\omega} = \frac{3}{5 + j\omega}$$

**Magnitude:** $|X(j\omega)| = \frac{3}{\sqrt{25 + \omega^2}}$

**Phase:** $\angle X(j\omega) = -\arctan(\omega/5)$

**Sanity check:** $X(j0) = 3/5 = 0.6$

Verify: $\int_0^{\infty} 3e^{-5t} \, dt = 3 \cdot \frac{1}{5} = 0.6$ ✓

### Part (b): $x(t) = 4e^{-2|t|}$

Using the two-sided exponential pair $e^{-a|t|} \leftrightarrow \frac{2a}{a^2 + \omega^2}$ with $a = 2$:

$$X(j\omega) = 4 \cdot \frac{2(2)}{4 + \omega^2} = \frac{16}{4 + \omega^2}$$

**Magnitude:** $|X(j\omega)| = \frac{16}{4 + \omega^2}$ (already real and positive, so magnitude = value)

**Phase:** $\angle X(j\omega) = 0$ for all $\omega$ (real, even, positive → zero phase)

**Sanity check:** $X(j0) = 16/4 = 4$

Verify: $\int_{-\infty}^{\infty} 4e^{-2|t|} \, dt = 2 \int_0^{\infty} 4e^{-2t} \, dt = 2 \cdot 4 \cdot \frac{1}{2} = 4$ ✓

### Part (c): Rectangular Pulse — Height 2, Width 6

$$x(t) = \begin{cases} 2 & |t| \leq 3 \\ 0 & |t| > 3 \end{cases}$$

Using the rectangular pulse pair (height $A$, half-width $T_1$): $X(j\omega) = A \cdot \frac{2\sin(\omega T_1)}{\omega}$

With $A = 2$, $T_1 = 3$:

$$X(j\omega) = 2 \cdot \frac{2\sin(3\omega)}{\omega} = \frac{4\sin(3\omega)}{\omega}$$

Equivalently: $X(j\omega) = 12 \, \text{sinc}\left(\frac{3\omega}{\pi}\right)$

**Sanity check:** $X(j0) = \lim_{\omega \to 0} \frac{4\sin(3\omega)}{\omega} = 4 \cdot 3 = 12$

Verify: $\int_{-3}^{3} 2 \, dt = 12$ ✓

### Part (d): Sanity Check Discussion

The DC value $X(j0)$ equals the total area under $x(t)$:

$$X(j0) = \int_{-\infty}^{\infty} x(t) e^{-j(0)t} \, dt = \int_{-\infty}^{\infty} x(t) \, dt$$

This is because at $\omega = 0$, the complex exponential $e^{-j\omega t} = 1$, so the transform integral reduces to the plain area integral. This provides a quick verification for any computed FT.

---

## Problem 2: DTFT — Basic Pairs

### Part (a): $x[n] = (0.6)^n u[n]$

This is a one-sided exponential with $a = 0.6$, $|a| < 1$. Using geometric series:

$$X(e^{j\omega}) = \sum_{n=0}^{\infty} (0.6)^n e^{-j\omega n} = \sum_{n=0}^{\infty} (0.6 \, e^{-j\omega})^n = \frac{1}{1 - 0.6 \, e^{-j\omega}}$$

**Magnitude:**
$$|X(e^{j\omega})| = \frac{1}{|1 - 0.6 e^{-j\omega}|}$$

Expand: $1 - 0.6e^{-j\omega} = 1 - 0.6\cos\omega + j0.6\sin\omega$

$$|X(e^{j\omega})| = \frac{1}{\sqrt{(1-0.6\cos\omega)^2 + (0.6\sin\omega)^2}} = \frac{1}{\sqrt{1 - 1.2\cos\omega + 0.36}}$$

$$= \frac{1}{\sqrt{1.36 - 1.2\cos\omega}}$$

**Key values:**
- $\omega = 0$: $X(e^{j0}) = \frac{1}{1-0.6} = \frac{1}{0.4} = 2.5$
  - Check: $\sum_{n=0}^{\infty} (0.6)^n = 1/(1-0.6) = 2.5$ ✓
- $\omega = \pi$: $X(e^{j\pi}) = \frac{1}{1+0.6} = \frac{1}{1.6} = 0.625$
  - This is the minimum magnitude (alternating sum)

### Part (b): $h[n] = \{1, 2, 3, 2, 1\}$ (starting at $n = 0$)

$$H(e^{j\omega}) = 1 + 2e^{-j\omega} + 3e^{-j2\omega} + 2e^{-j3\omega} + e^{-j4\omega}$$

Factor out the center delay $e^{-j2\omega}$:

$$H(e^{j\omega}) = e^{-j2\omega}\left[e^{j2\omega} + 2e^{j\omega} + 3 + 2e^{-j\omega} + e^{-j2\omega}\right]$$

$$= e^{-j2\omega}\left[3 + 2(e^{j\omega} + e^{-j\omega}) + (e^{j2\omega} + e^{-j2\omega})\right]$$

$$= e^{-j2\omega}\left[3 + 4\cos\omega + 2\cos 2\omega\right]$$

So:
$$|H(e^{j\omega})| = |3 + 4\cos\omega + 2\cos 2\omega|$$

$$\angle H(e^{j\omega}) = -2\omega \quad \text{(plus } \pm\pi \text{ if bracketed term is negative)}$$

**Linear phase check:** The phase is $-2\omega$, which is **linear** in $\omega$ with slope $-2$. This corresponds to a pure delay of $n_d = 2$ samples.

**Why linear phase?** The coefficients are **symmetric** about the center ($n = 2$): $h[n] = h[4-n]$. Symmetric FIR filters always have linear phase.

**Key values:**
- $\omega = 0$: $H(e^{j0}) = 1+2+3+2+1 = 9$, $|H| = 9$
- $\omega = \pi$: $H(e^{j\pi}) = 1-2+3-2+1 = 1$, $|H| = 1$

---

## Problem 3: FT Properties

### Part (a): Time Shifting — $x(t) = e^{-3(t-2)}u(t-2)$

Recognize this as a time-shifted version of $g(t) = e^{-3t}u(t)$.

With $g(t) \leftrightarrow G(j\omega) = \frac{1}{3+j\omega}$ and time shift $t_0 = 2$:

$$X(j\omega) = e^{-j2\omega} \cdot \frac{1}{3+j\omega} = \frac{e^{-j2\omega}}{3+j\omega}$$

**Magnitude:** $|X(j\omega)| = \frac{1}{\sqrt{9+\omega^2}}$ (same as unshifted — time shift doesn't change magnitude)

**Phase:** $\angle X(j\omega) = -2\omega - \arctan(\omega/3)$ (original phase plus linear phase from delay)

### Part (b): Frequency Shifting — $x(t) = e^{-3t}u(t)\cos(10t)$

Start with $g(t) = e^{-3t}u(t) \leftrightarrow G(j\omega) = \frac{1}{3+j\omega}$.

Using the modulation property $g(t)\cos(\omega_0 t) = \frac{1}{2}[g(t)e^{j\omega_0 t} + g(t)e^{-j\omega_0 t}]$:

$$X(j\omega) = \frac{1}{2}\left[G(j(\omega-10)) + G(j(\omega+10))\right]$$

$$= \frac{1}{2}\left[\frac{1}{3+j(\omega-10)} + \frac{1}{3+j(\omega+10)}\right]$$

The spectrum of the exponential (centered at $\omega = 0$) is shifted to $\pm 10$ rad/s.

### Part (c): Differentiation — $y(t) = \frac{d}{dt}[e^{-3t}u(t)]$

First, note the derivative of $e^{-3t}u(t)$:

$$\frac{d}{dt}[e^{-3t}u(t)] = -3e^{-3t}u(t) + e^{-3t}\delta(t) = -3e^{-3t}u(t) + \delta(t)$$

(Product rule: the $\delta(t)$ comes from differentiating $u(t)$, evaluated at $t=0$ where $e^{-3t}=1$.)

**Method 1 — Direct from known pairs:**
$$Y(j\omega) = -3 \cdot \frac{1}{3+j\omega} + 1 = \frac{-3 + 3 + j\omega}{3+j\omega} = \frac{j\omega}{3+j\omega}$$

**Method 2 — Differentiation property:**
$$Y(j\omega) = j\omega \cdot G(j\omega) = j\omega \cdot \frac{1}{3+j\omega} = \frac{j\omega}{3+j\omega}$$

Both methods agree. ✓

### Part (d): Convolution Property with PFE

**Given:** $h(t) = 2e^{-4t}u(t)$ and $x(t) = e^{-3t}u(t)$. Find $y(t) = x(t) * h(t)$.

**Step 1 — Transform:**
$$H(j\omega) = \frac{2}{4+j\omega}, \quad X(j\omega) = \frac{1}{3+j\omega}$$

**Step 2 — Multiply:**
$$Y(j\omega) = X(j\omega) \cdot H(j\omega) = \frac{2}{(3+j\omega)(4+j\omega)}$$

**Step 3 — Partial Fraction Expansion:**
$$\frac{2}{(3+j\omega)(4+j\omega)} = \frac{A}{3+j\omega} + \frac{B}{4+j\omega}$$

Cover-up method:
- $A = \frac{2}{4+j\omega}\Big|_{j\omega=-3} = \frac{2}{4-3} = 2$
- $B = \frac{2}{3+j\omega}\Big|_{j\omega=-4} = \frac{2}{3-4} = -2$

$$Y(j\omega) = \frac{2}{3+j\omega} - \frac{2}{4+j\omega}$$

**Step 4 — Inverse FT:**
$$\boxed{y(t) = 2e^{-3t}u(t) - 2e^{-4t}u(t) = 2(e^{-3t} - e^{-4t})u(t)}$$

**Verification:** At $t = 0$: $y(0) = 2(1-1) = 0$ ✓ (convolution of causal signals starts at zero)

As $t \to \infty$: $y(t) \to 0$ ✓ (both terms decay)

---

## Problem 4: Systems from Differential/Difference Equations

### Part (a): CT System

**Given:** $\frac{d^2 y}{dt^2} + 7\frac{dy}{dt} + 10y(t) = 3x(t)$

Replace $d^n/dt^n \to (j\omega)^n$:

$$(j\omega)^2 Y + 7(j\omega)Y + 10Y = 3X$$

$$Y(j\omega)[(j\omega)^2 + 7(j\omega) + 10] = 3X(j\omega)$$

$$H(j\omega) = \frac{Y(j\omega)}{X(j\omega)} = \frac{3}{(j\omega)^2 + 7(j\omega) + 10}$$

**Factor the denominator:**
$(j\omega)^2 + 7(j\omega) + 10 = (j\omega + 2)(j\omega + 5)$

(Roots: $j\omega = -2$ and $j\omega = -5$)

$$\boxed{H(j\omega) = \frac{3}{(j\omega + 2)(j\omega + 5)}}$$

**System type:** Two real poles at $-2$ and $-5$. Both negative → stable system.

**Key values:**
- DC gain: $H(j0) = \frac{3}{2 \cdot 5} = \frac{3}{10} = 0.3$
- This is a second-order lowpass filter (both poles are real → overdamped)

**Impulse response via PFE:**
$$H(j\omega) = \frac{3}{(j\omega+2)(j\omega+5)} = \frac{A}{j\omega+2} + \frac{B}{j\omega+5}$$

- $A = \frac{3}{j\omega+5}\Big|_{j\omega=-2} = \frac{3}{3} = 1$
- $B = \frac{3}{j\omega+2}\Big|_{j\omega=-5} = \frac{3}{-3} = -1$

$$h(t) = e^{-2t}u(t) - e^{-5t}u(t) = (e^{-2t} - e^{-5t})u(t)$$

### Part (b): DT System

**Given:** $y[n] - 0.5y[n-1] - 0.06y[n-2] = x[n]$

Replace $y[n-k] \to e^{-j\omega k}Y(e^{j\omega})$ and $x[n-k] \to e^{-j\omega k}X(e^{j\omega})$:

$$Y(e^{j\omega})[1 - 0.5e^{-j\omega} - 0.06e^{-j2\omega}] = X(e^{j\omega})$$

$$H(e^{j\omega}) = \frac{1}{1 - 0.5e^{-j\omega} - 0.06e^{-j2\omega}}$$

**Factor the denominator:**
Let $z = e^{j\omega}$. The denominator in terms of $z^{-1}$ is:

$1 - 0.5z^{-1} - 0.06z^{-2}$

Multiply by $z^2$: $z^2 - 0.5z - 0.06 = 0$

Using quadratic formula:
$$z = \frac{0.5 \pm \sqrt{0.25 + 0.24}}{2} = \frac{0.5 \pm \sqrt{0.49}}{2} = \frac{0.5 \pm 0.7}{2}$$

$$z_1 = \frac{1.2}{2} = 0.6, \quad z_2 = \frac{-0.2}{2} = -0.1$$

So: $1 - 0.5e^{-j\omega} - 0.06e^{-j2\omega} = (1 - 0.6e^{-j\omega})(1 + 0.1e^{-j\omega})$

$$\boxed{H(e^{j\omega}) = \frac{1}{(1 - 0.6e^{-j\omega})(1 + 0.1e^{-j\omega})}}$$

**Stability:** Poles at $z = 0.6$ and $z = -0.1$. Both $|z| < 1$ → **stable**.

**DC gain:** $H(e^{j0}) = \frac{1}{(1-0.6)(1+0.1)} = \frac{1}{0.4 \times 1.1} = \frac{1}{0.44} \approx 2.273$

**Impulse response via PFE:**
$$H(e^{j\omega}) = \frac{A}{1-0.6e^{-j\omega}} + \frac{B}{1+0.1e^{-j\omega}}$$

Multiply both sides by $(1-0.6e^{-j\omega})(1+0.1e^{-j\omega})$:

$1 = A(1+0.1e^{-j\omega}) + B(1-0.6e^{-j\omega})$

Set $e^{-j\omega} = 1/0.6$ (i.e., at pole $z=0.6$): $1 = A(1 + 0.1/0.6) = A(1+1/6) = 7A/6$, so $A = 6/7$

Set $e^{-j\omega} = -1/0.1 = -10$ (i.e., at pole $z=-0.1$): $1 = B(1-0.6(-10)) = B(7) = 7B$, so $B = 1/7$

$$h[n] = \frac{6}{7}(0.6)^n u[n] + \frac{1}{7}(-0.1)^n u[n]$$

---

## Problem 5: Magnitude, Phase, and Group Delay

### Setup

**Given:** $H(j\omega) = \frac{1}{1 + j\omega/5}$

This is a first-order lowpass with cutoff $\omega_c = 5$ rad/s.

### Part (a): Fill the Table

$$|H(j\omega)| = \frac{1}{\sqrt{1+(\omega/5)^2}}, \quad \angle H(j\omega) = -\arctan(\omega/5)$$

$$|H|_{\text{dB}} = -10\log_{10}(1+(\omega/5)^2)$$

| $\omega$ (rad/s) | $\omega/\omega_c$ | $|H(j\omega)|$ | $|H|_{\text{dB}}$ | $\angle H(j\omega)$ |
|---|---|---|---|---|
| 0 | 0 | 1 | 0 dB | $0°$ |
| 1 | 0.2 | $\frac{1}{\sqrt{1.04}} \approx 0.981$ | $-0.17$ dB | $-11.3°$ |
| 2 | 0.4 | $\frac{1}{\sqrt{1.16}} \approx 0.928$ | $-0.64$ dB | $-21.8°$ |
| 5 | 1 | $\frac{1}{\sqrt{2}} \approx 0.707$ | $-3.01$ dB | $-45°$ |
| 10 | 2 | $\frac{1}{\sqrt{5}} \approx 0.447$ | $-6.99$ dB | $-63.4°$ |
| 50 | 10 | $\frac{1}{\sqrt{101}} \approx 0.0995$ | $-20.04$ dB | $-84.3°$ |
| 100 | 20 | $\frac{1}{\sqrt{401}} \approx 0.0500$ | $-26.05$ dB | $-87.1°$ |

### Part (b): Group Delay

$$\angle H(j\omega) = -\arctan(\omega/5)$$

$$\tau(\omega) = -\frac{d}{d\omega}[-\arctan(\omega/5)] = \frac{1/5}{1+(\omega/5)^2} = \frac{5}{25+\omega^2}$$

**Key values:**
- $\tau(0) = 1/5 = 0.2$ seconds (maximum delay)
- $\tau(5) = 5/50 = 0.1$ seconds
- $\tau(\omega) \to 0$ as $\omega \to \infty$

### Part (c): Linear Phase Test

For linear phase, we need $\angle H(j\omega) = -\omega t_d$ (straight line through origin).

$\angle H(j\omega) = -\arctan(\omega/5)$ is **not** a linear function of $\omega$.

Equivalently, $\tau(\omega) = \frac{5}{25+\omega^2}$ is **not constant**.

**Conclusion:** The system does **NOT** have linear phase. It introduces phase distortion — different frequency components experience different delays.

### Part (d): Two-Tone Signal

**Given:** $x(t) = \cos(t) + \cos(50t)$

Input has two frequencies: $\omega_1 = 1$ rad/s and $\omega_2 = 50$ rad/s.

**At $\omega = 1$:**
$$|H(j1)| = \frac{1}{\sqrt{1+0.04}} = \frac{1}{\sqrt{1.04}} \approx 0.981$$
$$\angle H(j1) = -\arctan(0.2) \approx -11.3°$$

**At $\omega = 50$:**
$$|H(j50)| = \frac{1}{\sqrt{1+100}} = \frac{1}{\sqrt{101}} \approx 0.0995$$
$$\angle H(j50) = -\arctan(10) \approx -84.3°$$

**Output:**
$$y(t) = 0.981\cos(t - 11.3°) + 0.0995\cos(50t - 84.3°)$$

**Interpretation:** The low-frequency component ($\omega = 1$) passes nearly unattenuated (98.1%), while the high-frequency component ($\omega = 50$) is strongly attenuated (9.95%). This confirms the lowpass filtering behavior — the system effectively removes the high-frequency tone.

**Group delay comparison:**
- $\tau(1) = 5/26 \approx 0.192$ s
- $\tau(50) = 5/2525 \approx 0.00198$ s

The low-frequency component is delayed ~100× more than the high-frequency component — severe phase distortion (but since the high-frequency component is nearly eliminated, this matters less in practice).

---

## Problem 6: Second-Order System

### Setup

**Given:** $\omega_n = 20$ rad/s, $\zeta = 0.25$

$$H(j\omega) = \frac{\omega_n^2}{(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2} = \frac{400}{(j\omega)^2 + 10(j\omega) + 400}$$

### Part (a): Classification

Since $\zeta = 0.25 < 1$: system is **underdamped**.

The poles are complex conjugate:
$$s = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2} = -5 \pm j20\sqrt{1-0.0625}$$
$$= -5 \pm j20(0.9682) = -5 \pm j19.36$$

- Real part: $\sigma = \zeta\omega_n = 5$ (decay rate)
- Damped frequency: $\omega_d = \omega_n\sqrt{1-\zeta^2} = 20\sqrt{0.9375} \approx 19.36$ rad/s

### Part (b): Key Frequency Response Values

**At DC ($\omega = 0$):**
$$H(j0) = \frac{400}{400} = 1 \quad \Rightarrow \quad |H| = 1, \quad 0 \text{ dB}, \quad \angle H = 0°$$

**At $\omega = \omega_n = 20$:**
$$H(j20) = \frac{400}{-400 + j200 + 400} = \frac{400}{j200} = \frac{2}{j} = -j2$$

$$|H(j20)| = 2 = \frac{1}{2\zeta} = \frac{1}{0.5} \quad \Rightarrow \quad 20\log_{10}(2) \approx 6.02 \text{ dB}$$

$$\angle H(j20) = -90°$$

**Resonance frequency:**
$$\omega_r = \omega_n\sqrt{1-2\zeta^2} = 20\sqrt{1-0.125} = 20\sqrt{0.875} \approx 18.71 \text{ rad/s}$$

Since $\zeta = 0.25 < 1/\sqrt{2} \approx 0.707$, resonance exists.

**Peak magnitude:**
$$|H(j\omega_r)| = \frac{1}{2\zeta\sqrt{1-\zeta^2}} = \frac{1}{2(0.25)\sqrt{1-0.0625}} = \frac{1}{0.5\sqrt{0.9375}} = \frac{1}{0.4841} \approx 2.066$$

$$|H|_{\text{dB}} = 20\log_{10}(2.066) \approx 6.30 \text{ dB}$$

### Part (c): Step Response Specifications

**Percent Overshoot:**
$$\%OS = 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}} = 100 \cdot e^{-\pi(0.25)/\sqrt{0.9375}}$$
$$= 100 \cdot e^{-0.7854/0.9682} = 100 \cdot e^{-0.8112} \approx 100 \times 0.4443 = 44.4\%$$

**Peak Time:**
$$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{19.36} \approx 0.162 \text{ s}$$

**Settling Time (2%):**
$$t_s \approx \frac{4}{\zeta\omega_n} = \frac{4}{5} = 0.8 \text{ s}$$

**Rise Time (approximate):**
$$t_r \approx \frac{1.8}{\omega_n} = \frac{1.8}{20} = 0.09 \text{ s}$$

### Part (d): Bode Plot Asymptotes

**Magnitude asymptotes:**
- For $\omega \ll 20$: $|H|_{\text{dB}} \approx 0$ dB (flat)
- For $\omega \gg 20$: slope = $-40$ dB/decade
- Asymptotes break at $\omega = \omega_n = 20$ rad/s
- Near $\omega_n$: resonance peak of ~6.3 dB above the 0 dB asymptote

**Phase asymptotes:**
- For $\omega \ll 20$: $\angle H \approx 0°$
- At $\omega = 20$: $\angle H = -90°$ (exact, regardless of $\zeta$)
- For $\omega \gg 20$: $\angle H \to -180°$
- Transition is sharper for lower $\zeta$

**Bode plot sketch notes:**
- The resonance peak makes the actual magnitude curve exceed the flat 0 dB asymptote near $\omega_n$
- With $\zeta = 0.25$, the peak is prominent (~6.3 dB)
- The phase transition through $-90°$ at $\omega_n$ is relatively sharp
- High-frequency rolloff is -40 dB/decade (two poles)
