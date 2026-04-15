# Lecture 20 — Inverse Z-Transform and Z-Transform Properties

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro (verify in PDF)
**Source PDF:** `all_lectures/cec315-lctr20-inverse-z-transform-properties.pdf`
**Exam coverage:** Exam 3

---

## Lctr 20: Inverse z-Transform, Pole-Zero Analysis, and Properties

Rogelio Gracia Otalvaro
Spring 2026

Focus: Sections 10.3–10.6 (Pages 757–774)

---

## 20.1 The Big Picture

### Why This Matters

Lecture 19 taught us how to go forward: from $x[n]$ to $X(z)$. Now we need to go back. Given a system's transfer function $H(z)$ (obtained from a difference equation), how do we find $h[n]$? The method is partial fractions, exactly as with the Laplace transform. The only difference is that we work with $z^{-1}$ instead of $s$, and we use the ROC (circles instead of vertical lines) to assign right-sided vs. left-sided terms.

This lecture also covers the z-transform properties table and geometric evaluation of the frequency response from pole-zero plots in the z-plane.

**Roadmap:**

1. Inverse z-transform via partial fractions (the practical method).
2. Worked examples: distinct real poles, repeated poles, complex poles.
3. Geometric evaluation of the frequency response from the z-plane.
4. Properties of the z-transform.
5. The initial-value theorem for causal sequences.

---

## 20.2 The Inverse z-Transform: Practical Method

### 20.2.1 Strategy

1. Write $X(z)$ as a proper fraction in $z^{-1}$ (degree of numerator $\leq$ degree of denominator in $z^{-1}$). If not proper, perform long division first.
2. Expand into partial fractions of the form $\frac{A_i}{1 - d_i z^{-1}}$.
3. Invert each term using the table pairs. Use the ROC to decide right-sided vs. left-sided.

### Key Insight

The ROC determines the direction, just as in the Laplace transform. For a pole at $z = d_i$:

- **ROC outside** $|d_i|$: the term is $d_i^n u[n]$ (right-sided, causal).
- **ROC inside** $|d_i|$: the term is $-d_i^n u[-n-1]$ (left-sided, anti-causal).

---

## 20.3 Example: Distinct Real Poles, Right-Sided

### Inverse z-Transform: Distinct Real Poles

Find $x[n]$ given:

$$X(z) = \frac{3 - z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.25 z^{-1})}, \qquad |z| > 0.5$$

**Step 1:** Partial fractions in $z^{-1}$.

$$\frac{3 - z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.25 z^{-1})} = \frac{A}{1 - 0.5 z^{-1}} + \frac{B}{1 - 0.25 z^{-1}}$$

Multiply through by the denominator:

$$3 - z^{-1} = A(1 - 0.25 z^{-1}) + B(1 - 0.5 z^{-1})$$

Set $z^{-1} = 1/0.5 = 2$: $3 - 2 = A(1 - 0.5) \Rightarrow 1 = 0.5 A \Rightarrow A = 2$.

Set $z^{-1} = 1/0.25 = 4$: $3 - 4 = B(1 - 2) \Rightarrow -1 = -B \Rightarrow B = 1$.

So:

$$X(z) = \frac{2}{1 - 0.5 z^{-1}} + \frac{1}{1 - 0.25 z^{-1}}$$

**Step 2:** ROC is $|z| > 0.5$. Both poles ($z = 0.5$ and $z = 0.25$) are inside the ROC circle, so both terms are right-sided.

**Step 3:**

$$x[n] = 2 \cdot (0.5)^n u[n] + (0.25)^n u[n]$$

**Check:** $x[0] = 2 + 1 = 3$. From the initial-value theorem: $X(z)|_{z \to \infty} = 3/1 = 3$. ✓

*Figure: Pole-zero plot in the z-plane showing poles at $z = 0.25$ and $z = 0.5$, with the unit circle and the ROC $|z| > 0.5$ (both poles inside $\Rightarrow$ both right-sided).*

---

## 20.4 Example: Mixed ROC (Two-Sided Signal)

### Inverse z-Transform: Two-Sided Signal

Find $x[n]$ given:

$$X(z) = \frac{1}{(1 - 2 z^{-1})(1 - 0.5 z^{-1})}, \qquad 0.5 < |z| < 2$$

**Step 1:** Partial fractions.

$$\frac{1}{(1 - 2 z^{-1})(1 - 0.5 z^{-1})} = \frac{A}{1 - 2 z^{-1}} + \frac{B}{1 - 0.5 z^{-1}}$$

Set $z^{-1} = 0.5$: $1 = A(1 - 0.25) \Rightarrow A = 4/3$.

Set $z^{-1} = 2$: $1 = B(1 - 1) = 0$... this fails because $z^{-1} = 2$ makes $(1 - 2 z^{-1}) = 1 - 4 \neq 0$.

Let us redo. Set $z^{-1} = 1/2$ to kill the $(1 - 2 z^{-1})$ factor: $1 = A(1 - 0.5 \cdot 0.5) = A(0.75)$, so $A = 4/3$.

Set $z^{-1} = 1/0.5 = 2$ to kill $(1 - 0.5 z^{-1})$: $1 = B(1 - 2 \cdot 2) = B(-3)$, so $B = -1/3$.

So:

$$X(z) = \frac{4/3}{1 - 2 z^{-1}} + \frac{-1/3}{1 - 0.5 z^{-1}}$$

**Step 2:** Assign directions from the annular ROC $0.5 < |z| < 2$:

- Pole at $z = 2$ ($|z| = 2$): ROC is inside this pole circle $\Rightarrow$ left-sided.
- Pole at $z = 0.5$ ($|z| = 0.5$): ROC is outside this pole circle $\Rightarrow$ right-sided.

**Step 3:** Invert.

$$\frac{4/3}{1 - 2 z^{-1}} \;\text{(left-sided)} \longrightarrow -\frac{4}{3} \cdot 2^n u[-n-1]$$

$$\frac{-1/3}{1 - 0.5 z^{-1}} \;\text{(right-sided)} \longrightarrow -\frac{1}{3} \cdot (0.5)^n u[n]$$

$$x[n] = -\frac{4}{3} \cdot 2^n u[-n-1] - \frac{1}{3} \cdot (0.5)^n u[n]$$

*Figure: Pole-zero plot showing poles at $z = 0.5$ (right-sided) and $z = 2$ (left-sided), with an annular ROC $0.5 < |z| < 2$ between them.*

---

## 20.5 Example: Repeated Poles

### Repeated Poles

Find $x[n]$ given:

$$X(z) = \frac{1}{(1 - 0.5 z^{-1})^2}, \qquad |z| > 0.5$$

**Step 1:** Use the pair $n a^n u[n] \xleftrightarrow{\mathcal{Z}} \frac{a z^{-1}}{(1 - a z^{-1})^2}$, ROC: $|z| > |a|$.

Rewrite:

$$\frac{1}{(1 - 0.5 z^{-1})^2} = \frac{1}{(1 - 0.5 z^{-1})} \cdot \frac{1}{(1 - 0.5 z^{-1})}$$

We know $\frac{1}{1 - 0.5 z^{-1}} \leftrightarrow (0.5)^n u[n]$, so by the convolution property in the z-domain (multiplication $\leftrightarrow$ convolution):

$$x[n] = (0.5)^n u[n] * (0.5)^n u[n]$$

Alternatively, use the formula directly. Since $\frac{1}{(1 - a z^{-1})^2} = \frac{d}{d(a z^{-1})} \frac{1}{1 - a z^{-1}} \cdot a z^{-1} / a z^{-1}$ ... this gets complicated. A cleaner approach: note that

$$\frac{1}{(1 - a z^{-1})^2} \xleftrightarrow{\mathcal{Z}} (n + 1) a^n u[n]$$

This can be verified by differentiating the geometric series $\sum_{n=0}^{\infty} a^n z^{-n} = \frac{1}{1 - a z^{-1}}$ with respect to $a$.

$$x[n] = (n + 1)(0.5)^n u[n]$$

**Check:** $x[0] = 1 \cdot 1 = 1$, $x[1] = 2 \cdot 0.5 = 1$, $x[2] = 3 \cdot 0.25 = 0.75$. The sequence starts at 1, grows briefly, then decays. ✓

*Figure: Pole-zero plot with a double pole at $z = 0.5$ (order 2) and ROC $|z| > 0.5$ (right-sided).*

---

## 20.6 Example: Complex Conjugate Poles

### Complex Poles: Damped Sinusoid

Find $x[n]$ given:

$$X(z) = \frac{1 - 0.8 \cos(0.4\pi) z^{-1}}{1 - 2 \cdot 0.8 \cos(0.4\pi) z^{-1} + 0.64 z^{-2}}, \qquad |z| > 0.8$$

**Step 1:** Identify the parameters. Comparing with the table pair for $r^n \cos(\omega_0 n) u[n]$:

$$\frac{1 - r \cos(\omega_0) z^{-1}}{1 - 2 r \cos(\omega_0) z^{-1} + r^2 z^{-2}}$$

We read off: $r = 0.8$, $\omega_0 = 0.4\pi$.

The poles are at $z = 0.8 e^{\pm j 0.4\pi}$, both with $|z| = 0.8$.

**Step 2:** Invert.

$$x[n] = (0.8)^n \cos(0.4\pi n) u[n]$$

This is a discrete-time damped sinusoid with envelope $(0.8)^n$ (decays because $r < 1$) and oscillation frequency $\omega_0 = 0.4\pi$ rad/sample.

*Figure: Pole-zero plot with complex conjugate poles at $0.8 e^{\pm j 0.4\pi}$ inside the unit circle; ROC $|z| > 0.8$ (right-sided).*

*Figure: Time-domain plot of $x[n]$ showing damped oscillation with $\pm (0.8)^n$ envelope over $n = 0$ to $20$.*

---

## 20.7 Geometric Evaluation of the Frequency Response

To obtain the frequency response $H(e^{j\omega})$ from the pole-zero plot, evaluate $H(z)$ on the unit circle ($z = e^{j\omega}$).

### 20.7.1 The Key Idea

For $H(z) = K \dfrac{\prod_i (z - z_i)}{\prod_i (z - p_i)}$, each factor $(e^{j\omega} - z_i)$ is a vector from $z_i$ to the point $e^{j\omega}$ on the unit circle:

$$|H(e^{j\omega})| = |K| \frac{\prod_i |e^{j\omega} - z_i|}{\prod_i |e^{j\omega} - p_i|}$$

**Near a pole:** the denominator vector is short $\Rightarrow |H|$ is large (peak).

**Near a zero:** the numerator vector is short $\Rightarrow |H|$ is small (notch).

### 20.7.2 Reading the Frequency Response from the Pole-Zero Plot

*Figure: Pole-zero plot showing a pole $p$ and its conjugate $p^*$ inside the unit circle, with a vector drawn from pole $p$ to the point $e^{j\omega}$ on the unit circle — short vector from pole to $e^{j\omega}$ $\Rightarrow$ large $|H(e^{j\omega})|$.*

### Key Insight

As $\omega$ sweeps from $0$ to $\pi$ (i.e., $z = e^{j\omega}$ moves along the top half of the unit circle from $z = 1$ to $z = -1$):

- At $\omega = 0$, you are at $z = 1$ (DC, the "low-frequency" end).
- At $\omega = \pi$, you are at $z = -1$ (the Nyquist frequency, the "high-frequency" end).
- Whenever $e^{j\omega}$ passes close to a pole, $|H|$ peaks.
- Whenever $e^{j\omega}$ passes close to a zero, $|H|$ dips.

Poles near the unit circle create sharp peaks; poles far from it create broad, gentle bumps. Poles on the unit circle create infinite peaks (marginally stable).

---

## 20.8 Properties of the z-Transform

| Property | Sequence | z-Domain / ROC |
|---|---|---|
| Linearity | $a x_1[n] + b x_2[n]$ | $a X_1(z) + b X_2(z)$, ROC $\supseteq R_1 \cap R_2$ |
| Time shifting | $x[n - n_0]$ | $z^{-n_0} X(z)$, ROC $= R_x$ (possibly add/remove $z = 0, \infty$) |
| z-domain scaling | $z_0^n x[n]$ | $X(z/z_0)$, ROC $= |z_0| \cdot R_x$ |
| Time reversal | $x[-n]$ | $X(z^{-1})$, ROC $= 1/R_x$ |
| Convolution | $x_1[n] * x_2[n]$ | $X_1(z) \cdot X_2(z)$, ROC $\supseteq R_1 \cap R_2$ |
| Differentiation in $z$ | $n \, x[n]$ | $-z \dfrac{d}{dz} X(z)$, ROC $= R_x$ |
| First difference | $x[n] - x[n-1]$ | $(1 - z^{-1}) X(z)$ |
| Accumulation | $\displaystyle\sum_{k=-\infty}^{n} x[k]$ | $\dfrac{1}{1 - z^{-1}} X(z)$, ROC $\supseteq R_x \cap \{|z| > 1\}$ |

### 20.8.1 Most Important Properties

### Key Insight

**Convolution $\leftrightarrow$ Multiplication:** $y[n] = x[n] * h[n] \xleftrightarrow{\mathcal{Z}} Y(z) = X(z) \cdot H(z)$.

This is the foundation of DT system analysis, exactly paralleling the Laplace transform.

**Time shift $\leftrightarrow$ Multiplication by $z^{-n_0}$:** A delay of one sample corresponds to multiplying by $z^{-1}$. This is why $z^{-1}$ is called the "unit delay operator" in signal processing and digital filter design.

### 20.8.2 Worked Example: Time Shifting

### Time Shifting in the z-Domain

Given $x[n] = (0.5)^n u[n] \xleftrightarrow{\mathcal{Z}} \dfrac{1}{1 - 0.5 z^{-1}}$, $|z| > 0.5$.

Find the z-transform of $y[n] = x[n - 3] = (0.5)^{n-3} u[n - 3]$.

By the time-shift property:

$$Y(z) = z^{-3} \cdot \frac{1}{1 - 0.5 z^{-1}} = \frac{z^{-3}}{1 - 0.5 z^{-1}}, \qquad |z| > 0.5$$

The delay of 3 samples introduces the factor $z^{-3}$, which adds 3 zeros at $z = 0$.

### 20.8.3 The Initial-Value Theorem

### Initial-Value Theorem for Causal Sequences

If $x[n] = 0$ for $n < 0$:

$$x[0] = \lim_{z \to \infty} X(z)$$

This is simpler than the Laplace version (no multiplication by $s$). For a proper rational $X(z)$ in $z^{-1}$, the limit as $z \to \infty$ just sets all $z^{-1}$ terms to zero.

### 20.8.4 The Final-Value Theorem

### Final-Value Theorem for Causal Sequences

If $x[n]$ has a finite limit as $n \to \infty$ (i.e., all poles of $(1 - z^{-1}) X(z)$ are strictly inside the unit circle):

$$\lim_{n \to \infty} x[n] = \lim_{z \to 1} (1 - z^{-1}) X(z)$$

### Warning

The final-value theorem is only valid if $\lim_{n \to \infty} x[n]$ actually exists as a finite number. If $x[n]$ oscillates (poles on the unit circle at $z \neq 1$) or grows (poles outside the unit circle), the theorem gives a meaningless result. Always check that $(1 - z^{-1}) X(z)$ has all its poles strictly inside the unit circle before applying it.

Compare with the Laplace version $x(\infty) = \lim_{s \to 0} s X(s)$: the factor $(1 - z^{-1})$ in the z-domain plays the same role as $s$ in the s-domain. Both "cancel" the pole that a step-like signal creates (at $z = 1$ or $s = 0$, respectively).

### Initial and Final Value Theorems

Given: $X(z) = \dfrac{5}{(1 - z^{-1})(1 - 0.6 z^{-1})}$, ROC: $|z| > 1$.

**Initial value:** $x[0] = \lim_{z \to \infty} X(z) = \dfrac{5}{(1)(1)} = 5$.

**Final value check:** $(1 - z^{-1}) X(z) = \dfrac{5}{1 - 0.6 z^{-1}}$, which has a single pole at $z = 0.6$ (inside the unit circle). The theorem applies. ✓

$$x[\infty] = \lim_{z \to 1} (1 - z^{-1}) X(z) = \lim_{z \to 1} \frac{5}{1 - 0.6 z^{-1}} = \frac{5}{1 - 0.6} = \frac{5}{0.4} = 12.5$$

So $x[n]$ starts at $5$ and settles to $12.5$ as $n \to \infty$.

---

## 20.9 Summary

1. Partial fractions in $z^{-1}$ is the practical inversion method. Decompose into $\dfrac{A}{1 - d z^{-1}}$ terms and look up each pair.
2. The ROC determines right-sided vs. left-sided: ROC outside the pole $\Rightarrow d^n u[n]$; ROC inside $\Rightarrow -d^n u[-n-1]$.
3. Complex poles at $z = r e^{\pm j \omega_0}$ produce $r^n \cos(\omega_0 n)$ or $r^n \sin(\omega_0 n)$ responses.
4. The frequency response is read geometrically from the pole-zero plot by sweeping $z = e^{j\omega}$ around the unit circle: short vectors to poles $\Rightarrow$ peaks; short vectors to zeros $\Rightarrow$ notches.
5. The convolution property turns DT convolution sums into algebraic multiplication in the z-domain; the time-shift property makes $z^{-1}$ the unit delay operator.

---

## 20.10 Common Mistakes to Avoid

1. **Doing partial fractions in positive powers of $z$:** Always work in $z^{-1}$. The standard pairs are expressed in $z^{-1}$ form. If you do partial fractions in $z$, you will need extra algebra to convert back.
2. **Wrong direction assignment:** ROC outside the pole $\Rightarrow$ right-sided. ROC inside $\Rightarrow$ left-sided. ("Outside" means $|z|$ is larger than the pole magnitude.)
3. **Forgetting the negative sign for left-sided terms:** The pair is $-a^n u[-n-1]$, not $a^n u[-n-1]$.
4. **Improper fractions:** If the degree of numerator in $z^{-1}$ equals or exceeds the degree of denominator, you must do long division first to extract a polynomial in $z^{-1}$ (which inverts to $\delta$ functions) before applying partial fractions.
5. **Sweeping $\omega$ in the wrong direction:** $\omega = 0$ corresponds to $z = 1$ (not $z = 0$). $\omega = \pi$ corresponds to $z = -1$.

---

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

- **Example (Section 20.3) — Distinct Real Poles, Right-Sided:** Invert $X(z) = \frac{3 - z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.25 z^{-1})}$ with $|z| > 0.5$ using partial fractions to get $x[n] = 2(0.5)^n u[n] + (0.25)^n u[n]$.
- **Example (Section 20.4) — Mixed ROC (Two-Sided Signal):** Invert $X(z) = \frac{1}{(1 - 2 z^{-1})(1 - 0.5 z^{-1})}$ with annular ROC $0.5 < |z| < 2$, producing a two-sided signal with one left-sided and one right-sided term.
- **Example (Section 20.5) — Repeated Poles:** Invert $X(z) = \frac{1}{(1 - 0.5 z^{-1})^2}$ with $|z| > 0.5$ using the repeated-pole pair to get $x[n] = (n+1)(0.5)^n u[n]$.
- **Example (Section 20.6) — Complex Conjugate Poles:** Invert a second-order $X(z)$ with complex conjugate poles at $0.8 e^{\pm j 0.4\pi}$ to get the damped sinusoid $x[n] = (0.8)^n \cos(0.4\pi n) u[n]$.
- **Example (Section 20.8.2) — Time Shifting:** Apply the time-shift property to $x[n] = (0.5)^n u[n]$ with a 3-sample delay to obtain $Y(z) = \frac{z^{-3}}{1 - 0.5 z^{-1}}$.
- **Example (Section 20.8.4) — Initial and Final Value Theorems:** For $X(z) = \frac{5}{(1 - z^{-1})(1 - 0.6 z^{-1})}$, apply both theorems to show $x[0] = 5$ and $x[\infty] = 12.5$.
