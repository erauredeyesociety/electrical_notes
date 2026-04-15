# Modules 33-36 Review — Midterm 3 Problem Set

This is the comprehensive review/problem set for midterm 3, covering Modules 33 (reflection/refraction/polarization), 34 (mirrors/lenses/optical instruments), 35 (interference), and 36 (diffraction). Every problem is reproduced below with its full solution.

---

## Module 33 — Reflection, Refraction, Polarization

### Question 1 — Two Reflections Off Tilted Mirrors

**Problem:** A beam of light is incident on a mirror lying flat on the ground at an angle of $\theta = 74°$ with respect to the normal. A second mirror is aligned with one edge of the first mirror and tilted up at an angle of $\phi = 40°$. At what angle $\alpha$ with respect to the normal does the ray reflect off the second mirror?

> Figure: Ray strikes a horizontal mirror at $\theta$ from normal, then reflects up to a tilted mirror at angle $\phi$ from horizontal.

**Solution:** Two reflections.

1. First mirror: angle of reflection = angle of incidence = $74°$.
2. The second mirror is tilted $40°$ from horizontal, so its normal is $40°$ from vertical.
3. The angle between the reflected ray (from first mirror) and the normal of the second mirror is $180° - 74° - 40° = 66°$.

So $\alpha' = 66°$, and by law of reflection $\alpha = \alpha' = 66°$.

$$\alpha = 66°$$

### Question 2 — Two Plane Mirrors

**Problem:** The figure (not to scale) shows two plane mirrors and an incident light ray. Find the angle $\alpha$ if $\phi = 58°$ and $\theta = 29°$.

**Solution:** Using law of reflection $\varphi = \varphi'$ and the geometric relation $\varphi = 90° - \alpha$, then applying the triangle angle sum with the other mirror:
$$\gamma + \beta + \phi = 180°, \quad \beta = \alpha, \quad \gamma = 90° - \theta$$

This gives $\alpha = 61°$.

### Question 3 — Speed of Light in a Medium

**Problem:** Suppose the index of refraction of a certain medium is 1.87. Calculate the speed of light in that medium.

**Solution:**
$$v = \frac{c}{n} = \frac{3.00 \times 10^8 \text{ m/s}}{1.87} \approx 1.60 \times 10^8 \text{ m/s}$$

### Question 4 — Wavelength in a Medium

**Problem:** Light with a wavelength of 507 nm in vacuum enters a material with an index of refraction of 2.5. Calculate its wavelength in nm in the medium.

**Solution:**
$$\lambda_{\text{medium}} = \frac{\lambda_{\text{vacuum}}}{n} = \frac{507 \text{ nm}}{2.5} = 202.8 \text{ nm}$$

### Question 5 — Snell's Law

**Problem:** A ray of light traveling in a fluid with index of refraction $n_1 = 1.3$ is incident at an angle of $33°$ with respect to the normal on a transparent material with index of refraction $n_2 = 2.6$. Calculate the refraction angle in degrees.

**Solution:** Using Snell's law $n_1 \sin\theta_1 = n_2 \sin\theta_2$:
$$\theta_2 = \sin^{-1}\left(\frac{n_1}{n_2}\sin\theta_1\right) = \sin^{-1}\left(\frac{1.3}{2.6}\sin 33°\right) \approx 16.14°$$

### Question 6 — Work Backwards Through TIR

**Problem:** A light ray in a glass slab passes into a fluid layer and then undergoes total internal reflection at the fluid-air boundary. Calculate the angle $\theta$ in the glass if $n_g = 2.77$ and $n_f = 1.74$.

**Solution:** Critical angle at fluid-air boundary:
$$\theta_c = \arcsin\left(\frac{1}{n_f}\right) = \arcsin\left(\frac{1}{1.74}\right) \approx 35.61°$$

Within the fluid, angle of incidence must equal $\theta_c$. Applying Snell's law at glass-fluid boundary:
$$n_g \sin\theta = n_f \sin\theta_f$$
$$\sin\theta = \frac{1.74}{2.77}\sin(35.61°) \approx 0.362 \Rightarrow \theta \approx 21.20°$$

### Question 7 — Lateral Shift Through a Glass Pane

**Problem:** A light ray incident on a pane of glass in air with $\theta = 44°$. Calculate the lateral distance $d$ in cm the ray is shifted if $n_{\text{glass}} = 6$ and $h = 9$ cm.

**Solution:** Triangle relations give:
$$d = \frac{h}{\cos r} \sin(\theta - r)$$
where $r = \arcsin\left(\frac{1}{n_{\text{glass}}}\sin\theta\right)$.

Numerical result: $d \approx 4.49$ cm.

### Question 8 — Dispersion Through BK7 Glass

**Problem:** White light incident at $50°$ on top face of BK7 glass block (0.47 m thick). How many mm are wavelengths 2 (475 nm, $n=1.523$) and 4 (625 nm, $n=1.515$) separated at the bottom face?

| Number | Wavelength (nm) | Index of Refraction |
|--------|-----------------|---------------------|
| 1 | 400 | 1.531 |
| 2 | 475 | 1.523 |
| 3 | 550 | 1.519 |
| 4 | 625 | 1.515 |

**Solution:** Each color refracts at its own angle $r_i$ determined by Snell's law. The lateral shift for each color is:
$$\delta_i = h \tan(r_i)$$
where $r_i = \arcsin\left(\frac{\sin\theta}{n_i}\right)$. The relative separation is:
$$\Delta = \delta_2 - \delta_1 = h\left[\tan(r_2) - \tan(r_1)\right] \approx 1.93 \text{ mm}$$

### Question 9 — Critical Angle

**Problem:** A ray of light in a fluid with $n_1 = 2$ encounters a boundary with another fluid having $n_2 = 1.2$. Calculate the critical angle.

**Solution:**
$$\sin\theta_c = \frac{n_2}{n_1} = \frac{1.2}{2} = 0.6$$
$$\theta_c = \arcsin(0.6) \approx 36.87°$$

### Question 10 — Critical Angle Given, Find Refraction Angle

**Problem:** A liquid-air boundary has critical angle $40.1°$. A ray of light in air with incident angle $29°$ at the liquid-air boundary — calculate the angle between the refracted ray and the surface normal.

**Solution:** From $\sin\theta_c = 1/n_{\text{fluid}}$ we get $n_{\text{fluid}} = 1/\sin(40.1°)$. Then:
$$\theta_r = \arcsin\left(\frac{1}{n_{\text{fluid}}}\sin\theta_i\right) = \arcsin(\sin(40.1°)\sin(29°)) \approx 18.61°$$

### Question 11 — Brewster's Angle

**Problem:** Light traveling in air incident on a fluid with index of refraction 1.95. At what angle of incidence is the reflected light completely polarized?

**Solution:**
$$\tan\theta_B = n = 1.95 \Rightarrow \theta_B = \arctan(1.95) \approx 63.6°$$

### Question 12 — Index of Refraction Conceptual

**Statement:** The larger the index of refraction of a given material, the **lower** the speed of light in the material. For a given nonzero angle with respect to the normal, a larger index of refraction means the ray will bend **more** from its original trajectory upon entering from air.

### Question 13 — Polarizing Filters

**Statement:** When unpolarized light encounters a polarization filter, the ray's intensity is reduced by **[1/2]**. If it then encounters a second polarization filter with axis perpendicular to the first filter, the intensity is **[0]**.

---

## Module 34 — Mirrors, Lenses, Optical Instruments

### Question 1 — Flat Mirror

**Problem:** An object is placed 21 cm to the left of a flat mirror. (a) Image position? (b) Magnification? (c) Real or virtual? (d) Upright or inverted?

**Answers:** (a) $s' = -21$ cm, (b) $m = +1$, (c) virtual, (d) upright.

### Question 2 — Concave Spherical Mirror

**Problem:** Concave mirror with focal length 15.6 cm. If object distance is 7.9 cm, calculate image distance $s'$ in cm.

**Solution:** Mirror equation:
$$\frac{1}{f} = \frac{1}{s} + \frac{1}{s'} \Rightarrow s' = \frac{sf}{s-f} = \frac{7.9 \times 15.6}{7.9 - 15.6} \approx -16 \text{ cm}$$

Virtual image (object inside focal length).

### Question 3 — Convex Mirror Magnification

**Problem:** An eggplant is 2.9 cm from vertex of a convex spherical mirror having radius of curvature 14 cm. Calculate the lateral magnification.

**Solution:** $f = R/2 = -7$ cm (convex).
$$s' = \frac{sf}{s-f} = \frac{2.9 \times (-7)}{2.9 - (-7)} \approx -2.05 \text{ cm}$$
$$m = -\frac{s'}{s} = -\frac{-2.05}{2.9} \approx 0.707$$

### Question 4 — Thin Diverging Lens

**Problem:** Diverging lens with focal length 9.00 cm. Object distance 6.0 cm. Find image distance, magnification, and image characteristics.

**Solution:** $f = -9.00$ cm:
$$s' = \frac{sf}{s-f} = \frac{6.0 \times (-9.00)}{6.0 + 9.00} = -3.6 \text{ cm}$$
$$m = -\frac{s'}{s} = \frac{3.6}{6.0} = 0.6$$

Image is **virtual** ($s' < 0$) and **upright** ($m > 0$).

### Question 5 — Lensmaker's Equation

**Problem:** Contact lens made from material with index of refraction 1.8. Front and back surfaces have radii of curvature 1.8 cm and 2.6 cm. Calculate focal length in cm.

**Solution:** For a convex-concave contact lens, $R_1 = +1.8$ cm, $R_2 = -2.6$ cm (assuming convention).
$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

With the problem's sign choice (treating $R_2$ as negative):
$$\frac{1}{f} = (1.8 - 1)\left(\frac{1}{1.8} - \frac{1}{2.6}\right) \Rightarrow f \approx 7.31 \text{ cm}$$

### Question 6 — Apparent Depth

**Problem:** A coin at bottom of a 148 cm deep tank of fluid with $n = 1.56$. Calculate image distance from directly above.

**Solution:** For a flat interface ($R = \infty$):
$$\frac{n_1}{s} + \frac{n_2}{s'} = 0 \Rightarrow s' = -\frac{s}{n_1} = -\frac{148}{1.56} \approx -94.87 \text{ cm}$$

### Question 7 — Two-Lens System

**Problem:** A tiny tree is 23 cm from a converging lens followed by a diverging lens with $L = 11$ cm. Find x-position (cm) of final image if $f_1 = 9$ cm, $|f_2| = 16$ cm (diverging → $f_2 = -16$ cm).

**Solution:** First lens:
$$s_1' = \frac{f_1 s_1}{s_1 - f_1} = \frac{9 \times 23}{23-9} = 14.7857 \text{ cm}$$

Second lens: $s_2 = L - s_1' = 11 - 14.7857 = -3.7857$ cm (virtual object).
$$s_2' = \frac{f_2(L-s_1')}{(L-s_1') - f_2} = \frac{-16 \times (-3.7857)}{-3.7857 + 16} = 4.9590 \text{ cm}$$

### Question 8 — Reading Glasses (Presbyopia)

**Problem:** A man has near point of 50 cm. What power glasses (diopters) to read comfortably at 25.6 cm?

**Solution:** Glasses must image an object at 25.6 cm to virtual image at 50 cm:
$$\frac{1}{f} = \frac{1}{25.6} + \frac{1}{-50} = 0.0191 \text{ cm}^{-1} = 1.91 \text{ m}^{-1}$$
$$P = +1.91 \text{ diopters}$$

### Question 9 — Simple Magnifier

**Problem:** Simple magnifier with focal length 6.7 cm. Calculate magnification.

**Solution:**
$$M = \frac{25 \text{ cm}}{f} = \frac{25}{6.7} = 3.7313$$

### Question 10 — Vision Correction Conceptual

**Statement:** A **diverging** (or concave) lens corrects for near-sightedness. The image it creates is **virtual** and **reduced**. A **converging** (or convex) lens corrects for far-sightedness. The image it creates is **virtual** and **enlarged**.

---

## Module 35 — Interference (labeled "Module 36" in source review)

### Question 1 — Young's Double Slit Wavelength

**Problem:** Monochromatic coherent light on Young's experiment with slit spacing 0.3 mm. Screen 2 m away; $m$-th order maximum is 2.5 mm from center line. Calculate wavelength in nm if $m = 3$.

**Solution:**
$$y_m = \frac{m\lambda D}{d} \Rightarrow \lambda = \frac{y_m d}{mD}$$

With $y_m = 2.5 \times 10^{-3}$ m, $d = 0.3 \times 10^{-3}$ m, $D = 2$ m, $m = 3$:
$$\lambda = \frac{2.5\times 10^{-3} \times 0.3\times 10^{-3}}{3 \times 2} = 125 \text{ nm}$$

### Question 2 — Distance Between Dark Fringes

**Problem:** Two slits 0.33 mm apart, 72 cm from screen. Wavelength 477 nm. Distance in mm between $m = +3$ and $m = +5$ dark lines.

**Solution:** Dark fringes at $y_{\text{dark}} = (m + 1/2)\lambda D/d$:
$$\Delta y = \left[(5+1/2) - (3+1/2)\right]\frac{\lambda D}{d} = 2\frac{\lambda D}{d}$$
$$= 2 \times \frac{477\times 10^{-9} \times 0.72}{0.33\times 10^{-3}} = 2.0815 \text{ mm}$$

### Question 3 — Nonreflective Coating (half-shift on both surfaces)

**Problem:** Flat glass sheet ($n_{\text{glass}} = 1.61$) with thin coating ($n_{\text{coating}} = 1.27$). Minimum thickness for nonreflective (destructive interference) at vacuum wavelength 557 nm.

**Solution:** Both interfaces have $\pi$ phase shift (low→high at both), so destructive interference condition is:
$$2nt = (m+1/2)\lambda$$
For minimum ($m = 0$):
$$t = \frac{\lambda}{4n} = \frac{557}{4 \times 1.27} \approx 109.65 \text{ nm}$$

### Question 4 — Anti-Reflective Film on Solar Cell

**Problem:** Silicon solar cell, $n_{\text{Si}} = 3.88$, coated with film $n = 1.55$. Minimum thickness (nm) that produces least reflection at $\lambda = 480$ nm.

**Solution:** Same phase-shift situation as Q3:
$$t = \frac{\lambda}{4n} = \frac{480}{4 \times 1.55} \approx 77.42 \text{ nm}$$

### Question 4 (second) — Anti-Glare Museum Glass (only one phase shift)

**Problem:** Glass ($n_{\text{glass}} = 1.5$) coated with thin film of $n = 3$. Minimum nonzero thickness (nm) to cancel $\lambda = 501$ nm.

**Solution:** CAREFUL. Upfront reflection at air→film (low→high): $\pi$ shift. At film→glass: $n_{\text{glass}}=1.5 < n_{\text{film}}=3$, so high→low, **no** phase shift. Only one ray has a phase shift, so destructive reflection condition becomes:
$$2nt = m\lambda$$
For minimum nonzero ($m = 1$):
$$t = \frac{\lambda}{2n} = \frac{501}{2\times 3} = 83.5 \text{ nm}$$

### Question 5 — Double-Slit Spacing Conceptual

**Statement:** In a double-slit experiment, decreasing the distance between slits **increases** the distance between bright fringes on the screen. Decreasing the distance to the screen **increases** (actually decreases — check context; the review answer states "increases" meaning increases distance to screen, which is contradictory) — per review answer: decreasing screen distance makes fringes closer, so the answer as written should be "decreases."

---

## Module 36 — Diffraction (labeled section continues after Module 35 review)

### Question 6 — Single-Slit Dark Line

**Problem:** Single-slit with monochromatic coherent light $\lambda = 513$ nm, aperture width 0.38 mm. Screen 2.1 m away. Distance from central max to $m = +3$ dark line (in mm)?

**Solution:** Dark fringes at $\sin\theta = m\lambda/a$; small angle:
$$y_m = \frac{m\lambda D}{a} = \frac{3 \times 513\times 10^{-9} \times 2.1}{0.38\times 10^{-3}} = 2.9 \text{ mm}$$

### Question 7 — Diffraction Grating Wavelength

**Problem:** Grating with 6440 slits/cm. Angular position of second-order bright band is $47°$. Wavelength (nm)?

**Solution:** Slit spacing $d = 1/6440$ cm $= 10^{-2}/6440$ m. From $d\sin\theta = m\lambda$:
$$\lambda = \frac{d\sin\theta}{m} = \frac{(10^{-2}/6440)\sin(47°)}{2}$$

(The review gives the answer in odd units — the proper result is approximately 568 nm.)

### Question 8 — Chromatic Resolving Power

**Problem:** Atom emits two wavelengths: 589.21 nm and 588.54 nm. To resolve in first order using grating 1.114 cm long, minimum slits/cm?

**Solution:** Resolving power:
$$R = \frac{\lambda}{\Delta\lambda} = \frac{589.21}{589.21 - 588.54} = \frac{589.21}{0.67} \approx 879.4$$

And $R = Nm$, so $N = R/m = 879.4$ total slits. Per cm:
$$\frac{N}{\text{length}} = \frac{879.4}{1.114} \approx 789.7 \text{ slits/cm}$$

### Question 9 — Bragg's Law

**Problem:** X-rays of wavelength 0.24 nm incident at grazing angle $16.1°$ on crystal produces first-order fringe. Calculate interatomic spacing (nm) between Bragg planes.

**Solution:** Bragg's law $2d\sin\theta = m\lambda$ with $m = 1$:
$$d = \frac{\lambda}{2\sin\theta} = \frac{0.24}{2\sin(16.1°)} \approx 0.433 \text{ nm}$$

(Review gives $\approx 0.451$ nm.)

### Question 10 — Eye Resolving Power

**Problem:** Pupil diameter 5 mm, light $\lambda = 600$ nm. Resolving power in milli-degrees.

**Solution:** Rayleigh criterion:
$$\theta = \frac{1.22\lambda}{D} = \frac{1.22 \times 600\times 10^{-9}}{5\times 10^{-3}} = 146.4\times 10^{-6} \text{ rad}$$

Convert to milli-degrees: $\theta \times (180/\pi) \times 1000 \approx 8.41$ milli-degrees.

### Question 10 (second) — Telescope Resolution of Astronauts on Moon

**Problem:** Two astronauts 2.4 m apart on moon, viewed from space station 100 km above. Light $\lambda = 525$ nm. Aperture (cm) to just resolve?

**Solution:** Required angular resolution:
$$\theta = \frac{d}{L} = \frac{2.4}{100\times 10^3} = 2.4\times 10^{-5} \text{ rad}$$

Set equal to Rayleigh criterion:
$$D = \frac{1.22\lambda}{\theta} = \frac{1.22 \times 525 \times 10^{-9}}{2.4\times 10^{-5}} \approx 0.266 \text{ m} = 26.6 \text{ cm}$$

### Question 11 — Grating Conceptual

**Statement:** As the number of lines per centimeter increases, the interference fringes created by a diffraction grating **move farther apart**. As the distance between the grating and the screen increases, the interference fringes **move farther apart**.
