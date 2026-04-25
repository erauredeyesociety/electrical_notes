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

The "central maximum" of a double-slit pattern is bracketed by the $m=0$ dark fringes at $d\sin\theta = (m+\tfrac12)\lambda$ with $m=-1,0$ (i.e., the two closest dark fringes to center). Their separation: $\Delta y = \lambda L/d$.

$$d = \dfrac{\lambda L}{\Delta y} = \dfrac{(502\times 10^{-9})(2.1)}{0.0119} = 8.86\times 10^{-5}\ \text{m} = \boxed{0.0886\ \text{mm}}$$

---

## Q2 — Wavelength from double-slit position

$y = m\lambda L/d$ ⇒ $\lambda = yd/(mL)$.
$$\lambda = \dfrac{(0.004)(4.2\times 10^{-4})}{(2)(3)} = \dfrac{1.68\times 10^{-6}}{6} = 2.80\times 10^{-7}\ \text{m} = \boxed{280\ \text{nm}}$$

---

## Q3 — Soap bubble, *enhancement* in reflected light, minimum thickness

Bubble (thin water-like film with air on both sides). Reflections:
- Top (air→film, low→high $n$): $\pi$ flip
- Bottom (film→air, high→low $n$): no flip

Net = 1 flip ⇒ constructive in reflection requires $2nt = (m+\tfrac12)\lambda$.
Minimum: $m=0$ → $2nt = \lambda/2$.
$$t_{\min} = \dfrac{\lambda}{4n} = \dfrac{481}{4(1.34)} = \boxed{89.74\ \text{nm}}$$

---

## Q4 — Antireflection coating on glass

Light goes air → coating ($n=1.49$) → glass ($n=1.70$). Both reflections are at low→high boundaries ⇒ both have a $\pi$ flip ⇒ net = 0 flips.

For *destructive* reflection (antireflective): $2nt = (m+\tfrac12)\lambda$.
Minimum: $m=0$ → $t = \lambda/(4n)$.
$$t_{\min} = \dfrac{636}{4(1.49)} = \boxed{106.7\ \text{nm}}$$

---

## Q5 — Qualitative double-slit response

Fringe spacing $\Delta y = \lambda L/d$:
- Decreasing $d$ → $\Delta y$ **increases** ✓
- Decreasing $L$ → $\Delta y$ **decreases** ✓

---

## Q6 — Single-slit central-max width

$\lambda=283$ nm, $a=0.11$ mm, $L=2.7$ m. Width = $2\lambda L/a$:
$$W = \dfrac{2(283\times 10^{-9})(2.7)}{1.1\times 10^{-4}} = \dfrac{1.528\times 10^{-6}}{1.1\times 10^{-4}} = 0.01389\ \text{m} = \boxed{13.89\ \text{mm}}$$

---

## Q7 — Grating slits/cm to resolve sodium doublet

Mean $\bar\lambda = 588.81$ nm; $\Delta\lambda = 0.55$ nm.
$$R = \bar\lambda/\Delta\lambda = 1070.6$$
For first order: $N_{\min} = R/m = 1071$ slits illuminated. Over 1.206 cm:
$$\sigma = N/L = 1071/1.206 = \boxed{888\ \text{lines/cm}}$$

---

## Q8 — Number of maxima observed

$\sigma = 293$ lines/mm $\Rightarrow d = 1/293{,}000\ \text{m} = 3.413\times 10^{-6}$ m.
$$m_{\max} = \lfloor d/\lambda\rfloor = \lfloor 3.413\times 10^{-6}/(649\times 10^{-9})\rfloor = \lfloor 5.26\rfloor = 5$$
Total maxima = $2(5) + 1 = \boxed{11}$.

---

## Q9 — Bragg spacing

$\lambda = 1.65$ nm, $m=1$, $\theta = 27.6°$.
$$d = \dfrac{m\lambda}{2\sin\theta} = \dfrac{1.65}{2\sin(27.6°)} = \dfrac{1.65}{0.9266} = \boxed{1.781\ \text{nm}}$$

---

## Q10 — Eye's resolving power

$D = 6\times 10^{-3}$ m, $\lambda = 558\times 10^{-9}$ m.
$$\theta_{\min} = 1.22\,\lambda/D = \dfrac{1.22(558\times 10^{-9})}{6\times 10^{-3}} = 1.134\times 10^{-4}\ \text{rad}$$
$$\theta_{\min} = 1.134\times 10^{-4}\cdot\dfrac{180°}{\pi} = 6.50\times 10^{-3}°= \boxed{6.50\ \text{millidegrees}}$$

---

## Q11 — Single-slit formula language

The single-slit equation $a\sin\theta = m\lambda$ locates **dark fringes**, with $m = \pm1, \pm2, \pm3, \ldots$ (zero is the *central maximum*, not a dark fringe).

Replacing $m$ by $(m+\tfrac{1}{2})$ gives the **approximate location of the bright** subsidiary maxima (away from the central one), with $m = \pm1, \pm2, \pm3, \ldots$ as well.

---

**Reminder:** No source key was provided. The "antireflection" thin-film logic and grating-resolution arithmetic are the most error-prone — re-derive if your textbook uses a different sign convention for thin-film phase flips.
