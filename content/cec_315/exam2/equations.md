# Equations Reference: Fourier Analysis (Lectures 9-14)

## CT Fourier Series (CTFS)

$$x(t) = \sum_{k=-\infty}^{\infty} a_k \, e^{jk\omega_0 t} \qquad a_k = \frac{1}{T} \int_T x(t) \, e^{-jk\omega_0 t} \, dt \qquad \omega_0 = \frac{2\pi}{T}$$

## DT Fourier Series (DTFS)

$$x[n] = \sum_{k=\langle N \rangle} a_k \, e^{jk(2\pi/N)n} \qquad a_k = \frac{1}{N} \sum_{n=\langle N \rangle} x[n] \, e^{-jk(2\pi/N)n} \qquad \omega_0 = \frac{2\pi}{N}$$

## CT Fourier Transform (CTFT)

$$X(j\omega) = \int_{-\infty}^{\infty} x(t) \, e^{-j\omega t} \, dt \qquad x(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} X(j\omega) \, e^{j\omega t} \, d\omega$$

## DT Fourier Transform (DTFT)

$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] \, e^{-j\omega n} \qquad x[n] = \frac{1}{2\pi} \int_{2\pi} X(e^{j\omega}) \, e^{j\omega n} \, d\omega$$

## System Function / Frequency Response

$$H(j\omega) = \int_{-\infty}^{\infty} h(\tau) e^{-j\omega\tau} d\tau \qquad H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} h[n] \, e^{-j\omega n}$$

For causal $h(t) = e^{-at}u(t)$: $\quad H(j\omega) = \dfrac{1}{a + j\omega}$

For causal $h[n] = a^n u[n]$: $\quad H(e^{j\omega}) = \dfrac{1}{1 - ae^{-j\omega}}$

## LTI Output (Periodic Input)

$$b_k = a_k \cdot H(jk\omega_0) \qquad \text{(CT)} \qquad b_k = a_k \cdot H(e^{jk\omega_0}) \qquad \text{(DT)}$$

## Convolution Property

$$y(t) = x(t) * h(t) \iff Y(j\omega) = X(j\omega) H(j\omega)$$

$$y[n] = x[n] * h[n] \iff Y(e^{j\omega}) = X(e^{j\omega}) H(e^{j\omega})$$

## Multiplication Property

$$x(t) y(t) \iff \frac{1}{2\pi} X(j\omega) * Y(j\omega)$$

## Key FT Properties (CT)

| Property | Time | Frequency |
|---|---|---|
| Time Shift | $x(t - t_0)$ | $e^{-j\omega t_0} X(j\omega)$ |
| Freq Shift | $e^{j\omega_0 t} x(t)$ | $X(j(\omega - \omega_0))$ |
| Scaling | $x(at)$ | $\frac{1}{\|a\|} X(j\omega/a)$ |
| Differentiation | $dx/dt$ | $j\omega \, X(j\omega)$ |
| Duality | $X(jt)$ | $2\pi x(-\omega)$ |

## FS Properties (CT)

| Property | Time | Coefficients |
|---|---|---|
| Linearity | $Ax(t) + By(t)$ | $Aa_k + Bb_k$ |
| Time Shift | $x(t - t_0)$ | $a_k e^{-jk\omega_0 t_0}$ |
| Differentiation | $dx/dt$ | $jk\omega_0 \, a_k$ |

## Parseval's Relations

**CTFS (average power):**
$$\frac{1}{T} \int_T |x(t)|^2 \, dt = \sum_{k=-\infty}^{\infty} |a_k|^2$$

**CTFT (total energy):**
$$\int_{-\infty}^{\infty} |x(t)|^2 \, dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 \, d\omega$$

**DTFS:**
$$\frac{1}{N} \sum_{n=\langle N \rangle} |x[n]|^2 = \sum_{k=\langle N \rangle} |a_k|^2$$

## Conjugate Symmetry (Real Signals)

- CTFS: $a_{-k} = a_k^*$
- CTFT: $X(-j\omega) = X^*(j\omega)$ $\Rightarrow$ $|X|$ even, $\angle X$ odd

## Magnitude-Phase

$$X(j\omega) = |X(j\omega)| \, e^{j\angle X(j\omega)}$$

**Decibels:** $20\log_{10}|H(j\omega)|$ dB

**Cutoff:** $|H(j\omega_c)| = \frac{1}{\sqrt{2}} |H(0)|$ $\quad$ (-3 dB point)

## Group Delay

$$\tau(\omega) = -\frac{d}{d\omega} \angle H(j\omega)$$

Linear phase $\angle H = -\omega t_0$ $\Rightarrow$ pure delay, no distortion.

## Common FT Pairs

| $x(t)$ | $X(j\omega)$ |
|---|---|
| $e^{-at}u(t)$ | $\frac{1}{a+j\omega}$ |
| $e^{-a\|t\|}$ | $\frac{2a}{a^2+\omega^2}$ |
| $\delta(t)$ | $1$ |
| $1$ | $2\pi\delta(\omega)$ |
| $\cos(\omega_0 t)$ | $\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)]$ |
| rect pulse (width $T_1$) | $2T_1\text{sinc}(\omega T_1/\pi)$ |

## First-Order System Cutoff

For $H(j\omega) = \frac{1}{a+j\omega}$: cutoff $\omega_c = a$

For RC circuit: $\omega_c = 1/RC$

## Bandwidth-Rise Time

$$\omega_c \cdot t_r \approx \text{constant}$$
