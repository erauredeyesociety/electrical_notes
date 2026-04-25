# ME33: Geometric Optics — Walkthrough

**Module:** M33 — see [m33,34,35,36/](../../m33,34,35,36/)

> ⚠️ **Source key not provided in the .tex.** Solutions below are independently computed; double-check against any official key when one becomes available. Q1 depends on a figure not viewed here, so a method is given but the numeric answer is conditional.

**Core formulas**
- Reflection: angle of incidence = angle of reflection (both measured from the normal).
- Snell's law: $n_1\sin\theta_1 = n_2\sin\theta_2$
- Speed in medium: $v = c/n$. Wavelength in medium: $\lambda_{\text{med}} = \lambda_{\text{vac}}/n$ (frequency is unchanged).
- Critical angle (TIR, going from $n_1$ to $n_2 < n_1$): $\sin\theta_c = n_2/n_1$.
- Brewster's angle: $\tan\theta_B = n_2/n_1$ (light reflected from interface is fully polarized).
- Malus's law (linear polarizers): $I = I_0\cos^2\theta$.

---

## Q1 — Two plane mirrors at angle (image-dependent)

**Setup.** Two flat mirrors meet at some angle and a light ray bounces off both. The figure labels three angles: $\phi=62°$ between the mirrors (or between a mirror and the incoming ray, depending on the diagram), $\theta=28°$ for the incident ray, and $\alpha$ is the angle to find on the second reflection. Without the figure the labeling is ambiguous, but the geometry is always solved by the same trick: close the ray + mirror segments into a triangle and use angle-sum = 180°.

Without the figure I can't pin down the geometry uniquely. The standard tools:

For a ray reflecting off two mirrors meeting at angle $\phi$, the *total deviation* is
$$\delta = 360° - 2\phi$$
(if both reflections occur). For a ray that strikes the first mirror at angle $\theta$ from its normal, the angle to the second mirror's normal can usually be found via the triangle made by the two mirrors and the connecting ray segment: angle in that triangle $= \phi - (90°-\theta) - (90°-\alpha)$ etc. — depends on which angle the figure labels "α."

**Method:** identify the closed triangle formed by ray segments and mirrors; sum of interior angles $= 180°$ relates $\alpha$, $\phi$, $\theta$ directly.

A common version of this figure gives $\alpha = \phi - \theta = 62° - 28° = \boxed{34°}$ — *verify against the figure.*

---

## Q2 — Speed of light in a medium

**Setup.** A material with index of refraction $n=1.91$ slows light relative to vacuum. The index *is* the slow-down factor: by definition $n = c/v$, so the speed in the medium is just $c$ divided by $n$.

$n=1.91$.
$$v = c/n = (3.00\times 10^8)/1.91 = 1.571\times 10^8\ \text{m/s} \Rightarrow \boxed{1.57\times 10^8\ \text{m/s}}$$

---

## Q3 — Wavelength in a medium

**Setup.** Light of fixed frequency $f = 6.23\times 10^{14}$ Hz crosses from air into a medium with $n=1.21$. Frequency is set by the source and does *not* change at a boundary; the speed drops to $c/n$, so the wavelength must shrink by the same factor $n$. Compute the vacuum wavelength first ($\lambda_{\text{vac}} = c/f$), then divide by $n$.

$f = 6.23\times 10^{14}$ Hz, $n=1.21$.
$$\lambda_{\text{vac}} = c/f = 4.815\times 10^{-7}\ \text{m} = 481.5\ \text{nm}$$
$$\lambda_{\text{med}} = \lambda_{\text{vac}}/n = 481.5/1.21 = \boxed{397.9\ \text{nm}}$$

(Frequency does not change crossing into a medium; wavelength shrinks by $n$.)

---

## Q4 — Find angle of incidence

**Setup.** A ray traveling in air ($n_1=1$) hits a fluid surface ($n_2=1.61$) at some unknown angle and refracts to $\theta_2=21°$ inside the fluid. We want the original angle of incidence in air. Snell's law $n_1\sin\theta_1 = n_2\sin\theta_2$ links the two; since the ray is going from less dense to more dense, the angle in air is *larger* than the angle in the fluid (the ray bends toward the normal as it enters).

$n_1=1$, $n_2=1.61$, $\theta_2 = 21°$.
$$\sin\theta_1 = n_2\sin\theta_2 = 1.61\sin(21°) = 1.61(0.3584) = 0.5770$$
$$\theta_1 = \arcsin(0.5770) = \boxed{35.24°}$$

---

## Q5 — Air → oil → water, find angle in water

**Setup.** Light hits a layer of oil floating on water at an angle $\theta=32°$ from the normal (in the top medium) and we want the final angle $\phi$ of the refracted ray inside the water. Useful fact about parallel slabs: applying Snell's law at each interface chains the indices, and the *intermediate* layer (the oil) drops out — only the first and last $n$ matter for the final ray direction. So this reduces to one Snell's-law step from air directly to water.

For a stack of parallel layers, Snell's law chains: $\sin$ in any layer = $n_{\text{air}}\sin\theta_{\text{air}}/n_{\text{layer}}$. The middle layer (oil) drops out for the *direction* in water.

If $\theta = 32°$ is the angle of incidence in air:
$$\sin\phi = \sin(32°)/n_{\text{water}} = 0.5299/1.33 = 0.3984$$
$$\phi = \boxed{23.49°}$$

(If $\theta$ is the angle inside the oil instead, use $n_{\text{oil}}\sin\theta = n_{\text{water}}\sin\phi$ — same final water angle to within Snell's chain.)

---

## Q6 — Dispersion through BK7 glass slab

**Setup.** White light hits a 0.42-m-thick block of BK7 glass at $48°$ from the normal. Different wavelengths see slightly different indices of refraction (dispersion), so they bend by slightly different amounts on entry and follow slightly different paths through the glass. We want the *spatial separation* at the exit face between two of those wavelengths (entry #2 at 475 nm vs #4 at 625 nm). For each beam: refract on entry, travel a horizontal distance $d\tan\theta_{\text{inside}}$ before hitting the bottom, then take the difference.

Incident in air at $48°$; $n_2 = 1.523$ (475 nm), $n_4 = 1.515$ (625 nm); slab thickness $d=0.42$ m.

Refracted angles inside the glass:
$$\theta_2 = \arcsin(\sin 48°/1.523) = \arcsin(0.4880) = 29.20°$$
$$\theta_4 = \arcsin(\sin 48°/1.515) = \arcsin(0.4905) = 29.37°$$

Horizontal offsets at exit face (each $d\tan\theta$):
$$x_2 = 0.42\tan(29.20°) = 0.2347\ \text{m}$$
$$x_4 = 0.42\tan(29.37°) = 0.2364\ \text{m}$$
$$\Delta x = x_4 - x_2 = 1.74\times 10^{-3}\ \text{m} = \boxed{1.74\ \text{mm}}$$

(Longer-wavelength beam — smaller $n$ — bends less, so it lands farther from the entry-normal projection.)

---

## Q7 — Critical angle, find $n_1$

**Setup.** A ray inside material 1 (unknown $n_1$) hits a boundary with material 2 ($n_2=1.5$). The figure shows the geometry of total internal reflection: the refracted ray skims along the interface at exactly the critical angle $\theta_c=49°$. At the critical angle, $\sin\theta_c = n_2/n_1$, which we invert to solve for $n_1$. Because TIR requires going from denser to less dense, $n_1>n_2$ — the answer should exceed 1.5.

If the figure depicts $\theta = 49°$ as the critical angle for TIR at the boundary with $n_2 = 1.5$:
$$\sin\theta_c = n_2/n_1 \Rightarrow n_1 = n_2/\sin\theta_c = 1.5/\sin(49°) = 1.5/0.7547 = \boxed{1.988}$$

---

## Q8 — Refraction angle from a known critical angle

**Setup.** We're told the critical angle at a liquid-air interface is $42.3°$ — meaning a ray traveling *inside the liquid* would TIR at that incidence. That number lets us back out the liquid's index: $n_{\text{liquid}} = 1/\sin(42.3°)$ since air has $n=1$. Then we run a *separate* problem: a ray comes from the air side at $34°$ and refracts into the liquid; find that refraction angle. Light entering a denser medium bends toward the normal, so the answer should be less than $34°$.

Critical angle 42.3° at the liquid-air interface ⇒ $n_{\text{liquid}} = 1/\sin(42.3°) = 1/0.6730 = 1.486$.

Ray in air enters liquid at $\theta_1 = 34°$:
$$\sin\theta_2 = \sin(34°)/n_{\text{liquid}} = 0.5592/1.486 = 0.3763$$
$$\theta_2 = \boxed{22.10°}$$

---

## Q9 — Two polarizers (Malus chain)

**Setup.** Polarized light hits a polarizer whose axis is rotated $37°$ from the light's polarization, then passes through a second polarizer rotated a further $49°$ relative to the *first* polarizer. After each filter, intensity is multiplied by $\cos^2$ of the angle between the incoming polarization and that filter's axis (Malus's law). Important: after the first filter the light's polarization is along the first filter's axis, so the relevant angle for the second filter is the $49°$ between the two axes — not 49° from the original polarization.

First filter at $37°$ from input polarization → $I_1 = I_0\cos^2(37°) = I_0(0.7986)^2 = 0.6378\,I_0$.
Second filter at $49°$ relative to the first → $I_2 = I_1\cos^2(49°) = I_1(0.6561)^2 = 0.4305\,I_1$.
$$I_2/I_0 = 0.6378\cdot 0.4305 = \boxed{0.2746}$$

---

## Q10 — Brewster's angle for glass in oil

**Setup.** Glass with $n_{\text{glass}}=1.6$ is immersed in oil ($n_{\text{oil}}=1.465$, medium 3 from the table) and we want the angle at which reflected light is completely polarized — Brewster's angle. The formula $\tan\theta_B = n_2/n_1$ uses $n_1$ for the medium the light is *coming from* (oil) and $n_2$ for the medium being entered (glass). Because the index contrast is small (1.6 vs 1.465), $\theta_B$ ends up close to 45°.

$n_{\text{glass}} = 1.6$, $n_{\text{oil}} = 1.465$. With incident in oil, reflected from glass:
$$\theta_B = \arctan(n_{\text{glass}}/n_{\text{oil}}) = \arctan(1.6/1.465) = \arctan(1.0922) = \boxed{47.53°}$$

---

## Q11 — Refraction qualitative

A bigger index contrast at a boundary forces a bigger change in direction (Snell's law: the ratio of sines equals the inverse ratio of indices, so a larger ratio = larger angle change). Index of refraction depends on *wavelength* — the phenomenon called dispersion. For normal materials $n$ rises as wavelength shrinks, so blue/violet light bends more than red.

- Bigger $\Delta n$ → more bending → **larger** ✓
- $n$ depends on **wavelength** → called **dispersion**
- For normal materials $n$ is larger at shorter $\lambda$, so shorter wavelengths bend **more than** longer ones.

---

## Q12 — TIR conditions

Total internal reflection only happens when the refracted ray would have to bend *past* 90° from the normal — and that's only possible going from a denser to a less dense medium (higher $n$ to lower $n$). If you start in a medium with $n<1$, every other typical medium has $n\ge 1$, so you're going *into* a denser medium and there's no critical angle to exceed.

TIR requires going from higher $n$ to **lower** $n$. A ray traveling in a medium of index **less than one** (or equal to anything's neighbors) can never TIR into a denser medium — there's no $\theta_c$ to exceed.

---

**Note:** Q1 depends on the mirror-figure geometry. All other answers were computed from first principles and should be reliable; please cross-check with any answer key.
