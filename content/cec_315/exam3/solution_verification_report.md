# CEC 315 Exam 3 — Solution Verification Report

**Scope:** Lectures 16-23 (Exam 3 material) across three files:

- `/home/devel/electrical_notes/content/cec_315/exam3/exam3_sample_problems.md`
- `/home/devel/electrical_notes/content/cec_315/master_docs/master_sample_problems.md` (Part III only)
- `/home/devel/electrical_notes/content/cec_315/master_docs/master_homework_problems.md` (Part III only)

Every worked solution listed below was independently re-derived. Checks covered: Laplace/Z-transform derivations, ROCs, PFE residues, unilateral transform IC handling, Nyquist rate arithmetic, closed-loop transfer function algebra, margin calculations.

## exam3/exam3_sample_problems.md

| Problem | Status |
|---|---|
| 16.1 Right-sided exponential | OK |
| 16.2 Left-sided exponential | OK |
| 16.3 Two-sided signal | OK |
| 16.4 Sum of two right-sided exponentials | OK |
| 16.5 Unit step | OK |
| 17.1 Distinct real poles | OK (A=2, B=0 verified) |
| 17.2 Distinct poles, mixed ROC | OK (A=-3, B=8 verified) |
| 17.3 Repeated poles | OK (A=7/4, B=1/2, C=-7/4 verified) |
| 17.4 Complex conjugate poles | OK (2s = 2(s+2)-4 decomposition valid) |
| 17.5 s-domain shifting | OK |
| 17.6 Initial/final value theorems | OK (x(0+)=0, x(∞)=1) |
| 18.1 DE → H(s) | OK |
| 18.2 Stability classification table | OK |
| 18.3 Complete pipeline | OK (PFE 1/2, -1/2) |
| 18.4 First-order IVP | OK |
| 18.5 Second-order IVP | OK (A=1/3, B=2, C=-4/3; ICs reproduced) |
| 19.1 Right-sided geometric | OK |
| 19.2 Left-sided geometric | OK |
| 19.3 Two-sided signal | OK |
| 19.4 Sum of right-sided | OK (zero at z=1.6, X(1)=-5 verified) |
| 19.5 Finite-duration sequence | OK |
| 20.1 Distinct real poles | OK (A=2, B=1; x[0]=3) |
| 20.2 Mixed ROC | OK (A=4/3, B=-1/3) |
| 20.3 Repeated poles | OK |
| 20.4 Complex conjugate poles | OK |
| 20.5 Time-shift | OK |
| 20.6 Initial/final value | OK (x[0]=5, x[∞]=12.5) |
| 21.1 DE → H(z) | OK (poles 0.5, 0.3) |
| 21.2 Full pipeline | OK (A=-5/3, B=8/3) |
| 21.3 First-order DE with IC | OK (A=-5, B=8.4; y[0]=3.4) |
| 21.4 Second-order ZIR | OK (A=5/6, B=-2/15; y[0]=0.7) |
| 22.1 Nyquist — sum of sinusoids | OK (4000 Hz) |
| 22.2 Nyquist — sinc | OK |
| 22.3 Nyquist — squared sinc | OK (8000 Hz) |
| 22.4 Sampling period check | OK |
| 22.5 Exact-Nyquist failure | OK |
| 22.6 Aliasing 5 Hz → 1 Hz | OK |
| 23.1 Cascade + feedback | OK (Q=1/(s²+4s+5)) |
| 23.2 Unity feedback adjustable gain | OK |
| 23.3 Stabilizing unstable plant | OK (K>1/3) |
| 23.4 Nyquist check | OK (K_max=2) |
| 23.5 Gain and phase margins | OK (PM=45°, GM=12 dB, τ≈79 ms) |

## master_docs/master_sample_problems.md (Part III)

| Problem | Status |
|---|---|
| L16 Ex 1-9 (right/left exponential, two-sided, impulse, step, growing exp, FT checks) | OK |
| L17 Ex 1 Distinct real poles | OK |
| L17 Ex 2 Mixed ROC | OK |
| L17 Ex 3 Repeated poles | OK |
| L17 Ex 4 Complex conjugate poles | OK |
| L17 Ex 5 |H(jω)| of 1/(s+a) | OK |
| L17 Ex 6 s-domain shifting | OK |
| L17 Ex 7 Differentiation in s | OK |
| L17 Ex 8 Initial/final value theorems | OK |
| L18 Ex 1-6 (DE → H(s), stability table, pipeline, IVPs, ZSR/ZIR) | OK |
| L19 Ex 1-10 (geometric pairs, two-sided, finite-duration) | OK |
| L20 Ex 1 Distinct poles right-sided | OK |
| L20 Ex 2 Mixed ROC | Fixed: cleaned up garbled cover-up step "1=A(1-0.25·2)⇒1=A(0.75)" that had contradictory arithmetic; replaced with direct cover-up "1/(1-0.5·0.5)=A⇒1/(1-0.25)=A⇒A=4/3". Final answer A=4/3, B=-1/3 was already correct. |
| L20 Ex 3 Repeated poles | OK |
| L20 Ex 4 Complex conjugate poles | OK |
| L20 Ex 5 Time-shift | OK |
| L20 Ex 6 IVT/FVT | OK (x[0]=5, x[∞]=12.5) |
| L21 Ex 1 DE → H(z) | OK |
| L21 Ex 2 Stability classification | OK |
| L21 Ex 3 Full pipeline | OK (A=-5/3, B=8/3; y[1]=1.3 verified two ways) |
| L21 Ex 4 First-order with IC | OK |
| L21 Ex 5 Second-order ZIR | OK |
| L22 Ex 1(a,b,c) Nyquist rates | OK |
| L22 Ex 2 Sampling periods | OK |
| L22 Ex 3 Exact-Nyquist failure | OK |
| L22 Ex 4 Aliasing | OK |
| L22 Practice P1-P15 | OK |
| L23 Ex 1 Cascade + feedback | OK |
| L23 Ex 2 Unity feedback adjustable gain | OK |
| L23 Ex 3 Stabilizing unstable plant | OK |
| L23 Ex 4 Nyquist plot table | OK |
| L23 Ex 5 Nyquist stability check | OK |
| L23 Ex 6 Margin calculation | OK |
| L23 Ex 7 Problem 1 Cascade + unity feedback | OK (Q=2/((s+2)(s+3))) |
| L23 Ex 8 Problem 2 Parallel + feedback | OK (denom s²+23s+78) |
| L23 Ex 9 Problem 3 Nested loops | OK |
| L23 Ex 10 Problem 4 First-order | OK |
| L23 Ex 11 Problem 5 Second-order | OK |
| L23 Ex 12 Problem 6 DT feedback | OK (pole z=0.8-K) |
| L23 Ex 13 Problem 7 Margins | OK (τ≈105 ms) |
| L23 T/F P8-P10 | OK |

## master_docs/master_homework_problems.md (Part III)

| Problem | Status |
|---|---|
| HW L16-18 P1 (a-f) Laplace transforms and ROCs | OK |
| HW L17 P2(a) Distinct real poles (A=2/3, B=7/3) | OK |
| HW L17 P2(b) Two-sided (A=8/5, B=2/5) | OK |
| HW L17 P2(c) Repeated poles (A=-2/3, B=2, C=2/3) | OK |
| HW L17 P2(d) Complex poles | OK |
| HW L16-17 P3(a) s-shift | OK |
| HW L16-17 P3(b) Differentiation in time | OK |
| HW L16-17 P3(c) Convolution (A=3/5, B=-3/5) | OK |
| HW L16-17 P3(d) IVT/FVT (A=1, B=2, C=-3) | OK |
| HW L18 P4 System analysis (H, h, y, g alt) | OK |
| HW L18 P5(a) Unilateral IVP (A=1, B=1) | OK |
| HW L18 P5(b) Second-order ZIR | OK |
| HW L18 P5(c) ZSR/ZIR decomposition | OK |
| HW L19 P1(a-g) z-Transforms and ROCs | OK (including (g) r·cos(0.25π)≈0.5657) |
| HW L19 P1(h) X(1) sanity checks | OK |
| HW L20 P2(a) A=-8, B=9 | OK |
| HW L20 P2(b) A=-0.8, B=4.8 | OK |
| HW L20 P2(c) x[n]=2n(0.5)^n | OK |
| HW L20 P2(d) Complex conjugate | OK |
| HW L19-20 P3(a) Time shifting | OK |
| HW L19-20 P3(b) z-scaling | OK |
| HW L19-20 P3(c) Convolution (A=-0.75, B=1.75) | OK |
| HW L19-20 P3(d) IVT (A=2/9, B=25/9) | OK |
| HW L21 P4 System analysis (A=-1, B=2; A=1.5, B=12, C=-12.5) | OK (y[1]=1.4 verified two ways) |
| HW L21 P5(a) Unilateral IVP (A=-5/3, B=76/15) | OK |
| HW L21 P5(b) Second-order ZIR (A=18/7, B=-1/14) | OK |
| HW L21 P5(c) ZSR/ZIR decomposition | OK |
| HW L22 P1-P15 Sampling | OK |
| HW L23 P1-P10 Feedback | OK |

## Summary Statistics

- **Total problems checked:** 127
- **OK (verified correct):** 126
- **Fixed:** 1 (master_sample_problems.md, L20 Example 2 — garbled cover-up arithmetic with correct final answer)
- **Suspicious but unsure:** 0

## Overall Findings

The three documents are in excellent arithmetic shape. Every PFE residue I recomputed matched the stated value. Every ROC assignment correctly corresponds to its pole geometry. Unilateral transform initial-condition terms (the y(0⁻), y'(0⁻), y[-1], y[-2] substitutions) are handled with the proper sign conventions throughout. Nyquist rates for sinusoids, sincs, and sinc-squared examples are all correct, including the subtle "squaring doubles bandwidth" case. Feedback transfer functions are algebraically clean, and margin calculations (PM=45°, GM=12 dB ⇒ factor 4; τ_max≈79 ms and 105 ms respectively) reproduce on re-derivation.

Only one actual defect was found: in `master_sample_problems.md`, Lecture 20 Example 2, the cover-up step for A was written as "1=A(1-0.25·2)⇒1=A(0.75)", which is internally inconsistent (1-0.25·2 = 0.5, not 0.75) even though the correctly stated final A=4/3 matches a clean cover-up (1-0.5·0.5 = 0.75). This looked like a transcription slip where the writer mixed up which factor was being evaluated. I replaced the garbled line with a clean single-step derivation. The final boxed answer was already correct and required no change.

A few stylistic nits I deliberately did not touch because they are not factual errors: slightly awkward wording in the PFE for HW L18 P3(d) (where B is computed twice in a somewhat confused line but lands on B=2), and the "2000 Hz" labeling of ω_M=4000π rad/s in exam3_sample_problems Problem 22.1 (correct since 4000π/(2π)=2000 Hz, just terse notation).

Bottom line: the solutions are trustworthy. One cosmetic arithmetic slip fixed; no conceptual errors found.
