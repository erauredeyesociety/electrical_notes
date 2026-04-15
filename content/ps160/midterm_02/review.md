# PS160 Midterm 2 --- Topics and Theory Review

**Scope:** Modules 17 (Temperature and Heat), 18 (Thermal Properties of Matter / Kinetic Theory), 19 (First Law of Thermodynamics), 20 (Second Law of Thermodynamics / Entropy).

See [equations.tex](equations.tex) for the equation sheet, [knowledge_ps160_mid02.pdf](knowledge_ps160_mid02.pdf) for the knowledge questions, and [Study_guide_mt2.pdf](Study_guide_mt2.pdf) for the official study guide.

---

## Module 17 --- Temperature and Heat

### Topics
- Temperature and thermometers
- Thermal expansion (linear and volumetric)
- Thermal stress
- Quantity of heat, specific heat, heat capacity
- Phase changes and latent heat
- Calorimetry
- Heat transfer: conduction, convection, radiation

### Theory

**Temperature** is the quantity that is equal between two bodies in thermal equilibrium (zeroth law). SI unit is Kelvin; $T_K = T_C + 273.15$. Absolute zero is $0$ K.

**Thermal expansion:** Most materials expand when heated. Linear: $\Delta L = \alpha L_0\,\Delta T$. Volumetric: $\Delta V = \beta V_0\,\Delta T$ with $\beta = 3\alpha$ for isotropic solids. Water is anomalous near 4°C — contracts on warming from 0 to 4°C.

**Thermal stress:** A rigidly constrained rod that is prevented from expanding develops stress $F/A = -Y\alpha\,\Delta T$ (Young's modulus times the thermal strain you removed).

**Heat** is energy transferred due to a temperature difference. $Q = mc\,\Delta T$ (specific heat $c$, J/(kg·K)) or $Q = nC\,\Delta T$ (molar heat capacity $C$, J/(mol·K)). Key constants: $c_{\text{water}} = 4190$ J/(kg·K).

**Latent heat:** During a phase change, $Q = \pm mL$ (sign depends on melting vs. freezing, vaporization vs. condensation). $L_f$ = heat of fusion, $L_v$ = heat of vaporization. Temperature stays constant during the phase change.

**Calorimetry:** In an isolated system, $\sum Q_i = 0$. You set up heat transfers between the hot and cold objects (including any phase changes that occur) and solve for the final temperature.

**Conduction:** $H = dQ/dt = kA\,\Delta T/L$ for steady-state through a slab of thickness $L$, area $A$, thermal conductivity $k$. For slabs in series, add thermal resistances $L/(kA)$.

**Radiation:** A surface at temperature $T$ radiates $H = e A\sigma T^4$ where $e$ is emissivity ($e = 1$ for a blackbody), $\sigma = 5.67\times 10^{-8}$ W/(m²·K⁴). Net radiation to surroundings: $H_{\text{net}} = e A\sigma(T^4 - T_s^4)$.

**Convection** is qualitative on this exam — you should recognize natural vs. forced and why it's hard to model analytically.

### Common problem archetypes
- Two-block calorimetry, possibly with a phase change.
- Bimetallic strip / expansion gap.
- Steady-state conduction through composite wall.
- Radiation balance for an object in a room.

---

## Module 18 --- Thermal Properties of Matter / Kinetic Theory

### Topics
- Equations of state / ideal gas law
- Kinetic theory of an ideal gas
- Equipartition of energy and degrees of freedom
- Molar heat capacities
- Maxwell-Boltzmann distribution
- Phases of matter (brief)

### Theory

**Ideal gas law:** $pV = nRT = NkT$, where $R = 8.314$ J/(mol·K), $k = 1.38\times 10^{-23}$ J/K, and $N = nN_A$. Valid in the low-density / high-temperature limit where intermolecular forces and molecular volume are negligible.

**Kinetic theory:** Treat a gas as many point particles undergoing elastic collisions with the container walls. Derivation gives $pV = \tfrac{1}{3}Nm\langle v^2\rangle$, and comparison with the ideal gas law yields $\tfrac{1}{2}m\langle v^2\rangle = \tfrac{3}{2}kT$. This is the **translational kinetic energy per molecule**.

**Root-mean-square speed:** $v_{\text{rms}} = \sqrt{3kT/m} = \sqrt{3RT/M}$ where $M$ is molar mass. Lighter molecules move faster at the same temperature.

**Equipartition theorem:** Each quadratic degree of freedom (a $\tfrac{1}{2}$-something-squared term in the energy) contributes $\tfrac{1}{2}kT$ of energy per molecule at temperature $T$. So a monatomic gas ($f = 3$, just translation) has $U = \tfrac{3}{2}NkT$. A diatomic gas at room temperature adds 2 rotational d.o.f. → $f = 5$ → $U = \tfrac{5}{2}NkT$. Vibrational modes unfreeze only at high $T$.

**Molar heat capacities:** $C_V = (f/2)R$. For any ideal gas: $C_P = C_V + R$ (extra work done at constant $p$). Ratio $\gamma = C_P/C_V$ (monatomic: 5/3, diatomic: 7/5). For solids, Dulong--Petit gives $C_V = 3R$ (3 d.o.f. × 2 from kinetic+potential).

**Maxwell-Boltzmann distribution:** $f(v) \propto v^2 e^{-mv^2/(2kT)}$. Peak is the most probable speed $v_p = \sqrt{2kT/m}$, average speed $\bar v = \sqrt{8kT/(\pi m)}$, and $v_{\text{rms}} = \sqrt{3kT/m}$. They're ordered $v_p < \bar v < v_{\text{rms}}$.

### Common problem archetypes
- Given two of $p$, $V$, $T$, $n$, find the fourth (with unit conversions).
- Find $v_{\text{rms}}$ given $T$ and gas species.
- Predict heat capacity from number of degrees of freedom.
- Compare two different gases at the same temperature.

---

## Module 19 --- First Law of Thermodynamics

### Topics
- Thermodynamic systems, state variables, processes
- Work done by and on a gas
- Heat and the first law of thermodynamics
- Internal energy of an ideal gas
- Specific processes: isobaric, isochoric, isothermal, adiabatic
- $pV$ diagrams

### Theory

**State variables** ($p$, $V$, $T$, $U$, $S$) depend only on the current state of a system, not on how it got there. **Path variables** ($Q$, $W$) depend on the process.

**Work done by a gas:** $W = \int p\,dV$. On a $pV$ diagram, $W$ is the area under the curve. Expansion: $W > 0$; compression: $W < 0$.

**First law:** $\Delta U = Q - W$ where $Q$ is heat added to the system and $W$ is work done *by* the system. (Different conventions exist; PS160 uses this "engineering" convention.) Internal energy $U$ is a state variable.

**Ideal gas internal energy depends only on $T$:** $U = nC_V T$, so $\Delta U = nC_V\,\Delta T$ regardless of the process — important when computing $Q$ or $W$ for a non-isochoric process.

**Four idealized processes on an ideal gas:**

1. **Isobaric** ($p$ const): $W = p\,\Delta V$. $Q = nC_P\,\Delta T$. $\Delta U = nC_V\,\Delta T$.
2. **Isochoric** ($V$ const): $W = 0$. $Q = nC_V\,\Delta T = \Delta U$.
3. **Isothermal** ($T$ const): $\Delta U = 0$ so $Q = W = nRT\ln(V_2/V_1)$.
4. **Adiabatic** ($Q = 0$): $\Delta U = -W$. Follows $pV^{\gamma} = $ const and $TV^{\gamma-1} = $ const. $W = (p_1V_1 - p_2V_2)/(\gamma - 1)$.

**Cycles:** For any closed loop on a $pV$ diagram, $\Delta U_{\text{cycle}} = 0$, so $W_{\text{net}} = Q_{\text{net}}$. The net work is the area enclosed by the loop (positive if traversed clockwise).

### Common problem archetypes
- Trace a multi-step cycle on a $pV$ diagram and compute $Q$, $W$, $\Delta U$ for each leg and for the cycle.
- Adiabatic compression: given $V_1$, $V_2$, $p_1$, find $p_2$ and $T_2$.
- Compare the work done by two different paths between the same endpoints (work depends on path; $\Delta U$ does not).

---

## Module 20 --- Second Law of Thermodynamics / Entropy

### Topics
- Direction of thermodynamic processes
- Heat engines and efficiency
- Refrigerators and heat pumps
- Second law statements (Kelvin-Planck, Clausius)
- Carnot cycle
- Entropy and disorder
- Microscopic interpretation ($S = k\ln w$)

### Theory

**Second law** has several equivalent forms:
- *Kelvin-Planck:* No process can convert heat entirely into work (no 100% efficient engine).
- *Clausius:* Heat cannot spontaneously flow from cold to hot.
- *Entropy:* $\Delta S_{\text{universe}} \ge 0$ for any process; equality for reversible processes only.

**Heat engine** takes heat $Q_H$ from a hot reservoir, does work $W$, and dumps heat $|Q_C|$ to a cold reservoir. Efficiency:
$$e = \frac{W}{Q_H} = 1 - \frac{|Q_C|}{Q_H}$$

**Refrigerator** is a heat engine running backward: work input $W$ moves heat $Q_C$ from cold to hot. Coefficient of performance $K = Q_C/|W|$. A **heat pump** is the same device operated to deliver heat; its COP is $|Q_H|/|W|$.

**Carnot cycle** is a reversible cycle consisting of two isotherms (at $T_H$ and $T_C$) and two adiabats. It is the **most efficient cycle possible between two reservoirs**, with efficiency
$$e_{\text{Carnot}} = 1 - \frac{T_C}{T_H}.$$
Any engine with higher efficiency than Carnot would violate the second law. Corollary: no engine operating between two temperatures can do better than Carnot; all reversible engines operating between the same two temperatures have the same efficiency.

**Entropy** is defined by $\Delta S = \int dQ_{\text{rev}}/T$ — integrate along any reversible path connecting the two states. Because $S$ is a state variable, you can always pick the easiest reversible path. Examples:
- Isothermal ideal gas: $\Delta S = nR\ln(V_2/V_1)$.
- Heating: $\Delta S = mc\ln(T_2/T_1)$.
- Phase change at $T$: $\Delta S = \pm mL/T$.

**Microscopic view:** $S = k\ln w$ where $w$ is the number of microstates. More disordered = more microstates = higher entropy. Statistical origin of the second law: macroscopic evolution is overwhelmingly likely toward the most probable (highest-$w$) macrostate.

**Carnot entropy check:** For a complete Carnot cycle, $\Delta S_{\text{gas}} = Q_H/T_H + Q_C/T_C = 0$, consistent with $S$ being a state variable.

### Common problem archetypes
- Given $T_H$ and $T_C$, find max efficiency; compare to a quoted real efficiency.
- Heat pump / fridge COP computations.
- Entropy change of: isothermal ideal gas; object brought from $T_1$ to $T_2$; mixing two bodies.
- Entropy change of the universe for a heat transfer across a finite $\Delta T$ (always positive).

---

## Cross-module connections
- The temperature in modules 17-18 feeds the processes in 19 and the efficiency formulas in 20.
- $nC_V\,\Delta T$ is the bridge: $C_V$ comes from equipartition (M18), used in first-law process analysis (M19) and in entropy integrals (M20).
- Carnot efficiency $1 - T_C/T_H$ is the single most cited formula from M20 — know it absolutely.

## Tips for exam prep
1. Practice drawing and labeling $pV$ diagrams. Know how each process (isobaric/isochoric/isothermal/adiabatic) looks.
2. On cycle problems, tabulate $Q$, $W$, $\Delta U$ for each leg and sum; sanity-check with $\Delta U_{\text{cycle}} = 0$.
3. Don't confuse **heat** (path) and **internal energy** (state). $Q$ depends on the process; $\Delta U$ for an ideal gas only on $\Delta T$.
4. Sign conventions: $Q > 0$ into system, $W > 0$ done by system.
5. Entropy problems: pick a reversible path for the computation even if the actual process is irreversible — the answer is the same because $S$ is a state variable.
