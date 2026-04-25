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

---

## Practice Final Coverage Analysis

Two practice finals are now available:

- **Fall 2024** ([test_finalexam_DRAFT_ps160_2024_fall.pdf](test_finalexam_DRAFT_ps160_2024_fall.pdf)) — 33 questions, best **230/271** points, default 10 pts per problem. **Q1-10 are knowledge formula-write** (1-3 pts each, 21 pts total covering optics formulas only — no fluids/thermo/sound knowledge questions). **Q11-33 are calculation problems**. Answers for Q11-33 in [test_final_ps160_2024_fall_answers.pdf](test_final_ps160_2024_fall_answers.pdf).
- **Spring 2024** ([test_finalexam_ps160_2024_spring.pdf](test_finalexam_ps160_2024_spring.pdf)) — 26 questions, best **250/300** points, all calculation. No knowledge section, no answer key (verify against agent-generated solutions).

### Notable structural facts

- The course's actual final is the *length* of midterm 1 + midterm 2 + new optics — much longer than a single midterm.
- "Best N out of M points" means you can skip the hardest problems; aim to *attempt* everything but bank on your strongest topics for the 230/250 bar.
- All sub-part problems (wave-function diagnostic, mirror/lens, Carnot) are worth **20 pts** — these single questions are higher leverage than a typical 10-pt calculation.

### Point distribution by topic (Fall 2024 calculation section, Q11-33)

| Topic                                    | Questions | Points |
| ---------------------------------------- | --------- | ------ |
| Fluids (Bernoulli, buoyancy)             | Q11, Q12  | 20     |
| SHM/Pendulum                             | Q13, Q14  | 20     |
| Wave function diagnostic                 | Q15       | 20     |
| Sound intensity (dB falloff)             | Q16       | 10     |
| Doppler                                  | Q17       | 10     |
| Pipes (standing waves)                   | Q18       | 10     |
| Thermal expansion                        | Q19       | 10     |
| Calorimetry / latent heat                | Q20       | 10     |
| Kinetic theory ($K_{tr}$, $v_{rms}$)     | Q21, Q23  | 20     |
| Ideal gas law (combined)                 | Q22       | 10     |
| Thermo processes (isothermal, adiabatic) | Q24, Q25  | 20     |
| Engines / efficiency                     | Q26       | 10     |
| Entropy (water freezing)                 | Q27       | 10     |
| Optics: reflection + Snell               | Q28, Q29  | 20     |
| Optics: mirrors (concave)                | Q30       | 20     |
| Optics: thin-film (bubble)               | Q31       | 10     |
| Optics: double-slit                      | Q32       | 10     |
| Optics: Rayleigh (telescope)             | Q33       | 10     |
| **Knowledge formulas (optics only)**     | Q1-10     | 21     |

**Optics' share of the calculation section is only ~70/250 points** — the rest is comprehensive midterm-1 and midterm-2 material. *Don't* let optics dominate prep at the expense of waves and thermo.

### Spring 2024 calculation section (no knowledge section, more thermo-heavy)

Adds: pressure column (Q1), hydraulic jack (Q2), spring energy (Q4), vibrating string $n=3$ (Q5), isobaric work (Q13), Carnot 20-pt (Q15), single-slit (Q23), Bragg (Q26), TIR mediated refraction (Q21), and a diverging-lens 20-pt (Q20). Q1-15 are all pre-optics, **so this exam is heavier on midterms 1+2 content than the Fall draft**.

### Repeated / template question patterns across BOTH exams (high-confidence: will appear)

These problems show up *verbatim or nearly verbatim* on both practice finals. Treat them as guaranteed:

1. **Wave-function diagnostic.** Same numerical wave $y(x,t) = 5\cos(3t + 0.5x - 2.1)$ in both, asking for $A$, $\omega$, $k$, phase, $f$, $T$, $\lambda$, $v$, transverse speed at origin. Fall adds part (j) "max transverse speed" (= $\omega A$). Worth 20 pts.
2. **Ideal gas combined law.** $T_1=220°\!\text{C}\to450°\!\text{C}$, $V$ halves, $p_1=89$ kPa — find $p_2$. Identical numbers in both (Fall Q22, Spring Q11). Answer: 261 kPa.
3. **Water freezing entropy.** 11 kg of water at 0°C → ice at 0°C, $L_f = 3.35\times10^5$ J/kg, find $\Delta S$ (kJ/K). Identical (Fall Q27, Spring Q16). Answer: $-13.5$ kJ/K. Watch the **sign** (heat leaves water → $\Delta S < 0$).
4. **Two plane mirrors at a corner.** Ray reflects off mirror 1 then mirror 2; find angle $\alpha$ between outgoing ray and second mirror's normal, given $\phi$ and $\theta$. Same geometry, different numbers (Fall: $\phi=70°,\theta=50°,\alpha=60°$; Spring: $\phi=60°,\theta=60°,\alpha=60°$). Use the angle sum in the triangle formed by the two mirrors and the ray.
5. **Bubble thin-film enhancement.** Spherical-shell bubble, $\lambda=471$ nm, $n=1.5$, find minimum thickness for **enhancement** (constructive in reflection). Identical (Fall Q31, Spring Q22). Single hard reflection (air→soap), so condition is $2nt = (m+\tfrac{1}{2})\lambda_0$; thinnest is $t = \lambda_0/(4n)$. Answer: 78.5 nm.
6. **Double-slit central-max width.** $\lambda=418$ nm, $d=0.26$ mm, $L=2.1$ m, find full width of central max. Identical (Fall Q32, Spring Q24). The "full width" is from the $m=-1$ to $m=+1$ minimum positions, $\Delta y = 2\lambda L/d$ (note: this uses the *minima* spacing for "full width", not fringe spacing). Answer: 3.376 mm. Verify which definition the answer key uses.
7. **Rayleigh / Mars telescope crater.** $D=4.5$ cm, $\lambda=557$ nm, $L=883$ km, find smallest resolvable feature. Identical (Fall Q33, Spring Q25). $d_{\min} = 1.22 \lambda L / D = 13.33$ m.
8. **Concave mirror, real object, $s>f$.** $s=18$ cm with either $f=8$ cm (Spring Q19) or $R=16$ cm so $f=8$ cm (Fall Q30 — same answer). Asks for $s'$, $m$, real/virtual, upright/inverted. Answer: $s'=14.4$ cm, $m=-0.8$, real, inverted.
9. **Doppler.** Both have a single Doppler problem with sound speed given. Fall: source approaching observer at rest. Spring: source at rest, observer moving away. Master both sign cases.
10. **Snell, air to denser medium.** Both have one of these (Fall Q29, Spring Q18 air-oil-water 2-step).

### Question types DEFINITELY appearing on the real final (high-confidence)

Based on appearing in both practice exams:

- Ideal gas combined law (single equation problem)
- Doppler effect with given $v_\text{sound}$
- Two-mirror corner geometry (figure provided)
- Concave mirror with real object inside/outside $f$ (4-part: $s'$, $m$, real/virtual, upright/inverted)
- Thin-film bubble enhancement → $\lambda_0/(4n)$
- Water freezing entropy with sign
- Wave function diagnostic (multi-part)
- Calorimetry / specific heat or latent heat
- Rayleigh resolution applied to telescope
- Double-slit fringe geometry
- Pendulum period on a non-Earth gravity

### Novel question types (not previously encountered in this user's prep materials)

These appeared for the first time on the practice finals and warrant extra drill:

1. **Ice slab supports woman (minimum-volume buoyancy).** Fall Q11. Ice has $\rho_{\text{ice}} = 0.92\rho_w$. The buoyancy from the *submerged* ice must support both the ice's weight and the 45-kg woman; in the limit case the slab is fully submerged but its top is exactly at the waterline. Setup: $\rho_w V g = \rho_{\text{ice}}V g + Mg \Rightarrow V = M/[(\rho_w - \rho_{\text{ice}})] = 45/(1000-920) = 0.5625\text{ m}^3$. The trick is realizing that "fully submerged but no water on top" is the *minimum* condition.
2. **Maximum transverse speed sub-part on the wave function.** Fall Q15(j). $v_{y,\max} = \omega A$ — same idea as a SHM particle's max speed, but applied to the *transverse* motion of a string element. Don't confuse with propagation speed $v = \omega/k$.
3. **Find $L_f$ given $Q$ and $m$ at the melting point.** Fall Q20. Inverse latent-heat problem: $L_f = Q/m$. Trivial but trains comfort with rearranging $Q = mL$ for any unknown.
4. **$v_{\text{rms}}$ change after a *constant-volume* heat absorption.** Fall Q23. Procedure: at constant V, $Q = nC_V\Delta T$, so find $\Delta T$. New $v_{\text{rms}}$ comes from $\tfrac{1}{2}mv_{\text{rms}}^2 = \tfrac{3}{2}kT$, but easier: $v_{\text{rms}} \propto \sqrt{T}$ so $v_{\text{rms,new}}/v_{\text{rms,old}} = \sqrt{T_\text{new}/T_\text{old}}$. Need the $T_\text{old}$ from the *given* $v_{\text{rms,old}}$ via the ratio. This couples kinetic theory and the first law — a common synthesis question.
5. **20-pt Carnot engine as a "give all four legs" question** (Spring Q15). Standard, but worth more points than a typical Q.

### What the practice exams *don't* test (caution)

- **No M33 (EM waves) problems** in either practice exam — neither Maxwell's-equation derivations nor radiation-pressure calculations nor Malus's law numerical problems appear. Knowledge questions on the Fall ask for Malus's law as a *formula*, but no calculation. **Don't assume EM waves are absent from the real exam** — they could appear; just realize the practice set's silence is a data point that they're *less* likely than optics.
- **No lensmaker's equation calculation**, no two-lens system, no microscope/telescope angular magnification — but the formula-write Q5 asks for the lensmaker's. Practice these *just enough* to get the formula-write points.
- **No grating problem** — only single-slit (Spring Q23), double-slit, and Bragg (Spring Q26). The knowledge question Q8 (Fall) asks for the grating constructive condition, though.
- **No interferometer / Michelson** in either practice.
- **No EM Brewster/critical-angle calculation** — but both formulas appear in knowledge Q3 (Fall).
