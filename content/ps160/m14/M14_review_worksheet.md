# M14 Review Worksheet — Oscillations Problems

## Problem 1 — Frequency of SHM
Block-spring system: $k = 1178~\mathrm{N/m}$, $m = 2.7~\mathrm{kg}$. Frequency:

$$f = \frac{1}{2\pi}\sqrt{k/m}$$

## Problem 2 — Period of SHM
$k = 2199~\mathrm{N/m}$, $m = 7.3~\mathrm{kg}$. Period:

$$T = 2\pi\sqrt{m/k}$$

## Problem 3 — Tunnel Through a Planet
Equation of motion:

$$\frac{d^2 r}{dt^2} + \left(\frac{4\pi G\rho}{3}\right)r = 0$$

With $G = 6.67\times10^{-11}$, $\rho = 3743~\mathrm{kg/m^3}$, $R = 208~\mathrm{km}$. This is SHM with $\omega^2 = 4\pi G\rho/3$. Period for the astronaut to fall through and return:

$$T = 2\pi/\omega$$

Convert to hours.

## Problem 4 — SHM from ODE
$m\ddot{z} + k z = 0$, $m = 18.5~\mathrm{kg}$, $k = 66~\mathrm{N/m}$. $T = 2\pi\sqrt{m/k}$.

## Problem 5 — Parse SHM Equation
$x(t) = 5.50\cos(3.00t - 1.40)$. Identify:
- Amplitude $A = 5.50~\mathrm{m}$
- Angular frequency $\omega = 3.00~\mathrm{rad/s}$
- Phase shift $\phi = -1.40~\mathrm{rad}$
- Frequency $f = \omega/(2\pi) \approx 0.477~\mathrm{Hz}$
- Period $T = 2\pi/\omega \approx 2.09~\mathrm{s}$

## Problem 6 — Complete SHM Analysis
$x(t) = 0.7\cos(8 t + 1.9)$ (MKS). Find:
- (a) $A = 0.7~\mathrm{m}$
- (b) $\omega = 8~\mathrm{rad/s}$
- (c) $\phi = 1.9~\mathrm{rad}$
- (d) $f = \omega/(2\pi)$
- (e) $T = 2\pi/\omega$
- (f) $v_\max = \omega A$
- (g) $a_\max = \omega^2 A$
- (h) $x(0) = A\cos(\phi)$
- (i) $v(0) = -\omega A\sin(\phi)$
- (j) $a(0) = -\omega^2 A\cos(\phi)$
- (k) First $t > 0$ where $x = 0$: $8t + 1.9 = \pi/2 \Rightarrow t = (\pi/2 - 1.9)/8$ (if positive, else add $\pi/8$).
- (l) First $t > 0$ where $v = 0$: $8t + 1.9 = \pi \Rightarrow t = (\pi - 1.9)/8$.

## Problem 7 — Phase Shift from Initial Conditions
$k = 456~\mathrm{N/m}$, $m = 5~\mathrm{kg}$, $x_0 = +0.5~\mathrm{m}$, $v_0 = -2.4~\mathrm{m/s}$. Cosine solution $x(t) = A\cos(\omega t + \phi)$.

$\omega = \sqrt{k/m}$. Amplitude $A = \sqrt{x_0^2 + (v_0/\omega)^2}$. Phase from $\tan\phi = -v_0/(\omega x_0)$ (positive angle).

## Problem 8 — Mass from Max Acceleration
$k = 114~\mathrm{N/m}$, released from rest at $x = 0.27~\mathrm{m}$, so $A = 0.27~\mathrm{m}$. $a_\max = \omega^2 A = (k/m)A$.

$$m = \frac{kA}{a_\max} = \frac{(114)(0.27)}{3.4}$$

## Problem 9 — Max Acceleration
$m = 8~\mathrm{kg}$, $k = 186~\mathrm{N/m}$, $A = 0.34~\mathrm{m}$.

$$a_\max = \frac{k}{m}A = \frac{186}{8}(0.34)$$

## Problem 10 — Amplitude from Instantaneous $v$ and $x$
$m = 7~\mathrm{kg}$, $k = 132~\mathrm{N/m}$, at one instant $v = 1.92~\mathrm{m/s}$, $x = 0.27~\mathrm{m}$. Energy conservation:

$$\tfrac{1}{2}kA^2 = \tfrac{1}{2}kx^2 + \tfrac{1}{2}mv^2 \Rightarrow A = \sqrt{x^2 + mv^2/k}$$

## Problem 11 — Coffee Cup on Spring
$m = 0.48~\mathrm{kg}$, spring stretched $\Delta l = 0.03~\mathrm{m}$ at equilibrium so $k = mg/\Delta l$. Pulled down $A = 0.06~\mathrm{m}$ and released from rest. Speed at equilibrium:

$$v = \omega A = \sqrt{k/m}\cdot A$$

## Problem 12 — Simple Pendulum Period
$L = 0.97~\mathrm{m}$, $g = 11.4~\mathrm{m/s^2}$. Mass is irrelevant.

$$T = 2\pi\sqrt{L/g}$$

## Problem 13 — Simple Pendulum Frequency
$L = 1.8~\mathrm{m}$, $g = 7.89~\mathrm{m/s^2}$.

$$f = \frac{1}{2\pi}\sqrt{g/L}$$

## Problem 14 — Physical Pendulum Angular Frequency
$m = 18.3~\mathrm{kg}$, $I = 9.45~\mathrm{kg\cdot m^2}$, $d = 1.75~\mathrm{m}$.

$$\omega = \sqrt{m g d/I}$$

## Problem 15 — Physical Pendulum Period
$m = 7.2~\mathrm{kg}$, $I = 15.7~\mathrm{kg\cdot m^2}$, $d = 1.34~\mathrm{m}$.

$$T = 2\pi\sqrt{I/(m g d)}$$

## Problem 16 — Conceptual
SHM with amplitude $A$ around $x = 0$:
- Maximum speed occurs at **$x = 0$** (equilibrium).
- Maximum acceleration occurs at **$x = \pm A$** (extremes).
- Total energy: $E = \tfrac{1}{2}k A^2$.
