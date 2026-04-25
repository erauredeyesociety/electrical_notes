# Official Equation Sheet Audit: On-the-Sheet vs. Must-Memorize

**Source:** `test_finalexam_DRAFT_ps160_2024_fall.pdf` pages 2--3, titled
*"Formulas from Midterm 1 and Midterm 2."*

The official sheet covers **only** Midterm 1 and Midterm 2 material (Modules
12, 14--16 on page 2; Modules 17--20 on page 3). **Nothing from Modules
33--36 is on the sheet.** Every formula needed for EM waves, geometric
optics, interference, and diffraction must be memorized or derived.

---

## Part A --- What IS on the Official Sheet

### Page 2 (Midterm 1 material)

**Fluids (M12)**
- $\rho = m/V$
- $p = F_\perp/A$
- $dp/dy = -\rho g$, $p(y) = p_0 - \rho g y$
- $\rho A v = \mathcal C$ (continuity)
- $p + \rho g y + \tfrac{1}{2}\rho v^2 = \mathcal C'$ (Bernoulli)

**Oscillations (M14)**
- $d^2x/dt^2 + \omega^2 x = 0$
- $x(t) = A\cos(\omega t + \phi)$
- $\omega = \sqrt{k/m}$ (spring), $\omega = \sqrt{g/\ell}$ (simple pendulum), $\omega = \sqrt{mgd/I}$ (physical pendulum)
- $f = 1/T = \omega/(2\pi)$, $\omega = 2\pi f = 2\pi/T$, $T = 1/f = 2\pi/\omega$

**Waves (M15)**
- $y(x,t) = A\cos(kx - \omega t)$
- $k = 2\pi/\lambda$
- $v = \lambda f = \omega/k$
- $v = \sqrt{F/\mu}$ (string), $v = \sqrt{Y/\rho}$ (solid), $v = \sqrt{B/\rho}$ (fluid)
- $f_n = nv/(2L)$ or $nv/(4L)$
- $\lambda_n = 2L/n$ or $4L/n$
- $P_{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2$

**Sound (M16)**
- $I = \tfrac{1}{2}\sqrt{\rho B}\,\omega^2 A^2 = p_{\max}^2/(2\sqrt{\rho B})$
- $p_{\max} = BkA$
- $I = P/(4\pi r^2)$
- $\beta = (10\;\text{dB})\log_{10}(I/I_0)$, $I_0 = 10^{-12}\;\text{W/m}^2$
- $f_L = f_S(v + v_L)/(v + v_S)$ (Doppler)
- $f_{\text{beat}} = f_a - f_b$

### Page 3 (Midterm 2 material)

**Temperature & Heat (M17)**
- $\Delta L = \alpha L_0 \Delta T$
- $\Delta V = \beta V_0 \Delta T$, $\beta = 3\alpha$
- $Q = mc\Delta T = nC\Delta T$
- $Q = \pm mL$
- $H = kA\,\Delta T/L$ (conduction)
- $H = A\sigma T^4$ (radiation; **note:** sheet has no emissivity $e$ factor --- you must remember $H = e A\sigma T^4$ if a problem mentions emissivity)

**Kinetic Theory (M18)**
- $C_V = (f/2)R$, $C_P = C_V + R$, $\gamma = C_P/C_V$, $C_V = 3R$ (solid)
- $pV = NkT$, $pV = nRT$, $kN_A = R$
- $\tfrac{1}{2}m\langle v^2\rangle = \tfrac{3}{2}kT$
- $v_{rms} = \sqrt{\langle v^2\rangle}$
- $f(v) \propto v^2 e^{-mv^2/(2kT)}$

**First Law (M19)**
- $T_A = T_B = T_C$ (zeroth law)
- $dU = dQ - dW$
- $W = Q = Q_H + Q_C$ (for a cycle)
- $W = \int p\,dV$

**Second Law and Entropy (M20)**
- $\Delta S \ge 0$
- $\Delta S = \int dQ/T$
- $S = k\ln w$
- $e = W/Q_H$
- $K = Q_C/(-W)$ (refrigerator)
- $K = -Q_H/(-W)$ (heat pump in heating mode)
- $\Delta S = Q_H/T_H + Q_C/T_C = 0$ (Carnot)

---

## Part B --- What is NOT on the Sheet (Must Memorize / Derive)

### Midterm 1 territory

| Formula | Why you need it |
|---|---|
| $v(T) = (331\;\text{m/s})\sqrt{T/(273\;\text{K})}$ | Used in Doppler/beat problems where $T$ varies. Derivable from $v=\sqrt{\gamma RT/M}$ (also not on sheet). |
| Damped: $\omega' = \sqrt{k/m - b^2/(4m^2)}$ | If a damped problem appears. |
| Driven amplitude $A_d = F_0/\sqrt{(k - m\omega_d^2)^2 + b^2\omega_d^2}$ | Resonance problems. |
| SHM energy $E = \tfrac{1}{2}kA^2 = \tfrac{1}{2}m\omega^2 A^2$ | Constantly used; derivable but worth memorizing. |
| Wave equation $\partial_t^2 y = v^2 \partial_x^2 y$ | Conceptual problems. |

### Midterm 2 territory

| Formula | Why you need it |
|---|---|
| Temperature conversions: $T_K = T_C + 273.15$, $T_F = \tfrac{9}{5}T_C + 32$ | Used constantly. **Memorize.** |
| Thermal stress: $F/A = -Y\alpha\Delta T$ | Fixed-end expansion problems. |
| Total translational KE: $K_{\text{tr,tot}} = \tfrac{3}{2}nRT$ | Quick "find $T$ from $K$" --- derivable from equipartition. |
| Adiabatic: $pV^\gamma = \text{const}$, $TV^{\gamma-1} = \text{const}$ | The sheet gives $W=\int p\,dV$ but not the closed form $W = (p_1V_1 - p_2V_2)/(\gamma - 1)$. **Memorize.** |
| Isothermal $W = nRT\ln(V_2/V_1)$ | Derive from $W = \int p\,dV$ with $pV = nRT$. |
| Carnot efficiency $e_{\text{Carnot}} = 1 - T_C/T_H$ | Sheet has $\Delta S = Q_H/T_H + Q_C/T_C = 0$ and $e = W/Q_H$ --- combine to get Carnot $e$. |
| Useful entropy formulas: $\Delta S_{\text{isoT,gas}} = nR\ln(V_2/V_1)$, $\Delta S_{\text{heat}} = mc\ln(T_2/T_1)$, $\Delta S_{\text{phase}} = \pm mL/T$ | Derivable from $\Delta S = \int dQ/T$ but worth memorizing. |
| Stefan--Boltzmann emissivity factor: $H = e A\sigma T^4$ | Sheet writes $H = A\sigma T^4$ (no $e$). |

### Midterm 3 territory --- ALL of it

**Nothing from Modules 33--36 is on the sheet.** Memorize:

**EM Waves (M33)**
- $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 3.00\times 10^8$ m/s
- $E/B = c$
- $u = \varepsilon_0 E^2 = B^2/\mu_0$ (energy density)
- $\vec S = (1/\mu_0)\vec E\times\vec B$ (Poynting)
- $I = \tfrac{1}{2}c\varepsilon_0 E_{\max}^2 = E_{\max}^2/(2\mu_0 c)$
- $p_{\text{abs}} = I/c$, $p_{\text{refl}} = 2I/c$ (radiation pressure)
- Malus: $I = I_{\max}\cos^2\phi$; unpolarized $\to I_0/2$
- Brewster: $\tan\theta_B = n_2/n_1$
- (Maxwell's equations themselves are conceptual; the four integral forms are not on the sheet either.)

**Geometric Optics (M34)**
- $n = c/v$
- $\lambda_{\text{med}} = \lambda_0/n$
- Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$
- TIR: $\sin\theta_c = n_2/n_1$ (with $n_1 > n_2$)
- $\theta_i = \theta_r$ (reflection)
- Mirror/thin lens: $1/s + 1/s' = 1/f$
- $f_{\text{mirror}} = R/2$
- Magnification $m = -s'/s$
- Lensmaker: $1/f = (n-1)(1/R_1 - 1/R_2)$
- Single refracting surface: $n_1/s + n_2/s' = (n_2 - n_1)/R$
- Sign conventions (memorize)
- Two-lens: $s_2 = d - s_1'$, $m = m_1 m_2$
- Magnifier: $M = (25\;\text{cm})/f$
- Telescope: $M = -f_{\text{obj}}/f_{\text{eye}}$
- Lens power: $P[\text{diopter}] = 1/f[\text{m}]$
- Apparent depth: $d_{\text{app}} = d_{\text{real}}(n_{\text{obs}}/n_{\text{med}})$
- Vision: myopia $\to$ diverging, hyperopia $\to$ converging

**Interference (M35)**
- $\Delta\phi = (2\pi/\lambda)\Delta r$
- Bright: $\Delta r = m\lambda$; Dark: $\Delta r = (m+\tfrac{1}{2})\lambda$
- Young: $d\sin\theta = m\lambda$, $y_m = m\lambda R/d$
- Two-source intensity $I = I_0\cos^2(\pi d\sin\theta/\lambda)$
- Thin film: $2nt = m\lambda_0$ or $(m+\tfrac{1}{2})\lambda_0$ (depends on hard reflections)
- Michelson: $2\Delta d = \Delta m\,\lambda$
- Central max width (double slit): $w = 2\lambda R/d$

**Diffraction (M36)**
- Single-slit minima: $a\sin\theta = m\lambda$ ($m \ne 0$)
- Single-slit intensity: $I = I_0[\sin(\beta/2)/(\beta/2)]^2$, $\beta = 2\pi a\sin\theta/\lambda$
- Combined double-slit: $I = I_0\cos^2(\pi d\sin\theta/\lambda)\cdot[\sin(\beta/2)/(\beta/2)]^2$
- Grating maxima: $d\sin\theta = m\lambda$
- Resolving power: $R = \lambda/\Delta\lambda = Nm$
- Bragg: $2d\sin\theta = m\lambda$ ($\theta$ from the planes)
- Rayleigh: $\sin\theta_R = 1.22\lambda/D$
- Central max width (single slit): $w = 2\lambda R/a$
- Visible grating orders: $m_{\max} = \lfloor d/\lambda \rfloor$

---

## Part C --- Triage Summary

**Highest-priority memorize list (small, dense, frequently used):**
1. Snell $n_1\sin\theta_1 = n_2\sin\theta_2$
2. Index $n = c/v$, $\lambda_{\text{med}} = \lambda_0/n$
3. TIR $\sin\theta_c = n_2/n_1$
4. Brewster $\tan\theta_B = n_2/n_1$
5. Malus $I = I_{\max}\cos^2\phi$
6. Thin lens / mirror $1/s + 1/s' = 1/f$, $m = -s'/s$
7. Lensmaker $1/f = (n-1)(1/R_1 - 1/R_2)$
8. Young/grating $d\sin\theta = m\lambda$ (bright)
9. Single-slit minima $a\sin\theta = m\lambda$
10. Bragg $2d\sin\theta = m\lambda$
11. Rayleigh $\sin\theta_R = 1.22\lambda/D$
12. Thin-film $2nt$ rule
13. $I = E_{\max}^2/(2\mu_0 c) = \tfrac{1}{2}c\varepsilon_0 E_{\max}^2$, $p_{\text{abs}} = I/c$
14. Carnot $e = 1 - T_C/T_H$
15. Adiabatic $pV^\gamma = \text{const}$
16. Temperature conversion to Kelvin

Everything in Part A above is provided --- don't waste study time memorizing it,
just be sure you know how to read and apply it.
