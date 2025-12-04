# Final Quiz Cheatsheet

## SECTION 1: TRANSFER FUNCTIONS (NETWORK FUNCTIONS)

### Definition
$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} \quad \text{or} \quad H(s) = \frac{I_{out}(s)}{I_{in}(s)}$$

**Critical:** ALL initial conditions must be ZERO when finding H(s)

### Types of Network Functions
| Type | Definition | Same/Different Ports |
|------|------------|---------------------|
| Transfer Function | $H(s) = \frac{V_{out}(s)}{V_{in}(s)}$ | Different ports |
| Driving-Point Impedance | $Z(s) = \frac{V(s)}{I(s)}$ | Same port |
| Driving-Point Admittance | $Y(s) = \frac{I(s)}{V(s)} = \frac{1}{Z(s)}$ | Same port |

### Rational Function Form
$$H(s) = \frac{N(s)}{D(s)} = \frac{a_m s^m + a_{m-1}s^{m-1} + \cdots + a_0}{b_n s^n + b_{n-1}s^{n-1} + \cdots + b_0}$$

### Poles and Zeros
- **ZEROS:** Roots of numerator $N(s) = 0$ - Frequencies that are **blocked**
- **POLES:** Roots of denominator $D(s) = 0$ - **Natural frequencies** (always in output)

### s-Domain Element Impedances
$$Z_R = R \qquad Z_C = \frac{1}{sC} \qquad Z_L = sL$$

### Finding H(s) from Circuit - Quick Steps
1. Transform all elements to s-domain
2. **ZERO all initial conditions**
3. Apply circuit analysis (voltage divider, nodal, mesh)
4. Form $H(s) = \frac{\text{Output}}{\text{Input}}$
5. Simplify to rational function

---

## SECTION 2: PARTIAL FRACTION EXPANSION (PFE)

### Why PFE?
Convert $V_{out}(s) = H(s) \cdot V_{in}(s)$ into simple fractions for inverse Laplace transform.

### Standard Form
$$F(s) = \frac{k_1}{s-p_1} + \frac{k_2}{s-p_2} + \cdots + \frac{k_n}{s-p_n}$$

### Cover-Up Method for Residues
$$k_i = \left[(s-p_i) \cdot F(s)\right]_{s=p_i}$$

### Case 1: Distinct Real Poles
**Example:** $F(s) = \frac{100}{(s+10)(s+100)}$

Setup: $F(s) = \frac{k_1}{s+10} + \frac{k_2}{s+100}$

Find residues:
$$k_1 = \left[(s+10) \cdot \frac{100}{(s+10)(s+100)}\right]_{s=-10} = \frac{100}{-10+100} = \frac{100}{90}$$

$$k_2 = \left[(s+100) \cdot \frac{100}{(s+10)(s+100)}\right]_{s=-100} = \frac{100}{-100+10} = -\frac{100}{90}$$

Time domain: $f(t) = \frac{100}{90}e^{-10t} - \frac{100}{90}e^{-100t}$ for $t \geq 0$

### Case 2: Complex Conjugate Poles
**Poles:** $s = -\alpha \pm j\omega_d$

**Time Response:**
$$f(t) = 2|k|e^{-\alpha t}\cos(\omega_d t + \angle k) u(t)$$

### Common Laplace Transform Pairs
| Time Domain | s-Domain |
|-------------|----------|
| $u(t)$ | $\frac{1}{s}$ |
| $e^{-\alpha t}u(t)$ | $\frac{1}{s+\alpha}$ |
| $te^{-\alpha t}u(t)$ | $\frac{1}{(s+\alpha)^2}$ |
| $e^{-\alpha t}\cos(\omega t)u(t)$ | $\frac{s+\alpha}{(s+\alpha)^2 + \omega^2}$ |
| $e^{-\alpha t}\sin(\omega t)u(t)$ | $\frac{\omega}{(s+\alpha)^2 + \omega^2}$ |

---

## SECTION 3: OP-AMP FUNDAMENTALS

### Ideal Op-Amp Rules
1. **No current flows into either input:** $i_+ = i_- = 0$
2. **Voltage difference is zero (negative feedback):** $V_+ = V_-$

### Common Configurations

**Inverting Amplifier:**
$$H(s) = -\frac{Z_f(s)}{Z_{in}(s)}$$

**Non-Inverting Amplifier:**
$$H(s) = 1 + \frac{Z_f(s)}{Z_g(s)} = \mu$$
$$\mu = 1 + \frac{R_f}{R_g}$$

**Voltage Follower (Buffer):**
$$H(s) = 1 \quad (\mu = 1)$$
- High input impedance, low output impedance
- Prevents loading between stages

**Summing Amplifier:**
$$V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2}\right)$$

### Why Op-Amps in Filter Design?
- Enable **cascading** without loading: $H_{total}(s) = H_1(s) \times H_2(s) \times \cdots$
- Provide **gain** ($\mu > 1$)
- **Buffer** stages (high input Z, low output Z)

---

## SECTION 4: FILTER DESIGN - BUTTERWORTH METHOD

### Filter Types by H(s)
| Filter | H(s) Numerator | Passes | Blocks |
|--------|----------------|--------|--------|
| Low-Pass | Constant (K) | Low freq | High freq |
| High-Pass | $s^n$ | High freq | Low freq |
| Band-Pass | $s$ | Middle band | Low & High |
| Band-Stop | $s^2 + \omega_0^2$ | Low & High | Middle band |

### PHASE 1: Calculate Required Filter Order

#### Given Specifications
- $H_{MAX}$: Maximum passband gain (linear or dB)
- $H_{MIN}$: Minimum stopband gain (linear or dB)
- $\omega_C$ or $f_C$: Cutoff frequency
- $\omega_{MIN}$ or $f_{MIN}$: Stopband frequency

#### Convert dB to Linear
$$H_{\text{linear}} = 10^{H_{\text{dB}}/20}$$

#### Butterworth Order Formulas

**Low-Pass:**
$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_{MIN}/\omega_C)}$$

**High-Pass:**
$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_C/\omega_{MIN})}$$

**ALWAYS ROUND UP to nearest integer**

#### Section Count
- **Odd n:** $(n-1)/2$ second-order + 1 first-order
- **Even n:** $n/2$ second-order sections

---

### PHASE 2: Obtain Butterworth Poles

#### Pole Angles (Normalized omega_C = 1)
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}, \quad k = 1, 2, \ldots, n$$

#### Pole Locations
$$p_k = e^{j\theta_k} = \cos(\theta_k) + j\sin(\theta_k)$$

**Use only LEFT half-plane poles** (Real part < 0)

---

### PHASE 3: Extract Section Parameters

#### For 2nd-Order Section from Conjugate Pair
**Poles:** $p = \alpha + j\beta$ and $p^* = \alpha - j\beta$

**Quadratic form:**
$$(s - p)(s - p^*) = s^2 - 2\alpha s + (\alpha^2 + \beta^2)$$

For normalized ($|p| = 1$):
$$s^2 + as + 1$$
where $a = -2\cos(\theta_k)$

**Extract damping ratio:**
$$\zeta_k = \frac{a}{2} = -\cos(\theta_k)$$

**Quality factor:**
$$Q_k = \frac{1}{2\zeta_k}$$

#### Quick Reference Table for Damping Ratio and Q

| n | Section | Damping Ratio | Q Factor | a coefficient |
|---|---------|---------------|----------|---------------|
| 2 | 1 | 0.707 | 0.707 | 1.414 |
| 3 | 1 | 0.500 | 1.000 | 1.000 |
| 4 | 1 | 0.383 | 1.307 | 0.765 |
| 4 | 2 | 0.924 | 0.541 | 1.848 |

---

### PHASE 4: UNITY GAIN METHOD (RECOMMENDED)

#### Why Unity Gain?
- Works for **ALL damping ratios** (any positive value)
- Most **stable** configuration
- Op-amp as simple buffer ($\mu = 1$)

#### Design Equations - Low-Pass

**Option A:** Choose $C_1$ (typical: 0.01 to 1 microF)
$$C_2 = 4\zeta^2 C_1$$
$$R_1 = R_2 = R = \frac{1}{\zeta\omega_0 C_1}$$

**Option B:** Choose $R_2$ (typical: 1k to 100k ohms)
$$R_1 = 4\zeta^2 R_2$$
$$C_1 = C_2 = C = \frac{1}{\zeta\omega_0 R_2}$$

#### Design Equations - High-Pass
Swap R and C positions from low-pass design.

**With $R_2$ chosen:**
$$R_1 = 4\zeta^2 R_2$$
$$C_1 = C_2 = C = \frac{1}{\zeta\omega_0 R_2}$$

---

### PHASE 5: EQUAL ELEMENTS METHOD (BACKUP)

#### When to Use
- Only if damping ratio is between 0 and 1 (underdamped, Q > 0.5)
- Requires op-amp gain greater than 1

#### Design Equations - Low-Pass
Set $R_1 = R_2 = R$ and $C_1 = C_2 = C$

$$\mu = 3 - 2\zeta$$

**Choose C, then:**
$$R = \frac{1}{\omega_0 C}$$

**Op-amp gain circuit:**
$$\mu = 1 + \frac{R_f}{R_g}$$
$$R_f = (\mu - 1) \cdot R_g$$

**Validity check:** $1 \leq \mu \leq 3$ if and only if damping ratio is between 0 and 1

#### Design Equations - High-Pass
Same as low-pass: $R_1 = R_2 = R$, $C_1 = C_2 = C$, $\mu = 3 - 2\zeta$

---

### PHASE 6: First-Order Sections

#### For Real Pole at $s = -\omega_C$

**Passive RC Low-Pass:**
$$H(s) = \frac{1}{1 + sRC}, \quad \omega_C = \frac{1}{RC}$$

Choose C, then: $R = \frac{1}{\omega_C C}$

**Active Low-Pass (with gain K):**
$$H(s) = \frac{K}{1 + sRC}$$

Use non-inverting op-amp: $K = 1 + \frac{R_f}{R_g}$

**High-Pass (1st order):**
$$H(s) = \frac{sRC}{1 + sRC}$$
Swap R and C positions from low-pass.

---

### PHASE 7: Cascade Assembly

#### Section Ordering (CRITICAL)
**Order by Q: LOW to HIGH**

Place highest damping ratio (lowest Q) first, lowest damping ratio (highest Q) last.

**Why?** Prevents early clipping from resonant peaks.

#### Overall Transfer Function
$$H_{\text{total}}(s) = H_1(s) \times H_2(s) \times \cdots \times H_n(s)$$

---

### PHASE 8: Frequency & Impedance Scaling

#### Frequency Scaling (multiply by k_f)
$$C_{\text{new}} = \frac{C_{\text{old}}}{k_f}, \quad R_{\text{new}} = R_{\text{old}}$$

**Effect:** All frequencies multiplied by $k_f$

#### Impedance Scaling (multiply by k_z)
$$R_{\text{new}} = k_z \times R_{\text{old}}, \quad C_{\text{new}} = \frac{C_{\text{old}}}{k_z}$$

**Effect:** $H(s)$ and frequencies unchanged

#### Practical Component Ranges
| Component | Practical Range | Preferred Range |
|-----------|-----------------|-----------------|
| Resistors | 100 ohm - 10 Mohm | 1k ohm - 1 Mohm |
| Capacitors | 1pF - 1000 microF | 100pF - 10 microF |

---

## SECTION 5: BODE PLOTS

### Definition
Bode plots show **magnitude** (in dB) and **phase** versus frequency (log scale).

**Axes:**
- X: $\log_{10}(\omega)$
- Y: $20\log_{10}(|H(j\omega)|)$ dB

### Magnitude in dB
$$|H(j\omega)|_{dB} = 20\log_{10}|H(j\omega)|$$

### Conversions
**dB to Linear:**
$$|H| = 10^{(\text{dB}/20)}$$

**Linear to dB:**
$$\text{dB} = 20\log_{10}|H|$$

### Frequency Response from H(s)
1. Substitute $s = j\omega$
2. Calculate magnitude: $|H(j\omega)| = \sqrt{[\text{Re}(H)]^2 + [\text{Im}(H)]^2}$
3. Calculate phase: $\angle H(j\omega) = \arctan[\text{Im}(H)/\text{Re}(H)]$

### Sinusoidal Steady-State Response
**Input:** $v_{in}(t) = A\cos(\omega t + \theta)$

**Output:** $v_{out}(t) = A \cdot |H(j\omega)| \cos(\omega t + \theta + \angle H(j\omega))$

### Key Bode Plot Features

#### Cutoff Frequency (minus 3 dB point)
$$|H(j\omega_c)| = \frac{|H_{max}|}{\sqrt{2}}$$

#### Slopes (Asymptotic)
- **1st order:** plus/minus 20 dB/decade per pole/zero
- **2nd order:** plus/minus 40 dB/decade per pole pair
- **nth order:** plus/minus (n times 20) dB/decade

#### Phase at Cutoff
- **1st order:** plus/minus 45 degrees at cutoff frequency
- **2nd order (Butterworth):** minus 90 degrees at natural frequency

### First-Order Filter Forms

**Low-Pass:**
$$H(s) = \frac{K\omega_c}{s + \omega_c}$$
- DC gain = K
- Slope: minus 20 dB/decade above cutoff frequency

**High-Pass:**
$$H(s) = \frac{Ks}{s + \omega_c}$$
- HF gain = K
- Slope: plus 20 dB/decade below cutoff frequency

### Second-Order Standard Form
$$H(s) = \frac{K\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$

**Peak magnitude (underdamped):**
$$|H(j\omega_0)| = \frac{K}{2\zeta} \quad \text{for } \zeta < \frac{1}{\sqrt{2}}$$

---

## CRITICAL DESIGN CHECKLIST

- Convert all dB to linear
- Round n UP to integer
- Extract all poles (left half-plane only)
- Calculate damping ratio and Q for each section
- Use **Unity Gain Method** (always works)
- Check damping ratio < 1 if using Equal Elements
- Order sections LOW Q to HIGH Q
- Scale components to practical values
- Verify overall $H(s)$ = product of sections

---

## QUICK REFERENCE FORMULAS

### Butterworth Order
$$n \geq \frac{\ln[(H_{MAX}/H_{MIN})^2-1]}{2\ln(\omega_{MIN}/\omega_C)} \quad \text{(LP)}$$

$$n \geq \frac{\ln[(H_{MAX}/H_{MIN})^2-1]}{2\ln(\omega_C/\omega_{MIN})} \quad \text{(HP)}$$

### Pole Angles
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

### Damping and Q
$$\zeta = -\cos(\theta_k) = \frac{a}{2}, \quad Q = \frac{1}{2\zeta}$$

### Unity Gain (Low-Pass)
$$C_2 = 4\zeta^2 C_1, \quad R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1}$$

### Equal Elements
$$\mu = 3 - 2\zeta, \quad R = \frac{1}{\omega_0 C}$$

### Cover-Up Method
$$k_i = \left[(s-p_i)F(s)\right]_{s=p_i}$$

### Frequency Response
$$|H(j\omega)| = \sqrt{[\text{Re}]^2 + [\text{Im}]^2}$$
$$\angle H(j\omega) = \arctan[\text{Im}/\text{Re}]$$

---

## COMMON MISTAKES TO AVOID

- Rounding n down instead of up
- Using Equal Elements when damping ratio is 1 or greater
- Forgetting to convert dB to linear
- Wrong frequency ratio (LP vs HP)
- Cascading high-Q sections first
- Forgetting to zero initial conditions for H(s)
- Wrong impedance: C is $\frac{1}{sC}$ NOT $sC$

---

## PROBLEM-SOLVING WORKFLOW

### Given: Filter Specifications to Design Circuit

1. **Calculate n** using Butterworth formula (round UP)
2. **Find poles** using angle formula
3. **Extract damping ratio** for each 2nd-order section
4. **Choose Unity Gain Method** (always works)
5. **Design each section** using Unity Gain equations
6. **Order sections** by Q (low to high)
7. **Scale components** to practical values
8. **Cascade** with op-amp buffers

### Given: H(s) to Find Time Response

1. **Factor denominator** to find all poles
2. **Apply PFE** to $V_{out}(s) = H(s) \cdot V_{in}(s)$
3. **Use Cover-Up Method** for residues
4. **Inverse Laplace** each term
5. **Add u(t)** to all terms

### Given: Circuit to Find H(s)

1. **Transform to s-domain** (R, 1/(sC), sL)
2. **Zero all initial conditions**
3. **Apply circuit analysis** (nodal, mesh, divider)
4. **Form H(s)** = Output/Input
5. **Simplify** to rational function

---

## END OF CHEATSHEET