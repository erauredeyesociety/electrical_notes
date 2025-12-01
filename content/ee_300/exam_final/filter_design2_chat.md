pelase help fill in the gaps, i don't want example problems, i want all the explanation for all high level theory and relevant equations.

# Comprehensive Filter Design Theory & Equations

## Extended Mathematical Foundations

### Complex Frequency and the s-Domain

The **complex frequency** variable is defined as:
$$s = \sigma + j\omega$$

where:
- $\sigma$ is the real part (damping/growth rate)
- $\omega$ is the imaginary part (oscillation frequency)
- $j = \sqrt{-1}$

For **frequency response analysis**, we evaluate $H(s)$ along the imaginary axis by substituting $s = j\omega$:
$$H(j\omega) = |H(j\omega)| \angle \phi(\omega)$$

The magnitude in decibels:
$$|H(j\omega)|_{dB} = 20\log_{10}|H(j\omega)|$$

### Standard Second-Order Transfer Function

The general form of a second-order transfer function is:

$$H(s) = \frac{K \cdot N(s)}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$$

where:
- $K$ = DC gain or high-frequency gain
- $N(s)$ = numerator polynomial (determines filter type)
- $\zeta$ = damping ratio
- $\omega_0$ = undamped natural frequency (rad/s)

**Filter-specific numerators:**
- **Lowpass:** $N(s) = \omega_0^2$ → $H(s) = \frac{K\omega_0^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
- **Highpass:** $N(s) = s^2$ → $H(s) = \frac{Ks^2}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
- **Bandpass:** $N(s) = 2\zeta\omega_0 s$ → $H(s) = \frac{K \cdot 2\zeta\omega_0 s}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$
- **Notch (Band Stop):** $N(s) = s^2 + \omega_0^2$ → $H(s) = \frac{K(s^2 + \omega_0^2)}{s^2 + 2\zeta\omega_0 s + \omega_0^2}$

### Pole-Zero Analysis

**Poles** are the roots of the denominator:
$$s^2 + 2\zeta\omega_0 s + \omega_0^2 = 0$$

Solution using the quadratic formula:
$$s_{1,2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$$

**Three damping cases:**

1. **Underdamped** ($0 < \zeta < 1$): Complex conjugate poles
   $$s_{1,2} = -\zeta\omega_0 \pm j\omega_0\sqrt{1-\zeta^2} = -\sigma \pm j\omega_d$$
   
   where $\omega_d = \omega_0\sqrt{1-\zeta^2}$ is the **damped natural frequency**

2. **Critically Damped** ($\zeta = 1$): Two real, equal poles
   $$s_{1,2} = -\omega_0$$

3. **Overdamped** ($\zeta > 1$): Two real, distinct poles
   $$s_{1,2} = -\zeta\omega_0 \pm \omega_0\sqrt{\zeta^2 - 1}$$

### Quality Factor (Q)

The **quality factor** is inversely related to damping:
$$Q = \frac{1}{2\zeta}$$

or equivalently:
$$\zeta = \frac{1}{2Q}$$

**Physical interpretations:**
- $Q > 0.5$ ($\zeta < 1$): Underdamped, exhibits resonance
- $Q = 0.5$ ($\zeta = 1$): Critically damped
- $Q < 0.5$ ($\zeta > 1$): Overdamped

**Resonant frequency** (for underdamped systems):
$$\omega_r = \omega_0\sqrt{1-2\zeta^2} = \omega_0\sqrt{1-\frac{1}{2Q^2}}$$

Note: Resonance only exists when $\zeta < 1/\sqrt{2}$ (i.e., $Q > 1/\sqrt{2}$)

**Peak magnitude** at resonance:
$$|H(j\omega_r)|_{max} = \frac{Q}{\sqrt{1-\frac{1}{4Q^2}}} \approx Q \text{ (for } Q \gg 1\text{)}$$

### Bandwidth Relationships

For a second-order lowpass or bandpass filter:

**3-dB Bandwidth:**
$$B = 2\zeta\omega_0 = \frac{\omega_0}{Q}$$

**Half-power frequencies** (for bandpass):
$$\omega_1 = \omega_0\left(-\zeta + \sqrt{\zeta^2 + 1}\right)$$
$$\omega_2 = \omega_0\left(\zeta + \sqrt{\zeta^2 + 1}\right)$$

where $B = \omega_2 - \omega_1$

---

## Detailed Sallen-Key Circuit Equations

### Sallen-Key Lowpass Configuration

**General circuit impedances:**
- Input series: $Z_1, Z_2$
- Feedback: $Y_1, Y_2$ (admittances)
- Op-amp gain: $\mu$ (non-inverting configuration)

**Transfer function derivation:**
$$H(s) = \frac{V_{out}(s)}{V_{in}(s)} = \frac{\mu}{Z_1 Z_2 Y_1 Y_2 + sZ_1(Y_1+Y_2) + (1-\mu)sZ_1Y_1 + 1}$$

**For lowpass with $Z_1=R_1$, $Z_2=R_2$, $Y_1=sC_1$, $Y_2=sC_2$:**

$$H(s) = \frac{\mu}{R_1R_2C_1C_2s^2 + [R_1C_1 + R_2C_1 + R_1C_2(1-\mu)]s + 1}$$

**Comparing to standard form:**
$$s^2 + 2\zeta\omega_0 s + \omega_0^2$$

we get:

$$\omega_0 = \frac{1}{\sqrt{R_1R_2C_1C_2}}$$

$$2\zeta\omega_0 = \frac{R_1C_1 + R_2C_1 + R_1C_2(1-\mu)}{R_1R_2C_1C_2}$$

Simplifying the damping expression:
$$\zeta = \frac{1}{2}\sqrt{\frac{R_1C_1 + R_2C_1 + R_1C_2(1-\mu)}{R_2C_2}}$$

### Equal Elements Method (Lowpass)

**Constraints:** $R_1 = R_2 = R$ and $C_1 = C_2 = C$

**Results:**
$$\omega_0 = \frac{1}{RC}$$

$$\zeta = \frac{3-\mu}{2}$$

Rearranging for op-amp gain:
$$\mu = 3 - 2\zeta$$

**Valid range:** Since $\mu \geq 1$ (non-inverting amplifier), we need:
$$3 - 2\zeta \geq 1$$
$$\zeta \leq 1$$

This confirms the method only works for underdamped systems ($0 < \zeta < 1$).

**Component selection procedure:**
1. Choose convenient capacitor value $C$
2. Calculate $R = \frac{1}{\omega_0 C}$
3. Calculate $\mu = 3 - 2\zeta$
4. Design op-amp gain circuit: $\mu = 1 + \frac{R_f}{R_g}$

### Unity Gain Method (Lowpass)

**Constraint:** $\mu = 1$ (voltage follower configuration)

The damping equation becomes:
$$\zeta = \frac{1}{2}\left(\sqrt{\frac{C_1}{C_2}} + \sqrt{\frac{R_2}{R_1}}\right)$$

**Design approach 1 - Choose capacitor ratio:**

Let $m = \frac{C_1}{C_2}$, then choose $R_1 = R_2 = R$:

$$\omega_0 = \frac{1}{R\sqrt{C_1C_2}} = \frac{1}{RC_2\sqrt{m}}$$

$$\zeta = \frac{1}{2}(\sqrt{m} + 1)$$

Solving for $m$:
$$m = (2\zeta - 1)^2$$

Then:
$$C_2 = \frac{1}{\omega_0 R\sqrt{m}}$$
$$C_1 = mC_2$$

**Design approach 2 - Choose resistor ratio:**

Let $k = \frac{R_2}{R_1}$, then choose $C_1 = C_2 = C$:

$$\omega_0 = \frac{1}{C\sqrt{R_1R_2}} = \frac{1}{CR_1\sqrt{k}}$$

$$\zeta = \frac{1}{2}(1 + \sqrt{k})$$

Solving for $k$:
$$k = (2\zeta - 1)^2$$

### Sallen-Key Highpass Configuration

**Key transformation:** Swap all Rs ↔ Cs from lowpass

**For highpass with $Z_1=\frac{1}{sC_1}$, $Z_2=\frac{1}{sC_2}$, $Y_1=\frac{1}{R_1}$, $Y_2=\frac{1}{R_2}$:**

$$H(s) = \frac{\mu s^2}{s^2 + \frac{1}{C_2}\left(\frac{1}{R_1}+\frac{1}{R_2}+\frac{1-\mu}{R_1}\right)s + \frac{1}{R_1R_2C_1C_2}}$$

**Equal Elements Method (Highpass):**

With $R_1 = R_2 = R$ and $C_1 = C_2 = C$:

$$\omega_0 = \frac{1}{RC}$$
$$\mu = 3 - 2\zeta$$

(Same relationships as lowpass!)

**Unity Gain Method (Highpass):**

With $\mu = 1$ and $R_1 = R_2 = R$:

Let $m = \frac{C_2}{C_1}$ (note the inversion from lowpass):

$$\zeta = \frac{1}{2}(\sqrt{m} + 1)$$
$$m = (2\zeta - 1)^2$$

---

## Butterworth Filter Theory

### Magnitude Response

The **magnitude-squared function** for an $n^{th}$-order Butterworth lowpass filter:

$$|H(j\omega)|^2 = \frac{1}{1 + \left(\frac{\omega}{\omega_C}\right)^{2n}}$$

where $\omega_C$ is the **-3dB cutoff frequency** (half-power point).

**Key properties:**
- At DC ($\omega = 0$): $|H(0)| = 1$ (0 dB)
- At cutoff ($\omega = \omega_C$): $|H(j\omega_C)| = \frac{1}{\sqrt{2}}$ (-3 dB)
- Asymptotic slope: $-20n$ dB/decade for $\omega \gg \omega_C$

**Maximally flat property:**

The first $(2n-1)$ derivatives of $|H(j\omega)|^2$ are zero at $\omega = 0$, giving the flattest possible passband response.

### Pole Locations

Butterworth poles lie on a **circle** of radius $\omega_C$ in the left-half s-plane:

$$s_k = \omega_C \cdot e^{j(\pi/2 + (2k+n-1)\pi/(2n))}$$

for $k = 1, 2, ..., n$

**Simplified angle formula:**
$$\theta_k = \frac{\pi}{2} + \frac{(2k+n-1)\pi}{2n} = \frac{(2k+n-1)\pi}{2n}$$

**For even $n$:** Poles are symmetrically placed, no pole on the real axis

**For odd $n$:** One pole at $s = -\omega_C$, remaining poles in conjugate pairs

### Butterworth Polynomials

The denominator polynomials $B_n(s)$ for normalized Butterworth filters ($\omega_C = 1$):

- $B_1(s) = s + 1$
- $B_2(s) = s^2 + \sqrt{2}s + 1$
- $B_3(s) = (s+1)(s^2 + s + 1)$
- $B_4(s) = (s^2 + 0.765s + 1)(s^2 + 1.848s + 1)$
- $B_5(s) = (s+1)(s^2 + 0.618s + 1)(s^2 + 1.618s + 1)$
- $B_6(s) = (s^2 + 0.518s + 1)(s^2 + 1.414s + 1)(s^2 + 1.932s + 1)$

**Frequency scaling:** Replace $s$ with $s/\omega_C$ to denormalize.

### Second-Order Section Parameters

For a quadratic factor $s^2 + as + 1$ from $B_n(s)$:

$$\omega_0 = 1 \text{ (normalized)}$$
$$2\zeta = a$$
$$Q = \frac{1}{a}$$

**After denormalization** ($s \to s/\omega_C$):

$$\omega_0 = \omega_C$$
$$\zeta = \frac{a}{2}$$

---

## Chebyshev Filter Theory

### Type I Chebyshev (Passband Ripple)

**Magnitude-squared function:**

$$|H(j\omega)|^2 = \frac{1}{1 + \epsilon^2 T_n^2(\omega/\omega_C)}$$

where:
- $\epsilon$ = ripple factor
- $T_n(x)$ = Chebyshev polynomial of the first kind, order $n$
- $\omega_C$ = passband edge frequency

**Chebyshev polynomials** (recursive definition):
$$T_0(x) = 1$$
$$T_1(x) = x$$
$$T_{n+1}(x) = 2xT_n(x) - T_{n-1}(x)$$

Explicit forms:
- $T_2(x) = 2x^2 - 1$
- $T_3(x) = 4x^3 - 3x$
- $T_4(x) = 8x^4 - 8x^2 + 1$
- $T_5(x) = 16x^5 - 20x^3 + 5x$

**Alternative form for $|x| > 1$:**
$$T_n(x) = \cosh(n \cosh^{-1}(x))$$

### Ripple Specifications

**Passband ripple in dB:**
$$A_p = 10\log_{10}(1 + \epsilon^2)$$

Common values:
- 0.5 dB ripple: $\epsilon = 0.3493$
- 1 dB ripple: $\epsilon = 0.5088$
- 2 dB ripple: $\epsilon = 0.7648$
- 3 dB ripple: $\epsilon = 0.9976 \approx 1$

**Relationship between ripple factor and passband variation:**

$$\epsilon = \sqrt{10^{A_p/10} - 1}$$

### Passband Magnitude Behavior

**For odd $n$:**
- At DC: $|H(0)| = 1$ (0 dB)
- Ripple between 1 and $1/\sqrt{1+\epsilon^2}$
- For 3 dB ripple ($\epsilon \approx 1$): varies from 1 to $1/\sqrt{2}$ (0 to -3 dB)

**For even $n$:**
- At DC: $|H(0)| = 1/\sqrt{1+\epsilon^2}$
- Ripple between $1/\sqrt{1+\epsilon^2}$ and 1
- For 3 dB ripple: varies from $1/\sqrt{2}$ to 1 (-3 dB to 0 dB)

### Pole Locations

Chebyshev poles lie on an **ellipse** in the s-plane:

$$s_k = -\sinh(\beta)\sin(\theta_k) + j\cosh(\beta)\cos(\theta_k)$$

where:
$$\theta_k = \frac{(2k-1)\pi}{2n}, \quad k = 1,2,...,n$$

$$\beta = \frac{1}{n}\sinh^{-1}\left(\frac{1}{\epsilon}\right)$$

**Semi-axes of the ellipse:**
- Semi-minor axis (real): $a = \omega_C\sinh(\beta)$
- Semi-major axis (imaginary): $b = \omega_C\cosh(\beta)$

---

## Filter Order Determination - Complete Derivations

### Butterworth Order (Lowpass)

Starting from the magnitude specification:

$$\frac{|H(j\omega_{MIN})|}{|H(j\omega_C)|} = \frac{H_{MIN}}{H_{MAX}}$$

Using the Butterworth response:

$$\frac{1/\sqrt{1+(\omega_{MIN}/\omega_C)^{2n}}}{1/\sqrt{2}} = \frac{H_{MIN}}{H_{MAX}}$$

Since $|H(j\omega_C)| = 1/\sqrt{2}$ for Butterworth:

$$\frac{\sqrt{2}}{\sqrt{1+(\omega_{MIN}/\omega_C)^{2n}}} = \frac{H_{MIN}}{H_{MAX}}$$

Squaring and rearranging:

$$1 + \left(\frac{\omega_{MIN}}{\omega_C}\right)^{2n} = 2\left(\frac{H_{MAX}}{H_{MIN}}\right)^2$$

$$\left(\frac{\omega_{MIN}}{\omega_C}\right)^{2n} = 2\left(\frac{H_{MAX}}{H_{MIN}}\right)^2 - 1$$

For small stopband magnitudes, approximating:

$$\left(\frac{\omega_{MIN}}{\omega_C}\right)^{2n} \approx \left(\frac{H_{MAX}}{H_{MIN}}\right)^2 - 1$$

Taking logarithms:

$$2n\log\left(\frac{\omega_{MIN}}{\omega_C}\right) = \log\left[\left(\frac{H_{MAX}}{H_{MIN}}\right)^2 - 1\right]$$

$$n = \frac{\log[(H_{MAX}/H_{MIN})^2 - 1]}{2\log(\omega_{MIN}/\omega_C)}$$

**Round up to nearest integer:**
$$n_B = \left\lceil \frac{\log[(H_{MAX}/H_{MIN})^2 - 1]}{2\log(\omega_{MIN}/\omega_C)} \right\rceil$$

### Chebyshev Order (Lowpass)

Using the Chebyshev magnitude response at $\omega = \omega_{MIN}$:

$$|H(j\omega_{MIN})|^2 = \frac{1}{1 + \epsilon^2 T_n^2(\omega_{MIN}/\omega_C)}$$

The magnitude ratio gives:

$$\left(\frac{H_{MAX}}{H_{MIN}}\right)^2 = 1 + \epsilon^2 T_n^2\left(\frac{\omega_{MIN}}{\omega_C}\right)$$

For $\omega_{MIN}/\omega_C > 1$ (stopband), use:

$$T_n\left(\frac{\omega_{MIN}}{\omega_C}\right) = \cosh\left(n \cosh^{-1}\left(\frac{\omega_{MIN}}{\omega_C}\right)\right)$$

Therefore:

$$\sqrt{\left(\frac{H_{MAX}}{H_{MIN}}\right)^2 - 1} = \epsilon \cosh\left(n \cosh^{-1}\left(\frac{\omega_{MIN}}{\omega_C}\right)\right)$$

For typical 3 dB ripple filters, $\epsilon^2 \approx 1$:

$$\sqrt{\left(\frac{H_{MAX}}{H_{MIN}}\right)^2 - 1} \approx \cosh\left(n \cosh^{-1}\left(\frac{\omega_{MIN}}{\omega_C}\right)\right)$$

Solving for $n$:

$$n = \frac{\cosh^{-1}\left(\sqrt{(H_{MAX}/H_{MIN})^2 - 1}\right)}{\cosh^{-1}(\omega_{MIN}/\omega_C)}$$

**Round up to nearest integer:**
$$n_C = \left\lceil \frac{\cosh^{-1}(\sqrt{(H_{MAX}/H_{MIN})^2 - 1})}{\cosh^{-1}(\omega_{MIN}/\omega_C)} \right\rceil$$

### Highpass Order Formulas

For highpass filters, the frequency ratio is **inverted**:

**Butterworth (Highpass):**
$$n_B = \left\lceil \frac{\log[(H_{MAX}/H_{MIN})^2 - 1]}{2\log(\omega_C/\omega_{MIN})} \right\rceil$$

**Chebyshev (Highpass):**
$$n_C = \left\lceil \frac{\cosh^{-1}(\sqrt{(H_{MAX}/H_{MIN})^2 - 1})}{\cosh^{-1}(\omega_C/\omega_{MIN})} \right\rceil$$

---

## Frequency Transformations

### Lowpass to Highpass Transformation

**s-domain transformation:**
$$s \to \frac{\omega_C^2}{s}$$

This maps:
- Lowpass cutoff $\omega_C$ → Highpass cutoff $\omega_C$
- DC (s=0) → Infinity
- Infinity → DC

**Transfer function transformation:**

If lowpass $H_{LP}(s)$ has order $n$, then highpass:

$$H_{HP}(s) = H_{LP}\left(\frac{\omega_C^2}{s}\right) \cdot \frac{s^n}{\omega_C^n}$$

The factor $s^n/\omega_C^n$ accounts for the order reversal.

### Lowpass to Bandpass Transformation

**s-domain transformation:**
$$s \to \frac{s^2 + \omega_0^2}{Bs}$$

where:
- $\omega_0 = \sqrt{\omega_1\omega_2}$ = center frequency (geometric mean)
- $B = \omega_2 - \omega_1$ = bandwidth

This transforms an $n^{th}$-order lowpass to a $2n^{th}$-order bandpass.

### Lowpass to Band-Stop Transformation

**s-domain transformation:**
$$s \to \frac{Bs}{s^2 + \omega_0^2}$$

This also transforms $n^{th}$-order lowpass to $2n^{th}$-order band-stop.

---

## Practical Design Considerations

### Sensitivity Analysis

**Component sensitivity** measures how variations in component values affect circuit performance:

$$S_x^y = \frac{\partial y/y}{\partial x/x} = \frac{x}{y}\frac{\partial y}{\partial x}$$

**For Sallen-Key circuits:**

$$S_{R_i}^{\omega_0} = S_{C_i}^{\omega_0} = -\frac{1}{2}$$

Meaning a 1% change in R or C causes approximately 0.5% change in $\omega_0$.

$$S_{\mu}^{\zeta} = -\frac{R_1C_2(1-\mu)}{2[R_1C_1 + R_2C_1 + R_1C_2(1-\mu)]}$$

Unity gain designs ($\mu = 1$) have zero sensitivity to gain variations.

### Component Selection Guidelines

1. **Standard capacitor values:** Use E12 or E24 series
2. **Resistor range:** 1 kΩ to 1 MΩ (avoid extremes for noise/offset considerations)
3. **Capacitor range:** 100 pF to 10 μF (practical availability)
4. **Op-amp bandwidth:** Ensure $f_{GBW} \geq 100f_C$ where $f_{GBW}$ is gain-bandwidth product

### Impedance Scaling

To scale impedances by factor $k_Z$:
- All resistances: $R' = k_Z \cdot R$
- All capacitances: $C' = C/k_Z$
- Frequencies remain unchanged

### Frequency Scaling

To scale frequencies by factor $k_F$:
- All resistances: remain unchanged
- All capacitances: $C' = C/k_F$
- All frequencies: $\omega' = k_F \cdot \omega$

---

## Cascade Design Methodology

### Section Ordering

For optimal noise and dynamic range, order sections by **increasing Q**:

1. Lowest Q (most damped) section first
2. Highest Q (least damped) section last

This prevents early stages from clipping due to resonant peaks.

### Inter-stage Loading

**Buffer requirement:** Each Sallen-Key section should be buffered (high input impedance) to prevent loading of previous stages.

**Op-amp as buffer:** The unity-gain follower ($\mu = 1$) naturally provides buffering.

### Overall Gain Distribution

**Option 1:** Implement all gain in first stage
**Option 2:** Distribute gain equally across all stages
**Option 3:** Implement gain in final stage

Trade-offs involve noise, distortion, and signal-to-noise ratio at each stage.

---

## Advanced Topics

### Group Delay

**Definition:**
$$\tau_g(\omega) = -\frac{d\phi(\omega)}{d\omega}$$

where $\phi(\omega)$ is the phase response.

**Physical meaning:** Time delay for signals at frequency $\omega$

**For linear phase:** $\tau_g$ = constant (all frequencies delayed equally)

Butterworth filters have relatively poor group delay characteristics; Bessel filters optimize for flat group delay.

### Phase Response

**Second-order lowpass phase:**
$$\phi(\omega) = -\tan^{-1}\left(\frac{2\zeta\omega/\omega_0}{1-(\omega/\omega_0)^2}\right)$$

At $\omega = \omega_0$: $\phi = -90°$ (independent of $\zeta$)

### Transient Response

**Step response overshoot** for underdamped systems:
$$\text{Overshoot} = e^{-\pi\zeta/\sqrt{1-\zeta^2}} \times 100\%$$

**Settling time** (to within 2%):
$$t_s \approx \frac{4}{\zeta\omega_0}$$

**Rise time** (10% to 90%):
$$t_r \approx \frac{1.8}{\omega_0}$$

---

## Summary of Key Relationships

| Parameter | Relationship | Notes |
|-----------|-------------|-------|
| $Q$ and $\zeta$ | $Q = 1/(2\zeta)$ | Inverse relationship |
| $\omega_r$ and $\omega_0$ | $\omega_r = \omega_0\sqrt{1-2\zeta^2}$ | Resonance requires $\zeta < 1/\sqrt{2}$ |
| Bandwidth | $B = \omega_0/Q = 2\zeta\omega_0$ | 3-dB bandwidth |
| Butterworth cutoff | $\|H(j\omega_C)\| = 1/\sqrt{2}$ | Always -3 dB point |
| Chebyshev cutoff | Passband edge | Not necessarily -3 dB |
| Pole magnitude | $\|s_k\| = \omega_0$ | For normalized filters |
| Asymptotic slope | $-20n$ dB/decade (LP) | $n$ = filter order |
| Asymptotic slope | $+20n$ dB/decade (HP) | $n$ = filter order |

---

## Final Design Checklist

✓ Determine filter type and specifications ($H_{MAX}$, $H_{MIN}$, $\omega_C$, $\omega_{MIN}$)

✓ Calculate minimum order $n$ using appropriate formula

✓ Select polynomial type (Butterworth vs. Chebyshev)

✓ Obtain poles from tables or calculations

✓ Factor transfer function into first and second-order sections

✓ For each second-order section, determine $\omega_0$, $\zeta$, and $Q$

✓ Choose Sallen-Key design method (Equal Elements or Unity Gain)

✓ Calculate component values

✓ Verify practical component ranges

✓ Check op-amp bandwidth requirements

✓ Determine section ordering (by Q)

✓ Implement gain distribution

✓ Verify overall performance via simulation or calculation