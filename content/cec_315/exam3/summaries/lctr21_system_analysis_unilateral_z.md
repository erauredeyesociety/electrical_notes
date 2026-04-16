# Lecture 21 — System Analysis Using the Unilateral Z-Transform

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr21-system-analysis-unilateral-z.pdf`
**Exam coverage:** Exam 3

---

## Lctr 21: DT System Analysis and the Unilateral z-Transform

Rogelio Gracia Otalvaro

Spring 2026

**Focus: Sections 10.7–10.9 (Pages 774–796)**

---

## 21.1 The Big Picture

### Why This Matters

This lecture completes the z-transform trilogy by connecting the machinery to DT system analysis. The goals mirror Lecture 18 exactly:

**Part I:** Given a difference equation, find the system function $H(z)$, determine stability and causality, compute the output.

**Part II:** Use the unilateral z-transform to solve difference equations with nonzero initial conditions (the DT analog of solving IVPs with the unilateral Laplace transform).

After this lecture, you have a complete toolkit for both CT and DT system analysis.

**Roadmap:**

1. The system function $H(z)$ from difference equations.
2. Causality and stability in the z-domain.
3. Complete system analysis example.
4. Block diagram representations.
5. The unilateral z-transform and its time-shift property.
6. Solving difference equations with initial conditions.

---

# Part I: System Analysis with H(z)

## 21.2 The System Function H(z)

A causal LTI DT system described by a linear constant-coefficient difference equation:

$$\sum_{k=0}^{N} a_k\, y[n-k] = \sum_{k=0}^{M} b_k\, x[n-k]$$

Taking the bilateral z-transform (zero initial conditions): each delay $y[n-k]$ becomes $z^{-k} Y(z)$, each $x[n-k]$ becomes $z^{-k} X(z)$:

$$\left(\sum_{k=0}^{N} a_k z^{-k}\right) Y(z) = \left(\sum_{k=0}^{M} b_k z^{-k}\right) X(z)$$

$$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{k=0}^{M} b_k z^{-k}}{\sum_{k=0}^{N} a_k z^{-k}} = \frac{b_0 + b_1 z^{-1} + \cdots + b_M z^{-M}}{a_0 + a_1 z^{-1} + \cdots + a_N z^{-N}}$$

### Key Insight

The z-transform converts the difference equation into an algebraic equation: each unit delay $n \to n-1$ becomes multiplication by $z^{-1}$. This is why $z^{-1}$ is called the "delay operator" in digital signal processing.

### Example: From Difference Equation to H(z)

**System:** $y[n] - 0.8\, y[n-1] + 0.15\, y[n-2] = x[n] + 2x[n-1]$

**Step 1:** Replace delays with $z^{-k}$:

$$(1 - 0.8 z^{-1} + 0.15 z^{-2}) Y(z) = (1 + 2 z^{-1}) X(z)$$

**Step 2:** Form $H(z)$:

$$H(z) = \frac{1 + 2 z^{-1}}{1 - 0.8 z^{-1} + 0.15 z^{-2}}$$

**Step 3:** Factor the denominator. We need roots of $1 - 0.8 z^{-1} + 0.15 z^{-2} = 0$, i.e., $z^2 - 0.8 z + 0.15 = 0$:

$$z = \frac{0.8 \pm \sqrt{0.64 - 0.60}}{2} = \frac{0.8 \pm 0.2}{2}$$

$z_1 = 0.5$, $z_2 = 0.3$.

So:

$$H(z) = \frac{1 + 2 z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.3 z^{-1})}$$

**Poles:** $z = 0.5, 0.3$ (both inside the unit circle). **Zero:** from $1 + 2 z^{-1} = 0$, $z = -2$.

---

## 21.3 Causality and Stability

### Causality Criterion

A DT LTI system is causal iff $h[n] = 0$ for $n < 0$, which requires the ROC to be the exterior of a circle: $|z| > r_{\max}$ (outside the outermost pole).

For rational $H(z)$: causality also requires $M \leq N$ (numerator degree $\leq$ denominator degree in $z^{-1}$), or equivalently $H(z) \to$ finite as $z \to \infty$.

### Stability Criterion

A DT LTI system is BIBO stable iff $\sum |h[n]| < \infty$, which requires the ROC to include the unit circle ($|z| = 1$).

### The Golden Rule for Causal DT Systems

A causal LTI DT system with rational $H(z)$ is **BIBO stable if and only if all poles lie strictly inside the unit circle**:

$$\text{Causal + Stable} \iff |p_i| < 1 \ \forall \ \text{poles}\ p_i$$

**Why:** For a causal system, ROC is $|z| > |p_{\max}|$. For the unit circle to be in the ROC, we need $|p_{\max}| < 1$.

*Figure: Two pole-zero plots in the z-plane. Left — "Causal + Stable": all poles (×) lie inside the unit circle $|z| = 1$. Right — "Causal + Unstable": at least one pole lies outside the unit circle.*

### Stability Classification

| $H(z)$ | Poles | $\|p_i\|$ | Causal + Stable? |
|---|---|---|---|
| $\dfrac{1}{1 - 0.5 z^{-1}}$ | $z = 0.5$ | $0.5 < 1$ | Yes |
| $\dfrac{1}{1 - 1.2 z^{-1}}$ | $z = 1.2$ | $1.2 > 1$ | No (unstable) |
| $\dfrac{1}{1 - z^{-1}}$ | $z = 1$ | $1 = 1$ | Marginally stable |
| $\dfrac{1}{(1 - 0.3 z^{-1})(1 + 0.7 z^{-1})}$ | $z = 0.3, -0.7$ | $0.3, 0.7 < 1$ | Yes |

---

## 21.4 Complete System Analysis Pipeline

### Full Pipeline: Difference Equation to Output

**System:** $y[n] - 0.5\, y[n-1] = x[n]$, **Input:** $x[n] = (0.8)^n u[n]$.

**Step 1:** Find $H(z)$.

$$(1 - 0.5 z^{-1}) Y = X \implies H(z) = \frac{1}{1 - 0.5 z^{-1}}, \quad |z| > 0.5$$

Pole at $z = 0.5$ (inside unit circle $\Rightarrow$ causal and stable). ✓

**Step 2:** Find $X(z)$.

$$X(z) = \frac{1}{1 - 0.8 z^{-1}}, \quad |z| > 0.8$$

**Step 3:** Find $Y(z) = H(z) \cdot X(z)$.

$$Y(z) = \frac{1}{(1 - 0.5 z^{-1})(1 - 0.8 z^{-1})}, \quad |z| > 0.8$$

**Step 4:** Partial fractions.

$$\frac{1}{(1 - 0.5 z^{-1})(1 - 0.8 z^{-1})} = \frac{A}{1 - 0.5 z^{-1}} + \frac{B}{1 - 0.8 z^{-1}}$$

Set $z^{-1} = 2$: $1 = A(1 - 1.6) \Rightarrow A = -5/3$.
Set $z^{-1} = 1.25$: $1 = B(1 - 0.625) \Rightarrow B = 8/3$.

**Step 5:** Invert. Both poles inside ROC $\Rightarrow$ both right-sided:

$$y[n] = \left[-\frac{5}{3}(0.5)^n + \frac{8}{3}(0.8)^n\right] u[n]$$

**Step 6:** Verify.

- $y[0] = -5/3 + 8/3 = 3/3 = 1 = x[0]$ ✓ (from the difference equation with $y[-1] = 0$)
- $y[1] = -5/3 \cdot 0.5 + 8/3 \cdot 0.8 = -5/6 + 6.4/3 = -5/6 + 32/15$. From the ODE: $y[1] = 0.5 y[0] + x[1] = 0.5 + 0.8 = 1.3$. Check: $-5/6 + 32/15 = -25/30 + 64/30 = 39/30 = 1.3$ ✓

---

## 21.5 Block Diagram Representations

In the z-domain, the three basic building blocks are:

*Figure: Three basic z-domain building blocks — (1) Unit Delay: input $X(z)$ through a $z^{-1}$ block outputs $z^{-1} X(z)$; (2) Gain: a multiplier block labeled $a$; (3) Adder: a summing junction marked with $+$.*

Every rational $H(z)$ can be implemented as a combination of delays ($z^{-1}$), multipliers (gains), and adders. This is the basis of digital filter design.

### Key Insight

The block $z^{-1}$ represents storing one sample in memory. A difference equation of order $N$ requires exactly $N$ memory elements. In software, each $z^{-1}$ is one element of a circular buffer; in hardware, it is one register or latch. This direct correspondence between the z-domain and digital implementation is why the z-transform is the language of DSP.

---

# Part II: The Unilateral z-Transform

## 21.6 Definition

### The Unilateral z-Transform

$$\mathcal{X}(z) = \sum_{n=0}^{\infty} x[n]\, z^{-n}$$

The sum starts at $n = 0$, not $n = -\infty$. For causal signals ($x[n] = 0$ for $n < 0$), the unilateral and bilateral transforms are identical.

---

## 21.7 The Key Property: Time Shifting

The bilateral z-transform gives: $x[n-1] \xleftrightarrow{\mathcal{Z}} z^{-1} X(z)$.

The unilateral z-transform gives:

$$x[n-1] \xleftrightarrow{\mathcal{Z}_u} z^{-1} \mathcal{X}(z) + x[-1]$$

$$x[n-2] \xleftrightarrow{\mathcal{Z}_u} z^{-2} \mathcal{X}(z) + x[-2] + x[-1]\, z^{-1}$$

General pattern for delay by $m$:

$$x[n-m] \xleftrightarrow{\mathcal{Z}_u} z^{-m} \mathcal{X}(z) + x[-m] + x[-m+1]\, z^{-1} + \cdots + x[-1]\, z^{-(m-1)}$$

### Key Insight

The initial conditions $x[-1], x[-2], \ldots$ appear explicitly, just as $x(0^-), x'(0^-)$ appeared in the unilateral Laplace differentiation property. This is the mechanism for incorporating nonzero initial conditions into difference equation solutions.

---

## 21.8 Solving Difference Equations with Initial Conditions

### First-Order Difference Equation with IC

**Solve:** $y[n] - 0.6\, y[n-1] = (0.5)^n u[n]$, $\ y[-1] = 4$.

**Step 1:** Unilateral z-transform.

For the left side:

$$Y(z) - 0.6\left(z^{-1} Y(z) + y[-1]\right) = Y(z) - 0.6 z^{-1} Y(z) - 0.6 \cdot 4$$

$$= (1 - 0.6 z^{-1}) Y(z) - 2.4$$

For the right side: $\dfrac{1}{1 - 0.5 z^{-1}}$.

**Step 2:** Solve for $Y(z)$.

$$(1 - 0.6 z^{-1}) Y(z) = \frac{1}{1 - 0.5 z^{-1}} + 2.4$$

$$Y(z) = \frac{1}{(1 - 0.5 z^{-1})(1 - 0.6 z^{-1})} + \frac{2.4}{1 - 0.6 z^{-1}}$$

**Step 3:** Partial fractions on the first term.

$$\frac{1}{(1 - 0.5 z^{-1})(1 - 0.6 z^{-1})} = \frac{A}{1 - 0.5 z^{-1}} + \frac{B}{1 - 0.6 z^{-1}}$$

Set $z^{-1} = 2$: $1 = A(1 - 1.2) \Rightarrow A = -5$.
Set $z^{-1} = 5/3$: $1 = B(1 - 5/6) = B/6 \Rightarrow B = 6$.

So:

$$Y(z) = \frac{-5}{1 - 0.5 z^{-1}} + \frac{6}{1 - 0.6 z^{-1}} + \frac{2.4}{1 - 0.6 z^{-1}} = \frac{-5}{1 - 0.5 z^{-1}} + \frac{8.4}{1 - 0.6 z^{-1}}$$

**Step 4:** Invert.

$$y[n] = \left[-5 \cdot (0.5)^n + 8.4 \cdot (0.6)^n\right] u[n]$$

**Step 5:** Verify.

- $y[0] = -5 + 8.4 = 3.4$. From the ODE: $y[0] = 0.6 \cdot y[-1] + x[0] = 0.6 \cdot 4 + 1 = 3.4$ ✓.
- $y[1] = -5(0.5) + 8.4(0.6) = -2.5 + 5.04 = 2.54$. From the ODE: $y[1] = 0.6 \cdot y[0] + x[1] = 0.6 \cdot 3.4 + 0.5 = 2.54$ ✓.

### Second-Order

**Solve:** $y[n] - 0.7\, y[n-1] + 0.1\, y[n-2] = 0$, $\ y[-1] = 1, \ y[-2] = 0$.

**Step 1:** Unilateral z-transform.

$$\mathcal{Z}_u\{y[n-1]\} = z^{-1} Y(z) + y[-1] = z^{-1} Y + 1$$

$$\mathcal{Z}_u\{y[n-2]\} = z^{-2} Y(z) + y[-2] + y[-1] z^{-1} = z^{-2} Y + 0 + z^{-1}$$

Substitute:

$$Y - 0.7(z^{-1} Y + 1) + 0.1(z^{-2} Y + z^{-1}) = 0$$

$$(1 - 0.7 z^{-1} + 0.1 z^{-2}) Y = 0.7 - 0.1 z^{-1}$$

**Step 2:** Factor. $z^2 - 0.7 z + 0.1 = 0 \Rightarrow z = \dfrac{0.7 \pm \sqrt{0.49 - 0.4}}{2} = \dfrac{0.7 \pm 0.3}{2}$. Poles: $z = 0.5$ and $z = 0.2$.

$$Y(z) = \frac{0.7 - 0.1 z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.2 z^{-1})}$$

**Step 3:** Partial fractions.

$$\frac{0.7 - 0.1 z^{-1}}{(1 - 0.5 z^{-1})(1 - 0.2 z^{-1})} = \frac{A}{1 - 0.5 z^{-1}} + \frac{B}{1 - 0.2 z^{-1}}$$

Set $z^{-1} = 2$: $0.7 - 0.2 = A(1 - 0.4) \Rightarrow 0.5 = 0.6 A \Rightarrow A = 5/6$.
Set $z^{-1} = 5$: $0.7 - 0.5 = B(1 - 2.5) \Rightarrow 0.2 = -1.5 B \Rightarrow B = -2/15$.

**Step 4:** Invert.

$$y[n] = \left[\frac{5}{6} \cdot (0.5)^n - \frac{2}{15} \cdot (0.2)^n\right] u[n]$$

This is a **pure zero-input response**: there is no external input, so the output is entirely due to the initial conditions. Both modes decay because both poles are inside the unit circle.

**Verify:** $y[0] = 5/6 - 2/15 = 25/30 - 4/30 = 21/30 = 0.7$. From ODE: $y[0] = 0.7 \cdot y[-1] - 0.1 \cdot y[-2] = 0.7 \cdot 1 - 0 = 0.7$ ✓.

---

## 21.9 ZSR + ZIR Decomposition

Just as in CT (Lecture 18):

$$y[n] = \underbrace{y_{ZS}[n]}_{\text{zero-state}} + \underbrace{y_{ZI}[n]}_{\text{zero-input}}$$

$y_{ZS}[n]$: output due to input alone, with all initial conditions set to zero.
$y_{ZI}[n]$: output due to initial conditions alone, with zero input.

---

## 21.10 Summary of the Three-Lecture z-Transform Block

*Figure: Flow diagram showing the z-transform progression — Lecture 19 (Definition, ROC) → [tools] → Lecture 20 (Inverse, Properties) → [application] → Lecture 21 (Systems, IVPs).*

| | Laplace (Lctrs 16–18) | z-Transform (Lctrs 19–21) |
|---|---|---|
| Converts | differential eqs → algebra | difference eqs → algebra |
| Delay operator | $e^{-s t_0}$ | $z^{-1}$ |
| Causal + Stable | poles in LHP ($\mathrm{Re}\{p\} < 0$) | poles inside $\|z\| = 1$ ($\|p\| < 1$) |
| Unilateral IC property | $y'(t) \to sY - y(0^-)$ | $y[n-1] \to z^{-1} Y + y[-1]$ |
| FT exists | $j\omega$-axis in ROC | unit circle in ROC |

**Key takeaways:**

1. $H(z)$ from a difference equation: replace each delay $n - k$ with $z^{-k}$ and solve for $Y/X$.
2. Causal + stable $\iff$ all poles strictly inside the unit circle.
3. Block diagrams use $z^{-1}$ as the basic delay element; this maps directly to digital hardware/software.
4. The unilateral z-transform handles initial conditions via the modified time-shift property: $y[n-1] \to z^{-1} Y + y[-1]$.
5. Total response = ZSR + ZIR.

---

## 21.11 Common Mistakes to Avoid

1. **Confusing "inside unit circle" with "LHP":** In the z-domain, stability requires poles inside the unit circle (not in the left half-plane). A pole at $z = -0.9$ is stable (inside the circle) even though it is on the negative real axis.

2. **Getting the unilateral shift property wrong:** For $y[n-1]$: the IC term is $+y[-1]$, not $-y[-1]$. Compare with Laplace: $y'(t) \to sY - y(0^-)$ has a minus sign, but the z-domain version has a plus sign.

3. **Forgetting that $z^{-1}$ means delay, not advance:** $x[n-1] \leftrightarrow z^{-1} X(z)$ is a delay. $x[n+1] \leftrightarrow z X(z) - z x[0]$ is an advance (unilateral). Do not confuse the two.

4. **Misidentifying pole locations from the $z^{-1}$ form:** In $H(z) = \dfrac{1}{1 - a z^{-1}}$, the pole is at $z = a$, not $z = 1/a$ or $z = -a$.

5. **Checking stability by testing $a < 1$ instead of $|a| < 1$:** A pole at $z = -0.9$ has $|z| = 0.9 < 1$, so it is stable. But $a = -0.9 < 1$ is not the right check; $|a| < 1$ is.

---

*Rogelio Gracia Otalvaro*

---

## Practice Problems Summary

- **Example (Section 21.2) — From Difference Equation to H(z):** Given $y[n] - 0.8 y[n-1] + 0.15 y[n-2] = x[n] + 2 x[n-1]$, derive $H(z)$, factor, and identify poles $z = 0.5, 0.3$ and zero $z = -2$.
- **Stability Classification Table (Section 21.3):** Classify four sample transfer functions as causal-and-stable, unstable, or marginally stable based on pole locations relative to the unit circle.
- **Full Pipeline Example (Section 21.4):** Solve $y[n] - 0.5 y[n-1] = x[n]$ with $x[n] = (0.8)^n u[n]$ end-to-end: find $H(z)$, $X(z)$, $Y(z)$, partial fractions, inversion, and numerical verification.
- **First-Order Difference Equation with IC (Section 21.8):** Solve $y[n] - 0.6 y[n-1] = (0.5)^n u[n]$ with $y[-1] = 4$ using the unilateral z-transform, partial fractions, and verify $y[0], y[1]$.
- **Second-Order Zero-Input Response (Section 21.8):** Solve the homogeneous $y[n] - 0.7 y[n-1] + 0.1 y[n-2] = 0$ with $y[-1] = 1, y[-2] = 0$, demonstrating a pure zero-input response.

---

## Worked Examples (from Official Solutions)

**Source:** [hw6_official_solutions.md](../homework/hw6/hw6_official_solutions.md) — work through the problems before reading the solutions.

- **Problem 4 (all parts):** System analysis of a causal second-order difference equation $y[n] - 0.9y[n-1] + 0.18y[n-2] = x[n]$.
  - **(a)** Find $H(z) = 1/[(1-0.6z^{-1})(1-0.3z^{-1})]$, ROC $|z|>0.6$.
  - **(b)** Stability: both poles $|0.6|<1$, $|0.3|<1$ $\Rightarrow$ BIBO stable.
  - **(c)** Impulse response: $h[n] = [2(0.6)^n - (0.3)^n]u[n]$.
  - **(d)** Drive with $(0.5)^n u[n]$; compute $Y(z)$, partial fractions (three terms), verify $y[0]$ and $y[1]$ against direct recursion.
  - **(e)** Stability of $G(z) = 1/(1 - 1.5z^{-1})$: causal $\Rightarrow$ unstable (pole $z=1.5$ outside unit circle); anti-causal $\Rightarrow$ stable (unit circle in ROC $|z|<1.5$). Parallels the Laplace Problem 4(e) anti-causal result.
- **Problem 5 (all parts):** Unilateral $z$-transform.
  - **(a)** First-order with IC: $y[n] - 0.8y[n-1] = (0.5)^n u[n]$, $y[-1] = 3$; uses $\mathcal{Z}_u\{y[n-1]\} = z^{-1}Y + y[-1]$ (**plus** sign).
  - **(b)** Second-order zero-input: $y[n] - 0.5y[n-1] - 0.06y[n-2] = 0$, $y[-1]=5$, $y[-2]=0$; uses $\mathcal{Z}_u\{y[n-2]\} = z^{-2}Y + y[-2] + y[-1]z^{-1}$.
  - **(c)** ZSR/ZIR decomposition for part (a); their sum reproduces the full $y[n]$.

## Instructor Emphasis (from Official Study Guide)

- **Golden Rule (DT):** Causal + BIBO stable $\iff$ all poles strictly inside the unit circle ($|p_i|<1$). Note: $|a| < 1$, not $a < 1$ — e.g. $z=-0.9$ is stable.
- **Sign trap:** Unilateral Laplace shift uses $-y(0^-)$; unilateral $z$-shift uses **$+y[-1]$**. Don't mix them up.
- Pipeline: difference equation $\to \mathcal{Z}_u \to$ solve $Y(z) \to$ PFE $\to$ invert.
- Total response = ZSR + ZIR.
