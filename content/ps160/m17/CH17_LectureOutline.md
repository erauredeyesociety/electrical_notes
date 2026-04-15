# Chapter 17: Temperature and Heat — Lecture Outline

## Learning Outcomes

In this chapter, you'll learn:
- The meaning of **thermal equilibrium**, and what thermometers really measure.
- The physics behind the **absolute** (Kelvin) temperature scale.
- How the dimensions of an object change as a result of a temperature change.
- How to do calculations that involve heat flow, temperature changes, and changes of phase.
- How heat is transferred by **conduction**, **convection**, and **radiation**.

## Introduction

- Does molten iron at 1500 C contain heat? The terms **temperature** and **heat** have very different meanings despite common interchangeable usage.
- This chapter focuses on **macroscopic** objects (next chapter handles **microscopic** scale).

## Temperature and Thermal Equilibrium

- A **thermometer** measures **temperature**. E.g., the volume of liquid in a thermometer changes with temperature.
- Two systems are in **thermal equilibrium** if and only if they have the same temperature.
- Other thermometer types: temporal artery thermometers measure infrared radiation from the skin.

## Zeroth Law of Thermodynamics

If system $C$ is initially in thermal equilibrium with both $A$ and $B$, then $A$ and $B$ are in thermal equilibrium with each other.

> Figure: Two systems $A$ and $B$ separated by insulator, each in thermal contact with system $C$; when $A$ and $B$ equilibrate with $C$, they equilibrate with each other.

## Temperature Scales

- **Celsius (centigrade)**: 0 C is freezing point of pure water; 100 C is its boiling point.
- **Fahrenheit**: 32 F is freezing; 212 F is boiling.

Conversions:
$$T_F = \tfrac{9}{5} T_C + 32^\circ$$
$$T_C = \tfrac{5}{9}(T_F - 32^\circ)$$

### Absolute Zero and the Kelvin Scale

- At $-273.15$ C, the absolute pressure of any gas would extrapolate to zero.
- **Kelvin (absolute) scale**: 0 K is the extrapolated temperature at which a gas exerts no pressure.
$$T_K = T_C + 273.15$$
- Note: temperatures are measured in *kelvins*, not "degrees kelvin".

### Comparison Table
| Event | K | C | F |
|---|---|---|---|
| Water boils | 373 | 100° | 212° |
| Water freezes | 273 | 0° | 32° |
| CO$_2$ solidifies | 195 | −79° | −109° |
| Oxygen liquefies | 90 | −183° | −297° |
| Absolute zero | 0 | −273° | −460° |

## Thermal Expansion

### Linear Thermal Expansion

For moderate temperature changes, the change in length of a rod is:
$$\Delta L = \alpha L_0 \Delta T$$
where $\alpha$ is the **coefficient of linear expansion**, $L_0$ is the original length, and $\Delta T$ is the temperature change.

### Molecular Basis
- Model atoms as connected by springs. When temperature rises, average interatomic distance increases because the interatomic potential $U(x)$ is asymmetric — larger energy excursions push the average distance outward.
- Every dimension increases as atoms separate.

### Volume Expansion

For an object with hole: the hole **expands** with the object, it does not shrink.
$$\Delta V = \beta V_0 \Delta T$$
where $\beta$ is the **coefficient of volume expansion**. For isotropic solids: $\beta = 3\alpha$.

### Table 17.1 — Coefficients of Linear Expansion
| Material | $\alpha$ [K$^{-1}$] |
|---|---|
| Aluminum | $2.4 \times 10^{-5}$ |
| Brass | $2.0 \times 10^{-5}$ |
| Copper | $1.7 \times 10^{-5}$ |
| Glass | $0.4 - 0.9 \times 10^{-5}$ |
| Invar | $0.09 \times 10^{-5}$ |
| Quartz (fused) | $0.04 \times 10^{-5}$ |
| Steel | $1.2 \times 10^{-5}$ |

### Table 17.2 — Coefficients of Volume Expansion (Solids)
| Material | $\beta$ [K$^{-1}$] |
|---|---|
| Aluminum | $7.2 \times 10^{-5}$ |
| Brass | $6.0 \times 10^{-5}$ |
| Copper | $5.1 \times 10^{-5}$ |
| Glass | $1.2 - 2.7 \times 10^{-5}$ |
| Invar | $0.27 \times 10^{-5}$ |
| Quartz (fused) | $0.12 \times 10^{-5}$ |
| Steel | $3.6 \times 10^{-5}$ |

### Thermal Expansion of Water (Anomalous)
- Between 0 C and 4 C, water **decreases** in volume with increasing temperature. Water is most dense at 4 C.
- This is why lakes freeze from the top down.

### Thermal Stress

If a rod's temperature changes but it is prevented from expanding/contracting, thermal stress develops:
$$\frac{F}{A} = -Y \alpha \Delta T$$
where $Y$ is Young's modulus, $A$ is cross-sectional area, and $\alpha$ is the coefficient of linear expansion.

- Expansion joints on bridges accommodate these length changes.

## Quantity of Heat

- James Joule (1818–1889) showed water can be warmed by doing mechanical work (paddle-wheel stirring) — same warming as direct heating.
- **Calorie** (cal): heat required to raise 1 gram of water from 14.5 C to 15.5 C.

### Specific Heat

Heat $Q$ required to change temperature of mass $m$ by $\Delta T$:
$$Q = m c \Delta T$$
- **Specific heat** $c$ depends on material.
- For water: $c \approx 4190~\text{J/(kg·K)}$.

### Molar Heat Capacity

$$Q = n C \Delta T$$
- **Molar heat capacity** $C$ depends on material.
- For water: $C \approx 75.4~\text{J/(mol·K)}$.

### Table 17.3 — Specific Heats and Molar Heat Capacities
| Substance | $c$ [J/(kg·K)] | $M$ [kg/mol] | $C$ [J/(mol·K)] |
|---|---|---|---|
| Aluminum | 910 | 0.0270 | 24.6 |
| Beryllium | 1970 | 0.00901 | 17.7 |
| Copper | 390 | 0.0635 | 24.8 |
| Ethanol | 2428 | 0.0461 | 111.9 |
| Ethylene glycol | 2386 | 0.0620 | 148.0 |
| Ice (near 0 C) | 2100 | 0.0180 | 37.8 |
| Iron | 470 | 0.0559 | 26.3 |
| Lead | 130 | 0.207 | 26.9 |
| Marble (CaCO$_3$) | 879 | 0.100 | 87.9 |
| Mercury | 138 | 0.201 | 27.7 |
| Salt (NaCl) | 879 | 0.0585 | 51.4 |
| Silver | 234 | 0.108 | 25.3 |
| Water (liquid) | 4190 | 0.0180 | 75.4 |

## Phase Changes

- **Phases** (states) of matter: solid, liquid, gas.
- Temperature does **not** change during a phase change.
- **Latent heat** $L$: heat per unit mass transferred in a phase change.

$$Q = \pm m L$$
(+ if heat enters the material, − if heat leaves.)

### Heat Added to Ice at Constant Rate
> Figure: Temperature vs time as heat is added. Flat segments at 0 C (ice to liquid, $Q = +mL_f$) and 100 C (liquid to steam, $Q = +mL_v$); sloped segments during ice/water/steam warming where $Q = mc\Delta T$.

### Heat of Fusion
- Example: gallium melts at 29.8 C with $L_f = 8.04 \times 10^4$ J/kg.

### Heat of Vaporization
- Water evaporating from skin removes the heat of vaporization from the body — feels cold out of a pool.

## Mechanisms of Heat Transfer

In nature, energy flows from higher-temperature to lower-temperature objects.

Three mechanisms:
- **Conduction** — within an object or between two in contact.
- **Convection** — depends on mass motion of a fluid.
- **Radiation** — via electromagnetic waves; no intervening matter needed.

### Conduction of Heat

Consider a rod of cross-section $A$, length $L$, ends at $T_H$ and $T_C$. The **heat current** (rate of heat flow):
$$H = \frac{dQ}{dt} = k A \frac{T_H - T_C}{L}$$
where $k$ is the **thermal conductivity**.

R-value: for multi-layer walls, the effective $R$ is the sum of individual $R$ values. $H = \frac{A}{R}(T_H - T_C)$.

#### Thermal Conductivities of Common Substances
| Substance | $k$ [W/(m·K)] |
|---|---|
| Silver | 406 |
| Copper | 385 |
| Aluminum | 205 |
| Wood | 0.04 – 0.12 |
| Concrete | 0.8 |
| Fiberglass | 0.04 |
| Styrofoam | 0.027 |

### Convection of Heat
- **Convection** is transfer of heat by mass motion of a fluid (e.g., heated water rising producing free-convection patterns).

### Radiation of Heat
- Transfer of heat by electromagnetic waves (visible, infrared, etc.).
- **Stefan–Boltzmann law** — heat current in radiation:
$$H = A e \sigma T^4$$
where $A$ is the emitting surface area, $e$ is the **emissivity**, $\sigma$ is the Stefan–Boltzmann constant, and $T$ is absolute temperature.

Net radiation to surroundings at temperature $T_s$:
$$H_{\text{net}} = A e \sigma (T^4 - T_s^4)$$

### Radiation and Climate Change
- Earth's surface radiates mostly infrared.
- CO$_2$ in the atmosphere absorbs some of this IR and reradiates it back — increasing atmospheric CO$_2$ from fossil fuels is driving global temperature rise.

## Example Quiz Questions

1. Given $T = 322$ K, convert to degrees Fahrenheit.
2. A 10.9 m bar's length increases by 0.025 m when heated from 9 C to 56 C — find $\alpha$.
3. A metal with $\alpha = 2.5 \times 10^{-5}$ (C°)$^{-1}$; a 1.9 m pipe. Find $\Delta T$ if $\Delta L = 3.3$ mm.
4. Glass beaker ($\alpha_{\text{lin}} = 1.6 \times 10^{-5}$) filled to 110 cm$^3$ with liquid ($\beta = 3.9 \times 10^{-4}$). Warmed by 23 C°. Find overflow volume in mm$^3$.
5. A 7.2 L water bottle falls 245.1 m; all mechanical energy heats water. Find $\Delta T$.
6. Mass 2 kg, $c = 434$ J/(kg·C°); find $Q$ (kJ) to raise by 17 C°.
7. 2017 J into 1.6 kg block with $c = 447$ J/(kg·C°); find $\Delta T$.
8. 4.5 kg chloroform at 21.8 C into 10.5 kg propylene glycol at 40.4 C; $c_{\text{prop}} = 2500$, $c_{\text{chloro}} = 1050$ J/(kg·K). Find equilibrium $T$.
9. Energy to convert 1.92 kg ice at −12 C to water at 24 C. ($c_{\text{ice}} = 2100$, $c_{\text{water}} = 4190$, $L_{f,\text{water}} = 334 \times 10^3$.)
10. Energy in MJ to turn 5.5 kg ice at 0 C to steam at 100 C. ($L_f = 335{,}000$, $L_v = 2{,}260{,}000$, $c = 4190$.)
11. Wall: 10 cm brick ($k = 0.3$), 2 cm drywall ($k = 0.01$); 10 m$^2$; outside −5 C, inside 21 C. Find rate of heat loss.
12. Ball, radius 1.8 m, emissivity 0.67, surface 105 C, room 26 C. Find net radiated power in kW.
