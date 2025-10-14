# List of Operational Amplifier (Op-Amp) Types and Configurations

- inverting
- non-inverting
- voltage follower
- differential amplifier
- instrumentation amplifier
- summing amplifier
- integrator


----------------



The sources describe Operational Amplifiers (op-amps) primarily through their characteristics and the common circuit configurations built using them.

## Types and Applications of Operational Amplifier Circuits

An operational amplifier is fundamentally a **High Gain differential amplifier** that amplifies the **difference** between two input signals. Historically, op-amps were used in analog-computer circuits to perform mathematical operations such as **addition, subtraction, integration, and differentiation**.

Op-amps are almost always used with **negative feedback**, where part of the output signal is returned to the input in opposition to the source signal. This configuration allows for predictable and controlled circuit behavior.

The sources extensively detail the following types of op-amp circuit configurations:

| Op-Amp Type/Configuration | Purpose/Use | How It Works (Principle/Gain) |
| :--- | :--- | :--- |
| **Inverting Amplifier (Basic Inverter)** | Used to produce an output signal that is an **inverted version** of the input waveform. The output is 180 degrees out of phase with the input signal. | The input is applied to the inverting terminal ('-'). Its closed-loop voltage gain ($A_v$) is derived using a feedback resistor ($R_f$ or $R_2$) and input resistor ($R_1$). For an ideal op-amp, $A_v = -R_2/R_1$. |
| **Noninverting Amplifier** | Used to produce an output signal that is a **noninverting version** of the input waveform. The output signal is in phase with the input signal. | The input signal is applied to the non-inverting terminal ('+'). The closed-loop voltage gain is determined by resistors $R_1$ and $R_2$. For an ideal op-amp, $A_v = 1 + R_2/R_1$. |
| **Differential Amplifier (Subtractor)** | Performs subtraction/amplification of the **difference** between two input signals ($v_1$ and $v_2$). Widely used in engineering instrumentation, including along with sensors. | Ideally, the output voltage is proportional to the difference between the input voltages ($v_1 - v_2$) multiplied by a differential gain ($A_d$). Output voltage $v_o$ is proportional to $(v_1 - v_2)R_2/R_1$, assuming $R_4/R_3 = R_2/R_1$. |
| **Summing Amplifier (Summer)** | Used to create an output voltage that is a weighted sum of multiple input voltages. It is a special type of inverting amplifier. | The output voltage is given by $v_o = -(R_f/R_A)v_A - (R_f/R_B)v_B$. |
| **Voltage Follower** | Provides unity voltage gain ($A_v = +1$). Often used to achieve high input impedance . | A noninverting configuration where typically $R_2 = 0$ and $R_1$ is an open circuit. |
| **Integrator** | Used to perform integration of the input signal. | Produces an output voltage proportional to the **running time integral** of the input voltage. |
| **Differentiator** | Used to perform differentiation of the input signal. | Produces an output voltage proportional to the **time derivative** of the input voltage. |
| **Active Filters** | Designed to pass input components with frequencies in one range to the output while rejecting components in other ranges. Active filters often have better performance than passive filters. | Circuits composed of op-amps, resistors, and capacitors. An active Butterworth lowpass filter can be achieved by cascading several Sallen-Key circuits having the proper gains. |

## Specialized and Ideal Amplifier Types

### Instrumentation Amplifiers
The **instrumentation amplifier** is a specific, high-performance differential amplifier. It is used in practical cases dealing with **very small input voltages** coming from sensors. The main advantage of this amplifier is its **very high input impedance**, which is particularly useful when working with sensors.

### Operational Transconductance Amplifier (OTA)
The OTA is a special type of op-amp that functions as a **transconductance amplifier**. It accepts input voltage and produces output current. The primary characteristic distinguishing it from an ideal op-amp voltage amplifier is its **very large output resistance** (ideally infinite).

### Ideal Amplifier Classifications (Based on Impedance)
Amplifiers are often characterized by how they handle input and output impedance, leading to four ideal classifications:

1.  **Ideal Voltage Amplifier:** Has infinite input impedance and zero output impedance. It senses the open-circuit voltage of the source and produces an amplified voltage across the load regardless of load impedance.
2.  **Ideal Current Amplifier:** Has zero input impedance and infinite output impedance. It senses the short-circuit current of the source and forces an amplified version of this current to flow through the load.
3.  **Ideal Transconductance Amplifier:** Has infinite input impedance and infinite output impedance. It senses the open-circuit voltage of the source and forces a proportional current through the load.
4.  **Ideal Transresistance Amplifier:** Has zero input impedance and zero output impedance. It senses the short-circuit current of the source and causes a proportional voltage across the load.

## How Operational Amplifiers Work (Ideal and General Principles)

The operational amplifier operates as a **differential amplifier**. When ideal, it has the following characteristics:

*   **Infinite input impedances**. This means the input current for both terminals is zero.
*   **Infinite gain** for the differential input signal (open-loop gain, $A_{OL}$).
*   **Zero gain** for the common-mode input signal.
*   **Zero output impedance**.
*   **Infinite bandwidth**.

Because the open-loop gain is ideally infinite, when negative feedback is applied, a very tiny input voltage difference is needed to produce the required output voltage. This leads to the fundamental analysis tool known as the **summing-point constraint**: the differential input voltage and the input current of the op-amp are assumed to be forced to zero.

In reality, op-amps have finite characteristics (e.g., gain is $10^5$ to $10^6$). The output voltage is restricted by the **biasing voltages** applied to the op-amp. If the input signal is too large, the output will reach saturation limits (clipping) near the positive or negative supply voltages ($V_{CC}$ and $V_{EE}$).

The output voltage ($v_o$) is equal to the open-loop gain ($A_{OL}$) multiplied by the difference between the input signals ($v_1 - v_2$):
$$v_o = A_{OL}(v_1 - v_2) \text{}$$

In practical circuits using negative feedback, a fraction of the output is returned to the inverting input terminal, forcing the differential input voltage toward zero. If the op-amp uses the non-inverting terminal, the output is in phase with the input. If the op-amp uses the inverting terminal, the output is inverted by 180 degrees with respect to the input.