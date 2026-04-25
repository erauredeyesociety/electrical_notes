# ME19: Heat Transfer (Thermodynamic Processes) — Walkthrough

**Module:** M19 — see [m19/](../../m19/)

**Sign convention:** $W_{\text{by}}$ = work done by gas on surroundings; $W_{\text{on}} = -W_{\text{by}}$. First law: $\Delta U = Q - W_{\text{by}} = Q + W_{\text{on}}$.

**Process tools**
- $W_{\text{by}} = \int p\,dV$ — area under the path on a $pV$ diagram
- Isobaric: $W_{\text{by}} = p\,\Delta V$, $\Delta U = (f/2)nR\Delta T = (f/2)\,p\Delta V$
- Isochoric: $W = 0$, $Q = \Delta U$
- Isothermal: $\Delta U = 0$ (ideal gas), $Q = W_{\text{by}} = nRT\ln(V_f/V_i) = p_iV_i\ln(V_f/V_i)$
- Adiabatic: $Q = 0$, $pV^\gamma = \text{const}$, $W_{\text{by}} = (p_iV_i - p_fV_f)/(\gamma-1)$, $\Delta U = -W_{\text{by}}$
- $\gamma$: monatomic 5/3 ($f=3$), diatomic 7/5 ($f=5$)
- Internal energy change: $\Delta U = (f/2)V\Delta p$ (constant $V$); $\Delta U = (f/2)p\Delta V$ (constant $p$)

---

## Q1 — Isobaric compression, work *on* the gas

A gas is compressed at fixed pressure from a larger volume down to a smaller one. Because pressure is held steady, the area under the path on a $pV$ diagram is just a rectangle, and since the gas is being squeezed, the surroundings must be pushing in — so work *on* the gas is positive.

$p=197$ kPa, $V_i=3.2 \to V_f=1.1\ \text{m}^3$.
$$W_{\text{by}} = p\,\Delta V = 197\cdot(1.1 - 3.2) = -413.7\ \text{kJ}$$
$$W_{\text{on}} = -W_{\text{by}} = \boxed{+413.7\ \text{kJ}}\ \checkmark$$

(Compression ⇒ surroundings do positive work on the gas.)

---

## Q2 — Two-step "step-down" $pV$ diagram

The gas first expands at high pressure $p_2$ from $V_1$ to $V_2$, then drops vertically (isochoric pressure drop, no work) to $p_1$, and finally expands at low pressure $p_1$ from $V_2$ to $V_3$. Total work *by* the gas is the sum of two rectangles under the horizontal isobaric segments.

Standard step-down: start at $(V_1, p_2)$, expand isobarically to $V_2$, drop isochorically to $p_1$, then expand isobarically to $V_3$. Work is the sum of the two rectangles:
$$W_{\text{by}} = p_2(V_2 - V_1) + p_1(V_3 - V_2)$$
$$= 212(2 - 0.9) + 91(3 - 2) = 233.2 + 91 = \boxed{324.2\ \text{kJ}}\ \checkmark$$

---

## Q3 — V-shaped two-leg ramp, work *on* the gas

The path forms a V-shape: pressure drops linearly while volume grows from $V_1$ to $V_2$, then rises linearly while volume continues from $V_2$ to $V_3$. Each linear leg's work is a trapezoid under the segment; because the two trapezoids share the same average height $\tfrac12(p_1+p_2)$, they combine into one big trapezoid spanning $V_1$ to $V_3$.

Path: $(V_1, p_2) \to (V_2, p_1)$ [ramp down] $\to (V_3, p_2)$ [ramp up]. Each leg's work is a trapezoid:
$$W_{\text{by}} = \tfrac{1}{2}(p_1+p_2)(V_2-V_1) + \tfrac{1}{2}(p_1+p_2)(V_3-V_2)$$
$$= \tfrac{1}{2}(p_1+p_2)(V_3-V_1) = \tfrac{1}{2}(172+415)(5.1-1.3)$$
$$= \tfrac{1}{2}(587)(3.8) = +1115.3\ \text{kJ}$$
$$W_{\text{on}} = \boxed{-1115.3\ \text{kJ}}\ \checkmark$$

---

## Q4 — First law

The gas absorbs heat from the environment and uses a fixed fraction (62%) of that heat to push back on the surroundings. Whatever isn't spent on work stays inside as raised internal energy — exactly what the first law tracks.

$Q = +644$ J absorbed; $W_{\text{by}} = 0.62(644) = 399.28$ J.
$$\Delta U = Q - W_{\text{by}} = 644 - 399.28 = \boxed{244.72\ \text{J}}\ \checkmark$$

---

## Q5 — Heat at constant volume (monatomic)

A monatomic gas sits in a sealed rigid container while its pressure rises. With volume locked, the gas can do no work, so all heat input goes into internal energy. For a monatomic ideal gas, $\Delta U = (3/2)nR\Delta T$, and $nR\Delta T = V\Delta p$ at constant $V$.

Constant $V$: $W = 0$, so $Q = \Delta U = (3/2)nR\Delta T = (3/2)V\,\Delta p$.
$$Q = 1.5(1.1)(208 - 116)\ \text{kPa·m}^3 = 1.5(1.1)(92) = \boxed{151.8\ \text{kJ}}\ \checkmark$$

---

## Q6 — Work at constant volume

If the container can't change size, the gas has nothing to push on — no displacement, no $p\,dV$ work, regardless of how hot or pressurized it gets.

Isochoric ⇒ $\boxed{W = 0}$ ✓.

---

## Q7 — Diatomic isobaric compression, $\Delta U$

A diatomic gas is squeezed at fixed pressure. Since diatomic molecules have $f=5$ active degrees of freedom (3 translational + 2 rotational), each unit of $p\Delta V$ corresponds to a larger internal-energy change than for a monatomic gas. Compression ($\Delta V < 0$) cools the gas, so $\Delta U < 0$.

$\Delta U = (5/2)nR\Delta T = (5/2)\,p\,\Delta V$.
$$= 2.5(225)(1.7 - 3.9) = 2.5(225)(-2.2) = \boxed{-1237.5\ \text{kJ}}\ \checkmark$$

---

## Q8 — Monatomic isobaric expansion, $W_{\text{by}}$

A monatomic gas expands while pressure stays constant — think a piston rising under fixed weight. The work done by the gas is just the area of the rectangle $p\,\Delta V$.

$$W_{\text{by}} = p\,\Delta V = 130(4 - 1.2) = 130(2.8) = \boxed{364\ \text{kJ}}\ \checkmark$$

---

## Q9 — Isothermal expansion, work *on* the gas

The gas expands slowly while submerged in a heat bath that keeps its temperature pinned. Internal energy doesn't budge ($\Delta U = 0$), so every joule of heat absorbed goes straight into work pushing on the surroundings — the gas does positive work, so work done *on* the gas is negative.

$$W_{\text{by}} = p_iV_i\ln(V_f/V_i) = 159(1.3)\ln(2/1.3) = 206.7(0.4308) = +89.04\ \text{kJ}$$
$$W_{\text{on}} = \boxed{-89.04\ \text{kJ}}\ \checkmark$$

---

## Q10 — Isothermal compression

Same isothermal setup, but now we squeeze the gas down (volume drops from 3 to 1.2 m³). The surroundings push in, so the gas does negative work, and the gas must dump an equal amount of heat to the bath to hold $T$ steady.

$$W_{\text{by}} = p_iV_i\ln(V_f/V_i) = 120(3)\ln(1.2/3) = 360\ln(0.4) = 360(-0.9163) = \boxed{-329.86\ \text{kJ}}\ \checkmark$$

(Negative because work is done on the gas during compression.)

---

## Q11 — Diatomic adiabatic compression, $p_f$

A diatomic gas (air, roughly) is compressed quickly enough that no heat can escape — adiabatic. Pressure shoots up faster than for a slow isothermal compression because the gas also heats up, and the relationship $pV^\gamma = \text{const}$ with $\gamma = 7/5$ tracks both effects.

$\gamma = 7/5 = 1.4$. $p_iV_i^\gamma = p_fV_f^\gamma \Rightarrow p_f = p_i(V_i/V_f)^\gamma$.
$$p_f = 81\,(2.8/1.4)^{1.4} = 81\cdot 2^{1.4} = 81(2.6390) = \boxed{213.76\ \text{kPa}}\ \checkmark$$

---

## Q12 — Monatomic adiabatic, find $p_f$ and $\Delta U$

A monatomic gas is compressed adiabatically by a factor of 3 in volume. With no heat exchanged, the work done on the gas all becomes internal energy ($\Delta U = -W_{\text{by}} = +W_{\text{on}}$), so the gas ends up much hotter and at much higher pressure.

$\gamma = 5/3$. $p_i = 10^5$ Pa, $V_i = 3$, $V_f = 1$.
$$p_f = p_i(V_i/V_f)^\gamma = 10^5\cdot 3^{5/3} = 10^5(6.240) = 624\ \text{kPa}\ \checkmark$$

For adiabatic: $W_{\text{by}} = (p_iV_i - p_fV_f)/(\gamma-1)$.
$$W_{\text{by}} = \dfrac{(10^5)(3) - (6.24\times 10^5)(1)}{2/3} = \dfrac{-3.24\times 10^5}{2/3} = -4.86\times 10^5\ \text{J}$$
$$\Delta U = -W_{\text{by}} = \boxed{+486\ \text{kJ}}\ \checkmark$$

(Adiabatic compression ⇒ internal energy rises.)

---

## Q13 — Monatomic adiabatic expansion, $\Delta U$

Now the same monatomic gas expands adiabatically — the gas pushes the piston outward and, with no heat input to replace the spent energy, must cool. $\Delta U$ is therefore negative.

$\gamma = 5/3$, $V_i=1.4$, $V_f=2.6$, $p_i=304$ kPa.
$$p_f = 304(1.4/2.6)^{5/3} = 304(0.5385)^{1.6667} = 304(0.3563) = 108.32\ \text{kPa}$$
$$W_{\text{by}} = \dfrac{p_iV_i - p_fV_f}{\gamma-1} = \dfrac{304(1.4) - 108.32(2.6)}{2/3} = \dfrac{425.6 - 281.63}{0.6667}$$
$$= \dfrac{143.97}{0.6667} = +215.87\ \text{kJ}$$
$$\Delta U = -W_{\text{by}} = \boxed{-215.87\ \text{kJ}}\ \checkmark$$

(Expansion does work on surroundings ⇒ internal energy drops.)

---

## Q14 — Straight ramp on a $pV$ diagram

The state moves along a straight line from $(3\text{ m}^3, 146\text{ kPa})$ to $(5\text{ m}^3, 541\text{ kPa})$. Work *by* the gas is the area under that segment, which is a trapezoid with parallel sides equal to the initial and final pressures.

Trapezoidal area under straight segment from $(3, 146)$ to $(5, 541)$:
$$W_{\text{by}} = \tfrac{1}{2}(p_i+p_f)(V_f-V_i) = \tfrac{1}{2}(146+541)(2) = \boxed{687\ \text{kJ}}\ \checkmark$$

---

## Q15 — First-law statements

Each statement is a first-law identity in disguise. Apply $\Delta U = Q - W_{\text{by}} = Q + W_{\text{on}}$ and the defining condition of the named process.

**(a)** Isochoric: $W = 0$ ⇒ $\Delta U = Q$. The energy transfer (heat) equals the change in internal energy. **True** ✓
**(b)** Isothermal: $\Delta U = 0$ ⇒ $Q = W_{\text{by}}$. Heat in equals work done by the gas. **True** ✓
**(c)** "ΔU = Q − $W_{\text{on}}$" — wrong sign. The first law gives $\Delta U = Q + W_{\text{on}}$ (or $Q - W_{\text{by}}$). The minus sign in the statement double-counts the sign flip. **False** ✓
**(d)** Adiabatic: $Q=0$ ⇒ $\Delta U = -W_{\text{by}} = W_{\text{on}}$. With no heat flow, all work done on the gas becomes internal energy. **True** ✓

---

## Q16 — Name the process

Each named ideal-gas process pins down one of the four state quantities (T, V, p) or the heat flow Q.

- $\Delta U = 0$ (for an ideal gas this means $\Delta T = 0$) → **isothermal** ✓
- $W = 0$ requires no volume change → **isochoric** ✓
- $Q = 0$ defines the no-heat-flow process → **adiabatic** ✓

---

**All numeric answers match the source key.**
