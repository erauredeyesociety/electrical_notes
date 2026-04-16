# CEC 315 — Lecture 23 Feedback Systems: Official Solutions

**Course:** CEC 315 Signals and Systems
**Term:** Spring 2026
**Topic:** Lecture 23 — Feedback systems, block diagram simplification, closed-loop poles, stability, gain/phase margins, Nyquist
**Exam coverage:** Exam 3
**Source:** Transcribed from `lctr23-exercise-solutions.pdf` (instructor solutions).

---

## Block Diagram Simplification

### Problem 1 — Cascade + Feedback

The forward path is two blocks in cascade:

$$
H(s) = \frac{2}{s+1} \cdot \frac{1}{s+4} = \frac{2}{(s+1)(s+4)}.
$$

The feedback path is unity ($G = 1$). Apply the feedback formula $Q = H/(1 + GH)$:

$$
Q(s) = \frac{H(s)}{1 + G\cdot H(s)} = \frac{\dfrac{2}{(s+1)(s+4)}}{1 + \dfrac{2}{(s+1)(s+4)}}.
$$

Multiply numerator and denominator by $(s+1)(s+4)$:

$$
Q(s) = \frac{2}{(s+1)(s+4) + 2} = \frac{2}{s^2 + 5s + 4 + 2} = \frac{2}{s^2 + 5s + 6} = \frac{2}{(s+2)(s+3)}.
$$

$$
\boxed{\;Q(s) = \frac{2}{s^2 + 5s + 6} = \frac{2}{(s+2)(s+3)}\;}
$$

**Closed-loop poles:** $s = -2$ and $s = -3$. Both negative $\implies$ **stable**.

---

### Problem 2 — Parallel + Feedback

**Step 1 — Parallel combination:** The two blocks in parallel add:

$$
H(s) = \frac{3}{s+2} + \frac{1}{s+5} = \frac{3(s+5) + (s+2)}{(s+2)(s+5)} = \frac{4s + 17}{(s+2)(s+5)} = \frac{4s + 17}{s^2 + 7s + 10}.
$$

**Step 2 — Feedback:** Forward $= H(s)$, feedback $G = 4$. Apply $Q = H/(1 + GH)$:

$$
Q(s) = \frac{H(s)}{1 + 4H(s)} = \frac{\dfrac{4s+17}{s^2+7s+10}}{1 + \dfrac{4(4s+17)}{s^2+7s+10}} = \frac{4s + 17}{s^2 + 7s + 10 + 16s + 68}.
$$

$$
\boxed{\;Q(s) = \frac{4s + 17}{s^2 + 23s + 78}\;}
$$

**Check stability:** $s^2 + 23s + 78 = 0$. Quadratic formula:

$$
s = \frac{-23 \pm \sqrt{529 - 312}}{2} = \frac{-23 \pm \sqrt{217}}{2} = \frac{-23 \pm 14.73}{2}.
$$

So $s \approx -4.14$ and $s \approx -18.87$. Both negative $\implies$ **stable**.

---

### Problem 3 — Nested Loops

**Step 1 — Inner loop:** Forward path $= 1/s$, feedback path $= 3$:

$$
Q_{\text{inner}}(s) = \frac{1/s}{1 + 3/s} = \frac{1/s}{(s+3)/s} = \frac{1}{s + 3}.
$$

**Step 2 — Outer loop:** Forward path $= Q_{\text{inner}} = 1/(s+3)$, feedback path $= 1$:

$$
Q(s) = \frac{1/(s+3)}{1 + 1/(s+3)} = \frac{1/(s+3)}{(s+4)/(s+3)} = \frac{1}{s + 4}.
$$

$$
\boxed{\;Q(s) = \frac{1}{s + 4}\;}
$$

**Closed-loop pole:** $s = -4$. **Stable.**

**Strategy reminder:** Always start with the innermost loop. Replace it with a single block. Then treat the result as the forward path of the outer loop.

---

## Closed-Loop Poles and Stability

### Problem 4 — Unity Feedback with $H(s) = K/(s+5)$

**Part (a).** Forward: $H = K/(s+5)$, feedback: $G = 1$. Apply $Q = H/(1 + GH)$:

$$
Q(s) = \frac{K/(s+5)}{1 + K/(s+5)} = \frac{K}{s + 5 + K}.
$$

**Characteristic equation:** $s + 5 + K = 0$. **Closed-loop pole:** $s = -(5 + K)$.

$$
\boxed{\;Q(s) = \frac{K}{s + 5 + K}, \qquad s_{\text{cl}} = -(5 + K)\;}
$$

**Part (b).** For stability (CT: pole must be in LHP), we need $5 + K > 0$:

$$
\boxed{\;K > -5\;}
$$

**Part (c).** We want $s = -10$: $-(5 + K) = -10 \implies \boxed{\;K = 5\;}$.

---

### Problem 5 — Second-Order Feedback with $H(s) = K/[(s+1)(s+2)]$

**Part (a).** Apply $Q = H/(1 + GH)$ with $G = 1$:

$$
Q(s) = \frac{K/[(s+1)(s+2)]}{1 + K/[(s+1)(s+2)]} = \frac{K}{(s+1)(s+2) + K} = \frac{K}{s^2 + 3s + (2 + K)}.
$$

**Characteristic equation:**

$$
\boxed{\;s^2 + 3s + (2 + K) = 0\;}
$$

**Part (b).** For a second-order polynomial $s^2 + bs + c$ to have both roots in the left-half plane, we need $b > 0$ and $c > 0$.

- Here $b = 3 > 0$ always.
- $c = 2 + K > 0$ requires $K > -2$.

$$
\boxed{\;K > -2\;}
$$

**Verification at the boundary:** At $K = -2$, the characteristic equation is $s^2 + 3s = s(s+3) = 0$, giving poles at $s = 0$ and $s = -3$. The pole at $s = 0$ is on the imaginary axis, confirming marginal stability at the boundary.

---

### Problem 6 — DT Feedback with $H(z) = K z^{-1}/(1 - 0.8 z^{-1})$

Forward: $H(z) = K z^{-1}/(1 - 0.8 z^{-1})$. Feedback: $G = 1$. Apply $Q = H/(1 + GH)$:

$$
Q(z) = \frac{K z^{-1}/(1 - 0.8 z^{-1})}{1 + K z^{-1}/(1 - 0.8 z^{-1})} = \frac{K z^{-1}}{1 - 0.8 z^{-1} + K z^{-1}} = \frac{K z^{-1}}{1 + (K - 0.8) z^{-1}}.
$$

Rewriting in terms of $z$ (multiply numerator and denominator by $z$):

$$
Q(z) = \frac{K}{z + (K - 0.8)}.
$$

**Part (a).** Closed-loop pole: $z = -(K - 0.8) = 0.8 - K$.

$$
\boxed{\;z_{\text{cl}} = 0.8 - K\;}
$$

**Part (b).** DT stability requires $|z_{\text{cl}}| < 1$:

$$
|0.8 - K| < 1 \;\Longleftrightarrow\; -1 < 0.8 - K < 1 \;\Longleftrightarrow\; -0.2 < K < 1.8.
$$

For $K > 0$:

$$
\boxed{\;0 < K < 1.8\;}
$$

**Check:** At $K = 1$, pole at $z = -0.2$ (inside unit circle, stable). At $K = 1.8$, pole at $z = -1$ (on the unit circle, marginally stable). At $K = 2$, pole at $z = -1.2$ (outside, unstable).

---

## Gain and Phase Margins

### Problem 7 — Margins from Bode Data

Given data:

| $\omega$                                   | $\lvert GH\rvert$ (dB) | $\angle GH$     |
|--------------------------------------------|------------------------|-----------------|
| $\omega_2 = 5$ rad/s (where $|GH| = 0$ dB) | $0$ dB                 | $-150^\circ$    |
| $\omega_1 = 20$ rad/s (where $\angle GH = -180^\circ$) | $-8$ dB       | $-180^\circ$    |

**Part (a) — Phase margin.** Use the 0-dB crossing frequency $\omega_2 = \omega_{gc} = 5$ rad/s. By definition $\text{PM} = 180^\circ + \angle GH(\omega_{gc})$:

$$
\text{PM} = 180^\circ + \angle GH(\omega_2) = 180^\circ + (-150^\circ) = 30^\circ.
$$

$$
\boxed{\;\text{PM} = 30^\circ\;}
$$

**Part (b) — Gain margin.** Use the $-180^\circ$ phase-crossing frequency $\omega_1 = 20$ rad/s. By definition $\text{GM} = 0\text{ dB} - |GH|_{\text{dB}}$ at that frequency:

$$
\text{GM} = 0 \text{ dB} - |GH(\omega_1)|_{\text{dB}} = 0 - (-8) = 8 \text{ dB}.
$$

$$
\boxed{\;\text{GM} = 8 \text{ dB}\;}
$$

**Part (c) — Stability.** Both margins are positive $\implies$ **stable**.

$$
\boxed{\;\text{Stable}\;}
$$

**Part (d) — Maximum tolerable additional time delay.** A pure delay of $\tau$ seconds contributes phase $-\omega\tau$ radians (no gain change). The binding constraint is at the gain-crossover frequency $\omega_{gc} = \omega_2 = 5$ rad/s, where the system can tolerate $30^\circ$ (i.e. PM) of extra negative phase before instability:

$$
\omega_2 \cdot \tau_{\max} = 30^\circ \times \frac{\pi}{180^\circ} = 0.524 \text{ rad} \;=\; \text{PM(rad)}.
$$

$$
\tau_{\max} = \frac{\text{PM(rad)}}{\omega_{gc}} = \frac{0.524}{5} = 0.105 \text{ s} \approx 105 \text{ ms}.
$$

$$
\boxed{\;\tau_{\max} \approx 0.105 \text{ s} = 105 \text{ ms}\;}
$$

---

## True/False

### Problem 8 — "Negative feedback always stabilizes a system."

$$
\boxed{\;\textbf{FALSE}\;}
$$

**Explanation:** Negative feedback *can* stabilize an unstable open-loop system, but it can also destabilize a stable open-loop system if the loop gain is too high. The classical audio-feedback example (squealing microphone) and Example 23.5 in the lecture (which goes unstable for $K > 12$) both show that enough gain in the loop will push closed-loop poles into the RHP. Whether feedback stabilizes depends on the loop transfer function $GH$ and the gain $K$, not on the sign of the summer alone.

---

### Problem 9 — "If the phase margin is $60^\circ$, the system is stable."

$$
\boxed{\;\textbf{TRUE}\;}
$$

**Explanation:** A positive phase margin means that at the gain-crossover frequency the loop phase has not yet reached $-180^\circ$, so the system has not reached the instability condition $GH = -1$. In standard exam problems we also implicitly assume the gain margin is positive, so a positive (in fact generous $60^\circ$) phase margin indicates stability. $60^\circ$ is, in fact, a common "well-damped" design target.

---

### Problem 10 — "A Nyquist plot is constructed by evaluating $G(j\omega)H(j\omega)$ and plotting it in the complex plane."

$$
\boxed{\;\textbf{TRUE}\;}
$$

**Explanation:** At each frequency $\omega$, you evaluate the complex number $GH(j\omega)$ (magnitude and phase) and plot it as a point in the complex plane. Connecting all such points for $\omega$ running from $-\infty$ to $+\infty$ traces out the Nyquist contour. Instability is then diagnosed from encirclements of the critical point ($-1$ for unit loop gain, or $-1/K$ when the gain $K$ is factored out of $GH$).

---

## Key Takeaways

1. **Closed-loop formula:** $Q = \dfrac{H}{1 + GH}$. The denominator $1 + GH$ determines the closed-loop poles. For unity feedback ($G = 1$), this reduces to $H/(1 + H)$.
2. **Block diagram simplification — three rules:** cascade (multiply), parallel (add), feedback loop (apply $H/(1 + GH)$). Always reduce innermost loops first.
3. **Continuous-time stability:** All closed-loop poles must lie in the **left-half plane** ($\text{Re}\{s\} < 0$).
4. **Discrete-time stability:** All closed-loop poles must lie **inside the unit circle** ($|z| < 1$).
5. **Characteristic equation:** Set $1 + GH = 0$ (or equivalently the closed-loop denominator $= 0$); this is how the stable range of $K$ is determined symbolically.
6. **Instability condition:** $GH = -1$, i.e. $|GH| = 0$ dB *and* $\angle GH = -180^\circ$ simultaneously.
7. **Phase margin (PM):** measured at the 0-dB gain-crossover frequency $\omega_{gc}$:
   $$\text{PM} = 180^\circ + \angle GH(\omega_{gc}).$$
8. **Gain margin (GM):** measured at the $-180^\circ$ phase-crossover frequency $\omega_{pc}$:
   $$\text{GM} = 0 \text{ dB} - |GH(\omega_{pc})|_{\text{dB}} = -|GH(\omega_{pc})|_{\text{dB}}.$$
9. **Max tolerable time delay** (from PM):
   $$\tau_{\max} = \frac{\text{PM (in radians)}}{\omega_{gc}}.$$
10. **Nyquist criterion:** Plot $GH(j\omega)$ in the complex plane. For a stable open-loop system, closed-loop stability requires that the Nyquist curve not encircle the critical point $-1/K$. Encirclements of $-1/K$ indicate RHP closed-loop poles.
