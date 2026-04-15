# M12 Review — Fluid Mechanics Problems

## Problem 1 — Density Ratio
Object A has 5.7 times the mass and 1.4 times the volume of object B. If $\rho_B = 731~\mathrm{kg/m^3}$, find $\rho_A$.

Use $\rho_A = (m_A/m_B)/(V_A/V_B)\cdot \rho_B = (5.7/1.4)(731)$.

## Problem 2 — Hollow Pipe Weight
A hollow cylindrical iron pipe ($\rho = 7.8\times10^3~\mathrm{kg/m^3}$), length 3.8 m, outside diameter 3.7 cm, inside diameter 2.1 cm. Find weight in lb. ($1~\mathrm{lb} = 4.4482~\mathrm{N}$).

Volume = $\pi L(r_o^2 - r_i^2)$; weight = $\rho V g$; convert to lb.

Materials table: Copper $8.9\times10^3$, Iron $7.8\times10^3$, Lead $11.3\times10^3~\mathrm{kg/m^3}$.

## Problem 3 — Pressure Beneath a Cube
Cube of mass 24 kg and side 29 cm on a smooth flat surface in vacuum; $g = 5.6~\mathrm{m/s^2}$. Pressure on the surface beneath:

$$p = \frac{mg}{A} = \frac{(24)(5.6)}{(0.29)^2}$$

## Problem 4 — Planet X Barometer
Mercury barometer reads $h_1 = 7.5~\mathrm{cm}$ and $h_2 = 60.2~\mathrm{cm}$. Density of Hg $= 13{,}534~\mathrm{kg/m^3}$. $g_X = 7.2~\mathrm{m/s^2}$.

$$p_0 = \rho g (h_2 - h_1)$$

(The height difference gives the ambient pressure.)

## Problem 5 — Freshwater Lake Depth
Depth $d = 6.09~\mathrm{m}$, surface pressure $p_0 = 96{,}872~\mathrm{Pa}$, $\rho = 1000~\mathrm{kg/m^3}$.

$$p = p_0 + \rho g d$$

## Problem 6 — Oil Cylinder with Wood + Potato
Glass cylinder radius 6.3 cm, oil $\rho = 0.81\times10^3~\mathrm{kg/m^3}$. A 2.2-kg wooden disk supports a 0.4-kg potato. Find gauge pressure in psi at 12.1 cm below the oil surface. ($1~\mathrm{psi}=6.895~\mathrm{kPa}$.)

$$p_g = \frac{(m_\mathrm{wood}+m_\mathrm{potato})g}{\pi r^2} + \rho g d$$

## Problem 7 — Hydraulic Jack
Input piston radius 0.28 m, output radius 1.62 m, input force 388 N. Find output force in kN.

$$F_\mathrm{out} = F_\mathrm{in}\frac{A_\mathrm{out}}{A_\mathrm{in}} = F_\mathrm{in}\left(\frac{r_\mathrm{out}}{r_\mathrm{in}}\right)^2$$

## Problem 8 — Hydraulic Press Compressive Stress
Input piston radius 6 cm, output piston radius 24 cm, pressing plate area $9.5~\mathrm{cm^2}$, $F_1 = 246~\mathrm{N}$. Find compressive stress in kPa.

$$F_2 = F_1 (A_2/A_1); \quad p = F_2/A_\mathrm{plate}$$

## Problem 9 — Floating Ball Density
Ball of volume $V = 12~\mathrm{m^3}$ in fluid of $\rho_f = 783~\mathrm{kg/m^3}$. It floats with $V_\mathrm{sub} = 7.9~\mathrm{m^3}$. Find ball density.

$$\rho_o = \rho_f \frac{V_\mathrm{sub}}{V_o}$$

## Problem 10 — Loading a Raft
Raft: $\rho_\mathrm{wood} = 511~\mathrm{kg/m^3}$, dimensions $3.5\times 2.5\times 0.4~\mathrm{m}$, floating in water. How much mass can be added before 83% of volume is submerged?

$$(m_\mathrm{raft}+m_\mathrm{load}) g = \rho_w (0.83 V) g$$

## Problem 11 — Pipe Continuity
Pipe diameter increases 0.26 m → 0.84 m. Narrow speed 6.4 m/s. Wide speed?

$$v_2 = v_1 (d_1/d_2)^2$$

## Problem 12 — Filling a Bathtub
39-gal bathtub, faucet area 1.5 cm², flow 3.5 m/s. Time in minutes.

$$Q = vA, \quad t = V/Q$$

where $V = 39\times 3.785\times10^{-3}~\mathrm{m^3}$.

## Problem 13 — Underground Hot Water Vent
Chamber depth 39 m, $\rho = 1000~\mathrm{kg/m^3}$, chamber pressure 796{,}015 Pa, narrow vent (negligible area) at surface with $p_\mathrm{atm} = 1.01\times10^5~\mathrm{Pa}$. Find vent exit speed.

Use Bernoulli (chamber speed ≈ 0):

$$p_\mathrm{chamber} + 0 + \rho g(-h) = p_\mathrm{atm} + \tfrac{1}{2}\rho v^2 + 0$$

Solve for $v$.

## Problem 14 — Horizontal Pipe Rising
Constant radius pipe carries water horizontally at $p_1 = 177~\mathrm{kPa}$, $v = 3~\mathrm{m/s}$; pipe rises 2.9 m and levels. Find new pressure $p_2$. (Constant radius → $v_2 = v_1$.)

$$p_2 = p_1 - \rho g \Delta y$$

## Problem 15 — Buoyant Force on Aluminum vs. Gold Ball
Two balls of the same radius, one aluminum and one gold, both at the bottom of water. Which has larger buoyant force?

**Answer: The buoyant forces are the same** (same volume ⇒ same displaced water).

## Problem 16 — Venturi Pipe
An ideal liquid flows through a Venturi pipe with area $A_1$ (tube 1, wider) and $A_2$ (tube 2, narrower).

- **Answer 1**: Speed greater at **tube 2** (narrower → faster).
- **Answer 2**: Pressure greater at **tube 1** (wider → slower → higher pressure).

(Note: the worksheet has the wording flipped; the physically correct answers for a Venturi with the narrow section being tube 2 are as above.)
