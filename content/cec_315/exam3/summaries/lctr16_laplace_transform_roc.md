# Lecture 16 — Laplace Transform and Region of Convergence (ROC)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr16-laplace-transform-roc.pdf`
**Exam coverage:** Exam 3

---

**Lctr 16: The Laplace Transform: Definition and Region of Convergence**

Rogelio Gracia Otalvaro
Spring 2026

**Focus:** Sections 9.0–9.2 (Pages 654–670)

---

## 16.1 The Big Picture: Generalizing the Fourier Transform

> **Why This Matters**
>
> In Lectures 12–15 we used the Fourier transform to move between time and frequency domains. This works beautifully when signals have finite energy or when we restrict ourselves to the frequency variable $\omega$. But the Fourier transform has a fundamental limitation: **not all signals of engineering interest have Fourier transforms.**
>
> Consider $x(t) = e^{2t}\,u(t)$, a growing exponential. The integral $\int_0^{\infty} e^{2t}\,e^{-j\omega t}\,dt$ diverges for every $\omega$ because $e^{2t}$ grows without bound. Yet we absolutely need to analyze systems whose natural responses include growing exponentials (e.g., unstable systems, transient responses with initial conditions).
>
> The **Laplace transform** solves this problem by introducing an exponential damping factor $e^{-\sigma t}$ that can tame divergent integrals. This opens the door to analyzing a vastly larger class of signals and systems, including unstable ones, and provides the algebraic machinery we need to solve differential equations with initial conditions.

**Roadmap for this lecture:**

1. Motivate the Laplace transform as a generalization of the Fourier transform.
2. Define the bilateral Laplace transform and the complex variable $s = \sigma + j\omega$.
3. Introduce the Region of Convergence (ROC) and explain why it is essential.
4. Compute Laplace transforms and ROCs for fundamental signal types.
5. State the properties of the ROC that let us determine it without integration.

## 16.2 From Fourier to Laplace: The Key Idea

### 16.2.1 Multiplying by a Convergence Factor

Recall the CT Fourier transform:

$$X(j\omega) = \int_{-\infty}^{+\infty} x(t)\,e^{-j\omega t}\,dt$$

This integral converges if $x(t)$ is absolutely integrable: $\int |x(t)|\,dt < \infty$. For signals that grow, the integral diverges.

**The fix:** multiply $x(t)$ by a real exponential $e^{-\sigma t}$ before taking the Fourier transform. If we choose $\sigma$ large enough, the product $x(t)\,e^{-\sigma t}$ can be made to decay, making the integral converge:

$$\underbrace{\int_{-\infty}^{+\infty} \left[x(t)\,e^{-\sigma t}\right] e^{-j\omega t}\,dt}_{\text{Fourier transform of }x(t)\,e^{-\sigma t}} = \int_{-\infty}^{+\infty} x(t)\,e^{-(\sigma + j\omega)t}\,dt$$

Now define the complex variable:

$$\boxed{\,s = \sigma + j\omega\,}$$

The integral becomes:

$$\boxed{\,X(s) = \int_{-\infty}^{+\infty} x(t)\,e^{-st}\,dt\,}$$

This is the **bilateral (two-sided) Laplace transform** of $x(t)$.

> **Key Insight**
>
> The Laplace transform is simply the Fourier transform of $x(t)\,e^{-\sigma t}$. The real part $\sigma = \operatorname{Re}\{s\}$ provides the exponential damping that can force convergence. The imaginary part $\omega = \operatorname{Im}\{s\}$ is the same frequency variable from the Fourier transform. When $\sigma = 0$ (i.e., $s = j\omega$), the Laplace transform reduces exactly to the Fourier transform:
>
> $$X(s)\big|_{s=j\omega} = X(j\omega)$$

### 16.2.2 The $s$-Plane

Since $s = \sigma + j\omega$ is a complex number, we can visualize it on a two-dimensional plane called the **$s$-plane**:

*[Figure: The $s$-plane with horizontal axis $\sigma = \operatorname{Re}\{s\}$ and vertical axis $j\omega = \operatorname{Im}\{s\}$. The left half-plane (LHP) has $\sigma < 0$; the right half-plane (RHP) has $\sigma > 0$. A point $s_0 = \sigma_0 + j\omega_0$ is marked in the RHP at coordinates $(\sigma_0, j\omega_0)$. The vertical $j\omega$-axis is highlighted in green and labeled "Fourier transform lives here."]*

The vertical axis ($\sigma = 0$) is the $j\omega$-axis; this is where the Fourier transform lives. The Laplace transform extends the analysis to the entire complex plane, which is why it can handle a broader class of signals.

## 16.3 The Bilateral Laplace Transform: Formal Definition

> **The Laplace Transform Pair**
>
> **Analysis (forward transform):**
>
> $$X(s) = \int_{-\infty}^{+\infty} x(t)\,e^{-st}\,dt$$
>
> **Synthesis (inverse transform):**
>
> $$x(t) = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} X(s)\,e^{st}\,ds$$
>
> where the integration is along a vertical line $\operatorname{Re}\{s\} = \sigma$ that lies in the ROC.
> **Notation:** $x(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; X(s)$

> **Warning**
>
> The Laplace transform $X(s)$ alone does **not** uniquely specify $x(t)$. You must also specify the **Region of Convergence (ROC)**, the set of values of $s$ for which the integral converges. Different signals can have the same algebraic expression for $X(s)$ but different ROCs, corresponding to completely different time-domain signals. This is the single most important conceptual point of this lecture.

## 16.4 Computing Laplace Transforms: Fundamental Examples

### 16.4.1 Right-Sided Exponential: $x(t) = e^{-at}\,u(t)$

> **Laplace Transform of $e^{-at}\,u(t)$**
>
> **Step 1:** Write the integral. Since $u(t) = 0$ for $t < 0$:
>
> $$X(s) = \int_0^{\infty} e^{-at}\,e^{-st}\,dt = \int_0^{\infty} e^{-(s+a)t}\,dt$$
>
> **Step 2:** Evaluate. The integral of $e^{-\alpha t}$ from $0$ to $\infty$ converges if and only if $\operatorname{Re}\{\alpha\} > 0$. Here $\alpha = s + a$, so we need $\operatorname{Re}\{s + a\} > 0$, i.e., $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$.
>
> When this condition holds:
>
> $$X(s) = \left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_0^{\infty} = 0 - \frac{1}{-(s+a)} = \frac{1}{s+a}$$
>
> **Step 3:** State the ROC.
>
> $$\boxed{\,e^{-at}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s+a}, \qquad \operatorname{Re}\{s\} > -\operatorname{Re}\{a\}\,}$$
>
> For example, if $a$ is real and positive (say $a = 3$):
>
> $$e^{-3t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s+3}, \qquad \operatorname{Re}\{s\} > -3$$
>
> The ROC is the **right half of the $s$-plane** to the right of $\sigma = -3$.

*[Figure: Left — time-domain plot of $x(t) = e^{-3t}\,u(t)$, a decaying exponential starting at $x(0) = 1$ for $t \geq 0$ and zero for $t < 0$. Right — $s$-plane with a pole marked at $s = -3$ on the $\sigma$-axis. The ROC is the shaded right half-plane $\operatorname{Re}\{s\} > -3$, to the right of the vertical dashed line at $\sigma = -3$.]*

### 16.4.2 Left-Sided Exponential: $x(t) = -e^{-at}\,u(-t)$

> **Laplace Transform of $-e^{-at}\,u(-t)$**
>
> **Step 1:** Write the integral. Since $u(-t) = 1$ for $t < 0$ and $0$ for $t > 0$:
>
> $$X(s) = \int_{-\infty}^{0} (-1)\,e^{-at}\,e^{-st}\,dt = -\int_{-\infty}^{0} e^{-(s+a)t}\,dt$$
>
> **Step 2:** Evaluate. As $t \to -\infty$, $e^{-(s+a)t} = e^{-(\sigma+a)t}$ grows unless $\sigma + a < 0$, i.e., we need $\operatorname{Re}\{s\} < -\operatorname{Re}\{a\}$.
>
> When this condition holds:
>
> $$X(s) = -\left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_{-\infty}^{0} = -\left(\frac{1}{-(s+a)} - 0\right) = \frac{1}{s+a}$$
>
> **Step 3:** State the ROC.
>
> $$\boxed{\,-e^{-at}\,u(-t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s+a}, \qquad \operatorname{Re}\{s\} < -\operatorname{Re}\{a\}\,}$$

> **Warning**
>
> Look at the algebraic expressions for the two examples: **both** give $X(s) = \frac{1}{s+a}$. The **only** difference is the ROC. This is precisely why the ROC is not optional: without it, $\frac{1}{s+a}$ is ambiguous. It could represent a right-sided decaying exponential *or* a left-sided growing exponential (or other signals if $a$ is complex). **Always state the ROC.**

### 16.4.3 Side-by-Side Comparison

*[Figure: Top — Right-sided signal $e^{-3t}\,u(t)$. Time-domain plot shows a decaying exponential for $t \geq 0$ starting at $1$. $s$-plane shows a pole (×) at $s = -3$ and a shaded ROC of $\sigma > -3$ (right half-plane to the right of the pole).]*

*[Figure: Bottom — Left-sided signal $-e^{-3t}\,u(-t)$. Time-domain plot shows a growing (in magnitude, negative-valued) exponential for $t \leq 0$, reaching approximately $-6$ near $t = -1$. $s$-plane shows a pole (×) at $s = -3$ and a shaded ROC of $\sigma < -3$ (left half-plane to the left of the pole).]*

Both signals have $X(s) = \frac{1}{s+3}$. The pole is at $s = -3$ in both cases. The ROC determines which signal we are talking about.

### 16.4.4 Two-Sided Signal

> **Laplace Transform of a Two-Sided Signal**
>
> Let $x(t) = e^{-3t}\,u(t) + 2e^{2t}\,u(-t)$.
>
> **Step 1:** Use linearity. The Laplace transform of each piece:
>
> $$e^{-3t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s+3}, \qquad \operatorname{Re}\{s\} > -3$$
>
> $$2e^{2t}\,u(-t) = -2 \cdot \left[-e^{2t}\,u(-t)\right] \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{-2}{s-2}, \qquad \operatorname{Re}\{s\} < 2$$
>
> **Step 2:** Add the transforms and intersect the ROCs:
>
> $$X(s) = \frac{1}{s+3} - \frac{2}{s-2}, \qquad -3 < \operatorname{Re}\{s\} < 2$$
>
> **Step 3:** Verify the ROC is nonempty. Since $-3 < 2$, the strip $-3 < \sigma < 2$ is a valid region. If the two boundary values were reversed (e.g., if we needed $\sigma > 5$ and $\sigma < 2$ simultaneously), the ROC would be empty and the Laplace transform would not exist.

*[Figure: $s$-plane showing two poles marked with × — one at $\sigma = -3$ and one at $\sigma = 2$ on the $\sigma$-axis. The ROC is the shaded vertical strip between the two poles, labeled $-3 < \sigma < 2$, bounded by vertical dashed lines at $\sigma = -3$ and $\sigma = 2$.]*

## 16.5 Poles, Zeros, and the $s$-Plane

When $X(s)$ is a **rational function** (ratio of polynomials in $s$), we can factor it as:

$$X(s) = \frac{N(s)}{D(s)} = K\,\frac{(s - z_1)(s - z_2)\cdots(s - z_M)}{(s - p_1)(s - p_2)\cdots(s - p_N)}$$

**Zeros:** values $z_i$ where $X(s) = 0$ (roots of the numerator). Marked with $\circ$ on the $s$-plane.

**Poles:** values $p_i$ where $X(s) \to \infty$ (roots of the denominator). Marked with $\times$ on the $s$-plane.

> **Key Insight**
>
> For rational Laplace transforms, the ROC is always bounded by poles (or extends to $\pm\infty$ in the $\sigma$-direction). The ROC can never contain a pole, because $X(s) \to \infty$ at a pole, meaning the integral diverges there.

## 16.6 Properties of the Region of Convergence

These properties let you determine the ROC from the pole locations and the nature of the signal, *without* computing the integral.

> **ROC Properties (Memorize These)**
>
> **Property 1:** The ROC of $X(s)$ consists of strips parallel to the $j\omega$-axis in the $s$-plane. (The ROC depends only on $\sigma = \operatorname{Re}\{s\}$, not on $\omega$.)
>
> **Property 2:** For rational $X(s)$, the ROC does not contain any poles.
>
> **Property 3:** If $x(t)$ is of **finite duration** and is absolutely integrable, the ROC is the **entire $s$-plane** (possibly excluding $\sigma = \pm\infty$).
>
> **Property 4:** If $x(t)$ is **right-sided** (i.e., $x(t) = 0$ for $t < T_0$ for some finite $T_0$), and if $X(s)$ is rational, then the ROC is the **right half-plane** to the right of the rightmost pole:
>
> $$\text{ROC:}\quad \operatorname{Re}\{s\} > \max_i \operatorname{Re}\{p_i\}$$
>
> **Property 5:** If $x(t)$ is **left-sided** (i.e., $x(t) = 0$ for $t > T_0$), and if $X(s)$ is rational, then the ROC is the **left half-plane** to the left of the leftmost pole:
>
> $$\text{ROC:}\quad \operatorname{Re}\{s\} < \min_i \operatorname{Re}\{p_i\}$$
>
> **Property 6:** If $x(t)$ is **two-sided**, the ROC is a **strip** between two consecutive poles (if it exists at all).
>
> **Property 7:** If the ROC includes the $j\omega$-axis (i.e., $\sigma = 0$ is in the ROC), then the Fourier transform of $x(t)$ exists, and $X(j\omega) = X(s)\big|_{s=j\omega}$.

### 16.6.1 Visual Summary of ROC Types

*[Figure: Three $s$-plane sketches side by side.
(a) Right-sided: pole × on the $\sigma$-axis with a shaded right half-plane ROC labeled $\operatorname{Re}\{s\} > \sigma_{\max}$.
(b) Left-sided: pole × on the $\sigma$-axis with a shaded left half-plane ROC labeled $\operatorname{Re}\{s\} < \sigma_{\min}$.
(c) Two-sided: two poles × on the $\sigma$-axis with a shaded vertical strip between them labeled "strip between poles".]*

## 16.7 More Examples

### 16.7.1 Sum of Two Right-Sided Exponentials

> **Transform of $x(t)$**
>
> **Step 1:** Both terms are right-sided, so we use the known pair for each:
>
> $$3e^{-2t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{3}{s+2}, \qquad \operatorname{Re}\{s\} > -2$$
>
> $$-2e^{-5t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{-2}{s+5}, \qquad \operatorname{Re}\{s\} > -5$$
>
> **Step 2:** Add the transforms and intersect the ROCs:
>
> $$X(s) = \frac{3}{s+2} - \frac{2}{s+5} = \frac{3(s+5) - 2(s+2)}{(s+2)(s+5)} = \frac{s + 11}{(s+2)(s+5)}$$
>
> **Step 3:** The ROC is the intersection of $\sigma > -2$ and $\sigma > -5$, which is:
>
> $$\boxed{\,X(s) = \frac{s+11}{(s+2)(s+5)}, \qquad \operatorname{Re}\{s\} > -2\,}$$
>
> This makes sense: the signal is right-sided (both pieces are), so the ROC is to the right of the rightmost pole ($s = -2$). The zero at $s = -11$ is in the ROC.

### 16.7.2 The Impulse: $x(t) = \delta(t)$

> **Laplace Transform of the Impulse**
>
> Using the sifting property of $\delta(t)$:
>
> $$X(s) = \int_{-\infty}^{+\infty} \delta(t)\,e^{-st}\,dt = e^{-s\cdot 0} = 1$$
>
> $$\boxed{\,\delta(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; 1, \qquad \text{ROC: all } s\,}$$
>
> The impulse has finite duration (it is zero everywhere except $t = 0$), so by Property 3, the ROC is the entire $s$-plane. There are no poles.

### 16.7.3 The Unit Step: $x(t) = u(t)$

This is the special case $e^{-at}\,u(t)$ with $a = 0$:

$$\boxed{\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s}, \qquad \operatorname{Re}\{s\} > 0\,}$$

The pole is at $s = 0$ (on the $j\omega$-axis), and the ROC is the open right half-plane. Since the $j\omega$-axis is *not* in the ROC, the Fourier transform of $u(t)$ does not follow by simply setting $s = j\omega$. (Recall from Lecture 12 that the Fourier transform of $u(t)$ requires a special derivation involving impulses.)

### 16.7.4 A Growing Exponential: $x(t) = e^{2t}\,u(t)$

This is $e^{-at}\,u(t)$ with $a = -2$:

$$X(s) = \frac{1}{s-2}, \qquad \operatorname{Re}\{s\} > 2$$

> **Key Insight**
>
> Here is the power of the Laplace transform: $e^{2t}\,u(t)$ is a growing exponential whose Fourier transform does not exist (the integral diverges for all $\omega$). But the Laplace transform exists for $\operatorname{Re}\{s\} > 2$, because the $e^{-\sigma t}$ factor with $\sigma > 2$ provides enough damping to make $e^{2t}\,e^{-\sigma t} = e^{(2-\sigma)t}$ decay. The Fourier transform does not exist because the $j\omega$-axis ($\sigma = 0$) is *not* in the ROC.

## 16.8 Table of Basic Laplace Transform Pairs

| Signal $x(t)$ | $X(s)$ | ROC |
|---|---|---|
| $\delta(t)$ | $1$ | all $s$ |
| $u(t)$ | $\dfrac{1}{s}$ | $\operatorname{Re}\{s\} > 0$ |
| $-u(-t)$ | $\dfrac{1}{s}$ | $\operatorname{Re}\{s\} < 0$ |
| $e^{-at}\,u(t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$ |
| $-e^{-at}\,u(-t)$ | $\dfrac{1}{s+a}$ | $\operatorname{Re}\{s\} < -\operatorname{Re}\{a\}$ |
| $t\,e^{-at}\,u(t)$ | $\dfrac{1}{(s+a)^2}$ | $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$ |
| $\dfrac{t^{n-1}}{(n-1)!}\,e^{-at}\,u(t)$ | $\dfrac{1}{(s+a)^n}$ | $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$ |
| $\delta(t - t_0)$ | $e^{-st_0}$ | all $s$ |
| $\cos(\omega_0 t)\,u(t)$ | $\dfrac{s}{s^2 + \omega_0^2}$ | $\operatorname{Re}\{s\} > 0$ |
| $\sin(\omega_0 t)\,u(t)$ | $\dfrac{\omega_0}{s^2 + \omega_0^2}$ | $\operatorname{Re}\{s\} > 0$ |

## 16.9 Relationship to the Fourier Transform

> **When does $X(j\omega) = X(s)\big|_{s=j\omega}$?**
>
> This substitution is valid **if and only if** the ROC of $X(s)$ includes the $j\omega$-axis (i.e., $\sigma = 0$ is in the ROC).
>
> **Example:** $e^{-3t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s+3}$, ROC: $\operatorname{Re}\{s\} > -3$.
> Since $\sigma = 0 > -3$, the $j\omega$-axis is in the ROC. Therefore:
>
> $$X(j\omega) = \frac{1}{j\omega + 3}$$
>
> This matches the Fourier transform we computed in Lecture 12.
>
> **Counterexample:** $e^{2t}\,u(t) \;\overset{\mathcal{L}}{\longleftrightarrow}\; \frac{1}{s-2}$, ROC: $\operatorname{Re}\{s\} > 2$.
> Since $\sigma = 0 < 2$, the $j\omega$-axis is *not* in the ROC. The Fourier transform of $e^{2t}\,u(t)$ does *not* exist, so you cannot set $s = j\omega$.

## 16.10 Summary

*[Figure: Flow diagram showing two boxes connected by a bidirectional arrow. Left box: "Fourier Transform, $s = j\omega$ only". Right box: "Laplace Transform, $s = \sigma + j\omega$". The arrow from Fourier to Laplace is labeled "generalize"; the arrow from Laplace to Fourier is labeled "set $\sigma = 0$".]*

Key takeaways from this lecture:

1. The Laplace transform $X(s) = \int_{-\infty}^{+\infty} x(t)\,e^{-st}\,dt$ generalizes the Fourier transform by introducing the complex variable $s = \sigma + j\omega$.
2. The **ROC** (the set of $s$ values where the integral converges) is essential. Without it, $X(s)$ does not uniquely determine $x(t)$.
3. For rational $X(s)$: right-sided signals have ROCs to the right of the rightmost pole; left-sided signals have ROCs to the left of the leftmost pole; two-sided signals have strip ROCs between consecutive poles.
4. The Fourier transform is a special case: $X(j\omega) = X(s)\big|_{s=j\omega}$ when the $j\omega$-axis lies in the ROC.
5. Signals that have no Fourier transform (e.g., growing exponentials, unstable system responses) *can* have Laplace transforms; this is the primary motivation for the generalization.

## 16.11 Common Mistakes to Avoid

1. **Forgetting the ROC:** Writing $X(s) = \frac{1}{s+3}$ without specifying the ROC is *incomplete*. It could represent $e^{-3t}\,u(t)$ or $-e^{-3t}\,u(-t)$.
2. **Confusing the Laplace and Fourier transforms:** The Laplace transform is *not* the Fourier transform with $\omega$ replaced by $s$. The substitution $X(j\omega) = X(s)\big|_{s=j\omega}$ is only valid when the $j\omega$-axis is in the ROC.
3. **Thinking the ROC can contain poles:** By definition, $X(s) \to \infty$ at a pole. The integral cannot converge there.
4. **Getting the ROC direction wrong:** Right-sided signals $\Rightarrow$ ROC to the *right*. Left-sided signals $\Rightarrow$ ROC to the *left*. A useful mnemonic: the ROC points *away* from where the signal has its "problematic" (growing) behavior.

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **Example 16.4.1 — Right-Sided Exponential:** Compute the Laplace transform of $x(t) = e^{-at}\,u(t)$. Result: $X(s) = \frac{1}{s+a}$, ROC $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$. Special case $a = 3$: $e^{-3t}\,u(t) \leftrightarrow \frac{1}{s+3}$, ROC $\operatorname{Re}\{s\} > -3$.
2. **Example 16.4.2 — Left-Sided Exponential:** Compute the Laplace transform of $x(t) = -e^{-at}\,u(-t)$. Result: $X(s) = \frac{1}{s+a}$, ROC $\operatorname{Re}\{s\} < -\operatorname{Re}\{a\}$. Demonstrates that the algebraic expression alone does not identify the signal — the ROC does.
3. **Example 16.4.4 — Two-Sided Signal:** Compute the Laplace transform of $x(t) = e^{-3t}\,u(t) + 2e^{2t}\,u(-t)$. Result: $X(s) = \frac{1}{s+3} - \frac{2}{s-2}$, ROC $-3 < \operatorname{Re}\{s\} < 2$ (a strip).
4. **Example 16.7.1 — Sum of Two Right-Sided Exponentials:** Compute the Laplace transform of $x(t) = 3e^{-2t}\,u(t) - 2e^{-5t}\,u(t)$. Result: $X(s) = \frac{s+11}{(s+2)(s+5)}$, ROC $\operatorname{Re}\{s\} > -2$.
5. **Example 16.7.2 — The Impulse:** Compute the Laplace transform of $x(t) = \delta(t)$. Result: $X(s) = 1$, ROC all $s$.
6. **Example 16.7.3 — The Unit Step:** Compute the Laplace transform of $x(t) = u(t)$. Result: $X(s) = \frac{1}{s}$, ROC $\operatorname{Re}\{s\} > 0$. Note the pole lies on the $j\omega$-axis, so Fourier transform does not follow from $s = j\omega$ substitution.
7. **Example 16.7.4 — A Growing Exponential:** Compute the Laplace transform of $x(t) = e^{2t}\,u(t)$. Result: $X(s) = \frac{1}{s-2}$, ROC $\operatorname{Re}\{s\} > 2$. Illustrates a signal with no Fourier transform but a valid Laplace transform.
8. **Example 16.9 — Fourier from Laplace (valid case):** Given $e^{-3t}\,u(t) \leftrightarrow \frac{1}{s+3}$, ROC $\operatorname{Re}\{s\} > -3$, the $j\omega$-axis is in the ROC, so $X(j\omega) = \frac{1}{j\omega + 3}$.
9. **Example 16.9 — Fourier from Laplace (invalid case):** Given $e^{2t}\,u(t) \leftrightarrow \frac{1}{s-2}$, ROC $\operatorname{Re}\{s\} > 2$, the $j\omega$-axis is not in the ROC, so the Fourier transform does not exist and $s = j\omega$ substitution is invalid.

---

## Worked Examples (from Official Solutions)

**Source:** [hw5_solutions.md](../homework/hw5/hw5_solutions.md) — work through the problems before reading the solutions.

- **Problem 1 (all parts):** Compute Laplace transforms and ROCs for six signal types — every answer must include the ROC.
  - **(a)** $4e^{-2t}u(t)$ — causal exponential (right-sided pair).
  - **(b)** $-3e^{5t}u(-t)$ — anti-causal exponential (left-sided pair, ROC $\sigma < 5$).
  - **(c)** $7\delta(t-3)$ — shifted delta, $X(s) = 7e^{-3s}$, ROC all $s$.
  - **(d)** $t\,e^{-4t}u(t)$ — repeated-pole pair $1/(s+a)^2$.
  - **(e)** $2e^{-t}u(t) - 5e^{-3t}u(t)$ — sum of causal exponentials; ROC is the intersection $\sigma > -1$.
  - **(f)** $e^{-2t}u(t) + 3e^{4t}u(-t)$ — two-sided signal with strip ROC $-2 < \sigma < 4$; Fourier transform exists because the $j\omega$-axis lies inside the strip.

## Instructor Emphasis (from Official Study Guide)

- **"Always state the ROC with every transform."** $1/(s+a)$ alone is ambiguous — could be $e^{-at}u(t)$ or $-e^{-at}u(-t)$.
- ROC = vertical strip, never contains poles; right-sided $\Rightarrow$ right of rightmost pole; left-sided $\Rightarrow$ left of leftmost pole; two-sided $\Rightarrow$ strip between poles.
- Fourier transform exists iff the $j\omega$-axis lies in the ROC.
