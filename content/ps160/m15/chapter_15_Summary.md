# Chapter 15 Summary — Mechanical Waves

## Waves and Their Properties

A **wave** is any disturbance that propagates from one region to another. A **mechanical wave** travels within some material medium. The wave speed $v$ depends on the type of wave and properties of the medium.

In a **periodic wave**, the motion of each point is periodic with frequency $f$ and period $T$. The **wavelength** $\lambda$ is the distance over which the wave pattern repeats, and the **amplitude** $A$ is the maximum displacement of a particle in the medium.

$$v = \lambda f \quad (15.1)$$

A **sinusoidal wave** is a special periodic wave in which each point moves in SHM.

## Wave Functions and Wave Dynamics

The wave function $y(x, t)$ describes the displacements of individual particles. For a sinusoidal wave traveling in the $+x$-direction:

$$y(x, t) = A \cos\!\left[\omega\!\left(\frac{x}{v} - t\right)\right] \quad (15.3)$$

$$y(x, t) = A \cos\!\left[2\pi\!\left(\frac{x}{\lambda} - \frac{t}{T}\right)\right] \quad (15.4)$$

$$y(x, t) = A \cos(k x - \omega t) \quad (15.7)$$

where $k = 2\pi/\lambda$ (wave number) and $\omega = 2\pi f = v k$.

For waves moving in the $-x$-direction, replace the minus signs with plus signs.

### The Wave Equation

$$\frac{\partial^2 y(x,t)}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2 y(x,t)}{\partial t^2} \quad (15.12)$$

### Speed of Transverse Waves on a String

Depends on tension $F$ and mass per unit length $\mu$:

$$v = \sqrt{\frac{F}{\mu}} \quad (15.14)$$

## Wave Power

For a sinusoidal mechanical wave, the average power is proportional to the square of the amplitude and the square of the frequency:

$$P_\mathrm{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2 \quad (15.25)$$

### Inverse-Square Law for Intensity

For waves spreading out in three dimensions:

$$\frac{I_1}{I_2} = \frac{r_2^2}{r_1^2} \quad (15.26)$$

## Wave Superposition

A wave reflects when it reaches a boundary. At any point where two or more waves overlap, the total displacement is the sum of the individual displacements (**principle of superposition**):

$$y(x, t) = y_1(x, t) + y_2(x, t) \quad (15.27)$$

## Standing Waves on a String

When a sinusoidal wave reflects from a fixed or free end, the incident and reflected waves combine into a standing wave with **nodes** (no motion) and **antinodes** (maximum motion). Adjacent nodes are spaced $\lambda/2$ apart, as are adjacent antinodes.

### Standing wave, fixed end at $x = 0$

$$y(x, t) = (A_\mathrm{SW} \sin k x)\sin \omega t \quad (15.28)$$

### Normal Modes (string fixed at both ends, length $L$)

Standing waves occur only when $L$ is an integer multiple of $\lambda/2$.

$$f_n = n\frac{v}{2L} = n f_1 \quad (n = 1, 2, 3, \ldots) \quad (15.33)$$

$$f_1 = \frac{1}{2L}\sqrt{\frac{F}{\mu}} \quad (15.35)$$

Each frequency, with its associated vibration pattern, is called a **normal mode** (harmonic).

> Figure: standing-wave patterns $n = 1, 2, 3, 4$ showing nodes (N) and antinodes (A) with $nL\cdot\lambda/2 = L$ relationships.
