# PS160 --- Master Topics & Theory Index

One-page map of every topic in the course. Use this as a checklist when prepping for the comprehensive final.

For the full theory narrative of each midterm, see:
- [../midterm_01/review.md](../midterm_01/review.md)
- [../midterm_02/review.md](../midterm_02/review.md)
- [./review.md](./review.md)

---

## Part I --- Mechanics of Fluids and Waves (Midterm 1)

### Module 12 --- Fluid Mechanics
- Density, pressure
- Hydrostatic pressure, $p(y) = p_0 - \rho g y$
- Gauge vs. absolute pressure; Pascal's law
- Buoyancy and Archimedes' principle
- Surface tension (brief)
- Streamlines and continuity: $\rho A v = $ const
- Bernoulli's equation; Torricelli's law
- Venturi effect, lift on wings, atomizers
- Viscosity, Poiseuille flow (brief)

### Module 14 --- Oscillations
- Simple harmonic motion: $\ddot x + \omega^2 x = 0$
- Amplitude, angular frequency, phase
- Velocity and acceleration in SHM
- Energy in SHM: $E = \tfrac{1}{2}kA^2$
- Mass-spring system
- Simple pendulum (small angles)
- Physical pendulum
- Damped oscillations (underdamped, critical, overdamped)
- Driven oscillations and resonance

### Module 15 --- Mechanical Waves
- Transverse vs. longitudinal waves
- Wave function, wavenumber, wave speed
- Wave equation
- Wave speeds: string, solid, fluid
- Power and intensity
- Principle of superposition
- Interference of two waves
- Standing waves, normal modes, harmonics
- Boundary conditions on a string

### Module 16 --- Sound
- Sound waves as longitudinal pressure waves
- Speed of sound in gases; temperature dependence
- Intensity and the decibel scale
- Spherical source, inverse-square law
- Standing sound waves in pipes (open-open, open-closed)
- Beat phenomenon
- Doppler effect

## Part II --- Thermodynamics (Midterm 2)

### Module 17 --- Temperature and Heat
- Thermal equilibrium, temperature scales (K, °C, °F, R)
- Thermometers
- Linear and volumetric thermal expansion
- Thermal stress
- Heat, specific heat, molar heat capacity
- Phase changes and latent heat
- Calorimetry
- Conduction (steady-state slab)
- Convection (qualitative)
- Radiation (Stefan--Boltzmann, emissivity)

### Module 18 --- Thermal Properties of Matter / Kinetic Theory
- Equations of state, ideal gas law
- Kinetic theory derivation: $pV = \tfrac{1}{3}Nm\langle v^2\rangle$
- Translational kinetic energy per molecule: $\tfrac{3}{2}kT$
- Root-mean-square speed
- Maxwell-Boltzmann distribution
- Equipartition theorem and degrees of freedom
- Molar heat capacities, $C_V$ and $C_P$; $\gamma$
- Dulong-Petit for solids
- Phases of matter, phase diagrams (brief)

### Module 19 --- First Law of Thermodynamics
- System, surroundings, state variables
- Work done by a gas: $W = \int p\,dV$
- First law: $\Delta U = Q - W$
- Internal energy of an ideal gas depends only on $T$
- Isobaric, isochoric, isothermal, adiabatic processes
- $pV$ diagrams and path dependence
- Cyclic processes

### Module 20 --- Second Law of Thermodynamics
- Direction of thermodynamic processes
- Heat engines and thermal efficiency
- Refrigerators and heat pumps
- Kelvin-Planck and Clausius statements
- The Carnot cycle; Carnot efficiency $1 - T_C/T_H$
- Reversible and irreversible processes
- Entropy and $\Delta S$ for simple processes
- Microscopic view: $S = k\ln w$
- Entropy and the arrow of time

## Part III --- Electromagnetic Waves and Optics (Midterm 3 emphasis)

### Module 33 --- Electromagnetic Waves
- Maxwell's equations (conceptual)
- Displacement current
- Plane EM waves in vacuum
- $c = 1/\sqrt{\mu_0\varepsilon_0}$
- $E/B = c$; transverse nature
- EM waves in dielectrics, $v = c/n$
- Energy density, Poynting vector, intensity
- Radiation pressure and momentum
- Polarization, Malus's law
- Brewster's angle

### Module 34 --- Geometric Optics
- Reflection and refraction
- Snell's law and index of refraction
- Total internal reflection, critical angle
- Dispersion (brief, rainbow)
- Plane mirrors, spherical mirrors
- Thin lenses, converging and diverging
- Mirror/lens equation; sign conventions
- Lateral magnification
- Lensmaker's equation
- Refraction at a single spherical surface
- Ray diagrams
- Two-lens systems
- Optical instruments: eye, magnifier, microscope, telescope

### Module 35 --- Interference
- Superposition of waves, coherence
- Constructive and destructive interference conditions
- Young's double-slit experiment
- Two-source intensity pattern
- Phase shifts on reflection at an interface
- Thin-film interference (soap films, anti-reflection coatings, Newton's rings)
- Michelson interferometer

### Module 36 --- Diffraction
- Fraunhofer diffraction from a single slit
- Intensity distribution (sinc² pattern)
- Double-slit diffraction (combined)
- Diffraction gratings
- Chromatic resolving power
- Circular apertures and Airy disk
- Rayleigh resolution criterion
- X-ray diffraction and Bragg's law

---

## Cross-course conceptual threads

1. **Waves unify a lot of the course.** Chapters 15, 16, 33, 35, 36 are all variations on "add waves, look at intensity, enforce boundary conditions." The same math (superposition, standing conditions $d\sin\theta = m\lambda$, wave speed $v = \lambda f$) shows up repeatedly.

2. **Energy conservation** runs throughout:
    - Bernoulli's equation (M12)
    - Mechanical energy in SHM (M14)
    - Wave energy and power (M15, M16, M33)
    - First law of thermodynamics (M19)
    - EM wave energy density and Poynting vector (M33)

3. **Temperature and statistical ideas** (M17-M18) tie to the direction of time (M20), and the same $kT$ energy scale appears in equipartition and in Maxwell-Boltzmann.

4. **Maxwell's equations → speed of light → all of optics.** Everything in M33-M36 flows downstream from the four Maxwell equations. Knowing $c = 1/\sqrt{\mu_0\varepsilon_0}$ is non-negotiable.

5. **Superposition** holds in every linear medium: mechanical waves, sound, EM waves, quantum (next course). Diffraction and interference patterns are the same phenomenon with different source geometries.

---

## Quick-glance equation count by section

| Section | Equations to memorize |
|---|---|
| Fluids | ~7 |
| Oscillations | ~10 |
| Waves | ~10 |
| Sound | ~8 |
| Temperature & heat | ~8 |
| Kinetic theory | ~7 |
| First law & processes | ~10 |
| Second law & entropy | ~8 |
| EM waves | ~10 |
| Geometric optics | ~8 |
| Interference | ~6 |
| Diffraction | ~6 |
| **Total** | **~100** |

See [master_equations.tex](master_equations.tex) for all of them in one document.
