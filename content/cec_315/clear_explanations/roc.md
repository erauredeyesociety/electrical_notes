# Region of Convergence (ROC) — Clear Explanation

**For:** CEC 315 Signals and Systems, applies to both Laplace ($s$-domain) and $z$-transform ($z$-domain).

**What you'll get from this doc:** a deep-enough understanding of ROC that the rules stop feeling arbitrary. Most of the confusion around ROC comes from treating it as a list of facts to memorize. It's actually one idea (an integral has to converge) with a bunch of consequences.

---

## 1. The 30-second version

The Laplace transform is an integral:

$$X(s) = \int_{-\infty}^{\infty} x(t)\, e^{-st}\, dt$$

**That integral doesn't always converge.** For some values of $s$ it gives a finite number; for others it blows up to infinity. The **Region of Convergence (ROC)** is the set of complex numbers $s$ where the integral actually converges.

Same idea for the $z$-transform: $X(z) = \sum_n x[n] z^{-n}$ only converges for some values of $z$. That set is the ROC.

**Why this matters:** a transform formula $X(s) = \tfrac{1}{s+3}$ without an ROC is *ambiguous* — it can represent two completely different signals. The ROC is how you pick which one.

That's the whole thing. Everything else is mechanics.

---

## 2. Why does ROC exist at all? (The integral must converge)

Take a concrete signal and try to transform it by hand:

$$x(t) = e^{-3t}\, u(t) \quad\Rightarrow\quad X(s) = \int_{0}^{\infty} e^{-3t}\, e^{-st}\, dt = \int_{0}^{\infty} e^{-(s+3)t}\, dt$$

This integral converges **only if** the exponent is negative as $t \to \infty$, which means we need $\operatorname{Re}\{s+3\} > 0$, i.e., $\operatorname{Re}\{s\} > -3$.

Evaluate for $s$ in that region:

$$X(s) = \left[\frac{e^{-(s+3)t}}{-(s+3)}\right]_0^{\infty} = \frac{1}{s+3}, \quad \text{ROC: } \operatorname{Re}\{s\} > -3.$$

The **formula** $\tfrac{1}{s+3}$ is defined for any $s \ne -3$. But the transform *as an integral* is only defined where the integral converges. For $s$ with $\operatorname{Re}\{s\} \le -3$, the integral diverges. We can *analytically continue* the formula past the ROC, but the resulting expression doesn't correspond to the Laplace transform of $e^{-3t}u(t)$ anymore.

**Takeaway:** ROC is not a "rule tacked on at the end." It's where the transform integral actually makes sense.

---

## 3. The killer insight: same formula, different signals

Now take a different signal:

$$y(t) = -e^{-3t}\, u(-t) \quad\text{(exists only for } t<0\text{, and has a negative sign)}$$

Compute:

$$Y(s) = -\int_{-\infty}^{0} e^{-3t}\, e^{-st}\, dt = -\int_{-\infty}^{0} e^{-(s+3)t}\, dt$$

This integral converges as $t \to -\infty$ only if $\operatorname{Re}\{s+3\} < 0$, i.e., $\operatorname{Re}\{s\} < -3$. Evaluating:

$$Y(s) = \frac{1}{s+3}, \quad \text{ROC: } \operatorname{Re}\{s\} < -3.$$

**Same formula.** Completely different signal ($x$ lives on $t > 0$ and decays; $y$ lives on $t < 0$ and grows backwards). **Only the ROC distinguishes them.**

If someone hands you $X(s) = \tfrac{1}{s+3}$ without an ROC, you literally cannot tell whether they mean $x(t) = e^{-3t}u(t)$ or $y(t) = -e^{-3t}u(-t)$.

This is why *every* ROC rule, theorem, and warning keeps saying: **always state the ROC**. It's not pedantry — without it, the answer is undefined.

---

## 4. Why is the ROC a vertical strip (Laplace) or an annular ring (Z)?

Convergence of the Laplace integral depends only on how $|e^{-st}|$ behaves, because everything else in the integrand is bounded by $|x(t)|$. And:

$$|e^{-st}| = |e^{-(\sigma + j\omega)t}| = e^{-\sigma t}$$

It only depends on $\sigma = \operatorname{Re}\{s\}$. So whether the integral converges is purely a question of $\sigma$ — and the set of $s$ with $\sigma$ in some range is a **vertical strip** in the $s$-plane.

For the $z$-transform, the analogue argument: $|z^{-n}| = |r e^{j\omega}|^{-n} = r^{-n}$ where $r = |z|$. Convergence depends only on $r$, so the ROC is the set of $z$ with $|z|$ in some range — an **annular ring** centered at the origin.

**Takeaway:** the *shape* of the ROC isn't arbitrary, it follows directly from what variable actually controls convergence.

---

## 5. Why doesn't the ROC contain poles?

A pole is a value of $s$ (or $z$) where the transform formula evaluates to infinity. If the integral converged at a pole, the resulting number would be finite — contradicting the pole. So the ROC and the poles are disjoint by construction.

Another way to see it: near a pole, the transform blows up. The integral can't sum to "infinity."

---

## 6. The rules for which side of the pole

### Laplace

| Signal type | ROC shape |
|---|---|
| Finite duration | All of $s$-plane |
| Right-sided (nonzero only for $t \ge T_0$) | $\operatorname{Re}\{s\} > \sigma_{\max}$ (right of rightmost pole) |
| Left-sided (nonzero only for $t \le T_0$) | $\operatorname{Re}\{s\} < \sigma_{\min}$ (left of leftmost pole) |
| Two-sided | Vertical strip between two poles (may be empty) |

**Why "right of rightmost pole" for right-sided signals?** A right-sided signal's integral from $0$ to $\infty$ converges when the decay rate of $e^{-\sigma t}$ is faster than the signal's growth. The most-restrictive pole is the one with the largest real part (slowest-decaying mode). To kill that mode, you need $\sigma$ larger than it. So the ROC is $\sigma > \sigma_{\max}$ — to the right of the rightmost pole.

For left-sided, the integral is from $-\infty$ to $0$; convergence as $t \to -\infty$ requires $\sigma < \sigma_{\min}$ (left of leftmost pole).

### $z$-Transform

| Signal type | ROC shape |
|---|---|
| Finite duration | Entire $z$-plane (except possibly $0$ or $\infty$) |
| Right-sided (causal) | $|z| > r_{\max}$ (outside outermost pole) |
| Left-sided (anti-causal) | $|z| < r_{\min}$ (inside innermost pole) |
| Two-sided | Annular ring $r_1 < |z| < r_2$ |

Same logic, just in radius instead of $\sigma$.

### Finite-duration rule (both)

A finite-duration signal has a transform that converges for *any* $s$ (resp. $z$), because a finite integral of a finite signal is finite. So the ROC is the entire plane. (The $z$-transform may exclude $z = 0$ and/or $\infty$ because powers $z^{-k}$ blow up there for certain $k$.)

---

## 7. ROC and signal properties (the three-way relationship)

The ROC connects to **causality** and **stability** in a precise, useful way.

### Fourier transform exists iff ROC contains the imaginary axis (or unit circle)

The Fourier transform is the Laplace transform evaluated at $s = j\omega$ (or the $z$-transform at $z = e^{j\omega}$). That evaluation is valid only where the Laplace/$z$ transform converges.

- Laplace: FT exists $\iff$ $j\omega$-axis $\subset$ ROC
- Z: DTFT exists $\iff$ $|z| = 1$ (unit circle) $\subset$ ROC

### BIBO stable iff FT exists iff ROC contains the axis/unit-circle

A BIBO-stable system has a bounded Fourier transform (frequency response). So:

- CT: BIBO stable $\iff$ ROC of $H(s)$ contains $j\omega$-axis
- DT: BIBO stable $\iff$ ROC of $H(z)$ contains unit circle

### Causal iff ROC is right half-plane / exterior of circle

A causal signal is right-sided (zero for $t < 0$ or $n < 0$). From §6:

- Causal CT $\iff$ ROC is $\operatorname{Re}\{s\} > \sigma_{\max}$ (right of rightmost pole)
- Causal DT $\iff$ ROC is $|z| > r_{\max}$ (outside outermost pole, and ROC includes $z = \infty$)

### Causal + Stable = "all poles in LHP (CT) / inside unit circle (DT)"

This is the "Golden Rule" every cheat-sheet states. Here's why it follows from the other two:

- **Causal** puts the ROC to the right of every pole.
- **Stable** requires the ROC to include the $j\omega$-axis.
- For both: every pole must be to the **left** of the $j\omega$-axis, i.e., $\operatorname{Re}\{p_i\} < 0$ — all poles in the open LHP.

Analogous in DT: poles outside the ROC means poles inside the unit circle, so $|p_i| < 1$.

**Key insight:** the Golden Rule isn't a separate fact to memorize. It's forced by combining the causal-means-ROC-right-of-poles rule with the stable-means-ROC-includes-axis rule.

---

## 8. How to determine the ROC in practice

Given a signal, ROC is determined by the signal's time-domain shape:

- Right-sided? → ROC is right of rightmost pole.
- Left-sided? → ROC is left of leftmost pole.
- Two-sided? → ROC is the strip between two specific poles.
- Given "stable"? → ROC includes the axis.
- Given "causal"? → ROC is right-sided.

Given *just* the transform formula (no ROC), the signal is ambiguous — and they must tell you which of these applies.

### Worked example: given a formula, list the possibilities

$X(s) = \dfrac{1}{(s+1)(s-2)}$ has poles at $s = -1$ and $s = 2$. Three possible ROCs:

1. $\operatorname{Re}\{s\} > 2$: right-sided (causal). Signal grows (has $e^{2t}$ term). Not stable.
2. $\operatorname{Re}\{s\} < -1$: left-sided (anti-causal). Signal grows as $t \to -\infty$.
3. $-1 < \operatorname{Re}\{s\} < 2$: two-sided. ROC includes $j\omega$-axis → stable. Signal is $e^{-t}u(t)$-like for $t>0$ and $-e^{2t}u(-t)$-like for $t<0$, decaying on both sides.

All three have the same $X(s)$ formula. The ROC picks which one.

---

## 9. The most common ROC mistakes (and the fix)

### Mistake 1: "I computed X(s), I'm done"

**Symptom:** turn in `X(s) = 1/(s+3)` without ROC.

**Why it's wrong:** ambiguous signal (§3).

**Fix:** always write `X(s) = 1/(s+3), Re{s} > -3` (or whatever the ROC is).

### Mistake 2: "The pole is at s = -3, so the ROC is Re{s} > -3"

**Symptom:** assuming right-sided without being told.

**Why it's wrong:** if the signal is actually left-sided, the ROC is $\operatorname{Re}\{s\} < -3$ — same formula, different signal.

**Fix:** use the problem's statement about the signal's shape (causal? left-sided? stable?) to pick the ROC. Don't default to "right of pole."

### Mistake 3: Picking direction of each PFE term from the pole's sign

**Symptom:** in partial fractions, assuming a term like $\tfrac{1}{s+2}$ is always $e^{-2t}u(t)$ "because the pole is at $-2$, which is negative."

**Why it's wrong:** the direction of each term comes from the **ROC**, not the pole's sign. Same term $\tfrac{1}{s+2}$ could invert to:

- $e^{-2t}u(t)$ if the ROC is to the right of $s = -2$, or
- $-e^{-2t}u(-t)$ if the ROC is to the left of $s = -2$.

**Fix:** for each pole, ask "is the ROC to the right or left of this pole?" Right → use the right-sided pair; left → use the left-sided pair.

### Mistake 4: "ROC includes j-omega axis so everything is stable"

**Symptom:** treating every ROC that touches the $j\omega$-axis as stable.

**Why it's wrong:** the $j\omega$-axis (or unit circle for Z) must be *strictly inside* the ROC, not on its boundary. A pole on the $j\omega$-axis means the ROC boundary is the $j\omega$-axis — the axis is not included — and the system is only marginally stable (impulse response doesn't decay).

**Fix:** check that poles are strictly in the open LHP (CT) / strictly inside unit circle (DT).

### Mistake 5: Computing Z partial fractions in $z$ instead of $z^{-1}$

**Symptom:** expansion has terms like $\tfrac{A}{z - a}$ instead of $\tfrac{A}{1 - az^{-1}}$.

**Why it's wrong:** the standard $z$-transform pairs are written in $z^{-1}$. A pole at $z = a$ corresponds to the factor $(1 - az^{-1})$, not $(z - a)$. If you expand in the wrong form, the table lookup doesn't apply.

**Fix:** always set up the partial fraction in $z^{-1}$. Factor the denominator as a product of $(1 - d_k z^{-1})$ terms. Pole at $z = 0.5$ → factor $(1 - 0.5z^{-1})$.

---

## 10. Quick reference card

| Fact | Laplace | Z |
| --- | --- | --- |
| Variable | $s = \sigma + j\omega$ | $z = re^{j\omega}$ |
| ROC shape | vertical strip (in $\sigma$) | annular ring (in $r$) |
| FT lives on | $j\omega$-axis | unit circle |
| Right-sided ROC | $\sigma > \sigma_{\max}$ | $|z| > r_{\max}$ |
| Left-sided ROC | $\sigma < \sigma_{\min}$ | $|z| < r_{\min}$ |
| Two-sided ROC | strip between poles | ring between pole radii |
| Finite-duration ROC | all of $s$-plane | all of $z$-plane (except $0, \infty$) |
| FT exists | $j\omega \subset$ ROC | unit circle $\subset$ ROC |
| BIBO stable (same as FT exists) | $j\omega \subset$ ROC | unit circle $\subset$ ROC |
| Causal | ROC is rightmost half-plane | ROC is exterior of a circle (incl. $z = \infty$) |
| Causal + Stable | all poles $\operatorname{Re}\{p_i\} < 0$ | all poles $|p_i| < 1$ |

---

## 11. Summary

1. **ROC = where the transform integral/sum converges.** Not a tacked-on rule; it's the domain of the definition.
2. **A transform formula without an ROC is ambiguous** — same formula can be different signals.
3. **ROC shape is forced** by the fact that convergence depends only on $\sigma$ (Laplace) or $|z|$ (Z) → strip / annulus.
4. **ROC excludes poles**, because the transform can't converge to a finite value at a pole.
5. **Rules for which side of the pole** follow from whether the signal is right-sided, left-sided, two-sided, or finite.
6. **FT exists iff $j\omega$-axis (or unit circle) is in the ROC.** This is the same as saying BIBO stable, which is the same as saying the frequency response is well-defined.
7. **Causal = ROC right half-plane** (CT) **/ exterior of circle** (DT).
8. **Causal + Stable $\Leftrightarrow$ all poles in LHP / inside unit circle.** This is a consequence of (6) + (7), not a separate rule.
9. In partial fractions, **ROC picks each term's direction** (right- vs. left-sided), not the pole's sign.
10. Z partial fractions go in $z^{-1}$, **not** in $z$.

If you can reproduce the reasoning behind points 1–5 from scratch, the rest falls out. That's the goal.
