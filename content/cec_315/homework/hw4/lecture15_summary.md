# Lecture 15: First/Second-Order Systems and Bode Plots

## 1. First-Order CT Systems

### Standard Form
$$H(j\omega) = \frac{1}{1 + j\omega/\omega_c}$$

where $\omega_c$ is the **cutoff frequency** (also called corner frequency or -3 dB frequency).

### Key Characteristics

| Parameter | Value |
|---|---|
| DC gain | $|H(j0)| = 1$ (0 dB) |
| At cutoff | $|H(j\omega_c)| = 1/\sqrt{2}$ (-3 dB) |
| Phase at DC | $0°$ |
| Phase at cutoff | $-45°$ |
| Phase at $\omega \to \infty$ | $-90°$ |
| Time constant | $\tau = 1/\omega_c$ |
| Impulse response | $h(t) = \omega_c e^{-\omega_c t} u(t)$ |
| Step response | $y_{\text{step}}(t) = (1 - e^{-\omega_c t})u(t)$ |

### Magnitude and Phase Formulas
$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega/\omega_c)^2}}$$

$$\angle H(j\omega) = -\arctan(\omega/\omega_c)$$

$$|H|_{\text{dB}} = -10\log_{10}(1 + (\omega/\omega_c)^2)$$

## 2. Bode Plots

Bode plots display frequency response on **logarithmic frequency** axis:
- **Magnitude plot**: $|H|_{\text{dB}}$ vs $\log_{10}(\omega)$ (or equivalently vs $\omega$ on log scale)
- **Phase plot**: $\angle H$ (degrees) vs $\log_{10}(\omega)$

### Why Log-Frequency?
- Spans many decades of frequency on one plot
- Cascaded systems: total magnitude (dB) = sum of individual magnitudes (dB)
- Asymptotic behavior becomes straight lines

### First-Order Bode Asymptotes

**Magnitude:**
- For $\omega \ll \omega_c$: $|H|_{\text{dB}} \approx 0$ dB (flat)
- For $\omega \gg \omega_c$: $|H|_{\text{dB}} \approx -20\log_{10}(\omega/\omega_c)$ dB
  - Slope: **-20 dB/decade** (or -6 dB/octave)
- Asymptotes meet at $\omega = \omega_c$ (the corner)
- Maximum error between asymptote and actual: **3 dB** at $\omega_c$

**Phase:**
- For $\omega \ll \omega_c/10$: $\angle H \approx 0°$
- For $\omega = \omega_c$: $\angle H = -45°$
- For $\omega \gg 10\omega_c$: $\angle H \approx -90°$
- Approximate transition: linear from $0°$ to $-90°$ over two decades centered at $\omega_c$

### Bode Plot Building Blocks

| Factor | Magnitude slope | Phase change |
|---|---|---|
| Constant $K$ | Flat at $20\log_{10}K$ | $0°$ (or $\pm 180°$ if $K<0$) |
| $(j\omega)^{\pm 1}$ | $\pm 20$ dB/dec through all $\omega$ | $\pm 90°$ constant |
| $(1 + j\omega/\omega_c)^{-1}$ (pole) | $-20$ dB/dec for $\omega > \omega_c$ | $0° \to -90°$ |
| $(1 + j\omega/\omega_c)^{+1}$ (zero) | $+20$ dB/dec for $\omega > \omega_c$ | $0° \to +90°$ |

**Composite systems:** Plot each factor separately, then add (in dB for magnitude, in degrees for phase).

## 3. Second-Order CT Systems

### Standard Form
$$H(j\omega) = \frac{\omega_n^2}{(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2}$$

Parameters:
- $\omega_n$: **natural frequency** (undamped oscillation frequency)
- $\zeta$: **damping ratio** (controls oscillatory behavior)

### Classification by Damping Ratio

| $\zeta$ range | Classification | Pole type | Behavior |
|---|---|---|---|
| $0 < \zeta < 1$ | **Underdamped** | Complex conjugate | Oscillatory decay |
| $\zeta = 1$ | **Critically damped** | Repeated real | Fastest non-oscillatory decay |
| $\zeta > 1$ | **Overdamped** | Distinct real | Sluggish exponential decay |
| $\zeta = 0$ | **Undamped** | Pure imaginary | Sustained oscillation |

### Poles
$$(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2 = 0$$

Using $s = j\omega$: $s = -\zeta\omega_n \pm \omega_n\sqrt{\zeta^2 - 1}$

For underdamped ($\zeta < 1$): $s = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2} = -\sigma \pm j\omega_d$
- $\sigma = \zeta\omega_n$: decay rate
- $\omega_d = \omega_n\sqrt{1-\zeta^2}$: damped natural frequency

### Key Frequency Response Values

**At DC ($\omega = 0$):**
$$|H(j0)| = 1 \quad (0 \text{ dB})$$

**At natural frequency ($\omega = \omega_n$):**
$$H(j\omega_n) = \frac{\omega_n^2}{-\omega_n^2 + j2\zeta\omega_n^2 + \omega_n^2} = \frac{1}{j2\zeta}$$

$$|H(j\omega_n)| = \frac{1}{2\zeta}, \quad \angle H(j\omega_n) = -90°$$

**Resonance frequency** (where magnitude peaks):
$$\omega_r = \omega_n\sqrt{1 - 2\zeta^2} \quad \text{(exists only if } \zeta < 1/\sqrt{2} \approx 0.707\text{)}$$

**Peak magnitude:**
$$|H(j\omega_r)| = \frac{1}{2\zeta\sqrt{1-\zeta^2}}$$

### Second-Order Bode Asymptotes

**Magnitude:**
- For $\omega \ll \omega_n$: $|H|_{\text{dB}} \approx 0$ dB (flat)
- For $\omega \gg \omega_n$: slope = **-40 dB/decade** (-12 dB/octave)
- Near $\omega_n$: resonance peak if $\zeta < 1/\sqrt{2}$
- Lower $\zeta$ → sharper, taller peak

**Phase:**
- $\omega \ll \omega_n$: $\angle H \approx 0°$
- $\omega = \omega_n$: $\angle H = -90°$ (always, regardless of $\zeta$)
- $\omega \gg \omega_n$: $\angle H \to -180°$
- Lower $\zeta$ → sharper phase transition around $\omega_n$

## 4. Step Response Specifications (Second-Order)

For underdamped systems ($\zeta < 1$), the step response exhibits overshoot and oscillation:

- **Percent Overshoot (%OS):**
$$\%OS = 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$

- **Peak Time** (time to first peak):
$$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}$$

- **Settling Time** (to within 2% of final value):
$$t_s \approx \frac{4}{\zeta\omega_n}$$

- **Rise Time** (0% to 100%, approximate):
$$t_r \approx \frac{1.8}{\omega_n}$$

**Design trade-off:** Decreasing $\zeta$ gives faster rise time but more overshoot. Increasing $\zeta$ reduces overshoot but slows response.

## 5. DT First-Order Systems

### Standard Form
$$H(e^{j\omega}) = \frac{1}{1 - ae^{-j\omega}}, \quad |a| < 1$$

- Pole at $z = a$ in the z-plane
- $|a|$ close to 1 → narrow bandwidth (sharp filter)
- $|a|$ close to 0 → wide bandwidth

### DT Second-Order Systems
$$H(e^{j\omega}) = \frac{1}{1 - 2r\cos(\theta_0)e^{-j\omega} + r^2 e^{-j2\omega}}$$

- Poles at $z = re^{\pm j\theta_0}$
- $r$: pole radius (stability requires $r < 1$)
- $\theta_0$: pole angle (determines resonance location in $[0, \pi]$)
- Closer to unit circle ($r \to 1$) → sharper resonance peak

## 6. Integrative Examples from Lecture

### Auto Suspension Model
Second-order system where:
- Road bumps are the input
- Car body displacement is the output
- $\zeta$ controls ride quality vs handling trade-off

### FIR Filter Design
Finite-length DT systems with exactly linear phase:
- Symmetric coefficients guarantee linear phase
- Example: $h[n] = \{1, 2, 3, 2, 1\}/9$ — a simple lowpass FIR

### Full CT Pipeline Example
Given differential equation → find $H(j\omega)$ → find poles → PFE → inverse FT:
- Replace $d^n/dt^n$ with $(j\omega)^n$
- Factor denominator
- Partial fractions
- Each term maps to exponential in time domain

### Repeated Poles in PFE
If $H(j\omega) = \frac{A}{(j\omega + a)^2}$, the inverse is:
$$h(t) = At e^{-at}u(t)$$

General rule: repeated pole of order $m$ gives $t^{m-1}e^{-at}u(t)$ (times coefficient).
