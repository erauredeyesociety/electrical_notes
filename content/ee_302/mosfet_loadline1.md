# Complete MOSFET Load Line Analysis Guide

## Table of Contents
1. [Introduction to Load Line Analysis](#introduction)
2. [MOSFET Operating Regions](#operating-regions)
3. [Key Equations](#key-equations)
4. [DC Load Line Construction](#dc-load-line)
5. [AC Load Line Construction](#ac-load-line)
6. [Step-by-Step Analysis Process](#step-by-step-process)
7. [Q-Point Determination](#q-point)
8. [Common Circuit Configurations](#circuit-configurations)
9. [Practice Problems](#practice-problems)

---

## 1. Introduction to Load Line Analysis {#introduction}

Load line analysis is a graphical technique used to determine the operating point (Q-point) of a MOSFET amplifier circuit. It involves plotting:
- **DC Load Line**: Represents the constraint imposed by the DC circuit on the drain-source voltage and drain current
- **AC Load Line**: Represents the constraint during signal variations when AC coupling capacitors are present
- **Device Characteristic Curves**: The iD vs. vDS curves for different gate-source voltages

The intersection of the load line with the device characteristics gives the operating point.

---

## 2. MOSFET Operating Regions {#operating-regions}

### Cutoff Region
- **Condition**: vGS < Vth (threshold voltage)
- **Characteristic**: iD ≈ 0
- **Use**: Switch OFF state

### Triode (Linear/Ohmic) Region
- **Condition**: vGS > Vth AND vDS < (vGS - Vth)
- **Equation**: iD = Kn[(vGS - Vth)vDS - vDS²/2]
- **Characteristic**: MOSFET acts like a voltage-controlled resistor
- **Use**: Switch ON state, analog switches

### Saturation (Active) Region
- **Condition**: vGS > Vth AND vDS ≥ (vGS - Vth)
- **Equation**: iD = (Kn/2)(vGS - Vth)² (1 + λvDS)
- **Characteristic**: iD is relatively independent of vDS
- **Use**: Amplifiers (most common for analog circuits)

**Note**: "Saturation" for MOSFETs corresponds to the "active" region for BJTs. This terminology difference can be confusing!

---

## 3. Key Equations {#key-equations}

### MOSFET Device Equations

**Saturation Region (Primary for amplifiers):**
```
iD = (Kn/2)(vGS - Vth)²(1 + λvDS)
```

Where:
- Kn = μnCox(W/L) = transconductance parameter
- μn = electron mobility
- Cox = gate oxide capacitance per unit area
- W/L = width-to-length ratio
- Vth = threshold voltage
- λ = channel-length modulation parameter

**Simplified (when λvDS << 1):**
```
iD = (Kn/2)(vGS - Vth)²
```

**Alternative form using K'n:**
```
iD = (K'n/2)(W/L)(vGS - Vth)²
```

**Transconductance (small-signal parameter):**
```
gm = ∂iD/∂vGS = Kn(vGS - Vth) = √(2Kn·iD)
```

**Output resistance:**
```
ro = 1/(λ·iD)
```

### DC Load Line Equations

**General form (KVL around drain-source loop):**
```
VDD = iD·RD + vDS + iD·RS
VDD = iD(RD + RS) + vDS
```

**Standard form:**
```
iD = (VDD - vDS)/(RD + RS)
```

**Key points:**
- **When vDS = 0**: iD(max) = VDD/(RD + RS)
- **When iD = 0**: vDS(max) = VDD

### AC Load Line Equations

When bypass capacitors are present (RS bypassed, coupling capacitors isolate DC):

```
iD(ac) = -vDS(ac)/(RD || RL)
```

**Slope of AC load line:**
```
Slope = -1/(RD || RL)
```

Where RD || RL means RD in parallel with RL:
```
RD || RL = (RD × RL)/(RD + RL)
```

**AC load line passes through Q-point** with slope steeper than DC load line (if RL is present).

---

## 4. DC Load Line Construction {#dc-load-line}

### Step-by-Step Process

**Step 1: Identify Circuit Components**
- VDD = supply voltage
- RD = drain resistor
- RS = source resistor
- RG = gate resistor(s)
- Any coupling/bypass capacitors (open for DC analysis)

**Step 2: Write KVL Equation**

For common-source configuration:
```
VDD = iD·RD + vDS + iD·RS
```

Rearranging:
```
iD = (VDD - vDS)/(RD + RS)
```

**Step 3: Find Two Points to Plot the Line**

**Point 1 (vDS = 0):**
```
iD = VDD/(RD + RS)
```
Plot at coordinates: (0, VDD/(RD + RS))

**Point 2 (iD = 0):**
```
vDS = VDD
```
Plot at coordinates: (VDD, 0)

**Step 4: Draw the Load Line**

Connect these two points with a straight line. This is your DC load line.

**Step 5: Determine Load Line Equation Parameters**

- **Slope**: -1/(RD + RS)
- **y-intercept**: VDD/(RD + RS)
- **x-intercept**: VDD

### Example Calculation

Given: VDD = 20V, RD = 2kΩ, RS = 1kΩ

**Point 1 (vDS = 0):**
```
iD = 20V / (2kΩ + 1kΩ) = 20V / 3kΩ = 6.67 mA
```

**Point 2 (iD = 0):**
```
vDS = 20V
```

**Load Line**: Plot (0V, 6.67mA) and (20V, 0mA), then draw a straight line between them.

---

## 5. AC Load Line Construction {#ac-load-line}

### When AC Load Line Differs from DC Load Line

The AC load line differs from the DC load line when:
1. A bypass capacitor is placed across RS (shorts RS for AC signals)
2. A load resistor RL is AC-coupled to the output
3. The DC supply VDD is effectively at AC ground

### Step-by-Step Process

**Step 1: Identify AC Equivalent Circuit**
- Capacitors: short circuit (if large enough)
- DC supply VDD: AC ground
- Effective AC load: RD || RL

**Step 2: Determine AC Load Resistance**
```
Rac = RD || RL = (RD × RL)/(RD + RL)
```

If only RD is present (no external load):
```
Rac = RD
```

**Step 3: Find AC Load Line Slope**
```
Slope = -1/Rac
```

**Step 4: AC Load Line Passes Through Q-Point**

The AC load line must pass through the Q-point (IDQ, VDSQ) with the calculated slope.

**Step 5: Draw AC Load Line**

Using point-slope form:
```
iD - IDQ = (-1/Rac)(vDS - VDSQ)
```

Or find two points:

**Point 1**: Q-point itself (VDSQ, IDQ)

**Point 2**: Choose vDS = 0, then:
```
iD = IDQ + VDSQ/Rac
```

Or choose iD = 0, then:
```
vDS = VDSQ + IDQ·Rac
```

### Example Calculation

Given: Q-point at (10V, 4mA), RD = 2kΩ, RL = 3kΩ, RS bypassed

**AC Load Resistance:**
```
Rac = (2kΩ × 3kΩ)/(2kΩ + 3kΩ) = 6kΩ/5kΩ = 1.2kΩ
```

**AC Load Line Slope:**
```
Slope = -1/1.2kΩ = -0.833 mA/V
```

**Point 1**: (10V, 4mA) [Q-point]

**Point 2** (at vDS = 0):
```
iD = 4mA + 10V/1.2kΩ = 4mA + 8.33mA = 12.33mA
```

Plot: (0V, 12.33mA) and (10V, 4mA)

---

## 6. Step-by-Step Analysis Process {#step-by-step-process}

### Complete Analysis Procedure

#### Phase 1: DC Analysis (Find Q-Point)

**Step 1: Draw DC Equivalent Circuit**
- Open all capacitors
- Keep all resistors and DC sources

**Step 2: Determine Gate-Source Voltage (vGS)**

**For Voltage-Divider Bias:**
```
VG = VDD × (R2/(R1 + R2))
VS = iD × RS
vGS = VG - VS
```

**For Fixed Bias:**
```
vGS = VGG (if separate gate supply)
```

**For Self-Bias:**
```
vGS = -iD × RS (for n-channel with source resistor)
```

**Step 3: Determine Drain Current (iD)**

Using MOSFET equation in saturation:
```
iD = (Kn/2)(vGS - Vth)²
```

For self-bias or voltage divider, this requires solving simultaneously with:
```
vGS = VG - iD·RS
```

Substituting:
```
iD = (Kn/2)(VG - iD·RS - Vth)²
```

This is a quadratic equation in iD. Solve algebraically or graphically.

**Step 4: Determine Drain-Source Voltage (vDS)**

Using KVL:
```
vDS = VDD - iD·RD - iD·RS
```

Or:
```
vDS = VDD - iD(RD + RS)
```

**Step 5: Verify Operating Region**

Check that MOSFET is in saturation:
```
vDS ≥ (vGS - Vth)
```

If not satisfied, MOSFET is in triode region—recalculate using triode equations.

**Step 6: Plot Q-Point**

Plot point (VDSQ, IDQ) on the graph with the DC load line and device curves.

#### Phase 2: AC Analysis

**Step 7: Draw AC Equivalent Circuit**
- Short all capacitors
- Replace DC supply with ground
- Replace MOSFET with small-signal model

**Step 8: Determine AC Load Line**

Calculate Rac and plot AC load line through Q-point (see Section 5).

**Step 9: Calculate Small-Signal Parameters**

**Transconductance:**
```
gm = √(2Kn·IDQ) = Kn(vGSQ - Vth)
```

**Output resistance:**
```
ro = 1/(λ·IDQ)
```

Often ro >> RD, so it's approximated as infinite.

**Step 10: Determine Voltage Gain**

**For common-source with bypassed RS:**
```
Av = -gm(RD || RL || ro) ≈ -gm(RD || RL)
```

**For common-source without bypass:**
```
Av = -gm(RD || RL)/(1 + gm·RS)
```

**Step 11: Determine Maximum Output Swing**

The AC load line limits the output swing. Find the intersection points of the AC load line with:
- The vDS = (vGS - Vth) boundary (entering triode)
- The iD = 0 axis (cutoff)

Maximum peak-to-peak swing:
```
vDS(max swing) = min(distance to cutoff, distance to triode)
```

---

## 7. Q-Point Determination {#q-point}

### Why Q-Point Matters

The Q-point (quiescent point or operating point) determines:
1. **DC operating conditions**: Where the transistor sits at rest
2. **Linearity**: Centered Q-point allows maximum symmetric swing
3. **Efficiency**: Affects power consumption and heat dissipation
4. **Distortion**: Poor placement causes clipping or nonlinearity

### Optimal Q-Point Placement

**For maximum output swing:**
- Place Q-point at the center of the DC load line
- IDQ ≈ VDD/[2(RD + RS)]
- VDSQ ≈ VDD/2

**For low distortion:**
- Ensure sufficient distance from cutoff (vGS > Vth)
- Ensure sufficient distance from triode region
- Consider AC load line boundaries

### Graphical Q-Point Determination

**Method 1: Load Line and Device Curves**
1. Plot DC load line
2. Plot iD vs. vDS curves for various vGS values
3. Determine vGS from bias circuit
4. Q-point is where vGS curve intersects load line

**Method 2: Transfer Characteristic**
1. Plot iD vs. vGS transfer curve: iD = (Kn/2)(vGS - Vth)²
2. Plot bias line (depends on biasing scheme)
3. Intersection gives IDQ and vGSQ
4. Calculate VDSQ using load line equation

### Analytical Q-Point Determination

For voltage-divider bias with RS:

**Given:** VDD, R1, R2, RD, RS, Kn, Vth

**Step 1:** Calculate VG
```
VG = VDD × R2/(R1 + R2)
```

**Step 2:** Set up equations
```
vGS = VG - iD·RS
iD = (Kn/2)(vGS - Vth)²
```

**Step 3:** Substitute and solve
```
iD = (Kn/2)(VG - iD·RS - Vth)²
```

Expand and rearrange into standard quadratic form:
```
(Kn·RS²/2)·iD² - [1 + Kn·RS(VG - Vth)]·iD + (Kn/2)(VG - Vth)² = 0
```

**Step 4:** Use quadratic formula
```
iD = {[1 + Kn·RS(VG - Vth)] ± √{[1 + Kn·RS(VG - Vth)]² - 2Kn·RS²(VG - Vth)²}} / (Kn·RS²)
```

Choose the physically meaningful solution (positive, reasonable value).

**Step 5:** Calculate remaining values
```
vGSQ = VG - IDQ·RS
VDSQ = VDD - IDQ(RD + RS)
```

---

## 8. Common Circuit Configurations {#circuit-configurations}

### Configuration 1: Voltage-Divider Bias (Most Common)

**Circuit:**
- VDD at top
- R1 from VDD to gate
- R2 from gate to ground
- RD from VDD to drain
- RS from source to ground
- Bypass capacitor CS across RS (for AC)
- Coupling capacitors at input and output

**DC Analysis:**
```
VG = VDD·R2/(R1 + R2)
vGS = VG - iD·RS
iD = (Kn/2)(vGS - Vth)²
vDS = VDD - iD(RD + RS)
```

**AC Load:**
```
Rac = RD || RL  (if CS bypasses RS)
```

**Voltage Gain:**
```
Av = -gm(RD || RL)
```

### Configuration 2: Fixed Gate Bias

**Circuit:**
- Separate gate voltage source VGG
- RG from gate to VGG
- No source resistor or RS = 0

**DC Analysis:**
```
vGS = VGG
iD = (Kn/2)(VGG - Vth)²
vDS = VDD - iD·RD
```

**Disadvantage:** No DC feedback, poor stability

### Configuration 3: Self-Bias (Common in discrete designs)

**Circuit:**
- RG from gate to ground
- RS from source to ground
- Gate current ≈ 0, so VG ≈ 0

**DC Analysis:**
```
vGS = -iD·RS  (negative for n-channel)
iD = (Kn/2)(-iD·RS - Vth)²
```

Solve graphically or with quadratic formula.

### Configuration 4: Source Feedback Bias

**Circuit:**
- Similar to voltage divider but designed for stronger feedback

**DC Analysis:**
Same as voltage-divider bias but RS chosen for better Q-point stability.

---

## 9. Practice Problems {#practice-problems}

### Problem 1: Basic Load Line

**Given:**
- VDD = 15V
- RD = 3kΩ
- RS = 1kΩ
- Kn = 0.5 mA/V²
- Vth = 2V
- vGS = 4V

**Find:**
a) Plot the DC load line
b) Calculate IDQ and VDSQ
c) Verify the operating region

**Solution:**

**a) DC Load Line:**

Point 1 (vDS = 0):
```
iD = VDD/(RD + RS) = 15V/4kΩ = 3.75 mA
```

Point 2 (iD = 0):
```
vDS = VDD = 15V
```

**b) Q-Point:**
```
IDQ = (Kn/2)(vGS - Vth)²
IDQ = (0.5 mA/V²/2)(4V - 2V)²
IDQ = 0.25 × 4 = 1 mA
```

```
VDSQ = VDD - IDQ(RD + RS)
VDSQ = 15V - 1mA × 4kΩ
VDSQ = 15V - 4V = 11V
```

**c) Operating Region Check:**
```
vGS - Vth = 4V - 2V = 2V
vDS = 11V ≥ 2V ✓
```

MOSFET is in saturation (correct for amplifier operation).

---

### Problem 2: Voltage-Divider Bias

**Given:**
- VDD = 20V
- R1 = 100kΩ
- R2 = 50kΩ
- RD = 4kΩ
- RS = 2kΩ
- Kn = 1 mA/V²
- Vth = 1.5V

**Find:**
a) VG
b) IDQ and vGSQ (solve graphically or numerically)
c) VDSQ
d) Plot DC load line and Q-point

**Solution:**

**a) Gate Voltage:**
```
VG = VDD × R2/(R1 + R2)
VG = 20V × 50kΩ/150kΩ
VG = 6.67V
```

**b) Q-Point (numerical approach):**

Equation:
```
iD = (Kn/2)(VG - iD·RS - Vth)²
iD = 0.5(6.67 - 2iD - 1.5)²
iD = 0.5(5.17 - 2iD)²
```

Expanding:
```
iD = 0.5(26.73 - 20.68iD + 4iD²)
iD = 13.365 - 10.34iD + 2iD²
2iD² - 11.34iD + 13.365 = 0
```

Quadratic formula:
```
iD = [11.34 ± √(128.6 - 106.9)]/4
iD = [11.34 ± √21.7]/4
iD = [11.34 ± 4.66]/4
```

Two solutions: iD = 4.0 mA or iD = 1.67 mA

Check which is valid:
- For iD = 4.0 mA: vGS = 6.67 - 8 = -1.33V (not physical for n-channel)
- For iD = 1.67 mA: vGS = 6.67 - 3.34 = 3.33V ✓

```
IDQ = 1.67 mA
vGSQ = 3.33V
```

**c) Drain-Source Voltage:**
```
VDSQ = VDD - IDQ(RD + RS)
VDSQ = 20V - 1.67mA × 6kΩ
VDSQ = 20V - 10V = 10V
```

**d) Load Line:**
- Point 1: (0V, 3.33mA)
- Point 2: (20V, 0mA)
- Q-point: (10V, 1.67mA)

---

### Problem 3: AC Load Line and Gain

**Given (using Problem 2 results):**
- Q-point: (10V, 1.67mA)
- RD = 4kΩ
- RS = 2kΩ (with bypass capacitor CS)
- RL = 8kΩ (AC coupled load)
- Kn = 1 mA/V²
- vGSQ = 3.33V, Vth = 1.5V

**Find:**
a) AC load resistance
b) AC load line equation
c) Transconductance gm
d) Voltage gain Av
e) Maximum output voltage swing

**Solution:**

**a) AC Load Resistance:**
```
Rac = RD || RL = (4kΩ × 8kΩ)/(4kΩ + 8kΩ)
Rac = 32kΩ²/12kΩ = 2.67kΩ
```

**b) AC Load Line:**

Slope = -1/2.67kΩ = -0.375 mA/V

Passing through Q-point (10V, 1.67mA):
```
iD - 1.67mA = -0.375(vDS - 10V)
```

Points for plotting:
- At vDS = 0: iD = 1.67 + 0.375 × 10 = 5.42 mA
- At iD = 0: vDS = 10 + 1.67/0.375 = 14.45V

**c) Transconductance:**
```
gm = Kn(vGSQ - Vth)
gm = 1 mA/V² × (3.33V - 1.5V)
gm = 1.83 mA/V
```

**d) Voltage Gain:**
```
Av = -gm × Rac
Av = -1.83 mA/V × 2.67kΩ
Av = -4.88
```

**e) Maximum Swing:**

From Q-point (10V, 1.67mA):
- To cutoff (iD = 0): ΔvDS = 14.45V - 10V = 4.45V
- To saturation boundary: vDS = vGS - Vth = 3.33 - 1.5 = 1.83V
  Distance: 10V - 1.83V = 8.17V

Limiting factor: cutoff at 4.45V

Maximum peak swing ≈ 4.45V
Maximum peak-to-peak swing ≈ 8.9V

---

## Summary Checklist for Load Line Analysis

**DC Analysis:**
- ☐ Draw DC equivalent circuit (open capacitors)
- ☐ Calculate two load line points: (VDD, 0) and (0, VDD/(RD+RS))
- ☐ Determine vGS from bias circuit
- ☐ Calculate IDQ using MOSFET equation
- ☐ Calculate VDSQ using KVL
- ☐ Verify saturation region: vDS ≥ (vGS - Vth)
- ☐ Plot Q-point on load line

**AC Analysis:**
- ☐ Draw AC equivalent circuit (short capacitors)
- ☐ Calculate Rac = RD || RL (with RS bypassed)
- ☐ Plot AC load line through Q-point with slope -1/Rac
- ☐ Calculate gm = Kn(vGS - Vth)
- ☐ Calculate Av = -gm·Rac
- ☐ Determine maximum swing from AC load line boundaries

**Critical Checks:**
- ☐ Is MOSFET in saturation for linear amplification?
- ☐ Is Q-point centered for maximum swing?
- ☐ Does signal swing stay within linear region?
- ☐ Are all component values reasonable?

---

## Quick Reference Formulas

| Parameter | Formula |
|-----------|---------|
| Drain current (saturation) | iD = (Kn/2)(vGS - Vth)² |
| Transconductance | gm = Kn(vGS - Vth) = √(2Kn·iD) |
| DC load line | iD = (VDD - vDS)/(RD + RS) |
| AC load resistance | Rac = RD ‖ RL |
| Voltage gain (CS, bypassed) | Av = -gm(RD ‖ RL) |
| Gate voltage (divider) | VG = VDD·R2/(R1 + R2) |
| Drain-source voltage | vDS = VDD - iD(RD + RS) |
| Saturation condition | vDS ≥ (vGS - Vth) |

Good luck on your quiz!