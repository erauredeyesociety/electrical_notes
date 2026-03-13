# CEC 315 Exam 2 Solutions (Lectures 9–15)

**Total: 100 points | 60 minutes**

---

## Part I: Multiple Choice (20 pts, 4 pts each)

### 1. Answer: **(c)** — 9% of A, regardless of N

The **Gibbs phenomenon** states that for a signal with a jump discontinuity of height $A$, the Fourier series partial sum overshoots by approximately **9% of $A$** near each discontinuity. This overshoot does **not** vanish as $N \to \infty$ — the ripple narrows toward the discontinuity but the peak amplitude remains at ~9%. This eliminates (a), (b), and (d). Option (d) is wrong because the 9% persists for ALL $N$, not just $N < 100$.

### 2. Answer: **(b)** — $X(j(\omega - \omega_0))$

This is the **frequency-shifting property**: multiplying by $e^{j\omega_0 t}$ in time shifts the spectrum to the **right** by $\omega_0$:

$$e^{j\omega_0 t} x(t) \longleftrightarrow X(j(\omega - \omega_0))$$

Option (c) would correspond to multiplication by $e^{-j\omega_0 t}$ (shift left). Option (a) is wrong form. Option (d) describes convolution with an impulse, which would also give (b) after evaluation.

### 3. Answer: **(b)** — 8, because DT complex exponentials differing by $2\pi$ are identical

In discrete time, $e^{j(\omega_0 + 2\pi)n} = e^{j\omega_0 n}$ for all integer $n$. So harmonics $k$ and $k + N$ produce the same exponential. This means there are exactly $N = 8$ distinct harmonics.

Option (c) is wrong because Dirichlet conditions are a CT convergence concept — they don't limit the number of DT harmonics. Option (a) is wrong because the synthesis sum is finite (over $N$ terms). Option (d) confuses positive/negative counting.

### 4. Answer: **(b)** — $-20$ dB/decade

For a first-order lowpass $H(j\omega) = 1/(1 + j\omega/\omega_c)$:
- Low frequency: $|H| \approx 1$ → 0 dB (flat)
- High frequency: $|H| \approx \omega_c/\omega$ → decreases by 20 dB per decade

One pole contributes $-20$ dB/decade. Option (d) ($+20$ dB/decade) would be a zero. Option (a) ($-40$) would be second-order.

### 5. Answer: **(b)** — Underdamped with resonance peak because $\zeta < 1/\sqrt{2}$

With $\zeta = 0.3$:
- $\zeta < 1$ → **underdamped** (eliminates (a) overdamped and (d) critically damped)
- $\zeta = 0.3 < 1/\sqrt{2} \approx 0.707$ → **resonance peak exists** (eliminates (c))

---

## Problem 1 (20 pts): CT Fourier Series and Properties

### Given

$x(t)$ real-valued, $T = 2$, $\omega_0 = 2\pi/T = \pi$ rad/s.

$$x(t) = \begin{cases} +1 & 0 \leq t < 1 \\ -1 & 1 \leq t < 2 \end{cases}$$

### Part (a): Piecewise expression and $a_0$ (5 pts)

**Step 1:** Apply the average-value formula:

$$a_0 = \frac{1}{T}\int_T x(t)\,dt = \frac{1}{2}\left[\int_0^1 1\,dt + \int_1^2 (-1)\,dt\right] = \frac{1}{2}(1 - 1) = \boxed{0}$$

**Physical meaning:** $a_0$ is the **average (DC) value** of $x(t)$ over one period. The signal spends equal time at $+1$ and $-1$, so its average is zero.

### Part (b): General $a_k$ for $k \neq 0$ (8 pts)

**Step 1:** Set up the analysis integral, integrating only where $x(t) \neq 0$:

$$a_k = \frac{1}{2}\left[\int_0^1 (1)\,e^{-jk\pi t}\,dt + \int_1^2 (-1)\,e^{-jk\pi t}\,dt\right]$$

**Step 2:** Evaluate each integral using $\int e^{at}\,dt = \frac{1}{a}e^{at}$:

- Term 1: $\int_0^1 e^{-jk\pi t}\,dt = \left[\frac{e^{-jk\pi t}}{-jk\pi}\right]_0^1 = \frac{e^{-jk\pi} - 1}{-jk\pi} = \frac{1 - e^{-jk\pi}}{jk\pi}$

- Term 2: $-\int_1^2 e^{-jk\pi t}\,dt = -\left[\frac{e^{-jk\pi t}}{-jk\pi}\right]_1^2 = \frac{e^{-j2k\pi} - e^{-jk\pi}}{jk\pi}$

**Step 3:** Simplify using $e^{-j2k\pi} = 1$ for any integer $k$:

Term 2 becomes $\frac{1 - e^{-jk\pi}}{jk\pi}$, which is identical to Term 1. Combining:

$$a_k = \frac{1}{2}\left(2 \cdot \frac{1 - e^{-jk\pi}}{jk\pi}\right) = \frac{1 - e^{-jk\pi}}{jk\pi}$$

**Step 4:** Use the hint $e^{-jk\pi} = (-1)^k$:

$$\boxed{a_k = \frac{1 - (-1)^k}{jk\pi}}$$

- $k$ **even:** $1 - (1) = 0$, so $a_k = 0$.
- $k$ **odd:** $1 - (-1) = 2$, so $a_k = \frac{2}{jk\pi} = \frac{-2j}{k\pi}$.

### Part (c): Numerical magnitudes (4 pts)

For odd $k$: $|a_k| = \left|\frac{-2j}{k\pi}\right| = \frac{2}{|k|\pi}$.

| $k$ | $|a_k|$ |
|---|---|
| 1 | $2/\pi \approx 0.637$ |
| 2 | $0$ (even $k$) |
| 3 | $2/(3\pi) \approx 0.212$ |

The magnitudes decay as $1/k$. This is consistent with signals that have **jump discontinuities** — coefficients decay as $O(1/k)$. Smoother signals (e.g., triangular wave) decay faster ($1/k^2$).

### Part (d): Parseval's theorem (3 pts)

**Step 1:** Compute average power directly. Since $|x(t)|^2 = 1$ everywhere:

$$P = \frac{1}{T}\int_T |x(t)|^2\,dt = \frac{1}{2}\int_0^2 1\,dt = \boxed{1}$$

**Step 2:** Verify via coefficients. Only odd $k$ are nonzero, with $|a_k|^2 = 4/(k^2\pi^2)$:

$$\sum_{k=-\infty}^{\infty} |a_k|^2 = 2\sum_{\substack{k=1,3,5,\ldots}} \frac{4}{k^2\pi^2} = \frac{8}{\pi^2}\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2} = \frac{8}{\pi^2}\cdot\frac{\pi^2}{8} = 1 \quad \checkmark$$

---

## Problem 2 (25 pts): Fourier Transform Properties and Convolution

### Given

$x(t) = e^{-3t}u(t)$, so $X(j\omega) = \frac{1}{3 + j\omega}$.

### Part (a): Time-shifting property (5 pts)

**Step 1:** Recognize $y(t) = e^{-3(t-4)}u(t-4) = x(t-4)$, with $t_0 = 4$.

**Step 2:** Apply time-shifting property $x(t - t_0) \leftrightarrow e^{-j\omega t_0}X(j\omega)$:

$$\boxed{Y(j\omega) = \frac{e^{-j4\omega}}{3 + j\omega}}$$

**Step 3:** Show $|Y(j\omega)| = |X(j\omega)|$:

$$|Y(j\omega)| = |e^{-j4\omega}| \cdot |X(j\omega)| = 1 \cdot |X(j\omega)| = |X(j\omega)| \quad \checkmark$$

Time shifting only adds a linear phase $-4\omega$; $|e^{-j4\omega}| = 1$ for all $\omega$.

### Part (b): Frequency-shifting property (5 pts)

**Step 1:** Write $\cos(8t)$ using Euler's formula:

$$\cos(8t) = \frac{1}{2}e^{j8t} + \frac{1}{2}e^{-j8t}$$

**Step 2:** Apply frequency-shifting property $e^{j\omega_0 t}x(t) \leftrightarrow X(j(\omega - \omega_0))$ to each term:

$$\boxed{Z(j\omega) = \frac{1}{2}\cdot\frac{1}{3 + j(\omega - 8)} + \frac{1}{2}\cdot\frac{1}{3 + j(\omega + 8)}}$$

### Part (c): Convolution property (7 pts)

**Step 1:** Compute $H(j\omega)$ from $h(t) = 6e^{-5t}u(t)$:

$$H(j\omega) = \frac{6}{5 + j\omega}$$

**(i)** Output spectrum:

$$Y(j\omega) = X(j\omega) \cdot H(j\omega) = \frac{1}{3+j\omega} \cdot \frac{6}{5+j\omega} = \frac{6}{(3+j\omega)(5+j\omega)}$$

**(ii)** Set up partial fractions:

$$\frac{6}{(3+j\omega)(5+j\omega)} = \frac{A}{3+j\omega} + \frac{B}{5+j\omega}$$

**(iii)** Cover-up method:
- Set $j\omega = -3$: $6 = A(5-3) = 2A$ → $\boxed{A = 3}$
- Set $j\omega = -5$: $6 = B(3-5) = -2B$ → $\boxed{B = -3}$

$$Y(j\omega) = \frac{3}{3+j\omega} - \frac{3}{5+j\omega}$$

### Part (d): Inverse FT (4 pts)

Using $\frac{1}{a+j\omega} \leftrightarrow e^{-at}u(t)$ for $a > 0$:

$$\boxed{y(t) = 3e^{-3t}u(t) - 3e^{-5t}u(t) = 3(e^{-3t} - e^{-5t})\,u(t)}$$

### Part (e): Verification (4 pts)

**Check $y(0)$:** $y(0) = 3(1 - 1) = 0$. Consistent: $\int_0^0 (\cdots)\,d\tau = 0$. ✓

**Check $\lim_{t\to\infty} y(t)$:**

$$\lim_{t\to\infty} 3(e^{-3t} - e^{-5t}) = 3(0 - 0) = 0$$

Both $e^{-3t}$ and $e^{-5t}$ decay to zero as $t \to \infty$ since their exponents are negative. ✓

**Verify via convolution integral:**

$$y(t) = \int_0^t 6e^{-5\tau}\cdot e^{-3(t-\tau)}\,d\tau = 6e^{-3t}\int_0^t e^{-2\tau}\,d\tau = 6e^{-3t}\cdot\frac{1-e^{-2t}}{2} = 3e^{-3t} - 3e^{-5t} \quad \checkmark$$

---

## Problem 3 (20 pts): Frequency Response and Filtering

### Given

$h(t) = 4e^{-4t}u(t)$, input $x(t) = 3 + 2\cos(4t) + \cos(20t)$.

### Part (a): $H(j\omega)$ and cutoff frequency (4 pts)

**Step 1:** Compute $H(j\omega)$ from the standard pair $e^{-at}u(t) \leftrightarrow \frac{1}{a+j\omega}$ with $a = 4$:

$$H(j\omega) = \frac{4}{4 + j\omega}$$

**Step 2:** Express in standard first-order lowpass form $\frac{1}{1 + j\omega/\omega_c}$:

$$H(j\omega) = \frac{4}{4 + j\omega} = \frac{1}{1 + j\omega/4}$$

Comparing: $\boxed{\omega_c = 4 \text{ rad/s}}$

**Step 3:** Verify this is the $-3$ dB cutoff frequency.

The **$-3$ dB point** is the frequency where the magnitude drops to $1/\sqrt{2} \approx 0.707$ of its DC (maximum) value. In decibels:

$$20\log_{10}(1/\sqrt{2}) = 20 \times (-0.5)\log_{10}(2) = -10\log_{10}(2) \approx -3.01 \text{ dB}$$

This is why it's called the "$-3$ dB point" — the output power is halved ($1/\sqrt{2}$ in amplitude = $1/2$ in power). It marks the boundary between the passband and the transition/stopband.

> *Ref: Lecture 11 §— RC lowpass $\omega_c = 1/(RC)$ is the $-3$ dB point; Lecture 15 §1 — at cutoff $|H| = 1/\sqrt{2}$.*

Verify for $\omega = \omega_c = 4$:

$$|H(j4)| = \frac{4}{\sqrt{4^2+4^2}} = \frac{4}{\sqrt{32}} = \frac{4}{4\sqrt{2}} = \frac{1}{\sqrt{2}} \approx 0.707 \quad \checkmark \quad (-3 \text{ dB})$$

### Part (b): Evaluate $H(j\omega)$ at input frequencies (8 pts)

**At $\omega = 0$:**
$$H(j0) = \frac{4}{4} = 1, \quad |H| = 1, \quad \angle H = 0°$$

**At $\omega = 4$:**
$$H(j4) = \frac{4}{4+j4} = \frac{1}{1+j}$$

Magnitude: $\frac{1}{\sqrt{1^2+1^2}} = \frac{1}{\sqrt{2}} \approx 0.707$. Phase: $-\arctan(1) = -45°$.

**At $\omega = 20$:**
$$H(j20) = \frac{4}{4+j20} = \frac{1}{1+j5}$$

Magnitude: $\frac{1}{\sqrt{1^2+5^2}} = \frac{1}{\sqrt{26}} \approx 0.196$. Phase: $-\arctan(5) \approx -78.69°$.

| $\omega$ | $H(j\omega)$ | $|H(j\omega)|$ | $\angle H(j\omega)$ |
|---|---|---|---|
| 0 | $1$ | 1 | $0°$ |
| 4 | $\frac{1}{1+j}$ | $\frac{1}{\sqrt{2}} \approx 0.707$ | $-45°$ |
| 20 | $\frac{1}{1+j5}$ | $\frac{1}{\sqrt{26}} \approx 0.196$ | $-78.69°$ |

### Part (c): Output $y(t)$ in trigonometric form (5 pts)

For input $A\cos(\omega t + \phi)$, the output is $A|H(j\omega)|\cos(\omega t + \phi + \angle H(j\omega))$.

- **DC** ($\omega = 0$): $3 \cdot 1 = 3$
- **$\omega = 4$**: $2 \cdot \frac{1}{\sqrt{2}} = \sqrt{2} \approx 1.414$, phase shift $-45°$
- **$\omega = 20$**: $1 \cdot \frac{1}{\sqrt{26}} \approx 0.196$, phase shift $-78.69°$

$$\boxed{y(t) = 3 + \sqrt{2}\cos(4t - 45°) + \frac{1}{\sqrt{26}}\cos(20t - 78.69°)}$$

### Part (d): Relative attenuation and filter type (3 pts)

**Step 1:** Compute ratio of output magnitudes at $\omega = 20$ vs $\omega = 4$:

$$\frac{|H(j20)|}{|H(j4)|} = \frac{1/\sqrt{26}}{1/\sqrt{2}} = \sqrt{\frac{2}{26}} = \frac{1}{\sqrt{13}} \approx 0.277$$

**Step 2:** Convert to dB:

$$20\log_{10}(0.277) \approx \boxed{-11.14 \text{ dB}}$$

The $\omega = 20$ component is attenuated by ~11.1 dB relative to $\omega = 4$.

Since $|H|$ decreases with frequency, this is a **lowpass filter**.

---

## Problem 4 (15 pts): Second-Order System and Bode Plot

### Given

Standard second-order form with $\omega_n = 10$ rad/s, $\zeta = 0.5$:

$$H(j\omega) = \frac{\omega_n^2}{(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2} = \frac{100}{(j\omega)^2 + 10(j\omega) + 100}$$

> *Ref: Lecture 15 §4 — second-order standard form, damping classification, and key frequency values.*

### Part (a): Classification (3 pts)

**Step 1:** Check damping type using $\zeta$ vs 1:

$$\zeta = 0.5 < 1 \implies \boxed{\text{underdamped (complex conjugate poles)}}$$

> *Ref: Lecture 15 §4 — $\zeta < 1$: underdamped, $\zeta = 1$: critically damped, $\zeta > 1$: overdamped.*

**Step 2:** Check for resonance peak — requires $\zeta < 1/\sqrt{2} \approx 0.707$:

$$\zeta = 0.5 < 0.707 \implies \text{resonance peak exists}$$

**Step 3:** Compute resonance frequency:

$$\omega_r = \omega_n\sqrt{1 - 2\zeta^2} = 10\sqrt{1 - 2(0.25)} = 10\sqrt{0.5} = \boxed{7.07 \text{ rad/s}}$$

> *Ref: Lecture 15 §4 — resonance at $\omega_r = \omega_n\sqrt{1-2\zeta^2}$, exists only if $\zeta < 1/\sqrt{2}$.*

### Part (b): Key quantities (5 pts)

**Step 1 — DC gain:** Set $\omega = 0$:

$$|H(j0)| = \frac{100}{100 - 0 + j0} = \frac{100}{100} = \boxed{1 \text{ (0 dB)}}$$

> *Ref: Lecture 15 §4 — DC gain is always 1 for the standard form.*

**Step 2 — Magnitude at $\omega_n$:** Substitute $\omega = \omega_n = 10$:

$$H(j10) = \frac{100}{(j10)^2 + 10(j10) + 100} = \frac{100}{-100 + j100 + 100} = \frac{100}{j100} = -j$$

$$|H(j10)| = |-j| = 1 = \frac{1}{2\zeta} = \frac{1}{2(0.5)} = 1 \implies \boxed{|H(j\omega_n)| = 1 \text{ (0 dB)}}$$

> *Ref: Lecture 15 §4 — at $\omega_n$, $|H| = 1/(2\zeta)$ always. Here $\zeta = 0.5$ gives $|H| = 1$.*

**Step 3 — Percent overshoot** (step response):

$$\%OS = 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}} = 100 \cdot e^{-\pi(0.5)/\sqrt{1 - 0.25}} = 100 \cdot e^{-1.5708/0.8660}$$

$$= 100 \cdot e^{-1.8138} = 100 \times 0.1630 = \boxed{16.3\%}$$

> *Ref: Lecture 15 §5 — %OS $= 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$. Compare HW Problem 6: $\zeta = 0.25$ gave 44.4%.*

**Step 4 — Settling time** (2% criterion):

$$t_s \approx \frac{4}{\zeta\omega_n} = \frac{4}{0.5 \times 10} = \frac{4}{5} = \boxed{0.8 \text{ s}}$$

> *Ref: Lecture 15 §5 — $t_s \approx 4/(\zeta\omega_n)$. Compare HW Problem 6: $\zeta = 0.25$, $\omega_n = 20$ gave $t_s = 0.8$ s also.*

### Part (c): Bode magnitude asymptotes (4 pts)

**Step 1 — Low-frequency asymptote:** As $\omega \to 0$, $|H| \to 1$:

$$\boxed{0 \text{ dB (flat horizontal line)}}$$

**Step 2 — High-frequency slope:** For $\omega \gg \omega_n$, $H \approx \omega_n^2/(j\omega)^2$. Two poles each contribute $-20$ dB/decade:

$$\boxed{-40 \text{ dB/decade}}$$

> *Ref: Lecture 15 §6 — second-order rolloff is $-40$ dB/dec (vs $-20$ dB/dec for first-order).*

**Step 3 — Corner (break) frequency:** Bode asymptote plots use two straight lines:
1. The **low-freq asymptote**: a flat line at 0 dB (from Step 1)
2. The **high-freq asymptote**: a line falling at $-40$ dB/dec (from Step 2)

These two straight lines, if extended, intersect at the **corner frequency** $\omega = \omega_n$. This is the "break point" where the Bode plot transitions from flat to rolling off. For second-order systems, the corner is always at $\omega_n$:

$$\boxed{\omega_{\text{corner}} = \omega_n = 10 \text{ rad/s}}$$

> *This is analogous to the first-order case where the corner is at $\omega_c$ (Problem 3), but here the slope changes from 0 to $-40$ dB/dec instead of $-20$ dB/dec.*

**Step 4 — Resonance peak magnitude:** Since $\zeta = 0.5 < 1/\sqrt{2}$, there is a peak above the asymptote:

$$|H|_{\max} = \frac{1}{2\zeta\sqrt{1-\zeta^2}} = \frac{1}{2(0.5)\sqrt{1 - 0.25}} = \frac{1}{\sqrt{0.75}} = \frac{2}{\sqrt{3}} \approx 1.155$$

$$\boxed{|H|_{\max} \approx 1.25 \text{ dB above asymptote, at } \omega_r \approx 7.07 \text{ rad/s}}$$

> *Note: With $\zeta = 0.5$ the peak is mild (1.25 dB). Compare HW Problem 6: $\zeta = 0.25$ gave a 6.30 dB peak.*

### Part (d): Phase values (3 pts)

**Step 1 — Phase at $\omega_n$:**

$$\boxed{\angle H(j\omega_n) = -90° \text{ (always, regardless of } \zeta\text{)}}$$

*Why:* At $\omega = \omega_n$, the real terms $(j\omega)^2 + \omega_n^2 = -\omega_n^2 + \omega_n^2 = 0$ cancel, leaving only the imaginary damping term $j2\zeta\omega_n^2$ in the denominator. A purely imaginary denominator gives $-90°$.

> *Ref: Lecture 15 §4 — $\angle H = -90°$ at $\omega_n$ is a universal property of the standard form.*

**Step 2 — Limiting phase values:**

- $\omega \to 0$: $H \to \omega_n^2/\omega_n^2 = 1$ (real, positive) → $\boxed{\angle H \to 0°}$
- $\omega \to \infty$: $H \approx \omega_n^2/(j\omega)^2 = -\omega_n^2/\omega^2$ (real, negative) → $\boxed{\angle H \to -180°}$

**Step 3 — Phase transition summary:**

$$0° \xrightarrow{\text{below } \omega_n} -90° \xrightarrow{\text{at } \omega_n} -90° \xrightarrow{\text{above } \omega_n} -180°$$

The rate of phase transition through $-90°$ is controlled by $\zeta$: smaller $\zeta$ → sharper (more abrupt) transition near $\omega_n$.

> *Ref: Lecture 15 §6 — phase goes $0° \to -180°$ through $-90°$ at $\omega_n$. Compare first-order: $0° \to -90°$ (Lecture 15 §3).*
