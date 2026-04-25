# ME17: Temperature & Thermal Expansion — Walkthrough

**Module:** M17 — see [m17/](../../m17/)

**Core equations**
- Temperature: $T_F = \tfrac{9}{5}T_C + 32$, $T_K = T_C + 273.15$
- Linear expansion: $\Delta L = \alpha L_0\,\Delta T$
- Volume expansion: $\Delta V = \beta V_0\,\Delta T$, with $\beta \approx 3\alpha$ for an isotropic solid
- Heat: $Q = mc\,\Delta T$
- Phase change: $Q = mL_f$ (fusion) or $mL_v$ (vaporization)
- Conservation in mixing: $\sum Q_i = 0$ (heat lost = heat gained)
- Conduction: $H = kA\,\Delta T/d$
- Radiation (Stefan–Boltzmann): $H_{\text{net}} = \varepsilon\sigma A(T_s^4 - T_{\text{env}}^4)$, $\sigma = 5.67\times 10^{-8}\ \text{W/(m}^2\text{K}^4)$

Use $c_{\text{water}}=4190\ \text{J/(kg·K)}$ unless stated.

---

## Q1 — 201 K to °F

$T_C = 201 - 273.15 = -72.15$°C
$T_F = \tfrac{9}{5}(-72.15) + 32 = -129.87 + 32 = \boxed{-97.87\ ^\circ\text{F}}\ \checkmark$

---

## Q2 — $\Delta T$ for given expansion

$\alpha = 2.6\times 10^{-5}$, $L_0=1.7$ m, $\Delta L=0.0074$ m.
$$\Delta T = \dfrac{\Delta L}{\alpha L_0} = \dfrac{0.0074}{(2.6\times 10^{-5})(1.7)} = \boxed{167.42\ \text{C}°}\ \checkmark$$

---

## Q3 — $\Delta L$ for given $\Delta T$

$\alpha=1.1\times 10^{-5}$, $L_0=5.2$, $\Delta T=46$.
$$\Delta L = (1.1\times 10^{-5})(5.2)(46) = 2.6312\times 10^{-3}\ \text{m} = \boxed{2.6312\ \text{mm}}\ \checkmark$$

---

## Q4 — Volume coefficient of unknown fluid

$V_0=0.012\ \text{m}^3$, $\Delta T=7.1$, spill $\Delta V=16\times 10^{-6}\ \text{m}^3$, $\alpha_g=1.9\times 10^{-5}$.

The bottle's *capacity* expands like a solid: $\beta_g = 3\alpha_g = 5.7\times 10^{-5}$. Spill = fluid expansion − bottle expansion:
$$\Delta V_{\text{spill}} = (\beta_f - \beta_g)V_0\,\Delta T$$
$$\beta_f - \beta_g = \dfrac{16\times 10^{-6}}{(0.012)(7.1)} = 1.878\times 10^{-4}$$
$$\beta_f = 1.878\times 10^{-4} + 5.7\times 10^{-5} = 2.448\times 10^{-4}\ (\text{C}°)^{-1}$$
Convert to $(\text{kC}°)^{-1}$: multiply by 1000 ⇒ $\boxed{0.2448\ (\text{kC}°)^{-1}}\ \checkmark$

---

## Q5 — Falling water heated by impact

$V=1.3$ L ⇒ $m=1.3$ kg. All gravitational PE → heat: $mgh = mc\,\Delta T$ (mass cancels).
$$\Delta T = \dfrac{gh}{c} = \dfrac{9.8\cdot 150.2}{4190} = \boxed{0.3513\ ^\circ\text{C}}\ \checkmark$$

---

## Q6 — $\Delta T$ from $Q$, $m$, $c$

$\Delta T = Q/(mc) = 3141/(4.3\cdot 645) = 3141/2773.5 = \boxed{1.1325\ ^\circ\text{C}}\ \checkmark$

---

## Q7 — Specific heat from data

$c = Q/(m\Delta T) = 24512/(2.8\cdot 11) = 24512/30.8 = \boxed{795.84\ \text{J/(kg·C}°)}\ \checkmark$

---

## Q8 — Mixing two liquids

Heat balance, $\sum m_i c_i (T - T_{0i}) = 0$:
$$5.6(1050)(T - 13.5) + 9.5(2500)(T - 36.8) = 0$$
$$5880(T-13.5) + 23750(T-36.8) = 0$$
$$29630\,T = 5880(13.5) + 23750(36.8) = 79380 + 874000 = 953380$$
$$T = \boxed{32.176\ ^\circ\text{C}}\ \checkmark$$

---

## Q9 — Energy to freeze 0.29 kg of water from 17 °C

Cool to 0 °C, then freeze:
$$Q = mc\,\Delta T + mL_f = 0.29(4190)(17) + 0.29(335000)$$
$$= 20{,}654.7 + 97{,}150 = 117{,}804.7\ \text{J} = \boxed{117.81\ \text{kJ}}\ \checkmark$$

---

## Q10 — Ice at −20 °C → water at 16 °C, $m=2.69$ kg

Three steps: warm ice to 0, melt, warm water:
$$Q_1 = m c_{\text{ice}}(20) = 2.69(2100)(20) = 112{,}980\ \text{J}$$
$$Q_2 = m L_f = 2.69(334000) = 898{,}460\ \text{J}$$
$$Q_3 = m c_w (16) = 2.69(4190)(16) = 180{,}313.6\ \text{J}$$
$$Q_{\text{tot}} = 1{,}191{,}754\ \text{J} = \boxed{1191.78\ \text{kJ}}\ \checkmark$$

---

## Q11 — Ice + water, find equilibrium

Heat available from water cooling to 0:
$$Q_{\text{avail}} = 11.5(4190)(28.4) = 1.3685\times 10^6\ \text{J}$$
Heat to melt all ice:
$$Q_{\text{melt}} = 7.2(335000) = 2.412\times 10^6\ \text{J}$$
Since $Q_{\text{avail}} < Q_{\text{melt}}$, only some ice melts; equilibrium at the melting point: $\boxed{T_{\text{eq}} = 0\ ^\circ\text{C}}\ \checkmark$

---

## Q12 — Conduction through window

$A = 1.6\cdot 2 = 3.2\ \text{m}^2$, $d=0.0139$ m, $\Delta T = 35$ K, $k=0.8$ W/(m·K).
$$H = \dfrac{kA\,\Delta T}{d} = \dfrac{0.8(3.2)(35)}{0.0139} = 6446\ \text{W} = \boxed{6.446\ \text{kW}}\ \checkmark$$

---

## Q13 — Radiating sphere

$r=3.1$ m ⇒ $A=4\pi r^2 = 120.76\ \text{m}^2$; $\varepsilon = 0.63$.
$T_s = 365$ K ⇒ $T_s^4 = 1.7749\times 10^{10}$; $T_{\text{env}} = 301$ K ⇒ $T^4 = 8.2085\times 10^9$. Diff $= 9.540\times 10^9$.
$$H_{\text{net}} = \varepsilon\sigma A(T_s^4 - T_{\text{env}}^4) = 0.63(5.67\times 10^{-8})(120.76)(9.540\times 10^9)$$
$$= 41{,}156\ \text{W} = \boxed{41.16\ \text{kW}}\ \checkmark$$

---

## Q14 — Hole in heated metal

The hole **becomes larger** ✓ — every linear dimension scales by $1+\alpha\,\Delta T$, including the diameter of a hole. (Think of the hole's edge as if it were filled with the same metal: that "phantom" piece would expand, so the void expands too.)

---

## Q15 — Two rods, equal $Q$ absorbed

$\Delta T = Q/(mc)$. Rod A has $c_A = 2c_B$, so $\Delta T_A = \Delta T_B / 2$.
- A's final temperature is **less than** B's ✓
- $\Delta L = \alpha L_0\,\Delta T$. With $\alpha_A = 3\alpha_B$ and $\Delta T_A = \Delta T_B/2$:
$$\dfrac{\Delta L_A}{\Delta L_B} = 3\cdot\tfrac{1}{2} = \tfrac{3}{2}$$
- A is **greater** in length than B ✓

---

## Q16 — Hot stove + metal handle

Handle becomes **hot** by **conduction** ✓ (heat flows along the metal from the body of the pan through the handle).

---

**All numeric answers match the source key.**
