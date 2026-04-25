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

$p=197$ kPa, $V_i=3.2 \to V_f=1.1\ \text{m}^3$.
$$W_{\text{by}} = p\,\Delta V = 197\cdot(1.1 - 3.2) = -413.7\ \text{kJ}$$
$$W_{\text{on}} = -W_{\text{by}} = \boxed{+413.7\ \text{kJ}}\ \checkmark$$

(Compression ⇒ surroundings do positive work on the gas.)

---

## Q2 — Two-step "step-down" $pV$ diagram

Standard step-down: start at $(V_1, p_2)$, expand isobarically to $V_2$, drop isochorically to $p_1$, then expand isobarically to $V_3$. Work is the sum of the two rectangles:
$$W_{\text{by}} = p_2(V_2 - V_1) + p_1(V_3 - V_2)$$
$$= 212(2 - 0.9) + 91(3 - 2) = 233.2 + 91 = \boxed{324.2\ \text{kJ}}\ \checkmark$$

---

## Q3 — V-shaped two-leg ramp, work *on* the gas

Path: $(V_1, p_2) \to (V_2, p_1)$ [ramp down] $\to (V_3, p_2)$ [ramp up]. Each leg's work is a trapezoid:
$$W_{\text{by}} = \tfrac{1}{2}(p_1+p_2)(V_2-V_1) + \tfrac{1}{2}(p_1+p_2)(V_3-V_2)$$
$$= \tfrac{1}{2}(p_1+p_2)(V_3-V_1) = \tfrac{1}{2}(172+415)(5.1-1.3)$$
$$= \tfrac{1}{2}(587)(3.8) = +1115.3\ \text{kJ}$$
$$W_{\text{on}} = \boxed{-1115.3\ \text{kJ}}\ \checkmark$$

---

## Q4 — First law

$Q = +644$ J absorbed; $W_{\text{by}} = 0.62(644) = 399.28$ J.
$$\Delta U = Q - W_{\text{by}} = 644 - 399.28 = \boxed{244.72\ \text{J}}\ \checkmark$$

---

## Q5 — Heat at constant volume (monatomic)

Constant $V$: $W = 0$, so $Q = \Delta U = (3/2)nR\Delta T = (3/2)V\,\Delta p$.
$$Q = 1.5(1.1)(208 - 116)\ \text{kPa·m}^3 = 1.5(1.1)(92) = \boxed{151.8\ \text{kJ}}\ \checkmark$$

---

## Q6 — Work at constant volume

Isochoric ⇒ $\boxed{W = 0}$ ✓.

---

## Q7 — Diatomic isobaric compression, $\Delta U$

$\Delta U = (5/2)nR\Delta T = (5/2)\,p\,\Delta V$.
$$= 2.5(225)(1.7 - 3.9) = 2.5(225)(-2.2) = \boxed{-1237.5\ \text{kJ}}\ \checkmark$$

---

## Q8 — Monatomic isobaric expansion, $W_{\text{by}}$

$$W_{\text{by}} = p\,\Delta V = 130(4 - 1.2) = 130(2.8) = \boxed{364\ \text{kJ}}\ \checkmark$$

---

## Q9 — Isothermal expansion, work *on* the gas

$$W_{\text{by}} = p_iV_i\ln(V_f/V_i) = 159(1.3)\ln(2/1.3) = 206.7(0.4308) = +89.04\ \text{kJ}$$
$$W_{\text{on}} = \boxed{-89.04\ \text{kJ}}\ \checkmark$$

---

## Q10 — Isothermal compression

$$W_{\text{by}} = p_iV_i\ln(V_f/V_i) = 120(3)\ln(1.2/3) = 360\ln(0.4) = 360(-0.9163) = \boxed{-329.86\ \text{kJ}}\ \checkmark$$

(Negative because work is done on the gas during compression.)

---

## Q11 — Diatomic adiabatic compression, $p_f$

$\gamma = 7/5 = 1.4$. $p_iV_i^\gamma = p_fV_f^\gamma \Rightarrow p_f = p_i(V_i/V_f)^\gamma$.
$$p_f = 81\,(2.8/1.4)^{1.4} = 81\cdot 2^{1.4} = 81(2.6390) = \boxed{213.76\ \text{kPa}}\ \checkmark$$

---

## Q12 — Monatomic adiabatic, find $p_f$ and $\Delta U$

$\gamma = 5/3$. $p_i = 10^5$ Pa, $V_i = 3$, $V_f = 1$.
$$p_f = p_i(V_i/V_f)^\gamma = 10^5\cdot 3^{5/3} = 10^5(6.240) = 624\ \text{kPa}\ \checkmark$$

For adiabatic: $W_{\text{by}} = (p_iV_i - p_fV_f)/(\gamma-1)$.
$$W_{\text{by}} = \dfrac{(10^5)(3) - (6.24\times 10^5)(1)}{2/3} = \dfrac{-3.24\times 10^5}{2/3} = -4.86\times 10^5\ \text{J}$$
$$\Delta U = -W_{\text{by}} = \boxed{+486\ \text{kJ}}\ \checkmark$$

(Adiabatic compression ⇒ internal energy rises.)

---

## Q13 — Monatomic adiabatic expansion, $\Delta U$

$\gamma = 5/3$, $V_i=1.4$, $V_f=2.6$, $p_i=304$ kPa.
$$p_f = 304(1.4/2.6)^{5/3} = 304(0.5385)^{1.6667} = 304(0.3563) = 108.32\ \text{kPa}$$
$$W_{\text{by}} = \dfrac{p_iV_i - p_fV_f}{\gamma-1} = \dfrac{304(1.4) - 108.32(2.6)}{2/3} = \dfrac{425.6 - 281.63}{0.6667}$$
$$= \dfrac{143.97}{0.6667} = +215.87\ \text{kJ}$$
$$\Delta U = -W_{\text{by}} = \boxed{-215.87\ \text{kJ}}\ \checkmark$$

(Expansion does work on surroundings ⇒ internal energy drops.)

---

## Q14 — Straight ramp on a $pV$ diagram

Trapezoidal area under straight segment from $(3, 146)$ to $(5, 541)$:
$$W_{\text{by}} = \tfrac{1}{2}(p_i+p_f)(V_f-V_i) = \tfrac{1}{2}(146+541)(2) = \boxed{687\ \text{kJ}}\ \checkmark$$

---

## Q15 — First-law statements

Apply $\Delta U = Q - W_{\text{by}} = Q + W_{\text{on}}$.

**(a)** Isochoric: $W = 0$ ⇒ $\Delta U = Q$. **True** ✓
**(b)** Isothermal: $\Delta U = 0$ ⇒ $Q = W_{\text{by}}$. **True** ✓
**(c)** "ΔU = Q − $W_{\text{on}}$" — wrong sign. The first law gives $\Delta U = Q + W_{\text{on}}$. **False** ✓
**(d)** Adiabatic: $Q=0$ ⇒ $\Delta U = -W_{\text{by}} = W_{\text{on}}$. **True** ✓

---

## Q16 — Name the process

- $\Delta U = 0$ → **isothermal** ✓
- $W = 0$ → **isochoric** ✓
- $Q = 0$ → **adiabatic** ✓

---

**All numeric answers match the source key.**
