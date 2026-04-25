# PS160 Spring 2024 Final Exam — Walkthrough Solutions

> ⚠️ **No source answer key.** Independently computed. Where Spring 2024 questions reuse the *exact* same scenario as the Fall 2024 final (Q6, Q11, Q16, Q22, Q24, Q25), the numeric answer is cross-referenced to the [Fall 2024 walkthrough (`midterm3_final_v1_solutions.md`)](midterm3_final_v1_solutions.md) and the official Fall key. Image-dependent items (Q17, Q18) are flagged.

**Score:** 250 / 300 best — all questions 10 pts unless flagged. **Compound 20-pt items:** Q6 (a–i), Q15 (a–b), Q19 (a–d), Q20 (a–d).

---

## Equation bank (PS160 official sheet — Midterm 1, 2, and 3 material)

**Fluids / oscillations / waves:**
$$p = p_0 + \rho g h, \qquad F_2/F_1 = A_2/A_1, \qquad \omega=\sqrt{k/m},\ \omega=\sqrt{g/\ell}$$
$$E_{\text{spring}}=\tfrac12 kA^2,\qquad y(x,t)=A\cos(kx \pm \omega t + \phi),\qquad k=2\pi/\lambda,\ \omega=2\pi f,\ v=\lambda f=\omega/k$$
$$v_{\text{string}}=\sqrt{F/\mu},\qquad f_n=\tfrac{nv}{2L}\ (\text{both ends fixed}),\qquad v_y=\partial y/\partial t$$

**Sound:**
$$I = P/(4\pi r^2),\qquad \beta = (10\,\text{dB})\log_{10}(I/I_0),\ I_0 = 10^{-12}\,\text{W/m}^2$$
$$f_L = f_S\frac{v+v_L}{v+v_S}\quad\text{(sign convention: velocities measured toward source/listener)}$$

**Thermal:**
$$\Delta L=\alpha L_0\Delta T,\ \Delta V=\beta V_0\Delta T,\ \beta=3\alpha,\qquad Q=mc\Delta T,\ Q=\pm mL$$
$$pV=nRT,\ K_{\text{tr}}=\tfrac32 nRT,\qquad W=\int p\,dV$$
$$\Delta U=Q-W,\ \Delta U_{\text{ideal}}=nC_V\Delta T,\ \Delta S=\int dQ/T$$
$$e_{\text{Carnot}} = 1-T_C/T_H,\ e=W/Q_H$$

**Optics — geometric:**
$$\theta_i=\theta_r,\qquad n_1\sin\theta_1=n_2\sin\theta_2,\qquad \sin\theta_c = n_2/n_1$$
$$\tfrac1s+\tfrac1{s'}=\tfrac1f,\qquad m=-s'/s$$
Sign convention: $s'>0$ real/in-front-of-mirror or behind-lens; $f>0$ converging lens / concave mirror; $f<0$ diverging lens / convex mirror.

**Optics — wave:**
$$\text{Bubble (1 net flip), bright reflection: } 2nt=(m+\tfrac12)\lambda \Rightarrow t_{\min}=\lambda/(4n)$$
$$\text{Double slit fringe spacing: } \Delta y=\lambda L/d;\ \text{single slit central full-width: } 2\lambda L/a$$
$$\text{Single-slit minima: } a\sin\theta=m\lambda;\quad \text{Bragg: } 2d\sin\theta = m\lambda$$
$$\text{Rayleigh: } \theta_{\min} = 1.22\lambda/D$$

---

## Q1 — Pressure at bottom of mercury column

Hydrostatic: $p = p_{\text{atm}} + \rho g h$. With $\rho_{Hg} = 13.6\,\text{g/cm}^3 = 13600\,\text{kg/m}^3$, $h=0.46$ m:

$$p = 71{,}000 + (13600)(9.8)(0.46) = 71{,}000 + 61{,}308.8 = \boxed{1.323\times 10^5\ \text{Pa}}$$

## Q2 — Hydraulic jack force ratio

Equal pressure on both pistons: $F_2 = F_1 \cdot A_2/A_1 = 640 \cdot (0.25/0.03)$.

$$F_2 = 640(8.333) = 5333\,\text{N} = \boxed{5.333\ \text{kN}}$$

## Q3 — Pendulum period on exoplanet

Small-angle simple pendulum: $T = 2\pi\sqrt{L/g}$. (Mass cancels.)

$$T = 2\pi\sqrt{1.87/7.3} = 2\pi\sqrt{0.2562} = 2\pi(0.5061) = \boxed{3.180\ \text{s}}$$

## Q4 — Spring SHM total energy

Total mechanical energy of mass-spring oscillator: $E = \tfrac12 k A^2$.

$$E = \tfrac12(288)(0.14)^2 = \tfrac12(288)(0.0196) = \boxed{2.822\ \text{J}}$$

## Q5 — Vibrating string, $n=3$ mode

Linear density $\mu = 0.003/0.55 = 5.4545\times 10^{-3}$ kg/m. Wave speed $v = \sqrt{F/\mu}$. Standing wave on string fixed at both ends: $f_n = nv/(2L)$.

- (b) $v = \sqrt{12/5.4545\times 10^{-3}} = \sqrt{2200} = \boxed{46.90\ \text{m/s}}$
- (a) $f_3 = 3(46.90)/(2\cdot 0.55) = 140.71/1.1 = \boxed{127.9\ \text{Hz}}$

## Q6 — Wave function $y(x,t)=5\cos(3t+0.5x-2.1)$ [20 pts]

> Same wave as Fall 2024 final Q15 — see [Fall walkthrough](midterm3_final_v1_solutions.md). Spring asks 9 sub-parts (a–i); Fall added (j) max transverse speed which is omitted here.

Both $\omega t$ and $kx$ have the **same sign**, so the wave travels in the $-x$ direction.

- **(a)** Amplitude $A = \boxed{5\ \text{m}}$
- **(b)** Angular frequency $\omega = \boxed{3\ \text{rad/s}}$
- **(c)** Wavenumber $k = \boxed{0.5\ \text{rad/m}}$
- **(d)** Phase shift $\phi = \boxed{-2.1\ \text{rad}}$
- **(e)** $f = \omega/(2\pi) = 3/(2\pi) = \boxed{0.4775\ \text{Hz}}$
- **(f)** $T = 1/f = 2\pi/3 = \boxed{2.094\ \text{s}}$
- **(g)** $\lambda = 2\pi/k = 2\pi/0.5 = \boxed{12.57\ \text{m}}$
- **(h)** $v = \omega/k = 3/0.5 = \boxed{6\ \text{m/s}}$ (in the $-x$ direction)
- **(i)** $v_y(x,t) = -A\omega\sin(3t+0.5x-2.1)$. At $(0,0)$: $v_y = -5(3)\sin(-2.1) = -15(-0.8632) = \boxed{12.95\ \text{m/s}}$

## Q7 — Sound intensity at 39 m from a 116-dB siren

Reverse the dB at 6 m: $I_6 = I_0\cdot 10^{\beta/10} = 10^{-12}\cdot 10^{11.6} = 0.3981\,\text{W/m}^2$. Inverse-square to 39 m:

$$I_{39} = I_6\left(\frac{6}{39}\right)^2 = 0.3981\,(0.02367) = 9.422\times 10^{-3}\ \text{W/m}^2 = \boxed{9.42\ \text{mW/m}^2}$$

## Q8 — Doppler, listener moving away from stationary source

Listener moving away: $v_L = -49$ m/s (using sheet's $f_L=f_S(v+v_L)/(v+v_S)$ with the "toward source positive" convention). Source at rest: $v_S=0$.

$$f_L = 439\cdot\frac{340-49}{340} = 439\cdot\frac{291}{340} = 439(0.8559) = \boxed{375.7\ \text{Hz}}$$

## Q9 — Granite sphere thermal expansion

Volumetric: $\Delta V = \beta V_0\Delta T$ with $\beta = 3\alpha = 3(3.5\times 10^{-5}) = 1.05\times 10^{-4}\,\text{K}^{-1}$.

$$\Delta T = \frac{\Delta V}{\beta V_0} = \frac{10^{-3}}{(1.05\times 10^{-4})(1)} = \boxed{9.524\ ^\circ\text{C}}$$

## Q10 — Iron in water, equilibrium temperature

Heat lost by iron = heat gained by water: $m_{Fe}c_{Fe}(90-T) = m_w c_w(T-10)$.

$$9(444)(90-T) = 2(4190)(T-10)$$
$$3996(90-T) = 8380(T-10)$$
$$359{,}640 - 3996T = 8380T - 83{,}800$$
$$443{,}440 = 12{,}376\,T \Rightarrow T = \boxed{35.83\ ^\circ\text{C}}$$

## Q11 — Combined gas law

> Identical to Fall 2024 Q22 — answer **261 kPa** (Fall key). See [Fall walkthrough](midterm3_final_v1_solutions.md).

$T_1 = 493.15$ K, $T_2 = 723.15$ K, $V_2 = 0.5\,V_1$.

$$p_2 = p_1\frac{V_1}{V_2}\frac{T_2}{T_1} = 89(2)(723.15/493.15) = 89(2)(1.4664) = \boxed{261.0\ \text{kPa}}$$

## Q12 — Translational KE of ideal gas

$K_{\text{tr}} = \tfrac32 nRT$, $T = 296.15$ K.

$$K_{\text{tr}} = 1.5(7.2)(8.314)(296.15) = 26{,}579\ \text{J} = \boxed{26.58\ \text{kJ}}$$

## Q13 — Isobaric work done **by** the gas

$W = p\,\Delta V = (50\,\text{kPa})(1.2-1.8\,\text{m}^3) = 50(-0.6) = \boxed{-30\ \text{kJ}}$

(Negative because the gas is compressed — work is done **on** it.)

## Q14 — Isothermal expansion, $\Delta U$

For an ideal gas, internal energy depends only on $T$. Isothermal $\Rightarrow \Delta T = 0 \Rightarrow$

$$\Delta U = \boxed{0\ \text{J}}$$

(Pressure and volume values are red herrings for this part.)

## Q15 — Carnot engine [20 pts]

- **(b)** Efficiency $e = 1 - T_C/T_H = 1 - 305/799 = 1 - 0.3817 = \boxed{0.6183}$ (or 61.83%).
- **(a)** Work per cycle $W = e\cdot Q_H = 0.6183(2400) = \boxed{1484\ \text{J}}$.

## Q16 — 11 kg water freezes at 0 °C, $\Delta S$

> Identical to Fall 2024 Q27 — answer **−13.5 kJ/K** (Fall key). See [Fall walkthrough](midterm3_final_v1_solutions.md).

Reversible heat removal at $T = 273.15$ K: $Q = -mL_f$ (sign negative — heat leaves the water).

$$\Delta S = Q/T = -11(3.35\times 10^5)/273.15 = -3{,}685{,}000/273.15 = -13{,}491\ \text{J/K} = \boxed{-13.49\ \text{kJ/K}}$$

## Q17 — Two-mirror corner reflection ⚠️ figure-dependent

With $\phi = 60°$ (angle between mirrors at the corner) and $\theta = 60°$ (incidence on first mirror, measured from its normal). The triangle bounded by the corner, the bounce point on m1, and the bounce point on m2 has interior angles $\phi$, $(90°-\theta)$, and the third angle $\beta$ at m2:

$$\beta = 180° - \phi - (90°-\theta) = 90° + \theta - \phi = 90°+60°-60° = 90°$$

The ray hits mirror 2 along its surface-normal, so the angle of incidence on m2 is $0°$. By law of reflection, the **outgoing** ray is also along the normal:

$$\alpha = \boxed{0°}$$

(Coincidence-retroreflector geometry. *Verify against the figure orientation.*)

## Q18 — Light through oil layer onto water ⚠️ figure-dependent

Apply Snell at both interfaces. At air→oil: $1\sin(33°) = 1.59\sin\theta_{\text{oil}}$. At oil→water: $1.59\sin\theta_{\text{oil}} = 1.33\sin\phi$. The middle layer cancels — only first and last $n$ matter:

$$\sin\phi = \sin(33°)/1.33 = 0.5446/1.33 = 0.4095$$
$$\phi = \boxed{24.18°}$$

## Q19 — Concave mirror, $s=18$, $f=8$ [20 pts]

Mirror equation: $1/s' = 1/f - 1/s = 1/8 - 1/18 = (18-8)/144 = 10/144$.

- **(a)** $s' = 144/10 = \boxed{14.4\ \text{cm}}$
- **(b)** $m = -s'/s = -14.4/18 = \boxed{-0.8}$
- **(c)** $s' > 0 \Rightarrow$ **real**
- **(d)** $m<0 \Rightarrow$ **inverted**

## Q20 — Diverging lens, $s=16$, $f=-12$ [20 pts]

Lens equation: $1/s' = 1/f - 1/s = -1/12 - 1/16 = (-16-12)/192 = -28/192$.

- **(a)** $s' = -192/28 = \boxed{-6.857\ \text{cm}}$
- **(b)** $m = -s'/s = -(-6.857)/16 = \boxed{+0.4286}$
- **(c)** $s' < 0 \Rightarrow$ **virtual**
- **(d)** $m>0 \Rightarrow$ **upright**

(Diverging lenses always produce virtual, upright, reduced images of real objects.)

## Q21 — Refraction with critical angle given

The critical angle is for total internal reflection from the **liquid** side (denser medium). $n_{\text{liq}}\sin\theta_c = 1\cdot\sin(90°)$:

$$n_{\text{liq}} = 1/\sin(43.5°) = 1/0.6884 = 1.4524$$

Now ray in air at $28°$ refracts into the liquid:

$$\sin\theta_r = \sin(28°)/1.4524 = 0.4695/1.4524 = 0.3232$$
$$\theta_r = \boxed{18.85°}$$

## Q22 — Bubble enhancement, 471 nm, $n=1.5$

> Identical to Fall 2024 Q31 — answer **78.5 nm** (Fall key). See [Fall walkthrough](midterm3_final_v1_solutions.md).

Soap-bubble film with air on both sides: net 1 phase flip. Constructive reflection: $2nt=(m+\tfrac12)\lambda$, minimum at $m=0$:

$$t_{\min} = \lambda/(4n) = 471/(4\cdot 1.5) = \boxed{78.5\ \text{nm}}$$

## Q23 — Single-slit, find $\lambda$ from $m=2$ minimum

Dark fringe: $a\sin\theta = m\lambda$, small angle $y_m \approx m\lambda L/a$.

$$\lambda = \frac{y\,a}{m\,L} = \frac{(7.3\times 10^{-3})(3.1\times 10^{-4})}{2\cdot 2} = \frac{2.263\times 10^{-6}}{4} = 5.658\times 10^{-7}\,\text{m} = \boxed{565.8\ \text{nm}}$$

## Q24 — Double-slit central-max width

> Identical to Fall 2024 Q32 — answer **3.376 mm** (Fall key). See [Fall walkthrough](midterm3_final_v1_solutions.md).

For double slit, the central bright fringe spans one fringe spacing $\Delta y = \lambda L/d$ (between the two flanking dark fringes at $m=\pm\tfrac12$):

$$\Delta y = (418\times 10^{-9})(2.1)/(2.6\times 10^{-4}) = 8.778\times 10^{-7}/2.6\times 10^{-4} = \boxed{3.376\ \text{mm}}$$

## Q25 — Mars space telescope crater resolution

> Identical to Fall 2024 Q33 — answer **13.33 m** (Fall key). See [Fall walkthrough](midterm3_final_v1_solutions.md).

Rayleigh: $\theta_{\min} = 1.22\lambda/D$, then $d_{\min} = \theta_{\min}\cdot L$.

$$\theta_{\min} = 1.22(557\times 10^{-9})/0.045 = 1.510\times 10^{-5}\ \text{rad}$$
$$d_{\min} = (1.510\times 10^{-5})(883{,}000) = \boxed{13.33\ \text{m}}$$

## Q26 — Bragg first-order diffraction

Bragg's law uses the **grazing** angle: $2d\sin\theta = m\lambda$ with $m=1$, $\theta=23°$:

$$d = \lambda/(2\sin\theta) = 0.54/(2\sin 23°) = 0.54/(2\cdot 0.3907) = 0.54/0.7814 = \boxed{0.691\ \text{nm}}$$

---

**Independently computed; cross-check Q17 and Q18 against the figure.** Q6, Q11, Q16, Q22, Q24, Q25 confirmed against the official Fall 2024 answer key for the identical scenarios.
