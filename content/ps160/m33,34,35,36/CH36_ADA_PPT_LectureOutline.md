# Chapter 36 — Diffraction (Lecture Outline)

Covers single-slit diffraction, diffraction gratings, X-ray diffraction (Bragg's law), circular apertures and resolution limits (Rayleigh's criterion), and holography.

## Learning Outcomes

- Calculate intensity at various points in a single-slit diffraction pattern.
- What happens when coherent light shines on an array of narrow, closely-spaced slits.
- How X-ray diffraction reveals atomic arrangement in a crystal.
- How diffraction sets limits on the smallest details visible with an optical system.
- How holograms work.

## Diffraction

Geometric optics predicts sharp shadows, but the wave nature of light creates interference patterns that blur shadow edges. This is **diffraction** — bending/spreading of waves around obstacles or through apertures.

> Figure: Razor blade shadow photographed with monochromatic light shows fringe pattern at the blade edges — hallmark of diffraction.

## Fresnel vs. Fraunhofer Diffraction

- **Fresnel (near-field) diffraction:** screen close to aperture; rays from different parts of aperture to a point are **not** parallel.
- **Fraunhofer (far-field) diffraction:** screen far from aperture (or imaged by converging lens); rays are approximately **parallel**.

Most analytical results apply to Fraunhofer diffraction.

## Single-Slit Diffraction

Divide the slit (width $a$) into many narrow strips; each acts as a source of Huygens wavelets. Analyze interference of these wavelets at a distant point.

### Location of Dark Fringes (Single Slit)

$$\sin\theta = \frac{m\lambda}{a} \quad (m = \pm 1, \pm 2, \pm 3, \ldots)$$

**Note:** $m = 0$ is NOT a dark fringe — it's the central bright maximum.

The central bright fringe is **twice as wide** as the subsidiary bright fringes (it extends from $m = -1$ to $m = +1$ dark fringes).

### Intensity in Single-Slit Pattern

$$I = I_0 \left[\frac{\sin(\pi a \sin\theta/\lambda)}{\pi a \sin\theta/\lambda}\right]^2$$

Defining $\beta = \pi a\sin\theta/\lambda$:
$$I = I_0\left(\frac{\sin\beta}{\beta}\right)^2$$

Most of the wave power is in the central peak. Side maxima are at $I \approx 0.047 I_0, 0.017 I_0, 0.008 I_0$ for $m = 1, 2, 3$.

### Width of the Single-Slit Pattern

Depends on ratio $a/\lambda$:
- $a \ll \lambda$: single broad maximum (essentially no structure).
- $a \approx \lambda$: very wide central peak.
- $a \gg \lambda$: narrow central peak with many side lobes (approaches geometric optics).

## Two Slits of Finite Width

Real double-slit patterns combine two-slit **interference** (narrow fringes at $d\sin\theta = m_i\lambda$) with single-slit **diffraction envelope** (wider dark fringes at $a\sin\theta = m_d\lambda$).

- Every interference fringe where $m_i/m_d = d/a$ is a "missing order" (fringe location coincides with diffraction minimum).

> Figure: Two-slit pattern modulated by single-slit envelope. For $d = 4a$, every 4th interference max is missing.

## Several Slits / Multi-Slit Interference

With $N$ slits separated by $d$, principal maxima occur at the same angles as for two slits:
$$d\sin\theta = m\lambda$$

### Properties

- Height of each principal maximum $\propto N^2$.
- Width of each principal maximum $\propto 1/N$ (sharper as $N$ increases).
- Between principal maxima there are $N - 2$ subsidiary maxima and $N - 1$ minima.

## The Diffraction Grating

An array of a very large number of parallel equally-spaced slits (transmission) or grooves (reflection). Used for spectroscopy.

### Intensity Maxima

$$d\sin\theta = m\lambda \quad (m = 0, \pm 1, \pm 2, \ldots)$$

DVDs and CDs act as reflection gratings — colorful reflections come from the uniform spacing of pits.

### Chromatic Resolving Power

Ability to distinguish two close wavelengths:
$$R = \frac{\lambda}{\Delta\lambda} = Nm$$

where $N$ is the total number of slits and $m$ is the order.

## X-Ray Diffraction — Bragg's Law

When X-rays pass through a crystal, the crystal lattice acts as a 3-D diffraction grating. Constructive interference requires:

$$2d\sin\theta = m\lambda \quad (m = 1, 2, 3, \ldots)$$

where $d$ is the spacing between adjacent parallel planes (Bragg planes) and $\theta$ is the **grazing** angle (measured from the plane, not the normal).

Used to determine crystal structures (e.g., DNA).

## Circular Aperture Diffraction

The diffraction pattern from a circular aperture of diameter $D$ is a central bright spot — the **Airy disk** — surrounded by concentric dark and bright rings.

### Angular Radius of Airy Disk

$$\sin\theta_1 = 1.22 \frac{\lambda}{D}$$

(Angle to first dark ring.)

## Rayleigh's Criterion — Resolution Limit

Two point objects are just barely resolved when the center of one diffraction pattern coincides with the first minimum of the other. Minimum resolvable angular separation:

$$\theta_{\min} = 1.22 \frac{\lambda}{D}$$

**Larger aperture → better resolution.** This is why large telescopes see finer detail. VLA radio telescope arrays use many dishes as an effective large aperture.

## Holography

Uses coherent laser light split into object beam (illuminates object) and reference beam. Film records the interference pattern between them — the **hologram**. Illuminating the hologram with the reference beam reconstructs the 3-D image.

> Figure: Hologram reconstruction creates both real and virtual 3-D images; parallax visible as you shift viewing angle.

## In-Class Problems

### Q6 — Single-Slit Wavelength

Slit width 0.18 mm, screen 1.8 m, $m = 5$ minimum at 8 mm from central max. Wavelength?

Small angle: $y_m = m\lambda D/a$:
$$\lambda = \frac{y_m a}{m D} = \frac{8\times 10^{-3}\times 0.18\times 10^{-3}}{5\times 1.8} = 160 \text{ nm}$$

### Q7 — Minimum Slits to Resolve Two Wavelengths

$\lambda_1 = 589.22$ nm, $\lambda_2 = 588.5$ nm, first order, grating 1.902 cm long. Min slits/cm?

$R = \lambda/\Delta\lambda = 589.22/0.72 \approx 818.4$. $N = R/m = 818.4$. Per cm: $818.4/1.902 \approx 430$.

### Q8 — Grating Distance to m=2 Max

347 lines/cm, $\lambda = 553$ nm, screen 2.3 m. Distance to $m = 2$ max (cm)?

$d = 10^{-2}/347$ m $\approx 2.88\times 10^{-5}$ m.
$$\sin\theta = m\lambda/d = 2\times 553\times 10^{-9}/2.88\times 10^{-5} \approx 0.0384$$
$$y = R\tan\theta \approx 2.3 \times 0.0384 \approx 8.84 \text{ cm}$$

### Q9 — Bragg Spacing

$\lambda = 0.2$ nm, grazing angle $15.9°$, first order:
$$d = \frac{\lambda}{2\sin\theta} = \frac{0.2}{2\sin(15.9°)} \approx 0.365 \text{ nm}$$

### Q10 — Telescope Resolving Crater on Mars

Aperture 5.6 cm, $\lambda = 530$ nm, orbit 1833 km above Mars surface. Min crater width?
$$\theta_{\min} = 1.22\lambda/D = 1.22\times 530\times 10^{-9}/5.6\times 10^{-2} \approx 1.155\times 10^{-5} \text{ rad}$$
$$\text{Width} = \theta_{\min}\times L \approx 1.155\times 10^{-5}\times 1.833\times 10^{6} \approx 21.2 \text{ m}$$

## Key Equations Summary — Chapter 36

- Single-slit dark fringes: $\sin\theta = m\lambda/a$ ($m = \pm 1, \pm 2, \ldots$)
- Single-slit intensity: $I = I_0[\sin(\pi a\sin\theta/\lambda)/(\pi a\sin\theta/\lambda)]^2$
- Multi-slit / grating maxima: $d\sin\theta = m\lambda$
- Chromatic resolving power: $R = \lambda/\Delta\lambda = Nm$
- Bragg's law: $2d\sin\theta = m\lambda$ (grazing angle)
- Circular aperture first dark ring: $\sin\theta_1 = 1.22\lambda/D$
- Rayleigh criterion: $\theta_{\min} = 1.22\lambda/D$
