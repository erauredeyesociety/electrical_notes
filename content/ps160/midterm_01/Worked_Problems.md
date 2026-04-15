# PS 160 — Midterm 1 Worked Problems (Handwritten Solutions)

This is the same exam as [MT1_make_up.md](MT1_make_up.md) but scanned with handwritten solutions by the instructor. Below is a clean transcription of the **methods** and **numerical answers** used in the solutions.

---

## Knowledge questions — answer key

| # | Answer |
|---|---|
| 1 | $\rho = m/V$; $p = F/A$ |
| 2 | $dp/dy = -\rho g$; $p_2 = p_1 + \rho g h$ (with $h = y_1 - y_2$) |
| 3 | $\rho A v = \text{const}$; $p + \tfrac{1}{2}\rho v^2 + \rho g y = \text{const}$ |
| 4 | $\ddot x + \omega^2 x = 0$; $x(t) = A\cos(\omega t + \varphi)$ |
| 5 | $\omega = \sqrt{k/m}$, $\omega = \sqrt{g/\ell}$, $\omega = \sqrt{mgd/I}$ |
| 6 | $f = 1/T$, $\omega = 2\pi f = 2\pi/T$ |
| 7a | $y = A\cos(kx - \omega t + \varphi)$; $k = 2\pi/\lambda$; $v = \lambda f = \omega/k$ |
| 7b | $v = \sqrt{F/\mu}$, $v = \sqrt{Y/\rho}$, $v = \sqrt{B/\rho}$ |
| 7c | Both ends fixed / open-open pipe: $f_n = nv/(2L)$, $\lambda_n = 2L/n$. One end closed: $f_n = nv/(4L)$, $n$ odd. |
| 7d | $P_\text{av} = \tfrac{1}{2}\sqrt{F\mu}\,A^2\omega^2$; $I = \tfrac{1}{2}\sqrt{B\rho}\,A^2\omega^2$ |
| 7e | $p_\text{max} = BkA$; $I_1 r_1^2 = I_2 r_2^2$ |
| 7f | $\beta = (10\text{ dB})\log_{10}(I/I_0)$, $I_0 = 10^{-12}$ W/m² |
| 7g | $f' = f_S\,(v\pm v_L)/(v\pm v_S)$; $f_\text{beat} = f_2 - f_1$ |

---

## Calculation questions — solutions

**1. Mercury column pressure.** $h = 47\text{ cm} = 0.47$ m, $\rho = 13{,}600$ kg/m³, $p_0 = 105{,}368$ Pa.
$$p = p_0 + \rho g h = 105{,}368 + (13{,}600)(9.8)(0.47) \approx 168{,}000\text{ Pa}$$

**2. Hydraulic jack.** $r_\text{in} = 0.17$ m, $r_\text{out} = 1.48$ m, $F_\text{in} = 413$ N.
$$\frac{F_\text{in}}{A_\text{in}} = \frac{F_\text{out}}{A_\text{out}}\Rightarrow F_\text{out} = F_\text{in}\left(\frac{r_\text{out}}{r_\text{in}}\right)^2 = 413(1.48/0.17)^2 \approx 31{,}300\text{ N}$$
$$p = F_\text{in}/(\pi r_\text{in}^2) = 413/(\pi\cdot 0.17^2)\approx 4550\text{ Pa}$$

**3. Hose → pool.** Pool volume $= 3\cdot 3\cdot 8 = 72$ m³. Time $= 3\text{ hr} = 10{,}800$ s. Hose area $A = \pi(0.019)^2 \approx 1.134\times 10^{-3}$ m².
$$v = \frac{V}{A\,t} = \frac{72}{(1.134\times 10^{-3})(10{,}800)}\approx 5.88\text{ m/s}$$

**4. Spring period.** $T = 2\pi\sqrt{m/k} = 2\pi\sqrt{4.4/624}\approx 0.528$ s.

**5. Oscillator $\omega$.** $E = \tfrac{1}{2}k A^2 = \tfrac{1}{2}m\omega^2 A^2\Rightarrow \omega = \sqrt{2E/(mA^2)} = \sqrt{2(4.0)/((0.25)(0.20)^2)} = \sqrt{800}\approx 28.28$ rad/s.

**6. Pendulum frequency.** Mass irrelevant.
$$f = \frac{1}{2\pi}\sqrt{g/\ell} = \frac{1}{2\pi}\sqrt{5.9/0.67}\approx 0.472\text{ Hz}$$

**7. Wave $y = 5\cos(3t + 0.5 x - 2.1)$.**
(a) $A = 5$ m
(b) $\omega = 3$ rad/s
(c) $k = 0.5$ rad/m
(d) $\varphi = -2.1$ rad
(e) $f = 3/(2\pi)\approx 0.477$ Hz
(f) $T = 2\pi/3\approx 2.094$ s
(g) $\lambda = 2\pi/0.5\approx 12.57$ m
(h) $v = \omega/k = 6$ m/s
(i) $\partial y/\partial t|_{(0,0)} = -(5)(3)\sin(-2.1) = 15\sin(2.1)\approx 12.97$ m/s

**8. Piano wire second harmonic.** $\mu = 12.0\times 10^{-3}$ kg/m, $F = 8000$ N, $L = 2.00$ m.
$$v = \sqrt{F/\mu} = \sqrt{8000/0.012}\approx 816.5\text{ m/s}$$
$$f_n = n v/(2L)\Rightarrow f_2 = 2(816.5)/(2\cdot 2.00)\approx 408.2\text{ Hz}$$

**9. Bulk modulus from sound speed.** $v = 20.8/0.011\approx 1891$ m/s, $\rho = 1229$ kg/m³.
$$B = \rho v^2\approx 4.40\times 10^9\text{ Pa} = 4.40\text{ GPa}$$

**10. Intensity from 4 sirens at 119 dB.** Single siren: $I_1 = I_0\cdot 10^{119/10} = 10^{-12}\cdot 10^{11.9}\approx 0.794$ W/m². Total:
$$I_\text{tot} = 4 I_1 \approx 3.18\text{ W/m}^2$$

**11. Beat frequency.** $f_a = 1/(1.860\times 10^{-3}) = 537.63$ Hz, $f_b = 1/(1.889\times 10^{-3}) = 529.38$ Hz.
$$\Delta f = |f_a - f_b|\approx 8.25\text{ Hz}$$

**12. Doppler: receding motorcyclist.** $v = 340$ m/s, $v_L = 49$ m/s (moving away from source), $v_S = 0$, $f_S = 439$ Hz.
$$f' = f_S\cdot\frac{v - v_L}{v} = 439\cdot\frac{340 - 49}{340}\approx 375.75\text{ Hz}$$

**Bonus — minimum frequency for two-path constructive interference.** $\Delta r = 21.0 - 20.0 = 1.0$ m. Smallest $m = 1$:
$$\lambda = \Delta r = 1.0\text{ m},\qquad f = v/\lambda = 340/1 = 340\text{ Hz}$$
