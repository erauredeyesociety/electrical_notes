This documentation provides a comprehensive explanation of the Zero-Input Response (ZIR) and Zero-State Response (ZSR), drawing upon circuit theory concepts solved using the Laplace Transform (LT) methodology.

---

## Comprehensive Documentation: Zero-Input Response (ZIR) and Zero-State Response (ZSR)

The **total response** of a linear circuit can be separated into two fundamental components: the **zero-state response (ZSR)** and the **zero-input response (ZIR)**. This separation is possible because the effect of the initial state can be isolated.

$$\text{Total Response} = \text{Zero-State Response (ZSR)} + \text{Zero-Input Response (ZIR)} \quad \text{}$$

### 1. Theory Background: ZIR and ZSR

#### Zero-Input Response (ZIR)

The Zero-Input Response (ZIR) is the behavior of the circuit **due solely to the initial conditions** of energy storage elements (like capacitors or inductors), assuming no external input sources are active.

*   **Definition:** ZIR is the response due to the initial voltage (or current). It is calculated as if there were **zero input**.
*   **Circuit State:** To calculate ZIR, the input source ($V_s$ or $I_s$) of the circuit is set to zero. For a specific example, if the voltage source $V=0$ (shut circuit) for $t > 0$, the final response is the zero-input response (ZIR).
*   **Nature:** ZIR is the behavior due to **device characteristics** (R, C, L values) and is not related to any external sources. Consequently, **all ZIRs are natural responses**. The poles determining the natural characteristics are due to the values of R, C, and L.

#### Zero-State Response (ZSR)

The Zero-State Response (ZSR) is the behavior of the circuit due solely to the external input sources, assuming all initial energy storage in the circuit is zero.

*   **Definition:** ZSR is the response due to the input, or charging/discharging of a capacitor, assuming a **zero initial state voltage**. ZSR is the response due to the integral term.
*   **Circuit State:** To calculate ZSR, the initial state of the capacitor (or inductor) is set to zero.
*   **Response Origin:** ZSR is the voltage on a capacitor if $V_c = 0$ at $t = 0$, meaning the response is entirely derived from the input or charging/discharging.

### 2. Relevant Topics to Understand

Understanding ZIR and ZSR primarily requires the application of the Laplace Transform (LT) to circuit analysis, specifically in the $s$-domain.

| Relevant Topic | Subtopics and Importance | Source(s) |
| :--- | :--- | :--- |
| **Laplace Transform (LT) and $s$-Domain** | LT converts circuits from the time domain to the phase ($s$) domain, transforming differential equations into linear equations that are easier to solve. The Inverse LT converts the expression back to the time domain. | |
| **LT Properties** | Properties like **differentiation** (Property 4) and **integration** (Property 5) are crucial for transforming differential equations involving inductors and capacitors, respectively. | |
| **$s$-Domain Device Characteristics** | Resistors become impedance $R$. Capacitors (C) and Inductors (L) are modeled in the $s$-domain as an impedance plus an initial condition term. | |
| **Modeling Initial Conditions** | Initial conditions (energy stored at $t=0$) are converted into equivalent sources in the $s$-domain. For a capacitor, the initial voltage $v(0)$ is modeled by an $s$-domain voltage source $V_c(0)/s$. For an inductor, current response is typically used. | |
| **Inverse LT Techniques** | Once the response in the $s$-domain ($V(s)$ or $I(s)$) is found, the Inverse LT is performed, often requiring **Partial Fraction Expansion (PFE)** and the **cover-up method** to find residues ($k_i$). | |
| **Network Function** | The partial fraction derived from the circuit is known as the network function $H(s)$. The roots of the denominator of $H(s)$ define the system poles. | |

### 3. Step-by-Step Methods and Processes

Solving problems involving ZIR and ZSR typically involves applying the principle of superposition within the $s$-domain.

#### Step-by-Step Method (General Circuit Analysis using LT)

The process of solving circuits using LT, including finding the total response, generally follows these steps:

1.  **Derive the Differential Equation:** Develop the differential equation(s) that describe the circuit in the time domain, usually by applying KVL or KCL.
2.  **Analyze for $t<0$ (Initial Conditions):** Use circuit knowledge, physical insight, or classical techniques to find the required output variables (voltages, currents) for $t < 0$, particularly $v_c(0)$ or $i_L(0)$.
3.  **Transform to $s$-Domain:** For $t \ge 0$, transform the differential equation into the $s$-domain using the Laplace Transform, utilizing the differentiation property to incorporate initial conditions.
4.  **Solve for the $s$-Domain Variable:** Solve the resulting linear algebraic equation for the variable of interest, $V(s)$ or $I(s)$.
5.  **Separate into ZSR and ZIR (Superposition):** Use superposition to explicitly separate the total response $V(s)$ into $V_{ZSR}(s)$ and $V_{ZIR}(s)$.
6.  **Inverse Transform:** Perform the Inverse LT on $V_{ZSR}(s)$ and $V_{ZIR}(s)$ separately to get $v_{ZSR}(t)$ and $v_{ZIR}(t)$. The PFE/cover-up method is typically used here.
7.  **Calculate Total Response:** Combine $v_{ZSR}(t)$ and $v_{ZIR}(t)$ for the complete solution for $t \ge 0$.

#### Detailed Process for ZIR/ZSR Separation (Superposition Method)

The separation of ZIR and ZSR is achieved by modeling the circuit elements in the $s$-domain and applying the superposition principle:

**Phase 1: Zero-State Response (ZSR) Calculation**

1.  **Zero Initial Conditions:** In the $s$-domain equivalent circuit, set all initial condition sources to zero.
    *   For a capacitor, zero the $V_c(0)/s$ source.
    *   For an inductor, zero the $I_L(0)/s$ source (implied).
2.  **Keep External Sources:** Keep all external input sources ($V_s(s)$ or $I_s(s)$) active.
3.  **Calculate $s$-Domain ZSR:** Analyze the circuit (e.g., using KCL/node method) to find the response $V_{ZSR}(s)$ (or $I_{ZSR}(s)$) due to $V_s(s)$.
4.  **Inverse LT:** Find $v_{ZSR}(t)$ by applying the Inverse Laplace Transform to $V_{ZSR}(s)$.

**Phase 2: Zero-Input Response (ZIR) Calculation**

1.  **Zero External Sources:** Set all external input sources to zero (i.e., short-circuit voltage sources, open-circuit current sources).
2.  **Keep Initial Conditions:** Keep all initial condition sources ($V_c(0)/s$, $I_L(0)/s$) active.
3.  **Calculate $s$-Domain ZIR:** Analyze the resulting circuit to find the response $V_{ZIR}(s)$ (or $I_{ZIR}(s)$) due only to the initial conditions.
    *   *Note:* The analysis may involve calculating the current from the initial inductor condition.
4.  **Inverse LT:** Find $v_{ZIR}(t)$ by applying the Inverse Laplace Transform to $V_{ZIR}(s)$.

**Phase 3: Total Response**

1.  **Sum Responses:** The total response in the $s$-domain is $V_{total}(s) = V_{ZSR}(s) + V_{ZIR}(s)$.
2.  **Total Time Domain Response:** The total response in the time domain is $v_{total}(t) = v_{ZSR}(t) + v_{ZIR}(t)$.

### 4. Relevant Equations

The analysis of ZIR and ZSR occurs entirely within the framework of linear circuit analysis using the Laplace Transform.

#### Superposition Principle (Total Response)

$$\text{Total Response} = \text{Response due to Input Sources} + \text{Response due to Initial Conditions} \quad \text{}$$

$$V_{total}(s) = V_{ZSR}(s) + V_{ZIR}(s) \quad \text{}$$

$$v_{total}(t) = v_{ZSR}(t) + v_{ZIR}(t) \quad \text{}$$

#### $s$-Domain Device Characteristics and Initial Conditions

| Device | Time Domain (Example) | $s$-Domain Impedance ($Z$) | Initial Condition Model (Source) | Source(s) |
| :--- | :--- | :--- | :--- | :--- |
| **Resistor (R)** | $R$ | $R$ | None | |
| **Capacitor (C)** | $v_C(t) = \frac{1}{C} \int i_C(\tau) d\tau$ | $Z_C = \frac{1}{sC}$ | Voltage source: $\frac{v_C(0)}{s}$ | |
| **Inductor (L)** | $v_L(t) = L \frac{di_L}{dt}$ | $Z_L$ (implied $sL$) | Current source (implied) or Voltage source | |

In the $s$-domain, the capacitor is equivalent to an impedance $Z_C$ plus its initial voltage effect.

#### Laplace Transform Property (Differentiation)

This property is key for transforming the time-domain differential equation into the $s$-domain, inherently separating the initial condition ($f(0)$) term:

$$\mathcal{L}\left\{\frac{d f(t)}{d t}\right\}=s F(s)-f(0) \quad \text{}$$