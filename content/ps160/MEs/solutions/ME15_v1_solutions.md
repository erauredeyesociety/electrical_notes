# ME15: Waves — Walkthrough

**Module:** M15 (Waves) — see [m15/](../../m15/)

**Core equations**
- Wave speed: $v = f\lambda$
- Angular frequency / wave number: $\omega = 2\pi f$, $k = 2\pi/\lambda$, $T=1/f=2\pi/\omega$
- Speed from $(\omega,k)$: $v = \omega/k$
- Wave equation $\partial_t^2 y = v^2\,\partial_x^2 y$ ⇒ harmonic solutions travel at $v$
- Travelling wave: $y(x,t) = A\cos(\omega t \pm kx + \phi)$
- Wave on a string: $v = \sqrt{T/\mu}$, with $\mu = m/L$
- String fixed both ends — fundamental: $f_1 = v/(2L)$; harmonics: $f_n = n f_1$
- Standing-wave geometry: node-to-node = $\lambda/2$; node-to-antinode = $\lambda/4$
- Power on a string: $P_{\text{avg}} = \tfrac{1}{2}\mu\omega^2 A^2 v$

---

## Q1 — Frequency of 564 nm light

$f = c/\lambda = (2.9979\times 10^8)/(564\times 10^{-9})$
$= 5.3154\times 10^{14}$ Hz $= \boxed{531.5426\times 10^{12}\ \text{Hz}}$ ✓

---

## Q2 — $v$, $\omega$, $T$, $k$ for $f=36$ Hz, $\lambda=4.20$ m

- $v = f\lambda = 36\cdot 4.20 = \mathbf{151}$ m/s ✓
- $\omega = 2\pi f = \mathbf{226}$ rad/s ✓
- $T = 1/f = \mathbf{0.0278}$ s ✓
- $k = 2\pi/\lambda = 6.2832/4.20 = \mathbf{1.50}$ rad/m ✓

---

## Q3 — Read $\beta$ from $y = A e^{\omega t + kx}$ in $\partial_t^2 y - \beta^2\partial_x^2 y = 0$

For an exponential, $\partial_t^2 y = \omega^2 y$ and $\partial_x^2 y = k^2 y$. Plug in:
$$\omega^2 y - \beta^2 k^2 y = 0 \Rightarrow \beta = \omega/k = 20/0.8 = \boxed{25}\ \checkmark$$

(Same relation $v=\omega/k$ as for cosine waves.)

---

## Q4 — Full diagnostic for $y = 5\cos(3t + 0.5x - 2.1)$

Compare to $A\cos(\omega t + kx + \phi)$:

**(a)** $A = 5$ m
**(b)** $\omega = 3$ rad/s ✓
**(c)** $k = 0.5$ rad/m ✓
**(d)** $\phi = -2.1$ rad ✓
**(e)** $f = \omega/(2\pi) = 0.477$ Hz ✓
**(f)** $T = 2\pi/\omega = 2.09$ s ✓
**(g)** $\lambda = 2\pi/k = 12.6$ m ✓
**(h)** $v = \omega/k = 3/0.5 = 6.0$ m/s ✓ (sign indicates direction; speed is the magnitude)

**(i)** Transverse speed at $(x,t)=(0,0)$:
$$\dfrac{\partial y}{\partial t} = -5\cdot 3\sin(3t+0.5x-2.1) \xrightarrow{(0,0)} -15\sin(-2.1) = -15(-0.8632) = \boxed{12.9\ \text{m/s}}\ \checkmark$$

---

## Q5 — Average power on a wire

$m=0.012$ kg, $L=0.7$ m, $T=514$ N, $A=0.008$ m, $f=123$ Hz.

$$\mu = m/L = 0.01714\ \text{kg/m},\quad v = \sqrt{T/\mu} = \sqrt{514/0.01714} = 173.16\ \text{m/s}$$
$$\omega = 2\pi f = 772.83\ \text{rad/s},\quad \omega^2 A^2 = (772.83)^2(0.008)^2 = 38.225$$
$$P_{\text{avg}} = \tfrac{1}{2}\mu\,\omega^2 A^2\, v = 0.5\cdot 0.01714\cdot 38.225\cdot 173.16 = \boxed{56.73\ \text{W}}\ \checkmark$$

---

## Q6 — Wavelength from node spacing

Adjacent nodes are $\lambda/2$ apart. From node 1 to node 6 is $5$ intervals:
$$5(\lambda/2) = 4.89 \Rightarrow \lambda = \boxed{1.956\ \text{m}}\ \checkmark$$

(Frequency was given as a distractor.)

---

## Q7 — Third harmonic from fourth

$f_n = n f_1$, so $f_1 = 242/4 = 60.5$ Hz.
$$f_3 = 3\cdot 60.5 = \boxed{182\ \text{Hz}}\ \checkmark$$

---

## Q8 — Tension from fundamental frequency

$m=0.066$ kg, $L=0.4$ m, $f_1=107$ Hz.

$f_1 = v/(2L) \Rightarrow v = 2Lf_1 = 85.6$ m/s; $\mu = m/L = 0.165$ kg/m.
$$T = \mu v^2 = 0.165(85.6)^2 = 0.165\cdot 7327.36 = \boxed{1209\ \text{N}}\ \checkmark$$

---

## Q9 — Length from tension and fundamental

$m=0.006$ kg, $T=759$ N, $f_1=318$ Hz.

Combine $v = \sqrt{T/\mu} = \sqrt{TL/m}$ with $v = 2Lf_1$:
$$4L^2 f_1^2 = TL/m \Rightarrow L = \dfrac{T}{4 m f_1^2} = \dfrac{759}{4(0.006)(318)^2} = \dfrac{759}{2426.98} = \boxed{0.3127\ \text{m}}\ \checkmark$$

(Watch units: $m$ in kg, not g.)

---

## Q10 — Standing-wave geometry

- Node to adjacent antinode: **one-quarter** wavelength ✓ (a half-loop has length $\lambda/2$; node and antinode bracket half of that)
- String length at fundamental: **one-half** wavelength ✓ ($n=1$: $L = \lambda_1/2$)

---

## Q11 — Transverse vs longitudinal

Vibration ⊥ propagation = **transverse** ✓
Vibration ∥ propagation = **longitudinal** ✓

---

## Q12 — Guitar string with $v=\sqrt{T/\mu}$, $f_1 = v/(2L)$

- Doubling tension → $v$ scales by $\sqrt{2}$ ⇒ $v$ **increases**, $f$ **increases**.
- Quadrupling mass (length fixed) → $\mu$ ×4 → $v$ scales by $1/\sqrt{4} = 1/2$ ⇒ $v$ **decreases by one-half**, $f$ **decreases by one-half**.

---

## Q13 — Name of $k = 2\pi/\lambda$

**Wave number / angular wavenumber** ✓ (radians per meter).

---

**All numeric answers match the source key.**
