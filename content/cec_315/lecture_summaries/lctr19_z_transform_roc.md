# Lecture 19 — Z-Transform and Region of Convergence (ROC)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro (per PDF; original instructions said "Jianhua Liu — verify in PDF")
**Source PDF:** `all_lectures/cec315-lctr19-z-transform-roc.pdf`
**Exam coverage:** Exam 3

---

**Lctr 19: The z-Transform: Definition and Region of Convergence**

Rogelio Gracia Otalvaro
Spring 2026

**Lctr 19: The z-Transform: Definition and Region of Convergence**

Spring 2026

Focus: Sections 10.0–10.2 (Pages 741–757)

---

## 19.1 The Big Picture: The DT Counterpart of the Laplace Transform

### Why This Matters

In Lectures 16–18 we developed the Laplace transform for continuous-time signals. It generalized the CT Fourier transform by replacing $j\omega$ with the complex variable $s = \sigma + j\omega$, letting us analyze signals that the Fourier transform cannot handle (growing exponentials, unstable systems).

We now need the **exact same generalization for discrete time**. The DTFT (from Lecture 12) requires $\sum |x[n]| < \infty$, so a growing sequence like $x[n] = 2^n u[n]$ has no DTFT. The **z-transform** fixes this by introducing a complex variable $z$ that plays the same role in DT that $s$ plays in CT. The parallel is systematic:

| Laplace (CT) | z-Transform (DT) |
|---|---|
| Complex variable $s = \sigma + j\omega$ | Complex variable $z = r e^{j\omega}$ |
| $j\omega$-axis ($\sigma = 0$) | Unit circle ($|z| = 1$) |
| Left/Right half-plane | Inside/outside the unit circle |
| ROC: vertical strip | ROC: annular ring |
| Differential equations $\to$ algebra | Difference equations $\to$ algebra |

Because you already understand the Laplace transform, learning the z-transform is substantially faster. This lecture focuses on what is *different* between the two.

**Roadmap:**

1. Motivate and define the z-transform.
2. Explain the z-plane and the role of the unit circle.
3. Compute z-transforms and ROCs for fundamental DT signals.
4. State the ROC properties.
5. Summarize the complete CT/DT parallel.

## 19.2 From the DTFT to the z-Transform

### 19.2.1 The Convergence Problem

Recall the DTFT from Lecture 12:

$$X(e^{j\omega}) = \sum_{n=-\infty}^{+\infty} x[n]\, e^{-j\omega n}$$

This requires **absolute convergence**: $\sum_{n=-\infty}^{\infty} |x[n]| < \infty$. Many important sequences violate this condition. For instance, $x[n] = 2^n u[n]$ gives $\sum_{n=0}^{\infty} 2^n = \infty$.

### 19.2.2 The Fix: Multiply by a Geometric Damping Factor

In the Laplace transform, we multiplied $x(t)$ by $e^{-\sigma t}$ to force convergence. The DT analog is to multiply $x[n]$ by $r^{-n}$, where $r > 0$ is a real constant. Apply the DTFT to the damped sequence $x[n]\, r^{-n}$:

$$\sum_{n=-\infty}^{+\infty} \bigl[x[n]\, r^{-n}\bigr] e^{-j\omega n} = \sum_{n=-\infty}^{+\infty} x[n]\, \bigl(r\, e^{j\omega}\bigr)^{-n}$$

If we choose $r$ large enough, $x[n]\, r^{-n}$ may decay fast enough for the sum to converge. Now define the complex variable:

$$\boxed{z = r\, e^{j\omega}}$$

where $r = |z|$ is the magnitude and $\omega = \angle z$ is the angle. Substituting gives the z-transform:

$$\boxed{X(z) = \sum_{n=-\infty}^{+\infty} x[n]\, z^{-n}}$$

### Key Insight

The z-transform is the DTFT of $x[n]\, r^{-n}$. When $r = 1$ (i.e., $|z| = 1$), the damping disappears and the z-transform reduces exactly to the DTFT:

$$X(z)\bigr|_{z = e^{j\omega}} = X(e^{j\omega}) \qquad \text{(the DTFT)}$$

The **unit circle** in the z-plane plays the same role as the $j\omega$-axis in the s-plane: it is where the Fourier transform lives.

### 19.2.3 The z-Plane

Since $z = re^{j\omega}$ is complex, we visualize it on the z-plane:

*[Figure: z-plane diagram. Horizontal axis Re{z}, vertical axis Im{z}. A green unit circle of radius 1 labeled "unit circle |z|=1" is centered at the origin, crossing the real axis at $\pm 1$ and the imaginary axis at $\pm j$. A blue point $z_0$ sits outside the unit circle; a dashed line from origin to $z_0$ shows magnitude $r = |z_0|$ and angle $\omega$. Green annotation "DTFT lives here" points at the unit circle. Label "|z| > 1" indicates the region outside the unit circle.]*

Three facts to remember about the z-plane:

1. Points on the unit circle have $|z| = 1$, so $z = e^{j\omega}$. This is where the DTFT lives.
2. $z = 1$ corresponds to $\omega = 0$ (DC). $z = -1$ corresponds to $\omega = \pi$ (Nyquist frequency).
3. Points inside the unit circle have $|z| < 1$; points outside have $|z| > 1$.

## 19.3 Formal Definition

### The z-Transform Pair

**Analysis (forward transform):**

$$X(z) = \sum_{n=-\infty}^{+\infty} x[n]\, z^{-n}$$

**Synthesis (inverse transform):**

$$x[n] = \frac{1}{2\pi j} \oint X(z)\, z^{n-1}\, dz$$

where the contour integral is along a closed path in the ROC that encircles the origin.
**Notation:** $x[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; X(z)$

### Warning

Just as with the Laplace transform, $X(z)$ alone does **not** uniquely determine $x[n]$. The Region of Convergence (ROC), the set of $z$ values where the sum converges absolutely, must also be specified. Different signals can share the same $X(z)$ but have different ROCs.

## 19.4 Fundamental z-Transform Pairs

### 19.4.1 Right-Sided Exponential: $x[n] = a^n u[n]$

#### Right-Sided Geometric Sequence

**Signal:** $x[n] = a^n u[n]$.
**Step 1: Write the sum.** Since $u[n] = 0$ for $n < 0$:

$$X(z) = \sum_{n=0}^{\infty} a^n z^{-n} = \sum_{n=0}^{\infty} \left(\frac{a}{z}\right)^n = \sum_{n=0}^{\infty} (az^{-1})^n$$

**Step 2: Recognize the geometric series.** The sum $\sum_{n=0}^{\infty} w^n = \frac{1}{1-w}$ converges if and only if $|w| < 1$. Here $w = az^{-1} = a/z$, so we need:

$$|az^{-1}| < 1 \;\;\Longleftrightarrow\;\; |z| > |a|$$

When this condition holds:

$$X(z) = \frac{1}{1 - az^{-1}} = \frac{z}{z-a}$$

**Step 3: Identify pole, zero, and ROC.**
Pole at $z = a$, zero at $z = 0$. ROC: $|z| > |a|$ (exterior of a circle of radius $|a|$).

$$\boxed{a^n u[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - az^{-1}} = \frac{z}{z-a}, \qquad |z| > |a|}$$

#### Numerical: Decaying Sequence $a$

With $a = 0.5$:

$$(0.5)^n u[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - 0.5\, z^{-1}}, \qquad |z| > 0.5$$

Pole at $z = 0.5$. The unit circle ($|z| = 1 > 0.5$) is in the ROC, so the DTFT exists.
**Sanity checks:**
At $z = 1$ (DC): $X(1) = \frac{1}{1 - 0.5} = 2$. Direct sum: $\sum_{n=0}^{\infty} (0.5)^n = \frac{1}{1 - 0.5} = 2$. ✓
At $z = -1$ (Nyquist): $X(-1) = \frac{1}{1 + 0.5} = \frac{2}{3}$. Direct sum: $\sum_{n=0}^{\infty} (-0.5)^n = \frac{1}{1.5} = \frac{2}{3}$. ✓

*[Figure: Left panel — stem plot of $x[n] = (0.5)^n u[n]$ with samples at $n = 0, 1, 2, \ldots, 7$; heights decay geometrically: 1, 0.5, 0.25, 0.125, … Right panel — z-plane pole-zero diagram. Green solid unit circle, red dashed circle of radius 0.5 (the ROC boundary), a red X at $z = 0.5$ marking the pole. Shaded region $|z| > 0.5$ is the ROC (exterior of the dashed circle). The unit circle lies inside the ROC.]*

#### Numerical: Growing Sequence $a$

With $a = 2$:

$$2^n u[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - 2z^{-1}}, \qquad |z| > 2$$

Pole at $z = 2$. The unit circle ($|z| = 1$) is *not* in the ROC ($|z| > 2$), so the DTFT does not exist. This makes sense: $\sum_{n=0}^{\infty} 2^n$ diverges, so the sequence is not absolutely summable. This is the power of the z-transform: it can handle sequences whose DTFT does not exist, just as the Laplace transform handles growing exponentials.

### 19.4.2 Left-Sided Exponential: $x[n] = -a^n u[-n-1]$

#### Left-Sided Geometric Sequence

**Signal:** $x[n] = -a^n u[-n-1]$. This equals $-a^n$ for $n \leq -1$ and $0$ for $n \geq 0$.
**Step 1: Write the sum.**

$$X(z) = \sum_{n=-\infty}^{-1} (-a^n)\, z^{-n} = -\sum_{n=-\infty}^{-1} (az^{-1})^n$$

**Step 2: Substitute** $m = -n$ so that $m$ runs from $1$ to $\infty$:

$$X(z) = -\sum_{m=1}^{\infty} (a^{-1} z)^m = -\sum_{m=1}^{\infty} \left(\frac{z}{a}\right)^m$$

This is a geometric series in $w = z/a$, starting at $m = 1$. It converges iff $|z/a| < 1$, i.e., $|z| < |a|$.
**Step 3: Evaluate.** Using $\sum_{m=1}^{\infty} w^m = \frac{w}{1-w}$ for $|w| < 1$:

$$X(z) = -\frac{z/a}{1 - z/a} = -\frac{z}{a - z} = \frac{z}{z - a} = \frac{1}{1 - az^{-1}}$$

$$\boxed{-a^n u[-n-1] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - az^{-1}}, \qquad |z| < |a|}$$

### Warning

The right-sided pair $a^n u[n]$ and the left-sided pair $-a^n u[-n-1]$ produce the **same** algebraic expression $\frac{1}{1-az^{-1}}$. The ROC is the *only* difference:

| Signal | $X(z)$ | ROC |
|---|---|---|
| $a^n u[n]$ | $\dfrac{1}{1 - az^{-1}}$ | $|z| > |a|$ (exterior) |
| $-a^n u[-n-1]$ | $\dfrac{1}{1 - az^{-1}}$ | $|z| < |a|$ (interior) |

Without the ROC, the transform is ambiguous. **Always state the ROC.**

#### Numerical: Left-Sided with $a$

$x[n] = -(3)^n u[-n-1]$. With $a = 3$:

$$X(z) = \frac{1}{1 - 3z^{-1}}, \qquad |z| < 3$$

The signal values are: $x[-1] = -3^{-1} = -1/3$, $x[-2] = -3^{-2} = -1/9$, $x[-3] = -1/27$, $\ldots$
The sequence decays as $n \to -\infty$, which is why it is absolutely summable.
The pole is at $z = 3$ (outside the unit circle). The ROC ($|z| < 3$) *includes* the unit circle, so the DTFT exists. ✓

### 19.4.3 ROC Diagrams: Right-Sided vs. Left-Sided

*[Figure: Two z-plane diagrams side by side. Left diagram ("Right-sided: $|z| > |a|$") — green unit circle, red dashed circle of radius $|a|$ with a red X at $z = a$, shaded exterior region labeled ROC. Right diagram ("Left-sided: $|z| < |a|$") — green unit circle, red dashed circle of radius $|a|$ with red X at $z = a$, shaded interior region labeled ROC.]*

### 19.4.4 The Unit Impulse and Unit Step

#### Unit Impulse and Delayed Impulse

**Unit impulse:** $\delta[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; 1$, ROC: all $z$.
The only nonzero term in the sum is $n = 0$, giving $\delta[0] \cdot z^0 = 1$.
**Delayed impulse:** $\delta[n - k] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; z^{-k}$, ROC: $|z| > 0$ (for $k \geq 1$).
Each unit of delay contributes a factor of $z^{-1}$. A delay of $k$ samples gives $z^{-k}$, which has $k$ zeros at $z = 0$ and a $k$-th order pole at $z = 0$ when viewed as $1/z^k$.

#### Unit Step

The unit step $u[n]$ is the special case $a^n u[n]$ with $a = 1$:

$$u[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - z^{-1}} = \frac{z}{z - 1}, \qquad |z| > 1$$

The pole is at $z = 1$, which sits exactly on the unit circle. The ROC does not include the unit circle (the boundary $|z| = 1$ is excluded by the strict inequality $|z| > 1$), so the DTFT of $u[n]$ cannot be obtained by simply setting $z = e^{j\omega}$ in the z-transform. (Recall from Lecture 12 that the DTFT of $u[n]$ requires a special treatment with impulse terms.)

### 19.4.5 Two-Sided Signals

#### Two-Sided Signal with Annular ROC

**Signal:** $x[n] = (0.5)^n u[n] + 2 \cdot (3)^n u[-n-1]$.
**Step 1: Transform each piece separately.**
Right-sided part:

$$(0.5)^n u[n] \;\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{1}{1 - 0.5 z^{-1}}, \qquad |z| > 0.5$$

Left-sided part: $2 \cdot (3)^n u[-n-1] = -2 \cdot \bigl[-(3)^n u[-n-1]\bigr]$, so:

$$\overset{\mathcal{Z}}{\longleftrightarrow}\; \frac{-2}{1 - 3z^{-1}}, \qquad |z| < 3$$

**Step 2: Add and intersect the ROCs.**

$$X(z) = \frac{1}{1 - 0.5 z^{-1}} - \frac{2}{1 - 3z^{-1}}, \qquad 0.5 < |z| < 3$$

The ROC is the intersection $\{|z| > 0.5\} \cap \{|z| < 3\}$, which is the annular ring $0.5 < |z| < 3$. Since $0.5 < 1 < 3$, the unit circle lies inside this ring, so the DTFT exists. ✓

*[Figure: z-plane diagram. Green solid unit circle, a smaller red dashed circle of radius 0.5 with red X marking pole at $z = 0.5$, a larger blue dashed circle of radius 3 with blue X marking pole at $z = 3$. The annular region between the two dashed circles is shaded green and labeled ROC: $0.5 < |z| < 3$. The unit circle lies inside the shaded annulus.]*

### Key Insight

The ROC for a two-sided signal is a ring $r_1 < |z| < r_2$ between two pole circles. If the inner pole has a larger radius than the outer pole (e.g., requiring $|z| > 5$ and $|z| < 2$ simultaneously), the intersection is empty and the z-transform does not exist.

### 19.4.6 Sum of Two Right-Sided Exponentials

#### Combining Two Right-Sided Terms

**Signal:** $x[n] = 3(0.4)^n u[n] - 2(0.8)^n u[n]$.

**Step 1:** Transform each term:

$$\frac{3}{1 - 0.4 z^{-1}},\; |z| > 0.4 \qquad \text{and} \qquad \frac{-2}{1 - 0.8 z^{-1}},\; |z| > 0.8$$

**Step 2:** Common denominator:

$$X(z) = \frac{3(1 - 0.8 z^{-1}) - 2(1 - 0.4 z^{-1})}{(1 - 0.4 z^{-1})(1 - 0.8 z^{-1})} = \frac{1 - 1.6 z^{-1}}{(1 - 0.4 z^{-1})(1 - 0.8 z^{-1})}$$

**Step 3:** ROC is the intersection $|z| > 0.4 \,\cap\, |z| > 0.8 = |z| > 0.8$.
Poles: $z = 0.4$ and $z = 0.8$. Zero: from $1 - 1.6 z^{-1} = 0$, so $z = 1.6$.
**Check:** $X(1) = \frac{1 - 1.6}{(1 - 0.4)(1 - 0.8)} = \frac{-0.6}{(0.6)(0.2)} = -5$. Direct: $\frac{3}{0.6} - \frac{2}{0.2} = 5 - 10 = -5$. ✓

### 19.4.7 Finite-Duration Sequence

#### Polynomial in $z^{-1}$

**Signal:** $x[n] = \{2, -1, 3, 0, 4\}$ for $n = 0, 1, 2, 3, 4$ (zero elsewhere).

$$X(z) = 2 \cdot z^0 + (-1) \cdot z^{-1} + 3 \cdot z^{-2} + 0 \cdot z^{-3} + 4 \cdot z^{-4} = 2 - z^{-1} + 3 z^{-2} + 4 z^{-4}$$

This is a polynomial in $z^{-1}$. No poles except at $z = 0$ (from the $z^{-4}$ term). By ROC Property 3 (finite-duration sequences), the ROC is all $z \neq 0$.
**Check:** $X(1) = 2 - 1 + 3 + 0 + 4 = 8 = \sum_n x[n]$. ✓
Note: the sum of all samples always equals the z-transform evaluated at $z = 1$, just as $X(0)$ equals the area under $x(t)$ in the CT Fourier transform. This is a useful sanity check.

## 19.5 Poles, Zeros, and the ROC

For rational $X(z)$ (a ratio of polynomials in $z^{-1}$), the ROC is bounded by circles passing through pole locations. The ROC can never contain a pole, because $X(z) \to \infty$ at a pole.

### Key Insight

**Reading a pole-zero plot:**

- Poles ($\times$): values where $X(z) \to \infty$. ROC boundaries are circles through the poles.
- Zeros ($\circ$): values where $X(z) = 0$. Zeros do not affect the ROC.
- In the $z^{-1}$ form $X(z) = \frac{1}{1 - az^{-1}}$, the pole is at $z = a$ (not at $z = 1/a$).
- If $X(z)$ has $N$ poles and $M < N$ finite zeros, there are also $N - M$ zeros at $z = 0$.

## 19.6 Properties of the ROC

### ROC Properties for the z-Transform

**P1:** The ROC is a ring (annulus) centered at the origin: $r_1 < |z| < r_2$.
**P2:** The ROC does not contain any poles.
**P3: Finite-duration** sequences have ROC = entire z-plane (possibly excluding $z = 0$ or $z = \infty$).
**P4: Right-sided** signals with rational $X(z)$: ROC is exterior, $|z| > \max_i |d_i|$.
**P5: Left-sided** signals with rational $X(z)$: ROC is interior, $|z| < \min_i |d_i|$.
**P6: Two-sided** signals: ROC is an annular ring between consecutive pole circles.
**P7:** If the ROC includes the unit circle ($|z| = 1$), the DTFT exists.

## 19.7 The Complete CT/DT Parallel

| | **Laplace ($s$-domain)** | **z-Transform ($z$-domain)** |
|---|---|---|
| Variable | $s = \sigma + j\omega$ | $z = r e^{j\omega}$ |
| Transform | $\displaystyle\int_{-\infty}^{\infty} x(t)\, e^{-st}\, dt$ | $\displaystyle\sum_{n=-\infty}^{\infty} x[n]\, z^{-n}$ |
| FT lives on | $j\omega$-axis ($\sigma = 0$) | unit circle ($|z| = 1$) |
| ROC shape | vertical strip | annular ring |
| Right-sided ROC | $\mathrm{Re}\{s\} > \sigma_{\max}$ | $|z| > r_{\max}$ |
| Left-sided ROC | $\mathrm{Re}\{s\} < \sigma_{\min}$ | $|z| < r_{\min}$ |
| Causal + Stable | all poles in LHP | all poles inside unit circle |
| Basic pair | $e^{-at} u(t) \leftrightarrow \frac{1}{s+a}$ | $a^n u[n] \leftrightarrow \frac{1}{1 - az^{-1}}$ |

## 19.8 Table of Basic z-Transform Pairs

| Signal $x[n]$ | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $\delta[n-k],\; k \geq 0$ | $z^{-k}$ | $|z| > 0$ |
| $u[n]$ | $\dfrac{1}{1 - z^{-1}}$ | $|z| > 1$ |
| $a^n\, u[n]$ | $\dfrac{1}{1 - az^{-1}}$ | $|z| > |a|$ |
| $-a^n\, u[-n-1]$ | $\dfrac{1}{1 - az^{-1}}$ | $|z| < |a|$ |
| $n\, a^n\, u[n]$ | $\dfrac{az^{-1}}{(1 - az^{-1})^2}$ | $|z| > |a|$ |
| $(n+1)\, a^n\, u[n]$ | $\dfrac{1}{(1 - az^{-1})^2}$ | $|z| > |a|$ |
| $r^n \cos(\omega_0 n)\, u[n]$ | $\dfrac{1 - r \cos\omega_0\, z^{-1}}{1 - 2 r \cos\omega_0\, z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |
| $r^n \sin(\omega_0 n)\, u[n]$ | $\dfrac{r \sin\omega_0\, z^{-1}}{1 - 2 r \cos\omega_0\, z^{-1} + r^2 z^{-2}}$ | $|z| > r$ |

## 19.9 Summary

1. The z-transform $X(z) = \sum x[n]\, z^{-n}$ generalizes the DTFT via $z = r e^{j\omega}$. Setting $r = 1$ recovers the DTFT.
2. The ROC is essential: without it, $X(z)$ does not uniquely determine $x[n]$.
3. Right-sided $\Rightarrow$ ROC outside the outermost pole. Left-sided $\Rightarrow$ ROC inside the innermost pole. Two-sided $\Rightarrow$ annular ring between pole circles.
4. The **unit circle** ($|z| = 1$) plays the role of the $j\omega$-axis. DTFT exists iff the unit circle is in the ROC.
5. The structure parallels the Laplace transform exactly, with circles replacing lines and $|z|$ replacing $\mathrm{Re}\{s\}$.

## 19.10 Common Mistakes to Avoid

1. **Omitting the ROC:** $\frac{1}{1 - 0.5 z^{-1}}$ with $|z| > 0.5$ means $(0.5)^n u[n]$, but with $|z| < 0.5$ it means $-(0.5)^n u[-n-1]$.
2. **Confusing "outside" and "inside":** Right-sided signals have ROC *outside* the outermost pole circle. This is different from the Laplace convention ("to the right" of the rightmost pole).
3. **Forgetting that the unit circle replaces the $j\omega$-axis:** The DTFT exists iff the unit circle is in the ROC.
4. **Misidentifying poles:** In $\frac{1}{1 - az^{-1}}$, the pole is at $z = a$, *not* at $z = 1/a$.
5. **Geometric series convergence:** $\sum_{n=0}^{\infty} w^n$ converges iff $|w| < 1$, not just $w < 1$. For complex $w$, the magnitude $|w|$ is what matters.

---

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **§19.4.1 Right-Sided Geometric Sequence** — Derive the z-transform of $x[n] = a^n u[n]$ via the geometric series, identify pole/zero/ROC, yielding $\frac{1}{1 - az^{-1}} = \frac{z}{z-a}$ for $|z| > |a|$.
2. **§19.4.1 Numerical: Decaying Sequence ($a = 0.5$)** — Compute z-transform of $(0.5)^n u[n]$, verify via DC ($z=1$) and Nyquist ($z=-1$) sanity checks.
3. **§19.4.1 Numerical: Growing Sequence ($a = 2$)** — Compute z-transform of $2^n u[n]$, show that the DTFT does not exist because the unit circle is not in the ROC $|z| > 2$.
4. **§19.4.2 Left-Sided Geometric Sequence** — Derive the z-transform of $x[n] = -a^n u[-n-1]$ via substitution $m = -n$, obtain $\frac{1}{1 - az^{-1}}$ with ROC $|z| < |a|$.
5. **§19.4.2 Numerical: Left-Sided with $a = 3$** — Compute z-transform of $-(3)^n u[-n-1]$; show ROC $|z| < 3$ includes the unit circle so the DTFT exists.
6. **§19.4.4 Unit Impulse / Delayed Impulse** — Show $\delta[n] \leftrightarrow 1$ (all $z$) and $\delta[n-k] \leftrightarrow z^{-k}$ ($|z|>0$).
7. **§19.4.4 Unit Step** — Derive $u[n] \leftrightarrow \frac{1}{1 - z^{-1}} = \frac{z}{z-1}$ with ROC $|z| > 1$; note DTFT subtlety since the pole sits on the unit circle.
8. **§19.4.5 Two-Sided Signal with Annular ROC** — Transform $x[n] = (0.5)^n u[n] + 2(3)^n u[-n-1]$; intersect ROCs to obtain annular ring $0.5 < |z| < 3$.
9. **§19.4.6 Combining Two Right-Sided Terms** — Transform $x[n] = 3(0.4)^n u[n] - 2(0.8)^n u[n]$; combine over common denominator, identify poles at $z = 0.4, 0.8$ and zero at $z = 1.6$; verify via $X(1) = -5$.
10. **§19.4.7 Finite-Duration Sequence** — Transform $x[n] = \{2, -1, 3, 0, 4\}$ as a polynomial in $z^{-1}$; ROC is all $z \neq 0$; verify $X(1) = \sum_n x[n] = 8$.
