# Chapter 15 Lecture Outline — Mechanical Waves

*Young & Freedman University Physics, 15th ed.*

## Learning Goals

- Use the relationship among speed, frequency, and wavelength for a periodic wave.
- Calculate the speed of waves on a rope or string.
- Understand what happens when mechanical waves overlap and interfere.
- Analyze the properties of standing waves on a string.
- Understand how stringed instruments produce sounds of specific frequencies.

## Introduction

Earthquake waves carry enormous power as they travel through the earth. Other mechanical waves — sound waves, piano strings — carry far less energy. Overlapping waves interfere, which helps explain musical instruments.

## Types of Mechanical Waves

- **Transverse waves**: hand moves string up and down; wave moves to the right — particles move perpendicular to propagation.
- **Longitudinal waves**: piston compresses a fluid — particles move parallel to propagation.
- **Surface waves on a liquid**: combination of longitudinal and transverse (particles move in circles).

"Doing the wave" at a sports stadium illustrates how a disturbance propagates without transport of matter.

## Periodic Waves

Each particle undergoes periodic motion. The **wavelength** $\lambda$ is the length of one complete wave pattern.

$$v = \lambda f$$

- Periodic transverse wave on a string (spring-mass oscillator): crests and troughs of amplitude $A$ traveling at speed $v$.
- Periodic longitudinal wave: compressions and rarefactions from a plunger in SHM. Wavelength = distance between corresponding points on successive cycles.
- Radial waves from drops in water: concentric circular crests and troughs.

## Mathematical Description

Sinusoidal wave propagating in the $+x$-direction (Eq. 15.7):

$$y(x, t) = A\cos(k x - \omega t)$$

- $A$ = amplitude
- $k = 2\pi/\lambda$ = wave number
- $\omega = 2\pi f = 2\pi/T$ = angular frequency

Plotting $y$ vs. $x$ at $t = 0$ shows the string's shape (wavelength $\lambda$ visible). Plotting $y$ vs. $t$ at $x = 0$ shows a particle's motion (period $T$ visible).

### Particle Velocity and Acceleration

For a sinusoidal wave, particles far from crests/troughs move with maximum velocity; at crests/troughs $v_y = 0$ and $|a_y|$ is maximum.

## Speed of a Wave on a String

$$\boxed{v = \sqrt{\frac{F}{\mu}}}$$

- Increases with tension $F$.
- Decreases with linear mass density $\mu$.

Example: Transmission cables with large $\mu$ and low $F$ carry transverse waves slowly.

## Power in a Wave

Instantaneous power in a sinusoidal wave is never negative — energy always flows in the direction of propagation.

$$P_\mathrm{av} = \tfrac{1}{2}\sqrt{\mu F}\,\omega^2 A^2$$

Average power is proportional to the **square** of the amplitude and the **square** of the frequency. This is true for all waves.

## Wave Intensity

If waves spread uniformly in all directions with no absorption:

$$I \propto \frac{1}{r^2}$$

The same power is spread over a larger area at greater distance.

## Reflection at a String End

- **Fixed end**: arriving pulse exerts a force on the wall; the wall's reaction kicks back, producing a reflected pulse that **inverts**.
- **Free end**: the ring on a rod moves freely, overshoots, and the stretched string pulls it back — reflected pulse **does not invert**.

## Superposition

**Principle of superposition**: when two or more waves overlap, the total displacement is the algebraic sum of the individual displacements.

- Inverted pulse + upright pulse moving oppositely can momentarily cancel (destructive interference).
- Two upright pulses moving oppositely constructively add at overlap.

## Standing Waves on a String

When two waves of equal $A$, $f$, $\lambda$ travel in opposite directions, they interfere to form a **standing wave** that does not propagate.

- **Nodes** (N): no motion.
- **Antinodes** (A): maximum amplitude.

### Mathematics (fixed end at $x = 0$)

$$y(x, t) = (A_\mathrm{SW}\sin k x)\sin\omega t$$

with $A_\mathrm{SW} = 2A$.

## Normal Modes

For a taut string of length $L$ fixed at both ends:

$$\lambda_n = \frac{2L}{n}, \quad f_n = n\frac{v}{2L} = n f_1, \quad n = 1, 2, 3, \ldots$$

- $n = 1$: fundamental ($f_1$)
- $n = 2$: second harmonic / first overtone
- $n = 3$: third harmonic / second overtone
- $n = 4$: fourth harmonic / third overtone

Figure: $n\cdot\lambda/2 = L$ with nodes/antinodes along the string.

## Standing Waves and String Instruments

$$f_1 = \frac{1}{2L}\sqrt{\frac{F}{\mu}}$$

This is also the frequency of the sound wave produced in the surrounding air. Increasing tension $F$ increases pitch.

## Selected Examples

- **Ex. 1** — Wavelength of a 784 Hz note (G$_5$) in air ($v = 344~\mathrm{m/s}$): $\lambda = v/f \approx 0.439~\mathrm{m}$. Period: $T = 1/f \approx 1.28~\mathrm{ms}$.
- **Ex. 8** — Wave $y(x,t) = (6.50~\mathrm{mm})\cos 2\pi(x/28\,\mathrm{cm} - t/0.0360\,\mathrm{s})$. Amplitude 6.5 mm; $\lambda = 28~\mathrm{cm}$; $T = 0.036~\mathrm{s}$; $v = \lambda/T$; propagates in $+x$.
- **Ex. 15** — Rope with 1.50 kg mass tensioning it ($F = mg$), $\mu = 0.048~\mathrm{kg/m}$, $f = 120~\mathrm{Hz}$. $v = \sqrt{F/\mu}$, $\lambda = v/f$. If mass doubles to 3.00 kg, $v$ and $\lambda$ scale by $\sqrt{2}$.
- **Ex. 22** — Piano wire 3.00 g, 80.0 cm, $F = 25.0~\mathrm{N}$, $f = 120~\mathrm{Hz}$, $A = 1.6~\mathrm{mm}$: $P_\mathrm{av} = \tfrac{1}{2}\sqrt{\mu F}\omega^2 A^2$. Halving $A$ reduces $P$ by factor of 4.
- **Ex. 35** — Standing wave with $A_\mathrm{SW} = 2.5~\mathrm{mm}$, $\omega = 942~\mathrm{rad/s}$, $k = 0.750\pi~\mathrm{rad/m}$. Nodes at $x$ where $\sin kx = 0$; antinodes where $|\sin kx| = 1$.
- **Prob. 46** — $y(x,t) = 0.75~\mathrm{cm}\cos\pi[(0.400~\mathrm{cm}^{-1})x + (250~\mathrm{s}^{-1})t]$. $+$ sign → wave moves in $-x$.
- **Prob. 69** — Rock on wire: $f_1$ changes from 42 Hz to 28 Hz when submerged. Ratio $(f_\mathrm{sub}/f_\mathrm{air})^2 = F_\mathrm{sub}/F_\mathrm{air}$; solve for buoyant force and liquid density.

*See `chapter_15.md` for the full chapter text derivation.*
