# Butterworth Filter Design - Comprehensive Worked Examples

This document contains detailed worked examples covering all major problem types for Butterworth filter design, based on typical homework and exam problems.

---

## EXAMPLE 1: Basic Low-Pass Filter Design (Given All Specs)

### Problem Statement
Design a low-pass Butterworth filter with the following specifications:
- Passband: DC to 2 kHz with maximum gain $H_{MAX} = 0$ dB (gain = 1)
- Stopband: Above 8 kHz with minimum attenuation $H_{MIN} = -40$ dB (gain = 0.01)
- Implement using Sallen-Key topology

### Solution

**Step 1: Convert specifications to rad/s**
$$f_C = 2 \text{ kHz} \rightarrow \omega_C = 2\pi \times 2000 = 12566 \text{ rad/s}$$
$$f_{MIN} = 8 \text{ kHz} \rightarrow \omega_{MIN} = 2\pi \times 8000 = 50265 \text{ rad/s}$$

**Step 2: Calculate minimum order**
$$n \geq \frac{\ln[(1/0.01)^2-1]}{2\ln(50265/12566)} = \frac{\ln(9999)}{2\ln(4)} = \frac{9.210}{2.773} = 3.32$$

**Round up: n = 4** (4th order filter)

**Step 3: Determine section breakdown**
- n = 4 (even) → 2 second-order sections
- No first-order sections needed

**Step 4: Calculate pole angles for n = 4**
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{8}$$

For k = 1, 2, 3, 4:
- $\theta_1 = \frac{\pi}{2} + \frac{\pi}{8} = \frac{5\pi}{8} = 112.5°$
- $\theta_2 = \frac{\pi}{2} + \frac{3\pi}{8} = \frac{7\pi}{8} = 157.5°$
- $\theta_3 = \frac{\pi}{2} + \frac{5\pi}{8} = \frac{9\pi}{8} = 202.5°$
- $\theta_4 = \frac{\pi}{2} + \frac{7\pi}{8} = \frac{11\pi}{8} = 247.5°$

**Step 5: Calculate pole locations**
- $p_1 = \cos(112.5°) + j\sin(112.5°) = -0.383 + j0.924$
- $p_2 = \cos(157.5°) + j\sin(157.5°) = -0.924 + j0.383$
- $p_3 = -0.924 - j0.383$ (conjugate of $p_2$)
- $p_4 = -0.383 - j0.924$ (conjugate of $p_1$)

All in left half-plane ✓

**Step 6: Form second-order sections**

**Section 1** (poles $p_1, p_4$):
$$(s - p_1)(s - p_4) = s^2 - 2(-0.383)s + [(-0.383)^2 + (0.924)^2]$$
$$= s^2 + 0.765s + 1$$

Compare to standard form $s^2 + 2\zeta\omega_0 s + \omega_0^2$:
- $\omega_0 = 1$ (normalized)
- $2\zeta = 0.765$
- $\zeta = 0.383$
- $Q = \frac{1}{2(0.383)} = 1.307$

**Section 2** (poles $p_2, p_3$):
$$s^2 + 1.848s + 1$$

- $\zeta = 0.924$
- $Q = 0.541$

**Step 7: Design Method Selection**

Both sections have $0 < \zeta < 1$, so we can use either method. Choose **Unity Gain Method** for both sections (always works).

**Step 8: Design Section 1** ($\zeta = 0.383$, $\omega_0 = 12566$ rad/s)

Choose $C_1 = 0.1$ $\mu $F

$$C_2 = 4(0.383)^2(0.1\text{ $\mu $F}) = 0.0586 \text{ $\mu $F} \approx 0.056 \text{ $\mu $F (standard)}$$

$$R = \frac{1}{0.383 \times 12566 \times 0.1 \times 10^{-6}} = 2078 \text{ ohms} \approx 2.2 \text{ k ohms (standard)}$$

**Step 9: Design Section 2** ($\zeta = 0.924$, $\omega_0 = 12566$ rad/s)

Choose $C_1 = 0.1$ $\mu $F

$$C_2 = 4(0.924)^2(0.1\text{ $\mu $F}) = 0.341 \text{ $\mu $F} \approx 0.33 \text{ $\mu $F (standard)}$$

$$R = \frac{1}{0.924 \times 12566 \times 0.1 \times 10^{-6}} = 861 \text{ ohms} \approx 820 \text{ ohms (standard)}$$

**Step 10: Cascade Order**

Section 2 (Q = 0.541, higher $\zeta$) → Section 1 (Q = 1.307, lower $\zeta$)

**Final Design:**
- **Stage 1**: $R_1 = R_2 = 820$ ohms, $C_1 = 0.1$ $\mu $F, $C_2 = 0.33$ $\mu $F, $\mu = 1$
- **Stage 2**: $R_1 = R_2 = 2.2$ k ohms, $C_1 = 0.1$ $\mu $F, $C_2 = 0.056$ $\mu $F, $\mu = 1$

---

## EXAMPLE 2: High-Pass Filter with Gain Requirement

### Problem Statement
Design a 3rd-order high-pass Butterworth filter with:
- Cutoff frequency: $f_C = 500$ Hz
- Stopband frequency: $f_{MIN} = 100$ Hz
- Stopband attenuation: $H_{MIN} = -50$ dB
- Overall passband gain: K = 10

### Solution

**Step 1: Verify order requirement**

Convert to linear: $H_{MIN} = 10^{-50/20} = 0.00316$

$$n \geq \frac{\ln[(1/0.00316)^2-1]}{2\ln(3142/628)} = \frac{\ln(99999)}{2\ln(5)} = \frac{11.51}{3.22} = 3.58$$

**Given n = 3**, check if sufficient: $3 < 3.58$ → Need n = 4 minimum!

However, if problem states "design 3rd order," proceed with n = 3 (may not meet all specs).

**Step 2: Convert to rad/s**
$$\omega_C = 2\pi \times 500 = 3142 \text{ rad/s}$$

**Step 3: Pole angles for n = 3**
$$\theta_k = \frac{\pi}{2} + \frac{(2k-1)\pi}{6}$$

- $\theta_1 = \frac{2\pi}{3} = 120°$ → $p_1 = -0.5 + j0.866$
- $\theta_2 = \pi = 180°$ → $p_2 = -1$ (real pole)
- $\theta_3 = \frac{4\pi}{3} = 240°$ → $p_3 = -0.5 - j0.866$

**Step 4: Form sections**

**Second-order section** ($p_1, p_3$):
$$s^2 + s + 1$$
- $\zeta = 0.5$
- $Q = 1.0$

**First-order section** ($p_2$):
$$s + 1$$

**Step 5: Design high-pass sections**

For high-pass Sallen-Key, we **swap R and C** from low-pass design.

**Second-order HP** (Unity Gain, $\zeta = 0.5$, $\omega_0 = 3142$ rad/s):

Choose $R_2 = 10$ k ohms

$$R_1 = 4(0.5)^2(10\text{ k ohms}) = 10 \text{ k ohms}$$

$$C = \frac{1}{0.5 \times 3142 \times 10000} = 63.7 \text{ nF} \approx 68 \text{ nF}$$

So: $R_1 = R_2 = 10$ k ohms, $C_1 = C_2 = 68$ nF

**First-order HP** ($\omega_C = 3142$ rad/s):

$$H(s) = \frac{sRC}{1 + sRC}$$

Choose $C = 68$ nF:
$$R = \frac{1}{3142 \times 68 \times 10^{-9}} = 4.68 \text{ k ohms} \approx 4.7 \text{ k ohms}$$

**Step 6: Add gain of K = 10**

Distribute gain equally: $K_1 = K_2 = \sqrt{10} \approx 3.16$ per section

For 2nd-order section, use Equal Elements Method:
- Need $\mu = 3.16$
- But Equal Elements requires $\mu = 3 - 2(0.5) = 2$ ✗

Alternative: Add gain stage at output:
$$\mu_{final} = 1 + \frac{R_f}{R_g} = 10$$

Choose $R_g = 1$ k ohms → $R_f = 9$ k ohms

**Final Cascade:**
1st-order HP → 2nd-order HP → Gain stage (non-inverting amp with gain 10)

---

## EXAMPLE 3: Design from Transfer Function H(s)

### Problem Statement
Given the transfer function:
$$H(s) = \frac{10000}{(s+50)(s^2 + 100s + 10000)}$$

Implement this filter using Sallen-Key topology.

### Solution

**Step 1: Identify structure**
- Numerator: constant → Low-pass filter
- Denominator: one real pole + one complex conjugate pair
- Order: n = 3

**Step 2: Extract section parameters**

**First-order section:** $s + 50$
- Pole at $s = -50$
- $\omega_C = 50$ rad/s

**Second-order section:** $s^2 + 100s + 10000$
- Compare to $s^2 + 2\zeta\omega_0 s + \omega_0^2$
- $\omega_0^2 = 10000$ → $\omega_0 = 100$ rad/s
- $2\zeta\omega_0 = 100$ → $2\zeta(100) = 100$ → $\zeta = 0.5$
- $Q = 1.0$

**Step 3: Design first-order section**

$$\omega_C = 50 \text{ rad/s}$$

Choose $C = 1$ $\mu $F:
$$R = \frac{1}{50 \times 1 \times 10^{-6}} = 20 \text{ k ohms}$$

**Step 4: Design second-order section (Unity Gain)**

$\zeta = 0.5$, $\omega_0 = 100$ rad/s

Choose $C_1 = 1$ $\mu $F:
$$C_2 = 4(0.5)^2(1\text{ $\mu $F}) = 1 \text{ $\mu $F}$$
$$R = \frac{1}{0.5 \times 100 \times 1 \times 10^{-6}} = 20 \text{ k ohms}$$

**Step 5: Verify DC gain**

Given $H(0) = \frac{10000}{50 \times 10000} = 0.02$

Designed sections both have unity gain → Need gain stage:
$$K = 0.02 \text{ (or can be distributed)}$$

**Final Implementation:**
- 1st-order: $R = 20$ k ohms, $C = 1$ $\mu $F
- 2nd-order: $R_1 = R_2 = 20$ k ohms, $C_1 = C_2 = 1$ $\mu $F, $\mu = 1$
- Attenuator at input or output to achieve DC gain of 0.02

---

## EXAMPLE 4: Given Bode Plot, Find H(s)

### Problem Statement
A Bode magnitude plot shows:
- DC gain: 20 dB
- -3 dB frequency: 1 kHz
- Asymptotic slope: -40 dB/decade starting at 1 kHz
- Phase at 1 kHz: -90°

Determine H(s) and identify the filter type.

### Solution

**Step 1: Extract information**
- DC gain = 20 dB → Linear: $K = 10^{20/20} = 10$
- $\omega_C = 2\pi \times 1000 = 6283$ rad/s
- Slope = -40 dB/dec → 2nd order
- Phase = -90° at $\omega_C$ → Butterworth 2nd order

**Step 2: Identify filter type**
- Constant at DC, rolls off at high frequency → Low-pass
- 2nd order Butterworth → $\zeta = 0.707$

**Step 3: Write H(s)**

Standard 2nd-order Butterworth LP:
$$H(s) = \frac{K\omega_C^2}{s^2 + \sqrt{2}\omega_C s + \omega_C^2}$$

$$H(s) = \frac{10 \times (6283)^2}{s^2 + \sqrt{2}(6283)s + (6283)^2}$$

$$H(s) = \frac{3.95 \times 10^8}{s^2 + 8886s + 3.95 \times 10^7}$$

**Verification:**
- At DC ($s = 0$): $H(0) = \frac{3.95 \times 10^8}{3.95 \times 10^7} = 10$ ✓
- At $\omega_C$ ($s = j6283$): $|H(j6283)| = \frac{10}{\sqrt{2}} = 7.07$ → 20log(7.07) = 17 dB (20 - 3 = 17) ✓

---

## EXAMPLE 5: Frequency and Impedance Scaling

### Problem Statement
A normalized 2nd-order low-pass Butterworth filter has:
- $R = 1$ ohms, $C = 1$ F, $\omega_C = 1$ rad/s

Scale this design to:
- New cutoff: $f_C = 10$ kHz
- Practical component values: $R$ around 10 k ohms

### Solution

**Step 1: Determine scaling factors**

**Frequency scaling:**
$$k_f = \frac{\omega_{new}}{\omega_{old}} = \frac{2\pi \times 10000}{1} = 62832$$

**Impedance scaling:**
$$k_z = \frac{R_{new}}{R_{old}} = \frac{10000}{1} = 10000$$

**Step 2: Apply scaling**

**Resistors:**
$$R_{new} = k_z \times R_{old} = 10000 \times 1 = 10 \text{ k ohms}$$

**Capacitors:**
$$C_{new} = \frac{C_{old}}{k_f \times k_z} = \frac{1}{62832 \times 10000} = 1.59 \times 10^{-9} \text{ F} = 1.59 \text{ nF}$$

Use standard value: $C = 1.5$ nF

**Step 3: Verify new cutoff**
$$\omega_{C,new} = \frac{1}{R_{new}C_{new}} = \frac{1}{10000 \times 1.5 \times 10^{-9}} = 66667 \text{ rad/s}$$

$$f_{C,new} = \frac{66667}{2\pi} = 10.6 \text{ kHz}$$ (close to 10 kHz target)

---

## EXAMPLE 6: Equal Elements Method Design

### Problem Statement
Design a 2nd-order low-pass Butterworth filter using the Equal Elements Method:
- Cutoff frequency: $f_C = 5$ kHz
- Use $C = 0.01$ $\mu $F

### Solution

**Step 1: Identify parameters**
- 2nd-order Butterworth → $\zeta = 0.707$
- $\omega_C = 2\pi \times 5000 = 31416$ rad/s

**Step 2: Check if Equal Elements is valid**
$$0 < \zeta < 1$$ → 0.707 is valid ✓

**Step 3: Calculate op-amp gain**
$$\mu = 3 - 2\zeta = 3 - 2(0.707) = 1.586$$

**Step 4: Calculate resistor values**
$$R = \frac{1}{\omega_C C} = \frac{1}{31416 \times 0.01 \times 10^{-6}} = 3.18 \text{ k ohms}$$

Use $R_1 = R_2 = 3.3$ k ohms (standard value)

**Step 5: Design op-amp gain circuit**
$$\mu = 1 + \frac{R_f}{R_g} = 1.586$$

$$\frac{R_f}{R_g} = 0.586$$

Choose $R_g = 10$ k ohms → $R_f = 5.86$ k ohms \approx 5.6 k ohms (standard)

**Final Design:**
- Main circuit: $R_1 = R_2 = 3.3$ k ohms, $C_1 = C_2 = 0.01$ $\mu $F
- Gain resistors: $R_f = 5.6$ k ohms, $R_g = 10$ k ohms

---

## EXAMPLE 7: Bandpass Filter Design

### Problem Statement
Design a bandpass filter to pass frequencies from 1 kHz to 5 kHz with:
- Minimum attenuation of -40 dB below 200 Hz
- Minimum attenuation of -40 dB above 25 kHz

### Solution

**Step 1: Identify requirements**
- Lower cutoff: $f_1 = 1$ kHz ($\omega_1 = 6283$ rad/s)
- Upper cutoff: $f_2 = 5$ kHz ($\omega_2 = 31416$ rad/s)
- Lower stopband: $f_{s1} = 200$ Hz
- Upper stopband: $f_{s2} = 25$ kHz

**Step 2: Design highpass section** (for lower cutoff)

$$n_{HP} \geq \frac{\ln[(1/0.01)^2-1]}{2\ln(6283/1257)} = \frac{9.21}{3.22} = 2.86$$

Round up: $n_{HP} = 3$

Design 3rd-order HP with $\omega_C = 6283$ rad/s (from Example 2)

**Step 3: Design lowpass section** (for upper cutoff)

$$n_{LP} \geq \frac{\ln[(1/0.01)^2-1]}{2\ln(157080/31416)} = \frac{9.21}{3.22} = 2.86$$

Round up: $n_{LP} = 3$

Design 3rd-order LP with $\omega_C = 31416$ rad/s:
- One 1st-order + one 2nd-order section
- Use normalized poles, scale to $\omega_C = 31416$ rad/s

**Step 4: Cascade sections**
$$H_{BP}(s) = H_{HP}(s) \times H_{LP}(s)$$

Order: HP sections first, then LP sections

**Total order:** 3 + 3 = 6th order bandpass filter

**Step 5: Calculate center frequency and bandwidth**
$$\omega_0 = \sqrt{\omega_1 \omega_2} = \sqrt{6283 \times 31416} = 14048 \text{ rad/s}$$
$$f_0 = 2.24 \text{ kHz}$$

$$BW = \omega_2 - \omega_1 = 25133 \text{ rad/s}$$

---

## EXAMPLE 8: Component Value Selection from Specs

### Problem Statement
A 2nd-order Sallen-Key low-pass section requires:
- $\zeta = 0.383$
- $\omega_0 = 10000$ rad/s
- Must use $R_1 = 10$ k ohms

Find $R_2, C_1, C_2$ using Unity Gain Method.

### Solution

**Unity Gain equations:**
$$R_1 = R_2 = R = \frac{1}{\zeta\omega_0 C_1}$$

$$C_2 = 4\zeta^2 C_1$$

**Step 1: Given $R_1 = 10$ k ohms, find $C_1$**
$$10000 = \frac{1}{0.383 \times 10000 \times C_1}$$

$$C_1 = \frac{1}{0.383 \times 10000 \times 10000} = 2.61 \times 10^{-8} \text{ F} = 26.1 \text{ nF}$$

Use standard value: $C_1 = 27$ nF

**Step 2: Calculate $C_2$**
$$C_2 = 4(0.383)^2(27\text{ nF}) = 15.9 \text{ nF}$$

Use standard value: $C_2 = 15$ nF

**Step 3: Verify $R_2$**

Since Unity Gain Method requires $R_1 = R_2$:
$$R_2 = 10 \text{ k ohms}$$

**Final values:**
- $R_1 = R_2 = 10$ k ohms
- $C_1 = 27$ nF
- $C_2 = 15$ nF
- $\mu = 1$ (buffer)

---

## EXAMPLE 9: Verifying Filter Performance

### Problem Statement
A designed 4th-order Butterworth low-pass filter has:
- Section 1: $\zeta_1 = 0.924$, $\omega_0 = 5000$ rad/s
- Section 2: $\zeta_2 = 0.383$, $\omega_0 = 5000$ rad/s

Verify that this meets the specification: -40 dB at 20 kHz.

### Solution

**Step 1: Write section transfer functions**

**Section 1:**
$$H_1(s) = \frac{\omega_0^2}{s^2 + 2(0.924)(5000)s + 5000^2} = \frac{25 \times 10^6}{s^2 + 9240s + 25 \times 10^6}$$

**Section 2:**
$$H_2(s) = \frac{25 \times 10^6}{s^2 + 3830s + 25 \times 10^6}$$

**Overall:**
$$H(s) = H_1(s) \times H_2(s)$$

**Step 2: Evaluate at $\omega = 2\pi \times 20000 = 125664$ rad/s**

For Section 1 at $s = j125664$:
$$|H_1(j\omega)| = \frac{25 \times 10^6}{\sqrt{(25 \times 10^6 - \omega^2)^2 + (9240\omega)^2}}$$

$$= \frac{25 \times 10^6}{\sqrt{(25 \times 10^6 - 1.58 \times 10^{10})^2 + (1.16 \times 10^9)^2}}$$

$$\approx \frac{25 \times 10^6}{1.58 \times 10^{10}} = 0.00158$$

Similarly for Section 2: $|H_2(j\omega)| \approx 0.00158$

**Overall magnitude:**
$$|H(j\omega)| = 0.00158 \times 0.00158 = 2.5 \times 10^{-6}$$

$$20\log_{10}(2.5 \times 10^{-6}) = -112 \text{ dB}$$

This exceeds -40 dB requirement ✓ (much better attenuation)

---

## EXAMPLE 10: Troubleshooting - Why Unity Gain Required

### Problem Statement
Attempt to design a 2nd-order section with $\zeta = 1.2$ using Equal Elements Method. What goes wrong?

### Solution

**Step 1: Check Equal Elements validity**
$$\mu = 3 - 2\zeta = 3 - 2(1.2) = -0.4$$

**Problem:** $\mu = -0.4 < 1$

This is impossible! A non-inverting amplifier must have $\mu \geq 1$.

**Step 2: Why this happens**

Equal Elements Method constraint:
$$\mu = 3 - 2\zeta \geq 1$$
$$3 - 1 \geq 2\zeta$$
$$\zeta \leq 1$$

For $\zeta = 1.2 > 1$, the method **cannot work**.

**Step 3: Correct approach - Unity Gain Method**

With $\zeta = 1.2$, use Unity Gain:

Choose $C_1 = 0.1$ $\mu $F:
$$C_2 = 4(1.2)^2(0.1) = 0.576 \text{ $\mu $F}$$
$$R = \frac{1}{1.2 \times \omega_0 \times 0.1 \times 10^{-6}}$$

**Lesson:** Always check $\zeta < 1$ before using Equal Elements. For overdamped systems ($\zeta \geq 1$), **must use Unity Gain Method**.

---

## PRACTICE PROBLEMS (Try These!)

### Problem A
Design a 5th-order low-pass Butterworth filter with $f_C = 3$ kHz to meet -50 dB attenuation at 15 kHz.

### Problem B
Given $H(s) = \frac{10^8}{(s+100)(s^2+200s+10000)}$, identify all section parameters and design the circuit.

### Problem C
Convert a 3rd-order normalized low-pass filter to a high-pass filter with $f_C = 8$ kHz.

### Problem D
Design a bandstop filter to reject 60 Hz \pm 10 Hz (notch out 50-70 Hz) with -40 dB rejection.

---

## SUMMARY OF KEY TAKEAWAYS

1. **Always round order UP** - Never round down or you won't meet specs
2. **Check $\zeta < 1$** before using Equal Elements Method
3. **Unity Gain works for everything** - It's the safe choice
4. **Order sections by Q** - Low Q (high $\zeta$) first
5. **Use standard component values** - Nearest E12/E24 series
6. **Verify DC gain** - Make sure overall gain matches requirements
7. **Frequency scaling** - Affects only C (not R)
8. **Impedance scaling** - Affects both R and C oppositely
9. **Bandpass = Cascade** - Multiply transfer functions
10. **Bandstop = Parallel Sum** - Add transfer functions

---

## END OF WORKED EXAMPLES