# CEC 315 Exam Style Analysis

Analysis of past exams (Exam 1 Ch. 1-2, Exam 2 Lectures 9-15) to predict format, scope, and emphasis of Exam 3 (Lectures 16-23).

---

## 1. Past Exam 1 Breakdown (Chapters 1 & 2, Lectures 2-8)

**Header:** "Exam: Chapters 1 & 2 (Modified Version), Spring 2026"
**Structure:** 100 points = 4 problems x 20 pts + 5 multiple choice x 4 pts = 20 pts. One problem per page. "Show all your work."
**Formatting:** Each problem is inside a blue-bordered title box (topic label on dark blue header, light blue interior). Problem title appears outside the box as `Problem N (20 points)`. Part II MC at the end, no box, 4 pts each, "no partial credit."

| # | Topic (Box Label) | Pts | Lec | Type | Technique |
|---|---|---|---|---|---|
| 1 | System Properties | 20 | 3-4 | Multi-part, 3 systems x 4 properties | Memoryless / causal / TI / linear classification with justification. Mix CT and DT. |
| 2 | Discrete-Time Convolution | 20 | 5-6 | Computational | Convolution sum on two finite sequences; state output length; show sum. |
| 3 | Continuous-Time LTI Systems | 20 | 5-7 | Multi-part | Sifting integrals (2 sub-parts), causal/memory/BIBO-stable from $h(t)$, convolution with shifted delta. |
| 4 | Differential and Difference Equations | 20 | 7-8 | Multi-part CT+DT | Find $h(t)$ from 1st-order ODE; iterate DT difference eqn for $h[0],h[1],h[2]$; general $h[n]$; stability. |
| MC1 | LTI characterization | 4 | 6 | Conceptual | Impulse response is "complete characterization." |
| MC2 | DT convolution definition | 4 | 6 | Conceptual | Symmetric-form identity. |
| MC3 | CT BIBO condition | 4 | 7 | Conceptual | Absolute integrability. |
| MC4 | 1st-order ODE impulse response | 4 | 8 | Computational-ish | $h(t)=b e^{-at}u(t)$. |
| MC5 | Shifted unit impulse | 4 | 6 | Conceptual | Ideal delay. |

**Emphasis:** System properties (1 full problem + 2 MC) and LTI/impulse response (2 full problems + 3 MC). Convolution is tested on both CT (sifting + shifted impulse) and DT (full convolution sum). Stability, causality, and memory appear at least three times.

---

## 2. Past Exam 2 Breakdown (Lectures 9-15)

**Header:** "Exam: Lectures 9-15 (Exam 2), Spring 2026, Rogelio Gracia Otalvaro."
**Structure:** 100 points. Time: 60 minutes. **Part I (5 MC x 4 pts = 20 pts) first**, then **Part II (4 problems = 80 pts)** with non-uniform weights (20 + 25 + 20 + 15). Name/Date line. Instruction block: "Show all work clearly. Box your final answers. Assume all systems are causal and stable unless stated otherwise."
**Formulas provided on page 1:** Euler, CT FS analysis/synthesis, CT FT pair, exponential FT pair $e^{-at}u(t)\leftrightarrow 1/(a+j\omega)$, convolution-multiplication, Parseval (FS), 2nd-order standard form with %OS and $t_s$.

| # | Topic | Pts | Lec | Type | Technique |
|---|---|---|---|---|---|
| MC1 | Gibbs phenomenon (9% overshoot) | 4 | 10 | Conceptual |
| MC2 | Frequency shift / modulation FT property | 4 | 13 | Conceptual |
| MC3 | DT Fourier series - N distinct coefficients | 4 | 10 | Conceptual |
| MC4 | Bode high-freq slope (1st-order LPF) | 4 | 14-15 | Conceptual |
| MC5 | 2nd-order damping / resonance peak condition | 4 | 15 | Conceptual |
| P1 | CT Fourier Series + Properties | 20 | 9-10 | Multi-part (a-d) | Piecewise square wave, analysis integral with Euler trick, $\|a_1\|,\|a_2\|,\|a_3\|$, $1/k$ decay commentary, Parseval check. |
| P2 | FT Properties + Convolution | 25 | 12-13 | Multi-part (a-e) | Time-shift (phase only), freq-shift with cos(8t) via Euler, convolution-multiplication $Y=X\cdot H$, 2-term PFE, inverse to $y(t)$, verify $y(0)$ and $y(\infty)$. |
| P3 | Frequency Response and Filtering | 20 | 11, 14 | Multi-part (a-d) | $H(j\omega)$ from $h(t)=4e^{-4t}u(t)$, 3 dB cutoff, table at $\omega\in\{0,4,20\}$, trig-form output, dB attenuation, LP/HP classification. |
| P4 | Second-Order System + Bode | 15 | 15 | Multi-part (a-d) | Classify damping, DC gain, $\|H(j\omega_n)\|$ dB, %OS, $t_s$, Bode asymptotes + corner, phase at $\omega_n$ and limits. |

**Emphasis:** Fourier properties (time shift, freq shift, Parseval, convolution-multiplication) dominate (>45 pts). 2nd-order time/frequency metrics - 15+ pts concentrated in P4 and MC5. Filtering/Bode - 20+ pts. Integration of concepts: every problem is a multi-part 3-5 sub-question chain that walks through "setup -> compute -> verify/interpret."

## 2a. Exam 2 Study Guide vs Actual Exam

The 32-page study guide covered Lectures 9-15 and flagged, in green "Key Insight" boxes and red "Common Mistake" boxes, the following high-emphasis items: Euler inspection trick for simple signals, Parseval sanity check, differentiation shortcut for triangular waves, $1/k$ vs $1/k^2$ decay for square vs triangular, DT has only $N$ distinct coefficients, Gibbs $\approx 9\%$, time-shift changes phase but not magnitude, eigenfunction property as the bridge to frequency response, 2nd-order %OS / $t_s$ / resonance condition $\zeta<1/\sqrt{2}$.

**Hit rate:** Every green/red box in the guide maps to a question on the actual exam (MC1 = Gibbs, MC2 = freq shift, MC3 = DT N coefficients, MC4 = Bode slope, MC5 = resonance condition; P1 = Euler inspection + Parseval + $1/k$ decay; P2 = time-shift magnitude invariance + convolution-multiplication; P4 = 2nd-order metrics). **Takeaway: the study guide's "Key Insight" and "Common Mistake" boxes predict exam content almost 1:1.**

---

## 3. Pattern Observations

1. **Layout identical in spirit, different in detail.** Both use LaTeX-boxed problems in blue, both say "Show all your work," both are 100 pts, both end with multiple choice worth 20 pts (5 x 4). Exam 1 puts problems before MC; Exam 2 puts MC before problems and adds a useful-formulas box + name/date line. Exam 3 will almost certainly follow Exam 2's updated template (same instructor, same semester).
2. **Problem count:** 4 long problems + 5 MC is the stable pattern.
3. **Point distribution is not always uniform.** Exam 1 used 4 x 20; Exam 2 used 20/25/20/15. Expect non-uniform on Exam 3.
4. **Per-problem scope.** A 20-pt problem has 3-5 sub-parts (a-e) and walks through a complete technique: setup the transform/integral, compute, interpret or verify. The sub-part point split on Exam 2 averaged 4-5 pts per sub-part.
5. **Topic weighting follows "flagship technique + properties + interpretation."** Exam 1 flagship = convolution + system properties. Exam 2 flagship = Fourier (FS coefficients, FT properties, filtering, 2nd-order). Exam 3 flagship will be Laplace + Z + sampling + feedback.
6. **Conceptual multiple choice targets the exact "Key Insight" and "Common Mistake" callouts in the lecture summaries.** This is the single most reliable predictor.
7. **Instructor always provides useful formulas** when a formula is bulky to memorize (FT pair, 2nd-order metrics). Exam 3 should get an even bigger formula box.
8. **One problem per page** on Exam 1; Exam 2 is denser (formulas on p.1, MC on p.2, problems on p.3-6). The Exam 2 format is the likely template.
9. **Length/difficulty:** Exam 2 is moderately harder than Exam 1 because every problem integrates 2-3 lectures. Exam 3 covers 8 lectures - expect continued integration (e.g., Laplace ROC + inverse + system analysis in one problem).

---

## 4. Exam 3 Predictions (Lectures 16-23)

**Likely structure (high confidence):**
- 100 pts total, 60 minutes.
- Useful Formulas box on page 1 including: Laplace pair $e^{-at}u(t)\leftrightarrow 1/(s+a)$, unilateral Laplace derivative property with initial conditions, Z pair $a^n u[n]\leftrightarrow z/(z-a)$, sampling theorem $\omega_s > 2\omega_M$, closed-loop $T = GH/(1+GH)$.
- Part I: 5 multiple choice x 4 pts = 20 pts.
- Part II: 4 problems = 80 pts, non-uniform (likely 20/20/20/20 or 25/20/20/15).
- Same boxed blue problem style, "Show all work, box final answer, assume causal/stable unless stated."

**Likely multiple choice topics (pulled from the "Key Insight / Common Mistake" boxes in lecture summaries 16-23):**
- ROC shape rule: right-sided -> right half-plane of rightmost pole (CT) or outside outermost pole (DT).
- Causality + stability together imply ROC contains $j\omega$-axis (CT) or unit circle (DT).
- Unilateral Laplace derivative property: $\mathcal{L}\{y'\} = sY(s) - y(0^-)$.
- Nyquist rate: $\omega_s > 2\omega_M$; aliasing if violated.
- Closed-loop sensitivity reduction by factor $1/(1+GH)$.

**Likely long problems (high confidence):**

1. **Bilateral Laplace + inverse (20 pts, Lec 16-17).** Given $X(s)$ with a 2-3 pole rational expression, do PFE, identify possible ROCs, invert for each ROC case (right-sided, left-sided, two-sided). Sub-parts: (a) poles/zeros (b) PFE constants (c) $x(t)$ for causal ROC (d) which ROC makes $x(t)$ stable. This is a direct analog of Exam 2 Problem 2.

2. **Unilateral Laplace IVP / system analysis (20 pts, Lec 18).** Given an ODE like $y''+3y'+2y=x(t)$ with $y(0^-)$, $y'(0^-)$, and $x(t)=u(t)$, solve using unilateral Laplace. Sub-parts: transform with initial conditions, solve for $Y(s)$, PFE, inverse, identify zero-input vs zero-state response, transfer function $H(s)$, pole locations + stability.

3. **Z-transform + inverse + DT system (20 pts, Lec 19-21).** Given $H(z)$ or a difference equation, find poles, ROC for causal, stability check (unit circle), PFE, inverse via table, response to $x[n]=u[n]$ via unilateral Z (include initial conditions).

4. **Sampling OR Feedback (15-20 pts, Lec 22-23).** One of two flavors - or possibly one problem split:
   - **Sampling:** Given $x(t)$ with stated bandwidth, state Nyquist rate, sketch $X_p(j\omega)$ for given $\omega_s$, identify aliasing, reconstruct with ideal LPF, give cutoff.
   - **Feedback:** Given open-loop $G(s)$ and feedback $H(s)$, compute $T(s)=G/(1+GH)$, closed-loop poles, show stability (pole LHP), compute steady-state tracking error from final-value theorem, comment on sensitivity.

**Estimated point distribution (calibrated against Exam 2's 20/25/20/15):**
- Laplace (bilateral inverse + unilateral IVP): ~40 pts across 2 problems + 1-2 MC.
- Z-transform (inverse + DT system analysis): ~20 pts, 1 problem + 1 MC.
- Sampling: ~10-20 pts, likely 1 problem or fused with feedback.
- Feedback: ~10-20 pts, likely 1 problem or fused with sampling.
- Conceptual MC distributed across all 8 lectures.

**Confidence levels:**
- Near certainty: Laplace PFE + inverse, unilateral Laplace IVP, Z-transform, Nyquist rate question, closed-loop transfer function.
- High: ROC reasoning, pole-location stability checks, final-value theorem.
- Moderate: State-space / block diagram reduction, Bode-style root-locus or gain margin discussion (only if covered in class).

---

## 5. Difficulty and Length Comparison (Exam 1 vs Exam 2)

| Dimension | Exam 1 | Exam 2 |
|---|---|---|
| Total pts | 100 | 100 |
| Problem count | 4 + 5 MC | 4 + 5 MC |
| Per-problem scope | 2-3 sub-parts, one focused technique | 3-5 sub-parts, chained techniques |
| Formulas given | None | Full formula box |
| Integration across lectures | Moderate (each problem stays in one chapter) | Heavy (Fourier properties chain into filtering and 2nd-order) |
| Computational burden | Moderate (one convolution sum, one ODE, sifting integrals) | Higher (Euler-trick analysis integral, PFE, table fills, dB calc) |
| Conceptual reasoning | Baked into sub-parts (stable? causal?) | Baked into sub-parts + heavier MC |
| Average difficulty | Moderate | Moderate-High |

**Verdict:** Exam 2 is noticeably longer per problem and demands more integration of multiple properties. Exam 3 covers the broadest span (8 lectures across Laplace, Z, sampling, feedback) and will likely match Exam 2's density and difficulty, not exceed it. Expect tight timing - 60 minutes for 4 multi-part problems means ~12-13 minutes per long problem.

---

## 6. Preparation Priorities

1. **Laplace PFE + inverse with ROC reasoning** - the single highest-value drill. Practice 2-pole and 3-pole rational $X(s)$, partial fractions, and associating each ROC with causality.
2. **Unilateral Laplace IVPs** - ODE with nonzero $y(0^-),y'(0^-)$, find $Y(s)$, split into zero-input and zero-state, invert. Memorize the derivative property exactly.
3. **Z-transform symmetry with Laplace** - same workflow, substitute $1/(1-az^{-1})$ or $z/(z-a)$, inverse via table + long division for improper, apply unilateral Z to difference equations.
4. **Nyquist rate + aliasing sketches** - know $\omega_s > 2\omega_M$, be able to draw $X_p(j\omega)$ as shifted replicas and identify overlap.
5. **Closed-loop transfer function and stability** - $T = G/(1+GH)$, roots of $1+GH=0$ must be LHP (CT) or inside unit circle (DT), final-value theorem for tracking error.
6. **Memorize transform pairs** for the useful formulas list the instructor is likely to provide: $e^{-at}u(t), tu(t), \cos/\sin\times u(t), a^n u[n], n a^n u[n]$.
7. **Review every green "Key Insight" and red "Common Mistake" box** in the lecture 16-23 summaries - these map 1:1 onto the multiple-choice section historically.
8. **Time pressure drill** - work a full practice problem in 12 minutes to calibrate pacing.
