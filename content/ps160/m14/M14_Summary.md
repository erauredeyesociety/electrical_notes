# Chapter 14 Summary — Periodic Motion (Oscillations)

## Resonance and Its Consequences

The peaking of amplitude at driving frequencies close to the natural frequency is called **resonance**. Examples:
- Building up the amplitude of a child on a swing by pushing in time with the swing's natural frequency.
- A vibrating rattle in a car at a specific engine speed.
- Loudspeaker resonances producing an audible buzz when a musical note coincides with a speaker cone/housing resonance.
- Tuned circuits in radio receivers (Chapter 31).

Resonance can be destructive — e.g., soldiers breaking step on bridges, or an airplane wing whose natural frequency matched engine vibration.

## Periodic Motion

Periodic motion repeats in a definite cycle, occurring whenever there's a stable equilibrium and a restoring force.

$$f = \frac{1}{T}, \quad T = \frac{1}{f} \quad (14.1)$$

$$\omega = 2\pi f = \frac{2\pi}{T} \quad (14.2)$$

- $T$ = period (one cycle)
- $f$ = frequency (cycles per unit time)
- $\omega$ = angular frequency

## Simple Harmonic Motion (SHM)

If the restoring force is directly proportional to displacement:

$$F_x = -kx \quad (14.3)$$

$$a_x = \frac{F_x}{m} = -\frac{k}{m}x \quad (14.4)$$

$$\omega = \sqrt{\frac{k}{m}} \quad (14.10)$$

$$f = \frac{\omega}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{k}{m}} \quad (14.11)$$

$$T = \frac{1}{f} = 2\pi\sqrt{\frac{m}{k}} \quad (14.12)$$

$$x = A\cos(\omega t + \phi) \quad (14.13)$$

- Angular frequency, frequency, and period in SHM depend only on mass $m$ and force constant $k$, **not on amplitude**.
- $A$ = amplitude, $\phi$ = phase angle (set by initial conditions).

## Energy in SHM

Energy is conserved in SHM. Total energy:

$$E = \tfrac{1}{2}m v_x^2 + \tfrac{1}{2}kx^2 = \tfrac{1}{2}kA^2 = \text{constant} \quad (14.21)$$

## Angular Simple Harmonic Motion

With moment of inertia $I$ and torsion constant $\kappa$:

$$\omega = \sqrt{\frac{\kappa}{I}}, \quad f = \frac{1}{2\pi}\sqrt{\frac{\kappa}{I}} \quad (14.24)$$

> Figure: balance wheel with spring torque $\tau$ opposing angular displacement $\theta$.

## Simple Pendulum

A point mass $m$ at the end of a massless string of length $L$. For small amplitude:

$$\omega = \sqrt{\frac{g}{L}} \quad (14.32)$$

$$f = \frac{\omega}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{g}{L}} \quad (14.33)$$

$$T = \frac{2\pi}{\omega} = \frac{1}{f} = 2\pi\sqrt{\frac{L}{g}} \quad (14.34)$$

Period depends on $g$ and $L$ only — not on mass or amplitude (for small oscillations).

## Physical Pendulum

Any object suspended from an axis, with mass $m$, distance $d$ from axis to center of gravity, moment of inertia $I$ about the axis:

$$\omega = \sqrt{\frac{m g d}{I}} \quad (14.38)$$

$$T = 2\pi\sqrt{\frac{I}{m g d}} \quad (14.39)$$

## Damped Oscillations

When a damping force $F_x = -b v_x$ is added:

$$x = A e^{-(b/2m)t}\cos(\omega' t + \phi) \quad (14.42)$$

$$\omega' = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}} \quad (14.43)$$

Three regimes:
- **Underdamping**: $b < 2\sqrt{km}$ — oscillates with decaying amplitude.
- **Critical damping**: $b = 2\sqrt{km}$ — returns to equilibrium without oscillating, fastest.
- **Overdamping**: $b > 2\sqrt{km}$ — returns slowly without oscillating.

## Forced Oscillations and Resonance

A sinusoidal driving force applied to a damped oscillator produces a **forced (driven) oscillation**. Amplitude is a function of driving frequency $\omega_d$:

$$A = \frac{F_\max}{\sqrt{(k - m\omega_d^2)^2 + b^2 \omega_d^2}} \quad (14.46)$$

Amplitude peaks when $\omega_d$ is close to the natural frequency — **resonance**. Less damping → sharper, higher resonance peak.

> Figure: resonance curves for $b = 0.2, 0.4, 0.7, 1.0, 2.0 \sqrt{km}$, showing sharper peaks for smaller $b$.
