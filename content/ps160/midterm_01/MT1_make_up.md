# PS 160 — Test #1 (Make-up) — Fall 2024

**Instructor:** Oussama Mhibik
**Date:** Thursday, 10 October 2024
**Scope:** Fluids, Oscillations, Waves, Sound (Modules 12, 14, 15, 16)
**Total:** 150 points

---

## Knowledge questions [30 points]

### Fluids

1. **[2 pts]** Write the definitions of density and pressure.
   - $\rho = m/V$
   - $p = F_\perp/A$

2. **[2 pts]** Write the hydrostatic condition and its solution for constant density.
   - $dp/dy = -\rho g$
   - $p(y) = p_0 - \rho g y$

3. **[2 pts]** Write the continuity equation and Bernoulli's equation.
   - Continuity: $\rho A v = \text{const}$ (incompressible: $A_1 v_1 = A_2 v_2$)
   - Bernoulli: $p + \rho g y + \tfrac{1}{2}\rho v^2 = \text{const}$

### Oscillations

4. **[2 pts]** Write the differential equation for SHM and its solution.
   - $\ddot x + \omega^2 x = 0$
   - $x(t) = A\cos(\omega t + \varphi)$

5. **[3 pts]** Angular frequency for spring-mass, simple pendulum, physical pendulum.
   - $\omega_\text{spring} = \sqrt{k/m}$
   - $\omega_\text{simple} = \sqrt{g/\ell}$
   - $\omega_\text{phys} = \sqrt{m g d/I}$

6. **[3 pts]** Relations between $f$, $\omega$, $T$.
   - $\omega = 2\pi f = 2\pi/T$, $T = 1/f$

### Waves and Sound

(a) **[3 pts]** Right-going wave function; wavenumber; wave speed.
$$y(x,t) = A\cos(kx - \omega t),\quad k = 2\pi/\lambda,\quad v = \omega/k = \lambda f$$

(b) **[3 pts]** Wave speeds on string, in a solid, in a fluid.
$$v_\text{string} = \sqrt{F/\mu},\quad v_\text{solid} = \sqrt{Y/\rho},\quad v_\text{fluid} = \sqrt{B/\rho}$$

(c) **[2 pts]** Standing wave frequencies and wavelengths.
$$f_n = \frac{n v}{2 L}\text{ or }\frac{n v}{4 L},\quad \lambda_n = \frac{2 L}{n}\text{ or }\frac{4 L}{n}$$

(d) **[2 pts]** Average power on a string, intensity of sound.
$$P_\text{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2,\quad I = \tfrac{1}{2}\sqrt{\rho B}\,\omega^2 A^2$$

(e) **[2 pts]** Pressure amplitude, intensity vs. distance.
$$p_\text{max} = B k A,\quad I = P/(4\pi r^2)\text{ (spherical source)}$$

(f) **[2 pts]** Sound intensity level, reference intensity.
$$\beta = (10\text{ dB})\log_{10}(I/I_0),\quad I_0 = 10^{-12}\text{ W/m}^2$$

(g) **[2 pts]** Doppler shift (source right of listener) and beat frequency.
$$f_L = \frac{v + v_L}{v + v_S}\,f_S,\quad f_\text{beat} = |f_a - f_b|$$

---

## Calculation questions [120 points]

**1.** Pressure at the bottom of a mercury column, 47 cm deep. $p_\text{atm} = 105{,}368$ Pa, $\rho_\text{Hg} = 13{,}600$ kg/m³.
$$p = p_\text{atm} + \rho g h$$

**2.** Hydraulic jack: input piston radius $R_1 = 0.17$ m, output piston radius $R_2 = 1.48$ m, input force 413 N.
(a) Output force: $F_\text{out} = F_\text{in}(A_2/A_1) = F_\text{in}(R_2/R_1)^2$
(b) Pressure: $p = F_\text{in}/(\pi R_1^2)$

**3.** Hose fills a $8\text{ m}\times 3\text{ m}\times 3\text{ m}$ pool in 3 hours. Hose radius 1.9 cm. Find exit speed.
Volume flow rate: $dV/dt = A v\Rightarrow v = V_\text{pool}/(A_\text{hose}\cdot t)$

**4.** Block-spring oscillator, $k = 624$ N/m, $m = 4.4$ kg. Find period.
$$T = 2\pi\sqrt{m/k}$$

**5.** $m = 0.25$ kg oscillator, $E = 4.0$ J, $A = 0.20$ m. Find $\omega$.
$$E = \tfrac{1}{2}m\omega^2 A^2\Rightarrow \omega = \sqrt{2E/(mA^2)}$$

**6.** Pendulum $\ell = 0.67$ m, $m = 6.9$ kg, $g = 5.9$ m/s². Find frequency.
$$f = \frac{1}{2\pi}\sqrt{g/\ell}$$
(Mass is irrelevant.)

**7.** Wave $y(x,t) = 5\cos(3t + 0.5 x - 2.1)$, MKS. Identify all parameters:
- $A = 5$ m
- $\omega = 3$ rad/s (coeff. of $t$)
- $k = 0.5$ rad/m (coeff. of $x$)
- $\varphi = -2.1$ rad
- $f = \omega/(2\pi)\approx 0.477$ Hz
- $T = 2\pi/\omega\approx 2.094$ s
- $\lambda = 2\pi/k\approx 12.57$ m
- $v = \omega/k = 6$ m/s
- Note the $+$ sign on $x$ $\Rightarrow$ this wave moves in the $-x$ direction.
- Transverse speed at $(0,0)$: $\dot y = -A\omega\sin\varphi = -(5)(3)\sin(-2.1)\approx 12.97$ m/s

**8.** Piano wire: length 2.00 m, $\mu = 12.0$ g/m = 0.012 kg/m, $F = 8000$ N. Second harmonic frequency.
$$v = \sqrt{F/\mu},\quad f_1 = v/(2L),\quad f_2 = 2 f_1$$

**9.** Sound wave travels 20.8 m in 11 ms in a fluid with $\rho = 1229$ kg/m³. Find bulk modulus (GPa).
$$v = 20.8/0.011\text{ m/s},\qquad B = \rho v^2$$

**10.** 4 sirens each at 119 dB at 10 m. Find total intensity.
Single siren: $I_1 = I_0\cdot 10^{\beta/10}$; then $I_\text{total} = 4 I_1$.

**11.** Two guitars with periods $T_a = 1.860$ ms, $T_b = 1.889$ ms. Beat frequency.
$$f_\text{beat} = |1/T_a - 1/T_b|$$

**12.** Motorcyclist recedes from police car at 49 m/s; siren at 439 Hz, $v = 340$ m/s. Find frequency heard.
Listener moving away from stationary source; source is behind the listener.
$$f_L = \frac{v - v_L}{v}\,f_S = \frac{340 - 49}{340}\cdot 439\approx 375.8\text{ Hz}$$

### Bonus — two-path interference

Paths of 20.0 m and 21.0 m from source to point O, $\Delta r = 1.0$ m, $v = 340$ m/s. Minimum frequency for constructive interference:
$$\Delta r = m\lambda,\quad m_\text{min} = 1\Rightarrow \lambda = 1.0\text{ m},\quad f = v/\lambda = 340\text{ Hz}$$
