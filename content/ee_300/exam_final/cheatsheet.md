---
title: Filter Design Cheatsheet
description: Concise problem-solving guide for filter design including Butterworth and Chebyshev filters, Sallen-Key circuits, and Bode analysis
weight: 1
---

# Filter Design Cheatsheet

## DESIGN PROCESS OVERVIEW

### PHASE 1: IDENTIFY SPECIFICATIONS
- Transfer function $H(s)$ given → Phase 3
- Frequency specs ($\omega_c$, $H_{MAX}$, $H_{MIN}$, $\omega_{MIN}$) → Phase 2
- Time response → Extract $\zeta$, $\omega_0$ → Phase 2
- Bode plot → Extract poles/zeros → Phase 3

**Filter Type Identification:**
- **Lowpass:** $H(s) = K/(s^2 + bs + c)$ or $K/(s + \alpha)$
- **Highpass:** $H(s) = Ks^2/(s^2 + bs + c)$ or $Ks/(s + \alpha)$
- **Bandpass:** $H(s) = Ks/(s^2 + bs + c)$
- **Band-Stop:** $H(s) = K(s^2 + \omega_0^2)/(s^2 + bs + c)$

### PHASE 2: CALCULATE FILTER ORDER

**Butterworth (Maximally Flat):**
- Lowpass: $n_B = \lceil \frac{1}{2} \frac{\log[(H_{MAX}/H_{MIN})^2 - 1]}{\log(\omega_{MIN}/\omega_c)} \rceil$
- Highpass: $n_B = \lceil \frac{1}{2} \frac{\log[(H_{MAX}/H_{MIN})^2 - 1]}{\log(\omega_c/\omega_{MIN})} \rceil$

**Chebyshev (Steeper Roll-off):**
- Lowpass: $n_C = \lceil \frac{\cosh^{-1}(\sqrt{(H_{MAX}/H_{MIN})^2 - 1})}{\cosh^{-1}(\omega_{MIN}/\omega_c)} \rceil$
- Highpass: $n_C = \lceil \frac{\cosh^{-1}(\sqrt{(H_{MAX}/H_{MIN})^2 - 1})}{\cosh^{-1}(\omega_c/\omega_{MIN})} \rceil$

**Round up to nearest integer!**

### PHASE 3: FACTOR H(s) INTO SECTIONS

1. Get poles from polynomial tables
2. Factor: $H(s) = K / [(s + \alpha_1)(s^2 + b_2s + c_2)(s^2 + b_3s + c_3)]$
3. Real pole → 1st order section
4. Complex pair → 2nd order section

**Extract 2nd order parameters:**
- $\omega_0 = \sqrt{c}$
- $\zeta = \frac{b}{2\sqrt{c}}$
- $Q = \frac{\sqrt{c}}{b} = \frac{1}{2\zeta}$

### PHASE 4: DESIGN 2ND ORDER SECTIONS (SALLEN-KEY)

**ALWAYS TRY UNITY GAIN FIRST!**

**Unity Gain Method ($\mu = 1$) - PREFERRED:**
- Works for ALL $\zeta$ values
- Most stable configuration

**Lowpass:**
1. Set $\mu = 1$ (buffer)
2. Choose $C_1$
3. $C_2 = 4\zeta^2 C_1$
4. $R_1 = R_2 = \frac{1}{\zeta\omega_0 C_1}$

**Highpass:**
1. Set $\mu = 1$
2. Choose $R_2$
3. $R_1 = 4\zeta^2 R_2$
4. $C_1 = C_2 = \frac{1}{\zeta\omega_0 R_2}$

**Equal Elements Method ($\mu = 3 - 2\zeta$):**
- **ONLY for $0 < \zeta < 1$**
- Set $R_1 = R_2 = R$, $C_1 = C_2 = C$
- $R = \frac{1}{\omega_0 C}$
- $\mu = 3 - 2\zeta$
- $\mu = 1 + \frac{R_f}{R_g}$

**Topology Swap:** Highpass = swap all $R \leftrightarrow C$ from lowpass

### PHASE 5: DESIGN 1ST ORDER SECTIONS

**Passive RC:**
- Lowpass: $H(s) = \frac{1}{1 + sRC}$, $\omega_c = \frac{1}{RC}$
- Highpass: $H(s) = \frac{sRC}{1 + sRC}$, $\omega_c = \frac{1}{RC}$

**Active (Non-Inverting):**
- $H(s) = \frac{K}{1 + sRC}$
- $K = 1 + \frac{R_f}{R_g}$
- $\omega_c = \frac{1}{RC}$

### PHASE 6: CASCADE & ORDER SECTIONS

**Section Ordering (Critical!):**
1. FIRST: Lowest $Q$ (Highest $\zeta$)
2. MIDDLE: Medium $Q$
3. LAST: Highest $Q$ (Lowest $\zeta$)

**Prevents early clipping from resonant peaks**

**Gain Distribution:**
- All in first stage, OR
- Equal distribution: $K^{1/n}$ per stage, OR
- All in last stage

**Verify:** $H_{total}(s) = H_1(s) \times H_2(s) \times \cdots \times H_n(s)$

### PHASE 7: BANDPASS & BAND-STOP

**Bandpass (Cascade):**
- $H_{BP}(s) = H_{LP}(s) \times H_{HP}(s)$
- LP with $\omega_{c2}$ (upper) × HP with $\omega_{c1}$ (lower)
- $\omega_0 = \sqrt{\omega_{c1} \omega_{c2}}$
- $BW = \omega_{c2} - \omega_{c1}$

**Band-Stop (Parallel):**
- $H_{BS}(s) = H_{LP}(s) + H_{HP}(s)$
- LP with $\omega_{c1}$ + HP with $\omega_{c2}$
- Use summing amplifier

### PHASE 8: COMPONENT SCALING

**Frequency Scaling ($\times k_f$):**
- $R_{new} = R_{old}$ (unchanged)
- $C_{new} = \frac{C_{old}}{k_f}$
- $\omega_{new} = k_f \omega_{old}$

**Impedance Scaling ($\times k_z$):**
- $R_{new} = k_z R_{old}$
- $C_{new} = \frac{C_{old}}{k_z}$
- $H(s)$, $\omega$ unchanged

### PHASE 9: VERIFICATION

- Cutoff frequency correct?
- Gain at DC/∞ correct?
- Order matches calculated $n$?
- All $\zeta$ achievable with chosen method?
- Components: R (1kΩ-1MΩ), C (100pF-10μF)
- Op-amp: $GBW \geq 100 f_c Q K$

## KEY FORMULAS

**Standard 2nd Order:**
- Lowpass: $\frac{K\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
- Highpass: $\frac{Ks^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
- Bandpass: $\frac{K(2\zeta\omega_0)s}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$

**Relationships:**
- $Q = \frac{1}{2\zeta}$, $\zeta = \frac{1}{2Q}$
- $BW = 2\zeta\omega_0 = \frac{\omega_0}{Q}$
- $\omega_0 = \frac{1}{RC}$ (equal elements)

**Damping:**
- $\zeta > 1$: Overdamped, Unity Gain ONLY
- $\zeta = 1$: Critically Damped, Unity Gain ONLY
- $0 < \zeta < 1$: Underdamped, Either method

## BODE PLOT ESSENTIALS

**Axes:**
- X: $\log_{10}(\omega)$
- Y: $20\log_{10}(|H(j\omega)|)$ dB

**Slopes:**
- 1st order LP: -20 dB/decade
- 1st order HP: +20 dB/decade
- 2nd order LP: -40 dB/decade
- 2nd order HP: +40 dB/decade
- nth order: $\pm 20n$ dB/decade

**Corner Frequency ($\omega_c$):**
- Actual: -3 dB from asymptote
- Approximation: lines intersect

**Decibel Conversions:**
- 0 dB = 1.0
- -3 dB = 0.707
- -6 dB = 0.5
- -20 dB = 0.1
- 20 dB = 10

**Plotting Complex $H(s)$:**
1. Find all poles/zeros
2. Order by frequency
3. Start with DC/HF asymptote
4. At each break: change slope by ±20 or ±40 dB/dec
5. Poles: decrease slope
6. Zeros: increase slope

## CRITICAL DESIGN TIPS

**DO:**
- Try Unity Gain first
- Check $\zeta$ before using Equal Elements
- Order sections by Q (low → high)
- Use buffers between stages
- Verify practical component values

**DON'T:**
- Use Equal Elements for $\zeta \geq 1$
- Forget to round up $n$
- Mix up LP/HP frequency ratios
- Cascade high-Q sections first
- Use extreme component values

**Quick Checks:**
- Lowpass: $H(0)$ = max
- Highpass: $H(\infty)$ = max
- Butterworth at $\omega_c$: $|H| = K/\sqrt{2}$
- Unity gain: direct connection
- Equal elements: need gain resistors ($\mu > 1$)