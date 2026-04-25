# MQ16a + MQ16b: Sound Practice — Walkthrough

**Module:** M16 — see [m16/](../../m16/) and the verified [ME16 walkthrough](ME16_v1_solutions.md).

> ⚠️ **No source answer key.** Independently computed.

---

# MQ16a

## Q1 — Sound from depth 1342 m through water then 920 m through 7 °C air

$v_{\text{water}} = \sqrt{B/\rho} = \sqrt{2.34\times 10^9/1025} = 1510.93$ m/s.
$v_{\text{air}} = \sqrt{\gamma RT/M} = \sqrt{1.4(8.314)(280)/0.0288} = \sqrt{113{,}159} = 336.39$ m/s.
$$t = 1342/1510.93 + 920/336.39 = 0.888 + 2.735 = \boxed{3.62\ \text{s}}$$

## Q2 — Bulk modulus from sound transit

$v = 10.6/0.0103 = 1029.1$ m/s; $B = \rho v^2 = 1027(1.059\times 10^6) = \boxed{1.088\ \text{GPa}}$

## Q3 — Two sirens at 9 m

$I_1 = 10^{-12}\cdot 10^{11.4} = 0.2512$ W/m²; two sirens add ⇒ $\boxed{0.5024\ \text{W/m}^2}$

## Q4 — Inverse square: 122 dB at 9 m → 45 m

$\Delta\beta = 20\log_{10}(9/45) = -13.98$; $\beta_{45} = 122 - 13.98 = \boxed{108.02\ \text{dB}}$

## Q5 — Cluster of 4 rocket engines at 42 m

Single engine at 42 m: $\beta_1 = 122 + 20\log_{10}(20/42) = 122 - 6.44 = 115.56$ dB.
Four engines: $+10\log_{10}(4) = +6.02$ dB ⇒ $\boxed{121.58\ \text{dB}}$

## Q6 — Beat frequency, second fork lower

$f_2 = 493 - 0.9 = \boxed{492.1\ \text{Hz}}$

## Q7 — First constructive interference right of center

$T=289$ K ⇒ $v = 331\sqrt{289/273} = 340.56$ m/s; $\lambda = 340.56/423 = 0.8051$ m.
$\Delta = 2x-7 = n\lambda$; first $x>3.5$ at $n=1$:
$$x = (7+0.8051)/2 = \boxed{3.903\ \text{m}}$$

## Q8 — First destructive interference left of center

$T=291$ K ⇒ $v = 341.72$ m/s; $\lambda = 0.7594$ m.
For $x<1.5$: $\Delta = (3-x) - x = 3-2x = (n+\tfrac12)\lambda$; first $x<1.5$ at $n=0$:
$$x = (3 - 0.5\cdot 0.7594)/2 = \boxed{1.310\ \text{m}}$$

---

# MQ16b

## Q1 — Open-open pipe length, $n=2$, $v=344$

$f_n = nv/(2L)$ ⇒ $L = nv/(2f_n) = 344/506 = \boxed{0.680\ \text{m}}$

## Q2 — Closed-open pipe fundamental at 8 °C

$v = 331\sqrt{281/273} = 335.81$ m/s; $f_1 = v/(4L) = 335.81/4 = \boxed{83.95\ \text{Hz}}$

## Q3 — Doppler: motorcyclist away from stationary horn

$f' = f_s(v-v_o)/v = 532(347-31)/347 = 532(0.9107) = \boxed{484.49\ \text{Hz}}$

## Q4 — Doppler: bicyclist toward stationary horn

$f' = f_s(v+v_o)/v = 498(340+8)/340 = \boxed{509.72\ \text{Hz}}$

## Q5 — Doppler: ambulance ahead pulling away east

Source recedes ($v_s=-34$); observer chases ($v_o=+15$).
$f' = 1483(340+15)/(340+34) = 1483(355/374) = \boxed{1407.6\ \text{Hz}}$

## Q6 — Doppler: fire truck east, motorcyclist west (away)

Both move *away* from each other. With ground convention: source velocity $+42$ east means receding from observer (who's west of source) ⇒ $v_s = -42$. Observer at $-30$ (moving west, away from source) ⇒ $v_o = -30$.
$$f' = 1211(343-30)/(343+42) = 1211(313/385) = \boxed{984.6\ \text{Hz}}$$

## Q7 — Speed ratio $v_B/v_A$

$v = \sqrt{B/\rho}$ ⇒ $v_B/v_A = \sqrt{(B_B/B_A)(\rho_A/\rho_B)} = \sqrt{4/2.2} = \boxed{1.349}$

## Q8 — Open-open → closed-open

Open-open $f_1 = v/(2L)$. Closing one end gives $f_1 = v/(4L)$ — half the value.
$$f_{1,\text{closed}} = 596/2 = \boxed{298\ \text{Hz}}$$

---
