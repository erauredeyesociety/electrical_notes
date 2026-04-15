# Chapter 35 — Interference (Lecture Outline)

Covers superposition of waves, two-source interference (Young's double-slit), intensity in interference patterns, thin-film interference, and the Michelson interferometer.

## Learning Outcomes

- What happens when two waves combine (interfere) in space.
- Interference pattern from two coherent light waves.
- Calculating intensity at various points in an interference pattern.
- Interference when light reflects from both surfaces of a thin film.
- How interference makes it possible to measure extremely small distances.

## Principle of Superposition

**Interference** = any situation where two or more waves overlap in space.

**Principle of superposition:** When two or more waves overlap, the resultant displacement at any point and any instant is the sum of the instantaneous displacements from the individual waves alone.

## Two-Source Interference

For two identical **in-phase** sinusoidal sources $S_1$ and $S_2$:

### Constructive Interference

Path difference is an integral number of wavelengths:
$$r_2 - r_1 = m\lambda \quad (m = 0, \pm 1, \pm 2, \ldots)$$

Waves arrive in phase and reinforce each other.

### Destructive Interference

Path difference is a half-integral number of wavelengths:
$$r_2 - r_1 = \left(m + \frac{1}{2}\right)\lambda$$

Waves arrive out of phase by $\pi$ and cancel.

### Antinodal and Nodal Curves

Antinodal curves: loci of constructive interference (labelled by integer $m$). Nodal curves: loci of destructive interference.

> Figure: Two point sources radiate circular wave fronts; red hyperbolic antinodal curves emanate from between them, labelled $m = 0, \pm 1, \pm 2, \ldots$.

## Two-Source Interference of Light — Young's Double-Slit Experiment

Thomas Young's historic experiment: monochromatic coherent light illuminates two narrow slits $S_1, S_2$ separated by $d$, producing an interference pattern on a distant screen.

### Geometry

For screen at distance $R \gg d$, the rays from the two slits to point $P$ are nearly parallel, and the path difference is:
$$r_2 - r_1 = d\sin\theta$$

### Condition for Bright Fringes (Constructive)

$$d\sin\theta = m\lambda \quad (m = 0, \pm 1, \pm 2, \ldots)$$

### Condition for Dark Fringes (Destructive)

$$d\sin\theta = \left(m + \frac{1}{2}\right)\lambda$$

### Small-Angle Approximation — Fringe Position on Screen

For small $\theta$, $\sin\theta \approx \tan\theta = y/R$, so the $m$-th bright fringe is at:
$$y_m = \frac{m\lambda R}{d}$$

Fringe spacing $\Delta y = \lambda R/d$.

## Intensity in Interference Patterns

To find intensity at any point $P$ in the two-source pattern, combine the two sinusoidal $\vec{E}$ fields. If both have amplitude $E$, the combined amplitude is:

$$E_P = 2E\left|\cos\frac{\phi}{2}\right|$$

where $\phi$ is the phase difference between the waves.

### Intensity

$$I = I_0 \cos^2\left(\frac{\phi}{2}\right)$$

where $I_0$ is the maximum intensity (4× the intensity of each individual source).

### Phase Difference

$$\phi = \frac{2\pi}{\lambda}(r_2 - r_1) = k(r_2 - r_1)$$

### Phasor Representation

Each sinusoidal wave is a rotating phasor; the resultant is found by vector addition of the phasors. Used for deriving the $\cos(\phi/2)$ amplitude result.

## Interference in Thin Films

Light reflecting from the top and bottom surfaces of a thin film (e.g., soap bubble, oil slick) interferes. Phase difference comes from **two** sources:

1. **Path difference** of $2t$ (approximately, for normal incidence), adjusted for the wavelength in the film $\lambda/n$.
2. **Phase shift upon reflection** — occurs when light reflects off a denser medium (lower $n$ → higher $n$).

### Phase Shifts During Reflection

- Reflecting off a **higher-index** medium ($n_a < n_b$): $\pi$ phase shift (inversion).
- Reflecting off a **lower-index** medium ($n_a > n_b$): **no** phase shift.

Analogous to a wave on a rope reflecting from a rigid (inversion) or free (no inversion) end.

### Conditions for Thin-Film Interference

**Case A** — Neither or both reflected waves have a half-cycle phase shift:
$$2t = m\lambda \quad \text{(constructive reflection)}$$
$$2t = \left(m+\frac{1}{2}\right)\lambda \quad \text{(destructive reflection)}$$

**Case B** — Only one reflected wave has a half-cycle phase shift:
$$2t = \left(m+\frac{1}{2}\right)\lambda \quad \text{(constructive)}$$
$$2t = m\lambda \quad \text{(destructive)}$$

Where $\lambda$ is the wavelength **in the film** = $\lambda_0/n$.

### Example: Soap Film in Air

$n_{\text{film}} > n_{\text{air}} = 1$, so front surface (air → film) has $\pi$ shift; back surface (film → air) has no shift. **One half-cycle phase shift total.** Condition for **constructive** reflection:
$$2t = \left(m+\frac{1}{2}\right)\frac{\lambda_0}{n}$$

### Nonreflective (Anti-Reflective) Coatings

Film with intermediate index between air and glass ($n_{\text{air}} < n_{\text{film}} < n_{\text{glass}}$) produces $\pi$ phase shift at **both** interfaces → phase difference due to reflection is zero → destructive interference requires half-integer path difference:
$$2t = \left(m+\frac{1}{2}\right)\frac{\lambda_0}{n_{\text{film}}}$$

Minimum thickness ($m = 0$):
$$t_{\min} = \frac{\lambda_0}{4 n_{\text{film}}}$$

## Michelson Interferometer

A monochromatic light source sends light to a beam splitter. Two beams travel to mirrors $M_1$ (fixed) and $M_2$ (movable), reflect, recombine at the splitter, and interfere at the observer's eye. Moving $M_2$ by $\lambda/2$ shifts the fringe pattern by one fringe.

### Uses

- Precisely measure small displacements.
- Measure wavelength.
- Historic role: Michelson-Morley experiment demonstrated constancy of $c$.

## In-Class Problems

### Q1 — Distance Between Dark Lines

Slits 0.3 mm apart, 113 cm from screen, $\lambda = 590$ nm. Distance (mm) between $m = +2$ and $m = +4$ dark lines.

Dark fringes: $y_m = (m + 1/2)\lambda R/d$.
$$\Delta y = 2\frac{\lambda R}{d} = 2 \times \frac{590 \times 10^{-9} \times 1.13}{0.3\times 10^{-3}} \approx 4.45 \text{ mm}$$

### Q2 — Width of Central Maximum

$\lambda = 600$ nm, $d = 0.11$ mm, screen 2.8 m. Width of central max = distance between $m = 0$ dark bands on either side.

Two $m = 0$ dark bands at $y = \pm (1/2)\lambda R/d$:
$$\text{Width} = \frac{\lambda R}{d} = \frac{600\times 10^{-9}\times 2.8}{1.1\times 10^{-4}} \approx 15.3 \text{ mm}$$

### Q3 — Anti-Reflective Glass Coating

Glass $n = 1.5$, film $n = 2.9$, $\lambda = 533$ nm. Film has higher index than glass → only one phase shift (at air-film). Destructive reflection:
$$2nt = m\lambda \Rightarrow t_{\min}(m=1) = \frac{\lambda}{2n} = \frac{533}{2\times 2.9} \approx 91.9 \text{ nm}$$

### Q4 — Enhancement in Soap Bubble

Soap bubble $n = 1.48$, enhancement (constructive) at $\lambda = 532$ nm. One phase shift at the outer air-film interface.

Constructive:
$$2nt = (m+1/2)\lambda \Rightarrow t_{\min}(m=0) = \frac{\lambda}{4n} = \frac{532}{4\times 1.48} \approx 89.9 \text{ nm}$$

## Key Equations Summary — Chapter 35

- Constructive (two slits): $d\sin\theta = m\lambda$
- Destructive (two slits): $d\sin\theta = (m + 1/2)\lambda$
- Small-angle fringe position: $y_m = m\lambda R/d$
- Fringe spacing: $\Delta y = \lambda R/d$
- Intensity in two-source interference: $I = I_0\cos^2(\phi/2)$
- Phase difference: $\phi = (2\pi/\lambda)(r_2 - r_1) = k(r_2 - r_1)$
- Wavelength in film: $\lambda_{\text{film}} = \lambda_0/n$
- Thin-film (one phase shift, constructive reflection): $2nt = (m+1/2)\lambda_0$
- Thin-film (no/two phase shifts, constructive reflection): $2nt = m\lambda_0$
- Minimum nonreflective coating: $t = \lambda_0/(4n)$
