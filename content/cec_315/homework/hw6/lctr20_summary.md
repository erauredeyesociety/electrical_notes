# Lecture 20: Inverse z-Transform, Pole-Zero Analysis, and Properties

**Textbook Reference:** Sections 10.3--10.6 (Pages 757--774)

---

## 1. Inverse z-Transform: Practical Method (Partial Fractions)

### Step-by-Step Procedure

1. **Write X(z) as a proper fraction in z^{-1}** (degree of numerator <= degree of denominator in z^{-1}). If not proper, perform **long division first** to extract a polynomial in z^{-1} (inverts to delta functions).
2. **Expand into partial fractions** of the form: A_i / (1 - d_i z^{-1})
3. **Invert each term** using table pairs. Use the **ROC** to decide right-sided vs. left-sided.

### ROC Direction Rule

For a pole at z = d_i:

| ROC Region | Time-Domain Signal | Type |
|---|---|---|
| ROC **outside** \|d_i\| | d_i^n u[n] | Right-sided (causal) |
| ROC **inside** \|d_i\| | **-** d_i^n u[-n - 1] | Left-sided (anti-causal) |

> **Critical:** Do not forget the **negative sign** for left-sided terms.

---

## 2. Key Z-Transform Pairs (for Inversion)

| X(z) | x[n] (right-sided, ROC: \|z\| > \|a\|) |
|---|---|
| 1 / (1 - a z^{-1}) | a^n u[n] |
| a z^{-1} / (1 - a z^{-1})^2 | n a^n u[n] |
| 1 / (1 - a z^{-1})^2 | (n+1) a^n u[n] |
| (1 - r cos(w0) z^{-1}) / (1 - 2r cos(w0) z^{-1} + r^2 z^{-2}) | r^n cos(w0 n) u[n] |
| (r sin(w0) z^{-1}) / (1 - 2r cos(w0) z^{-1} + r^2 z^{-2}) | r^n sin(w0 n) u[n] |

---

## 3. Worked Examples

### 3.1 Distinct Real Poles (Right-Sided)

**Given:** X(z) = (3 - z^{-1}) / [(1 - 0.5z^{-1})(1 - 0.25z^{-1})], |z| > 0.5

**Partial fractions:** Set up A/(1 - 0.5z^{-1}) + B/(1 - 0.25z^{-1})

- Multiply through by denominator: 3 - z^{-1} = A(1 - 0.25z^{-1}) + B(1 - 0.5z^{-1})
- Set z^{-1} = 1/0.5 = 2: 1 = 0.5A => **A = 2**
- Set z^{-1} = 1/0.25 = 4: -1 = -B => **B = 1**

**Result:** x[n] = 2(0.5)^n u[n] + (0.25)^n u[n]

**Check with initial-value theorem:** x[0] = 2 + 1 = 3. X(z)|_{z->inf} = 3/1 = 3. Matches.

### 3.2 Two-Sided Signal (Annular ROC)

**Given:** X(z) = 1 / [(1 - 2z^{-1})(1 - 0.5z^{-1})], 0.5 < |z| < 2

**Partial fractions:**
- Set z^{-1} = 1/2 to kill (1 - 2z^{-1}): A = 4/3
- Set z^{-1} = 1/0.5 = 2 to kill (1 - 0.5z^{-1}): B = -1/3

**Assign directions from annular ROC:**
- Pole at z = 2: ROC is **inside** this pole => **left-sided**
- Pole at z = 0.5: ROC is **outside** this pole => **right-sided**

**Result:** x[n] = -(4/3) * 2^n u[-n-1] - (1/3) * (0.5)^n u[n]

### 3.3 Repeated Poles

**Given:** X(z) = 1 / (1 - 0.5z^{-1})^2, |z| > 0.5

**Use the pair:** 1/(1 - az^{-1})^2 <-> (n+1) a^n u[n]

**Result:** x[n] = (n+1)(0.5)^n u[n]

**Check:** x[0] = 1, x[1] = 2(0.5) = 1, x[2] = 3(0.25) = 0.75

### 3.4 Complex Conjugate Poles (Damped Sinusoid)

**Given:** X(z) = [1 - 0.8cos(0.4pi) z^{-1}] / [1 - 2(0.8)cos(0.4pi) z^{-1} + 0.64 z^{-2}], |z| > 0.8

**Identify parameters by matching** to the table pair for r^n cos(w0 n) u[n]:
- r = 0.8, w0 = 0.4pi
- Poles at z = 0.8 e^{+/- j0.4pi}

**Result:** x[n] = (0.8)^n cos(0.4pi n) u[n]

Damped sinusoid with envelope (0.8)^n (decays since r < 1).

---

## 4. Geometric Evaluation of Frequency Response

To get H(e^{jw}) from the pole-zero plot, evaluate H(z) on the unit circle (z = e^{jw}):

```
|H(e^{jw})| = |K| * product_i |e^{jw} - z_i| / product_i |e^{jw} - p_i|
```

**Rules:**
- **Near a pole:** denominator vector is short => |H| is **large** (peak)
- **Near a zero:** numerator vector is short => |H| is **small** (notch)
- Poles **near** the unit circle => sharp peaks
- Poles **far** from the unit circle => broad, gentle bumps
- Poles **on** the unit circle => infinite peaks (marginally stable)

**Frequency mapping:**
- w = 0 corresponds to z = 1 (DC, low frequency)
- w = pi corresponds to z = -1 (Nyquist frequency, high frequency)

---

## 5. Z-Transform Properties Table

| Property | Sequence | z-Domain / ROC |
|---|---|---|
| Linearity | a x1[n] + b x2[n] | a X1(z) + b X2(z), ROC >= R1 intersect R2 |
| Time shifting | x[n - n0] | z^{-n0} X(z), ROC = Rx (possibly add/remove z=0, inf) |
| z-domain scaling | z0^n x[n] | X(z/z0), ROC = \|z0\| * Rx |
| Time reversal | x[-n] | X(z^{-1}), ROC = 1/Rx |
| **Convolution** | x1[n] * x2[n] | **X1(z) * X2(z)**, ROC >= R1 intersect R2 |
| Differentiation in z | n x[n] | -z (d/dz) X(z), ROC = Rx |
| First difference | x[n] - x[n-1] | (1 - z^{-1}) X(z) |
| Accumulation | sum_{k=-inf}^{n} x[k] | X(z) / (1 - z^{-1}), ROC >= Rx intersect {\|z\| > 1} |

### Most Important Properties

- **Convolution <-> Multiplication:** y[n] = x[n] * h[n] <=> Y(z) = X(z) H(z). Foundation of DT system analysis.
- **Time shift <-> z^{-n0}:** A delay of one sample = multiply by z^{-1} (the "unit delay operator").

### Worked Example: Time Shifting

Given x[n] = (0.5)^n u[n] <-> 1/(1 - 0.5z^{-1}), |z| > 0.5

Find Z{x[n-3]} = Z{(0.5)^{n-3} u[n-3]}:

Y(z) = z^{-3} / (1 - 0.5z^{-1}), |z| > 0.5

The delay of 3 samples introduces z^{-3}, adding 3 zeros at z = 0.

---

## 6. Initial-Value and Final-Value Theorems

### Initial-Value Theorem (causal sequences, x[n] = 0 for n < 0)

```
x[0] = lim_{z -> inf} X(z)
```

For a proper rational X(z) in z^{-1}, just set all z^{-1} terms to zero.

### Final-Value Theorem (causal sequences with finite steady state)

```
lim_{n -> inf} x[n] = lim_{z -> 1} (1 - z^{-1}) X(z)
```

**WARNING:** Only valid if lim x[n] actually exists as a finite number. Check that all poles of (1 - z^{-1})X(z) are strictly inside the unit circle before applying.

### Worked Example: Both Theorems

Given: X(z) = 5 / [(1 - z^{-1})(1 - 0.6z^{-1})], ROC: |z| > 1

- **Initial value:** x[0] = lim_{z->inf} X(z) = 5/(1)(1) = **5**
- **Final value check:** (1 - z^{-1})X(z) = 5/(1 - 0.6z^{-1}), pole at z = 0.6 (inside unit circle) -- theorem applies.
- **Final value:** x[inf] = lim_{z->1} 5/(1 - 0.6) = 5/0.4 = **12.5**

---

## 7. Common Mistakes to Avoid

1. **Always do partial fractions in z^{-1}**, not positive powers of z.
2. **ROC outside pole => right-sided.** ROC inside pole => left-sided. "Outside" means |z| > |pole|.
3. **Left-sided terms have a negative sign:** -a^n u[-n-1], not a^n u[-n-1].
4. **Improper fractions:** If numerator degree >= denominator degree in z^{-1}, do long division first.
5. **Frequency mapping:** w = 0 is z = 1 (not z = 0). w = pi is z = -1.
