# PS160 Midterm 1 --- Topics and Theory Review

**Scope:** Modules 12 (Fluid Mechanics), 14 (Oscillations), 15 (Mechanical Waves), 16 (Sound).

See [equations.tex](equations.tex) for the equation sheet, and [knowledge_ps160_mid01.pdf](knowledge_ps160_mid01.pdf) for the official knowledge questions.

---

## Module 12 --- Fluid Mechanics

### Topics
- Density and pressure
- Pressure in a static fluid (hydrostatic equation)
- Pascal's law and hydraulic systems
- Buoyancy / Archimedes' principle
- Surface tension (brief)
- Fluid flow: streamlines, continuity, Bernoulli
- Viscosity / Poiseuille (brief)

### Theory

**Density** $\rho = m/V$ is an intensive property. **Pressure** $p = F_\perp/A$ is the normal force per unit area; it's a scalar, the same in all directions at a point (Pascal's principle on a differential level).

**Hydrostatic equation:** In a fluid at rest in a uniform gravitational field, $dp/dy = -\rho g$. For constant density this integrates to $p(y) = p_0 - \rho g y$. A key consequence: pressure depends only on depth, not on container shape.

**Gauge vs. absolute pressure:** Most gauges read $p - p_{\text{atm}}$. When you see "gauge pressure", add $p_{\text{atm}} = 101{,}325$ Pa to convert to absolute.

**Pascal's law:** A pressure change applied to any part of a confined incompressible fluid is transmitted undiminished. This is what makes hydraulic lifts work — a small force on a small piston produces a large force on a large piston in the same ratio as the areas.

**Archimedes' principle:** A body fully or partially submerged in a fluid experiences a buoyant force equal to the weight of the displaced fluid: $F_B = \rho_{\text{fluid}} V_{\text{disp}} g$. Floating condition: $\rho_{\text{object}} \le \rho_{\text{fluid}}$.

**Continuity equation:** For an incompressible fluid in steady flow, $\rho A v$ is conserved along a streamline, so $A_1 v_1 = A_2 v_2$. Narrower pipe ⇒ faster flow. Volume flow rate $dV/dt = Av$.

**Bernoulli's equation:** Along a streamline, $p + \rho g y + \tfrac{1}{2}\rho v^2 = \text{const}$. It's energy conservation per unit volume for an ideal (inviscid, incompressible, steady) flow. Used for: Venturi meters, Torricelli's law ($v = \sqrt{2gh}$ for fluid draining from a tank), lift on wings, atomizers.

### Common problem archetypes
- "Pressure at depth $h$": $p = p_0 + \rho g h$.
- "Manometer with two fluids": set pressures equal at the lowest common point.
- Hydraulic lift force ratios.
- Floating iceberg: fraction submerged = $\rho_{\text{ice}}/\rho_{\text{water}}$.
- Pipe narrowing: use continuity + Bernoulli together.

---

## Module 14 --- Oscillations

### Topics
- Simple harmonic motion (SHM)
- Energy in SHM
- Pendulums: simple and physical
- Damped oscillations
- Driven/forced oscillations and resonance

### Theory

**Defining SHM:** A system obeys $F = -kx$ (linear restoring force) so $\ddot{x} + \omega^2 x = 0$ with $\omega^2 = k/m$. The general solution is $x(t) = A\cos(\omega t + \varphi)$. $A$ is set by the initial displacement/energy, $\varphi$ by the initial phase.

**Relations you must know by reflex:**
- $v(t) = -A\omega\sin(\omega t + \varphi)$, $v_{\max} = A\omega$
- $a(t) = -\omega^2 x$, $a_{\max} = A\omega^2$
- $f = 1/T = \omega/(2\pi)$, $T = 2\pi/\omega$

**Period is independent of amplitude** for ideal SHM — this is the key fact that makes it useful as a clock.

**Mass-spring:** $\omega = \sqrt{k/m}$. Horizontal or vertical (gravity just shifts the equilibrium).

**Simple pendulum (small angle):** $\omega = \sqrt{g/\ell}$, so $T = 2\pi\sqrt{\ell/g}$. Valid for small angles where $\sin\theta \approx \theta$.

**Physical pendulum (rigid body on pivot):** $\omega = \sqrt{mgd/I}$ where $d$ is distance from pivot to center of mass and $I$ is the moment of inertia about the pivot axis.

**Energy:** Total mechanical energy $E = \tfrac{1}{2}kA^2 = \tfrac{1}{2}m\omega^2 A^2$ is conserved (ideal case). Kinetic and potential exchange twice per period.

**Damped SHM:** Adding $-b\dot{x}$ gives $m\ddot{x} + b\dot{x} + kx = 0$. Three regimes: underdamped (oscillates with decaying envelope), critically damped (fastest non-oscillatory return to equilibrium, $b = 2\sqrt{mk}$), overdamped (slow return).

**Driven resonance:** Steady-state amplitude peaks when drive frequency $\omega_d \approx$ natural $\omega_0$. Amplitude at resonance is limited by damping constant $b$. Smaller damping ⇒ taller, sharper peak.

### Common problem archetypes
- Given $x(0)$ and $v(0)$, find $A$ and $\varphi$.
- Spring: two springs in series/parallel (series adds $1/k$; parallel adds $k$).
- Physical pendulum around a non-COM pivot.
- Damped: find time for amplitude to decay to half.
- Match differential equation to regime.

---

## Module 15 --- Mechanical Waves

### Topics
- Transverse vs. longitudinal waves
- Wave function and wave speed
- The wave equation
- Wave speeds in strings, solids, fluids
- Energy and power in waves
- Wave interference / superposition
- Standing waves on strings
- Boundary conditions, normal modes, harmonics

### Theory

**Traveling wave (right-going):** $y(x,t) = A\cos(kx - \omega t)$. Replace $-\omega t$ with $+\omega t$ for left-going.

**Wavenumber and wave speed:** $k = 2\pi/\lambda$, $\omega = 2\pi f$, $v = \lambda f = \omega/k$. Note: $k$ here is not spring constant.

**Wave equation:** $\partial^2 y/\partial t^2 = v^2\,\partial^2 y/\partial x^2$. Any function of the form $f(x - vt)$ or $g(x + vt)$ solves it; superposition of two gives standing waves.

**Wave speed depends on medium, not on amplitude or frequency** (in the linear regime):
- On a string: $v = \sqrt{F/\mu}$ — tension over mass per unit length.
- In a solid: $v = \sqrt{Y/\rho}$ — Young's modulus over density.
- In a fluid: $v = \sqrt{B/\rho}$ — bulk modulus over density.

**Power** carried by a wave on a string: $P_{\text{av}} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2$. Power scales as $\omega^2 A^2$.

**Superposition principle:** In a linear medium, if $y_1$ and $y_2$ are solutions so is $y_1 + y_2$. Gives interference.

**Standing waves** arise from two counter-propagating waves with equal $A$, $\omega$, $k$. On a string with both ends fixed (or both ends free, or in a pipe open at both ends): $\lambda_n = 2L/n$, $f_n = nv/(2L)$, $n = 1, 2, 3, \dots$. With one end fixed and one free: $\lambda_n = 4L/n$, $f_n = nv/(4L)$, $n = 1, 3, 5, \dots$ (odd only).

**Nodes** are where amplitude is always zero; **antinodes** are where it's maximum. Successive nodes are half a wavelength apart.

### Common problem archetypes
- Identify $A$, $\omega$, $k$, direction, speed from a wave function.
- Find tension or $\mu$ for a desired wave speed.
- Standing wave: given $L$ and a harmonic, find $f_n$ and $\lambda_n$.
- Beat of two frequencies (also appears in M16).

---

## Module 16 --- Sound

### Topics
- Sound as a longitudinal pressure wave
- Speed of sound in gases
- Intensity, decibels, inverse-square law
- Standing sound waves in pipes
- Beats
- Doppler effect

### Theory

**Sound waves are longitudinal.** They can be represented either as a displacement wave $y(x,t)$ or as an equivalent pressure wave $p(x,t)$ — these are $90°$ out of phase with each other in space. Pressure amplitude: $p_{\max} = BkA$.

**Speed of sound:** In a fluid, $v = \sqrt{B/\rho}$. In an ideal gas, $v = \sqrt{\gamma RT/M}$, so it scales with $\sqrt{T}$ and depends on the gas. At $20°$C in air, $v \approx 343$ m/s (this is the standard value used in PS160).

**Intensity** is average power per unit area: $I = \tfrac{1}{2}\sqrt{\rho B}\,\omega^2 A^2 = p_{\max}^2/(2\sqrt{\rho B})$. For a point source radiating uniformly, $I = P/(4\pi r^2)$ — inverse-square law.

**Decibel scale:** $\beta = (10\text{ dB})\log_{10}(I/I_0)$ with $I_0 = 10^{-12}$ W/m². A factor-of-10 increase in $I$ is 10 dB; a doubling is $\approx 3$ dB. Threshold of hearing is 0 dB; typical conversation $\sim 60$ dB; pain threshold $\sim 120$ dB.

**Standing sound waves in pipes:**
- Open at both ends: both ends are pressure nodes / displacement antinodes. $f_n = nv/(2L)$, all integers.
- Closed at one end: closed end is pressure antinode / displacement node. $f_n = nv/(4L)$, odd integers only.

**Beats:** Two sounds of slightly different frequency $f_a$ and $f_b$ produce a slow amplitude modulation at $f_{\text{beat}} = |f_a - f_b|$. Used by musicians to tune instruments.

**Doppler effect:** For a source and listener moving along the line between them (source to the right of listener, velocities positive in the $+x$ direction):
$$f_L = f_S\left(\frac{v + v_L}{v + v_S}\right)$$
where $v$ is the speed of sound in the medium. Get the signs right by remembering: approaching source ⇒ higher frequency observed; receding source ⇒ lower.

### Common problem archetypes
- dB $\leftrightarrow$ intensity conversions.
- Given distance and source power, find intensity and dB.
- Pipe length from fundamental frequency, or vice versa.
- Doppler: moving car and stationary listener, or two moving vehicles.
- Beat frequency: one "target" + one "tuning fork".

---

## Cross-module connections
- Oscillations + waves: every point in a wave undergoes SHM; $\omega^2 A^2$ shows up in both energy and intensity.
- Fluids + sound: $v = \sqrt{B/\rho}$ comes from fluid mechanics and gives sound speed.
- SHM natural frequency + waves: standing waves are eigenmodes — each mode is an SHM.

## Tips for exam prep
1. Memorize the knowledge-question formulas cold — they're guaranteed 30 points.
2. Practice dimensional analysis: every formula on the equation sheet has clean SI units you can use to check answers.
3. Sign conventions in Doppler and in buoyancy (floating vs. sinking) cause most algebra errors.
4. Know which modes exist for each boundary condition (standing waves on strings, sound in pipes).
