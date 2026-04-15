# Module 20 Review — Worked Problems on the Second Law

Practice problems with full solutions covering heat engines, Carnot cycles, refrigerators/heat pumps, and entropy.

---

## Problem 1 — Engine efficiency from work and waste heat

Engine rejects $Q_C = 1837$ J while doing $W = 1200$ J of work.
$$Q_H = W + |Q_C| = 3037\text{ J},\qquad e = W/Q_H = 1200/3037 \approx 0.395 = 39.5\%$$

## Problem 2 — Work from heat in/out

Aircraft engine takes in 8.88 kJ, discards 5.9 kJ.
$$W = Q_\text{in} - Q_\text{out} = 2.98\text{ kJ}$$

## Problem 3 — Net work from $pV$ cycle

Rectangular-like cycle with $p_1 = 88$ kPa, $p_2 = 174$ kPa, $p_3 = 291$ kPa, $V_1 = 1.3$ m³, $V_2 = 4.3$ m³. Net work = enclosed area of the loop.

## Problem 4 — Refrigerator COP

$Q_\text{cold} = 429$ J, COP $K = 13$.
$$W = Q_C/K = 33\text{ J},\qquad Q_\text{hot} = Q_C + W = 462\text{ J}$$

## Problem 5 — Heat-pump COP (heating mode)

Heat pump extracts $Q_C = 1037$ J from outside, does $W = 464$ J of work.
$$Q_H = Q_C + W = 1501\text{ J}$$
$$K_\text{heating} = Q_H/W = 1501/464 \approx 3.24$$

## Problem 6 — Heat-pump COP (cooling mode)

$Q_H = 1650$ J, $W = 242$ J.
$$Q_C = Q_H - W = 1408\text{ J}$$
$$K_\text{cooling} = Q_C/W = 1408/242 \approx 5.82$$

## Problem 7 — Efficiency from rectangular $pV$ cycle, monatomic gas

Rectangle with $p_1 = 66$ kPa, $p_2 = 246$ kPa, $V_1 = 0.9$ m³, $V_2 = 2.8$ m³.

Net work (area of the rectangle):
$$W = (p_2 - p_1)(V_2 - V_1)$$

Heat supplied is along the AB (isochoric at $V_1$, pressure rising) and BC (isobaric at $p_2$, volume expanding) legs:
$$Q_{AB} = n C_V\Delta T_{AB} = \tfrac{3}{2}(p_2 - p_1)V_1$$
$$Q_{BC} = n C_P\Delta T_{BC} = \tfrac{5}{2}(V_2 - V_1)p_2$$

For a monatomic gas, $C_V = \tfrac{3}{2}R$, $C_P = \tfrac{5}{2}R$. Then
$$e = \frac{W}{Q_{AB} + Q_{BC}} = \frac{(p_2 - p_1)(V_2 - V_1)}{\tfrac{3}{2}(p_2 - p_1)V_1 + \tfrac{5}{2}(V_2 - V_1)p_2}$$

Plugging in: $e \approx 0.717$ — **note:** the PDF's printed "$\tfrac{1}{2}$" for $Q_{BC}$ is a typo; the correct coefficient is $\tfrac{5}{2}$ (isobaric monatomic heat). Verify numerically.

## Problem 8 — Carnot: find $T_H$ from efficiency and $T_C$

$e = 0.35$, $T_C = 77°\text{C} = 350.15$ K.
$$T_H = \frac{T_C}{1 - e} = \frac{350.15}{0.65}\approx 538.7\text{ K}$$

## Problem 9 — Carnot again

$e = 0.77$, $T_C = 278$ K.
$$T_H = \frac{278}{0.23}\approx 1208.7\text{ K}$$

## Problem 10 — Entropy change on freezing water

$m = 6.2$ kg of water freezes at $T = 273.15$ K. $L_f = 3.35\times 10^5$ J/kg.
$$Q = -m L_f = -2.077\times 10^6\text{ J (heat leaves the water)}$$
$$\Delta S_\text{water} = Q/T = -7605\text{ J/K} = -7.605\text{ kJ/K}$$

## Problem 11 — Entropy change of universe: gallium freezing in room

$m = 39$ kg of liquid gallium at $T_f = 29.76°\text{C} = 302.91$ K freezes into a room at $T_R = 17°\text{C} = 290.15$ K. $L_f = 8.04\times 10^4$ J/kg.

$$\Delta S_\text{universe} = \Delta S_\text{Ga} + \Delta S_\text{room} = -\frac{m L_f}{T_f} + \frac{m L_f}{T_R} = m L_f\left(\frac{1}{T_R} - \frac{1}{T_f}\right) \approx 455.7\text{ J/K}$$

The universe's entropy increases — process is irreversible.

## Problem 12 — Entropy change of a heated metal block

$Q = 14569$ J added to $m = 1.6$ kg block, $c = 471$ J/(kg·K), $T_i = 285°\text{C} = 558.15$ K.

Find $T_f$ from $Q = mc\Delta T$: $T_f = 558.15 + Q/(mc) = 577.52$ K.

$$\Delta S = m c \ln(T_f/T_i) = (1.6)(471)\ln(577.52/558.15)\approx 25.68\text{ J/K}$$

## Problem 13 — Free expansion of an ideal gas (4 compartments)

2.2 mol ideal gas initially in 1 of 4 equal compartments. After removing partitions, $V_f = 4 V_i$.
$$\Delta S = nR\ln(V_f/V_i) = (2.2)(8.314)\ln 4\approx 25.34\text{ J/K}$$

Note: for a free expansion $Q = 0$ and $W = 0$, but entropy is a state function so $\Delta S$ is calculated along a reversible isothermal path.

## Problem 14 — Ice melts, warms to room: entropy of the universe

$m = 7$ kg ice at 0 °C melts, warms to 19 °C (292.15 K). Room stays at $T_R = 292.15$ K. $L_f = 3.35\times 10^5$ J/kg, $c_w = 4186$ J/(kg·K).

$$\Delta S_\text{ice} = \frac{m L_f}{T_1} + m c_w\ln\!\frac{T_2}{T_1}$$

$$\Delta S_\text{room} = -\frac{m L_f + m c_w(T_2 - T_1)}{T_R}$$

$$\Delta S_\text{universe} = \Delta S_\text{ice} + \Delta S_\text{room}\approx 623.78\text{ J/K}$$

---

## Key formulas used

$$e = \frac{W}{Q_H} = 1 - \frac{|Q_C|}{Q_H},\qquad e_\text{Carnot} = 1 - \frac{T_C}{T_H}$$
$$K_\text{refrig / cool} = \frac{Q_C}{W},\qquad K_\text{heat pump} = \frac{Q_H}{W}$$
$$\Delta S = \int\frac{dQ_\text{rev}}{T},\qquad \Delta S_\text{phase change} = \pm\frac{m L}{T}$$
$$\Delta S_\text{heating/cooling} = m c\ln(T_f/T_i)$$
$$\Delta S_\text{isothermal ideal gas} = nR\ln(V_f/V_i)$$
$$\Delta S_\text{universe} \ge 0\text{ (second law)}$$
