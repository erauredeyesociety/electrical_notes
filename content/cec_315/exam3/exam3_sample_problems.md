# CEC 315 — Exam 3 Sample Problems (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Exam 3 — Lectures 16–23
**Source:** Worked examples extracted from lecture PDFs / summaries.

Each problem lists: the problem statement, the lecture reference, a full step-by-step solution, the topic/technique used, and the concepts tested.

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

### Problem 16.1 — Right-Sided Exponential
**Reference:** Lecture 16, §16.4.1 (Example 9.1 in textbook).
**Topic:** Bilateral Laplace transform from definition; ROC.
**Concepts tested:** Definition of Laplace transform, geometric integral convergence, ROC.

**Statement.** Compute the Laplace transform of $x(t) = e^{-at}u(t)$ and specify the ROC.

**Solution.**

**Step 1.** Since $u(t)=0$ for $t<0$:
$$X(s) = \int_0^{\infty} e^{-at}e^{-st}\,dt = \int_0^{\infty} e^{-(s+a)t}\,dt.$$

**Step 2.** The integral converges iff $\operatorname{Re}\{s+a\}>0$, i.e., $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$. Then
$$X(s) = \left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_0^\infty = \frac{1}{s+a}.$$

**Result.**
$$\boxed{\,e^{-at}u(t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{1}{s+a},\quad \operatorname{Re}\{s\}>-\operatorname{Re}\{a\}\,}$$

---

### Problem 16.2 — Left-Sided Exponential
**Reference:** Lecture 16, §16.4.2.
**Topic:** Laplace transform of left-sided signals.
**Concepts tested:** ROC direction for left-sided signals; ROC distinguishes signals with the same $X(s)$.

**Statement.** Compute the Laplace transform of $x(t) = -e^{-at}u(-t)$.

**Solution.**

**Step 1.** $u(-t)=1$ for $t<0$:
$$X(s) = -\int_{-\infty}^{0} e^{-(s+a)t}\,dt.$$

**Step 2.** As $t\to-\infty$ the integrand decays iff $\operatorname{Re}\{s+a\}<0$, so $\operatorname{Re}\{s\} < -\operatorname{Re}\{a\}$. Evaluating:
$$X(s) = \frac{1}{s+a}.$$

**Result.**
$$\boxed{\,-e^{-at}u(-t)\ \overset{\mathcal{L}}{\longleftrightarrow}\ \frac{1}{s+a},\quad \operatorname{Re}\{s\}<-\operatorname{Re}\{a\}\,}$$

**Remark.** The algebraic form is identical to Problem 16.1 — only the ROC distinguishes the two signals. **Always state the ROC.**

---

### Problem 16.3 — Two-Sided Signal
**Reference:** Lecture 16, §16.4.4.
**Topic:** Linearity; intersecting ROCs.
**Concepts tested:** Right-sided + left-sided decomposition; strip ROC.

**Statement.** Find $X(s)$ and the ROC of
$$x(t) = e^{-3t}u(t) + 2e^{2t}u(-t).$$

**Solution.**

**Step 1.** Transform each piece.
$$e^{-3t}u(t)\leftrightarrow \frac{1}{s+3},\quad \operatorname{Re}\{s\}>-3.$$
$$2e^{2t}u(-t) = -2\cdot[-e^{2t}u(-t)] \leftrightarrow \frac{-2}{s-2},\quad \operatorname{Re}\{s\}<2.$$

**Step 2.** Add and intersect ROCs.
$$X(s) = \frac{1}{s+3} - \frac{2}{s-2},\qquad -3<\operatorname{Re}\{s\}<2.$$

**Remark.** The ROC is a vertical strip between poles $s=-3$ and $s=2$.

---

### Problem 16.4 — Sum of Two Right-Sided Exponentials
**Reference:** Lecture 16, §16.7.1.
**Topic:** Linearity; consolidating ROCs.

**Statement.** Find $X(s)$ for $x(t)=3e^{-2t}u(t) - 2e^{-5t}u(t)$.

**Solution.**
$$X(s) = \frac{3}{s+2} - \frac{2}{s+5} = \frac{3(s+5)-2(s+2)}{(s+2)(s+5)} = \frac{s+11}{(s+2)(s+5)},$$
ROC: $\operatorname{Re}\{s\}>-2$.

---

### Problem 16.5 — Unit Step
**Reference:** Lecture 16, §16.7.3.
**Topic:** Fundamental Laplace pairs.

**Statement.** Compute $\mathcal{L}\{u(t)\}$.

**Solution.** Set $a=0$ in Problem 16.1:
$$u(t)\leftrightarrow \frac{1}{s},\quad \operatorname{Re}\{s\}>0.$$

The pole is on the $j\omega$-axis; the ROC does **not** include it, so the FT of $u(t)$ cannot be obtained by simply setting $s=j\omega$.

---

## Lecture 17 — Inverse Laplace and Properties

### Problem 17.1 — Distinct Real Poles
**Reference:** Lecture 17, §17.3.
**Topic:** Partial fraction expansion; cover-up method.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{2s+6}{(s+1)(s+3)},\quad \operatorname{Re}\{s\}>-1.$$

**Solution.**

**Step 1.** PFE:
$$\frac{2s+6}{(s+1)(s+3)} = \frac{A}{s+1}+\frac{B}{s+3}.$$

Cover-up at $s=-1$: $2(-1)+6 = A(-1+3) \Rightarrow A = 2$.
Cover-up at $s=-3$: $2(-3)+6 = B(-3+1) \Rightarrow B = 0$.

**Step 2.** ROC is to the right of both poles $\Rightarrow$ right-sided.

**Step 3.** Invert:
$$\boxed{x(t) = 2e^{-t}u(t)}.$$

---

### Problem 17.2 — Distinct Poles with Mixed ROC
**Reference:** Lecture 17, §17.4.
**Topic:** ROC determines direction of each term.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{5s+17}{(s+1)(s-3)},\quad -1<\operatorname{Re}\{s\}<3.$$

**Solution.**

**PFE.** $A=-3$, $B=8$ (via cover-up).
$$X(s) = \frac{-3}{s+1}+\frac{8}{s-3}.$$

**Direction:** ROC is right of $s=-1$ (right-sided term) and left of $s=3$ (left-sided term).

**Invert.**
$$\boxed{x(t) = -3e^{-t}u(t) - 8e^{3t}u(-t)}.$$

---

### Problem 17.3 — Repeated Poles
**Reference:** Lecture 17, §17.5.
**Topic:** Partial fractions with repeated poles.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{4s+5}{(s+1)^2(s+3)},\quad \operatorname{Re}\{s\}>-1.$$

**Solution.**

$$\frac{4s+5}{(s+1)^2(s+3)} = \frac{A}{s+1}+\frac{B}{(s+1)^2}+\frac{C}{s+3}.$$

- $s=-3$: $-7 = 4C \Rightarrow C = -7/4$.
- $s=-1$: $1 = 2B \Rightarrow B = 1/2$.
- Coefficient of $s^2$: $0 = A+C \Rightarrow A = 7/4$.

**Invert** (all right-sided):
$$\boxed{x(t) = \tfrac{7}{4}e^{-t}u(t) + \tfrac{1}{2}te^{-t}u(t) - \tfrac{7}{4}e^{-3t}u(t)}.$$

---

### Problem 17.4 — Complex Conjugate Poles
**Reference:** Lecture 17, §17.6.
**Topic:** Complete the square; damped sinusoid pairs.

**Statement.** Find $x(t)$ given
$$X(s) = \frac{2s}{s^2+4s+13},\quad \operatorname{Re}\{s\}>-2.$$

**Solution.**

Complete the square: $s^2+4s+13 = (s+2)^2+3^2$, poles at $s=-2\pm j3$.

Rewrite numerator: $2s = 2(s+2)-4$.

$$X(s) = 2\cdot\frac{s+2}{(s+2)^2+9} - \frac{4}{3}\cdot\frac{3}{(s+2)^2+9}.$$

Invert:
$$\boxed{x(t) = \left[2e^{-2t}\cos(3t) - \tfrac{4}{3}e^{-2t}\sin(3t)\right]u(t)}.$$

---

### Problem 17.5 — $s$-Domain Shifting
**Reference:** Lecture 17, §17.8.2.
**Topic:** Property-based transform derivation.

**Statement.** Find $\mathcal{L}\{e^{-3t}\cos(5t)u(t)\}$.

**Solution.** Start from $\cos(5t)u(t)\leftrightarrow s/(s^2+25)$. Applying $e^{-3t}x(t)\leftrightarrow X(s+3)$:
$$e^{-3t}\cos(5t)u(t)\leftrightarrow \frac{s+3}{(s+3)^2+25},\quad \operatorname{Re}\{s\}>-3.$$

---

### Problem 17.6 — Initial/Final Value Theorems
**Reference:** Lecture 17, §17.9.
**Topic:** Boundary behavior without inversion.

**Statement.** Given $X(s) = \dfrac{10}{s(s+2)(s+5)}$, ROC $\operatorname{Re}\{s\}>0$, find $x(0^+)$ and $x(\infty)$.

**Solution.**
$$x(0^+) = \lim_{s\to\infty}sX(s) = \lim_{s\to\infty}\frac{10}{(s+2)(s+5)} = 0.$$

Check final-value validity: $sX(s) = 10/[(s+2)(s+5)]$ has poles at $-2,-5$ (both in LHP). $\checkmark$
$$x(\infty) = \lim_{s\to 0}\frac{10}{(s+2)(s+5)} = \frac{10}{10} = 1.$$

---

## Lecture 18 — System Analysis via Unilateral Laplace

### Problem 18.1 — Differential Equation to $H(s)$
**Reference:** Lecture 18, §18.2.
**Topic:** $H(s)$ from an ODE.

**Statement.** Find $H(s)$ for the system
$$\frac{d^2y}{dt^2}+5\frac{dy}{dt}+6y = 2\frac{dx}{dt}+x.$$

**Solution.** Replace $d^k/dt^k\to s^k$ with zero ICs:
$$(s^2+5s+6)Y(s) = (2s+1)X(s)\Rightarrow H(s) = \frac{2s+1}{(s+2)(s+3)}.$$

Poles: $s=-2,-3$ (LHP); zero: $s=-1/2$. **Causal and stable.**

---

### Problem 18.2 — Stability Classification
**Reference:** Lecture 18, §18.5.
**Topic:** Causality + stability from pole locations.

**Statement.** Classify the following causal LTI systems.

| $H(s)$ | Poles | Classification |
|---|---|---|
| $\dfrac{1}{s+3}$ | $-3$ | Stable |
| $\dfrac{1}{s-2}$ | $+2$ | Unstable |
| $\dfrac{1}{s^2+4}$ | $\pm j2$ | Marginally stable |
| $\dfrac{s+1}{(s+2)(s+5)}$ | $-2,-5$ | Stable |
| $\dfrac{1}{(s+1)(s-1)}$ | $\pm 1$ | Unstable (RHP pole) |

---

### Problem 18.3 — Complete Pipeline
**Reference:** Lecture 18, §18.6.
**Topic:** DE $\to$ $H(s)\to$ output.

**Statement.** Solve $\dfrac{dy}{dt}+3y = x(t)$ with $x(t)=e^{-t}u(t)$, zero ICs.

**Solution.**
$H(s)=1/(s+3)$; $X(s)=1/(s+1)$;
$$Y(s) = \frac{1}{(s+1)(s+3)} = \frac{1/2}{s+1}-\frac{1/2}{s+3}.$$
$$\boxed{y(t) = \tfrac{1}{2}(e^{-t}-e^{-3t})u(t)}.$$

Checks: $y(0^+)=0$, $y(\infty)=0$; both decay.

---

### Problem 18.4 — First-Order ODE with IC
**Reference:** Lecture 18, §18.11.
**Topic:** Unilateral Laplace with initial conditions.

**Statement.** Solve $\dfrac{dy}{dt}+3y = 0$, $y(0^-)=5$.

**Solution.** Unilateral Laplace:
$$sY(s)-5+3Y(s) = 0\Rightarrow Y(s)=\frac{5}{s+3}.$$
$$\boxed{y(t) = 5e^{-3t}u(t)}.$$

---

### Problem 18.5 — Second-Order ODE with ICs
**Reference:** Lecture 18, §18.11.
**Topic:** Unilateral Laplace, second derivative IC formula.

**Statement.** Solve $\dfrac{d^2y}{dt^2}+5\dfrac{dy}{dt}+6y = 2u(t)$, $y(0^-)=1$, $y'(0^-)=0$.

**Solution.**
$$s^2Y - s - 0 + 5(sY - 1)+6Y = \frac{2}{s}$$
$$(s^2+5s+6)Y = \frac{2}{s}+s+5$$
$$Y(s) = \frac{s^2+5s+2}{s(s+2)(s+3)} = \frac{1/3}{s}+\frac{2}{s+2}+\frac{-4/3}{s+3}.$$

Cover-up: $A=1/3$, $B=2$, $C=-4/3$.

$$\boxed{y(t) = \left[\tfrac{1}{3}+2e^{-2t}-\tfrac{4}{3}e^{-3t}\right]u(t)}.$$

Checks: $y(0)=1/3+2-4/3 = 1$. $y(\infty)=1/3$. $y'(0) = -4+4 = 0$. $\checkmark$

---

## Lecture 19 — Z-Transform and ROC

### Problem 19.1 — Right-Sided Geometric Sequence
**Reference:** Lecture 19, §19.4.1.
**Topic:** Geometric series; basic Z pair.

**Statement.** Find $X(z)$ and the ROC of $x[n]=a^n u[n]$.

**Solution.**
$$X(z) = \sum_{n=0}^\infty a^n z^{-n} = \sum_{n=0}^\infty (az^{-1})^n = \frac{1}{1-az^{-1}},$$
valid for $|az^{-1}|<1$, i.e., $|z|>|a|$.

$$\boxed{a^n u[n]\ \overset{\mathcal{Z}}{\longleftrightarrow}\ \frac{1}{1-az^{-1}},\quad |z|>|a|.}$$

---

### Problem 19.2 — Left-Sided Geometric Sequence
**Reference:** Lecture 19, §19.4.2.
**Topic:** Left-sided signals; annular ROC.

**Statement.** Find $X(z)$ for $x[n]=-a^n u[-n-1]$.

**Solution.**
$$X(z) = -\sum_{n=-\infty}^{-1}(az^{-1})^n.$$
Substitute $m=-n$:
$$X(z) = -\sum_{m=1}^\infty (a^{-1}z)^m = -\frac{z/a}{1-z/a} = \frac{1}{1-az^{-1}},\quad |z|<|a|.$$

The algebraic expression is identical to Problem 19.1; only the ROC differs.

---

### Problem 19.3 — Two-Sided Signal
**Reference:** Lecture 19, §19.4.5.
**Topic:** Linearity with annular ROC.

**Statement.** Find $X(z)$ for $x[n] = (0.5)^n u[n] + 2(3)^n u[-n-1]$.

**Solution.**

Right-sided: $(0.5)^n u[n] \leftrightarrow 1/(1-0.5z^{-1})$, $|z|>0.5$.

Left-sided: $2(3)^n u[-n-1] = -2\cdot[-(3)^n u[-n-1]] \leftrightarrow -2/(1-3z^{-1})$, $|z|<3$.

Intersection: $0.5<|z|<3$ (annular ring).

$$X(z) = \frac{1}{1-0.5z^{-1}} - \frac{2}{1-3z^{-1}},\quad 0.5<|z|<3.$$

---

### Problem 19.4 — Sum of Two Right-Sided Sequences
**Reference:** Lecture 19, §19.4.6.
**Topic:** Combining right-sided pairs.

**Statement.** Find $X(z)$ for $x[n]=3(0.4)^n u[n] - 2(0.8)^n u[n]$.

**Solution.**
$$X(z) = \frac{3}{1-0.4z^{-1}} - \frac{2}{1-0.8z^{-1}} = \frac{1-1.6z^{-1}}{(1-0.4z^{-1})(1-0.8z^{-1})},$$
ROC: $|z|>0.8$.

Poles at $z=0.4,0.8$; zero at $z=1.6$. Sanity check at $z=1$: $X(1) = -0.6/0.12 = -5$ matches direct sum $5-10=-5$. $\checkmark$

---

### Problem 19.5 — Finite-Duration Sequence
**Reference:** Lecture 19, §19.4.7.
**Topic:** Polynomial-form Z transform.

**Statement.** Find $X(z)$ for $x[n]=\{2,-1,3,0,4\}$, $n=0,\ldots,4$ (zero elsewhere).

**Solution.**
$$X(z) = 2 - z^{-1}+3z^{-2}+4z^{-4}.$$
ROC: all $z\neq 0$.

Check: $X(1)=2-1+3+0+4=8=\sum x[n]$. $\checkmark$

---

## Lecture 20 — Inverse Z-Transform and Properties

### Problem 20.1 — Distinct Real Poles, Right-Sided
**Reference:** Lecture 20, §20.3.
**Topic:** Partial fractions in $z^{-1}$.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{3-z^{-1}}{(1-0.5z^{-1})(1-0.25z^{-1})},\quad |z|>0.5.$$

**Solution.** PFE with $A=2$, $B=1$ (set $z^{-1}=2$ and $z^{-1}=4$).
$$X(z) = \frac{2}{1-0.5z^{-1}} + \frac{1}{1-0.25z^{-1}}.$$

ROC outside both poles $\Rightarrow$ both right-sided:
$$\boxed{x[n] = 2(0.5)^n u[n] + (0.25)^n u[n]}.$$

Check: $x[0]=3$; from IVT $\lim_{z\to\infty}X(z)=3$. $\checkmark$

---

### Problem 20.2 — Mixed ROC
**Reference:** Lecture 20, §20.4.
**Topic:** Two-sided inversion.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{1}{(1-2z^{-1})(1-0.5z^{-1})},\quad 0.5<|z|<2.$$

**Solution.** PFE: $A=4/3$ (at $z^{-1}=2$), $B=-1/3$ (at $z^{-1}=1/0.5=2$... carefully: kill first factor with $z^{-1}=1/0.5=2$ gives $B$... actually kill $(1-2z^{-1})$ with $z^{-1}=0.5$, yields $A=4/3$; kill $(1-0.5z^{-1})$ with $z^{-1}=2$ yields $B=-1/3$).

$$X(z) = \frac{4/3}{1-2z^{-1}} + \frac{-1/3}{1-0.5z^{-1}}.$$

Directions from ROC $0.5<|z|<2$:
- Pole at $z=2$: ROC inside $\Rightarrow$ left-sided.
- Pole at $z=0.5$: ROC outside $\Rightarrow$ right-sided.

$$\boxed{x[n] = -\tfrac{4}{3}\cdot 2^n u[-n-1] - \tfrac{1}{3}(0.5)^n u[n]}.$$

---

### Problem 20.3 — Repeated Poles
**Reference:** Lecture 20, §20.5.
**Topic:** Repeated-pole pair $(n+1)a^n u[n]$.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{1}{(1-0.5z^{-1})^2},\quad |z|>0.5.$$

**Solution.** Using the pair $\dfrac{1}{(1-az^{-1})^2}\leftrightarrow (n+1)a^n u[n]$:
$$\boxed{x[n] = (n+1)(0.5)^n u[n]}.$$

Check: $x[0]=1$, $x[1]=1$, $x[2]=0.75$. $\checkmark$

---

### Problem 20.4 — Complex Conjugate Poles
**Reference:** Lecture 20, §20.6.
**Topic:** Damped DT sinusoid pair.

**Statement.** Find $x[n]$ given
$$X(z) = \frac{1-0.8\cos(0.4\pi)z^{-1}}{1-2\cdot 0.8\cos(0.4\pi)z^{-1}+0.64z^{-2}},\quad |z|>0.8.$$

**Solution.** Match the pair $r^n\cos(\omega_0 n)u[n]\leftrightarrow\ldots$: read off $r=0.8$, $\omega_0=0.4\pi$.

$$\boxed{x[n] = (0.8)^n\cos(0.4\pi n)u[n]}.$$

---

### Problem 20.5 — Time-Shift Property
**Reference:** Lecture 20, §20.8.2.
**Topic:** Delay as $z^{-n_0}$.

**Statement.** Given $x[n]=(0.5)^n u[n]$, find the Z-transform of $y[n]=x[n-3]$.

**Solution.**
$$Y(z) = z^{-3}\cdot\frac{1}{1-0.5z^{-1}} = \frac{z^{-3}}{1-0.5z^{-1}},\quad |z|>0.5.$$

---

### Problem 20.6 — Initial and Final Value Theorems
**Reference:** Lecture 20, §20.8.4.
**Topic:** Z initial/final value theorems.

**Statement.** Given $X(z) = \dfrac{5}{(1-z^{-1})(1-0.6z^{-1})}$, $|z|>1$. Find $x[0]$ and $x[\infty]$.

**Solution.**
$$x[0] = \lim_{z\to\infty}X(z) = \frac{5}{1\cdot 1} = 5.$$

Validity check: $(1-z^{-1})X(z) = 5/(1-0.6z^{-1})$ has a single pole at $z=0.6$ (inside unit circle). $\checkmark$
$$x[\infty] = \lim_{z\to 1}\frac{5}{1-0.6z^{-1}} = \frac{5}{0.4} = 12.5.$$

---

## Lecture 21 — System Analysis via Unilateral Z

### Problem 21.1 — Difference Equation to $H(z)$
**Reference:** Lecture 21, §21.2.
**Topic:** Deriving $H(z)$.

**Statement.** Find $H(z)$ for
$$y[n] - 0.8y[n-1]+0.15y[n-2] = x[n]+2x[n-1].$$

**Solution.**
$$(1-0.8z^{-1}+0.15z^{-2})Y(z) = (1+2z^{-1})X(z).$$

Factor denominator ($z^2-0.8z+0.15=0$, roots $z=0.5,0.3$):
$$H(z) = \frac{1+2z^{-1}}{(1-0.5z^{-1})(1-0.3z^{-1})}.$$

Poles $0.5, 0.3$ inside unit circle $\Rightarrow$ causal + stable. Zero at $z=-2$.

---

### Problem 21.2 — Full Pipeline (Difference Equation to Output)
**Reference:** Lecture 21, §21.4.
**Topic:** Complete DT system response.

**Statement.** Solve $y[n]-0.5y[n-1]=x[n]$ with $x[n]=(0.8)^n u[n]$, $y[-1]=0$.

**Solution.**
$H(z) = 1/(1-0.5z^{-1})$; $X(z) = 1/(1-0.8z^{-1})$;
$$Y(z) = \frac{1}{(1-0.5z^{-1})(1-0.8z^{-1})} = \frac{-5/3}{1-0.5z^{-1}} + \frac{8/3}{1-0.8z^{-1}}.$$

$$\boxed{y[n] = \left[-\tfrac{5}{3}(0.5)^n + \tfrac{8}{3}(0.8)^n\right]u[n]}.$$

Check: $y[0] = -5/3+8/3 = 1 = x[0]$. $\checkmark$

---

### Problem 21.3 — First-Order Difference Equation with IC
**Reference:** Lecture 21, §21.8.
**Topic:** Unilateral Z with initial conditions.

**Statement.** Solve $y[n]-0.6y[n-1]=(0.5)^n u[n]$, $y[-1]=4$.

**Solution.** Unilateral Z:
$$Y(z) - 0.6[z^{-1}Y(z)+4] = \frac{1}{1-0.5z^{-1}}$$
$$(1-0.6z^{-1})Y(z) = \frac{1}{1-0.5z^{-1}}+2.4.$$

Solve:
$$Y(z) = \frac{1}{(1-0.5z^{-1})(1-0.6z^{-1})} + \frac{2.4}{1-0.6z^{-1}}.$$

PFE on first term: $A=-5$ (at $z^{-1}=2$), $B=6$ (at $z^{-1}=5/3$).

$$Y(z) = \frac{-5}{1-0.5z^{-1}} + \frac{8.4}{1-0.6z^{-1}}.$$

$$\boxed{y[n] = \left[-5(0.5)^n + 8.4(0.6)^n\right]u[n]}.$$

Check: $y[0] = -5+8.4 = 3.4$; ODE says $y[0]=0.6(4)+1=3.4$. $\checkmark$

---

### Problem 21.4 — Second-Order Zero-Input Response
**Reference:** Lecture 21, §21.8.
**Topic:** Natural response from initial conditions.

**Statement.** Solve $y[n]-0.7y[n-1]+0.1y[n-2]=0$, $y[-1]=1$, $y[-2]=0$.

**Solution.** Unilateral Z:
$Y - 0.7(z^{-1}Y + 1) + 0.1(z^{-2}Y + z^{-1}) = 0$,
$$(1-0.7z^{-1}+0.1z^{-2})Y = 0.7 - 0.1z^{-1}.$$

Factor: poles at $z=0.5$ and $z=0.2$.
$$Y(z) = \frac{0.7-0.1z^{-1}}{(1-0.5z^{-1})(1-0.2z^{-1})} = \frac{5/6}{1-0.5z^{-1}} - \frac{2/15}{1-0.2z^{-1}}.$$

$$\boxed{y[n] = \left[\tfrac{5}{6}(0.5)^n - \tfrac{2}{15}(0.2)^n\right]u[n]}.$$

Check: $y[0]=5/6-2/15 = 21/30 = 0.7$; from ODE $y[0]=0.7(1)-0.1(0)=0.7$. $\checkmark$

---

## Lecture 22 — Sampling

### Problem 22.1 — Nyquist Rate of a Sum of Sinusoids
**Reference:** Lecture 22, Example 22.1(a).
**Topic:** Identify highest frequency; Nyquist rate.

**Statement.** Find the Nyquist rate of
$$x(t) = 1 + \cos(2000\pi t) + \sin(4000\pi t).$$

**Solution.** Highest frequency is $\omega_M = 4000\pi$ rad/s $= 2000$ Hz.
$$\text{Nyquist rate} = 2\omega_M = 8000\pi\text{ rad/s} = 4000\text{ Hz}.$$

---

### Problem 22.2 — Nyquist Rate of a Sinc
**Reference:** Lecture 22, Example 22.1(b).
**Topic:** Time/frequency duality; sinc $\leftrightarrow$ rect.

**Statement.** Find the Nyquist rate of $x(t) = \dfrac{\sin(4000\pi t)}{\pi t}$.

**Solution.** $X(j\omega)$ is a rectangle with $|\omega|<4000\pi$. So $\omega_M = 4000\pi$ and Nyquist rate is $8000\pi$ rad/s $= 4000$ Hz.

---

### Problem 22.3 — Nyquist Rate of a Squared Sinc
**Reference:** Lecture 22, Example 22.1(c).
**Topic:** Squaring doubles bandwidth.

**Statement.** Find the Nyquist rate of $x(t) = \left(\dfrac{\sin(4000\pi t)}{\pi t}\right)^2$.

**Solution.** Squaring in time = self-convolution in frequency. Rect $*$ Rect $=$ Triangle of total width $2\times 8000\pi$, so $\omega_M = 8000\pi$.
$$\text{Nyquist rate} = 16000\pi\text{ rad/s} = 8000\text{ Hz}.$$

**Lesson:** Squaring doubles bandwidth.

---

### Problem 22.4 — Checking a Sampling Period
**Reference:** Lecture 22, Example 22.2.
**Topic:** Converting the sampling theorem to $T$.

**Statement.** A signal has $X(j\omega)=0$ for $|\omega|>1000\pi$ rad/s. Which of these $T$ work?

(a) $T = 0.5$ ms, (b) $T = 2$ ms, (c) $T = 0.1$ ms.

**Solution.** $\omega_M = 1000\pi$, need $\omega_s > 2000\pi$, i.e., $T < 1$ ms.

- (a) $0.5$ ms $< 1$ ms $\Rightarrow$ works.
- (b) $2$ ms $> 1$ ms $\Rightarrow$ aliases.
- (c) $0.1$ ms $< 1$ ms $\Rightarrow$ works.

---

### Problem 22.5 — Sampling at Exactly Nyquist Fails
**Reference:** Lecture 22, Example 22.3.
**Topic:** Why the strict inequality matters.

**Statement.** Sample $x(t)=\sin(\omega_s t/2)$ at frequency $\omega_s$. What are the samples?

**Solution.** Sample points: $x(nT) = \sin(\omega_s/2 \cdot 2\pi n/\omega_s) = \sin(\pi n) = 0$ for all integer $n$. All samples are zero! Therefore, sampling at exactly the Nyquist rate cannot recover the signal.

---

### Problem 22.6 — Aliasing of a Cosine
**Reference:** Lecture 22, Example 22.4.
**Topic:** Alias formula $f_\text{alias}=|f_s-f_0|$.

**Statement.** A 5 Hz cosine is sampled at $f_s = 6$ Hz. What is the reconstructed frequency?

**Solution.** Nyquist rate is 10 Hz; $f_s=6$ is too low. Aliased frequency:
$$f_\text{alias} = |f_s - f_0| = |6-5| = 1\text{ Hz}.$$

The 5 Hz signal looks like 1 Hz after reconstruction.

---

## Lecture 23 — Linear Feedback Systems

### Problem 23.1 — Cascade + Feedback
**Reference:** Lecture 23, Worked Example 23.1.
**Topic:** Block diagram simplification.

**Statement.** With $H_1(s)=1/(s+1)$, $H_2(s)=1/(s+3)$, $G=2$ in the forward cascade-then-feedback configuration, find the closed-loop $Q(s)$.

**Solution.**

Cascade: $H_1 H_2 = 1/(s^2+4s+3)$.

Feedback:
$$Q(s) = \frac{H_1 H_2}{1+2H_1 H_2} = \frac{1}{s^2+4s+5}.$$

Poles: $s=-2\pm j$ (LHP) $\Rightarrow$ stable.

---

### Problem 23.2 — Unity Feedback with Adjustable Gain
**Reference:** Lecture 23, Worked Example 23.2.
**Topic:** Pole locations as a function of $K$.

**Statement.** $H(s) = K/(s+2)$, unity feedback. Find the closed-loop pole as a function of $K$ and determine the stability range.

**Solution.**
$$Q(s) = \frac{K/(s+2)}{1+K/(s+2)} = \frac{K}{s+2+K}.$$

Pole at $s=-(2+K)$. Stable iff $K>-2$.

Examples: $K=0\Rightarrow s=-2$; $K=8\Rightarrow s=-10$ (faster); $K=-3\Rightarrow s=+1$ (unstable).

---

### Problem 23.3 — Stabilizing an Unstable Plant
**Reference:** Lecture 23, Worked Example 23.3.
**Topic:** Feedback can stabilize.

**Statement.** Plant $H(s)=3/(s-1)$ (pole at $+1$). Apply unity feedback with gain $K$. Find the stability range.

**Solution.**
$$Q(s) = \frac{3K}{s-1+3K}.$$

Closed-loop pole at $s=1-3K$. Stable iff $1-3K<0$, so $K>1/3$.

For $K=1$: pole at $s=-2$. Feedback converted an unstable plant into a stable closed-loop system.

---

### Problem 23.4 — Nyquist Stability Check
**Reference:** Lecture 23, Worked Example 23.5.
**Topic:** Reading Nyquist data; critical point.

**Statement.** A system's Nyquist plot crosses the negative real axis at $-0.5$. The open-loop is stable. (a) Is the closed-loop stable at $K=1$? (b) What is the maximum $K$?

**Solution.**

(a) $-1/K = -1$; since the curve reaches only $-0.5$, the point $-1$ is not encircled $\Rightarrow$ **stable**.

(b) Instability at $-1/K = -0.5$ $\Rightarrow$ $K_\text{max} = 2$.

---

### Problem 23.5 — Gain and Phase Margins
**Reference:** Lecture 23, Worked Example 23.6.
**Topic:** Reading margins from Bode data.

**Statement.** From Bode data:

| Frequency | $|GH|$ | $\angle GH$ |
|---|---|---|
| $\omega_2 = 10$ rad/s | 0 dB | $-135°$ |
| $\omega_1 = 31$ rad/s | $-12$ dB | $-180°$ |

Find PM, GM, stability, and the maximum tolerable time delay.

**Solution.**

**Phase margin:** $\text{PM} = 180°+(-135°) = 45°$.

**Gain margin:** $\text{GM} = 0 - (-12) = 12$ dB, i.e., factor $10^{12/20} = 4$.

Both positive $\Rightarrow$ **stable**.

**Max delay:** A delay $\tau$ adds phase $-\omega\tau$. At $\omega_2=10$:
$$\tau_\text{max} = \frac{\text{PM (rad)}}{\omega_2} = \frac{45° \cdot \pi/180°}{10} = \frac{0.785}{10} \approx 79\text{ ms}.$$

---

*Prepared for CEC 315 Exam 3 — Spring 2026.*
