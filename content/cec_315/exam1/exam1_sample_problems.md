# CEC 315 — Exam 1 Sample Problems (Lectures 2–8)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Exam 1 — Lectures 2–8
**Source:** Worked examples extracted from the lecture PDFs / summaries.

Each problem lists: the problem statement, the lecture reference, a full step-by-step solution, the topic / technique used, and the concepts tested.

---

## Table of Contents

- [Lecture 2 — Signal Definitions and Transformations](#lecture-2--signal-definitions-and-transformations)
- [Lecture 3 — Complex Exponentials and Sinusoidal Signals](#lecture-3--complex-exponentials-and-sinusoidal-signals)
- [Lecture 4 — Key Functions and System Basics](#lecture-4--key-functions-and-system-basics)
- [Lecture 5 — Basic System Properties](#lecture-5--basic-system-properties)
- [Lecture 6 — DT LTI Convolution](#lecture-6--dt-lti-convolution)
- [Lecture 7 — CT LTI Properties and Convolution](#lecture-7--ct-lti-properties-and-convolution)
- [Lecture 8 — Difference / Differential Equations and Singularity Functions](#lecture-8--difference--differential-equations-and-singularity-functions)

---

## Lecture 2 — Signal Definitions and Transformations

### Problem 2.1 — Time-Shift Sketch
**Reference:** Lecture 2, §2.4.1.
**Topic:** Time shift.
**Concepts tested:** Direction of delay/advance.

**Statement.** Let $x(t)$ be a triangular pulse nonzero only for $0\le t\le 2$. Sketch $x(t-3)$ and $x(t+1)$.

**Solution.**

- $x(t-3)$ is the same triangular pulse *delayed* by 3: it is nonzero for $3\le t\le 5$.
- $x(t+1)$ is the same triangular pulse *advanced* by 1: it is nonzero for $-1\le t\le 1$.

**Rule.** $x(t-t_0)$ delays by $t_0$ if $t_0>0$, advances if $t_0<0$.

---

### Problem 2.2 — Combined Scale and Shift
**Reference:** Lecture 2, §2.4 (combined transformations).
**Topic:** Order of operations for $x(at-b)$.
**Concepts tested:** Factoring out $a$ before shifting.

**Statement.** Given a signal $x(t)$ with support $[0,4]$, determine the support of $y(t)=x(2t-4)$.

**Solution.**

**Step 1.** Factor: $y(t)=x(2t-4)=x(2(t-2))$.

**Step 2.** Interpret: shift right by 2, then compress by a factor of 2.

**Step 3.** Work from the support. $x(\cdot)$ is nonzero when its argument lies in $[0,4]$:
$$0 \le 2t-4 \le 4 \;\Rightarrow\; 2\le t\le 4.$$

**Result.** $y(t)$ has support $[2,4]$. Length has halved (due to compression) and the pulse has moved.

---

### Problem 2.3 — Energy of a Rectangular Pulse
**Reference:** Lecture 2, §2.3.3.
**Topic:** Signal energy.
**Concepts tested:** Energy integral.

**Statement.** Compute $E_\infty$ for $x(t)=A$ for $0\le t\le T$, zero otherwise.

**Solution.**
$$E_\infty = \int_{-\infty}^\infty |x(t)|^2\,dt = \int_0^T A^2\,dt = A^2 T.$$

Since $E_\infty<\infty$, $P_\infty=0$ and $x$ is a **finite-energy** signal.

---

### Problem 2.4 — Power of a Sinusoid
**Reference:** Lecture 2, §2.3.4 / Lecture 3, §3.5.2.
**Topic:** Average power of a sinusoid.
**Concepts tested:** Infinite energy, finite power classification.

**Statement.** Compute $P_\infty$ for $x(t)=A\cos(\omega_0 t+\phi)$.

**Solution.**
$$P_\infty = \lim_{T\to\infty}\frac{1}{2T}\int_{-T}^T A^2\cos^2(\omega_0 t+\phi)\,dt.$$
Using $\cos^2\theta = \tfrac12(1+\cos 2\theta)$, the $\cos(2\omega_0 t+2\phi)$ term averages to 0. Thus
$$P_\infty = \frac{A^2}{2}.$$

Since $E_\infty=\infty$ but $P_\infty<\infty$, $x$ is a **finite-power** signal.

---

### Problem 2.5 — Even/Odd Decomposition
**Reference:** Lecture 2, §2.6.3.
**Topic:** Even/odd decomposition.

**Statement.** Decompose $x(t)=e^{-2t}u(t)$ into its even and odd parts.

**Solution.**
$$x_e(t) = \tfrac12[x(t)+x(-t)] = \tfrac12[e^{-2t}u(t)+e^{2t}u(-t)] = \tfrac12\,e^{-2|t|}.$$
$$x_o(t) = \tfrac12[x(t)-x(-t)] = \tfrac12[e^{-2t}u(t)-e^{2t}u(-t)] = \tfrac12\,\mathrm{sign}(t)\,e^{-2|t|}.$$

**Check.** $x_e(t)+x_o(t)=e^{-2t}u(t)$ for $t>0$ and $0$ for $t<0$.

---

## Lecture 3 — Complex Exponentials and Sinusoidal Signals

### Problem 3.1 — Rectangular / Polar Conversion
**Reference:** Lecture 3, §3.2.4.
**Topic:** Complex number form conversion.

**Statement.** Convert $c=1+j\sqrt 3$ to polar form $re^{j\theta}$.

**Solution.**
$$r=\sqrt{1^2+(\sqrt 3)^2}=\sqrt{4}=2,\qquad \theta=\mathrm{atan2}(\sqrt 3,1)=\pi/3.$$
$$c = 2e^{j\pi/3}.$$

---

### Problem 3.2 — Complex Multiplication
**Reference:** Lecture 3, §3.2.7.
**Topic:** Polar multiplication.

**Statement.** Compute $(2e^{j\pi/3})(3e^{j\pi/6})$ and write the result in rectangular form.

**Solution.** Magnitudes multiply, angles add:
$$= 6e^{j\pi/2} = 6(\cos\tfrac{\pi}{2}+j\sin\tfrac{\pi}{2}) = 6j.$$

---

### Problem 3.3 — Cosine Addition via Euler
**Reference:** Lecture 3, §3.8 (Exercise).
**Topic:** Deriving trig identities from Euler.

**Statement.** Derive $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$.

**Solution.**
$$e^{j(\alpha+\beta)}=e^{j\alpha}e^{j\beta}=(\cos\alpha+j\sin\alpha)(\cos\beta+j\sin\beta).$$

Expanding:
$$=(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+j(\sin\alpha\cos\beta+\cos\alpha\sin\beta).$$

Taking the real part: $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$. The imaginary part gives $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$.

---

### Problem 3.4 — CT Sinusoid Period
**Reference:** Lecture 3, §3.3 / §3.5.1.
**Topic:** Fundamental period of a CT sinusoid.

**Statement.** Find the fundamental period of $x(t)=5\cos(10\pi t + \pi/4)$.

**Solution.**
$\omega_0=10\pi$, so $T_0=2\pi/\omega_0 = 2\pi/(10\pi) = 0.2$ s.

---

### Problem 3.5 — DT Sinusoid Periodicity Test
**Reference:** Lecture 3, §3.7.
**Topic:** DT periodicity.
**Concepts tested:** $\omega_0/(2\pi)$ rational test.

**Statement.** Is $x[n]=\cos(n)$ periodic? How about $x[n]=\cos(\pi n/4)$?

**Solution.**

(a) $\cos(n)$: $\omega_0=1$, so $\omega_0/(2\pi)=1/(2\pi)$ which is **irrational**. **Not periodic.**

(b) $\cos(\pi n/4)$: $\omega_0=\pi/4$, so $\omega_0/(2\pi)=1/8$ is rational. Periodic with fundamental period $N_0=8$ (smallest integer such that $\omega_0 N_0$ is an integer multiple of $2\pi$).

---

### Problem 3.6 — Expressing a Real Sinusoid with Complex Exponentials
**Reference:** Lecture 3, §3.3.3.
**Topic:** Sinusoid $\leftrightarrow$ complex exponentials.

**Statement.** Express $x(t)=A\cos(\omega_0 t+\theta)$ as a sum of two complex exponentials.

**Solution.** Using $\cos\phi = \tfrac12(e^{j\phi}+e^{-j\phi})$:
$$x(t) = \frac{A}{2}e^{j(\omega_0 t+\theta)} + \frac{A}{2}e^{-j(\omega_0 t+\theta)} = \frac{A}{2}e^{j\theta}e^{j\omega_0 t} + \frac{A}{2}e^{-j\theta}e^{-j\omega_0 t}.$$

The complex amplitudes are $X_C=\tfrac{A}{2}e^{j\theta}$ and $X_C^*=\tfrac{A}{2}e^{-j\theta}$ — symmetric, matching the two-sided spectrum of a real sinusoid.

---

## Lecture 4 — Key Functions and System Basics

### Problem 4.1 — Sifting with Sum of Impulses
**Reference:** Lecture 4, Exercise 1.
**Topic:** CT integrator fed by impulse train.

**Statement.** A CT integrator $y(t)=\int_0^t x(\tau)\,d\tau$ is driven by $x(t)=\delta(t+1)+\delta(t-1)+\delta(t-3)$. Find $y(t)$ for $t\ge 0$.

**Solution.** Each impulse, once it lies inside the integration interval $[0,t]$, contributes a unit step.

- $\delta(t+1)$ is at $\tau=-1<0$, *outside* $[0,t]$ for every $t\ge 0$. Contributes 0.
- $\delta(t-1)$ enters once $t\ge 1$ $\Rightarrow u(t-1)$.
- $\delta(t-3)$ enters once $t\ge 3$ $\Rightarrow u(t-3)$.

**Result.** $y(t)=u(t-1)+u(t-3)$ — a staircase stepping up at $t=1$ and $t=3$.

---

### Problem 4.2 — CT Differentiator with Rectangular Pulse
**Reference:** Lecture 4, Exercise 2.
**Topic:** Derivatives of unit steps.

**Statement.** A differentiator $y(t)=dx/dt$ is fed $x(t)=u(t)-u(t-2)$. Find $y(t)$.

**Solution.** Differentiate each term using $du/dt=\delta(t)$:
$$y(t)=\delta(t)-\delta(t-2).$$

Interpretation: an upward jump at $t=0$ (impulse of $+1$) and a downward jump at $t=2$ (impulse of $-1$).

---

### Problem 4.3 — Sifting Computation
**Reference:** Lecture 7, §7.2.2 (reinforces Lecture 4).
**Topic:** CT sifting property.

**Statement.** Evaluate $\displaystyle\int_{-\infty}^{\infty}(t^2+3t)\,\delta(t-2)\,dt$.

**Solution.** Set $t=2$ in $t^2+3t$: $4+6=10$.

**Result.** $\boxed{10}$.

---

### Problem 4.4 — Sifting with Limits
**Reference:** Lecture 7, §7.2.2 (warning).
**Topic:** Delta outside integration range.

**Statement.** Evaluate $\displaystyle\int_{0}^{5} x(t)\,\delta(t+2)\,dt$ for any continuous $x$.

**Solution.** The delta is at $t=-2$, which is **outside** $[0,5]$. The integral is $\boxed{0}$.

---

### Problem 4.5 — Sampling Multiplication
**Reference:** Lecture 4, §4.3.6 / Lecture 8, §8.6.2.
**Topic:** Impulse sampling property.

**Statement.** Simplify $(t^2+3)\,\delta(t-2)$.

**Solution.** $(t^2+3)\big|_{t=2}=7$, so
$$(t^2+3)\,\delta(t-2) = 7\,\delta(t-2).$$

The result is a *scaled impulse*, not a number — compare with Problem 4.3.

---

## Lecture 5 — Basic System Properties

### Problem 5.1 — Classify $y(t)=3x(t)+2$
**Reference:** Lecture 5, §5.5.2 / §5.6.5.
**Topic:** Full six-property classification.

**Statement.** Classify $y(t)=3x(t)+2$ for memory, causality, stability, time invariance, linearity, invertibility.

**Solution.**

- **Memoryless:** yes (uses only $x(t)$).
- **Causal:** yes (no future values).
- **Stable:** yes, $|y|\le 3B_x+2$ whenever $|x|\le B_x$.
- **Time invariant:** yes, $y_1(t-t_0)=3x_1(t-t_0)+2$ matches the output from $x_2(t)=x_1(t-t_0)$.
- **Linear:** **no**. Zero input gives $y=2\ne 0$. This is *affine*, not linear.
- **Invertible:** yes, $x(t)=(y(t)-2)/3$.

---

### Problem 5.2 — Classify $y(t)=tx(t)$
**Reference:** Lecture 5, §5.5.2.
**Topic:** Explicit $t$ coefficient.

**Statement.** Classify $y(t)=tx(t)$.

**Solution.**

- Memoryless yes; causal yes.
- **Stable:** no. Let $x(t)=1$ (bounded); $y(t)=t$ diverges.
- **Time invariant:** **no**. $y_2(t)=tx_1(t-t_0)$, but $y_1(t-t_0)=(t-t_0)x_1(t-t_0)$.
- **Linear:** yes. At each fixed $t$, the system is scalar multiplication.
- **Invertible:** yes for $t\ne 0$: $x(t)=y(t)/t$.

---

### Problem 5.3 — Classify $T_1(x[n])=1/x[n+1]$
**Reference:** Lecture 5, Exercise 1.
**Topic:** DT classification; nonlinearity of $1/\cdot$.

**Statement.** Classify $T_1(x[n])=1/x[n+1]$.

**Solution.**

- **Memoryless:** no (uses $x[n+1]$).
- **Causal:** **no** (uses future).
- **Linear:** **no**. $T_1(ax)=1/(ax[n+1])=(1/a)T_1(x)\ne a T_1(x)$.
- **Time invariant:** yes.
- **Stable:** no. If $x[n+1]\to 0$, output diverges.
- **Invertible:** yes: $x[n]=1/y[n-1]$.

---

### Problem 5.4 — Classify $T_2(x[n])=x[n]+0.5 x[n+1]$
**Reference:** Lecture 5, Exercise 1.
**Topic:** FIR filter with future input.

**Statement.** Classify $T_2(x[n])=x[n]+0.5 x[n+1]$.

**Solution.**

- Memoryless no; **causal no**; linear yes; time invariant yes.
- **Stable:** yes, $|y|\le |x[n]|+0.5|x[n+1]|\le 1.5 B_x$.
- **Invertible:** yes (requires solving a first-order difference equation).

---

### Problem 5.5 — Inverse Systems via Z-Transform Preview
**Reference:** Lecture 5, §5.2.2.
**Topic:** Cascade giving the identity.

**Statement.** Given $H_1(z)=\dfrac{1}{1-\alpha z^{-1}}$ and $H_2(z)=1+\beta z^{-1}$, find $\alpha,\beta$ so that the systems are inverses.

**Solution.**
$$H_1(z)H_2(z) = \frac{1+\beta z^{-1}}{1-\alpha z^{-1}}.$$
Setting $\alpha=-\beta$ gives $H_1 H_2=1$, whose inverse transform is $\delta[n]$. So choose $\alpha=-\beta$.

---

## Lecture 6 — DT LTI Convolution

### Problem 6.1 — Finite-Length Convolution
**Reference:** Lecture 6, §6.5.1.
**Topic:** Convolution sum on finite sequences.

**Statement.** Compute $y[n]=x[n]*h[n]$ where $x[n]=\{1,2,3\}$ for $n=0,1,2$ and $h[n]=\{1,1\}$ for $n=0,1$ (zero elsewhere).

**Solution.**

**Step 1.** Length: $N+M-1=3+2-1=4$ samples, range $n=0,\ldots,3$.

**Step 2.** Apply $y[n]=\sum_k x[k]h[n-k]$.

| $n$ | Contributions | $y[n]$ |
|---|---|---|
| 0 | $x[0]h[0]=1\cdot 1$ | 1 |
| 1 | $x[0]h[1]+x[1]h[0]=1+2$ | 3 |
| 2 | $x[1]h[1]+x[2]h[0]=2+3$ | 5 |
| 3 | $x[2]h[1]=3$ | 3 |

**Result.** $y[n]=\{1,3,5,3\}$ for $n=0,1,2,3$.

**Sanity.** $(\sum x)(\sum h)=6\cdot 2=12 = 1+3+5+3$. $\checkmark$

---

### Problem 6.2 — Polynomial-Multiplication Trick
**Reference:** Lecture 6, alternate view.
**Topic:** Convolution via polynomial multiplication in $z^{-1}$.

**Statement.** Redo Problem 6.1 using polynomials in $z^{-1}$.

**Solution.**
$$X(z)=1+2z^{-1}+3z^{-2},\quad H(z)=1+z^{-1}.$$
$$X(z)H(z) = 1+2z^{-1}+3z^{-2}+z^{-1}+2z^{-2}+3z^{-3} = 1+3z^{-1}+5z^{-2}+3z^{-3}.$$

Reading off coefficients: $y[n]=\{1,3,5,3\}$. $\checkmark$

---

### Problem 6.3 — Geometric with Step
**Reference:** Lecture 6, §6.5.2.
**Topic:** Closed-form DT convolution.

**Statement.** Compute $y[n]=\alpha^n u[n]*u[n]$, $|\alpha|<1$.

**Solution.** For $n\ge 0$,
$$y[n]=\sum_{k=0}^{n}\alpha^k = \frac{1-\alpha^{n+1}}{1-\alpha}.$$
For $n<0$, $y[n]=0$.

**Result.** $y[n]=\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$; asymptotes to $1/(1-\alpha)$.

---

### Problem 6.4 — Accumulator
**Reference:** Lecture 6, §6.5.3.
**Topic:** Convolving with $u[n]$ = running sum.

**Statement.** Express $y[n]=x[n]*u[n]$ as a sum.

**Solution.** Since $u[n-k]=1$ for $k\le n$ and $0$ otherwise,
$$y[n]=\sum_{k=-\infty}^{n} x[k].$$

Convolving with $u[n]$ is an *accumulator*. For $x[n]=\{1,2,3\}$, $y[n]=1,3,6,6,6,\ldots$

---

### Problem 6.5 — Shift via Convolution
**Reference:** Lecture 6, §6.5.4.
**Topic:** Shift-as-convolution property.

**Statement.** Compute $x[n]*\delta[n-n_0]$.

**Solution.**
$$x[n]*\delta[n-n_0]=\sum_k x[k]\delta[n-k-n_0] = x[n-n_0].$$

A shifted impulse is a *delay element*.

---

## Lecture 7 — CT LTI Properties and Convolution

### Problem 7.1 — Rectangle-with-Rectangle Convolution
**Reference:** Lecture 7, §7.6.1.
**Topic:** Piecewise CT convolution.

**Statement.** Let $x(t)=u(t)-u(t-1)$ and $h(t)=u(t)-u(t-2)$. Find $y(t)=x(t)*h(t)$.

**Solution.** Supports $[0,1]$ and $[0,2]$; $h(t-\tau)$ has support $[t-2,t]$. Critical values: $t=0,1,2,3$.

| Region | Limits | Result |
|---|---|---|
| $t<0$ | no overlap | $0$ |
| $0\le t<1$ | $\int_0^t d\tau$ | $t$ |
| $1\le t<2$ | $\int_0^1 d\tau$ | $1$ |
| $2\le t<3$ | $\int_{t-2}^1 d\tau$ | $3-t$ |
| $t\ge 3$ | no overlap | $0$ |

**Result.** Trapezoidal pulse rising on $[0,1]$, flat on $[1,2]$, falling on $[2,3]$.

**Sanity.** Area: $\int y\,dt = \tfrac12(1)+1+\tfrac12(1) = 2 = 1\cdot 2 = \int x\,dt \cdot\int h\,dt$. $\checkmark$

---

### Problem 7.2 — Exponential with Unit Step
**Reference:** Lecture 7, §7.6.2.
**Topic:** Convolution with an integrator ($h=u$).

**Statement.** Let $x(t)=e^{-at}u(t)$, $a>0$, and $h(t)=u(t)$. Find $y(t)$.

**Solution.** For $t<0$, $y=0$. For $t\ge 0$,
$$y(t)=\int_0^t e^{-a\tau}\,d\tau = \frac{1}{a}(1-e^{-at}).$$

**Result.** $y(t)=\dfrac{1}{a}(1-e^{-at})u(t)$.

---

### Problem 7.3 — Classify an Impulse Response
**Reference:** Lecture 7, §7.8.
**Topic:** LTI properties from $h(t)$.

**Statement.** Classify the LTI system with $h(t)=e^{-2t}u(t)$.

**Solution.**

- **Causal:** yes, $h(t)=0$ for $t<0$.
- **Stable:** $\int_0^\infty e^{-2t}\,dt = 1/2 <\infty \Rightarrow$ **stable**.
- **Memoryless:** no, $h$ is not a scaled impulse.
- **Invertible:** yes (corresponds to $\dfrac{dy}{dt}+2y=x$; inverse operation is $x=\dfrac{dy}{dt}+2y$).

---

### Problem 7.4 — Stable but Non-Causal
**Reference:** Lecture 7, §7.8.2 / §7.8.3.
**Topic:** Causality vs. stability independence.

**Statement.** Classify $h(t)=e^{t}u(-t)$ for causality and stability.

**Solution.**

- **Causal:** **no** ($h(t)\ne 0$ for $t<0$).
- **Stable:** $\int_{-\infty}^0 e^{t}\,dt = 1<\infty \Rightarrow$ **stable**.

Confirms that causality and stability are independent properties.

---

### Problem 7.5 — Step Response from Impulse Response
**Reference:** Lecture 7, §7.9.
**Topic:** $s(t)=\int_{-\infty}^t h(\tau)d\tau$.

**Statement.** Given $h(t)=e^{-t}u(t)$, find the step response.

**Solution.** For $t<0$, $s(t)=0$. For $t\ge 0$,
$$s(t) = \int_0^t e^{-\tau}\,d\tau = 1-e^{-t}.$$

**Result.** $s(t)=(1-e^{-t})u(t)$. Check: $ds/dt=e^{-t}u(t)$ recovers $h$. $\checkmark$

---

### Problem 7.6 — Inverse of a Pure Delay
**Reference:** Lecture 7, §7.8.4.
**Topic:** Invertibility.

**Statement.** Let $h(t)=\delta(t-t_0)$ (pure delay). Find the inverse impulse response.

**Solution.** The inverse advances by $t_0$: $h_i(t)=\delta(t+t_0)$. Verify:
$$\delta(t-t_0)*\delta(t+t_0) = \delta(t).$$

---

## Lecture 8 — Difference / Differential Equations and Singularity Functions

### Problem 8.1 — CT Impulse Response via Jump Condition
**Reference:** Lecture 8, Worked Example 1.
**Topic:** Impulse response of first-order ODE.

**Statement.** Find $h(t)$ for $\dfrac{dy}{dt}+2y=x$.

**Solution.**

**Step 1.** For $t>0$, set $x=\delta(t)=0$; solve $h'+2h=0 \Rightarrow h(t)=Ce^{-2t}$.

**Step 2.** Jump condition: integrating the ODE across $t=0$ gives $h(0^+)-h(0^-)=1$. With $h(0^-)=0$ (initial rest), $h(0^+)=1$, so $C=1$.

**Step 3.** Combine with causality:
$$h(t) = e^{-2t}u(t).$$

Stability: $a=2>0$, so the system is stable.

---

### Problem 8.2 — CT Step Response
**Reference:** Lecture 8, Worked Example 2.
**Topic:** Homogeneous + particular method.

**Statement.** Solve $\dfrac{dy}{dt}+2y=3x$ with $x(t)=u(t)$, $y(0^-)=0$.

**Solution.**

**Step 1.** For $t\ge 0$, ODE becomes $\dfrac{dy}{dt}+2y=3$.

**Step 2.** Homogeneous solution: $y_h(t)=Ce^{-2t}$.

**Step 3.** Particular solution: try $y_p=K$. Then $2K=3 \Rightarrow K=3/2$.

**Step 4.** Total: $y(t)=Ce^{-2t}+3/2$ for $t\ge 0$. Apply $y(0)=0$: $C=-3/2$.

**Result.** $y(t)=\tfrac32(1-e^{-2t})u(t)$. Steady state $3/2$; time constant $0.5$ s.

---

### Problem 8.3 — DT Impulse Response by Iteration
**Reference:** Lecture 8, Worked Example 3.
**Topic:** Recursive DT difference equation.

**Statement.** Find $h[n]$ for $y[n]=\tfrac12 y[n-1]+x[n]$ with initial rest.

**Solution.** Set $x[n]=\delta[n]$; iterate from $y[n]=0$ for $n<0$:

| $n$ | $h[n]$ |
|---|---|
| 0 | $\tfrac12\cdot 0 + 1 = 1$ |
| 1 | $\tfrac12\cdot 1 + 0 = 1/2$ |
| 2 | $\tfrac12\cdot 1/2 = 1/4$ |
| 3 | $1/8$ |

**Pattern.** $h[n]=(1/2)^n u[n]$.

Stability: $|\alpha|=1/2<1$, stable.

---

### Problem 8.4 — DT Step Response by Iteration
**Reference:** Lecture 8, Worked Example 4.
**Topic:** Iterating for step response.

**Statement.** Find $s[n]$ for $y[n]=\tfrac12 y[n-1]+x[n]$, $x[n]=u[n]$.

**Solution.** Iterate:

| $n$ | $s[n]$ |
|---|---|
| 0 | $\tfrac12\cdot 0 + 1 = 1$ |
| 1 | $\tfrac12\cdot 1 + 1 = 3/2$ |
| 2 | $\tfrac12\cdot 3/2 + 1 = 7/4$ |
| 3 | $\tfrac12\cdot 7/4 + 1 = 15/8$ |

**Pattern.** $s[n]=2(1-(1/2)^{n+1})u[n]$. Steady state $=2$.

Matches closed form $s[n]=\dfrac{1-\alpha^{n+1}}{1-\alpha}u[n]$ with $\alpha=1/2$. $\checkmark$

---

### Problem 8.5 — Stability Classification
**Reference:** Lecture 8, §8.4.
**Topic:** Stability from first-order coefficients.

**Statement.** Classify the stability of each system.

(a) $\dfrac{dy}{dt}+3y=x$.
(b) $\dfrac{dy}{dt}-2y=x$.
(c) $y[n]=0.5\,y[n-1]+x[n]$.
(d) $y[n]=2\,y[n-1]+x[n]$.

**Solution.**

(a) $a=3>0 \Rightarrow$ **stable**.
(b) $a=-2<0 \Rightarrow$ **unstable** (grows as $e^{2t}$).
(c) $|\alpha|=0.5<1 \Rightarrow$ **stable**.
(d) $|\alpha|=2>1 \Rightarrow$ **unstable**.

---

### Problem 8.6 — Derivative of a Ramp-Like Signal
**Reference:** Lecture 8, Worked Example 5.
**Topic:** Derivative involving $\delta(t)$ and the product rule.

**Statement.** Compute $\dfrac{d}{dt}[(t+1)u(t)]$.

**Solution.** Product rule:
$$\frac{d}{dt}[(t+1)u(t)] = 1\cdot u(t) + (t+1)\cdot\delta(t).$$

Use $x(t)\delta(t)=x(0)\delta(t)$ with $x(0)=1$: $(t+1)\delta(t)=\delta(t)$.

**Result.** $u(t)+\delta(t)$.

**Interpretation.** The step captures the constant slope of the ramp for $t\ge 0$; the impulse captures the jump of height 1 at $t=0$.

---

### Problem 8.7 — Impulse Scaling
**Reference:** Lecture 8, §8.6.1.
**Topic:** $\delta(at)=\delta(t)/|a|$.

**Statement.** Simplify $\delta(2t)$.

**Solution.** By the scaling rule,
$$\delta(2t) = \tfrac12\,\delta(t).$$

Compressing by factor 2 halves the "area per unit of original $t$," so we multiply by $1/|a|$ to preserve unit area.

---

### Problem 8.8 — Doublet Convolution
**Reference:** Lecture 8, §8.5.4.
**Topic:** Derivative via $\delta'$.

**Statement.** Given $x(t)=e^{-t}u(t)$, compute $x(t)*\delta'(t)$.

**Solution.** Convolution with $\delta'$ differentiates:
$$x(t)*\delta'(t) = \frac{dx}{dt} = -e^{-t}u(t)+e^{-t}\delta(t) = -e^{-t}u(t)+\delta(t),$$
using $e^{-t}\delta(t)=\delta(t)$ (smooth factor evaluated at $t=0$).

---

*Prepared for CEC 315 Exam 1 — Spring 2026.*
