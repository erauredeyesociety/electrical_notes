# Butterworth Filter Design Complete Cheatsheet

## Quick Reference: Filter Types & Forms

| Filter Type | H(s) Numerator | Passes | Attenuates |
|-------------|----------------|--------|------------|
| **Low-Pass** | Constant (K) | Low frequencies | High frequencies |
| **High-Pass** | $s^n$ | High frequencies | Low frequencies |
| **Band-Pass** | $s$ | Middle band | Low & High |
| **Band-Stop** | $s^2 + \omega_0^2$ | Low & High | Middle band |

---

## PHASE 1: CALCULATE REQUIRED FILTER ORDER

### Given Specifications (Typical)

- **Filter Type**: LP, HP, BP, or BS
- **$H_{MAX}$**: Maximum passband gain (linear or dB)
- **$H_{MIN}$**: Minimum stopband gain (linear or dB)
- **$\omega_C$ or $f_C$**: Cutoff/corner frequency
- **$\omega_{MIN}$ or $f_{MIN}$**: Frequency where $H_{MIN}$ must be met

### Step 1.1: Convert dB to Linear (if needed)

$$H_{\text{linear}} = 10^{H_{\text{dB}}/20}$$

### Step 1.2: Calculate Minimum Order n

**Low-Pass Butterworth:**

$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_{MIN}/\omega_C)}$$

**High-Pass Butterworth:**

$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_C/\omega_{MIN})}$$

**⚠️ CRITICAL: Always round UP to nearest integer**

### Step 1.3: Determine Section Count

Always use as many second order circuits if possible. If an odd number n, then the most second order and then 1 first order.

**General formula:**
- **Odd n**: $(n-1)/2$ second-order + 1 first-order
- **Even n**: $n/2$ second-order

---

## PHASE 2: OBTAIN BUTTERWORTH POLES

### Step 2.1: Calculate Pole Angles

For normalized Butterworth ($\omega_C = 1$):

$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}, \quad k = 1, 2, \ldots, n$$

k is simply an index used to enumerate the poles of the normalized Butterworth polynomial.
Nothing more. It has no electrical meaning like gain, component value, or stage count.

### Step 2.2: Calculate Pole Locations

$$p_k = e^{j\theta_k} = \cos(\theta_k) + j\sin(\theta_k)$$

**Only use left half-plane poles** (Real part < 0)

---

## PHASE 3: EXTRACT SECTION PARAMETERS

### For 2nd-Order Section from Conjugate Pair

**Step 3.1: Form quadratic**

Poles $p = \alpha + j\beta$ and $p^* = \alpha - j\beta$:

$$(s - p)(s - p^*) = s^2 - 2\alpha s + (\alpha^2 + \beta^2)$$

For normalized: $|p| = 1$, so:

$$s^2 + as + 1$$

where $a = -2\text{Re}(p) = -2\cos(\theta_k)$

**Step 3.2: Extract damping ratio $\zeta$**

Standard form: $s^2 + 2\zeta\omega_0 s + \omega_0^2$

For normalized ($\omega_0 = 1$): $s^2 + 2\zeta s + 1$

$$\zeta_k = \frac{a}{2} = -\cos(\theta_k)$$

**Step 3.3: Calculate Q factor**

$$Q_k = \frac{1}{2\zeta_k}$$

### Quick Reference: ζ and Q for Common Orders

| n | Section | $\zeta$ | Q | a coefficient |
|---|---------|---------|---|---------------|
| 2 | 1 | 0.707 | 0.707 | 1.414 |
| 3 | 1 | 0.500 | 1.000 | 1.000 |
| 4 | 1 | 0.383 | 1.307 | 0.765 |
| 4 | 2 | 0.924 | 0.541 | 1.848 |
| 5 | 1 | 0.309 | 1.618 | 0.618 |
| 5 | 2 | 0.809 | 0.618 | 1.618 |

---

## PHASE 4: DESIGN METHOD SELECTION

**Decision Rule:** If $\zeta \geq 1$ (or $Q \leq 0.5$), MUST use Unity Gain. Otherwise, use Unity Gain (recommended) or Equal Elements (simpler).

### Method Comparison

| Criterion | Unity Gain | Equal Elements |
|-----------|------------|----------------|
| **Valid $\zeta$ range** | All ($\zeta \geq 0$) | $0 < \zeta < 1$ only |
| **Op-amp gain $\mu$** | 1 (buffer) | $3 - 2\zeta$ (1 to 3) |
| **Stability** | Excellent | Good |
| **Sensitivity** | Low | Medium |

---

## PHASE 5A: UNITY GAIN METHOD (RECOMMENDED)

### Circuit Description

Op-amp as voltage follower (buffer), non-inverting input connects to RC network, output feeds back directly to inverting input. **Components: 2 resistors ($R_1, R_2$) and 2 capacitors ($C_1, C_2$).**

### Design Equations

**Step 1: Set gain**

$$\mu = 1$$

**Step 2: Choose starting component**

**Option A** – Choose $C_1$ (typical: 0.01 to 1 µF)

$$C_2 = (2\zeta)^2 \cdot C_1 = 4\zeta^2 C_1$$

$$R_1 = R_2 = R = \frac{1}{\zeta \omega_0 C_1}$$

**Option B** – Choose $R_2$ (typical: 1k to 100k)

$$R_1 = (2\zeta)^2 \cdot R_2 = 4\zeta^2 R_2$$

$$C_1 = C_2 = C = \frac{1}{\zeta \omega_0 R_2}$$



---

## PHASE 5B: EQUAL ELEMENTS METHOD

### Circuit Description

Op-amp with gain > 1 (non-inverting configuration). Feedback resistors $R_f$ and $R_g$ set gain. **Components: Equal resistors $R_1 = R_2 = R$ and equal capacitors $C_1 = C_2 = C$ in filter network.**

### Design Equations

**Step 1: Calculate required gain**

$$\mu = 3 - 2\zeta$$

**Validity check:** $1 \leq \mu \leq 3 \Leftrightarrow 0 < \zeta < 1$. If outside this range, **cannot use this method**.

**Step 2: Choose C (typical: 0.01 to 1 µF)**

$$R = \frac{1}{\omega_0 C}$$

**Step 3: Design op-amp gain circuit**

$$\mu = 1 + \frac{R_f}{R_g}$$

$$R_f = (\mu - 1) \cdot R_g$$

Typical: Choose $R_g = 10$ k$\Omega$, then: $R_f = (\mu - 1) \times 10$ k$\Omega$



---

## PHASE 6: FIRST-ORDER SECTIONS

### For Real Pole at $s = -\omega_C$

**Components: 1 resistor (R) and 1 capacitor (C).**

**Passive RC Low-Pass:**

$H(s) = \frac{1}{1 + sRC}, \quad \omega_C = \frac{1}{RC}$

Choose C, solve for R: $R = \frac{1}{\omega_C C}$

**Active Low-Pass (with gain K):**

$H(s) = \frac{K}{1 + sRC}$

Use non-inverting op-amp: $K = 1 + \frac{R_f}{R_g}$

**High-Pass (1st order):**

$H(s) = \frac{sRC}{1 + sRC}$

Swap R and C positions from low-pass.

---

## PHASE 7: CASCADE ASSEMBLY

### Step 7.1: Section Ordering (CRITICAL)

**Order sections by Q: LOW → HIGH**

Place highest $\zeta$ (lowest Q) first, lowest $\zeta$ (highest Q) last. **Why?** Prevents early clipping from resonant peaks.

### Step 7.2: Buffering

Each Sallen-Key stage has high input impedance (op-amp input), so stages naturally don't load each other. No additional buffers needed between stages.

### Step 7.3: Overall Transfer Function

$$H_{\text{total}}(s) = H_1(s) \times H_2(s) \times \cdots \times H_n(s)$$

---

## OP-AMP FUNDAMENTALS

### Why Use Op-Amps?

- High input impedance (prevents loading previous stages)
- Low output impedance (drives next stage without degradation)
- Enable gain without passive component losses
- Allow cascading of sections without interaction

### Key Configurations

**1. Voltage Follower (Buffer)**: $\mu = 1$ exactly. Use for Unity Gain Method. Output connects directly to inverting input. Most stable configuration.

**2. Non-Inverting Amplifier**: $\mu = 1 + \frac{R_f}{R_g}$. Use for Equal Elements Method when $1 < \mu < 3$. Maintains input signal polarity.

**3. Inverting Amplifier**: $\mu = -\frac{R_f}{R_{in}}$. NOT typically used in Sallen-Key filters. Can be used for summing (bandstop filters).

**4. Summing Amplifier**: $V_{out} = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2}\right)$. Required for bandstop (notch) filters to combine LP and HP paths.

### Op-Amp Placement

- **Within each Sallen-Key section**: Required (one per 2nd-order section)
- **After passive RC sections**: Required (use buffer)
- **Between active sections**: Usually NOT needed (already buffered)
- **At filter output**: Recommended if driving cables/loads

### Critical Op-Amp Specifications

**Gain-Bandwidth Product (GBW):** $GBW \geq 100 \times f_c \times Q \times \mu$

**Slew Rate (SR):** $SR \geq 2\pi f_{max} V_{peak}$

**Common choices:** TL072/LF412 (audio), LM358/TL082 (general), TL071/OPA2134 (high-speed)

### Power Supply & Decoupling

Use dual supply (±15V, ±12V, or ±5V typical). **Always add 0.1 µF ceramic capacitor** at each IC between V+ and GND, and between V− and GND. Prevents oscillation and noise.

---

## PHASE 8: FREQUENCY & IMPEDANCE SCALING

### When Component Values Are Impractical

**Frequency Scaling ($\times k_f$):**

$$C_{\text{new}} = \frac{C_{\text{old}}}{k_f}, \quad R_{\text{new}} = R_{\text{old}}$$

**Impedance Scaling ($\times k_z$):**

$$R_{\text{new}} = k_z \times R_{\text{old}}, \quad C_{\text{new}} = \frac{C_{\text{old}}}{k_z}$$

**Combined Scaling:**

$$R_{\text{final}} = k_z \times R_{\text{normalized}}, \quad C_{\text{final}} = \frac{C_{\text{normalized}}}{k_f \times k_z}$$

### Practical Component Ranges

| Component | Practical Range | Preferred Range |
|-----------|----------------|-----------------|
| Resistors | 100$\Omega$ - 10M$\Omega$ | 1k$\Omega$ - 1M$\Omega$ |
| Capacitors | 1pF - 1000µF | 100pF - 10µF |

---

## DERIVING MISSING SPECIFICATIONS

### If $\omega_C$ Given, But $\omega_{MIN}$ Not Given

Typical assumption: Transition band = 1 decade

$$\omega_{MIN} = 10 \times \omega_C \text{ (low-pass)}, \quad \omega_{MIN} = 0.1 \times \omega_C \text{ (high-pass)}$$

### If $H_{MIN}$ Not Given

Use standard attenuation: -40 dB (0.01) for audio, -60 dB (0.001) for instrumentation

### If $\zeta$ or Q Given for Section

$$Q = \frac{1}{2\zeta}, \quad \zeta = \frac{1}{2Q}$$

### If $\omega_0$ and $\zeta$ Given, Find Pole Locations

Complex conjugate poles: $p = -\zeta\omega_0 \pm j\omega_0\sqrt{1-\zeta^2}$

Real part: $\sigma = -\zeta\omega_0$, Imaginary part: $\omega_d = \omega_0\sqrt{1-\zeta^2}$ (damped frequency)

### Bandwidth Relationships

For 2nd-order: $BW = 2\zeta\omega_0 = \frac{\omega_0}{Q}$

Half-power frequencies:

$$\omega_1 = \omega_0\left(-\zeta + \sqrt{\zeta^2+1}\right), \quad \omega_2 = \omega_0\left(\zeta + \sqrt{\zeta^2+1}\right)$$

---

## BANDPASS AND BANDSTOP FILTER DESIGN

### Bandpass Filter (BP)

**Concept:** Pass middle band, attenuate low and high frequencies.

**Design:** Cascade lowpass and highpass: $H_{BP}(s) = H_{LP}(s) \times H_{HP}(s)$

**Steps:**
1. Define: Lower cutoff $\omega_1$ (HP), upper cutoff $\omega_2$ (LP), center $\omega_0 = \sqrt{\omega_1 \omega_2}$, bandwidth $BW = \omega_2 - \omega_1$
2. Design HP section with $\omega_C = \omega_1$
3. Design LP section with $\omega_C = \omega_2$
4. Cascade: HP → LP (or LP → HP)

**Key:** Total order = (LP order) + (HP order). Use series connection.

### Bandstop (Notch) Filter (BS)

**Concept:** Attenuate middle band, pass low and high frequencies.

**Design:** Parallel sum: $H_{BS}(s) = H_{LP}(s) + H_{HP}(s)$

**Steps:**
1. Define: Lower passband edge $\omega_1$ (LP cutoff), upper passband edge $\omega_2$ (HP cutoff), notch center $\omega_0 = \sqrt{\omega_1 \omega_2}$
2. Design LP section with $\omega_C = \omega_1$ (passes below notch)
3. Design HP section with $\omega_C = \omega_2$ (passes above notch)
4. Use **summing amplifier** to combine outputs

**Key:** Unlike BP (cascade), BS requires **parallel combination** via summing amplifier. Both sections must have same DC/HF gain for flat response.

---

### Comparison: BP vs BS Implementation

| Aspect | Bandpass (BP) | Bandstop (BS) |
|--------|---------------|---------------|
| **Combination** | Cascade (multiply) | Parallel (sum) |
| **Circuit** | Series connection | Summing amplifier |
| **Passes** | Middle band | Low & High |
| **Attenuates** | Low & High | Middle band |

---

## QUICK REFERENCE FORMULAS

### Order Calculation

LP: $n \geq \frac{\ln[(H_{MAX}/H_{MIN})^2-1]}{2\ln(\omega_{MIN}/\omega_C)}$

HP: $n \geq \frac{\ln[(H_{MAX}/H_{MIN})^2-1]}{2\ln(\omega_C/\omega_{MIN})}$

### Pole Angles

$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

### Damping & Q

$$\zeta = -\cos(\theta_k) = \frac{a}{2}, \quad Q = \frac{1}{2\zeta}$$

### Unity Gain

$$C_2 = 4\zeta^2 C_1, \quad R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1}$$

### Equal Elements

$$\mu = 3 - 2\zeta, \quad R = \frac{1}{\omega_0 C}$$

---

## CRITICAL CHECKLIST

- [ ] Converted all dB to linear
- [ ] Rounded n UP to integer
- [ ] Extracted all poles (left half-plane only)
- [ ] Grouped poles into sections
- [ ] Calculated $\zeta$ and Q for each section
- [ ] Checked $\zeta < 1$ before using Equal Elements
- [ ] Verified $1 \leq \mu \leq 3$ for Equal Elements
- [ ] Ordered sections LOW Q → HIGH Q
- [ ] Scaled components to practical values
- [ ] Verified $H_{\text{total}}(s)$ = product of sections

---

## COMMON MISTAKES TO AVOID

❌ Rounding n down instead of up

❌ Using Equal Elements when $\zeta \geq 1$

❌ Forgetting to convert dB to linear

❌ Wrong frequency ratio (LP vs HP)

❌ Cascading high-Q sections first

❌ Using right half-plane poles

❌ Forgetting to denormalize from $\omega_C = 1$

---

## COMPLETE WORKED EXAMPLE

### Given Requirements

Low-pass filter: $H_{MAX} = 0$ dB (1.0), $H_{MIN} = -40$ dB (0.01), $f_C = 1$ kHz, $f_{MIN} = 5$ kHz

### Solution

**Calculate order:** $n \geq \frac{\ln[(1/0.01)^2-1]}{2\ln(5)} = 2.86$ → **Round up: n = 3**

**Sections:** $n = 3$ (odd) → 1 first-order + 1 second-order

**Poles for n = 3:** $\theta_1 = 120°$, $\theta_2 = 180°$, $\theta_3 = 240°$

Pole locations: $p_1 = -0.5 + j0.866$, $p_2 = -1$ (real), $p_3 = -0.5 - j0.866$

**2nd-order section** ($p_1, p_3$): $s^2 + s + 1$ → $\zeta = 0.5$, $Q = 1$

**1st-order section** ($p_2$): $s + 1$

**Cascade:** 1st-order (Q=0.5) → 2nd-order (Q=1)