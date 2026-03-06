# Lecture 11: Frequency Response and Filtering

## Frequency Response

An LTI system acts as a **frequency-by-frequency multiplier**. For a periodic input with FS coefficients $\{a_k\}$, the output coefficients are:

$$b_k = a_k \cdot H(jk\omega_0)$$

where $H(j\omega)$ is the **frequency response** (eigenvalue at frequency $\omega$).

### CT Frequency Response

$$H(j\omega) = \int_{-\infty}^{\infty} h(\tau) e^{-j\omega\tau} d\tau$$

For causal $h(t) = e^{-at}u(t)$:

$$H(j\omega) = \frac{1}{a + j\omega}$$

### DT Frequency Response

$$H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} h[n] \, e^{-j\omega n}$$

## Output of LTI System to Periodic Input

Given input $x(t) = \sum a_k e^{jk\omega_0 t}$:

$$y(t) = \sum_{k=-\infty}^{\infty} a_k \, H(jk\omega_0) \, e^{jk\omega_0 t}$$

Each harmonic is independently scaled by $|H(jk\omega_0)|$ and phase-shifted by $\angle H(jk\omega_0)$.

## Filter Types

| Filter | Passes | Attenuates |
|---|---|---|
| **Lowpass** | Low frequencies (near $\omega = 0$) | High frequencies |
| **Highpass** | High frequencies | Low frequencies (near $\omega = 0$) |
| **Bandpass** | Frequencies in a specific band | Frequencies outside the band |

## Ideal vs Real Filters

**Ideal filters:** Perfectly rectangular magnitude response (1 in passband, 0 in stopband). Physically **unrealizable** (noncausal).

**Real filters:** Gradual roll-off with a **transition band** between passband and stopband.

## RC Circuit Example

### Lowpass: $H(j\omega) = \frac{1}{1 + j\omega RC}$

- Cutoff frequency: $\omega_c = 1/RC$
- At $\omega_c$: magnitude drops to $1/\sqrt{2}$ of DC value (-3 dB point)
- Phase at cutoff: $-45°$

### Highpass: $H(j\omega) = \frac{j\omega RC}{1 + j\omega RC}$

- Same cutoff frequency $\omega_c = 1/RC$
- At DC ($\omega = 0$): output is zero
- At high frequencies: output approaches input

## General First-Order Lowpass: $H(j\omega) = \frac{1}{a + j\omega}$

- Cutoff: $\omega_c = a$ (the pole location)
- $|H(j\omega_c)| = \frac{1}{\sqrt{2}} |H(0)|$ (definition of -3 dB)
- Increasing $a$ widens bandwidth (less aggressive filtering)

## FIR vs IIR Filters (DT)

| Type | Impulse Response | Memory | Example |
|---|---|---|---|
| **FIR** (Finite Impulse Response) | Finite duration | Finite | Moving average |
| **IIR** (Infinite Impulse Response) | Infinite duration | Infinite | Recursive filter |

## Time-Frequency Trade-off

Narrower filters (sharper frequency selection) require longer impulse responses (more time-domain spread). You cannot have both sharp frequency cutoff and compact time response:

$$\omega_c \cdot t_r \approx \text{constant}$$
