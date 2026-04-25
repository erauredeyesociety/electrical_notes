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

Without the figure I can't pin down the geometry uniquely. The standard tools:

For a ray reflecting off two mirrors meeting at angle $\phi$, the *total deviation* is
$$\delta = 360° - 2\phi$$
(if both reflections occur). For a ray that strikes the first mirror at angle $\theta$ from its normal, the angle to the second mirror's normal can usually be found via the triangle made by the two mirrors and the connecting ray segment: angle in that triangle $= \phi - (90°-\theta) - (90°-\alpha)$ etc. — depends on which angle the figure labels "α."

**Method:** identify the closed triangle formed by ray segments and mirrors; sum of interior angles $= 180°$ relates $\alpha$, $\phi$, $\theta$ directly.

A common version of this figure gives $\alpha = \phi - \theta = 62° - 28° = \boxed{34°}$ — *verify against the figure.*

---

## Q2 — Speed of light in a medium

$n=1.91$.
$$v = c/n = (3.00\times 10^8)/1.91 = 1.571\times 10^8\ \text{m/s} \Rightarrow \boxed{1.57\times 10^8\ \text{m/s}}$$

---

## Q3 — Wavelength in a medium

$f = 6.23\times 10^{14}$ Hz, $n=1.21$.
$$\lambda_{\text{vac}} = c/f = 4.815\times 10^{-7}\ \text{m} = 481.5\ \text{nm}$$
$$\lambda_{\text{med}} = \lambda_{\text{vac}}/n = 481.5/1.21 = \boxed{397.9\ \text{nm}}$$

(Frequency does not change crossing into a medium; wavelength shrinks by $n$.)

---

## Q4 — Find angle of incidence

$n_1=1$, $n_2=1.61$, $\theta_2 = 21°$.
$$\sin\theta_1 = n_2\sin\theta_2 = 1.61\sin(21°) = 1.61(0.3584) = 0.5770$$
$$\theta_1 = \arcsin(0.5770) = \boxed{35.24°}$$

---

## Q5 — Air → oil → water, find angle in water

For a stack of parallel layers, Snell's law chains: $\sin$ in any layer = $n_{\text{air}}\sin\theta_{\text{air}}/n_{\text{layer}}$. The middle layer (oil) drops out for the *direction* in water.

If $\theta = 32°$ is the angle of incidence in air:
$$\sin\phi = \sin(32°)/n_{\text{water}} = 0.5299/1.33 = 0.3984$$
$$\phi = \boxed{23.49°}$$

(If $\theta$ is the angle inside the oil instead, use $n_{\text{oil}}\sin\theta = n_{\text{water}}\sin\phi$ — same final water angle to within Snell's chain.)

---

## Q6 — Dispersion through BK7 glass slab

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

If the figure depicts $\theta = 49°$ as the critical angle for TIR at the boundary with $n_2 = 1.5$:
$$\sin\theta_c = n_2/n_1 \Rightarrow n_1 = n_2/\sin\theta_c = 1.5/\sin(49°) = 1.5/0.7547 = \boxed{1.988}$$

---

## Q8 — Refraction angle from a known critical angle

Critical angle 42.3° at the liquid-air interface ⇒ $n_{\text{liquid}} = 1/\sin(42.3°) = 1/0.6730 = 1.486$.

Ray in air enters liquid at $\theta_1 = 34°$:
$$\sin\theta_2 = \sin(34°)/n_{\text{liquid}} = 0.5592/1.486 = 0.3763$$
$$\theta_2 = \boxed{22.10°}$$

---

## Q9 — Two polarizers (Malus chain)

First filter at $37°$ from input polarization → $I_1 = I_0\cos^2(37°) = I_0(0.7986)^2 = 0.6378\,I_0$.
Second filter at $49°$ relative to the first → $I_2 = I_1\cos^2(49°) = I_1(0.6561)^2 = 0.4305\,I_1$.
$$I_2/I_0 = 0.6378\cdot 0.4305 = \boxed{0.2746}$$

---

## Q10 — Brewster's angle for glass in oil

$n_{\text{glass}} = 1.6$, $n_{\text{oil}} = 1.465$. With incident in oil, reflected from glass:
$$\theta_B = \arctan(n_{\text{glass}}/n_{\text{oil}}) = \arctan(1.6/1.465) = \arctan(1.0922) = \boxed{47.53°}$$

---

## Q11 — Refraction qualitative

- Bigger $\Delta n$ → more bending → **larger** ✓
- $n$ depends on **wavelength** → called **dispersion**
- For normal materials $n$ is larger at shorter $\lambda$, so shorter wavelengths bend **more than** longer ones.

---

## Q12 — TIR conditions

TIR requires going from higher $n$ to **lower** $n$. A ray traveling in a medium of index **less than one** (or equal to anything's neighbors) can never TIR into a denser medium — there's no $\theta_c$ to exceed.

---

**Note:** Q1 depends on the mirror-figure geometry. All other answers were computed from first principles and should be reliable; please cross-check with any answer key.
