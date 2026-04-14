# Lecture 18 — System Analysis Using the Unilateral Laplace Transform

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr18-system-analysis-unilateral-laplace.pdf`
**Exam coverage:** Exam 3

---

**Lctr 18: System Analysis with the Laplace Transform and the Unilateral Laplace Transform**

Rogelio Gracia Otalvaro
Spring 2026

**Lctr 18: System Analysis with the Laplace Transform and the Unilateral Laplace Transform**

Spring 2026

Focus: Sections 9.7–9.9 (Pages 693–720)

---

## 18.1 The Big Picture

### Why This Matters

In Lectures 16–17 we built the machinery: how to compute and invert Laplace transforms, and the properties that make them useful. Now we put it all to work. This lecture has two main goals:

**Part I (System Analysis):** Given a system described by a differential equation, find its transfer function $H(s)$, determine stability and causality from the pole locations and ROC, and compute the output for any input.

**Part II (Unilateral Laplace Transform):** Extend our tools to handle systems with **nonzero initial conditions**, the key to solving real-world transient problems where the system starts in some state other than rest.

By the end of this lecture, you will have a complete pipeline: differential equation $\to$ transfer function $\to$ pole-zero analysis $\to$ stability/causality determination $\to$ output computation, with or without initial conditions.

**Roadmap:**

1. The system function $H(s)$ for LTI systems described by differential equations.
2. Causality from the ROC.
3. Stability from the ROC (the $j\omega$-axis criterion).
4. Causality + stability together: the "all poles in the LHP" rule.
5. Block diagram representations.
6. The unilateral Laplace transform: definition and modified differentiation property.
7. Solving differential equations with initial conditions.

---

## Part I: System Analysis with $H(s)$

## 18.2 The System Function $H(s)$

Consider a causal LTI system described by a linear constant-coefficient differential equation:

$$\sum_{k=0}^{N} a_k \frac{d^k y}{dt^k} = \sum_{k=0}^{M} b_k \frac{d^k x}{dt^k}$$

Taking the bilateral Laplace transform of both sides (assuming zero initial conditions, i.e., the system is initially at rest):

$$\sum_{k=0}^{N} a_k\, s^k\, Y(s) = \sum_{k=0}^{M} b_k\, s^k\, X(s)$$

The **system function** (or **transfer function**) is:

$$H(s) = \frac{Y(s)}{X(s)} = \frac{\sum_{k=0}^{M} b_k\, s^k}{\sum_{k=0}^{N} a_k\, s^k} = \frac{b_M s^M + b_{M-1} s^{M-1} + \cdots + b_0}{a_N s^N + a_{N-1} s^{N-1} + \cdots + a_0}$$

### Key Insight

The Laplace transform converts the differential equation into an algebraic equation: each derivative $d^k/dt^k$ becomes multiplication by $s^k$. The transfer function $H(s)$ is a **rational function**, a ratio of polynomials in $s$. The denominator roots are the poles; the numerator roots are the zeros. Everything about the system's behavior (stability, frequency response, transient response) is encoded in these pole and zero locations.

### From Differential Equation to $H(s)$

**System:** $\dfrac{d^2 y}{dt^2} + 5\dfrac{dy}{dt} + 6y = 2\dfrac{dx}{dt} + x$

**Step 1:** Replace $d^k/dt^k \to s^k$:

$$(s^2 + 5s + 6)\, Y(s) = (2s + 1)\, X(s)$$

**Step 2:** Form $H(s)$:

$$H(s) = \frac{2s + 1}{s^2 + 5s + 6} = \frac{2s + 1}{(s+2)(s+3)}$$

**Poles:** $s = -2, -3$ (both in the LHP). **Zero:** $s = -1/2$.

**Step 3: Pole-zero plot.**

*Figure: Pole-zero plot in the $s$-plane. Horizontal axis $\sigma$, vertical axis $j\omega$. Two poles marked with $\times$ at $s = -3$ and $s = -2$ on the real axis. One zero marked with $\circ$ at $s = -1/2$ on the real axis, just to the left of the $j\omega$-axis. The $j\omega$-axis is labeled in green.*

Both poles are in the LHP $\Rightarrow$ stable and causal (as we will formalize below).

---

## 18.3 Causality from the ROC

### Causality Criterion

An LTI system is **causal** (output depends only on present and past input) if and only if:

1. The impulse response $h(t)$ is **right-sided**: $h(t) = 0$ for $t < 0$.
2. Equivalently, the ROC of $H(s)$ is a **right half-plane**:

$$\text{ROC}: \quad \operatorname{Re}\{s\} > \sigma_{\max}$$

where $\sigma_{\max}$ is the real part of the rightmost pole.

3. If $H(s)$ is rational, causality also requires that $H(s) \to 0$ (or a finite constant) as $|s| \to \infty$, which means $M \leq N$ (degree of numerator $\leq$ degree of denominator).

---

## 18.4 BIBO Stability from the ROC

### Stability Criterion

An LTI system is **BIBO stable** (bounded input $\Rightarrow$ bounded output) if and only if:

1. The impulse response is absolutely integrable: $\displaystyle\int_{-\infty}^{+\infty} |h(t)|\, dt < \infty$.
2. Equivalently, the ROC of $H(s)$ **includes the $j\omega$-axis**: $\operatorname{Re}\{s\} = 0$ is in the ROC.

This means the Fourier transform $H(j\omega)$ exists, and the system has a well-defined frequency response.

---

## 18.5 Causal *and* Stable: The "All Poles in the LHP" Rule

Combining the two criteria:

### The Golden Rule for Causal LTI Systems

A causal LTI system with rational $H(s)$ is BIBO stable **if and only if all poles of $H(s)$ lie in the open left half-plane** (i.e., all poles have strictly negative real parts).

$$\text{Causal + Stable} \iff \operatorname{Re}\{p_i\} < 0 \ \ \forall \text{ poles } p_i$$

**Why this works:** For a causal system, the ROC is $\operatorname{Re}\{s\} > \sigma_{\max}$ (to the right of the rightmost pole). For this ROC to include the $j\omega$-axis, we need $\sigma_{\max} < 0$, which means every pole must have $\operatorname{Re}\{p_i\} < 0$.

*Figure: Two $s$-plane diagrams side by side. Left: "Causal + Stable" — three poles marked with $\times$ all in the LHP; the ROC is shaded green as a right half-plane that includes the $j\omega$-axis (checkmark). Right: "Causal + Unstable" — some poles marked with $\times$ in the RHP; the ROC is a right half-plane shaded red to the right of the rightmost pole, which does NOT include the $j\omega$-axis (X mark).*

### Stability Classification

Classify each system as stable, marginally stable, or unstable (assuming causality):

| $H(s)$ | Poles | Pole locations | Classification |
|---|---|---|---|
| $\dfrac{1}{s+3}$ | $s = -3$ | LHP | **Stable** |
| $\dfrac{1}{s-2}$ | $s = 2$ | RHP | **Unstable** |
| $\dfrac{1}{s^2+4}$ | $s = \pm j2$ | $j\omega$-axis | **Marginally stable** |
| $\dfrac{s+1}{(s+2)(s+5)}$ | $s = -2, -5$ | LHP | **Stable** |
| $\dfrac{1}{(s+1)(s-1)}$ | $s = \pm 1$ | one in RHP | **Unstable** |

### Warning

Poles on the $j\omega$-axis (e.g., $s = \pm j\omega_0$) correspond to **marginally stable** systems: the impulse response neither decays nor grows but oscillates forever. These are on the boundary: technically not BIBO stable, because the $j\omega$-axis is *not* in the ROC (it is the ROC boundary). A sinusoidal input at the resonance frequency produces an unbounded output.

---

## 18.6 Complete System Analysis Pipeline

### Complete Pipeline: Differential Equation to Output

**System:** $\dfrac{dy}{dt} + 3y = x(t),$ **Input:** $x(t) = e^{-t}\, u(t)$.

**Step 1: Find $H(s)$.**

$$(s + 3)\, Y(s) = X(s) \ \Rightarrow\ H(s) = \frac{1}{s+3}, \quad \text{ROC: } \operatorname{Re}\{s\} > -3$$

Pole at $s = -3$ (LHP) $\Rightarrow$ system is causal and stable. $\checkmark$

**Step 2: Find $X(s)$.**

$$X(s) = \frac{1}{s+1}, \quad \operatorname{Re}\{s\} > -1$$

**Step 3: Find $Y(s) = H(s) \cdot X(s)$.**

$$Y(s) = \frac{1}{(s+3)(s+1)}, \quad \operatorname{Re}\{s\} > -1$$

(The ROC is the intersection: $\sigma > -3\ \cap\ \sigma > -1 = \sigma > -1$.)

**Step 4: Partial fractions.**

$$\frac{1}{(s+3)(s+1)} = \frac{A}{s+3} + \frac{B}{s+1}$$

- $s = -3$: $1 = A(-3+1) \Rightarrow A = -1/2$.
- $s = -1$: $1 = B(-1+3) \Rightarrow B = 1/2$.

**Step 5: Invert.** Both poles are to the left of the ROC boundary ($\sigma = -1$), so both terms are right-sided:

$$y(t) = \frac{1}{2}\left(e^{-t} - e^{-3t}\right) u(t)$$

**Step 6: Verify.**

- $y(0^+) = \tfrac{1}{2}(1-1) = 0$ $\checkmark$ (system starts at rest)
- $y(\infty) = 0$ $\checkmark$ (both exponentials decay)
- $y'(0^+) = \tfrac{1}{2}(-1+3) = 1 = x(0^+)$ $\checkmark$ (from the ODE: $y'(0^+) + 3 \cdot 0 = 1$)

*Figure: Plot showing $y(t)$ (solid blue curve) and $x(t) = e^{-t}u(t)$ (dashed red curve) versus $t$ from 0 to 4. The input starts at 1 and decays exponentially. The output starts at 0, rises to a peak near $t \approx 0.5$ at about $y \approx 0.2$, then decays back toward 0.*

---

## 18.7 Block Diagram Representations

Complex systems are built from interconnections of simpler subsystems. In the $s$-domain:

### 18.7.1 Series (Cascade) Connection

*Figure: Block diagram — $X(s)$ feeds into block $H_1(s)$, whose output feeds into block $H_2(s)$, whose output is $Y(s)$.*

$$H(s) = H_1(s) \cdot H_2(s)$$

### 18.7.2 Parallel Connection

*Figure: Block diagram — $X(s)$ splits and feeds into two parallel blocks $H_1(s)$ and $H_2(s)$. Their outputs are summed at a summing junction (circle with $+$) to produce $Y(s)$.*

$$H(s) = H_1(s) + H_2(s)$$

### 18.7.3 Feedback Connection

*Figure: Block diagram — $X(s)$ enters a summing junction (with a $+$ input and a $-$ feedback input), whose output feeds forward block $G(s)$ to produce $Y(s)$. $Y(s)$ is tapped and fed back through block $F(s)$ to the negative input of the summing junction.*

$$H(s) = \frac{G(s)}{1 + G(s)\, F(s)}$$

### Key Insight

Block diagrams in the $s$-domain are purely algebraic. Series connection = multiply. Parallel = add. Feedback = the formula above. This is far simpler than working with convolution integrals in the time domain, which is one of the main practical advantages of the Laplace transform.

---

## Part II: The Unilateral Laplace Transform

## 18.8 Why We Need the Unilateral Transform

The bilateral Laplace transform assumes the system is **initially at rest** (all initial conditions are zero). But in practice, systems often have nonzero initial conditions:

- A capacitor charged to 5 V before a switch closes.
- A mass-spring system released from a displaced position.
- A control system with a nonzero set point at startup.

The **unilateral Laplace transform** handles these cases by modifying the lower limit of integration.

## 18.9 Definition

### The Unilateral Laplace Transform

$$\mathcal{X}(s) = \int_{0^-}^{\infty} x(t)\, e^{-st}\, dt$$

The lower limit is $0^-$ (just before $t = 0$), which captures any impulse at $t = 0$. For signals that are zero for $t < 0$ (i.e., causal signals), the unilateral and bilateral transforms are identical.

**Notation:** We use $\mathcal{X}(s)$ or simply $X(s)$ for the unilateral transform when context is clear. Many textbooks use the same notation for both.

---

## 18.10 The Key Difference: The Differentiation Property

This is where the unilateral transform earns its keep. Recall that the bilateral transform gives:

$$\frac{dx}{dt} \ \stackrel{\mathcal{L}}{\longleftrightarrow}\ s\, X(s) \qquad (\text{bilateral, assumes zero ICs})$$

The unilateral transform gives:

$$\frac{dx}{dt} \ \stackrel{\mathcal{L}_u}{\longleftrightarrow}\ s\, \mathcal{X}(s) - x(0^-)$$

For the second derivative:

$$\frac{d^2 x}{dt^2} \ \stackrel{\mathcal{L}_u}{\longleftrightarrow}\ s^2\, \mathcal{X}(s) - s\, x(0^-) - x'(0^-)$$

General pattern for the $n$-th derivative:

$$\frac{d^n x}{dt^n} \ \stackrel{\mathcal{L}_u}{\longleftrightarrow}\ s^n\, \mathcal{X}(s) - s^{n-1} x(0^-) - s^{n-2} x'(0^-) - \cdots - x^{(n-1)}(0^-)$$

### Key Insight

The initial conditions $x(0^-)$, $x'(0^-)$, etc. appear explicitly in the unilateral differentiation property. This is exactly the information needed to solve an ODE with specified initial conditions. Each derivative $d^n/dt^n$ still becomes multiplication by $s^n$, but with correction terms that encode the initial state.

---

## 18.11 Solving Differential Equations with Initial Conditions

### First-Order ODE with Nonzero Initial Condition

**Solve:** $\dfrac{dy}{dt} + 3y = 0, \quad y(0^-) = 5$

**Step 1:** Take the unilateral Laplace transform of both sides.

$$\bigl[s\, Y(s) - y(0^-)\bigr] + 3\, Y(s) = 0$$
$$s\, Y(s) - 5 + 3\, Y(s) = 0$$

**Step 2:** Solve for $Y(s)$.

$$(s+3)\, Y(s) = 5 \ \Rightarrow\ Y(s) = \frac{5}{s+3}$$

**Step 3:** Invert.

$$y(t) = 5\, e^{-3t}\, u(t)$$

The system decays from its initial value of 5 with time constant $\tau = 1/3$.

**Check:** $y(0) = 5\ \checkmark$. $y'(0) = -15$. From ODE: $y'(0) = -3 y(0) = -15\ \checkmark$.

### Second-Order ODE with Initial Conditions

**Solve:** $\dfrac{d^2 y}{dt^2} + 5\dfrac{dy}{dt} + 6y = 2u(t), \quad y(0^-) = 1,\ y'(0^-) = 0$

**Step 1:** Unilateral Laplace transform.

For the left side:

$$\mathcal{L}_u\!\left\{\frac{d^2 y}{dt^2}\right\} = s^2 Y(s) - s y(0^-) - y'(0^-) = s^2 Y - s - 0$$

$$\mathcal{L}_u\!\left\{5 \frac{dy}{dt}\right\} = 5\bigl[sY(s) - y(0^-)\bigr] = 5sY - 5$$

$$\mathcal{L}_u\{6y\} = 6 Y(s)$$

For the right side: $\mathcal{L}_u\{2 u(t)\} = \dfrac{2}{s}$.

**Step 2:** Combine.

$$s^2 Y - s + 5sY - 5 + 6Y = \frac{2}{s}$$

$$(s^2 + 5s + 6)\, Y(s) = \frac{2}{s} + s + 5$$

$$Y(s) = \frac{2/s + s + 5}{(s+2)(s+3)} = \frac{s^2 + 5s + 2}{s(s+2)(s+3)}$$

**Step 3:** Partial fractions.

$$\frac{s^2 + 5s + 2}{s(s+2)(s+3)} = \frac{A}{s} + \frac{B}{s+2} + \frac{C}{s+3}$$

- $s = 0$: $2 = A(2)(3) \Rightarrow A = 1/3$.
- $s = -2$: $4 - 10 + 2 = B(-2)(1) \Rightarrow -4 = -2B \Rightarrow B = 2$.
- $s = -3$: $9 - 15 + 2 = C(-3)(-1) \Rightarrow -4 = 3C \Rightarrow C = -4/3$.

**Step 4:** Invert (all poles have ROC to the right, so all terms are right-sided):

$$y(t) = \left[\frac{1}{3} + 2\, e^{-2t} - \frac{4}{3}\, e^{-3t}\right] u(t)$$

**Step 5: Verify.**

- $y(0) = \tfrac{1}{3} + 2 - \tfrac{4}{3} = \tfrac{1+6-4}{3} = 1\ \checkmark$
- $y'(0) = 0 + 2(-2) - \tfrac{4}{3}(-3) = -4 + 4 = 0\ \checkmark$
- $y(\infty) = 1/3$ (the steady-state response to a step of amplitude 2, with DC gain $H(0) = 1/6$: $2 \times 1/6 = 1/3$) $\checkmark$

*Figure: Plot of $y(t)$ versus $t$ from 0 to 4. The response starts at $y(0^-) = 1$ (marked blue dot), decays smoothly, and asymptotes to the steady-state value $y_{\text{ss}} = 1/3$ (marked as a red dashed horizontal line).*

---

## 18.12 Zero-State Response + Zero-Input Response

The total response of a system with initial conditions can be decomposed:

$$\underbrace{y(t)}_{\text{total response}} = \underbrace{y_{\text{ZS}}(t)}_{\substack{\text{zero-state} \\ \text{response}}} + \underbrace{y_{\text{ZI}}(t)}_{\substack{\text{zero-input} \\ \text{response}}}$$

**Zero-state response (ZSR):** The output due to the input alone, assuming all initial conditions are zero. This is $Y_{\text{ZS}}(s) = H(s) \cdot X(s)$.

**Zero-input response (ZIR):** The output due to the initial conditions alone, with zero input. This is the "natural response" of the system from its initial state.

### Key Insight

In the second-order example above, we can separate the two contributions:

**ZSR** (set $y(0^-) = 0$, $y'(0^-) = 0$, keep input $2u(t)$):

$$Y_{\text{ZS}}(s) = \frac{2/s}{(s+2)(s+3)} = \frac{2}{s(s+2)(s+3)}$$

**ZIR** (set input to 0, keep $y(0^-) = 1$, $y'(0^-) = 0$):

$$Y_{\text{ZI}}(s) = \frac{s+5}{(s+2)(s+3)}$$

Adding: $Y_{\text{ZS}} + Y_{\text{ZI}} = \dfrac{s^2 + 5s + 2}{s(s+2)(s+3)}$, which is exactly what we computed. The decomposition helps you understand *which part of the output comes from the input and which comes from the initial conditions.*

---

## 18.13 Summary of the Three-Lecture Block

*Figure: Flow diagram — three boxes connected by arrows. Box 1 (blue): "Lecture 16 — Definition, ROC". Arrow labeled "tools" to Box 2 (green): "Lecture 17 — Inverse, Properties". Arrow labeled "application" to Box 3 (orange): "Lecture 18 — Systems, IVPs".*

1. **$H(s)$ from a differential equation:** Replace $d^k/dt^k$ with $s^k$ and rearrange. $H(s) = Y(s)/X(s)$ is a rational function whose poles and zeros fully characterize the system.
2. **Causality:** The system is causal iff the ROC is a right half-plane (to the right of the rightmost pole) and $M \leq N$.
3. **Stability:** The system is BIBO stable iff the ROC includes the $j\omega$-axis. For a causal system, this reduces to: **all poles in the open LHP**.
4. **Block diagrams:** Series = multiply, parallel = add, feedback = $G/(1 + GF)$.
5. **Unilateral Laplace transform:** The differentiation property $dx/dt \leftrightarrow sX(s) - x(0^-)$ incorporates initial conditions. This converts an IVP (differential equation + initial conditions) into an algebraic equation.
6. **Total response = ZSR + ZIR:** Zero-state (due to input) plus zero-input (due to ICs).

---

## 18.14 Common Mistakes to Avoid

1. **Confusing bilateral and unilateral transforms:** The bilateral transform assumes zero ICs. If the problem gives nonzero ICs, you *must* use the unilateral transform (or account for ICs explicitly).
2. **Forgetting IC terms in the unilateral differentiation property:** $\mathcal{L}_u\{y'\} = sY - y(0^-)$, **not** just $sY$. For second derivatives, there are *two* IC terms.
3. **Checking stability from the wrong criterion:** For a causal system, stability $\Leftrightarrow$ all poles in LHP. For a non-causal system, this rule does not apply; you must check whether the $j\omega$-axis is in the (possibly non-right-half-plane) ROC.
4. **Concluding instability from RHP zeros:** Zeros in the RHP do *not* cause instability. Only **poles** in the RHP (for causal systems) cause instability. RHP zeros affect the transient response shape (nonminimum-phase behavior) but not stability.
5. **Applying the pipeline to noncausal systems without adjusting the ROC:** If the system is not causal, the ROC is not necessarily a right half-plane. Always determine the ROC from the signal type (right-sided, left-sided, or two-sided).
6. **Mixing up $y(0^-)$ and $y(0^+)$:** The unilateral Laplace transform uses $0^-$ (just *before* $t = 0$) as the initial condition. If the input has a discontinuity at $t = 0$ (like a step), $y(0^+)$ may differ from $y(0^-)$.

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **Example: From Differential Equation to $H(s)$** (Section 18.2) — Given $\dfrac{d^2y}{dt^2} + 5\dfrac{dy}{dt} + 6y = 2\dfrac{dx}{dt} + x$, find $H(s) = \dfrac{2s+1}{(s+2)(s+3)}$, identify poles at $s = -2, -3$ and zero at $s = -1/2$, draw pole-zero plot, conclude stable and causal.
2. **Example: Stability Classification Table** (Section 18.5) — Classify five transfer functions ($\tfrac{1}{s+3}$, $\tfrac{1}{s-2}$, $\tfrac{1}{s^2+4}$, $\tfrac{s+1}{(s+2)(s+5)}$, $\tfrac{1}{(s+1)(s-1)}$) as stable, marginally stable, or unstable based on pole locations.
3. **Example: Complete Pipeline — Differential Equation to Output** (Section 18.6) — Solve $\dfrac{dy}{dt} + 3y = x(t)$ with $x(t) = e^{-t}u(t)$ via the six-step pipeline (find $H(s)$, $X(s)$, $Y(s)$, partial fractions, invert, verify), obtaining $y(t) = \tfrac{1}{2}(e^{-t} - e^{-3t})u(t)$.
4. **Example: First-Order ODE with Nonzero Initial Condition** (Section 18.11) — Solve $\dfrac{dy}{dt} + 3y = 0$ with $y(0^-) = 5$ using the unilateral Laplace transform; obtain $y(t) = 5e^{-3t}u(t)$.
5. **Example: Second-Order ODE with Initial Conditions** (Section 18.11) — Solve $\dfrac{d^2y}{dt^2} + 5\dfrac{dy}{dt} + 6y = 2u(t)$ with $y(0^-) = 1$, $y'(0^-) = 0$; obtain $y(t) = \left[\tfrac{1}{3} + 2e^{-2t} - \tfrac{4}{3}e^{-3t}\right]u(t)$, with verification of initial and steady-state values.
6. **Example: ZSR + ZIR Decomposition** (Section 18.12) — For the second-order ODE above, separate the total response into zero-state response $Y_{\text{ZS}}(s) = \dfrac{2}{s(s+2)(s+3)}$ and zero-input response $Y_{\text{ZI}}(s) = \dfrac{s+5}{(s+2)(s+3)}$, and confirm that their sum equals the total response.
