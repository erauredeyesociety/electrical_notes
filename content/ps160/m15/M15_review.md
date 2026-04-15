# M15 Review Problems — Mechanical Waves

Practice problems for Module 15 (mechanical waves, standing waves, power).

---

## Problem 1 — Wavelength from speed and frequency

The speed of sound in air at 20 °C is 344 m/s. Use this speed to calculate the wavelength (in cm) of a 737 Hz sound wave.

$\lambda = v/f$

---

## Problem 2 — Wave properties from frequency and wavelength

A wave has frequency 25.0 Hz and wavelength 3.30 m. Find:

- (a) speed $v = \lambda f$
- (b) angular frequency $\omega = 2\pi f$
- (c) period $T = 1/f$
- (d) wave number $k = 2\pi/\lambda$

---

## Problem 3 — Wave speed from the wave equation

A wave equation is given by
$$\alpha\frac{\partial^2 y}{\partial t^2} - \beta\frac{\partial^2 y}{\partial x^2} = 0$$
with $\alpha = 3\;\mathrm{s}^2$ and $\beta = 258.6\;\mathrm{m}^2$.

Compare to the standard form $\partial_t^2 y = v^2 \partial_x^2 y$: dividing through, $v^2 = \beta/\alpha$, so $v = \sqrt{\beta/\alpha}$.

---

## Problem 4 — Wave function decomposition

Given $y(t,x) = 2\cos(4t - 2.2 x + 1.4)$ in MKS units, identify:

- (a) amplitude: $A = 2$ m
- (b) angular frequency: $\omega = 4$ rad/s
- (c) wave number: $k = 2.2$ rad/m
- (d) phase shift: $\varphi = 1.4$ rad
- (e) frequency: $f = \omega/(2\pi)$ Hz
- (f) period: $T = 2\pi/\omega$ s
- (g) wavelength: $\lambda = 2\pi/k$ m
- (h) propagation speed: $v = \omega/k$ m/s
- (i) transverse speed at $x=0, t=0$: $\dot y = -A\omega\sin(\varphi)$ m/s

---

## Problem 5 — Power on a wire

A wire has mass 13 g and length 1.3 m under tension 711 N. Amplitude 0.85 cm, frequency 152 Hz. Find the average power.

$$P_\text{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2,\qquad \mu = m/L,\quad \omega = 2\pi f$$

---

## Problem 6 — Standing wave node count

Two traveling waves of frequency $f = 200$ Hz interfere to produce a standing wave. Distance from node #1 to node #5 is 4.02 m. Find $\lambda$.

Adjacent nodes are separated by $\lambda/2$. From node 1 to node 5 is 4 intervals, so $4(\lambda/2) = 4.02\Rightarrow \lambda = 2.01$ m.

---

## Problem 7 — Harmonic ratios

A vibrating string has fifth harmonic 1436 Hz. Second harmonic?

$f_n = n f_1\Rightarrow f_1 = 1436/5$, then $f_2 = 2 f_1$.

---

## Problem 8 — Linear density from fundamental

Wire with fundamental 339 Hz, length 0.37 m, tension 1472 N. Find $\mu$ in g/m.

String fixed at both ends: $f_1 = v/(2L)$ with $v = \sqrt{F/\mu}$. Solve:
$$\mu = \frac{F}{(2 L f_1)^2}$$

---

## Problem 9 — Tension from mass and fundamental

Wire mass 0.051 kg, length 0.67 m, fundamental 140 Hz. Find tension.

$$F = \mu(2L f_1)^2,\quad \mu = m/L$$

---

## Conceptual questions

- **Wave number.** Number of radians per meter is called the **wave number** $k$.
- **Standing waves (string fixed at both ends).** Distance from a node to adjacent antinode = **one-quarter** wavelength. At the fundamental, the string length = **one-half** wavelength.
- **Wave types.** Vibration perpendicular to propagation: **transverse**. Parallel: **longitudinal**.
- **Superposition.** "The linear combination of any number of solutions of the wave equation is also a solution" is the principle of **superposition**.

---

## Key formulas (summary)

$$v = \lambda f = \omega/k,\quad k = 2\pi/\lambda,\quad \omega = 2\pi f$$
$$y(x,t) = A\cos(kx - \omega t + \varphi)$$
$$\partial_t^2 y = v^2\partial_x^2 y$$
$$v_\text{string} = \sqrt{F/\mu}$$
$$P_\text{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2$$
$$f_n = \frac{n v}{2L}\quad\text{(both ends fixed / open pipe)}$$
$$f_n = \frac{n v}{4L},\; n\text{ odd}\quad\text{(one end closed)}$$
