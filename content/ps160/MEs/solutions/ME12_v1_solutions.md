# ME12: Fluid Mechanics — Walkthrough

**Module:** M12 (Fluid Mechanics) — see [m12/Fluid_Mechanics.md](../../m12/Fluid_Mechanics.md), [m12/M12_summary.md](../../m12/M12_summary.md)

**Core equations used in this ME**
- Density: $\rho = m/V$; sphere volume $V = \tfrac{4}{3}\pi r^3$; cylinder volume $V=\pi r^2 L$
- Mixture density: $\rho_{\text{mix}} = \dfrac{m_1+m_2}{V_1+V_2} = \dfrac{m_1+m_2}{m_1/\rho_1 + m_2/\rho_2}$
- Pressure from a force on a surface: $p = F/A$ (with $F=mg$)
- Hydrostatic pressure: $p = p_0 + \rho g h$
- Barometer: $p_0 = \rho g (h_2 - h_1)$
- Pascal's principle (hydraulic): $\dfrac{F_1}{A_1}=\dfrac{F_2}{A_2}$
- Buoyancy (Archimedes): $B = \rho_{\text{fluid}}\, V_{\text{disp}}\, g$
- Continuity: $A_1 v_1 = A_2 v_2$
- Torricelli (efflux): $v = \sqrt{2gh}$
- Bernoulli (horizontal): $p_1 + \tfrac{1}{2}\rho v_1^2 = p_2 + \tfrac{1}{2}\rho v_2^2$

Assume $g = 9.80\ \text{m/s}^2$ unless the problem states otherwise.

---

## Q1 — Density of a sphere

**Given:** $m = 454$ kg, $r = 1$ m. **Find:** $\rho$.

**Equation:** $\rho = m/V$ with $V = \tfrac{4}{3}\pi r^3$.

$$V = \tfrac{4}{3}\pi(1)^3 = 4.18879\ \text{m}^3$$
$$\rho = \dfrac{454}{4.18879} = \boxed{108.3846\ \text{kg/m}^3}\ \checkmark$$

---

## Q2 — Alloy density

**Given:** $m_s = 4.3$ kg ($\rho_s = 10{,}490$), $m_g = 2.3$ kg ($\rho_g = 19{,}300$).

**Idea:** Mass adds, volumes add — so use $\rho_{\text{mix}} = \dfrac{m_s+m_g}{m_s/\rho_s + m_g/\rho_g}$.

$$V_s = \frac{4.3}{10490} = 4.0992\times10^{-4}\ \text{m}^3,\quad V_g = \frac{2.3}{19300} = 1.1917\times10^{-4}\ \text{m}^3$$
$$V_{\text{tot}} = 5.2909\times10^{-4}\ \text{m}^3$$
$$\rho = \frac{6.6}{5.2909\times10^{-4}} = \boxed{12{,}474.36\ \text{kg/m}^3}\ \checkmark$$

---

## Q3 — Pressure under a cube

**Given:** $m = 40$ kg, side $L = 0.19$ m, $g = 2.9\ \text{m/s}^2$.

**Equation:** $p = F/A = mg / L^2$.

$$F = mg = 40\cdot 2.9 = 116\ \text{N},\quad A = (0.19)^2 = 0.0361\ \text{m}^2$$
$$p = \dfrac{116}{0.0361} = \boxed{3{,}213.30\ \text{Pa}}\ \checkmark$$

---

## Q4 — Barometer

**Given:** $h_1 = 3.9$ cm, $h_2 = 31$ cm, $\rho = 6{,}282\ \text{kg/m}^3$.

A barometer reads ambient pressure as the column height $\Delta h = h_2 - h_1$ of fluid that the atmosphere can support: $p_0 = \rho g\,\Delta h$.

$$\Delta h = 0.271\ \text{m}$$
$$p_0 = 6282 \cdot 9.80 \cdot 0.271 = 16{,}683.7\ \text{Pa} = \boxed{16.6837\ \text{kPa}}\ \checkmark$$

---

## Q5 — Pressure below the surface of a fluid

**Given:** $g = 8.3\ \text{m/s}^2$, $p_{\text{atm}} = 80{,}512$ Pa, $h = 7.4$ m, $\rho = 936\ \text{kg/m}^3$.

**Equation:** $p = p_{\text{atm}} + \rho g h$.

$$\rho g h = 936\cdot 8.3\cdot 7.4 = 57{,}489.12\ \text{Pa}$$
$$p = 80{,}512 + 57{,}489.12 = \boxed{138{,}001.12\ \text{Pa}}\ \checkmark$$

---

## Q6 — Gauge pressure under a floating disk + potato

**Given:** cylinder $r = 5.1$ cm, oil $\rho_o = 810\ \text{kg/m}^3$, disk $m_d = 2.9$ kg, potato $m_p = 0.5$ kg, depth from oil surface $h = 13.2$ cm. Want gauge pressure at that depth in psi.

**Idea:** "Gauge" means we drop $p_{\text{atm}}$. The oil surface still has the disk+potato weight pressing down, so

$$p_{\text{gauge}} = \underbrace{\dfrac{(m_d+m_p)g}{\pi r^2}}_{\text{from weight on top}} + \underbrace{\rho_o g h}_{\text{oil column}}$$

$$A = \pi(0.051)^2 = 8.1713\times10^{-3}\ \text{m}^2$$
$$\dfrac{(3.4)(9.80)}{8.1713\times10^{-3}} = 4{,}077.48\ \text{Pa}$$
$$\rho_o g h = 810\cdot 9.80\cdot 0.132 = 1{,}047.82\ \text{Pa}$$
$$p_{\text{gauge}} = 5{,}125.30\ \text{Pa}$$
$$p = \dfrac{5{,}125.30}{6{,}895} = \boxed{0.7434\ \text{psi}}\ \checkmark$$

---

## Q7 — Hydraulic jack

**Given:** $A_1 = 0.05\ \text{m}^2$, $A_2 = 0.17\ \text{m}^2$, $F_2 = 1{,}243$ N. **Find:** $F_1$.

**Equation:** Pascal: $F_1/A_1 = F_2/A_2 \Rightarrow F_1 = F_2 (A_1/A_2)$.

$$F_1 = 1243 \cdot \dfrac{0.05}{0.17} = \boxed{365.588\ \text{N}}\ \checkmark$$

---

## Q8 — Hydraulic brake torque

**Given:** $A_1 = 1.7\ \text{cm}^2$, $A_2 = 7.4\ \text{cm}^2$, $\mu = 0.5$, $r_{\text{wheel}} = 0.45$ m, $F_{\text{pedal}} = 49$ N.

**Idea:** pedal force → hydraulic force on shoe → friction force on drum → torque.

$$F_{\text{shoe}} = F_{\text{pedal}}\dfrac{A_2}{A_1} = 49 \cdot \dfrac{7.4}{1.7} = 213.294\ \text{N}$$
$$f = \mu F_{\text{shoe}} = 0.5\cdot 213.294 = 106.647\ \text{N}$$
$$\tau = f\cdot r_{\text{wheel}} = 106.647\cdot 0.45 = \boxed{47.991\ \text{N·m}}\ \checkmark$$

(Areas appear as a ratio, so cm² vs m² cancels — no unit conversion needed.)

---

## Q9 — Buoyant force, fully submerged

**Given:** $m = 7.8$ kg, $V = 0.3\ \text{m}^3$, $\rho_f = 609\ \text{kg/m}^3$, $g = 6.3\ \text{m/s}^2$.

**Equation:** $B = \rho_f V g$ (volume displaced = object volume since fully submerged).

$$B = 609\cdot 0.3\cdot 6.3 = \boxed{1{,}151.01\ \text{N}}\ \checkmark$$

(Object mass is a distractor for $B$.)

---

## Q10 — Tension on a submerged rock

**Given:** rock $m = 6.4$ kg, $\rho_r = 3.1\times10^3\ \text{kg/m}^3$, water $\rho_w = 1000$.

**Idea:** Static equilibrium: $T + B = W$ ⇒ $T = mg - \rho_w V g$, with $V = m/\rho_r$.

$$V = 6.4/3100 = 2.0645\times10^{-3}\ \text{m}^3$$
$$W = 6.4\cdot 9.80 = 62.72\ \text{N};\quad B = 1000\cdot 2.0645\times10^{-3}\cdot 9.80 = 20.232\ \text{N}$$
$$T = 62.72 - 20.232 = \boxed{42.488\ \text{N}}\ \checkmark$$

Or compactly: $T = mg(1 - \rho_w/\rho_r) = 62.72\cdot(1 - 1/3.1) = 42.488$ N.

---

## Q11 — Continuity in a narrowing pipe

**Given:** $r_1 = 1.1$ m, $v_1 = 2.9$ m/s, $r_2 = 0.4$ m.

**Equation:** $A_1 v_1 = A_2 v_2 \Rightarrow v_2 = v_1 (r_1/r_2)^2$.

$$v_2 = 2.9\cdot (1.1/0.4)^2 = 2.9\cdot 7.5625 = \boxed{21.9313\ \text{m/s}}\ \checkmark$$

---

## Q12 — Hose flow speed filling a pool

**Given:** hose $r = 0.03$ m, pool $10\times 3\times 4$ m³ in $t = 3.5$ hr $= 12{,}600$ s.

$$Q = \dfrac{V}{t} = \dfrac{120}{12600} = 9.5238\times10^{-3}\ \text{m}^3/\text{s}$$
$$A_{\text{hose}} = \pi(0.03)^2 = 2.8274\times10^{-3}\ \text{m}^2$$
$$v = Q/A = \boxed{3.3684\ \text{m/s}}\ \checkmark$$

(The problem says "10 m in width, 3 m in width" — treat them as length × width; volume $=10\cdot 3\cdot 4 = 120\ \text{m}^3$.)

---

## Q13 — Torricelli's theorem (tank leak)

**Given:** depth filled = 16.3 m; leak at 8 m above bottom. **Find:** efflux speed.

**Idea:** Bernoulli from open surface (atm, $v\approx 0$) to leak (atm, speed $v$) gives $v = \sqrt{2gh}$ with $h$ = depth of leak below surface.

$$h = 16.3 - 8 = 8.3\ \text{m}$$
$$v = \sqrt{2\cdot 9.80\cdot 8.3} = \sqrt{162.68} = \boxed{12.7546\ \text{m/s}}\ \checkmark$$

---

## Q14 — Bernoulli in a horizontal narrowing pipe

**Given:** $r_1=0.25$ m, $v_1=2.3$ m/s, $p_1=239$ kPa; $r_2=0.11$ m; $\rho=1000$.

**Steps:** Continuity → $v_2$. Bernoulli (no height change) → $p_2$.

$$v_2 = v_1\left(\frac{r_1}{r_2}\right)^2 = 2.3\cdot 5.16529 = 11.8802\ \text{m/s}$$
$$p_2 = p_1 + \tfrac{1}{2}\rho(v_1^2 - v_2^2) = 239000 + 500\cdot(5.29 - 141.138)$$
$$p_2 = 239000 - 67{,}924.1 = 171{,}075.9\ \text{Pa} = \boxed{171.076\ \text{kPa}}\ \checkmark$$

(Sanity: faster fluid → lower pressure, as expected.)

---

## Q15 — Conceptual: what causes buoyancy?

**Answer:** *The buoyant force is a result of increasing pressure with depth.* ✓

The bottom of a submerged body sits at greater depth than the top, so fluid pressure (which grows linearly with depth, $p = p_0 + \rho g h$) pushes harder up on the bottom face than down on the top face. The net upward force is $B = \rho_f V g$ — Archimedes' principle is a *consequence* of the depth-dependent hydrostatic pressure.

Why the others are wrong: $B$ depends on submerged volume; with equal masses the *less* dense object has more volume → more $B$; $B$ comes from the displaced *fluid's* weight, not the object's; $B$ can be less than, equal to, or greater than the object's weight (sink/float/rise).

---

## Q16 — Two metal balls, equal radii, both at the bottom

**Answer:** *The buoyant forces on the balls are the same.* ✓

$B = \rho_{\text{water}} V g$. Both balls have the same $V$ (same radius, fully submerged), so the same $B$ regardless of what they're made of. The *net* force differs because the gold ball is heavier — but $B$ alone is identical.

---

**All 16 answers match the source key.**
