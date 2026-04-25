# MQ12a + MQ12b: Fluid Mechanics Practice — Walkthrough

**Module:** M12 — see [m12/](../../m12/) and the verified [ME12 walkthrough](ME12_v1_solutions.md) for the same equations applied to similar problems.

> ⚠️ **No source answer key for MQ files.** Values below are independently computed; verify with your instructor.

---

# MQ12a

## Q1 — Mass from density/volume ratios

$\rho_A = 0.5\rho_B$, $V_A = 2.7V_B$, $m_A = 1.7$ kg.
$m_A = \rho_A V_A = 0.5\rho_B(2.7V_B) = 1.35\,m_B$
$$m_B = 1.7/1.35 = \boxed{1.259\ \text{kg}}$$

## Q2 — Weight of a hollow lead pipe (lbs)

$L=3.3$ m, OD = 3.6 cm, ID = 2.4 cm, $\rho_{\text{Pb}} = 11{,}300\ \text{kg/m}^3$.
$$A = \pi(R_o^2 - R_i^2) = \pi((0.018)^2 - (0.012)^2) = 5.655\times 10^{-4}\ \text{m}^2$$
$$V = AL = 1.866\times 10^{-3}\ \text{m}^3,\quad m = \rho V = 21.09\ \text{kg}$$
$$W = mg = 206.66\ \text{N} = 206.66/4.4482 = \boxed{46.46\ \text{lbs}}$$

## Q3 — Pressure under one shoe (absolute)

Total weight on player + cheerleader $= (134)(9.80) = 1313.2$ N, split between two shoes ⇒ 656.6 N per shoe; $A = 279\ \text{cm}^2 = 0.0279\ \text{m}^2$.
$$p_{\text{gauge}} = 656.6/0.0279 = 23{,}534\ \text{Pa}$$
$$p_{\text{abs}} = 101{,}000 + 23{,}534 = \boxed{124{,}534\ \text{Pa}}$$

## Q4 — Barometer on Planet X

$\Delta h = 51.1 - 6 = 45.1$ cm $= 0.451$ m, $\rho = 13{,}534$, $g_X = 2.6$.
$$p_0 = \rho g\,\Delta h = 13534(2.6)(0.451) = 15{,}872\ \text{Pa} = \boxed{15.87\ \text{kPa}}$$

## Q5 — Bottom of mercury cylinder

$$p = p_{\text{atm}} + \rho g h = 66488 + 13600(9.8)(0.29) = 66488 + 38{,}651 = \boxed{105{,}139\ \text{Pa}}$$

## Q6 — Two-layer fuel tank

Stacking layers: $p = p_{\text{atm}} + \rho_{\text{oil}} g h_{\text{oil}} + \rho_{\text{w}} g h_{\text{w}}$.
$$= 105000 + 617(9.8)(1) + 1033(9.8)(2.9) = 105000 + 6047 + 29{,}358 = 140{,}405\ \text{Pa} = \boxed{140.4\ \text{kPa}}$$

## Q7 — Hydraulic press, output force

$F_{\text{out}}/F_{\text{in}} = A_{\text{out}}/A_{\text{in}} = 5.6$.
$$F_{\text{out}} = 5.6(314) = 1758.4\ \text{N} = \boxed{1.758\ \text{kN}}$$

## Q8 — Two-stage hydraulic + pressing plate

Input piston $r_1 = 0.07$ m ⇒ $A_1 = 0.01539\ \text{m}^2$. Output piston $r_2 = 0.16$ m ⇒ $A_2 = 0.08042\ \text{m}^2$. Plate $A_p = 11.6\ \text{cm}^2 = 1.16\times 10^{-3}\ \text{m}^2$.

Fluid pressure: $P = F_1/A_1 = 282/0.01539 = 18{,}319$ Pa.
Force on plate: $F_2 = P A_2 = 18319(0.08042) = 1473.2$ N.
Compressive stress on plate:
$$\sigma = F_2/A_p = 1473.2/0.00116 = 1.27\times 10^6\ \text{Pa} = \boxed{1{,}270\ \text{kPa}}$$

---

# MQ12b

## Q1 — Buoyant force on submerged object

$B = \rho_f V g = 632(0.6)(3.3) = \boxed{1251.36\ \text{N}}$

## Q2 — Mass that brings raft to 97% submerged

$V_{\text{raft}} = 4.6(3)(0.5) = 6.9\ \text{m}^3$, $\rho_{\text{wood}}=540$.
At 97% submerged: buoyancy supports raft + load.
$\rho_{\text{w}}(0.97V)g = (m_{\text{raft}} + m_{\text{load}})g$
$$m_{\text{tot}} = 1000(0.97)(6.9) = 6693\ \text{kg}$$
$$m_{\text{raft}} = 540(6.9) = 3726\ \text{kg}$$
$$m_{\text{load}} = 6693 - 3726 = \boxed{2967\ \text{kg}}$$

## Q3 — Nozzle diameter

Continuity ⇒ $D_2 = D_1\sqrt{v_1/v_2} = 1.24\sqrt{1.4/4.2} = 1.24(0.5774) = \boxed{0.716\ \text{cm}}$

## Q4 — Pipe splits into three

$A_1 v_1 = 3 A_2 v_2$ ⇒ $v_2 = (2.43)(2.3)/(3\cdot 0.8) = 5.589/2.4 = \boxed{2.329\ \text{m/s}}$

## Q5 — Geyser-like vent

Bernoulli from chamber (depth 51 m, $v\approx 0$) to surface vent:
$$P_c = P_{\text{atm}} + \rho g h + \tfrac12\rho v^2$$
$$\tfrac12\rho v^2 = 729924 - 101000 - 1000(9.8)(51) = 729924 - 101000 - 499800 = 129{,}124\ \text{Pa}$$
$$v = \sqrt{2(129124)/1000} = \sqrt{258.25} = \boxed{16.07\ \text{m/s}}$$

## Q6 — Bernoulli with narrowing pipe

$v_2 = v_1(r_1/r_2)^2 = 2.4(0.24/0.13)^2 = 2.4(3.408) = 8.18$ m/s.
$$P_2 = P_1 + \tfrac12\rho(v_1^2 - v_2^2) = 201000 + 500(5.76 - 66.91) = 201000 - 30575 = \boxed{170.4\ \text{kPa}}$$

---
