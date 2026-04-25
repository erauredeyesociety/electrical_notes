# ME34: Mirrors & Lenses — Walkthrough

**Module:** M34 — see [m33,34,35,36/](../../m33,34,35,36/)

> ⚠️ **Source key not provided.** Q1's expected answers are reproduced from the .tex (which inlined them); everything else is independently computed. Q8 depends on a two-lens figure; my coordinate convention is stated and may need to be adjusted to match the figure's origin.

**Sign convention (lensmaker / Gauss form):**
- $\dfrac{1}{s} + \dfrac{1}{s'} = \dfrac{1}{f}$ for mirrors *and* thin lenses
- $s > 0$: object on the side light comes from (real object)
- $s' > 0$: image on the side light is going to (real image)
- $f > 0$: converging lens / concave mirror; $f < 0$: diverging lens / convex mirror
- Magnification: $m = -s'/s$. $|m|>1$ enlarged, $m>0$ upright, $m<0$ inverted
- Refraction at a spherical surface: $\dfrac{n_1}{s} + \dfrac{n_2}{s'} = \dfrac{n_2-n_1}{R}$
- Lensmaker's equation: $\dfrac{1}{f} = (n-1)\!\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$

---

## Q1 — Flat mirror, object at 21 cm

**Setup.** A plane (flat) mirror — the simplest case. An object sits 21 cm in front of it; the image always forms the same distance *behind* the mirror, same size, upright, and virtual (no real light converges there — your brain just traces the reflected rays back behind the glass). The convention here flips the sign so "behind the mirror" reads as negative.

(a) Image is at $-21$ cm (same distance, opposite side).
(b) $m = +1$.
(c) **Virtual** (no real light converges there).
(d) **Upright**.

---

## Q2 — Concave mirror, $f=10.7$, $s=23$

**Setup.** A concave (converging) spherical mirror has focal length $10.7$ cm. The object sits at $23$ cm — *outside* the focal point (since $s>f$), so we expect a real, inverted image somewhere on the same side as the object. Plug into the mirror equation $1/s + 1/s' = 1/f$ and solve for $s'$.

$$\dfrac{1}{s'} = \dfrac{1}{f} - \dfrac{1}{s} = \dfrac{1}{10.7} - \dfrac{1}{23} = 0.09346 - 0.04348 = 0.04998$$
$$s' = \boxed{20.0\ \text{cm}}\quad\text{(real, inverted; }m = -s'/s = -0.870\text{)}$$

---

## Q3 — Convex mirror, $R=5.8$, $s=1.3$

**Setup.** A convex (diverging) spherical mirror with radius of curvature $5.8$ cm — so $f = -R/2 = -2.9$ cm (negative for diverging). A small eggplant sits very close, $s=1.3$ cm. Convex mirrors *always* form virtual, upright, reduced images regardless of object distance, so we expect $m$ to be positive and less than 1. We want lateral magnification specifically.

Convex ⇒ $f = -R/2 = -2.9$ cm.
$$\dfrac{1}{s'} = -\dfrac{1}{2.9} - \dfrac{1}{1.3} = -0.3448 - 0.7692 = -1.1140$$
$$s' = -0.898\ \text{cm}\Rightarrow m = -s'/s = -(-0.898)/1.3 = \boxed{+0.690}$$

(Virtual, upright, reduced — typical convex-mirror behavior.)

---

## Q4 — Converging lens, $f=14$, $s=10$ (object inside focal length)

**Setup.** A converging lens with $f=14$ cm, but the object is at $s=10$ cm — *inside* the focal point. When that happens with a converging lens, the lens can't bring the rays back together on the far side; instead, traced backward, they appear to diverge from a magnified upright image on the *same* side as the object. That's a virtual image, with $s'<0$ and $m>0$. (This is exactly how a magnifying glass works.)

$$\dfrac{1}{s'} = \dfrac{1}{14} - \dfrac{1}{10} = -0.02857 \Rightarrow s' = \mathbf{-35\ \text{cm}}$$
$$m = -s'/s = +35/10 = \mathbf{+3.5}$$

Image is **upright** (positive $m$) and **virtual** (negative $s'$).

---

## Q5 — Diverging lens, $f=-9$, $s=16$

**Setup.** A diverging (concave) thin lens has $f=-9$ cm; object at $s=16$ cm. Diverging lenses *always* produce virtual, upright, reduced images for any real object — the math should give $s'<0$ and $0<m<1$.

$$\dfrac{1}{s'} = \dfrac{1}{-9} - \dfrac{1}{16} = -0.1111 - 0.0625 = -0.1736 \Rightarrow s' = \mathbf{-5.76\ \text{cm}}$$
$$m = -s'/s = +5.76/16 = \mathbf{+0.36}$$

**Virtual** and **upright**.

---

## Q6 — Lensmaker, then image position

**Setup.** A thin lens has unusually high index $n=2$, with surface radii $R_1 = 8$ cm (first surface, convex toward incoming light) and $R_2 = -11$ cm (second surface, also convex outward — the negative sign is the sign convention). First use the lensmaker's equation to compute $f$, then the thin-lens equation with $s=23$ cm to get the image position.

$n=2$, $R_1=8$, $R_2=-11$.
$$\dfrac{1}{f} = (2-1)\!\left(\dfrac{1}{8} - \dfrac{1}{-11}\right) = 0.125 + 0.0909 = 0.2159 \Rightarrow f = 4.63\ \text{cm}$$
$$\dfrac{1}{s'} = 0.2159 - \dfrac{1}{23} = 0.17242 \Rightarrow s' = \boxed{5.80\ \text{cm}}$$

(Real image, since $s'>0$.)

---

## Q7 — Object inside sphere, virtual image at 14 cm

**Setup.** A pebble is embedded inside a transparent sphere of $n=2$ and radius $33$ cm. Light from the pebble has to refract once at the curved sphere-air boundary on its way to your eye. Because $n_{\text{inside}} > n_{\text{outside}}$, the surface acts like a diverging element from the outside view, and the image you see appears displaced *inside* the sphere (virtual). Use the single-surface refraction equation $\frac{n_1}{s} + \frac{n_2}{s'} = \frac{n_2-n_1}{R}$, paying very close attention to signs: object real and inside ($s>0$), image inside the same side ($s'<0$, virtual), and the center of curvature on the *incoming* side from the standpoint of the light heading outward ($R<0$).

Light travels from object (inside sphere, $n_1=2$) outward across the curved boundary into air ($n_2=1$).

Sign conventions (object on incoming side; image and center of curvature judged from outgoing side):
- $s > 0$ (real object inside sphere)
- Image *appears inside sphere* (same side as object) ⇒ virtual ⇒ $s' = -14$
- Center of curvature is on the incoming side (the center of the sphere) ⇒ $R = -33$

$$\dfrac{n_1}{s} + \dfrac{n_2}{s'} = \dfrac{n_2 - n_1}{R}$$
$$\dfrac{2}{s} + \dfrac{1}{-14} = \dfrac{1-2}{-33} \Rightarrow \dfrac{2}{s} = \dfrac{1}{33} + \dfrac{1}{14} = \dfrac{47}{462}$$
$$s = \dfrac{2(462)}{47} = \boxed{19.66\ \text{cm}}$$

---

## Q8 — Two-lens system (depends on figure origin)

**Setup.** A tiny tree sits 21 cm in front of a converging lens ($f_1=+8$ cm), with a diverging lens ($f_2=-17$ cm) placed $L=10$ cm farther down the optical axis. We find the final image by treating the two lenses *sequentially*: first compute where lens 1 would form its image if lens 2 were absent, then use that image's location relative to lens 2 as the object for lens 2 (with the correct sign — if lens 1's image would form past lens 2, it acts as a *virtual object* with $s_2<0$).

$f_1 = +8$, $f_2 = -17$, lens separation $L=10$, object at 21 cm in front of lens 1.

**Lens 1** (image from lens 1):
$$\dfrac{1}{s_1'} = \dfrac{1}{8} - \dfrac{1}{21} = 0.07738 \Rightarrow s_1' = +12.92\ \text{cm}$$
(Real image, would form 12.92 cm right of lens 1, but lens 2 is only 10 cm away.)

**Lens 2:** object for lens 2 is the would-be image of lens 1, at $12.92 - 10 = 2.92$ cm *behind* lens 2 (the image hasn't formed yet, so it's a *virtual* object for lens 2 ⇒ $s_2 = -2.92$).
$$\dfrac{1}{s_2'} = \dfrac{1}{-17} - \dfrac{1}{-2.92} = -0.0588 + 0.3425 = 0.2837$$
$$s_2' = +3.53\ \text{cm}\ \text{(right of lens 2)}$$

Final image position **3.53 cm to the right of the diverging lens**. With origin at the object: $x_{\text{img}} = 21 + 10 + 3.53 = \boxed{34.53\ \text{cm}}$ (with origin at the object). If the figure puts $x=0$ at lens 1: $x_{\text{img}} = 13.53$ cm.

---

## Q9 — Corrective lens for myopia

**Setup.** A near-sighted person can focus at most out to her "far point" of 43.3 cm — anything past that is blurry. A corrective lens needs to take light from infinity and form a virtual image at her far point, where her eye can naturally focus. Plug $s\to\infty$ and $s'=-0.433$ m (virtual, in front of the lens) into the thin-lens equation; lens power is $P=1/f$ in diopters when $f$ is in meters. The answer should be negative (diverging lens) since myopia is corrected with a diverging lens.

Far point at 43.3 cm → need to image objects at infinity to that point. Use diverging lens with $f$ in m, image at far point ($s' = -0.433$ m, $s\to\infty$): $1/f = 1/s' = -1/0.433$.
$$P = 1/f = -2.31\ \text{D} \Rightarrow \boxed{-2.31\ \text{D}}$$

---

## Q10 — Magnifier focal length

**Setup.** Designing a simple magnifying glass with target angular magnification $M=2.3$. The standard "relaxed eye" formula puts the image at infinity, giving $M = 25\ \text{cm}/f$ where 25 cm is the conventional near point distance. (An alternate convention puts the image at the near point, giving $M = 1 + 25/f$ — slightly larger magnification for the same lens; check which form your textbook uses.)

Standard simple-magnifier (image at infinity, relaxed eye) angular magnification: $M = 25\ \text{cm}/f$.
$$f = 25/2.3 = \boxed{10.87\ \text{cm}}$$

(If the textbook uses $M = 1 + 25/f$ — image at the near point — then $f = 25/(M-1) = 25/1.3 = 19.23$ cm. Use whichever form your class uses.)

---

## Q11 — Corrective optics

Near-sightedness (myopia) means the eye focuses *in front of* the retina; a diverging lens spreads the rays so the eye's lens then refocuses them onto the retina. The diverging lens forms a virtual image of distant objects at the eye's far point. Far-sightedness (hyperopia) is the opposite: the eye can't focus close enough, so a converging lens is used to form a virtual image of nearby print farther away — at the eye's near point — where the eye can focus.

- Near-sightedness: **diverging** lens; image is **virtual**. ✓
- Far-sightedness: **converging** lens; image is **virtual** (forms farther away than the object so the eye can focus on it).

---

## Q12 — Spherical mirror image type by object distance

For a concave (converging) spherical mirror, the focal point divides the two regimes. With the object beyond $f$ the rays converge on the far side of the mirror and form a real, inverted image (this is how a shaving mirror at arm's length works only at certain distances). With the object inside $f$, the rays diverge after reflection — traced backward they form a virtual, upright, magnified image (the magnifying-shave-mirror regime up close).

- Object farther than $f$ (concave mirror): **real**, **inverted**.
- Object closer than $f$: **virtual**, **upright** (the magnifying mirror).

---

**Note:** Q8 numerical position depends on origin of $x$-axis in the figure. Q11 wording ("real or virtual" for hyperopia correction) is sometimes ambiguous; the corrective lens itself produces a virtual image of nearby print at a comfortable distance.
