# Equation Gaps: MEs vs. master_equations.tex

Equations / relations used in ME and MQ problems that were **not** (or only implicitly) present in the original `master_equations.tex`. Cross-checked against every ME12–ME36, MQ12–MQ36, and the three practice midterms.

---

## Module 12 — Fluid Mechanics

No gaps found that affect problem-solving. All problems use $\rho$, $p$, Pascal's law, buoyancy, continuity, Bernoulli, Torricelli — all already in master.

*Minor:* hydraulic torque problem uses $\tau = F r$ and friction $F = \mu N$ (mechanics, not fluids — fine to leave off).

## Module 14 — Oscillations

No gaps. Practice problems use $\omega_\text{spring}$, $\omega_\text{pend}$, SHM energy, damped, driven, all present.

## Module 15 — Waves

No gaps. All problems use $v = \sqrt{F/\mu}$, $\omega$, $k$, $\lambda$, $f_n$, $P_\text{av}$ — all present.

## Module 16 — Sound

**Gap:** Temperature-dependent speed of sound in air appears in multiple problems (MQ16b, midterm1, midterm3_final):
$$v(T) = (331\text{ m/s})\sqrt{T/(273\text{ K})}$$

This is the approximate form (valid near STP) derived from $v = \sqrt{\gamma R T/M}$.

## Module 17 — Temperature and Heat

**Gap:** Temperature scale conversions used constantly but not listed:
$$T_K = T_C + 273.15,\quad T_F = \tfrac{9}{5}T_C + 32,\quad T_R = T_F + 459.67$$

*Minor:* MEs reference "mechanical energy → thermal" conversion $\Delta U_\text{thermal} = mc\Delta T$ — same as $Q = mc\Delta T$.

## Module 18 — Kinetic Theory

No gaps. $v_\text{rms} = \sqrt{3RT/M}$ is listed (equivalent form to $\sqrt{3kT/m}$).

*Could add explicitly:* $K_\text{tr,tot} = \tfrac{3}{2}nRT$ (total translational KE of $n$ moles) — used in problems like "find $T$ from $K_\text{tr}$".

## Module 19 — First Law

No gaps.

## Module 20 — Second Law and Entropy

No gaps.

## Module 33 — EM Waves

No gaps. Malus, Brewster, Poynting, intensity, radiation pressure — all present.

## Module 34 — Geometric Optics

**Gap:** Lens power in diopters — used in ME34, MQ34b ("glasses with power -4.32 diopters"):
$$P\;[\text{diopters}] = 1/f\;[\text{m}]$$

**Gap:** Vision correction (near/far point) — a converging lens corrects hyperopia (far-sightedness), a diverging lens corrects myopia (near-sightedness). No new equation, just conceptual.

**Gap:** Apparent depth (useful for "object in water viewed from air" problems):
$$d_\text{apparent} = d_\text{real}\cdot\frac{n_\text{observer}}{n_\text{medium}}$$

Already mentioned in review.md but not in master_equations.tex.

## Module 35 — Interference

**Gap:** Width of central maximum (distance between $m = -1$ and $m = +1$ dark fringes in Young's setup) — explicit formula used in ME35-36:
$$w_\text{central} = 2\lambda R/d$$
(Follows directly from fringe spacing $\lambda R/d$; noting this makes the "width of central max" problems trivial.)

## Module 36 — Diffraction

**Gap:** Width of central maximum for single slit:
$$w_\text{central} = 2\lambda R/a$$

(Again follows from $a\sin\theta = \lambda$ at $m = \pm 1$.)

**Gap:** Number of visible orders for a grating: $m_\text{max} = \lfloor d/\lambda\rfloor$, total visible maxima $= 2 m_\text{max} + 1$.

---

## Summary

Total gaps identified: **~8**, mostly formulas derivable on the spot from material already in the master sheet. The two most load-bearing additions are:

1. Temperature-dependent sound speed (appears in multiple midterm 1 and final practice problems)
2. Lens power in diopters (appears in vision-correction problems in M34)

These have been appended to `master_equations.tex`.
