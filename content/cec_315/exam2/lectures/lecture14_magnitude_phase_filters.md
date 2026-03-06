# Lecture 14: Magnitude-Phase Representation and Filters

## Polar Form of FT

$$X(j\omega) = |X(j\omega)| \, e^{j\angle X(j\omega)}$$

- **Magnitude spectrum** $|X(j\omega)|$: amplitude at each frequency
- **Phase spectrum** $\angle X(j\omega)$: phase shift at each frequency

## Decibel Scale

$$|H(j\omega)|_{\text{dB}} = 20 \log_{10} |H(j\omega)|$$

| Linear | dB |
|---|---|
| 1 | 0 dB |
| $1/\sqrt{2} \approx 0.707$ | -3 dB |
| 0.5 | -6 dB |
| 0.1 | -20 dB |
| 0.01 | -40 dB |
| 10 | +20 dB |

**Cutoff frequency:** defined at the **-3 dB point** where power is halved ($|H|^2 = \frac{1}{2}|H(0)|^2$).

## Energy Spectral Density

$$E = \int_{-\infty}^{\infty} |x(t)|^2 \, dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 \, d\omega$$

$|X(j\omega)|^2$ tells how energy is distributed across frequency. Phase does not affect total energy.

## Phase and Delay

### Linear Phase

$$\angle H(j\omega) = -\omega t_0$$

A system with linear phase imposes a **pure time delay** of $t_0$ seconds on all frequencies equally. The output shape is preserved -- no distortion.

$$h(t) \text{ linear phase} \implies y(t) = c \cdot x(t - t_0)$$

### Phase Distortion

Nonlinear phase means different frequencies experience different delays. The output waveform shape is **distorted** even if magnitude is flat.

### Group Delay

$$\tau(\omega) = -\frac{d}{d\omega} \angle H(j\omega)$$

- For linear phase: $\tau(\omega) = t_0$ (constant for all $\omega$)
- For nonlinear phase: $\tau(\omega)$ varies with frequency

## Ideal Filters

### Ideal Lowpass Filter

$$H(j\omega) = \begin{cases} 1, & |\omega| \leq \omega_c \\ 0, & |\omega| > \omega_c \end{cases}$$

Impulse response: $h(t) = \frac{\sin(\omega_c t)}{\pi t} = \frac{\omega_c}{\pi} \text{sinc}\left(\frac{\omega_c t}{\pi}\right)$

**Non-causal:** $h(t) \neq 0$ for $t < 0$, so ideal filters are **physically unrealizable**.

### With Linear Phase (Delayed Ideal Filter)

$$H(j\omega) = e^{-j\omega t_0}, \quad |\omega| \leq \omega_c$$

$$h(t) = \frac{\sin(\omega_c(t - t_0))}{\pi(t - t_0)}$$

Still noncausal for any finite $t_0$ (sinc extends to $-\infty$).

## Nonideal (Real) Filter Specifications

- **Passband edge** $\omega_p$: end of the passband
- **Stopband edge** $\omega_s$: start of the stopband
- **Transition band**: $\omega_p < \omega < \omega_s$ (gradual roll-off region)
- **Passband ripple** $\delta_1$: maximum deviation from 1 in passband
- **Stopband attenuation** $\delta_2$: maximum leakage in stopband

## Bandwidth and Rise Time Trade-off

$$\omega_c \cdot t_r \approx \text{constant}$$

- **Wider bandwidth** (larger $\omega_c$) $\Rightarrow$ **shorter rise time** (faster response)
- **Narrower bandwidth** $\Rightarrow$ **longer rise time** (slower, smoother response)
- Cannot have both sharp frequency cutoff and fast time response

## Real-Part Sufficiency

For a **real and causal** system, $H(j\omega)$ is completely determined by:
- Its real part alone, OR
- Its imaginary part alone

The real and imaginary parts are related by the **Hilbert transform**.
