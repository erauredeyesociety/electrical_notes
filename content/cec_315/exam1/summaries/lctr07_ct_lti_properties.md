# Lecture 7 — Continuous-Time LTI Systems and Properties

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr07-ct-lti-properties.pdf`
**Exam coverage:** Exam 1

---

**Lctr 7: Continuous-Time LTI Systems and Properties**

Rogelio Gracia Otalvaro

Spring 2026

**Focus:** Sections 2.2 and 2.3 (Pages 97 to 115)

---

## 7.1 From Discrete-Time to Continuous-Time: The Big Picture

> **Why This Matters**
>
> In Lecture 6, we learned that for discrete-time LTI systems, the output is the **convolution sum**. Now we extend these ideas to **continuous-time** systems. The math changes from sums to integrals, but the intuition remains the same: **if you know how a system responds to an impulse, you can predict its response to any input!**

**Quick comparison:**

| Concept | Discrete-Time (DT) | Continuous-Time (CT) |
|---|---|---|
| Signal decomposition | $\displaystyle \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]$ | $\displaystyle \int_{-\infty}^{\infty} x(\tau)\,\delta(t-\tau)\,d\tau$ |
| Convolution | $\displaystyle \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$ | $\displaystyle \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$ |
| Impulse function | $\delta[n]$ (unit sample) | $\delta(t)$ (Dirac delta) |

> **Key Insight**
>
> Sums become integrals, and the index $k$ becomes the continuous variable $\tau$. The concepts are the same — only the notation changes!

## 7.2 The Continuous-Time Unit Impulse (Dirac Delta)

Before we can do convolution, we need to understand the continuous-time impulse function $\delta(t)$.

### 7.2.1 What is $\delta(t)$?

The **Dirac delta function** $\delta(t)$ is **not** a regular function — it is a mathematical idealization. Think of it as:

- An infinitely tall, infinitely narrow spike at $t=0$
- With area under the spike equal to exactly 1

Formally:

$$\delta(t) = 0 \text{ for } t \neq 0, \qquad \int_{-\infty}^{\infty} \delta(t)\,dt = 1$$

**Intuition:** imagine a rectangular pulse that gets narrower and taller while keeping its area equal to 1. The Dirac delta is the "limit" of this process.

*[Figure: A sequence of narrow pulses of widths $\Delta, \Delta/2, \Delta/4, \ldots$ and corresponding heights $1/\Delta, 2/\Delta, 4/\Delta, \ldots$ — each has unit area. As $\Delta \to 0$, the limit is $\delta(t)$.]*

### 7.2.2 The Sifting Property (Most Important!)

The sifting property is the key to understanding convolution:

$$\boxed{\;\int_{-\infty}^{\infty} x(\tau)\,\delta(\tau - t_0)\,d\tau = x(t_0)\;}$$

**What this means:** the integral "sifts out" (extracts) the value of $x(\tau)$ at the point $\tau = t_0$.

*[Figure 2.14: (a) an arbitrary signal $x(\tau)$; (b) the shifted impulse $\delta(t-\tau)$ as a function of $\tau$, showing a spike at $\tau = t$; (c) the product $x(\tau)\,\delta(t-\tau) = x(t)\,\delta(t-\tau)$, which is a single impulse of area $x(t)$.]*

> **Key Insight — How to Use the Sifting Property**
>
> 1. Find where the delta function is "active" (where its argument equals zero).
> 2. Evaluate the other function at that point.
> 3. That's your answer!

**Example 1:** Evaluate $\displaystyle\int_{-\infty}^{\infty} (t^2 + 3t)\,\delta(t-2)\,dt$.

**Solution.**

- The delta is at $t=2$ (set $t-2=0$).
- Evaluate $(t^2+3t)$ at $t=2$: $(2)^2 + 3(2) = 4 + 6 = 10$.
- **Answer:** $\boxed{10}$

**Example 2:** Evaluate $\displaystyle\int_{-\infty}^{\infty} e^{-3t}\,\delta(t+1)\,dt$.

**Solution.**

- The delta is at $t = -1$ (set $t+1=0$).
- Evaluate $e^{-3t}$ at $t=-1$: $e^{-3(-1)} = e^{3}$.
- **Answer:** $\boxed{e^{3}}$

> **Common Mistake — Watch the Limits!**
>
> If the delta function is **outside** the integration limits, the integral equals zero!
>
> Example: $\displaystyle\int_0^5 x(t)\,\delta(t+2)\,dt = 0$ because the delta is at $t=-2$, which is outside $[0,5]$.

## 7.3 Representing CT Signals Using Impulses

Just like in discrete-time, any continuous-time signal can be written as a "sum" (integral) of shifted, scaled impulses:

$$\boxed{\;x(t) = \int_{-\infty}^{\infty} x(\tau)\,\delta(t - \tau)\,d\tau\;}$$

**Interpretation:**

- We decompose $x(t)$ into infinitely many infinitesimally small impulses.
- Each impulse at time $\tau$ has "weight" $x(\tau)\,d\tau$.
- The integral adds up all these weighted impulses.

This representation is the foundation for deriving the convolution integral.

*[Figure 2.12: Staircase approximation to a continuous-time signal. The signal is approximated by a sum of narrow rectangular pulses of width $\Delta$ and heights $x(k\Delta)$. As $\Delta \to 0$, the sum becomes an integral and the pulses become impulses.]*

## 7.4 The Continuous-Time Impulse Response

### 7.4.1 Definition

> **Definition — Impulse Response**
>
> The **impulse response** $h(t)$ is the output of an LTI system when the input is the unit impulse $\delta(t)$:
>
> $$h(t) = T\{\delta(t)\}$$

**Due to time invariance:**

- If input is $\delta(t)$, output is $h(t)$.
- If input is $\delta(t - \tau)$ (impulse shifted to time $\tau$), output is $h(t - \tau)$.

> **Key Insight**
>
> The impulse response **completely characterizes** an LTI system. Once you know $h(t)$, you can find the output for **any** input!

## 7.5 The Convolution Integral

### 7.5.1 Derivation (Step by Step)

This derivation follows the exact same logic as the discrete-time case.

**Step 1: Decompose the input.**

$$x(t) = \int_{-\infty}^{\infty} x(\tau)\,\delta(t - \tau)\,d\tau$$

**Step 2: Apply the system.**

$$y(t) = T\{x(t)\} = T\!\left\{\int_{-\infty}^{\infty} x(\tau)\,\delta(t - \tau)\,d\tau\right\}$$

**Step 3: Use LINEARITY** (move $T$ inside the integral):

$$y(t) = \int_{-\infty}^{\infty} x(\tau)\,T\{\delta(t - \tau)\}\,d\tau$$

**Step 4: Use TIME-INVARIANCE:**

$$T\{\delta(t - \tau)\} = h(t - \tau)$$

**Step 5: The convolution integral.**

$$\boxed{\;y(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t - \tau)\,d\tau = x(t)*h(t)\;}$$

### 7.5.2 The Flip-and-Shift Interpretation

To compute $y(t)$ for a specific value of $t$:

1. **Flip:** take $h(\tau)$ and flip it about $\tau = 0$ to get $h(-\tau)$.
2. **Shift:** shift by $t$ to get $h(t - \tau)$.
3. **Multiply:** multiply $x(\tau)$ by $h(t - \tau)$.
4. **Integrate:** integrate the product over all $\tau$.

> **Common Mistake**
>
> Just like in discrete-time, you must **flip before shifting**! The argument $h(t - \tau)$ means: flip $h$, then shift it by $t$. Forgetting the flip is the most common mistake!

### 7.5.3 Alternative Form (Commutativity)

By a change of variables, we can also write:

$$y(t) = \int_{-\infty}^{\infty} x(t - \tau)\,h(\tau)\,d\tau$$

This shows convolution is **commutative**: $x(t)*h(t) = h(t)*x(t)$.

> **Key Insight — Practical Tip**
>
> You can flip either $x$ or $h$ — choose whichever is simpler! Flip the signal with a simpler shape or smaller support.

### 7.5.4 How to Find the Cases and Integration Limits

This is one of the most challenging parts of CT convolution. Here's a systematic approach:

> **Key Insight — The Golden Rule**
>
> The integration limits are determined by the **overlap** between $x(\tau)$ and $h(t-\tau)$. You only integrate where **both** functions are nonzero!

**Step-by-Step Procedure.**

**Step 1: Identify the "support" of each signal.** The support is the range of values where the signal is nonzero.

- For $x(\tau)$: find where $x(\tau) \neq 0$. Call this range $[a,b]$.
- For $h(t-\tau)$: start with where $h(\tau) \neq 0$, say $[c,d]$. After flipping and shifting, $h(t-\tau) \neq 0$ for $t-d \leq \tau \leq t-c$.

**Step 2: Find the overlap region.** The integrand $x(\tau)\cdot h(t-\tau)$ is nonzero only where both signals are nonzero:

$$\text{Overlap} = [a,b]\cap[t-d,\,t-c]$$

Lower limit $= \max(a, t-d)$; upper limit $= \min(b, t-c)$.

**Step 3: Find the critical values of $t$.** The "cases" change when the overlap relationship changes. This happens at the four $t$-values where the edges align:

- Left edge of $h(t-\tau)$ reaches left edge of $x(\tau)$: $t-d = a \Rightarrow t = a+d$.
- Left edge of $h(t-\tau)$ reaches right edge of $x(\tau)$: $t-d = b \Rightarrow t = b+d$.
- Right edge of $h(t-\tau)$ reaches left edge of $x(\tau)$: $t-c = a \Rightarrow t = a+c$.
- Right edge of $h(t-\tau)$ reaches right edge of $x(\tau)$: $t-c = b \Rightarrow t = b+c$.

Sort these critical values to find the boundaries between cases.

**Step 4: For each case, determine the limits.** For each range of $t$ between critical points:

- Lower limit of integral $=\max(\text{left edge of } x,\text{left edge of } h(t-\tau))$.
- Upper limit of integral $=\min(\text{right edge of } x,\text{right edge of } h(t-\tau))$.

> **Common Mistake**
>
> Students often set limits incorrectly. Remember:
>
> - If $x(\tau)$ is nonzero on $[a,b]$, these are **fixed** limits (don't depend on $t$).
> - If $h(t-\tau)$ is nonzero on $[t-d,t-c]$, these limits **move with $t$**.

### 7.5.5 Detailed Example: Finding the Cases

Let $x(\tau) = u(\tau) - u(\tau - 1)$ (a pulse from 0 to 1) and $h(\tau) = u(\tau) - u(\tau - 2)$ (a pulse from 0 to 2).

**Step 1 — Identify supports.**

- $x(\tau) \neq 0$ for $0 \leq \tau \leq 1$, so $a=0$, $b=1$.
- $h(\tau) \neq 0$ for $0 \leq \tau \leq 2$, so $c=0$, $d=2$.
- After flip-and-shift: $h(t-\tau) \neq 0$ for $t-2 \leq \tau \leq t$.

**Step 2 — Critical values of $t$.**

- Right edge of $h(t-\tau)$ reaches left edge of $x$: $t-0 = 0 \Rightarrow t=0$.
- Right edge of $h(t-\tau)$ reaches right edge of $x$: $t-0 = 1 \Rightarrow t=1$.
- Left edge of $h(t-\tau)$ reaches left edge of $x$: $t-2 = 0 \Rightarrow t=2$.
- Left edge of $h(t-\tau)$ reaches right edge of $x$: $t-2 = 1 \Rightarrow t=3$.

Critical values in order: $t = 0,\,1,\,2,\,3$.

**Step 3 — Analyze each region.**

| Case | Range of $t$ | Overlap? | Integration Limits |
|---|---|---|---|
| 1 | $t < 0$ | No ($h$ is to the left of $x$) | None, $y(t) = 0$ |
| 2 | $0 \leq t < 1$ | Partial ($h$ entering) | $\int_0^t$ |
| 3 | $1 \leq t < 2$ | Full overlap with $x$ | $\int_0^1$ |
| 4 | $2 \leq t < 3$ | Partial ($h$ exiting) | $\int_{t-2}^1$ |
| 5 | $t \geq 3$ | No ($h$ is to the right of $x$) | None, $y(t) = 0$ |

*[Figure: Five graphical snapshots of $x(\tau)$ (fixed, blue) and $h(t-\tau)$ (moving right, red-dashed), with the green overlap region shaded. Shows Cases 1–5 at representative $t$ values.]*

> **Key Insight — Continuity Check**
>
> At the boundary between cases, the limits should give the same value. For example, at $t=1$:
>
> - From Case 2: $\int_0^1 = 1$
> - From Case 3: $\int_0^1 = 1$ $\checkmark$
>
> This continuity check helps verify your cases are correct!

## 7.6 Worked Examples: Computing the Convolution Integral

### 7.6.1 Example: Two Rectangular Pulses

**Problem:** Let $x(t) = u(t) - u(t-1)$ and $h(t) = u(t) - u(t-2)$. Find $y(t) = x(t)*h(t)$.

**Step 1 — Sketch the signals.** $x(t)$ is a pulse of height 1 from $t=0$ to $t=1$; $h(t)$ is a pulse of height 1 from $t=0$ to $t=2$.

**Step 2 — Flip and shift $h$.**

- $h(-\tau)$: pulse from $\tau = -2$ to $\tau = 0$.
- $h(t-\tau)$: pulse from $\tau = t-2$ to $\tau = t$.

**Step 3 — Find regions of overlap.** We computed the cases above. Now evaluate the integrals.

**Case 1:** $t < 0$ (no overlap): $y(t) = 0$.

**Case 2:** $0 \leq t < 1$ (partial, $h$ entering):

$$y(t) = \int_0^t 1\cdot 1\,d\tau = t$$

**Case 3:** $1 \leq t < 2$ (full overlap with $x$):

$$y(t) = \int_0^1 1\cdot 1\,d\tau = 1$$

**Case 4:** $2 \leq t < 3$ (partial, $h$ exiting):

$$y(t) = \int_{t-2}^1 1\cdot 1\,d\tau = 1 - (t-2) = 3-t$$

**Case 5:** $t \geq 3$ (no overlap): $y(t) = 0$.

**Final answer:**

$$y(t) = \begin{cases} 0, & t < 0 \\ t, & 0 \leq t < 1 \\ 1, & 1 \leq t < 2 \\ 3-t, & 2 \leq t < 3 \\ 0, & t \geq 3 \end{cases}$$

> **Key Insight — Sanity Check**
>
> The result is a **trapezoidal pulse**. This makes sense because convolving two rectangular pulses always produces a trapezoidal (or triangular, when widths are equal) shape!

### 7.6.2 Example: Exponential With Unit Step

**Problem:** Let $x(t) = e^{-at}\,u(t)$ and $h(t) = u(t)$, where $a > 0$. Find $y(t) = x(t)*h(t)$.

**Solution.** For $t<0$ there is no overlap, so $y(t) = 0$. For $t \geq 0$:

$$y(t) = \int_0^t e^{-a\tau}\cdot 1\,d\tau = \int_0^t e^{-a\tau}\,d\tau$$

$$y(t) = \left[-\frac{1}{a}\,e^{-a\tau}\right]_0^t = -\frac{1}{a}\,e^{-at} - \left(-\frac{1}{a}\,e^0\right) = \frac{1}{a}\left(1 - e^{-at}\right)$$

**Final answer:**

$$\boxed{\;y(t) = \frac{1}{a}\left(1 - e^{-at}\right)u(t)\;}$$

**Physical interpretation:** If $h(t) = u(t)$ represents an integrator and $x(t)$ is a decaying exponential starting at $t=0$, then $y(t)$ is the running integral of that exponential. At $t=0$ the integral is 0; as $t\to\infty$ it asymptotes to $1/a$.

## 7.7 Properties of LTI Systems

> **Why This Matters**
>
> These properties are not just abstract math — they have practical implications! They tell us how to:
>
> - Simplify calculations (commutativity)
> - Analyze **series** connections of systems (associativity)
> - Analyze **parallel** connections of systems (distributivity)

### 7.7.1 Commutativity

$$\boxed{\;x(t)*h(t) = h(t)*x(t)\;}$$

**Meaning:** you can interchange the roles of input and impulse response. Flip whichever signal is simpler!

### 7.7.2 Distributivity

$$\boxed{\;x(t)*[h_1(t) + h_2(t)] = x(t)*h_1(t) + x(t)*h_2(t)\;}$$

**Application:** for **parallel** systems, the equivalent impulse response is:

$$h_{\text{eq}}(t) = h_1(t) + h_2(t)$$

### 7.7.3 Associativity

$$\boxed{\;x(t)*[h_1(t)*h_2(t)] = [x(t)*h_1(t)]*h_2(t)\;}$$

**Application:** for **cascade (series)** systems, the equivalent impulse response is:

$$h_{\text{eq}}(t) = h_1(t)*h_2(t)$$

> **Key Insight**
>
> **Cascade systems are interchangeable!** Due to commutativity and associativity, the order of LTI systems in a cascade doesn't affect the overall input-output relationship.

### 7.7.4 Convolution With the Impulse

$$x(t)*\delta(t) = x(t)$$

The impulse is the **identity element** for convolution (like 1 for multiplication).

### 7.7.5 Convolution With a Shifted Impulse (Time Delay)

$$x(t)*\delta(t - t_0) = x(t - t_0)$$

Convolving with a shifted impulse **delays** the signal by $t_0$.

## 7.8 LTI System Properties From the Impulse Response

> **Why This Matters**
>
> One of the most powerful aspects of LTI systems: you can determine important properties just by looking at $h(t)$!

### 7.8.1 Memory

**Memoryless:** the output depends only on the current input value. An LTI system is memoryless if and only if:

$$h(t) = K\,\delta(t)\quad\text{for some constant } K$$

In this case $y(t) = K\cdot x(t)$ (just scaling).

**Has memory:** if $h(t)$ is anything other than a scaled impulse, the system has memory.

**Example.**

- $h(t) = 2\,\delta(t)\;\Rightarrow$ **memoryless** (output $= 2\,x(t)$).
- $h(t) = e^{-t}\,u(t)\;\Rightarrow$ **has memory** (output depends on past inputs).

### 7.8.2 Causality

**Causal:** the output at time $t$ depends only on the input at time $t$ and earlier (not the future). An LTI system is causal if and only if:

$$\boxed{\;h(t) = 0\quad\text{for }t<0\;}$$

**Physical interpretation:** the system cannot respond *before* the impulse is applied.

**Examples.**

- $h(t) = e^{-2t}\,u(t)\;\Rightarrow$ **causal** (zero for $t<0$).
- $h(t) = e^{2t}\,u(-t)\;\Rightarrow$ **non-causal** (nonzero for $t<0$).
- $h(t) = e^{-|t|}\;\Rightarrow$ **non-causal** (nonzero for all $t$).

> **Key Insight**
>
> For a **causal** system with a **causal** input (i.e., $x(t) = 0$ for $t<0$), the convolution integral simplifies to:
>
> $$y(t) = \int_0^t x(\tau)\,h(t-\tau)\,d\tau$$
>
> This is often easier to compute!

### 7.8.3 Stability (BIBO)

**BIBO stable:** Bounded Input $\Rightarrow$ Bounded Output. An LTI system is BIBO stable if and only if the impulse response is **absolutely integrable**:

$$\boxed{\;\int_{-\infty}^{\infty} |h(t)|\,dt < \infty\;}$$

**Intuition:** if the "total area" under $|h(t)|$ is finite, then a bounded input cannot produce an unbounded output.

**Examples.**

- $h(t) = e^{-2t}\,u(t)$: $\int_0^{\infty} e^{-2t}\,dt = \tfrac{1}{2} < \infty \Rightarrow$ **stable**.
- $h(t) = e^{t}\,u(-t)$: $\int_{-\infty}^0 e^{t}\,dt = 1 < \infty \Rightarrow$ **stable**.
- $h(t) = e^{2t}\,u(t)$: $\int_0^{\infty} e^{2t}\,dt = \infty \Rightarrow$ **unstable**.
- $h(t) = u(t)$: $\int_0^{\infty} 1\,dt = \infty \Rightarrow$ **unstable**.

> **Common Mistake**
>
> A system can be **causal but unstable** (like $h(t) = e^{2t}\,u(t)$), or **stable but non-causal** (like $h(t) = e^{t}\,u(-t)$). Causality and stability are independent properties!

### 7.8.4 Invertibility

An LTI system with impulse response $h(t)$ is **invertible** if there exists an inverse system $h_i(t)$ such that:

$$h(t)*h_i(t) = \delta(t)$$

The cascade of the system and its inverse gives back the original signal.

**Example — Time delay and time advance.**

- If $h(t) = \delta(t - t_0)$ (delay by $t_0$),
- then $h_i(t) = \delta(t + t_0)$ (advance by $t_0$),
- because $\delta(t - t_0)*\delta(t + t_0) = \delta(t)$.

## 7.9 The Unit Step Response

The **unit step response** $s(t)$ is the output when the input is the unit step $u(t)$:

$$\boxed{\;s(t) = u(t)*h(t) = \int_{-\infty}^{t} h(\tau)\,d\tau\;}$$

**Why this formula?** Since $u(t - \tau) = 1$ for $\tau \leq t$ and 0 otherwise:

$$s(t) = \int_{-\infty}^{\infty} h(\tau)\,u(t-\tau)\,d\tau = \int_{-\infty}^{t} h(\tau)\,d\tau$$

### 7.9.1 Relationship Between $h(t)$ and $s(t)$

The step response is the integral of the impulse response:

$$s(t) = \int_{-\infty}^{t} h(\tau)\,d\tau$$

Conversely, the impulse response is the derivative of the step response:

$$\boxed{\;h(t) = \frac{d s(t)}{d t}\;}$$

> **Key Insight**
>
> If measuring the impulse response directly is difficult (an ideal impulse is hard to generate physically), you can:
>
> 1. Apply a step input $u(t)$.
> 2. Measure the step response $s(t)$.
> 3. Differentiate to get $h(t) = ds(t)/dt$.

**Example:** If $h(t) = e^{-t}\,u(t)$, find the step response.

$$s(t) = \int_{-\infty}^{t} e^{-\tau}\,u(\tau)\,d\tau = \int_0^t e^{-\tau}\,d\tau = 1 - e^{-t}\text{ for } t\geq 0$$

So $s(t) = (1 - e^{-t})\,u(t)$.

## 7.10 Summary and Key Formulas

| Concept | Formula |
|---|---|
| Sifting property | $\int_{-\infty}^{\infty} x(\tau)\,\delta(\tau-t_0)\,d\tau = x(t_0)$ |
| Signal decomposition | $x(t) = \int_{-\infty}^{\infty} x(\tau)\,\delta(t-\tau)\,d\tau$ |
| Impulse response | $h(t) = T\{\delta(t)\}$ |
| Convolution integral | $y(t) = \int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau$ |
| Commutativity | $x(t)*h(t) = h(t)*x(t)$ |
| Distributivity | $x*(h_1 + h_2) = x*h_1 + x*h_2$ |
| Associativity | $(x*h_1)*h_2 = x*(h_1*h_2)$ |
| Identity | $x(t)*\delta(t) = x(t)$ |
| Delay | $x(t)*\delta(t-t_0) = x(t-t_0)$ |
| Memoryless | $h(t) = K\,\delta(t)$ |
| Causal | $h(t) = 0$ for $t<0$ |
| BIBO stable | $\int_{-\infty}^{\infty} |h(t)|\,dt < \infty$ |
| Step response | $s(t) = \int_{-\infty}^{t} h(\tau)\,d\tau$ |

## 7.11 Common Mistakes to Avoid

1. **Forgetting to flip before shifting:** in $h(t-\tau)$, you must flip $h(\tau)$ first, then shift. Most common error!
2. **Wrong integration limits:** the limits depend on where both signals are nonzero. Always sketch the signals and identify the overlap region.
3. **Confusing $t$ and $\tau$:**
   - $t$ is the output time (the variable in your answer).
   - $\tau$ is the dummy integration variable.
4. **Forgetting delta sifting rules:** when the delta is outside the integration limits, the integral equals zero.
5. **Confusing stability and causality:** these are independent properties! A system can be stable but non-causal, or causal but unstable.
6. **Computing $\int h(t)\,dt$ without absolute values:** for stability, you need the integral of $|h(t)|$, **not** $h(t)$.

> **Key Insight — Study Strategy**
>
> Practice computing convolutions by hand. Work through the graphical method (flip-shift-multiply-integrate) until it becomes automatic. This builds intuition that will help you throughout the course!

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **Sifting Example 1:** $\int (t^2+3t)\delta(t-2)\,dt = (2)^2 + 3(2) = 10$.
2. **Sifting Example 2:** $\int e^{-3t}\delta(t+1)\,dt = e^{-3(-1)} = e^3$.
3. **Sifting with limits:** $\int_0^5 x(t)\delta(t+2)\,dt = 0$ (delta at $t=-2$ is outside the interval).
4. **Two rectangular pulses:** $x(t)=u(t)-u(t-1)$ convolved with $h(t)=u(t)-u(t-2)$ gives a trapezoidal pulse: $y(t) = 0$/$t$/$1$/$(3-t)$/$0$ over five regions.
5. **Exponential and step:** $e^{-at}u(t) * u(t) = \frac{1}{a}(1 - e^{-at})\,u(t)$.
6. **Impulse response of memoryless system:** $h(t) = K\delta(t)$ gives $y(t) = K\,x(t)$.
7. **Causality check:** $h(t) = e^{-2t}u(t)$ is causal; $h(t) = e^{2t}u(-t)$ and $h(t) = e^{-|t|}$ are non-causal.
8. **Stability check:** $h(t)=e^{-2t}u(t)$ is stable; $h(t)=e^{2t}u(t)$ and $h(t)=u(t)$ are unstable.
9. **Inverse of delay:** $\delta(t-t_0) * \delta(t+t_0) = \delta(t)$ — advance is the inverse of delay.
10. **Step response of $h(t)=e^{-t}u(t)$:** $s(t) = (1 - e^{-t})\,u(t)$, and $ds/dt = e^{-t}u(t) + 0 = h(t)$ recovers $h$.
