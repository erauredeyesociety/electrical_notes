# Lecture 13: Fourier Transform Properties and Convolution

## 1. Why Properties Matter

Computing FTs from the definition (integral/sum) is tedious. Properties let us build complex transform pairs from simple ones via algebraic manipulation. The **Convolution Property** is the most important — it is the reason we use frequency-domain analysis for LTI systems.

## 2. CT Fourier Transform Properties

### Linearity
$$ax(t) + by(t) \leftrightarrow aX(j\omega) + bY(j\omega)$$

### Time Shifting
$$x(t - t_0) \leftrightarrow e^{-j\omega t_0} X(j\omega)$$

- Magnitude unchanged: $|e^{-j\omega t_0} X(j\omega)| = |X(j\omega)|$
- Phase shifted by $-\omega t_0$ (linear in $\omega$)
- **Time delay adds linear phase**

### Frequency Shifting (Modulation)
$$e^{j\omega_0 t} x(t) \leftrightarrow X(j(\omega - \omega_0))$$

- Multiplying by a complex exponential shifts the spectrum
- For real modulation: $x(t)\cos(\omega_0 t) \leftrightarrow \frac{1}{2}[X(j(\omega-\omega_0)) + X(j(\omega+\omega_0))]$

### Conjugation and Conjugate Symmetry
$$x^*(t) \leftrightarrow X^*(-j\omega)$$

For **real** $x(t)$: $X(-j\omega) = X^*(j\omega)$, meaning:
- $|X(j\omega)|$ is even
- $\angle X(j\omega)$ is odd
- $\text{Re}\{X(j\omega)\}$ is even
- $\text{Im}\{X(j\omega)\}$ is odd

### Time Scaling
$$x(at) \leftrightarrow \frac{1}{|a|} X\left(\frac{j\omega}{a}\right)$$

- Time compression → frequency expansion (and vice versa)
- **Uncertainty principle:** Can't be simultaneously narrow in both time and frequency

### Differentiation in Time
$$\frac{dx(t)}{dt} \leftrightarrow j\omega \, X(j\omega)$$

- Each differentiation multiplies by $j\omega$ — amplifies high frequencies
- **Higher-order:** $\frac{d^n x}{dt^n} \leftrightarrow (j\omega)^n X(j\omega)$
- Useful for solving differential equations in frequency domain

### Integration in Time
$$\int_{-\infty}^{t} x(\tau) \, d\tau \leftrightarrow \frac{1}{j\omega} X(j\omega) + \pi X(j0) \delta(\omega)$$

- Division by $j\omega$ — attenuates high frequencies (smoothing)
- The $\delta(\omega)$ term accounts for any DC component

### Duality (CT)
If $x(t) \leftrightarrow X(j\omega)$, then:
$$X(jt) \leftrightarrow 2\pi x(-\omega)$$

- Swaps roles of time and frequency
- Example: If rectangular pulse $\leftrightarrow$ sinc, then sinc in time $\leftrightarrow$ rectangular in frequency

### Parseval's Relation (Energy)
$$\int_{-\infty}^{\infty} |x(t)|^2 \, dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |X(j\omega)|^2 \, d\omega$$

- Total energy is the same whether computed in time or frequency
- $|X(j\omega)|^2$ is the **energy spectral density**

## 3. The Convolution Property (Most Important!)

### CT Convolution Property
$$y(t) = x(t) * h(t) \leftrightarrow Y(j\omega) = X(j\omega) \cdot H(j\omega)$$

**Convolution in time = multiplication in frequency.**

This transforms the computationally expensive convolution integral into simple pointwise multiplication. For LTI systems:
- $H(j\omega)$ is the **frequency response** (FT of impulse response $h(t)$)
- System output = input spectrum × frequency response

### DT Convolution Property
$$y[n] = x[n] * h[n] \leftrightarrow Y(e^{j\omega}) = X(e^{j\omega}) \cdot H(e^{j\omega})$$

Same principle in discrete time.

## 4. The Multiplication Property (Dual of Convolution)

### CT Multiplication Property
$$x(t) \cdot y(t) \leftrightarrow \frac{1}{2\pi} [X(j\omega) * Y(j\omega)]$$

**Multiplication in time = convolution in frequency** (with $1/(2\pi)$ factor).

This explains amplitude modulation: multiplying by $\cos(\omega_0 t)$ convolves the spectrum with two impulses, shifting it to $\pm\omega_0$.

## 5. DT Fourier Transform Properties

All CT properties have DT analogs with minor differences:

| Property | CT | DT |
|---|---|---|
| Time shift | $e^{-j\omega t_0}X(j\omega)$ | $e^{-j\omega n_0}X(e^{j\omega})$ |
| Freq shift | $X(j(\omega-\omega_0))$ | $X(e^{j(\omega-\omega_0)})$ |
| Differentiation | $j\omega X(j\omega)$ | No direct analog; use **first difference** |
| First difference | — | $x[n]-x[n-1] \leftrightarrow (1-e^{-j\omega})X(e^{j\omega})$ |
| Accumulation | Integration analog | $\sum_{k=-\infty}^{n} x[k] \leftrightarrow \frac{X(e^{j\omega})}{1-e^{-j\omega}} + \pi X(e^{j0})\sum_k \delta(\omega-2\pi k)$ |
| Convolution | $X(j\omega)H(j\omega)$ | $X(e^{j\omega})H(e^{j\omega})$ |
| Multiplication | $\frac{1}{2\pi}X*Y$ | $\frac{1}{2\pi}\int_{2\pi} X(e^{j\theta})Y(e^{j(\omega-\theta)})d\theta$ |

### DT Duality
Connects DTFT and DT Fourier Series:
- If DTFT of $x[n]$ is $X(e^{j\omega})$, and we sample this at $\omega = 2\pi k/N$, we get DT FS coefficients of a periodic extension of $x[n]$

## 6. Deriving $H(j\omega)$ from System Equations

### From CT Differential Equations
Replace $d/dt \to j\omega$ (or $d^n/dt^n \to (j\omega)^n$):

$$\sum_k b_k \frac{d^k y}{dt^k} = \sum_k a_k \frac{d^k x}{dt^k}$$

becomes:

$$H(j\omega) = \frac{Y(j\omega)}{X(j\omega)} = \frac{\sum_k a_k (j\omega)^k}{\sum_k b_k (j\omega)^k}$$

### From DT Difference Equations
Replace delay $y[n-m] \to e^{-j\omega m} Y(e^{j\omega})$:

$$\sum_k b_k y[n-k] = \sum_k a_k x[n-k]$$

becomes:

$$H(e^{j\omega}) = \frac{\sum_k a_k e^{-j\omega k}}{\sum_k b_k e^{-j\omega k}}$$

## 7. The Analysis Pipeline

The standard workflow for LTI system analysis:

| Step | Action | Tool |
|---|---|---|
| **1** | Find $X(j\omega)$ from $x(t)$ | FT definition or table + properties |
| **2** | Find $H(j\omega)$ from $h(t)$ or system equation | FT or replace $d/dt \to j\omega$ |
| **3** | Multiply: $Y(j\omega) = X(j\omega) \cdot H(j\omega)$ | Algebra |
| **4** | Inverse FT: $y(t)$ from $Y(j\omega)$ | Partial Fraction Expansion + table |

### Partial Fraction Expansion (PFE)
For rational $Y(j\omega) = N(j\omega)/D(j\omega)$:

1. Factor denominator into first-order terms: $D(j\omega) = (j\omega + p_1)(j\omega + p_2)\cdots$
2. Expand: $Y(j\omega) = \frac{A_1}{j\omega + p_1} + \frac{A_2}{j\omega + p_2} + \cdots$
3. Each term $\frac{A_i}{j\omega + p_i}$ corresponds to $A_i e^{-p_i t} u(t)$ (if causal, $p_i > 0$)

**Cover-up method** for finding coefficients:
$$A_i = (j\omega + p_i) Y(j\omega) \Big|_{j\omega = -p_i}$$
