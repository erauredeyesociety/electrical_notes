# CEC 315 HW6 — References and Expanded Work

This document maps each solution to lecture material and explains the methods used.

---

## Problem 1 References (Lecture 19)

All parts use the Z-transform definition and table from Lecture 19, Section 19.4.

Key pairs used (from lctr19_summary.md):
- a^n u[n] <-> 1/(1 - a z^{-1}), ROC: |z| > |a| — used in (a), (e), (f), (g)
- -a^n u[-n-1] <-> 1/(1 - a z^{-1}), ROC: |z| < |a| — used in (b), (f)
- delta[n-k] <-> z^{-k} — used in (c)
- n a^n u[n] <-> a z^{-1}/(1 - a z^{-1})^2, ROC: |z| > |a| — used in (d)
- r^n cos(w0 n) u[n] <-> (1 - r cos(w0) z^{-1})/(1 - 2r cos(w0) z^{-1} + r^2 z^{-2}) — used in (g)

ROC rules (Lecture 19, Section 19.5):
- Right-sided signals: ROC is |z| > |largest pole|
- Left-sided signals: ROC is |z| < |smallest pole|
- Two-sided signals: ROC is annular ring between poles
- DTFT exists when ROC includes unit circle |z| = 1

Part (h) uses the property X(1) = sum of x[n] (Lecture 19, Section 19.3 — evaluating on the unit circle at z=1 gives the DC value / total sum).

## Problem 2 References (Lecture 20)

All parts use the inverse Z-transform via partial fractions from Lecture 20.

Procedure (from lctr20_summary.md, Section 1):
1. Write X(z) as partial fractions A_i/(1 - d_i z^{-1})
2. Use cover-up method: multiply both sides by denominator, substitute z^{-1} = 1/d_i
3. Invert each term using table and ROC direction rule

ROC direction rule (Lecture 20, Section 1):
- If ROC is OUTSIDE a pole -> right-sided: a^n u[n]
- If ROC is INSIDE a pole -> left-sided: -a^n u[-n-1]

Part (b) is the critical two-sided example: annular ROC 0.5 < |z| < 3 means pole at 0.5 gives right-sided, pole at 3 gives left-sided.

Part (c) uses the repeated-pole pair n a^n u[n] from Lecture 20 table.
Part (d) uses the damped-cosine pair from Lecture 20 table.

## Problem 3 References (Lectures 19-20)

Properties used (from lctr20_summary.md, Properties table):
- (a) Time shift: x[n-n0] <-> z^{-n0} X(z). Each z^{-1} factor adds a zero at z=0. Ref: Lecture 20 properties.
- (b) Z-domain scaling: z0^n x[n] <-> X(z/z0), ROC scaled by |z0|. Ref: Lecture 20 properties.
- (c) Convolution: x1*x2 <-> X1*X2. This is the fundamental property that makes Z-transforms useful for LTI system analysis. Ref: Lecture 20 properties.
- (d) Initial-value theorem: x[0] = lim_{z->inf} X(z) for causal signals. Ref: Lecture 20, final-value/initial-value theorems.

## Problem 4 References (Lecture 21)

System analysis pipeline (from lctr21_summary.md):
1. Take Z-transform of difference equation (assuming zero ICs for H(z))
2. Solve for H(z) = Y(z)/X(z)
3. Factor denominator to find poles
4. Check stability: causal + all poles inside unit circle = BIBO stable
5. Invert H(z) via partial fractions for h[n]
6. For a specific input: Y(z) = H(z)X(z), then invert

Stability criteria (Lecture 21, stability section):
- Causal system: BIBO stable iff ALL poles strictly inside unit circle (|pi| < 1)
- Anti-causal system: can be stable if ROC includes unit circle (even with poles outside)
- This is why part (e) gives different stability answers for causal vs anti-causal cases

## Problem 5 References (Lecture 21)

Unilateral Z-transform (from lctr21_summary.md):
- Definition: sum from n=0 to infinity (ignores negative-time values, encodes ICs separately)
- Key time-shift properties:
  - y[n-1] <-> z^{-1} Y(z) + y[-1]
  - y[n-2] <-> z^{-2} Y(z) + y[-2] + y[-1] z^{-1}
  - Note the PLUS sign on IC terms (contrast with Laplace which has minus)

ZSR/ZIR decomposition (Lecture 21):
- Y_ZS: set all ICs to zero, solve with input only
- Y_ZI: set input to zero, solve with ICs only
- Total response Y = Y_ZS + Y_ZI (superposition for linear systems)
- Part (c) demonstrates this decomposition explicitly

Comparison with Laplace (Lecture 21):
- Laplace: s-domain, ROC is vertical strip, stability = poles in left half-plane
- Z-transform: z-domain, ROC is annular ring, stability = poles inside unit circle
- Both convert differential/difference equations to algebraic equations
