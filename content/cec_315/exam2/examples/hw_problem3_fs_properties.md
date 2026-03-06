# Problem 3: CT Fourier Series Properties

## Setup

**Given:** $x(t)$ real-valued, $T = \pi$, $\omega_0 = 2$ rad/s, with coefficients:

$$a_0 = 2, \quad a_{\pm1} = 1, \quad a_{\pm2} = 1/4, \quad a_{\pm3} = 1/9, \quad a_k = 0 \text{ for } |k| > 3$$

## Part (a): Linearity

### FS coefficients of $\sin(2t)$

With $\omega_0 = 2$: $\sin(2t) = \frac{e^{j2t} - e^{-j2t}}{2j}$

$$b_1 = \frac{1}{2j} = -\frac{j}{2}, \quad b_{-1} = -\frac{1}{2j} = \frac{j}{2}, \quad b_k = 0 \text{ otherwise}$$

### Coefficients of $w(t) = 4x(t) + 6\sin(2t)$

By linearity: $c_k = 4a_k + 6b_k$

| $k$ | $4a_k$ | $6b_k$ | $c_k$ |
|---|---|---|---|
| 0 | 8 | 0 | **8** |
| 1 | 4 | $-3j$ | **$4-3j$** |
| -1 | 4 | $3j$ | **$4+3j$** |
| $\pm 2$ | 1 | 0 | **1** |
| $\pm 3$ | 4/9 | 0 | **4/9** |

Note: $c_{-1} = (c_1)^*$ as expected for a real signal.

## Part (b): Time-Shifting Property

**Given:** $y(t) = x(t - \pi/4)$, so $t_0 = \pi/4$, $\omega_0 = 2$

$$b_k = a_k \, e^{-jk\omega_0 t_0} = a_k \, e^{-jk\pi/2}$$

| $k$ | $a_k$ | $e^{-jk\pi/2}$ | $b_k$ |
|---|---|---|---|
| 0 | 2 | 1 | 2 |
| $\pm 1$ | 1 | $\mp j$ | $\mp j$ |
| $\pm 2$ | 1/4 | $-1$ | $-1/4$ |
| $\pm 3$ | 1/9 | $\pm j$ | $\pm j/9$ |

**Key insight:** $|b_k| = |a_k|$ for all $k$. Time shifting changes phase only, so **power is preserved**.

## Part (c): Differentiation Property

**Given:** $g(t) = dx(t)/dt$ with $d_k = jk\omega_0 \, a_k = 2jk \, a_k$

| $k$ | $a_k$ | $d_k = 2jk \cdot a_k$ | $|d_k|$ |
|---|---|---|---|
| 0 | 2 | 0 | 0 |
| $\pm 1$ | 1 | $\pm 2j$ | 2 |
| $\pm 2$ | 1/4 | $\pm j$ | 1 |
| $\pm 3$ | 1/9 | $\pm 2j/3$ | 2/3 |

**Key insight:** Differentiation amplifies higher harmonics by factor $k$. DC is always killed. This is why differentiation "sharpens" signals and amplifies noise.

## Part (d): Parseval's Theorem

$$P_x = \sum_{k=-\infty}^{\infty} |a_k|^2 = |a_0|^2 + 2(|a_1|^2 + |a_2|^2 + |a_3|^2)$$

$$= 4 + 2\left(1 + \frac{1}{16} + \frac{1}{81}\right) = 4 + 2(1.07485) = 6.1497$$

DC fraction: $|a_0|^2 / P_x = 4/6.1497 \approx$ **65%** of total power.
