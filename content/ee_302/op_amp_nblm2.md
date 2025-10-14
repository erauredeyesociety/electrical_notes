This is a comprehensive overview of the functional differences between non-inverting and inverting operational amplifier (op amp) circuits, the definitions of differential and common-mode signals, and the concept of gain expressed in voltage ratio and decibels.

***

### Functional Differences Between Non-Inverting and Inverting Op Amp Circuits

Operational amplifiers are fundamentally differential amplifiers that amplify the difference between their two input terminals. They are almost always used with **negative feedback**. When used in closed-loop configurations with resistive feedback, the primary functional difference lies in the **phase relationship** between the input and output signals, and the way the voltage gain is calculated.

| Feature | Inverting Amplifier | Non-Inverting Amplifier |
| :--- | :--- | :--- |
| **Input Connection** | Applied to the **inverting terminal** (marked '-'). | Applied to the **non-inverting terminal** (marked '+'). |
| **Gain Polarity** | **Negative** voltage gain ($A_v$). | **Positive** voltage gain ($A_v$). |
| **Phase Relationship** | Output waveform is an **inverted version** (180° phase shift) of the input waveform. | Output waveform is **in phase** (non-inverted) with the input waveform. |
| **Closed-Loop Gain ($A_v$)** | $A_v = -R_2/R_1$. | $A_v = 1 + R_2/R_1$. |
| **Input Impedance (Ideal)** | Equal to the input resistor $R_1$. | **Infinite** ($R_{in} = \infty$). |
| **Minimum Gain** | Can be less than 1 (e.g., -0.5). | **Unity** (minimum gain magnitude is 1), typically implemented as a voltage follower. |

The negative gain in the inverting configuration means that the output voltage is an inverted version of the input. This may not matter for signals like monaural audio, but it is critical for applications like video signals where inversion leads to a negative image.

The non-inverting amplifier, under ideal op amp assumptions, is classified as an **ideal voltage amplifier**. This is because it theoretically possesses infinite input impedance and zero output impedance.

***

### Common-Mode Signal and Differential Signal

The operational amplifier is defined as a **differential amplifier** because its core function is to amplify the difference between its two input terminals. The inputs to a differential amplifier, $v_1$ (non-inverting input) and $v_2$ (inverting input), can be decomposed into a differential signal and a common-mode signal.

#### 1. Differential Signal ($v_{id}$ or $v_d$)
The differential signal is the **difference between the two input voltages**:
$$v_{id} = v_1 - v_2$$.

In instrumentation systems, the differential signal is typically the **signal of interest**. An ideal differential amplifier produces an output voltage proportional only to this differential signal.

#### 2. Common-Mode Signal ($v_{cm}$ or $v_{icm}$)
The common-mode signal is the **average of the input voltages**:
$$v_{icm} = \frac{1}{2}(v_1 + v_2)$$.

The common-mode signal usually represents **unwanted noise**. For example, when recording an electrocardiogram (ECG), a large 60-Hz common-mode signal may be present due to the power system ground, even though the desired heart signal is differential.

An ideal op amp has **zero gain** for the common-mode input signal. Real differential amplifiers, however, respond to both signals.

#### Common-Mode Rejection Ratio (CMRR)
The effectiveness of a differential amplifier in rejecting the unwanted common-mode signal is quantified by the **Common-Mode Rejection Ratio (CMRR)**. The CMRR is defined as the ratio of the magnitude of the differential gain ($A_d$) to the magnitude of the common-mode gain ($A_{cm}$):
$$\text{CMRR} = \frac{|A_d|}{|A_{cm}|}$$.

A large CMRR is critical when amplifying a small differential signal in the presence of a strong common-mode interfering signal.

***

### Understanding Gain in Terms of Voltage Gain and dB

#### Voltage Gain ($A_v$)
Voltage gain is a fundamental characteristic of an amplifier. Ideally, an amplifier produces an output signal with the identical waveshape as the input signal, but with a larger amplitude.

The voltage gain ($A_v$) is the **constant** that relates the output voltage $v_o(t)$ to the input voltage $v_i(t)$:
$$v_o(t) = A_v v_i(t)$$.

When analyzing signals that vary with frequency (sinusoidal input signals), the more general definition is **complex gain**. Complex voltage gain ($A_v$) is defined as the ratio of the phasor for the output signal ($V_o$) to the phasor for the input signal ($V_i$):
$$A_v = \frac{V_o}{V_i}$$.

Complex gain is a complex quantity that includes both **magnitude** and **phase**.

#### Gain in Decibels (dB)
Gain magnitudes (or transfer function magnitudes) are frequently expressed in **decibels (dB)**.

To convert a transfer function magnitude (or gain magnitude) to decibels, you take **20 times the common logarithm of the magnitude**:
$$|A_v|_{\text{dB}} = 20 \log |A_v|$$.

Decibels are particularly advantageous for creating Bode plots, which plot the gain magnitude versus frequency on a logarithmic scale.

Key relationships concerning decibels include:
*   A magnitude of **unity gain** ($|A_v| = 1$) corresponds to **0 dB**.
*   The half-power frequencies (or 3-dB frequencies) are points where the gain magnitude is $1/\sqrt{2} \approx 0.707$ times the midband value, and the gain expressed in decibels is approximately **3 dB lower** than the midband gain.
*   Specifications like the Common-Mode Rejection Ratio (CMRR) are also frequently expressed in decibels.