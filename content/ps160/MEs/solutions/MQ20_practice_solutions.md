# MQ20a + MQ20b: Engines, Refrigerators, Entropy Practice

**Module:** M20 — see [m20/](../../m20/) and [ME20 walkthrough](ME20_v1_solutions.md).

> ⚠️ **No source answer key.** Independently computed.

---

# MQ20a

## Q1 — Heat discarded per second

$P_{\text{in}} = P_{\text{out}}/e = 101/0.57 = 177.19$ kW; $P_{Q_C} = P_{\text{in}} - P_{\text{out}} = \boxed{76.19\ \text{kJ/s}}$

## Q2 — Net work in one cycle (ME20_PV_5)

Same cycle shape as ME20 Q3:
- Iso V (pressurize): 0
- Linear ramp from $(V_1,p_3)$ to $(V_2,p_2)$: $\tfrac12(p_3+p_2)(V_2-V_1) = 0.5(478)(2.6) = 621.4$ kJ
- Iso V (depressurize): 0
- Iso p contract at $p_1$: $p_1(V_1-V_2) = 102(-2.6) = -265.2$ kJ
$W_{\text{net}} = \boxed{356.2\ \text{kJ}}$

## Q3 — Refrigerator extraction

$|Q_H| = (\text{COP}+1)W$ ⇒ $W = 85/13 = 6.538$ J; $Q_C = 85 - 6.538 = \boxed{78.46\ \text{J}}$

## Q4 — Heat-pump COP

$|Q_H| = |Q_C| + W = 1614$; $\text{COP}_{HP} = |Q_H|/W = 1614/558 = \boxed{2.892}$

## Q5 — Heat-pump cooling COP

$Q_C = 1021$, $W = 1224 - 1021 = 203$; $\text{COP} = 1021/203 = \boxed{5.030}$

## Q6 — Three-process diatomic engine

Sketch the cycle: $(V_2, p_2) \xrightarrow{\text{iso T}} (V_1, p_a)$ where $p_a = 574$ kPa; isothermal: $p_2V_2 = p_aV_1$ ⇒ $V_1 = 230(2)/574 = 0.8014$ m³.
Then $(V_1, p_a) \xrightarrow{\text{iso p}} (V_2, p_a)$ and $(V_2, p_a) \xrightarrow{\text{iso V}} (V_2, p_2)$.

**Leg 1 (iso T, compression):** $W_1 = p_2V_2\ln(V_1/V_2) = 460\ln(0.4007) = -420.7$ kJ; $Q_1 = W_1 = -420.7$ kJ.
**Leg 2 (iso p, expansion):** $W_2 = p_a\Delta V = 574(1.1986) = 688.0$ kJ. Diatomic: $Q_2 = (7/2)p_a\Delta V = 2408$ kJ.
**Leg 3 (iso V, depressurize):** $W_3 = 0$; $Q_3 = (5/2)V_2\Delta p = 2.5(2)(-344) = -1720$ kJ.

$W_{\text{net}} = -420.7 + 688.0 = 267.3$ kJ; $Q_{\text{in}} = Q_2 = 2408$ kJ.
$$e = W_{\text{net}}/Q_{\text{in}} = 267.3/2408 = \boxed{0.1110}\ (\approx 11.1\%)$$

---

# MQ20b

## Q1 — Carnot $T_C$ from efficiency

$T_H = 815.15$ K; $T_C = T_H(1-e) = 815.15(0.49) = \boxed{399.42\ \text{K}}$

## Q2 — Carnot $T_H$

$|Q_H| = 1067 + 467 = 1534$; $T_H = T_C(Q_H/Q_C) = 263(1534/1067) = \boxed{378.11\ \text{K}}$

## Q3 — Entropy of water freezing

$Q = mL_f = 19.1(335000) = 6.3985\times 10^6$ J released.
$\Delta S_{\text{water}} = -Q/T = -6.3985\times 10^6/273.15 = \boxed{-23.43\ \text{kJ/K}}$

## Q4 — Universe entropy: gallium freezing

$T_g = 302.76$ K, $T_r = 290$ K (using $0$°C $= 273$ K). $Q = 21(80400) = 1.6884\times 10^6$ J.
$\Delta S_g = -Q/T_g = -5576.4$ J/K; $\Delta S_r = +Q/T_r = +5822.1$ J/K.
$\Delta S_{\text{univ}} = \boxed{+245.7\ \text{J/K}}$

## Q5 — Water warming

$\Delta S = mc\ln(T_f/T_i) = 2.1(4186)\ln(327.15/302.15) = 8790.6(0.07946) = \boxed{698.5\ \text{J/K}}$

## Q6 — Free expansion in compartment box

Initial volume = 4 cells; final = 9. $\Delta S = nR\ln(V_f/V_i) = 2.5(8.314)\ln(9/4) = 20.785(0.8109) = \boxed{16.86\ \text{J/K}}$

## Q7 — Steam → ice, full sequence

A. Condense steam at 100°C: $\Delta S_A = -mL_v/T = -18.8(2.26\times 10^6)/373.15 = -113{,}876$ J/K
B. Cool water 100→0: $\Delta S_B = mc\ln(T_f/T_i) = 18.8(4186)\ln(273.15/373.15) = 78697(-0.3119) = -24{,}544$ J/K
C. Freeze at 0°C: $\Delta S_C = -mL_f/T = -18.8(335000)/273.15 = -23{,}062$ J/K
$$\Delta S_{\text{total}} = -161{,}482\ \text{J/K} = \boxed{-161.5\ \text{kJ/K}}$$

---
