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

(a) Image is at $-21$ cm (same distance, opposite side).
(b) $m = +1$.
(c) **Virtual** (no real light converges there).
(d) **Upright**.

---

## Q2 — Concave mirror, $f=10.7$, $s=23$

$$\dfrac{1}{s'} = \dfrac{1}{f} - \dfrac{1}{s} = \dfrac{1}{10.7} - \dfrac{1}{23} = 0.09346 - 0.04348 = 0.04998$$
$$s' = \boxed{20.0\ \text{cm}}\quad\text{(real, inverted; }m = -s'/s = -0.870\text{)}$$

---

## Q3 — Convex mirror, $R=5.8$, $s=1.3$

Convex ⇒ $f = -R/2 = -2.9$ cm.
$$\dfrac{1}{s'} = -\dfrac{1}{2.9} - \dfrac{1}{1.3} = -0.3448 - 0.7692 = -1.1140$$
$$s' = -0.898\ \text{cm}\Rightarrow m = -s'/s = -(-0.898)/1.3 = \boxed{+0.690}$$

(Virtual, upright, reduced — typical convex-mirror behavior.)

---

## Q4 — Converging lens, $f=14$, $s=10$ (object inside focal length)

$$\dfrac{1}{s'} = \dfrac{1}{14} - \dfrac{1}{10} = -0.02857 \Rightarrow s' = \mathbf{-35\ \text{cm}}$$
$$m = -s'/s = +35/10 = \mathbf{+3.5}$$

Image is **upright** (positive $m$) and **virtual** (negative $s'$).

---

## Q5 — Diverging lens, $f=-9$, $s=16$

$$\dfrac{1}{s'} = \dfrac{1}{-9} - \dfrac{1}{16} = -0.1111 - 0.0625 = -0.1736 \Rightarrow s' = \mathbf{-5.76\ \text{cm}}$$
$$m = -s'/s = +5.76/16 = \mathbf{+0.36}$$

**Virtual** and **upright**.

---

## Q6 — Lensmaker, then image position

$n=2$, $R_1=8$, $R_2=-11$.
$$\dfrac{1}{f} = (2-1)\!\left(\dfrac{1}{8} - \dfrac{1}{-11}\right) = 0.125 + 0.0909 = 0.2159 \Rightarrow f = 4.63\ \text{cm}$$
$$\dfrac{1}{s'} = 0.2159 - \dfrac{1}{23} = 0.17242 \Rightarrow s' = \boxed{5.80\ \text{cm}}$$

(Real image, since $s'>0$.)

---

## Q7 — Object inside sphere, virtual image at 14 cm

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

Far point at 43.3 cm → need to image objects at infinity to that point. Use diverging lens with $f$ in m, image at far point ($s' = -0.433$ m, $s\to\infty$): $1/f = 1/s' = -1/0.433$.
$$P = 1/f = -2.31\ \text{D} \Rightarrow \boxed{-2.31\ \text{D}}$$

---

## Q10 — Magnifier focal length

Standard simple-magnifier (image at infinity, relaxed eye) angular magnification: $M = 25\ \text{cm}/f$.
$$f = 25/2.3 = \boxed{10.87\ \text{cm}}$$

(If the textbook uses $M = 1 + 25/f$ — image at the near point — then $f = 25/(M-1) = 25/1.3 = 19.23$ cm. Use whichever form your class uses.)

---

## Q11 — Corrective optics

- Near-sightedness: **diverging** lens; image is **virtual**. ✓
- Far-sightedness: **converging** lens; image is **virtual** (forms farther away than the object so the eye can focus on it).

---

## Q12 — Spherical mirror image type by object distance

- Object farther than $f$ (concave mirror): **real**, **inverted**.
- Object closer than $f$: **virtual**, **upright** (the magnifying mirror).

---

**Note:** Q8 numerical position depends on origin of $x$-axis in the figure. Q11 wording ("real or virtual" for hyperopia correction) is sometimes ambiguous; the corrective lens itself produces a virtual image of nearby print at a comfortable distance.
