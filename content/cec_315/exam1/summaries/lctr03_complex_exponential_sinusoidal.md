# Lecture 3 — Complex Numbers and Exponential and Sinusoidal Signals

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Jianhua Liu
**Source PDF:** `all_lectures/cec315-lctr03-complex-nums-exp-n-sinusoidal-sigs.pdf`
**Exam coverage:** Exam 1

**Focus:** Section 1.3 (Pages 14 to 26). Yet, we go much more beyond that coverages.

## 3.1 Review of Sinusoidal Functions

### 3.1.1 Definitions of cosine and sine functions on a triangle

The definition of cosine and sine functions can be shown easily using a triangle, such as the upper one in Figure 1:

$$\cos\theta = x/r,$$
$$\sin\theta = y/r.$$

*[Figure 1: Mirror triangles for the definition and illustration of cosine and sine functions. Upper triangle has hypotenuse $r$, horizontal leg $x$, vertical leg $y$, with angle $\theta$ at origin. Lower mirrored triangle has vertical leg $-y$ with angle $-\theta$ at origin.]*

### 3.1.2 Properties of cosine and sine functions

From the bottom triangle of Figure 1 we can see:

$$\cos(-\theta) = \cos\theta,$$
$$\sin(-\theta) = \sin\theta.$$

We can also see the following from Figure 2, where the above $r$ is changed to 1, that

$$\cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta,$$
$$\sin\left(\frac{\pi}{2} - \theta\right) = \cos\theta,$$
$$\cos(\pi + \theta) = -\cos\theta,$$
$$\sin(\pi + \theta) = -\sin\theta.$$

*[Figure 2: Opposite triangles for the illustration of cosine and sine properties. Unit hypotenuse, showing angles $\theta$ and $\pi+\theta$ with annotations $\cos\theta = \sin(\pi/2 - \theta)$, $\sin\theta = \cos(\pi/2 - \theta)$, $\cos(\pi+\theta) = -\cos\theta$, $\sin(\pi+\theta) = -\sin\theta$.]*

Using the above properties, we have the following properties:

$$\cos\left(\theta - \frac{\pi}{2}\right) = \cos\left(\frac{\pi}{2} - \theta\right) = \sin\theta,$$
$$\sin\left(\theta - \frac{\pi}{2}\right) = -\sin\left(\frac{\pi}{2} - \theta\right) = -\cos\theta,$$
$$\cos\left(\frac{\pi}{2} + \theta\right) = \cos\left(\frac{\pi}{2} - (-\theta)\right) = \sin(-\theta) = -\sin\theta,$$
$$\sin\left(\frac{\pi}{2} + \theta\right) = \sin\left(\frac{\pi}{2} - (-\theta)\right) = \cos(-\theta) = \cos\theta,$$
$$\cos(\pi - \theta) = \cos(\pi + (-\theta)) = -\cos(-\theta) = -\cos\theta,$$
$$\sin(\pi - \theta) = \sin(\pi + (-\theta)) = -\sin(-\theta) = \sin\theta.$$

Additionally, we have, for integer $k$:

$$\cos(\theta + 2k\pi) = \cos\theta,$$
$$\sin(\theta + 2k\pi) = \sin\theta.$$

To see the relationship between the rotation on a circle and a sine function, see https://www.mathsisfun.com/algebra/trig-sin-cos-tan-graphs.html.

## 3.2 A Review of Complex Numbers and Operations

### 3.2.1 Definition of complex numbers

A **complex numbers** extends a real number by including an imaginary part, which is signified by the imaginary unit, often expressed as $i$ or $j$. Here we use $j$, which is defined as $j^2 = -1$ or $j = \sqrt{-1}$.

While a real number is often expressed in a 1D axis, a complex number is often expressed on a 2D complex plane, on which it can be expressed in two different forms: the rectangular (Cartesian) form and the polar form.

### 3.2.2 Rectangular (Cartesian) form

$$c = a + jb,$$

where $a \in \mathcal{R}$ and $b \in \mathcal{R}$ are the real and imaginary parts, respectively.

### 3.2.3 Polar form

$$c = r \angle \theta,$$

where $r \geq 0$ is the **magnitude** (absolute value or modulus) and $\theta \in \mathcal{R}$ is the **angle**.

### 3.2.4 Conversion between the rectangular and polar forms

For a given complex number, its two expression forms should be the same. So, we can perform conversion between these two forms.

According to the above definition of sinusoidal functions, we should have

$$c = r\angle\theta = r\cos(\theta) + jr\sin(\theta) = a + jb,$$

which leads to the following conversion from the polar form to rectangular:

$$a = r\cos\theta \qquad b = r\sin\theta,$$

as well as the following conversion from the rectangular form to polar:

$$r = \sqrt{a^2 + b^2}, \qquad \theta = \begin{cases} \tan^{-1}(b/a), & a \geq 0, \\ \pi + \tan^{-1}(b/a), & a < 0. \end{cases}$$

Note that $\tan^{-1}(b/a)$ is the result in radians, which is obtained by using the calculator directly.

### 3.2.5 Euler's Formula

For a given angle $\phi$, we have

$$e^{j\phi} = \cos\phi + j\sin\phi,$$

where $e \approx 2.71828$ is the base for the natural logarithm. This can be proved using Tyler series expansion of the exponential, cosine, and sine functions.

Euler's formula is often illustrated using a unit circle, as shown in Figure 3.

*[Figure 3: Unit circle for expressing the complex sinusoids in terms of cosine and sine functions. Complex plane with Re and Im axes, unit circle, vector at angle $\varphi$ showing $e^{j\varphi} = \cos\varphi + i\sin\varphi$, with horizontal component $\cos\varphi$ and vertical component $\sin\varphi$.]*

#### 3.2.5.1 A second form of polar expression based on Euler's formula

We can see from the Euler's formula and the conversation between polar and rectangular form that we can use the complex exponential function as the second polar form, which means

$$re^{j\theta} = r\angle\theta = r\cos(\theta) + jr\sin(\theta).$$

Note that there are some differences between the two forms of polar expression:

- If we use the first format, the angle can be in any unit: degrees or radians.
- If we use the second format, the angle can only be in the unit radians.

### 3.2.6 Conjugate of a complex number

The conjugate of the above $e^{j\phi}$ is

$$(e^{j\phi})^* = e^{-j\phi} = \cos(-\phi) + j\sin(-\phi) = \cos\phi - j\sin\phi.$$

To see the relationship between the rotation on a circle and a sine function, see https://www.mathsisfun.com/algebra/trig-sin-cos-tan-graphs.html.

### 3.2.7 Basic calculations

Assume we have two complex numbers $c_1 = a_1 + jb_1 = r_1 e^{j\theta_1}$ and $c_2 = a_2 + jb_2 = r_2 e^{j\theta_2}$.

Then, we have the following two calculations which are preformed using the rectangular form:

Addition:

$$c_1 + c_2 = (a_1 + a_2) + j(b_1 + b_2)$$

Subtraction:

$$c_1 - c_2 = (a_1 + a_2) - j(b_1 + b_2)$$

We also have the following two calculations which are preformed using the polar form.

Multiplication:

$$c_1 \times c_2 = r_1 r_2 e^{j(\theta_1 + \theta_2)}$$

Division:

$$\frac{c_1}{c_2} = \frac{r_1}{r_2} e^{j(\theta_1 - \theta_2)}$$

Note that the above multiplication and division can also be done via the following way:

$$c_1 \times c_2 = (a_1 + jb_1) \times (a_2 + jb_2)$$
$$= (a_1 a_2 - b_1 b_2) + j(a_1 b_2 + a_2 b_1),$$

$$\frac{c_1}{c_2} = \frac{a_1 + jb_1}{a_2 + jb_2}$$
$$= \frac{(a_1 + jb_1)(a_2 - jb_2)}{(a_2 + jb_2)(a_2 - jb_2)}$$
$$= \frac{(a_1 a_2 + b_1 b_2) - j(a_1 b_2 - a_2 b_1)}{a_2^2 + b_2^2}.$$

### 3.2.8 A few special complex numbers

- $1 = e^{j0}$
- $j = e^{j\pi/2}$
- $-1 = e^{j\pi}$
- $1/j = -j = e^{j3\pi/2} = e^{-j\pi/2}$

## 3.3 Continuous-Time Complex and Real Sinusoidal Signals

Now, let's lets extend the above exponential-based polar form complex numbers and sinusoidal functions to CT signals.

### 3.3.1 Single-frequency complex sinusoid

A single frequency complex sinusoid, a function of time $t$, has the following general form:

$$x_C(t) = A e^{j(2\pi F t + \theta)},$$

whit the following parameters:

- $A$, the amplitude of the signal, the radius of the circle if we draw $x_C(t)$ on a complex plane.
- $F$, the (ordinary) frequency in Hz. Often, we can use $\Omega = 2\pi F$, the **angular** frequency, to simplify the notation.
- $\theta$, the initial phase, the phase of the function when $t$ is 0.

The above parameters are usually classified into two groups:

- $X_C = A e^{j\theta}$, the complex amplitude, specifies the amplitude and initial phase.
- $F$, the frequency, determines how fast the complex sinusoidal signal changes.

### 3.3.2 Single frequency real sinusoid

If we only take the real part of the above complex sinusoid, we will have the following single-frequency real sinusoidal function:

$$x(t) = A\cos(2\pi F t + \theta).$$

See the top part of Figure 4 for an illustration of the waveform of a sinusoidal function. The bottom part shows its spectrum, which is defined below.

*[Figure 4: Waveform and spectrum of a sinusoid. Top plot: $x_{A1}(t)$ versus $t$ (ms) showing a sinusoid of amplitude ~0.5 over 0–45 ms. Bottom plot: $X_{A1}(F)$ versus $F$ (Hz) showing two stems at symmetric frequencies with value $0.000 + -0.250j$.]*

### 3.3.3 Expressing a real sinusoid using complex sinusoids

The real sinusoidal signal $x(t)$ can be expressed using $x_C(t)$ as shown below:

$$x(t) = \Re x_C(t),$$
$$= \frac{x_C(t) + x_C^*(t)}{2},$$
$$= \frac{A}{2} e^{j\theta} e^{j2\pi F t} + \frac{A}{2} e^{-j\theta} e^{-j2\pi F t}.$$

### 3.3.4 Spectrum of a real sinusoid

Given the values of $A$, $\theta$, and $F$, the entire waveform of $x(t)$ can be completely determined. To express these three parameters in an effective way, especially when we consider the summation of sinusoids with multiple different frequencies, we can express them in a single graph, as shown in the bottom part of Figure 4.

### 3.3.5 Why using complex sinusoids?

It seems that we are making the matters more complicated by using complex sinusoids to express a simple real sinusoid. The reason, which will be illustrated in the class, is that in linear systems and analysis, we need *linear combinations* of multiple real sinusoids with the same frequency but different amplitudes and phases. The result of the linear combination is a sinusoid with the same frequency but unknow amplitude and phase. When expressing each real sinusoid using its complex counterpart, the calculation of the amplitude and phase is very straight using complex numbers.

### 3.3.6 Superposition of harmonic signals

We can generate a signal as the summation of harmonics, as shown in the top of Figure 5.

*[Figure 5: Waveform and spectrum of the summation of harmonics. Top plot: $x(t)$ versus $t$ (ms) showing a periodic non-sinusoidal waveform. Bottom plot: $X(F)$ versus $F$ (Hz) showing multiple stems at harmonic frequencies with annotations $0.000 + -0.250j$, $0.175 + 0.000j$, $0.071 + 0.071j$.]*

### 3.3.7 Spectrum of superposition of harmonic signals

The spectrum of superposition of harmonic signals really shows the advantage of spectrum—it include all the information we need to determine the time-domain signals.

## 3.4 Continuous-Time Complex Exponentials in Book's Notations

Now, we come back to use the notations of the book.

### 3.4.1 Complex Exponential in the General Form

We have discussed the

$$x(t) = C e^{jat}.$$

Here:

- $C$ is a complex constant, about the magnitude.
- $a$ is a complex constant, about the attenuation and frequency of the signal.
- $t$ is the time.

### 3.4.2 Real Exponentials

If $C$ and $a$ are real, the signal is a growing (if $a > 0$) or decaying (if $a < 0$) exponential.

See Figure 1.19 of the book

### 3.4.3 Periodic Complex Exponentials

If $a$ is purely imaginary ($j\omega_0$), then signal $e^{j\omega_0 t}$ is periodic with fundamental period $T_0 = 2\pi/|\omega_0|$. This is the form we discussed before.

## 3.5 Sinusoidal Signals and Euler's Relation

### 3.5.1 CT Sinusoids

Using book's notation, CT sinusoids take the form

$$x(t) = A\cos(\omega_0 t + \phi).$$

See Figure 1.20.

### 3.5.2 Energy and Power of Sinusoids

They are examples of signals with infinite total energy but finite average power.

## 3.6 Discrete-Time Complex Exponentials

### 3.6.1 Generic Expression

$$x[n] = C\alpha^n \text{ or } C e^{\beta n}.$$

### 3.6.2 Real Exponentials

Magnitude grows if $|\alpha| > 1$ and decays if $|\alpha| < 1$.

### 3.6.3 Sinusoidal Sequences

$$x[n] = A\cos(\omega_0 n + \phi).$$

## 3.7 The Periodicity Problem in Discrete Time

- Unlike CT signals, the DT signal $e^{j\omega_0 n}$ is **not** necessarily distinct for every value of $\omega_0$.
- Frequencies separated by multiples of $2\pi$ are identical: $e^{j(\omega_0 + 2\pi)n} = e^{j\omega_0 n}$.
- Low frequencies are located near $\omega = 0, 2\pi, ...$; high frequencies are near $\omega = \pm\pi, \pm 3\pi, ...$.

If you are curious now, read the book. If you can wait, this will be discussed in CEC 410.

## 3.8 Exercise

Derive the equations, based on Euler's formula, for

$$\cos(\alpha + \beta) =$$
$$\cos(\alpha - \beta) =$$
$$\sin(\alpha + \beta) =$$
$$\sin(\alpha - \beta) =$$

and

$$\cos(\alpha)\cos(\beta) =$$
$$\cos(\alpha)\sin(\beta) =$$
$$\sin(\alpha)\sin(\beta) =$$

## Practice Problems Summary

- **Exercise 3.8:** Derive, using Euler's formula, the angle-sum/difference identities for $\cos(\alpha \pm \beta)$ and $\sin(\alpha \pm \beta)$, and the product-to-sum identities for $\cos\alpha\cos\beta$, $\cos\alpha\sin\beta$, and $\sin\alpha\sin\beta$.
