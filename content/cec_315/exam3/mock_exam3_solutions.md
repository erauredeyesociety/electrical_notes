# CEC 315 — Mock Exam 3 — Solution Key

**Coverage:** Lectures 16–23 (Laplace, Z-transform, Sampling, Feedback)
**Course:** CEC 315 — Signals and Systems — Spring 2026

---

## Part I: Multiple Choice — Answer Key

**1.** Answer: **(b) $T = 0.5$ ms.**

The bandlimit is $\omega_M = 1500\pi$ rad/s, i.e., $f_M = 750$ Hz. The Nyquist rate is $2 f_M = 1500$ Hz, so we need $f_s > 1500$ Hz, i.e., $T < 1/1500$ s $\approx 0.667$ ms.

- (a) $T=1.0$ ms $\Rightarrow f_s=1000$ Hz — aliases.
- (b) $T=0.5$ ms $\Rightarrow f_s=2000$ Hz — works. ✓
- (c) $T=2.0$ ms $\Rightarrow f_s=500$ Hz — aliases.
- (d) $T=0.75$ ms $\Rightarrow f_s\approx 1333$ Hz — aliases.

**2.** Answer: **(c) $100$ Hz.**

The analog tone is at $f_0 = 300$ Hz. Sampling at $f_s=400$ Hz (Nyquist rate needed is $600$ Hz), the alias is
$$f_{\text{alias}} = |f_s - f_0| = |400 - 300| = 100\text{ Hz}.$$

**3.** Answer: **(c) Unstable, because one pole is in the RHP.**

Poles: $s=-1$ (LHP), $s=+2$ (RHP). For a causal LTI system, stability requires **all** poles in the open LHP; one RHP pole makes the system unstable. The zero location is irrelevant for BIBO stability.

**4.** Answer: **(b) $K > 0$.**

The closed-loop transfer function is
$$Q(s) = \frac{K/[s(s+4)]}{1 + K/[s(s+4)]} = \frac{K}{s^2 + 4s + K}.$$
Stability (Routh or direct check on $s^2+4s+K$) requires all coefficients positive: $4>0$ (always) and $K>0$.

**5.** Answer: **(c) $0.3 < |z| < 1.5$.**

Two-sided signals have annular ROCs between two poles. The annulus between the two poles is $0.3<|z|<1.5$. Option (a) would be purely right-sided (causal), (b) purely left-sided (anti-causal), and (d) does not include the constraint $|z|<1.5$.

---

## Part II: Problems — Full Solutions

---

### Problem 1 — Laplace Inverse with Bilateral ROC

**Given.** $X(s) = \dfrac{7s+2}{(s+2)(s-1)},\ -2 < \operatorname{Re}\{s\} < 1.$

**(a) Poles and ROC sketch.**

Poles: $s_1 = -2$ and $s_2 = +1$. The ROC is the vertical strip $-2 < \operatorname{Re}\{s\} < 1$ (between the two poles), and does not include either pole.

```
              Im{s}
                |
        ROC ░░░░|░░░░
       -2 ░░░░░░|░░░░░ +1
        x ░░░░░░|░░░░░ x   -> Re{s}
          ░░░░░░|░░░░░
                |
```

**(b) Partial fractions.** Write
$$X(s) = \frac{A}{s+2} + \frac{B}{s-1}.$$

Cover-up at $s=-2$:
$$A = \left.\frac{7s+2}{s-1}\right|_{s=-2} = \frac{-14+2}{-3} = \frac{-12}{-3} = 4.$$

Cover-up at $s=+1$:
$$B = \left.\frac{7s+2}{s+2}\right|_{s=1} = \frac{7+2}{3} = \frac{9}{3} = 3.$$

So $X(s) = \dfrac{4}{s+2} + \dfrac{3}{s-1}.$

Sanity check: $\frac{4(s-1)+3(s+2)}{(s+2)(s-1)} = \frac{4s-4+3s+6}{(s+2)(s-1)} = \frac{7s+2}{(s+2)(s-1)}.$ ✓

**(c) Assigning directions from the ROC.**

The ROC is $-2<\operatorname{Re}\{s\}<1$:

- Pole at $s=-2$: ROC is to the **right** of this pole ⇒ **right-sided** term:
  $\dfrac{4}{s+2} \Leftrightarrow 4e^{-2t}u(t)$.
- Pole at $s=+1$: ROC is to the **left** of this pole ⇒ **left-sided** term:
  $\dfrac{3}{s-1} = -\dfrac{-3}{s-1} \Leftrightarrow -3e^{t}u(-t)$.

$$\boxed{\,x(t) = 4e^{-2t}u(t) \;-\; 3e^{t}u(-t)\,.}$$

**(d) Fourier transform.**

**Yes** — the ROC contains the $j\omega$-axis ($\operatorname{Re}\{s\}=0 \in (-2,1)$), so the Fourier transform exists and is given by $X(j\omega) = X(s)\big|_{s=j\omega}$.

---

### Problem 2 — Unilateral Laplace IVP with ZSR/ZIR Split

**Given.** $y'' + 4y' + 3y = 2u(t)$, $y(0^-) = 2$, $y'(0^-) = -1$.

**(a) Transform.**

Using $\mathcal{L}\{y'\} = sY - y(0^-)$ and $\mathcal{L}\{y''\} = s^2 Y - s y(0^-) - y'(0^-)$:
$$\bigl[s^2 Y - 2s - (-1)\bigr] + 4\bigl[sY - 2\bigr] + 3Y = \frac{2}{s}.$$
$$(s^2+4s+3)Y \;-\; 2s + 1 \;-\; 8 \;=\; \frac{2}{s}.$$
$$(s^2+4s+3)Y = \frac{2}{s} + 2s + 7.$$

Factor $s^2+4s+3 = (s+1)(s+3)$:
$$Y(s) = \frac{2/s + 2s + 7}{(s+1)(s+3)} = \frac{2 s^2 + 7 s + 2}{s(s+1)(s+3)}.$$

**(b) ZIR / ZSR decomposition.**

- **Zero-Input Response** (set input $=0$, keep ICs): $(s^2+4s+3)Y_{\text{zir}} = 2s + 7$
  $$Y_{\text{zir}}(s) = \frac{2s+7}{(s+1)(s+3)}.$$

- **Zero-State Response** (set ICs $=0$, keep input): $(s^2+4s+3)Y_{\text{zsr}} = 2/s$
  $$Y_{\text{zsr}}(s) = \frac{2}{s(s+1)(s+3)}.$$

Check: $Y_{\text{zir}} + Y_{\text{zsr}} = \dfrac{(2s+7)\cdot s + 2}{s(s+1)(s+3)} = \dfrac{2s^2+7s+2}{s(s+1)(s+3)} = Y(s).$ ✓

**(c) Invert each piece.**

*ZIR PFE:* $\dfrac{2s+7}{(s+1)(s+3)} = \dfrac{A}{s+1} + \dfrac{B}{s+3}$

- $s=-1$: $A = (-2+7)/2 = 5/2$.
- $s=-3$: $B = (-6+7)/(-2) = -1/2$.

$$y_{\text{zir}}(t) = \left[\tfrac{5}{2}e^{-t} - \tfrac{1}{2}e^{-3t}\right]u(t).$$

*ZSR PFE:* $\dfrac{2}{s(s+1)(s+3)} = \dfrac{C}{s}+\dfrac{D}{s+1}+\dfrac{E}{s+3}$

- $s=0$: $C = 2/[(1)(3)] = 2/3$.
- $s=-1$: $D = 2/[(-1)(2)] = -1$.
- $s=-3$: $E = 2/[(-3)(-2)] = 1/3$.

$$y_{\text{zsr}}(t) = \left[\tfrac{2}{3} - e^{-t} + \tfrac{1}{3}e^{-3t}\right]u(t).$$

**(d) Total response and verification.**

$$y(t) = y_{\text{zir}}(t) + y_{\text{zsr}}(t) = \left[\tfrac{2}{3} + \left(\tfrac{5}{2} - 1\right)e^{-t} + \left(-\tfrac{1}{2}+\tfrac{1}{3}\right)e^{-3t}\right]u(t)$$

$$\boxed{\,y(t) = \left[\tfrac{2}{3} + \tfrac{3}{2}e^{-t} - \tfrac{1}{6}e^{-3t}\right]u(t)\,.}$$

*Verification of ICs* (evaluate the smooth part at $t=0$):

- $y(0) = \tfrac{2}{3} + \tfrac{3}{2} - \tfrac{1}{6} = \tfrac{4}{6} + \tfrac{9}{6} - \tfrac{1}{6} = \tfrac{12}{6} = 2.$ ✓
- $y'(t) = -\tfrac{3}{2}e^{-t} + \tfrac{1}{2}e^{-3t}\Rightarrow y'(0) = -\tfrac{3}{2} + \tfrac{1}{2} = -1.$ ✓

*Steady state:* $y(\infty) = 2/3$ (matches the DC gain $H(0)\cdot 2 = (1/3)\cdot 2 = 2/3$).

---

### Problem 3 — Z-Transform Inverse with Annular ROC

**Given.** $X(z) = \dfrac{1+z^{-1}}{(1-0.4z^{-1})(1+0.2z^{-1})},\ 0.2 < |z| < 0.4.$

**(a) Pole-zero plot.**

- Poles: $z = 0.4$ and $z = -0.2$.
- Zero (from $1+z^{-1}=0 \Rightarrow z = -1$). Also a zero at $z=0$ from the $z^{-1}$ factor if we track the rational-in-$z$ form, but the essential zero to state is $z=-1$.
- ROC: annulus $0.2 < |z| < 0.4$, lying **between** the two poles. (The unit circle $|z|=1$ is **outside** the ROC.)

**(b) Partial fraction expansion.**

$$X(z) = \frac{A}{1-0.4z^{-1}} + \frac{B}{1+0.2z^{-1}}.$$

*Cover-up at $z^{-1}=1/0.4 = 2.5$* (killing the first factor):
$$A = \left.\frac{1+z^{-1}}{1+0.2z^{-1}}\right|_{z^{-1}=2.5} = \frac{1+2.5}{1+0.5} = \frac{3.5}{1.5} = \frac{7}{3}.$$

*Cover-up at $z^{-1}=1/(-0.2)=-5$* (killing the second factor):
$$B = \left.\frac{1+z^{-1}}{1-0.4z^{-1}}\right|_{z^{-1}=-5} = \frac{1+(-5)}{1-0.4(-5)} = \frac{-4}{1+2} = \frac{-4}{3}.$$

Check numerator: $\tfrac{7}{3}(1+0.2z^{-1}) - \tfrac{4}{3}(1-0.4z^{-1}) = \tfrac{7-4}{3} + \tfrac{1.4+1.6}{3}z^{-1} = 1 + z^{-1}.$ ✓

**(c) Directions from the ROC $0.2 < |z| < 0.4$.**

- Pole at $z=0.4$: ROC is **inside** this pole (i.e., $|z|<0.4$) ⇒ **left-sided**:
  $\dfrac{7/3}{1-0.4z^{-1}} \Leftrightarrow -\tfrac{7}{3}(0.4)^n u[-n-1].$
- Pole at $z=-0.2$: ROC is **outside** this pole (i.e., $|z|>0.2$) ⇒ **right-sided**:
  $\dfrac{-4/3}{1+0.2z^{-1}} = \dfrac{-4/3}{1-(-0.2)z^{-1}} \Leftrightarrow -\tfrac{4}{3}(-0.2)^n u[n].$

$$\boxed{\,x[n] = -\tfrac{7}{3}(0.4)^n\,u[-n-1] \;-\; \tfrac{4}{3}(-0.2)^n\,u[n]\,.}$$

**(d) Absolute summability.**

**Yes** — the ROC $0.2 < |z| < 0.4$ contains no point of the unit circle... wait, does it? The unit circle is $|z|=1$, which is **outside** the annulus (since $1 > 0.4$). Therefore the ROC does **not** contain the unit circle, and $x[n]$ is **not** absolutely summable; its DTFT does **not** exist.

---

### Problem 4 — Unilateral Z with Initial Conditions

**Given.** $y[n] - \tfrac{1}{6}y[n-1] - \tfrac{1}{6}y[n-2] = x[n]$, $x[n]=u[n]$, $y[-1]=6$, $y[-2]=0$.

**(a) Transform.**

Using $\mathcal{Z}\{y[n-1]\} = z^{-1}Y + y[-1]$ and $\mathcal{Z}\{y[n-2]\} = z^{-2}Y + z^{-1}y[-1] + y[-2]$:

$$Y - \tfrac{1}{6}\bigl(z^{-1}Y + 6\bigr) - \tfrac{1}{6}\bigl(z^{-2}Y + 6z^{-1} + 0\bigr) = \frac{1}{1-z^{-1}}.$$

$$\bigl(1 - \tfrac{1}{6}z^{-1} - \tfrac{1}{6}z^{-2}\bigr)Y \;-\; 1 \;-\; z^{-1} = \frac{1}{1-z^{-1}}.$$

$$\bigl(1 - \tfrac{1}{6}z^{-1} - \tfrac{1}{6}z^{-2}\bigr)Y = \frac{1}{1-z^{-1}} + 1 + z^{-1} = \frac{1 + (1+z^{-1})(1-z^{-1})}{1-z^{-1}} = \frac{2 - z^{-2}}{1-z^{-1}}.$$

**(b) Factor and stability.**

$$1 - \tfrac{1}{6}z^{-1} - \tfrac{1}{6}z^{-2} = \bigl(1 - \tfrac{1}{2}z^{-1}\bigr)\bigl(1 + \tfrac{1}{3}z^{-1}\bigr),$$
which can be verified: $1 + \tfrac{1}{3}z^{-1} - \tfrac{1}{2}z^{-1} - \tfrac{1}{6}z^{-2} = 1 - \tfrac{1}{6}z^{-1} - \tfrac{1}{6}z^{-2}.$ ✓

**Poles:** $z = 1/2$ and $z = -1/3$. Both are inside the unit circle, so the causal system is **BIBO stable**.

$$Y(z) = \frac{2 - z^{-2}}{(1-z^{-1})\bigl(1-\tfrac{1}{2}z^{-1}\bigr)\bigl(1+\tfrac{1}{3}z^{-1}\bigr)}.$$

**(c) PFE and inversion.**

$$Y(z) = \frac{A}{1-z^{-1}} + \frac{B}{1-\tfrac{1}{2}z^{-1}} + \frac{C}{1+\tfrac{1}{3}z^{-1}}.$$

Cover-up at $z^{-1}=1$:
$$A = \frac{2-1}{(1-\tfrac{1}{2})(1+\tfrac{1}{3})} = \frac{1}{(1/2)(4/3)} = \frac{1}{2/3} = \frac{3}{2}.$$

Cover-up at $z^{-1}=2$:
$$B = \frac{2-4}{(1-2)(1+\tfrac{2}{3})} = \frac{-2}{(-1)(5/3)} = \frac{-2}{-5/3} = \frac{6}{5}.$$

Cover-up at $z^{-1}=-3$:
$$C = \frac{2-9}{(1-(-3))(1-\tfrac{1}{2}(-3))} = \frac{-7}{(4)(5/2)} = \frac{-7}{10}.$$

Check: $A+B+C = \tfrac{3}{2} + \tfrac{6}{5} - \tfrac{7}{10} = \tfrac{15+12-7}{10} = \tfrac{20}{10} = 2$, which must match the numerator of $Y(z)$ at $z^{-1}=0$. ✓

Since the causal system is stable and all three terms correspond to right-sided sequences:

$$\boxed{\,y[n] = \left[\tfrac{3}{2} + \tfrac{6}{5}\bigl(\tfrac{1}{2}\bigr)^{n} - \tfrac{7}{10}\bigl(-\tfrac{1}{3}\bigr)^{n}\right]u[n]\,.}$$

**(d) Verification from the recursion.**

From the difference equation: $y[n] = \tfrac{1}{6}y[n-1] + \tfrac{1}{6}y[n-2] + x[n]$.

- $y[0] = \tfrac{1}{6}(6) + \tfrac{1}{6}(0) + 1 = 1 + 0 + 1 = 2.$
- $y[1] = \tfrac{1}{6}y[0] + \tfrac{1}{6}y[-1] + 1 = \tfrac{2}{6} + \tfrac{6}{6} + 1 = \tfrac{1}{3} + 1 + 1 = \tfrac{7}{3}.$

From closed form:

- $y[0] = \tfrac{3}{2} + \tfrac{6}{5} - \tfrac{7}{10} = \tfrac{15+12-7}{10} = \tfrac{20}{10} = 2.$ ✓
- $y[1] = \tfrac{3}{2} + \tfrac{6}{5}\cdot\tfrac{1}{2} - \tfrac{7}{10}\cdot(-\tfrac{1}{3}) = \tfrac{3}{2} + \tfrac{3}{5} + \tfrac{7}{30} = \tfrac{45+18+7}{30} = \tfrac{70}{30} = \tfrac{7}{3}.$ ✓

*Steady state:* $y[\infty] = 3/2$ (the other terms decay geometrically).

---

*End of Solution Key — Mock Exam 3 — CEC 315, Spring 2026.*
