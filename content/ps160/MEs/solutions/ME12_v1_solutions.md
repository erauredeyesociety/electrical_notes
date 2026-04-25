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

We have a uniform spherical ball with known mass and radius and we need its density. Because mass is uniformly distributed throughout the volume, $\rho = m/V$ applies directly; the only modeling choice is computing the sphere volume from its radius.

**Given:** $m = 454$ kg, $r = 1$ m. **Find:** $\rho$.

**Equation:** $\rho = m/V$ with $V = \tfrac{4}{3}\pi r^3$.

$$V = \tfrac{4}{3}\pi(1)^3 = 4.18879\ \text{m}^3$$
$$\rho = \dfrac{454}{4.18879} = \boxed{108.3846\ \text{kg/m}^3}\ \checkmark$$

---

## Q2 — Alloy density

Two metals are melted together to form an alloy. The total mass is just the sum of the two component masses, and (assuming no chemical volume change) the total volume is the sum of the two volumes. So the alloy's density is the *combined* mass divided by the *combined* volume — not the average of the two densities.

**Given:** $m_s = 4.3$ kg ($\rho_s = 10{,}490$), $m_g = 2.3$ kg ($\rho_g = 19{,}300$).

**Idea:** Mass adds, volumes add — so use $\rho_{\text{mix}} = \dfrac{m_s+m_g}{m_s/\rho_s + m_g/\rho_g}$.

$$V_s = \frac{4.3}{10490} = 4.0992\times10^{-4}\ \text{m}^3,\quad V_g = \frac{2.3}{19300} = 1.1917\times10^{-4}\ \text{m}^3$$
$$V_{\text{tot}} = 5.2909\times10^{-4}\ \text{m}^3$$
$$\rho = \frac{6.6}{5.2909\times10^{-4}} = \boxed{12{,}474.36\ \text{kg/m}^3}\ \checkmark$$

---

## Q3 — Pressure under a cube

A cube sits on a flat surface and we want the pressure it exerts on the surface. Pressure is force per area: the contact area is one square face of the cube ($L^2$), and the force is the cube's weight $mg$ using the local gravity. Vacuum just means we don't add atmospheric pressure on top.

**Given:** $m = 40$ kg, side $L = 0.19$ m, $g = 2.9\ \text{m/s}^2$.

**Equation:** $p = F/A = mg / L^2$.

$$F = mg = 40\cdot 2.9 = 116\ \text{N},\quad A = (0.19)^2 = 0.0361\ \text{m}^2$$
$$p = \dfrac{116}{0.0361} = \boxed{3{,}213.30\ \text{Pa}}\ \checkmark$$

---

## Q4 — Barometer

A barometer is a closed tube of fluid inverted in a reservoir; atmospheric pressure pushes the fluid up the tube, and the height it rises measures the pressure. Here $h_2-h_1$ is the column length the atmosphere supports, so $p_0 = \rho g (h_2 - h_1)$. The two heights are heights of the two fluid surfaces from a common reference, so subtracting gives the column length directly.

**Given:** $h_1 = 3.9$ cm, $h_2 = 31$ cm, $\rho = 6{,}282\ \text{kg/m}^3$.

$$\Delta h = 0.271\ \text{m}$$
$$p_0 = 6282 \cdot 9.80 \cdot 0.271 = 16{,}683.7\ \text{Pa} = \boxed{16.6837\ \text{kPa}}\ \checkmark$$

---

## Q5 — Pressure below the surface of a fluid

We want the *absolute* pressure at depth $h$ below a fluid's free surface. The pressure at the surface is the atmospheric pressure pressing down on it, and as we descend we accumulate the weight per area of fluid above us — that's the $\rho g h$ term. Add the two and we have the total pressure at depth.

**Given:** $g = 8.3\ \text{m/s}^2$, $p_{\text{atm}} = 80{,}512$ Pa, $h = 7.4$ m, $\rho = 936\ \text{kg/m}^3$.

**Equation:** $p = p_{\text{atm}} + \rho g h$.

$$\rho g h = 936\cdot 8.3\cdot 7.4 = 57{,}489.12\ \text{Pa}$$
$$p = 80{,}512 + 57{,}489.12 = \boxed{138{,}001.12\ \text{Pa}}\ \checkmark$$

---

## Q6 — Gauge pressure under a floating disk + potato

A wooden disk and a potato float on top of an oil column inside a cylinder. We want the gauge (above-atmospheric) pressure 13.2 cm under the oil's surface. Two contributions push down on that depth: the weight of the disk+potato spread over the cylinder cross-section (equivalent to an extra surface pressure), plus the hydrostatic column of oil itself. Then convert Pa → psi at the end since the question asks for psi.

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

A hydraulic jack is two pistons connected by an incompressible fluid. Pascal's principle says pressure is the same throughout the fluid, so $F_1/A_1 = F_2/A_2$. Force is amplified by the area ratio — a larger output piston gives a larger output force for the same input force. Here we know the output force and want the (smaller) input force needed.

**Given:** $A_1 = 0.05\ \text{m}^2$, $A_2 = 0.17\ \text{m}^2$, $F_2 = 1{,}243$ N. **Find:** $F_1$.

**Equation:** Pascal: $F_1/A_1 = F_2/A_2 \Rightarrow F_1 = F_2 (A_1/A_2)$.

$$F_1 = 1243 \cdot \dfrac{0.05}{0.17} = \boxed{365.588\ \text{N}}\ \checkmark$$

---

## Q8 — Hydraulic brake torque

A driver pushes the pedal with force $F_{\text{pedal}}$ on the master cylinder ($A_1$), which (Pascal) creates a larger force on the brake-shoe cylinder ($A_2$). That shoe pushes against the rotating drum with normal force $F_{\text{shoe}}$; the kinetic friction force is $\mu F_{\text{shoe}}$ tangent to the drum, applied at the wheel radius — so the friction torque about the axle is $\tau = \mu F_{\text{shoe}}\, r_{\text{wheel}}$.

**Given:** $A_1 = 1.7\ \text{cm}^2$, $A_2 = 7.4\ \text{cm}^2$, $\mu = 0.5$, $r_{\text{wheel}} = 0.45$ m, $F_{\text{pedal}} = 49$ N.

**Idea:** pedal force → hydraulic force on shoe → friction force on drum → torque.

$$F_{\text{shoe}} = F_{\text{pedal}}\dfrac{A_2}{A_1} = 49 \cdot \dfrac{7.4}{1.7} = 213.294\ \text{N}$$
$$f = \mu F_{\text{shoe}} = 0.5\cdot 213.294 = 106.647\ \text{N}$$
$$\tau = f\cdot r_{\text{wheel}} = 106.647\cdot 0.45 = \boxed{47.991\ \text{N·m}}\ \checkmark$$

(Areas appear as a ratio, so cm² vs m² cancels — no unit conversion needed.)

---

## Q9 — Buoyant force, fully submerged

An object is fully submerged in a fluid. Archimedes says the buoyant force equals the weight of the *displaced fluid*. Since the object is completely under, the displaced volume equals the object's own volume. The object's mass is irrelevant to $B$ — it would only matter if you were asked whether the object floats or what the net force is.

**Given:** $m = 7.8$ kg, $V = 0.3\ \text{m}^3$, $\rho_f = 609\ \text{kg/m}^3$, $g = 6.3\ \text{m/s}^2$.

**Equation:** $B = \rho_f V g$ (volume displaced = object volume since fully submerged).

$$B = 609\cdot 0.3\cdot 6.3 = \boxed{1{,}151.01\ \text{N}}\ \checkmark$$

(Object mass is a distractor for $B$.)

---

## Q10 — Tension on a submerged rock

A rock hangs from a cord, fully submerged in water. Three forces act on it: gravity (down), buoyancy (up), and cord tension (up). Static equilibrium: $T + B = W$, so $T = W - B$. We don't know the rock's volume directly, but we can compute it from its mass and density via $V = m/\rho_r$.

**Given:** rock $m = 6.4$ kg, $\rho_r = 3.1\times10^3\ \text{kg/m}^3$, water $\rho_w = 1000$.

**Idea:** Static equilibrium: $T + B = W$ ⇒ $T = mg - \rho_w V g$, with $V = m/\rho_r$.

$$V = 6.4/3100 = 2.0645\times10^{-3}\ \text{m}^3$$
$$W = 6.4\cdot 9.80 = 62.72\ \text{N};\quad B = 1000\cdot 2.0645\times10^{-3}\cdot 9.80 = 20.232\ \text{N}$$
$$T = 62.72 - 20.232 = \boxed{42.488\ \text{N}}\ \checkmark$$

Or compactly: $T = mg(1 - \rho_w/\rho_r) = 62.72\cdot(1 - 1/3.1) = 42.488$ N.

---

## Q11 — Continuity in a narrowing pipe

Continuity says incompressible flow conserves volume rate: $A_1 v_1 = A_2 v_2$. A pipe narrowing from radius 1.1 m to 0.4 m has its cross-sectional area shrink by a factor of $(1.1/0.4)^2$, so the speed must increase by that same factor to push the same volume per second through the smaller opening.

**Given:** $r_1 = 1.1$ m, $v_1 = 2.9$ m/s, $r_2 = 0.4$ m.

**Equation:** $A_1 v_1 = A_2 v_2 \Rightarrow v_2 = v_1 (r_1/r_2)^2$.

$$v_2 = 2.9\cdot (1.1/0.4)^2 = 2.9\cdot 7.5625 = \boxed{21.9313\ \text{m/s}}\ \checkmark$$

---

## Q12 — Hose flow speed filling a pool

A hose fills a known pool volume in a known time, giving us the volumetric flow rate $Q = V/t$. Continuity then ties $Q = A_{\text{hose}} v_{\text{hose}}$, so the water exits the hose at $v = Q/A$. Convert hours to seconds and watch the hose radius (cm vs m).

**Given:** hose $r = 0.03$ m, pool $10\times 3\times 4$ m³ in $t = 3.5$ hr $= 12{,}600$ s.

$$Q = \dfrac{V}{t} = \dfrac{120}{12600} = 9.5238\times10^{-3}\ \text{m}^3/\text{s}$$
$$A_{\text{hose}} = \pi(0.03)^2 = 2.8274\times10^{-3}\ \text{m}^2$$
$$v = Q/A = \boxed{3.3684\ \text{m/s}}\ \checkmark$$

(The problem says "10 m in width, 3 m in width" — treat them as length × width; volume $=10\cdot 3\cdot 4 = 120\ \text{m}^3$.)

---

## Q13 — Torricelli's theorem (tank leak)

A tank is open at the top with a leak in the side. Apply Bernoulli between the open top (atmospheric pressure, slow descent — call $v\approx 0$) and the leak hole (atmospheric pressure outside). The pressure terms cancel, leaving $\tfrac12 v^2 = g h$ where $h$ is the *vertical drop from surface to leak* — that is Torricelli's $v = \sqrt{2gh}$. Be careful: $h$ is the depth of the leak below the water *surface*, not the leak's height above the tank bottom.

**Given:** depth filled = 16.3 m; leak at 8 m above bottom. **Find:** efflux speed.

$$h = 16.3 - 8 = 8.3\ \text{m}$$
$$v = \sqrt{2\cdot 9.80\cdot 8.3} = \sqrt{162.68} = \boxed{12.7546\ \text{m/s}}\ \checkmark$$

---

## Q14 — Bernoulli in a horizontal narrowing pipe

A horizontal pipe narrows; we know the wide-section pressure and speed and want the narrow-section pressure. Two principles in series: continuity ($A_1 v_1 = A_2 v_2$) gives the new speed, then Bernoulli (with no height change) trades kinetic energy for pressure. Faster fluid has lower pressure — so the narrow side should come out below 239 kPa.

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

$B = \rho_{\text{water}} V g$. Both balls have the same $V$ (same radius, fully submerged), so the same $B$ regardless of what they're made of. The *net* force differs because the gold ball is heavier — but $B$ alone is identical. Density only matters for whether something floats or sinks; once both are submerged, only displaced volume sets $B$.

---

**All 16 answers match the source key.**
