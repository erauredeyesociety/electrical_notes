# Module 19 Review — Worked Problems on the First Law

Practice problems with full solutions from the Module 19 review set. Sign convention here: $W$ is work done **by** the gas (positive when gas expands); work done **on** the gas is $-W$. $Q > 0$ when heat is added to the gas.

---

## Problem 1 — Isobaric work, work done on the gas

A system of gas increases in volume from $0.7$ m³ to $1.8$ m³ at a constant pressure of $52$ kPa. Find the work done **on** the gas.

$$W_\text{on} = -p\,\Delta V = -(52\text{ kPa})(1.1\text{ m}^3) = -57.2\text{ kJ}$$

Negative sign: the gas did work on the surroundings, so work was transferred out.

---

## Problem 2 — Multi-step $pV$ cycle (work)

For a multi-leg process on a $pV$-diagram with $p_1 = 104$ kPa, $p_2 = 194$ kPa, $V_1 = 1.2$ m³, $V_2 = 2$ m³, $V_3 = 2.9$ m³, compute the work done by the system.

Add the areas under each leg (triangles + rectangles as appropriate). The total:
$$W = \tfrac{1}{2}(V_2 - V_1)(p_3 - p_2) + p_2(V_2 - V_1) + \tfrac{1}{2}(V_3 - V_2)(p_2 - p_1) + p_1(V_3 - V_2) \approx 607.1\text{ kJ}$$

---

## Problem 3 — Multi-step work (simpler cycle)

For $p_1, p_2, V_1, V_2, V_3$ as given, the multi-step process yields
$$W = p_2(V_2 - V_1) + p_1(V_3 - V_2) = 248.8\text{ kJ}$$

---

## Problem 4 — First-law solve for $Q$

$\Delta U = 157$ J, $W = 297$ J (work by system). From $\Delta U = Q - W$:
$$Q = \Delta U + W = 157 + 297 = 454\text{ J}$$
Positive $\Rightarrow$ heat flows **into** the system.

---

## Problem 5 — Isochoric process, monatomic

An ideal monatomic gas increases from $p_1 = 134$ kPa to $p_2 = 226$ kPa at constant $V = 0.7$ m³. Find $Q$.

Isochoric: $W = 0$, so $Q = \Delta U$. For a monatomic ideal gas, $C_V = \tfrac{3}{2}R$, and $\Delta U = nC_V\Delta T$. Using $pV = nRT$ with $V$ constant:
$$\Delta U = \tfrac{3}{2} V (p_2 - p_1) = \tfrac{3}{2}(0.7)(92\text{ kPa}) = 96.6\text{ kJ}$$

---

## Problem 6 — Isochoric process, diatomic

Diatomic ideal gas, $V = 1.5$ m³, $p_1 = 135$ kPa $\to p_2 = 80$ kPa. $C_V = \tfrac{5}{2}R$.
$$Q = \Delta U = \tfrac{5}{2} V(p_2 - p_1) = \tfrac{5}{2}(1.5)(-55\text{ kPa}) = -206.25\text{ kJ}$$
Heat leaves the system.

---

## Problem 7 — Isobaric expansion, monatomic

Monatomic ideal gas expands isobarically at $p = 135$ kPa from $V_1 = 1.5$ m³ to $V_2 = 4$ m³. Find $Q$.

$\Delta U = \tfrac{3}{2}p\Delta V$, $W = p\Delta V$, so
$$Q = \Delta U + W = \tfrac{3}{2}p\Delta V + p\Delta V = \tfrac{5}{2}p\Delta V = \tfrac{5}{2}(135)(2.5) = 843.75\text{ kJ}$$

General rule for an isobaric process on an ideal gas: $Q = \tfrac{f+2}{2}\,p\Delta V$ where $f$ is the number of active degrees of freedom.

---

## Problem 8 — Isobaric compression, diatomic

Diatomic ideal gas contracts from $V_1 = 5.2$ m³ to $V_2 = 2.2$ m³ at $p = 190$ kPa.
$$Q = \tfrac{7}{2} p\Delta V = \tfrac{7}{2}(190)(-3) = -1995\text{ kJ}$$

---

## Problem 9 — Isothermal compression

Monatomic ideal gas from $V_1 = 2.7$ m³, $p_1 = 103$ kPa isothermally to $V_2 = 1.2$ m³. Work done **by** the gas:
$$W = nRT\ln(V_2/V_1) = p_1 V_1\ln(V_2/V_1) = (103)(2.7)\ln(1.2/2.7) \approx -225.5\text{ kJ}$$
Negative $\Rightarrow$ gas was compressed (work done **on** the gas).

---

## Problem 10 — Isothermal expansion

Monatomic ideal gas from $V_1 = 0.6$ m³, $p_i = 169$ kPa isothermally to $V_2 = 2$ m³. Work done **on** the gas (negative of work by):
$$W_\text{by} = p_i V_i \ln(V_f/V_i) = (169)(0.6)\ln(2/0.6) \approx 122\text{ kJ}$$
Work done *on* the gas is $\approx -122$ kJ (gas did 122 kJ of work on the surroundings).

---

## Problem 11 — Adiabatic compression (diatomic)

Diatomic ideal gas adiabatically from $V_1 = 2.2$ m³, $p_1 = 90$ kPa to $V_2 = 1$ m³. $\gamma = 1.4$.
$$p_2 = p_1\left(\frac{V_1}{V_2}\right)^{\gamma} = 90\,(2.2)^{1.4} \approx 271.4\text{ kPa}$$

---

## Problem 12 — Adiabatic expansion (diatomic), find $\Delta U$

Diatomic, $p_1 = 1.50\times 10^5$ Pa, $V_1 = 1.00$ m³, $V_2 = 2.00$ m³.
$$p_2 = p_1(V_1/V_2)^{1.4} \approx 56.8\text{ kPa}$$
$$W = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1} = \frac{150 - 113.6}{0.4}\approx 90.8\text{ kJ}$$
$$\Delta U = -W = -90.8\text{ kJ}$$

---

## Problem 13 — Another adiabatic expansion (diatomic)

$p_1 = 179$ kPa, $V_1 = 1.00$ m³, $V_2 = 1.9$ m³, $\gamma = 1.4$.
Compute $p_2 = p_1(V_1/V_2)^{1.4}$, then
$$W = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1},\qquad \Delta U = -W \approx -101.3\text{ kJ}$$

---

## Problem 14 — Straight-line process on $pV$ (monatomic)

Monatomic gas proceeds along a straight line on the $pV$ diagram from $(3\text{ m}^3, 167\text{ kPa})$ to $(5\text{ m}^3, 418\text{ kPa})$. Find $Q$.

$\Delta U$ depends only on endpoints:
$$\Delta U = \tfrac{3}{2}(p_2 V_2 - p_1 V_1)\approx 2383.5\text{ kJ}$$

Work = area under the straight line (trapezoid):
$$W = \tfrac{1}{2}(p_1 + p_2)(V_2 - V_1) = \tfrac{1}{2}(V_2 - V_1)(p_2 - p_1) + p_1(V_2 - V_1) = 585\text{ kJ}$$

$$Q = \Delta U + W \approx 2968.5\text{ kJ}$$

---

## Key formulas used throughout

$$\Delta U = Q - W\quad\text{(first law, with $W$ = work by system)}$$
$$\Delta U = n C_V\Delta T\quad\text{(ideal gas, any path)}$$
$$W_\text{isothermal} = nRT\ln(V_2/V_1) = p_1 V_1\ln(V_2/V_1)$$
$$W_\text{isobaric} = p\,\Delta V,\qquad Q_\text{isobaric} = \tfrac{f+2}{2}p\Delta V\text{ for ideal gas}$$
$$W_\text{isochoric} = 0,\qquad Q_\text{isochoric} = \Delta U = \tfrac{f}{2}V\Delta p$$
$$pV^\gamma = \text{const},\quad TV^{\gamma - 1} = \text{const}$$
$$W_\text{adiabat} = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1}$$

Monatomic $\gamma = 5/3$, diatomic $\gamma = 7/5$.
