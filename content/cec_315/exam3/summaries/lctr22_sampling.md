# Lecture 22 — Sampling

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr22-sampling.pdf`
**Exam coverage:** Exam 3

---

**Lctr 22: Sampling**
Spring 2026
Focus: Chapter 7 (Pages 514–555)

## 1 The Big Picture: From Continuous Time to Discrete Time

### Why This Matters

Nearly every modern signal-processing system converts continuous-time signals into discrete-time signals at some point. Your phone digitizes your voice before compressing and transmitting it. A digital camera samples a spatially continuous scene onto a finite grid of pixels. An MRI scanner collects discrete frequency-domain measurements of a continuous spatial distribution.

The central question of this lecture is: **Under what conditions can we recover a continuous-time signal perfectly from a set of equally spaced samples?** The answer is the *sampling theorem*, one of the most important results in all of signals and systems.

**Roadmap for this lecture:**

1. Introduce impulse-train sampling and derive its frequency-domain effect.
2. State and interpret the sampling theorem.
3. Show how to reconstruct a signal from its samples (band-limited interpolation).
4. Explore what happens when we violate the sampling theorem (aliasing).
5. Connect sampling to discrete-time processing of continuous-time signals.

## 2 Impulse-Train Sampling

### 2.1 The Sampling Model

To study sampling mathematically, we model the process as multiplying $x(t)$ by a periodic impulse train $p(t)$ with period $T$:

$$x_p(t) \;=\; x(t)\,p(t), \qquad p(t) \;=\; \sum_{n=-\infty}^{+\infty} \delta(t-nT). \tag{1}$$

The period $T$ is the **sampling period** (time between samples), and the fundamental frequency $\omega_s = 2\pi/T$ is the **sampling frequency** (how many radians per second we sample at).

Because multiplying by an impulse simply captures the signal value at that instant ($x(t)\,\delta(t-nT) = x(nT)\,\delta(t-nT)$), the sampled signal is an impulse train whose amplitudes are the sample values:

$$x_p(t) \;=\; \sum_{n=-\infty}^{+\infty} x(nT)\,\delta(t-nT). \tag{2}$$

Think of it this way: we "grab" the value of $x(t)$ at every multiple of $T$ and store it as the height of an impulse at that location.

*[Figure: three-panel diagram showing original signal $x(t)$ (smooth curve) times impulse train $p(t)$ (uniformly spaced impulses of period $T$) equals sampled signal $x_p(t)$ (impulses whose heights match $x$ at the sample times).]*

### 2.2 Frequency-Domain Effect of Sampling

From the multiplication property of the Fourier transform, multiplying in time corresponds to convolution in frequency (scaled by $1/2\pi$). The Fourier transform of the impulse train is itself an impulse train:

$$P(j\omega) \;=\; \frac{2\pi}{T}\sum_{k=-\infty}^{+\infty}\delta(\omega-k\omega_s). \tag{3}$$

Convolving $X(j\omega)$ with this impulse train produces shifted replicas:

$$\boxed{\,X_p(j\omega) \;=\; \frac{1}{T}\sum_{k=-\infty}^{+\infty} X\!\big(j(\omega-k\omega_s)\big).\,} \tag{4}$$

In plain English: the spectrum of the sampled signal is just the original spectrum $X(j\omega)$ *copied and pasted* at every integer multiple of $\omega_s$, and each copy is scaled by $1/T$.

### Key Insight

Sampling in time creates **periodic copies (replicas)** of the original spectrum $X(j\omega)$, shifted to every integer multiple of $\omega_s$ and scaled by $1/T$. The entire content of the sampling theorem comes down to one question: **do these copies overlap, or not?**

Let us visualize both cases. Suppose $X(j\omega)$ is a simple triangle living between $-\omega_M$ and $+\omega_M$.

*[Figure: top panel labeled "$\omega_s > 2\omega_M$: No overlap" shows triangular spectrum replicas at $-\omega_s$, $0$, $\omega_s$ with a visible gap between them, height $1/T$. Bottom panel labeled "$\omega_s < 2\omega_M$: Overlap (aliasing)" shows the replicas intruding into each other near $\pm\omega_M$ with red "overlap!" annotations.]*

## 3 The Sampling Theorem

### The Sampling Theorem (Shannon / Nyquist)

Let $x(t)$ be a **band-limited** signal with

$$X(j\omega) = 0 \quad \text{for}\quad |\omega| > \omega_M.$$

Then $x(t)$ is **uniquely determined** by its samples $x(nT)$, $n = 0, \pm 1, \pm 2, \ldots$, if

$$\boxed{\;\omega_s > 2\omega_M\;} \qquad \text{where}\quad \omega_s = \frac{2\pi}{T}.$$

Given these samples, $x(t)$ can be reconstructed exactly by passing an impulse train (whose impulse amplitudes equal the sample values) through an ideal lowpass filter with gain $T$ and cutoff frequency $\omega_c$ satisfying $\omega_M < \omega_c < \omega_s - \omega_M$.

The frequency $2\omega_M$ is called the **Nyquist rate**: the minimum sampling frequency you need. The frequency $\omega_M$ (half the Nyquist rate) is often called the **Nyquist frequency**.

### Key Insight

The sampling theorem says two things:

1. **Uniqueness:** If you sample fast enough, no information is lost.
2. **Reconstruction:** You can get $x(t)$ back exactly using an ideal lowpass filter.

The condition $\omega_s > 2\omega_M$ is a *strict* inequality. Sampling at exactly twice the highest frequency is *not* sufficient in general (Example 22.3 shows why).

### 3.1 The Reconstruction System

The ideal lowpass filter $H(j\omega)$ isolates the center copy of the spectrum and throws away all the other replicas.

*[Figure: block diagram — $x(t)$ enters a multiplier driven by $p(t)$, producing $x_p(t)$, which feeds an LPF $H(j\omega)$ whose output is $x_r(t) = x(t)$.]*

With cutoff at $\omega_c = \omega_s/2$: $H(j\omega) = T$ for $|\omega| < \omega_s/2$, and $H(j\omega) = 0$ for $|\omega| > \omega_s/2$.

Here is the full picture of what happens at each stage in the frequency domain:

*[Figure: four stacked spectra — (a) Original $X(j\omega)$: triangle of height 1 between $\pm\omega_M$; (b) After sampling $X_p(j\omega)$: replicas at $0,\pm\omega_s,\ldots$ each of height $1/T$; (c) Ideal LPF $H(j\omega)$: rectangle of height $T$ spanning the passband; (d) Recovered $X_r(j\omega) = X(j\omega)$ labeled "Perfect!".]*

## 4 Worked Examples

### Example 22.1(a): Nyquist Rate of a Sum of Sinusoids

**Problem.** Find the Nyquist rate of $x(t) = 1 + \cos(2000\pi t) + \sin(4000\pi t)$.

The three frequency components are at $0$, $2000\pi$, and $4000\pi$ rad/s. The highest is $\omega_M = 4000\pi$ rad/s = 2000 Hz.

$$\text{Nyquist rate} = 2\omega_M = 8000\pi\ \text{rad/s} = 4000\ \text{Hz}.$$

We need to sample faster than 4000 times per second.

*[Figure: magnitude spectrum $|X(j\omega)|$ showing DC impulse at 0, impulses at $\pm 2000\pi$, and impulses at $\pm 4000\pi$; the double-headed arrow "Nyquist rate = $2\omega_M$" spans from $-\omega_M$ to $+\omega_M$.]*

### Example 22.1(b): Nyquist Rate of a Sinc Function

**Problem.** Find the Nyquist rate of $x(t) = \dfrac{\sin(4000\pi t)}{\pi t}$.

We rewrite: $x(t) = 4000 \cdot \dfrac{\sin(4000\pi t)}{4000\pi t} = 4000\,\mathrm{sinc}(4000\,t)$, where $\mathrm{sinc}(u) \triangleq \sin(\pi u)/(\pi u)$.

Its Fourier transform is a **rectangle**: $X(j\omega) = 1$ for $|\omega| < 4000\pi$, and $0$ otherwise. So $\omega_M = 4000\pi$ and the Nyquist rate is $8000\pi$ rad/s = 4000 Hz.

*[Figure: left — time domain sinc waveform; right — frequency domain rectangle spanning $-4000\pi$ to $4000\pi$.]*

### Example 22.1(c): Nyquist Rate of a Squared Sinc

**Problem.** Find the Nyquist rate of $x(t) = \left(\dfrac{\sin(4000\pi t)}{\pi t}\right)^{2}$.

First, recognize what is being squared. From part (b) we know that $\dfrac{\sin(4000\pi t)}{\pi t} = 4000\,\mathrm{sinc}(4000\,t)$ is a sinc function with bandwidth $\omega_M = 4000\pi$.

Now we are squaring that entire sinc function. Squaring in the time domain corresponds to convolving the spectrum with itself in the frequency domain (since $x^2(t) \leftrightarrow \frac{1}{2\pi}\,X(j\omega) * X(j\omega)$). The convolution of two rectangles, each of width $2 \times 4000\pi = 8000\pi$, produces a **triangle** of total width $2 \times 8000\pi = 16000\pi$. Therefore $\omega_M = 8000\pi$ and:

$$\text{Nyquist rate} = 2\omega_M = 16000\pi\ \text{rad/s} = 8000\ \text{Hz}.$$

The lesson: squaring a signal **doubles** the bandwidth!

*[Figure: left — $X(j\omega)$ rectangle spanning $\pm\omega_M$; right — after squaring, $X * X$ triangle spanning $\pm 2\omega_M$.]*

### Example 22.2: Checking Whether a Sampling Period Works

**Problem.** A signal $x(t)$ is the output of an ideal lowpass filter with cutoff frequency $\omega_c = 1000\pi$ rad/s. Which of the following sampling periods guarantee that $x(t)$ can be perfectly reconstructed from its samples?

(a) $T = 0.5 \times 10^{-3}$ s
(b) $T = 2 \times 10^{-3}$ s
(c) $T = 10^{-4}$ s

**Step 1: Identify the highest frequency.**
Since $x(t)$ comes out of an ideal lowpass filter with cutoff $\omega_c = 1000\pi$ rad/s, we know $X(j\omega) = 0$ for $|\omega| > 1000\pi$. So the highest frequency present in $x(t)$ is:

$$\omega_M = 1000\pi\ \text{rad/s} \qquad (\text{equivalently, } f_M = 500\ \text{Hz}).$$

**Step 2: Compute the Nyquist rate.**
The sampling theorem requires $\omega_s > 2\omega_M$:

$$\omega_s > 2 \times 1000\pi = 2000\pi\ \text{rad/s} \qquad (\text{equivalently, } f_s > 1000\ \text{Hz}).$$

**Step 3: Convert to a constraint on $T$.**
Since $\omega_s = 2\pi/T$, the condition $\omega_s > 2000\pi$ becomes:

$$\frac{2\pi}{T} > 2000\pi \quad\Longrightarrow\quad T < \frac{2\pi}{2000\pi} = \frac{1}{1000} = 10^{-3}\ \text{s} = 1\ \text{ms}.$$

Any sampling period *less than* 1 ms will work.

**Step 4: Check each option.**

*[Figure: number line showing $T_\text{max} = 1$ ms as dashed boundary; green region "No aliasing" to the left with (c) 0.1 and (a) 0.5; red region "Aliasing" to the right with (b) 2.0.]*

- **(a)** $T = 0.5$ ms $< 1$ ms: $\omega_s = 2\pi/(0.5 \times 10^{-3}) = 4000\pi > 2000\pi$. ✓ This works. We are sampling at twice the Nyquist rate (oversampled by 2×).
- **(b)** $T = 2$ ms $> 1$ ms: $\omega_s = 2\pi/(2 \times 10^{-3}) = 1000\pi < 2000\pi$. ✗ This is too slow. The sampling frequency is only half of what we need, so aliasing will distort the signal.
- **(c)** $T = 0.1$ ms $< 1$ ms: $\omega_s = 2\pi/(10^{-4}) = 20000\pi \gg 2000\pi$. ✓ This works easily. We are sampling at 10× the Nyquist rate.

### Example 22.3: Sampling at Exactly the Nyquist Rate Fails

**Problem.** Consider $x(t) = \sin\!\big(\tfrac{\omega_s}{2}t\big)$ sampled at frequency $\omega_s$ (exactly two samples per cycle).

**Solution.** The samples are $x(nT) = \sin\!\big(\tfrac{\omega_s}{2}\cdot\tfrac{2\pi n}{\omega_s}\big) = \sin(\pi n) = 0$ for every integer $n$. Every sample is zero! The sampler sees nothing.

*[Figure: sinusoid with red sample markers all landing exactly on zero crossings, labeled "All samples = 0!"; sampling period $T$ indicated.]*

This is why $\omega_s$ must be *strictly greater than* $2\omega_M$.

## 5 Reconstruction via Band-Limited Interpolation

In the time domain, the output of the ideal lowpass reconstruction filter is:

$$x_r(t) \;=\; \sum_{n=-\infty}^{+\infty} x(nT)\,h(t - nT), \qquad h(t) = \frac{\sin(\pi t/T)}{\pi t/T}. \tag{5}$$

So the reconstruction formula is:

$$\boxed{\,x_r(t) \;=\; \sum_{n=-\infty}^{+\infty} x(nT)\,\frac{\sin\!\big[\pi(t-nT)/T\big]}{\pi(t-nT)/T}.\,} \tag{6}$$

Place a sinc at every sample point, scale it by the sample value, and add them all up. Each sinc equals 1 at its own sample time and 0 at every other sample time.

*[Figure: several dashed sinc functions centered at $0, T, 2T, 3T, 4T$ weighted by their sample values, summing (solid black) to a smooth reconstructed waveform; legend lists "sum", "sinc at 0", "sinc at $T$", etc.]*

### Key Insight

Equation (6) is the **ideal band-limited interpolation formula**. In practice, the sinc extends to $\pm\infty$ (you would need infinitely many samples), so real systems use approximate methods: zero-order holds, linear interpolation, or windowed-sinc filters.

## 6 Practical Interpolation: Zero-Order and First-Order Holds

### 6.1 Zero-Order Hold (Staircase)

Hold each sample value constant until the next sample arrives. Uses a rectangular pulse $h_0(t)$ of width $T$:

*[Figure: left — $h_0(t)$ rectangular pulse of height 1, width $T$; right — "Zero-order hold output": staircase approximation (red) overlaid on the original smooth curve (blue dashed).]*

### 6.2 First-Order Hold (Connect-the-Dots)

Connect adjacent samples with straight lines. Uses a triangular pulse $h_1(t)$:

*[Figure: left — $h_1(t)$ triangular pulse of height 1 with base from $-T$ to $T$; right — "First-order hold output": piecewise-linear reconstruction (solid) overlaid on the original smooth curve (dashed).]*

Neither method is exact. Both approximate the ideal sinc interpolation.

## 7 The Effect of Undersampling: Aliasing

When $\omega_s < 2\omega_M$, the shifted replicas of $X(j\omega)$ overlap, and the original spectrum cannot be separated out by lowpass filtering. This distortion is called **aliasing**: high-frequency components masquerade as lower frequencies.

### Warning

Aliasing is **irreversible**. Once spectral replicas overlap, there is no way to undo the damage. The only way to prevent aliasing is to ensure $\omega_s > 2\omega_M$ *before* sampling, or to pre-filter the signal to remove frequencies above $\omega_s/2$ (an **anti-aliasing filter**).

### 7.1 Aliasing of a Sinusoid

#### Example 22.4: A 5 Hz Cosine Sampled at 6 Hz

Consider $x(t) = \cos(2\pi \cdot 5\,t)$ sampled at $f_s = 6$ Hz. The Nyquist rate is $2f_0 = 10$ Hz. Since $f_s = 6 < 10$, we are undersampling. The aliased frequency is $f_\text{alias} = f_s - f_0 = 6 - 5 = 1$ Hz.

*[Figure: 5 Hz cosine (blue) and 1 Hz cosine (red dashed) plotted on the same axis with red sample dots showing both curves passing through the same sample points; caption: "Both curves pass through the same sample points!"]*

The 5 Hz and 1 Hz signals produce the same samples. The lowpass filter picks the lower one, so the 5 Hz tone is aliased to 1 Hz.

### 7.2 Aliasing in the Frequency Domain

The original spectrum has impulses at $\pm 5$ Hz. After sampling at 6 Hz, replicas appear at $\pm 5 + 6k$. The replicas at $\pm 1$ Hz land inside the lowpass filter:

*[Figure: (a) Original spectrum with impulses at $\pm 5$ Hz. (b) After sampling at $f_s = 6$ Hz: impulses at $\pm 5$ plus additional circled impulses at $\pm 1$ Hz (labeled "Circled = aliased") inside the LPF passband box "$|f| < 3$".]*

### 7.3 Everyday Examples of Aliasing

**Wagon-wheel effect in movies:** A movie camera captures frames at 24 fps. If a wagon wheel spins near 12 revolutions per second, it can appear to stand still or rotate backward. The rotation frequency exceeds half the frame rate.

**Moiré patterns:** Photographing a fine-striped shirt with a coarse pixel grid produces wavy interference patterns: spatial aliasing.

## 8 Discrete-Time Processing of Continuous-Time Signals

One of the most powerful applications of sampling is using discrete-time systems (computers, DSP chips) to process continuous-time signals:

*[Figure: block diagram — $x_c(t)$ into "C/D converter" (A-to-D) producing $x_d[n]$, into "Discrete-time system" producing $y_d[n]$, into "D/C converter" (D-to-A) producing $y_c(t)$.]*

The C/D converter creates $x_d[n] = x_c(nT)$. The D/C converter reconstructs $y_c(t)$ from $y_d[n]$ via lowpass filtering. If $x_c(t)$ is band-limited and the sampling theorem is satisfied, this entire cascade behaves like a continuous-time LTI system. The discrete-time frequency $\Omega$ and the continuous-time frequency $\omega$ are related by $\Omega = \omega T$, so the full range $|\omega| < \omega_s/2$ maps onto $|\Omega| < \pi$.

## 9 Summary of Key Formulas

| Concept | Formula / Condition |
|---|---|
| Sampling period / frequency | $T = 2\pi/\omega_s$ |
| Nyquist rate | $2\omega_M$ (must be exceeded by $\omega_s$) |
| Sampling condition | $\omega_s > 2\omega_M$ (strict inequality!) |
| Spectrum of sampled signal | $X_p(j\omega) = \dfrac{1}{T}\sum_{k} X\!\big(j(\omega - k\omega_s)\big)$ |
| Sinc interpolation | $x_r(t) = \sum_{n} x(nT)\,\dfrac{\sin[\pi(t-nT)/T]}{\pi(t-nT)/T}$ |
| Aliased frequency | $f_\text{alias} = |f_s - f_0|$ (for $f_s/2 < f_0 < f_s$) |
| CT $\leftrightarrow$ DT frequency | $\Omega = \omega T$ |

## 10 Summary

*[Figure: flow diagram — "Continuous-time signal $x(t)$" → "Sample at rate $\omega_s > 2\omega_M$" → "Discrete-time signal $x[n]$" → "Ideal LPF reconstruction" looping back to the continuous-time signal.]*

**Key takeaways:**

1. **Sampling in time creates periodic copies in frequency.** The sampled spectrum is the original copy-pasted at every multiple of $\omega_s$, scaled by $1/T$.
2. **The sampling theorem** guarantees perfect reconstruction when $\omega_s > 2\omega_M$. Reconstruction uses an ideal lowpass filter (sinc interpolation in time).
3. **Aliasing** is the irreversible distortion from sampling too slowly. Higher frequencies fold back into lower ones. Use anti-aliasing filters *before* sampling.
4. **Practical reconstruction** uses zero-order holds, first-order holds, or other approximate filters.
5. **Discrete-time processing of CT signals** works because sampling preserves all information in a band-limited signal. The link: $\Omega = \omega T$.

## 11 Common Mistakes to Avoid

1. **Confusing Hz and rad/s.** $f_s > 2f_M$ (Hz) or $\omega_s > 2\omega_M$ (rad/s). Mixing units gives factor-of-$2\pi$ errors.
2. **Assuming $\omega_s = 2\omega_M$ is sufficient.** It is not (Example 22.3).
3. **Forgetting the $1/T$ scaling.** Replicas are scaled by $1/T$; the reconstruction filter compensates with gain $T$.
4. **Thinking aliasing can be undone.** It cannot. Prevent it before sampling.
5. **Claiming non-band-limited signals can't be sampled.** In practice, we band-limit with an anti-aliasing filter first.

## 12 Practice Questions

Test your understanding with these quick questions. Answers are at the bottom of the section.

1. A signal $x(t)$ has $X(j\omega) = 0$ for $|\omega| > 5000\pi$. What is the Nyquist rate? What is the maximum allowable sampling period $T$?
2. True or false: if $\omega_s = 2\omega_M$, the sampling theorem guarantees perfect reconstruction.
3. In one sentence, explain *why* sampling in time produces copies of the spectrum in the frequency domain.
4. A signal is sampled and the resulting spectrum $X_p(j\omega)$ shows overlapping replicas. Can you undo the overlap with a clever filter? Why or why not?
5. What is an anti-aliasing filter, and *where* in the signal chain does it go (before or after the sampler)?
6. Determine the Nyquist rate for $x(t) = \cos(600\pi t) + \cos(1800\pi t)$.
7. A signal with $\omega_M = 3000\pi$ is sampled with $T = 2 \times 10^{-4}$ s. Compute $\omega_s$ and state whether aliasing occurs.
8. You sample $x(t) = \cos(2\pi \cdot 900\,t)$ at $f_s = 1000$ Hz. What frequency does the reconstructed signal have?
9. Repeat the previous question for $f_s = 1500$ Hz.
10. A signal has Nyquist rate $\omega_0$. What is the Nyquist rate of $x(t-5)$? What about $x(2t)$?
11. The ideal reconstruction filter has gain $T$ in its passband. Why is that factor of $T$ needed? (Hint: look at the $1/T$ scaling of the replicas.)
12. A zero-order hold is used instead of an ideal lowpass filter for reconstruction. Is the result exact? What kind of error does it introduce?
13. A movie camera shoots at 24 frames per second. A helicopter blade spins at 25 revolutions per second. Describe qualitatively what the blade looks like in the film.
14. You are told that $X(j\omega) = 0$ for $|\omega| > 10{,}000\pi$. Someone samples $x(t)$ at $f_s = 8000$ Hz. Is the sampling theorem satisfied? If not, what is the minimum $f_s$ that works?
15. Suppose $x(t)$ is *not* band-limited (its spectrum extends to $\pm\infty$). Does this mean we can never sample it in practice? Explain what is done in real systems.

*Rogelio Gracia Otalvaro*

## Practice Problems Summary

- **Example 22.1(a):** Compute the Nyquist rate of a sum of sinusoids $1 + \cos(2000\pi t) + \sin(4000\pi t)$ by identifying the highest frequency component.
- **Example 22.1(b):** Find the Nyquist rate of a sinc function $\sin(4000\pi t)/(\pi t)$ by recognizing its Fourier transform as a rectangle.
- **Example 22.1(c):** Determine the Nyquist rate of a squared sinc, using the fact that squaring in time doubles the bandwidth (rectangle convolved with itself becomes a triangle).
- **Example 22.2:** Decide which of three candidate sampling periods (0.5 ms, 2 ms, 0.1 ms) allow perfect reconstruction of a signal band-limited to $1000\pi$ rad/s.
- **Example 22.3:** Demonstrate that sampling $\sin(\omega_s t/2)$ at exactly $\omega_s$ yields all-zero samples, showing the strict inequality in the sampling theorem is required.
- **Example 22.4:** Show how a 5 Hz cosine sampled at 6 Hz aliases to a 1 Hz cosine because $f_s < 2f_0$.
- **Practice Question 1:** Compute Nyquist rate and maximum sampling period for a signal with $\omega_M = 5000\pi$.
- **Practice Question 2:** True/false check on whether $\omega_s = 2\omega_M$ guarantees perfect reconstruction.
- **Practice Question 3:** Explain in one sentence why sampling creates spectral copies.
- **Practice Question 4:** Explain whether overlapping replicas (aliasing) can be undone by filtering.
- **Practice Question 5:** Define an anti-aliasing filter and state its placement in the signal chain.
- **Practice Question 6:** Compute the Nyquist rate of $\cos(600\pi t) + \cos(1800\pi t)$.
- **Practice Question 7:** Given $\omega_M = 3000\pi$ and $T = 2 \times 10^{-4}$ s, compute $\omega_s$ and determine whether aliasing occurs.
- **Practice Question 8:** Identify the reconstructed frequency when $\cos(2\pi \cdot 900\,t)$ is sampled at 1000 Hz.
- **Practice Question 9:** Repeat the aliasing analysis with $f_s = 1500$ Hz.
- **Practice Question 10:** Determine the Nyquist rate of $x(t-5)$ and $x(2t)$ given that $x(t)$ has Nyquist rate $\omega_0$.
- **Practice Question 11:** Explain why the ideal reconstruction filter must have gain $T$ in its passband.
- **Practice Question 12:** Describe the error introduced when a zero-order hold replaces the ideal lowpass filter.
- **Practice Question 13:** Qualitatively describe the appearance of a 25 rev/s helicopter blade filmed at 24 fps.
- **Practice Question 14:** Determine whether $f_s = 8000$ Hz satisfies the sampling theorem for $\omega_M = 10{,}000\pi$, and find the minimum valid $f_s$.
- **Practice Question 15:** Explain how non-band-limited signals are handled in practice.
