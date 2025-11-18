please help fill in the gaps to explain the problem solving processes for each mentioned topic... I have uploaded sample homework files for you to understand the skills required to pass the exam. I don't want example problems. just complete problem solving processes and checklists with relevant equations.


I'll analyze the homework problems to identify gaps in the problem-solving processes and fill them in. Let me search for any additional context on specific topics that might need clarification.Now I'll compile comprehensive additions and clarifications to fill gaps in the problem-solving processes:

---

## EXPANDED PROBLEM-SOLVING PROCESSES AND CHECKLISTS

Based on the homework problems, here are the critical gaps filled in:

---

### 9. Op-Amp Circuit Analysis (All Previous Skills with Op-Amps)

**High-Level Theory:**
Op-Amps in ideal operation satisfy two golden rules: (1) No current flows into either input terminal ($i_+ = i_- = 0$), and (2) The voltage difference between inputs is zero when in negative feedback ($V_+ = V_-$). Op-Amps enable high input impedance, low output impedance, and isolation between cascaded stages (buffering).

**Common Op-Amp Configurations:**

*   **Inverting Amplifier:** $H(s) = -Z_f(s)/Z_{in}(s)$ where $Z_f$ is feedback impedance and $Z_{in}$ is input impedance.
*   **Non-Inverting Amplifier:** $H(s) = 1 + Z_f(s)/Z_g(s)$ where $Z_g$ is ground impedance.
*   **Voltage Follower (Buffer):** $H(s) = 1$ (unity gain, $\mu = 1$).

**Process: Analyze Op-Amp Circuit for H(s)**

1.  **Apply Ideal Op-Amp Assumptions:** Set $i_+ = i_- = 0$ and $V_+ = V_-$ (for negative feedback).
2.  **Label Node Voltages:** Identify critical nodes (e.g., $V_+$, $V_-$, intermediate nodes).
3.  **Write KCL at Key Nodes:** Write current balance equations at the inverting input, non-inverting input, and any intermediate nodes.
4.  **Express Impedances:** Replace R, L, C with their S-domain impedances ($R$, $sL$, $1/sC$).
5.  **Solve for Output/Input Ratio:** Algebraically manipulate to find $H(s) = V_{out}(s)/V_{in}(s)$.
6.  **Identify Gain Factor:** For non-inverting configurations, calculate $\mu = 1 + R_B/R_A$ (or similar ratio).

| Check List | Theory / Equations |
| :--- | :--- |
| Ideal Op-Amp Rules | $i_+ = i_- = 0$; $V_+ = V_-$ (negative feedback). |
| Inverting Config | $H(s) = -Z_f/Z_{in}$. |
| Non-Inverting Config | $H(s) = 1 + Z_f/Z_g$; $\mu = 1 + R_B/R_A$. |
| Buffer | $H(s) = 1$ (unity gain). |

---

### 10. Frequency Response and Bode Plots

**High-Level Theory:**
The frequency response $H(j\omega)$ describes how a circuit responds to sinusoids of different frequencies. A Bode plot displays magnitude $|H(j\omega)|$ (in dB) and phase $\angle H(j\omega)$ (in degrees) versus frequency $\omega$ (typically on a log scale).

**Filter Classifications:**
*   **Low-Pass:** Passes low frequencies, attenuates high frequencies.
*   **High-Pass:** Passes high frequencies, attenuates low frequencies.
*   **Band-Pass:** Passes a specific frequency band.
*   **Band-Stop (Notch):** Attenuates a specific frequency band.

**Process: Create/Interpret Bode Plot from H(s)**

1.  **Substitute $s = j\omega$:** Convert $H(s)$ to $H(j\omega)$.
2.  **Calculate Magnitude:** $|H(j\omega)| = \sqrt{[\text{Re}(H)]^2 + [\text{Im}(H)]^2}$.
3.  **Convert to dB:** $20\log_{10}|H(j\omega)|$ dB.
4.  **Calculate Phase:** $\angle H(j\omega) = \arctan[\text{Im}(H)/\text{Re}(H)]$.
5.  **Plot vs Frequency:** Plot magnitude (dB) and phase (degrees) on semi-log axes.

**Process: Extract Parameters from Bode Plot**

1.  **Identify DC Gain:** Read magnitude at $\omega \to 0$ (low frequency asymptote). This gives $K$ or $|H(j0)|$.
2.  **Identify Corner/Cutoff Frequency ($\alpha$ or $\omega_c$):** 
    *   For first-order low-pass: $\alpha$ occurs where $|H(j\omega)| = |H(j0)|/\sqrt{2}$ (–3 dB point).
    *   For first-order high-pass: $\alpha$ occurs where phase $= 45°$.
3.  **Verify Roll-off Rate:** 
    *   First-order: \pm20 dB/decade.
    *   Second-order: \pm40 dB/decade.

**Process: Design Circuit for Specified Frequency Response**

1.  **Determine Filter Type:** Based on requirements (low-pass, high-pass, etc.).
2.  **Choose Filter Order:** First-order for simple response, second-order for sharper roll-off.
3.  **Select Topology:** 
    *   Passive (R-C divider) if no gain needed.
    *   Active (Op-Amp based) if gain or buffering needed.
4.  **Apply Design Equations:** Use canonical forms (see below).
5.  **Select Component Values:** Choose standard values that satisfy design equations.

| Check List | Theory / Equations |
| :--- | :--- |
| Frequency Substitution | $s = j\omega$. |
| Magnitude (dB) | $20\log_{10}|H(j\omega)|$ dB. |
| Phase | $\angle H(j\omega) = \arctan[\text{Im}/\text{Re}]$. |
| Cutoff Frequency | $|H(j\omega_c)| = |H(j0)|/\sqrt{2}$ (–3 dB point). |
| First-Order Low-Pass | $H(s) = K\alpha/(s+\alpha)$; $\omega_c = \alpha$. |
| First-Order High-Pass | $H(s) = Ks/(s+\alpha)$; $\omega_c = \alpha$. |

---

### 11. Sallen-Key Filter Design (Second-Order Active Filters)

**High-Level Theory:**
The Sallen-Key topology uses a voltage-controlled voltage-source configuration to implement second-order active filters, valued for simplicity. The circuit uses two resistors, two capacitors, and an Op-Amp. The general form of a second-order transfer function is:

$$H(s) = \frac{\mu \omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$ (Low-Pass)

$$H(s) = \frac{\mu s^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$ (High-Pass)

Where:
*   $\omega_0$ = undamped natural frequency (cutoff frequency)
*   $\zeta$ = damping ratio
*   $\mu$ = DC gain (or high-frequency gain for high-pass)
*   $Q = 1/(2\zeta)$ = quality factor

**Design Methods:**

**Method 1: Equal Elements ($R_1 = R_2 = R$, $C_1 = C_2 = C$)**
*   **Constraint:** Only works for $0 < \zeta < 1$ (underdamped, $Q > 0.5$).
*   **Gain Required:** $\mu = 3 - 1/Q = 3 - 2\zeta$.
*   **Design Equations:**
    *   Choose $C$ (standard value).
    *   Calculate $R = 1/(\omega_0 C)$.
    *   Calculate $R_A$ and $R_B$ for Op-Amp gain: $\mu = 1 + R_B/R_A$.

**Method 2: Unity Gain ($\mu = 1$, Buffer)**
*   **Advantage:** Works for all $\zeta$ (including $\zeta \geq 1$, overdamped).
*   **Design Equations (Low-Pass):**
    *   Choose $C_1$ (standard value).
    *   Calculate $C_2 = \zeta^2 C_1$.
    *   Calculate $R_1 = R_2 = R = 1/(\zeta\omega_0 C_1)$.
    *   Op-Amp configured as buffer ($R_A = \infty$, $R_B = 0$, or direct connection).

**Method 3: $m$-$n$ Ratio Method (General)**
*   Set $R_1 = mR$, $R_2 = R/m$, $C_1 = nC$, $C_2 = C/n$.
*   **Design Equations:**
    *   $\omega_0 = 1/(RC)$.
    *   $Q = \sqrt{mn}/(m + 1 - \mu)$ or $\zeta = (m + 1 - \mu)/(2\sqrt{mn})$.
    *   Choose $m$, $n$, and $\mu$ to satisfy $Q$ or $\zeta$ requirements.
    *   Calculate component values.

**Process: Design Sallen-Key Filter Given $H(s)$**

1.  **Identify Filter Parameters:** From $H(s)$, extract $\omega_0$, $\zeta$ (or $Q$), and gain $\mu$.
2.  **Choose Design Method:** 
    *   Equal elements if $Q > 0.5$ and gain $\mu > 1$ is acceptable.
    *   Unity gain if $Q \leq 0.5$ or buffer is desired.
    *   $m$-$n$ ratio for general cases.
3.  **Select Base Component Value:** Choose $C$ or $R$ from standard values (e.g., $C = 0.01~\mu\text{F}$, $R = 10~\text{k}\Omega$).
4.  **Calculate Remaining Components:** Use design equations for chosen method.
5.  **Configure Op-Amp Gain:** Calculate $R_A$ and $R_B$ using $\mu = 1 + R_B/R_A$.
6.  **Apply Scaling (if needed):**
    *   **Frequency Scaling:** Multiply all C values by $k_f$, or divide all R values by $k_f$.
    *   **Impedance Scaling:** Multiply all R values by $k_z$, divide all C values by $k_z$.

**Process: Verify Sallen-Key Circuit Realizes Given $H(s)$**

1.  **Label Nodes:** Identify $V_{in}$, $V_+$ (non-inverting input), intermediate node $V_x$, and $V_{out}$.
2.  **Apply Op-Amp Rule:** $V_{out} = \mu V_+$ where $\mu = 1 + R_B/R_A$.
3.  **Write KCL at $V_x$:** $(V_{in} - V_x)/Z_1 = (V_x - V_{out})/Z_4 + (V_x - V_+)/Z_2$.
4.  **Write KCL at $V_+$:** $(V_x - V_+)/Z_2 = V_+/Z_3$.
5.  **Solve for $H(s)$:** Eliminate intermediate variables to find $H(s) = V_{out}/V_{in}$.
6.  **Compare:** Verify the resulting $H(s)$ matches the given transfer function.

| Check List | Theory / Equations |
| :--- | :--- |
| Second-Order Form | $H(s) = \mu\omega_0^2/(s^2 + 2\zeta\omega_0 s + \omega_0^2)$ (LP). |
| Quality Factor | $Q = 1/(2\zeta)$. |
| Equal Elements Gain | $\mu = 3 - 2\zeta = 3 - 1/Q$. |
| Unity Gain Design | $R_1 = R_2 = 1/(\zeta\omega_0 C_1)$; $C_2 = \zeta^2 C_1$. |
| Frequency Scaling | Divide all C by $k_f$ (or multiply all R by $k_f^{-1}$). |
| Impedance Scaling | Multiply all R by $k_z$, divide all C by $k_z$. |
| Op-Amp Gain | $\mu = 1 + R_B/R_A$. |

---

### 12. Cascade Design (High-Order Filters)

**High-Level Theory:**
Complex high-order transfer functions $H(s)$ can be decomposed into a product of first- and second-order sections. Each section is implemented separately, then cascaded using Op-Amp buffers to prevent loading effects. The overall transfer function is the product of individual sections:

$$H(s) = H_1(s) \cdot H_2(s) \cdot H_3(s) \cdots$$

**Process: Design Cascaded Filter for High-Order $H(s)$**

1.  **Factor $H(s)$:** Decompose $H(s)$ into first-order and second-order sections.
    *   Real poles → first-order sections.
    *   Complex conjugate pole pairs → second-order sections.
2.  **Design Each Section:** Use appropriate topology for each section:
    *   First-order: Simple R-C with Op-Amp (inverting or non-inverting).
    *   Second-order: Sallen-Key circuit.
3.  **Order Sections:** Place low-$Q$ sections first, high-$Q$ sections last (minimizes sensitivity).
4.  **Connect with Buffers:** Use Op-Amp buffers (voltage followers) between sections to isolate stages.
5.  **Verify Overall $H(s)$:** Multiply individual $H_i(s)$ to confirm overall response.

**Process: Evaluate Cascade Loading Effects**

1.  **Check Source Impedance:** If input comes from a source with non-zero impedance $R_s$, this forms a voltage divider with the first stage's input impedance.
    *   **Passive circuits:** Input impedance affects $H(s)$.
    *   **Active circuits (Op-Amp input):** High input impedance minimizes loading.
2.  **Check Load Impedance:** If output drives a load $R_L$, this forms a voltage divider with the output impedance.
    *   **Passive circuits:** Output impedance affects $H(s)$ under load.
    *   **Active circuits (Op-Amp output):** Low output impedance minimizes loading effects.
3.  **Recommendation:** Use Op-Amp-based (active) circuits when source or load impedances are unknown or variable.

| Check List | Theory / Equations |
| :--- | :--- |
| Cascade Rule | $H(s) = H_1(s) \cdot H_2(s) \cdots$ (requires isolation). |
| Buffer Between Stages | Use voltage follower ($\mu = 1$) to prevent loading. |
| Source Loading | $V_{in,actual} = V_{source} \cdot Z_{in}/(Z_{in} + Z_s)$. |
| Load Loading | $V_{out,actual} = V_{out} \cdot R_L/(R_L + Z_{out})$. |

---

### 13. Passive Filter Design (R, L, C Only)

**High-Level Theory:**
Passive filters use only resistors, inductors, and capacitors without amplification. They are limited in gain (always $\leq 1$) and are susceptible to loading effects. However, they are simple, inexpensive, and do not require power.

**Process: Design Passive Filter for Given $H(s)$**

1.  **Normalize $H(s)$:** Factor out $s$ from numerator and denominator to form impedance ratios.
2.  **Identify Topology:** 
    *   **Voltage Divider:** $H(s) = Z_2/(Z_1 + Z_2)$.
    *   **Series R-L-C:** Multiple impedances in series/parallel.
3.  **Assign Impedances:**
    *   Constant term → Resistor $R$.
    *   Term with $s$ → Inductor $sL$ (inductance $L$).
    *   Term with $1/s$ → Capacitor $1/(sC)$ (capacitance $C$).
4.  **Solve for Component Values:** Match coefficients in $H(s)$ to impedance expressions.
5.  **Avoid Inductors if Possible:** Prefer capacitors over inductors (inductors are bulky and expensive).

**Example Impedance Mappings:**
*   $200s \to$ Inductor with $L = 200$ H.
*   $10^6/s \to$ Capacitor with $1/C = 10^6$, so $C = 1~\mu\text{F}$.
*   $s^2 \to$ Two inductors in series, or single inductor with equivalent $L$.

| Check List | Theory / Equations |
| :--- | :--- |
| Voltage Divider | $H(s) = Z_2/(Z_1 + Z_2)$. |
| Impedances | $Z_R = R$; $Z_L = sL$; $Z_C = 1/(sC)$. |
| Passive Gain Limit | $|H(j\omega)| \leq 1$ (no amplification). |
| Loading Sensitivity | Performance changes with source/load impedances. |

---

### 14. Design from Time-Domain Response (Step or Impulse)

**High-Level Theory:**
Given a desired time-domain response $v_{out}(t)$ to a specific input (step or impulse), work backwards to find $H(s)$, then design a circuit to realize it.

**Process: Design Circuit from Step Response**

1.  **Take Laplace Transform:** $V_{out}(s) = \mathcal{L}\{v_{out}(t)\}$.
2.  **Find $H(s)$:** For step input, $V_{in}(s) = 1/s$, so $H(s) = V_{out}(s) \cdot s$.
3.  **Identify Poles and Zeros:** Factor $H(s) = N(s)/D(s)$.
4.  **Choose Topology:** Select circuit type (passive, active, cascade) based on $H(s)$ complexity.
5.  **Design Circuit:** Apply design methods (voltage divider, Op-Amp, Sallen-Key, etc.).
6.  **Verify:** Inverse transform $H(s)/s$ to confirm step response matches $v_{out}(t)$.

**Process: Design Circuit from Impulse Response**

1.  **Take Laplace Transform:** $H(s) = \mathcal{L}\{h(t)\}$ (impulse response is $H(s)$ directly).
2.  **Proceed as above:** Identify poles/zeros, choose topology, design circuit.

**Special Case: Multiple Poles (Repeated Roots)**
*   If $H(s)$ has a pole of order $n$ at $s = p$, the time-domain response includes terms like $t^{k}e^{pt}$ for $k = 0, 1, \ldots, n-1$.
*   Example: $(s+50)^{-2}$ in $H(s)$ produces $te^{-50t}$ in time domain.

| Check List | Theory / Equations |
| :--- | :--- |
| Step Input | $V_{in}(s) = 1/s$; $H(s) = V_{out}(s) \cdot s$. |
| Impulse Input | $V_{in}(s) = 1$; $H(s) = V_{out}(s)$. |
| Multiple Poles | $\mathcal{L}^{-1}\{1/(s-p)^n\} = t^{n-1}e^{pt}/(n-1)!$. |
| Design Verification | Check $\mathcal{L}^{-1}\{H(s) \cdot V_{in}(s)\} = v_{out}(t)$. |

---

### 15. Component Scaling

**High-Level Theory:**
Component values can be scaled to achieve practical, standard values without changing the transfer function $H(s)$.

**Frequency Scaling:** Changes the frequency response (shifts cutoff frequencies).
*   **Rule:** Divide all capacitors by $k_f$ (or multiply all inductors by $k_f^{-1}$).
*   **Effect:** All frequencies (poles, zeros, $\omega_0$) are multiplied by $k_f$.

**Impedance Scaling:** Changes component values without affecting frequency response.
*   **Rule:** Multiply all resistors by $k_z$, divide all capacitors by $k_z$, multiply all inductors by $k_z$.
*   **Effect:** $H(s)$ and all frequencies remain unchanged.

**Process: Scale Circuit to Standard Values**

1.  **Design Prototype:** Create initial design with any component values that satisfy $H(s)$.
2.  **Apply Frequency Scaling (if needed):** To shift frequency response, calculate $k_f = \omega_{desired}/\omega_{prototype}$.
    *   Divide all C by $k_f$.
    *   Divide all L by $k_f$ (or multiply R by $k_f$ if using R-C only).
3.  **Apply Impedance Scaling:** To achieve standard values (e.g., all C = $0.01~\mu$F), calculate $k_z = C_{desired}/C_{prototype}$.
    *   Multiply all R by $k_z$.
    *   Divide all C by $k_z$.
    *   Multiply all L by $k_z$.
4.  **Round to Standard Values:** Select nearest E12, E24, or E96 series values.

| Check List | Theory / Equations |
| :--- | :--- |
| Frequency Scaling | $C_{new} = C/k_f$; $L_{new} = L/k_f$; $\omega_{new} = k_f \omega$. |
| Impedance Scaling | $R_{new} = k_z R$; $C_{new} = C/k_z$; $L_{new} = k_z L$. |
| Standard Series | E12 (10% tolerance), E24 (5%), E96 (1%). |

---

### 16. Poles, Zeros, and Time-Domain Behavior

**High-Level Theory:**
The location of poles and zeros in the S-plane directly determines the circuit's time-domain behavior.

**Pole Locations and Natural Response:**
*   **Real Negative Pole ($p = -\alpha$, $\alpha > 0$):** Exponential decay $e^{-\alpha t}$.
    *   Larger $|\alpha|$ → Faster decay.
*   **Real Positive Pole ($p = +\alpha$):** Exponential growth $e^{\alpha t}$ (unstable).
*   **Complex Conjugate Poles ($p = -\zeta\omega_0 \pm j\omega_d$):** Damped sinusoid $e^{-\zeta\omega_0 t}\cos(\omega_d t + \phi)$.
    *   $\zeta > 0$ → Decaying oscillation (stable).
    *   $\zeta < 0$ → Growing oscillation (unstable).
    *   $\zeta = 0$ → Sustained oscillation (marginally stable).
*   **Poles on Imaginary Axis ($p = \pm j\omega_0$):** Pure sinusoid $\cos(\omega_0 t)$ (marginally stable).
*   **Multiple Poles:** Include polynomial terms $t^k e^{pt}$.

**Zero Locations and Forced Response:**
*   **Zero at $s = z_0$:** Input signal $e^{z_0 t}$ will not appear in output (blocked/filtered).
*   **Zero at Origin ($s = 0$):** DC signals (constant inputs) are blocked (high-pass behavior).
*   **Zero at Infinity:** High-frequency signals are blocked (low-pass behavior).

**Process: Predict Time-Domain Behavior from Pole-Zero Plot**

1.  **Locate Poles:** Identify all poles of $H(s)$ in S-plane.
2.  **Determine Stability:** 
    *   All poles in left half-plane (LHP) → Stable.
    *   Any pole in right half-plane (RHP) → Unstable.
    *   Poles on imaginary axis → Marginally stable.
3.  **Predict Natural Response Form:**
    *   Real poles → Exponentials.
    *   Complex poles → Damped sinusoids.
4.  **Identify Dominant Poles:** Poles closest to imaginary axis dominate long-term behavior.
5.  **Estimate Time Constants:** For real pole at $p = -\alpha$, time constant $\tau = 1/\alpha$.

| Check List | Theory / Equations |
| :--- | :--- |
| Stability Criterion | All poles in LHP ($\text{Re}(p) < 0$) for stability. |
| Real Pole Response | $\mathcal{L}^{-1}\{1/(s-p)\} = e^{pt}$. |
| Complex Pole Response | $\mathcal{L}^{-1}\{(s-a)/[(s-a)^2+\omega^2]\} = e^{at}\cos(\omega t)$. |
| Time Constant | $\tau = 1/|\text{Re}(p)|$ for dominant pole. |
| Settling Time | $t_s \approx 4\tau$ (to within 2% of final value). |

---

### 17. Working with Bode Plots for Design

**Process: Design First-Order Filter from Bode Plot Specifications**

1.  **Read DC Gain (Low-Frequency):** For low-pass, read $|H(j0)|$ from low-frequency asymptote. For high-pass, read $|H(j\infty)|$ from high-frequency asymptote. Convert from dB: $K = 10^{(\text{dB}/20)}$.
2.  **Identify Cutoff Frequency:** Find frequency where magnitude drops by 3 dB from passband (or where phase = \pm45°). This is $\alpha$ or $\omega_c$.
3.  **Determine Phase Shift:** Read phase at frequency of interest from phase plot.
4.  **Write $H(s)$:**
    *   Low-pass: $H(s) = K\alpha/(s + \alpha)$.
    *   High-pass: $H(s) = Ks/(s + \alpha)$.
5.  **Design Circuit:** Choose topology (passive or active), then calculate component values.

**Process: Calculate Output from Input Using Bode Plot**

1.  **Identify Input Frequency:** Extract $\omega$ from input signal $v_{in}(t) = A\cos(\omega t + \theta)$.
2.  **Read Gain at $\omega$:** From magnitude plot, read $|H(j\omega)|$ in dB. Convert: $|H(j\omega)| = 10^{(\text{dB}/20)}$.
3.  **Read Phase at $\omega$:** From phase plot, read $\angle H(j\omega)$ in degrees.
4.  **Calculate Output:** $v_{out}(t) = A \cdot |H(j\omega)| \cos(\omega t + \theta + \angle H(j\omega))$.

| Check List | Theory / Equations |
| :--- | :--- |
| dB to Linear | $|H| = 10^{(\text{dB}/20)}$. |
| Linear to dB | $\text{dB} = 20\log_{10}|H|$. |
| –3 dB Point | $|H(j\omega_c)| = |H_{max}|/\sqrt{2}$ (cutoff frequency). |
| Phase at Cutoff | $\angle H(j\alpha) = \pm 45°$ (first-order). |

---

### 18. Standard Values and Realizable Components

**High-Level Theory:**
Components must have practical, commercially available values. Standard resistor and capacitor series (E12, E24, E96) provide discrete values. Inductors should be avoided when possible due to cost and size.

**Common Standard Values:**
*   **Resistors:** E12 series (10% tolerance): 1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2 (and multiples of 10).
*   **Capacitors:** Common values: 1 pF to 1000 μF. Prefer capacitors over inductors.
*   **Inductors:** Avoid if possible. If required, typical range: 1 μH to 100 mH.

**Process: Ensure Realizable Component Values**

1.  **Design with Arbitrary Values:** Complete initial design without worrying about standard values.
2.  **Apply Scaling:** Use frequency and impedance scaling to move components into realizable ranges.
3.  **Round to Standard Values:** Select nearest E12, E24, or E96 values.
4.  **Verify Performance:** Check that rounded values still meet specifications (poles, zeros, gain within \pm10% if required).
5.  **Avoid Extreme Values:** Stay within practical ranges:
    *   Resistors: 10 Ω to 10 MΩ.
    *   Capacitors: 1 pF to 1000 μF.
    *   Inductors: Avoid or limit to 1 μH to 100 mH.

| Check List | Theory / Equations |
| :--- | :--- |
| Standard Series | E12 (\pm10%), E24 (\pm5%), E96 (\pm1%). |
| Practical R Range | 10 Ω to 10 MΩ. |
| Practical C Range | 1 pF to 1000 μF. |
| Prefer Capacitors | Avoid inductors when possible. |

---

## SUMMARY OF SKILL DEPENDENCIES

The skills build upon each other in this hierarchy:

1. **Foundation:** Laplace Transform, ZIR/ZSR separation.
2. **Core Concept:** Network Function $H(s)$, poles, zeros.
3. **Bidirectional Conversion:** $H(s) \leftrightarrow$ Differential Equation.
4. **Response Calculations:** Exponential, step, impulse, sinusoidal steady-state responses.
5. **Parameter Extraction:** Derive circuit parameters from response graphs.
6. **Op-Amp Integration:** Apply all above skills to circuits with Op-Amps.
7. **Frequency Domain:** Bode plots, frequency response, filter classification.
8. **Design Synthesis:** Realize given $H(s)$ using passive or active circuits.
9. **Advanced Design:** Sallen-Key filters, cascading, scaling, standard values.
10. **Verification:** Evaluate loading effects, verify designs meet specifications.

All skills ultimately converge on the central task: **Given a desired behavior (time or frequency domain), design a realizable circuit that achieves it.**