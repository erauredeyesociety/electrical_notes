# CEC 315 Homework 5 Solutions — Laplace Transform: Lectures 16–18

**Course:** CEC 315 – Signals and Systems
**Author:**
**Date:**

These solutions are the official instructor solutions transcribed from `hw-lctr16-18-solutions.pdf` (Rogelio Gracia Otalvaro, Spring 2026). Steps and explanatory commentary have been preserved; minor LaTeX/Markdown formatting enhancements have been applied for clarity.

---

## Problem 1: Computing Laplace Transforms and ROCs

### Part (a): $x_1(t) = 4 e^{-2t}\,u(t)$

**Step 1:** Apply the standard pair $e^{-at}\,u(t) \xleftrightarrow{\mathcal{L}} \dfrac{1}{s+a}$, ROC: $\mathrm{Re}\{s\} > -a$.

Here $a = 2$, so:

$$\boxed{\,X_1(s) = \frac{4}{s+2}, \qquad \mathrm{Re}\{s\} > -2\,}$$

---

### Part (b): $x_2(t) = -3 e^{5t}\,u(-t)$

**Step 1:** Rewrite as $-3 \cdot \bigl[-e^{-(-5)t}\,u(-t)\bigr] \cdot (-1)$. Using the pair $-e^{-at}\,u(-t) \xleftrightarrow{\mathcal{L}} \dfrac{1}{s+a}$ with ROC $\mathrm{Re}\{s\} < -a$.

Here $a = -5$:

$$-e^{5t}\,u(-t) \;\xleftrightarrow{\mathcal{L}}\; \frac{1}{s-5}, \qquad \mathrm{Re}\{s\} < 5$$

Multiply by $3$:

$$\boxed{\,X_2(s) = \frac{3}{s-5}, \qquad \mathrm{Re}\{s\} < 5\,}$$

---

### Part (c): $x_3(t) = 7\,\delta(t-3)$

**Step 1:** Use the pair $\delta(t - t_0) \xleftrightarrow{\mathcal{L}} e^{-s t_0}$, ROC: all $s$.

$$\boxed{\,X_3(s) = 7\,e^{-3s}, \qquad \text{ROC: all } s\,}$$

---

### Part (d): $x_4(t) = t\,e^{-4t}\,u(t)$

**Step 1:** Use the pair $t\,e^{-at}\,u(t) \xleftrightarrow{\mathcal{L}} \dfrac{1}{(s+a)^2}$, ROC: $\mathrm{Re}\{s\} > -a$.

With $a = 4$:

$$\boxed{\,X_4(s) = \frac{1}{(s+4)^2}, \qquad \mathrm{Re}\{s\} > -4\,}$$

---

### Part (e): $x_5(t) = 2 e^{-t}\,u(t) - 5 e^{-3t}\,u(t)$

**Step 1:** Transform each term:

$$2 e^{-t}\,u(t) \;\xleftrightarrow{\mathcal{L}}\; \frac{2}{s+1}, \qquad \mathrm{Re}\{s\} > -1$$

$$-5 e^{-3t}\,u(t) \;\xleftrightarrow{\mathcal{L}}\; \frac{-5}{s+3}, \qquad \mathrm{Re}\{s\} > -3$$

**Step 2:** Add and find common denominator:

$$X_5(s) = \frac{2}{s+1} - \frac{5}{s+3} = \frac{2(s+3) - 5(s+1)}{(s+1)(s+3)} = \frac{2s+6-5s-5}{(s+1)(s+3)} = \frac{-3s+1}{(s+1)(s+3)}$$

**Step 3:** ROC is the intersection $\mathrm{Re}\{s\}>-1 \cap \mathrm{Re}\{s\}>-3 = \mathrm{Re}\{s\}>-1$.

$$\boxed{\,X_5(s) = \frac{-3s+1}{(s+1)(s+3)}, \qquad \mathrm{Re}\{s\} > -1\,}$$

**Poles:** $s = -1$ and $s = -3$. **Zero:** $s = 1/3$.

---

### Part (f): $x_6(t) = e^{-2t}\,u(t) + 3 e^{4t}\,u(-t)$

**Step 1:** Transform each term:

$$e^{-2t}\,u(t) \;\xleftrightarrow{\mathcal{L}}\; \frac{1}{s+2}, \qquad \mathrm{Re}\{s\} > -2$$

$$3 e^{4t}\,u(-t) = -3\cdot\bigl[-e^{4t}\,u(-t)\bigr] \;\xleftrightarrow{\mathcal{L}}\; \frac{-3}{s-4}, \qquad \mathrm{Re}\{s\} < 4$$

**Step 2:** Add and find the ROC:

$$X_6(s) = \frac{1}{s+2} - \frac{3}{s-4} = \frac{(s-4) - 3(s+2)}{(s+2)(s-4)} = \frac{-2s-10}{(s+2)(s-4)}$$

**Step 3:** ROC is the intersection $\sigma > -2 \cap \sigma < 4$:

$$\boxed{\,X_6(s) = \frac{-2s-10}{(s+2)(s-4)} = \frac{-2(s+5)}{(s+2)(s-4)}, \qquad -2 < \mathrm{Re}\{s\} < 4\,}$$

**Step 4:** The $j\omega$-axis ($\sigma=0$) lies in the strip $-2 < \sigma < 4$, so the Fourier transform of $x_6(t)$ **does exist**.

> **Key Point.** The Fourier transform exists whenever the $j\omega$-axis is contained in the ROC. For this two-sided signal the ROC is a strip, and $\sigma = 0$ falls inside it.

---

## Problem 2: Inverse Laplace Transform via Partial Fractions

### Part (a): Distinct Real Poles, Right-Sided

Given: $X(s) = \dfrac{3s+5}{(s+1)(s+4)}$, ROC: $\mathrm{Re}\{s\} > -1$.

**Step 1: Partial fractions.**

$$\frac{3s+5}{(s+1)(s+4)} = \frac{A}{s+1} + \frac{B}{s+4}$$

Cover-up:

- $s=-1$: $3(-1)+5 = A(-1+4) \Rightarrow 2 = 3A \Rightarrow A = 2/3$.
- $s=-4$: $3(-4)+5 = B(-4+1) \Rightarrow -7 = -3B \Rightarrow B = 7/3$.

**Step 2: Determine directions.** ROC is $\sigma > -1$. Both poles ($s=-1$ and $s=-4$) are to the left of the ROC boundary, so both terms are right-sided.

**Step 3: Invert.**

$$\boxed{\,x(t) = \tfrac{2}{3}\,e^{-t}\,u(t) + \tfrac{7}{3}\,e^{-4t}\,u(t)\,}$$

**Check:** $x(0^+) = 2/3 + 7/3 = 3$. Initial value theorem: $\displaystyle\lim_{s\to\infty} sX(s) = \lim_{s\to\infty}\frac{3s^2 + 5s}{s^2+5s+4} = 3$. ✓

---

### Part (b): Distinct Real Poles, Two-Sided

Given: $X(s) = \dfrac{2s-4}{(s+2)(s-3)}$, ROC: $-2 < \mathrm{Re}\{s\} < 3$.

**Step 1: Partial fractions.**

$$\frac{2s-4}{(s+2)(s-3)} = \frac{A}{s+2} + \frac{B}{s-3}$$

- $s=-2$: $2(-2)-4 = A(-2-3) \Rightarrow -8 = -5A \Rightarrow A = 8/5$.
- $s=3$: $2(3)-4 = B(3+2) \Rightarrow 2 = 5B \Rightarrow B = 2/5$.

**Step 2: Determine directions from the ROC strip $-2 < \sigma < 3$.**

- Pole at $s = -2$: the ROC is to the **right** of this pole ⇒ right-sided term.
- Pole at $s = 3$: the ROC is to the **left** of this pole ⇒ left-sided term.

**Step 3: Invert.**

$$\frac{8/5}{s+2}\ (\text{right-sided}) \;\longrightarrow\; \tfrac{8}{5}\,e^{-2t}\,u(t)$$

$$\frac{2/5}{s-3}\ (\text{left-sided}) \;\longrightarrow\; -\tfrac{2}{5}\,e^{3t}\,u(-t)$$

$$\boxed{\,x(t) = \tfrac{8}{5}\,e^{-2t}\,u(t) - \tfrac{2}{5}\,e^{3t}\,u(-t)\,}$$

> **Key Point.** The left-sided term uses the pair $\dfrac{1}{s-a}$ with ROC $\sigma < a \;\longleftrightarrow\; -e^{at}\,u(-t)$. That negative sign in front is part of the pair, not an error.

---

### Part (c): Repeated Poles

Given: $X(s) = \dfrac{6}{(s+2)^2(s+5)}$, ROC: $\mathrm{Re}\{s\} > -2$.

**Step 1: Partial fractions.**

$$\frac{6}{(s+2)^2(s+5)} = \frac{A}{s+2} + \frac{B}{(s+2)^2} + \frac{C}{s+5}$$

Multiply through by $(s+2)^2(s+5)$:

$$6 = A(s+2)(s+5) + B(s+5) + C(s+2)^2$$

- **Find $C$:** set $s=-5$: $6 = C(-5+2)^2 = 9C \Rightarrow C = 2/3$.
- **Find $B$:** set $s=-2$: $6 = B(-2+5) = 3B \Rightarrow B = 2$.
- **Find $A$:** compare $s^2$ coefficients: $0 = A + C \Rightarrow A = -C = -2/3$.

**Step 2:** All poles at $\sigma \le -2$, ROC to the right, so all terms are right-sided.

**Step 3: Invert** using $\dfrac{1}{(s+a)^2} \leftrightarrow t\,e^{-at}\,u(t)$:

$$\boxed{\,x(t) = \left[-\tfrac{2}{3}\,e^{-2t} + 2t\,e^{-2t} + \tfrac{2}{3}\,e^{-5t}\right]u(t)\,}$$

**Check:** $x(0^+) = -2/3 + 0 + 2/3 = 0$. Initial value theorem: $\displaystyle\lim_{s\to\infty} sX(s) = \lim_{s\to\infty}\frac{6s}{(s+2)^2(s+5)} = 0$. ✓

---

### Part (d): Complex Conjugate Poles

Given: $X(s) = \dfrac{s+3}{s^2+6s+25}$, ROC: $\mathrm{Re}\{s\} > -3$.

**Step 1: Complete the square.**

$$s^2 + 6s + 25 = (s+3)^2 + 16 = (s+3)^2 + 4^2$$

Poles at $s = -3 \pm j4$. **Damping rate:** $\sigma_0 = 3$. **Oscillation frequency:** $\omega_d = 4$ rad/s.

**Step 2: Rewrite the numerator.**

$$s+3 = (s+3) + 0$$

So:

$$X(s) = \frac{(s+3)}{(s+3)^2 + 4^2}$$

**Step 3: Invert** using $\dfrac{s+a}{(s+a)^2 + \omega_d^2} \leftrightarrow e^{-at}\cos(\omega_d t)\,u(t)$:

$$\boxed{\,x(t) = e^{-3t}\cos(4t)\,u(t)\,}$$

This is a damped sinusoid decaying with time constant $\tau = 1/3$ s, oscillating at $4$ rad/s.

---

## Problem 3: Laplace Transform Properties

### Part (a): $s$-Domain Shift

Given: $\cos(5t)\,u(t) \xleftrightarrow{\mathcal{L}} \dfrac{s}{s^2+25}$, ROC: $\sigma > 0$.

The $s$-domain shift property says: multiplying by $e^{-2t}$ in time replaces $s$ by $s+2$ in the transform.

$$\boxed{\,F(s) = \frac{s+2}{(s+2)^2 + 25}, \qquad \mathrm{Re}\{s\} > -2\,}$$

The ROC shifts from $\sigma > 0$ to $\sigma > 0 - 2 = -2$.

---

### Part (b): Differentiation in Time

Given: $X(s) = \dfrac{1}{s+3}$, ROC: $\sigma > -3$. So $x(t) = e^{-3t}\,u(t)$.

**Step 1:** By the differentiation property:

$$Y(s) = s\,X(s) = \frac{s}{s+3} = 1 - \frac{3}{s+3}$$

(where the last step uses polynomial division: $\dfrac{s}{s+3} = \dfrac{(s+3)-3}{s+3}$).

ROC: $\mathrm{Re}\{s\} > -3$ (at least).

**Step 2: Verify** by computing $y(t) = dx/dt$ explicitly. $x(t) = e^{-3t}\,u(t)$, so:

$$y(t) = \frac{d}{dt}\bigl[e^{-3t}\,u(t)\bigr] = -3 e^{-3t}\,u(t) + e^{-3\cdot 0}\,\delta(t) = -3 e^{-3t}\,u(t) + \delta(t)$$

Taking the Laplace transform of this:

$$Y(s) = \frac{-3}{s+3} + 1 = \frac{-3 + (s+3)}{s+3} = \frac{s}{s+3} \checkmark$$

---

### Part (c): Convolution Property

**Step (i):** $H_1(s) = \dfrac{1}{s+1}$, ROC: $\sigma > -1$. $\quad H_2(s) = \dfrac{3}{s+6}$, ROC: $\sigma > -6$.

**Step (ii):**

$$H(s) = H_1(s)\cdot H_2(s) = \frac{3}{(s+1)(s+6)}, \qquad \mathrm{Re}\{s\} > -1$$

**Step (iii): Partial fractions.**

$$\frac{3}{(s+1)(s+6)} = \frac{A}{s+1} + \frac{B}{s+6}$$

- $s=-1$: $3 = A(5) \Rightarrow A = 3/5$.
- $s=-6$: $3 = B(-5) \Rightarrow B = -3/5$.

$$\boxed{\,h(t) = \tfrac{3}{5}\,e^{-t}\,u(t) - \tfrac{3}{5}\,e^{-6t}\,u(t) = \tfrac{3}{5}\bigl(e^{-t} - e^{-6t}\bigr)u(t)\,}$$

**Check:** $h(0^+) = 3/5 - 3/5 = 0$ ✓ (convolution of two causal signals starts at zero).

---

### Part (d): Initial and Final Value Theorems

Given: $X(s) = \dfrac{8(s+1)}{s(s+2)(s+4)}$, ROC: $\sigma > 0$.

**(i) Initial value:**

$$x(0^+) = \lim_{s\to\infty} s X(s) = \lim_{s\to\infty}\frac{8s(s+1)}{s(s+2)(s+4)} = \lim_{s\to\infty}\frac{8s^2+8s}{s^3+6s^2+8s} = 0$$

$$\boxed{\,x(0^+) = 0\,}$$

**(ii) Final value check:** $sX(s) = \dfrac{8(s+1)}{(s+2)(s+4)}$ has poles at $s=-2$ and $s=-4$, both in the LHP. The theorem applies. ✓

$$x(\infty) = \lim_{s\to 0}\frac{8(s+1)}{(s+2)(s+4)} = \frac{8(1)}{(2)(4)} = 1$$

$$\boxed{\,x(\infty) = 1\,}$$

**(iii) Full inversion.**

$$\frac{8(s+1)}{s(s+2)(s+4)} = \frac{A}{s} + \frac{B}{s+2} + \frac{C}{s+4}$$

- $s=0$: $8(1) = A(2)(4) \Rightarrow A = 1$.
- $s=-2$: $8(-1) = B(-2)(2) \Rightarrow -8 = -4B \Rightarrow B = 2$.
- $s=-4$: $8(-3) = C(-4)(-2) \Rightarrow -24 = 8C \Rightarrow C = -3$.

$$\boxed{\,x(t) = \bigl[1 + 2 e^{-2t} - 3 e^{-4t}\bigr]u(t)\,}$$

**Verify:** $x(0^+) = 1 + 2 - 3 = 0$ ✓. $\quad x(\infty) = 1 + 0 - 0 = 1$ ✓.

---

## Problem 4: System Analysis with $H(s)$

**System:** $\dfrac{d^2 y}{dt^2} + 6\dfrac{dy}{dt} + 8y = 2x(t)$.

### Part (a): System Function

Replace $d^k/dt^k \to s^k$:

$$s^2 Y + 6sY + 8Y = 2X \;\Rightarrow\; H(s) = \frac{2}{s^2 + 6s + 8} = \frac{2}{(s+2)(s+4)}$$

Poles: $s = -2$ and $s = -4$. No finite zeros. Gain constant: $K = 2$.

$$\boxed{\,H(s) = \frac{2}{(s+2)(s+4)}, \qquad \mathrm{Re}\{s\} > -2 \; (\text{causal})\,}$$

---

### Part (b): Pole-Zero Plot and Stability

Pole-zero plot: two poles on the real axis at $s = -2$ and $s = -4$ (both in the open LHP); no finite zeros; the $j\omega$-axis is to the right of both poles.

```
              jω
              │
   × ─────── × ────────── σ
  -4        -2
              │
```

Both poles are in the open LHP ($\mathrm{Re}\{p_i\} < 0$). Since the system is causal, it is **BIBO stable**. ✓

---

### Part (c): Impulse Response

$$\frac{2}{(s+2)(s+4)} = \frac{A}{s+2} + \frac{B}{s+4}$$

- $s=-2$: $2 = A(2) \Rightarrow A = 1$.
- $s=-4$: $2 = B(-2) \Rightarrow B = -1$.

$$\boxed{\,h(t) = \bigl(e^{-2t} - e^{-4t}\bigr)u(t)\,}$$

---

### Part (d): Output for $x(t) = e^{-t}\,u(t)$

**(i)** $X(s) = \dfrac{1}{s+1}$, ROC: $\sigma > -1$.

$$Y(s) = H(s)\cdot X(s) = \frac{2}{(s+1)(s+2)(s+4)}, \qquad \mathrm{Re}\{s\} > -1$$

**(ii) Partial fractions.**

$$\frac{2}{(s+1)(s+2)(s+4)} = \frac{A}{s+1} + \frac{B}{s+2} + \frac{C}{s+4}$$

- $s=-1$: $2 = A(1)(3) \Rightarrow A = 2/3$.
- $s=-2$: $2 = B(-1)(2) \Rightarrow B = -1$.
- $s=-4$: $2 = C(-3)(-2) \Rightarrow C = 1/3$.

$$\boxed{\,y(t) = \left[\tfrac{2}{3}\,e^{-t} - e^{-2t} + \tfrac{1}{3}\,e^{-4t}\right]u(t)\,}$$

**(iii) Verify:**

- $y(0^+) = 2/3 - 1 + 1/3 = 0$ ✓ (initially at rest).
- $y(\infty) = 0$ ✓ (all exponentials decay).
- Final-value theorem: $\displaystyle\lim_{s\to 0} sY(s) = \lim_{s\to 0}\dfrac{2s}{(s+1)(s+2)(s+4)} = 0$ ✓.

---

### Part (e): Stability of $G(s) = 3/(s-1)$

The pole is at $s = 1$ (in the RHP).

**If causal:** ROC is $\mathrm{Re}\{s\} > 1$. The $j\omega$-axis ($\sigma=0$) is **not** in the ROC, so the system is **unstable**. The impulse response $g(t) = 3 e^{t}\,u(t)$ grows without bound.

**If anti-causal (left-sided):** ROC is $\mathrm{Re}\{s\} < 1$. The $j\omega$-axis ($\sigma=0$) **is** in the ROC, so the system is **BIBO stable**. The impulse response $g(t) = -3 e^{t}\,u(-t)$ decays for $t<0$.

> **Key Point.** Stability depends on the ROC, not just the pole location. A pole in the RHP makes a *causal* system unstable, but the same pole is compatible with a stable *anti-causal* system. This is why specifying causality (or the ROC) matters.

---

## Problem 5: The Unilateral Laplace Transform

### Part (a): First-Order IVP

**System:** $y' + 4y = 3 e^{-t}\,u(t)$, $\;y(0^-) = 2$.

**(i) Transform both sides.**

Left side: $\mathcal{L}_u\{y'\} + 4\mathcal{L}_u\{y\} = [sY(s) - y(0^-)] + 4Y(s) = sY - 2 + 4Y$.

Right side: $\mathcal{L}_u\{3e^{-t}u(t)\} = \dfrac{3}{s+1}$.

So:

$$(s+4)Y(s) - 2 = \frac{3}{s+1}$$

**(ii) Solve for $Y(s)$:**

$$Y(s) = \frac{3}{(s+1)(s+4)} + \frac{2}{s+4} = \frac{3 + 2(s+1)}{(s+1)(s+4)} = \frac{2s+5}{(s+1)(s+4)}$$

**(iii) Partial fractions.**

$$\frac{2s+5}{(s+1)(s+4)} = \frac{A}{s+1} + \frac{B}{s+4}$$

- $s=-1$: $2(-1)+5 = A(3) \Rightarrow A = 1$.
- $s=-4$: $2(-4)+5 = B(-3) \Rightarrow B = 1$.

$$\boxed{\,y(t) = \bigl(e^{-t} + e^{-4t}\bigr)u(t)\,}$$

**(iv) Verify:**

- $y(0) = 1 + 1 = 2 = y(0^-)$ ✓.
- $y(\infty) = 0 + 0 = 0$ ✓ (both exponentials decay).
- Extra check: $y'(0^+) = -1 - 4 = -5$. From the ODE: $y'(0^+) = -4y(0) + 3 e^0 = -8 + 3 = -5$ ✓.

---

### Part (b): Second-Order IVP

**System:** $y'' + 3y' + 2y = 0$, $\;y(0^-) = 1$, $\;y'(0^-) = -1$.

**(i) Transform:**

$$\mathcal{L}_u\{y''\} = s^2 Y - s y(0^-) - y'(0^-) = s^2 Y - s + 1$$

$$\mathcal{L}_u\{3 y'\} = 3[sY - y(0^-)] = 3sY - 3$$

$$\mathcal{L}_u\{2 y\} = 2Y$$

Combine:

$$s^2 Y - s + 1 + 3sY - 3 + 2Y = 0$$

$$(s^2 + 3s + 2)Y = s + 2$$

$$Y(s) = \frac{s+2}{s^2+3s+2} = \frac{s+2}{(s+1)(s+2)} = \frac{1}{s+1}$$

**(ii) Invert:**

$$\boxed{\,y(t) = e^{-t}\,u(t)\,}$$

**Verify:** $y(0) = 1$ ✓. $\quad y'(t) = -e^{-t}\,u(t) + \delta(t)$, so $y'(0^-) = -1$ ✓.

**(iii)** The input is zero ($x(t) = 0$), so there is no zero-state response. This is **purely a zero-input response**: the output is entirely due to the initial conditions.

> **Key Point.** The cancellation of the $(s+2)$ factor between numerator and denominator is not a coincidence. It happens because the initial conditions were chosen so that only one of the two natural modes ($e^{-t}$ and $e^{-2t}$) is excited. The IC $y'(0^-) = -1 = -y(0^-)$ exactly suppresses the $e^{-2t}$ mode.

---

### Part (c): ZSR/ZIR Decomposition for Part (a)

From part (a): $Y(s) = \dfrac{2s+5}{(s+1)(s+4)}$.

**Zero-state response** (set $y(0^-) = 0$, keep input):

$$Y_{\text{ZS}}(s) = \frac{3}{(s+1)(s+4)}$$

Partial fractions:

- $s=-1$: $3 = A(3) \Rightarrow A = 1$.
- $s=-4$: $3 = B(-3) \Rightarrow B = -1$.

$$\boxed{\,y_{\text{ZS}}(t) = \bigl(e^{-t} - e^{-4t}\bigr)u(t)\,}$$

**Zero-input response** (set input to 0, keep $y(0^-) = 2$):

$$(s+4)Y_{\text{ZI}} = 2 \;\Rightarrow\; Y_{\text{ZI}}(s) = \frac{2}{s+4}$$

$$\boxed{\,y_{\text{ZI}}(t) = 2 e^{-4t}\,u(t)\,}$$

**Verify the sum:**

$$y_{\text{ZS}}(t) + y_{\text{ZI}}(t) = \bigl(e^{-t} - e^{-4t}\bigr)u(t) + 2 e^{-4t}\,u(t) = \bigl(e^{-t} + e^{-4t}\bigr)u(t) = y(t) \checkmark$$

> **Key Point.** The ZSR starts at zero ($y_{\text{ZS}}(0) = 0$) because the system is initially at rest. The ZIR carries the initial condition ($y_{\text{ZI}}(0) = 2$). Their sum gives the full response.

---

*Rogelio Gracia Otalvaro*

---

## Problem Index

- **Problem 1:** Compute Laplace transforms and ROCs of six signals: causal exponential, anti-causal exponential, shifted delta, $t\,e^{-at}$, sum of two causal exponentials as a rational function, and a two-sided signal.
- **Problem 2:** Inverse Laplace transforms via partial fractions for four cases: distinct real poles causal, distinct real poles two-sided, repeated poles, and complex conjugate poles (completing the square).
- **Problem 3:** Laplace transform properties — $s$-domain shift (damped cosine), differentiation in time, convolution (cascade of two causal exponentials), and initial/final value theorems.
- **Problem 4:** System analysis of a second-order causal LTI ODE: find $H(s)$, plot poles/zeros, check stability, compute $h(t)$, drive with $e^{-t}u(t)$, and analyze a second system $G(s) = 3/(s-1)$ causal vs anti-causal.
- **Problem 5:** Unilateral Laplace transform: first-order IVP, second-order zero-input IVP, and ZSR/ZIR decomposition.
