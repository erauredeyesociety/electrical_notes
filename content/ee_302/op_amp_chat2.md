# Complete Operational Amplifier Reference Guide

A comprehensive reference covering op-amp theory, configurations, analysis methods, and practical applications.

---

## Table of Contents

1. [Introduction to Operational Amplifiers](#1-introduction-to-operational-amplifiers)
2. [Ideal vs Real Op-Amp Characteristics](#2-ideal-vs-real-op-amp-characteristics)
3. [Fundamental Op-Amp Concepts](#3-fundamental-op-amp-concepts)
4. [Analysis Methodology](#4-analysis-methodology)
5. [Standard Op-Amp Configurations](#5-standard-op-amp-configurations)
6. [Understanding Gain](#6-understanding-gain)
7. [Frequency Response and Bandwidth](#7-frequency-response-and-bandwidth)
8. [Practical Limitations and Imperfections](#8-practical-limitations-and-imperfections)
9. [Advanced Applications](#9-advanced-applications)
10. [Problem-Solving Guide](#10-problem-solving-guide)
11. [Quick Reference Tables](#11-quick-reference-tables)

---

## 1. Introduction to Operational Amplifiers

### 1.1 What is an Operational Amplifier?

An **operational amplifier (op-amp)** is a high-gain differential amplifier designed as an integrated circuit (IC). The name derives from its historical use in analog computers to perform mathematical operations: addition, subtraction, integration, differentiation, and more.

### 1.2 Op-Amp Symbol and Terminals

```
         +Vcc (Positive Supply)
            |
    v₁ -----|\
            | \
            |  \______ vₒ (Output)
            | /
    v₂ -----|/
            |
         -Vee (Negative Supply)

    v₁ = Noninverting input (+)
    v₂ = Inverting input (-)
```

**Key Terminals:**
- **Noninverting Input (+)**: Positive input terminal
- **Inverting Input (-)**: Negative input terminal
- **Output**: Amplified signal output
- **Power Supplies**: Typically dual supplies (±15V, ±12V, or ±5V), though omitted in circuit diagrams for clarity

### 1.3 Basic Operating Principle

The op-amp amplifies the **differential voltage** between its two inputs:

$$v_o = A_{OL}(v_+ - v_-)$$

Where:
- $v_o$ = output voltage
- $A_{OL}$ = open-loop gain (very large, typically 10⁵ to 10⁶)
- $v_+$ = voltage at noninverting input
- $v_-$ = voltage at inverting input

---

## 2. Ideal vs Real Op-Amp Characteristics

### 2.1 Ideal Op-Amp Properties

An **ideal operational amplifier** has the following characteristics:

| Characteristic | Ideal Value | Practical Implication |
|----------------|-------------|----------------------|
| **Input Impedance ($R_{in}$)** | **∞** (infinite) | No current flows into inputs: $i_+ = i_- = 0$ |
| **Output Impedance ($R_{out}$)** | **0** (zero) | Output voltage independent of load |
| **Open-Loop Gain ($A_{OL}$)** | **∞** (infinite) | With negative feedback: $v_+ = v_-$ |
| **Bandwidth** | ∞ (infinite) | No frequency limitations |
| **Common-Mode Gain** | 0 (zero) | Perfect rejection of common-mode signals |
| **Slew Rate** | ∞ (infinite) | Instantaneous output changes possible |
| **Offset Voltage** | 0 (zero) | Zero output when inputs are equal |

**Two Golden Rules for Ideal Op-Amps (with negative feedback):**

1. **Voltage Rule**: The voltages at both input terminals are equal
   $$v_+ = v_-$$

2. **Current Rule**: No current flows into or out of either input terminal
   $$i_+ = 0 \quad \text{and} \quad i_- = 0$$

### 2.2 Real Op-Amp Imperfections

#### Linear Range Imperfections

1. **Finite Open-Loop Gain**
   - Typical range: 10⁴ to 10⁶ (80-120 dB)
   - Still large enough that ideal approximation works well

2. **Finite Input Impedance**
   - Typical: 1-10 MΩ (BJT inputs)
   - Very high for FET inputs: >10¹² Ω
   
3. **Nonzero Output Impedance**
   - Typical: 50-100 Ω
   - Reduced by negative feedback

4. **Limited Bandwidth**
   - Gain decreases at higher frequencies
   - Characterized by gain-bandwidth product (GBW)

#### Nonlinear Limitations

1. **Output Voltage Swing (Saturation)**
   - Output cannot exceed power supply voltages
   - Typical range: $\pm 14V$ for $\pm 15V$ supplies
   - Causes clipping when exceeded

2. **Slew Rate Limitation**
   $$SR = \left|\frac{dv_o}{dt}\right|_{max}$$
   - Maximum rate of output voltage change
   - Typical: 0.5 V/μs (LM741) to 1000 V/μs (high-speed op-amps)
   - Causes distortion at high frequencies/amplitudes

3. **Full-Power Bandwidth**
   $$f_{FP} = \frac{SR}{2\pi V_{om}}$$
   - Maximum frequency for full-amplitude sinusoidal output
   - Limited by slew rate

#### DC Imperfections (Offsets)

1. **Input Bias Current ($I_B$)**
   $$I_B = \frac{I_{B+} + I_{B-}}{2}$$
   - DC current into input terminals
   - Typical: 80 nA (BJT), <1 pA (FET)

2. **Input Offset Current ($I_{off}$)**
   $$I_{off} = I_{B+} - I_{B-}$$
   - Difference between bias currents
   - Typical: 20 nA (BJT)

3. **Input Offset Voltage ($V_{off}$)**
   - Equivalent DC voltage that causes nonzero output when inputs grounded
   - Typical: 1-5 mV

---

## 3. Fundamental Op-Amp Concepts

### 3.1 Differential and Common-Mode Signals

Any two input voltages can be decomposed into differential and common-mode components:

#### Differential Signal ($v_{id}$ or $v_d$)
$$v_{id} = v_+ - v_-$$

- The **signal of interest** in most applications
- Op-amps are designed to amplify this component
- Represents the actual information being processed

#### Common-Mode Signal ($v_{icm}$ or $v_{cm}$)
$$v_{icm} = \frac{v_+ + v_-}{2}$$

- The **average** of both inputs
- Usually represents unwanted noise (e.g., 60 Hz power line interference)
- Ideal op-amps completely reject this component

**Example**: In ECG measurements, the heart signal is differential while power line noise appears as common-mode interference.

### 3.2 Common-Mode Rejection Ratio (CMRR)

$$\text{CMRR} = \frac{|A_d|}{|A_{cm}|} = \frac{\text{Differential Gain}}{\text{Common-Mode Gain}}$$

- Measures ability to reject common-mode signals
- Expressed in decibels: $\text{CMRR}_{\text{dB}} = 20 \log(\text{CMRR})$
- Typical values: 80-120 dB
- Higher is better

**Practical Significance**: A CMRR of 100 dB means the differential signal is amplified 100,000 times more than the common-mode signal.

### 3.3 Virtual Ground and Virtual Short

#### Virtual Short
When negative feedback is present, the infinite open-loop gain forces:
$$v_+ = v_-$$

This is called a "virtual short" because the voltages are equal, but **no current flows** between the terminals (unlike a real short circuit).

#### Virtual Ground
When the noninverting input is grounded ($v_+ = 0V$):
$$v_- = v_+ = 0V$$

The inverting input is at ground potential but cannot sink or source current. It's "virtually" at ground.

### 3.4 Negative vs Positive Feedback

#### Negative Feedback
- Output signal fed back to **inverting input (−)**
- Opposes the input signal
- Stabilizes the circuit in linear region
- Enables predictable, controlled gain
- **Required for linear amplification**

#### Positive Feedback
- Output fed back to **noninverting input (+)**
- Reinforces the input signal
- Causes saturation (output goes to rail)
- Used in comparators, oscillators, Schmitt triggers
- Summing-point constraint **does not apply**

---

## 4. Analysis Methodology

### 4.1 The Summing-Point Constraint Method

When an op-amp has **negative feedback**, use the summing-point constraint:

**Two Key Constraints:**

1. **Voltage Constraint (Virtual Short)**
   $$v_- = v_+$$

2. **Current Constraint (Virtual Open)**
   $$i_- = 0 \quad \text{and} \quad i_+ = 0$$

### 4.2 Step-by-Step Analysis Procedure

#### Step 1: Verify Negative Feedback
- Check that output connects to inverting input (−)
- If positive feedback present, summing-point constraint **cannot** be used
- Circuit will saturate (not operate linearly)

#### Step 2: Apply Summing-Point Constraint
- Set $v_+ = v_-$
- Set $i_+ = 0$ and $i_- = 0$

#### Step 3: Apply Circuit Analysis Techniques

**Primary Method: Nodal Analysis (KCL)**
- Write KCL equation at inverting input node
- Most efficient because $i_{op-amp} = 0$
- Example: "Current in = Current out"

**Secondary Method: Voltage Division**
- Used for noninverting configurations
- Analyze voltage divider in feedback network

**Supporting Tool: Ohm's Law**
- Calculate currents through resistors: $i = \frac{v_1 - v_2}{R}$
- Use node voltages from constraints

**When Needed: Mesh Analysis (KVL)**
- Occasionally needed for output voltage
- Usually nodal analysis is sufficient

### 4.3 Detailed KCL Application

**At the Inverting Node:**

All currents entering the node must equal currents leaving:
$$\sum i_{in} = \sum i_{out}$$

Since $i_{op-amp} = 0$, all current through input resistors must flow through feedback elements.

**Example Steps:**
1. Identify all resistors connected to inverting node
2. Write current expression for each: $i = \frac{v_{from} - v_{to}}{R}$
3. Apply KCL: sum of currents = 0
4. Solve for output voltage

---

## 5. Standard Op-Amp Configurations

### 5.1 Inverting Amplifier

```
      R₁           R₂
vᵢₙ ----/\/\/----+----/\/\/---- vₒ
                 |            |
              (-)|\          |
                 | \         |
            0V --|+) >-------+
                 | /
                 |/
```

**Analysis:**
1. $v_+ = 0V$ (grounded)
2. $v_- = v_+ = 0V$ (virtual ground)
3. KCL at inverting node: $i_1 = i_2$
4. $\frac{v_{in}}{R_1} = \frac{0 - v_o}{R_2} = -\frac{v_o}{R_2}$

**Characteristics:**

$$A_v = \frac{v_o}{v_{in}} = -\frac{R_2}{R_1}$$

| Property | Value |
|----------|-------|
| Voltage Gain | $-\frac{R_2}{R_1}$ |
| Phase Shift | 180° (inverted) |
| Input Impedance | $R_1$ |
| Output Impedance | ~0 Ω (ideal) |
| Minimum Gain | <1 (can attenuate) |

**Key Features:**
- Negative gain (output inverted)
- Input impedance determined by $R_1$
- Can have gain magnitude <1
- Most common configuration

### 5.2 Noninverting Amplifier

```
            R₂
       +----/\/\/----+
       |             |
vᵢₙ ---|+)|\        |
          | \       |
       +-|-) >------+---- vₒ
       |  | /
       |  |/
       |
       +----/\/\/---- 0V
            R₁
```

**Analysis:**
1. $v_+ = v_{in}$
2. $v_- = v_+ = v_{in}$ (constraint)
3. Voltage divider: $v_- = v_o \cdot \frac{R_1}{R_1 + R_2}$
4. $v_{in} = v_o \cdot \frac{R_1}{R_1 + R_2}$

**Characteristics:**

$$A_v = \frac{v_o}{v_{in}} = 1 + \frac{R_2}{R_1}$$

| Property | Value |
|----------|-------|
| Voltage Gain | $1 + \frac{R_2}{R_1}$ |
| Phase Shift | 0° (non-inverted) |
| Input Impedance | ∞ (ideal) |
| Output Impedance | ~0 Ω (ideal) |
| Minimum Gain | 1 (unity gain) |

**Key Features:**
- Positive gain (output in phase)
- Very high input impedance
- Minimum gain of 1
- Ideal voltage amplifier

### 5.3 Voltage Follower (Buffer)

```
vᵢₙ ---|+)|\
          | \
       +--|-) >---- vₒ
       |  | /
       |  |/
       |
       +--------+
```

**Special case of noninverting amplifier where $R_2 = 0$ and $R_1 = ∞$**

**Characteristics:**

$$A_v = 1$$
$$v_o = v_{in}$$

| Property | Value |
|----------|-------|
| Voltage Gain | 1 (unity) |
| Phase Shift | 0° |
| Input Impedance | ∞ (ideal) |
| Output Impedance | ~0 Ω (ideal) |

**Applications:**
- Impedance matching
- Buffering signals to prevent loading
- Isolation between stages
- Current amplification

### 5.4 Summing Amplifier

```
      Rₐ
vₐ ----/\/\/----+
                |    Rf
      Rᵦ        |----/\/\/---- vₒ
vᵦ ----/\/\/----+            |
                |            |
      Rᴄ        |         (-)|\
vᴄ ----/\/\/----+            | \
                          0V --|+) >-------+
                               | /
                               |/
```

**Analysis:**
1. $v_- = 0V$ (virtual ground)
2. KCL: $i_A + i_B + i_C = i_f$
3. $\frac{v_A}{R_A} + \frac{v_B}{R_B} + \frac{v_C}{R_C} = -\frac{v_o}{R_f}$

**General Formula:**

$$v_o = -\left(\frac{R_f}{R_A}v_A + \frac{R_f}{R_B}v_B + \frac{R_f}{R_C}v_C + \cdots\right)$$

**For n inputs:**

$$v_o = -\sum_{i=1}^{n} \frac{R_f}{R_i}v_i$$

**Special Cases:**
- Equal resistors ($R_A = R_B = R_C = R_f$): $v_o = -(v_A + v_B + v_C)$
- Weighted summer: Different resistor ratios give different weights

**Applications:**
- Audio mixing
- Digital-to-analog conversion (DAC)
- Signal combining
- Analog computation

### 5.5 Difference Amplifier (Subtractor)

```
      R₁           R₂
v₁ ----/\/\/----+----/\/\/---- vₒ
                |            |
             (-)|\          |
                | \         |
            +---|+) >-------+
            |   | /
      R₃    |   |/
v₂ ---/\/\/--+
            |
            +----/\/\/---- 0V
                R₄
```

**Analysis:**
1. Voltage divider at $v_+$: $v_+ = v_2 \cdot \frac{R_4}{R_3 + R_4}$
2. $v_- = v_+$ (constraint)
3. KCL at inverting node: $\frac{v_1 - v_-}{R_1} = \frac{v_- - v_o}{R_2}$

**General Formula:**

$$v_o = v_2\left(\frac{R_4}{R_3 + R_4}\right)\left(1 + \frac{R_2}{R_1}\right) - v_1\left(\frac{R_2}{R_1}\right)$$

**For matched resistors ($R_1 = R_3$ and $R_2 = R_4$):**

$$v_o = \frac{R_2}{R_1}(v_2 - v_1)$$

**Applications:**
- Differential signal amplification
- Common-mode rejection
- Bridge amplifiers
- Instrumentation systems

### 5.6 Integrator

```
      R            C
vᵢₙ ----/\/\/----+----||---- vₒ
                 |          |
              (-)|\        |
                 | \       |
            0V --|+) >-----+
                 | /
                 |/
```

**Analysis:**
1. $v_- = 0V$ (virtual ground)
2. $i_R = \frac{v_{in}}{R}$ (current through resistor)
3. $i_C = C\frac{dv_C}{dt} = -C\frac{dv_o}{dt}$ (capacitor current)
4. $i_R = i_C$ (KCL)

**Transfer Function:**

$$v_o(t) = -\frac{1}{RC}\int_0^t v_{in}(\tau)d\tau + v_o(0)$$

**For DC input ($v_{in} = V_{DC}$):**

$$v_o(t) = -\frac{V_{DC}}{RC}t + v_o(0)$$

**Frequency Domain:**

$$H(j\omega) = \frac{V_o}{V_{in}} = -\frac{1}{j\omega RC}$$

**Characteristics:**
- Time constant: $\tau = RC$
- Phase shift: -90°
- Gain increases at lower frequencies (1/f response)
- Output is ramp for DC input, phase-shifted sine for AC input

**Applications:**
- Waveform generation
- Analog computation
- Signal processing
- Control systems

**Practical Considerations:**
- DC input causes output to saturate (add resistor in parallel with C)
- Reset switch often needed to discharge capacitor

### 5.7 Differentiator

```
      C            R
vᵢₙ ----||-------+----/\/\/---- vₒ
                 |            |
              (-)|\          |
                 | \         |
            0V --|+) >-------+
                 | /
                 |/
```

**Analysis:**
1. $v_- = 0V$ (virtual ground)
2. $i_C = C\frac{dv_{in}}{dt}$ (capacitor current)
3. $i_R = -\frac{v_o}{R}$ (resistor current)
4. $i_C = i_R$ (KCL)

**Transfer Function:**

$$v_o(t) = -RC\frac{dv_{in}}{dt}$$

**Frequency Domain:**

$$H(j\omega) = -j\omega RC$$

**Characteristics:**
- Time constant: $\tau = RC$
- Phase shift: +90°
- Gain increases at higher frequencies
- Output is spike for step input, phase-shifted sine for AC input

**Applications:**
- Edge detection
- Rate-of-change measurement
- High-pass filtering
- Waveform shaping

**Practical Considerations:**
- **Very sensitive to high-frequency noise** (amplifies noise)
- Usually requires input filtering (add series resistor with C)
- Limited practical use compared to integrator

---

## 6. Understanding Gain

### 6.1 Voltage Gain Fundamentals

**Voltage gain** ($A_v$) is the ratio of output voltage to input voltage:

$$A_v = \frac{v_o}{v_{in}}$$

For ideal linear amplifier:
$$v_o(t) = A_v \cdot v_{in}(t)$$

**Key Points:**
- Gain can be positive (noninverting) or negative (inverting)
- Magnitude indicates amplification factor
- Sign indicates phase relationship

### 6.2 Complex Gain (Frequency-Dependent)

For sinusoidal signals, gain is a **complex quantity**:

$$A_v(j\omega) = \frac{V_o}{V_{in}} = |A_v|e^{j\phi}$$

Where:
- $|A_v|$ = magnitude (amplification factor)
- $\phi$ = phase shift

**Magnitude and Phase:**
$$|A_v| = \sqrt{\text{Re}(A_v)^2 + \text{Im}(A_v)^2}$$
$$\phi = \tan^{-1}\left(\frac{\text{Im}(A_v)}{\text{Re}(A_v)}\right)$$

### 6.3 Gain in Decibels (dB)

Decibels provide logarithmic representation of gain:

$$A_v|_{\text{dB}} = 20\log_{10}|A_v|$$

**Conversion Table:**

| Voltage Gain | dB Gain |
|--------------|---------|
| 0.001 | -60 dB |
| 0.01 | -40 dB |
| 0.1 | -20 dB |
| 0.707 ($1/\sqrt{2}$) | -3 dB |
| 1 | 0 dB |
| 2 | +6 dB |
| 10 | +20 dB |
| 100 | +40 dB |
| 1000 | +60 dB |

**Key Relationships:**
- **Unity gain** (gain = 1): 0 dB
- **Half-power point** (gain = 0.707): -3 dB
- **Decade increase** (gain ×10): +20 dB
- **Double gain** (gain ×2): +6 dB

**Advantages of dB:**
- Multiplication becomes addition: $A_{total} = A_1 \times A_2$ → $A_{dB} = A_{1,dB} + A_{2,dB}$
- Easier to plot wide ranges (Bode plots)
- Industry standard for specifications

### 6.4 Open-Loop vs Closed-Loop Gain

#### Open-Loop Gain ($A_{OL}$ or $A_0$)
- Gain without feedback
- Very large: 10⁵ to 10⁶ (100-120 dB)
- Frequency-dependent
- Unstable and impractical for most applications

#### Closed-Loop Gain ($A_{CL}$ or $A_v$)
- Gain with negative feedback
- Determined by external resistors
- Predictable and stable
- **Much smaller than open-loop gain**

**Relationship:**
$$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$$

Where $\beta$ is the feedback factor.

For large $A_{OL}$:
$$A_{CL} \approx \frac{1}{\beta}$$

This is why closed-loop gain depends only on resistor ratios, not op-amp parameters.

### 6.5 Gain-Bandwidth Product (GBW)

The product of gain and bandwidth is constant:

$$\text{GBW} = A_{CL} \times f_{BW} = A_0 \times f_0 = f_t$$

Where:
- $f_t$ = unity-gain frequency (frequency where $|A| = 1$)
- $A_0$ = DC open-loop gain
- $f_0$ = open-loop bandwidth

**Practical Implication:**
Higher closed-loop gain → Lower bandwidth

**Example:** If GBW = 1 MHz:
- Gain of 1 → Bandwidth = 1 MHz
- Gain of 10 → Bandwidth = 100 kHz
- Gain of 100 → Bandwidth = 10 kHz

---

## 7. Frequency Response and Bandwidth

### 7.1 Open-Loop Frequency Response

Real op-amps have frequency-dependent gain:

$$A(j\omega) = \frac{A_0}{1 + j\frac{\omega}{\omega_0}}$$

Where:
- $A_0$ = DC gain
- $\omega_0 = 2\pi f_0$ = break frequency

**Bode Plot Characteristics:**
- Flat response up to $f_0$
- -20 dB/decade rolloff above $f_0$
- -90° phase shift at high frequencies

### 7.2 Closed-Loop Bandwidth

$$f_{CL} = \frac{f_t}{A_{CL}}$$

**Example (LM741):**
- $f_t$ = 1 MHz
- For $A_{CL}$ = 10: $f_{CL}$ = 100 kHz
- For $A_{CL}$ = 100: $f_{CL}$ = 10 kHz

### 7.3 Stability Considerations

**Phase Margin:**
- Difference between phase shift and -180° at unity-gain frequency
- Must be >45° for stable operation
- >60° preferred for good transient response

**Compensation:**
- Internal compensation (most modern op-amps)
- External compensation (older designs, high-speed op-amps)
- Unity-gain stable vs. conditionally stable op-amps

---

## 8. Practical Limitations and Imperfections

### 8.1 Output Voltage Saturation

**Limitation:**
$$V_{-rail} + V_{sat} \leq v_o \leq V_{+rail} - V_{sat}$$

**Typical Values:**
- Standard op-amps: $\pm 14V$ for $\pm 15V$ supplies
- Rail-to-rail op-amps: Within 50-100 mV of rails

**Effect:** Output clips when theoretical voltage exceeds limits

### 8.2 Slew Rate Limiting

**Definition:**
$$SR = \left|\frac{dv_o}{dt}\right|_{max}$$

**For sinusoidal output:**
$$\frac{dv_o}{dt} = 2\pi f V_{om} \cos(2\pi ft)$$

**Maximum occurs at zero crossing:**
$$\left|\frac{dv_o}{dt}\right|_{max} = 2\pi f V_{om}$$

**Distortion occurs when:**
$$2\pi f V_{om} > SR$$

**Full-Power Bandwidth:**
$$f_{FP} = \frac{SR}{2\pi V_{om}}$$

**Example (LM741, SR = 0.5 V/μs):**
- For 10V peak output: $f_{FP} = 7.96$ kHz
- For 1V peak output: $f_{FP} = 79.6$ kHz

### 8.3 Offset Voltage Effects

**Input offset voltage** creates DC error:

$$v_o(\text{error}) = V_{off}(1 + \frac{R_2}{R_1})$$

For inverting amplifier, this is multiplied by closed-loop gain.

**Compensation Methods:**
1. **Balancing resistors**: Add $R_3 = R_1 \parallel R_2$ at noninverting input
2. **Offset nulling**: Use trim potentiometer on offset null pins
3. **AC coupling**: Block DC with capacitor (if DC accuracy not needed)
4. **Chopper stabilization**: Auto-zeroing circuits

### 8.4 Input Bias Current Effects

Bias currents through source resistances create offset voltages:

$$V_{error} = I_B \times R_{source}$$

**Minimization:**
- Use **matched source impedances** at both inputs
- Use **FET-input op-amps** (pA bias currents vs. nA for BJT)
- Add compensation resistor at noninverting input

---

## 9. Advanced Applications

### 9.1 Instrumentation Amplifier

**Three op-amp configuration:**

```
        R₁
v₁ --+--/\/\/--+-- (+) Op-Amp 1 Out --+
     |         |                       |
     |    Rg   |                       +--/\/\/-- R₃ --+
     +--/\/\/--+                       |                |
              |                        |           (-) Op-Amp 3 -- vₒ
     +--/\/\/--+                       |                |
     |    Rg   |                       +--/\/\/-- R₄ --+
     |         |                       |
v₂ --+--/\/\/--+-- (+) Op-Amp 2 Out --+
        R₂
```

**Gain:**
$$A_v = \left(1 + \frac{2R_1}{R_g}\right)\frac{R_4}{R_3}$$

**For matched resistors:**
$$A_v = \left(1 + \frac{2R}{R_g}\right)$$

**Advantages:**
- Very high input impedance (both inputs)
- Excellent CMRR (>100 dB)
- Single resistor sets gain
- Differential input, single-ended output

**Applications:**
- Biomedical instrumentation (ECG, EEG)
- Strain gauge amplifiers
- Bridge amplifiers
- Precision measurement systems

### 9.2 Active Filters

#### Low-Pass Filter (Sallen-Key)

**2nd-order Butterworth:**
$$H(s) = \frac{K\omega_c^2}{s^2 + \sqrt{2}\omega_c s + \omega_c^2}$$

**Cutoff frequency:**
$$f_c = \frac{1}{2\pi\sqrt{R_1 R_2 C_1 C_2}}$$

#### High-Pass Filter

Simply swap resistors and capacitors from low-pass design.

#### Band-Pass Filter

Cascade low-pass and high-pass filters, or use multiple feedback topology.

**Center frequency:**
$f_0 = \frac{1}{2\pi RC}$

**Quality factor (Q):**
$Q = \frac{f_0}{BW}$

Where BW is the bandwidth between -3 dB points.

### 9.3 Precision Rectifiers

#### Half-Wave Rectifier

```
      R₁
vᵢₙ ----/\/\/----+
                 |
              (-)|\    D₁
                 | \---|>|---+
            0V --|+) >-------+---- vₒ
                 | /         |
                 |/          |
                             |
                        +----+
                        |
                       ---  D₂
                        V
                        |
                       ---
```

**Advantages over passive diode:**
- Eliminates diode voltage drop (0.7V)
- Works with small signals (<0.7V)
- Sharp breakpoint at 0V

#### Full-Wave Rectifier

Uses two op-amps for precision full-wave rectification without center-tapped transformer.

### 9.4 Comparators

```
v₁ ---|+)|\
         | \
         |  >---- vₒ (±Vsat)
         | /
v₂ ---|-)/ 
```

**Operation:**
- No feedback (open-loop)
- Output saturates to +Vsat or -Vsat
- Fast switching between rails

**Output:**
$v_o = \begin{cases} +V_{sat} & \text{if } v_+ > v_- \\ -V_{sat} & \text{if } v_+ < v_- \end{cases}$

**Applications:**
- Level detection
- Zero-crossing detection
- Analog-to-digital conversion
- Waveform generation

**Schmitt Trigger (with hysteresis):**
- Add positive feedback
- Creates two threshold voltages
- Prevents oscillation from noise
- Upper threshold: $V_{TH}$
- Lower threshold: $V_{TL}$
- Hysteresis: $V_{TH} - V_{TL}$

### 9.5 Oscillators

#### Wien Bridge Oscillator

**Frequency of oscillation:**
$f_0 = \frac{1}{2\pi RC}$

**Gain requirement:**
$A_v = 3$

**Features:**
- Low distortion sine wave
- Variable frequency by varying R or C
- Requires amplitude stabilization

#### Phase-Shift Oscillator

Uses RC network to create 180° phase shift, combined with inverting amplifier.

**Frequency:**
$f_0 = \frac{1}{2\pi RC\sqrt{6}}$

### 9.6 Logarithmic Amplifier

Uses diode or transistor in feedback path to create logarithmic transfer function:

$v_o = -K \ln\left(\frac{v_{in}}{V_{ref}}\right)$

**Applications:**
- Compression of wide dynamic range signals
- Multiplication/division (log of product = sum of logs)
- Power measurement in dB

### 9.7 Sample and Hold Circuit

```
        S (switch)
vᵢₙ ------o/o------+------|+)|\
                   |         | \---- vₒ
                  ---        |  >
                  --- C   +--|-)/
                   |      |  |/
                   |      |
                  ---     +----+
```

**Operation:**
- Switch closed: Capacitor charges to input voltage
- Switch open: Capacitor holds voltage
- Buffer prevents discharge

**Applications:**
- Analog-to-digital conversion
- Peak detection
- Signal processing

---

## 10. Problem-Solving Guide

### 10.1 Quick Analysis Strategy

**For ANY op-amp circuit:**

1. **Identify configuration** (inverting, noninverting, summing, etc.)
2. **Check for negative feedback** (required for linear operation)
3. **Apply summing-point constraint:**
   - $v_+ = v_-$
   - $i_+ = 0$, $i_- = 0$
4. **Write KCL at summing node** (usually inverting input)
5. **Apply Ohm's Law** to express currents
6. **Solve algebraically** for desired quantity
7. **Verify result** (check sign, magnitude, saturation limits)

### 10.2 Common Problem Types

#### Type 1: Find Output Voltage

**Given:** Input voltage(s) and resistor values

**Method:**
1. Apply summing-point constraint to find node voltages
2. Write KCL equation at inverting node
3. Express currents using Ohm's Law
4. Solve for $v_o$

**Example:** Inverting amplifier with $v_{in} = 1V$, $R_1 = 10k\Omega$, $R_2 = 100k\Omega$

Solution:
$v_o = -\frac{R_2}{R_1}v_{in} = -\frac{100k}{10k}(1V) = -10V$

#### Type 2: Design for Specific Gain

**Given:** Required gain $A_v$

**Method:**
1. Choose configuration (inverting or noninverting)
2. Select standard resistor values
3. Calculate second resistor from gain formula

**Example:** Design noninverting amplifier with gain = 11

Choose $R_1 = 10k\Omega$:
$A_v = 1 + \frac{R_2}{R_1}$
$11 = 1 + \frac{R_2}{10k}$
$R_2 = 100k\Omega$

#### Type 3: Find Frequency Response

**Given:** Circuit with reactive elements (C or L)

**Method:**
1. Replace reactive elements with impedances: $Z_C = \frac{1}{j\omega C}$, $Z_L = j\omega L$
2. Apply standard analysis with impedances instead of resistances
3. Express gain as function of frequency: $A_v(j\omega)$
4. Find magnitude and phase

**Example:** Low-pass filter cutoff frequency
$f_c = \frac{1}{2\pi RC}$

#### Type 4: Account for Real Op-Amp Limitations

**Given:** Real op-amp parameters

**Check:**
1. **Saturation:** Is $|v_o| < V_{sat}$?
2. **Slew rate:** Is $2\pi f V_{om} < SR$?
3. **Bandwidth:** Is $f < f_{CL}$?
4. **Offset:** Calculate DC error from $V_{off}$ and $I_B$

### 10.3 Troubleshooting Checklist

**If circuit doesn't work as expected:**

- [ ] Verify power supply connections and voltages
- [ ] Check for negative feedback (correct topology)
- [ ] Verify all component values and connections
- [ ] Check for output saturation (measure with DMM)
- [ ] Look for oscillation (check with oscilloscope)
- [ ] Verify input signal amplitude and frequency
- [ ] Check for excessive output loading
- [ ] Measure DC offset at output with inputs grounded
- [ ] Verify op-amp not damaged (swap with known good unit)
- [ ] Check ground connections and ground loops

### 10.4 Common Mistakes to Avoid

**Conceptual Errors:**
1. ❌ Applying summing-point constraint to positive feedback circuits
2. ❌ Assuming current flows into op-amp inputs
3. ❌ Forgetting negative sign in inverting amplifier gain
4. ❌ Confusing voltage gain with power gain

**Calculation Errors:**
1. ❌ Wrong sign in KCL equation (current directions)
2. ❌ Incorrect voltage difference in Ohm's Law ($v_1 - v_2$ vs. $v_2 - v_1$)
3. ❌ Forgetting to include "1+" in noninverting gain formula
4. ❌ Using voltage divider formula when currents aren't zero

**Design Errors:**
1. ❌ Choosing resistor values too high (>1MΩ) or too low (<1kΩ)
2. ❌ Ignoring frequency limitations (bandwidth, slew rate)
3. ❌ Not checking for output saturation
4. ❌ Forgetting decoupling capacitors on power supplies

**Practical Errors:**
1. ❌ No ground connection or poor grounding
2. ❌ Breadboard parasitics causing oscillation
3. ❌ Excessive capacitive loading on output
4. ❌ Wrong pin connections (consult datasheet)

---

## 11. Quick Reference Tables

### 11.1 Configuration Summary

| Configuration | Gain Formula | Input Z | Phase | Min Gain |
|--------------|--------------|---------|-------|----------|
| Inverting | $-\frac{R_2}{R_1}$ | $R_1$ | 180° | <1 |
| Noninverting | $1 + \frac{R_2}{R_1}$ | ∞ | 0° | 1 |
| Voltage Follower | $1$ | ∞ | 0° | 1 |
| Summing | $-\sum\frac{R_f}{R_i}v_i$ | Varies | 180° | — |
| Difference | $\frac{R_2}{R_1}(v_2-v_1)$ | Varies | 0° or 180° | — |
| Integrator | $-\frac{1}{RC}\int v_{in}dt$ | $R$ | -90° | — |
| Differentiator | $-RC\frac{dv_{in}}{dt}$ | Varies | +90° | — |

### 11.2 Standard Op-Amp Specifications (LM741 Example)

| Parameter | Symbol | Typical Value | Units |
|-----------|--------|---------------|-------|
| Open-loop gain | $A_{OL}$ | 200,000 (106 dB) | V/V |
| Input offset voltage | $V_{os}$ | 1 | mV |
| Input bias current | $I_B$ | 80 | nA |
| Input offset current | $I_{os}$ | 20 | nA |
| Input impedance | $Z_{in}$ | 2 | MΩ |
| Output impedance | $Z_{out}$ | 75 | Ω |
| Slew rate | SR | 0.5 | V/μs |
| Gain-bandwidth product | GBW | 1 | MHz |
| CMRR | — | 90 | dB |
| Power supply voltage | $V_{CC}, V_{EE}$ | ±15 | V |
| Output voltage swing | $V_{o(max)}$ | ±14 | V |
| Quiescent current | $I_Q$ | 1.7 | mA |

### 11.3 Typical Op-Amp Families

| Type | Input | $I_B$ | $V_{os}$ | SR | GBW | Application |
|------|-------|-------|----------|----|----|-------------|
| LM741 | BJT | 80 nA | 1 mV | 0.5 V/μs | 1 MHz | General purpose |
| TL071 | JFET | 65 pA | 3 mV | 13 V/μs | 3 MHz | Low noise audio |
| LM358 | BJT | 45 nA | 2 mV | 0.3 V/μs | 1 MHz | Single supply |
| LF411 | JFET | 50 pA | 0.5 mV | 15 V/μs | 4 MHz | High speed |
| OP07 | BJT | 4 nA | 25 μV | 0.3 V/μs | 0.6 MHz | Precision |
| AD8065 | BJT | 2 μA | 2 mV | 180 V/μs | 145 MHz | High speed |
| OPA627 | BJT | 1 nA | 100 μV | 55 V/μs | 16 MHz | Audio/precision |

### 11.4 Resistor Selection Guidelines

| Application | Recommended Range | Reason |
|-------------|------------------|--------|
| Input resistors | 1kΩ - 100kΩ | Balance between noise and bias current effects |
| Feedback resistors | 1kΩ - 1MΩ | Avoid excessive offset from bias current |
| Summing networks | 10kΩ - 100kΩ | Standard range for most applications |
| High impedance inputs | >100kΩ | Use FET-input op-amps |
| Low noise | <10kΩ | Minimize thermal noise |
| DC applications | Equal source impedances | Minimize offset from bias currents |

### 11.5 Capacitor Selection Guidelines

| Application | Type | Value Range | Notes |
|-------------|------|-------------|-------|
| Integrator | Film, ceramic | 10 nF - 10 μF | Low leakage, stable |
| Differentiator | Film, ceramic | 100 pF - 1 nF | Small values, add series R |
| AC coupling | Electrolytic, film | 1 μF - 100 μF | Consider polarity |
| Power supply decoupling | Ceramic | 0.1 μF | Close to IC pins |
| Power supply bulk | Electrolytic | 10 μF - 100 μF | At power entry |
| Compensation | Ceramic | 10 pF - 100 pF | High-speed op-amps |

### 11.6 Important Formulas Quick Reference

**Gain Conversions:**
- Voltage gain to dB: $A_{dB} = 20\log_{10}|A_v|$
- dB to voltage gain: $|A_v| = 10^{A_{dB}/20}$

**Frequency Calculations:**
- Cutoff frequency (RC): $f_c = \frac{1}{2\pi RC}$
- Closed-loop bandwidth: $f_{CL} = \frac{f_t}{A_{CL}}$
- Full-power bandwidth: $f_{FP} = \frac{SR}{2\pi V_{om}}$

**Time Constants:**
- RC time constant: $\tau = RC$
- 5τ rule: Circuit settles to 99.3% in 5τ

**Power and Energy:**
- Power dissipation: $P = \frac{V^2}{R} = I^2R = VI$
- Energy in capacitor: $E = \frac{1}{2}CV^2$

### 11.7 Standard Resistor Values (E12 Series)

10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 (and multiples)

**Common ratios for gain:**
- Gain of 2: $R_2/R_1 = 1$ (10k/10k for noninverting)
- Gain of 5: $R_2/R_1 = 4$ (82k/22k = 3.73, close to 4)
- Gain of 10: $R_2/R_1 = 9$ (100k/11k ≈ 9)
- Gain of 11: $R_2/R_1 = 10$ (100k/10k)

### 11.8 Decibel Reference Table

| Ratio | dB | Ratio | dB |
|-------|-------|-------|-------|
| 0.1 | -20 | 10 | +20 |
| 0.2 | -14 | 5 | +14 |
| 0.5 | -6 | 2 | +6 |
| 0.707 | -3 | 1.41 | +3 |
| 1.0 | 0 | 1.0 | 0 |

### 11.9 Design Example Worksheet

**Problem:** Design an inverting amplifier with gain of -5, input impedance of 10kΩ.

**Solution Steps:**
1. Configuration: Inverting amplifier
2. Input impedance = $R_1 = 10k\Omega$ ✓
3. Gain formula: $A_v = -\frac{R_2}{R_1}$
4. Required: $-5 = -\frac{R_2}{10k}$
5. Therefore: $R_2 = 50k\Omega$ ✓
6. Check bandwidth: If $f_t = 1MHz$, then $f_{CL} = \frac{1MHz}{5} = 200kHz$ ✓
7. Check saturation: For ±15V supplies, $V_{o,max} = \pm 14V$, so $V_{in,max} = \frac{14V}{5} = 2.8V$ ✓

**Final Design:**
- $R_1 = 10k\Omega$
- $R_2 = 47k\Omega$ or $50k\Omega$ (use standard value)
- $A_v = -4.7$ or $-5.0$

---

## 12. Advanced Concepts and Theory

### 12.1 Loop Gain and Feedback Theory

**Loop gain ($A\beta$):**
$T = A_{OL} \cdot \beta$

Where:
- $A_{OL}$ = open-loop gain
- $\beta$ = feedback factor

**Closed-loop gain:**
$A_{CL} = \frac{A_{OL}}{1 + A_{OL}\beta}$

For large loop gain ($A_{OL}\beta >> 1$):
$A_{CL} \approx \frac{1}{\beta}$

**Feedback factor examples:**
- Inverting: $\beta = -\frac{R_1}{R_1 + R_2}$
- Noninverting: $\beta = \frac{R_1}{R_1 + R_2}$

### 12.2 Noise Analysis

**Input-referred noise:**
$v_{n,total} = \sqrt{v_{n,opamp}^2 + v_{n,R1}^2 + v_{n,R2}^2 + \cdots}$

**Thermal noise in resistor:**
$v_n = \sqrt{4kTRB}$

Where:
- $k = 1.38 \times 10^{-23}$ J/K (Boltzmann constant)
- $T$ = temperature (K)
- $R$ = resistance (Ω)
- $B$ = bandwidth (Hz)

**Noise minimization:**
- Use low-noise op-amps
- Minimize resistor values (where practical)
- Limit bandwidth to minimum required
- Use matched impedances

### 12.3 PSRR (Power Supply Rejection Ratio)

Measures ability to reject power supply variations:

$\text{PSRR} = 20\log\left(\frac{\Delta V_{supply}}{\Delta V_{offset}}\right)$

**Typical values:** 80-120 dB

**Importance:** High PSRR reduces output variations due to supply noise

### 12.4 Input Common-Mode Range

Maximum voltage range that can be applied to both inputs simultaneously while maintaining linear operation.

**Typical:** 
- Standard op-amps: $V_{EE} + 2V$ to $V_{CC} - 2V$
- Rail-to-rail input: $V_{EE}$ to $V_{CC}$

### 12.5 Output Current Limiting

**Short-circuit current:**
Typically 20-40 mA for standard op-amps.

**For higher current:**
- Add push-pull buffer stage
- Use power op-amps
- Add external pass transistors

---

## 14. Example Problems with Solutions

### Example 1: Basic Inverting Amplifier

**Given:** $v_{in} = 0.5V$, $R_1 = 10k\Omega$, $R_2 = 100k\Omega$

**Find:** $v_o$

**Solution:**
$A_v = -\frac{R_2}{R_1} = -\frac{100k}{10k} = -10$
$v_o = A_v \cdot v_{in} = -10 \times 0.5V = -5V$

**Answer:** $v_o = -5V$

### Example 2: Noninverting Amplifier Design

**Design:** Noninverting amplifier with gain of 21

**Solution:**
$A_v = 1 + \frac{R_2}{R_1} = 21$
$\frac{R_2}{R_1} = 20$

Choose $R_1 = 10k\Omega$ (standard value):
$R_2 = 20 \times 10k = 200k\Omega$

Use $R_2 = 200k\Omega$ (or closest standard value: 220kΩ)

**Answer:** $R_1 = 10k\Omega$, $R_2 = 200k\Omega$ (or 220kΩ for $A_v = 23$)

### Example 3: Summing Amplifier

**Given:** $v_A = 1V$, $v_B = 2V$, $v_C = -1V$
$R_A = R_B = R_C = 10k\Omega$, $R_f = 10k\Omega$

**Find:** $v_o$

**Solution:**
$v_o = -\left(\frac{R_f}{R_A}v_A + \frac{R_f}{R_B}v_B + \frac{R_f}{R_C}v_C\right)$
$v_o = -\left(\frac{10k}{10k}(1) + \frac{10k}{10k}(2) + \frac{10k}{10k}(-1)\right)$
$v_o = -(1 + 2 - 1) = -2V$

**Answer:** $v_o = -2V$

### Example 4: Slew Rate Check

**Given:** Op-amp with $SR = 0.5V/\mu s$, $f = 10kHz$, $V_{om} = 10V$

**Determine:** Will slew rate limiting occur?

**Solution:**
$\text{Required rate} = 2\pi f V_{om} = 2\pi(10^4)(10) = 628,318 V/s = 0.628 V/\mu s$
$\text{Since } 0.628 > 0.5, \text{ YES, slew rate limiting will occur}$

**Answer:** Slew rate limiting will occur; reduce amplitude or frequency

### Example 5: Bandwidth Calculation

**Given:** $f_t = 1MHz$, $A_{CL} = 100$

**Find:** Closed-loop bandwidth

**Solution:**
$f_{CL} = \frac{f_t}{A_{CL}} = \frac{1MHz}{100} = 10kHz$

**Answer:** $f_{CL} = 10kHz$

---

## 15. Conclusion

This comprehensive guide covers the fundamental theory, practical analysis methods, and real-world applications of operational amplifiers. Key takeaways:

1. **Golden Rules:** $v_+ = v_-$ and $i_+ = i_- = 0$ (with negative feedback)
2. **Analysis Method:** Apply summing-point constraint, then use KCL and Ohm's Law
3. **Configuration Selection:** Choose based on input impedance needs and phase requirements
4. **Real-World Limitations:** Always check saturation, bandwidth, and slew rate
5. **Design Approach:** Select configuration → choose resistors → verify performance

**Further Study:**
- Op-amp datasheets and application notes
- Active filter design
- Precision analog design
- High-speed amplifier techniques
- Noise analysis and reduction

**Recommended References:**
- "Op Amps for Everyone" (Texas Instruments)
- "The Art of Electronics" by Horowitz and Hill
- Manufacturer application notes (Analog Devices, Texas Instruments, Linear Technology)

---

*End of Comprehensive Op-Amp Reference Guide*