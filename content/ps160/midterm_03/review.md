# PS160 Midterm 3 (Final) --- Topics and Theory Review

**Scope:** Modules 33 (Electromagnetic Waves), 34 (Geometric Optics), 35 (Interference), 36 (Diffraction).

**Comprehensive exam** --- midterms 1 and 2 content is also testable, but the emphasis is on chapters 33--36 (light propagation, optics).

**Companion files:**
- [equations.tex](equations.tex) --- equation sheet for midterm 3 (Ch 33-36)
- [master_equations.tex](master_equations.tex) --- ALL course equations, for comprehensive review
- [master_topics.md](master_topics.md) --- brief listing of every topic on the course
- [study_plan.md](study_plan.md) --- week-by-week prep schedule
- [../midterm_01/review.md](../midterm_01/review.md) --- midterm 1 theory refresher
- [../midterm_02/review.md](../midterm_02/review.md) --- midterm 2 theory refresher

---

## Module 33 --- Electromagnetic Waves

### Topics
- Maxwell's equations (conceptual)
- Plane electromagnetic waves in vacuum
- Speed of light from $c = 1/\sqrt{\mu_0\varepsilon_0}$
- Transverse nature, $\vec{E}\perp\vec{B}\perp\vec{k}$, and $E/B = c$
- Energy density, Poynting vector, intensity
- Radiation pressure
- Polarization, Malus's law
- Brewster's angle

### Theory

**Maxwell's equations** unify electricity and magnetism. In vacuum and in the absence of charges/currents, they imply a wave equation for $\vec{E}$ and $\vec{B}$ with wave speed $c = 1/\sqrt{\mu_0\varepsilon_0}$. The key conceptual takeaway: **a changing electric field generates a magnetic field (displacement current) and a changing magnetic field generates an electric field (Faraday's law). Together, they self-sustain as a traveling wave.**

**Plane EM wave:** $\vec{E}$ and $\vec{B}$ oscillate in phase, perpendicular to each other and to the propagation direction. They are related by $E = cB$ always. The direction of propagation is $\vec{E}\times\vec{B}$.

**In a dielectric medium** light slows to $v = c/n$. The frequency is unchanged (set by the source); the wavelength shortens to $\lambda_0/n$.

**Energy:** The electric and magnetic fields carry equal amounts of energy ($\tfrac{1}{2}\varepsilon_0 E^2 = B^2/(2\mu_0)$). The **Poynting vector** $\vec{S} = (1/\mu_0)\vec{E}\times\vec{B}$ points in the direction of energy flow and has magnitude equal to the instantaneous power per unit area. For a sinusoidal wave the time-average intensity is $I = \tfrac{1}{2}c\varepsilon_0 E_{\max}^2$.

**Radiation pressure:** Light carries momentum $p = U/c$, so it exerts pressure $I/c$ on a perfect absorber and $2I/c$ on a perfect reflector (momentum reversal doubles the impulse).

**Polarization.** Unpolarized light passed through an ideal polarizer becomes linearly polarized with half the intensity. Two ideal polarizers in series: if the angle between their axes is $\phi$, Malus's law gives $I = I_{\max}\cos^2\phi$. Three polarizers at $0°$/$45°$/$90°$ transmit $I_0/2 \cdot \cos^2 45° \cdot \cos^2 45° = I_0/8$ — classic problem.

**Brewster's angle:** Light reflected at $\theta_B$ from an interface where $\tan\theta_B = n_2/n_1$ is fully polarized perpendicular to the plane of incidence.

### Common problem archetypes
- Given $E_{\max}$ (or power + area), find $B_{\max}$ and $I$.
- Solar constant + geometry → radiation pressure or force on a solar sail.
- Chain of polarizers at arbitrary angles.
- Find $\theta_B$ for air-glass, air-water, etc.

---

## Module 34 --- Geometric Optics

### Topics
- Reflection and refraction
- Snell's law, index of refraction
- Total internal reflection, critical angle
- Dispersion (brief)
- Plane, spherical, and parabolic mirrors
- Thin lenses: converging and diverging
- Image formation (ray diagrams)
- Magnification
- Optical instruments (magnifier, microscope, telescope, eye)

### Theory

**Geometric optics** treats light as rays — valid whenever feature sizes are $\gg\lambda$. Two basic laws: reflection ($\theta_i = \theta_r$) and refraction (Snell: $n_1\sin\theta_1 = n_2\sin\theta_2$).

**Index of refraction** $n = c/v$ is dimensionless, $\ge 1$ for ordinary materials. Frequency of light stays fixed between media; wavelength and speed scale by $1/n$.

**Total internal reflection** happens when going from higher to lower $n$ and the angle of incidence exceeds $\sin^{-1}(n_2/n_1)$. No transmitted ray — all the light reflects. This is how fiber optics work.

**Mirror equation / thin lens equation (same form):**
$$\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}$$
You *must* get the sign convention right. A common one (used in Young & Freedman):
- $s > 0$ if the object is on the incoming side of the optical element (usually the case).
- $s' > 0$ if the image is on the *outgoing* side (transmitted side for a lens, reflected side for a mirror). $s' < 0$ is a virtual image (on the same side as the object for a lens, or behind the mirror).
- $f > 0$ for converging elements (concave mirror, convex lens), $f < 0$ for diverging elements.
- $R > 0$ if the center of curvature is on the outgoing side.

**Magnification:** $m = -s'/s$. Negative $m$ = inverted image; $|m| > 1$ = enlarged.

**Lensmaker's equation:** $\tfrac{1}{f} = (n - 1)(1/R_1 - 1/R_2)$ — lets you design a lens given the material and the two radii of curvature. $R_i$ are signed — $R_1$ is the first surface the light hits.

**Ray-tracing rules for converging thin lens:**
1. Ray parallel to axis goes through the far focal point after the lens.
2. Ray through the center of the lens passes undeviated.
3. Ray through the near focal point emerges parallel to the axis.
The image is where any two rays intersect. Diverging lens: "through" $F$ is replaced by "heading toward" $F$.

**Two-lens systems:** The image formed by the first lens is the object for the second. If the first image forms a distance $d - s_1'$ in front of (or behind) the second lens, that's $s_2$. Overall magnification is the product. This gives a compound microscope or a telescope.

**Telescope** (in normal adjustment, image at infinity): angular magnification $M = -f_{\text{obj}}/f_{\text{eye}}$.

### Common problem archetypes
- Snell's law from air into water/glass; critical angle.
- Ray diagram to predict image location and character for converging/diverging lenses.
- Multi-lens (microscope or telescope) systems.
- Apparent depth: $d_{\text{apparent}} = d_{\text{real}} \cdot (n_{\text{observer}}/n_{\text{medium}})$.

---

## Module 35 --- Interference

### Topics
- Coherence
- Superposition of two coherent waves
- Young's double-slit experiment
- Intensity pattern of two-source interference
- Thin-film interference, phase shifts at interfaces
- Newton's rings and air wedges
- Michelson interferometer

### Theory

**Coherence:** Two sources are coherent if their relative phase is fixed in time. Independent sources (like two bulbs) are *not* coherent; splitting one beam (by slits, or by a partially reflecting surface) *is*. Coherence is a prerequisite for observing stable interference fringes.

**Young's double slit:** Two slits separated by $d$ are illuminated by a coherent plane wave. The path difference to a point at angle $\theta$ on the screen is $d\sin\theta$. Constructive interference (bright fringes) when $d\sin\theta = m\lambda$; destructive when $d\sin\theta = (m + \tfrac{1}{2})\lambda$. For small angles and screen distance $R$: $y_m = m\lambda R/d$. Fringe spacing is $\Delta y = \lambda R/d$ — a larger screen distance or smaller slit separation spreads fringes out.

**Intensity pattern:** $I(\theta) = I_0\cos^2(\pi d\sin\theta/\lambda)$. Note that this is an idealization — in reality it's modulated by the single-slit envelope from each slit's finite width (see M36).

**Thin-film interference.** Two reflections: one off the top of the film, one off the bottom. Their phase difference comes from (a) the extra path $2nt$ (at normal incidence) and (b) any $\pi$ phase shifts at hard reflections (low-$n$ to high-$n$). If there's exactly one hard reflection, the constructive / destructive conditions are swapped compared to the "no phase flip" case.

*Soap film in air* (air-soap-air): one hard reflection at the top surface. Constructive (bright): $2nt = (m + \tfrac{1}{2})\lambda_0$. Destructive (dark): $2nt = m\lambda_0$.

*Anti-reflection coating* on glass (air-coating-glass with $n_{\text{coat}} < n_{\text{glass}}$): two hard reflections, so the rule is as for zero — destructive: $2nt = (m + \tfrac{1}{2})\lambda_0$, which for the thinnest case is $t = \lambda_0/(4n)$.

**Michelson interferometer:** Splits a beam into two perpendicular arms. Moving one mirror by $\Delta d$ changes the path length of that arm by $2\Delta d$. Fringe count at a point: $\Delta m = 2\Delta d/\lambda$. Used historically for precision length metrology and in the Michelson-Morley experiment; modern descendant is LIGO.

### Common problem archetypes
- Given $d$, $\lambda$, $R$, find fringe spacing or position of $m$th bright fringe.
- Thin-film: minimum film thickness for a given wavelength, given the reflection context.
- Michelson: how far did the mirror move for $N$ fringes to pass.
- Two-source in air: what happens if one slit is covered / submerged in water / phase-shifted.

---

## Module 36 --- Diffraction

### Topics
- Fraunhofer vs. Fresnel diffraction (conceptual)
- Single-slit diffraction pattern
- Intensity distribution (sinc² envelope)
- Double-slit with finite slit widths
- Diffraction gratings
- Resolution (Rayleigh criterion), circular apertures
- X-ray diffraction and Bragg's law

### Theory

**Diffraction** is the bending and interference of waves at obstacles or apertures. Fraunhofer (far-field) diffraction is what we compute on the exam — slit and screen are far apart or lenses focus parallel rays.

**Single slit** of width $a$, wavelength $\lambda$: minima (dark fringes) occur at $a\sin\theta = m\lambda$ for $m = \pm 1, \pm 2, \dots$. **Note that $m = 0$ is a maximum, not a minimum** — the central maximum is twice as wide as the side maxima.

**Intensity pattern:** $I(\theta) = I_0[\sin(\beta/2)/(\beta/2)]^2$ with $\beta = 2\pi a\sin\theta/\lambda$. This is a sinc² — fast falloff, so most of the light is in the central maximum.

**Combined double-slit diffraction pattern:** You get the double-slit interference fringes *inside* the single-slit envelope:
$$I = I_0\cos^2\!\left(\frac{\pi d\sin\theta}{\lambda}\right)\left(\frac{\sin(\beta/2)}{\beta/2}\right)^2$$
Sometimes a double-slit bright fringe lands on a single-slit minimum — "missing order" — when $d/a$ is an integer times $m_{\text{interference}}/m_{\text{diffraction}}$.

**Diffraction grating:** Many slits with spacing $d$. Principal maxima where $d\sin\theta = m\lambda$. Compared to the double slit, a grating's maxima are *much sharper* because the more slits you have, the narrower each bright line. Chromatic resolving power $R = \lambda/\Delta\lambda = Nm$ where $N$ is the number of illuminated slits. Used in spectrometers.

**Circular aperture / Airy disk:** A circular aperture of diameter $D$ produces a central disk surrounded by faint rings, with the first dark ring at $\sin\theta = 1.22\lambda/D$. **Rayleigh criterion:** two point sources are barely resolved when the central maximum of one lies on the first minimum of the other, i.e., angular separation $\ge 1.22\lambda/D$. This sets fundamental limits on telescope and microscope resolution, the diffraction limit.

**X-ray diffraction / Bragg's law:** When X-rays of wavelength $\lambda$ hit a crystal with plane spacing $d$, constructive interference between waves reflected off adjacent planes occurs at $2d\sin\theta = m\lambda$. Note here $\theta$ is measured *from the plane*, not from the normal. Used to determine crystal structures.

### Common problem archetypes
- Given slit width and wavelength, find angular width of central max or position of $m$th minimum.
- Grating: given $d$ and $\lambda$, list all visible orders (need $|m\lambda/d| \le 1$).
- Rayleigh resolution: what's the smallest angular (or linear) separation resolvable by a telescope with aperture $D$?
- Bragg: find crystal plane spacing from X-ray scattering angles.

---

## Cross-module connections
- **EM waves → optics:** Malus's law (M33) connects the vector nature of light to the wave optics of M35/M36.
- **Interference vs. diffraction:** They're the same physical phenomenon (superposition). Interference is usually two sources, diffraction is usually one aperture — but they combine in the double-slit experiment.
- **Wave fundamentals from M15 reappear:** $v = \lambda f$, $k = 2\pi/\lambda$, superposition, standing-wave-like conditions for maxima. If you understand M15, you already understand most of M35/M36.
- **Snell's law and the reflection phase shift** in thin films both come from Maxwell's equations at an interface (covered conceptually in M33).

---

## What is "comprehensive" likely to mean on this exam?

The user has said midterm 3 is comprehensive with **emphasis on later topics** (Ch 33-36). Based on how comprehensive finals are typically structured in this course and the knowledge-question banks for midterms 1-2:

1. **Knowledge questions** (≈30 points) will probably include equations from *all* sections. Memorize the equation sheets for all three midterms. See [master_equations.tex](master_equations.tex).
2. **Problem questions** will emphasize Ch 33-36 but will likely include at least one problem from each of the earlier blocks:
    - One fluid/oscillation/wave problem (M12-M16)
    - One thermodynamics problem (M17-M20)
    - Several optics problems (M33-M36)
3. **Conceptual synthesis:** Be ready to explain why, e.g., $E/B = c$ in a wave; why entropy increases for irreversible processes; why a standing wave picks certain frequencies.

## Tips for exam prep
1. Re-work every question in [M33-36_Review.pdf](../m33,34,35,36/M33-36_Review.md) — this is likely the best single predictor of exam content.
2. Re-take midterm 1 and midterm 2 from the HTML banks (converted to .tex) cold.
3. Drill sign conventions for lenses and mirrors until they're reflexive.
4. Memorize the canonical short derivations: $c = 1/\sqrt{\mu_0\varepsilon_0}$ link; $E/B = c$; Malus; Snell → critical angle; fringe spacing $\lambda R/d$; Rayleigh $1.22\lambda/D$.
5. Draw every problem — ray diagrams for optics, phasor diagrams for interference, $pV$ diagrams for thermo.
