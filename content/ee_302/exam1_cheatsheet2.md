---
title: Exam 1 Cheat Sheet
type: docs
prev: ee_300/
next: ee_300/exam_2_roadmap_notebookLM
sidebar:
  open: true
math: true
---

### Step-by-Step Methodology: Ideal Diode Analysis

The ideal diode model treats the diode as a perfect conductor (short circuit) in the forward direction and an open circuit in the reverse direction, assuming the forward voltage drop and reverse current are negligible.

1.  **Assume Diode States:** Assume a state for each diode, either **ON** or **OFF**.
    *   For $n$ diodes, consider $2^n$ possible combinations of diode states. Try to guess with your best judgment, considering the source direction.
2.  **Replace Diodes:** Redraw the circuit by replacing the assumed diode states with their linear equivalents:
    *   **ON** diodes $\rightarrow$ Short circuit ($V_D = 0$).
    *   **OFF** diodes $\rightarrow$ Open circuit ($I_D = 0$).
3.  **Analyze Circuit:** Analyze the resulting linear circuit using techniques like Kirchhoff’s laws and Ohm’s law to determine the following for each diode:
    *   Current ($I_D$) through the diodes assumed to be **ON**.
    *   Voltage ($V_D$) across the diodes assumed to be **OFF**.
4.  **Check Constraints:** Check to see if the calculated results are consistent with the assumed state for each diode:
    *   For **ON** diodes: Current must flow in the forward direction ($I_D > 0$).
    *   For **OFF** diodes: The voltage must be reverse biased ($V_D < 0$), or positive at the cathode.
5.  **Validate or Iterate:**
    *   If the results are consistent with the assumed states, the analysis is finished.
    *   Otherwise, return to step 1 and choose a different combination of diode states.
    *   *Note:* In general, you cannot decide on the state of a particular diode until a combination works for all the diodes in the circuit.

---

### Step-by-Step Methodology: Load-Line Method

The load-line analysis technique is a graphical method used to analyze nonlinear circuits, such as those involving diodes or BJT amplifiers.

1.  **Simplify the Circuit:** If the circuit contains multiple linear elements connected to the nonlinear device (the load), replace the network external to the nonlinear device with its Thévenin equivalent circuit ($V_{TH}$ and $R_{TH}$).
2.  **Apply KVL (Derive Load Line Equation):** Apply Kirchhoff's Voltage Law (KVL) to the simplified circuit loop containing the nonlinear device. This yields a linear equation (the load line equation) relating the device voltage ($v_D$) and device current ($i_D$).
    *   *Notable Equation (Example Diode Circuit):* $V_{SS} = R i_D + v_D$
3.  **Plot the Load Line:** Plot this linear KVL equation on the same set of axes used for the nonlinear device’s experimentally obtained volt–ampere characteristic.
    *   Determine two points to plot the straight line:
        *   The voltage axis intercept (where $i_D = 0$): $v_D = V_{SS}$
        *   The current axis intercept (where $v_D = 0$): $i_D = \frac{V_{SS}}{R}$
4.  **Determine the Operating Point (Q-Point):** The **operating point** is the intersection of the load line and the device characteristic curve. This point represents the simultaneous solution of the circuit.
5.  **Read Results:** Read the quiescent voltage ($V_{DQ}$) and current ($I_{DQ}$) at the operating point from the plot.

---

### Step-by-Step Methodology: Clipper Circuits

Clipper circuits are wave-shaping circuits that limit the output waveform by removing the portion of the input voltage that falls above or below a specified level.

1.  **Identify Clipping Levels (Breakpoints):** Determine the critical input voltage levels ($V_{in}$) where the diodes change state (turn ON, OFF, or enter Zener breakdown).
    *   Account for the diode forward voltage drop (e.g., $0.6$ V or $0.7$ V) or the Zener breakdown voltage ($V_Z$).
2.  **Define Operating Regions:** Analyze the circuit across different ranges of $V_{in}$ corresponding to the possible combinations of diode states.
    *   Typically, analyze the negative cycle and positive cycle of $V_{in}$ separately.
3.  **Analyze Linear Regions:** For each defined operating region, treat the diodes as linear elements (short circuit, open circuit, or voltage source/resistor combination, depending on the diode model used).
4.  **Calculate Output Voltage ($V_{out}$):** Use KVL, KCL, and Ohm’s law to determine the relationship between $V_{out}$ and $V_{in}$ for each region.
    *   In regions where diodes are OFF, the slope of the transfer characteristic ($V_{out}$ vs. $V_{in}$) is often 1, meaning $V_{out} = V_{in}$
    *   In regions where diodes are ON (clipping), $V_{out}$ is generally limited to a constant voltage determined by the limiting elements (batteries, Zener diodes, and forward drops).
5.  **Sketch Results:** Sketch the transfer characteristics ($V_{out}$ versus $V_{in}$) or the output waveform ($v_o(t)$) for a given input waveform $v_{in}(t)$

---

### Step-by-Step Methodology: Rectifier Circuits

Rectifiers convert AC power into DC power, forming the basis for electronic power supplies.

1.  **Determine Diode Conduction Cycles:** Based on the rectifier configuration (half-wave, full-wave bridge, or center-tapped), determine which diodes conduct current during the positive and negative half-cycles of the AC source voltage, $v_s(t)$
2.  **Analyze Forward Bias:** When the source voltage causes a diode to be forward biased:
    *   For an **Ideal Diode**: The output voltage across the load ($v_o(t)$) equals the source voltage.
    *   For an **Actual Diode**: The output voltage is typically reduced by the forward voltage drop, $V_f \approx 0.7$ V.
3.  **Analyze Reverse Bias:** When the source voltage causes the diodes to be reverse biased:
    *   For a resistive load, current flow stops, and $v_o(t)$ drops to zero (for half-wave).
4.  **Calculate Peak Inverse Voltage (PIV):** Determine the maximum reverse voltage that appears across the non-conducting diodes.
    *   For a half-wave rectifier with a resistive load, PIV $= V_m$ (peak source voltage).
    *   For a full-wave center-tapped rectifier, PIV $\approx 2 V_m$
5.  **Analyze Circuits with Smoothing Capacitors (If Applicable):** If a capacitor ($C$) is placed in parallel with the load to smooth the voltage (reducing ripple $V_r$), calculate the required capacitance or the average load voltage.
    *   *Notable Equation (Average Load Voltage with Capacitor):* $V_L \cong V_m - \frac{V_r}{2}$
    *   *Notable Equation (Capacitance for Half-Wave Rectifier):* $C \cong \frac{I_L T}{V_r}$
    *   *Notable Equation (Capacitance for Full-Wave Rectifier):* $C = \frac{I_L T}{2 V_r}$
        *Where $I_L$ is the average load current, $T$ is the period, and $V_r$ is the peak-to-peak ripple voltage.*