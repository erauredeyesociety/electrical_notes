# Midterm 3 / Final — Fall 2024 (DRAFT) Practice — Walkthrough

Cumulative final spanning **all modules** (M12, M14–M20, M33–M36). Score scales to **230/271** total points; default is 10 pts/question unless otherwise marked. **Q1–Q10 are formula-knowledge** (write the equation; ≈2 pts each); **Q11–Q33 are calculation** (mostly 10 pts, two are 20 pts).

- Source PDF: [`../../midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf`](../../midterm_03/test_finalexam_DRAFT_ps160_2024_fall.pdf)
- Answer key: [`../../midterm_03/test_final_ps160_2024_fall_answers.pdf`](../../midterm_03/test_final_ps160_2024_fall_answers.pdf) (Q11–Q33; Q1–Q10 carry no listed answers)
- Companion midterm: [Midterm 3 / Final v1 walkthrough](midterm3_final_v1_solutions.md)
- Module folder: [`../../midterm_03/`](../../midterm_03/)

> ✓ = matches stated answer key. Q1–Q10 are "free points" — verbatim formula recall from the equation sheet / lectures.

---

## Equation bank (from official equation sheet, pages 2–3)

**Fluids (M12).** $\rho = m/V$, $p = F_\perp/A$, $dp/dy = -\rho g$, $p(y) = p_0 - \rho g y$, $\rho A v = \mathcal{C}$, $p + \rho g y + \tfrac12\rho v^2 = \mathcal{C}'$.

**SHM (M14).** $\ddot x + \omega^2 x = 0$, $x(t)=A\cos(\omega t+\phi)$, $\omega=\sqrt{k/m}$, $\omega=\sqrt{g/\ell}$ (simple pendulum), $\omega=\sqrt{mgd/I}$ (physical pendulum).

**Wave kinematics (M15).** $f=1/T=\omega/(2\pi)$, $\omega=2\pi f$, $T=1/f=2\pi/\omega$, $y(x,t)=A\cos(kx-\omega t)$, $k=2\pi/\lambda$, $v=\lambda f=\omega/k$.

**Wave speeds.** $v=\sqrt{F/\mu}$ (string), $v=\sqrt{Y/\rho}$ (solid rod), $v=\sqrt{B/\rho}$ (fluid/gas).

**Standing waves & power.** $f_n = nv/(2L)$ or $nv/(4L)$; $\lambda_n=2L/n$ or $4L/n$; $P_{av}=\tfrac12\sqrt{\mu F}\,\omega^2 A^2$.

**Sound (M16).** $I=\tfrac12\sqrt{\rho B}\,\omega^2 A^2 = p_{\max}^2/(2\sqrt{\rho B})$, $p_{\max}=BkA$, $I=P/(4\pi r^2)$, $\beta=(10\,\text{dB})\log_{10}(I/I_0)$, $I_0=10^{-12}\,\text{W/m}^2$. Doppler: $f_L=f_S(v+v_L)/(v+v_S)$. Beats: $f_{\text{beat}}=|f_a-f_b|$.

**Thermal expansion (M17).** $\Delta L=\alpha L_0 \Delta T$, $\Delta V=\beta V_0\Delta T$, $\beta=3\alpha$.

**Heat (M17).** $Q=mc\Delta T = nC\Delta T$, $Q=\pm m L$ (latent), $C_V=(f/2)R$, $C_P=C_V+R$, $\gamma=C_P/C_V$, $C_V=3R$ (solid). Conduction $H=kA\Delta T/L$; radiation $H=A\sigma T^4$.

**Ideal gas / kinetic theory (M18).** $pV=NkT=nRT$, $kN_A=R$, $\tfrac12 m\langle v^2\rangle = \tfrac32 kT$, $v_{\text{rms}}=\sqrt{\langle v^2\rangle}$, Maxwell-Boltzmann $f(v)\propto v^2 e^{-mv^2/2kT}$.

**Thermo first law / processes (M19).** $T_A=T_B=T_C$ (zeroth law), $dU=dQ-dW$, $W=\int p\,dV$. For a cycle $W=Q=Q_H+Q_C$.

**Entropy & engines (M20).** $\Delta S \ge 0$, $\Delta S=\int dQ/T$, $S=k\ln w$, $e=W/Q_H$, $K=Q_C/(-W)$ (refrig), $K=-Q_H/(-W)$ (heat pump), Carnot: $Q_H/T_H + Q_C/T_C = 0$.

> The optics/wave-optics formulas (M33–M36) needed for Q1–Q10 and Q28–Q33 are **not on the printed equation sheet** — these are the Knowledge Questions, so you must memorize them.

---

# Knowledge Questions (Q1–Q10) — formulas only

## Q1 — Reflection & Snell's Law [2 pts] (M33)

- **Law of reflection:** $\theta_i = \theta_r$ (both from normal, in plane of incidence).
- **Snell's law:** $n_1 \sin\theta_1 = n_2\sin\theta_2$.

## Q2 — Index of refraction & wavelength in a medium [2 pts] (M33)

- $n = c/v$
- $\lambda_{\text{med}} = \lambda_{\text{vac}}/n$ (frequency unchanged)

## Q3 — Critical angle (TIR) and Brewster's angle [2 pts] (M33)

- **Critical:** $\sin\theta_c = n_2/n_1$ (with $n_1>n_2$).
- **Brewster (fully polarized reflection):** $\tan\theta_B = n_2/n_1$.

## Q4 — Thin lens / mirror equation & lateral magnification [3 pts] (M34)

- $\dfrac{1}{s} + \dfrac{1}{s'} = \dfrac{1}{f}$
- $m = -\dfrac{s'}{s} = \dfrac{y'}{y}$

## Q5 — Lensmaker's equation & paraxial approximation [2 pts] (M34)

- $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$
- Small angle: $\sin\theta\approx\tan\theta\approx\theta$, $\cos\theta\approx 1$ (radians).

## Q6 — Malus's law & angular magnification of a magnifier [2 pts] (M34)

- **Malus:** $I = I_0 \cos^2\theta$.
- **Magnifier:** $M = 25\,\text{cm}/f$ (image at infinity); $M = 1 + 25\,\text{cm}/f$ (image at near point).

## Q7 — Phase difference between two rays [3 pts] (M35)

$$\phi = \dfrac{2\pi}{\lambda}\,\Delta r = k\,\Delta r$$

where $\Delta r$ is the path-length difference.

## Q8 — Constructive interference: double slit & grating [2 pts] (M35/M36)

Both share the same condition (the grating just makes maxima narrower):

$$d\sin\theta = m\lambda, \quad m = 0, \pm 1, \pm 2, \ldots$$

## Q9 — Two-source intensity [1 pt] (M35)

$$I = I_0 \cos^2\!\left(\dfrac{\phi}{2}\right) = I_0\cos^2\!\left(\dfrac{\pi d \sin\theta}{\lambda}\right)$$

## Q10 — Thin-film path difference & Rayleigh criterion [2 pts] (M35/M36)

- **Thin film** (path-length difference inside film): $\Delta = 2nt$ (normal incidence; add $\lambda/2$ for each hard reflection).
- **Rayleigh (circular aperture):** $\sin\theta_1 \approx \theta_1 = 1.22\,\lambda/D$.

---

# Calculation Questions (Q11–Q33)

## Q11 — Ice slab supports a woman (buoyancy, minimum-volume twist)

**Setup.** A 45.0-kg woman stands on a freshwater ice slab ($\rho_{\text{ice}}=0.92\,\rho_w = 920$ kg/m³). At the *minimum* volume the slab is just barely fully submerged (top surface flush with water) so her feet stay dry. Buoyancy = weight of displaced water = full-volume's worth of water.

$$\rho_w V g = (m_w + \rho_{\text{ice}} V)\,g \;\Rightarrow\; V = \dfrac{m_w}{\rho_w - \rho_{\text{ice}}}$$

$$V_{\min} = \dfrac{45.0}{1000 - 920} = \dfrac{45.0}{80} = \boxed{0.5625\ \text{m}^3}\ \checkmark$$

> Mass of that ice slab: $m_{\text{ice}}=920\cdot 0.5625 = 517.5$ kg. The answer key parenthetical "(157.5 kg)" appears to be a typo for 517.5 kg.

## Q12 — Bernoulli, narrowing horizontal pipe

**Setup.** Continuity gives the new speed; Bernoulli (no height change) gives the new pressure.

$$v_2 = v_1 (r_1/r_2)^2 = 3.3\,(0.23/0.12)^2 = 3.3\,(3.6736) = 12.123\ \text{m/s}$$

$$p_2 = p_1 + \tfrac12\rho(v_1^2 - v_2^2) = 233000 + 500(10.89 - 146.96) = 233000 - 68035 = \boxed{164.96\ \text{kPa}}\ \checkmark$$

## Q13 — Simple pendulum period on another planet

$$T = 2\pi\sqrt{\ell/g} = 2\pi\sqrt{0.67/5.9} = 2\pi(0.3370) = \boxed{2.117\ \text{s}}\ \checkmark$$

## Q14 — SHM block: mass from $v_{\max}$

**Setup.** $v_{\max}=\omega A = A\sqrt{k/m}$, so $m = kA^2/v_{\max}^2$.

$$m = \dfrac{776\,(1.55)^2}{(12.1)^2} = \dfrac{1864.34}{146.41} = \boxed{12.73\ \text{kg}}\ \checkmark$$

## Q15 — Wave function $y(x,t) = 5\cos(3t + 0.5x - 2.1)$ [20 pts]

Read off the standard form $A\cos(\omega t + kx + \phi)$:

- **(a)** $A = \boxed{5\ \text{m}}\ \checkmark$
- **(b)** $\omega = \boxed{3\ \text{rad/s}}\ \checkmark$
- **(c)** $k = \boxed{0.5\ \text{rad/m}}\ \checkmark$
- **(d)** $\phi = \boxed{-2.1\ \text{rad}}\ \checkmark$
- **(e)** $f = \omega/(2\pi) = 3/6.2832 = \boxed{0.4775\ \text{Hz}}\ \checkmark$
- **(f)** $T = 1/f = \boxed{2.094\ \text{s}}\ \checkmark$
- **(g)** $\lambda = 2\pi/k = \boxed{12.57\ \text{m}}\ \checkmark$
- **(h)** $v = \omega/k = 3/0.5 = \boxed{6\ \text{m/s}}\ \checkmark$
- **(i)** $v_y(0,0) = \partial y/\partial t\big|_{0,0} = -A\omega\sin(\phi) = -5(3)\sin(-2.1) = -15(-0.8632) = \boxed{12.95\ \text{m/s}}\ \checkmark$
- **(j)** Maximum transverse speed $= \omega A = 3\cdot 5 = \boxed{15\ \text{m/s}}\ \checkmark$ *(new in fall 2024 — not on ME15)*

## Q16 — Sound intensity vs. distance

**Setup.** Drop in dB from $r_1$ to $r_2$ in free space: $\Delta\beta = -20\log_{10}(r_2/r_1)$ (since $I\propto 1/r^2$).

$$\beta_2 = 122 - 20\log_{10}(56/11) = 122 - 20\log_{10}(5.0909) = 122 - 20(0.7066) = \boxed{107.87\ \text{dB}}\ \checkmark$$

## Q17 — Doppler, source approaching stationary listener

$$f_L = f_S \dfrac{v}{v - v_S} = 670\cdot\dfrac{342}{342-32} = 670\cdot\dfrac{342}{310} = \boxed{739\ \text{Hz}}\ \checkmark$$

## Q18 — Open-open pipe, $n=2$ harmonic

$$f_n = \dfrac{nv}{2L} \;\Rightarrow\; f_2 = \dfrac{2(331)}{2(0.5)} = \boxed{662\ \text{Hz}}\ \checkmark$$

## Q19 — Linear thermal expansion

$$\Delta L = \alpha L_0 \Delta T = (3.7\times 10^{-5})(4.6)(31-(-4)) = (3.7\times 10^{-5})(4.6)(35) = 5.957\times 10^{-3}\ \text{m} = \boxed{5.96\ \text{mm}}\ \checkmark$$

## Q20 — Latent heat of fusion from $Q$ (inverse melt problem)

**Setup.** All heat goes into the phase change (constant $T$): $Q = mL_f$, solve for $L_f$. *New twist: solving for $L_f$ instead of $Q$.*

$$L_f = \dfrac{Q}{m} = \dfrac{10^6}{5.2} = 192{,}308\ \text{J/kg} = \boxed{192\ \text{kJ/kg}}\ \checkmark$$

## Q21 — Total translational KE of an ideal gas

$$K_{\text{tr}} = \dfrac{3}{2}nRT = 1.5(10.1)(8.314)(300.15) = \boxed{37.79\ \text{kJ}}\ \checkmark$$

## Q22 — Combined gas law (T up, V halved)

$$p_2 = p_1 \dfrac{V_1}{V_2}\dfrac{T_2}{T_1} = 89\cdot 2 \cdot\dfrac{723.15}{493.15} = 178\,(1.4664) = \boxed{261\ \text{kPa}}\ \checkmark$$

## Q23 — New $v_{\text{rms}}$ after isochoric heat addition (kinetic theory + 1st law)

**Setup.** Heat at constant V goes entirely into $\Delta U = (3/2)nR\Delta T$ for a monatomic gas. Initial $T$ from given $v_{\text{rms}}$, then add $\Delta T$, then recompute $v_{\text{rms}}$. *New combination: kinetic-theory $v_{\text{rms}}$ tied to a heat-input gas-law problem.*

$$v_{\text{rms}}^2 = \dfrac{3RT}{M} \;\Rightarrow\; T_1 = \dfrac{Mv_1^2}{3R} = \dfrac{(4\times 10^{-3})(900)^2}{3(8.314)} = 129.93\ \text{K}$$

$$\Delta T = \dfrac{2Q}{3nR} = \dfrac{2(2400)}{3(3)(8.314)} = 64.15\ \text{K} \;\Rightarrow\; T_2 = 194.08\ \text{K}$$

$$v_{\text{rms},2} = \sqrt{\dfrac{3(8.314)(194.08)}{4\times 10^{-3}}} = \sqrt{1.2098\times 10^6} = \boxed{1100\ \text{m/s}}\ \checkmark$$

## Q24 — Isothermal expansion, $Q = W$

For an isothermal ideal-gas process, $\Delta U = 0$ so $Q = W = nRT\ln(V_2/V_1) = p_1V_1\ln(V_2/V_1)$.

$$Q = (152{,}000)(0.7)\ln(3.3/0.7) = 106{,}400\,\ln(4.714) = 106{,}400\,(1.5506) = \boxed{165\ \text{kJ}}\ \checkmark$$

(Sign positive: heat absorbed by the gas as it expands.)

## Q25 — Adiabatic expansion of monatomic gas

$\gamma = 5/3$.

$$p_2 = p_1\left(\dfrac{V_1}{V_2}\right)^\gamma = 281\,(0.7/2.5)^{5/3} = 281\,(0.28)^{1.6667} = 281\,(0.1199) = \boxed{33.7\ \text{kPa}}\ \checkmark$$

## Q26 — Engine $Q_C$ from efficiency and $W$

$$Q_H = W/e = 1400/0.16 = 8750\ \text{J}; \quad Q_C = W - Q_H = 1400 - 8750 = \boxed{Q_C = -7350\ \text{J}}\ \checkmark$$

(Negative: exhausted from system to cold reservoir.)

## Q27 — Entropy change when water freezes

**Setup.** Freezing releases heat ($Q<0$) at constant $T=273.15$ K.

$$\Delta S = \dfrac{Q}{T} = \dfrac{-mL_f}{T} = \dfrac{-(11)(3.35\times 10^5)}{273.15} = \dfrac{-3.685\times 10^6}{273.15} = \boxed{-13.5\ \text{kJ/K}}\ \checkmark$$

## Q28 — Two-mirror corner geometry

**Setup.** Two flat mirrors meet at a corner; the figure shows $\phi=70°$ between the slanted mirror and the vertical dashed normal of the bottom (ground) mirror, with incidence angle $\theta=50°$ at the first mirror. Want $\alpha$ between the outgoing ray and the second mirror's normal.

**Geometric interpretation.** Treat the problem as a triangle whose vertices are (i) the corner, (ii) the first mirror's hit point, (iii) the second mirror's hit point. Interior angle at corner = $180°-\phi=110°$ (the wedge between the two mirror surfaces). Interior angle at first hit = $90°-\theta=40°$. Interior angle at second hit = $90°-\alpha$. Sum $=180°$:

$$110° + 40° + (90°-\alpha) = 180° \;\Rightarrow\; \alpha = \boxed{60°}\ \checkmark$$

## Q29 — Snell's law: find incidence angle

$$\sin\theta_1 = n_2\sin\theta_2 = 1.6\sin(20°) = 1.6(0.3420) = 0.5472$$
$$\theta_1 = \arcsin(0.5472) = \boxed{33.2°}\ \checkmark$$

## Q30 — Concave mirror, $s=18$ cm, $R=16$ cm [20 pts]

$f = R/2 = 8$ cm.

- **(a)** $\dfrac{1}{s'} = \dfrac{1}{f} - \dfrac{1}{s} = \dfrac{1}{8} - \dfrac{1}{18} = \dfrac{18-8}{144} = \dfrac{10}{144}$ ⇒ $s' = \boxed{14.4\ \text{cm}}\ \checkmark$
- **(b)** $m = -s'/s = -14.4/18 = \boxed{-0.8}\ \checkmark$
- **(c)** $s'>0$ ⇒ image is **real** ✓
- **(d)** $m<0$ ⇒ image is **inverted** ✓

## Q31 — Thin-film bubble, minimum thickness for enhancement

**Setup.** Air–film–air (a "bubble"): one phase reversal occurs (top air→soap, $n_2>n_1$), none at the bottom (soap→air, $n$ decreases). With one $\lambda/2$ flip, **constructive** (enhancement) requires:

$$2nt = \left(m + \tfrac12\right)\lambda, \quad m=0,1,2,\ldots$$

Minimum thickness ($m=0$):

$$t_{\min} = \dfrac{\lambda}{4n} = \dfrac{471}{4(1.5)} = \boxed{78.5\ \text{nm}}\ \checkmark$$

## Q32 — Double-slit central maximum width

**Setup.** "Full width of central maximum" = distance between the two first-order minima. For double-slit, first minima at $d\sin\theta = \tfrac{\lambda}{2}$, so $y_1 = L\lambda/(2d)$ on each side, giving full width $\Delta y = L\lambda/d$.

$$\Delta y = \dfrac{L\lambda}{d} = \dfrac{(2.1)(418\times 10^{-9})}{0.26\times 10^{-3}} = 3.376\times 10^{-3}\ \text{m} = \boxed{3.376\ \text{mm}}\ \checkmark$$

## Q33 — Rayleigh resolution: smallest crater a Mars-orbiting telescope can see

**Setup.** Rayleigh criterion gives the minimum resolvable angular separation; multiplying by orbital altitude gives the minimum linear separation on the planet's surface. *Application of Rayleigh to a real-world space-telescope problem.*

$$\theta_{\min} = 1.22\,\lambda/D = 1.22(557\times 10^{-9})/(0.045) = 1.510\times 10^{-5}\ \text{rad}$$

$$d_{\min} = \theta_{\min}\cdot L = (1.510\times 10^{-5})(883{,}000) = \boxed{13.33\ \text{m}}\ \checkmark$$

---

## Summary

All 23 numeric answers (Q11–Q33, including all 10 sub-parts of Q15 and all 4 sub-parts of Q30) match the official key. Only flag: Q11's answer-key parenthetical "(157.5 kg)" appears to be a typo — the correct ice-slab mass at $V_{\min}=0.5625$ m³ is $\rho_{\text{ice}}V = 517.5$ kg.
