# MQ14a + MQ14b: Oscillations Practice — Walkthrough

**Module:** M14 — see [m14/](../../m14/) and the verified [ME14 walkthrough](ME14_v1_solutions.md).

> ⚠️ **No source answer key.** Independently computed.

---

# MQ14a

## Q1 — Block-spring angular frequency

$\omega = \sqrt{k/m} = \sqrt{818/12} = \sqrt{68.167} = \boxed{8.256\ \text{rad/s}}$

## Q2 — Tunnel through uniform planet

$\omega^2 = 4\pi G\rho/3 = 4\pi(6.67\times 10^{-11})(3856)/3 = 1.0773\times 10^{-6}\ \text{s}^{-2}$
$\omega = 1.038\times 10^{-3}$ rad/s
$T = 2\pi/\omega = 6053.6$ s $= \boxed{1.682\ \text{h}}$

(Period independent of $R$.)

## Q3 — Read parameters from $x(t)=4.00\cos(2.00t - 0.500)$

$A = \mathbf{4.00}$ m, $\omega = \mathbf{2.00}$ rad/s, $\phi = \mathbf{-0.500}$ rad,
$f = \omega/(2\pi) = \mathbf{0.318}$ Hz, $T = 2\pi/\omega = \mathbf{3.14}$ s.

## Q4 — Phase shift (positive value)

$k=711$, $m=6$, $x_0=-0.43$, $v_0=+2.59$.
$\omega = \sqrt{711/6} = 10.886$ rad/s.
$$\tan\phi = -v_0/(\omega x_0) = -2.59/(10.886\cdot -0.43) = 0.5532$$
The principal-value $\arctan = 0.505$ rad sits in Q1, but the actual quadrant must satisfy $x_0 = A\cos\phi < 0$ (so $\cos\phi < 0$) and $v_0 = -A\omega\sin\phi > 0$ (so $\sin\phi < 0$) ⇒ Q3.
$$\phi = \pi + 0.505 = \boxed{3.647\ \text{rad}}$$

---

# MQ14b

## Q1 — Mass from $v_{\max}$ and $A$

$v_{\max} = A\sqrt{k/m}$ ⇒ $m = kA^2/v_{\max}^2 = 689(1.58)^2/(14.8)^2 = 1719.6/219.04 = \boxed{7.851\ \text{kg}}$

## Q2 — Amplitude from $(x_0, v_0)$

Energy: $A^2 = x_0^2 + (v_0/\omega)^2$, $\omega = \sqrt{665/5} = 11.533$ rad/s.
$A^2 = 0.04 + (2.1/11.533)^2 = 0.04 + 0.03316 = 0.07316$
$$A = \boxed{0.2705\ \text{m}}$$

## Q3 — Maximum spring force

$E = \tfrac12 kA^2$ ⇒ $k = 2E/A^2 = 2(7.98)/(0.14)^2 = 15.96/0.0196 = 814.29$ N/m.
$$F_{\max} = kA = 814.29(0.14) = \boxed{114.0\ \text{N}}$$

## Q4 — Pendulum length from $\omega$

$L = g/\omega^2 = 9.8/(2.74)^2 = 9.8/7.508 = \boxed{1.305\ \text{m}}$

## Q5 — Physical pendulum, $\omega$

$m=13.6$, $I=11.18$, $d=1.74$.
$\omega = \sqrt{mgd/I} = \sqrt{13.6(9.8)(1.74)/11.18} = \sqrt{231.92/11.18} = \sqrt{20.74} = \boxed{4.554\ \text{rad/s}}$

---
