# MQ15a + MQ15b: Waves Practice — Walkthrough

**Module:** M15 — see [m15/](../../m15/) and the verified [ME15 walkthrough](ME15_v1_solutions.md).

> ⚠️ **No source answer key.** Independently computed.

---

# MQ15a

## Q1 — Ultrasound frequency

$f = v/\lambda = 1550/(9.2\times 10^{-4}) = 1.685\times 10^6$ Hz $= \boxed{1.685\ \text{MHz}}$

## Q2 — $v$, $\omega$, $T$, $k$ for $f=25$, $\lambda=3.30$

- $v = 25(3.30) = \boxed{82.5\ \text{m/s}}$
- $\omega = 2\pi(25) = \boxed{157.08\ \text{rad/s}}$
- $T = 1/25 = \boxed{0.040\ \text{s}}$
- $k = 2\pi/3.30 = \boxed{1.904\ \text{rad/m}}$

## Q3 — Wave speed from $\alpha\,\partial_t^2 y - \beta\,\partial_x^2 y = 0$

Rearrange: $\partial_t^2 y = (\beta/\alpha)\,\partial_x^2 y$ ⇒ $v = \sqrt{\beta/\alpha} = \sqrt{750.7/10} = \sqrt{75.07} = \boxed{8.664\ \text{m/s}}$

## Q4 — Read parameters from $y = 3\cos(2t - 0.6x + 1.2)$

- $A = 3$ m
- $\omega = 2$ rad/s
- $k = 0.6$ rad/m (read coefficient of $x$ as a magnitude)
- $\phi = 1.2$ rad
- $f = \omega/(2\pi) = 0.318$ Hz; $T = 2\pi/\omega = 3.14$ s
- $\lambda = 2\pi/k = 10.47$ m
- $v = \omega/k = 3.33$ m/s
- Transverse speed at $(0,0)$: $\partial_t y = -A\omega\sin(\omega t - kx + \phi)|_{(0,0)} = -6\sin(1.2) = -6(0.9320) = \boxed{-5.59\ \text{m/s}}$ (speed magnitude $= 5.59$ m/s)

## Q5 — Power on a wire

$\mu = m/L = 0.011/2.1 = 5.238\times 10^{-3}$ kg/m.
$v = \sqrt{T/\mu} = \sqrt{454/0.005238} = 294.40$ m/s.
$\omega = 2\pi f = 873.36$ rad/s.
$$P = \tfrac{1}{2}\mu\omega^2 A^2 v = 0.5(5.238\times 10^{-3})(762560)(1.296\times 10^{-5})(294.4) = \boxed{7.62\ \text{W}}$$

---

# MQ15b

## Q1 — Wavelength from node-to-node spacing

Adjacent nodes are $\lambda/2$ apart. Nodes 3 → 5 spans 2 intervals = $\lambda$.
$\lambda = \boxed{5.27\ \text{m}}$

## Q2 — Second harmonic from fifth

$f_n = nf_1$: $f_1 = 1436/5 = 287.2$ Hz; $f_2 = 2(287.2) = \boxed{574.4\ \text{Hz}}$

## Q3 — Tension from fundamental

$v = 2Lf_1 = 2(0.57)(105) = 119.7$ m/s. $\mu = m/L = 0.0702$ kg/m.
$T = \mu v^2 = 0.0702(119.7)^2 = 0.0702(14328) = \boxed{1005.8\ \text{N}}$

## Q4 — Fundamental from tension

$\mu = 0.07/0.67 = 0.1045$ kg/m; $v = \sqrt{516/0.1045} = \sqrt{4938} = 70.27$ m/s.
$f_1 = v/(2L) = 70.27/1.34 = \boxed{52.44\ \text{Hz}}$

## Q5 — Wave number

$k$ is the **wave number** (a.k.a. **angular wavenumber**), in rad/m.

## Q6 — Transverse vs longitudinal

Vibration ⊥ propagation = **transverse** ✓
Vibration ∥ propagation = **longitudinal** ✓

## Q7 — Standing wave special points

Destructive (zero amplitude) = **nodes**; constructive (max amplitude) = **antinodes**.

## Q8 — Guitar string scaling

- Doubling $T$: $v = \sqrt{T/\mu}$ → $v$ **increases** by $\sqrt{2}$; $f$ **increases**.
- 4× mass (length fixed): $\mu$ ×4 → $v$ scales by $1/\sqrt{4} = 1/2$ → $v$ **decreases** by **one-half**; $f$ **decreases** by **one-half**.

---
