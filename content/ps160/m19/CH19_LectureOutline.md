# Chapter 19: First Law of Thermodynamics — Lecture Outline

## Learning Outcomes

In this chapter, you'll learn:
- How to calculate work done by a system when its volume changes.
- How to interpret and use the **first law of thermodynamics**.
- Four important kinds of thermodynamic processes.
- Why the internal energy of an ideal gas depends only on temperature.
- The difference between molar heat capacities at constant volume and at constant pressure.
- How to analyze adiabatic processes in an ideal gas.

## Introduction

Steam locomotives, air conditioners, car engines all operate via thermodynamics. The first law is a generalized conservation of energy.

## Thermodynamic Systems

A **thermodynamic system** is any collection of objects that may exchange energy with its surroundings.

### Sign Convention
- $Q$ is **positive** when heat flows **into** the system; negative when it leaves.
- $W$ is the work done **by** the system; **positive for expansion**, negative for compression (work done on the system).

## Work Done During Volume Changes

When a gas expands, it does positive work on its surroundings (molecules bounce off a receding piston and lose KE). When compressed, it does negative work.

Infinitesimal work done by system during expansion $dx$:
$$dW = pA\, dx = p\, dV$$

For finite volume change:
$$W = \int_{V_1}^{V_2} p\, dV$$

### Special Cases
- **Constant pressure (isobaric)**: $W = p(V_2 - V_1)$
- Expansion → $W > 0$; Compression → $W < 0$.

### Work Depends on Path

Going from state 1 to state 2 on a $pV$-diagram, different paths give different work:
- Path $1 \to 3 \to 2$ (expand at $p_1$, then drop pressure): large $W$.
- Path $1 \to 4 \to 2$ (drop pressure, then expand at $p_2$): small $W$.
- Smooth curve from 1 to 2: different from both.

Work equals the **area under the curve** in the $pV$-diagram.

## First Law of Thermodynamics

$$\Delta U = Q - W$$

- $\Delta U$: change in internal energy of the system
- $Q$: heat added **to** the system
- $W$: work done **by** the system

For infinitesimal changes: $dU = dQ - dW$.

Although $Q$ and $W$ each depend on the path, $\Delta U$ is **path-independent** — internal energy is a state function.

### Cases
- If $Q > W$: $\Delta U > 0$ (internal energy increases).
- If $Q < W$: $\Delta U < 0$ (internal energy decreases).
- If $Q = W$: $\Delta U = 0$.

### First Law of Exercise Thermodynamics
Your body: during exercise $W > 0$, $Q < 0$ (body loses heat via sweat). So $\Delta U < 0$ — body burns stored fat.

### Cyclic Process
In a cyclic process (body over a day), total $\Delta U = 0$, so $Q_{\text{total}} = W_{\text{total}}$.

## Internal Energy — State Function

Depends only on current thermodynamic state (e.g., amount, composition, temperature). Does not depend on how the state was reached.

## Four Kinds of Thermodynamic Processes

- **Adiabatic**: $Q = 0$ (no heat transferred). $\Delta U = -W$.
- **Isochoric**: $V$ constant. $W = 0$, so $\Delta U = Q$.
- **Isobaric**: $p$ constant. $W = p(V_2 - V_1)$.
- **Isothermal**: $T$ constant.

### Illustrations
- **Adiabatic example**: popping a champagne cork — gases expand rapidly, little time for heat exchange; $T$ drops; water vapor condenses as a mist.
- **Isobaric example**: most cooking (open to atmosphere).
- **Exhaling adiabatically**: wide mouth → breath feels warm (body $T$); pursed lips → rapid expansion → feels cool.

### pV Diagram of Four Processes (starting from state $a$)
- Adiabatic: steeper than isotherm; $T_1 < T_a$.
- Isothermal: $T_4 = T_a$.
- Isobaric: horizontal line; $T_3 > T_a$.
- Isochoric: vertical line; $T_2 < T_a$.

## Internal Energy of an Ideal Gas

**Internal energy of an ideal gas depends only on temperature**, not on pressure or volume.
- In a free expansion (breaking a partition into vacuum), $T$ does not change because no work is done and no heat flows; hence $U$ doesn't change.

## Heat Capacities of an Ideal Gas

### Constant Volume

$$dQ = n C_V\, dT \quad \text{so} \quad \Delta U = n C_V \Delta T$$

### Constant Pressure

$$dQ = n C_p\, dT$$

### Relation between $C_p$ and $C_V$

To produce the same $\Delta T$, more heat is needed at constant $p$ (because gas also does work).

$$C_p = C_V + R$$

So $C_p > C_V$.

### Ratio of Heat Capacities

$$\gamma = \frac{C_p}{C_V}$$

- Monatomic ideal gas: $\gamma = 5/3 \approx 1.67$
- Diatomic ideal gas: $\gamma = 7/5 = 1.40$

## Adiabatic Processes for an Ideal Gas

In an adiabatic process, $Q = 0$, so $\Delta U = -W$. As an ideal gas expands adiabatically, it does positive work on surroundings, internal energy decreases, and $T$ drops.

An adiabatic curve on a $pV$-diagram is always **steeper** than the isotherm passing through the same point.

### Adiabatic Relations for an Ideal Gas

$$T V^{\gamma - 1} = \text{const}$$
$$p V^{\gamma} = \text{const}$$
$$T^\gamma p^{1-\gamma} = \text{const}$$

Work done in an adiabatic process:
$$W = n C_V (T_1 - T_2) = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1}$$

## Example Quiz Questions

1. Gas volume decreases 2 → 0.8 m$^3$ at $p = 65$ kPa. $W_{\text{by}}$ = −78 kJ.
2. pV-diagram with $p_1 = 109$ kPa, $p_2 = 459$ kPa; $V_1 = 1.9$, $V_2 = 4.5$, $V_3 = 5.3$ m$^3$. Triangle path. $W_{\text{on}}$ = −965.6 kJ.
3. pV-diagram with $p_1 = 84.6$ kPa, $p_2 = 222.1$ kPa; $V_1 = 1$, $V_2 = 1.9$, $V_3 = 3.4$ m$^3$. $W_{\text{on}}$ = 264.915 kJ.
4. System absorbs $Q = 741$ J, does work = $0.24 Q$. $\Delta U = 741 - 177.84 = 563.16$ J.
5. Ideal monatomic gas: $p$ rises from 119 to 210 kPa at $V = 1.4$ m$^3$. $Q = n C_V \Delta T = \tfrac{3}{2} V \Delta p = 191.1$ kJ.
6. Same gas, 150 → 206 kPa, 1.8 m$^3$. $\Delta U = 151.2$ kJ.
7. Monatomic ideal gas expands at $p = 123$ kPa from 0.7 → 2.9 m$^3$. $W = 270.6$ kJ.
8. Diatomic ideal gas contracts 3.5 → 0.8 m$^3$ at $p = 168$ kPa. $Q = \tfrac{7}{2} p \Delta V = -1587.6$ kJ.
9. Diatomic ideal gas isothermal expansion. $\Delta U = 0$.
10. Monatomic ideal gas isothermal compression 3.2 → 1.3 m$^3$ at $p_1 = 71$ kPa. $W_{\text{by}} = p_1 V_1 \ln(V_2/V_1) = -204.66$ kJ.
11. Diatomic ideal gas adiabatic compression 2.6 → 1 m$^3$; $p_1 = 65$ kPa. $p_2 = p_1 (V_1/V_2)^{1.4} \approx 247.67$ kPa.
12. Monatomic ideal gas adiabatic, $p_1 = 10^5$ Pa, 3 → 1 m$^3$. $p_2 \approx 624$ kPa; $\Delta U \approx 486$ kJ.
13. Monatomic adiabatic expansion 1.3 → 3 m$^3$, $p_1 = 111$ kPa. $Q = 0$ (adiabatic).
14. Diatomic process along straight line on pV from (2, 284) to (5, 415) kPa. $W = \tfrac{1}{2}(p_1 + p_2)\Delta V \approx 1048.5$ kJ.
15. True/False:
    - Isobaric expansion → heat in: **Always True**.
    - Isothermal → heat out: **Sometimes True**.
    - Adiabatic compression → heat in: **Always False** (adiabatic = no heat).
    - Isochoric pressure decrease → heat out: **Always True**.
16. Names:
    - $\Delta U = 0$ → **isothermal**
    - $W = 0$ → **isochoric**
    - $Q = 0$ → **adiabatic**
