# Final Quiz - Comprehensive Worked Examples

This document contains detailed worked examples covering all major problem types that may appear on the quiz, based on homework assignments, class slides, and typical exam problems.

---

## SECTION 1: TRANSFER FUNCTIONS & CIRCUIT ANALYSIS

### EXAMPLE 1.1: Finding H(s) from Op-Amp Circuit (HW07-P1)

**Problem:** For the inverting op-amp circuit with R1 = 1 kohm, Rf = 2 kohm, C = 0.5 microF in feedback, find H(s) = V2(s)/V1(s).

**Solution:**

**Step 1:** Identify impedances
- Input impedance: $Z_{in} = R_1 = 1000$ ohm
- Feedback impedance (parallel RC): 
$$Z_f = R_f \parallel \frac{1}{sC} = \frac{R_f \cdot \frac{1}{sC}}{R_f + \frac{1}{sC}} = \frac{R_f}{1 + sR_fC}$$

**Step 2:** Apply inverting amplifier formula
$$H(s) = -\frac{Z_f}{Z_{in}} = -\frac{R_f/(1+sR_fC)}{R_1}$$

**Step 3:** Substitute values
$$H(s) = -\frac{2000}{1000(1 + s \cdot 2000 \cdot 0.5 \times 10^{-6})}$$

$$H(s) = -\frac{2}{1 + 0.001s} = -\frac{2000}{s + 1000}$$

**Answer:** $H(s) = -\frac{2000}{s + 1000}$ (first-order low-pass with gain 2 and cutoff at 1000 rad/s)

---

### EXAMPLE 1.2: Lead Network Analysis (HW08-P1)

**Problem:** For the RC network with two series RC branches in voltage divider configuration, find:
(a) Input impedance Z(s) = V1(s)/I1(s)
(b) Transfer function H(s) = V2(s)/V1(s) in form $H(s) = K\frac{s+\beta}{s+\alpha}$
(c) Design for H(s) with beta = 1000, alpha = 100

**Solution:**

**Part (a):** Input impedance (series combination)
$$Z(s) = R_1 + \frac{1}{sC_1} + R_2 \parallel \frac{1}{sC_2}$$

For parallel branch:
$$R_2 \parallel \frac{1}{sC_2} = \frac{R_2}{1 + sR_2C_2}$$

**Part (b):** Voltage divider for H(s)
$$H(s) = \frac{Z_{output}}{Z_{total}} = \frac{R_2/(1+sR_2C_2)}{R_1 + 1/(sC_1) + R_2/(1+sR_2C_2)}$$

After algebraic manipulation:
$$H(s) = K\frac{s + 1/(R_2C_2)}{s + 1/(R_{eq}C_{eq})}$$

where K depends on component values.

**Part (c):** Design with C1 = C2 = C

Given: beta = 1000, alpha = 100

From zero: $\beta = \frac{1}{R_2C} = 1000 \implies R_2 = \frac{1}{1000C}$

From pole: $\alpha = \frac{1}{R_{eq}C} = 100 \implies R_{eq} = \frac{1}{100C}$

Choose C = 1 microF:
- $R_2 = 1$ kohm
- Need to solve for R1 based on pole constraint

---

### EXAMPLE 1.3: Series RLC Bandpass (HW07-P3)

**Problem:** Given R = 20 ohm, L = 1 H, C = 1 microF, find H(s) = V2(s)/V1(s) where V2 is across R.

**Solution:**

**Step 1:** Total impedance
$$Z_{total} = R + sL + \frac{1}{sC}$$

**Step 2:** Voltage divider (output across R)
$$H(s) = \frac{R}{R + sL + \frac{1}{sC}} = \frac{R \cdot sC}{sRLC + s^2LC + 1}$$

**Step 3:** Substitute values
$$H(s) = \frac{20s \cdot 10^{-6}}{s \cdot 20 \cdot 1 \cdot 10^{-6} + s^2 \cdot 1 \cdot 10^{-6} + 1}$$

Multiply numerator and denominator by $10^6$:
$$H(s) = \frac{20s}{s^2 + 20s + 10^6}$$

**Step 4:** Find resonant frequency
$$\omega_0 = \sqrt{\frac{1}{LC}} = \sqrt{\frac{1}{1 \times 10^{-6}}} = 1000 \text{ rad/s}$$

**Step 5:** At resonance ($\omega = 1000$ rad/s)
$$H(j1000) = \frac{20 \cdot j1000}{(j1000)^2 + 20(j1000) + 10^6} = \frac{j20000}{j20000} = 1$$

**Maximum output at resonance!**

---

## SECTION 2: PARTIAL FRACTION EXPANSION

### EXAMPLE 2.1: Basic PFE with Two Real Poles

**Problem:** Find inverse Laplace transform of $F(s) = \frac{100000}{(s+100)(s+1000)}$

**Solution:**

**Step 1:** Setup PFE
$$F(s) = \frac{k_1}{s+100} + \frac{k_2}{s+1000}$$

**Step 2:** Cover-up method for k1 (pole at s = -100)
$$k_1 = \left[(s+100) \cdot \frac{100000}{(s+100)(s+1000)}\right]_{s=-100}$$
$$k_1 = \frac{100000}{-100+1000} = \frac{100000}{900} = 111.11$$

**Step 3:** Cover-up method for k2 (pole at s = -1000)
$$k_2 = \left[(s+1000) \cdot \frac{100000}{(s+100)(s+1000)}\right]_{s=-1000}$$
$$k_2 = \frac{100000}{-1000+100} = \frac{100000}{-900} = -111.11$$

**Step 4:** Inverse Laplace transform
$$f(t) = 111.11e^{-100t} - 111.11e^{-1000t} \text{ for } t \geq 0$$

**Answer:** $f(t) = 111.11(e^{-100t} - e^{-1000t})u(t)$

---

### EXAMPLE 2.2: PFE with s Term in Numerator (HW08-P3b)

**Problem:** Find partial fraction expansion of $H(s) = \frac{10^4 s}{(s+10)(s+1000)}$ in form $K\left(\frac{\alpha}{s+\alpha} - \frac{\beta}{s+\beta}\right)$

**Solution:**

**Step 1:** Factor out constant K
$$H(s) = 10^4 \cdot \frac{s}{(s+10)(s+1000)}$$

**Step 2:** Standard PFE
$$\frac{s}{(s+10)(s+1000)} = \frac{k_1}{s+10} + \frac{k_2}{s+1000}$$

**Step 3:** Cover-up for k1
$$k_1 = \left[\frac{s}{s+1000}\right]_{s=-10} = \frac{-10}{-10+1000} = \frac{-10}{990} = -0.0101$$

**Step 4:** Cover-up for k2
$$k_2 = \left[\frac{s}{s+10}\right]_{s=-1000} = \frac{-1000}{-1000+10} = \frac{-1000}{-990} = 1.0101$$

**Step 5:** Rewrite in requested form
$$H(s) = 10^4(1.0101 \cdot \frac{1}{s+1000} - 0.0101 \cdot \frac{1}{s+10})$$

$$H(s) = 10101\left(\frac{1000}{s+1000} - \frac{10}{s+10}\right)$$

$$H(s) = 10.1\left(\frac{1000}{s+1000} - \frac{10}{s+10}\right)$$

**This shows:** K = 10.1, alpha = 1000, beta = 10

---

### EXAMPLE 2.3: Repeated Poles (HW06-P4a)

**Problem:** Given step response $v_2(t) = 24(1 - e^{-50t} - 50te^{-50t})u(t)$, find H(s).

**Solution:**

**Step 1:** Take Laplace transform
$$V_2(s) = 24\left[\frac{1}{s} - \frac{1}{s+50} - \frac{50}{(s+50)^2}\right]$$

**Step 2:** Common denominator
$$V_2(s) = 24 \cdot \frac{(s+50)^2 - s(s+50) - 50s}{s(s+50)^2}$$

$$= 24 \cdot \frac{s^2 + 100s + 2500 - s^2 - 50s - 50s}{s(s+50)^2}$$

$$= 24 \cdot \frac{2500}{s(s+50)^2} = \frac{60000}{s(s+50)^2}$$

**Step 3:** Find H(s) (input is step, so V1(s) = 1/s)
$$H(s) = \frac{V_2(s)}{V_1(s)} = V_2(s) \cdot s = \frac{60000}{(s+50)^2}$$

**This has a repeated pole at s = -50**

---

## SECTION 3: SINUSOIDAL STEADY-STATE & FREQUENCY RESPONSE

### EXAMPLE 3.1: Finding Output for Sinusoidal Input (HW07-P1)

**Problem:** Given $H(s) = -\frac{2000}{s+1000}$, find v2(t) for various inputs.

**General Method:**
1. Substitute $s = j\omega$
2. Find $|H(j\omega)|$ and $\angle H(j\omega)$
3. Output: $v_2(t) = A|H(j\omega)|\cos(\omega t + \theta + \angle H(j\omega))$

---

**Case (a): v1(t) = 5cos(10t) V (omega = 10 rad/s, much less than cutoff)**

$$H(j10) = -\frac{2000}{j10 + 1000} = -\frac{2000}{1000 + j10}$$

Magnitude:
$$|H(j10)| = \frac{2000}{\sqrt{1000^2 + 10^2}} = \frac{2000}{\sqrt{1000100}} \approx 2.0$$

Phase (negative sign contributes 180 degrees):
$$\angle H(j10) = 180° - \arctan(10/1000) = 180° - 0.57° = 179.4°$$

**Answer:** $v_2(t) = 10\cos(10t + 179.4°)$ V

---

**Case (b): v1(t) = 5cos(1000t) V (omega = cutoff frequency)**

$$H(j1000) = -\frac{2000}{j1000 + 1000} = -\frac{2000}{1000(1+j)}$$

Magnitude:
$$|H(j1000)| = \frac{2000}{1000\sqrt{2}} = \frac{2}{\sqrt{2}} = \sqrt{2} \approx 1.414$$

Phase:
$$\angle H(j1000) = 180° - 45° = 135°$$

**Answer:** $v_2(t) = 7.07\cos(1000t + 135°)$ V (This is -3 dB point!)

---

**Case (c): v1(t) = 5cos(100000t) V (omega much greater than cutoff)**

$$H(j10^5) = -\frac{2000}{j10^5 + 1000} \approx -\frac{2000}{j10^5}$$

Magnitude:
$$|H(j10^5)| = \frac{2000}{10^5} = 0.02$$

Phase:
$$\angle H(j10^5) = 180° - 90° = 90°$$

**Answer:** $v_2(t) = 0.1\cos(10^5 t + 90°)$ V

---

### EXAMPLE 3.2: Extracting H(s) from Bode Plot (HW07-P4 & P5)

**Problem Type 1:** Low-pass $H(s) = K\frac{\alpha}{s+\alpha}$

**Given from Bode plot:**
- DC gain = 6 dB
- Phase = -45 degrees at omega = 1000 rad/s

**Solution:**

Phase is -45 degrees at corner frequency, so: **alpha = 1000 rad/s**

DC gain: $20\log_{10}K = 6$ dB
$$K = 10^{6/20} = 10^{0.3} = 2$$

**Answer:** $H(s) = \frac{2 \cdot 1000}{s+1000} = \frac{2000}{s+1000}$

---

**Problem Type 2:** High-pass $H(s) = K\frac{s}{s+\alpha}$

**Given from Bode plot:**
- Phase = 45 degrees at omega = 100 rad/s
- High-frequency gain = 0 dB

**Solution:**

For high-pass, phase = 45 degrees at corner, so: **alpha = 100 rad/s**

High-frequency gain (as omega approaches infinity):
$$\lim_{\omega \to \infty}|H(j\omega)| = K$$

From plot: 0 dB means K = 1

**Answer:** $H(s) = \frac{s}{s+100}$

---

## SECTION 4: CIRCUIT DESIGN FROM H(s)

### EXAMPLE 4.1: First-Order Circuit Design (HW06-P1a)

**Problem:** Design circuit for $H(s) = \frac{200000}{s+100000}$

**Solution:**

**Step 1:** Identify characteristics
- First-order low-pass
- DC gain K = 2
- Cutoff omega_c = 100000 rad/s = 100 krad/s

**Step 2:** Choose topology - Non-inverting with RC low-pass

Basic form: $H(s) = \mu \cdot \frac{1/RC}{s + 1/RC}$

**Step 3:** Design RC section for cutoff
Choose C = 0.1 microF:
$$\omega_c = \frac{1}{RC} = 100000 \implies R = \frac{1}{100000 \times 0.1 \times 10^{-6}} = 100 \text{ ohm}$$

**Step 4:** Design op-amp gain
Need mu = 2:
$$\mu = 1 + \frac{R_f}{R_g} = 2 \implies R_f = R_g$$

Choose Rg = 10 kohm, then Rf = 10 kohm

**Final Design:**
- Input RC low-pass: R = 100 ohm, C = 0.1 microF
- Non-inverting op-amp: Rf = Rg = 10 kohm

---

### EXAMPLE 4.2: Parallel Summing Design (HW08-P3c)

**Problem:** Implement $H(s) = 10.1\left(\frac{1000}{s+1000} - \frac{10}{s+10}\right)$ using parallel summing.

**Solution:**

**Step 1:** Recognize as difference of two first-order sections
$$H(s) = K_1 \cdot \frac{\alpha_1}{s+\alpha_1} - K_2 \cdot \frac{\alpha_2}{s+\alpha_2}$$

where K1 = 10100, alpha1 = 1000, K2 = 101, alpha2 = 10

**Step 2:** Design first branch (alpha1 = 1000)

RC section: Choose C11 = 0.1 microF
$$R_{11} = \frac{1}{1000 \times 0.1 \times 10^{-6}} = 10 \text{ kohm}$$

Gain: Need 10100
Use inverting: $\frac{R_f}{R_{in}} = 10100$ (impractical - use cascade instead)

**Step 3:** Design second branch (alpha2 = 10)

RC section: Choose C21 = 1 microF
$$R_{21} = \frac{1}{10 \times 1 \times 10^{-6}} = 100 \text{ kohm}$$

**Step 4:** Use summing amplifier to combine with subtraction

The summing stage inverts, so design first stages as inverting to get correct signs.

---

### EXAMPLE 4.3: Integrator and Differentiator (HW08-P4)

**Problem:** Find H(s) for op-amp integrator and explain name.

**Solution:**

**Circuit:** Inverting op-amp with R in input, C in feedback

$$H(s) = -\frac{Z_f}{Z_{in}} = -\frac{1/(sC)}{R} = -\frac{1}{sRC}$$

**Time domain relationship:**
$$V_{out}(s) = -\frac{1}{sRC}V_{in}(s)$$

$$sV_{out}(s) = -\frac{1}{RC}V_{in}(s)$$

$$\frac{dv_{out}}{dt} = -\frac{1}{RC}v_{in}(t)$$

$$v_{out}(t) = -\frac{1}{RC}\int v_{in}(t)dt$$

**This is an integrator!**

**Differentiator:** Swap R and C
$$H(s) = -\frac{R}{1/(sC)} = -sRC$$

This gives: $v_{out}(t) = -RC\frac{dv_{in}}{dt}$

---

## SECTION 5: BUTTERWORTH FILTER DESIGN

### EXAMPLE 5.1: Complete 4th-Order Low-Pass (Class 27)

**Problem:** Design Butterworth low-pass filter:
- Hmax = 0 dB (gain = 1.0)
- Hmin = -40 dB (gain = 0.01)  
- fc = 2 kHz
- fmin = 8 kHz

**Solution:**

---

**PHASE 1: Calculate Required Order**

**Step 1:** Convert to linear and rad/s
- Hmax = 1.0 (already linear)
- Hmin = 0.01 (already linear)
- omega_C = 2pi × 2000 = 12566 rad/s
- omega_MIN = 2pi × 8000 = 50265 rad/s

**Step 2:** Apply Butterworth order formula (low-pass)
$$n \geq \frac{\ln[(H_{max}/H_{min})^2 - 1]}{2\ln(\omega_{min}/\omega_C)}$$

$$n \geq \frac{\ln[(1/0.01)^2 - 1]}{2\ln(50265/12566)} = \frac{\ln(10000-1)}{2\ln(4)}$$

$$n \geq \frac{\ln(9999)}{2\ln(4)} = \frac{9.210}{2.773} = 3.32$$

**Round UP:** **n = 4**

**Step 3:** Section breakdown
n = 4 (even) → 2 second-order sections, 0 first-order sections

---

**PHASE 2: Calculate Butterworth Poles**

**Step 4:** Pole angles for n = 4
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n} = \frac{\pi}{2} + \frac{(2k-1)\pi}{8}$$

For k = 1, 2, 3, 4:
- theta_1 = pi/2 + pi/8 = 5pi/8 = 112.5 degrees
- theta_2 = pi/2 + 3pi/8 = 7pi/8 = 157.5 degrees
- theta_3 = pi/2 + 5pi/8 = 9pi/8 = 202.5 degrees
- theta_4 = pi/2 + 7pi/8 = 11pi/8 = 247.5 degrees

**Step 5:** Pole locations (normalized, |p| = 1)
- p1 = cos(112.5°) + j sin(112.5°) = -0.383 + j0.924
- p2 = cos(157.5°) + j sin(157.5°) = -0.924 + j0.383
- p3 = cos(202.5°) + j sin(202.5°) = -0.924 - j0.383
- p4 = cos(247.5°) + j sin(247.5°) = -0.383 - j0.924

**Use only left-half-plane poles (all have negative real parts)**

---

**PHASE 3: Extract Section Parameters**

**Section 1:** Pair p1 and p4 (conjugates)
$$(s - p_1)(s - p_4^*) = s^2 - (p_1 + p_4)s + p_1 \cdot p_4$$

$$= s^2 - 2(-0.383)s + (0.383^2 + 0.924^2)$$

$$= s^2 + 0.765s + 1$$

Extract parameters:
- Coefficient a = 0.765
- Damping ratio: zeta_1 = a/2 = 0.383
- Quality factor: Q_1 = 1/(2×0.383) = 1.307

**Section 2:** Pair p2 and p3 (conjugates)
$$s^2 + 1.848s + 1$$

- Coefficient a = 1.848
- Damping ratio: zeta_2 = 0.924
- Quality factor: Q_2 = 0.541

---

**PHASE 4: Design Using Unity Gain Method**

**Section 1:** zeta = 0.383, omega_0 = 12566 rad/s

Choose C1 = 0.1 microF:

$$C_2 = 4\zeta^2 C_1 = 4(0.383)^2(0.1 \text{ microF}) = 0.0586 \text{ microF}$$

Use standard value: **C2 = 0.056 microF** or **0.068 microF**

$$R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1} = \frac{1}{0.383 \times 12566 \times 0.1 \times 10^{-6}}$$

$$= 2078 \text{ ohm} \approx 2.2 \text{ kohm}$$

**Section 2:** zeta = 0.924, omega_0 = 12566 rad/s

Choose C1 = 0.1 microF:

$$C_2 = 4(0.924)^2(0.1) = 0.341 \text{ microF}$$

Use standard value: **C2 = 0.33 microF**

$$R_1 = R_2 = \frac{1}{0.924 \times 12566 \times 0.1 \times 10^{-6}} = 861 \text{ ohm}$$

Use standard value: **R1 = R2 = 820 ohm**

---

**PHASE 5: Cascade Assembly**

**Order by Q (LOW to HIGH):**

1. **First stage:** Section 2 (Q = 0.541, lower)
   - R1 = R2 = 820 ohm
   - C1 = 0.1 microF, C2 = 0.33 microF
   - Op-amp as buffer (mu = 1)

2. **Second stage:** Section 1 (Q = 1.307, higher)
   - R1 = R2 = 2.2 kohm
   - C1 = 0.1 microF, C2 = 0.056 microF
   - Op-amp as buffer (mu = 1)

**Total H(s):**
$$H_{total}(s) = H_1(s) \times H_2(s)$$

---

### EXAMPLE 5.2: 3rd-Order Butterworth (Odd Order)

**Problem:** Design 3rd-order Butterworth low-pass with fc = 1 kHz.

**Solution:**

**Step 1:** Section count
n = 3 (odd) → 1 first-order + 1 second-order section

**Step 2:** Pole angles
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{6}$$

For k = 1, 2, 3:
- theta_1 = pi/2 + pi/6 = 2pi/3 = 120° → p1 = -0.5 + j0.866
- theta_2 = pi/2 + 3pi/6 = pi = 180° → p2 = -1 (REAL pole)
- theta_3 = pi/2 + 5pi/6 = 4pi/3 = 240° → p3 = -0.5 - j0.866

**Step 3:** Second-order section (p1, p3)
$$s^2 + s + 1$$

- zeta = 0.5
- omega_0 = 2pi × 1000 = 6283 rad/s

**Unity Gain Design:**

Choose C1 = 0.1 microF:
$$C_2 = 4(0.5)^2(0.1) = 0.1 \text{ microF}$$

$$R_1 = R_2 = \frac{1}{0.5 \times 6283 \times 0.1 \times 10^{-6}} = 3183 \text{ ohm}$$

Use: **R1 = R2 = 3.3 kohm**

**Step 4:** First-order section (p2 at s = -omega_c)

$$H_{1st}(s) = \frac{1}{1 + s/\omega_c}$$

Passive RC: Choose C = 0.1 microF:
$$R = \frac{1}{6283 \times 0.1 \times 10^{-6}} = 1592 \text{ ohm}$$

Use: **R = 1.6 kohm**

**Step 5:** Cascade order
**First-order first, then second-order** (buffer between stages)

---

### EXAMPLE 5.3: High-Pass 2nd-Order Butterworth (Class 28)

**Problem:** Design 2nd-order high-pass:
- fc = 20 kHz
- High-frequency gain = 0 dB
- Corner gain = -3 dB (Butterworth characteristic)

**Solution:**

**Step 1:** Recognize standard 2nd-order Butterworth
- n = 2 → zeta = 0.707
- omega_0 = 2pi × 20000 = 125664 rad/s

**Step 2:** Unity Gain Method for HIGH-PASS

**Key difference:** Swap R and C positions from low-pass

Choose R2 = 10 kohm:

$$R_1 = 4\zeta^2 R_2 = 4(0.707)^2(10 \text{ kohm}) = 20 \text{ kohm}$$

$$C_1 = C_2 = C = \frac{1}{\zeta\omega_0 R_2}$$

$$= \frac{1}{0.707 \times 125664 \times 10000} = 1.13 \times 10^{-9} \text{ F}$$

Use: **C1 = C2 = 1.2 nF** or **1.0 nF**

**Step 3:** Circuit topology
Sallen-Key high-pass:
- Capacitors in series with input path
- Resistors to ground
- Op-amp as buffer

---

### EXAMPLE 5.4: High-Pass Order Calculation (Class 28 Example)

**Problem:** Design high-pass Butterworth:
- Hmax = 20 dB (gain = 10)
- Hmin = -40 dB (gain = 0.01)
- fc = 10 kHz
- fmin = 1 kHz (note: fmin < fc for high-pass!)

**Solution:**

**Step 1:** Apply HIGH-PASS order formula (note reversed frequencies!)
$$n \geq \frac{\ln[(H_{max}/H_{min})^2 - 1]}{2\ln(\omega_C/\omega_{min})}$$

Notice: omega_C in numerator for high-pass (opposite of low-pass)

$$n \geq \frac{\ln[(10/0.01)^2 - 1]}{2\ln(62832/6283)} = \frac{\ln(999999)}{2\ln(10)}$$

$$= \frac{13.816}{4.605} = 3.0$$

**Exactly n = 3** (no need to round up)

**Step 2:** Section breakdown
n = 3 → 1 first-order + 1 second-order

**Then proceed with pole calculations and design as before...**

---

## SECTION 6: EQUAL ELEMENTS METHOD

### EXAMPLE 6.1: When to Use Equal Elements vs Unity Gain

**Problem:** Design 2nd-order section with:
- omega_0 = 1000 rad/s
- zeta = 0.5

Can we use equal elements method?

**Solution:**

**Equal Elements Constraint:**
For equal elements method (R1 = R2 = R, C1 = C2 = C):
$$\mu = 3 - 2\zeta$$

For zeta = 0.5:
$$\mu = 3 - 2(0.5) = 2$$

**This is valid!** (mu >= 1 and zeta < 1)

**Equal Elements Design:**

Choose C = 0.1 microF:
$$R = \frac{1}{\zeta\omega_0 C} = \frac{1}{0.5 \times 1000 \times 0.1 \times 10^{-6}} = 20 \text{ kohm}$$

Gain stage: Need mu = 2
$$\mu = 1 + \frac{R_f}{R_g} = 2 \implies R_f = R_g$$

Choose Rg = 10 kohm, then Rf = 10 kohm

**Unity Gain Alternative:**

Choose C1 = 0.1 microF:
$$C_2 = 4\zeta^2 C_1 = 4(0.5)^2(0.1) = 0.1 \text{ microF}$$

$$R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1} = 20 \text{ kohm}$$

**Both methods work! Equal elements is simpler here.**

---

### EXAMPLE 6.2: When Unity Gain is Required

**Problem:** Design 2nd-order section with:
- omega_0 = 1000 rad/s
- zeta = 1.5 (overdamped)

**Solution:**

**Check Equal Elements:**
$$\mu = 3 - 2(1.5) = 0$$

**This fails!** (mu must be >= 1)

**Must use Unity Gain Method:**

Choose C1 = 0.1 microF:
$$C_2 = 4\zeta^2 C_1 = 4(1.5)^2(0.1) = 0.9 \text{ microF}$$

$$R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1} = \frac{1}{1.5 \times 1000 \times 0.1 \times 10^{-6}}$$

$$= 6667 \text{ ohm} \approx 6.8 \text{ kohm}$$

**Key Rule:** 
- Equal elements: ONLY for 0 < zeta < 1 (underdamped)
- Unity gain: Works for ALL zeta values (including overdamped)

---

## SECTION 7: STATE-VARIABLE FILTER (HW08-P5)

### EXAMPLE 7.1: Understanding State-Variable Filter

**Problem:** For the state-variable filter in HW08-P5, derive H(s) = V2(s)/V1(s).

**Solution:**

**Step 1:** Recognize cascaded integrators

The two right-side op-amps are integrators:
$$V_4(s) = -\frac{1}{sRC}V_2(s)$$

$$V_3(s) = -\frac{1}{sRC}V_4(s) = \frac{1}{(sRC)^2}V_2(s) = s^2(RC)^2V_2(s)$$

**Step 2:** Analyze leftmost op-amp

Non-inverting input (V+): Voltage divider from V1 and V2 feedback
$$V_+(s) = \frac{-sRCR_1V_2(s) + R_2V_1(s)}{R_1 + R_2}$$

Inverting input (V-): Voltage divider from V3 and ground
$$V_-(s) = \frac{s^2(RC)^2R_4V_2(s)}{R_3 + R_4}$$

**Step 3:** Apply ideal op-amp property (V+ = V-)

$$\frac{-sRCR_1V_2(s) + R_2V_1(s)}{R_1 + R_2} = \frac{s^2(RC)^2R_4V_2(s)}{R_3 + R_4}$$

**Step 4:** With R4 = R3, solve for H(s)

After algebraic manipulation:
$$H(s) = \frac{V_2(s)}{V_1(s)} = \frac{\frac{R_2(R_3+R_4)}{(R_1+R_2)R_3}}{s^2(RC)^2\frac{R_4}{R_3} + sRC\frac{R_1(R_3+R_4)}{(R_1+R_2)R_3} + 1}$$

With R4 = R3:
$$H(s) = \frac{K}{\left(\frac{s}{\omega_0}\right)^2 + 2\zeta\left(\frac{s}{\omega_0}\right) + 1}$$

where:
- $\omega_0 = \frac{1}{RC}$
- $2\zeta = 2\frac{R_1}{R_1 + R_2}$
- $K = \frac{R_2(2R_3)}{(R_1+R_2)R_3} = \frac{2R_2}{R_1+R_2}$

**Key Advantage:** Can tune omega_0 and zeta independently!

---

## SECTION 8: COMMON MISTAKES TO AVOID

### MISTAKE 1: Wrong Butterworth Order Formula

**WRONG (Low-Pass):**
$$n \geq \frac{\ln[(H_{max}/H_{min})^2 - 1]}{2\ln(\omega_{min}/\omega_C)}$$

with omega_MIN < omega_C (INCORRECT!)

**CORRECT (Low-Pass):**
$$n \geq \frac{\ln[(H_{max}/H_{min})^2 - 1]}{2\ln(\omega_{min}/\omega_C)}$$

with omega_MIN > omega_C (frequency beyond passband)

**CORRECT (High-Pass):**
$$n \geq \frac{\ln[(H_{max}/H_{min})^2 - 1]}{2\ln(\omega_C/\omega_{min})}$$

with omega_MIN < omega_C (frequency below passband)

---

### MISTAKE 2: Forgetting to Scale Poles

**Problem:** 4th-order Butterworth with fc = 2 kHz

**WRONG:** Use normalized poles directly in H(s)

**CORRECT:** Scale ALL poles by omega_c
- Normalized: p1 = -0.383 + j0.924
- Scaled: p1 = omega_c(-0.383 + j0.924) = 12566(-0.383 + j0.924)

---

### MISTAKE 3: Wrong Cascade Order

**WRONG:** Place high-Q section first

**CORRECT:** Always cascade LOW Q to HIGH Q
- Prevents overload of high-Q section
- Better overall performance

---

### MISTAKE 4: Confusing zeta and Q

**Relationship:** 
$$Q = \frac{1}{2\zeta}$$

**Example:**
- If zeta = 0.5, then Q = 1.0 (NOT 0.5!)
- If Q = 1.307, then zeta = 0.383 (NOT 1.307!)

---

### MISTAKE 5: Using Equal Elements When zeta >= 1

**Example:** zeta = 1.2 (overdamped)

**WRONG:** Try equal elements method
$$\mu = 3 - 2(1.2) = 0.6$$ (less than 1, INVALID!)

**CORRECT:** Must use unity gain method

**Rule:** Equal elements ONLY for 0 < zeta < 1

---

## SECTION 9: QUICK FORMULAS REFERENCE

### First-Order Sections

**Low-Pass:**
$$H(s) = K\frac{\alpha}{s + \alpha}$$
- DC gain: K
- Cutoff: alpha rad/s
- Slope: -20 dB/decade

**High-Pass:**
$$H(s) = K\frac{s}{s + \alpha}$$
- High-frequency gain: K
- Cutoff: alpha rad/s
- Slope: +20 dB/decade

### Second-Order Sections

**Standard Form:**
$$H(s) = \frac{K\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$

**Key Parameters:**
- Resonant frequency: omega_0 rad/s
- Damping ratio: zeta
- Quality factor: Q = 1/(2*zeta)
- Bandwidth (low-pass): B = 2*zeta*omega_0
- Peak gain (underdamped): K/(2*zeta) at omega_0

### Butterworth Pole Angles

**Formula:**
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{2n}$$

for k = 1, 2, ..., n

**Common Values:**
- n=2: 135°, 225° → conjugate pair
- n=3: 120°, 180°, 240° → one real, one conjugate pair
- n=4: 112.5°, 157.5°, 202.5°, 247.5° → two conjugate pairs

### Sallen-Key Design Formulas

**Equal Elements (R1=R2=R, C1=C2=C):**
- Constraint: mu = 3 - 2*zeta (only valid for 0 < zeta < 1)
- R = 1/(zeta * omega_0 * C)

**Unity Gain (mu=1, R1=R2):**
- C2 = 4*zeta^2 * C1
- R1 = R2 = 1/(zeta * omega_0 * C1)
- Works for ALL zeta values

---

## SECTION 10: FINAL CHECKLIST

### Before Submitting Your Answer:

**Transfer Functions:**
- [ ] Correct form (low-pass vs high-pass)?
- [ ] Units correct (rad/s)?
- [ ] Gain at appropriate frequency correct?
- [ ] Poles in left-half plane?

**Butterworth Design:**
- [ ] Used correct order formula (low-pass vs high-pass)?
- [ ] Rounded order UP to integer?
- [ ] Calculated poles at correct angles?
- [ ] Scaled poles by omega_c?
- [ ] Paired conjugate poles correctly?
- [ ] Cascaded sections in correct order (low Q to high Q)?

**Circuit Design:**
- [ ] Component values realistic (10 ohm to 1 Mohm, 1 pF to 1000 microF)?
- [ ] Used standard values when required?
- [ ] Correct op-amp configuration (inverting/non-inverting)?
- [ ] All grounds and connections shown?
- [ ] Gain stages correct?

**Frequency Response:**
- [ ] Magnitude units (linear or dB)?
- [ ] Phase units (degrees or radians)?
- [ ] Correct asymptotic behavior (omega → 0 and omega → infinity)?
- [ ] Corner frequencies correct?

---

## APPENDIX: STANDARD COMPONENT VALUES

### Standard Resistor Values (E12 series):
10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82 (and multiples)

### Standard Capacitor Values:
**pF range:** 10, 22, 47, 100, 220, 470
**nF range:** 1.0, 2.2, 4.7, 10, 22, 47, 100, 220, 470
**microF range:** 0.1, 0.22, 0.47, 1.0, 2.2, 4.7, 10, 22, 47, 100

### Typical Choices for Design:
- **R:** 1k, 2.2k, 4.7k, 10k, 22k, 47k, 100k
- **C:** 0.01 microF, 0.1 microF, 1.0 microF, 10 microF

---

**END OF WORKED EXAMPLES**

*Good luck on your quiz! Remember to:*
1. *Read problems carefully*
2. *Show your work*
3. *Check units*
4. *Verify reasonableness of answers*