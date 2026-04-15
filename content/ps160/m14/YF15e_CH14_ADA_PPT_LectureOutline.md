# Chapter 14 Lecture Outline — Periodic Motion

*Young & Freedman University Physics, 15th ed.*

## Learning Outcomes

- Describe oscillations in terms of amplitude, period, frequency, and angular frequency.
- Apply **simple harmonic motion** to different physical situations.
- Analyze pendulum motions.
- Understand what determines how rapidly an oscillation dies out.
- Understand how a driving force near the natural frequency produces a large response — **resonance**.

## Introduction

Periodic motion (oscillation) occurs in pendulums, musical vibrations, car engine pistons, and many other systems.

## What Causes Periodic Motion?

A displaced object attached to a spring experiences a **restoring force** that tends to return it to equilibrium. This restoring force causes **oscillation** or **periodic motion**.

- $x > 0$: glider displaced right; spring pulls it toward equilibrium ($F_x < 0$, $a_x < 0$).
- $x = 0$: relaxed spring exerts no force; zero acceleration.
- $x < 0$: glider displaced left; compressed spring pushes it back ($F_x > 0$, $a_x > 0$).

## Characteristics of Periodic Motion

- **Amplitude** $A$: maximum displacement magnitude from equilibrium.
- **Period** $T$: time for one cycle.
- **Frequency** $f$: cycles per unit time.
- **Angular frequency**: $\omega = 2\pi f$.
- $f = 1/T$ and $T = 1/f$.

## Simple Harmonic Motion (SHM)

When the restoring force is **directly proportional** to displacement (Hooke's law $F_x = -kx$), the resulting motion is **simple harmonic motion**.

For small amplitudes, many real systems obey $F_x \approx -kx$ and are approximately simple harmonic.

### SHM Viewed as a Projection

While a ball moves in uniform circular motion on a turntable (the **reference circle**), its shadow projected on a screen moves in SHM. The rotating radius vector is called a **phasor**. If the radius is $A$ and it rotates at $\omega$:

$$x = A\cos\theta = A\cos(\omega t + \phi)$$

### Characteristics of SHM (Spring-mass system)

$$\omega = \sqrt{\frac{k}{m}}$$

$$f = \frac{\omega}{2\pi} = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

$$T = \frac{1}{f} = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}$$

> Tuning-fork intuition: greater tine mass → lower frequency (lower pitch).

### Displacement as a Function of Time

$$x(t) = A\cos(\omega t + \phi)$$

- Varies between $-A$ and $+A$; period $T$.
- Increasing $m$ (same $k$, $A$) → longer period.
- Increasing $k$ (same $m$, $A$) → shorter period.
- Changing $A$ (same $m$, $k$) → **no change** in period.
- Increasing $\phi$ → shifts the $x$-$t$ curve left.

### Velocity and Acceleration

$$v_x(t) = -\omega A \sin(\omega t + \phi), \quad v_\max = \omega A$$

$$a_x(t) = -\omega^2 A \cos(\omega t + \phi), \quad a_\max = \omega^2 A$$

- $v_x$-$t$ graph shifted by $\tfrac{1}{4}$ cycle from $x$-$t$.
- $a_x$-$t$ graph shifted by $\tfrac{1}{4}$ cycle from $v_x$-$t$ (and $\tfrac{1}{2}$ cycle from $x$-$t$).

## Energy in SHM

Total mechanical energy is conserved:

$$E = \tfrac{1}{2}m v_x^2 + \tfrac{1}{2}k x^2 = \tfrac{1}{2}k A^2 = \text{constant}$$

- At $x = \pm A$: $v_x = 0$, all energy is potential ($U = \tfrac{1}{2}kA^2$).
- At $x = 0$: $|v_x| = v_\max$, all energy is kinetic.
- At $x = \pm\tfrac{1}{2}A$: $v_x = \pm\sqrt{3/4}\,v_\max$; energy is $\tfrac{1}{4}$ potential, $\tfrac{3}{4}$ kinetic.

> Figure: $U(x) = \tfrac{1}{2}kx^2$ parabola with total energy line $E$; turning points at $\pm A$.

## Vertical SHM

An object hanging from a spring oscillates in SHM about its equilibrium position. When the weight $mg$ stretches the spring by $\Delta l$:

$$k = \frac{mg}{\Delta l}$$

The net force still obeys $F = -kx$ about the new equilibrium, so the motion is SHM with $\omega = \sqrt{k/m}$.

## Angular SHM

A coil spring exerts a restoring torque:

$$\tau_z = -\kappa\theta$$

where $\kappa$ is the **torsion constant**. The result is angular SHM with:

$$\omega = \sqrt{\frac{\kappa}{I}}, \quad f = \frac{1}{2\pi}\sqrt{\frac{\kappa}{I}}$$

> Figure: balance wheel with coil spring (e.g., mechanical watch).

## Vibrations of Molecules

For two atoms at separation $r$ with equilibrium at $r = R_0$, the Lennard-Jones-like potential can be approximated near equilibrium by a parabola. The restoring force for small displacement $x = r - R_0$ is:

$$F_r \approx -\left(\frac{72 U_0}{R_0^2}\right)x$$

so $k = 72 U_0/R_0^2$ and the motion is SHM.

## The Simple Pendulum

A point mass $m$ (bob) suspended by a massless, unstretchable string of length $L$. The restoring force is $-mg\sin\theta$; for small $\theta$, $\sin\theta \approx \theta$, so the motion is approximately SHM:

$$\omega = \sqrt{\frac{g}{L}}$$

$$f = \frac{1}{2\pi}\sqrt{\frac{g}{L}}$$

$$T = 2\pi\sqrt{\frac{L}{g}}$$

Period depends on $L$ and $g$ only — not on mass or amplitude (small angles).

## The Physical Pendulum

Any extended object suspended from a pivot. For small amplitudes, the motion is SHM with:

$$\omega = \sqrt{\frac{m g d}{I}}, \quad T = 2\pi\sqrt{\frac{I}{m g d}}$$

where $I$ is the moment of inertia about the pivot and $d$ is the distance from pivot to center of gravity.

> Tyrannosaurus rex's leg can be modeled as a physical pendulum to estimate stride length from leg length.

## Damped Oscillations

Real systems have dissipative forces that decrease amplitude — **damping**. With damping force $F_x = -b v_x$:

$$x(t) = A e^{-(b/2m)t}\cos(\omega' t + \phi)$$

$$\omega' = \sqrt{\frac{k}{m} - \frac{b^2}{4m^2}}$$

- **Underdamped** ($b < 2\sqrt{km}$): decaying oscillation.
- **Critically damped** ($b = 2\sqrt{km}$): returns to equilibrium without oscillating, fastest.
- **Overdamped** ($b > 2\sqrt{km}$): returns slowly, no oscillation.

With stronger damping (larger $b$), amplitude decays faster and period $T$ increases compared to $T_0$ (the undamped period).

## Forced Oscillations and Resonance

A damped oscillator left alone eventually stops. Applying a periodic **driving force** of angular frequency $\omega_d$ produces a **forced (driven) oscillation**. The steady-state amplitude is:

$$A = \frac{F_\max}{\sqrt{(k - m\omega_d^2)^2 + b^2 \omega_d^2}}$$

$A$ peaks when $\omega_d \approx \sqrt{k/m}$ — this is **resonance**. Lower damping → taller, sharper peak.

A lady beetle flies via forced oscillation: muscles rhythmically deform its exoskeleton, driving the wings at the same frequency as the muscle contractions.

## Selected Example Problems

**Ex. 3** — A tuning fork tip completes 440 vibrations in 0.500 s. Find $\omega$ and $T$.
$f = 440/0.5 = 880~\mathrm{Hz}$; $T = 1/f \approx 1.14~\mathrm{ms}$; $\omega = 2\pi f \approx 5529~\mathrm{rad/s}$.

**Ex. 9** — An unknown mass on a spring with $k = 120~\mathrm{N/m}$ vibrates at $f = 6.00~\mathrm{Hz}$. Find (a) $T$, (b) $\omega$, (c) mass.
(a) $T = 1/6 \approx 0.167~\mathrm{s}$. (b) $\omega = 2\pi f \approx 37.7~\mathrm{rad/s}$. (c) $m = k/\omega^2 \approx 0.0845~\mathrm{kg}$.

**Ex. 11** — SHM, $T = 0.900~\mathrm{s}$, $A = 0.320~\mathrm{m}$, at $t=0$: $x = 0.320~\mathrm{m}$, at rest (so $\phi = 0$). Times for:
(a) $x = 0.320 \to 0.160$: set $0.160 = 0.320\cos(\omega t)$, $\omega t = \pi/3$, $t = T/6 = 0.150~\mathrm{s}$.
(b) $x = 0.160 \to 0$: $\omega t = \pi/2$, $t = T/4 - T/6 = T/12 = 0.075~\mathrm{s}$.

**Ex. 28** — Oscillator with $\omega$, $A$. Find:
(a) $|x|$ and $|v|$ when $U = K$. $U = K = \tfrac{1}{2}E = \tfrac{1}{4}kA^2$; $\tfrac{1}{2}kx^2 = \tfrac{1}{4}kA^2 \Rightarrow |x| = A/\sqrt{2}$; $|v| = \omega A/\sqrt{2}$.
(b) Occurs 4 times per cycle; time between = $T/4$.
(c) At $|x| = A/2$: $U/E = (A/2)^2/A^2 = 1/4$, so $K = 3E/4$. Kinetic fraction = 3/4, potential = 1/4.
