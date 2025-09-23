---
title: Diode Fundamentals Roadmap Chat
type: docs
prev: ee_302/exam_1_roadmap_chat
next: ee_302/exam_1_roadmap_notebookLM
sidebar:
  open: true
math: true
---


# High-Level Topics, Context, Subtopics, Example Problems, and Methodologies

---

## I. Diode Fundamentals and Models (Diodes, Piecewise Linear)

**Key Equations & Concepts:**

* **Shockley Equation (exact I–V law):**

  $$
  i_D = I_S \Big(e^{\tfrac{v_D}{nV_T}} - 1\Big)
  $$
* **Thermal voltage:**

  $$
  V_T = \frac{kT}{q} \approx 25\ \text{mV at 300 K}
  $$
* **Dynamic resistance (small-signal):**

  $$
  r_d = \frac{nV_T}{I_D}
  $$
* **Piecewise-linear approximation:**

  $$
  v_D \approx V_\gamma + i_D R_D
  $$

---

## II. Load-Line Analysis

**Key Equations & Concepts:**

* **KVL (linear circuit + diode):**

  $$
  V_{SS} = R i_D + v_D
  $$
* **Thévenin form:**

  $$
  V_T = R_T i_D + v_D
  $$
* **Q-point (operating point):** simultaneous solution of device law and load line:

  $$
  i_D = f(v_D), \quad v_D = V_T - R_T i_D
  $$

---

## III. Diode Application Circuits (Rectifiers, Clippers, Clamps)

**Key Equations & Concepts:**

* **Half-wave rectifier:**

  $$
  v_o(t) = 
  \begin{cases}
  v_{in}(t) - V_\gamma & v_{in}(t) > V_\gamma \\
  0 & v_{in}(t) \leq V_\gamma
  \end{cases}
  $$
* **Full-wave rectifier PIV:**

  * Center-tap: \$\text{PIV} = V\_m\$
  * Bridge: \$\text{PIV} = 2V\_m\$
* **Ripple voltage (capacitor filter):**

  * Half-wave: \$V\_{r(pp)} \approx \tfrac{I\_L}{fC}\$
  * Full-wave: \$V\_{r(pp)} \approx \tfrac{I\_L}{2fC}\$
* **Clamper output:**

  $$
  v_{out}(t) \approx v_{in}(t) + V_{bias}
  $$

---

## IV. Amplifier DC Analysis (Bias Circuits) and Small-Signal Analysis

**Key Equations & Concepts:**

* **BJT active region:**

  $$
  I_C = \beta I_B, \quad V_{BE} \approx 0.7\ \text{V}
  $$
* **Collector-emitter voltage:**

  $$
  V_{CE} = V_{CC} - I_C R_C
  $$
* **Small-signal parameters:**

  * Input resistance: \$r\_\pi = \tfrac{\beta V\_T}{I\_C}\$
  * Transconductance: \$g\_m = \tfrac{I\_C}{V\_T}\$
  * Output current: \$i\_c = g\_m v\_{be}\$
* **MOSFET saturation region:**

  $$
  I_D = \tfrac{1}{2} k' \tfrac{W}{L} (V_{GS} - V_T)^2
  $$

---

## V. Operational Amplifiers (Op Amps)

**Key Equations & Concepts:**

* **Ideal constraints:**

  $$
  v^+ = v^-, \quad i^+ = i^- = 0
  $$
* **Inverting gain:**

  $$
  A_v = -\tfrac{R_f}{R_{in}}
  $$
* **Noninverting gain:**

  $$
  A_v = 1 + \tfrac{R_f}{R_{in}}
  $$
* **Summing amplifier:**

  $$
  v_{out} = -R_f \left(\frac{v_1}{R_1} + \frac{v_2}{R_2} + \dots \right)
  $$

---

## VI. Piecewise Linear Models

**Key Equations & Concepts:**

* **Segment approximation:**

  $$
  v_D = V_\gamma + i_D R_D
  $$
* Equivalent circuit: constant drop \$V\_\gamma\$ + series resistance \$R\_D\$.

---

## VII. Clipper Circuits and Clamp Circuits (Wave-Shaping Details)

**Key Equations & Concepts:**

* **Clipper transfer:**

  $$
  v_{out} =
  \begin{cases}
  V_{clip} & v_{in} > V_{clip} \\
  v_{in} & |v_{in}| \leq V_{clip} \\
  -V_{clip} & v_{in} < -V_{clip}
  \end{cases}
  $$
* **Clamp capacitor charge:**

  $$
  V_C \approx V_{peak} - V_D
  $$
* **Clamp output (steady state):**

  $$
  v_{out}(t) \approx v_{in}(t) \pm V_C
  $$
