# ME14: Oscillations — Walkthrough

**Module:** M14 (Oscillations) — see [m14/M14_Summary.md](../../m14/M14_Summary.md), [m14/M14_textbook_chapter.md](../../m14/M14_textbook_chapter.md)

**Core equations**
- Block-spring: $\omega = \sqrt{k/m}$, $T = 2\pi\sqrt{m/k}$, $f = \omega/(2\pi)$, $T = 1/f$
- General SHM solution: $x(t) = A\cos(\omega t + \phi)$
  - $v(t) = -A\omega\sin(\omega t+\phi)$, $\,a(t) = -A\omega^2\cos(\omega t+\phi) = -\omega^2 x$
  - $v_{\max} = A\omega$, $a_{\max} = A\omega^2$
- Initial conditions for cosine form: $x_0 = A\cos\phi$, $v_0 = -A\omega\sin\phi$ ⇒ $\tan\phi = -v_0/(\omega x_0)$
- Energy: $E = \tfrac{1}{2}kA^2 = \tfrac{1}{2}kx^2 + \tfrac{1}{2}mv^2$
- Simple pendulum (small angles): $\omega = \sqrt{g/L}$, $T = 2\pi\sqrt{L/g}$
- Physical pendulum: $\omega = \sqrt{mgd/I}$, $T = 2\pi\sqrt{I/(mgd)}$

Use $g=9.80\ \text{m/s}^2$.

---

## Q1 — Angular frequency of block-spring

$k=1055\ \text{N/m}$, $m=11\ \text{kg}$.
$$\omega = \sqrt{\dfrac{1055}{11}} = \sqrt{95.909} = \boxed{9.7933\ \text{rad/s}}\ \checkmark$$

---

## Q2 — $\omega$, $f$, $T$ for block-spring

$k=1240$, $m=15.0$.
$$\omega = \sqrt{1240/15} = \sqrt{82.667} = 9.09\ \text{rad/s}\ \checkmark$$
$$f = \omega/(2\pi) = 1.45\ \text{Hz}\ \checkmark,\quad T = 1/f = 0.691\ \text{s}\ \checkmark$$

---

## Q3 — Tunnel through a uniform planet

The given ODE $\ddot r + (4\pi G\rho/3)\,r = 0$ is SHM with $\omega^2 = 4\pi G\rho/3$.

$$\omega^2 = \frac{4\pi (6.67\times10^{-11})(4740)}{3} = 1.3243\times10^{-6}\ \text{s}^{-2}$$
$$\omega = 1.1508\times10^{-3}\ \text{rad/s}$$
$$T = \dfrac{2\pi}{\omega} = 5460.6\ \text{s} = \boxed{1.5168\ \text{h}}\ \checkmark$$

(Note: the radius $R$ is a distractor — the period of SHM through the tunnel doesn't depend on $R$, only $\rho$.)

---

## Q4 — Period from $ma+kz=0$

$m=11.7$, $k=94$.
$$T = 2\pi\sqrt{m/k} = 2\pi\sqrt{11.7/94} = 2\pi\sqrt{0.12447} = \boxed{2.2167\ \text{s}}\ \checkmark$$

---

## Q5 — Read parameters from $x(t)=4.00\cos(2.00t - 0.500)$

Compare to $A\cos(\omega t + \phi)$:
- Amplitude $A = \mathbf{4.00}$ m ✓
- Angular frequency $\omega = \mathbf{2.00}$ rad/s ✓
- Phase shift $\phi = \mathbf{-0.500}$ rad ✓
- Frequency $f = \omega/(2\pi) = \mathbf{0.318}$ Hz ✓
- Period $T = 1/f = 2\pi/\omega = \pi \approx \mathbf{3.14}$ s ✓

---

## Q6 — Full diagnostic for $x(t)=0.7\cos(8t+1.9)$

**(a)** $A = 0.7$ m ✓
**(b)** $\omega = 8$ rad/s ✓
**(c)** $\phi = 1.9$ rad ✓
**(d)** $f = 8/(2\pi) = 1.27$ Hz ✓
**(e)** $T = 2\pi/8 = \pi/4 = 0.785$ s ✓
**(f)** $v_{\max} = A\omega = 0.7\cdot 8 = 5.6$ m/s ✓
**(g)** $a_{\max} = A\omega^2 = 0.7\cdot 64 = 44.8$ m/s² ✓
**(h)** $x(0) = 0.7\cos(1.9) = 0.7(-0.3233) = -0.226$ m ✓
**(i)** $v(0) = -A\omega\sin(1.9) = -5.6(0.9463) = -5.30$ m/s ✓
**(j)** $a(0) = -\omega^2 x(0) = -64(-0.226) = 14.48$ m/s² ✓

**(k)** First $t>0$ with $x=0$: $\cos(8t+1.9)=0 \Rightarrow 8t+1.9 = \pi/2 + n\pi$.
$\;n=0:\ t=(\pi/2-1.9)/8 = -0.0411$ (rejected);
$\;n=1:\ t=(3\pi/2-1.9)/8 = 2.8124/8 = 0.352$ s ✓

**(l)** First $t>0$ with $v=0$: $\sin(8t+1.9)=0 \Rightarrow 8t+1.9 = n\pi$.
$\;n=1:\ t=(\pi - 1.9)/8 = 0.155$ s ✓

---

## Q7 — Phase shift from initial conditions

$m=4$, $k=539$, $x_0=0.51$, $v_0=-2.6$.
$$\omega = \sqrt{539/4} = 11.609\ \text{rad/s}$$
$$\tan\phi = -\dfrac{v_0}{\omega x_0} = -\dfrac{-2.6}{11.609\cdot 0.51} = \dfrac{2.6}{5.9206} = 0.4391$$
$$\phi = \arctan(0.4391) = \boxed{0.4138\ \text{rad}}\ \checkmark$$

(Check quadrant: $x_0>0$ ⇒ $\cos\phi>0$ and $v_0<0$ ⇒ $\sin\phi>0$ ⇒ $\phi$ in Q1 ✓.)

---

## Q8 — Mass from amplitude and $v_{\max}$

$k=514$, $A=1.6$, $v_{\max}=12.9$.
$$v_{\max} = A\sqrt{k/m} \Rightarrow m = \dfrac{kA^2}{v_{\max}^2} = \dfrac{514(1.6)^2}{(12.9)^2} = \dfrac{1315.84}{166.41} = \boxed{7.907\ \text{kg}}\ \checkmark$$

---

## Q9 — Amplitude from $v_{\max}$

$m=4.7$, $k=183$, $v_{\max}=10$.
$$\omega = \sqrt{183/4.7} = 6.240\ \text{rad/s},\quad A = v_{\max}/\omega = 10/6.240 = \boxed{1.603\ \text{m}}\ \checkmark$$

---

## Q10 — Amplitude from instantaneous $(x,v)$

$m=7$, $k=133$, $x=0.26$, $v=2.9$.
Energy: $\tfrac{1}{2}kA^2 = \tfrac{1}{2}kx^2 + \tfrac{1}{2}mv^2$
$$A^2 = x^2 + (m/k)v^2 = 0.0676 + (7/133)(8.41) = 0.0676 + 0.4427 = 0.5103$$
$$A = \boxed{0.7144\ \text{m}}\ \checkmark$$

---

## Q11 — Speed at fractional displacement

$m=1.5$, $E=5.8$ J, $x = 0.14A$.
$$E = \tfrac{1}{2}kA^2,\quad \tfrac{1}{2}kx^2 = E(x/A)^2 = E(0.14)^2$$
$$\tfrac{1}{2}mv^2 = E - E(0.14)^2 = E(1 - 0.0196) = 0.9804\,E$$
$$v = \sqrt{2E(0.9804)/m} = \sqrt{2\cdot 5.8\cdot 0.9804/1.5} = \sqrt{7.5818} = \boxed{2.7535\ \text{m/s}}\ \checkmark$$

---

## Q12 — Pendulum length from $\omega$

$\omega=2.82$, $g=9.8$.
$$L = g/\omega^2 = 9.8/7.9524 = \boxed{1.2323\ \text{m}}\ \checkmark$$

---

## Q13 — Pendulum length from $T$

$T=1.579$ s.
$$L = g\!\left(\dfrac{T}{2\pi}\right)^2 = 9.8\cdot(0.25131)^2 = 9.8\cdot 0.06316 = 0.6189\ \text{m} = \boxed{61.89\ \text{cm}}\ \checkmark$$

---

## Q14 — Physical pendulum, period

$d=1.41$, $m=11.5$, $I=15$.
$$T = 2\pi\sqrt{\dfrac{I}{mgd}} = 2\pi\sqrt{\dfrac{15}{11.5\cdot 9.8\cdot 1.41}} = 2\pi\sqrt{0.09439} = \boxed{1.9304\ \text{s}}\ \checkmark$$

---

## Q15 — Physical pendulum, frequency

$d=0.48$, $m=6$, $I=8.6$.
$$\omega = \sqrt{\dfrac{mgd}{I}} = \sqrt{\dfrac{6\cdot 9.8\cdot 0.48}{8.6}} = \sqrt{3.2819} = 1.812\ \text{rad/s}$$
$$f = \omega/(2\pi) = \boxed{0.2883\ \text{Hz}}\ \checkmark$$

---

## Q16 — Pendulum conceptual

$T_{\text{simple}} = 2\pi\sqrt{L/g}$ — depends on $L$ and $g$ only, **not** mass.

- Longer period → use a **longer** string ✓
- Lighter mass → period is unchanged → "**can't be**" obtained that way ✓
- Longer period → take to a place with **smaller** $g$ ✓

---

**All answers match the source key.**
