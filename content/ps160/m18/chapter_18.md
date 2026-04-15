# Chapter 18 — Thermal Properties of Matter

This chapter defines the thermodynamic state variables and their relationships (the equation of state). The system of interest is typically a closed container of gas. Once its properties are defined, we explore its interactions with the surroundings through the first law (Ch. 19) and second law (Ch. 20) of thermodynamics.

---

## 1. Equations of State

The state variables of a thermodynamic system are:

| Symbol | Quantity | Units |
|---|---|---|
| $P$ | pressure | Pa |
| $V$ | volume | m$^3$ |
| $T$ | temperature | K |
| $n$ | number of moles | mol |
| $N$ | number of particles | — |
| $S$ | entropy | J/K |

The mass of the gas is obtained from the number of moles $n$ and the molar mass $M$:

$$\text{mass} = n M$$

Experimentally we observe:

$$P \propto T, \qquad P \propto n, \qquad P \propto \frac{1}{V}$$

These combine to give the **ideal gas law**:

$$\boxed{\, PV = nRT \,}$$

where $R = 8.314 \ \text{J/(mol·K)}$ is the universal gas constant.

### Example Problems

**Ex. 3.** A cylindrical tank with a tight-fitting piston originally contains $0.110\ \text{m}^3$ of air at $0.355$ atm. The piston is slowly pulled out until the volume reaches $0.390\ \text{m}^3$ at constant temperature. Find the final pressure.

**Ex. 9.** A cylindrical tank contains $0.750\ \text{m}^3$ of nitrogen at $27^\circ\text{C}$ and $7.50\times10^3$ Pa. Find the pressure after the volume is decreased to $0.410\ \text{m}^3$ and the temperature is raised to $157^\circ\text{C}$.

### 1.1 The Van Der Waals Equation

$$\left(p + \frac{a n^2}{V^2}\right)(V - nb) = nRT$$

- $a$ and $b$ are empirical constants depending on the gas.
- $b$ represents the volume occupied by one mole of molecules.
- $a$ accounts for attractive intermolecular forces that reduce the pressure.
- When $n/V$ is small, this reduces to the ideal gas law.

### 1.2 pV-Diagrams

If $P$, $V$, and $n$ are known, there is a unique temperature:

$$T = \frac{PV}{nR}$$

Holding $T$ constant and varying $P$ and $V$ traces out a hyperbolic curve on the pV-diagram called an **isotherm**. Higher-temperature isotherms lie farther from the origin ($T_4 > T_3 > T_2 > T_1$).

---

## 2. Molecular Properties of Matter

One mole contains Avogadro's number of particles:

$$N_A = 6.022\times 10^{23} \ \text{molecules/mol}$$

The mass per molecule (or atom) $m$ is:

$$m = \frac{M}{N_A}$$

where $M$ is the molar mass in kg/mol.

**Intermolecular forces.** Force and potential energy vs. separation $r$: at equilibrium separation $r_0$ the potential has its minimum $U_0$ and $F_r = 0$. For $r < r_0$ the force is repulsive; for $r > r_0$ it is attractive.

**Ex. 23 — How close are gas molecules?** At $27^\circ\text{C}$ and $1.00$ atm, imagine the molecules uniformly spaced in touching cubes. Find the edge length, compare to a typical molecular diameter, and compare to interatomic spacing in solids ($\sim 0.3$ nm).

---

## 3. Kinetic-Molecular Model of an Ideal Gas

### Properties of the Ideal Gas

1. The ideal gas consists of particles in random motion obeying Newton's laws.
2. The total number of molecules is "large."
3. The volume occupied by the molecules is a negligibly small fraction of the gas volume.
4. No forces act on a molecule except during collisions with walls or other molecules.
5. All collisions are (i) elastic and (ii) of negligible duration.

### A Molecular View of Pressure

Consider a cubical box of edge $L$. The force exerted on one wall by a single molecule of momentum $p_x = m v_x$ is:

$$F_x = \frac{\Delta p_x}{\Delta t} = \frac{2 m v_x}{2L/v_x} = \frac{m v_x^2}{L}$$

The pressure due to $N$ molecules is:

$$p = \frac{F}{A} = \frac{1}{L^2}\cdot\frac{m v_{1x}^2 + m v_{2x}^2 + \cdots}{L} = \frac{m}{L^3}\left(v_{1x}^2 + v_{2x}^2 + \cdots\right)$$

With mass density $\rho = Nm/L^3$:

$$p = \rho\,\langle v_x^2\rangle_\text{av}$$

Because the motion is isotropic, $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle = \tfrac{1}{3}\langle v^2\rangle$, so:

$$\boxed{\, p = \tfrac{1}{3}\rho \langle v^2\rangle_\text{av} \,}$$

### Root-Mean-Square Velocity

$$v_\text{rms} = \sqrt{\frac{3p}{\rho}}$$

Note that the pressure varies as $p \propto v_\text{rms}^2$.

### Average Translational Kinetic Energy

For $N$ molecules the total translational KE is:

$$K_\text{tot} = \tfrac{1}{2} m v_\text{rms}^2 \cdot N$$

Using $v_\text{rms}^2 = 3p/(Nm/V)$ we get:

$$pV = \tfrac{2}{3} N\left(\tfrac{1}{2} m v_\text{rms}^2\right) = \tfrac{2}{3} N \langle K_\text{trans}\rangle$$

Equating with $pV = nRT$:

$$\boxed{\, \langle K_\text{trans}\rangle = \tfrac{3}{2} k T \,} \qquad\text{(per molecule)}$$

where $k = R/N_A = 1.38\times10^{-23}$ J/K is the **Boltzmann constant**.

Total translational KE of the gas:

$$K_\text{tot} = \tfrac{3}{2} N k T = \tfrac{3}{2} n R T$$

### RMS Speed in Terms of Temperature

$$\boxed{\, v_\text{rms} = \sqrt{\frac{3 k T}{m}} = \sqrt{\frac{3 R T}{M}} \,}$$

### Two Forms of the Equation of State

$$pV = nRT \quad\text{(macroscopic)}\qquad pV = N k T \quad\text{(microscopic)}$$

**Ex. 29.** A deuteron plasma ($^2_1$H) in a fusion reactor is heated to $\sim 300$ million K. Find $v_\text{rms}$ and compare to $c$. Also find the temperature for which $v_\text{rms} = 0.10 c$.

### 3.1 Collisions Between Molecules — Mean Free Path

Modeling molecules as rigid spheres of radius $r$, the **mean free path** between collisions is:

$$\lambda = \frac{V}{4\pi\sqrt{2}\, r^2 N}$$

Using $pV = NkT$:

$$\lambda = \frac{kT}{4\pi\sqrt{2}\, r^2 p}$$

---

## 4. Heat Capacities

Adding heat at **constant volume** increases the kinetic energy of the gas. For a monatomic ideal gas:

$$dK = dQ \;\Rightarrow\; \tfrac{3}{2} n R\, dT = n C_V\, dT$$

So:

$$C_V = \tfrac{3}{2} R \approx 12.47 \ \text{J/(mol·K)} \qquad \text{(monatomic)}$$

**Equipartition theorem.** Each quadratic degree of freedom contributes $\tfrac{1}{2} R$ to $C_V$. For a diatomic gas at ordinary temperatures (three translational + two rotational DOF active):

$$C_V = \tfrac{5}{2} R \approx 20.79 \ \text{J/(mol·K)} \qquad \text{(diatomic)}$$

At very low temperature only translation is active ($C_V = 3R/2$); at high temperature vibrational modes also activate ($C_V \to 7R/2$).

### Table 18.1 — Molar Heat Capacities of Gases

| Type | Gas | $C_V$ [J/(mol·K)] |
|---|---|---|
| Monatomic | He, Ar | 12.47 |
| Diatomic | H$_2$ | 20.42 |
| Diatomic | N$_2$ | 20.76 |
| Diatomic | O$_2$, CO | 20.85 |
| Polyatomic | CO$_2$ | 28.46 |
| Polyatomic | SO$_2$ | 31.39 |
| Polyatomic | H$_2$S | 25.95 |

**Ex. 37.** How much heat is needed to raise 1.80 mol of an ideal gas by 50.0 K at constant volume if it is (a) diatomic, (b) monatomic? Use $dQ = n C_V\, dT$.

---

## 5. Molecular Speeds

For $N$ molecules at temperature $T$, the number of molecules with speed in $[v, v+dv]$ is:

$$dN = N f(v)\, dv$$

where $f(v)$ is the probability density per unit speed.

### 5.1 Maxwell–Boltzmann Speed Distribution

$$\boxed{\, f(v) = 4\pi\left(\frac{m}{2\pi k T}\right)^{3/2} v^2 e^{-mv^2/(2kT)} \,}$$

#### 5.1.1 Most Probable Speed

Set $\partial f/\partial v = 0$ and solve:

$$v_\text{mp} = \sqrt{\frac{2kT}{m}}$$

#### 5.1.2 Average Speed

$$v_\text{av} = \int_0^\infty v\, f(v)\, dv = \sqrt{\frac{8kT}{\pi m}}$$

#### 5.1.3 Root-Mean-Square Speed

$$\langle v^2\rangle_\text{av} = \int_0^\infty v^2\, f(v)\, dv$$

$$v_\text{rms} = \sqrt{\frac{3kT}{m}}$$

Ordering:

$$v_\text{mp} < v_\text{av} < v_\text{rms}$$

**Ex. 41.** For CO$_2$ ($M = 44.0$ g/mol) at $T = 300$ K, find (a) $v_\text{mp}$, (b) $v_\text{av}$, and (c) $v_\text{rms}$.

### Barometric Formula (Isothermal Atmosphere)

$$P(h) = P_0 e^{-mgh/(kT)} = P_0 e^{-Mgh/(RT)}$$

This assumes a constant temperature (usually an approximation).

---

## 6. Phases of Matter

On a $p$–$T$ phase diagram, three curves meet at the **triple point** where solid, liquid, and vapor coexist:

- **Fusion curve** (solid–liquid boundary)
- **Vaporization curve** (liquid–vapor boundary), terminating at the **critical point**
- **Sublimation curve** (solid–vapor boundary)

Beyond the critical point, liquid and gas phases merge into a **supercritical fluid** with no distinct liquid/vapor phase transition. A supercritical fluid can effuse through solids like a gas and dissolve materials like a liquid.
