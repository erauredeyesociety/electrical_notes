# CEC 315 — Signals and Systems

**Exam: Lectures 16–23  (Exam 3 — MOCK)**

Rogelio Gracia Otalvaro — Spring 2026

---

**Name:** ________________________          **Date:** ________________________

## Instructions

- Total time: **60 minutes**. Total points: **100**.
- Show all work clearly. Box your final answers.
- Make sure your answers are clear and easy to understand.
- Read the text carefully and understand the questions, there is plenty of time.
- Assume all systems are causal and stable unless stated otherwise.

## Useful Formulas

- **Laplace pairs (one-sided):**
  $u(t)\leftrightarrow 1/s$,  $e^{-at}u(t)\leftrightarrow 1/(s+a)$,  $te^{-at}u(t)\leftrightarrow 1/(s+a)^2$

  $\cos(\omega_0 t)u(t)\leftrightarrow s/(s^2+\omega_0^2)$,  $\sin(\omega_0 t)u(t)\leftrightarrow \omega_0/(s^2+\omega_0^2)$

- **Unilateral Laplace derivative rule:**
  $\mathcal{L}\{y'(t)\} = sY(s) - y(0^-)$,  $\mathcal{L}\{y''(t)\} = s^2Y(s) - sy(0^-) - y'(0^-)$

- **Z pairs:**
  $a^n u[n]\leftrightarrow 1/(1-az^{-1}),\ |z|>|a|$;  $-a^n u[-n-1]\leftrightarrow 1/(1-az^{-1}),\ |z|<|a|$

  $(n+1)a^n u[n]\leftrightarrow 1/(1-az^{-1})^2$,  $na^n u[n]\leftrightarrow az^{-1}/(1-az^{-1})^2$

- **Unilateral Z shift rule:**
  $\mathcal{Z}\{y[n-1]\} = z^{-1}Y(z) + y[-1]$,  $\mathcal{Z}\{y[n-2]\} = z^{-2}Y(z) + z^{-1}y[-1] + y[-2]$

- **Sampling theorem:** To reconstruct $x(t)$ without aliasing, sample at $\omega_s > 2\omega_M$.
- **Closed loop (negative feedback):** $Q(s) = \dfrac{G(s)}{1+G(s)H(s)}$.

---

## Part I: Multiple Choice  (5 questions × 4 points = 20 points)

Circle the single best answer for each question.

**1.** A continuous-time signal has Fourier transform $X(j\omega)=0$ for $|\omega|>1500\pi$ rad/s. Which of the following sampling periods $T$ guarantees perfect reconstruction from the samples?

  (a) $T = 1.0$ ms
  (b) $T = 0.5$ ms
  (c) $T = 2.0$ ms
  (d) $T = 0.75$ ms

**2.** A signal $x(t) = \cos(600\pi t)$ is sampled at $f_s = 400$ Hz. The reconstructed signal after an ideal lowpass filter with cutoff $f_s/2$ is a cosine of frequency:

  (a) $300$ Hz
  (b) $200$ Hz
  (c) $100$ Hz
  (d) $0$ Hz (DC)

**3.** A causal LTI system has transfer function $H(s) = \dfrac{s+4}{(s+1)(s-2)}$. The system is:

  (a) Stable, because it has a zero in the LHP.
  (b) Stable, because two of its three singularities lie in the LHP.
  (c) Unstable, because one pole is in the RHP.
  (d) Marginally stable, because $|{-2}|<5$.

**4.** The open-loop transfer function of a unity-feedback system is $G(s) = \dfrac{K}{s(s+4)}$. For what range of $K$ is the closed-loop system stable?

  (a) $K < 0$
  (b) $K > 0$
  (c) $0 < K < 4$
  (d) All real $K$ (it is always stable)

**5.** A discrete-time signal has Z-transform $X(z)$ with poles at $z=0.3$ and $z=1.5$, and the signal is known to be two-sided (neither purely causal nor purely anti-causal). Which ROC is correct?

  (a) $|z| > 1.5$
  (b) $|z| < 0.3$
  (c) $0.3 < |z| < 1.5$
  (d) $|z| > 0.3$

---

## Part II: Problems  (4 problems × 20 points = 80 points)

---

### Problem 1: Laplace Transform, ROC, and Inverse via PFE  (20 points)

Consider the Laplace transform
$$X(s) = \frac{7s + 2}{(s+2)(s-1)}, \qquad \text{ROC: } -2 < \operatorname{Re}\{s\} < 1.$$

  (a) **(4 pts)** Locate the poles of $X(s)$ in the $s$-plane and sketch the ROC.

  (b) **(8 pts)** Perform a partial fraction expansion of $X(s)$. Show your cover-up work.

  (c) **(6 pts)** Use the given ROC to determine whether each term corresponds to a right-sided or left-sided signal, and write the time-domain signal $x(t)$.

  (d) **(2 pts)** Does the bilateral Fourier transform $X(j\omega)$ exist? Justify in one sentence.

---

### Problem 2: Unilateral Laplace — Second-Order IVP with ZSR/ZIR  (20 points)

A causal LTI system is governed by
$$\frac{d^2 y}{dt^2} + 4\,\frac{dy}{dt} + 3\,y(t) \;=\; 2\,u(t),$$
with initial conditions $y(0^-) = 2$ and $y'(0^-) = -1$.

  (a) **(4 pts)** Take the unilateral Laplace transform of both sides and solve algebraically for $Y(s)$ as a single rational function.

  (b) **(4 pts)** Decompose $Y(s) = Y_{\text{zir}}(s) + Y_{\text{zsr}}(s)$, where $Y_{\text{zir}}(s)$ is the zero-input response (input set to zero, ICs kept) and $Y_{\text{zsr}}(s)$ is the zero-state response (ICs set to zero, input kept).

  (c) **(8 pts)** Invert both pieces via partial fractions and write $y_{\text{zir}}(t)$ and $y_{\text{zsr}}(t)$ as explicit functions of $t$ for $t \ge 0$.

  (d) **(4 pts)** Write the total response $y(t)$ and verify that it satisfies the initial conditions $y(0^-)=2$ and $y'(0^-)=-1$. Also state $y(\infty)$.

---

### Problem 3: Z-Transform, ROC, and Inverse with Mixed ROC  (20 points)

A discrete-time signal $x[n]$ has Z-transform
$$X(z) = \frac{1 + z^{-1}}{\bigl(1 - 0.4\,z^{-1}\bigr)\bigl(1 + 0.2\,z^{-1}\bigr)}, \qquad \text{ROC: } 0.2 < |z| < 0.4.$$

  (a) **(3 pts)** Locate the poles and the zero. Sketch the pole-zero plot and shade the ROC on the complex $z$-plane.

  (b) **(9 pts)** Perform a partial fraction expansion in $z^{-1}$. Show your cover-up calculations.

  (c) **(6 pts)** Use the given annular ROC to decide whether each pole contributes a right-sided or left-sided term. Write $x[n]$ explicitly.

  (d) **(2 pts)** Is $x[n]$ absolutely summable? Justify in one sentence using the ROC.

---

### Problem 4: Unilateral Z — Difference Equation with Initial Conditions  (20 points)

A causal discrete-time system satisfies
$$y[n] - \tfrac{1}{6}\,y[n-1] - \tfrac{1}{6}\,y[n-2] \;=\; x[n],$$
with input $x[n] = u[n]$ and initial conditions $y[-1] = 6$, $y[-2] = 0$.

  (a) **(4 pts)** Apply the unilateral Z-transform to the difference equation, carefully accounting for the initial conditions. Solve algebraically for $Y(z)$.

  (b) **(4 pts)** Factor the characteristic polynomial and identify the system poles in the $z$-plane. Is the system stable?

  (c) **(10 pts)** Perform a partial fraction expansion and invert to obtain $y[n]$ for $n \ge 0$ as an explicit closed-form expression.

  (d) **(2 pts)** Verify your answer by computing $y[0]$ and $y[1]$ directly from the difference equation and confirming that they match your closed-form $y[n]$.

---

*End of Exam — Mock Exam 3 — CEC 315, Spring 2026.*
