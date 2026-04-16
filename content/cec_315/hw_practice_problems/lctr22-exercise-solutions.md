# CEC 315 — Lecture 22 Sampling Exercise: Official Solutions

**Course:** CEC 315 — Signals and Systems
**Lecture:** 22 — Sampling theorem, Nyquist rate, aliasing, reconstruction
**Exam coverage:** Exam 3
**Source:** Transcribed from `lctr22-exercise-solutions.pdf` (instructor solutions by Rogelio Gracia Otalvaro, Spring 2026).

---

## Problem 1 — Nyquist rate and maximum $T$

A signal $x(t)$ has $X(j\omega) = 0$ for $|\omega| > 5000\pi$.

With $\omega_M = 5000\pi$ rad/s:

$$\text{Nyquist rate} = 2\omega_M = 10{,}000\pi \text{ rad/s} = 5000 \text{ Hz}.$$

The sampling theorem requires $\omega_s > 10{,}000\pi$, i.e.,

$$T < \frac{2\pi}{10{,}000\pi} = \frac{1}{5000} = 0.2 \text{ ms}.$$

$$\boxed{\text{Nyquist rate} = 10{,}000\pi \text{ rad/s} = 5000 \text{ Hz}, \qquad T < 0.2 \text{ ms}}$$

---

## Problem 2 — True or false: $\omega_s = 2\omega_M$ is sufficient

**False.** The sampling theorem requires the *strict* inequality $\omega_s > 2\omega_M$. Sampling at exactly twice the highest frequency can fail. For example, $x(t) = \sin(\omega_M t)$ sampled at $\omega_s = 2\omega_M$ gives $x(nT) = \sin(\pi n) = 0$ for all $n$ — the signal is completely invisible to the sampler.

$$\boxed{\text{False — strict inequality } \omega_s > 2\omega_M \text{ is required.}}$$

---

## Problem 3 — Why does sampling create spectral copies?

Sampling is multiplication by an impulse train $p(t)$ in the time domain. By the multiplication property, this corresponds to convolution of $X(j\omega)$ with $P(j\omega)$ in the frequency domain. Since $P(j\omega)$ is itself an impulse train (with impulses at every multiple of $\omega_s$), convolving with it shifts copies of $X(j\omega)$ to each of those multiples.

---

## Problem 4 — Can you undo aliasing with a clever filter?

**No.** When replicas overlap, their spectral contributions add together at each frequency. This addition is irreversible because you cannot determine which part of the sum came from which replica. No linear (or nonlinear) filter can separate them after the fact.

---

## Problem 5 — What is an anti-aliasing filter?

An anti-aliasing filter is a lowpass filter placed **before** the sampler. Its cutoff frequency is set at or below $\omega_s/2$ so that any frequency content above $\omega_s/2$ is removed before sampling takes place. This guarantees that the sampled signal satisfies the conditions of the sampling theorem, preventing aliasing.

---

## Problem 6 — Nyquist rate of $x(t) = \cos(600\pi t) + \cos(1800\pi t)$

The two components have frequencies $600\pi$ and $1800\pi$ rad/s. The highest is $\omega_M = 1800\pi$ rad/s $= 900$ Hz.

$$\boxed{\text{Nyquist rate} = 2\omega_M = 3600\pi \text{ rad/s} = 1800 \text{ Hz}.}$$

---

## Problem 7 — Aliasing for $\omega_M = 3000\pi$, $T = 2 \times 10^{-4}$ s?

Compute the sampling frequency:

$$\omega_s = \frac{2\pi}{T} = \frac{2\pi}{2 \times 10^{-4}} = 10{,}000\pi \text{ rad/s}.$$

The Nyquist rate is $2\omega_M = 6000\pi$. Since $10{,}000\pi > 6000\pi$, the sampling theorem is satisfied.

$$\boxed{\omega_s = 10{,}000\pi \text{ rad/s}; \text{ no aliasing occurs.}}$$

---

## Problem 8 — 900 Hz cosine sampled at $f_s = 1000$ Hz

The Nyquist frequency (maximum representable frequency) is $f_s/2 = 500$ Hz. Since $f_0 = 900 > 500$, aliasing occurs. The aliased frequency is:

$$f_{\text{alias}} = f_s - f_0 = 1000 - 900 = 100 \text{ Hz}.$$

$$\boxed{\text{Reconstructed signal: } \cos(2\pi \cdot 100\, t).}$$

---

## Problem 9 — 900 Hz cosine sampled at $f_s = 1500$ Hz

The Nyquist frequency is $f_s/2 = 750$ Hz. Since $f_0 = 900 > 750$, aliasing still occurs:

$$f_{\text{alias}} = f_s - f_0 = 1500 - 900 = 600 \text{ Hz}.$$

$$\boxed{\text{Reconstructed signal: } \cos(2\pi \cdot 600\, t).}$$

---

## Problem 10 — Nyquist rate of $x(t-5)$ and $x(2t)$

**Time shift:** $x(t-5)$ has the same magnitude spectrum as $x(t)$ (only the phase changes). The bandwidth is unchanged, so the Nyquist rate is still $\omega_0$.

**Time scaling:** $x(2t)$ compresses the signal by a factor of 2, which stretches the spectrum by the same factor. All frequencies double, so the Nyquist rate becomes $2\omega_0$.

$$\boxed{x(t-5): \omega_0; \qquad x(2t): 2\omega_0.}$$

---

## Problem 11 — Why does the reconstruction filter need gain $T$?

Equation (3) in the lecture shows that the sampled spectrum is:

$$X_p(j\omega) = \frac{1}{T} \sum_k X\!\left(j(\omega - k\omega_s)\right).$$

Each replica (including the one centered at $\omega = 0$) is scaled by $1/T$. The lowpass filter isolates the center replica, but it arrives with amplitude $1/T$ instead of the original amplitude $1$. To compensate, the filter must multiply by $T$, giving gain $T$ in its passband.

---

## Problem 12 — Is the zero-order hold exact?

**No.** The frequency response of the zero-order hold is:

$$H_0(j\omega) = e^{-j\omega T/2} \,\frac{2\sin(\omega T/2)}{\omega},$$

which is a sinc-shaped function in frequency, not a flat rectangle. This causes two problems: (1) the passband is not perfectly flat (amplitude "droop" at higher frequencies within the band), and (2) the spectral replicas are not fully suppressed (imperfect stopband rejection). Both effects introduce distortion in the reconstructed signal.

---

## Problem 13 — Helicopter blade at 25 rps filmed at 24 fps

The blade's rotation frequency is $f_0 = 25$ Hz. The camera samples at $f_s = 24$ fps, so $f_s/2 = 12$ Hz. Since $25 > 12$, aliasing occurs. The aliased frequency is:

$$f_{\text{alias}} = f_s - f_0 = 24 - 25 = -1 \text{ Hz}.$$

The magnitude is $1$ Hz, but the negative sign means the apparent rotation is in the *opposite* direction.

$$\boxed{\text{The blade appears to rotate slowly backward at 1 revolution per second.}}$$

---

## Problem 14 — Is $f_s = 8000$ Hz enough for $\omega_M = 10{,}000\pi$?

The highest frequency is $f_M = \omega_M/(2\pi) = 10{,}000\pi/(2\pi) = 5000$ Hz. The sampling theorem requires $f_s > 2f_M = 10{,}000$ Hz. Since $8000 < 10{,}000$, the theorem is **not satisfied** and aliasing will occur. The minimum sampling frequency that works is any $f_s > 10{,}000$ Hz (e.g., $f_s = 10{,}001$ Hz).

$$\boxed{\text{Theorem not satisfied; need } f_s > 10{,}000 \text{ Hz.}}$$

---

## Problem 15 — Can a non-band-limited signal be sampled in practice?

**Yes, but with a caveat.** A non-band-limited signal has energy at arbitrarily high frequencies, so no finite sampling rate can capture it perfectly. In practice, we place an **anti-aliasing filter** (a lowpass filter with cutoff at or below $\omega_s/2$) before the sampler. This makes the signal effectively band-limited by removing all content above the cutoff. Some high-frequency information is lost, but everything below the cutoff is preserved perfectly. This is the standard approach in all real A/D conversion systems (audio recording, medical imaging, communication receivers, etc.).

---

## Key Takeaways

- **Nyquist rate** for a band-limited signal with highest frequency $\omega_M$ is $2\omega_M$ (in rad/s) or $2f_M$ (in Hz).
- The sampling theorem requires the **strict inequality** $\omega_s > 2\omega_M$; sampling at exactly $2\omega_M$ can fail (e.g., a sine sampled at its zero crossings).
- **Sampling produces spectral replicas** at every multiple of $\omega_s$, scaled by $1/T$ (convolution with an impulse train in frequency).
- **Aliasing is irreversible.** Once replicas overlap, no filter can separate them. Prevention is the only cure.
- An **anti-aliasing filter** (lowpass, cutoff $\le \omega_s/2$) must be placed **before** the sampler — never after.
- The **ideal reconstruction filter** is a lowpass with passband gain $T$ (to cancel the $1/T$ replica scaling).
- A **zero-order hold** is not an exact reconstruction: it introduces sinc-shaped passband droop and imperfect replica suppression.
- **Time shifts** do not change the Nyquist rate; **time compression** $x(at)$ (with $|a|>1$) multiplies the Nyquist rate by $|a|$.
- For a pure tone $f_0$ sampled at $f_s$ with $f_0 > f_s/2$, the **aliased frequency** is $|f_s - f_0|$ (and the sign flip can indicate reversed apparent direction, as with the helicopter blade).
- **Non-band-limited signals** are sampled in practice by band-limiting them first with an anti-aliasing filter; high-frequency content above the cutoff is irrecoverably lost, but the passband is preserved perfectly.
