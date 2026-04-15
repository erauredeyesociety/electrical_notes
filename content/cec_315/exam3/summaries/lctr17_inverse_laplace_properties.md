# Lecture 17 — Inverse Laplace Transform and Properties

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr17-inverse-laplace-properties.pdf`
**Exam coverage:** Exam 3

---

**Lctr 17: Inverse Laplace Transform, Pole-Zero Analysis, and Properties**

Rogelio Gracia Otalvaro
Spring 2026

**Lctr 17: Inverse Laplace Transform, Pole-Zero Analysis, and Properties**

Spring 2026

Focus: Sections 9.3–9.6 (Pages 670–692)

---

## 17.1 The Big Picture

> **Why This Matters**
>
> In Lecture 16 we learned how to go *forward*: given a time-domain signal $x(t)$, compute its Laplace transform $X(s)$ and ROC. In practice, we almost always need to go in the *reverse* direction: given a system's transfer function $H(s)$ (which we get from a differential equation), find the corresponding impulse response $h(t)$.
>
> This lecture covers three essential skills: (1) how to invert the Laplace transform using partial fractions, (2) how to read system behavior directly from pole-zero plots without doing algebra, and (3) the properties of the Laplace transform that let us handle operations like differentiation, convolution, and time shifting algebraically.

**Roadmap:**

1. The inverse Laplace transform via partial fraction expansion.
2. Worked examples: distinct real poles, repeated poles, complex poles.
3. Geometric evaluation of the Fourier transform from pole-zero plots.
4. Properties of the Laplace transform (with ROC implications).
5. Summary table of transform pairs and properties.

## 17.2 The Inverse Laplace Transform

### 17.2.1 The Formal Inversion Integral

The exact inverse is:

$$x(t) = \frac{1}{2\pi j} \int_{\sigma-j\infty}^{\sigma+j\infty} X(s)\, e^{st}\, ds$$

This is a contour integral in the complex plane along a vertical line in the ROC. In this course, we will **never evaluate this integral directly**. Instead, we use a far more practical method.

### 17.2.2 The Practical Method: Partial Fraction Expansion

The strategy is:

1. Express $X(s)$ as a sum of simple terms $\frac{A_i}{s-p_i}$, $\frac{A_i}{(s-p_i)^n}$, etc.
2. Invert each term using the table from Lecture 16.
3. Use the ROC to determine whether each term is right-sided or left-sided.

> **Key Insight**
>
> The ROC tells you which direction each exponential goes. For a pole at $s = p_i$:
>
> - If the ROC is to the **right** of $p_i$: the term is $e^{p_i t} u(t)$ (right-sided).
> - If the ROC is to the **left** of $p_i$: the term is $-e^{p_i t} u(-t)$ (left-sided).
>
> This is the only place where the ROC enters the inversion process, but it is critical.

## 17.3 Example: Distinct Real Poles

> **Inverse Laplace Transform with Distinct Real Poles**
>
> Find $x(t)$ given:
>
> $$X(s) = \frac{2s+6}{(s+1)(s+3)}, \qquad \text{Re}\{s\} > -1$$
>
> **Step 1: Partial fraction expansion.**
>
> $$\frac{2s+6}{(s+1)(s+3)} = \frac{A}{s+1} + \frac{B}{s+3}$$
>
> Multiply both sides by $(s+1)(s+3)$:
>
> $$2s+6 = A(s+3) + B(s+1)$$
>
> **Cover-up method:**
>
> - Set $s = -1$: $2(-1)+6 = A(-1+3) \Rightarrow 4 = 2A \Rightarrow A = 2$.
> - Set $s = -3$: $2(-3)+6 = B(-3+1) \Rightarrow 0 = -2B \Rightarrow B = 0$.
>
> So: $X(s) = \dfrac{2}{s+1} + \dfrac{0}{s+3} = \dfrac{2}{s+1}$
>
> **Step 2: Check the ROC for each pole.**
> The ROC is $\text{Re}\{s\} > -1$. The pole at $s = -1$ has the ROC to its *right*, so the corresponding term is right-sided.
>
> **Step 3: Invert.**
>
> $$\boxed{x(t) = 2\, e^{-t}\, u(t)}$$
>
> **Check:** At $t = 0^+$: $x(0^+) = 2$. From the initial value theorem (which we will see later), $\lim_{s \to \infty} s X(s) = \lim_{s \to \infty} \frac{2s^2 + 6s}{s^2 + 4s + 3} = 2$. ✓

## 17.4 Example: Distinct Real Poles with Mixed ROC

> **Two-Sided Signal from Partial Fractions**
>
> Find $x(t)$ given:
>
> $$X(s) = \frac{5s+17}{(s+1)(s-3)}, \qquad -1 < \text{Re}\{s\} < 3$$
>
> **Step 1: Partial fractions.**
>
> $$\frac{5s+17}{(s+1)(s-3)} = \frac{A}{s+1} + \frac{B}{s-3}$$
>
> - $s = -1$: $5(-1)+17 = A(-1-3) \Rightarrow 12 = -4A \Rightarrow A = -3$.
> - $s = 3$: $5(3)+17 = B(3+1) \Rightarrow 32 = 4B \Rightarrow B = 8$.
>
> So: $X(s) = \dfrac{-3}{s+1} + \dfrac{8}{s-3}$
>
> **Step 2: Determine the direction of each term from the ROC.**
> The ROC is the strip $-1 < \sigma < 3$.
>
> - Pole at $s = -1$: The ROC is to the **right** of this pole $\Rightarrow$ right-sided.
> - Pole at $s = 3$: The ROC is to the **left** of this pole $\Rightarrow$ left-sided.
>
> **Step 3: Invert each term.**
>
> $$\frac{-3}{s+1}\ (\text{right-sided}) \longrightarrow -3\, e^{-t}\, u(t)$$
>
> $$\frac{8}{s-3}\ (\text{left-sided}) \longrightarrow -8\, e^{3t}\, u(-t)$$
>
> $$\boxed{x(t) = -3\, e^{-t}\, u(t) - 8\, e^{3t}\, u(-t)}$$

**Figure:** Pole-zero plot in the $s$-plane showing poles at $s = -1$ (marked with ×) and $s = 3$ (marked with ×). The ROC is the vertical strip between $\sigma = -1$ and $\sigma = 3$ (shaded green), bounded by dashed vertical lines. Labels below the strip indicate "right-sided" (for the pole at $-1$) and "left-sided" (for the pole at $3$).

## 17.5 Example: Repeated Poles

> **Repeated Poles**
>
> Find $x(t)$ given:
>
> $$X(s) = \frac{4s+5}{(s+1)^2 (s+3)}, \qquad \text{Re}\{s\} > -1$$
>
> **Step 1: Partial fraction expansion.**
> For a repeated pole at $s = -1$ of order 2, we need:
>
> $$\frac{4s+5}{(s+1)^2(s+3)} = \frac{A}{s+1} + \frac{B}{(s+1)^2} + \frac{C}{s+3}$$
>
> Multiply through by $(s+1)^2 (s+3)$:
>
> $$4s+5 = A(s+1)(s+3) + B(s+3) + C(s+1)^2$$
>
> **Find $C$:** set $s = -3$: $4(-3)+5 = C(-3+1)^2 = 4C \Rightarrow C = -7/4$.
> **Find $B$:** set $s = -1$: $4(-1)+5 = B(-1+3) = 2B \Rightarrow B = 1/2$.
> **Find $A$:** compare coefficients of $s^2$: $0 = A + C \Rightarrow A = -C = 7/4$.
>
> So:
>
> $$X(s) = \frac{7/4}{s+1} + \frac{1/2}{(s+1)^2} + \frac{-7/4}{s+3}$$
>
> **Step 2:** ROC is $\text{Re}\{s\} > -1$. All poles are at $\sigma \le -1$, so all terms are right-sided.
>
> **Step 3: Invert** using the pair $\dfrac{1}{(s+a)^2} \leftrightarrow t\, e^{-at}\, u(t)$:
>
> $$\boxed{x(t) = \frac{7}{4} e^{-t} u(t) + \frac{1}{2} t\, e^{-t} u(t) - \frac{7}{4} e^{-3t} u(t)}$$

> **Warning**
>
> For repeated poles of order $n$, the partial fraction expansion includes terms $\frac{B_1}{(s-p)}, \frac{B_2}{(s-p)^2}, \ldots, \frac{B_n}{(s-p)^n}$. The inverse of $\frac{1}{(s-p)^k}$ involves $t^{k-1} e^{pt}$, not just $e^{pt}$. Forgetting the lower-order terms $\frac{B_1}{s-p}, \ldots$ is a very common mistake.

## 17.6 Example: Complex Conjugate Poles

> **Complex Poles: Second-Order System**
>
> Find $x(t)$ given:
>
> $$X(s) = \frac{2s}{s^2 + 4s + 13}, \qquad \text{Re}\{s\} > -2$$
>
> **Step 1: Find the poles** by completing the square:
>
> $$s^2 + 4s + 13 = (s+2)^2 + 9 = (s+2)^2 + 3^2$$
>
> Poles are at $s = -2 \pm j3$ (complex conjugate pair with $\sigma_0 = -2$, $\omega_d = 3$).
>
> **Step 2: Rewrite the numerator** in terms of $(s+2)$:
>
> $$2s = 2(s+2) - 4$$
>
> So:
>
> $$X(s) = \frac{2(s+2)}{(s+2)^2 + 9} - \frac{4}{(s+2)^2 + 9} = 2 \cdot \frac{(s+2)}{(s+2)^2 + 3^2} - \frac{4}{3} \cdot \frac{3}{(s+2)^2 + 3^2}$$
>
> **Step 3: Invert** using the pairs:
>
> $$\frac{s+a}{(s+a)^2 + \omega_d^2} \ \overset{\mathcal{L}}{\longleftrightarrow}\ e^{-at} \cos(\omega_d t)\, u(t)$$
>
> $$\frac{\omega_d}{(s+a)^2 + \omega_d^2} \ \overset{\mathcal{L}}{\longleftrightarrow}\ e^{-at} \sin(\omega_d t)\, u(t)$$
>
> $$\boxed{x(t) = \left[2\, e^{-2t} \cos(3t) - \frac{4}{3}\, e^{-2t} \sin(3t)\right] u(t)}$$
>
> This is a damped sinusoid: the $e^{-2t}$ envelope decays (since the real part of the poles is $-2 < 0$), and the oscillation frequency is $\omega_d = 3$ rad/s.

**Figure:** Plot of $x(t) = e^{-2t}\left[2\cos(3t) - \frac{4}{3}\sin(3t)\right] u(t)$ versus $t$. The signal starts at $x(0^+) = 2$, oscillates, and decays toward zero. A red dashed envelope $\pm A e^{-2t}$ bounds the damped oscillation. Horizontal $t$-axis from 0 to 4, vertical axis from $-1$ to $2$.

> **Key Insight**
>
> Complex conjugate poles always come in pairs $s = -\sigma_0 \pm j\omega_d$. They produce **damped sinusoidal** time-domain signals of the form $e^{-\sigma_0 t}\left[A\cos(\omega_d t) + B\sin(\omega_d t)\right] u(t)$. The real part $-\sigma_0$ controls the decay rate; the imaginary part $\omega_d$ controls the oscillation frequency. This is the same behavior we saw in second-order systems in Lecture 15, now derived systematically from the Laplace transform.

## 17.7 Geometric Evaluation from Pole-Zero Plots

### 17.7.1 The Key Formula

Given $X(s)$ in factored form:

$$X(s) = K \frac{\prod_{i=1}^{M} (s - z_i)}{\prod_{i=1}^{N} (s - p_i)}$$

Each factor $(s - z_i)$ or $(s - p_i)$ is a complex number. We can write it in polar form:

$$(s - z_i) = |s - z_i|\, e^{j \angle (s - z_i)}$$

The magnitude and phase of $X(s)$ are therefore:

$$\boxed{|X(s)| = |K| \frac{\prod_{i=1}^{M} |s - z_i|}{\prod_{i=1}^{N} |s - p_i|}} \qquad \boxed{\angle X(s) = \angle K + \sum_{i=1}^{M} \angle (s - z_i) - \sum_{i=1}^{N} \angle (s - p_i)}$$

Geometrically, $|s - p_i|$ is the **distance** from the point $s$ to the pole $p_i$ in the $s$-plane, and $\angle (s - p_i)$ is the **angle** of the vector from $p_i$ to $s$.

### 17.7.2 Evaluating the Frequency Response

To get the frequency response $H(j\omega)$, we evaluate at $s = j\omega$ (points on the $j\omega$-axis):

**Figure:** $s$-plane diagram showing the $j\omega$-axis (vertical) and $\sigma$-axis (horizontal). A zero (○) labeled $z_1$ sits near the origin and a complex conjugate pair of poles (×) labeled $p_1$ and $p_1^*$ are in the left half plane. A test point at $s = j\omega$ is marked on the $j\omega$-axis. Three vectors are drawn: from $z_1$ to $s = j\omega$ (labeled $|s - z_1|$), from $p_1$ to $s = j\omega$ (labeled $|s - p_1|$), and from $p_1^*$ to $s = j\omega$ (labeled $|s - p_1^*|$). The formula annotated is $|H(j\omega)| = |K| \dfrac{|s - z_1|}{|s - p_1| \cdot |s - p_1^*|}$.

> **Key Insight**
>
> **Near a pole:** the denominator vector gets short $\Rightarrow |H|$ gets large (resonance peak).
> **Near a zero:** the numerator vector gets short $\Rightarrow |H|$ gets small (notch/null).
> This gives you a quick qualitative picture of the frequency response by just looking at the pole-zero plot.

### 17.7.3 First-Order System Example

Consider $H(s) = \dfrac{1}{s+a}$ with $a > 0$ (single pole at $s = -a$, no finite zeros):

$$|H(j\omega)| = \frac{1}{|j\omega + a|} = \frac{1}{\sqrt{a^2 + \omega^2}}$$

**Figure:** Plot of $|H(j\omega)| = 1/\sqrt{a^2 + \omega^2}$ for $a = 1, 2, 4$. Three curves are shown: $a = 1$ (solid blue), $a = 2$ (dashed red), and $a = 4$ (dotted green). All curves peak on the $j\omega$-axis at $\omega = 0$, with peak values $1$, $0.5$, and $0.25$ respectively. Horizontal axis $\omega$ ranges from $-10$ to $10$.

When the pole is farther from the $j\omega$-axis (larger $a$), the minimum distance from any point on the $j\omega$-axis to the pole is larger, so the peak magnitude is lower and the response is wider. This connects directly to the bandwidth–decay-rate relationship from Lecture 15.

## 17.8 Properties of the Laplace Transform

In the table below, $x(t) \overset{\mathcal{L}}{\longleftrightarrow} X(s)$ with ROC $R_x$, and $y(t) \overset{\mathcal{L}}{\longleftrightarrow} Y(s)$ with ROC $R_y$.

| Property | Time Domain | $s$-Domain / ROC |
|---|---|---|
| Linearity | $ax(t) + by(t)$ | $aX(s) + bY(s)$, ROC $\supseteq R_x \cap R_y$ |
| Time shifting | $x(t - t_0)$ | $e^{-st_0} X(s)$, ROC $= R_x$ |
| $s$-domain shifting | $e^{s_0 t} x(t)$ | $X(s - s_0)$, ROC $= R_x$ shifted by $\text{Re}\{s_0\}$ |
| Time scaling | $x(at)$, $a > 0$ | $\dfrac{1}{a} X\!\left(\dfrac{s}{a}\right)$, ROC $= a R_x$ |
| Conjugation | $x^*(t)$ | $X^*(s^*)$, ROC $= R_x$ |
| Convolution | $x(t) * y(t)$ | $X(s) \cdot Y(s)$, ROC $\supseteq R_x \cap R_y$ |
| Differentiation in $t$ | $\dfrac{d}{dt} x(t)$ | $s X(s)$, ROC $\supseteq R_x$ |
| Integration in $t$ | $\displaystyle\int_{-\infty}^{t} x(\tau)\, d\tau$ | $\dfrac{1}{s} X(s)$, ROC $\supseteq R_x \cap \{\text{Re}\{s\} > 0\}$ |
| Differentiation in $s$ | $-t\, x(t)$ | $\dfrac{d}{ds} X(s)$, ROC $= R_x$ |

### 17.8.1 Why These Properties Matter

> **Key Insight**
>
> **Convolution $\longleftrightarrow$ Multiplication:** This is the most important property for system analysis. If a system has impulse response $h(t) \leftrightarrow H(s)$ and input $x(t) \leftrightarrow X(s)$, then the output is:
>
> $$y(t) = x(t) * h(t) \ \overset{\mathcal{L}}{\longleftrightarrow}\ Y(s) = X(s) \cdot H(s)$$
>
> Convolution in time becomes multiplication in $s$, the same simplification as the Fourier transform, but now applicable to a much wider class of signals.
>
> **Differentiation $\longleftrightarrow$ Multiplication by $s$:** This is why the Laplace transform turns differential equations into algebraic equations. Each derivative $d/dt$ becomes a multiplication by $s$.

### 17.8.2 Worked Example: Using the $s$-Domain Shift Property

> **Using $s$-Domain Shifting**
>
> Find the Laplace transform of $x(t) = e^{-3t} \cos(5t)\, u(t)$.
>
> **Step 1:** Start with the known pair:
>
> $$\cos(5t)\, u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{s}{s^2 + 25}, \qquad \text{Re}\{s\} > 0$$
>
> **Step 2:** Apply the $s$-domain shift: multiplication by $e^{-3t}$ in time $\Rightarrow$ replace $s$ by $s + 3$ in the transform:
>
> $$e^{-3t} \cos(5t)\, u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{s+3}{(s+3)^2 + 25}, \qquad \text{Re}\{s\} > -3$$
>
> Notice the ROC shifted left by 3: from $\sigma > 0$ to $\sigma > -3$.

### 17.8.3 Worked Example: Using the Differentiation Property

> **Transform of $t\, e^{-2t} u(t)$ via the Differentiation-in-$s$ Property**
>
> **Step 1:** Start with:
>
> $$e^{-2t} u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{1}{s+2}, \qquad \text{Re}\{s\} > -2$$
>
> **Step 2:** Apply the property $-t\, x(t) \leftrightarrow \dfrac{d}{ds} X(s)$:
>
> $$-t\, e^{-2t} u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{d}{ds}\!\left(\frac{1}{s+2}\right) = \frac{-1}{(s+2)^2}$$
>
> **Step 3:** Multiply both sides by $-1$:
>
> $$\boxed{t\, e^{-2t} u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{1}{(s+2)^2}, \qquad \text{Re}\{s\} > -2}$$
>
> This confirms the repeated-pole pair from the table.

## 17.9 The Initial-Value and Final-Value Theorems

These theorems let you extract the behavior of $x(t)$ at $t = 0^+$ and $t \to \infty$ directly from $X(s)$, without inverting.

> **Initial-Value Theorem**
>
> If $x(t) = 0$ for $t < 0$ and $x(t)$ contains no impulses at $t = 0$:
>
> $$\boxed{x(0^+) = \lim_{s \to \infty} s\, X(s)}$$

> **Final-Value Theorem**
>
> If $x(t) = 0$ for $t < 0$ and $x(t)$ has a finite limit as $t \to \infty$ (i.e., all poles of $s X(s)$ have negative real parts):
>
> $$\boxed{x(\infty) = \lim_{s \to 0} s\, X(s)}$$

> **Warning**
>
> The final-value theorem is only valid if $\lim_{t \to \infty} x(t)$ actually exists as a finite number. If $x(t)$ oscillates (poles on the $j\omega$-axis) or grows (poles in the RHP), the theorem gives a **meaningless result**. Always check that $s X(s)$ has all its poles in the open left half-plane before applying it.

> **Initial and Final Value Theorems**
>
> Let $X(s) = \dfrac{10}{s(s+2)(s+5)}$, ROC: $\text{Re}\{s\} > 0$.
>
> **Initial value:**
>
> $$x(0^+) = \lim_{s \to \infty} s \cdot \frac{10}{s(s+2)(s+5)} = \lim_{s \to \infty} \frac{10}{(s+2)(s+5)} = 0$$
>
> **Final value:** Check: $sX(s) = \dfrac{10}{(s+2)(s+5)}$ has poles at $s = -2, -5$ (both in LHP). ✓
>
> $$x(\infty) = \lim_{s \to 0} \frac{10}{(s+2)(s+5)} = \frac{10}{(2)(5)} = 1$$
>
> So $x(t)$ starts at 0 and settles to 1 as $t \to \infty$, a step response that rises from zero to a final value of 1.

## 17.10 Comprehensive Laplace Transform Pairs

| Signal $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $u(t)$ | $\dfrac{1}{s}$ | $\text{Re}\{s\} > 0$ |
| $t\, u(t)$ | $\dfrac{1}{s^2}$ | $\text{Re}\{s\} > 0$ |
| $\dfrac{t^{n-1}}{(n-1)!}\, u(t)$ | $\dfrac{1}{s^n}$ | $\text{Re}\{s\} > 0$ |
| $e^{-at}\, u(t)$ | $\dfrac{1}{s+a}$ | $\text{Re}\{s\} > -\text{Re}\{a\}$ |
| $t\, e^{-at}\, u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\text{Re}\{s\} > -\text{Re}\{a\}$ |
| $e^{-at} \cos(\omega_d t)\, u(t)$ | $\dfrac{s+a}{(s+a)^2 + \omega_d^2}$ | $\text{Re}\{s\} > -a$ |
| $e^{-at} \sin(\omega_d t)\, u(t)$ | $\dfrac{\omega_d}{(s+a)^2 + \omega_d^2}$ | $\text{Re}\{s\} > -a$ |

## 17.11 Summary

1. **Partial fractions** is the practical method for inverting Laplace transforms: decompose $X(s)$ into simple terms, invert each using the table, and use the ROC to determine right-sided vs. left-sided.
2. **Distinct real poles** give pure exponentials. **Repeated poles** give polynomial-times-exponential terms. **Complex poles** give damped sinusoids.
3. The **pole-zero plot** gives geometric insight: the frequency response magnitude is the product of zero-distances divided by the product of pole-distances. Near a pole $\Rightarrow$ large magnitude (resonance). Near a zero $\Rightarrow$ small magnitude (notch).
4. The **convolution property** $(x * h \leftrightarrow XH)$ is the foundation of system analysis. The **differentiation property** $(dx/dt \leftrightarrow sX)$ turns differential equations into algebra.
5. The **initial-** and **final-value theorems** let you check boundary behavior without full inversion.

## 17.12 Common Mistakes to Avoid

1. **Forgetting to use the ROC to assign direction:** Each term in the partial fraction expansion can be right-sided or left-sided. The ROC, not the sign of the pole, determines which.
2. **Incomplete partial fractions for repeated poles:** A pole of order $n$ at $s = p$ requires $n$ terms: $\dfrac{B_1}{s-p}, \dfrac{B_2}{(s-p)^2}, \ldots, \dfrac{B_n}{(s-p)^n}$.
3. **Wrong handling of complex poles:** Never split complex conjugate poles into separate $\dfrac{A}{s-p}$ and $\dfrac{A^*}{s-p^*}$ terms and try to invert them individually with real exponentials. Instead, complete the square and use the cos/sin pairs.
4. **Applying the final-value theorem when it does not apply:** If $sX(s)$ has poles on the $j\omega$-axis or in the RHP, the theorem is invalid. Always check first.
5. **Confusing pole-zero distances with pole-zero locations:** The frequency response depends on *distances from $s = j\omega$ to each pole/zero*, not on the pole/zero locations themselves.

Rogelio Gracia Otalvaro

## Practice Problems Summary

1. **Example (17.3) — Distinct Real Poles:** Find $x(t)$ given $X(s) = \dfrac{2s+6}{(s+1)(s+3)}$, $\text{Re}\{s\} > -1$. Answer: $x(t) = 2 e^{-t} u(t)$.
2. **Example (17.4) — Distinct Real Poles with Mixed ROC:** Find $x(t)$ given $X(s) = \dfrac{5s+17}{(s+1)(s-3)}$, $-1 < \text{Re}\{s\} < 3$. Answer: $x(t) = -3 e^{-t} u(t) - 8 e^{3t} u(-t)$.
3. **Example (17.5) — Repeated Poles:** Find $x(t)$ given $X(s) = \dfrac{4s+5}{(s+1)^2 (s+3)}$, $\text{Re}\{s\} > -1$. Answer: $x(t) = \frac{7}{4} e^{-t} u(t) + \frac{1}{2} t e^{-t} u(t) - \frac{7}{4} e^{-3t} u(t)$.
4. **Example (17.6) — Complex Conjugate Poles:** Find $x(t)$ given $X(s) = \dfrac{2s}{s^2 + 4s + 13}$, $\text{Re}\{s\} > -2$. Answer: $x(t) = \left[2 e^{-2t} \cos(3t) - \frac{4}{3} e^{-2t} \sin(3t)\right] u(t)$.
5. **Example (17.7.3) — First-Order Frequency Response:** Evaluate $|H(j\omega)|$ for $H(s) = \dfrac{1}{s+a}$, $a > 0$. Answer: $|H(j\omega)| = 1/\sqrt{a^2 + \omega^2}$.
6. **Example (17.8.2) — $s$-Domain Shifting:** Find the Laplace transform of $x(t) = e^{-3t} \cos(5t) u(t)$. Answer: $\dfrac{s+3}{(s+3)^2 + 25}$, $\text{Re}\{s\} > -3$.
7. **Example (17.8.3) — Differentiation in $s$:** Derive the Laplace transform of $t\, e^{-2t} u(t)$ using the differentiation-in-$s$ property. Answer: $\dfrac{1}{(s+2)^2}$, $\text{Re}\{s\} > -2$.
8. **Example (17.9) — Initial and Final Value Theorems:** For $X(s) = \dfrac{10}{s(s+2)(s+5)}$, $\text{Re}\{s\} > 0$, find $x(0^+)$ and $x(\infty)$. Answer: $x(0^+) = 0$, $x(\infty) = 1$.
