# Lecture 23 — Linear Feedback Systems

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr23-linear-feedback-systems.pdf`
**Textbook focus:** Chapter 11 §§11.0–11.5 (pp. 816–866)
**Exam coverage:** Exam 3

Focus: Chapter 11, Sections 11.0–11.5 (Pages 816–866)

## 1. The Big Picture

### Why This Matters

Up to now we have analyzed systems where the input goes in, gets processed, and the output comes out. A **feedback system** takes some version of the output and routes it back to the input. This one structural change gives engineers the power to make unstable systems stable, make imprecise systems precise, and make sluggish systems fast. Feedback is everywhere: cruise control in your car, the thermostat in your house, your body's reflexes, autopilots in aircraft, and audio systems. The goal of this lecture is to understand the basic structure, learn how to compute the closed-loop transfer function from a block diagram, and build intuition for what feedback does and what can go wrong.

**What you need to be able to do for the exam:**
1. Read a block diagram and write the closed-loop system function.
2. Simplify block diagrams with cascades, parallel paths, and nested loops.
3. Determine whether a closed-loop system is stable by finding its poles.
4. Understand what a Nyquist plot is and what it tells you about stability.
5. Compute gain margin and phase margin from Bode plot data.

## 2. Open-Loop vs. Closed-Loop

*[Figure 1: (a) Open-loop block diagram — input arrow into "Plant" block, then output arrow out. (b) Closed-loop block diagram — ref input into summer (+ on ref, − on feedback), summer output labeled "error" feeds the Plant block, Plant output is the system output and also routes back through a feedback path to the summer's negative input.]*

Figure 1: (a) Open-loop: no correction. (b) Closed-loop: the output is compared to the reference and the error drives the plant.

In an open-loop system you set the input and hope for the best. In a closed-loop system, the system watches its own output and continuously corrects itself. The two main benefits of negative feedback are **disturbance rejection** (the system fights back against perturbations) and **reduced sensitivity** (the closed-loop behavior depends mostly on the feedback path, not on the imprecise plant).

## 3. Block Diagram Basics and the Closed-Loop Formula

### 3.1 The Standard Negative Feedback Loop

*[Figure 2: Standard negative feedback configuration. $X(s)$ enters a summer (+ on input, − on feedback return); summer output is $E(s)$; $E(s)$ feeds $H(s)$ whose output is $Y(s)$; $Y(s)$ feeds back through $G(s)$ into the negative input of the summer.]*

Figure 2: Standard negative feedback configuration.

Reading the diagram: the summer computes $E = X - G \cdot Y$, and the forward path gives $Y = H \cdot E$. Substituting and solving:

### The Closed-Loop Formula (memorize this)

$$Q(s) = \frac{Y(s)}{X(s)} = \frac{H(s)}{1 + G(s)H(s)}$$

The denominator $1 + G(s)H(s)$ determines the closed-loop poles and therefore stability. The product $G(s)H(s)$ is called the **loop gain**. If the feedback is *positive* (added instead of subtracted), the formula becomes $H/(1 - GH)$.

### 3.2 Block Diagram Simplification Rules

*[Figure 3: The three block diagram simplification rules:
- **Cascade:** two blocks $H_1$ then $H_2$ in series $\implies H_1 \cdot H_2$
- **Parallel:** two blocks $H_1$ and $H_2$ in parallel summed $\implies H_1 + H_2$
- **Neg. feedback:** summer (−) into $H$ with feedback $G$ $\implies \dfrac{H}{1 + GH}$]*

Figure 3: The three block diagram simplification rules.

The strategy for any block diagram: identify the innermost loop or cascade, replace it with a single block using the rules above, and repeat until you have one block.

### Worked Example 23.1: Cascade Plus Feedback

Given: $H_1 = \dfrac{1}{s+1}$, $H_2 = \dfrac{1}{s+3}$, $G = 2$.

*[Figure: input $X$ into summer (−), into $H_1$, into $H_2$, out as $Y$; $Y$ feeds back through $G$ into the negative summer input.]*

**Step 1 – Cascade**: combine $H_1$ and $H_2$ in series:

$$H_1 H_2 = \frac{1}{(s+1)(s+3)} = \frac{1}{s^2 + 4s + 3}.$$

**Step 2 – Feedback**: forward path $= H_1 H_2$, feedback path $= G = 2$:

$$Q(s) = \frac{H_1 H_2}{1 + G \cdot H_1 H_2} = \frac{\frac{1}{s^2+4s+3}}{1 + \frac{2}{s^2+4s+3}} = \frac{1}{s^2 + 4s + 3 + 2} = \frac{1}{s^2 + 4s + 5}.$$

**Step 3 – Poles**: $s^2 + 4s + 5 = 0 \implies s = -2 \pm j$. Both have negative real part $\implies$ **stable**.

### Worked Example 23.2: Unity Feedback with Adjustable Gain

*[Figure: input $X$ into summer (−), into block $K$, into block $\dfrac{1}{s+2}$, out as $Y$; unity feedback from $Y$ to negative summer input.]*

Forward path: $H(s) = K/(s+2)$. Feedback: $G = 1$ (unity).

$$Q(s) = \frac{K/(s+2)}{1 + K/(s+2)} = \frac{K}{s + 2 + K}. \qquad \text{Closed-loop pole: } s = -(2 + K).$$

| $K$ | Closed-loop pole | Comment |
|---|---|---|
| $K = 0$ | pole at $s = -2$ | (open-loop pole, no feedback effect) |
| $K = 8$ | pole at $s = -10$ | (faster, stable) |
| $K = -3$ | pole at $s = +1$ | (**unstable**) |

Stable when $2 + K > 0$, i.e. $K > -2$.

### Worked Example 23.3: Stabilizing an Unstable Plant

Plant: $H(s) = \dfrac{3}{s - 1}$ (unstable: pole at $s = +1$). Unity feedback with gain $K$.

$$Q(s) = \frac{3K/(s-1)}{1 + 3K/(s-1)} = \frac{3K}{s - 1 + 3K} = \frac{3K}{s + (3K - 1)}.$$

Closed-loop pole: $s = 1 - 3K$. For stability: $1 - 3K < 0$, so $K > 1/3$.

Feedback moved the pole from $+1$ (unstable) to $1 - 3K$. For $K = 1$: pole at $s = -2$ (stable, fast).

## 4. What Does Feedback Actually Do?

Three cases of $Q = H/(1 + GH)$ tell the whole story:

| Situation | Result | Meaning |
|---|---|---|
| $\lvert GH \rvert \gg 1$ | $Q \approx 1/G$ | Output set by feedback path only |
| $\lvert GH \rvert \ll 1$ | $Q \approx H$ | Feedback barely matters |
| $GH = -1$ at some $\omega$ | $Q \to \infty$ | Instability! |

The "danger zone" is when $GH = -1$: magnitude 1 and phase $-180°$ simultaneously. Every stability tool we will discuss is a way of checking how close we are to that condition.

## 5. The Nyquist Plot and Nyquist Stability Criterion

### Why This Matters

Sometimes we do not have an analytic expression for $G(s)H(s)$; all we have is measured frequency-response data (a Bode plot). The **Nyquist criterion** works in this situation. It answers a simple yes/no question: for a given $K$, is the closed-loop system stable?

### 5.1 What Is a Nyquist Plot?

A Nyquist plot is a **polar plot of the loop gain** $G(j\omega)H(j\omega)$ in the complex plane, traced out as $\omega$ goes from $-\infty$ to $+\infty$. At each frequency $\omega$, the loop gain has a magnitude $\lvert GH \rvert$ and a phase $\angle GH$. You plot the point with those polar coordinates. Connecting all such points gives a curve.

Because the impulse response is real-valued, the plot for $\omega < 0$ is just the mirror image (about the real axis) of the plot for $\omega > 0$. So you really only need to compute the $\omega > 0$ half and reflect it.

### Worked Example 23.4: Drawing a Nyquist Plot

Let $G(s)H(s) = \dfrac{1}{(s+1)(s/2+1)}$. Evaluate at $s = j\omega$:

$$G(j\omega)H(j\omega) = \frac{1}{(j\omega + 1)(j\omega/2 + 1)}.$$

At a few key frequencies:

| $\omega$ | $\lvert GH \rvert$ | $\angle GH$ | Point in complex plane |
|---|---|---|---|
| $0$ | $1$ | $0°$ | $(1,\ 0)$ |
| $1$ | $0.632$ | $-71.6°$ | $(0.20,\ -0.60)$ |
| $2$ | $0.316$ | $-108.4°$ | $(-0.10,\ -0.30)$ |
| $\infty$ | $0$ | $-180°$ | $(0,\ 0)$ |

*[Figure: Nyquist plot in the complex plane. Solid blue curve starts at $(1,0)$ for $\omega = 0$, passes through lower half plane through $\omega = 1$ point, curves toward origin at $\omega = \infty$ with phase $-180°$. Dashed blue curve is the mirror image in upper half plane for $\omega < 0$. A red marker shows $-1/K$ on the negative real axis. Arrows indicate direction of traversal (increasing $\omega$).]*

The solid blue curve is $\omega > 0$; the dashed curve is $\omega < 0$ (mirror image). Together they form a closed contour. The arrows show the direction of traversal (increasing $\omega$).

### 5.2 How to Use the Nyquist Plot for Stability

### Nyquist Stability Criterion (Simplified)

If the open-loop system $GH$ is **stable** (no right-half-plane poles), then the closed-loop system with gain $K$ is stable if and only if the Nyquist plot does **not encircle** the point $-1/K$.

**How to check**: locate the point $-1/K$ on the real axis. If it falls *outside* the closed Nyquist contour, the system is stable. If it falls *inside* the contour (the curve wraps around it), the system is unstable.

In Example 23.6, the Nyquist plot stays to the right of approximately $\mathrm{Re} = -0.15$. So for $K = 1$, the critical point is $-1$, which is far to the left of the curve and clearly not encircled $\implies$ stable. The curve crosses the negative real axis at approximately $-0.15$, so the system goes unstable when $-1/K = -0.15$, giving $K = 1/0.15 \approx 6.7$. For any $K < 6.7$, the system is stable.

### Worked Example 23.5: Nyquist Stability Check

A system has the following Nyquist-plot data: the curve crosses the negative real axis at the point $(-0.5,\ 0)$.

The open-loop system is stable. Is the closed-loop system stable for $K = 1$?

**Solution**: for $K = 1$, the critical point is $-1/K = -1$. Since the curve only reaches $-0.5$ on the negative real axis, the point $-1$ is to the left of the curve and is not encircled. $\implies$ **Stable**.

What is the maximum $K$ for stability? The curve crosses the negative real axis at $-0.5$, so instability begins when $-1/K = -0.5$, giving $K_{\max} = 2$.

## 6. Gain Margin and Phase Margin

### Why This Matters

Even when a system is stable, we want to know *how much room for error* we have. If a component degrades slightly or a signal gets delayed, will the system still work? Gain margin and phase margin quantify this safety buffer. Both are read directly from Bode plot data.

### 6.1 Definitions

Instability occurs when $GH = -1$, which means *simultaneously*:
- $\lvert GH \rvert = 1$ (i.e. 0 dB), and
- $\angle GH = -180°$.

The two margins measure how far we are from satisfying both conditions at the same time:

| Margin | Definition | How to read from Bode plot |
|---|---|---|
| **Gain margin (GM)** | At the frequency $\omega_1$ where $\angle GH = -180°$: $\mathrm{GM} = \dfrac{1}{\lvert GH(\omega_1) \rvert}$ or in dB: $\mathrm{GM}_{\mathrm{dB}} = -20\log_{10}\lvert GH(\omega_1)\rvert$ | Go to the **phase plot**, find where the phase curve crosses $-180°$, read off $\omega_1$. Go to the **magnitude plot** at that same $\omega_1$. GM is how far *below* 0 dB the magnitude is. |
| **Phase margin (PM)** | At the frequency $\omega_2$ where $\lvert GH \rvert = 1$ (0 dB): $\mathrm{PM} = 180° + \angle GH(\omega_2)$ | Go to the **magnitude plot**, find where the magnitude curve crosses 0 dB, read off $\omega_2$. Go to the **phase plot** at that same $\omega_2$. PM is how far *above* $-180°$ the phase is. |

*[Figure 4: Bode plots. Top: magnitude $\lvert GH \rvert$ (dB) vs $\omega$ (log scale), curve decreasing through 0 dB at $\omega_2$, then continuing below 0 dB; at $\omega_1$ the magnitude is some amount below 0 dB (labeled GM in dB, green double-arrow). Bottom: phase $\angle GH$ vs $\omega$ (log scale), curve descending from 0° toward $-180°$; at $\omega_2$ the phase is some amount above $-180°$ (labeled PM, green double-arrow); at $\omega_1$ the phase equals $-180°$.]*

Figure 4: Reading gain margin and phase margin from Bode plots. **GM**: at $\omega_1$ (where phase $= -180°$), how far is the magnitude below 0 dB? **PM**: at $\omega_2$ (where magnitude $= 0$ dB), how far is the phase above $-180°$?

### Worked Example 23.6: Gain and Phase Margin Calculation

From a Bode plot you read the following data:

| | $\lvert GH \rvert$ (dB) | $\angle GH$ |
|---|---|---|
| At $\omega_2 = 10$ rad/s (where $\lvert GH \rvert = 0$ dB) | 0 dB | $-135°$ |
| At $\omega_1 = 31$ rad/s (where $\angle GH = -180°$) | $-12$ dB | $-180°$ |

**Phase margin**: we use the definition $\mathrm{PM} = 180° + \angle GH(\omega_2)$. At $\omega_2 = 10$ rad/s:

$$\mathrm{PM} = 180° + (-135°) = 45°.$$

This means we could add $45°$ of extra phase lag (e.g. from a time delay) before hitting instability.

**Gain margin**: we use the definition $\mathrm{GM}_{\mathrm{dB}} = -20 \log_{10} \lvert GH(\omega_1)\rvert = 0 - \lvert GH(\omega_1) \rvert_{\mathrm{dB}}$. At $\omega_1 = 31$ rad/s the magnitude is $-12$ dB, so:

$$\mathrm{GM} = 0 - (-12) = 12 \text{ dB}.$$

This means we could increase the loop gain by 12 dB (a factor of $10^{12/20} = 4.0$) before hitting instability.

**Is the system stable?** Both margins are positive $\implies$ **yes**.

**Follow-up: maximum tolerable time delay.**

A pure delay of $\tau$ seconds adds phase $= -\omega\tau$ radians. At the 0-dB crossover frequency $\omega_2 = 10$ rad/s, the maximum extra phase is the phase margin:

$$\omega_2 \cdot \tau_{\max} = 45° \times \frac{\pi}{180°} = 0.785 \text{ rad} \implies \tau_{\max} = \frac{0.785}{10} = 0.079 \text{ s} \approx 79 \text{ ms}.$$

### Warning
- If the phase *never* reaches $-180°$, the gain margin is infinite (you can crank up the gain as much as you like). First-order systems are like this.
- The gain margin tells you how much you can *increase* the gain. Some systems also go unstable if the gain is *decreased* (conditionally stable systems).
- Both margins positive $\implies$ stable. Either margin zero or negative $\implies$ unstable (or marginally stable).

## 7. Feedback Can Cause Instability

Feedback is not automatically good. Two classic scenarios:

**Audio feedback**: a microphone picks up sound from a speaker, the amplifier boosts it, and the speaker plays it louder. If the round-trip gain exceeds 1 ($K_1 K_2 > 1$), the signal grows without bound, producing the familiar squeal.

**Too much gain in a control system**: the telescope-pointing system from the textbook is stable for moderate gain. If the gain is set too high, the system overshoots, overcorrects, and oscillations grow (the closed-loop poles cross into the right-half plane).

## 8. CT vs. DT Feedback: Quick Reference

| | Continuous-time | Discrete-time |
|---|---|---|
| Closed-loop formula | $H(s)/[1 + G(s)H(s)]$ | $H(z)/[1 + G(z)H(z)]$ |
| Stability boundary | Imaginary axis ($j\omega$) | Unit circle ($\lvert z \rvert = 1$) |
| Stable poles | $\mathrm{Re}\{s\} < 0$ | $\lvert z \rvert < 1$ |
| Stability interpretation | Left-half plane | Inside unit circle |

## 9. Summary

1. $Q = H/(1 + GH)$. The denominator $1 + GH$ determines the closed-loop poles.
2. Simplify block diagrams with three rules: cascade ($\times$), parallel ($+$), feedback loop ($H/(1 + GH)$).
3. Nyquist plot: plot $GH(j\omega)$ in the complex plane. If the curve encircles $-1/K$, the system is unstable (assuming stable open-loop).
4. Gain margin: how many dB of gain you can add before instability (measured at the $-180°$ phase crossing). Phase margin: how many degrees of phase lag you can add before instability (measured at the 0-dB gain crossing).
5. Instability condition: $GH = -1$ (magnitude $= 0$ dB, phase $= -180°$, simultaneously).

## 10. Common Mistakes to Avoid

### Common Mistake
1. **Sign error at the summer**: negative feedback $\to 1 + GH$; positive feedback $\to 1 - GH$.
2. **Confusing open-loop and closed-loop poles**: the poles of $GH$ are the open-loop poles. The closed-loop poles are the roots of $1 + KGH = 0$, which change with $K$.
3. **CT vs. DT stability**: left-half plane in CT, inside unit circle in DT.
4. **Reading margins from the wrong curve**: gain margin is read from the *magnitude* plot at the frequency found from the *phase* plot, and vice versa. Do not mix them up.
5. **Forgetting to multiply cascaded blocks**: series $\to$ product, not sum.

## 11. Practice Problems

### Block Diagram Simplification

1. **(Cascade + Feedback)** Simplify the following to a single transfer function $Q(s) = Y/X$.

   *[Figure: input $X$ into summer (−), into block $\dfrac{2}{s+1}$, into block $\dfrac{1}{s+4}$, out as $Y$; unity feedback from $Y$ to negative summer input.]*

2. **(Parallel + Feedback)** Simplify the following.

   *[Figure: input $X$ into summer (−); summer output splits into two parallel blocks $\dfrac{3}{s+2}$ and $\dfrac{1}{s+5}$ whose outputs go into a plus-summer; combined output is $Y$; $Y$ feeds back through block $4$ to the negative input of the first summer.]*

3. **(Nested Loops)** Find $Q(s) = Y/X$.

   *[Figure: input $X$ into outer summer (−), into inner summer (−), into block $\dfrac{1}{s}$, out as $Y$. Inner loop: $Y$ feeds back through block $3$ to the negative input of the inner summer. Outer loop: $Y$ feeds back through block $1$ to the negative input of the outer summer.]*

### Closed-Loop Poles and Stability

4. A unity-feedback system has $H(s) = K/(s+5)$, $G = 1$.
   (a) Find the closed-loop transfer function and the closed-loop pole.
   (b) For what values of $K$ is the system stable?
   (c) What value of $K$ places the pole at $s = -10$?

5. A feedback system has $H(s) = K/[(s+1)(s+2)]$, $G = 1$.
   (a) Write the characteristic equation (denominator $= 0$).
   (b) For what range of $K$ is the system stable?

6. A DT feedback system has $H(z) = Kz^{-1}/(1 - 0.8z^{-1})$, $G = 1$.
   (a) Find the closed-loop pole as a function of $K$.
   (b) For what range of $K > 0$ is the system stable?

### Gain and Phase Margins

7. From a Bode plot you read:
   - At $\omega_2 = 5$ rad/s (where $\lvert GH \rvert = 0$ dB): $\angle GH = -150°$.
   - At $\omega_1 = 20$ rad/s (where $\angle GH = -180°$): $\lvert GH \rvert = -8$ dB.

   (a) What is the phase margin?
   (b) What is the gain margin (in dB)?
   (c) Is the system stable?
   (d) What is the maximum tolerable additional time delay?

### True/False

8. Negative feedback always stabilizes a system.

9. If the phase margin is $60°$, the system is stable.

10. A Nyquist plot is constructed by evaluating $G(j\omega)H(j\omega)$ and plotting it in the complex plane.

## Practice Problems Summary

1. **Problem 1 (Cascade + Feedback):** Simplify a unity-feedback block diagram with two cascaded forward blocks $\tfrac{2}{s+1}$ and $\tfrac{1}{s+4}$ to a single closed-loop transfer function $Q(s) = Y/X$.
2. **Problem 2 (Parallel + Feedback):** Simplify a block diagram with two parallel forward blocks $\tfrac{3}{s+2}$ and $\tfrac{1}{s+5}$ and a feedback gain of $4$ to a single transfer function.
3. **Problem 3 (Nested Loops):** Find $Q(s) = Y/X$ for a system with an integrator $\tfrac{1}{s}$ in the forward path, an inner feedback loop with gain $3$, and an outer unity feedback loop.
4. **Problem 4 (Unity feedback, first-order):** For $H(s) = K/(s+5)$: find the closed-loop transfer function and pole, determine the range of $K$ for stability, and find the $K$ that places the pole at $s = -10$.
5. **Problem 5 (Unity feedback, second-order):** For $H(s) = K/[(s+1)(s+2)]$: write the characteristic equation and find the range of $K$ for stability.
6. **Problem 6 (DT feedback):** For $H(z) = Kz^{-1}/(1 - 0.8z^{-1})$ with unity feedback: find the closed-loop pole as a function of $K$ and determine for what $K > 0$ the system is stable.
7. **Problem 7 (Margins from Bode data):** Given Bode-plot readings at the gain and phase crossover frequencies, compute the phase margin, gain margin (in dB), determine stability, and find the maximum tolerable additional time delay.
8. **Problem 8 (True/False):** Evaluate whether negative feedback always stabilizes a system.
9. **Problem 9 (True/False):** Evaluate whether a phase margin of $60°$ implies the system is stable.
10. **Problem 10 (True/False):** Evaluate whether a Nyquist plot is constructed by evaluating $G(j\omega)H(j\omega)$ and plotting it in the complex plane.

---

## Worked Examples (from Official Solutions)

**Source:** [lctr23-exercise-solutions.md](../hw_practice_problems/lctr23-exercise-solutions.md) — work through the problems before reading the solutions.

- **Problem 1 (Block diagram — cascade + unity feedback):** $H_1 = 2/(s+1)$, $H_2 = 1/(s+4)$ $\to$ $Q(s) = 2/[(s+2)(s+3)]$; both poles in LHP $\Rightarrow$ stable.
- **Problem 2 (Parallel + feedback):** Parallel $3/(s+2) + 1/(s+5)$, feedback $G = 4$ $\to$ $Q(s) = (4s+17)/(s^2 + 23s + 78)$; stable.
- **Problem 3 (Nested loops):** Simplify innermost first — inner forward $1/s$, inner feedback $3$ gives $1/(s+3)$; then outer unity feedback gives $Q(s) = 1/(s+4)$.
- **Problem 4 (Unity feedback, $H = K/(s+5)$):**
  - **(a)** $Q(s) = K/(s + 5 + K)$, pole at $-(5+K)$.
  - **(b)** Stable for $K > -5$.
  - **(c)** $K = 5$ places the pole at $s = -10$.
- **Problem 5 (Second-order, $H = K/[(s+1)(s+2)]$):**
  - **(a)** Characteristic equation: $s^2 + 3s + (2+K) = 0$.
  - **(b)** Stable for $K > -2$ (second-order Routh: both coeffs positive).
- **Problem 6 (DT feedback, $H(z) = Kz^{-1}/(1 - 0.8z^{-1})$):**
  - **(a)** Closed-loop pole at $z = 0.8 - K$.
  - **(b)** Stable ($|z_{\text{cl}}|<1$) for $0 < K < 1.8$.
- **Problem 7 (Margins from Bode data):** At $\omega_{gc}=5$ (0 dB), $\angle GH = -150^\circ$; at $\omega_{pc}=20$ ($-180^\circ$), $|GH| = -8$ dB.
  - **(a)** PM $= 180^\circ + (-150^\circ) = 30^\circ$.
  - **(b)** GM $= 0 - (-8) = 8$ dB.
  - **(c)** Both positive $\Rightarrow$ stable.
  - **(d)** $\tau_{\max} = \text{PM(rad)}/\omega_{gc} = 0.524/5 \approx 105$ ms.
- **Problem 8 (T/F):** "Negative feedback always stabilizes" — **FALSE** (enough loop gain pushes poles into the RHP).
- **Problem 9 (T/F):** "PM of $60^\circ$ $\Rightarrow$ stable" — **TRUE** (assuming positive GM too; $60^\circ$ is a well-damped design target).
- **Problem 10 (T/F):** Nyquist plot is $G(j\omega)H(j\omega)$ plotted in the complex plane — **TRUE**.

## Instructor Emphasis (from Official Study Guide)

- **Feedback formula:** $Q = H/(1 + GH)$ (negative feedback); $1 - GH$ in the denominator for positive feedback.
- **Strategy:** simplify innermost loop first, then work outward.
- Closed-loop stability: all closed-loop poles in LHP (CT) or inside unit circle (DT).
- Instability $\iff$ $GH = -1$ (i.e., $|GH| = 0$ dB **and** $\angle GH = -180^\circ$ simultaneously).
- **Reading Bode plots (instructor warning):** GM from the **magnitude** plot at the $-180^\circ$ frequency; PM from the **phase** plot at the 0-dB frequency. Don't mix them up.
- $\tau_{\max} = \text{PM(rad)}/\omega_{gc}$ — maximum tolerable pure delay.
- Nyquist criterion (simplified): open-loop stable $\Rightarrow$ closed-loop (gain $K$) stable iff the Nyquist contour does not encircle $-1/K$.
