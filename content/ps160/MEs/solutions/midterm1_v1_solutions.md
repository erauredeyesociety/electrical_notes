# Midterm 1 (v1) — Fluids, Oscillations, Waves, Sound — Walkthrough

Covers modules **M12, M14, M15, M16**. See module folders and ME walkthroughs:
[ME12](ME12_v1_solutions.md), [ME14](ME14_v1_solutions.md), [ME15](ME15_v1_solutions.md), [ME16](ME16_v1_solutions.md).

---

## Q1 — Hydrostatic pressure on another planet

$P = P_{\text{atm}} + \rho g h = 100241 + 1040(13.6)(6.8) = 100241 + 96179 = \boxed{196{,}420.2\ \text{Pa}}\ \checkmark$

## Q2 — Hydraulic press output

$F_{\text{out}} = (A_{\text{out}}/A_{\text{in}})F_{\text{in}} = 3.3(419) = 1382.7\ \text{N} = \boxed{1.3827\ \text{kN}}\ \checkmark$

## Q3 — Density of a floating object

Floating: $\rho_{\text{obj}}V_{\text{tot}} = \rho_f V_{\text{sub}}$.
$\rho_{\text{obj}} = 813(8.7/12) = \boxed{589.425\ \text{kg/m}^3}\ \checkmark$

## Q4 — Time to fill a 37-gallon tub

$V = 37(3.785\times 10^{-3}) = 0.14005\ \text{m}^3$; $Q = Av = (1.3\times 10^{-4})(3.1) = 4.03\times 10^{-4}\ \text{m}^3/\text{s}$.
$t = 0.14005/4.03\times 10^{-4} = 347.5\ \text{s} = \boxed{5.79\ \text{min}}\ \checkmark$

## Q5 — Bernoulli with height & cross-section change

$v_2 = v_1(A_1/A_2) = 2(0.34/0.12) = 5.667$ m/s.
$P_2 = P_1 + \tfrac12\rho(v_1^2-v_2^2) + \rho g(h_1-h_2)$
$= 204000 + 500(4 - 32.11) + 1000(9.8)(-3)$
$= 204000 - 14055.6 - 29400 = \boxed{160.54\ \text{kPa}}\ \checkmark$

## Q6 — Block-spring frequency

$\omega = \sqrt{1330/3.6} = 19.22$ rad/s; $f = \omega/(2\pi) = \boxed{3.059\ \text{Hz}}\ \checkmark$

## Q7 — Spring constant from $v_{\max}$

$k = m v_{\max}^2/A^2 = 3.4(5.4)^2/(0.49)^2 = 99.144/0.2401 = \boxed{412.93\ \text{N/m}}\ \checkmark$

## Q8 — Amplitude from $v_{\max}$

$\omega = \sqrt{56/1.3} = 6.563$ rad/s. $A = v_{\max}/\omega = 1.1/6.563 = 0.1676$ m $= \boxed{16.76\ \text{cm}}\ \checkmark$

## Q9 — Pendulum length

$L = g/\omega^2 = 9.8/(3.61)^2 = 9.8/13.03 = \boxed{0.752\ \text{m}}\ \checkmark$

## Q10 — Read parameters from $y = 5\cos(0.2\pi t - 0.3\pi x + 0.25\pi)$

- $A = \mathbf{5\ \text{m}}$
- $\phi = 0.25\pi = \mathbf{0.785\ \text{rad}}$
- $k = 0.3\pi = \mathbf{0.942\ \text{rad/m}}$
- $\omega = 0.2\pi = \mathbf{0.628\ \text{rad/s}}$
- $f = \omega/(2\pi) = \mathbf{0.1\ \text{Hz}}$
- $T = 1/f = \mathbf{10\ \text{s}}$
- $\lambda = 2\pi/k = \mathbf{6.67\ \text{m}}$
- $v = \omega/k = \mathbf{0.667\ \text{m/s}}$
- Transverse speed at $(0,0)$: $|\partial_t y| = A\omega|\sin(0.25\pi)| = 5(0.628)(0.7071) = \mathbf{2.22\ \text{m/s}}$ ✓

## Q11 — Mass per length from $f_1$ and $T$

$v = 2Lf_1 = 2(0.37)(351) = 259.74$ m/s. $\mu = T/v^2 = 1403/(259.74)^2 = 0.02080$ kg/m $= \boxed{20.80\ \text{g/m}}\ \checkmark$

## Q12 — Underwater sound transit

$v = \sqrt{2.34\times 10^9/1025} = 1510.93$ m/s. $t = 333000/1510.93 = \boxed{220.39\ \text{s}}\ \checkmark$

## Q13 — dB at new distance

$\Delta\beta = 20\log_{10}(12/51) = -12.57$; $\beta = 117 - 12.57 = \boxed{104.43\ \text{dB}}\ \checkmark$

## Q14 — Open-open pipe at 12 °C, $n=1$

$T=285$ K ⇒ $v = 331\sqrt{285/273} = 338.20$ m/s. $f_1 = v/(2L) = 338.20/2 = \boxed{169.10\ \text{Hz}}\ \checkmark$

## Q15 — Doppler: motorcyclist W, fire truck E (separating)

Source recedes (eastbound, observer west of source): $v_s = -40$.
Observer recedes (westbound, away from source): $v_o = -29$. $v=350$.
$$f' = 1094(350-29)/(350+40) = 1094(0.8231) = \boxed{900.45\ \text{Hz}}\ \checkmark$$

---

**All numeric answers match the source key.**
