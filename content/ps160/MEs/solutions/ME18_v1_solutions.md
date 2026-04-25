# ME18: Kinetic Theory & Calorimetry — Walkthrough

**Module:** M18 — see [m18/](../../m18/)

**Core equations**
- Ideal gas law: $PV = nRT = Nk_BT$, $R = 8.314\ \text{J/(mol·K)}$, $N_A = 6.022\times 10^{23}$, $k_B = R/N_A$
- Comparative form (fixed mass, no leaks): $\dfrac{P_1V_1}{T_1} = \dfrac{P_2V_2}{T_2}$ — generalize with $n_1, n_2$ if mass changes
- Mole/molecule conversions: $n = m/M$, $N = nN_A$
- Translational KE per molecule: $\langle KE\rangle = \tfrac{3}{2}k_BT$; for $n$ moles: $K_{\text{tr}} = \tfrac{3}{2}nRT$
- Equipartition: each quadratic dof contributes $\tfrac{1}{2}k_BT$; internal energy $U = \tfrac{f}{2}nRT$
- Speeds: $v_{\text{avg}} = \sqrt{8RT/(\pi M)}$, $v_{\text{rms}} = \sqrt{3RT/M}$, $v_p = \sqrt{2RT/M}$ (M in kg/mol)
- Avg of any signed component (e.g. $\langle v_x\rangle$) = 0 by symmetry
- $1$ atm $= 101{,}325$ Pa

---

## Q1 — Volume at STP

Direct application of $PV = nRT$ at standard conditions (1 atm, 273 K). The factor of $10^{-3}$ converts m³ to liters; expect roughly the textbook 22.4 L/mol scaled by 0.8.

$n=0.8$, $P=101325$ Pa, $T=273$ K.
$$V = \dfrac{nRT}{P} = \dfrac{0.8\cdot 8.314\cdot 273}{101325} = 0.01792\ \text{m}^3 = \boxed{17.92\ \text{L}}\ \checkmark$$

---

## Q2 — Combined gas law (no mass change)

A sealed gas sample undergoes a process where pressure becomes 1.9× and absolute temperature rises 85% (to 1.85× the original). Since no mass is exchanged, $PV/T$ is conserved, and the new volume comes from balancing the two factors.

$P_1V_1/T_1 = P_2V_2/T_2$ with $P_2 = 1.9P_1$ and $T_2 = 1.85T_1$:
$$V_2 = V_1\cdot\dfrac{P_1}{P_2}\cdot\dfrac{T_2}{T_1} = 1\cdot\dfrac{1}{1.9}\cdot 1.85 = \boxed{0.9737\ \text{m}^3}\ \checkmark$$

---

## Q3 — Solve for new temperature

A sealed sample changes to $0.9P_1$ and $0.7V_1$; with mass fixed, the temperature must drop because both $P$ and $V$ shrank. Use the combined gas law and solve for $T_2$.

$T_2 = T_1\cdot(P_2V_2)/(P_1V_1) = 297\cdot(0.9)(0.7) = 297(0.63) = \boxed{187.11\ \text{K}}\ \checkmark$

---

## Q4 — Tire with leak and warming

A tire warms by 19 °C while losing 9% of its gas through a nail puncture. Two complications: gauge pressure must be converted to absolute pressure (add 1 atm) before applying the gas law, and mole count changes, so use the generalized form $P_1V_1/(n_1T_1) = P_2V_2/(n_2T_2)$ with $V$ constant.

Initial absolute pressure: $P_1 = 211466 + 100000 = 311466$ Pa, $T_1 = 278.15$ K.
After: $T_2 = 297.15$ K, $n_2 = 0.91\,n_1$, $V$ unchanged.
$$\dfrac{P_2}{P_1} = \dfrac{n_2}{n_1}\cdot\dfrac{T_2}{T_1} = 0.91\cdot\dfrac{297.15}{278.15} = 0.91\cdot 1.0683 = 0.9722$$
$$P_2 = 311466\cdot 0.9722 = 302{,}810\ \text{Pa (abs)}$$
$$P_{\text{gauge}} = 302810 - 100000 = 202{,}810\ \text{Pa} = \dfrac{202810}{6895} = \boxed{29.41\ \text{psi}}\ \checkmark$$

---

## Q5 — Number of molecules in 77.1 ag of C₄H₈OH

Three-step conversion: attograms → grams, grams → moles via molar mass, moles → molecules via $N_A$. The molecular formula C₄H₈OH = C₄H₉O, giving $4(12.011)+9(1.008)+16.00 = 73.116$ g/mol.

Mass: $77.1\times 10^{-18}\ \text{g} = 7.71\times 10^{-17}$ g.
Molar mass of C₄H₉O (= C₄H₈OH): $4(12.011) + 9(1.008) + 16.00 = 73.116$ g/mol.
$$n = m/M = 7.71\times 10^{-17}/73.116 = 1.0545\times 10^{-18}\ \text{mol}$$
$$N = nN_A = 1.0545\times 10^{-18}\cdot 6.022\times 10^{23} = \boxed{6.351\times 10^5\ \text{molecules}}\ \checkmark$$

(Source key: 635,071.32 — within rounding of constants.)

---

## Q6 — Moles of AlCl₃ in 501 g

Compute the molar mass of AlCl₃ from atomic weights, then $n = m/M$.

$M = 26.98 + 3(35.45) = 133.33$ g/mol.
$n = 501/133.33 = \boxed{3.757\ \text{mol}}\ \checkmark$

---

## Q7 — Temperature from translational KE

The translational kinetic energy of $n$ moles of an ideal gas is $K_{\text{tr}} = \tfrac{3}{2}nRT$ (independent of molecular mass — only $T$ matters). Solve for $T$.

$K_{\text{tr}} = \tfrac{3}{2}nRT \Rightarrow T = \dfrac{2K}{3nR} = \dfrac{2(64356)}{3(8)(8.314)} = \boxed{645.02\ \text{K}}\ \checkmark$

---

## Q8 — Total KE of 7.6 mol at 90 °C

Plug 7.6 mol and $T=363.15$ K into $K_{\text{tr}}=\tfrac{3}{2}nRT$. Reminder: convert °C → K before using ideal-gas formulas.

$T = 363.15$ K.
$K_{\text{tr}} = \tfrac{3}{2}nRT = 1.5(7.6)(8.314)(363.15) = \boxed{34{,}407\ \text{J}}\ \checkmark$

---

## Q9 — Average speed of O₂ at 81.9 °C

Use the Maxwell–Boltzmann mean speed $v_{\text{avg}} = \sqrt{8RT/(\pi M)}$. Watch the molar mass: for *molecular* O₂, $M = 2(16.0)\,\text{g/mol} = 0.032$ kg/mol.

$T = 355.05$ K, $M_{\text{O}_2} = 0.032$ kg/mol.
$$v_{\text{avg}} = \sqrt{\dfrac{8RT}{\pi M}} = \sqrt{\dfrac{8(8.314)(355.05)}{\pi(0.032)}} = \sqrt{234{,}909} = \boxed{484.67\ \text{m/s}}\ \checkmark$$

---

## Q10 — Average $v_x$

Conceptual: although molecules zoom at hundreds of m/s, the *signed* x-component averages to zero — for every molecule moving +x, another moves −x. Speed (a positive scalar) is nonzero, but a signed component is symmetric about zero.

By symmetry of the velocity distribution (Maxwell–Boltzmann), $\langle v_x\rangle = \boxed{0}$ ✓.
Speeds (a positive quantity) are nonzero on average, but a signed component averages to zero.

---

## Q11 — RMS speed at 39 °C

The root-mean-square speed (the one that appears in $\tfrac12 m v_{\text{rms}}^2 = \tfrac32 k_BT$) is $v_{\text{rms}} = \sqrt{3RT/M}$. Same setup as Q9 but with the slightly different prefactor 3 vs 8/π.

$T=312.15$ K, $M=0.032$ kg/mol.
$$v_{\text{rms}} = \sqrt{3RT/M} = \sqrt{3(8.314)(312.15)/0.032} = \sqrt{243{,}295} = \boxed{493.15\ \text{m/s}}\ \checkmark$$

---

## Q12 — Internal energy of helium

Helium is monatomic, so each atom has only 3 translational degrees of freedom ($f=3$): $U = \tfrac{f}{2}nRT = \tfrac{3}{2}nRT$. Convert °C to K first.

He is monatomic ($f=3$). $T = 428.15$ K.
$$U = \tfrac{3}{2}nRT = 1.5(2.4)(8.314)(428.15) = \boxed{12.81\ \text{kJ}}\ \checkmark$$

---

## Q13 — Internal energy change with $f=2$

By the equipartition theorem, each quadratic degree of freedom contributes $\tfrac12 k_BT$ per molecule (or $\tfrac12 RT$ per mole). Two dof gives $\Delta U = nR\,\Delta T$.

$\Delta U = (f/2)nR\Delta T = 1\cdot(6.2)(8.314)(53) = \boxed{2.732\ \text{kJ}}\ \checkmark$

---

## Q14 — Definition of $k_B$

The Boltzmann constant connects the per-molecule and per-mole formulations: $nR = Nk_B$ requires $k_B = R/N_A$. So one mole of $k_B$ equals $R$.

$k_B = R/N_A$ — "the gas constant **divided by** Avogadro's number" ✓

---

## Q15 — Same $Q$ into monatomic vs diatomic gas

At constant volume, all input heat $Q$ goes to internal energy: $Q = \Delta U = (f/2)nR\Delta T$. A monatomic gas ($f=3$) has fewer "energy buckets" than a diatomic gas ($f=5$, including rotation), so the same $Q$ gives a *larger* $\Delta T$ in the monatomic gas. For the rms speed, however, $v_{\text{rms}}\propto\sqrt{T/M}$ depends on molecular mass, which isn't specified, so the comparison is indeterminate.

At constant volume, $Q = \Delta U = (f/2)nR\Delta T$. With $f_A=3 < f_B=5$ at the same $n$:
- $\Delta T_A > \Delta T_B$ → A's new temperature is **higher than** B's ✓
- $v_{\text{rms}} \propto \sqrt{T/M}$. The molecular masses $M$ aren't given, so even though $T_A > T_B$ we can't compare $v_{\text{rms}}$. → **impossible to determine without more information** ✓

---

## Q16 — Ordering of speed measures

For a Maxwell–Boltzmann distribution the three speed measures are ordered $v_p < v_{\text{avg}} < v_{\text{rms}}$. This is because $v_{\text{rms}}^2 = \langle v^2\rangle$ weights faster molecules more heavily, while $v_p$ (the peak of the distribution) sits below the mean because of the long high-speed tail.

For a Maxwell–Boltzmann distribution: $v_p < v_{\text{avg}} < v_{\text{rms}}$.
- Highest: **root-mean-square speed** ✓
- Lowest: **most probable speed** ✓

---

**All numeric answers match the source key.**
