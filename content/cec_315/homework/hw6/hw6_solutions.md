# CEC 315 HW6 Solutions — Z-Transform (Lectures 19-21)

---

## Problem 1: Computing Z-Transforms and ROCs

### (a) x1[n] = 5(0.7)^n u[n]

Using the pair a^n u[n] <-> 1/(1 - a z^{-1}), |z| > |a|, with a = 0.7:

    X1(z) = 5 / (1 - 0.7 z^{-1}),  ROC: |z| > 0.7

### (b) x2[n] = -(4)^n u[-n-1]

Using the pair -a^n u[-n-1] <-> 1/(1 - a z^{-1}), |z| < |a|, with a = 4:

    X2(z) = 1 / (1 - 4 z^{-1}),  ROC: |z| < 4

### (c) x3[n] = 3 delta[n] - 2 delta[n-1] + delta[n-4]

Using delta[n-k] <-> z^{-k}:

    X3(z) = 3 - 2 z^{-1} + z^{-4},  ROC: |z| > 0 (all z except z=0)

### (d) x4[n] = n(0.5)^n u[n]

Using the pair n a^n u[n] <-> a z^{-1} / (1 - a z^{-1})^2, with a = 0.5:

    X4(z) = 0.5 z^{-1} / (1 - 0.5 z^{-1})^2,  ROC: |z| > 0.5

### (e) x5[n] = 2(0.3)^n u[n] + 4(0.9)^n u[n]

Each term separately:
    2/(1 - 0.3 z^{-1}) + 4/(1 - 0.9 z^{-1})

Combine over common denominator (1 - 0.3 z^{-1})(1 - 0.9 z^{-1}):
    Numerator = 2(1 - 0.9 z^{-1}) + 4(1 - 0.3 z^{-1})
              = 2 - 1.8 z^{-1} + 4 - 1.2 z^{-1}
              = 6 - 3 z^{-1}

    X5(z) = (6 - 3 z^{-1}) / ((1 - 0.3 z^{-1})(1 - 0.9 z^{-1}))
    ROC: |z| > 0.9 (intersection of |z|>0.3 and |z|>0.9)

Poles: z = 0.3, z = 0.9
Zeros: 6 - 3 z^{-1} = 0 -> z^{-1} = 2 -> z = 0.5. Also a zero at z = 0 (from z^{-1} terms).

### (f) x6[n] = (0.6)^n u[n] - 3(2)^n u[-n-1]

First term: 1/(1 - 0.6 z^{-1}), ROC: |z| > 0.6
Second term: -3(2)^n u[-n-1] -> 3/(1 - 2 z^{-1}), ROC: |z| < 2

Note: -(-a^n u[-n-1]) with coefficient 3 and a=2 gives 3/(1 - 2z^{-1}).

    X6(z) = 1/(1 - 0.6 z^{-1}) + 3/(1 - 2 z^{-1})

Combine:
    = [(1 - 2 z^{-1}) + 3(1 - 0.6 z^{-1})] / [(1 - 0.6 z^{-1})(1 - 2 z^{-1})]
    = [4 - 3.8 z^{-1}] / [(1 - 0.6 z^{-1})(1 - 2 z^{-1})]

    ROC: 0.6 < |z| < 2 (intersection of |z|>0.6 and |z|<2)

DTFT exists? The DTFT exists if the ROC includes the unit circle (|z|=1). Since 0.6 < 1 < 2, yes, the unit circle is in the ROC. The DTFT exists.

### (g) x7[n] = (0.8)^n cos(0.25 pi n) u[n]

Using the pair r^n cos(w0 n) u[n] <-> (1 - r cos(w0) z^{-1}) / (1 - 2r cos(w0) z^{-1} + r^2 z^{-2})
with r = 0.8, w0 = 0.25 pi:

cos(0.25 pi) = cos(45 deg) = sqrt(2)/2 = 0.7071
r cos(w0) = 0.8 * 0.7071 = 0.5657
2r cos(w0) = 1.1314
r^2 = 0.64

    X7(z) = (1 - 0.5657 z^{-1}) / (1 - 1.1314 z^{-1} + 0.64 z^{-2})
    ROC: |z| > 0.8

Poles: roots of 1 - 1.1314 z^{-1} + 0.64 z^{-2} = 0
In z-domain: z^2 - 1.1314 z + 0.64 = 0
z = (1.1314 +/- sqrt(1.2801 - 2.56)) / 2
  = (1.1314 +/- sqrt(-1.2799)) / 2
  = (1.1314 +/- j 1.1314) / 2

Actually, poles are at z = r e^{+/- j w0} = 0.8 e^{+/- j 0.25 pi}

Polar form: |z| = 0.8, angle = +/- 45 degrees (0.25 pi radians)
Pole radius: r = 0.8
Oscillation frequency: w0 = 0.25 pi rad/sample

DTFT exists? Since all poles are at |z| = 0.8 < 1, the ROC |z| > 0.8 includes the unit circle. Yes, the DTFT exists.

### (h) Evaluate X(z) at z=1

At z=1, z^{-1} = 1, so X(1) = sum of all x[n] values.

(a) X1(1) = 5/(1-0.7) = 5/0.3 = 16.667
    Verify: sum 5(0.7)^n for n=0 to inf = 5/(1-0.7) = 16.667 ✓

(b) X2(1) = 1/(1-4) = -1/3 = -0.333
    Verify: sum -(4)^n for n=-inf to -1 = -sum (4)^n for n=-inf to -1
    = -sum (1/4)^m for m=1 to inf = -(1/4)/(1-1/4) = -1/3 ✓

(c) X3(1) = 3 - 2 + 1 = 2
    Verify: sum = 3(1) - 2(1) + 1(1) = 2 ✓

(d) X4(1) = 0.5/(1-0.5)^2 = 0.5/0.25 = 2
    Verify: sum n(0.5)^n for n=0 to inf = 0.5/(1-0.5)^2 = 2 ✓

(e) X5(1) = (6-3)/((1-0.3)(1-0.9)) = 3/(0.7*0.1) = 3/0.07 = 42.857
    Verify: sum 2(0.3)^n + 4(0.9)^n = 2/0.7 + 4/0.1 = 2.857 + 40 = 42.857 ✓

(f) X6(1) = (4-3.8)/((1-0.6)(1-2)) = 0.2/(0.4*(-1)) = 0.2/(-0.4) = -0.5
    Verify: sum (0.6)^n u[n] + sum -3(2)^n u[-n-1] at z=1
    = 1/0.4 + 3/(1-2) = 2.5 + (-3) = -0.5 ✓

(g) X7(1) = (1-0.5657)/(1-1.1314+0.64) = 0.4343/0.5086 = 0.854
    Verify: sum (0.8)^n cos(0.25 pi n) for n=0 to inf = 0.854 ✓

---

## Problem 2: Inverse Z-Transform

### (a) Distinct real poles, causal

    X(z) = (1 + 3 z^{-1}) / ((1 - 0.2 z^{-1})(1 - 0.6 z^{-1})),  |z| > 0.6

Partial fractions: X(z) = A/(1 - 0.2 z^{-1}) + B/(1 - 0.6 z^{-1})

Multiply through: 1 + 3 z^{-1} = A(1 - 0.6 z^{-1}) + B(1 - 0.2 z^{-1})

Set z^{-1} = 1/0.2 = 5: 1 + 15 = A(1-3) -> 16 = -2A -> A = -8
Set z^{-1} = 1/0.6 = 5/3: 1 + 5 = B(1-1/3) -> 6 = 2B/3 -> B = 9

    x[n] = -8(0.2)^n u[n] + 9(0.6)^n u[n]

Both terms right-sided because ROC is outside both poles.

### (b) Distinct real poles, two-sided

    X(z) = 4 / ((1 - 0.5 z^{-1})(1 - 3 z^{-1})),  0.5 < |z| < 3

Partial fractions: A/(1 - 0.5 z^{-1}) + B/(1 - 3 z^{-1})

Multiply: 4 = A(1 - 3 z^{-1}) + B(1 - 0.5 z^{-1})

Set z^{-1} = 2 (for pole at 0.5): 4 = A(1-6) -> A = -4/5 = -0.8
Set z^{-1} = 1/3 (for pole at 3): 4 = B(1-1/6) -> 4 = 5B/6 -> B = 24/5 = 4.8

ROC is 0.5 < |z| < 3:
- Pole at z=0.5: ROC is OUTSIDE |0.5| -> right-sided term: (0.5)^n u[n]
- Pole at z=3: ROC is INSIDE |3| -> left-sided term: -(3)^n u[-n-1]

    x[n] = -0.8(0.5)^n u[n] - 4.8(3)^n u[-n-1]

The pole at 0.5 gives a right-sided term because the ROC extends outside it. The pole at 3 gives a left-sided term (with negative sign) because the ROC extends inside it.

### (c) Repeated poles

    X(z) = z^{-1} / (1 - 0.5 z^{-1})^2,  |z| > 0.5

Using the hint: n a^n u[n] <-> a z^{-1} / (1 - a z^{-1})^2 with a = 0.5:

    X(z) = 0.5 z^{-1} / (1 - 0.5 z^{-1})^2 * (1/0.5)
         = 2 * [0.5 z^{-1} / (1 - 0.5 z^{-1})^2]

    x[n] = 2 n (0.5)^n u[n]

### (d) Complex conjugate poles

    X(z) = (1 - 0.9 cos(0.3 pi) z^{-1}) / (1 - 2(0.9) cos(0.3 pi) z^{-1} + 0.81 z^{-2}),  |z| > 0.9

This matches the damped-cosine pair r^n cos(w0 n) u[n] with:
- r = 0.9 (pole radius)
- w0 = 0.3 pi (oscillation frequency)
- r^2 = 0.81 ✓
- Numerator matches (1 - r cos(w0) z^{-1}) ✓

    x[n] = (0.9)^n cos(0.3 pi n) u[n]

Pole locations: z = 0.9 e^{+/- j 0.3 pi} (polar form: magnitude 0.9, angle +/- 54 degrees)

---

## Problem 3: Z-Transform Properties

### (a) Time shifting

Given: (0.8)^n u[n] <-> 1/(1 - 0.8 z^{-1}), |z| > 0.8

y[n] = (0.8)^{n-2} u[n-2] = (0.8)^{-2} * (0.8)^n u[n] shifted by 2... 

Actually, y[n] is x[n-2] where x[n] = (0.8)^n u[n]. By the time-shift property:

    Y(z) = z^{-2} X(z) = z^{-2} / (1 - 0.8 z^{-1})
    ROC: |z| > 0.8 (time shift doesn't change ROC, except possibly z=0)

Zeros at z=0: The factor z^{-2} introduces 2 zeros at z=0. So Y(z) has 2 zeros at z=0, one pole at z=0.8.

### (b) Z-domain scaling

Given: u[n] <-> 1/(1 - z^{-1}), |z| > 1

Want Z{(0.5)^n u[n]}. Using scaling property z0^n x[n] <-> X(z/z0) with z0 = 0.5, x[n] = u[n]:

    F(z) = X(z/0.5) = 1/(1 - (z/0.5)^{-1}) = 1/(1 - 0.5 z^{-1})
    ROC: |z/0.5| > 1 -> |z| > 0.5

Verify: this matches the standard pair a^n u[n] <-> 1/(1 - a z^{-1}) with a = 0.5. ✓

### (c) Convolution property

h1[n] = (0.3)^n u[n], h2[n] = (0.7)^n u[n]

(i) H1(z) = 1/(1 - 0.3 z^{-1}), |z| > 0.3
    H2(z) = 1/(1 - 0.7 z^{-1}), |z| > 0.7

(ii) H(z) = H1(z) * H2(z) = 1 / ((1 - 0.3 z^{-1})(1 - 0.7 z^{-1})), |z| > 0.7

(iii) Partial fractions: A/(1 - 0.3 z^{-1}) + B/(1 - 0.7 z^{-1})

    1 = A(1 - 0.7 z^{-1}) + B(1 - 0.3 z^{-1})

    Set z^{-1} = 1/0.3 = 10/3: 1 = A(1 - 7/3) = A(-4/3) -> A = -3/4 = -0.75
    Set z^{-1} = 1/0.7 = 10/7: 1 = B(1 - 3/7) = B(4/7) -> B = 7/4 = 1.75

    h[n] = -0.75(0.3)^n u[n] + 1.75(0.7)^n u[n]

(iv) Verify h[0] and h[1]:
    h[0] = -0.75(1) + 1.75(1) = 1.0
    Direct: h[0] = sum h1[k] h2[0-k] for k=0 to 0 = h1[0]*h2[0] = 1*1 = 1 ✓

    h[1] = -0.75(0.3) + 1.75(0.7) = -0.225 + 1.225 = 1.0
    Direct: h[1] = h1[0]*h2[1] + h1[1]*h2[0] = 1(0.7) + 0.3(1) = 1.0 ✓

### (d) Initial-value theorem

    X(z) = (3 - z^{-1}) / ((1 - 0.4 z^{-1})(1 + 0.5 z^{-1})),  |z| > 0.5

(i) x[0] = lim_{z->inf} X(z) = (3 - 0) / ((1 - 0)(1 + 0)) = 3/1 = 3

(ii) Partial fractions: A/(1 - 0.4 z^{-1}) + B/(1 + 0.5 z^{-1})

    3 - z^{-1} = A(1 + 0.5 z^{-1}) + B(1 - 0.4 z^{-1})

    Set z^{-1} = 1/0.4 = 2.5: 3 - 2.5 = A(1 + 1.25) -> 0.5 = 2.25A -> A = 2/9
    Set z^{-1} = -1/0.5 = -2: 3 + 2 = B(1 + 0.8) -> 5 = 1.8B -> B = 25/9

    x[n] = (2/9)(0.4)^n u[n] + (25/9)(-0.5)^n u[n]

    Verify x[0] = 2/9 + 25/9 = 27/9 = 3 ✓

(iii) x[1] = (2/9)(0.4) + (25/9)(-0.5) = 0.8/9 - 12.5/9 = -11.7/9 = -1.3
     x[2] = (2/9)(0.16) + (25/9)(0.25) = 0.32/9 + 6.25/9 = 6.57/9 = 0.730

---

## Problem 4: System Analysis with H(z)

### Given: y[n] - 0.9 y[n-1] + 0.18 y[n-2] = x[n]

### (a) System function H(z)

Take the Z-transform (zero ICs, causal):
    Y(z) - 0.9 z^{-1} Y(z) + 0.18 z^{-2} Y(z) = X(z)
    Y(z)(1 - 0.9 z^{-1} + 0.18 z^{-2}) = X(z)

    H(z) = Y(z)/X(z) = 1 / (1 - 0.9 z^{-1} + 0.18 z^{-2})

Factor denominator: 1 - 0.9 z^{-1} + 0.18 z^{-2} = (1 - 0.3 z^{-1})(1 - 0.6 z^{-1})
Check: (1 - 0.3 z^{-1})(1 - 0.6 z^{-1}) = 1 - 0.6 z^{-1} - 0.3 z^{-1} + 0.18 z^{-2} = 1 - 0.9 z^{-1} + 0.18 z^{-2} ✓

    H(z) = 1 / ((1 - 0.3 z^{-1})(1 - 0.6 z^{-1})),  ROC: |z| > 0.6

Poles: z = 0.3 and z = 0.6. No finite zeros (numerator is constant 1).

### (b) BIBO stability

Both poles are at |z| = 0.3 and |z| = 0.6, both strictly inside the unit circle.
For a causal system, BIBO stable requires all poles inside the unit circle.

    The system is BIBO stable. ✓

### (c) Impulse response h[n]

Partial fractions: A/(1 - 0.3 z^{-1}) + B/(1 - 0.6 z^{-1})

    1 = A(1 - 0.6 z^{-1}) + B(1 - 0.3 z^{-1})

    Set z^{-1} = 1/0.3 = 10/3: 1 = A(1 - 2) = -A -> A = -1
    Set z^{-1} = 1/0.6 = 5/3: 1 = B(1 - 0.5) = 0.5B -> B = 2

    h[n] = -(0.3)^n u[n] + 2(0.6)^n u[n]

    Check h[0] = -1 + 2 = 1. From diff eq: y[0] = x[0] = delta[0] = 1 ✓

### (d) Input x[n] = (0.5)^n u[n]

(i) X(z) = 1/(1 - 0.5 z^{-1}), |z| > 0.5

    Y(z) = H(z) X(z) = 1 / ((1 - 0.3 z^{-1})(1 - 0.6 z^{-1})(1 - 0.5 z^{-1}))

(ii) Partial fractions: A/(1-0.3z^{-1}) + B/(1-0.6z^{-1}) + C/(1-0.5z^{-1})

    1 = A(1-0.6z^{-1})(1-0.5z^{-1}) + B(1-0.3z^{-1})(1-0.5z^{-1}) + C(1-0.3z^{-1})(1-0.6z^{-1})

    Set z^{-1}=10/3: 1 = A(1-2)(1-5/3) = A(-1)(-2/3) = 2A/3 -> A = 3/2 = 1.5
    Set z^{-1}=5/3: 1 = B(1-0.5)(1-5/6) = B(0.5)(1/6) = B/12 -> B = 12
    Set z^{-1}=2: 1 = C(1-0.6)(1-1.2) = C(0.4)(-0.2) = -0.08C -> C = -12.5

    y[n] = 1.5(0.3)^n u[n] + 12(0.6)^n u[n] - 12.5(0.5)^n u[n]

(iii) Verify:
    y[0] = 1.5 + 12 - 12.5 = 1.0
    From diff eq: y[0] - 0.9(0) + 0.18(0) = x[0] = 1 -> y[0] = 1 ✓

    y[1] = 1.5(0.3) + 12(0.6) - 12.5(0.5) = 0.45 + 7.2 - 6.25 = 1.4
    From diff eq: y[1] = 0.9 y[0] + x[1] = 0.9(1) + 0.5 = 1.4 ✓

### (e) G(z) = 1/(1 - 1.5 z^{-1}), pole at z = 1.5

Causal (ROC: |z| > 1.5): g[n] = (1.5)^n u[n]. Pole at |z|=1.5 > 1, outside unit circle. The system is NOT BIBO stable (impulse response grows without bound). DTFT does not exist (unit circle not in ROC).

Anti-causal (ROC: |z| < 1.5): g[n] = -(1.5)^n u[-n-1]. The ROC |z| < 1.5 DOES include the unit circle (|z|=1 < 1.5). The system IS BIBO stable with this ROC. DTFT exists.

---

## Problem 5: Unilateral Z-Transform

### (a) First-order with IC

    y[n] - 0.8 y[n-1] = (0.5)^n u[n], y[-1] = 3

(i) Transform using unilateral property y[n-1] <-> z^{-1} Y(z) + y[-1]:

    Y(z) - 0.8(z^{-1} Y(z) + y[-1]) = 1/(1 - 0.5 z^{-1})
    Y(z) - 0.8 z^{-1} Y(z) - 0.8(3) = 1/(1 - 0.5 z^{-1})
    Y(z)(1 - 0.8 z^{-1}) = 1/(1 - 0.5 z^{-1}) + 2.4

(ii) Solve for Y(z):

    Y(z) = 1/((1 - 0.5 z^{-1})(1 - 0.8 z^{-1})) + 2.4/(1 - 0.8 z^{-1})

Combine over common denominator (1 - 0.5 z^{-1})(1 - 0.8 z^{-1}):
    = [1 + 2.4(1 - 0.5 z^{-1})] / [(1 - 0.5 z^{-1})(1 - 0.8 z^{-1})]
    = (3.4 - 1.2 z^{-1}) / [(1 - 0.5 z^{-1})(1 - 0.8 z^{-1})]

(iii) Partial fractions: A/(1-0.5z^{-1}) + B/(1-0.8z^{-1})

    3.4 - 1.2 z^{-1} = A(1 - 0.8 z^{-1}) + B(1 - 0.5 z^{-1})

    Set z^{-1} = 2: 3.4 - 2.4 = A(1-1.6) -> 1.0 = -0.6A -> A = -5/3
    Set z^{-1} = 1.25: 3.4 - 1.5 = B(1-0.625) -> 1.9 = 0.375B -> B = 76/15

    y[n] = (-5/3)(0.5)^n u[n] + (76/15)(0.8)^n u[n]

(iv) Verify:
    y[0] = -5/3 + 76/15 = -25/15 + 76/15 = 51/15 = 3.4
    From diff eq: y[0] = 0.8 y[-1] + x[0] = 0.8(3) + 1 = 3.4 ✓

    y[1] = (-5/3)(0.5) + (76/15)(0.8) = -5/6 + 60.8/15 = -0.833 + 4.053 = 3.22
    From diff eq: y[1] = 0.8 y[0] + x[1] = 0.8(3.4) + 0.5 = 2.72 + 0.5 = 3.22 ✓

### (b) Second-order, zero-input

    y[n] - 0.5 y[n-1] - 0.06 y[n-2] = 0, y[-1] = 5, y[-2] = 0

(i) Transform using unilateral properties:
    y[n-1] <-> z^{-1} Y(z) + y[-1] = z^{-1} Y(z) + 5
    y[n-2] <-> z^{-2} Y(z) + y[-2] + y[-1] z^{-1} = z^{-2} Y(z) + 0 + 5 z^{-1}

    Y(z) - 0.5(z^{-1} Y(z) + 5) - 0.06(z^{-2} Y(z) + 5 z^{-1}) = 0
    Y(z)(1 - 0.5 z^{-1} - 0.06 z^{-2}) = 2.5 + 0.3 z^{-1}

    Y(z) = (2.5 + 0.3 z^{-1}) / (1 - 0.5 z^{-1} - 0.06 z^{-2})

(ii) Factor denominator: 1 - 0.5 z^{-1} - 0.06 z^{-2} = (1 - 0.6 z^{-1})(1 + 0.1 z^{-1})
Check: (1 - 0.6 z^{-1})(1 + 0.1 z^{-1}) = 1 + 0.1 z^{-1} - 0.6 z^{-1} - 0.06 z^{-2} = 1 - 0.5 z^{-1} - 0.06 z^{-2} ✓

Partial fractions: A/(1-0.6z^{-1}) + B/(1+0.1z^{-1})

    2.5 + 0.3 z^{-1} = A(1 + 0.1 z^{-1}) + B(1 - 0.6 z^{-1})

    Set z^{-1} = 1/0.6 = 5/3: 2.5 + 0.5 = A(1 + 1/6) = 7A/6 -> A = 18/7
    Set z^{-1} = -10: 2.5 - 3 = B(1+6) = 7B -> B = -0.5/7 = -1/14

    y[n] = (18/7)(0.6)^n u[n] + (-1/14)(-0.1)^n u[n]

(iii) This is the zero-input response (ZIR) because the input is zero and the response comes entirely from initial conditions.

### (c) ZSR/ZIR decomposition for part (a)

**Y_ZS(z) — zero-state (ICs = 0, input only):**

    Y(z)(1 - 0.8 z^{-1}) = 1/(1 - 0.5 z^{-1})
    Y_ZS(z) = 1/((1 - 0.5 z^{-1})(1 - 0.8 z^{-1}))

PF: A/(1-0.5z^{-1}) + B/(1-0.8z^{-1})
    1 = A(1-0.8z^{-1}) + B(1-0.5z^{-1})
    z^{-1}=2: 1=-0.6A -> A=-5/3
    z^{-1}=1.25: 1=0.375B -> B=8/3

    y_ZS[n] = (-5/3)(0.5)^n u[n] + (8/3)(0.8)^n u[n]

**Y_ZI(z) — zero-input (input = 0, ICs only):**

    Y(z)(1 - 0.8 z^{-1}) = 2.4
    Y_ZI(z) = 2.4/(1 - 0.8 z^{-1})

    y_ZI[n] = 2.4(0.8)^n u[n]

**Verify sum:**
    y_ZS[n] + y_ZI[n] = (-5/3)(0.5)^n u[n] + (8/3)(0.8)^n u[n] + 2.4(0.8)^n u[n]
    = (-5/3)(0.5)^n u[n] + (8/3 + 2.4)(0.8)^n u[n]
    = (-5/3)(0.5)^n u[n] + (8/3 + 12/5)(0.8)^n u[n]
    = (-5/3)(0.5)^n u[n] + (40/15 + 36/15)(0.8)^n u[n]
    = (-5/3)(0.5)^n u[n] + (76/15)(0.8)^n u[n]

This matches the total y[n] from part (a). ✓
