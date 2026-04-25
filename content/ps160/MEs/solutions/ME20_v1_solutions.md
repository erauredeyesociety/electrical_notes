# ME20: Heat Engines, Refrigerators & Entropy — Walkthrough

**Module:** M20 — see [m20/](../../m20/)

**Core formulas**
- Heat engine: $|Q_H| = W + |Q_C|$, efficiency $e = W/|Q_H| = 1 - |Q_C|/|Q_H|$
- Refrigerator / heat-pump (cooling) COP: $K = |Q_C|/W$
- Heat-pump (heating) COP: $K_{HP} = |Q_H|/W$
- Carnot: $|Q_C|/|Q_H| = T_C/T_H$, $e_{\text{Carnot}} = 1 - T_C/T_H$
- Net work in a cycle = enclosed area on $pV$
- Entropy (reversible): $\Delta S = \int dQ/T$. Specials:
  - Phase change at $T$: $\Delta S = \pm mL/T$
  - Constant V, ideal gas: $\Delta S = nC_v\ln(T_f/T_i)$
  - Constant T, ideal gas: $\Delta S = nR\ln(V_f/V_i)$
  - Reservoir absorbing $Q$ at $T$: $\Delta S = Q/T$ (with sign)

---

## Q1 — Q_C from efficiency

A gasoline engine takes in $Q_H$ from combustion and converts a fraction $e$ of it to mechanical work; the rest is dumped to the cold reservoir (exhaust). The "be careful of sign" hint reminds us that $Q_C$ is heat *out of* the system, so it carries a negative sign.

$Q_H = +8.87$ kJ, $e = 0.37$.
$W = e\,Q_H = 3.2819$ kJ; $|Q_C| = Q_H - W = 5.5881$ kJ. With sign convention "out of system":
$$Q_C = \boxed{-5.5881\ \text{kJ}}\ \checkmark$$

---

## Q2 — Work from heat in/out

An aircraft engine ingests heat each cycle and discards some of it. By energy conservation $|Q_H| = W + |Q_C|$, so the mechanical work output is just the difference between heat absorbed and heat rejected.

$W = Q_H - |Q_C| = 9.52 - 6.08 = \boxed{3.44\ \text{kJ}}\ \checkmark$

---

## Q3 — Engine cycle, net work

The cycle on the $pV$ diagram has four legs: pressurize at fixed $V_1$, then ramp linearly down/right to $(V_2,p_2)$, then drop at fixed $V_2$, then contract isobarically back to start. Net work in a cycle is the area enclosed; equivalently, sum the work along each leg, with vertical (isochoric) legs contributing nothing.

The cycle traces: $(V_1,p_1) \xrightarrow{\text{iso V}} (V_1,p_3) \xrightarrow{\text{linear ramp down}} (V_2,p_2) \xrightarrow{\text{iso V}} (V_2,p_1) \xrightarrow{\text{iso p}} (V_1,p_1)$.

- Leg 1 (iso V, pressurize): $W_1 = 0$
- Leg 2 (line from $p_3$ to $p_2$ as $V$ goes $V_1 \to V_2$): trapezoid area
$$W_2 = \tfrac{1}{2}(p_3 + p_2)(V_2 - V_1) = \tfrac{1}{2}(283 + 177)(2.6) = 598.0\ \text{kJ}$$
- Leg 3 (iso V): $W_3 = 0$
- Leg 4 (iso p at $p_1$, contract): $W_4 = p_1(V_1 - V_2) = 93(-2.6) = -241.8$ kJ
$$W_{\text{net}} = 598.0 - 241.8 = \boxed{356.2\ \text{kJ}}\ \checkmark$$

---

## Q4 — Refrigerator COP

A fridge moves heat from the cold interior to the warm kitchen by paying work $W$. Energy conservation says the heat dumped to the kitchen is $|Q_H| = |Q_C| + W$, so we can back out $|Q_C|$ and compute the cooling-mode COP.

Refrigerator dumps $|Q_H| = 1305$ J to kitchen; $W = 106$ J.
$|Q_C| = |Q_H| - W = 1199$ J.
$$K = |Q_C|/W = 1199/106 = \boxed{11.31}\ \checkmark$$

---

## Q5 — Heat pump (heating), $Q_C$ from COP

A heat pump in heating mode delivers $|Q_H|$ to the home; the heating COP relates that delivered heat to the work input. Once we get $W$, energy conservation gives $|Q_C|$ — the heat extracted from the outdoors.

$|Q_H| = 1116$ J, $K_{HP} = |Q_H|/W = 10.9 \Rightarrow W = 1116/10.9 = 102.39$ J.
$$|Q_C| = |Q_H| - W = 1116 - 102.39 = \boxed{1013.61\ \text{J}}\ \checkmark$$

---

## Q6 — Heat pump (cooling) COP

In cooling mode the heat pump pulls $|Q_C|$ from inside and ejects $|Q_H|$ outside. Work input is the difference, and cooling COP is heat-removed-from-cold per joule of work.

$|Q_C| = 1050$, $|Q_H| = 1236$, $W = 186$.
$$K = 1050/186 = \boxed{5.645}\ \checkmark$$

---

## Q7 — Rectangular cycle, monatomic, efficiency

The gas traces a rectangle on the $pV$ diagram between $(p_L, p_H) = (86, 216)$ kPa and $(V_L, V_H) = (0.6, 2.5)$ m³. Net work is the rectangle's area. To find efficiency we need $Q_{\text{in}}$, which is the sum of heat absorbed on the two legs where heat *enters* the gas: the isochoric pressurization at $V_L$ (where $\Delta U = (3/2)V\Delta p$) and the isobaric expansion at $p_H$ (where $\Delta U + W = (5/2)p\Delta V$).

Net work = enclosed rectangle:
$$W_{\text{net}} = (p_H - p_L)(V_H - V_L) = (216 - 86)(2.5 - 0.6) = 130(1.9) = 247\ \text{kJ}$$
Heat in (the two legs where $Q>0$): isochoric pressurize + isobaric expansion at high $p$.
$$Q_1 = \tfrac{3}{2}V_L\,\Delta p = 1.5(0.6)(130) = 117\ \text{kJ}$$
$$Q_2 = \tfrac{5}{2}p_H\,\Delta V = 2.5(216)(1.9) = 1026\ \text{kJ}$$
$$Q_{\text{in}} = 1143\ \text{kJ},\quad e = W/Q_{\text{in}} = 247/1143 = \boxed{0.2161}\ \checkmark$$

---

## Q8 — Carnot work output

A Carnot engine running between hot/cold reservoirs has the maximum possible efficiency, $e = 1 - T_C/T_H$. Multiply that by $Q_H$ to get the work output.

$T_C=334$, $T_H=564$, $Q_H=2313$ J.
$e = 1 - 334/564 = 0.4078$; $W = e Q_H = \boxed{943.24\ \text{J}}$ $\checkmark$

---

## Q9 — Carnot, find $T_H$

We're told the heat ejected to the cold reservoir, the cold-reservoir temperature, and the work done. Energy conservation gives $|Q_H|$, and the Carnot identity $|Q_C|/|Q_H| = T_C/T_H$ then pins down $T_H$.

$|Q_C| = 1171$, $T_C = 301$, $W = 339$ ⇒ $|Q_H| = 1510$.
$$\dfrac{T_H}{T_C} = \dfrac{|Q_H|}{|Q_C|} \Rightarrow T_H = 301\cdot\dfrac{1510}{1171} = \boxed{388.14\ \text{K}}\ \checkmark$$

---

## Q10 — Entropy change on melting

A solid sits at its melting point and absorbs $mL_f$ of heat at fixed temperature to liquefy. Because the temperature is constant during the phase change, $\Delta S$ is just heat-in divided by the (absolute) melting temperature.

$T_{\text{melt}} = -24°\text{C} = 249.15$ K. $Q = mL_f = 2.2(191022) = 420{,}248$ J.
$$\Delta S = Q/T = 420248/249.15 = \boxed{1687.74\ \text{J/K}}\ \checkmark$$

---

## Q11 — Entropy of universe as gallium freezes

Liquid gallium at its melting point (29.76 °C) is placed in an 18 °C room. The gallium freezes, releasing $mL_f$ of heat. The gallium loses entropy at the higher temperature $T_g$; the room gains entropy at the lower temperature $T_r$. Because $T_r < T_g$, the room's positive entropy change outweighs the gallium's negative one, and $\Delta S_{\text{univ}} > 0$ as the second law requires.

Heat released $Q = mL_f = 39(8.04\times 10^4) = 3.1356\times 10^6$ J.
- Gallium loses heat at $T_g = 302.76$ K: $\Delta S_g = -Q/T_g = -10{,}356.7$ J/K
- Room absorbs heat at $T_r = 291$ K: $\Delta S_r = +Q/T_r = +10{,}775.3$ J/K
$$\Delta S_{\text{univ}} = +418.6\ \text{J/K} \approx \boxed{418.5\ \text{J/K}}\ \checkmark$$

---

## Q12 — Isochoric warming entropy

A monatomic gas in a rigid container is warmed by 42 K. With volume fixed, $dQ = nC_v\,dT$, so the entropy integral becomes $nC_v\ln(T_f/T_i)$ with $C_v = (3/2)R$. Remember to convert the starting temperature to Kelvin.

Monatomic ⇒ $C_v = (3/2)R$. $T_i = 292.15$ K, $T_f = 334.15$ K.
$$\Delta S = nC_v\ln(T_f/T_i) = 12(1.5)(8.314)\ln(334.15/292.15)$$
$$= 149.65\cdot 0.13428 = \boxed{20.10\ \text{J/K}}\ \checkmark$$

(Source: 20.1125 — within rounding.)

---

## Q13 — Free expansion of helium

Helium expands into a vacuum, doubling-plus its volume. No work is done and no heat flows, so $\Delta U = 0$ and $T$ is unchanged for an ideal gas. Entropy is a state function, so we evaluate it along an equivalent reversible isothermal expansion using $\Delta S = nR\ln(V_f/V_i)$.

Free expansion is irreversible but $\Delta S$ depends only on endpoints — equate to a reversible isothermal expansion:
$$n = 43.2/4.00 = 10.8\ \text{mol},\quad V_f/V_i = (1.6+3.9)/1.6 = 3.4375$$
$$\Delta S = nR\ln(V_f/V_i) = 10.8(8.314)\ln(3.4375) = 89.79(1.2347) = \boxed{110.88\ \text{J/K}}\ \checkmark$$

---

## Q14 — Universe entropy: ice melts then water warms (room at 24 °C)

A 5.4 kg block of ice melts and then warms to room temperature, with the room acting as a reservoir at 297 K. Two stages, each contributing to the universe's entropy: the ice/water gains entropy as it absorbs heat, and the room loses entropy as it gives heat up. Stage 1 is a phase change at 273.15 K; stage 2 is constant-pressure warming where $\Delta S_{\text{water}} = mc\ln(T_f/T_i)$.

Two stages, room at $T_r = 297$ K throughout.

**Stage 1 (melt at 273.15 K):** $Q_1 = mL_f = 5.4(335000) = 1.809\times 10^6$ J.
- $\Delta S_{\text{ice}} = +Q_1/273.15 = 6624.4$ J/K
- $\Delta S_{\text{room}} = -Q_1/297 = -6090.9$ J/K

**Stage 2 (warm 273.15 → 297 K):** $Q_2 = mc\Delta T = 5.4(4186)(24) = 5.425\times 10^5$ J.
- $\Delta S_{\text{water}} = mc\ln(T_f/T_i) = 5.4(4186)\ln(297/273.15) = 22604\cdot 0.08428 = 1905$ J/K
- $\Delta S_{\text{room}} = -Q_2/297 = -1826.6$ J/K

$$\Delta S_{\text{univ}} = 6624.4 - 6090.9 + 1905 - 1826.6 = \boxed{612\text{–}614\ \text{J/K}}\ \approx 613.5\ \checkmark$$

---

## Q15 — Entropy true/false

These probe the precise statement of the second law and what "isentropic" actually requires.

(A) "Entropy of *any* region always increases" — **False** ✓ The second law applies to the universe as a whole; a subsystem can lose entropy if it dumps heat to its surroundings (e.g., the gallium in Q11).
(B) "Entropy of universe $\ge 0$ for any process" — **True** ✓ This is the statement of the 2nd law: $\Delta S_{\text{univ}} \ge 0$, with equality only for reversible processes.
(C) "Universe entropy increases during free expansion" — **True** ✓ Free expansion is irreversible and adiabatic ($\Delta S_{\text{gas}} > 0$, no reservoir change), so $\Delta S_{\text{univ}} > 0$.
(D) "Adiabatic non-isothermal process has $\Delta S = 0$" — **False** ✓. Only *reversible* adiabatic processes are isentropic; irreversible adiabatic (e.g., free expansion of an insulated gas) has $\Delta S > 0$.

---

## Q16 — Pre-power-stroke process

The "thermal process just before the power stroke" is the combustion event itself in each cycle.

- **Diesel** cycle: fuel is injected as the piston nears TDC and burns gradually as the piston descends, holding pressure roughly constant → **isobaric** ✓
- **Otto** cycle: spark ignites the pre-mixed charge at TDC almost instantly, before the piston has moved appreciably → **isochoric** ✓

---

**All numeric answers match the source key.**
