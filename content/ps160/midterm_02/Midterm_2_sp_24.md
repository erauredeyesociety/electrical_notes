# PS 160 — Test #2 (Spring 2024)

**Instructor:** Oussama Mhibik
**Date:** Thursday 4 April 2024
**Scope:** Thermodynamics (Modules 17, 18, 19, 20)
**Total:** 160 points (all problems 10 pts unless noted)

Equation sheet + calculator allowed.

---

## Problem 1 — Linear thermal expansion

Metal bar $L_0 = 1.5$ m, heated from 1 °C to 39 °C, $\alpha = 2.8\times 10^{-5}$ K⁻¹. Find $\Delta L$ in mm.
$$\Delta L = \alpha L_0\,\Delta T = (2.8\times 10^{-5})(1.5)(38) = 1.596\times 10^{-3}\text{ m}\approx 1.60\text{ mm}$$

## Problem 2 — Calorimetry (two-liquid mixture)

$m_\text{chl} = 7.3$ kg at 17.5 °C, $m_\text{prop} = 11.9$ kg at 32.7 °C. $c_\text{chl} = 1050$ J/(kg·K), $c_\text{prop} = 2500$ J/(kg·K). Find final $T_f$.
$$m_\text{chl}c_\text{chl}(T_f - 17.5) + m_\text{prop}c_\text{prop}(T_f - 32.7) = 0$$
$$T_f = \frac{m_\text{chl}c_\text{chl}(17.5) + m_\text{prop}c_\text{prop}(32.7)}{m_\text{chl}c_\text{chl} + m_\text{prop}c_\text{prop}}$$

## Problem 3 — Ice → steam energy

$m = 10.5$ kg of ice at 0 °C to steam at 100 °C. $L_f = 335{,}000$ J/kg, $L_v = 2{,}260{,}000$ J/kg, $c = 4190$ J/(kg·K). Three steps:

1. Melt ice: $Q_1 = m L_f$
2. Heat water 0 → 100 °C: $Q_2 = m c\Delta T$
3. Boil water: $Q_3 = m L_v$

Sum and convert to MJ:
$$Q = m(L_f + c\Delta T + L_v)$$

## Problem 4 — Spherical shell conduction

Shell thickness 10 mm, $k = 40$ W/(m·K), radius 6 m, $T_\text{in} = 24$ °C, $T_\text{out} = -16$ °C. Find $H$ in MW.

For a thin shell, use plane-slab approximation with area $A = 4\pi R^2$:
$$H = k A\frac{\Delta T}{L} = (40)(4\pi\cdot 6^2)\cdot\frac{40}{0.010}$$

## Problem 5 — Net radiation: find temperature

Iron ball $A = 1.03$ m², room $T_s = 16$ °C $= 289.15$ K, $e = 0.66$, net radiation $H_\text{net} = 2420$ W. Find $T$ (°C).
$$H_\text{net} = e A\sigma(T^4 - T_s^4)\Rightarrow T = \left(\frac{H_\text{net}}{e A\sigma} + T_s^4\right)^{1/4}$$

## Problem 6 — Moles of AlCl₃

$m = 610$ g. $M_\text{Al} = 26.98$ g/mol, $M_\text{Cl} = 35.45$ g/mol.
$$M_\text{AlCl}_3 = 26.98 + 3(35.45) = 133.33\text{ g/mol}$$
$$n = 610/133.33 \approx 4.575\text{ mol}$$

## Problem 7 — Ideal gas pressure

$n = 1$ mol, $V = 34$ L $= 0.034$ m³, $T = 300.15$ K. Find $p$ in atm.
$$p = nRT/V = (1)(8.314)(300.15)/0.034\approx 73{,}400\text{ Pa}\approx 0.724\text{ atm}$$

## Problem 8 — Temperature from translational KE

$n = 9$ mol, $K_\text{tr} = 49{,}891$ J. Find $T$.
$$K_\text{tr} = \tfrac{3}{2}nRT\Rightarrow T = \frac{2 K_\text{tr}}{3 nR} = \frac{2(49{,}891)}{3(9)(8.314)}\approx 444.5\text{ K}$$

## Problem 9 — Temperature from $v_\text{rms}$

$v_\text{rms} = 339$ m/s, $M = 19$ g/mol $= 0.019$ kg/mol. Find $T$.
$$v_\text{rms} = \sqrt{3RT/M}\Rightarrow T = \frac{M v_\text{rms}^2}{3R} = \frac{(0.019)(339)^2}{3(8.314)}\approx 87.6\text{ K}$$

## Problem 10 — Work from multi-step $pV$ process

$p_1 = 94$ kPa, $p_2 = 207$ kPa, $V_1 = 0.9$ m³, $V_2 = 4.1$ m³.

(Typical shape: straight-line process or isochoric + isobaric.) Work = area under the path. From the figure, likely a straight line from $(V_1, p_1)$ to $(V_2, p_2)$:
$$W = \tfrac{1}{2}(p_1 + p_2)(V_2 - V_1) = \tfrac{1}{2}(301)(3.2) = 481.6\text{ kJ}$$

## Problem 11 — Isobaric expansion, monatomic gas

$p = 131$ kPa, $V_1 = 1.7$ m³, $V_2 = 3.5$ m³.
$$Q = \tfrac{5}{2}p\,\Delta V = \tfrac{5}{2}(131)(1.8) = 589.5\text{ kJ}$$

## Problem 12 — Adiabatic compression, diatomic

$p_1 = 60$ kPa, $V_1 = 2.8$ m³, $V_2 = 1$ m³, $\gamma = 1.4$.
$$p_2 = p_1(V_1/V_2)^\gamma = 60(2.8)^{1.4}\approx 245\text{ kPa}$$

## Problem 13 — Waste heat from efficiency

$e = 0.24$, $W = 1017$ J. Find $|Q_C|$.
$$Q_H = W/e = 4237.5\text{ J},\qquad |Q_C| = Q_H - W = 3220.5\text{ J}$$

## Problem 14 — Heat-pump COP (heating)

$Q_C = 1152$ J, $Q_H = 1324$ J.
$$W = Q_H - Q_C = 172\text{ J}$$
$$K_\text{heating} = Q_H/W = 1324/172\approx 7.70$$

## Problem 15 — Entropy change: water freezing

$m = 11$ kg water at 0 °C $\to$ ice at 0 °C. $L_f = 3.35\times 10^5$ J/kg, $T = 273.15$ K.
$$Q = -m L_f = -3.685\times 10^6\text{ J}$$
$$\Delta S = Q/T = -1.349\times 10^4\text{ J/K}\approx -13.49\text{ kJ/K}$$
Negative because heat leaves the water.

## Problem 16 — Carnot: find $T_H$

$e = 0.48$, $T_C = 70$ °C $= 343.15$ K.
$$T_H = T_C/(1 - e) = 343.15/0.52\approx 659.9\text{ K}$$

## Bonus — Steam/water mixing

$m_s = 1.5$ kg steam at 100 °C condensed into $m_w = 13$ kg water at 27 °C. $L_v = 2.26\times 10^6$ J/kg, $c = 4190$ J/(kg·K).

**Check if all steam condenses.** Heat to warm water from 27 → 100 °C:
$$Q_\text{warm} = m_w c (100 - 27) = (13)(4190)(73)\approx 3.97\times 10^6\text{ J}$$
Heat from fully condensing steam:
$$Q_\text{cond} = m_s L_v = (1.5)(2.26\times 10^6) = 3.39\times 10^6\text{ J}$$
Since $Q_\text{cond} < Q_\text{warm}$, **not all** steam condenses — or the water reaches 100 °C before the steam finishes condensing. More precisely, check whether all the steam condenses and then cools to some $T_f < 100$ °C, or whether the final state has some steam remaining.

Assuming all steam condenses and cools to $T_f$ while water warms from 27 °C to $T_f$:
$$m_s L_v + m_s c(100 - T_f) = m_w c(T_f - 27)$$

Solve for $T_f$:
$$T_f = \frac{m_s L_v + m_s c(100) + m_w c(27)}{(m_s + m_w)c}$$

Plug numbers to check; if $T_f > 100$ °C, then not all steam condenses and the final state is partial steam at 100 °C.
