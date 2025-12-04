# Butterworth Filter Design Cheatsheet

## CORE CONCEPT

**Butterworth = Maximally Flat Magnitude Response**
- No ripple in passband
- Poles evenly distributed on circle in s-plane
- At cutoff: $|H(j\omega_C)| = H_{MAX}/\sqrt{2}$ (-3 dB) ALWAYS

---

## PHASE 1: CALCULATE FILTER ORDER

### Given Specifications
- $H_{MAX}$: Maximum passband gain (linear or dB)
- $H_{MIN}$: Minimum stopband gain (linear or dB)  
- $\omega_C$ (or $f_C$): Cutoff frequency
- $\omega_{MIN}$ (or $f_{MIN}$): Stopband frequency where $H_{MIN}$ must be met

### Convert Units

**dB to Linear:**
$$H_{\text{linear}} = 10^{H_{\text{dB}}/20}$$

**Hz to rad/s:**
$$\omega = 2\pi f$$

### Calculate Minimum Order

**Low-Pass (stopband ABOVE cutoff):**
$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_{MIN}/\omega_C)}$$

**High-Pass (stopband BELOW cutoff):**
$$n \geq \frac{1}{2} \cdot \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{\ln(\omega_C/\omega_{MIN})}$$

**CRITICAL: ALWAYS ROUND UP to nearest integer**

### Why This Formula Works

Starting from Butterworth magnitude response:
$$|H(j\omega)|^2 = \frac{H_{MAX}^2}{1 + (\omega/\omega_C)^{2n}}$$

At stopband frequency $\omega_{MIN}$:
$$|H(j\omega_{MIN})| = H_{MIN}$$

Substituting and solving:
$$\frac{H_{MAX}^2}{1 + (\omega_{MIN}/\omega_C)^{2n}} = H_{MIN}^2$$

$$(\omega_{MIN}/\omega_C)^{2n} = \frac{H_{MAX}^2}{H_{MIN}^2} - 1$$

Taking logarithm of both sides:
$$2n \ln(\omega_{MIN}/\omega_C) = \ln[(H_{MAX}/H_{MIN})^2 - 1]$$

$$n = \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{2\ln(\omega_{MIN}/\omega_C)}$$

### Determine Section Count

- **Even $n$:** Use $n/2$ second-order sections
- **Odd $n$:** Use $(n-1)/2$ second-order sections + 1 first-order section

---

## PHASE 2: CALCULATE BUTTERWORTH POLES

### Pole Angles (Normalized $\omega_C = 1$)

For each pole $k = 1, 2, \ldots, n$:
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

**Note:** $k$ is just an enumeration index (1, 2, 3...). It has NO electrical meaning.

### Pole Locations (Normalized)

$$p_k = e^{j\theta_k} = \cos(\theta_k) + j\sin(\theta_k)$$

**Properties:**
- All poles have magnitude $|p_k| = 1$ (on unit circle)
- **Only use LEFT half-plane poles** (Real part < 0)
- Complex poles always come in conjugate pairs

### Denormalize Poles

Scale by actual cutoff frequency:
$$p_{k,\text{actual}} = \omega_C \cdot p_k$$

## PHASE 3: EXTRACT SECTION PARAMETERS

### Form Quadratic from Conjugate Pair

For poles $p = \alpha + j\beta$ and $p^* = \alpha - j\beta$:

$$(s - p)(s - p^*) = s^2 - (p + p^*)s + p \cdot p^*$$

Since $p + p^* = 2\alpha$ and $p \cdot p^* = \alpha^2 + \beta^2 = |p|^2$:

$$(s - p)(s - p^*) = s^2 - 2\alpha s + (\alpha^2 + \beta^2)$$

For normalized poles ($|p| = 1$):
$$s^2 + as + 1$$

where $a = -2\text{Re}(p) = -2\cos(\theta_k)$

### Extract Damping Ratio $\zeta$

Standard second-order form:
$$s^2 + 2\zeta\omega_0 s + \omega_0^2$$

For normalized ($\omega_0 = 1$):
$$s^2 + 2\zeta s + 1$$

Comparing coefficients:
$$2\zeta = a = -2\cos(\theta_k)$$

$$\zeta = -\cos(\theta_k) = \frac{a}{2}$$

**Why negative?** Poles are in left half-plane, so $\cos(\theta_k) < 0$ for $90° < \theta_k < 270°$.

### Calculate Quality Factor $Q$

$$Q = \frac{1}{2\zeta}$$

**Relationships:**
- Higher $Q$ → Lower $\zeta$ → More resonance/peaking
- Lower $Q$ → Higher $\zeta$ → More damping

---

## PHASE 4: UNITY GAIN SALLEN-KEY DESIGN (2nd Order)

### Why Unity Gain is ALWAYS Preferred

- **Works for ALL $\zeta$ values** (even $\zeta \geq 1$ overdamped)
- Most stable configuration
- Op-amp as simple buffer ($\mu = 1$)
- Zero sensitivity to gain variations

### Design Equations - Low-Pass

**Given:** $\omega_0$ (rad/s) and $\zeta$ for the section

**Option A - Choose $C_1$ (typical: 0.01 to 1 μF):**

$$C_2 = 4\zeta^2 C_1$$

$$R_1 = R_2 = R = \frac{1}{\zeta\omega_0 C_1}$$

**Option B - Choose $R_2$ (typical: 1kΩ to 100kΩ):**

$$R_1 = 4\zeta^2 R_2$$

$$C_1 = C_2 = C = \frac{1}{\zeta\omega_0 R_2}$$

### Why These Formulas Work

From Sallen-Key transfer function with $\mu = 1$:

$$H(s) = \frac{1}{R_1R_2C_1C_2 s^2 + (R_1C_1 + R_2C_1 + R_1C_2)s + 1}$$

Comparing to standard form $s^2 + 2\zeta\omega_0 s + \omega_0^2$:

$$\omega_0 = \frac{1}{\sqrt{R_1R_2C_1C_2}}$$

$$2\zeta\omega_0 = \frac{R_1C_1 + R_2C_1 + R_1C_2}{R_1R_2C_1C_2}$$

**For Option A** (R1 = R2 = R, choose C1):

$$\omega_0 = \frac{1}{R\sqrt{C_1C_2}}$$

$$2\zeta = \frac{2C_1 + C_2}{\sqrt{C_1C_2}}$$

Solving: $C_2 = 4\zeta^2 C_1$ and $R = \frac{1}{\zeta\omega_0 C_1}$

### Design Equations - High-Pass

**KEY: Swap ALL R ↔ C from low-pass design**

**With $R_2$ chosen:**

$$R_1 = 4\zeta^2 R_2$$

$$C_1 = C_2 = C = \frac{1}{\zeta\omega_0 R_2}$$

---

## PHASE 5: FIRST-ORDER SECTIONS (Odd Order Only)

### For Real Pole at $s = -\omega_C$

**Transfer Function:**
$$H(s) = \frac{1}{1 + s/\omega_C} = \frac{\omega_C}{s + \omega_C}$$

### Passive RC Design

**Circuit:** Series R, shunt C to ground

$$\omega_C = \frac{1}{RC}$$

**Design:** Choose C, then:
$$R = \frac{1}{\omega_C C}$$

**Properties:**
- DC gain = 1
- Slope: -20 dB/decade
- No resonance (monotonic response)

### Active Design (with gain K)

$$H(s) = \frac{K}{1 + sRC}$$

Use non-inverting op-amp:
$$K = 1 + \frac{R_f}{R_g}$$

---

## PHASE 6: CASCADE ASSEMBLY

### Section Ordering - CRITICAL

**Rule: Order by Q from LOW to HIGH**

Equivalently: Order by $\zeta$ from HIGH to LOW

| Order | $Q$ | $\zeta$ | Reason |
|-------|-----|---------|---------|
| First | 0.541 | 0.924 | Low Q = high damping = no peaks |
| Last | 1.307 | 0.383 | High Q = resonance peaks = must be last |

**Why?** High-Q sections have resonant peaks. If placed first, they amplify input → clipping. Low-Q sections first reduce signal gradually.

### Buffering

**Good News:** Each Sallen-Key stage naturally has:
- High input impedance (op-amp input)
- Low output impedance (op-amp output)

**Result:** No additional buffers needed between stages!

### Overall Transfer Function

$$H_{\text{total}}(s) = H_1(s) \times H_2(s) \times \cdots \times H_n(s)$$

**Verification:**
- Multiply all section transfer functions
- Check DC gain (set $s = 0$)
- Check high-frequency behavior ($s \to \infty$)

---

## PHASE 7: COMPONENT SCALING

### When Calculated Values Are Impractical

### Frequency Scaling (multiply by $k_f$)

$$C_{\text{new}} = \frac{C_{\text{old}}}{k_f}$$

$$R_{\text{new}} = R_{\text{old}}$$ (unchanged)

**Effect:** $\omega_{\text{new}} = k_f \times \omega_{\text{old}}$

**Example:** To shift cutoff from 1 kHz to 10 kHz, use $k_f = 10$

### Impedance Scaling (multiply by $k_z$)

$$R_{\text{new}} = k_z \times R_{\text{old}}$$

$$C_{\text{new}} = \frac{C_{\text{old}}}{k_z}$$

**Effect:** $H(s)$ and frequencies unchanged

**Example:** To increase resistors by factor of 10, use $k_z = 10$

### Combined Scaling

$$R_{\text{final}} = k_z \times R_{\text{normalized}}$$

$$C_{\text{final}} = \frac{C_{\text{normalized}}}{k_f \times k_z}$$

### Practical Component Ranges

| Component | Practical Range | Preferred Range |
|-----------|-----------------|-----------------|
| Resistors | 100Ω - 10MΩ | 1kΩ - 1MΩ |
| Capacitors | 1pF - 1000μF | 100pF - 10μF |

---

## UNDERSTANDING TRANSFER FUNCTIONS FROM LINEAR H(s)

### Given: Linear Transfer Function

Example: $H(s) = \frac{K}{s + 1000}$

### Identify Filter Type

**From Denominator:**
- First-order (degree 1): One real pole
- Second-order (degree 2): Complex conjugate pair

**From Numerator:**
- Constant → Low-pass
- $s$ term → High-pass or Band-pass
- $s^2$ term → High-pass (2nd order)

### Extract Pole Locations

For $H(s) = \frac{K}{s + 1000}$:

Denominator: $s + 1000 = 0$

Pole: $s = -1000$ (real pole at $-1000$ rad/s)

### Extract Cutoff Frequency

For first-order: $\omega_C = |\text{pole}| = 1000$ rad/s

### Extract DC Gain

$$H(0) = \frac{K}{0 + 1000} = \frac{K}{1000}$$

If DC gain should be 1: $K = 1000$

### For Second-Order: $H(s) = \frac{K}{s^2 + bs + c}$

**Find poles:** Solve $s^2 + bs + c = 0$

$$s = \frac{-b \pm \sqrt{b^2 - 4c}}{2}$$

**If complex conjugate pair ($b^2 < 4c$):**

$$\omega_0 = \sqrt{c}$$

$$\zeta = \frac{b}{2\sqrt{c}}$$

$$Q = \frac{\sqrt{c}}{b}$$

**Now use these in Unity Gain design formulas!**

---

## POLE ANGLES - COMPLETE DERIVATION

### Why Butterworth Poles Are on a Circle

Butterworth magnitude-squared:
$$|H(s)|^2 = \frac{1}{1 + (s/j\omega_C)^{2n}}$$

Poles occur where denominator = 0:
$$1 + (s/j\omega_C)^{2n} = 0$$

$$(s/j\omega_C)^{2n} = -1 = e^{j(2m+1)\pi}$$

$$s/j\omega_C = e^{j(2m+1)\pi/(2n)}$$

$$s = j\omega_C e^{j(2m+1)\pi/(2n)}$$

Since $j = e^{j\pi/2}$:

$$s = \omega_C e^{j[\pi/2 + (2m+1)\pi/(2n)]}$$

For $m = 0, 1, 2, \ldots, n-1$ (using $k = m+1$):

$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

### Plugging into Pole Formula

1. **Calculate $\theta_k$ for your section's pole**
   
   Example: For $n=4$, $k=1$:
   $$\theta_1 = \frac{\pi}{2} + \frac{(2 \cdot 1 - 1)\pi}{2 \cdot 4} = \frac{\pi}{2} + \frac{\pi}{8} = \frac{5\pi}{8} = 112.5°$$

2. **Calculate pole location:**
   $$p_1 = \cos(112.5°) + j\sin(112.5°) = -0.383 + j0.924$$

3. **Extract $a$ coefficient:**
   $$a = -2\cos(\theta_1) = -2\cos(112.5°) = -2(-0.383) = 0.765$$

4. **Calculate $\zeta$:**
   $$\zeta = \frac{a}{2} = \frac{0.765}{2} = 0.383$$

5. **Calculate $Q$:**
   $$Q = \frac{1}{2\zeta} = \frac{1}{2(0.383)} = 1.307$$

6. **Now design Unity Gain section** with $\zeta = 0.383$ and $\omega_0 = \omega_C$

---

## WORKED EXAMPLE: 4th-Order Low-Pass

### Given
- $H_{MAX} = 0$ dB → 1.0 linear
- $H_{MIN} = -40$ dB → 0.01 linear
- $f_C = 2$ kHz → $\omega_C = 12566$ rad/s
- $f_{MIN} = 8$ kHz → $\omega_{MIN} = 50265$ rad/s

### Step 1: Calculate Order

$$n \geq \frac{\ln[(1/0.01)^2 - 1]}{2\ln(50265/12566)} = \frac{\ln(9999)}{2\ln(4)} = \frac{9.210}{2.773} = 3.32$$

**Round UP: $n = 4$**

### Step 2: Calculate Poles

For $n=4$, $k = 1, 2, 3, 4$:

$$\theta_1 = 112.5°, \quad \theta_2 = 157.5°, \quad \theta_3 = 202.5°, \quad \theta_4 = 247.5°$$

Normalized poles:
- $p_1 = -0.383 + j0.924$
- $p_2 = -0.924 + j0.383$
- $p_3 = -0.924 - j0.383$ (conjugate of $p_2$)
- $p_4 = -0.383 - j0.924$ (conjugate of $p_1$)

### Step 3: Form Sections

**Section 1** (poles $p_1, p_4$):
$$s^2 + 0.765s + 1$$
- $\zeta = 0.383$, $Q = 1.307$

**Section 2** (poles $p_2, p_3$):
$$s^2 + 1.848s + 1$$
- $\zeta = 0.924$, $Q = 0.541$

### Step 4: Design Unity Gain Sections

**Section 1:** Choose $C_1 = 0.1$ μF

$$C_2 = 4(0.383)^2(0.1) = 0.0586 \text{ μF} \approx 0.056 \text{ μF}$$

$$R = \frac{1}{0.383 \times 12566 \times 0.1 \times 10^{-6}} = 2078\text{ Ω} \approx 2.2\text{ kΩ}$$

**Section 2:** Choose $C_1 = 0.1$ μF

$$C_2 = 4(0.924)^2(0.1) = 0.341 \text{ μF} \approx 0.33 \text{ μF}$$

$$R = \frac{1}{0.924 \times 12566 \times 0.1 \times 10^{-6}} = 861\text{ Ω} \approx 820\text{ Ω}$$

### Step 5: Cascade (LOW Q → HIGH Q)

1. **Section 2** ($Q = 0.541$): R1=R2=820Ω, C1=0.1μF, C2=0.33μF
2. **Section 1** ($Q = 1.307$): R1=R2=2.2kΩ, C1=0.1μF, C2=0.056μF

---

## KEY FORMULAS SUMMARY

**Order:**
$$n \geq \frac{\ln[(H_{MAX}/H_{MIN})^2 - 1]}{2\ln(\omega_{MIN}/\omega_C)} \quad \text{(LP)}$$

**Pole Angles:**
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

**Damping:**
$$\zeta = -\cos(\theta_k) = \frac{a}{2}, \quad Q = \frac{1}{2\zeta}$$

**Unity Gain (choose $C_1$):**
$$C_2 = 4\zeta^2 C_1, \quad R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1}$$

**First-Order:**
$$H(s) = \frac{1}{1 + sRC}, \quad \omega_C = \frac{1}{RC}$$

---

## DESIGN WORKFLOW

**Given Specs → Circuit:**
1. Calculate $n$ (round UP)
2. Find pole angles $\theta_k$
3. Extract $\zeta$ for each section
4. Use Unity Gain formulas
5. Order sections by $Q$ (low → high)
6. Scale components
7. Cascade with buffers

**Given Linear $H(s)$ → Design:**
1. Factor denominator → find poles
2. Extract $\omega_0$, $\zeta$ from each factor
3. Use Unity Gain formulas
4. Cascade sections

---