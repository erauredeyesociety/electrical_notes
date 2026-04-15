# Lecture 5 — Basic System Properties

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Jianhua Liu
**Source PDF:** `all_lectures/cec315-lctr05-basic-sys-properties.pdf`
**Exam coverage:** Exam 1

---

**Lctr 5: Basic System Properties**

Jianhua Liu

Spring 2026

**Focus:** Section 1.6 (Pages 44 to 55)

---

## 5.1 Memory vs. Memoryless Systems

> **Why This Matters**
>
> Every system you will encounter in this course — and in your engineering career — can be classified by a small set of "basic properties": memory, invertibility, causality, stability, time invariance, and linearity. These properties aren't just vocabulary; they determine which mathematical tools you can use to analyze the system. Only **linear time-invariant (LTI)** systems can be analyzed with convolution, Fourier, Laplace, and $z$-transforms. So the first step in analyzing any system is to check these properties.

### 5.1.1 Memoryless Systems

> **Definition — Memoryless System**
>
> A system is **memoryless** if the output at any time depends **only on the input at that same time**.
>
> Mathematically: $y(t)$ depends only on $x(t)$ (CT), or $y[n]$ depends only on $x[n]$ (DT).

**Example:** The **ReLU** (Rectified Linear Unit) activator used in neural networks:

$$y[n] = \begin{cases} x[n], & x[n] \geq 0 \\ 0, & \text{otherwise}\end{cases}$$

For any given $n$, the output $y[n]$ is computed purely from $x[n]$ — no past or future samples are involved. ReLU is memoryless.

**Other memoryless examples:**

- $y(t) = 5 x(t)$ (pure scaling)
- $y(t) = x^2(t)$ (squaring)
- $y[n] = \cos(x[n])$

### 5.1.2 Systems With Memory

> **Definition — System With Memory**
>
> A system has **memory** if the output depends on past or future values of the input (or on past values of the output itself).

**Examples:**

- **Recursive (IIR) system:** $y_1[n] = x[n] + \alpha\,y_1[n-1]$
  The current output depends on the previous output $y_1[n-1]$ in addition to the current input.

- **Moving-average / FIR system:** $y_2[n] = x[n] - \beta\,x[n-1]$
  The current output depends on the previous input $x[n-1]$ in addition to the current input.

- **Capacitor voltage:** $v_C(t) = \frac{1}{C}\int_{-\infty}^{t} i(\tau)\,d\tau$
  The voltage at time $t$ remembers all past current.

> **Key Insight**
>
> Any system that contains an integrator, a delay element, a difference, or a recursion has memory. Memoryless systems are algebraic (or at most, instantaneous functions of the current sample).

## 5.2 Invertibility and Inverse Systems

### 5.2.1 Definitions of Inverse Systems

> **Definition — Invertible System**
>
> Two equivalent definitions:
>
> 1. A system is **invertible** if distinct inputs lead to distinct outputs (the input-output map is one-to-one).
> 2. A system $T_1(\cdot)$ is invertible if there exists another system $T_2(\cdot)$ such that the impulse response of the cascade $T_2\!\circ\!T_1$ equals the unit impulse. In this case, $T_1$ and $T_2$ are inverse systems of each other.

*[Figure: Block diagram — $x[n] \to T_1 \to w[n] \to T_2 \to x[n]$. The overall cascade is the identity system; its impulse response is $\delta[n]$.]*

**Remark.** In many real applications we cannot find an exact inverse, but we can find a system such that the cascade is an **all-pass filter** (magnitude response equal to 1 for all frequencies). This technique underlies **minimum-phase filter** design and is explored in CEC 410.

### 5.2.2 Finding an Inverse System (Preview via $z$-Transform)

Consider the two DT systems introduced above:

$$\text{System 1: } y_1[n] = x[n] + \alpha\,y_1[n-1]$$
$$\text{System 2: } y_2[n] = x[n] - \beta\,x[n-1]$$

Using the $z$-transform (to be formally introduced later in the course), their system functions are:

$$H_1(z) = \frac{1}{1 - \alpha z^{-1}}, \qquad H_2(z) = 1 + \beta z^{-1}.$$

Setting $\alpha = -\beta$ gives:

$$H_1(z)\,H_2(z) = \frac{1}{1 + \beta z^{-1}}\,(1 + \beta z^{-1}) = 1.$$

Since the $z$-transform of $\delta[n]$ is $1$, the two systems are indeed inverses of each other. This preview illustrates *why* transform-domain analysis is powerful: inversion becomes algebraic.

## 5.3 Causality

### 5.3.1 Definition of a Causal System

> **Definition — Causal System**
>
> Two equivalent definitions:
>
> 1. A system is **causal** if the output at any time depends only on **present and past** values of the input.
> 2. A system is **causal** if the output at any time does **not depend on future input**.

### 5.3.2 Quick Test via the Impulse Response

For an LTI system, there is an easy test:

$$\boxed{\,\text{LTI system is causal} \iff h[n] = 0 \text{ for } n < 0 \text{ (or } h(t) = 0 \text{ for } t < 0\text{)}\,}$$

**Why?** The impulse response is the system's output when the input is $\delta[n]$. The impulse "happens" at $n=0$; it has no energy at $n<0$. A causal system cannot produce a nonzero response before the stimulus arrives.

### 5.3.3 Examples of Causal / Non-Causal Systems

| System | Causal? | Reasoning |
|---|---|---|
| $y_1[n] = x[n] + \alpha y_1[n-1]$ | **Yes** | Depends on present input and past output only. |
| $y_2[n] = x[n] - \beta x[n-1]$ | **Yes** | Depends on present and past input only. |
| $y_3[n] = x[n] - \beta x[n+1]$ | **No** | Depends on future input $x[n+1]$. |
| ReLU $y[n] = \max(x[n],0)$ | **Yes** | Only depends on current input. |

> **Key Insight**
>
> All **real-time** physical systems are causal (time flows forward). Non-causal systems arise naturally in *offline* processing: audio editing, image processing, batch-mode speech recognition, etc. Any system that "peeks" at future samples is non-causal.

## 5.4 Stability

### 5.4.1 Definition of a Stable System

Informally, a stable system is one where **small inputs do not lead to diverging responses**.

> **Definition — BIBO Stability (Bounded-Input, Bounded-Output)**
>
> A system is **BIBO stable** if every bounded input produces a bounded output:
>
> $$|x(t)| \leq B_x < \infty \;\;\Longrightarrow\;\; |y(t)| \leq B_y < \infty$$
>
> for some constants $B_x, B_y$.

### 5.4.2 Examples of Stable / Unstable Systems

- **Pendulum** (hanging down): stable — small pushes produce bounded swings.
- **Inverted pendulum** (balanced on its tip): unstable — any perturbation grows without bound.
- $y[n] = 0.5\,y[n-1] + x[n]$: stable (pole inside unit circle, as we will see later).
- $y[n] = 2\,y[n-1] + x[n]$: unstable (pole outside unit circle).
- Integrator $y(t) = \int_{-\infty}^t x(\tau)\,d\tau$: **not** BIBO stable. Feeding in the bounded input $x(t) = u(t)$ (the unit step) gives $y(t) = t\,u(t)$, which is unbounded.

> **Key Insight**
>
> Stability is the single most important property for control and filter design. An unstable system is useless in practice — it will saturate, oscillate, or destroy hardware. We will later derive stability conditions in terms of poles (Laplace: LHP; $z$-transform: inside unit circle) and in terms of $h(t)$ or $h[n]$ (absolutely integrable / summable).

## 5.5 Time Invariance

### 5.5.1 Definition of Time Invariance

> **Definition — Time-Invariant System**
>
> A system is **time-invariant** if its behavior and characteristics do **not change over time**. Equivalently, a **time shift in the input** produces an **identical time shift in the output**.
>
> Formally: if $x(t) \to y(t)$, then $x(t - t_0) \to y(t - t_0)$ for every $t_0$.

### 5.5.2 Verifying Time Invariance

**Procedure:**

1. Let $y_1(t)$ be the output when the input is $x_1(t)$.
2. Shift the input: $x_2(t) = x_1(t - t_0)$. Compute $y_2(t)$ directly from the system equation.
3. Compute $y_1(t - t_0)$ — that is, shift the *output* of step 1 by $t_0$.
4. If $y_2(t) = y_1(t - t_0)$ for every $t_0$ and every input, the system is time invariant.

**Example (time invariant):** $y(t) = 3\,x(t) + 2$.
Then $y_2(t) = 3\,x_1(t-t_0) + 2$ and $y_1(t-t_0) = 3\,x_1(t-t_0) + 2$. These match: time invariant.

**Example (time varying):** $y(t) = t\,x(t)$.
Then $y_2(t) = t\,x_1(t-t_0)$ but $y_1(t-t_0) = (t-t_0)\,x_1(t-t_0)$. These don't match unless $t_0 = 0$: **time varying**. The explicit $t$ multiplier is a red flag.

> **Warning**
>
> Any system equation that contains an **explicit** dependence on $t$ or $n$ (outside of the input/output signals) is typically time varying. Watch for things like $t x(t)$, $x(2t)$ (time scaling), or coefficients that themselves depend on time.

## 5.6 Linearity

### 5.6.1 Definition of Linearity

> **Definition — Linear System**
>
> A system is **linear** if it possesses the **superposition** property. Superposition = additivity + homogeneity.

### 5.6.2 Additivity

If $x_1(t) \to y_1(t)$ and $x_2(t) \to y_2(t)$, then:

$$x_1(t) + x_2(t) \;\longrightarrow\; y_1(t) + y_2(t).$$

### 5.6.3 Scaling (Homogeneity)

If $x_1(t) \to y_1(t)$, then for every constant $a$ (real or complex):

$$a\,x_1(t) \;\longrightarrow\; a\,y_1(t).$$

### 5.6.4 Combined Superposition Statement

$$\boxed{\;a\,x_1(t) + b\,x_2(t) \;\longrightarrow\; a\,y_1(t) + b\,y_2(t)\;}$$

### 5.6.5 Zero-In / Zero-Out Test (Necessary Condition)

> **Key Insight**
>
> For a linear system, a **zero input must produce a zero output**. Setting $a = 0$ in homogeneity gives $0 \to 0$. So if you can find any input that's zero but produces a nonzero output (e.g., a constant offset), the system is nonlinear.

**Example (nonlinear):** $y(t) = 3\,x(t) + 2$. Zero input gives $y(t) = 2 \neq 0$. **Nonlinear** (it's *affine*, not linear). Though earlier we found it to be time invariant, linearity fails.

**Example (linear):** $y(t) = 5\,x(t)$. Obviously linear.

**Example (nonlinear):** $y(t) = x^2(t)$. Response to $x_1+x_2$ is $(x_1+x_2)^2 = x_1^2 + 2 x_1 x_2 + x_2^2$, not $x_1^2 + x_2^2$. Fails additivity.

### 5.6.6 ASR (Speech Recognition) Case Study

Using **Automatic Speech Recognition (ASR)** as an end-to-end example of how these properties apply to different components of a real system:

- **Memory**
  - Mel-frequency vector calculation: **memoryless** (each frame independent).
  - Phoneme estimation: has memory (context windows, recurrent models).
- **Causality**
  - A **streaming** ASR system is causal (must respond in real time).
  - A **batch-processing** ASR system is non-causal (can look ahead).
- **Stability**
  - The overall system is stable (bounded audio produces bounded labels).
- **Linearity**
  - The entire system is **nonlinear** (classification is an inherently nonlinear operation).
  - Individual components can be linear — for example, the **FFT** inside the mel-frequency extraction is a linear operator.

## 5.7 Exercises

### 5.7.1 Exercise 1: System Classification

Consider:

$$T_1(x[n]) = \frac{1}{x[n+1]}, \qquad T_2(x[n]) = x[n] + 0.5\,x[n+1].$$

Determine whether each system is: invertible, causal, BIBO stable, time invariant, linear, and memoryless.

**Analysis of $T_1$:**

- **Memoryless?** No — uses $x[n+1]$.
- **Causal?** No — depends on future input $x[n+1]$.
- **Linear?** No — $T_1(a\,x) = 1/(a\,x[n+1]) = (1/a)\,T_1(x) \neq a\,T_1(x)$. Fails homogeneity.
- **Time invariant?** Yes — shifting the input shifts the output identically.
- **BIBO stable?** No — if $x[n+1] \to 0$ (bounded input going through zero), output diverges.
- **Invertible?** Yes — from $y[n] = 1/x[n+1]$ we recover $x[n+1] = 1/y[n]$, so $x[n] = 1/y[n-1]$.

**Analysis of $T_2$:**

- **Memoryless?** No — uses $x[n+1]$.
- **Causal?** No — depends on $x[n+1]$.
- **Linear?** Yes — sum and scale carry through directly.
- **Time invariant?** Yes.
- **BIBO stable?** Yes — $|y[n]| \leq |x[n]| + 0.5|x[n+1]| \leq 1.5\,B_x$.
- **Invertible?** Yes (it has an inverse, though it requires solving a first-order difference equation).

### 5.7.2 Exercise 2: Signal Sketching (Preparation for Convolution)

Sketch the following DT signals:

- $x_1[n] = (0.5)^n\,u[n]$ — a decaying geometric sequence starting at $n=0$ with value $1$ and halving each step.
- $x_2[n] = x_1[n-2]$ — the same shape, shifted right by 2 (starts at $n=2$).
- $x_3[n] = x_2[-n]$ — time reversal of $x_2$, giving a sequence that *ends* at $n = -2$ with the same decaying shape mirrored.

*[Figure: Three DT stem plots. (a) $x_1[n]$: stems at $n=0,1,2,\ldots$ of heights $1, 0.5, 0.25, 0.125, \ldots$; (b) $x_2[n]$: same heights starting at $n=2$; (c) $x_3[n]$: same heights at $n=-2, -3, -4, \ldots$ (mirrored into negative time).]*

## 5.8 Summary

Key takeaways from this lecture:

1. **Memory:** Output depends only on the current input ($\Rightarrow$ memoryless) vs. past/future input or past output ($\Rightarrow$ memory).
2. **Invertibility:** One-to-one map from inputs to outputs; cascade with inverse gives identity $\delta[n]$.
3. **Causality:** Output depends only on present and past input. For LTI, equivalent to $h[n] = 0$ for $n<0$.
4. **Stability (BIBO):** Bounded input produces bounded output. Unstable systems are unusable in practice.
5. **Time invariance:** Shifting the input by $t_0$ shifts the output by exactly $t_0$; equivalently, no explicit $t$ coefficients.
6. **Linearity:** Superposition — additivity and scaling. Zero input must give zero output.

The next three lectures will focus on **LTI systems** (linear **and** time-invariant) because this is the class for which convolution applies and all the transform machinery of this course is valid.

## 5.9 Common Mistakes to Avoid

1. **Calling affine systems linear.** $y = mx + b$ is *affine*, not linear. Always apply the zero-in / zero-out test.
2. **Conflating causality and stability.** They are independent: a system can be causal but unstable, or stable but non-causal.
3. **Forgetting to check both additivity AND homogeneity** when testing linearity. Some systems satisfy one but not the other.
4. **Assuming time invariance from smooth coefficients.** The telltale sign of time variance is an explicit $t$ or $n$ outside the signal arguments (e.g., $y(t) = t\,x(t)$).
5. **Confusing "has memory" with "uses $x[n-1]$".** Both recursive ($y[n-1]$) and delay-line ($x[n-1]$) structures have memory; so do systems with future dependence ($x[n+1]$, though that also makes them non-causal).

Jianhua Liu

---

## Practice Problems Summary

1. **Memoryless check:** ReLU $y[n] = \max(x[n],0)$ is memoryless; $y_1[n] = x[n] + \alpha y_1[n-1]$ has memory.
2. **Inverse system:** For $H_1(z) = 1/(1-\alpha z^{-1})$ and $H_2(z) = 1 + \beta z^{-1}$, choosing $\alpha = -\beta$ gives $H_1 H_2 = 1$, confirming they are inverses.
3. **Causality check:** $y_3[n] = x[n] - \beta x[n+1]$ is non-causal (uses future input); all other earlier examples are causal.
4. **Stability intuition:** Pendulum stable; inverted pendulum unstable. Integrator fed by $u(t)$ gives $t\,u(t)$, proving it is not BIBO stable.
5. **Time invariance check:** $y(t) = t\,x(t)$ is time varying due to the explicit $t$ coefficient.
6. **Linearity check:** $y(t) = 3 x(t) + 2$ is nonlinear (nonzero output for zero input).
7. **Exercise 1:** $T_1(x[n]) = 1/x[n+1]$ is non-causal, nonlinear, time invariant, not BIBO stable, invertible. $T_2(x[n]) = x[n] + 0.5 x[n+1]$ is non-causal, linear, time invariant, BIBO stable, invertible.
8. **Exercise 2:** Sketch $x_1[n] = 0.5^n u[n]$ and its shifts/reflections — preparation for visualizing convolution in the next lecture.
