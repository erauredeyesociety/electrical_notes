# CEC 315 — Exam 3 Flashcards (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Coverage:** Laplace, Inverse Laplace, Unilateral Laplace, Z-Transform, Inverse Z, Unilateral Z, Sampling, Feedback Systems
**Format:** Front/back Q&A for rapid memorization drilling.

---

## Lecture 16 — Laplace Transform and ROC

**Q1:** Write the definition of the bilateral Laplace transform.
**A:** $X(s) = \int_{-\infty}^{\infty} x(t)\,e^{-st}\,dt$, where $s = \sigma + j\omega$. It is the Fourier transform of $x(t)e^{-\sigma t}$; the damping factor $e^{-\sigma t}$ can tame signals whose FT diverges.
*Pitfall:* $X(s)$ alone is incomplete — you must always state the ROC.

**Q2:** Why do we need the Laplace transform when we already have the Fourier transform?
**A:** The FT fails for signals that are not absolutely integrable (e.g., $e^{2t}u(t)$, unstable system responses). The factor $e^{-\sigma t}$ with $\sigma$ large enough forces convergence, so Laplace handles a strictly larger class of signals.
*Pitfall:* Laplace is **not** just "FT with $\omega\to s$"; the substitution $s=j\omega$ works only if $j\omega$-axis $\subset$ ROC.

**Q3:** What is the Region of Convergence (ROC)?
**A:** The set of complex $s$ for which $\int x(t)e^{-st}dt$ converges. For rational $X(s)$, it is a vertical strip in the $s$-plane bounded by poles, parallel to the $j\omega$-axis.
*Pitfall:* ROC depends only on $\sigma=\operatorname{Re}\{s\}$, never on $\omega$.

**Q4:** State the Laplace pair for $e^{-at}u(t)$.
**A:** $e^{-at}u(t) \overset{\mathcal{L}}{\longleftrightarrow} \dfrac{1}{s+a}$, ROC $\operatorname{Re}\{s\} > -\operatorname{Re}\{a\}$.
*Pitfall:* Same algebraic $1/(s+a)$ is also the transform of $-e^{-at}u(-t)$ with ROC $\operatorname{Re}\{s\} < -\operatorname{Re}\{a\}$ — the ROC distinguishes them.

**Q5:** Laplace transform of $\delta(t)$ and $u(t)$?
**A:** $\delta(t) \leftrightarrow 1$, ROC = all $s$. $u(t) \leftrightarrow 1/s$, ROC $\operatorname{Re}\{s\}>0$.
*Pitfall:* The pole of $u(t)$ sits on the $j\omega$-axis, so you cannot get the FT of $u(t)$ just by setting $s=j\omega$.

**Q6:** Laplace transform of $\cos(\omega_0 t)u(t)$ and $\sin(\omega_0 t)u(t)$?
**A:** $\cos\to\dfrac{s}{s^2+\omega_0^2}$, $\sin\to\dfrac{\omega_0}{s^2+\omega_0^2}$, both with ROC $\operatorname{Re}\{s\}>0$.
*Pitfall:* Poles are at $\pm j\omega_0$ (on the axis) — these are marginally stable, so FVT doesn't apply.

**Q7:** Laplace pair for $te^{-at}u(t)$ and $\dfrac{t^{n-1}}{(n-1)!}e^{-at}u(t)$?
**A:** $te^{-at}u(t) \leftrightarrow \dfrac{1}{(s+a)^2}$; general: $\dfrac{t^{n-1}}{(n-1)!}e^{-at}u(t) \leftrightarrow \dfrac{1}{(s+a)^n}$, same ROC as simple pole.
*Pitfall:* Repeated-pole numerators need the $(n-1)!$ normalization.

**Q8:** What is the ROC rule for a right-sided signal?
**A:** The ROC is a right half-plane to the right of the rightmost pole: $\operatorname{Re}\{s\} > \max_i \operatorname{Re}\{p_i\}$.
*Pitfall:* "Right-sided" means $x(t)=0$ for $t<T_0$; strictly causal ($T_0=0$) is the usual case.

**Q9:** What is the ROC rule for a left-sided signal?
**A:** Left half-plane to the left of the leftmost pole: $\operatorname{Re}\{s\} < \min_i \operatorname{Re}\{p_i\}$.
*Pitfall:* Don't confuse with right-sided — the ROC points *away* from where the signal "explodes."

**Q10:** What is the ROC of a finite-duration signal?
**A:** The entire $s$-plane (possibly excluding $s=\pm\infty$) — because the integral has finite limits and always converges.
*Pitfall:* $\delta(t)$ and any truncated signal satisfy this; there are no poles.

**Q11:** Can the ROC contain a pole?
**A:** No — at a pole $X(s)\to\infty$, so the integral cannot converge there.
*Pitfall:* Poles form the *boundaries* of the ROC, never interior points.

**Q12:** When does $X(j\omega) = X(s)\big|_{s=j\omega}$?
**A:** Iff the $j\omega$-axis lies inside the ROC, i.e., $\sigma = 0$ is a convergent line.
*Pitfall:* For $e^{2t}u(t)$, ROC is $\operatorname{Re}\{s\}>2$ — $j\omega$-axis excluded, so no FT exists.

**Q13:** What shape is the ROC for a two-sided signal?
**A:** A vertical strip between two consecutive poles: $\sigma_- < \operatorname{Re}\{s\} < \sigma_+$. If the required bounds are inconsistent, the ROC is empty (no Laplace transform exists).
*Pitfall:* Always intersect the individual ROCs when using linearity.

**Q14:** In a pole-zero plot, what symbols mark poles and zeros?
**A:** $\times$ for poles (roots of denominator $D(s)$), $\circ$ for zeros (roots of numerator $N(s)$). Rational form: $X(s) = K\dfrac{\prod(s-z_i)}{\prod(s-p_j)}$.
*Pitfall:* Zeros don't affect stability; only poles do.

**Q15:** What is the ROC of $\delta(t-t_0)$?
**A:** $\delta(t-t_0) \leftrightarrow e^{-st_0}$, ROC = all $s$. Finite duration $\Rightarrow$ no poles.
*Pitfall:* The shift shows up in the exponent, not in the ROC.

**Q16:** How does the Laplace transform relate to eigenfunctions of LTI systems?
**A:** $e^{st}$ is an eigenfunction: $y(t) = H(s)e^{st}$ where $H(s)=\int h(t)e^{-st}dt$ is the Laplace transform of the impulse response evaluated at $s$.
*Pitfall:* This only holds for LTI systems, and requires $s$ to lie in the ROC of $H(s)$.

---

## Lecture 17 — Inverse Laplace and Properties

**Q1:** What is the practical method for computing an inverse Laplace transform?
**A:** Partial-fraction expansion (PFE) + table lookup. Rewrite $X(s)$ as a sum of standard pairs; each pair's direction (right- or left-sided) is fixed by the ROC.
*Pitfall:* Partial fractions alone are ambiguous — you need the ROC to pick the correct inverse for each term.

**Q2:** How do you handle a repeated pole of order $n$ at $s = p$ in PFE?
**A:** Include $n$ terms: $\dfrac{B_1}{s-p} + \dfrac{B_2}{(s-p)^2} + \cdots + \dfrac{B_n}{(s-p)^n}$. Invert each with $\dfrac{t^{k-1}}{(k-1)!}e^{pt}u(t)$.
*Pitfall:* Forgetting any order — you must list *all* orders up to $n$.

**Q3:** How do you invert a pair of complex-conjugate poles?
**A:** Complete the square in the denominator: $(s+a)^2 + \omega_d^2$. Use pairs $e^{-at}\cos(\omega_d t)u(t) \leftrightarrow \dfrac{s+a}{(s+a)^2+\omega_d^2}$ and $e^{-at}\sin(\omega_d t)u(t) \leftrightarrow \dfrac{\omega_d}{(s+a)^2+\omega_d^2}$.
*Pitfall:* Don't split into complex PFE terms — use the damped sinusoid pairs directly.

**Q4:** State the Laplace linearity property.
**A:** $ax(t)+by(t) \leftrightarrow aX(s)+bY(s)$. The new ROC contains $\text{ROC}_x \cap \text{ROC}_y$ (may be larger if cancellation occurs).
*Pitfall:* If the two ROCs don't overlap, the sum has no Laplace transform.

**Q5:** State the time-shift property.
**A:** $x(t-t_0) \leftrightarrow e^{-st_0}X(s)$, same ROC.
*Pitfall:* Only the algebraic $X(s)$ picks up $e^{-st_0}$; ROC is unchanged. Don't confuse with $s$-shift.

**Q6:** State the $s$-domain shift property.
**A:** $e^{s_0 t}x(t) \leftrightarrow X(s-s_0)$. ROC shifts by $\operatorname{Re}\{s_0\}$.
*Pitfall:* Time-shift changes $X(s)$ multiplicatively; $s$-shift changes its argument — duals, not the same thing.

**Q7:** State the time-scaling property.
**A:** $x(at) \leftrightarrow \dfrac{1}{|a|}X(s/a)$. ROC scales by $|a|$.
*Pitfall:* Sign of $a$ matters: $a<0$ flips the ROC across the $j\omega$-axis.

**Q8:** State the differentiation-in-time property (bilateral).
**A:** $\dfrac{dx}{dt} \leftrightarrow sX(s)$; ROC contains the original ROC.
*Pitfall:* No initial-condition term — that's unilateral only.

**Q9:** State the integration-in-time property.
**A:** $\displaystyle\int_{-\infty}^{t} x(\tau)d\tau \leftrightarrow \dfrac{X(s)}{s}$; ROC = $\text{ROC}_x \cap \{\operatorname{Re}\{s\}>0\}$.
*Pitfall:* Dividing by $s$ adds a pole at the origin, which may shrink the ROC.

**Q10:** State the differentiation-in-$s$ property.
**A:** $-tx(t) \leftrightarrow \dfrac{dX(s)}{ds}$. Equivalently $tx(t) \leftrightarrow -X'(s)$.
*Pitfall:* Watch the minus sign — common source of errors when computing $tx(t)$.

**Q11:** State the convolution property.
**A:** $x(t)*y(t) \leftrightarrow X(s)Y(s)$; ROC contains $\text{ROC}_x\cap\text{ROC}_y$.
*Pitfall:* This is the whole reason Laplace makes LTI analysis easy — differential equations become algebra.

**Q12:** State the Initial Value Theorem (IVT).
**A:** If $x(t)=0$ for $t<0$ and $x(t)$ has no impulse at the origin: $x(0^+) = \lim_{s\to\infty} sX(s)$.
*Pitfall:* Requires $x(t)$ causal and regular at $t=0$; impulses break it.

**Q13:** State the Final Value Theorem (FVT).
**A:** $x(\infty) = \lim_{s\to 0} sX(s)$, **valid only if** all poles of $sX(s)$ are in the open LHP (one allowed at $s=0$).
*Pitfall:* Applying FVT to oscillating or unstable signals gives nonsense. Check pole locations first.

**Q14:** How do you compute the residue at a simple pole $p$ in PFE?
**A:** $B = \lim_{s\to p}(s-p)X(s)$. Then that term is $\dfrac{B}{s-p}$.
*Pitfall:* Valid only for simple poles; repeated poles require derivatives.

**Q15:** How do you compute residues at a repeated pole $(s-p)^n$?
**A:** $B_k = \dfrac{1}{(n-k)!}\left.\dfrac{d^{n-k}}{ds^{n-k}}\left[(s-p)^n X(s)\right]\right|_{s=p}$ for $k = 1,\dots,n$.
*Pitfall:* Keep track of the factorial and the order of differentiation — off-by-one errors are common.

**Q16:** How do you evaluate $|H(j\omega)|$ geometrically from the pole-zero plot?
**A:** $|H(j\omega_0)| = K\dfrac{\prod \text{(distances from } j\omega_0 \text{ to zeros)}}{\prod \text{(distances from } j\omega_0 \text{ to poles)}}$. Phase = sum of zero angles − sum of pole angles.
*Pitfall:* A pole near the $j\omega$-axis produces a peak; a zero near the axis produces a notch.

**Q17:** Laplace transform of $e^{-at}\cos(\omega_d t)u(t)$?
**A:** $\dfrac{s+a}{(s+a)^2+\omega_d^2}$, ROC $\operatorname{Re}\{s\}>-a$. (Shift the cosine pair using the $s$-shift property.)
*Pitfall:* The numerator is $s+a$, not $s$ — easy to drop the shift.

---

## Lecture 18 — System Analysis via Unilateral Laplace

**Q1:** Given an LCCDE $\sum a_k y^{(k)}(t) = \sum b_k x^{(k)}(t)$, how do you find $H(s)$?
**A:** Take Laplace transforms with **zero** initial conditions, replace $d^k/dt^k \to s^k$, and solve: $H(s) = \dfrac{Y(s)}{X(s)} = \dfrac{\sum b_k s^k}{\sum a_k s^k}$.
*Pitfall:* ICs must be zero to get the transfer function; nonzero ICs give ZIR contributions, not $H(s)$.

**Q2:** What does the ROC of $H(s)$ tell you about causality?
**A:** The system is causal iff $H(s)$ is rational with $M\le N$ (proper) and the ROC is a right half-plane to the right of the rightmost pole.
*Pitfall:* Causality is an ROC statement, not just a pole statement.

**Q3:** What does the ROC tell you about BIBO stability?
**A:** The system is BIBO stable iff the ROC of $H(s)$ contains the $j\omega$-axis (so $h(t)$ is absolutely integrable).
*Pitfall:* Stability is about the impulse response, not about poles alone.

**Q4:** State the "Golden Rule" for causal LTI systems.
**A:** A causal LTI system is BIBO stable iff *all* poles of $H(s)$ lie strictly in the open LHP ($\operatorname{Re}\{p_i\}<0$ for all $i$).
*Pitfall:* Poles on the $j\omega$-axis $\Rightarrow$ marginally stable, **not** BIBO stable. RHP poles $\Rightarrow$ unstable.

**Q5:** What are the block-diagram reduction rules?
**A:** Cascade: $H_1 H_2$. Parallel: $H_1 + H_2$. Negative feedback: $\dfrac{G}{1+GF}$ (forward $G$, feedback $F$).
*Pitfall:* For positive feedback use $1-GF$; sign convention matters.

**Q6:** Define the unilateral Laplace transform.
**A:** $\mathcal{X}(s) = \displaystyle\int_{0^-}^{\infty} x(t)e^{-st}dt$. The $0^-$ lower limit captures impulses and initial conditions at $t=0$.
*Pitfall:* $0^-$ vs $0^+$ matters if $x(t)$ has an impulse or jump at $t=0$; always use $0^-$.

**Q7:** Unilateral differentiation rule (first derivative)?
**A:** $\mathcal{L}_u\{x'(t)\} = sX(s) - x(0^-)$.
*Pitfall:* The sign is **minus**; contrast with the $+$ sign in the unilateral Z shift rule.

**Q8:** Unilateral differentiation rule (second derivative)?
**A:** $\mathcal{L}_u\{x''(t)\} = s^2 X(s) - sx(0^-) - x'(0^-)$.
*Pitfall:* Order matters: $sx(0^-)$ (not $x(0^-)s^2$), and $x'(0^-)$ is the last term.

**Q9:** How do you solve an LCCDE with nonzero ICs using unilateral Laplace?
**A:** Transform both sides, substitute IC-bearing derivative formulas, solve for $Y(s)$, then invert. The result splits into ZSR (input-driven, ICs set to 0) + ZIR (input set to 0, ICs preserved).
*Pitfall:* Don't forget the IC terms when transforming each derivative.

**Q10:** What is the zero-state response (ZSR)?
**A:** The response when all ICs are zero, computed from $Y_{\text{ZSR}}(s) = H(s)X(s)$.
*Pitfall:* ZSR alone is not the full answer if ICs are nonzero.

**Q11:** What is the zero-input response (ZIR)?
**A:** The response to initial conditions alone (input set to zero); generated entirely by the modes of the homogeneous equation.
*Pitfall:* ZIR lives on the natural frequencies (poles of $H(s)$), independent of $X(s)$.

**Q12:** How do you tell natural-response modes from forced-response modes?
**A:** Natural modes come from poles of $H(s)$ (system eigenvalues). Forced modes come from poles of $X(s)$ (input).
*Pitfall:* Nothing stops them from coinciding; repeated coincident poles produce $t e^{pt}$-style terms.

**Q13:** If an ODE is $y'' + 3y' + 2y = x(t)$, what is $H(s)$?
**A:** $H(s) = \dfrac{1}{s^2+3s+2} = \dfrac{1}{(s+1)(s+2)}$. Both poles in LHP $\Rightarrow$ causal + stable.
*Pitfall:* Don't forget to factor to read off pole locations.

**Q14:** For a causal LTI system with $H(s) = \dfrac{1}{s-1}$, is it stable?
**A:** No — the pole at $s=1$ is in the RHP. The Golden Rule fails.
*Pitfall:* Causality alone doesn't imply stability; you need all poles in the open LHP.

**Q15:** What is the feedback transfer function $Y/X$ if forward path is $G(s)$ and feedback path is $F(s)$ (negative feedback)?
**A:** $\dfrac{Y(s)}{X(s)} = \dfrac{G(s)}{1+G(s)F(s)}$.
*Pitfall:* Unity feedback is $F=1$: $Y/X = G/(1+G)$. Don't drop the "+1".

**Q16:** Why does causal + stable imply rightmost pole $<0$?
**A:** Causal $\Rightarrow$ ROC is right of rightmost pole. Stable $\Rightarrow j\omega$-axis $\subset$ ROC. Both $\Rightarrow$ rightmost pole's real part is $<0$.
*Pitfall:* The two conditions combine into the single statement "all poles in open LHP."

---

## Lecture 19 — Z-Transform and ROC

**Q1:** Write the definition of the bilateral Z-transform.
**A:** $X(z) = \displaystyle\sum_{n=-\infty}^{\infty} x[n]z^{-n}$, with $z = re^{j\omega}$ (complex variable).
*Pitfall:* It is the DTFT of $x[n]r^{-n}$; when $r=1$, Z reduces to DTFT.

**Q2:** What replaces the $j\omega$-axis in the $z$-plane?
**A:** The unit circle $|z|=1$. The DTFT lives on the unit circle: $X(e^{j\omega}) = X(z)\big|_{z=e^{j\omega}}$.
*Pitfall:* Valid only if the unit circle is contained in the ROC.

**Q3:** Z-transform pair for $a^n u[n]$?
**A:** $a^n u[n] \leftrightarrow \dfrac{1}{1-az^{-1}} = \dfrac{z}{z-a}$, ROC $|z|>|a|$. Pole at $z=a$.
*Pitfall:* The pole is at $z=a$, not $z=1/a$.

**Q4:** Z-transform pair for $-a^n u[-n-1]$?
**A:** $-a^n u[-n-1] \leftrightarrow \dfrac{1}{1-az^{-1}}$, ROC $|z|<|a|$.
*Pitfall:* Same algebraic $X(z)$ as $a^n u[n]$ — ROC (inside vs. outside the pole) distinguishes them.

**Q5:** Z-transform of $\delta[n]$ and $\delta[n-k]$?
**A:** $\delta[n]\leftrightarrow 1$, ROC = all $z$. $\delta[n-k]\leftrightarrow z^{-k}$, ROC $|z|>0$ (if $k>0$) or $|z|<\infty$ (if $k<0$).
*Pitfall:* Shift introduces an exclusion at $0$ or $\infty$ depending on sign of $k$.

**Q6:** Z-transform of $u[n]$?
**A:** $u[n]\leftrightarrow \dfrac{1}{1-z^{-1}} = \dfrac{z}{z-1}$, ROC $|z|>1$. Pole on the unit circle at $z=1$.
*Pitfall:* Since pole lies on $|z|=1$, the DTFT of $u[n]$ does not come from simple substitution.

**Q7:** What shape is the ROC of a Z-transform?
**A:** An annular ring $r_1 < |z| < r_2$ in the $z$-plane, centered at the origin. It never contains a pole.
*Pitfall:* ROC depends only on $|z|$, not on $\arg z$.

**Q8:** ROC rule for a right-sided (causal) sequence?
**A:** $|z| > |p_{\max}|$, the exterior of the circle passing through the outermost pole. May extend to $\infty$.
*Pitfall:* Must also include $z=\infty$ for truly causal sequences (no future samples).

**Q9:** ROC rule for a left-sided (anti-causal) sequence?
**A:** $|z|<|p_{\min}|$, the interior of the circle passing through the innermost pole. May include $z=0$ only if $x[n]=0$ for all $n>0$.
*Pitfall:* "Inside" here means closer to the origin, i.e., smaller $|z|$.

**Q10:** ROC rule for a two-sided sequence?
**A:** An annular ring $|p_k|<|z|<|p_{k+1}|$ between two consecutive poles (ordered by magnitude). May be empty.
*Pitfall:* Intersection with each individual ROC must be nonempty.

**Q11:** ROC of a finite-length sequence?
**A:** The entire $z$-plane, possibly excluding $z=0$ (if there are positive-index samples) and/or $z=\infty$ (if there are negative-index samples).
*Pitfall:* Pure causal finite sequences exclude only $z=0$; pure anticausal exclude only $z=\infty$.

**Q12:** When does the DTFT exist (in terms of ROC)?
**A:** Iff the unit circle $|z|=1$ lies in the ROC of $X(z)$. Then $X(e^{j\omega}) = X(z)|_{z=e^{j\omega}}$.
*Pitfall:* A pole on the unit circle kills DTFT existence in the ordinary sense.

**Q13:** CT–DT parallel: what maps to what?
**A:** $s$-plane LHP $\leftrightarrow$ interior of unit circle (stable region). $j\omega$-axis $\leftrightarrow$ unit circle. RHP $\leftrightarrow$ exterior. ROC strips in CT $\leftrightarrow$ annular rings in DT.
*Pitfall:* This intuition generalizes stability; only $z=e^{sT}$ is a literal map.

**Q14:** How does pole magnitude relate to sequence growth?
**A:** For causal sequences: $|p|<1 \Rightarrow$ decaying; $|p|=1 \Rightarrow$ constant-amplitude; $|p|>1 \Rightarrow$ growing.
*Pitfall:* Sign of the pole matters for alternation (e.g., $(-0.5)^n$ oscillates but still decays).

**Q15:** Z-transform of $na^n u[n]$?
**A:** $na^n u[n]\leftrightarrow \dfrac{az^{-1}}{(1-az^{-1})^2}$, ROC $|z|>|a|$.
*Pitfall:* Derived from $z$-differentiation: $nx[n]\leftrightarrow -z\,dX/dz$.

**Q16:** Why is Z the "DT analog" of Laplace?
**A:** Both generalize their respective Fourier transforms by introducing a damping/growth factor. Laplace uses $e^{-\sigma t}$; Z uses $r^{-n}$. Same structure: rational pairs, ROC rules, stability via pole locations.
*Pitfall:* They use different variables ($s$ vs $z$) and different stability regions (LHP vs unit circle).

---

## Lecture 20 — Inverse Z-Transform and Properties

**Q1:** What is the standard method for inverse Z-transform?
**A:** Partial-fraction expansion **in $z^{-1}$**, then table lookup. Each term's direction (right- or left-sided) is chosen to match the ROC.
*Pitfall:* Work in $z^{-1}$, not $z$. Otherwise the standard-form $1/(1-az^{-1})$ doesn't appear and you'll miscompute residues.

**Q2:** ROC outside a pole $\Rightarrow$ which sign of the inverse?
**A:** Right-sided: each term $\dfrac{A}{1-az^{-1}}$ inverts to $A\,a^n u[n]$.
*Pitfall:* Only valid if that pole is on the "inside" of your ROC ring.

**Q3:** ROC inside a pole $\Rightarrow$ which sign?
**A:** Left-sided: $\dfrac{A}{1-az^{-1}}$ inverts to $-A\,a^n u[-n-1]$ (negative and anti-causal).
*Pitfall:* Forgetting the minus sign and the $-1$ shift in $u[-n-1]$ is a classic error.

**Q4:** How to invert a pair of complex-conjugate poles at $re^{\pm j\omega_0}$?
**A:** They combine into damped sinusoids: $r^n\cos(\omega_0 n)u[n]$ or $r^n\sin(\omega_0 n)u[n]$, ROC $|z|>r$. Use the pairs in the Z table rather than splitting into complex residues.
*Pitfall:* Work in terms of $r$ (magnitude) and $\omega_0$ (angle); don't try complex PFE.

**Q5:** State the Z linearity property.
**A:** $ax_1[n]+bx_2[n]\leftrightarrow aX_1(z)+bX_2(z)$, ROC contains $\text{ROC}_1\cap\text{ROC}_2$ (possibly larger).
*Pitfall:* If ROCs don't overlap, the sum has no Z-transform.

**Q6:** State the Z time-shift property.
**A:** $x[n-n_0]\leftrightarrow z^{-n_0}X(z)$. Same ROC except possibly at $z=0$ or $z=\infty$.
*Pitfall:* $z^{-1}$ is the *unit delay* — not a scaling.

**Q7:** State the Z-domain scaling ($z$-shift) property.
**A:** $z_0^n x[n]\leftrightarrow X(z/z_0)$. ROC scales: bounds multiply by $|z_0|$.
*Pitfall:* Special case: $(-1)^n x[n]\leftrightarrow X(-z)$, reflecting poles/zeros through the origin.

**Q8:** State the Z convolution property.
**A:** $x_1[n]*x_2[n]\leftrightarrow X_1(z)X_2(z)$. ROC contains the intersection.
*Pitfall:* This is what makes $H(z)=Y(z)/X(z)$ meaningful for LTI systems.

**Q9:** State the $z$-differentiation property.
**A:** $nx[n]\leftrightarrow -z\dfrac{dX(z)}{dz}$.
*Pitfall:* Note the $-z$ multiplier, not just $-d/dz$; used to derive $na^n u[n]$ pair.

**Q10:** State the time-reversal property.
**A:** $x[-n]\leftrightarrow X(z^{-1})$. ROC is inverted: $r_1<|z|<r_2$ becomes $1/r_2<|z|<1/r_1$.
*Pitfall:* A causal sequence reversed becomes anti-causal; the ROC flips accordingly.

**Q11:** State the first-difference and accumulation properties.
**A:** $x[n]-x[n-1]\leftrightarrow (1-z^{-1})X(z)$. $\displaystyle\sum_{k=-\infty}^{n} x[k]\leftrightarrow \dfrac{X(z)}{1-z^{-1}}$.
*Pitfall:* Accumulation introduces a pole at $z=1$, potentially shrinking the ROC.

**Q12:** State the IVT for Z (causal sequences).
**A:** $x[0] = \lim_{z\to\infty} X(z)$, valid when $x[n]$ is causal.
*Pitfall:* Works only if $x[n]=0$ for $n<0$; otherwise you get the wrong answer.

**Q13:** State the FVT for Z.
**A:** $x[\infty] = \lim_{z\to 1}(1-z^{-1})X(z)$, **valid only if** all poles of $(1-z^{-1})X(z)$ lie strictly inside the unit circle (one allowed at $z=1$).
*Pitfall:* Apply only after checking pole locations — oscillating signals break it.

**Q14:** What is the long-division method for inverse Z?
**A:** Perform polynomial long division of $X(z)$ as a ratio in $z^{-1}$ to get a power series $x[0]+x[1]z^{-1}+x[2]z^{-2}+\cdots$. The coefficients are the sample values.
*Pitfall:* Only practical for the first few samples; direction depends on whether you divide in powers of $z^{-1}$ (causal) or $z$ (anti-causal).

**Q15:** How do you evaluate the residue at a simple pole $p$?
**A:** With $X(z)$ in the form $\sum\dfrac{A_k}{1-p_k z^{-1}}$: $A_k = (1-p_k z^{-1})X(z)\big|_{z=p_k}$.
*Pitfall:* Compute in $z^{-1}$-form; if you use $z$-form you'll get residues with an extra factor of $z$.

**Q16:** What does a $z^{-1}$ block mean in a DSP block diagram?
**A:** A unit delay (one-sample memory element). Multiplying by $z^{-1}$ in the Z-domain corresponds to delaying by one sample in time.
*Pitfall:* $z^{-1}$ is cheap in hardware; it's the fundamental building block of FIR and IIR filters.

---

## Lecture 21 — System Analysis via Unilateral Z

**Q1:** How do you derive $H(z)$ from a difference equation?
**A:** Take the Z-transform with **zero** ICs, substitute $y[n-k]\to z^{-k}Y(z)$ and $x[n-k]\to z^{-k}X(z)$, solve for $Y(z)/X(z)$.
*Pitfall:* Must use zero ICs for the transfer function. Nonzero ICs require the unilateral version.

**Q2:** Given $y[n] - 0.5y[n-1] = x[n]$, what is $H(z)$?
**A:** $H(z) = \dfrac{Y(z)}{X(z)} = \dfrac{1}{1-0.5z^{-1}}$. One pole at $z=0.5$, inside unit circle $\Rightarrow$ causal + stable.
*Pitfall:* $|0.5|<1$ means stable; magnitude, not sign, is what matters.

**Q3:** State the Golden Rule for DT causal LTI stability.
**A:** A causal LTI system is BIBO stable iff all poles of $H(z)$ are strictly inside the unit circle, $|p_i|<1$ for all $i$.
*Pitfall:* Poles *on* the unit circle give only marginal stability — not BIBO stable.

**Q4:** What does causality imply about the ROC of $H(z)$?
**A:** The ROC is the exterior of a circle: $|z|>|p_{\max}|$, extending to $\infty$. Rational $H(z)$ with $M\le N$.
*Pitfall:* Causality is the ROC condition; stability is a separate ROC-includes-unit-circle condition.

**Q5:** Define the unilateral Z-transform.
**A:** $\mathcal{X}(z) = \displaystyle\sum_{n=0}^{\infty} x[n]z^{-n}$. Only $n\ge 0$ samples contribute.
*Pitfall:* Unilateral ignores $n<0$; ICs enter through the shift rules, not through the sum.

**Q6:** Unilateral Z shift rule for $x[n-1]$?
**A:** $x[n-1]\leftrightarrow z^{-1}X(z) + x[-1]$. Note the **plus** sign.
*Pitfall:* Opposite sign from unilateral Laplace differentiation (which uses minus). Sign errors are common.

**Q7:** Unilateral Z shift rule for $x[n-2]$?
**A:** $x[n-2]\leftrightarrow z^{-2}X(z) + x[-1]z^{-1} + x[-2]$.
*Pitfall:* The order of the IC terms matters: $x[-1]$ multiplies $z^{-1}$, $x[-2]$ stands alone.

**Q8:** How do you compute the step response of an LTI system in the Z-domain?
**A:** $Y_{\text{step}}(z) = H(z)U(z) = H(z)\cdot\dfrac{1}{1-z^{-1}}$, then inverse Z-transform.
*Pitfall:* Step response has a pole at $z=1$ added to the system poles; FVT applies only if the system is otherwise stable.

**Q9:** ZSR vs ZIR decomposition in DT?
**A:** Total $Y = Y_{\text{ZSR}} + Y_{\text{ZIR}}$. ZSR uses $H(z)X(z)$ with zero ICs. ZIR uses nonzero ICs with $X(z)=0$; it consists of natural modes.
*Pitfall:* Same decomposition idea as CT unilateral Laplace.

**Q10:** What are natural modes of a DT system?
**A:** The terms $p_k^n$ coming from poles $p_k$ of $H(z)$ — exponentially growing/decaying/oscillating sequences.
*Pitfall:* Repeated poles give $n p_k^n$, $n^2 p_k^n$, etc.

**Q11:** What's the DT analog of an $RC$ time constant?
**A:** For a pole at $p$ (real, $0<p<1$), the "time constant" is $-1/\ln|p|$ samples. Smaller $|p|\Rightarrow$ faster decay.
*Pitfall:* Only meaningful for $|p|<1$; on/outside the unit circle there is no decay.

**Q12:** Can an FIR filter be unstable?
**A:** No — an FIR filter has only poles at $z=0$ (and/or $z=\infty$), always inside/outside relative to the unit circle in a way that keeps it BIBO stable. FIR filters are always stable.
*Pitfall:* FIR stability is free; design effort goes into the zeros (frequency response).

**Q13:** What's the pole-zero condition for a real-valued impulse response?
**A:** Poles and zeros must come in complex-conjugate pairs.
*Pitfall:* Same rule as CT systems; symmetric pole-zero plot $\Leftrightarrow$ real coefficients.

**Q14:** How do you find the steady-state sinusoidal response of a stable DT system?
**A:** Evaluate $H(e^{j\omega_0})$ — that complex value gives both magnitude and phase of the response at frequency $\omega_0$.
*Pitfall:* Valid only if the system is stable (unit circle $\subset$ ROC); otherwise no steady state exists.

**Q15:** If $y[n]+0.9y[n-1]=x[n]$ with $y[-1]=2$, $x[n]=0$, what is $y[n]$ (ZIR)?
**A:** Applying unilateral Z: $Y(z)+0.9(z^{-1}Y(z)+y[-1])=0$, so $Y(z)(1+0.9z^{-1}) = -1.8$, giving $Y(z) = \dfrac{-1.8}{1+0.9z^{-1}}$ and $y[n] = -1.8(-0.9)^n u[n]$.
*Pitfall:* The IC term enters with a $+$ on the LHS via the unilateral shift rule, producing a $-1.8$ when moved to the RHS.

**Q16:** Where do open-loop and closed-loop poles differ in a DT feedback system?
**A:** Open-loop poles are the poles of $G(z)H(z)$; closed-loop poles are roots of $1+G(z)H(z)=0$.
*Pitfall:* Feedback can move poles into or out of the unit circle — it does not automatically stabilize.

---

## Lecture 22 — Sampling

**Q1:** State the (Shannon) sampling theorem.
**A:** A band-limited signal with $X(j\omega)=0$ for $|\omega|>\omega_M$ can be perfectly reconstructed from samples spaced $T$ apart, provided $\omega_s = 2\pi/T > 2\omega_M$ (strict inequality).
*Pitfall:* $\omega_s = 2\omega_M$ is **not** sufficient in general.

**Q2:** Define the Nyquist rate.
**A:** Twice the highest frequency: $\omega_{\text{Nyquist}} = 2\omega_M$ (rad/s) or $f_{\text{Nyquist}} = 2f_M$ (Hz). Minimum sampling rate for perfect reconstruction.
*Pitfall:* "Nyquist rate" is a property of the *signal*; "Nyquist frequency" ($\omega_s/2$) is a property of the *sampler*.

**Q3:** What is the impulse train $p(t)$ and its role in sampling?
**A:** $p(t)=\sum_n\delta(t-nT)$ with $\omega_s=2\pi/T$. Sampled signal $x_p(t) = x(t)p(t)= \sum_n x(nT)\delta(t-nT)$.
*Pitfall:* Multiplication in time $\Rightarrow$ convolution in frequency; this creates the spectral replicas.

**Q4:** What is the frequency-domain relation for impulse-train sampling?
**A:** $X_p(j\omega) = \dfrac{1}{T}\displaystyle\sum_{k=-\infty}^{\infty} X(j(\omega-k\omega_s))$ — spectrum replicated at every multiple of $\omega_s$, scaled by $1/T$.
*Pitfall:* The scaling is $1/T$; when reconstructing, the LPF must have gain $T$ to cancel it.

**Q5:** Describe ideal reconstruction.
**A:** Pass $x_p(t)$ through an ideal LPF with gain $T$ and cutoff $\omega_c$ between $\omega_M$ and $\omega_s-\omega_M$. Result: $x(t)$ reconstructed exactly (no aliasing).
*Pitfall:* LPF gain is $T$, not $1$. Forgetting the gain gives output scaled by $1/T$.

**Q6:** Write the band-limited (sinc) interpolation formula.
**A:** $x(t) = \displaystyle\sum_{n=-\infty}^{\infty} x(nT)\,\text{sinc}\!\left(\dfrac{t-nT}{T}\right)$, where $\text{sinc}(u)=\sin(\pi u)/(\pi u)$.
*Pitfall:* Sinc kernels have infinite support — practical reconstruction uses truncated sincs or other kernels.

**Q7:** What is aliasing and when does it occur?
**A:** When $\omega_s<2\omega_M$, spectral replicas overlap and fold back into the baseband, producing false low-frequency content. Aliased frequency: $f_a = |f_s - f_0|$ (nearest replica).
*Pitfall:* Aliasing is **irreversible** — cannot be removed after sampling. Use an anti-aliasing LPF before sampling.

**Q8:** What is the relation between DT and CT frequencies?
**A:** $\Omega = \omega T$ (radians/sample $=$ radians/sec $\times$ seconds/sample). The DT band $[-\pi,\pi]$ corresponds to CT $[-\pi/T,\pi/T]=[-\omega_s/2,\omega_s/2]$.
*Pitfall:* Mixing up radians-per-sample and radians-per-second is a perennial unit error.

**Q9:** What is a zero-order hold (ZOH)?
**A:** Practical reconstruction that holds each sample constant for one period: impulse response $h_{\text{ZOH}}(t)=1$ for $0\le t<T$, 0 else. Frequency response $H(j\omega) = T\,\text{sinc}(\omega T/2\pi)e^{-j\omega T/2}$.
*Pitfall:* ZOH introduces amplitude droop and a half-sample delay; often compensated by an inverse-sinc filter.

**Q10:** What is a first-order hold?
**A:** Linear interpolation between adjacent samples; triangular impulse response of length $2T$. Smoother than ZOH but still imperfect.
*Pitfall:* Neither ZOH nor FOH is ideal — they cannot perfectly reconstruct a generic band-limited signal.

**Q11:** Nyquist rate of $x(t-a)$ vs $x(2t)$ vs $x^2(t)$?
**A:** $x(t-a)$: same rate. $x(2t)$: doubled rate (bandwidth doubles under time compression). $x^2(t)$: doubled rate (self-convolution in frequency doubles the support).
*Pitfall:* Squaring/multiplying signals doubles bandwidth — always account for it before sampling.

**Q12:** What happens if you sample a $1$ kHz cosine at $1.5$ kHz?
**A:** $f_s/2 = 750$ Hz, so the $1$ kHz tone aliases to $|1000-1500|=500$ Hz. The sampled output looks like a $500$ Hz cosine.
*Pitfall:* Undersampling real-world signals produces "wagon-wheel" and moiré effects.

**Q13:** Why does the reconstruction LPF need gain $T$?
**A:** Because the sampling multiplication produces an extra $1/T$ factor in each spectral replica; the LPF gain $T$ cancels this to recover the original amplitude.
*Pitfall:* Units check: $T$ has dimensions of time, balancing the $1/T$ from the periodic impulse train.

**Q14:** Describe DSP of continuous-time signals (block chain).
**A:** Chain: CT anti-aliasing LPF $\to$ C/D converter $\to$ DT system $H(e^{j\Omega})\to$ D/C converter (reconstruction LPF). Effective CT transfer: $H_{\text{eff}}(j\omega) = H(e^{j\omega T})$ for $|\omega|<\pi/T$.
*Pitfall:* The "effective" CT transfer only holds within $|\omega|<\omega_s/2$.

**Q15:** Why is the anti-aliasing filter applied *before* sampling?
**A:** Because aliasing is irreversible — once high-frequency content folds into the baseband, you cannot tell it apart from true baseband content. Filtering after sampling cannot fix it.
*Pitfall:* Trying to remove aliasing afterward only removes (already corrupted) baseband content.

**Q16:** State the sampling theorem in Hz form.
**A:** $f_s > 2f_M$, i.e., $T < \dfrac{1}{2f_M}$. Equivalently, sample period less than half of the shortest period in the signal.
*Pitfall:* Watch units: $\omega$ uses rad/s, $f$ uses Hz; they differ by $2\pi$.

---

## Lecture 23 — Linear Feedback Systems

**Q1:** Write the closed-loop transfer function for a unity-feedback system with forward gain $H(s)$.
**A:** $Q(s) = \dfrac{Y(s)}{X(s)} = \dfrac{H(s)}{1+H(s)}$.
*Pitfall:* This is the **unity** case. For feedback gain $F(s)$ use $H/(1+HF)$.

**Q2:** Closed-loop transfer function for non-unity negative feedback ($G$ forward, $H$ feedback)?
**A:** $Q(s) = \dfrac{G(s)}{1 + G(s)H(s)}$.
*Pitfall:* If feedback is *positive*, use $1-GH$; sign convention is critical.

**Q3:** Where are the closed-loop poles?
**A:** At the roots of the characteristic equation $1 + G(s)H(s) = 0$, equivalently $G(s)H(s) = -1$.
*Pitfall:* Closed-loop poles differ from open-loop poles (of $GH$); feedback relocates them.

**Q4:** What is the sensitivity function and why do we care?
**A:** $S(s) = \dfrac{1}{1+L(s)}$, where $L = GH$ is the loop gain. High loop gain $\Rightarrow$ low sensitivity to plant variation and disturbances.
*Pitfall:* Very high gain also amplifies noise and can destabilize — always a trade-off.

**Q5:** State the Nyquist criterion (simplified version for open-loop stable systems).
**A:** The closed-loop is stable iff the Nyquist plot of $L(j\omega) = G(j\omega)H(j\omega)$ does **not** encircle the point $-1/K$ (or $-1$ if $K$ is absorbed into $L$).
*Pitfall:* The general form counts encirclements of $-1$ and relates them to RHP open-loop poles; the simplified version assumes open-loop stability.

**Q6:** Define gain margin (GM).
**A:** At $\omega_1$ where $\angle L(j\omega_1) = -180°$, GM is how far $|L(j\omega_1)|$ is below $0$ dB: $\text{GM} = -20\log_{10}|L(j\omega_1)|$ dB.
*Pitfall:* Positive GM $\Rightarrow$ stable in this respect. A first-order $L(s)$ never reaches $-180°$, so its GM is infinite.

**Q7:** Define phase margin (PM).
**A:** At $\omega_2$ (gain crossover) where $|L(j\omega_2)|=1$ ($0$ dB), $\text{PM} = 180° + \angle L(j\omega_2)$.
*Pitfall:* Positive PM $\Rightarrow$ stable in this respect. Typical target: $45°$–$60°$.

**Q8:** When is a closed-loop system stable from Bode plots alone?
**A:** Both GM and PM must be positive (assuming open-loop stable and $L$ has no multiple crossovers).
*Pitfall:* Multiple crossovers or conditional stability require full Nyquist analysis.

**Q9:** Can feedback stabilize an unstable plant?
**A:** Yes — feedback relocates poles; sufficient loop gain can push RHP poles into the LHP. But excessive gain can do the opposite.
*Pitfall:* "More feedback is always better" is false — stability is nonmonotonic in gain.

**Q10:** What is the maximum time delay a system with phase margin PM can tolerate at crossover $\omega_2$?
**A:** $\tau_{\max} = \dfrac{\text{PM (in radians)}}{\omega_2}$.
*Pitfall:* Convert PM from degrees to radians ($\times\pi/180$) before dividing.

**Q11:** Cascade and parallel block-diagram rules?
**A:** Cascade: $H_1 H_2$. Parallel: $H_1 + H_2$. Used to simplify block diagrams to a single transfer function.
*Pitfall:* Loading effects may invalidate cascade in physical systems; always check block independence.

**Q12:** What is the loop gain and why is it important?
**A:** $L(s) = G(s)H(s)$ — the product of all gains around the loop. Its magnitude determines sensitivity, bandwidth, and stability margins; its characteristic equation $1+L=0$ gives closed-loop poles.
*Pitfall:* Define the loop consistently; sign conventions and break points matter.

**Q13:** How do you sketch the Nyquist plot?
**A:** Plot $L(j\omega)$ in the complex plane for $\omega:0\to\infty$, reflect for $\omega:-\infty\to 0$, close with a large semicircle at $\infty$. Count encirclements of $-1$.
*Pitfall:* Poles on the $j\omega$-axis require small indentations; forgetting them leads to wrong encirclement counts.

**Q14:** What's the effect of increasing forward gain $K$ on the Nyquist plot?
**A:** Scales the plot radially by $K$. Equivalently, look at encirclements of $-1/K$ instead of $-1$.
*Pitfall:* As $K$ grows, the plot may eventually enclose $-1$, destabilizing the closed loop.

**Q15:** What's the open-loop vs closed-loop distinction?
**A:** Open loop has no feedback ($Y = GX$). Closed loop uses measured $Y$ to adjust the input: $Y = GX - GHY$, giving $Y = GX/(1+GH)$.
*Pitfall:* Open-loop control relies on accurate plant knowledge; closed-loop can tolerate uncertainty.

**Q16:** For a stable minimum-phase $L(s)$, how does Bode stability relate to slope at crossover?
**A:** Rule of thumb: if $|L|$ crosses $0$ dB with slope $\approx -20$ dB/dec, PM is usually adequate; $-40$ dB/dec often signals marginal or unstable behavior.
*Pitfall:* This is a heuristic — always confirm with exact GM/PM or Nyquist for critical designs.

**Q17:** What role does feedback play in disturbance rejection?
**A:** With loop gain $L$, an output-referred disturbance is attenuated by $1/(1+L)$. High $L$ at disturbance frequencies $\Rightarrow$ good rejection.
*Pitfall:* Rejection is frequency-dependent; design $L(j\omega)$ to have high magnitude where the disturbance lives.

---

*Prepared for CEC 315 Exam 3 — Spring 2026. Drill until the questions feel boring, then take the exam.*
