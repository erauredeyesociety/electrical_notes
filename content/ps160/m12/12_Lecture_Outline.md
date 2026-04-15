# Chapter 12 / 14: Fluid Mechanics — Lecture Outline

## Molecular Model of Gases and Liquids (Model 14.1)

Gases and liquids are **fluids** — they flow and exert pressure.

**Gases**
- Molecules move freely through space.
- Molecules interact only via occasional collisions with each other or walls.
- Molecules far apart, so a gas is **compressible**.
- A gas fills its container.

**Liquids**
- Molecules weakly bound, stay close together.
- **Incompressible** — molecules can't get any closer.
- Weak bonds allow molecules to move around.
- A liquid has a surface.

## Volume

An important macroscopic parameter is volume $V$. SI unit: $\mathrm{m^3}$.

Unit conversions:
- $1~\mathrm{m^3} = 1000~\mathrm{L}$
- $1~\mathrm{L} = 1000~\mathrm{cm^3}$
- $1~\mathrm{m^3} = 10^6~\mathrm{cm^3}$

## Density

**Mass density** is the ratio of an object's mass to its volume:

$$\rho = \frac{m}{V} \quad \text{(mass density)}$$

SI units: $\mathrm{kg/m^3}$.

Density characterizes the substance itself, not particular pieces.

### Densities of Various Fluids (at 0°C, 1 atm)

| Substance    | $\rho~(\mathrm{kg/m^3})$ |
|--------------|:------------------------:|
| Helium gas   | 0.18                     |
| Air          | 1.29                     |
| Gasoline     | 680                      |
| Ethyl alcohol| 790                      |
| Benzene      | 880                      |
| Oil (typical)| 900                      |
| Water        | 1000                     |
| Seawater     | 1030                     |
| Glycerin     | 1260                     |
| Mercury      | 13,600                   |

### Example 14.1 — Weighing the air

A living room of dimensions $4.0 \times 6.0 \times 2.5~\mathrm{m}$ has volume $V = 60~\mathrm{m^3}$. Air density $\rho = 1.29~\mathrm{kg/m^3}$, so

$$m = \rho V = (1.29)(60) = 77~\mathrm{kg}$$

## Pressure

**Pressure** is the ratio of force exerted on a surface to its area:

$$p = \frac{F}{A}$$

- SI unit: $\mathrm{Pa} = \mathrm{N/m^2}$.
- Pressure exists *everywhere* in a fluid.
- Pressure at a point is the same in all directions (up, down, sideways).
- In a liquid, pressure increases with depth; in a gas (lab scale), pressure is nearly uniform.

Two contributions to fluid pressure:
1. **Gravitational** — gravity pulls down on the liquid/gas.
2. **Thermal** — collisions of freely moving gas molecules; depends on temperature.

## Atmospheric Pressure

Global average sea-level pressure defines the standard atmosphere:

$$1~\mathrm{atm} \equiv 101{,}300~\mathrm{Pa} = 101.3~\mathrm{kPa}$$

Density and pressure decrease with height; air's density and pressure are greatest at Earth's surface.

Although atmospheric pressure on your outstretched arm is $\sim 2000~\mathrm{N}$ (450 lb), you can lift your arm because fluids push in all directions — net force is near zero.

## Pressure in Liquids (Hydrostatic Pressure)

For a liquid column of depth $d$, density $\rho$, with surface pressure $p_0$:

$$\boxed{p = p_0 + \rho g d} \quad \text{(hydrostatic pressure at depth } d\text{)}$$

### Example 14.3 — Pressure on a submarine (depth 300 m)

$$p = 1.013\times10^5 + (1030)(9.80)(300) = 3.13\times10^6~\mathrm{Pa} \approx 30.9~\mathrm{atm}$$

### Key fact
A connected liquid in hydrostatic equilibrium rises to the same height in all *open* regions. Pressure is the same at all points on any horizontal line through a connected fluid — regardless of container shape.

### Example 14.4 — Closed tube
Water fills a tube open on one side (height 100 cm) and sealed on the other (height 40 cm, closed at top). The pressure at the top of the closed tube is found using the horizontal-line rule: at depth 60 cm in the open tube, $p = p_0 + \rho g d = 1.072\times10^5~\mathrm{Pa} = 1.06~\mathrm{atm}$.

## Tactics Box 14.1: Hydrostatics

1. **Draw a picture.** Show surfaces, pistons, boundaries. Include heights, areas, densities.
2. **Determine pressure at surfaces.**
   - Open to air: $p_0 = p_\mathrm{atmos}$ (usually 1 atm).
   - Covered by gas: $p_0 = p_\mathrm{gas}$.
   - Closed surface: $p = F/A$.
3. **Use horizontal lines.** Pressure is constant along a horizontal line in a connected fluid.
4. **Allow for gauge pressure.** $p_g = p - 1~\mathrm{atm}$.
5. **Apply hydrostatic equation.** $p = p_0 + \rho g d$.

## Gauge Pressure

$$p_g = p - 1~\mathrm{atm}$$

Tire gauges and air-tank gauges read gauge (not absolute) pressure.

## Manometers

A **manometer** is a U-tube connected to a gas at one end and open to air at the other, filled with a liquid of density $\rho$. Using $p_1 = p_2$:

$$p_\mathrm{gas} = 1~\mathrm{atm} + \rho g h$$

## Barometers

A sealed tube inverted in a container of liquid reads atmospheric pressure:

$$p_\mathrm{atmos} = \rho g h$$

### Pressure Units (Table 14.2)

| Unit            | Abbrev.  | Conversion to 1 atm | Uses                         |
|-----------------|----------|---------------------|------------------------------|
| pascal          | Pa       | 101.3 kPa           | SI: $1~\mathrm{Pa}=1~\mathrm{N/m^2}$ |
| atmosphere      | atm      | 1 atm               | general                      |
| mm of mercury   | mm Hg    | 760 mm Hg           | gases, barometric            |
| inches of Hg    | in       | 29.92 in            | U.S. weather                 |
| pounds/sq. inch | psi      | 14.7 psi            | engineering, industry        |

## Blood Pressure

- **Systolic** = peak (heart contracting), first number in reading (~120 mm Hg).
- **Diastolic** = base pressure, second number (~80 mm Hg).

## Hydraulic Lift (Pascal's Principle)

A car rests on piston 2 of area $A_2$. Input force $F_1$ on piston 1 of area $A_1$. Static equilibrium (with height difference $h$):

$$F_2 = \frac{A_2}{A_1} F_1 - \rho g h A_2$$

Because the fluid is incompressible, $A_1 d_1 = A_2 d_2$, so the output travels:

$$d_2 = \frac{d_1}{A_2/A_1}$$

Small force + large distance → large force + small distance.

### Example 14.7 — Lifting a car
Car on a 25-cm-diameter piston ($A_2$), compressed-air piston of 6.0 cm diameter ($A_1$), oil density 900 kg/m³, car mass 1300 kg at $h = 2.0~\mathrm{m}$:

$$F_1 = \frac{A_1}{A_2}F_2 + \rho g h A_1 = 782~\mathrm{N}$$

Gauge pressure reading: $p = F_1/A_1 \approx 276~\mathrm{kPa} \approx 2.7~\mathrm{atm}$.

## Buoyancy

Because pressure increases with depth, the upward force on a submerged body's bottom exceeds the downward force on its top:

$$\vec{F}_\mathrm{net} = \vec{F}_\mathrm{up} - \vec{F}_\mathrm{down} = \vec{F}_B$$

**The buoyant force on an object equals the buoyant force on the fluid it displaces.**

### Archimedes' Principle

A fluid exerts an upward buoyant force $\vec{F}_B$ on an object immersed in or floating on it. The magnitude equals the weight of the displaced fluid:

$$\boxed{F_B = \rho_f V_f g}$$

where $\rho_f$ is the fluid density and $V_f$ is the volume of fluid displaced.

### Sink / Float / Neutral Buoyancy

| Condition       | Relation            | Outcome         |
|-----------------|---------------------|-----------------|
| $\rho_\mathrm{avg} > \rho_f$ | $F_B < m_o g$  | Sinks           |
| $\rho_\mathrm{avg} < \rho_f$ | $F_B > m_o g$  | Floats          |
| $\rho_\mathrm{avg} = \rho_f$ | $F_B = m_o g$  | Neutrally buoyant |

### Example 14.8 — Holding wood underwater

A 10 cm cube of wood ($\rho_o = 700~\mathrm{kg/m^3}$) held underwater by a string tied to the bottom. Equilibrium: $T = F_B - m_o g = (\rho_f - \rho_o)V_o g$.

$$T = (1000 - 700)(10^{-3})(9.8) = 2.9~\mathrm{N}$$

### Floating Object

$$F_B = \rho_f V_f g = m_o g = \rho_o V_o g \implies V_f = \frac{\rho_o}{\rho_f}V_o < V_o$$

**Iceberg example:** fresh-water ice $\rho = 917~\mathrm{kg/m^3}$, seawater $\rho = 1030~\mathrm{kg/m^3}$, so $V_f = 0.89 V_o$ — about 90% of an iceberg is underwater.

### Boats

Minimum side-wall height for a boat of area $A$ and mass $m_o$:

$$h_\mathrm{min} = \frac{m_o}{\rho_f A}$$

## Fluid Dynamics — Ideal-Fluid Model

Three assumptions:
1. **Incompressible** — like liquid, not gas.
2. **Nonviscous** — like water, not syrup.
3. **Steady flow** — laminar, not turbulent.

Each smoke trail in a wind tunnel represents a **streamline**.

## Equation of Continuity

For an incompressible fluid in a flow tube:

$$\boxed{v_1 A_1 = v_2 A_2}$$

The **volume flow rate** is:

$$Q = vA \quad (\mathrm{m^3/s})$$

Narrower sections → faster flow.

## Bernoulli's Equation

Along a streamline in an ideal fluid:

$$\boxed{p_1 + \tfrac{1}{2}\rho v_1^2 + \rho g y_1 = p_2 + \tfrac{1}{2}\rho v_2^2 + \rho g y_2}$$

Or equivalently:

$$p + \tfrac{1}{2}\rho v^2 + \rho g y = \text{constant}$$

This is the conservation of energy for a flowing fluid.

### Example 14.11 — Irrigation system

Water at $v_1 = 5.0~\mathrm{m/s}$, $p_1 = 75~\mathrm{kPa}$ (gauge) in a 6.0-cm-diameter pipe. Upper pipe is 4.0 cm diameter, 2.0 m higher.

By continuity: $v_2 = (r_1/r_2)^2 v_1 = (3/2)^2(5.0) = 11.25~\mathrm{m/s}$.

By Bernoulli: $p_2 = p_1 + \tfrac{1}{2}\rho(v_1^2 - v_2^2) + \rho g(y_1 - y_2)$.
Plugging in: $p_2 \approx 105{,}900~\mathrm{Pa}$ (absolute), so the gauge reads $\approx 4.6~\mathrm{kPa}$.

Reducing pipe size decreases pressure (higher $v$); gaining elevation also decreases pressure.

## Venturi Tubes

Measure gas speeds via a U-tube of height $h$:

$$v_1 = A_2 \sqrt{\frac{2\rho_\mathrm{liq}\,g\,h}{\rho(A_1^2 - A_2^2)}}, \quad v_2 = A_1 \sqrt{\frac{2\rho_\mathrm{liq}\,g\,h}{\rho(A_1^2 - A_2^2)}}$$

## Lift on a Wing

Airflow over the top of a wing is compressed/faster → lower pressure on top. The pressure difference exerts an upward **lift** force:

$$p_\mathrm{top} < p_\mathrm{atmos} \approx p_\mathrm{bottom} \implies \vec{F}_\mathrm{lift} \text{ upward}$$

## Chapter Summary

### General Principles
- **Gases**: freely moving particles, compressible, pressure is primarily thermal, nearly constant in lab-size container.
- **Liquids**: loosely bound particles, incompressible, pressure is primarily gravitational, $p = p_0 + \rho g d$.
- **Ideal-fluid model**: incompressible, nonviscous, laminar.
- **Continuity**: $v_1 A_1 = v_2 A_2$.
- **Bernoulli**: $p_1 + \tfrac{1}{2}\rho v_1^2 + \rho g y_1 = p_2 + \tfrac{1}{2}\rho v_2^2 + \rho g y_2$ — conservation of energy.

### Important Concepts
- Density $\rho = m/V$.
- Pressure $p = F/A$, exists at all points, pushes equally in all directions, constant along a horizontal line.
- Gauge pressure $p_g = p - 1~\mathrm{atm}$.

### Applications — Buoyancy

**Archimedes' principle**: $F_B = \rho_f V_f g$.

| State             | Condition                      |
|-------------------|--------------------------------|
| Sink              | $\rho_\mathrm{avg} > \rho_f$; $F_B < m_o g$ |
| Rise to surface   | $\rho_\mathrm{avg} < \rho_f$; $F_B > m_o g$ |
| Neutrally buoyant | $\rho_\mathrm{avg} = \rho_f$; $F_B = m_o g$ |
