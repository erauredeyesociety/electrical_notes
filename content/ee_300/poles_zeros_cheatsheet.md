# Poles & Zeros Cheat Sheet

1. Poles of circuit are rates of exponentials that are “always” in the output
2. Poles determined by output side of differential equation
3. Zeros of circuit are rates of exponentials that are “never” in the output
4. Zeros determined by input side of differential equation

## 1. Circuit Response Components

### Total Response
$$\text{Total Response} = \text{ZIR} + \text{ZSR}$$

### Zero-Input Response (ZIR)
- Response due to **initial conditions only** (stored energy)
- No external sources applied
- Composed entirely of **natural response**

### Zero-State Response (ZSR)
- Response due to **external inputs only**
- All initial conditions = 0
- Composed of **natural response + forced response**

---

## 2. Transform to s-Domain

### Element Impedances
| Element | Time Domain | s-Domain Impedance |
|---------|-------------|-------------------|
| Resistor | $R$ | $Z_R = R$ |
| Capacitor | $C$ | $Z_C = \frac{1}{sC}$ |
| Inductor | $L$ | $Z_L = sL$ |

### Initial Condition Sources
- Capacitor: Voltage source $\frac{V_c(0)}{s}$ in series with $\frac{1}{sC}$
- Inductor: Current source $\frac{I_L(0)}{s}$ in parallel with $sL$

**For Network Functions:** Set all initial conditions to **ZERO**

---

## 3. Network Functions (Transfer Functions)

### Definition
$$H(s) = \frac{\text{Output}(s)}{\text{Input}(s)} \quad \text{[with all ICs = 0]}$$

### Types
1. **Transfer Function:** $H(s) = \frac{V_{out}(s)}{V_{in}(s)}$ (different ports)
2. **Driving-Point Impedance:** $Z(s) = \frac{V(s)}{I(s)}$ (same port)
3. **Driving-Point Admittance:** $Y(s) = \frac{I(s)}{V(s)} = \frac{1}{Z(s)}$ (same port)

### Finding H(s) from Circuit - 6 Steps
1. **Transform** all elements to s-domain ($R$, $\frac{1}{sC}$, $sL$)
2. **Zero** all initial conditions (voltage sources → short, current sources → open)
3. **Define** input and output variables
4. **Apply** circuit analysis (voltage/current divider, nodal, mesh, KCL/KVL)
5. **Form** $H(s) = \frac{\text{Output}(s)}{\text{Input}(s)}$
6. **Simplify** to rational function: $H(s) = \frac{N(s)}{D(s)}$

---

## 4. Poles and Zeros

### Rational Function Form
$$H(s) = \frac{N(s)}{D(s)} = \frac{a_m s^m + a_{m-1}s^{m-1} + \cdots + a_0}{b_n s^n + b_{n-1}s^{n-1} + \cdots + b_0}$$

### Definitions

**ZEROS:** Roots of numerator
$$N(s) = 0 \implies \text{Zeros: } s = z_1, z_2, \ldots, z_m$$

**POLES:** Roots of denominator (characteristic equation)
$$D(s) = 0 \implies \text{Poles: } s = p_1, p_2, \ldots, p_n$$

### What They Mean

| Property | Poles | Zeros |
|----------|-------|-------|
| **Mathematical** | $D(s) = 0$ | $N(s) = 0$ |
| **H(s) value** | $H(s) \to \infty$ | $H(s) = 0$ |
| **Time domain** | Always in output | Never in output |
| **Physical** | Natural frequencies | Blocked frequencies |
| **ODE location** | Output side (left) | Input side (right) |

### Finding Poles and Zeros - 3 Steps
1. **Express** $H(s) = \frac{N(s)}{D(s)}$ in polynomial form
2. **Find Zeros:** Set $N(s) = 0$ and solve for $s$
3. **Find Poles:** Set $D(s) = 0$ and solve for $s$

### Solving Polynomials
- **1st order** ($as + b$): $s = -\frac{b}{a}$
- **2nd order** ($as^2 + bs + c$): $s = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- **Higher order:** Factor or use numerical methods

---

## 5. Pole Types and Time Response

### Discriminant for 2nd Order
$$\Delta = b^2 - 4ac$$

| Discriminant | Pole Type | Time Response | Stability |
|--------------|-----------|---------------|-----------|
| $\Delta > 0$ | Two real poles | $k_1 e^{p_1 t} + k_2 e^{p_2 t}$ | Stable if $p_i < 0$ |
| $\Delta = 0$ | Repeated real pole | $(k_1 + k_2 t)e^{pt}$ | Stable if $p < 0$ |
| $\Delta < 0$ | Complex conjugate | $Ae^{-\alpha t}\cos(\omega_d t + \phi)$ | Stable if $\alpha > 0$ |

### Specific Pole Locations

**Real Pole:** $s = -\alpha$
$$\text{Time response: } k e^{-\alpha t} u(t)$$
- $\alpha > 0$: Decaying exponential (stable)
- $\alpha < 0$: Growing exponential (unstable)

**Complex Conjugate Poles:** $s = -\alpha \pm j\omega_d$
$$\text{Time response: } Ae^{-\alpha t}\cos(\omega_d t + \phi) u(t)$$
- $\alpha > 0$: Damped oscillation (stable)
- $\alpha < 0$: Growing oscillation (unstable)
- $\alpha = 0$: Sustained oscillation (marginally stable)

**Pole at Origin:** $s = 0$
$$\text{Time response: } k \cdot u(t) \text{ (step function)}$$
- Indicates integrator in system

---

## 6. Natural vs Forced Response

### From Output Expression
$$V_{out}(s) = H(s) \cdot V_{in}(s)$$

After factoring denominator, all poles come from:
1. **Poles of $H(s)$** → Natural Response
2. **Poles of $V_{in}(s)$** → Forced Response

### Natural Response
- Comes from **network function poles** (circuit's own modes)
- Independent of input type
- Determined by R, L, C values
- Same modes appear in ZIR

### Forced Response
- Comes from **input signal poles**
- Has same "shape" as input
- Amplitude scaled by $H(s)$ evaluated at input frequency
- If input is $Ke^{s_0 t}u(t)$, forced term is $K \cdot H(s_0) \cdot e^{s_0 t}$

### Special Case: Resonance
When input frequency = pole of $H(s)$:
$$\text{Output term becomes: } t \cdot e^{s_0 t} \text{ (grows with time)}$$

---

## 7. Time Response via Inverse Laplace Transform

### Complete Process - 6 Steps

1. **Find Output:** $V_{out}(s) = H(s) \cdot V_{in}(s)$

2. **Factor Denominator:** Find ALL poles (from $H(s)$ and $V_{in}(s)$)

3. **Partial Fraction Expansion (PFE):**
   $$V_{out}(s) = \frac{k_0}{s - p_0} + \frac{k_1}{s - p_1} + \frac{k_2}{s - p_2} + \cdots$$

4. **Find Residues** (Cover-Up Method):
   $$k_i = \left[(s - p_i) \cdot V_{out}(s)\right]_{s = p_i}$$

5. **Inverse Transform:**
   $$\frac{k_i}{s - p_i} \xrightarrow{\mathcal{L}^{-1}} k_i e^{p_i t} u(t)$$

6. **Combine and Identify:**
   - Terms from $H(s)$ poles = Natural response
   - Terms from $V_{in}(s)$ poles = Forced response

### Complex Conjugate Poles
If poles are $s = -\alpha \pm j\omega_d$ with residues $k$ and $k^*$:
$$\frac{k}{s - (-\alpha + j\omega_d)} + \frac{k^*}{s - (-\alpha - j\omega_d)} \xrightarrow{\mathcal{L}^{-1}} 2|k|e^{-\alpha t}\cos(\omega_d t + \angle k) u(t)$$

---

## 8. Common Laplace Transform Pairs

| Time Domain $f(t)$ | s-Domain $F(s)$ |
|-------------------|----------------|
| $u(t)$ | $\frac{1}{s}$ |
| $e^{at}u(t)$ | $\frac{1}{s-a}$ |
| $te^{at}u(t)$ | $\frac{1}{(s-a)^2}$ |
| $\cos(\omega t)u(t)$ | $\frac{s}{s^2 + \omega^2}$ |
| $\sin(\omega t)u(t)$ | $\frac{\omega}{s^2 + \omega^2}$ |
| $e^{-\alpha t}\cos(\omega t)u(t)$ | $\frac{s+\alpha}{(s+\alpha)^2 + \omega^2}$ |
| $e^{-\alpha t}\sin(\omega t)u(t)$ | $\frac{\omega}{(s+\alpha)^2 + \omega^2}$ |

### Transform Properties
$$\frac{d}{dt}f(t) \xrightarrow{\mathcal{L}} s F(s) - f(0^-)$$
$$\int_0^t f(\tau)d\tau \xrightarrow{\mathcal{L}} \frac{F(s)}{s}$$

---

## 9. Differential Equations

### From H(s) to ODE - 4 Steps

1. **Start with:** $H(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{N(s)}{D(s)}$

2. **Cross-multiply:** $V_{out}(s) \cdot D(s) = V_{in}(s) \cdot N(s)$

3. **Replace $s$ with $\frac{d}{dt}$:**
   - $s \to \frac{d}{dt}$
   - $s^2 \to \frac{d^2}{dt^2}$
   - $s^n \to \frac{d^n}{dt^n}$

4. **Write ODE:**
   $$\left(b_n \frac{d^n}{dt^n} + b_{n-1}\frac{d^{n-1}}{dt^{n-1}} + \cdots + b_0\right) v_{out}(t) = \left(a_m \frac{d^m}{dt^m} + \cdots + a_0\right) v_{in}(t)$$

### Key Insight
- **Denominator coefficients** (poles) → **Output side** (left)
- **Numerator coefficients** (zeros) → **Input side** (right)

### Example
$$H(s) = \frac{2s + 3}{s^2 + 5s + 6}$$

Cross-multiply: $V_{out}(s)(s^2 + 5s + 6) = V_{in}(s)(2s + 3)$

ODE: 
$$\frac{d^2v_{out}}{dt^2} + 5\frac{dv_{out}}{dt} + 6v_{out} = 2\frac{dv_{in}}{dt} + 3v_{in}$$

---

## 10. Quick Problem-Solving Guide

### Given Circuit → Find H(s)
1. Transform to s-domain: $R$, $\frac{1}{sC}$, $sL$
2. **Zero all ICs** (critical!)
3. Use voltage/current divider, nodal, or mesh analysis
4. Form $H(s) = \frac{\text{Output}}{\text{Input}}$

### Given H(s) → Find Poles/Zeros
1. Express as $H(s) = \frac{N(s)}{D(s)}$
2. Zeros: $N(s) = 0$
3. Poles: $D(s) = 0$

### Given H(s) → Find Differential Equation
1. Cross-multiply: $\text{Output}(s) \cdot D(s) = \text{Input}(s) \cdot N(s)$
2. Replace $s \to \frac{d}{dt}$
3. Write ODE

### Given Circuit + Input → Find Time Response
1. Find $H(s)$ from circuit
2. Calculate $V_{out}(s) = H(s) \cdot V_{in}(s)$
3. Do partial fraction expansion
4. Use cover-up method for residues
5. Inverse Laplace transform each term
6. Add $u(t)$ to each term

---

## 11. Critical Reminders

### Always Remember
✓ **Zero all initial conditions** when finding $H(s)$
✓ $H(s)$ only describes **ZSR** (not ZIR)
✓ Capacitor: $\frac{1}{sC}$ **NOT** $sC$
✓ Inductor: $sL$ **NOT** $\frac{1}{sL}$
✓ Include $u(t)$ in time-domain responses
✓ Complex poles come in **conjugate pairs**

### Common Mistakes
✗ Forgetting to zero ICs for $H(s)$
✗ Confusing poles (denominator) with zeros (numerator)
✗ Wrong impedance transformations
✗ Not factoring denominator completely
✗ Forgetting $u(t)$ in inverse Laplace
✗ Mixing up natural response (from $H(s)$ poles) vs forced response (from input poles)

---

## 12. Analysis Flowchart Summary

```
START
  ↓
What are you given?
  ├─ Circuit → Transform to s-domain → Find H(s) → Poles/Zeros
  ├─ H(s) → Direct to Poles/Zeros OR Create ODE
  └─ ODE → Laplace Transform → Find H(s) → Poles/Zeros
  ↓
Need Time Response?
  ├─ Yes → V_out(s) = H(s)·V_in(s) → PFE → ILT → v_out(t)
  └─ No → DONE
```

---

## 13. Example: RC Low-Pass Filter

**Given:** $V_{in} \to R \to C \to V_{out}$ (across capacitor)

### Find H(s)
$$H(s) = \frac{Z_C}{Z_R + Z_C} = \frac{1/(sC)}{R + 1/(sC)} = \frac{1}{1 + sRC} = \frac{1/RC}{s + 1/RC}$$

### Poles and Zeros
- **Pole:** $s + \frac{1}{RC} = 0 \implies s = -\frac{1}{RC}$
- **Zeros:** None (numerator is constant)

### Differential Equation
Cross-multiply: $V_{out}(s)(s + \frac{1}{RC}) = V_{in}(s) \cdot \frac{1}{RC}$

$$\frac{dv_{out}}{dt} + \frac{v_{out}}{RC} = \frac{v_{in}}{RC}$$

### Time Response to Step Input ($v_{in} = u(t)$)
$$V_{in}(s) = \frac{1}{s}, \quad V_{out}(s) = \frac{1/RC}{(s + 1/RC) \cdot s}$$

PFE: $V_{out}(s) = \frac{1}{s} - \frac{1}{s + 1/RC}$

$$v_{out}(t) = \left[1 - e^{-t/RC}\right]u(t)$$

- **Forced response:** $1$ (from input pole at $s = 0$)
- **Natural response:** $-e^{-t/RC}$ (from $H(s)$ pole at $s = -1/RC$)

---

## 14. Stability Summary

| Pole Location | Stability | Time Response |
|---------------|-----------|---------------|
| Left half-plane (Re$(s) < 0$) | **Stable** | Decaying |
| Right half-plane (Re$(s) > 0$) | **Unstable** | Growing |
| Imaginary axis (Re$(s) = 0$) | **Marginally stable** | Sustained |

**System is stable if and only if ALL poles are in the left half-plane.**