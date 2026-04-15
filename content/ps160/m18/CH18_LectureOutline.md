# Chapter 18: Thermal Properties of Matter — Lecture Outline

## Learning Outcomes

In this chapter, you'll learn:
- How to relate the pressure, volume, and temperature of a gas.
- How pressure and temperature of a gas are related to the **kinetic energy** of its molecules.
- How heat capacities of a gas reveal whether molecules rotate or vibrate.
- How molecular speeds are distributed in a gas.
- What determines whether a substance is a gas, liquid, or solid.

## Introduction

- Microscopic properties of matter determine macroscopic properties.
- Example: ideal-gas equation $pV = nRT$ describes the air in a tire (≈3 atm, well above liquefaction). As $T$ rises, $V$ is nearly constant so $p$ rises.

## Equations of State and the Ideal-Gas Law

**State variables**: pressure, volume, temperature, amount of substance — describe the state of a material.

**Ideal-gas equation** (an equation of state):
$$pV = nRT$$
- $p$: pressure
- $V$: volume
- $n$: number of moles
- $R$: gas constant $= 8.314$ J/(mol·K)
- $T$: absolute temperature (Kelvin)

**Molar mass** $M$: mass per mole. Total mass of $n$ moles: $m_{\text{total}} = nM$.

### pV Diagrams
- **Isotherms**: curves of constant $T$. For each curve, $pV = $ const and is proportional to $T$ (Boyle's law).
- $T_4 > T_3 > T_2 > T_1$ on successive isotherms.

### Van der Waals Equation

More realistic model (accounts for molecular volume and attractive forces):
$$\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT$$

- Ideal gas assumes molecules are infinitely small with no mutual forces.
- $a$ accounts for attraction reducing pressure; $b$ for molecular volume reducing free volume.

### pV Diagrams for Nonideal Gas
- Critical temperature $T_c$: above this no liquid-vapor phase transition occurs.
- Below $T_c$, isotherms enter a liquid-vapor equilibrium region as the gas compresses.

## Molecules and Intermolecular Forces

- In gases, molecules move nearly independently.
- Force vs. separation $r$: at $r = r_0$, $U$ is minimum and force is zero. For $r < r_0$, force is repulsive; for $r > r_0$, force is attractive.
- Solids: molecules essentially fixed. Liquids/gases: more freedom.

## Moles and Avogadro's Number

- One **mole** = number of entities in 0.012 kg of carbon-12.
- **Avogadro's number**:
$$N_A = 6.022 \times 10^{23}~\text{molecules/mol}$$
- **Molar mass**:
$$M = N_A m$$
where $m$ is the mass per molecule.

## Kinetic-Molecular Model of an Ideal Gas

**Assumptions**:
1. Container holds a very large number of identical molecules.
2. Molecules behave as point particles (small compared to container and interparticle spacing).
3. Molecules in constant motion, undergo perfectly elastic collisions.
4. Container walls are perfectly rigid and don't move.

### Collisions and Gas Pressure
- In collisions with walls, the velocity component parallel to the wall is unchanged; the component perpendicular reverses direction (same magnitude). Speed $v$ is unchanged.
- During $dt$, molecules within distance $|v_x|\,dt$ of wall area $A$ (moving toward it) will collide — a cylindrical volume $A|v_x|dt$.

### Pressure and Molecular Kinetic Energies

**Total translational kinetic energy** of $n$ moles of ideal gas:
$$K_{\text{tr}} = \tfrac{3}{2} n R T$$

**Per-molecule** average translational kinetic energy depends only on temperature:
$$\tfrac{1}{2} m (v^2)_{\text{av}} = \tfrac{3}{2} k T$$
where $k$ is the Boltzmann constant, $k = R/N_A$.

### Molecular Speeds — RMS Speed

$$v_{\text{rms}} = \sqrt{(v^2)_{\text{av}}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}}$$

## Collisions Between Molecules

Model molecules as rigid spheres of radius $r$.

- **Mean free path** $\lambda$: average distance traveled between collisions.
- **Mean free time** $t_{\text{mean}}$: average time between collisions.

In a time $dt$ a molecule of radius $r$ collides with any other molecule in a cylindrical volume of radius $2r$ and length $v\, dt$.

$$\lambda = v\, t_{\text{mean}} = \frac{V}{4\pi \sqrt{2}\, r^2 N}$$

More molecules or larger molecules → shorter mean free path.

## Heat Capacities of Gases

**Degrees of freedom**: number of velocity components needed to describe a molecule.
- Monatomic: 3 degrees of freedom.
- Diatomic: 5 (3 translational + 2 rotational).

**Equipartition of energy**: each degree of freedom has $\tfrac{1}{2}kT$ of kinetic energy.

### Molar heat capacity at constant volume
- Monatomic ideal gas:
$$C_V = \tfrac{3}{2} R$$
- Diatomic ideal gas:
$$C_V = \tfrac{5}{2} R$$

### Compare Theory with Experiment

| Type | Gas | $C_V$ [J/(mol·K)] |
|---|---|---|
| Monatomic | He | 12.47 |
| Monatomic | Ar | 12.47 |
| Diatomic | H$_2$ | 20.42 |
| Diatomic | N$_2$ | 20.76 |
| Diatomic | O$_2$ | 20.85 |
| Diatomic | CO | 20.85 |
| Polyatomic | CO$_2$ | 28.46 |
| Polyatomic | SO$_2$ | 31.39 |
| Polyatomic | H$_2$S | 25.95 |

### Hydrogen $C_V$ vs Temperature
> Figure: Staircase plot — below 50 K only translation ($C_V = 3R/2$); above 50 K rotation adds ($C_V = 5R/2$); above 600 K vibration adds ($C_V \to 7R/2$).

## Heat Capacities of Solids

Monatomic solid: think of $N$ atoms bound by springs. Each atom has average KE $\tfrac{3}{2}kT$ plus average PE $\tfrac{3}{2}kT$ → total $3kT$ per atom.

**Rule of Dulong and Petit**:
$$C_V = 3R$$

### Experimental Observations
- At high $T$, $C_V \to 3R$ for lead, aluminum, silicon, diamond.
- At low $T$, $C_V \ll 3R$ (quantum effects suppress vibrational modes).

## Molecular Speeds — Maxwell–Boltzmann Distribution

**Maxwell–Boltzmann distribution** $f(v)$ gives the distribution of molecular speeds.

As $T$ increases: curve flattens, maximum shifts to higher speeds.
- $v_{\text{mp}}$: **most probable speed** (peak of curve).
- Fraction of molecules with speeds between $v_1$ and $v_2$ = area under curve.

$$f(v) = 4\pi \left(\frac{m}{2\pi kT}\right)^{3/2} v^2 e^{-mv^2/(2kT)}$$

Most probable speed:
$$v_{\text{mp}} = \sqrt{\frac{2kT}{m}} = \sqrt{\frac{2RT}{M}}$$

## Phases of Matter

- Real substances have interactions that condense them to liquid/solid under certain conditions.
- Each phase stable only in certain ranges of $T$ and $p$.
- **Phase equilibrium** between two phases occurs along curves in the $pT$ phase diagram.

### Typical pT Phase Diagram

> Figure: Fusion curve (solid + liquid), vaporization curve (liquid + vapor), sublimation curve (solid + vapor), all meeting at the **triple point**. Vaporization curve ends at the **critical point**. Above critical point, transitions are smooth.

### pVT Surfaces
- A **pVT surface** represents the equation of state as a 3D surface.
- Projections onto the $pT$- and $pV$-planes yield phase diagrams and isotherms.
- For an ideal gas, the pVT surface is smooth and much simpler than for a real substance.

## Example Quiz Questions

1. A 5 L tank at 37 C contains $24.7 \times 10^{-4}$ kg of neon (M = 20.2 g/mol). Find $p$ in kPa.
2. Ideal gas at $p_0$, $V = 1.7$ m$^3$. Pressure changes to $1.8 p_0$, Kelvin $T$ rises by 67%. Find final $V$.
3. Ideal gas from 237 C to 480 C; volume decreases by 47%; initial $p = 74{,}643$ Pa. Find $p_f$ in kPa.
4. Bubble at 19 m in freshwater lake, initial 136 mm$^3$, rises isothermally. Surface $p = 98{,}360$ Pa, water density 1000 kg/m$^3$. Find final volume.
5. Moles in 97 g of C$_2$H$_5$.
6. Mass of one molecule of C$_2$H$_6$OH in kg.
7. Avg translational KE per He atom = $9.2 \times 10^{-21}$ J. Find $T$.
8. Total translational KE of 6.1 mol ideal gas at 90 C.
9. $v_{\text{rms}}$ of molecular oxygen at 17.3 C ($M_\text{atomic O} = 16.0$ g/mol).
10. Given $v_{\text{rms}} = 557$ m/s, $M = 16$ g/mol. Find $T$ in K.
11. Most probable speed of molecular oxygen at 82.7 C.
12. Monatomic solid, atomic mass 56.6 amu. Energy to heat 24 g by 15 C° (Dulong–Petit).
13. Total internal energy of 7.8 mol of H$_2$ (diatomic) at 412 K.
