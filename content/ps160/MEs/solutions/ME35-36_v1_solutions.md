# ME35-36: Interference & Diffraction — Walkthrough

**Module:** M35/36 — see [m33,34,35,36/](../../m33,34,35,36/)

> ⚠️ **Source key absent for numeric items.** All numeric values below were derived from first principles; please cross-check with any official key.

**Core formulas**
- Double slit (Young): bright fringes at $d\sin\theta = m\lambda$; small-angle position $y_m \approx m\lambda L/d$. Fringe spacing $\Delta y = \lambda L/d$.
- Single slit minima: $a\sin\theta = m\lambda$ for $m = \pm 1, \pm 2, \ldots$. Central maximum width = distance between $m=\pm 1$ minima $\approx 2\lambda L/a$.
- Thin film (light goes 1→2→3): a $\pi$ phase flip occurs at each reflection where the next medium has *higher* index.
  - Net "1 flip" total → constructive: $2nt = (m+\tfrac12)\lambda_{\text{vac}}$; destructive: $2nt = m\lambda$.
  - Net "0 or 2 flips" total → constructive: $2nt = m\lambda$; destructive: $2nt = (m+\tfrac12)\lambda$.
- Grating resolving power: $R = \lambda/\Delta\lambda = mN$ (N = number of illuminated slits).
- Grating max order: $m_{\max} = \lfloor d/\lambda\rfloor$. Total observed maxima = $2m_{\max} + 1$.
- Bragg: $2d\sin\theta = m\lambda$, with $\theta$ measured from the planes (grazing angle).
- Rayleigh resolution: $\theta_{\min} = 1.22\,\lambda/D$ (radians).

---

## Q1 — Slit separation from central-max width (double slit)

**Setup.** Coherent 502-nm light illuminates a *double* slit and forms an interference pattern on a screen 2.1 m away. The "central maximum" is the bright bar at the center of the pattern, bounded by the first dark fringes on either side. The problem defines its width as the gap between those two flanking minima ($m=0$ in the dark-fringe formula), and that width is $11.9$ mm. Use $\Delta y = \lambda L/d$ to back out the slit spacing $d$.

The "central maximum" of a double-slit pattern is bracketed by the $m=0$ dark fringes at $d\sin\theta = (m+\tfrac12)\lambda$ with $m=-1,0$ (i.e., the two closest dark fringes to center). Their separation: $\Delta y = \lambda L/d$.

$$d = \dfrac{\lambda L}{\Delta y} = \dfrac{(502\times 10^{-9})(2.1)}{0.0119} = 8.86\times 10^{-5}\ \text{m} = \boxed{0.0886\ \text{mm}}$$

---

## Q2 — Wavelength from double-slit position

**Setup.** Standard Young's double-slit setup: $d=0.42$ mm slit spacing, $L=3$ m to the screen, and the *second-order* bright fringe ($m=2$) is observed 4 mm off the center line. Solve $y_m = m\lambda L/d$ for $\lambda$.

$y = m\lambda L/d$ ⇒ $\lambda = yd/(mL)$.
$$\lambda = \dfrac{(0.004)(4.2\times 10^{-4})}{(2)(3)} = \dfrac{1.68\times 10^{-6}}{6} = 2.80\times 10^{-7}\ \text{m} = \boxed{280\ \text{nm}}$$

---

## Q3 — Soap bubble, *enhancement* in reflected light, minimum thickness

**Setup.** A thin spherical soap bubble (water-like film, $n=1.34$) has air on both sides. Light reflecting off the bubble interferes with itself: part reflects off the outer surface, part reflects off the inner surface after a round trip through the film. The problem says reflected light is *enhanced* (constructive in reflection) at $\lambda=481$ nm, and asks for the minimum (thinnest) film thickness that achieves this. Phase-flip bookkeeping: outer reflection (air→water) flips $\pi$, inner reflection (water→air) does not — net 1 flip, which inverts the usual constructive/destructive condition.

Bubble (thin water-like film with air on both sides). Reflections:
- Top (air→film, low→high $n$): $\pi$ flip
- Bottom (film→air, high→low $n$): no flip

Net = 1 flip ⇒ constructive in reflection requires $2nt = (m+\tfrac12)\lambda$.
Minimum: $m=0$ → $2nt = \lambda/2$.
$$t_{\min} = \dfrac{\lambda}{4n} = \dfrac{481}{4(1.34)} = \boxed{89.74\ \text{nm}}$$

---

## Q4 — Antireflection coating on glass

**Setup.** A glass surface ($n_{\text{glass}}=1.7$) gets a thin coating ($n_{\text{coat}}=1.49$); we want the minimum coating thickness that *suppresses* reflection of $\lambda_{\text{vac}}=636$ nm light (destructive interference in reflection). Phase-flip count: light goes air ($1$) → coating ($1.49$) → glass ($1.7$). *Both* reflections are at low-to-high $n$ boundaries, so each flips $\pi$ — net 2 flips, which is equivalent to 0 flips. With no net flip, destructive in reflection requires $2nt = (m+\tfrac12)\lambda$.

Light goes air → coating ($n=1.49$) → glass ($n=1.70$). Both reflections are at low→high boundaries ⇒ both have a $\pi$ flip ⇒ net = 0 flips.

For *destructive* reflection (antireflective): $2nt = (m+\tfrac12)\lambda$.
Minimum: $m=0$ → $t = \lambda/(4n)$.
$$t_{\min} = \dfrac{636}{4(1.49)} = \boxed{106.7\ \text{nm}}$$

---

## Q5 — Qualitative double-slit response

The double-slit fringe spacing is $\Delta y = \lambda L/d$, so $d$ is in the denominator and $L$ in the numerator. Decreasing $d$ (slits closer together) makes the denominator smaller and the fringes farther apart. Decreasing $L$ (screen closer to the slits) directly shrinks the spacing.

Fringe spacing $\Delta y = \lambda L/d$:
- Decreasing $d$ → $\Delta y$ **increases** ✓
- Decreasing $L$ → $\Delta y$ **decreases** ✓

---

## Q6 — Single-slit central-max width

**Setup.** A *single* slit of width $a=0.11$ mm is illuminated with $\lambda=283$ nm light, and the diffraction pattern is observed on a screen $L=2.7$ m away. The central diffraction maximum is bounded by the $m=\pm 1$ minima of $a\sin\theta = m\lambda$, so its full width on the screen is $W \approx 2\lambda L/a$ (twice the small-angle position of the first dark fringe).

$\lambda=283$ nm, $a=0.11$ mm, $L=2.7$ m. Width = $2\lambda L/a$:
$$W = \dfrac{2(283\times 10^{-9})(2.7)}{1.1\times 10^{-4}} = \dfrac{1.528\times 10^{-6}}{1.1\times 10^{-4}} = 0.01389\ \text{m} = \boxed{13.89\ \text{mm}}$$

---

## Q7 — Grating slits/cm to resolve sodium doublet

**Setup.** The sodium D doublet has two close lines at 589.08 nm and 588.53 nm (separation $\Delta\lambda=0.55$ nm). To resolve them in first order ($m=1$) we need a grating with resolving power $R = \bar\lambda/\Delta\lambda = mN$, which sets a *minimum number* of slits $N$ that must be illuminated. The grating is 1.206 cm long, so we get the required line density (lines per cm) by dividing $N$ by the length.

Mean $\bar\lambda = 588.81$ nm; $\Delta\lambda = 0.55$ nm.
$$R = \bar\lambda/\Delta\lambda = 1070.6$$
For first order: $N_{\min} = R/m = 1071$ slits illuminated. Over 1.206 cm:
$$\sigma = N/L = 1071/1.206 = \boxed{888\ \text{lines/cm}}$$

---

## Q8 — Number of maxima observed

**Setup.** A diffraction grating with line density $293$ lines/mm (so slit spacing $d = 1/293\,000$ m) is hit by 649-nm light. The grating equation $d\sin\theta = m\lambda$ has solutions only for $|\sin\theta|\le 1$, which caps the order at $m_{\max}=\lfloor d/\lambda\rfloor$. Total visible maxima = central ($m=0$) plus pairs at each $\pm m$, i.e., $2m_{\max}+1$.

$\sigma = 293$ lines/mm $\Rightarrow d = 1/293{,}000\ \text{m} = 3.413\times 10^{-6}$ m.
$$m_{\max} = \lfloor d/\lambda\rfloor = \lfloor 3.413\times 10^{-6}/(649\times 10^{-9})\rfloor = \lfloor 5.26\rfloor = 5$$
Total maxima = $2(5) + 1 = \boxed{11}$.

---

## Q9 — Bragg spacing

**Setup.** X-ray diffraction off a crystal: $\lambda=1.65$ nm light reflects off planes of atoms at *grazing* angle $\theta=27.6°$ (measured from the plane, not the normal — this is Bragg's convention) and produces a first-order interference maximum ($m=1$). Bragg's law $2d\sin\theta = m\lambda$ gives the spacing $d$ between atomic planes.

$\lambda = 1.65$ nm, $m=1$, $\theta = 27.6°$.
$$d = \dfrac{m\lambda}{2\sin\theta} = \dfrac{1.65}{2\sin(27.6°)} = \dfrac{1.65}{0.9266} = \boxed{1.781\ \text{nm}}$$

---

## Q10 — Eye's resolving power

**Setup.** Diffraction at the pupil sets a hard floor on the angular resolution of the eye: two point sources separated by less than $\theta_{\min}=1.22\lambda/D$ blur into one. With pupil diameter $D=6$ mm and $\lambda=558$ nm (peak human sensitivity), compute $\theta_{\min}$ in radians and convert to milli-degrees.

$D = 6\times 10^{-3}$ m, $\lambda = 558\times 10^{-9}$ m.
$$\theta_{\min} = 1.22\,\lambda/D = \dfrac{1.22(558\times 10^{-9})}{6\times 10^{-3}} = 1.134\times 10^{-4}\ \text{rad}$$
$$\theta_{\min} = 1.134\times 10^{-4}\cdot\dfrac{180°}{\pi} = 6.50\times 10^{-3}°= \boxed{6.50\ \text{millidegrees}}$$

---

## Q11 — Single-slit formula language

The single-slit equation $a\sin\theta = m\lambda$ is the *minimum* (dark-fringe) condition: light from one edge of the slit cancels light from the center when the path difference is a half wavelength, etc. The center of the pattern ($m=0$) is the *bright* central maximum, not a dark fringe, so $m$ runs over nonzero integers. Replacing $m$ by $(m+\tfrac{1}{2})$ shifts halfway between successive minima — approximately where the (much weaker) subsidiary bright maxima sit.

The single-slit equation $a\sin\theta = m\lambda$ locates **dark fringes**, with $m = \pm1, \pm2, \pm3, \ldots$ (zero is the *central maximum*, not a dark fringe).

Replacing $m$ by $(m+\tfrac{1}{2})$ gives the **approximate location of the bright** subsidiary maxima (away from the central one), with $m = \pm1, \pm2, \pm3, \ldots$ as well.

---

**Reminder:** No source key was provided. The "antireflection" thin-film logic and grating-resolution arithmetic are the most error-prone — re-derive if your textbook uses a different sign convention for thin-film phase flips.
