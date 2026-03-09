# Lecture 14: Magnitude, Phase, Group Delay, and Filtering

## 1. Polar Representation of Frequency Response

Any complex-valued $X(j\omega)$ can be written in polar form:

$$X(j\omega) = |X(j\omega)| \, e^{j\angle X(j\omega)}$$

- **Magnitude spectrum** $|X(j\omega)|$: amplitude scaling at each frequency
- **Phase spectrum** $\angle X(j\omega)$: phase shift at each frequency

For real signals:
- Magnitude is **even**: $|X(-j\omega)| = |X(j\omega)|$
- Phase is **odd**: $\angle X(-j\omega) = -\angle X(j\omega)$

## 2. Energy Spectral Density

$$|X(j\omega)|^2 = \text{energy spectral density}$$

By Parseval's:
$$E = \int_{-\infty}^{\infty} |x(t)|^2 \, dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 \, d\omega$$

The energy in a frequency band $[\omega_1, \omega_2]$ is:
$$E_{\text{band}} = \frac{1}{2\pi} \int_{\omega_1}^{\omega_2} |X(j\omega)|^2 \, d\omega + \frac{1}{2\pi}\int_{-\omega_2}^{-\omega_1} |X(j\omega)|^2 \, d\omega$$

## 3. Decibel Scale

$$|H(j\omega)|_{\text{dB}} = 20\log_{10}|H(j\omega)|$$

**Key reference values:**

| $|H|$ | dB |
|---|---|
| 1 | 0 dB |
| $1/\sqrt{2} \approx 0.707$ | $-3$ dB (half-power point) |
| $1/2 = 0.5$ | $-6$ dB |
| $1/10 = 0.1$ | $-20$ dB |
| $1/100 = 0.01$ | $-40$ dB |
| 2 | $+6$ dB |
| 10 | $+20$ dB |

**Why dB?**
- Compresses large dynamic ranges
- Multiplication becomes addition: $|H_1 H_2|_{\text{dB}} = |H_1|_{\text{dB}} + |H_2|_{\text{dB}}$
- Cascaded systems: total dB = sum of individual dBs

## 4. Phase — Why It Matters

**Phase carries structural information.** Two key experiments:
1. Keep magnitude, scramble phase → signal becomes unrecognizable
2. Keep phase, flatten magnitude → signal structure is preserved

This shows phase encodes the **timing and alignment** of frequency components, while magnitude encodes **energy**.

## 5. Linear Phase and Pure Delay

A system has **linear phase** if:
$$\angle H(j\omega) = -\omega t_d$$

where $t_d$ is a constant delay.

**Consequence:** Every frequency component is delayed by the same amount $t_d$:
$$y(t) = |H(j\omega_0)| \cdot x(t - t_d)$$

- Output is a scaled, delayed copy of input → **no distortion**
- Linear phase is the ideal for signal transmission

**Nonlinear phase** means different frequencies experience different delays → **waveform distortion** even if magnitude is flat.

## 6. Group Delay

$$\tau(\omega) = -\frac{d}{d\omega} \angle H(j\omega)$$

- For linear phase: $\tau(\omega) = t_d$ (constant) — all frequencies delayed equally
- For nonlinear phase: $\tau(\omega)$ varies — different frequencies experience different delays
- Group delay measures the **effective delay** of a narrow band of frequencies centered at $\omega$

### First-Order System Group Delay

For $H(j\omega) = \frac{1}{1 + j\omega/\omega_c}$:

$$\angle H(j\omega) = -\arctan(\omega/\omega_c)$$

$$\tau(\omega) = -\frac{d}{d\omega}\left[-\arctan(\omega/\omega_c)\right] = \frac{1/\omega_c}{1 + (\omega/\omega_c)^2}$$

- Maximum delay at $\omega = 0$: $\tau(0) = 1/\omega_c$
- Decreases monotonically
- NOT constant → nonlinear phase → distortion

## 7. Ideal Filters

### Ideal Lowpass Filter

$$H_{\text{LP}}(j\omega) = \begin{cases} 1 & |\omega| \leq \omega_c \\ 0 & |\omega| > \omega_c \end{cases}$$

- Perfect passband (gain = 1), perfect stopband (gain = 0)
- Linear phase in passband: $H(j\omega) = e^{-j\omega t_d}$ for $|\omega| \leq \omega_c$
- Impulse response: $h(t) = \frac{\omega_c}{\pi} \text{sinc}\left(\frac{\omega_c(t-t_d)}{\pi}\right)$

**Why ideal filters are unrealizable:**
1. Impulse response extends to $t = -\infty$ → **noncausal**
2. Requires infinite delay ($t_d \to \infty$) for approximation
3. Brick-wall cutoff requires infinite-order system

### Other Ideal Filters
- **Highpass:** $H = 1$ for $|\omega| > \omega_c$, $H = 0$ otherwise
- **Bandpass:** $H = 1$ for $\omega_1 < |\omega| < \omega_2$
- **Bandstop/Notch:** $H = 0$ in a band, $H = 1$ elsewhere

## 8. Nonideal (Practical) Filter Specifications

Real filters cannot achieve brick-wall transitions. Specs include:

- **Passband edge** $\omega_p$: frequency where passband ends
- **Stopband edge** $\omega_s$: frequency where stopband begins
- **Transition band**: $\omega_p < \omega < \omega_s$ (gradual rolloff)
- **Passband ripple** $\delta_p$: maximum deviation from unity in passband
- **Stopband attenuation** $\delta_s$: maximum leakage in stopband

$$1 - \delta_p \leq |H(j\omega)| \leq 1 + \delta_p \quad \text{for } |\omega| \leq \omega_p$$
$$|H(j\omega)| \leq \delta_s \quad \text{for } |\omega| \geq \omega_s$$

**Trade-off:** Narrower transition band requires higher-order filters (more computation/hardware).

## 9. Bandwidth and Rise Time

**Time-bandwidth trade-off:**
$$\Delta\omega \cdot \Delta t \approx \text{constant}$$

- Wider bandwidth → faster rise time (sharper time features)
- Narrower bandwidth → slower rise time (smoother output)
- For first-order system: $\text{rise time} \approx 2.2/\omega_c$

## 10. DT Ideal and Nonideal Filters

Same concepts apply to DT:
- Frequency range is $-\pi < \omega \leq \pi$ (or $0$ to $2\pi$)
- Ideal DT lowpass: $H(e^{j\omega}) = 1$ for $|\omega| \leq \omega_c$
- Impulse response: $h[n] = \frac{\omega_c}{\pi} \text{sinc}\left(\frac{\omega_c n}{\pi}\right)$ (also noncausal, infinite length)
- Practical DT filters: FIR (finite impulse response) or IIR (infinite impulse response)
