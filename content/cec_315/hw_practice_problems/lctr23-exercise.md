# CEC 315 — Lecture 23 Exercise: Feedback Systems Practice

**Source PDF:** `hw_practice_problems/lctr23-exercise.pdf`
**Lectures covered:** Lecture 23: Feedback systems, block diagram simplification, closed-loop poles, stability, gain/phase margins, Nyquist
**Exam coverage:** Exam 3

---

## Reference Tables and Summary (from PDF)

### CT vs. DT Feedback: Quick Reference

|                          | Continuous-time              | Discrete-time                   |
|--------------------------|------------------------------|---------------------------------|
| Closed-loop formula      | $H(s)/[1 + G(s)H(s)]$        | $H(z)/[1 + G(z)H(z)]$           |
| Stability boundary       | Imaginary axis ($j\omega$)   | Unit circle ($|z| = 1$)         |
| Stable poles             | $\mathrm{Re}\{s\} < 0$       | $|z| < 1$                       |
| Stability interpretation | Left-half plane              | Inside unit circle              |

### Summary

1. $Q = H/(1 + GH)$. The denominator $1 + GH$ determines the closed-loop poles.
2. Simplify block diagrams with three rules: cascade ($\times$), parallel ($+$), feedback loop ($H/(1 + GH)$).
3. Nyquist plot: plot $GH(j\omega)$ in the complex plane. If the curve encircles $-1/K$, the system is unstable (assuming stable open-loop).
4. Gain margin: how many dB of gain you can add before instability (measured at the $-180^\circ$ phase crossing). Phase margin: how many degrees of phase lag you can add before instability (measured at the 0-dB gain crossing).
5. Instability condition: $GH = -1$ (magnitude $= 0$ dB, phase $= -180^\circ$, simultaneously).

### Common Mistakes to Avoid

1. **Sign error at the summer**: negative feedback $\to 1 + GH$; positive feedback $\to 1 - GH$.
2. **Confusing open-loop and closed-loop poles**: the poles of $GH$ are the open-loop poles. The closed-loop poles are the roots of $1 + KGH = 0$, which change with $K$.
3. **CT vs. DT stability**: left-half plane in CT, inside unit circle in DT.
4. **Reading margins from the wrong curve**: gain margin is read from the *magnitude* plot at the frequency found from the *phase* plot, and vice versa. Do not mix them up.
5. **Forgetting to multiply cascaded blocks**: series $\to$ product, not sum.

---

## Practice Problems

### Block Diagram Simplification

## Problem 1

**(Cascade + Feedback)** Simplify the following to a single transfer function $Q(s) = Y/X$.

*[Figure: Block diagram. Input $X$ enters a summing junction (with the feedback subtracted, marked $-$). Output of summer feeds block $\frac{2}{s+1}$, then block $\frac{1}{s+4}$, producing output $Y$. $Y$ is fed back directly to the summing junction.]*

## Problem 2

**(Parallel + Feedback)** Simplify the following.

*[Figure: Block diagram. Input $X$ enters a summing junction (feedback subtracted). The summer output branches into two parallel paths: upper path $\frac{3}{s+2}$ and lower path $\frac{1}{s+5}$; the two paths recombine at a summing junction (both added, marked $+$) to produce $Y$. $Y$ is fed back through a block of gain $4$ to the input summer.]*

## Problem 3

**(Nested Loops)** Find $Q(s) = Y/X$.

*[Figure: Block diagram with two nested feedback loops. Input $X$ enters an outer summing junction (marked $-$), whose output enters an inner summing junction (marked $-$), whose output feeds block $\frac{1}{s}$ producing $Y$. Inner loop feedback: $Y$ passes through block of gain $3$ back to the inner summer. Outer loop feedback: $Y$ passes through block of gain $1$ back to the outer summer. Labels: "inner loop" on the inner feedback, "outer loop" on the outer feedback.]*

### Closed-Loop Poles and Stability

## Problem 4

A unity-feedback system has $H(s) = K/(s + 5)$, $G = 1$.

### Part (a)
Find the closed-loop transfer function and the closed-loop pole.

### Part (b)
For what values of $K$ is the system stable?

### Part (c)
What value of $K$ places the pole at $s = -10$?

## Problem 5

A feedback system has $H(s) = K/[(s + 1)(s + 2)]$, $G = 1$.

### Part (a)
Write the characteristic equation (denominator $= 0$).

### Part (b)
For what range of $K$ is the system stable?

## Problem 6

A DT feedback system has $H(z) = Kz^{-1}/(1 - 0.8z^{-1})$, $G = 1$.

### Part (a)
Find the closed-loop pole as a function of $K$.

### Part (b)
For what range of $K > 0$ is the system stable?

### Gain and Phase Margins

## Problem 7

From a Bode plot you read:

- At $\omega_2 = 5$ rad/s (where $|GH| = 0$ dB): $\angle GH = -150^\circ$.
- At $\omega_1 = 20$ rad/s (where $\angle GH = -180^\circ$): $|GH| = -8$ dB.

### Part (a)
What is the phase margin?

### Part (b)
What is the gain margin (in dB)?

### Part (c)
Is the system stable?

### Part (d)
What is the maximum tolerable additional time delay?

### True/False

## Problem 8

Negative feedback always stabilizes a system.

## Problem 9

If the phase margin is $60^\circ$, the system is stable.

## Problem 10

A Nyquist plot is constructed by evaluating $G(j\omega)H(j\omega)$ and plotting it in the complex plane.

---

## Problem Index

- **Problem 1:** Simplify a cascade-plus-unity-feedback block diagram (two first-order blocks $\frac{2}{s+1}$ and $\frac{1}{s+4}$) to a single $Q(s) = Y/X$.
- **Problem 2:** Simplify a parallel-plus-feedback block diagram (parallel paths $\frac{3}{s+2}$ and $\frac{1}{s+5}$ with feedback gain $4$).
- **Problem 3:** Find $Q(s) = Y/X$ for a nested-loop block diagram with inner loop gain $3$ around $\frac{1}{s}$ and outer unity feedback.
- **Problem 4:** Unity-feedback system with $H(s) = K/(s+5)$; find closed-loop TF, range of $K$ for stability, and $K$ placing the pole at $s=-10$.
- **Problem 5:** Feedback system with $H(s) = K/[(s+1)(s+2)]$; write the characteristic equation and find the stable range of $K$.
- **Problem 6:** DT feedback system with $H(z) = Kz^{-1}/(1 - 0.8z^{-1})$; find closed-loop pole vs $K$ and stable range of $K > 0$.
- **Problem 7:** From Bode plot readings at $\omega = 5$ and $\omega = 20$ rad/s, compute phase margin, gain margin, stability, and max tolerable time delay.
- **Problem 8:** True/False — Negative feedback always stabilizes a system.
- **Problem 9:** True/False — Phase margin of $60^\circ$ implies stability.
- **Problem 10:** True/False — Nyquist plot is $G(j\omega)H(j\omega)$ plotted in the complex plane.
