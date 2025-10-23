# Comprehensive Operational Amplifier Circuit Guide

## Introduction

An operational amplifier (op-amp) is a high-gain differential amplifier that amplifies the difference between two input signals. Op-amps are versatile building blocks in analog electronics, historically used to perform mathematical operations such as addition, subtraction, integration, and differentiation in analog computers.

### Ideal Op-Amp Characteristics

- **Infinite input impedance** (Zin = ∞): No current flows into the input terminals
- **Infinite open-loop gain** (AOL = ∞): Amplifies differential input voltage to maximum
- **Zero output impedance** (Zout = 0): Can drive any load without voltage drop
- **Zero gain for common-mode signals**: Rejects signals common to both inputs
- **Infinite bandwidth**: Responds equally to all frequencies

### Fundamental Analysis Principle: Summing-Point Constraint

Due to infinite open-loop gain and negative feedback:
- **v+ \approx v-** (differential input voltage \approx 0)
- **i+ = i- = 0** (no current flows into input terminals)

### General Output Equation

$$v_o = A_{OL}(v_+ - v_-)$$

Where:
- vo = output voltage
- AOL = open-loop gain (typically 10⁵ to 10⁶)
- v+ = voltage at non-inverting input
- v- = voltage at inverting input

---

## 1. Inverting Amplifier

### Description
Produces an inverted and amplified version of the input signal. The output is 180° out of phase with the input.

### Circuit Configuration
- Input signal applied to inverting terminal (-) through resistor R1
- Non-inverting terminal (+) connected to ground
- Feedback resistor Rf (or R2) from output to inverting input

### Key Equations

**Closed-Loop Voltage Gain:**
$$A_v = -\frac{R_f}{R_1} = -\frac{R_2}{R_1}$$

**Output Voltage:**
$$v_o = -\frac{R_f}{R_1} \cdot v_{in}$$

**Input Impedance:**
$$Z_{in} = R_1$$

**Output Impedance:**
$$Z_{out} \approx 0$$

### Characteristics
- Gain magnitude controlled by resistor ratio
- Input impedance equals R1 (relatively low)
- Phase inversion (180°)
- Virtual ground at inverting input

---

## 2. Non-Inverting Amplifier

### Description
Produces an amplified version of the input signal with no phase inversion. Output is in phase with input.

### Circuit Configuration
- Input signal applied to non-inverting terminal (+)
- Inverting terminal (-) connected to voltage divider (R1 and R2)
- Feedback from output through R2 to inverting input

### Key Equations

**Closed-Loop Voltage Gain:**
$$A_v = 1 + \frac{R_2}{R_1} = 1 + \frac{R_f}{R_1}$$

**Output Voltage:**
$$v_o = \left(1 + \frac{R_2}{R_1}\right) \cdot v_{in}$$

**Input Impedance:**
$$Z_{in} \approx \infty$$ (very high, typically MΩ range)

**Output Impedance:**
$$Z_{out} \approx 0$$

### Characteristics
- Always has gain \geq 1
- Very high input impedance
- No phase inversion
- Ideal for buffering high-impedance sources

---

## 3. Voltage Follower (Buffer)

### Description
A special case of the non-inverting amplifier with unity gain (Av = +1). Provides impedance transformation without gain.

### Circuit Configuration
- Input signal applied to non-inverting terminal (+)
- Output directly connected to inverting terminal (-) (100% feedback)
- Equivalent to R2 = 0 and R1 = ∞ in non-inverting configuration

### Key Equations

**Voltage Gain:**
$$A_v = +1$$

**Output Voltage:**
$$v_o = v_{in}$$

**Input Impedance:**
$$Z_{in} \approx \infty$$ (extremely high)

**Output Impedance:**
$$Z_{out} \approx 0$$ (extremely low)

### Applications
- Impedance matching and isolation
- Buffering high-impedance sources
- Preventing loading effects
- Driving low-impedance loads

---

## 4. Summing Amplifier (Adder)

### Description
A special type of inverting amplifier that produces an output equal to the weighted sum of multiple input voltages. Can have two or more inputs.

### Circuit Configuration
- Multiple inputs (vA, vB, vC, ...) each through input resistors (RA, RB, RC, ...)
- All input resistors connect to inverting terminal (-)
- Non-inverting terminal (+) grounded
- Feedback resistor Rf from output to inverting input

### Key Equations

**Output Voltage (General):**
$$v_o = -\left(\frac{R_f}{R_A}v_A + \frac{R_f}{R_B}v_B + \frac{R_f}{R_C}v_C + ...\right)$$

**Two-Input Summer:**
$$v_o = -\left(\frac{R_f}{R_A}v_A + \frac{R_f}{R_B}v_B\right)$$

**Equal Resistors (Averaging):**
If RA = RB = RC = ... = Rf:
$$v_o = -(v_A + v_B + v_C + ...)$$

**Weighted Average:**
If RA = RB = RC = ... = R and Rf = R/n:
$$v_o = -\frac{1}{n}(v_A + v_B + ... + v_n)$$

### Applications
- Audio mixing
- Digital-to-analog conversion (DAC)
- Analog signal processing
- Weighted averaging

---

## 5. Differential Amplifier (Subtractor)

### Description
Amplifies the difference between two input signals while rejecting common-mode signals. Fundamental op-amp operation.

### Circuit Configuration
- Input v1 applied to non-inverting terminal (+) through R3
- Input v2 applied to inverting terminal (-) through R1
- Feedback resistor R2 from output to inverting input
- R4 from non-inverting terminal to ground

### Key Equations

**Output Voltage (Matched Resistors):**
When R4/R3 = R2/R1:
$$v_o = \frac{R_2}{R_1}(v_1 - v_2)$$

**Differential Gain:**
$$A_d = \frac{R_2}{R_1}$$

**General Output (Unmatched Resistors):**
$$v_o = \left(1 + \frac{R_2}{R_1}\right)\frac{R_4}{R_3 + R_4}v_1 - \frac{R_2}{R_1}v_2$$

**Matching Condition for Pure Subtraction:**
$$\frac{R_4}{R_3} = \frac{R_2}{R_1}$$

### Characteristics
- Common-mode rejection when properly balanced
- Used with sensors and measurement systems
- Can provide gain while subtracting
- Sensitive to resistor matching

---

## 6. Instrumentation Amplifier

### Description
A specialized, high-performance differential amplifier with very high input impedance, high common-mode rejection ratio (CMRR), and adjustable gain.

### Circuit Configuration
- Three op-amp design (two input buffers + difference amplifier)
- Two non-inverting amplifiers as input stage
- One differential amplifier as output stage
- Single resistor (RG) sets gain

### Key Equations

**Voltage Gain:**
$$A_v = 1 + \frac{2R}{R_G}$$

Where R is the matched input stage resistors and RG is the gain-setting resistor.

**Output Voltage:**
$$v_o = A_v(v_1 - v_2)$$

**Input Impedance:**
$$Z_{in} \approx \infty$$ (extremely high, typically GΩ range)

### Characteristics
- Extremely high input impedance
- Excellent CMRR (>100 dB typical)
- Low offset and drift
- Single resistor gain adjustment
- Ideal for sensor and biomedical applications

### Applications
- Strain gauge measurements
- Thermocouple amplification
- Medical instrumentation (ECG, EEG)
- Industrial process control

---

## 7. Integrator

### Description
Performs mathematical integration of the input signal with respect to time. Output voltage is proportional to the time integral of the input.

### Circuit Configuration
- Input through resistor R to inverting terminal (-)
- Capacitor C in feedback path (instead of resistor)
- Non-inverting terminal (+) grounded

### Key Equations

**Output Voltage:**
$$v_o(t) = -\frac{1}{RC}\int_0^t v_{in}(\tau) \, d\tau + v_o(0)$$

**Transfer Function (Frequency Domain):**
$$H(j\omega) = \frac{V_o(j\omega)}{V_{in}(j\omega)} = -\frac{1}{j\omega RC}$$

**For Constant Input:**
$$v_o(t) = -\frac{v_{in}}{RC} \cdot t + v_o(0)$$

**Time Constant:**
$$\tau = RC$$

### Characteristics
- Output is running time integral of input
- Phase shift of -90° relative to input
- Gain increases at low frequencies (1/f response)
- Susceptible to DC offset and drift
- May require reset switch across capacitor

### Applications
- Waveform generation (triangle from square wave)
- Analog computation
- Signal processing
- Active filters

---

## 8. Differentiator

### Description
Performs mathematical differentiation of the input signal. Output voltage is proportional to the rate of change of the input.

### Circuit Configuration
- Input through capacitor C to inverting terminal (-)
- Resistor R in feedback path
- Non-inverting terminal (+) grounded

### Key Equations

**Output Voltage:**
$$v_o(t) = -RC \frac{dv_{in}(t)}{dt}$$

**Transfer Function (Frequency Domain):**
$$H(j\omega) = \frac{V_o(j\omega)}{V_{in}(j\omega)} = -j\omega RC$$

**Time Constant:**
$$\tau = RC$$

### Characteristics
- Output proportional to rate of change of input
- Phase shift of +90° relative to input
- Gain increases at high frequencies
- Amplifies high-frequency noise
- Often unstable without modifications
- Usually requires additional resistor in series with C for stability

### Applications
- Waveshaping
- Frequency emphasis
- Edge detection
- Signal processing

---

## 9. Active Filters

### Description
Filters built using op-amps, resistors, and capacitors that actively shape frequency response. Offer superior performance compared to passive RC filters.

### Types

#### Low-Pass Filter
Passes low frequencies, attenuates high frequencies.

**First-Order Transfer Function:**
$$H(s) = \frac{A_0}{1 + s/\omega_c}$$

Where ωc = cutoff frequency = 1/RC

#### High-Pass Filter
Passes high frequencies, attenuates low frequencies.

**First-Order Transfer Function:**
$$H(s) = \frac{A_0 \cdot s/\omega_c}{1 + s/\omega_c}$$

#### Band-Pass Filter
Passes frequencies within a specific range.

#### Band-Reject (Notch) Filter
Attenuates frequencies within a specific range.

### Sallen-Key Topology

A popular second-order active filter configuration:

**Cutoff Frequency:**
$$f_c = \frac{1}{2\pi\sqrt{R_1R_2C_1C_2}}$$

**Quality Factor (Q):**
$$Q = \frac{\sqrt{R_1R_2C_1C_2}}{C_2(R_1 + R_2)}$$

### Advantages of Active Filters
- No inductor required (smaller, cheaper)
- Gain available in passband
- Good isolation between stages
- Adjustable Q and gain
- Better performance than passive filters

---

## Additional Amplifier Classifications

### Based on Input/Output Impedance

| Type | Input Impedance | Output Impedance | Input Senses | Output Produces |
|------|-----------------|------------------|--------------|-----------------|
| **Voltage Amplifier** | Infinite | Zero | Voltage | Voltage |
| **Current Amplifier** | Zero | Infinite | Current | Current |
| **Transconductance Amplifier** | Infinite | Infinite | Voltage | Current |
| **Transresistance Amplifier** | Zero | Zero | Current | Voltage |

### Operational Transconductance Amplifier (OTA)

A special op-amp that accepts input voltage and produces output current.

**Key Characteristic:**
$$i_{out} = g_m \cdot v_{in}$$

Where gm is transconductance (typically adjustable)

**Properties:**
- Very large output impedance (ideally infinite)
- Output current independent of load
- Used in voltage-controlled amplifiers and filters
- Common in analog synthesizers

---

## Practical Considerations

### Saturation and Clipping
Output voltage is limited by supply voltages:
$$V_{EE} < v_o < V_{CC}$$

Typically: vo(max) \approx VCC - 1V to 2V (depending on op-amp type)

### Slew Rate
Maximum rate of change of output voltage:
$$SR = \frac{dv_o}{dt}\Big|_{max}$$ (typically in V/μs)

Limits high-frequency, large-amplitude operation.

### Gain-Bandwidth Product (GBW)
$$GBW = A_v \cdot f_{-3dB} = \text{constant}$$

As closed-loop gain increases, bandwidth decreases proportionally.

### Input Offset Voltage
Small DC voltage that appears at output even with zero input. Can be nulled using trim potentiometer.

### Common-Mode Rejection Ratio (CMRR)**
$$CMRR = 20\log_{10}\left(\frac{A_d}{A_{cm}}\right) \text{ dB}$$

Measure of ability to reject common-mode signals.

---

## Summary

Operational amplifiers are fundamental building blocks enabling:
- Precision amplification with controlled gain
- Mathematical operations (sum, difference, integration, differentiation)
- Active filtering and signal conditioning
- Impedance transformation and buffering
- High-performance instrumentation

Understanding these configurations and their equations is essential for analog circuit design and analysis.