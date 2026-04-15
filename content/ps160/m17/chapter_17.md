# Chapter 17: Temperature and Heat

## 1. Temperature and Thermal Equilibrium

When objects are "hot" or "cold", we need a quantifiable, reproducible scientific way to express this. First we must establish **thermal equilibrium**.

When two systems are placed in contact through a **diathermic wall**, heat energy can pass through, causing the properties of both systems to change. When all measured properties approach constant values, the two systems are in **thermal equilibrium**.

### Zeroth Law of Thermodynamics

> If systems $A$ and $B$ are each in thermal equilibrium with a third system $C$, then $A$ and $B$ are in thermal equilibrium with each other.

System $C$ plays the role of a thermometer. Stated in terms of temperature:

> There exists a scalar quantity called **temperature**, which is a property of all thermodynamic systems in equilibrium. Two systems are in thermal equilibrium if and only if their temperatures are equal.

## 2. Thermometers and Temperature Scales

Historically, the Fahrenheit and Celsius scales were practical conventions without deep physical meaning. Physics adopts the **Kelvin scale**, where **absolute zero** is zero on the scale. Kelvin increments match Celsius degree sizes.

### Triple Point of Water

Thermometers are calibrated using the **triple point of water**, where ice, water, and water vapor coexist at atmospheric pressure. The vapor pressure of water at 0.01 C is 610 Pa. The triple point is defined exactly as:
$$T_{\text{tr}} = 273.16~\text{K}$$

> Figure: Phase diagram of water showing the solid, liquid, vapor regions, with triple point at ~0.01 C, 0.61 kPa; melting point $T_m$ and boiling point $T_b$ at 101.3 kPa; critical point near 374 C, 22100 kPa.

### Celsius and Fahrenheit

Celsius: water boils at 100 C, freezes at 0 C. Relation to Kelvin:
$$T_C = T - 273.15$$

Fahrenheit: water boils at 212 F, freezes at 32 F. Relation to Celsius:
$$T_F = \frac{9}{5} T_C + 32$$

The interval between the two scales: 9 F° = 5 C°.

**Ex. 8**: Convert to Celsius and Fahrenheit: (a) midday lunar surface (400 K); (b) top of Saturn clouds (95 K); (c) Sun's core ($1.55 \times 10^7$ K).

## 3. Gas Thermometers and the Kelvin Scale

Any temperature-dependent property $X$ of a substance can form the basis of a thermometer. In general, calibrating to the triple point:
$$T(X) = (273.16~\text{K}) \frac{X}{X_{\text{tr}}}$$

The most suitable thermometric property is the pressure $p$ of a fixed volume of gas (a **constant-volume gas thermometer**). The **ideal gas temperature scale**:
$$T = (273.16~\text{K}) \frac{p}{p_{\text{tr}}} \qquad (\text{constant } V)$$

**Ex. 7**: Gas at triple point has $p = 1.35$ atm. What is its pressure when CO$_2$ solidifies at $T = 195$ K?

## 4. Thermal Expansion

### Linear Expansion

$$\Delta L = \alpha L \Delta T$$
where $\alpha$ is the **coefficient of linear expansion**, defined by:
$$\alpha = \frac{\Delta L / L}{\Delta T}, \quad [\alpha] = (\text{C}^\circ)^{-1}$$

### Area and Volume (isotropic solid)

$$\Delta A = 2\alpha A \Delta T$$
$$\Delta V = 3\alpha V \Delta T$$

Derivation for area: $A = ab$, $A' = (a + \Delta a)(b + \Delta b)$, so
$$\Delta A = a\Delta b + b\Delta a + \Delta a \Delta b$$
$$\frac{\Delta A}{A} = \frac{\Delta a}{a} + \frac{\Delta b}{b} + \text{(very small)} \approx \alpha\Delta T + \alpha\Delta T = 2\alpha\Delta T$$

### Fluids: Volume Expansion

For fluids:
$$\Delta V = \beta V \Delta T$$
where $\beta$ is the **coefficient of volume expansion**. For ideal gases, $\beta = 1/T$ (with $T$ in Kelvin).

### Table 17.1: Coefficients of Linear Expansion
| Material | $\alpha$ [K$^{-1}$] |
|---|---|
| Aluminum | $2.4 \times 10^{-5}$ |
| Brass | $2.0 \times 10^{-5}$ |
| Copper | $1.7 \times 10^{-5}$ |
| Glass | $0.4 - 0.9 \times 10^{-5}$ |
| Invar | $0.09 \times 10^{-5}$ |
| Quartz (fused) | $0.04 \times 10^{-5}$ |
| Steel | $1.2 \times 10^{-5}$ |

### Table 17.2: Coefficients of Volume Expansion
Solids (typical $\beta \approx 3\alpha$); liquids much larger:
- Ethanol: $75 \times 10^{-5}$
- Carbon disulfide: $115 \times 10^{-5}$
- Glycerin: $49 \times 10^{-5}$
- Mercury: $18 \times 10^{-5}$

**Ex. 14 (Tight Fit)**: Aluminum rivets slightly larger than holes are cooled with dry ice (−78 C) before driving. Hole diameter at 23 C is 4.500 mm — find rivet diameter needed.

### 4.1 Thermal Expansion of Water

Water has anomalous behavior: between 0 C and ~4 C, volume *decreases* with rising temperature (density maximum at 4 C).

> Figure: V vs T curve showing minimum near 4 C.

### 4.2 Thermal Stress

Combining thermal strain and elastic (tensile) strain:
$$\left(\frac{\Delta L}{L_0}\right)_{\text{thermal}} = \alpha \Delta T, \quad \left(\frac{\Delta L}{L_0}\right)_{\text{tension}} = \frac{F}{AY}$$

For a rod held at constant length, total strain = 0, so:
$$\frac{F}{A} = -Y \alpha \Delta T$$

**Ex. 22**: Brass rod 185 cm long, 1.60 cm diameter. Force to prevent contraction when cooled from 120 C to 10 C. (Answer: $\approx 4 \times 10^4$ N.)

## 5. Quantity of Heat

**Heat capacity** $C$:
$$C = \frac{Q}{\Delta T}$$

**Specific heat** (per unit mass):
$$c = \frac{C}{m} = \frac{Q}{m \Delta T}$$

Units: J/(kg·K) for specific heat, J/(mol·K) for molar heat capacity.

Conversions:
- $1~\text{cal} = 4.186$ J
- $1~\text{kcal} = 4186$ J
- $1~\text{Btu} = 778~\text{ft·lbf} = 252~\text{cal} = 1055$ J

For mass form:
$$Q = m c \Delta T$$

For moles:
$$Q = n M c \Delta T = n C \Delta T$$
where $C$ is molar specific heat in J/(mol·K).

### Table 17.3: Specific Heats and Molar Heat Capacities
(See table from lecture outline; water: $c = 4190$ J/(kg·K), $C = 75.4$ J/(mol·K).)

**Ex. 31**: Worker drops a 1.00-L water bottle from 225 m. If mechanical energy loss heats the water, find $\Delta T$.

## 6. Calorimetry and Phase Changes

### Method of Mixtures

When different materials in thermal contact exchange heat until equilibrium:
$$Q_1 + Q_2 + Q_3 = 0 \qquad (\text{conservation of energy})$$

**Ex. 35**: 500-g metal from boiling water dropped into 1.00 kg water at 20.0 C in a Styrofoam beaker; equilibrium at 22.0 C. Find specific heat of metal, compare heat storage vs water, consider effect of non-negligible Styrofoam absorption.

### Heats of Transformation (Latent Heat)

When phase changes occur (solid↔liquid, liquid↔gas), heat flows without changing temperature. Total heat:
$$Q = m L$$
where $L_f$ = **latent heat of fusion** (solid↔liquid), $L_v$ = **latent heat of vaporization** (liquid↔gas).

### Table 17.4: Heats of Fusion and Vaporization (selected)
| Substance | Melting (C) | $L_f$ (J/kg) | Boiling (C) | $L_v$ (J/kg) |
|---|---|---|---|---|
| Water | 0.00 | $334 \times 10^3$ | 100.00 | $2256 \times 10^3$ |
| Ethanol | −114 | $104.2 \times 10^3$ | 78 | $854 \times 10^3$ |
| Mercury | −39 | $11.8 \times 10^3$ | 357 | $272 \times 10^3$ |
| Lead | 327.3 | $24.5 \times 10^3$ | 1750 | $871 \times 10^3$ |
| Silver | 960.80 | $88.3 \times 10^3$ | 2193 | $2336 \times 10^3$ |
| Copper | 1083 | $134 \times 10^3$ | 1187 | $5069 \times 10^3$ |

> Figure: T vs time for adding heat to ice: a→b (ice warms), b→c (ice melts at 0 C), c→d (water warms), d→e (water boils at 100 C), e→f (steam warms).

**Ex. 45**: Initial speed of a lead bullet at 25 C so that rest-heat melts it (no losses).

**Ex. 52**: 4.00 kg silver ingot at 750 C placed on ice at 0 C. How much ice melts?

## 7. Mechanisms of Heat Transfer

Three mechanisms: **conduction**, **convection**, **radiation**.

### Thermal Conduction

Rate of heat flow through a slab of thickness $\Delta x$ and area $A$ with temperature difference $\Delta T$:
$$H = \frac{Q}{\Delta t} = k A \frac{\Delta T}{\Delta x}$$
where $k$ is **thermal conductivity** [W/(m·K)]. For a rod of length $L$:
$$H = k A \frac{T_H - T_L}{L} \qquad (\text{macroscopic, steady state})$$

Or differential form:
$$H = -k A \frac{dT}{dx} \qquad (\text{microscopic, steady state})$$

The $dT/dx$ is the **temperature gradient** (intrinsically negative since heat flows toward lower $T$).

**Thermal resistance** or $R$-value:
$$R = \frac{L}{k}$$

For series (stacked) layers, $R$ values add: $R_{\text{total}} = \sum R_i$, and
$$H = \frac{A(T_H - T_C)}{R_{\text{total}}}$$

### Table 17.5: Thermal Conductivities (W/m·K)
| Substance | $k$ |
|---|---|
| Aluminum | 205 |
| Brass | 109 |
| Copper | 385 |
| Lead | 34.7 |
| Silver | 406 |
| Steel | 50.2 |
| Brick (red) | 0.6 |
| Brick (insulating) | 0.15 |
| Concrete | 0.8 |
| Glass | 0.8 |
| Ice | 1.6 |
| Fiberglass / felt / cork / rockwool | 0.04 |
| Styrofoam | 0.01 |
| Wood | 0.04 – 0.12 |
| Air | 0.024 |
| Helium / Hydrogen | 0.14 |

**Ex. 56**: Insulated metal rod 60.0 cm long, $A = 1.25$ cm$^2$, ends at 100 C and 0 C. 8.50 g of ice melt in 10.0 min. Find $k$.

### Convection

Heat transfer by bulk fluid motion. Warm fluid is less dense, rises via buoyancy. **Convection needs gravity** — no convection in orbit.

### Radiation

Heat transfer via electromagnetic waves (needs no medium). Rate:
$$H = \frac{dQ}{dt} = e A \sigma T^4$$
where $e$ is emissivity, $A$ is area, and $\sigma$ is the **Stefan–Boltzmann constant**:
$$\sigma = 5.67 \times 10^{-8}~\frac{\text{W}}{\text{m}^2\cdot\text{K}^4}$$

With derivation from statistical mechanics:
$$\sigma = \frac{2\pi^5 k^4}{15 c^2 h^3}$$

Net radiation to surroundings at $T_s$:
$$H_{\text{net}} = e A \sigma (T^4 - T_s^4)$$

**Ex. 106**: Solar constant 1.50 kW/m$^2$ at Earth ($1.50 \times 10^{11}$ m away, solar radius $6.96 \times 10^8$ m). (a) Rate of radiation per unit area at sun's surface; (b) blackbody equivalent temperature.

### Climate Change Note
Atmospheric CO$_2$ has risen >33% above pre-industrial, driving global average temperatures to rise ~0.18 C° per decade over the past 50 years.
