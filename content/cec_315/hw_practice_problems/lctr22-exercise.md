# CEC 315 — Lecture 22 Exercise: Sampling Practice Questions

**Source PDF:** `hw_practice_problems/lctr22-exercise.pdf`
**Lectures covered:** Lecture 22: Sampling theorem, Nyquist rate, aliasing, reconstruction
**Exam coverage:** Exam 3

---

## Common Mistakes (carry-over from start of section)

3. **Forgetting the $1/T$ scaling.** Replicas are scaled by $1/T$; the reconstruction filter compensates with gain $T$.
4. **Thinking aliasing can be undone.** It cannot. Prevent it before sampling.
5. **Claiming non-band-limited signals can't be sampled.** In practice, we band-limit with an anti-aliasing filter first.

## Practice Questions

Test your understanding with these quick questions. Answers are at the bottom of the section.

## Problem 1

A signal $x(t)$ has $X(j\omega) = 0$ for $|\omega| > 5000\pi$. What is the Nyquist rate? What is the maximum allowable sampling period $T$?

## Problem 2

True or false: if $\omega_s = 2\omega_M$, the sampling theorem guarantees perfect reconstruction.

## Problem 3

In one sentence, explain *why* sampling in time produces copies of the spectrum in the frequency domain.

## Problem 4

A signal is sampled and the resulting spectrum $X_p(j\omega)$ shows overlapping replicas. Can you undo the overlap with a clever filter? Why or why not?

## Problem 5

What is an anti-aliasing filter, and *where* in the signal chain does it go (before or after the sampler)?

## Problem 6

Determine the Nyquist rate for $x(t) = \cos(600\pi t) + \cos(1800\pi t)$.

## Problem 7

A signal with $\omega_M = 3000\pi$ is sampled with $T = 2 \times 10^{-4}$ s. Compute $\omega_s$ and state whether aliasing occurs.

## Problem 8

You sample $x(t) = \cos(2\pi \cdot 900\, t)$ at $f_s = 1000$ Hz. What frequency does the reconstructed signal have?

## Problem 9

Repeat the previous question for $f_s = 1500$ Hz.

## Problem 10

A signal has Nyquist rate $\omega_0$. What is the Nyquist rate of $x(t - 5)$? What about $x(2t)$?

## Problem 11

The ideal reconstruction filter has gain $T$ in its passband. Why is that factor of $T$ needed? (Hint: look at the $1/T$ scaling of the replicas.)

## Problem 12

A zero-order hold is used instead of an ideal lowpass filter for reconstruction. Is the result exact? What kind of error does it introduce?

## Problem 13

A movie camera shoots at 24 frames per second. A helicopter blade spins at 25 revolutions per second. Describe qualitatively what the blade looks like in the film.

## Problem 14

You are told that $X(j\omega) = 0$ for $|\omega| > 10{,}000\pi$. Someone samples $x(t)$ at $f_s = 8000$ Hz. Is the sampling theorem satisfied? If not, what is the minimum $f_s$ that works?

## Problem 15

Suppose $x(t)$ is *not* band-limited (its spectrum extends to $\pm\infty$). Does this mean we can never sample it in practice? Explain what is done in real systems.

*Rogelio Gracia Otalvaro*

---

## Problem Index

- **Problem 1:** Given $X(j\omega) = 0$ for $|\omega| > 5000\pi$, find the Nyquist rate and the maximum sampling period $T$.
- **Problem 2:** True/False — $\omega_s = 2\omega_M$ guarantees perfect reconstruction.
- **Problem 3:** Explain in one sentence why time-domain sampling produces spectral copies.
- **Problem 4:** Can overlapping replicas (aliasing) be undone after sampling via filtering? Justify.
- **Problem 5:** Define an anti-aliasing filter and state its placement in the signal chain.
- **Problem 6:** Nyquist rate for $x(t) = \cos(600\pi t) + \cos(1800\pi t)$.
- **Problem 7:** For $\omega_M = 3000\pi$ and $T = 2 \times 10^{-4}$ s, compute $\omega_s$ and check for aliasing.
- **Problem 8:** Reconstructed frequency of $\cos(2\pi\cdot 900\,t)$ sampled at $f_s = 1000$ Hz.
- **Problem 9:** Same as Problem 8 but $f_s = 1500$ Hz.
- **Problem 10:** Nyquist rates of $x(t-5)$ and $x(2t)$ given original rate $\omega_0$.
- **Problem 11:** Explain the factor-of-$T$ passband gain in the ideal reconstruction filter.
- **Problem 12:** Is zero-order-hold reconstruction exact, and what error does it introduce?
- **Problem 13:** Qualitative aliasing description for a 25 rev/s blade filmed at 24 fps.
- **Problem 14:** Given $|\omega| > 10{,}000\pi$ cutoff and $f_s = 8000$ Hz, check the sampling theorem and give the minimum $f_s$.
- **Problem 15:** How are non-band-limited signals sampled in practice?
