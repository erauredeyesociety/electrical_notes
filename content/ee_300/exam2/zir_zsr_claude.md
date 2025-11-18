---
title: "Zero-Input Response (ZIR) and Zero-State Response (ZSR)"
weight: 1
math: true
---

This documentation provides a comprehensive explanation of the Zero-Input Response (ZIR) and Zero-State Response (ZSR), drawing upon circuit theory concepts solved using the Laplace Transform (LT) methodology.

---

## Overview

The **total response** of a linear circuit can be separated into two fundamental components: the **zero-state response (ZSR)** and the **zero-input response (ZIR)**. This separation is possible because of the linearity property and the principle of superposition.

$$\text{Total Response} = \text{Zero-State Response (ZSR)} + \text{Zero-Input Response (ZIR)}$$

### 1. Theory Background: ZIR and ZSR

#### Zero-Input Response (ZIR)

The Zero-Input Response (ZIR) is the behavior of the circuit **due solely to the initial conditions** of energy storage elements (like capacitors or inductors), assuming no external input sources are active.

- **Definition:** ZIR is the response due to the initial voltage on capacitors (or current in inductors). It is calculated as if there were **zero input**.
- **Circuit State:** To calculate ZIR, the input source ($V_s$ or $I_s$) of the circuit is set to zero. For voltage sources, this means replacing them with short circuits. For current sources, this means replacing them with open circuits.
- **Nature:** ZIR is the behavior due to **device characteristics** (R, C, L values) and is not related to any external sources. Consequently, **all ZIRs are natural responses**. The poles determining the natural characteristics are due to the values of R, C, and L.
- **Physical Interpretation:** ZIR represents the "decay" or "relaxation" of energy initially stored in the circuit.

#### Zero-State Response (ZSR)

The Zero-State Response (ZSR) is the behavior of the circuit due solely to the external input sources, assuming all initial energy storage in the circuit is zero.

- **Definition:** ZSR is the response due to the input source, assuming a **zero initial state** (i.e., $v_C(0) = 0$ for capacitors and $i_L(0) = 0$ for inductors).
- **Circuit State:** To calculate ZSR, the initial state of all energy storage elements is set to zero.
- **Response Origin:** ZSR is the voltage (or current) that develops purely from the external excitation.
- **Components:** ZSR typically contains both a **natural response** component (due to circuit poles) and a **forced response** component (matching the form of the input).

---

### 2. Relevant Topics to Understand

Understanding ZIR and ZSR primarily requires the application of the Laplace Transform (LT) to circuit analysis, specifically in the $s$-domain.

| Relevant Topic | Subtopics and Importance |
| :--- | :--- |
| **Laplace Transform (LT) and $s$-Domain** | LT converts circuits from the time domain to the frequency ($s$) domain, transforming differential equations into algebraic equations that are easier to solve. The Inverse LT converts the expression back to the time domain. |
| **LT Properties** | Properties like **differentiation** and **integration** are crucial for transforming differential equations involving inductors and capacitors, respectively. |
| **$s$-Domain Device Characteristics** | Resistors: $Z_R = R$. Capacitors: $Z_C = \frac{1}{sC}$. Inductors: $Z_L = sL$. Each reactive element also has an associated initial condition term. |
| **Modeling Initial Conditions** | Initial conditions (energy stored at $t=0$) are converted into equivalent sources in the $s$-domain. For a capacitor with initial voltage $v_C(0)$, this appears as a voltage source $\frac{v_C(0)}{s}$ in series with the impedance. For an inductor with initial current $i_L(0)$, this appears as a current source $\frac{i_L(0)}{s}$ in parallel (or voltage source $Li_L(0)$ in series). |
| **Inverse LT Techniques** | Once the response in the $s$-domain ($V(s)$ or $I(s)$) is found, the Inverse LT is performed, often requiring **Partial Fraction Expansion (PFE)** and the **cover-up method** to find residues. |
| **Network Function** | The transfer function $H(s) = \frac{Y(s)}{X(s)}$ (output/input) characterizes the system. The roots of the denominator define the system poles, which determine the natural response. |

---

### 3. Step-by-Step Methods and Processes

Solving problems involving ZIR and ZSR typically involves applying the principle of superposition within the $s$-domain.

#### Step-by-Step Method (General Circuit Analysis using LT)

The process of solving circuits using LT, including finding the total response, generally follows these steps:

1. **Derive the Differential Equation:** Develop the differential equation(s) that describe the circuit in the time domain, usually by applying KVL (Kirchhoff's Voltage Law) or KCL (Kirchhoff's Current Law).

2. **Analyze for $t<0$ (Initial Conditions):** Use circuit knowledge and DC steady-state analysis to find the initial conditions. For $t < 0$, assume the circuit is in steady state:
   - Capacitors act as **open circuits** (no current flows)
   - Inductors act as **short circuits** (no voltage drop)
   - Find $v_C(0^-)$ and $i_L(0^-)$

3. **Apply Continuity:** Use continuity conditions:
   - Capacitor voltage cannot change instantaneously: $v_C(0^+) = v_C(0^-)$
   - Inductor current cannot change instantaneously: $i_L(0^+) = i_L(0^-)$

4. **Transform to $s$-Domain:** For $t \ge 0$, transform the circuit to the $s$-domain:
   - Replace each element with its $s$-domain equivalent
   - Include initial condition sources
   - Transform input sources using Laplace Transform tables

5. **Solve for the $s$-Domain Variable:** Solve the resulting algebraic equations for the variable of interest, $V(s)$ or $I(s)$, using circuit analysis techniques (nodal analysis, mesh analysis, voltage/current division, etc.).

6. **Separate into ZSR and ZIR (Superposition):** Use superposition to explicitly separate the total response $V(s)$ into $V_{\text{ZSR}}(s)$ and $V_{\text{ZIR}}(s)$.

7. **Inverse Transform:** Perform the Inverse LT on $V_{\text{ZSR}}(s)$ and $V_{\text{ZIR}}(s)$ separately using PFE and Laplace Transform tables to get $v_{\text{ZSR}}(t)$ and $v_{\text{ZIR}}(t)$.

8. **Calculate Total Response:** Combine the responses:
   $$v_{\text{total}}(t) = v_{\text{ZSR}}(t) + v_{\text{ZIR}}(t) \quad \text{for } t \ge 0$$

---

#### Detailed Process for ZIR/ZSR Separation (Superposition Method)

The separation of ZIR and ZSR is achieved by modeling the circuit elements in the $s$-domain and applying the superposition principle:

**Phase 1: Zero-State Response (ZSR) Calculation**

1. **Zero Initial Conditions:** In the $s$-domain equivalent circuit, set all initial condition sources to zero.
   - For a capacitor, remove (short-circuit) the $\frac{v_C(0)}{s}$ voltage source
   - For an inductor, remove (open-circuit) the $\frac{i_L(0)}{s}$ current source

2. **Keep External Sources:** Keep all external input sources ($V_s(s)$ or $I_s(s)$) active.

3. **Calculate $s$-Domain ZSR:** Analyze the circuit using standard techniques:
   - Nodal analysis (KCL at nodes)
   - Mesh analysis (KVL around loops)
   - Voltage/current division
   - Thévenin/Norton equivalents

4. **Result:** Obtain $V_{\text{ZSR}}(s)$ or $I_{\text{ZSR}}(s)$

5. **Inverse LT:** Find $v_{\text{ZSR}}(t)$ by applying the Inverse Laplace Transform to $V_{\text{ZSR}}(s)$ using PFE.

**Phase 2: Zero-Input Response (ZIR) Calculation**

1. **Zero External Sources:** Set all external input sources to zero:
   - Short-circuit voltage sources (replace with wire)
   - Open-circuit current sources (remove from circuit)

2. **Keep Initial Conditions:** Keep all initial condition sources active:
   - Capacitor: $\frac{v_C(0)}{s}$ voltage source in series with $\frac{1}{sC}$
   - Inductor: $\frac{i_L(0)}{s}$ current source in parallel with $sL$ (or equivalently, $Li_L(0)$ voltage source in series)

3. **Calculate $s$-Domain ZIR:** Analyze the resulting circuit to find the response $V_{\text{ZIR}}(s)$ (or $I_{\text{ZIR}}(s)$) due only to the initial conditions.

4. **Result:** Obtain $V_{\text{ZIR}}(s)$ or $I_{\text{ZIR}}(s)$

5. **Inverse LT:** Find $v_{\text{ZIR}}(t)$ by applying the Inverse Laplace Transform to $V_{\text{ZIR}}(s)$.

**Phase 3: Total Response**

1. **Sum in $s$-Domain:** 
   $$V_{\text{total}}(s) = V_{\text{ZSR}}(s) + V_{\text{ZIR}}(s)$$

2. **Sum in Time Domain:** 
   $$v_{\text{total}}(t) = v_{\text{ZSR}}(t) + v_{\text{ZIR}}(t) \quad \text{for } t \ge 0$$

---

### 4. Relevant Equations

The analysis of ZIR and ZSR occurs entirely within the framework of linear circuit analysis using the Laplace Transform.

#### Superposition Principle (Total Response)

$$\text{Total Response} = \text{Response due to Input Sources} + \text{Response due to Initial Conditions}$$

$$V_{\text{total}}(s) = V_{\text{ZSR}}(s) + V_{\text{ZIR}}(s)$$

$$v_{\text{total}}(t) = v_{\text{ZSR}}(t) + v_{\text{ZIR}}(t)$$

#### $s$-Domain Device Characteristics and Initial Conditions

| Device | Time Domain Relation | $s$-Domain Impedance | Initial Condition Model |
| :--- | :--- | :--- | :--- |
| **Resistor (R)** | $v_R(t) = R \cdot i_R(t)$ | $Z_R = R$ | None (no energy storage) |
| **Capacitor (C)** | $i_C(t) = C \frac{dv_C}{dt}$ | $Z_C = \frac{1}{sC}$ | Voltage source $\frac{v_C(0)}{s}$ in series |
| **Inductor (L)** | $v_L(t) = L \frac{di_L}{dt}$ | $Z_L = sL$ | Current source $\frac{i_L(0)}{s}$ in parallel (or voltage source $Li_L(0)$ in series) |

#### Capacitor $s$-Domain Model

A capacitor with initial voltage $v_C(0)$ is modeled as:

$$V_C(s) = \frac{1}{sC} I_C(s) + \frac{v_C(0)}{s}$$

Or equivalently, as an impedance $\frac{1}{sC}$ in series with a voltage source $\frac{v_C(0)}{s}$.

#### Inductor $s$-Domain Model

An inductor with initial current $i_L(0)$ is modeled as:

$$V_L(s) = sL \cdot I_L(s) - Li_L(0)$$

Or equivalently, as an impedance $sL$ in series with a voltage source $-Li_L(0)$ (or $+Li_L(0)$ with opposite polarity).

Alternatively, using current:

$$I_L(s) = \frac{V_L(s)}{sL} + \frac{i_L(0)}{s}$$

This represents an impedance $sL$ in parallel with a current source $\frac{i_L(0)}{s}$.

#### Laplace Transform Properties

**Differentiation Property:**

$$\mathcal{L}\left\{\frac{df(t)}{dt}\right\} = sF(s) - f(0)$$

**Integration Property:**

$$\mathcal{L}\left\{\int_0^t f(\tau)d\tau\right\} = \frac{F(s)}{s}$$

**Common Transform Pairs:**

| Time Domain $f(t)$ | Laplace Domain $F(s)$ | Condition |
| :--- | :--- | :--- |
| $\delta(t)$ (unit impulse) | $1$ | |
| $u(t)$ (unit step) | $\frac{1}{s}$ | |
| $e^{-at}u(t)$ | $\frac{1}{s+a}$ | $a > 0$ |
| $te^{-at}u(t)$ | $\frac{1}{(s+a)^2}$ | |
| $\sin(\omega t)u(t)$ | $\frac{\omega}{s^2 + \omega^2}$ | |
| $\cos(\omega t)u(t)$ | $\frac{s}{s^2 + \omega^2}$ | |

---

### 5. Partial Fraction Expansion (PFE)

To perform the inverse Laplace transform, we typically need to decompose $V(s)$ into simpler fractions using PFE.

#### General Form

For a rational function:

$$V(s) = \frac{N(s)}{D(s)} = \frac{b_ms^m + b_{m-1}s^{m-1} + \cdots + b_0}{a_ns^n + a_{n-1}s^{n-1} + \cdots + a_0}$$

where $m < n$ (proper fraction), we factor the denominator:

$$D(s) = a_n(s - p_1)(s - p_2)\cdots(s - p_n)$$

#### Distinct Real Poles

If all poles $p_1, p_2, \ldots, p_n$ are distinct:

$$V(s) = \frac{k_1}{s - p_1} + \frac{k_2}{s - p_2} + \cdots + \frac{k_n}{s - p_n}$$

**Cover-Up Method:** To find residue $k_i$:

$$k_i = \left[(s - p_i)V(s)\right]_{s=p_i}$$

#### Repeated Poles

If pole $p_1$ has multiplicity $r$:

$$V(s) = \frac{k_{1,r}}{(s - p_1)^r} + \frac{k_{1,r-1}}{(s - p_1)^{r-1}} + \cdots + \frac{k_{1,1}}{s - p_1} + \text{(other terms)}$$

**Residue Formulas:**

$$k_{1,r} = \left[(s - p_1)^r V(s)\right]_{s=p_1}$$

$$k_{1,j} = \frac{1}{(r-j)!} \frac{d^{r-j}}{ds^{r-j}}\left[(s - p_1)^r V(s)\right]_{s=p_1}$$

#### Complex Conjugate Poles

If poles are complex: $p = -\alpha \pm j\omega$

$$V(s) = \frac{k}{s - (-\alpha + j\omega)} + \frac{k^*}{s - (-\alpha - j\omega)} + \text{(other terms)}$$

The inverse transform yields:

$$v(t) = 2|k|e^{-\alpha t}\cos(\omega t + \angle k) + \text{(other terms)}$$

---

### 6. Worked Example: Series RC Circuit

Consider a series RC circuit with:
- Resistor: $R = 2\,\Omega$
- Capacitor: $C = 0.5\,\text{F}$
- Input: Step voltage $v_s(t) = 10u(t)\,\text{V}$
- Initial condition: $v_C(0) = 5\,\text{V}$

**Find:** The capacitor voltage $v_C(t)$ for $t \ge 0$, separating into ZIR and ZSR.

#### Step 1: $s$-Domain Circuit

Transform to $s$-domain:
- Input: $V_s(s) = \frac{10}{s}$
- Resistor: $R = 2\,\Omega$
- Capacitor: $Z_C = \frac{1}{sC} = \frac{1}{0.5s} = \frac{2}{s}$ with initial voltage source $\frac{v_C(0)}{s} = \frac{5}{s}$

#### Step 2: Total Response (Without Separation)

Using KVL around the loop:

$$V_s(s) = RI_C(s) + \frac{1}{sC}I_C(s) + \frac{v_C(0)}{s}$$

$$\frac{10}{s} = 2I_C(s) + \frac{2}{s}I_C(s) + \frac{5}{s}$$

$$\frac{10}{s} - \frac{5}{s} = I_C(s)\left(2 + \frac{2}{s}\right)$$

$$\frac{5}{s} = I_C(s)\frac{2s + 2}{s}$$

$$I_C(s) = \frac{5}{2s + 2} = \frac{5}{2(s + 1)} = \frac{2.5}{s + 1}$$

The capacitor voltage:

$$V_C(s) = \frac{1}{sC}I_C(s) + \frac{v_C(0)}{s} = \frac{2}{s} \cdot \frac{2.5}{s+1} + \frac{5}{s}$$

$$V_C(s) = \frac{5}{s(s+1)} + \frac{5}{s}$$

Using PFE on the first term:

$$\frac{5}{s(s+1)} = \frac{A}{s} + \frac{B}{s+1}$$

$$A = \left[s \cdot \frac{5}{s(s+1)}\right]_{s=0} = \frac{5}{1} = 5$$

$$B = \left[(s+1) \cdot \frac{5}{s(s+1)}\right]_{s=-1} = \frac{5}{-1} = -5$$

Therefore:

$$V_C(s) = \frac{5}{s} - \frac{5}{s+1} + \frac{5}{s} = \frac{10}{s} - \frac{5}{s+1}$$

Inverse transform:

$$v_C(t) = 10 - 5e^{-t} = 10 - 5e^{-t}\,\text{V} \quad \text{for } t \ge 0$$

#### Step 3: Zero-State Response (ZSR)

Set initial condition to zero: $v_C(0) = 0$

$$V_s(s) = RI_C(s) + \frac{1}{sC}I_C(s)$$

$$\frac{10}{s} = I_C(s)\left(2 + \frac{2}{s}\right) = I_C(s)\frac{2s + 2}{s}$$

$$I_C(s) = \frac{10}{2s + 2} = \frac{5}{s + 1}$$

$$V_{C,\text{ZSR}}(s) = \frac{2}{s} \cdot \frac{5}{s+1} = \frac{10}{s(s+1)}$$

Using PFE:

$$\frac{10}{s(s+1)} = \frac{10}{s} - \frac{10}{s+1}$$

Inverse transform:

$$v_{C,\text{ZSR}}(t) = 10 - 10e^{-t}\,\text{V} \quad \text{for } t \ge 0$$

#### Step 4: Zero-Input Response (ZIR)

Set input to zero: $V_s(s) = 0$ (short circuit), keep initial condition $v_C(0) = 5\,\text{V}$

$$0 = RI_C(s) + \frac{1}{sC}I_C(s) + \frac{v_C(0)}{s}$$

$$-\frac{5}{s} = I_C(s)\frac{2s + 2}{s}$$

$$I_C(s) = -\frac{5}{2(s+1)}$$

$$V_{C,\text{ZIR}}(s) = \frac{2}{s} \cdot \left(-\frac{5}{2(s+1)}\right) + \frac{5}{s} = -\frac{5}{s(s+1)} + \frac{5}{s}$$

$$V_{C,\text{ZIR}}(s) = -\frac{5}{s} + \frac{5}{s+1} + \frac{5}{s} = \frac{5}{s+1}$$

Inverse transform:

$$v_{C,\text{ZIR}}(t) = 5e^{-t}\,\text{V} \quad \text{for } t \ge 0$$

#### Step 5: Verify Total Response

$$v_C(t) = v_{C,\text{ZSR}}(t) + v_{C,\text{ZIR}}(t) = (10 - 10e^{-t}) + 5e^{-t} = 10 - 5e^{-t}\,\text{V}$$

✓ Matches the total response calculated earlier!

#### Physical Interpretation

- **ZIR:** The capacitor initially at $5\,\text{V}$ discharges exponentially toward $0\,\text{V}$ with time constant $\tau = RC = 1\,\text{s}$
- **ZSR:** Starting from $0\,\text{V}$, the capacitor charges toward the input voltage $10\,\text{V}$ with the same time constant
- **Total:** The capacitor voltage transitions from $5\,\text{V}$ to $10\,\text{V}$ exponentially

---

### 7. Key Insights and Common Mistakes

#### Key Insights

1. **Natural vs. Forced Response:**
   - ZIR contains only the natural response (exponential decay based on circuit poles)
   - ZSR contains both natural and forced responses

2. **Time Constants:**
   - Both ZIR and ZSR exhibit the same time constants (determined by circuit poles)
   - The difference is in the coefficients and the presence of forced response in ZSR

3. **Energy Considerations:**
   - ZIR represents the release of initially stored energy
   - ZSR represents energy delivered by the input source

4. **Superposition Validity:**
   - Only valid for linear circuits
   - Cannot be applied to circuits with nonlinear elements

#### Common Mistakes

1. **Forgetting initial condition sources** when calculating ZIR
2. **Not zeroing initial conditions** when calculating ZSR
3. **Incorrect $s$-domain models** for capacitors and inductors
4. **Sign errors** in initial condition sources
5. **Not verifying** that ZIR + ZSR equals total response
6. **Confusing natural response with ZIR** (ZSR also has a natural component!)

---

### 8. Summary Table

| Aspect | ZIR | ZSR |
| :--- | :--- | :--- |
| **Cause** | Initial conditions only | Input sources only |
| **Initial Conditions** | $v_C(0) \neq 0$, $i_L(0) \neq 0$ | $v_C(0) = 0$, $i_L(0) = 0$ |
| **Input Sources** | Set to zero (short/open) | Active |
| **Response Type** | Pure natural response | Natural + forced response |
| **Physical Meaning** | Energy relaxation | System response to excitation |
| **Time Constant** | Determined by $R$, $L$, $C$ | Same as ZIR |

---

### 9. Practice Problems

#### Problem 1: Series RL Circuit

A series RL circuit has $R = 4\,\Omega$, $L = 2\,\text{H}$, input $v_s(t) = 12u(t)\,\text{V}$, and $i_L(0) = 1\,\text{A}$.

Find $i_L(t)$ for $t \ge 0$, separating into ZIR and ZSR.

**Hint:** Time constant $\tau = \frac{L}{R}$

#### Problem 2: Parallel RC Circuit

A parallel RC circuit has $R = 5\,\Omega$, $C = 0.2\,\text{F}$, input current $i_s(t) = 2u(t)\,\text{A}$, and $v_C(0) = 3\,\text{V}$.

Find $v_C(t)$ for $t \ge 0$, separating into ZIR and ZSR.

**Hint:** For parallel RC, $\tau = RC$

---

### References and Further Reading

- **Laplace Transform Tables:** Essential for inverse transforms
- **Circuit Analysis Textbooks:** Alexander & Sadiku, Nilsson & Riedel
- **Control Systems:** Understanding poles and zeros
- **Differential Equations:** Foundation for circuit dynamics