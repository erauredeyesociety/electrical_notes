# CEC 315 — Exam 3 Additional Practice Problems (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Exam 3 — Lectures 16–23 (Laplace, Z, Sampling, Feedback)
**Purpose:** Brand-new variations on the worked examples in
`exam3_sample_problems.md`. Same techniques, different numerical data.

Each problem lists its topic, the concept tested, a full step-by-step
solution, and a boxed final answer. Work each one BEFORE looking at the
solution.

---

## Table of Contents

- [Lecture 16 — Laplace Transform and ROC](#lecture-16--laplace-transform-and-roc)
- [Lecture 17 — Inverse Laplace and Properties](#lecture-17--inverse-laplace-and-properties)
- [Lecture 18 — System Analysis via Unilateral Laplace](#lecture-18--system-analysis-via-unilateral-laplace)
- [Lecture 19 — Z-Transform and ROC](#lecture-19--z-transform-and-roc)
- [Lecture 20 — Inverse Z-Transform and Properties](#lecture-20--inverse-z-transform-and-properties)
- [Lecture 21 — System Analysis via Unilateral Z](#lecture-21--system-analysis-via-unilateral-z)
- [Lecture 22 — Sampling](#lecture-22--sampling)
- [Lecture 23 — Linear Feedback Systems](#lecture-23--linear-feedback-systems)

---

## Lecture 16 — Laplace Transform and ROC

### Problem P16.1 — Ramp–Exponential Pair
**Topic:** Basic Laplace pair $t^{n-1}e^{-at}u(t)/(n-1)!\leftrightarrow 1/(s+a)^n$.
**Concept tested:** Recognize a table entry; state the ROC.

**Statement.** Compute $\mathcal{L}\{t^2 e^{-5t}u(t)\}$ and state the ROC.

**Solution.**

**Step 1.** The standard pair (for $n=3$, $a=5$) is
$$\frac{t^{2}}{2!}e^{-5t}u(t)\leftrightarrow \frac{1}{(s+5)^{3}},\qquad \operatorname{Re}\{s\}>-5.$$

**Step 2.** Multiply both sides by $2!=2$:
$$t^{2}e^{-5t}u(t)\leftrightarrow \frac{2}{(s+5)^{3}}.$$

**Step 3.** The ROC is unchanged by the scalar.

**Result.**
$$\boxed{\,X(s) = \frac{2}{(s+5)^{3}},\qquad \operatorname{Re}\{s\}>-5.\,}$$

---

### Problem P16.2 — Two-Sided Combination with Strip ROC
**Topic:** Linearity; intersecting ROCs for a right-sided + left-sided piece.
**Concept tested:** Identify the strip ROC when two exponentials of opposite
type are added.

**Statement.** Find $X(s)$ and the ROC of
$$x(t) = 5e^{-t}u(t) - 2e^{4t}u(-t).$$

**Solution.**

**Step 1.** Right-sided piece: $5e^{-t}u(t)\leftrightarrow 5/(s+1)$,
ROC $\operatorname{Re}\{s\}>-1$.

**Step 2.** Left-sided piece: rewrite
$-2e^{4t}u(-t) = 2\bigl[-e^{4t}u(-t)\bigr]$. Using the pair
$-e^{-at}u(-t)\leftrightarrow 1/(s+a)$ with $a=-4$:
$$-2e^{4t}u(-t)\leftrightarrow \frac{2}{s-4},\qquad \operatorname{Re}\{s\}<4.$$

**Step 3.** Sum and intersect the ROCs.

**Result.**
$$\boxed{\,X(s) = \frac{5}{s+1}+\frac{2}{s-4},\qquad -1<\operatorname{Re}\{s\}<4.\,}$$

The ROC is a vertical strip between the two poles $s=-1$ and $s=4$.

---

### Problem P16.3 — Damped Sine via Frequency-Shift
**Topic:** Frequency-shift property $e^{-at}x(t)\leftrightarrow X(s+a)$.
**Concept tested:** Build a pair from a known one using a property.

**Statement.** Find $\mathcal{L}\{e^{-2t}\sin(3t)u(t)\}$ and its ROC.

**Solution.**

**Step 1.** Known pair: $\sin(3t)u(t)\leftrightarrow 3/(s^2+9)$,
ROC $\operatorname{Re}\{s\}>0$.

**Step 2.** Apply $e^{-2t}x(t)\leftrightarrow X(s+2)$:
$$X(s) = \frac{3}{(s+2)^{2}+9}.$$

**Step 3.** The ROC shifts left by $2$:
$$\operatorname{Re}\{s\}>-2.$$

**Result.**
$$\boxed{\,X(s) = \frac{3}{(s+2)^{2}+9},\qquad \operatorname{Re}\{s\}>-2.\,}$$

---

### Problem P16.4 — Hyperbolic Cosine Pulse
**Topic:** Decompose a hyperbolic function into exponentials.
**Concept tested:** Sum of two right-sided exponentials with opposite sign poles; find the common ROC.

**Statement.** Find $X(s)$ and the ROC of
$$x(t) = \cosh(3t)\,u(t) = \tfrac{1}{2}\bigl(e^{3t}+e^{-3t}\bigr)u(t).$$

**Solution.**

**Step 1.** By linearity,
$$X(s) = \frac{1}{2}\left[\frac{1}{s-3}+\frac{1}{s+3}\right].$$

**Step 2.** Common denominator:
$$X(s) = \frac{1}{2}\cdot\frac{(s+3)+(s-3)}{(s-3)(s+3)} = \frac{1}{2}\cdot\frac{2s}{s^{2}-9} = \frac{s}{s^{2}-9}.$$

**Step 3.** Individual ROCs: $\operatorname{Re}\{s\}>3$ and $\operatorname{Re}\{s\}>-3$.
Intersection: $\operatorname{Re}\{s\}>3$.

**Result.**
$$\boxed{\,X(s) = \frac{s}{s^{2}-9},\qquad \operatorname{Re}\{s\}>3.\,}$$

**Remark.** The poles are at $s=\pm 3$; since the signal is right-sided, the
ROC is to the right of the rightmost pole.

---

### Problem P16.5 — Finite-Duration Delayed Pulse
**Topic:** Time-shift property; finite-duration ROC is the entire plane.
**Concept tested:** Decompose a pulse as a difference of two shifted steps.

**Statement.** Find $X(s)$ and the ROC of
$$x(t) = u(t-4) - u(t-7).$$

**Solution.**

**Step 1.** Use $u(t)\leftrightarrow 1/s$ and the time-shift property
$u(t-t_0)\leftrightarrow e^{-st_0}/s$:
$$X(s) = \frac{e^{-4s}}{s} - \frac{e^{-7s}}{s} = \frac{e^{-4s}-e^{-7s}}{s}.$$

**Step 2.** The signal has finite support $[4,7]$ and is bounded, so
it is absolutely integrable. The ROC is the entire $s$-plane (the apparent
pole at $s=0$ is removable: $\lim_{s\to 0}(e^{-4s}-e^{-7s})/s = -4-(-7) = 3$).

**Result.**
$$\boxed{\,X(s) = \frac{e^{-4s}-e^{-7s}}{s},\qquad \text{all }s.\,}$$

---

## Lecture 17 — Inverse Laplace and Properties

### Problem P17.1 — Distinct Real Poles (Right-Sided)
**Topic:** Partial fraction expansion via cover-up.
**Concept tested:** Two distinct first-order terms, causal direction.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{s+7}{(s+1)(s+4)},\qquad \operatorname{Re}\{s\}>-1.$$

**Solution.**

**Step 1.** PFE:
$$X(s) = \frac{A}{s+1}+\frac{B}{s+4}.$$

**Step 2.** Cover-up.
- $A = (s+7)/(s+4)\big|_{s=-1} = 6/3 = 2$.
- $B = (s+7)/(s+1)\big|_{s=-4} = 3/(-3) = -1$.

$$X(s) = \frac{2}{s+1} - \frac{1}{s+4}.$$

**Step 3.** ROC is to the right of both poles $\Rightarrow$ both terms are
right-sided.

**Result.**
$$\boxed{\,x(t) = \bigl[2e^{-t} - e^{-4t}\bigr]u(t).\,}$$

**Check.** $x(0^{+}) = 2-1 = 1$; IVT:
$\lim_{s\to\infty}sX(s) = \lim_{s\to\infty}(s^{2}+7s)/((s+1)(s+4)) = 1$. $\checkmark$

---

### Problem P17.2 — Improper Rational (Long Division First)
**Topic:** Polynomial long division before PFE.
**Concept tested:** Recognize that $\deg\text{num}\ge\deg\text{den}$ produces an
impulse term.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{s^{2}+4s+5}{s^{2}+3s+2},\qquad \operatorname{Re}\{s\}>-1.$$

**Solution.**

**Step 1.** Long division: the numerator degree equals the denominator
degree. Divide:
$$s^{2}+4s+5 = 1\cdot(s^{2}+3s+2) + (s+3).$$

So
$$X(s) = 1 + \frac{s+3}{(s+1)(s+2)}.$$

**Step 2.** PFE of the proper part:
- $A$ at $s=-1$: $(-1+3)/(-1+2) = 2$.
- $B$ at $s=-2$: $(-2+3)/(-2+1) = -1$.

$$X(s) = 1 + \frac{2}{s+1}-\frac{1}{s+2}.$$

**Step 3.** The constant $1$ inverts to $\delta(t)$; the remaining terms are
right-sided.

**Result.**
$$\boxed{\,x(t) = \delta(t)+\bigl[2e^{-t}-e^{-2t}\bigr]u(t).\,}$$

---

### Problem P17.3 — Repeated Triple Pole
**Topic:** Table pair for $t^{n-1}e^{-at}u(t)$.
**Concept tested:** Direct match for a higher-order pole.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{1}{(s+3)^{3}},\qquad \operatorname{Re}\{s\}>-3.$$

**Solution.**

**Step 1.** Use the pair
$$\frac{t^{n-1}}{(n-1)!}e^{-at}u(t)\leftrightarrow \frac{1}{(s+a)^{n}},\qquad n=3,\ a=3.$$

**Step 2.** With $n=3$, $(n-1)!=2$:
$$\frac{t^{2}}{2}e^{-3t}u(t)\leftrightarrow \frac{1}{(s+3)^{3}}.$$

**Result.**
$$\boxed{\,x(t) = \tfrac{1}{2}t^{2}e^{-3t}u(t).\,}$$

---

### Problem P17.4 — Complex Conjugate Poles
**Topic:** Complete the square; use the damped cosine / sine pair.
**Concept tested:** Split the numerator into an "$(s+a)$-like" part and a constant.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{2s+8}{s^{2}+6s+25},\qquad \operatorname{Re}\{s\}>-3.$$

**Solution.**

**Step 1.** Complete the square:
$$s^{2}+6s+25 = (s+3)^{2}+16,$$
so the poles are at $s=-3\pm j4$ and $\omega_{d}=4$.

**Step 2.** Split the numerator to match the damped-cosine and
damped-sine templates:
$$2s+8 = 2(s+3)+2.$$

$$X(s) = 2\cdot\frac{s+3}{(s+3)^{2}+16} + \frac{1}{2}\cdot\frac{4}{(s+3)^{2}+16}.$$

**Step 3.** Invert, using
$(s+a)/((s+a)^{2}+\omega_{d}^{2})\leftrightarrow e^{-at}\cos(\omega_{d}t)u(t)$
and $\omega_{d}/((s+a)^{2}+\omega_{d}^{2})\leftrightarrow e^{-at}\sin(\omega_{d}t)u(t)$.

**Result.**
$$\boxed{\,x(t) = e^{-3t}\!\left[2\cos(4t)+\tfrac{1}{2}\sin(4t)\right]u(t).\,}$$

---

### Problem P17.5 — Mixed ROC (Two-Sided Inversion)
**Topic:** Use the ROC to assign direction per term.
**Concept tested:** One pole inverted right-sided, the other left-sided.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{6}{(s-1)(s+5)},\qquad -5<\operatorname{Re}\{s\}<1.$$

**Solution.**

**Step 1.** PFE.
- $A$ at $s=1$: $6/(1+5) = 1$.
- $B$ at $s=-5$: $6/(-5-1) = -1$.

$$X(s) = \frac{1}{s-1} - \frac{1}{s+5}.$$

**Step 2.** Direction from the ROC.
- Pole at $s=1$: ROC is to its **left** $\Rightarrow$ left-sided $\Rightarrow
1/(s-1)\leftrightarrow -e^{t}u(-t)$.
- Pole at $s=-5$: ROC is to its **right** $\Rightarrow$ right-sided $\Rightarrow
1/(s+5)\leftrightarrow e^{-5t}u(t)$.

**Step 3.** Apply the signs from the PFE.

**Result.**
$$\boxed{\,x(t) = -e^{t}u(-t) - e^{-5t}u(t).\,}$$

---

### Problem P17.6 — Initial and Final Value Theorems
**Topic:** IVT and FVT applied without inverting.
**Concept tested:** Check FVT validity before applying it.

**Statement.** Given
$$X(s) = \frac{2s+3}{s(s+1)(s+4)},\qquad \operatorname{Re}\{s\}>0,$$
find $x(0^{+})$ and $x(\infty)$.

**Solution.**

**IVT.**
$$x(0^{+}) = \lim_{s\to\infty}sX(s) = \lim_{s\to\infty}\frac{2s+3}{(s+1)(s+4)} = 0.$$

**FVT validity.** $sX(s) = (2s+3)/[(s+1)(s+4)]$ has poles at $s=-1,-4$
(both strictly in the LHP). $\checkmark$

$$x(\infty) = \lim_{s\to 0}\frac{2s+3}{(s+1)(s+4)} = \frac{3}{4}.$$

**Result.**
$$\boxed{\,x(0^{+})=0,\qquad x(\infty) = \tfrac{3}{4}.\,}$$

---

## Lecture 18 — System Analysis via Unilateral Laplace

### Problem P18.1 — Differential Equation to $H(s)$ with Cancellation
**Topic:** Derive $H(s)$; recognize a pole-zero cancellation.
**Concept tested:** ODE $\to$ transfer function; stability.

**Statement.** A causal LTI system obeys
$$\frac{d^{2}y}{dt^{2}}+7\frac{dy}{dt}+12y = 2\frac{dx}{dt}+8x.$$
Find $H(s)$ and classify stability.

**Solution.**

**Step 1.** Zero ICs, $d^{k}/dt^{k}\to s^{k}$:
$$(s^{2}+7s+12)Y(s) = (2s+8)X(s).$$

**Step 2.**
$$H(s) = \frac{2s+8}{s^{2}+7s+12} = \frac{2(s+4)}{(s+3)(s+4)} = \frac{2}{s+3}.$$

**Step 3.** After cancellation the only pole is $s=-3$ (LHP).
Causal $\Rightarrow$ ROC $\operatorname{Re}\{s\}>-3$, which contains the
$j\omega$-axis.

**Result.**
$$\boxed{\,H(s) = \frac{2}{s+3};\ \text{causal and stable.}\,}$$

---

### Problem P18.2 — Stability Classification Table
**Topic:** Causal pole-locations vs. BIBO stability.
**Concept tested:** Apply the LHP rule and spot marginal cases.

**Statement.** For each causal LTI system, state whether it is stable,
marginally stable, or unstable.

| | $H(s)$ |
|---|---|
| (a) | $\dfrac{4}{s+5}$ |
| (b) | $\dfrac{s+2}{(s+1)(s-4)}$ |
| (c) | $\dfrac{7}{s^{2}+16}$ |
| (d) | $\dfrac{3s+2}{s^{2}+4s+8}$ |
| (e) | $\dfrac{1}{s(s+2)}$ |

**Solution.**

| Case | Pole locations | Classification |
|---|---|---|
| (a) | $s=-5$ | Stable |
| (b) | $s=-1,\ +4$ | Unstable (RHP pole) |
| (c) | $s=\pm j4$ | Marginally stable (on $j\omega$-axis) |
| (d) | $s=-2\pm j2$ | Stable |
| (e) | $s=0,\ -2$ | Marginally stable (single pole at origin) |

$$\boxed{\,(a)\text{ stable},\ (b)\text{ unstable},\ (c)\text{ marginal},\ (d)\text{ stable},\ (e)\text{ marginal.}\,}$$

---

### Problem P18.3 — First-Order ODE with IC and Exponential Input
**Topic:** ZIR + ZSR via unilateral Laplace.
**Concept tested:** Solve a first-order ODE with a nonzero initial condition.

**Statement.** Solve
$$\frac{dy}{dt}+2y = 4e^{-t}u(t),\qquad y(0^{-})=3.$$

**Solution.**

**Step 1.** Unilateral Laplace:
$$[sY(s)-3]+2Y(s) = \frac{4}{s+1}.$$

**Step 2.** Solve:
$$(s+2)Y(s) = \frac{4}{s+1}+3\Rightarrow Y(s) = \frac{4}{(s+1)(s+2)}+\frac{3}{s+2}.$$

**Step 3.** PFE of the ZSR term:
$$\frac{4}{(s+1)(s+2)} = \frac{4}{s+1}-\frac{4}{s+2}.$$

Combine with the ZIR term $3/(s+2)$:
$$Y(s) = \frac{4}{s+1}-\frac{4}{s+2}+\frac{3}{s+2} = \frac{4}{s+1}-\frac{1}{s+2}.$$

**Step 4.** Invert.

**Result.**
$$\boxed{\,y(t) = \bigl[4e^{-t}-e^{-2t}\bigr]u(t).\,}$$

**Checks.** $y(0) = 4-1 = 3$ $\checkmark$ (matches $y(0^{-})$).
$y(\infty) = 0$ (expected, since the forcing decays and the system is stable).

---

### Problem P18.4 — Second-Order ODE with ICs and Step Input
**Topic:** Full unilateral-Laplace pipeline with both $y(0^{-})$ and $y'(0^{-})$.
**Concept tested:** Handle the $s^{2}Y-sy(0^{-})-y'(0^{-})$ formula carefully.

**Statement.** Solve
$$\frac{d^{2}y}{dt^{2}}+5\frac{dy}{dt}+6y = 12u(t),\qquad y(0^{-})=1,\ y'(0^{-})=-1.$$

**Solution.**

**Step 1.** Unilateral Laplace:
$$\bigl[s^{2}Y - s\cdot 1 - (-1)\bigr] + 5\bigl[sY - 1\bigr] + 6Y = \frac{12}{s}.$$

Simplify the IC terms: $s^{2}Y - s + 1 + 5sY - 5 + 6Y = 12/s$.

**Step 2.** Collect:
$$(s^{2}+5s+6)Y(s) = \frac{12}{s}+s+4.$$

Common denominator on the right:
$$Y(s) = \frac{s^{2}+4s+12}{s(s^{2}+5s+6)} = \frac{s^{2}+4s+12}{s(s+2)(s+3)}.$$

**Step 3.** PFE: $A/s + B/(s+2) + C/(s+3)$.
- $A = (s^{2}+4s+12)/((s+2)(s+3))\big|_{s=0} = 12/6 = 2$.
- $B = (s^{2}+4s+12)/(s(s+3))\big|_{s=-2} = (4-8+12)/((-2)(1)) = 8/(-2) = -4$.
- $C = (s^{2}+4s+12)/(s(s+2))\big|_{s=-3} = (9-12+12)/((-3)(-1)) = 9/3 = 3$.

$$Y(s) = \frac{2}{s}-\frac{4}{s+2}+\frac{3}{s+3}.$$

**Step 4.** Invert.

**Result.**
$$\boxed{\,y(t) = \bigl[2 - 4e^{-2t}+3e^{-3t}\bigr]u(t).\,}$$

**Checks.**
- $y(0) = 2-4+3 = 1$ $\checkmark$
- $y'(t) = 8e^{-2t}-9e^{-3t}$, so $y'(0) = 8-9 = -1$ $\checkmark$
- $y(\infty) = 2$, consistent with the DC gain $6y_{\text{ss}}=12$.

---

### Problem P18.5 — Step Response of a Second-Order System
**Topic:** Step response, ZSR.
**Concept tested:** $S(s) = H(s)/s$; PFE with a pole at the origin.

**Statement.** Find the step response $s(t)$ of the causal LTI system
$$H(s) = \frac{6}{s^{2}+5s+6}.$$

**Solution.**

**Step 1.** Factor: $s^{2}+5s+6 = (s+2)(s+3)$. Step-input transform: $X(s)=1/s$.

**Step 2.**
$$S(s) = \frac{6}{s(s+2)(s+3)}.$$

**Step 3.** PFE: $A/s + B/(s+2) + C/(s+3)$.
- $A = 6/((0+2)(0+3)) = 1$.
- $B = 6/((-2)(-2+3)) = 6/(-2) = -3$.
- $C = 6/((-3)(-3+2)) = 6/3 = 2$.

$$S(s) = \frac{1}{s}-\frac{3}{s+2}+\frac{2}{s+3}.$$

**Step 4.** Invert (right-sided).

**Result.**
$$\boxed{\,s(t) = \bigl[1 - 3e^{-2t} + 2e^{-3t}\bigr]u(t).\,}$$

**Checks.** $s(0) = 1-3+2 = 0$ $\checkmark$. $s(\infty) = 1$, consistent with
$H(0) = 6/6 = 1$. $\checkmark$

---

## Lecture 19 — Z-Transform and ROC

### Problem P19.1 — Right-Sided Geometric
**Topic:** Z-transform from the definition; geometric-series convergence.
**Concept tested:** Recognize a causal exponential and its ROC.

**Statement.** Find $X(z)$ and the ROC of $x[n] = (3/4)^{n}u[n]$.

**Solution.**

**Step 1.** Definition:
$$X(z) = \sum_{n=0}^{\infty}\Bigl(\tfrac{3}{4}\Bigr)^{\!n}z^{-n} = \sum_{n=0}^{\infty}\Bigl(\tfrac{3}{4}z^{-1}\Bigr)^{\!n}.$$

**Step 2.** Converges iff $|(3/4)z^{-1}|<1$, i.e., $|z|>3/4$. Then
$$X(z) = \frac{1}{1-\tfrac{3}{4}z^{-1}}.$$

**Result.**
$$\boxed{\,X(z) = \frac{1}{1-\tfrac{3}{4}z^{-1}},\qquad |z|>3/4.\,}$$

---

### Problem P19.2 — Two-Sided Signal (Annular ROC)
**Topic:** Right + left-sided sum; intersection of ROCs.
**Concept tested:** Apply the left-sided pair $-a^{n}u[-n-1]\leftrightarrow 1/(1-az^{-1})$.

**Statement.** Find $X(z)$ and the ROC of
$$x[n] = \left(\tfrac{1}{4}\right)^{n}u[n] - 3(5)^{n}u[-n-1].$$

**Solution.**

**Step 1.** Right-sided piece:
$(1/4)^{n}u[n]\leftrightarrow 1/(1-(1/4)z^{-1})$, ROC $|z|>1/4$.

**Step 2.** Left-sided piece. Rewrite
$-3(5)^{n}u[-n-1] = 3\bigl[-(5)^{n}u[-n-1]\bigr]$, which gives
$$\frac{3}{1-5z^{-1}},\qquad |z|<5.$$

**Step 3.** Sum; intersect the ROCs.

**Result.**
$$\boxed{\,X(z) = \frac{1}{1-\tfrac{1}{4}z^{-1}} + \frac{3}{1-5z^{-1}},\qquad \tfrac{1}{4}<|z|<5.\,}$$

The ROC is an annular ring between the two pole circles.

---

### Problem P19.3 — Finite-Length Sequence
**Topic:** Polynomial form; ROC of finite-length signals.
**Concept tested:** Direct summation for finite support.

**Statement.** Let $x[n] = \{1, 0, -2, 3\}$ at $n = 0,1,2,3$ (and $0$ elsewhere).
Find $X(z)$ and its ROC.

**Solution.**

**Step 1.** Direct sum:
$$X(z) = 1 + 0\cdot z^{-1} - 2z^{-2} + 3z^{-3} = 1 - 2z^{-2} + 3z^{-3}.$$

**Step 2.** Because $x[n]$ is nonzero only for $n\ge 0$, the point $z=\infty$
is in the ROC. Because there are nonzero samples at $n>0$, $z=0$ is
excluded. ROC: $|z|>0$.

**Check.** $X(1) = 1 - 2 + 3 = 2 = \sum x[n]$. $\checkmark$

**Result.**
$$\boxed{\,X(z) = 1 - 2z^{-2} + 3z^{-3},\qquad |z|>0.\,}$$

---

### Problem P19.4 — Damped Sinusoid (Simple Angle)
**Topic:** Damped-sine Z pair.
**Concept tested:** Match $r^{n}\sin(\omega_{0}n)u[n]\leftrightarrow\ldots$.

**Statement.** Find $X(z)$ and the ROC of
$$x[n] = (0.6)^{n}\sin\!\Bigl(\tfrac{\pi}{2}n\Bigr)u[n].$$

**Solution.**

**Step 1.** Identify $r = 0.6$, $\omega_{0} = \pi/2$. Then
$\cos\omega_{0} = 0$, $\sin\omega_{0} = 1$, $r^{2} = 0.36$.

**Step 2.** Apply
$$r^{n}\sin(\omega_{0}n)u[n]\leftrightarrow \frac{r\sin\omega_{0}\,z^{-1}}{1 - 2r\cos\omega_{0}\,z^{-1}+r^{2}z^{-2}}.$$

Numerator: $r\sin\omega_{0} = 0.6$. Denominator: $1 - 0 + 0.36z^{-2}$.

$$X(z) = \frac{0.6\,z^{-1}}{1+0.36\,z^{-2}}.$$

**Step 3.** Poles at $z = \pm j0.6$, both with $|z| = 0.6$. ROC: $|z|>0.6$.

**Result.**
$$\boxed{\,X(z) = \frac{0.6\,z^{-1}}{1+0.36\,z^{-2}},\qquad |z|>0.6.\,}$$

---

### Problem P19.5 — Sum of Two Causal Geometric Sequences
**Topic:** Linearity; combine into a single rational function.
**Concept tested:** Simplify $A/(1-a_{1}z^{-1})+B/(1-a_{2}z^{-1})$ into a single fraction.

**Statement.** Find $X(z)$ of $x[n] = 5(0.3)^{n}u[n] - 2(0.6)^{n}u[n]$.

**Solution.**

**Step 1.** Linearity:
$$X(z) = \frac{5}{1-0.3z^{-1}}-\frac{2}{1-0.6z^{-1}}.$$

**Step 2.** Common denominator:
$$X(z) = \frac{5(1-0.6z^{-1})-2(1-0.3z^{-1})}{(1-0.3z^{-1})(1-0.6z^{-1})}
= \frac{3 - 2.4\,z^{-1}}{(1-0.3z^{-1})(1-0.6z^{-1})}.$$

**Step 3.** Both terms are right-sided; outermost pole at $z=0.6$.
ROC: $|z|>0.6$.

**Result.**
$$\boxed{\,X(z) = \frac{3 - 2.4\,z^{-1}}{(1-0.3z^{-1})(1-0.6z^{-1})},\qquad |z|>0.6.\,}$$

**Check.** $x[0] = 5-2 = 3$; IVT:
$\lim_{z\to\infty}X(z) = 3/1 = 3$. $\checkmark$

---

## Lecture 20 — Inverse Z-Transform and Properties

### Problem P20.1 — Distinct Poles, Right-Sided
**Topic:** PFE in $z^{-1}$; cover-up.
**Concept tested:** Straightforward distinct-pole inversion.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{2+z^{-1}}{(1-0.3z^{-1})(1-0.7z^{-1})},\qquad |z|>0.7.$$

**Solution.**

**Step 1.** PFE:
$$X(z) = \frac{A}{1-0.3z^{-1}}+\frac{B}{1-0.7z^{-1}}.$$

**Step 2.** Cover-up in $z^{-1}$.
- For $A$, set $z^{-1} = 1/0.3 = 10/3$:
$$A = \frac{2+10/3}{1 - 0.7(10/3)} = \frac{16/3}{1-7/3} = \frac{16/3}{-4/3} = -4.$$
- For $B$, set $z^{-1} = 1/0.7 = 10/7$:
$$B = \frac{2+10/7}{1 - 0.3(10/7)} = \frac{24/7}{1-3/7} = \frac{24/7}{4/7} = 6.$$

$$X(z) = \frac{-4}{1-0.3z^{-1}}+\frac{6}{1-0.7z^{-1}}.$$

**Step 3.** ROC outside both poles $\Rightarrow$ both right-sided.

**Result.**
$$\boxed{\,x[n] = \bigl[-4(0.3)^{n}+6(0.7)^{n}\bigr]u[n].\,}$$

**Check.** $x[0] = -4+6 = 2$; IVT: $\lim_{z\to\infty}X(z) = 2/1 = 2$. $\checkmark$

---

### Problem P20.2 — Mixed ROC (Two-Sided)
**Topic:** Direction assignment from the ROC.
**Concept tested:** Invert with one pole inside and one outside the ROC annulus.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{2}{(1-4z^{-1})(1-0.5z^{-1})},\qquad 0.5<|z|<4.$$

**Solution.**

**Step 1.** PFE.
- $A$ at $z^{-1}=1/4$ (killing $(1-4z^{-1})$):
$$A = \frac{2}{1-0.5(1/4)} = \frac{2}{1-1/8} = \frac{2}{7/8} = \frac{16}{7}.$$
- $B$ at $z^{-1}=2$ (killing $(1-0.5z^{-1})$):
$$B = \frac{2}{1-4(2)} = \frac{2}{-7} = -\frac{2}{7}.$$

Check: $A+B = 16/7-2/7 = 14/7 = 2$, matches $X(z)$ at $z^{-1}=0$. $\checkmark$

$$X(z) = \frac{16/7}{1-4z^{-1}} - \frac{2/7}{1-0.5z^{-1}}.$$

**Step 2.** Direction from the ROC $0.5<|z|<4$.
- Pole at $z=4$: ROC is **inside** $\Rightarrow$ left-sided $\Rightarrow
-(4)^{n}u[-n-1]$.
- Pole at $z=0.5$: ROC is **outside** $\Rightarrow$ right-sided $\Rightarrow
(0.5)^{n}u[n]$.

**Result.**
$$\boxed{\,x[n] = -\tfrac{16}{7}(4)^{n}u[-n-1] - \tfrac{2}{7}(0.5)^{n}u[n].\,}$$

---

### Problem P20.3 — Repeated Pole with $z^{-1}$ Numerator
**Topic:** Pair $na^{n}u[n]\leftrightarrow az^{-1}/(1-az^{-1})^{2}$.
**Concept tested:** Distinguish the two repeated-pole pairs.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{0.4\,z^{-1}}{(1-0.4z^{-1})^{2}},\qquad |z|>0.4.$$

**Solution.**

**Step 1.** Apply the pair
$$\frac{a z^{-1}}{(1-a z^{-1})^{2}}\leftrightarrow n\,a^{n}u[n],\qquad |z|>|a|.$$

Here $a = 0.4$.

**Result.**
$$\boxed{\,x[n] = n(0.4)^{n}u[n].\,}$$

**Check.** $x[0] = 0$ (IVT also gives $0$ — the numerator has an extra
$z^{-1}$). $x[1] = 0.4$, $x[2] = 2(0.16) = 0.32$.

---

### Problem P20.4 — Power Series (Long Division)
**Topic:** Long division to read off $x[n]$ for small $n$.
**Concept tested:** Direct extraction of the series coefficients.

**Statement.** Given
$$X(z) = \frac{2-z^{-1}}{1-0.3z^{-1}},\qquad |z|>0.3,$$
find $x[0]$, $x[1]$, $x[2]$, and $x[3]$, and a closed-form $x[n]$.

**Solution.**

**Step 1.** Long division in $z^{-1}$.

- First quotient term: $2 / 1 = 2$. Multiply the divisor:
$2(1 - 0.3z^{-1}) = 2 - 0.6z^{-1}$. Subtract from $2 - z^{-1}$:
remainder $-0.4 z^{-1}$.
- Next: $-0.4z^{-1}/1 = -0.4z^{-1}$. Multiply:
$-0.4z^{-1}(1-0.3z^{-1}) = -0.4z^{-1}+0.12z^{-2}$. Subtract:
remainder $-0.12z^{-2}$.
- Next: $-0.12z^{-2}$. Multiply: $-0.12z^{-2}+0.036z^{-3}$.
Remainder $-0.036z^{-3}$.
- Next: $-0.036z^{-3}$.

So
$$X(z) = 2 - 0.4z^{-1} - 0.12 z^{-2} - 0.036 z^{-3} - \cdots.$$

**Step 2. Closed form.** Write $2 - z^{-1} = K(1-0.3z^{-1}) + R$ and match:
coefficient of $z^{-1}$ gives $-0.3K = -1$, so $K = 10/3$. Constant:
$K + R = 2 \Rightarrow R = 2 - 10/3 = -4/3$.

$$X(z) = \frac{10}{3} + \frac{-4/3}{1-0.3z^{-1}}.$$

Inverse:
$$x[n] = \tfrac{10}{3}\delta[n] - \tfrac{4}{3}(0.3)^{n}u[n].$$

**Check.** $x[0] = 10/3 - 4/3 = 2$ $\checkmark$. For $n\ge 1$:
$x[1] = -(4/3)(0.3) = -0.4$ $\checkmark$; $x[2] = -(4/3)(0.09) = -0.12$ $\checkmark$;
$x[3] = -(4/3)(0.027) = -0.036$ $\checkmark$.

**Result.**
$$\boxed{\,x[0]=2,\ x[1]=-0.4,\ x[2]=-0.12,\ x[3]=-0.036;\quad
x[n] = \tfrac{10}{3}\delta[n]-\tfrac{4}{3}(0.3)^{n}u[n].\,}$$

---

### Problem P20.5 — Initial and Final Value Theorems
**Topic:** DT IVT and FVT.
**Concept tested:** Apply the formulas; check FVT applicability.

**Statement.** Given
$$X(z) = \frac{3}{(1-z^{-1})(1-0.4z^{-1})},\qquad |z|>1,$$
find $x[0]$ and $x[\infty]$.

**Solution.**

**IVT.**
$$x[0] = \lim_{z\to\infty}X(z) = \frac{3}{1\cdot 1} = 3.$$

**FVT validity.** $(1-z^{-1})X(z) = 3/(1-0.4z^{-1})$ has a single pole at
$z=0.4$ (strictly inside the unit circle). $\checkmark$

$$x[\infty] = \lim_{z\to 1}\frac{3}{1-0.4z^{-1}} = \frac{3}{0.6} = 5.$$

**Result.**
$$\boxed{\,x[0] = 3,\qquad x[\infty] = 5.\,}$$

---

### Problem P20.6 — Time Shift Property
**Topic:** Delay $z^{-n_{0}}$.
**Concept tested:** Apply the shift property.

**Statement.** Let $x[n] = (0.4)^{n}u[n]$. Find the Z-transform and ROC of
$y[n] = x[n-3]$.

**Solution.**

**Step 1.** $X(z) = 1/(1-0.4z^{-1})$, $|z|>0.4$.

**Step 2.** Shift: $x[n-3]\leftrightarrow z^{-3}X(z)$.

$$Y(z) = \frac{z^{-3}}{1-0.4z^{-1}},\qquad |z|>0.4.$$

(A right-shift of a causal sequence does not change the ROC.)

**Result.**
$$\boxed{\,Y(z) = \frac{z^{-3}}{1-0.4z^{-1}},\qquad |z|>0.4.\,}$$

---

## Lecture 21 — System Analysis via Unilateral Z

### Problem P21.1 — Difference Equation to $H(z)$
**Topic:** Derive $H(z)$; stability from pole locations.
**Concept tested:** Replace $y[n-k]\to z^{-k}Y(z)$ and factor.

**Statement.** Find $H(z)$ and classify the stability of the causal LTI system
$$y[n]-\tfrac{5}{6}y[n-1]+\tfrac{1}{6}y[n-2] = x[n]+x[n-1].$$

**Solution.**

**Step 1.** Zero ICs:
$$\bigl(1-\tfrac{5}{6}z^{-1}+\tfrac{1}{6}z^{-2}\bigr)Y(z) = (1+z^{-1})X(z).$$

**Step 2.** Factor the denominator. Roots of $z^{2}-(5/6)z+1/6=0$ are
$$z = \frac{5/6\pm\sqrt{25/36-4/6}}{2} = \frac{5/6\pm 1/6}{2} = \tfrac{1}{2},\ \tfrac{1}{3}.$$

$$H(z) = \frac{1+z^{-1}}{(1-\tfrac{1}{2}z^{-1})(1-\tfrac{1}{3}z^{-1})}.$$

**Step 3.** Both poles lie strictly inside the unit circle, so the causal
system is BIBO stable. Zero at $z=-1$ (on the unit circle) is not a
stability concern.

**Result.**
$$\boxed{\,H(z) = \frac{1+z^{-1}}{(1-\tfrac{1}{2}z^{-1})(1-\tfrac{1}{3}z^{-1})};\ \text{causal and stable.}\,}$$

---

### Problem P21.2 — Full Pipeline (Difference Equation to Output, ZSR)
**Topic:** DE $\to Y(z)\to y[n]$; zero ICs.
**Concept tested:** ZSR via partial fractions.

**Statement.** Solve
$$y[n]-\tfrac{1}{4}y[n-1] = x[n],\qquad x[n] = (1/2)^{n}u[n],$$
with zero initial conditions.

**Solution.**

**Step 1.** $H(z) = 1/(1-(1/4)z^{-1})$; $X(z) = 1/(1-(1/2)z^{-1})$.

**Step 2.** $Y(z) = H(z)X(z) = 1/[(1-(1/4)z^{-1})(1-(1/2)z^{-1})]$.

**Step 3.** PFE.
- $A$ at $z^{-1} = 4$: $1/(1-(1/2)(4)) = 1/(-1) = -1$.
- $B$ at $z^{-1} = 2$: $1/(1-(1/4)(2)) = 1/(1/2) = 2$.

$$Y(z) = \frac{-1}{1-(1/4)z^{-1}}+\frac{2}{1-(1/2)z^{-1}}.$$

**Step 4.** Both right-sided (ROC $|z|>1/2$).

**Result.**
$$\boxed{\,y[n] = \left[-\bigl(\tfrac{1}{4}\bigr)^{n}+2\bigl(\tfrac{1}{2}\bigr)^{n}\right]u[n].\,}$$

**Check.** $y[0] = -1+2 = 1 = x[0]$. $\checkmark$

---

### Problem P21.3 — First-Order Difference Equation with IC
**Topic:** Unilateral Z with nonzero initial condition; ZSR + ZIR.
**Concept tested:** Apply $x[n-1]\leftrightarrow z^{-1}X(z)+x[-1]$ (note the plus).

**Statement.** Solve $y[n]-\tfrac{1}{3}y[n-1] = (1/5)^{n}u[n]$ with $y[-1]=6$.

**Solution.**

**Step 1.** Unilateral Z (recall $y[n-1]\leftrightarrow z^{-1}Y(z)+y[-1]$):
$$Y(z) - \tfrac{1}{3}\bigl[z^{-1}Y(z)+6\bigr] = \frac{1}{1-(1/5)z^{-1}}.$$

**Step 2.** Collect:
$$\bigl(1-\tfrac{1}{3}z^{-1}\bigr)Y(z) = \frac{1}{1-(1/5)z^{-1}} + 2.$$

**Step 3.** Solve:
$$Y(z) = \underbrace{\frac{1}{(1-(1/5)z^{-1})(1-(1/3)z^{-1})}}_{\text{ZSR}}
+\underbrace{\frac{2}{1-(1/3)z^{-1}}}_{\text{ZIR}}.$$

**Step 4.** PFE of the ZSR term.
- $A$ at $z^{-1}=5$: $1/(1-(1/3)(5)) = 1/(-2/3) = -3/2$.
- $B$ at $z^{-1}=3$: $1/(1-(1/5)(3)) = 1/(2/5) = 5/2$.

ZSR $= -3/2 /(1-(1/5)z^{-1})+5/2/(1-(1/3)z^{-1})$.

Combine with ZIR $2/(1-(1/3)z^{-1})$:
$$Y(z) = \frac{-3/2}{1-(1/5)z^{-1}}+\frac{9/2}{1-(1/3)z^{-1}}.$$

**Step 5.** Invert.

**Result.**
$$\boxed{\,y[n] = \left[-\tfrac{3}{2}\bigl(\tfrac{1}{5}\bigr)^{n}+\tfrac{9}{2}\bigl(\tfrac{1}{3}\bigr)^{n}\right]u[n].\,}$$

**Check.** $y[0] = -3/2+9/2 = 3$. Directly from the DE:
$y[0] = (1/3)y[-1] + (1/5)^{0} = 2+1 = 3$. $\checkmark$

---

### Problem P21.4 — Zero-Input Response with a Repeated Pole
**Topic:** ZIR only; repeated-pole case.
**Concept tested:** Apply the unilateral shift-2 formula and handle a double pole.

**Statement.** Solve
$$y[n]-\tfrac{1}{2}y[n-1]+\tfrac{1}{16}y[n-2] = 0,\qquad y[-1]=0,\ y[-2]=16.$$

**Solution.**

**Step 1.** Unilateral Z. Use $y[n-1]\leftrightarrow z^{-1}Y+y[-1]$ and
$y[n-2]\leftrightarrow z^{-2}Y+y[-1]z^{-1}+y[-2]$:
$$Y-\tfrac{1}{2}(z^{-1}Y+0)+\tfrac{1}{16}(z^{-2}Y+0\cdot z^{-1}+16) = 0.$$

Simplify:
$$\bigl(1-\tfrac{1}{2}z^{-1}+\tfrac{1}{16}z^{-2}\bigr)Y(z) = -1.$$

**Step 2.** Recognize the denominator as a perfect square:
$$1-\tfrac{1}{2}z^{-1}+\tfrac{1}{16}z^{-2} = \bigl(1-\tfrac{1}{4}z^{-1}\bigr)^{2}.$$

$$Y(z) = \frac{-1}{(1-(1/4)z^{-1})^{2}}.$$

**Step 3.** Apply the repeated-pole pair
$1/(1-az^{-1})^{2}\leftrightarrow (n+1)a^{n}u[n]$ with $a=1/4$.

**Result.**
$$\boxed{\,y[n] = -(n+1)\bigl(\tfrac{1}{4}\bigr)^{n}u[n].\,}$$

**Check.** $y[0] = -1$. Directly from the DE:
$y[0] = (1/2)(0)-(1/16)(16) = -1$. $\checkmark$

---

### Problem P21.5 — Step Response (First-Order)
**Topic:** Step response via $S(z) = H(z)/(1-z^{-1})$.
**Concept tested:** PFE with a pole at $z=1$; DC-gain sanity check.

**Statement.** Find the causal step response of
$$H(z) = \frac{1}{1-(1/3)z^{-1}}.$$

**Solution.**

**Step 1.** $X(z) = 1/(1-z^{-1})$, so
$$S(z) = \frac{1}{(1-z^{-1})(1-(1/3)z^{-1})}.$$

**Step 2.** PFE.
- $A$ at $z^{-1}=1$: $1/(1-(1/3)(1)) = 1/(2/3) = 3/2$.
- $B$ at $z^{-1}=3$: $1/(1-(1)(3)) = 1/(-2) = -1/2$.

$$S(z) = \frac{3/2}{1-z^{-1}}-\frac{1/2}{1-(1/3)z^{-1}}.$$

**Step 3.** Invert.

**Result.**
$$\boxed{\,s[n] = \left[\tfrac{3}{2}-\tfrac{1}{2}\bigl(\tfrac{1}{3}\bigr)^{n}\right]u[n].\,}$$

**Checks.** $s[0] = 3/2-1/2 = 1 = h[0]$ $\checkmark$.
$s[\infty] = 3/2 = H(1) = 1/(1-1/3)$ $\checkmark$.

---

## Lecture 22 — Sampling

### Problem P22.1 — Nyquist Rate of a Sum of Sinusoids
**Topic:** Identify the highest frequency component.
**Concept tested:** Report the Nyquist rate in both rad/s and Hz.

**Statement.** Find the Nyquist rate of
$$x(t) = \cos(400\pi t) + 2\sin(900\pi t) + 3\cos(1500\pi t).$$

**Solution.**

**Step 1.** The angular frequencies are $400\pi$, $900\pi$, and $1500\pi$ rad/s.

**Step 2.** The maximum is $\omega_{M} = 1500\pi$ rad/s, i.e., $f_{M} = 750$ Hz.

**Step 3.** Nyquist rate $= 2\omega_{M} = 3000\pi$ rad/s $= 1500$ Hz.

**Result.**
$$\boxed{\,\text{Nyquist rate} = 3000\pi\text{ rad/s} = 1500\text{ Hz}.\,}$$

---

### Problem P22.2 — Bandwidth of a Product (Convolution in Frequency)
**Topic:** Multiplication in time $\leftrightarrow$ (scaled) convolution in frequency.
**Concept tested:** Bandwidths add for a product.

**Statement.** $x_{1}(t)$ has $X_{1}(j\omega) = 0$ for $|\omega|>1500\pi$ and
$x_{2}(t)$ has $X_{2}(j\omega) = 0$ for $|\omega|>2500\pi$. Find the Nyquist
rate of $y(t) = x_{1}(t)x_{2}(t)$.

**Solution.**

**Step 1.** Multiplication in time $\leftrightarrow$ convolution in frequency.
The support of $Y(j\omega)$ is contained in the (Minkowski) sum of the
supports of $X_{1}$ and $X_{2}$, so $|\omega|\le 1500\pi+2500\pi = 4000\pi$.

**Step 2.** $\omega_{M,y} = 4000\pi$ rad/s, so the Nyquist rate is
$8000\pi$ rad/s $= 4000$ Hz.

**Result.**
$$\boxed{\,\text{Nyquist rate of }y(t) = 8000\pi\text{ rad/s} = 4000\text{ Hz}.\,}$$

---

### Problem P22.3 — Checking Sampling Periods
**Topic:** Converting $\omega_{s}>2\omega_{M}$ to a bound on $T$.
**Concept tested:** Strict inequality and unit conversion.

**Statement.** A signal has $X(j\omega) = 0$ for $|\omega|>800\pi$ rad/s.
Which of these sampling periods allow perfect reconstruction?
(a) $T = 0.5$ ms, (b) $T = 1.25$ ms, (c) $T = 1$ ms, (d) $T = 2$ ms.

**Solution.**

**Step 1.** Nyquist rate is $1600\pi$ rad/s. Required:
$\omega_{s} = 2\pi/T > 1600\pi$, i.e., $T < 2/1600 = 1/800$ s $= 1.25$ ms
(strict).

**Step 2.** Check each.
- (a) $0.5$ ms $<1.25$ ms $\Rightarrow$ works.
- (b) $1.25$ ms $=1.25$ ms $\Rightarrow$ **fails** (strict inequality violated).
- (c) $1$ ms $<1.25$ ms $\Rightarrow$ works.
- (d) $2$ ms $>1.25$ ms $\Rightarrow$ aliases.

**Result.**
$$\boxed{\,(a)\text{ works},\ (b)\text{ fails},\ (c)\text{ works},\ (d)\text{ aliases.}\,}$$

---

### Problem P22.4 — Aliased Tone
**Topic:** Aliased-frequency formula $f_{\text{alias}} = |f_{s}-f_{0}|$.
**Concept tested:** Recognize undersampling and compute the fold-back.

**Statement.** A tone at $f_{0} = 8$ Hz is sampled at $f_{s} = 6$ Hz.
After reconstruction through an ideal LPF with cutoff $f_{s}/2$, what
frequency appears?

**Solution.**

**Step 1.** Nyquist rate for 8 Hz is 16 Hz; $f_{s}=6$ Hz is too low.

**Step 2.** Since $f_{s}/2 = 3 < f_{0} = 8 < f_{s} = 6$ is **false**
($8 > 6$), we instead fold by $f_{s}$ until the frequency lands in
$[0,f_{s}/2]$. Compute $f_{0}-f_{s} = 2$ Hz, which lies in $[0,3]$.

So the apparent frequency is $f_{\text{alias}} = |f_{0}-f_{s}| = 2$ Hz.

**Result.**
$$\boxed{\,f_{\text{alias}} = 2\text{ Hz}.\,}$$

---

### Problem P22.5 — DT Processing of a CT Signal
**Topic:** Mapping $\Omega = \omega T$ from CT to DT frequency.
**Concept tested:** Sampling with no aliasing; apply the formula.

**Statement.** A CT sinusoid $x(t) = \cos(300\pi t)$ is sampled at
$f_{s} = 500$ Hz. What discrete-time frequency $\Omega$ (rad/sample) does
the resulting sequence have?

**Solution.**

**Step 1.** $T = 1/f_{s} = 2$ ms, and $\omega = 300\pi$ rad/s.

**Step 2.** Aliasing check: $f_{0} = 150$ Hz, and $f_{s}/2 = 250$ Hz;
since $f_{0}<f_{s}/2$, no aliasing occurs. $\checkmark$

**Step 3.**
$$\Omega = \omega T = 300\pi\cdot 2\times 10^{-3} = 0.6\pi\text{ rad/sample}.$$

**Result.**
$$\boxed{\,\Omega = 0.6\pi\text{ rad/sample}.\,}$$

---

### Problem P22.6 — Reconstruction Filter Specification
**Topic:** Ideal LPF for reconstruction.
**Concept tested:** Gain $T$ and cutoff range $\omega_{M}<\omega_{c}<\omega_{s}-\omega_{M}$.

**Statement.** A signal with $\omega_{M} = 2000\pi$ rad/s is sampled at
$\omega_{s} = 6000\pi$ rad/s. Specify the gain and allowable cutoff range
of the ideal reconstruction LPF.

**Solution.**

**Step 1.** Sampling period: $T = 2\pi/\omega_{s} = 2\pi/(6000\pi) = 1/3$ ms.
The ideal LPF must have gain $T = 1/3$ ms in its passband.

**Step 2.** The cutoff must satisfy $\omega_{M}<\omega_{c}<\omega_{s}-\omega_{M}$,
i.e.,
$$2000\pi < \omega_{c} < 4000\pi\ \text{rad/s}.$$

A typical choice is the midpoint $\omega_{c} = \omega_{s}/2 = 3000\pi$ rad/s.

**Result.**
$$\boxed{\,\text{Gain}=T=1/3\text{ ms};\quad \omega_{c}\in(2000\pi,4000\pi)\text{ rad/s}.\,}$$

---

## Lecture 23 — Linear Feedback Systems

### Problem P23.1 — Closed-Loop Transfer Function
**Topic:** Negative feedback formula $Q = H/(1+GH)$.
**Concept tested:** Simplify a single forward path with proportional feedback.

**Statement.** With forward path $H(s) = 3/(s+2)$ and feedback $G(s) = 4$
in a unity-summer negative-feedback loop, find $Q(s)$ and classify stability.

**Solution.**

**Step 1.**
$$Q(s) = \frac{H(s)}{1+G(s)H(s)} = \frac{3/(s+2)}{1+12/(s+2)} = \frac{3}{s+2+12} = \frac{3}{s+14}.$$

**Step 2.** Pole at $s=-14$ (LHP) $\Rightarrow$ stable.

**Result.**
$$\boxed{\,Q(s) = \frac{3}{s+14};\ \text{stable.}\,}$$

Feedback moved the pole from $s=-2$ (open loop) to $s=-14$ (faster).

---

### Problem P23.2 — Stability vs. Gain (Second-Order)
**Topic:** Characteristic equation; Routh for $s^{2}+a_{1}s+a_{0}$.
**Concept tested:** Find the range of $K$ for closed-loop stability.

**Statement.** Plant $H(s) = K/(s^{2}+3s+4)$ is placed in a unity-feedback
loop (with no extra gain in the feedback path). For what real $K$ is the
closed-loop system stable?

**Solution.**

**Step 1.** Closed-loop characteristic polynomial:
$$1+\frac{K}{s^{2}+3s+4} = 0\Rightarrow s^{2}+3s+(4+K) = 0.$$

**Step 2.** For $s^{2}+a_{1}s+a_{0}$, stability requires $a_{1}>0$ and $a_{0}>0$:
- $a_{1} = 3>0$ $\checkmark$
- $a_{0} = 4+K > 0 \Rightarrow K>-4$.

**Result.**
$$\boxed{\,\text{Closed loop is stable iff }K > -4.\,}$$

---

### Problem P23.3 — Stabilizing a Plant with a RHP Pole
**Topic:** Feedback can move an unstable pole into the LHP.
**Concept tested:** Compute the stability range when the plant already has a RHP pole.

**Statement.** Plant $H(s) = 4/((s-2)(s+3))$ is placed in unity negative
feedback with forward gain $K$. Find the range of $K$ for closed-loop
stability.

**Solution.**

**Step 1.** Characteristic polynomial:
$$(s-2)(s+3)+4K = s^{2}+s-6+4K = 0.$$

**Step 2.** Routh condition for $s^{2}+a_{1}s+a_{0}$:
- $a_{1} = 1>0$ $\checkmark$
- $a_{0} = 4K-6>0 \Rightarrow K > 3/2 = 1.5$.

**Result.**
$$\boxed{\,\text{Stable iff }K>1.5.\,}$$

For $K=2$: $s^{2}+s+2 = 0$, roots $s = -0.5\pm j\sqrt{7}/2$, both in the
LHP. Feedback has stabilized an otherwise unstable plant.

---

### Problem P23.4 — Nyquist Stability Check
**Topic:** Reading a Nyquist plot; critical point $-1/K$.
**Concept tested:** Determine whether the curve encircles the critical point.

**Statement.** An open-loop-stable $G(j\omega)H(j\omega)$ has a Nyquist
plot that crosses the negative real axis exactly once, at $-1/3$.
(a) Is the closed loop stable for $K=1$? (b) Find $K_{\max}$.

**Solution.**

**Step 1.** At $K=1$, the critical point is $-1/K = -1$. Since the plot
only reaches $-1/3$, it does not encircle $-1$. $\Rightarrow$ **Stable.**

**Step 2.** The stability boundary is where the critical point coincides
with the real-axis crossing:
$$-\frac{1}{K_{\max}} = -\frac{1}{3}\Rightarrow K_{\max} = 3.$$

**Result.**
$$\boxed{\,(a)\text{ stable},\quad K_{\max} = 3.\,}$$

---

### Problem P23.5 — Gain and Phase Margins from Bode
**Topic:** Reading GM, PM, maximum loop delay from Bode data.
**Concept tested:** Apply the margin and delay formulas.

**Statement.** Bode data for the open-loop $G(j\omega)H(j\omega)$:

| Frequency | $\lvert GH\rvert$ | $\angle GH$ |
|---|---|---|
| $\omega_{c} = 8$ rad/s | $0$ dB | $-135^{\circ}$ |
| $\omega_{\pi} = 25$ rad/s | $-20$ dB | $-180^{\circ}$ |

Find the phase margin, gain margin, the stability verdict, and the maximum
tolerable loop delay.

**Solution.**

**Step 1. PM.** At $\omega_{c} = 8$ rad/s:
$$\text{PM} = 180^{\circ}+\angle GH(\omega_{c}) = 180^{\circ}-135^{\circ} = 45^{\circ}.$$

**Step 2. GM.** At $\omega_{\pi} = 25$ rad/s:
$$\text{GM}_{\text{dB}} = 0-(-20) = 20\text{ dB},\qquad \text{GM}_{\text{linear}} = 10^{20/20} = 10.$$

**Step 3.** Both PM and GM are positive $\Rightarrow$ **stable**.

**Step 4. Max delay.** A pure delay $\tau$ adds phase $-\omega\tau$:
$$\tau_{\max} = \frac{\text{PM (rad)}}{\omega_{c}} = \frac{45^{\circ}\cdot\pi/180^{\circ}}{8} = \frac{\pi/4}{8} = \frac{\pi}{32}\approx 0.098\text{ s}.$$

**Result.**
$$\boxed{\,\text{PM}=45^{\circ},\ \text{GM}=20\text{ dB},\ \text{stable},\ \tau_{\max}\approx 98\text{ ms}.\,}$$

---

### Problem P23.6 — Cascade-then-Feedback
**Topic:** Block-diagram simplification (series $\to$ feedback).
**Concept tested:** Reduce a cascade first, then apply $Q = H/(1+H)$.

**Statement.** Two blocks $H_{1}(s) = 3/(s+3)$ and $H_{2}(s) = 2/(s+5)$
are in cascade in the forward path, with unity negative feedback wrapped
around the pair. Find $Q(s)$ and classify stability.

**Solution.**

**Step 1.** Forward cascade:
$$H(s) = H_{1}(s)H_{2}(s) = \frac{6}{(s+3)(s+5)} = \frac{6}{s^{2}+8s+15}.$$

**Step 2.** Unity negative feedback:
$$Q(s) = \frac{H(s)}{1+H(s)} = \frac{6/(s^{2}+8s+15)}{1+6/(s^{2}+8s+15)} = \frac{6}{s^{2}+8s+21}.$$

**Step 3.** Closed-loop poles:
$s = (-8\pm\sqrt{64-84})/2 = -4\pm j\sqrt{5}$. Both in the LHP.

**Result.**
$$\boxed{\,Q(s) = \frac{6}{s^{2}+8s+21};\ \text{stable (poles }s = -4\pm j\sqrt{5}\text{).}\,}$$

---

*Prepared for CEC 315 Exam 3 — Spring 2026. These are numerical variations
of the problems in `exam3_sample_problems.md`; same techniques, new data.
Total: 38 problems.*
