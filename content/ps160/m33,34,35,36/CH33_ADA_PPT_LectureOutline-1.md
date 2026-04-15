# Chapter 33 — The Nature and Propagation of Light (Lecture Outline)

This is the slide-deck version of Ch 33. Content is largely parallel to the Ch33-1 textbook notes; see that file for fuller prose. Below are the key equations, definitions, and lecture-specific in-class questions.

## Learning Outcomes

- What light rays are and how they relate to wave fronts.
- Laws of reflection and refraction of light.
- Conditions for total internal reflection.
- How to make polarized light from ordinary light.
- How scattering explains the blue sky.
- Huygens's principle and its use in analyzing reflection/refraction.

## Waves and Wave Fronts

A **wave front** is the locus of all adjacent points at which the phase of a wave is the same. Spherical wave fronts from a point source; plane wave fronts far from the source.

A **ray** is an imaginary line along the direction of travel of the wave. In a homogeneous, isotropic medium, rays are straight lines perpendicular (normal) to wave fronts.

## Reflection and Refraction

When a light wave strikes a smooth interface between two transparent materials, it is partly reflected and partly refracted (transmitted). Specular reflection from smooth surfaces; diffuse reflection from rough surfaces.

## Index of Refraction

$$n = \frac{c}{v}$$
where $c$ is the speed of light in vacuum and $v$ is the speed in the material. Higher $n$ → slower speed → ray bends toward the normal.

**Reference table (yellow sodium light $\lambda_0 = 589$ nm):**

| Substance | $n$ |
|-----------|-----|
| Ice | 1.309 |
| Water (20°C) | 1.333 |
| Glycerine | 1.473 |
| Crown glass | 1.52 |
| Rock salt | 1.544 |
| Quartz | 1.544 |
| Diamond | 2.417 |

## Law of Reflection

$$\theta_r = \theta_a$$
All angles measured from the normal.

## Law of Refraction (Snell's Law)

$$n_a \sin\theta_a = n_b \sin\theta_b$$

Three cases:
1. **Entering denser medium** ($n_b > n_a$): ray bends **toward** normal.
2. **Entering less dense medium** ($n_b < n_a$): ray bends **away** from normal.
3. **Normal incidence** ($\theta_a = 0$): ray passes straight through.

## Index of Refraction and Wave Aspects

- Frequency $f$ **unchanged** across an interface.
- Wavelength:
$$\lambda = \frac{\lambda_0}{n}$$
- Wave speed changes: waves are "squeezed" when entering slower medium.

## In-Class Question 1 — Two Perpendicular Mirrors

Two mirrors are arranged perpendicular to each other. A ray is incident on the vertical mirror at $46°$ from the normal. Find $\phi$ (angle with respect to normal of the horizontal mirror).

Answer: $\phi = 90° - 46° = 44°$ (perpendicular mirrors preserve the sum = 90°).

## In-Class Question 2

Index of refraction 3.39. Speed of light in medium?
$$v = c/n = 3.00\times 10^8 / 3.39 \approx 0.885 \times 10^8 \text{ m/s}$$

## In-Class Question 3

Speed of light in material = 121,567 km/s. Find index.
$$n = c/v = 3\times 10^8 / (1.21567\times 10^8) \approx 2.467$$

## In-Class Question 5 — Prism

Light perpendicular to a prism face with $\theta = 53°$, $\phi = 39°$. Calculate prism's index of refraction.

Since the ray enters perpendicular to the first face, it hits the second face at incidence angle equal to the prism apex angle. Use Snell's law at the exit face:
$$n\sin\theta_{\text{inside}} = \sin\phi_{\text{outside}}$$

## Total Internal Reflection

Occurs only when $n_b < n_a$. Critical angle:
$$\sin\theta_{\text{crit}} = \frac{n_b}{n_a}$$

For $\theta_a > \theta_{\text{crit}}$: 100% reflection. Fiber optics application.

## In-Class Question 7

Light in fluid with $n = 1.67$ hits air boundary. Find critical angle.
$$\theta_c = \arcsin(1/1.67) \approx 36.8°$$

## In-Class Question 8

Liquid-air boundary has critical angle $41°$. Light in air incident at $34°$. Find refraction angle.

$n_{\text{fluid}} = 1/\sin(41°)$, then $\theta_r = \arcsin(\sin(41°)\sin(34°))$.

## Dispersion

Speed of light in material varies with wavelength. $n$ **decreases** with increasing wavelength. Prism disperses white light into a **spectrum**.

## In-Class Question 6 — Dispersion in BK7

White light at $51°$ on BK7 block 0.3 m thick. How many mm are wavelengths 2 (475 nm, $n=1.523$) and 4 (625 nm, $n=1.515$) separated at the bottom?

Each color has its own refraction angle $r_i = \arcsin(\sin(51°)/n_i)$; lateral shift $= h\tan r_i$; compute difference.

## Rainbows

- Primary rainbow: single internal reflection; $\Delta = 40.8°$ (violet) to $42.5°$ (red).
- Secondary rainbow: two internal reflections; colors reversed; broader.

## Polarization

An EM wave is **linearly polarized** if $\vec{E}$ has only one transverse component. Unpolarized (natural) light is a random mixture.

A **Polaroid** polarizing filter transmits only $\vec{E}$ parallel to its axis.

## Malus's Law

$$I = I_{\max}\cos^2\phi$$

where $\phi$ is the angle between the polarization direction of the incident polarized light and the analyzer axis. For unpolarized input, first polarizer gives $I_0/2$.

## In-Class Question 9 — Three Polarizers

Unpolarized 12 W/cm² through three filters at $23°, 36°, 23°$ from vertical.

- After 1st polarizer: $I_1 = 12/2 = 6$ W/cm², polarization at $23°$.
- After 2nd: angle between filters = $36° - 23° = 13°$, $I_2 = 6\cos^2(13°)$.
- After 3rd: angle = $36° - 23° = 13°$, $I_3 = I_2\cos^2(13°) = 6\cos^4(13°) \approx 5.44$ W/cm².

## Polarization by Reflection — Brewster's Law

At the **polarizing angle** (Brewster's angle), reflected light is 100% polarized perpendicular to the plane of incidence. Reflected and refracted rays are perpendicular.

$$\tan\theta_p = \frac{n_b}{n_a}$$

## In-Class Question 10

Air → fluid with $n = 2.16$. Brewster's angle?
$$\theta_B = \arctan(2.16) \approx 65.2°$$

## Circular Polarization

$\vec{E}$ rotates with constant magnitude around the direction of propagation. Right circularly polarized (clockwise toward observer), left circularly polarized (counterclockwise). 3-D movie glasses use circular polarizers.

## Scattering of Light

Daytime sky is sunlight scattered by air molecules. Scattered intensity $\propto 1/\lambda^4$ → blue sky (blue scatters 15× more than red). Clouds scatter all $\lambda$ equally (droplets > wavelength) → white.

## Huygens's Principle

Every point on a wave front is a source of secondary wavelets spreading at wave speed $v$. The new wave front is the envelope (tangent surface) of these wavelets. Used to derive both law of reflection and Snell's law.

## Key Equations Summary

- $n = c/v$
- $\theta_r = \theta_a$
- $n_a\sin\theta_a = n_b\sin\theta_b$
- $\lambda = \lambda_0/n$
- $\sin\theta_{\text{crit}} = n_b/n_a$
- $I = I_{\max}\cos^2\phi$ (Malus)
- $\tan\theta_p = n_b/n_a$ (Brewster)
