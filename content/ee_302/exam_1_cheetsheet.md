---
title: Exam 1 Cheat Sheet
type: docs
prev: ee_300/
next: ee_300/exam_2_roadmap_notebookLM
sidebar:
  open: true
math: true
---

* The most common type of diode, typically has a forward voltage \(0.6\text{-}7\text{V}\), so make this assumption


<!-- Vega Scripts -->
<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<!-- Render Container -->
<div id="vis"></div>

<script type="text/javascript">
var spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "width": 400,
  "height": 400,
  "layer": [
    // --- Horizontal Axis Line ---
    {
      "data": {
        "values": [{"x": -10, "x2": 10, "y": 0}]
      },
      "mark": {
        "type": "rule",
        "color": "black",
        "strokeWidth": 2
      },
      "encoding": {
        "x": {"field": "x", "type": "quantitative"},
        "x2": {"field": "x2"},
        "y": {"field": "y", "type": "quantitative"}
      }
    },
    // --- Vertical Axis Line ---
    {
      "data": {
        "values": [{"y": -10, "y2": 10, "x": 0}]
      },
      "mark": {
        "type": "rule",
        "color": "black",
        "strokeWidth": 2
      },
      "encoding": {
        "y": {"field": "y", "type": "quantitative"},
        "y2": {"field": "y2"},
        "x": {"field": "x", "type": "quantitative"}
      }
    },
    // --- Ideal Diode Curve (Piecewise Line) ---
    {
      "data": {
        "values": [
          {"Voltage": -10, "Current": 0},
          {"Voltage": 0, "Current": 0},
          {"Voltage": 0, "Current": 10}
        ]
      },
      "mark": {
        "type": "line",
        "point": true,
        "color": "red"
      },
      "encoding": {
        "x": {"field": "Voltage", "type": "quantitative"},
        "y": {"field": "Current", "type": "quantitative"}
      }
    }
  ],
  // --- Shared Axis Config ---
  "encoding": {
    "x": {
      "type": "quantitative",
      "scale": {"domain": [-10, 10]},
      "axis": {
        "title": "Voltage (V)",
        "grid": true,
        "domain": false,
        "ticks": false,
        "labelFontSize": 12
      }
    },
    "y": {
      "type": "quantitative",
      "scale": {"domain": [-10, 10]},
      "axis": {
        "title": "Current (I)",
        "grid": true,
        "domain": false,
        "ticks": false,
        "labelFontSize": 12
      }
    }
  }
};
vegaEmbed('#vis', spec);
</script>

**Following the ideal diode graph**, if you get a positive voltage you must check that your current is not negative, otherwise your guess is wrong. 

* In an ideal diode, if \(I_d\) is positive, then the voltage is zero and the diode is on. If \(V_d\) is negative and the current is zero, then we say the diode is off.

* If a diode is supposed to be on, check that the current is greater than zero. If the current is 0, it can be either on or off, so you have to check the voltage.

* If you have a current greater than 0, and a voltage greater than 0, then thats fine, because you can't have current flow without voltage. To confirm that a diode is off, you need a negative voltage. If the voltage is positive, then the diode can't be off. 

**Diode Bias** - The triangle points in the direction of the bias of the diode. the anode (positive) must have a greater voltage than the cathode (negative) so that the voltage drop does not go against the diode (current flowing against diode bias). Voltage drop being in the reverse direction of a diode bias will result in the diode being off.

* Positive side of diode is the base of the triangle, negative side is the tip of the triangle. Current only goes through a diode one way, positive to negative. If it goes negative to positive, the current becomes 0 through the diode or current stops. If current flows in the same direction of where the diode is pointing, it is on, otherwise if the current is flowing against the diode, it is off.

**Voltage Divider** - The larger the resistor, the greater the voltage drop across it. The voltage divider principle applies specifically to components that are part of a single, closed series loop, not to two components in series but on different loops.

### Step-by-Step Methodology: Ideal Diode Analysis

1. **Assume diode states:** For \(n\) diodes, consider \(2^n\) possible ON/OFF combinations
2. **Replace diodes:** ON → short circuit, OFF → open circuit
3. **Analyze linear circuit:** Calculate \(I_D\) and \(V_D\) for each diode
4. **Check constraints:**
   - ON diodes: \(I_D > 0\)
   - OFF diodes: \(V_D < 0\)
5. **Validate or iterate:** If constraints satisfied, solution found; otherwise try different states

### Step-by-Step Methodology: Load-Line Analysis

1. **Derive KVL equation:** Write voltage equation relating device voltage and current
2. **Identify intercepts:** Find voltage and current intercepts
3. **Plot load line:** Draw line on device characteristic plot
4. **Find Q-point:** Locate intersection of load line and device curve
5. **Analyze operation:** Determine voltage, current, and power at Q-point

### Step-by-Step Methodology: Wave-Shaping Analysis

1. **Identify breakpoints:** Determine input voltages where diodes change state
2. **Analyze regions:** Consider each operating region separately
3. **Apply circuit laws:** Use KVL/KCL for each diode state
4. **Construct transfer characteristic:** Plot \(V_o\) vs \(V_{in}\)
5. **Verify operation:** Check diode states are consistent with assumptions
