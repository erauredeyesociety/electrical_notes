# CEC 315 — Exam 3 Pitfalls and Traps (Lectures 16–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Purpose:** Consolidated list of common mistakes, sign errors, and conceptual traps for Exam 3. For each pitfall: the mistake, *why* it happens, the correct approach, and a worked wrong-vs-right example.

---

## 1. Laplace Transform and ROC (Lecture 16)

### 1.1 Omitting the ROC entirely

- **Mistake:** Writing $X(s) = \dfrac{1}{s+3}$ and calling it "the Laplace transform" of a signal.
- **Why it happens:** Tables list only the algebraic expression, so students treat $X(s)$ and $x(t)$ as a one-to-one pair.
- **Correct approach:** The Laplace transform is the pair $(X(s),\ \text{ROC})$. Two different signals can share the same algebraic $X(s)$.
- **Example.**
  - *Wrong:* "$X(s) = \dfrac{1}{s+3}$, so $x(t) = e^{-3t}u(t)$."
  - *Right:* With ROC $\operatorname{Re}\{s\} > -3$, $x(t) = e^{-3t}u(t)$. With ROC $\operatorname{Re}\{s\} < -3$, $x(t) = -e^{-3t}u(-t)$. The algebra is identical; the ROC decides the signal.

### 1.2 Getting the ROC direction backward

- **Mistake:** Writing "ROC $\operatorname{Re}\{s\} < \sigma_{\max}$" for a right-sided signal.
- **Why it happens:** Students memorize "ROC is bounded by the rightmost pole" without attaching a direction.
- **Correct approach:** Right-sided $\Rightarrow$ ROC is *right of* the rightmost pole. Left-sided $\Rightarrow$ ROC is *left of* the leftmost pole. The ROC points away from where the signal grows.
- **Example.** $x(t) = 3e^{-2t}u(t) - 2e^{-5t}u(t)$, $X(s) = \dfrac{s+11}{(s+2)(s+5)}$.
  - *Wrong:* "Poles at $-2, -5$, so ROC is $\operatorname{Re}\{s\} < -5$."
  - *Right:* Both terms are right-sided, so ROC is right of the rightmost pole: $\operatorname{Re}\{s\} > -2$.

### 1.3 Assuming a pole can lie in the ROC

- **Mistake:** Listing a pole location as part of the ROC, e.g., "ROC $\operatorname{Re}\{s\} \ge -3$."
- **Why it happens:** "$\ge$" feels like a harmless boundary convention.
- **Correct approach:** $X(s) \to \infty$ at a pole, so the integral cannot converge there. ROC inequalities are always *strict* at poles.
- **Example.** $u(t) \leftrightarrow 1/s$, pole at $s=0$.
  - *Wrong:* "ROC $\operatorname{Re}\{s\} \ge 0$; so $u(t)$ has a Fourier transform from $s=j\omega$."
  - *Right:* ROC $\operatorname{Re}\{s\} > 0$. The $j\omega$-axis is *not* in the (open) ROC, so you cannot obtain $U(j\omega)$ by setting $s = j\omega$. The actual DTFT has an impulse at $\omega = 0$ that this substitution misses.

### 1.4 ROC of a sum — assuming it's always the intersection

- **Mistake:** "ROC of $X_1 + X_2$ = ROC$_1$ $\cap$ ROC$_2$, full stop."
- **Why it happens:** The linearity rule is usually stated this way.
- **Correct approach:** The ROC of a sum *contains* the intersection, but can be *larger* due to pole-zero cancellation. Always verify after simplification.
- **Example.** $x(t) = e^{-t}u(t) - e^{-t}u(t) = 0$.
  - *Wrong:* "ROC is $\operatorname{Re}\{s\} > -1 \cap \operatorname{Re}\{s\} > -1 = \operatorname{Re}\{s\} > -1$."
  - *Right:* The sum is identically zero, whose Laplace transform is $0$ with ROC the entire $s$-plane. Cancellation removed the pole at $s=-1$.

### 1.5 Treating Laplace as "Fourier with $\omega \to s$"

- **Mistake:** Claiming $X(j\omega) = X(s)\big|_{s=j\omega}$ without checking.
- **Why it happens:** The substitution usually works for damped, causal signals.
- **Correct approach:** The substitution is valid *only* when the $j\omega$-axis is in the ROC.
- **Example.** $x(t) = e^{2t}u(t) \leftrightarrow \dfrac{1}{s-2}$, ROC $\operatorname{Re}\{s\} > 2$.
  - *Wrong:* "$X(j\omega) = \dfrac{1}{j\omega - 2}$."
  - *Right:* The $j\omega$-axis is not in the ROC. $e^{2t}u(t)$ grows without bound, so the Fourier transform does not exist. The substitution is invalid.

### 1.6 Confusing finite-duration ROC with empty ROC

- **Mistake:** Thinking a finite-duration signal has a "trivial" or restricted ROC.
- **Why it happens:** Students pattern-match "exponential $\Rightarrow$ half-plane ROC."
- **Correct approach:** A finite-duration (and integrable) signal has ROC = *entire* $s$-plane (possibly minus $s=\pm\infty$). The integral is a finite sum and converges everywhere.
- **Example.** $x(t) = \delta(t) + \delta(t-2)$.
  - *Wrong:* "ROC $\operatorname{Re}\{s\} > 0$ from the $u(t)$-like behavior."
  - *Right:* $X(s) = 1 + e^{-2s}$, ROC = all $s$. No poles, no convergence issues.

---

## 2. Inverse Laplace via Partial Fractions (Lecture 17)

### 2.1 Assigning direction by the sign of the pole, not the ROC

- **Mistake:** "Pole at $s = -1$ is in the LHP, so the term is right-sided; pole at $s=+3$ is in the RHP, so that term is left-sided."
- **Why it happens:** Causal examples reinforce the pattern "LHP pole = stable = right-sided."
- **Correct approach:** The ROC alone determines direction. A pole at $s=-1$ can still be left-sided if the ROC lies to its left.
- **Example.** $X(s) = \dfrac{5s+17}{(s+1)(s-3)}$ with ROC $-1 < \operatorname{Re}\{s\} < 3$.
  - *Wrong:* $x(t) = -3e^{-t}u(t) + 8e^{3t}u(t)$ (wrong sign and wrong direction on the second term).
  - *Right:* ROC is a strip, so $s=-1$ is a right-sided pole and $s=3$ is a left-sided pole: $x(t) = -3e^{-t}u(t) - 8e^{3t}u(-t)$.

### 2.2 Missing terms in repeated-pole expansions

- **Mistake:** For $(s+1)^3$ writing only $\dfrac{A}{(s+1)^3}$.
- **Why it happens:** The cover-up method at the highest power gives one coefficient cleanly, and students stop there.
- **Correct approach:** A pole of order $n$ requires *all* $n$ terms: $\dfrac{B_1}{s+1} + \dfrac{B_2}{(s+1)^2} + \dfrac{B_3}{(s+1)^3}$.
- **Example.** $X(s) = \dfrac{4s+5}{(s+1)^2(s+3)}$, ROC $\operatorname{Re}\{s\} > -1$.
  - *Wrong:* $\dfrac{A}{(s+1)^2} + \dfrac{B}{s+3}$, leading to an incorrect $x(t)$ without a $1/(s+1)$ term.
  - *Right:* $\dfrac{B_1}{s+1} + \dfrac{B_2}{(s+1)^2} + \dfrac{C}{s+3}$, giving $x(t) = \tfrac{7}{4}e^{-t}u(t) + \tfrac{1}{2}t e^{-t}u(t) - \tfrac{7}{4}e^{-3t}u(t)$.

### 2.3 Splitting complex conjugate poles and inverting with complex exponentials

- **Mistake:** Writing $\dfrac{A}{s-p} + \dfrac{A^*}{s-p^*}$ and inverting each to $A e^{pt} + A^* e^{p^*t}$.
- **Why it happens:** It looks like the distinct-real-poles case.
- **Correct approach:** Complete the square in the denominator, then use the $e^{-at}\cos$/$\sin$ pairs. Keeps everything real-valued.
- **Example.** $X(s) = \dfrac{2s}{s^2 + 4s + 13}$, ROC $\operatorname{Re}\{s\} > -2$.
  - *Wrong:* Split into $\dfrac{A}{s+2-3j} + \dfrac{A^*}{s+2+3j}$, invert, then fight with complex arithmetic.
  - *Right:* $s^2+4s+13 = (s+2)^2 + 3^2$. Write as $\dfrac{2(s+2)}{(s+2)^2+3^2} - \dfrac{4}{(s+2)^2+3^2}$. Invert to $x(t) = [2e^{-2t}\cos(3t) - \tfrac{4}{3}e^{-2t}\sin(3t)]u(t)$.

### 2.4 Using cover-up on a repeated pole at the wrong order

- **Mistake:** For $\dfrac{N(s)}{(s+1)^2(s+3)}$, computing $B_1$ by cover-up as $(s+1)\cdot X(s)\big|_{s=-1}$.
- **Why it happens:** Cover-up works cleanly for distinct poles; students apply the same shortcut.
- **Correct approach:** Cover-up gives the coefficient of the *highest*-order term, $B_n$. For lower orders, use $B_k = \dfrac{1}{(n-k)!}\dfrac{d^{n-k}}{ds^{n-k}}\big[(s-p)^n X(s)\big]\big|_{s=p}$.
- **Example.** $X(s) = \dfrac{1}{(s+1)^2(s+3)}$.
  - *Wrong:* $B_1 = (s+1)X(s)\big|_{s=-1}$ — this is undefined because a factor of $(s+1)$ remains in the denominator.
  - *Right:* $B_2 = (s+1)^2 X(s)\big|_{s=-1} = \tfrac{1}{2}$, then $B_1 = \dfrac{d}{ds}\big[(s+1)^2 X(s)\big]\big|_{s=-1} = -\tfrac{1}{4}$.

### 2.5 Applying the Final-Value Theorem when it doesn't apply

- **Mistake:** Plugging into $\lim_{s\to 0} sX(s)$ without checking pole locations.
- **Why it happens:** The formula is short and easy to memorize.
- **Correct approach:** The FVT is valid only if $sX(s)$ has all poles strictly in the open LHP. If $X(s)$ has poles on the $j\omega$-axis (other than a simple one at $s=0$) or in the RHP, the limit exists but is meaningless.
- **Example.** $X(s) = \dfrac{1}{s^2+1}$ (undamped oscillator).
  - *Wrong:* $x(\infty) = \lim_{s\to 0}\dfrac{s}{s^2+1} = 0$, so "the output settles to zero."
  - *Right:* $x(t) = \sin(t)u(t)$, which oscillates forever — no limit exists. The poles at $\pm j$ violate the FVT hypothesis, so the theorem does not apply.

---

## 3. Unilateral Laplace System Analysis (Lecture 18)

### 3.1 Using the bilateral differentiation rule when ICs are nonzero

- **Mistake:** Transforming $y' \to sY$ in a problem with $y(0^-) \ne 0$.
- **Why it happens:** The bilateral property is the one students learn first.
- **Correct approach:** With initial conditions, use the *unilateral* rule: $\mathcal{L}_u\{y'\} = sY(s) - y(0^-)$. Second derivative: $s^2 Y(s) - s y(0^-) - y'(0^-)$.
- **Example.** $y'(t) + 3y(t) = 0$ with $y(0^-) = 5$.
  - *Wrong:* $sY + 3Y = 0 \Rightarrow Y = 0 \Rightarrow y(t)=0$, contradicting the IC.
  - *Right:* $[sY - 5] + 3Y = 0 \Rightarrow Y = \dfrac{5}{s+3} \Rightarrow y(t) = 5e^{-3t}u(t)$.

### 3.2 Sign error on the IC term

- **Mistake:** Writing $sX(s) + x(0^-)$ or forgetting the sign altogether.
- **Why it happens:** Students guess from symmetry without deriving; the plus sign "feels" natural.
- **Correct approach:** Memorize: $\mathcal{L}_u\{y'\} = sY(s) - y(0^-)$. The sign is *minus* in Laplace (but *plus* in unilateral Z — see §6.1). For $y''$: $s^2 Y - s y(0^-) - y'(0^-)$, both ICs subtracted.
- **Example.** $y'' + 5y' + 6y = 2u(t)$, $y(0^-)=1$, $y'(0^-)=0$.
  - *Wrong:* $s^2 Y + s(1) + (0) + 5[sY + 1] + 6Y = 2/s$.
  - *Right:* $[s^2 Y - s(1) - 0] + 5[sY - 1] + 6Y = 2/s$, leading to $y(t) = [\tfrac{1}{3} + 2e^{-2t} - \tfrac{4}{3}e^{-3t}]u(t)$.

### 3.3 Using $y(0^+)$ instead of $y(0^-)$

- **Mistake:** Plugging the post-switching value into the unilateral differentiation rule.
- **Why it happens:** In physical circuit problems, students often compute $y(0^+)$ from continuity arguments and jump to use it.
- **Correct approach:** The unilateral Laplace transform integrates from $0^-$, so ICs are at $0^-$. If the input has a discontinuity at $t=0$ (a step or impulse), $y(0^+)$ can differ from $y(0^-)$ — use $y(0^-)$.
- **Example.** RC circuit with $v_C(0^-) = 2$ V driven by a step input.
  - *Wrong:* Use $v_C(0^+) = 2$ V after arguing continuity, then immediately apply the unilateral rule with that value at $0^-$.
  - *Right:* Use $v_C(0^-) = 2$ V directly. The IC sits just *before* the step arrives.

### 3.4 Confusing ZSR and ZIR

- **Mistake:** Computing $Y(s) = H(s)X(s)$ and calling that the total response when ICs are nonzero.
- **Why it happens:** The convolution property is the most-used formula, and it equals the ZSR.
- **Correct approach:** Total = ZSR + ZIR. $Y_\text{ZS}(s) = H(s)X(s)$ (response with zero ICs). $Y_\text{ZI}(s)$ is the response to ICs with input zeroed out. Add them.
- **Example.** $y'' + 5y' + 6y = 2u(t)$, $y(0^-)=1, y'(0^-)=0$.
  - *Wrong:* $Y(s) = H(s)\cdot \dfrac{2}{s} = \dfrac{2}{s(s+2)(s+3)}$, missing the IC response.
  - *Right:* $Y_\text{ZS} = \dfrac{2}{s(s+2)(s+3)}$; $Y_\text{ZI} = \dfrac{s+5}{(s+2)(s+3)}$. Sum: $\dfrac{s^2+5s+2}{s(s+2)(s+3)}$.

### 3.5 Concluding instability from RHP zeros

- **Mistake:** "Zero at $s=+2$, so the system is unstable."
- **Why it happens:** Students conflate zero locations with pole locations.
- **Correct approach:** Stability depends only on *poles*. RHP zeros produce nonminimum-phase behavior (inverse response, phase lag) but do *not* cause instability.
- **Example.** $H(s) = \dfrac{s-2}{(s+1)(s+3)}$.
  - *Wrong:* "RHP zero at $s=2$ $\Rightarrow$ unstable."
  - *Right:* Both poles in LHP $\Rightarrow$ stable. The RHP zero only affects transient shape (initial undershoot).

### 3.6 Coupling causality and stability into one criterion

- **Mistake:** "Stable iff all poles in LHP" applied to a non-causal system.
- **Why it happens:** The "Golden Rule" is drilled for causal systems and students use it universally.
- **Correct approach:** The rule "causal + stable $\Leftrightarrow$ all poles in LHP" *assumes* causality. For non-causal systems, stability requires the $j\omega$-axis to be in the ROC, and the ROC need not be a right half-plane.
- **Example.** $H(s) = \dfrac{1}{s-2}$ with ROC $\operatorname{Re}\{s\} < 2$.
  - *Wrong:* "RHP pole $\Rightarrow$ unstable."
  - *Right:* The $j\omega$-axis lies in the ROC, so the system is BIBO stable — it is simply non-causal ($h(t) = -e^{2t}u(-t)$, anti-causal and decaying into the past).

---

## 4. Z-Transform and ROC (Lecture 19)

### 4.1 Omitting the ROC

- **Mistake:** Writing $X(z) = \dfrac{1}{1 - 0.5z^{-1}}$ as a complete answer.
- **Why it happens:** Same reason as Laplace — tables hide the ROC.
- **Correct approach:** Always pair $X(z)$ with its ROC.
- **Example.** $X(z) = \dfrac{1}{1-0.5z^{-1}}$.
  - *Wrong:* "$x[n] = (0.5)^n u[n]$, end of story."
  - *Right:* With ROC $|z|>0.5$, $x[n] = (0.5)^n u[n]$. With ROC $|z|<0.5$, $x[n] = -(0.5)^n u[-n-1]$.

### 4.2 Confusing "outside" with "inside" for left-sided signals

- **Mistake:** "Left-sided $\Rightarrow$ ROC outside the leftmost pole."
- **Why it happens:** Students carry over the Laplace "left/right" vocabulary literally, but $z$-plane ROCs are annular.
- **Correct approach:** Right-sided $\Rightarrow$ ROC *outside* the outermost pole circle. Left-sided $\Rightarrow$ ROC *inside* the innermost pole circle. Think of radius instead of $\operatorname{Re}\{\cdot\}$.
- **Example.** $x[n] = -3^n u[-n-1]$, pole at $z=3$.
  - *Wrong:* "Left-sided $\Rightarrow$ ROC $|z|>3$."
  - *Right:* ROC $|z|<3$. The unit circle lies in the ROC, so the DTFT exists.

### 4.3 Misidentifying the pole in $1/(1-az^{-1})$

- **Mistake:** Reading the pole as $z=1/a$ (because $z^{-1}=a$).
- **Why it happens:** Students confuse "where the denominator of the $z^{-1}$ expression equals zero" with "where $X(z)$ actually blows up."
- **Correct approach:** Multiply top and bottom by $z$: $\dfrac{1}{1-az^{-1}} = \dfrac{z}{z-a}$. The pole is at $z=a$; there is also a zero at $z=0$.
- **Example.** $X(z) = \dfrac{1}{1 - 0.4 z^{-1}}$.
  - *Wrong:* "Pole at $z = 1/0.4 = 2.5$, so ROC $|z|>2.5$."
  - *Right:* Pole at $z=0.4$, zero at $z=0$, ROC $|z|>0.4$.

### 4.4 Forgetting the unit circle replaces the $j\omega$-axis

- **Mistake:** Checking DTFT existence by looking at whether poles are in the left half-plane.
- **Why it happens:** CT habits bleed into DT analysis.
- **Correct approach:** DTFT exists iff the *unit circle* is in the ROC. Equivalently (for causal systems): all poles strictly inside $|z|=1$.
- **Example.** $x[n] = 2^n u[n]$, $X(z) = \dfrac{1}{1-2z^{-1}}$, ROC $|z|>2$.
  - *Wrong:* "Pole at $z=2$ is on positive real axis, not in LHP, so unstable." (Correct conclusion, wrong reason.)
  - *Right:* Unit circle $|z|=1$ is not in the ROC $|z|>2$, so the DTFT does not exist.

### 4.5 ROC of finite-duration signals

- **Mistake:** Writing a restrictive ROC like $|z|>0$ for a two-sided finite-duration sequence.
- **Why it happens:** Pattern-matching to the $u[n]$ case.
- **Correct approach:** A finite-length sequence has ROC = *entire* $z$-plane, possibly minus $z=0$ (if it has samples at $n>0$) and/or $z=\infty$ (if it has samples at $n<0$).
- **Example.** $x[n] = \{2, -1, 3, 0, 4\}$ for $n=0,\ldots,4$.
  - *Wrong:* "ROC $|z|>1$ because nonzero for $n\ge 0$."
  - *Right:* $X(z) = 2 - z^{-1} + 3z^{-2} + 4z^{-4}$, ROC = all $z \ne 0$ (it's a finite polynomial in $z^{-1}$, only $z=0$ causes trouble).

### 4.6 Wrong geometric-series convergence condition

- **Mistake:** Checking "$az^{-1} < 1$" instead of "$|az^{-1}| < 1$" when deriving the closed form.
- **Why it happens:** Real-variable intuition about "less than one."
- **Correct approach:** For complex $w$, $\sum_{n=0}^\infty w^n = \dfrac{1}{1-w}$ converges iff $|w| < 1$. Apply to $w = az^{-1}$: $|az^{-1}|<1 \Leftrightarrow |z| > |a|$.
- **Example.** $x[n] = (-0.8)^n u[n]$.
  - *Wrong:* "$-0.8 z^{-1} < 1$ for all $z > 0$, so ROC $|z|>0$."
  - *Right:* $|-0.8 z^{-1}| < 1 \Leftrightarrow |z|>0.8$. The pole is at $z=-0.8$ (inside the unit circle but on the negative real axis).

---

## 5. Inverse Z-Transform via PFE (Lecture 20)

### 5.1 Doing partial fractions in $z$ instead of $z^{-1}$

- **Mistake:** Treating $X(z)$ as a rational function of $z$ and expanding in $z$-poles.
- **Why it happens:** It feels natural to work in the same variable as Laplace ($s$).
- **Correct approach:** Standard Z-table pairs are stated in $z^{-1}$. Work with $z^{-1}$ as the expansion variable so you can directly match $\dfrac{A}{1-dz^{-1}}$ terms.
- **Example.** $X(z) = \dfrac{z}{(z-0.5)(z-0.25)}$, ROC $|z|>0.5$.
  - *Wrong:* $\dfrac{A}{z-0.5} + \dfrac{B}{z-0.25}$, then struggle to invert each.
  - *Right:* Divide numerator and denominator by $z^2$: $X(z) = \dfrac{z^{-1}}{(1-0.5z^{-1})(1-0.25z^{-1})}$. Or use the "$X(z)/z$ trick": expand $\dfrac{X(z)}{z}$ in $z$-partial fractions, then multiply back by $z$ at the end — this yields a clean $\dfrac{A}{1-dz^{-1}}$ form after simplification.

### 5.2 Wrong direction assignment from the ROC

- **Mistake:** "Pole at $z=0.5$ inside the unit circle $\Rightarrow$ right-sided" (applied blindly).
- **Why it happens:** Causal examples always have this pattern.
- **Correct approach:** For each pole, ask: is the ROC *outside* (right-sided, $d^n u[n]$) or *inside* (left-sided, $-d^n u[-n-1]$) that pole's radius?
- **Example.** $X(z) = \dfrac{1}{(1-2z^{-1})(1-0.5z^{-1})}$, ROC $0.5 < |z| < 2$.
  - *Wrong:* Both poles give right-sided terms, $x[n] = -\tfrac{2}{3}(0.5)^n u[n] + \tfrac{2}{3}\cdot 2^n u[n]$. The $2^n$ term grows and doesn't match the DTFT-existing annular ROC.
  - *Right:* ROC is outside the $0.5$ circle (so that pole is right-sided) but inside the $2$ circle (so that pole is left-sided). $x[n] = -\tfrac{2}{3}(0.5)^n u[n] - \tfrac{2}{3}\cdot 2^n u[-n-1]$.

### 5.3 Forgetting the minus sign on left-sided pairs

- **Mistake:** Writing the left-sided inverse as $a^n u[-n-1]$ instead of $-a^n u[-n-1]$.
- **Why it happens:** The Z-table rows for right- and left-sided signals have *identical algebra*, so students miss the sign.
- **Correct approach:** $\dfrac{1}{1-az^{-1}}$ with ROC $|z|<|a|$ gives $-a^n u[-n-1]$ (note the leading minus).
- **Example.** $X(z) = \dfrac{1}{1-3z^{-1}}$, ROC $|z|<3$.
  - *Wrong:* $x[n] = 3^n u[-n-1]$.
  - *Right:* $x[n] = -3^n u[-n-1]$.

### 5.4 Not doing long division when $X(z)$ is improper

- **Mistake:** Going straight to partial fractions when the numerator degree (in $z^{-1}$) equals or exceeds the denominator.
- **Why it happens:** Skipping a preliminary step that feels unnecessary.
- **Correct approach:** First extract a polynomial in $z^{-1}$ by long division (this inverts to delta functions). Then apply PFE to the proper remainder.
- **Example.** $X(z) = \dfrac{1 + 2z^{-1} + 3z^{-2}}{1 - 0.5 z^{-1}}$ (improper in $z^{-1}$).
  - *Wrong:* Jump to $\dfrac{A}{1-0.5z^{-1}}$ without long division, miss the delta-function content.
  - *Right:* Long division first: $X(z) = -6z^{-1} - 10 + \dfrac{11}{1-0.5z^{-1}}$ (or similar). Invert each piece: delta terms plus a right-sided exponential.

### 5.5 Mixing up $z=1$ and $z=0$ for DC

- **Mistake:** Evaluating "DC" behavior by plugging $z=0$ into $X(z)$.
- **Why it happens:** In Laplace, $s=0$ is DC, and students transfer the habit.
- **Correct approach:** In the $z$-plane, $\omega=0$ corresponds to $z=e^{j0}=1$ (not $z=0$!). $\omega = \pi$ corresponds to $z=-1$. The point $z=0$ is "$\omega=\infty$" — outside the DTFT's scope.
- **Example.** $X(z) = \dfrac{1}{1-0.5z^{-1}}$.
  - *Wrong:* "DC value = $X(0)$, undefined."
  - *Right:* DC value = $X(1) = \dfrac{1}{1-0.5} = 2$.

### 5.6 Applying the Z-domain FVT to non-decaying signals

- **Mistake:** Using $\lim_{z\to 1}(1-z^{-1})X(z)$ when the signal oscillates.
- **Why it happens:** The algebraic limit exists, giving a misleading "answer."
- **Correct approach:** The FVT requires $(1-z^{-1})X(z)$ to have all poles strictly *inside* the unit circle.
- **Example.** $x[n] = \cos(\pi n/2) u[n]$.
  - *Wrong:* "$x[\infty] = \lim_{z\to 1}(1-z^{-1})\cdot \dfrac{z^2}{z^2+1} = 0$."
  - *Right:* $x[n]$ oscillates forever; no limit. The poles of $X(z)$ are on the unit circle at $z=\pm j$, violating the FVT hypothesis.

---

## 6. Unilateral Z System Analysis (Lecture 21)

### 6.1 Sign error on the unilateral shift

- **Mistake:** Writing $\mathcal{Z}_u\{y[n-1]\} = z^{-1}Y(z) - y[-1]$ (minus, by analogy with Laplace).
- **Why it happens:** Laplace uses minus, so students assume Z does too.
- **Correct approach:** Unilateral Z shift: $y[n-1] \leftrightarrow z^{-1}Y(z) + y[-1]$ — **plus**. This is one of the most common Exam 3 sign errors.
- **Example.** $y[n] - 0.6 y[n-1] = 0$, $y[-1]=4$.
  - *Wrong:* $Y - 0.6[z^{-1}Y - 4] = 0 \Rightarrow Y(1 - 0.6z^{-1}) = -2.4 \Rightarrow y[n] = -2.4(0.6)^n u[n]$, giving $y[0] = -2.4$ (wrong).
  - *Right:* $Y - 0.6[z^{-1}Y + 4] = 0 \Rightarrow Y(1-0.6z^{-1}) = 2.4 \Rightarrow y[n] = 2.4(0.6)^n u[n]$, giving $y[0]=2.4$ and $y[1]=1.44 = 0.6\cdot 2.4$ ✓.

### 6.2 Second-shift rule confusion

- **Mistake:** For $y[n-2]$ writing $z^{-2}Y + y[-2]$ (missing the $y[-1]z^{-1}$ term).
- **Why it happens:** Students generalize the first-shift rule with one IC.
- **Correct approach:** $y[n-2] \leftrightarrow z^{-2}Y(z) + y[-1]z^{-1} + y[-2]$. Each past sample contributes a term, scaled by its own delay.
- **Example.** $y[n] - 0.7 y[n-1] + 0.1 y[n-2] = 0$, $y[-1]=1$, $y[-2]=0$.
  - *Wrong:* $Y - 0.7[z^{-1}Y+1] + 0.1[z^{-2}Y+0] = 0$ (missing the $y[-1]z^{-1}$ piece).
  - *Right:* $Y - 0.7[z^{-1}Y+1] + 0.1[z^{-2}Y + 1\cdot z^{-1} + 0] = 0$.

### 6.3 "Inside the unit circle" vs "in the LHP"

- **Mistake:** Calling a DT pole at $z=-0.9$ "on the negative real axis, so unstable/borderline."
- **Why it happens:** LHP intuition imported from CT. "Negative" sounds like "LHP."
- **Correct approach:** DT stability is about *magnitude*: $|p|<1$. The sign of the real part is irrelevant.
- **Example.** $H(z) = \dfrac{1}{1+0.9z^{-1}}$, pole at $z=-0.9$.
  - *Wrong:* "Negative-real pole $\Rightarrow$ not LHP $\Rightarrow$ unstable."
  - *Right:* $|-0.9|=0.9<1$ $\Rightarrow$ stable (impulse response is $(-0.9)^n u[n]$, which decays while alternating sign).

### 6.4 Testing $a<1$ instead of $|a|<1$

- **Mistake:** Declaring a pole at $z=-2$ stable because "$-2 < 1$."
- **Why it happens:** Reading the inequality as a real-number comparison.
- **Correct approach:** Stability is $|a|<1$, a *magnitude* test.
- **Example.** $H(z) = \dfrac{1}{1+2z^{-1}}$, pole at $z=-2$.
  - *Wrong:* "$-2 < 1$ $\Rightarrow$ stable."
  - *Right:* $|-2|=2>1$ $\Rightarrow$ unstable.

### 6.5 Confusing delay and advance

- **Mistake:** Writing $x[n+1] \leftrightarrow z^{-1}X(z)$.
- **Why it happens:** Students memorize "$z^{-1}$ = shift" and forget the sign.
- **Correct approach:** $z^{-1}$ is *delay*: $x[n-1] \leftrightarrow z^{-1}X(z) + x[-1]$ (unilateral). $z$ is *advance*: $x[n+1] \leftrightarrow zX(z) - z x[0]$ (unilateral).
- **Example.** $y[n+1] = 0.5 y[n]$, $y[0] = 2$.
  - *Wrong:* $z^{-1}Y = 0.5 Y$.
  - *Right:* $zY - 2z = 0.5 Y \Rightarrow Y(z-0.5) = 2z \Rightarrow Y = \dfrac{2z}{z-0.5} = \dfrac{2}{1-0.5z^{-1}}$, so $y[n] = 2(0.5)^n u[n]$.

### 6.6 Losing ZSR + ZIR structure

- **Mistake:** Calling $Y(z) = H(z) X(z)$ the total response when $y[-1], y[-2], \ldots$ are nonzero.
- **Why it happens:** Same root cause as §3.4 — convolution property overuse.
- **Correct approach:** Total = ZSR + ZIR. The ZSR is $H(z)X(z)$. The ZIR comes entirely from IC-generated terms after applying the unilateral shift rules with $X(z)\equiv 0$.
- **Example.** $y[n] - 0.6 y[n-1] = (0.5)^n u[n]$, $y[-1]=4$.
  - *Wrong:* $Y = H(z)X(z) = \dfrac{1}{1-0.6z^{-1}}\cdot \dfrac{1}{1-0.5z^{-1}}$, ignoring $y[-1]$.
  - *Right:* $Y(1-0.6z^{-1}) = X(z) + 0.6\cdot 4 = \dfrac{1}{1-0.5z^{-1}} + 2.4$. Solve for $Y$, invert, and the ZIR piece $\dfrac{2.4}{1-0.6z^{-1}}$ is explicit.

---

## 7. Sampling (Lecture 22)

### 7.1 $\Omega$ vs $\omega$ confusion

- **Mistake:** Comparing a DT frequency $\Omega$ (rad/sample) directly to a CT frequency $\omega$ (rad/s).
- **Why it happens:** Both are called "frequency" and both are in radians.
- **Correct approach:** $\Omega = \omega T$, where $T$ is the sampling period. $\Omega$ is dimensionless (rad/sample), $\omega$ has units rad/s.
- **Example.** CT sinusoid at $\omega_0 = 1000\pi$ rad/s, sampled at $T = 10^{-3}$ s.
  - *Wrong:* "DT frequency is $1000\pi$."
  - *Right:* $\Omega_0 = \omega_0 T = 1000\pi \cdot 10^{-3} = \pi$ rad/sample — the highest nonredundant DT frequency (Nyquist, right at the edge).

### 7.2 Nyquist rate vs Nyquist frequency vs sampling rate

- **Mistake:** Using these three terms interchangeably.
- **Why it happens:** Textbooks differ; the terms are one factor of 2 apart.
- **Correct approach:**
  - **Nyquist frequency** = $\omega_M$ (highest frequency in the signal).
  - **Nyquist rate** = $2\omega_M$ (minimum *sampling rate* needed).
  - **Sampling rate** = $\omega_s$ (what you actually chose; must satisfy $\omega_s > 2\omega_M$).
- **Example.** $x(t)$ has $\omega_M = 3000\pi$ rad/s.
  - *Wrong:* "Nyquist rate is $3000\pi$."
  - *Right:* Nyquist frequency = $3000\pi$; Nyquist rate = $6000\pi$. You must sample with $\omega_s > 6000\pi$, i.e., $T < 2\pi/6000\pi = 1/3000$ s.

### 7.3 Treating $\omega_s = 2\omega_M$ as sufficient

- **Mistake:** Sampling *at* the Nyquist rate and claiming perfect reconstruction.
- **Why it happens:** The textbook statement "$\omega_s \ge 2\omega_M$" appears informally, and the strict inequality looks like a detail.
- **Correct approach:** The theorem requires $\omega_s > 2\omega_M$ *strictly*. The boundary case can lose the signal entirely.
- **Example.** $x(t) = \sin(\omega_s t / 2) = \sin(\pi t / T)$ sampled at $t=nT$.
  - *Wrong:* "$\omega_s = 2\omega_M$ satisfies $\ge$, so perfect reconstruction."
  - *Right:* Samples are $\sin(n\pi) = 0$ for all $n$. Every sample is zero; the sinusoid is completely lost.

### 7.4 Aliasing direction (which frequency aliases to which)

- **Mistake:** Computing the aliased frequency as $f_0 - f_s$ (negative) or $f_0 + f_s$ or similar.
- **Why it happens:** Students forget that aliasing folds back into $[-f_s/2, f_s/2]$.
- **Correct approach:** A sinusoid at $f_0$ with $f_s/2 < f_0 < f_s$ aliases to $|f_s - f_0|$ (in the baseband). More generally, fold $f_0$ into $[-f_s/2, f_s/2]$ by adding/subtracting multiples of $f_s$ and taking magnitude.
- **Example.** $x(t) = \cos(2\pi \cdot 900 t)$ sampled at $f_s = 1000$ Hz.
  - *Wrong:* Reconstructed frequency is $900 - 1000 = -100$ Hz (and they write $-100$ as the answer).
  - *Right:* $f_\text{alias} = |1000 - 900| = 100$ Hz — the reconstruction yields a 100 Hz cosine.

### 7.5 Missing the $1/T$ scaling (and the compensating gain $T$)

- **Mistake:** Writing $X_p(j\omega) = \sum_k X(j(\omega - k\omega_s))$ (missing the $1/T$) or using unit-gain LPF for reconstruction.
- **Why it happens:** It's an easy factor to drop.
- **Correct approach:** Sampled spectrum is $X_p(j\omega) = \dfrac{1}{T}\sum_k X(j(\omega - k\omega_s))$. Ideal reconstruction LPF has passband gain $T$ to cancel the $1/T$.
- **Example.** Sampled $x(t)$ with $T=10^{-3}$ s, passed through unity-gain ideal LPF.
  - *Wrong:* Output = $x(t)$.
  - *Right:* Output = $x(t)/T = 1000\, x(t)$. Need LPF gain $T$ (not $1$) to recover $x(t)$ itself.

### 7.6 Hz vs rad/s unit mixing

- **Mistake:** Writing $f_s > 2\omega_M$ or $\omega_s > 2f_M$.
- **Why it happens:** Both "$f$" and "$\omega$" are called "frequency."
- **Correct approach:** Stay in one unit family. $f_s > 2f_M$ (Hz) or $\omega_s > 2\omega_M$ (rad/s). Converter: $\omega = 2\pi f$.
- **Example.** Signal with $f_M = 500$ Hz, sampled at $\omega_s = 1200$ rad/s.
  - *Wrong:* "$\omega_s = 1200 > 2 f_M = 1000$, so OK."
  - *Right:* Convert: $\omega_M = 2\pi \cdot 500 = 1000\pi \approx 3142$ rad/s. Need $\omega_s > 6284$ rad/s. $\omega_s = 1200$ is *way* below Nyquist — catastrophic aliasing.

---

## 8. Feedback Systems (Lecture 23)

### 8.1 Sign error at the summing junction

- **Mistake:** Writing $Q = \dfrac{H}{1-GH}$ for a negative-feedback system.
- **Why it happens:** Students derive the formula quickly and miss the sign at the summer.
- **Correct approach:** **Negative** feedback gives $Q = \dfrac{H}{1+GH}$. **Positive** feedback gives $Q = \dfrac{H}{1-GH}$. Always check the summer's sign convention.
- **Example.** $H(s) = \dfrac{2}{s+1}$ in a unity negative-feedback loop.
  - *Wrong:* $Q = \dfrac{2/(s+1)}{1 - 2/(s+1)} = \dfrac{2}{s-1}$ — pole at $s=+1$, "unstable."
  - *Right:* $Q = \dfrac{2/(s+1)}{1 + 2/(s+1)} = \dfrac{2}{s+3}$ — pole at $s=-3$, stable. Negative feedback moved the pole further left.

### 8.2 Confusing open-loop and closed-loop poles

- **Mistake:** Computing $K$-stability by examining the poles of $GH$ directly.
- **Why it happens:** The expression $GH$ is easiest to factor.
- **Correct approach:** Open-loop poles = poles of $GH$ (fixed). Closed-loop poles = roots of $1 + KGH = 0$ (depend on $K$).
- **Example.** $GH(s) = \dfrac{K}{(s+1)(s+2)}$.
  - *Wrong:* "Poles at $s=-1,-2$, so the system is stable for all $K>0$."
  - *Right:* Characteristic equation: $(s+1)(s+2) + K = 0 \Rightarrow s^2 + 3s + (2+K)=0$. Roots are $s = (-3 \pm \sqrt{9-4(2+K)})/2$. For $K>0$ roots stay in LHP; stable for all $K>0$ (this particular case happens to be). The point is that *the closed-loop poles are not $-1, -2$* — they move as $K$ changes.

### 8.3 Sensitivity formula — reading the denominator

- **Mistake:** Writing $S = 1/GH$ or $S = GH/(1+GH)$.
- **Why it happens:** Confusing sensitivity of the closed-loop gain to plant variation with the complementary sensitivity.
- **Correct approach:** For negative feedback, the sensitivity of $Q$ to $H$ is $S = \dfrac{1}{1+GH}$. The larger $|1+GH|$, the less sensitive the closed loop is to plant changes.
- **Example.** $GH = 9$ (high loop gain).
  - *Wrong:* "$S = 9/(1+9) = 0.9$ — high sensitivity."
  - *Right:* $S = 1/(1+9) = 0.1$. A 10% error in the plant causes only a 1% error in $Q$. High loop gain $\Rightarrow$ low sensitivity.

### 8.4 Solving the wrong equation for closed-loop poles

- **Mistake:** Setting $GH = 0$ or $GH = 1$ to find closed-loop poles.
- **Why it happens:** Students know "something equal to something" determines stability.
- **Correct approach:** Closed-loop poles are the roots of the *characteristic equation* $1 + L(s) = 0$, where $L = GH$ is the loop gain. Equivalently, $L(s) = -1$.
- **Example.** $L(s) = \dfrac{K}{s(s+2)}$.
  - *Wrong:* Set $L(s) = 0 \Rightarrow K=0$, no useful info.
  - *Right:* $1 + \dfrac{K}{s(s+2)} = 0 \Rightarrow s^2 + 2s + K = 0 \Rightarrow s = -1 \pm \sqrt{1-K}$. Closed-loop stable for all $K>0$ (roots have $\operatorname{Re}<0$).

### 8.5 Nyquist: miscounting encirclements or encircling the wrong point

- **Mistake:** Counting encirclements of the origin, or not noticing that the critical point is $-1/K$ (not $-1$).
- **Why it happens:** "Encircles $-1$" is the default statement; students forget the $K$ dependence.
- **Correct approach:** For open-loop-stable $GH$ with gain $K$: closed-loop is stable iff the Nyquist plot of $GH(j\omega)$ does *not* encircle $-1/K$. If $K$ varies, the critical point moves along the real axis.
- **Example.** $GH(j\omega)$ has a plot that passes close to $-0.25$ on the negative real axis.
  - *Wrong:* "Doesn't encircle $-1$, so stable for all $K$."
  - *Right:* For $K=4$, critical point is $-1/4 = -0.25$, right on the curve — marginal. For $K>4$, the critical point is inside the encirclement — unstable.

### 8.6 Swapping gain margin and phase margin readouts

- **Mistake:** Reading GM at the 0-dB gain crossing and PM at the $-180°$ phase crossing.
- **Why it happens:** Two crossings, two margins — easy to swap.
- **Correct approach:**
  - **Gain margin**: at $\omega_1$ where $\angle GH = -180°$, read $-20\log_{10}|GH(\omega_1)|$ from the *magnitude* plot.
  - **Phase margin**: at $\omega_2$ where $|GH| = 1$ (0 dB), read $180° + \angle GH(\omega_2)$ from the *phase* plot.
- **Example.** At $\omega_1 = 20$ rad/s, $\angle GH = -180°$, $|GH| = -8$ dB. At $\omega_2 = 5$ rad/s, $|GH| = 0$ dB, $\angle GH = -150°$.
  - *Wrong:* "GM $= 180 - 150 = 30°$, PM $= -8$ dB."
  - *Right:* GM $= -(-8) = +8$ dB (amount you can increase gain before instability); PM $= 180° + (-150°) = 30°$ (amount of phase lag you can add before instability). Both positive $\Rightarrow$ stable.

### 8.7 Assuming negative feedback always stabilizes

- **Mistake:** "Negative feedback always improves stability."
- **Why it happens:** The textbook narrative emphasizes feedback's stabilizing benefits.
- **Correct approach:** Negative feedback can *destabilize* a stable plant if loop gain is high enough to push closed-loop poles into the RHP, particularly when phase lag accumulates. Feedback is a tool, not a guarantee.
- **Example.** $H(s) = \dfrac{K}{s(s+1)(s+2)}$ with unity negative feedback.
  - *Wrong:* "Negative feedback, so stable for any $K>0$."
  - *Right:* Routh array on $s^3 + 3s^2 + 2s + K = 0$ shows stability requires $0<K<6$. For $K\ge 6$, closed-loop poles cross into the RHP — too much feedback gain destabilizes the system.

---

## Quick-Reference Sign Table (The Ones People Blow)

| Rule | Formula | Sign |
|---|---|---|
| Unilateral Laplace diff | $y'(t) \leftrightarrow sY(s) - y(0^-)$ | **minus** |
| Unilateral Laplace 2nd diff | $y'' \leftrightarrow s^2Y - sy(0^-) - y'(0^-)$ | **both minus** |
| Unilateral Z shift (delay) | $y[n-1] \leftrightarrow z^{-1}Y(z) + y[-1]$ | **plus** |
| Unilateral Z shift-2 | $y[n-2] \leftrightarrow z^{-2}Y + y[-1]z^{-1} + y[-2]$ | **both plus** |
| Unilateral Z advance | $y[n+1] \leftrightarrow zY(z) - z y[0]$ | **minus** |
| Negative-feedback loop | $Q = H/(1+GH)$ | **plus in denominator** |
| Positive-feedback loop | $Q = H/(1-GH)$ | **minus in denominator** |
| Left-sided Z pair | $-a^n u[-n-1] \leftrightarrow 1/(1-az^{-1})$, $|z|<|a|$ | **leading minus** |

---

*Prepared for CEC 315 Exam 3 — Spring 2026.*
