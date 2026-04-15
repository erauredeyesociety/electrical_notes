# Chapter 34 — Geometric Optics (Lecture Outline)

This chapter covers image formation by mirrors (plane/spherical), refraction at curved surfaces, thin lenses, the lensmaker's equation, and optical instruments (eye, magnifier, microscope, telescope).

## Learning Outcomes

- How plane mirrors form images; why concave/convex mirrors differ.
- How images form via curved refracting interfaces.
- What aspects of a lens determine the image type.
- Vision defects and corrections.
- How microscopes and telescopes work.

## Reflection at a Plane Surface

Light rays from object point $P$ reflected off a plane mirror appear to come from image point $P'$ **behind** the mirror. The image is **virtual** — no light actually passes through $P'$.

### Sign Rules (Plane Mirror)

- **Object distance** $s > 0$ when object is on the same side as incoming light.
- **Image distance** $s' < 0$ when image is **not** on the same side as outgoing light (virtual).
- For a plane mirror: $s = -s'$ (image is same distance behind the mirror as object is in front).

### Characteristics of Plane Mirror Images

- Virtual
- Erect (upright)
- Same size as object → lateral magnification $m = +1$
- **Reversed** (right hand appears as left hand)

### Lateral Magnification

$$m = \frac{y'}{y}$$
where $y'$ = image height, $y$ = object height. Positive $m$ = upright; negative $m$ = inverted.

## Spherical Mirrors

A spherical mirror with radius of curvature $R$ forms an image of a point object $P$ at image point $P'$. The paraxial (small-angle) object-image relation:

$$\frac{1}{s} + \frac{1}{s'} = \frac{2}{R}$$

### Sign Conventions for Spherical Mirrors

- $s > 0$: object on same side as incident light.
- $s' > 0$: image on same side as reflected (outgoing) light.
- $R > 0$: center of curvature $C$ on same side as reflected (outgoing) light.
  - **Concave** mirror: $R > 0$ (C in front of mirror).
  - **Convex** mirror: $R < 0$ (C behind mirror).

### Focal Point and Focal Length

For parallel incoming rays (object at infinity), the reflected rays converge to the **focal point** $F$. The focal length is:
$$f = \frac{R}{2}$$

From this, the mirror equation becomes:
$$\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}$$

For a **convex** mirror: parallel rays diverge as if coming from a **virtual focal point** behind the mirror; $f < 0$.

### Magnification for Spherical Mirrors

$$m = -\frac{s'}{s}$$

### Graphical Method — Principal Rays (Spherical Mirror)

1. Parallel ray → reflects through focal point $F$.
2. Ray through $F$ → reflects parallel to axis.
3. Ray through $C$ (center of curvature) → reflects back on itself.
4. Ray to vertex $V$ → reflects symmetrically about optic axis.

### Key Facts — Spherical Mirrors

- **Concave, object beyond $F$:** real, inverted image.
- **Concave, object inside $F$:** virtual, upright, enlarged image.
- **Convex:** always virtual, upright, reduced image.

## Refraction at a Spherical Surface

For a single spherical refracting surface separating media $n_a$ and $n_b$:

$$\frac{n_a}{s} + \frac{n_b}{s'} = \frac{n_b - n_a}{R}$$

### Apparent Depth (Plane Refracting Surface)

For flat interface, $R \to \infty$:
$$\frac{n_a}{s} + \frac{n_b}{s'} = 0 \Rightarrow s' = -\frac{n_b}{n_a}s$$

Objects in water appear closer than they really are (apparent depth = real depth × $n_b/n_a$).

## Thin Lenses

A **thin lens** has two refracting surfaces close together. Object-image relationship:

$$\frac{1}{s} + \frac{1}{s'} = \frac{1}{f}$$

### Magnification (Thin Lens)

$$m = -\frac{s'}{s}$$

### Converging vs. Diverging Lenses

- **Converging lens** (thicker at center, e.g., biconvex): $f > 0$. Parallel rays converge to the second focal point $F_2$.
- **Diverging lens** (thicker at edges, e.g., biconcave): $f < 0$. Parallel rays diverge as if from $F_2$ on the incoming side.

Any lens thicker at center than edges is converging; any lens thicker at edges is diverging.

### Lensmaker's Equation

For a thin lens in air with refractive index $n$ and surface radii $R_1$ (front) and $R_2$ (back):

$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

Sign convention: $R > 0$ if center of curvature is on the same side as outgoing light.

### Principal Rays for Lenses

- Ray 1: parallel to axis → refracts through $F_2$ (far focal point).
- Ray 2: through center of lens → passes undeflected.
- Ray 3: through $F_1$ (near focal point) → emerges parallel to axis.

For diverging lens, parallel ray appears to come from $F_2$; ray aimed at $F_1$ emerges parallel.

## Cameras

Camera lens forms a real, inverted, usually reduced image on sensor/film. Focus adjusted by moving lens.

### f-number

$$f\text{-number} = \frac{f}{D}$$
where $D$ is aperture diameter. Larger f-number = smaller aperture. Changing $D$ by $\sqrt{2}$ changes intensity by 2.

## The Eye

Structure: cornea, pupil (iris), crystalline lens, retina. Ciliary muscle adjusts lens shape (accommodation) to focus at different distances.

### Vision Defects

- **Myopia (nearsightedness):** eyeball too long → distant objects focus in front of retina. Corrected with **diverging lens** (negative $f$).
- **Hyperopia (farsightedness):** cornea too flat → near objects focus behind retina. Corrected with **converging lens** (positive $f$).
- **Presbyopia:** age-related loss of accommodation.

### Corrective Power (diopters)

$$P = \frac{1}{f \text{ (in meters)}}$$

Positive diopters: converging (farsighted correction); negative diopters: diverging (nearsighted correction).

## Angular Size and Magnification

**Angular size** is the angle subtended at the eye. Maximum useful angular size is at the near point (~25 cm).

### Simple Magnifier

$$M = \frac{25 \text{ cm}}{f}$$
where $f$ is in cm. The object is placed at the focal point, producing an image at infinity for relaxed viewing.

## Compound Microscope

Objective lens (short $f_1$) forms a real, inverted, magnified image just inside the focal point of the eyepiece $F_2$. Eyepiece acts as a magnifier, producing a further-enlarged virtual image (still inverted).

## Telescopes

### Refracting (Astronomical) Telescope

Objective (large $f_1$) forms real, inverted image at its focal point, which coincides with eyepiece's near focal point. Eyepiece magnifies to virtual image at infinity.

### Reflecting Telescope

Uses a large concave objective **mirror** (e.g., Gemini North uses 8-m mirror). Avoids chromatic aberration and allows larger apertures.

## Sample In-Class Problems

### Q1 — Half-size Mirror

Woman 1.9 m tall with eyes at 1.76 m. Find highest point above floor the bottom of a mirror can be so she can still see her feet.

The mirror must extend down to half the height from eyes to floor:
$$h = 1.76/2 = 0.88 \text{ m}$$

### Q2 — Concave Mirror, $f = 14$ cm, $s = 8$ cm

$$s' = \frac{sf}{s-f} = \frac{8\times 14}{8-14} = -18.67 \text{ cm}$$

Virtual ($s' < 0$), upright, enlarged. $m = -s'/s = +2.33$.

### Q3 — Convex Mirror, $f = -12$ cm, $s = 6$ cm

$$s' = \frac{6\times(-12)}{6+12} = -4 \text{ cm}$$
Virtual, upright, reduced. $m = +2/3$.

### Q4 — Converging Lens, $m = -4.5$, $f = 7$ cm

$m = -s'/s \Rightarrow s' = 4.5 s$. Combined with $1/s + 1/s' = 1/f$:
$$\frac{1}{s} + \frac{1}{4.5 s} = \frac{1}{7} \Rightarrow s \approx 8.56 \text{ cm}, \quad s' \approx 38.5 \text{ cm}$$

### Q5 — Diverging Lens, $f = -9$ cm, $s = 6$ cm

$$s' = \frac{6\times(-9)}{6+9} = -3.6 \text{ cm}$$
Virtual, upright, reduced. $m = +0.6$.

### Q6 — Lensmaker's Equation

Lens $n = 2.1$, $R_1 = 29.8$ cm, $R_2 = 13.4$ cm (biconcave, so $R_1 < 0$, $R_2 > 0$).
$$\frac{1}{f} = (2.1-1)\left(\frac{1}{-29.8} - \frac{1}{13.4}\right) \Rightarrow f < 0$$

### Q7 — Point Refraction on Crystal Ball

Coin 15 cm inside crystal ball, $n = 1.9$, $R = 33$ cm (diverging surface from inside, $R < 0$).
$$\frac{1.9}{15} + \frac{1}{s'} = \frac{1 - 1.9}{-33}$$

### Q8 — Two-Lens System

Tiny tree 21 cm from converging lens ($f_1 = 9$ cm), then diverging lens ($f_2 = -17$ cm) at $L = 12$ cm. Find final image x-position.

First lens: $s_1' = f_1 s_1/(s_1 - f_1) = 9\cdot 21 / 12 = 15.75$ cm.
Second lens: $s_2 = L - s_1' = -3.75$ cm.
$s_2' = f_2 s_2/(s_2 - f_2) = (-17)(-3.75)/(-3.75 + 17) \approx 4.81$ cm.

### Q9 — Reading Glasses

Near point 76 cm, read comfortably at 22.7 cm:
$$P = \frac{1}{0.227} + \frac{1}{-0.76} \approx 4.41 - 1.32 = 3.09 \text{ diopters}$$

### Q10 — Simple Magnifier, $f = 8.4$ cm

$M = 25/8.4 \approx 2.98$

## Key Equations Summary — Chapter 34

- Plane mirror: $s' = -s$, $m = +1$
- Lateral magnification: $m = y'/y = -s'/s$
- Spherical mirror: $1/s + 1/s' = 2/R = 1/f$; $f = R/2$
- Refraction at spherical surface: $n_a/s + n_b/s' = (n_b - n_a)/R$
- Plane refracting surface: $s' = -(n_b/n_a)s$
- Thin lens equation: $1/s + 1/s' = 1/f$
- Lensmaker's equation: $1/f = (n-1)(1/R_1 - 1/R_2)$
- f-number: $f/D$
- Power in diopters: $P = 1/f$ (in meters)
- Simple magnifier: $M = (25 \text{ cm})/f$

## Sign Convention Summary

| Quantity | Positive when |
|----------|---------------|
| $s$ (object) | Object on same side as incoming light |
| $s'$ (image) | Image on same side as outgoing light (real) |
| $R$ | C on same side as outgoing light |
| $f$ | Converging element |
| $m$ | Upright image |
