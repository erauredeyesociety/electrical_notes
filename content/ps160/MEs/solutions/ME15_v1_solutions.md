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

Light of any wavelength satisfies $c = f\lambda$, so $f = c/\lambda$. The answer is asked in units of $10^{12}$ Hz, so we compute the frequency in Hz and divide by $10^{12}$.

$f = c/\lambda = (2.9979\times 10^8)/(564\times 10^{-9})$
$= 5.3154\times 10^{14}$ Hz $= \boxed{531.5426\times 10^{12}\ \text{Hz}}$ ✓

---

## Q2 — $v$, $\omega$, $T$, $k$ for $f=36$ Hz, $\lambda=4.20$ m

A traveling wave is fully described by its frequency and wavelength. From these we get the speed $v = f\lambda$, the angular frequency $\omega = 2\pi f$ (rad/s), the period $T = 1/f$, and the wave number $k = 2\pi/\lambda$ (rad/m). Each quantity is just a different way of repackaging $f$ or $\lambda$.

- $v = f\lambda = 36\cdot 4.20 = \mathbf{151}$ m/s ✓
- $\omega = 2\pi f = \mathbf{226}$ rad/s ✓
- $T = 1/f = \mathbf{0.0278}$ s ✓
- $k = 2\pi/\lambda = 6.2832/4.20 = \mathbf{1.50}$ rad/m ✓

---

## Q3 — Read $\beta$ from $y = A e^{\omega t + kx}$ in $\partial_t^2 y - \beta^2\partial_x^2 y = 0$

Plug the proposed solution into the wave equation and see what $\beta$ must be for it to satisfy the PDE. For an exponential $e^{\omega t + kx}$, each time derivative pulls down a factor $\omega$ and each spatial derivative pulls down $k$, so $\partial_t^2 y = \omega^2 y$ and $\partial_x^2 y = k^2 y$. The equation reduces to $(\omega^2 - \beta^2 k^2)y = 0$, giving $\beta = \omega/k$ — exactly the same dispersion relation as the cosine wave.

$$\omega^2 y - \beta^2 k^2 y = 0 \Rightarrow \beta = \omega/k = 20/0.8 = \boxed{25}\ \checkmark$$

(Same relation $v=\omega/k$ as for cosine waves.)

---

## Q4 — Full diagnostic for $y = 5\cos(3t + 0.5x - 2.1)$

Standard traveling-wave form $y = A\cos(\omega t + kx + \phi)$. Read off $A$, $\omega$, $k$, $\phi$ directly. Frequency and period come from $\omega$; wavelength from $k$. The wave speed is $v = \omega/k$ (the sign tells direction; magnitude is the speed). The transverse speed at $(x,t) = (0,0)$ is $\partial y/\partial t$ evaluated at that point — note that's a velocity component of a particle on the string, not the wave's propagation speed.

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

A wave on a string carries energy at average rate $P_{\text{avg}} = \tfrac12 \mu\omega^2 A^2 v$. We need three derived numbers: linear density $\mu = m/L$, wave speed $v = \sqrt{T/\mu}$, and angular frequency $\omega = 2\pi f$. Then plug into the formula.

$m=0.012$ kg, $L=0.7$ m, $T=514$ N, $A=0.008$ m, $f=123$ Hz.

$$\mu = m/L = 0.01714\ \text{kg/m},\quad v = \sqrt{T/\mu} = \sqrt{514/0.01714} = 173.16\ \text{m/s}$$
$$\omega = 2\pi f = 772.83\ \text{rad/s},\quad \omega^2 A^2 = (772.83)^2(0.008)^2 = 38.225$$
$$P_{\text{avg}} = \tfrac{1}{2}\mu\,\omega^2 A^2\, v = 0.5\cdot 0.01714\cdot 38.225\cdot 173.16 = \boxed{56.73\ \text{W}}\ \checkmark$$

---

## Q6 — Wavelength from node spacing

In a standing wave, nodes are positions of zero displacement. Adjacent nodes are exactly $\lambda/2$ apart. Counting nodes 1 through 6 gives 5 *intervals* between them (not 6), so $5(\lambda/2) = 4.89$ m. The frequency is irrelevant for this geometry question.

$$5(\lambda/2) = 4.89 \Rightarrow \lambda = \boxed{1.956\ \text{m}}\ \checkmark$$

(Frequency was given as a distractor.)

---

## Q7 — Third harmonic from fourth

For a string fixed at both ends, the harmonics are integer multiples of the fundamental: $f_n = n f_1$. Knowing $f_4$ lets us back out $f_1 = f_4/4$, then compute $f_3 = 3 f_1$.

$f_n = n f_1$, so $f_1 = 242/4 = 60.5$ Hz.
$$f_3 = 3\cdot 60.5 = \boxed{182\ \text{Hz}}\ \checkmark$$

---

## Q8 — Tension from fundamental frequency

A string fixed at both ends has fundamental $f_1 = v/(2L)$, so $v = 2 L f_1$. Wave speed on a string is $v = \sqrt{T/\mu}$, so $T = \mu v^2$ where $\mu = m/L$. Plug it all together.

$m=0.066$ kg, $L=0.4$ m, $f_1=107$ Hz.

$f_1 = v/(2L) \Rightarrow v = 2Lf_1 = 85.6$ m/s; $\mu = m/L = 0.165$ kg/m.
$$T = \mu v^2 = 0.165(85.6)^2 = 0.165\cdot 7327.36 = \boxed{1209\ \text{N}}\ \checkmark$$

---

## Q9 — Length from tension and fundamental

We know mass, tension, and fundamental frequency, want length. Combine $v = \sqrt{T/\mu} = \sqrt{TL/m}$ (since $\mu = m/L$) with $v = 2Lf_1$ to eliminate $v$. Squaring gives $4L^2 f_1^2 = TL/m$, so $L = T/(4 m f_1^2)$. Critical: $m$ must be in kg.

$m=0.006$ kg, $T=759$ N, $f_1=318$ Hz.

$$4L^2 f_1^2 = TL/m \Rightarrow L = \dfrac{T}{4 m f_1^2} = \dfrac{759}{4(0.006)(318)^2} = \dfrac{759}{2426.98} = \boxed{0.3127\ \text{m}}\ \checkmark$$

(Watch units: $m$ in kg, not g.)

---

## Q10 — Standing-wave geometry

Standing-wave shapes are made of half-wavelength loops, each running from one node to the next.

- Node to adjacent antinode: **one-quarter** wavelength ✓ (a half-loop has length $\lambda/2$ and the antinode is its midpoint, halfway between the two bracketing nodes)
- String length at fundamental: **one-half** wavelength ✓ (the $n=1$ pattern fits exactly one half-loop on the string: $L = \lambda_1/2$)

---

## Q11 — Transverse vs longitudinal

Two ways a wave's vibration can orient relative to its direction of travel: perpendicular (think of a wave on a string — wiggle is up/down while the wave runs left/right) or parallel (think of a sound wave in air — air parcels compress/rarefy along the propagation direction).

Vibration ⊥ propagation = **transverse** ✓
Vibration ∥ propagation = **longitudinal** ✓

---

## Q12 — Guitar string with $v=\sqrt{T/\mu}$, $f_1 = v/(2L)$

Two scaling questions on a fixed-length string: how do $v$ and $f$ change when we (a) double tension, or (b) quadruple the mass? Since $v = \sqrt{T/\mu}$, the speed scales as $\sqrt{T}$ and as $1/\sqrt{\mu}$ (where $\mu = m/L$). And since $f_1 = v/(2L)$ at fixed $L$, the frequency tracks $v$ proportionally.

- Doubling tension → $v$ scales by $\sqrt{2}$ ⇒ $v$ **increases**, $f$ **increases**.
- Quadrupling mass (length fixed) → $\mu$ ×4 → $v$ scales by $1/\sqrt{4} = 1/2$ ⇒ $v$ **decreases by one-half**, $f$ **decreases by one-half**.

---

## Q13 — Name of $k = 2\pi/\lambda$

The number $k$ measures how many radians of phase fit into one meter — that is, $2\pi$ radians per wavelength. The standard names for $k$ are **wave number** / **angular wavenumber** ✓.

---

**All numeric answers match the source key.**
