# Lecture 15: First/Second-Order Systems and Bode Plots

## 1. First-Order CT Lowpass

**Standard form:** $H(j\omega) = \frac{1}{1 + j\omega/\omega_c}$

| Parameter | Value |
|---|---|
| DC gain | $|H(0)| = 1$ (0 dB) |
| At cutoff $\omega_c$ | $|H| = 1/\sqrt{2}$ ($-3$ dB) |
| Phase at DC | $0°$ |
| Phase at $\omega_c$ | $-45°$ |
| Phase as $\omega \to \infty$ | $-90°$ |
| Time constant | $\tau = 1/\omega_c$ |
| Impulse response | $h(t) = \omega_c e^{-\omega_c t}u(t)$ |

## 2. Bode Plot Conventions
- Magnitude in dB vs log-frequency axis
- Phase in degrees vs log-frequency axis
- Cascaded systems: add magnitudes (dB) and phases

## 3. First-Order Bode Asymptotes

**Magnitude:** 0 dB for $\omega \ll \omega_c$; $-20$ dB/decade for $\omega \gg \omega_c$. Max error 3 dB at corner.

**Phase:** $0°$ below $\omega_c/10$; $-45°$ at $\omega_c$; $-90°$ above $10\omega_c$. Linear transition over 2 decades.

**Building blocks:** Pole → $-20$ dB/dec, $0° \to -90°$. Zero → $+20$ dB/dec, $0° \to +90°$. $(j\omega)^{\pm 1}$ → $\pm 20$ dB/dec through all $\omega$.

## 4. Second-Order CT System

**Standard form:** $H(j\omega) = \frac{\omega_n^2}{(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2}$

**Damping classification:**
- $\zeta < 1$: underdamped (complex poles, oscillatory)
- $\zeta = 1$: critically damped (repeated real poles)
- $\zeta > 1$: overdamped (distinct real poles)

**Key frequency values:**
- DC: $|H(0)| = 1$
- At $\omega_n$: $|H(j\omega_n)| = 1/(2\zeta)$, $\angle H = -90°$ (always)
- Resonance: $\omega_r = \omega_n\sqrt{1-2\zeta^2}$ exists only if $\zeta < 1/\sqrt{2} \approx 0.707$
- Peak: $|H|_{\max} = 1/(2\zeta\sqrt{1-\zeta^2})$

## 5. Step Response (Underdamped)
- %OS $= 100 \cdot e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
- Peak time: $t_p = \pi/\omega_d$, where $\omega_d = \omega_n\sqrt{1-\zeta^2}$
- Settling time (2%): $t_s \approx 4/(\zeta\omega_n)$
- Rise time: $t_r \approx 1.8/\omega_n$

## 6. Second-Order Bode
- Low freq: 0 dB flat
- High freq: $-40$ dB/decade
- Break at $\omega_n$
- Near $\omega_n$: peak of $\approx 20\log_{10}(1/(2\zeta))$ dB above asymptote
- Phase: $0° \to -90°$ at $\omega_n \to -180°$

## 7. DT Systems
- First-order: pole at $z = a$, $|a| < 1$ for stability. $a \to 1$ = narrow bandwidth.
- Second-order: poles at $z = re^{\pm j\theta_0}$. $r$ = damping ($r \to 1$ = less damped), $\theta_0$ = resonance frequency.
