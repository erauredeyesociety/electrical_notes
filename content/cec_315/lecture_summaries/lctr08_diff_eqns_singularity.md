# Lecture 8 — Differential / Difference Equations and Singularity Functions

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr08-diff-eqns-singularity.pdf`
**Exam coverage:** Exam 1

---

**Lctr 8: Differential/Difference Equations and Singularity Functions**

Rogelio Gracia Otalvaro

Spring 2026

**Focus:** Sections 2.4 and 2.5 (Pages 116 to 140)

---

## 8.1 Introduction: Why Differential and Difference Equations?

> **Why This Matters**
>
> So far, we've characterized LTI systems by their **impulse response** $h(t)$ or $h[n]$. But how do we know what $h(t)$ is in the first place? For many physical systems (circuits, mechanical systems, etc.), the system is **naturally** described by a **differential equation** (CT) or **difference equation** (DT). This lecture shows how to connect these descriptions and find the impulse response!

**Two ways to describe an LTI system:**

| Impulse Response | Differential / Difference Equation |
|---|---|
| $y(t) = x(t)*h(t)$ | $\dfrac{dy}{dt} + a\,y = b\,x$ |
| Convolution integral | Derivative relationship |

Both describe the **same** system! We'll learn to go from one to the other.

## 8.2 First-Order Differential Equations (Continuous-Time)

### 8.2.1 The Standard Form

The simplest and most common CT LTI system is described by a **first-order** equation:

$$\boxed{\;\frac{dy(t)}{dt} + a\,y(t) = b\,x(t)\;}$$

where:

- $y(t)$ = output signal
- $x(t)$ = input signal
- $a,\,b$ = constants (system parameters)

**Physical example.** An RC circuit has the equation:

$$\frac{d v_C(t)}{d t} + \frac{1}{RC}\,v_C(t) = \frac{1}{RC}\,v_{\text{in}}(t)$$

Here $a = 1/(RC)$ is the "time constant" (inverse of) of the circuit.

### 8.2.2 Solving First-Order Equations: Step by Step

To solve $\tfrac{dy}{dt} + a\,y = b\,x(t)$, we use the **integrating factor method** (or, equivalently, split the solution into homogeneous + particular parts).

**Step 1:** Identify $a$ and $b$ from the equation.

**Step 2:** The **homogeneous solution** (when $x(t) = 0$) is:

$$y_h(t) = C\,e^{-at}$$

where $C$ is determined by initial conditions.

**Step 3:** Find the **particular solution** $y_p(t)$ based on the form of $x(t)$ (try a form similar to the input).

**Step 4:** The **total solution** is:

$$y(t) = y_h(t) + y_p(t) = C\,e^{-at} + y_p(t)$$

**Step 5:** Apply initial conditions to find $C$.

> **Key Insight — Initial Rest**
>
> For a **causal LTI system at initial rest**, the initial condition is $y(0^-) = 0$. This means the system has no stored energy before the input is applied. "Initial rest" is the convention we use throughout this course.

### 8.2.3 Worked Example 1: Finding the Impulse Response

**Problem:** Find the impulse response $h(t)$ of the system

$$\frac{dy(t)}{dt} + 2\,y(t) = x(t).$$

**Solution.** Set $x(t) = \delta(t)$ (unit impulse) and solve for $y(t) = h(t)$.

**Step 1: Identify parameters.** $a = 2$, $b = 1$.

**Step 2: For $t>0$,** the impulse has already passed and the equation becomes homogeneous:

$$\frac{dh(t)}{dt} + 2\,h(t) = 0\qquad t > 0$$

with solution $h(t) = C\,e^{-2t}$ for $t > 0$.

**Step 3: Find $C$ using the impulse's effect.** The impulse $\delta(t)$ causes an instantaneous jump in the output. Integrate the original equation across $t=0$:

$$\int_{0^-}^{0^+} \frac{dh}{dt}\,dt + 2\int_{0^-}^{0^+} h(t)\,dt = \int_{0^-}^{0^+} \delta(t)\,dt$$

The first integral is $h(0^+) - h(0^-)$. The second integral is zero (because $h$ is finite over an infinitesimal interval). The right side is 1. So:

$$h(0^+) - h(0^-) = 1$$

With initial rest ($h(0^-) = 0$) we get $h(0^+) = 1$. From $h(t) = C\,e^{-2t}$ at $t = 0^+$: $1 = C\,e^{0} = C$, so $C = 1$.

**Step 4: Write the complete answer.**

$$\boxed{\;h(t) = e^{-2t}\,u(t)\;}$$

The $u(t)$ ensures the response is zero for $t<0$ (causality).

> **Key Insight — Quick Formula**
>
> For the first-order system $\tfrac{dy}{dt} + a\,y = b\,x$, the impulse response is:
>
> $$h(t) = b\,e^{-at}\,u(t)$$
>
> This is a decaying exponential if $a > 0$ (stable system).

### 8.2.4 Worked Example 2: Response to a Step Input

**Problem:** Find the output $y(t)$ of the system $\tfrac{dy}{dt} + 2y = 3x$ when $x(t) = u(t)$, with $y(0^-) = 0$.

**Step 1:** $a = 2$, $b = 3$.

**Step 2:** For $t \geq 0$, the equation becomes:

$$\frac{dy}{dt} + 2y = 3\cdot 1 = 3$$

**Step 3:** Homogeneous solution: $y_h(t) = C\,e^{-2t}$.

**Step 4:** Particular solution. Since the RHS is a constant (3), try $y_p = K$ (constant):

$$\frac{d K}{dt} + 2K = 3\;\Rightarrow\;0 + 2K = 3\;\Rightarrow\;K = \frac{3}{2}$$

**Step 5:** Total solution:

$$y(t) = C\,e^{-2t} + \frac{3}{2}\quad\text{for } t \geq 0$$

**Step 6:** Apply initial condition. At $t=0$: $y(0) = 0$ (initial rest, since there is no impulse at $t=0$):

$$0 = C\,e^{0} + \frac{3}{2} = C + \frac{3}{2}\;\Rightarrow\;C = -\frac{3}{2}$$

**Final answer:**

$$\boxed{\;y(t) = \frac{3}{2}\left(1 - e^{-2t}\right)u(t)\;}$$

**Interpretation:** the output starts at 0 and exponentially approaches the steady-state value $3/2$. Note that this matches the step response $s(t) = h(t)*u(t)$ you would obtain from the impulse response $h(t) = 3\,e^{-2t}\,u(t)$.

## 8.3 First-Order Difference Equations (Discrete-Time)

### 8.3.1 The Standard Form

The discrete-time equivalent is a **first-order difference equation**:

$$\boxed{\;y[n] - \alpha\,y[n-1] = b\,x[n]\;}$$

or equivalently (rearranging):

$$y[n] = \alpha\,y[n-1] + b\,x[n]$$

This is a **recursive** equation: the current output depends on the previous output.

> **Key Insight — Recursive vs. Non-recursive**
>
> - **Recursive (IIR):** output depends on past outputs. Has an **I**nfinite **I**mpulse **R**esponse.
> - **Non-recursive (FIR):** output depends only on inputs. Has a **F**inite **I**mpulse **R**esponse.

### 8.3.2 Solving by Iteration

The easiest way to solve difference equations is by **iteration**: compute values one by one, starting from initial rest.

**Worked Example 3 — Finding Impulse Response by Iteration.**

**Problem:** Find the impulse response $h[n]$ of $y[n] = \tfrac{1}{2}\,y[n-1] + x[n]$.

**Solution.** Set $x[n] = \delta[n]$ and compute $h[n]$ for each $n$, starting from initial rest ($y[n] = 0$ for $n < 0$).

$$n = 0:\quad h[0] = \tfrac{1}{2}\,h[-1] + \delta[0] = \tfrac{1}{2}(0) + 1 = 1$$
$$n = 1:\quad h[1] = \tfrac{1}{2}\,h[0] + \delta[1] = \tfrac{1}{2}(1) + 0 = \tfrac{1}{2}$$
$$n = 2:\quad h[2] = \tfrac{1}{2}\,h[1] + \delta[2] = \tfrac{1}{2}\!\left(\tfrac{1}{2}\right) + 0 = \tfrac{1}{4}$$
$$n = 3:\quad h[3] = \tfrac{1}{2}\,h[2] + \delta[3] = \tfrac{1}{2}\!\left(\tfrac{1}{4}\right) + 0 = \tfrac{1}{8}$$

**Pattern:** $h[n] = (1/2)^n$ for $n \geq 0$.

$$\boxed{\;h[n] = \left(\tfrac{1}{2}\right)^n u[n]\;}$$

> **Key Insight — Quick Formula**
>
> For the first-order system $y[n] = \alpha\,y[n-1] + b\,x[n]$, the impulse response is:
>
> $$h[n] = b\,\alpha^n\,u[n]$$
>
> The system is **stable** if $|\alpha| < 1$ (decaying geometric sequence).

### 8.3.3 Worked Example 4: Step Response by Iteration

**Problem:** Find the step response $s[n]$ of $y[n] = \tfrac{1}{2}y[n-1] + x[n]$ when $x[n] = u[n]$.

**Solution (by iteration).**

$$n = 0:\quad s[0] = \tfrac{1}{2}s[-1] + u[0] = 0 + 1 = 1$$
$$n = 1:\quad s[1] = \tfrac{1}{2}s[0] + u[1] = \tfrac{1}{2}(1) + 1 = \tfrac{3}{2}$$
$$n = 2:\quad s[2] = \tfrac{1}{2}s[1] + u[2] = \tfrac{1}{2}\!\left(\tfrac{3}{2}\right) + 1 = \tfrac{7}{4}$$
$$n = 3:\quad s[3] = \tfrac{1}{2}s[2] + u[3] = \tfrac{1}{2}\!\left(\tfrac{7}{4}\right) + 1 = \tfrac{15}{8}$$

**Pattern:**

$$s[n] = 2 - \left(\tfrac{1}{2}\right)^n = 2\!\left(1 - \left(\tfrac{1}{2}\right)^{n+1}\right)$$

The output approaches 2 as $n\to\infty$ (steady state).

## 8.4 Stability From Differential / Difference Equations

> **Key Insight — Stability Check**
>
> - **CT:** $\tfrac{dy}{dt} + a\,y = b\,x$ is **stable** if $a > 0$ (exponential decays).
> - **DT:** $y[n] = \alpha\,y[n-1] + b\,x[n]$ is **stable** if $|\alpha| < 1$ (geometric series converges).

**Examples.**

- $\frac{dy}{dt} + 3y = x\;\Rightarrow\;a = 3 > 0\;\Rightarrow$ **stable**.
- $\frac{dy}{dt} - 2y = x\;\Rightarrow\;a = -2 < 0\;\Rightarrow$ **unstable** (grows exponentially!).
- $y[n] = 0.5\,y[n-1] + x[n]\;\Rightarrow\;|\alpha| = 0.5 < 1\;\Rightarrow$ **stable**.
- $y[n] = 2\,y[n-1] + x[n]\;\Rightarrow\;|\alpha| = 2 > 1\;\Rightarrow$ **unstable**.

## 8.5 Singularity Functions

> **Why This Matters**
>
> Singularity functions ($\delta(t)$, $u(t)$, and their derivatives / integrals) form a **family** of related functions. Understanding their relationships helps us analyze systems and solve differential equations more easily.

### 8.5.1 The Family of Singularity Functions

The singularity family is connected by differentiation (moving right) and integration (moving left):

$$r(t) = t\,u(t) \;\xrightarrow{d/dt}\; u(t) \;\xrightarrow{d/dt}\; \delta(t) \;\xrightarrow{d/dt}\; \delta'(t)$$

Going the other way (by integration):

$$\text{Ramp } r(t) \;\xleftarrow{\int}\; \text{Step } u(t) \;\xleftarrow{\int}\; \text{Impulse } \delta(t) \;\xleftarrow{\int}\; \text{Doublet } \delta'(t)$$

*[Figure: The four members of the singularity family displayed as a horizontal chain. From left to right: ramp $r(t) = t\,u(t)$, step $u(t)$, impulse $\delta(t)$, doublet $\delta'(t)$. Arrows pointing right are labeled $d/dt$; arrows pointing left are labeled $\int$.]*

### 8.5.2 Key Relationships

**Derivative relationships:**

$$\frac{d}{dt}[r(t)] = u(t),\qquad \frac{d}{dt}[u(t)] = \delta(t),\qquad \frac{d}{dt}[\delta(t)] = \delta'(t)$$

**Integral relationships:**

$$\int_{-\infty}^{t}\delta(\tau)\,d\tau = u(t),\qquad \int_{-\infty}^{t}u(\tau)\,d\tau = r(t) = t\,u(t)$$

> **Key Insight**
>
> Remember: moving **right** in the diagram = taking derivatives. Moving **left** = integrating.

### 8.5.3 The Ramp Function

The **ramp function** is defined as:

$$r(t) = t\,u(t) = \begin{cases} 0, & t < 0 \\ t, & t \geq 0 \end{cases}$$

It is the integral of the unit step (accumulation of a constant).

### 8.5.4 The Unit Doublet

The **unit doublet** $\delta'(t)$ (also written $u_1(t)$) is the derivative of the impulse:

$$\delta'(t) = \frac{d\delta(t)}{dt}$$

**Property — Convolving with the doublet takes the derivative:**

$$x(t)*\delta'(t) = \frac{d x(t)}{d t}$$

## 8.6 Useful Properties of Singularity Functions

### 8.6.1 Scaling the Impulse

$$\boxed{\;\delta(at) = \frac{1}{|a|}\,\delta(t)\;}$$

**Example.** $\delta(2t) = \tfrac{1}{2}\,\delta(t)$.

**Why?** The impulse is "compressed" by factor $a$, but its area must remain 1, so its "height" increases by $|a|$ — hence the $1/|a|$ scale.

### 8.6.2 Impulse Times a Function

$$\boxed{\;x(t)\,\delta(t - t_0) = x(t_0)\,\delta(t - t_0)\;}$$

The impulse "samples" the value of $x(t)$ at $t = t_0$.

**Example.** $(t^2 + 3)\,\delta(t - 2) = (4 + 3)\,\delta(t - 2) = 7\,\delta(t - 2)$.

> **Common Mistake**
>
> Don't confuse this with the **sifting property**! This is multiplication, not integration:
>
> - Multiplication: $x(t)\,\delta(t-t_0) = x(t_0)\,\delta(t-t_0)$ (result is a **scaled impulse**).
> - Sifting (integration): $\int x(t)\,\delta(t-t_0)\,dt = x(t_0)$ (result is a **number**).

## 8.7 Worked Example 5: Using Singularity Functions

**Problem:** Find the derivative of $x(t) = (t + 1)\,u(t)$.

**Solution.** Use the product rule:

$$\frac{d}{dt}\!\left[(t+1)\,u(t)\right] = \frac{d(t+1)}{dt}\cdot u(t) + (t+1)\cdot \frac{d u(t)}{dt}$$

We know $du(t)/dt = \delta(t)$, so:

$$= 1\cdot u(t) + (t+1)\cdot\delta(t)$$

Using the multiplication rule $(t+1)\,\delta(t) = (0+1)\,\delta(t) = \delta(t)$:

$$\boxed{\;\frac{d}{dt}\!\left[(t+1)\,u(t)\right] = u(t) + \delta(t)\;}$$

**Interpretation.** The derivative has:

- A **step** $u(t)$: the slope of the ramp part (the function grows with slope 1 for $t \geq 0$).
- An **impulse** $\delta(t)$: the "jump" at $t=0$ from $0$ up to $1$ (the function jumps from 0 to 1 at the origin because $(0+1)\cdot u(0^+) = 1$).

## 8.8 Summary and Key Formulas

| Concept | Formula |
|---|---|
| First-order CT system | $\dfrac{dy}{dt} + a\,y = b\,x$ |
| CT impulse response | $h(t) = b\,e^{-at}\,u(t)$ |
| CT stability condition | $a > 0$ |
| First-order DT system | $y[n] = \alpha\,y[n-1] + b\,x[n]$ |
| DT impulse response | $h[n] = b\,\alpha^n\,u[n]$ |
| DT stability condition | $|\alpha| < 1$ |
| Derivative of step | $\dfrac{d u(t)}{dt} = \delta(t)$ |
| Integral of impulse | $\displaystyle\int_{-\infty}^{t}\delta(\tau)\,d\tau = u(t)$ |
| Impulse scaling | $\delta(at) = \dfrac{1}{|a|}\,\delta(t)$ |
| Impulse sampling | $x(t)\,\delta(t - t_0) = x(t_0)\,\delta(t - t_0)$ |
| Ramp function | $r(t) = t\,u(t)$ |
| Doublet derivative | $x(t)*\delta'(t) = dx(t)/dt$ |

## 8.9 Common Mistakes to Avoid

1. **Forgetting the $u(t)$ or $u[n]$:** impulse responses of causal systems must include the unit step to ensure $h(t) = 0$ for $t<0$ (or $h[n] = 0$ for $n<0$).
2. **Sign errors in the exponent:** for $\tfrac{dy}{dt} + a\,y = b\,x$, the impulse response has $e^{-at}$, **not** $e^{+at}$. Watch the signs!
3. **Confusing stability conditions:**
   - **CT:** need $a > 0$ (positive coefficient of $y$).
   - **DT:** need $|\alpha| < 1$ (magnitude less than 1).
4. **Iteration errors in DT:** always start from initial rest ($y[n] = 0$ for $n < 0$) and compute values in order.
5. **Derivative of $u(t)$:** remember $du(t)/dt = \delta(t)$, **not** $u(t)$ or 0!

> **Key Insight — Study Tip**
>
> Practice the iteration method for DT systems — it builds intuition for how recursive systems work and is a reliable way to check your closed-form answers!

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **Worked Example 1 — CT impulse response:** $\frac{dy}{dt} + 2y = x$ has impulse response $h(t) = e^{-2t}u(t)$, obtained by solving the homogeneous equation for $t>0$ and applying the jump condition $h(0^+) - h(0^-) = 1$.
2. **Worked Example 2 — CT step response:** $\frac{dy}{dt} + 2y = 3x$ with $x(t) = u(t)$ gives $y(t) = \tfrac{3}{2}(1 - e^{-2t})\,u(t)$; steady state $= 3/2$.
3. **Worked Example 3 — DT impulse response by iteration:** $y[n] = \tfrac{1}{2}y[n-1] + x[n]$ yields $h[n] = (1/2)^n u[n]$ (iterate: 1, 1/2, 1/4, 1/8, …).
4. **Worked Example 4 — DT step response by iteration:** Same system with $x[n] = u[n]$ gives $s[n] = 2(1 - (1/2)^{n+1})$; iterates: 1, 3/2, 7/4, 15/8, … approaching 2.
5. **Stability examples:** $\frac{dy}{dt} + 3y = x$ stable; $\frac{dy}{dt} - 2y = x$ unstable; $y[n] = 0.5 y[n-1] + x[n]$ stable; $y[n] = 2 y[n-1] + x[n]$ unstable.
6. **Singularity family relationships:** $\frac{d}{dt}[r(t)] = u(t)$, $\frac{d}{dt}[u(t)] = \delta(t)$, $\frac{d}{dt}[\delta(t)] = \delta'(t)$; integrals invert these.
7. **Impulse scaling:** $\delta(2t) = \tfrac{1}{2}\delta(t)$.
8. **Impulse times a function:** $(t^2 + 3)\delta(t - 2) = 7\,\delta(t - 2)$.
9. **Worked Example 5 — Derivative of $(t+1)u(t)$:** Product rule gives $u(t) + (t+1)\delta(t) = u(t) + \delta(t)$; the step captures the slope of the ramp and the impulse captures the jump at $t=0$.
