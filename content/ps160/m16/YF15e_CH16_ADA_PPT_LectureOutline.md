# Chapter 16 — Sound and Hearing (Lecture Outline)

Lecture outline notes for Module 16. Based on the YF Ch 16 ADA PPT.

---

## Learning outcomes

- Describe a sound wave in terms of particle displacements or pressure fluctuations.
- Calculate the speed and intensity of sound waves.
- Understand what determines the resonance frequencies in an organ or flute.
- Understand interference and beats when sound waves from different sources overlap.
- Understand the Doppler effect.

## Sound waves

- Sound is any longitudinal wave in a medium.
- Audible range for humans: $\approx 20$ Hz to $20{,}000$ Hz.
- For a sinusoidal sound wave traveling in $+x$, the displacement of a particle at position $x$ and time $t$ is
$$y(x,t) = A\cos(kx - \omega t)$$
- In a longitudinal wave the particle displacements are **parallel** to the propagation direction (contrast transverse waves like waves on a string).

### Displacement vs. pressure description

The same sound wave can be described as either a displacement wave or a pressure wave:
$$y(x,t) = A\cos(kx - \omega t)$$
$$p(x,t) = B k A\sin(kx - \omega t)$$
The pressure amplitude is $p_\text{max} = B k A$, where $B$ is the bulk modulus.

Note: the pressure wave is $90°$ out of phase with the displacement wave — where the displacement is a maximum (crest), the pressure fluctuation is zero, and vice versa.

### Perception — Fourier analysis

Instruments produce complex pressure-time waveforms that can be decomposed into harmonic content via Fourier analysis. Different instruments playing the same fundamental have different overtone structures, giving each its timbre.

## Speed of sound

Speed depends on the properties of the medium.

- **Fluid:** $v = \sqrt{B/\rho}$
- **Solid rod / bar:** $v = \sqrt{Y/\rho}$ (Young's modulus)
- **Ideal gas:** $v = \sqrt{\gamma R T / M}$ where $\gamma$ is the adiabatic index, $R$ the gas constant, $T$ absolute temperature, $M$ molar mass.

Representative values:

| Material | Speed (m/s) |
|---|---|
| Air (20 °C) | 344 |
| Helium (20 °C) | 999 |
| Hydrogen (20 °C) | 1330 |
| Water (20 °C) | 1482 |
| Aluminum | 6420 |
| Steel | 5941 |

## Sound intensity

Intensity $I$ is the time-average rate at which wave energy is transported per unit area, across a surface perpendicular to the direction of propagation.

For a sinusoidal sound wave in a fluid:
$$I = \tfrac{1}{2}\sqrt{\rho B}\,\omega^2 A^2 = \frac{p_\text{max}^2}{2\rho v} = \frac{p_\text{max}^2}{2\sqrt{\rho B}}$$

For a spherical (point) source radiating total power $P$, at distance $r$:
$$I = \frac{P}{4\pi r^2}$$

## Decibel scale

Because the human ear is sensitive over many decades of intensity, a logarithmic scale is used:
$$\beta = (10\text{ dB})\log_{10}\!\frac{I}{I_0},\qquad I_0 = 10^{-12}\;\mathrm{W/m^2}$$

Representative levels:

| Source | $\beta$ (dB) | $I$ (W/m²) |
|---|---|---|
| Threshold of pain | 120 | $10^0$ |
| Elevated train | 90 | $10^{-3}$ |
| Busy street | 70 | $10^{-5}$ |
| Quiet radio | 40 | $10^{-8}$ |
| Whisper | 20 | $10^{-10}$ |
| Threshold of hearing (1 kHz) | 0 | $10^{-12}$ |

## Standing sound waves in pipes

Sound waves in a pipe reflect from the ends and form standing waves.
- **Open end:** displacement antinode, pressure node.
- **Closed end:** displacement node, pressure antinode.

### Open pipe (both ends open)

All harmonics present:
$$f_n = \frac{n v}{2 L},\quad n = 1, 2, 3,\dots$$

### Stopped pipe (one end closed)

Only odd harmonics:
$$f_n = \frac{n v}{4 L},\quad n = 1, 3, 5,\dots$$

Resonance: a driving tone at $f \approx f_n$ excites a large-amplitude standing wave (e.g. opera singer shattering a glass).

## Interference

When two or more waves overlap, their amplitudes add. Two coherent sources produce:
- Constructive interference where path difference $\Delta r = m\lambda$
- Destructive interference where $\Delta r = (m + \tfrac{1}{2})\lambda$

## Beats

Two tones of slightly different frequencies $f_a$ and $f_b$ sum to a wave whose amplitude is modulated at the difference frequency:
$$f_\text{beat} = |f_a - f_b|$$

Humans hear beats up to $\sim 6$-$7$ Hz; above that, the slow pulsation blurs into a continuous tone. Listening for beats is used to tune instruments.

## Doppler effect

Frequency shift due to source or listener motion (through the medium):
$$f_L = \frac{v + v_L}{v + v_S}\,f_S$$

Sign convention: velocities are positive in the direction from listener toward source.
- Listener approaching stationary source ($v_L > 0$): $f_L > f_S$.
- Source approaching stationary listener ($v_S < 0$): $f_L > f_S$.
- Source receding ($v_S > 0$): $f_L < f_S$ (pitch drops).

## Shock waves

When the source speed $v_S$ exceeds the sound speed $v$, the wavefronts pile up into a cone-shaped **shock wave** with half-angle
$$\sin\alpha = \frac{v}{v_S}$$

The Mach number is $\mathrm{M} = v_S/v$. A sonic boom is heard when the shock cone reaches the observer, not when the plane breaks the sound barrier.
