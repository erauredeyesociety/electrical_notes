# Chapter 16 — Sound and Hearing (Textbook Summary)

Concise summary of Chapter 16 (Young & Freedman), corresponding to Module 16.

---

## Sound waves

Sound consists of longitudinal waves in a medium. A sinusoidal sound wave is characterized by its frequency $f$ and wavelength $\lambda$ (or angular frequency $\omega$ and wave number $k$) and by its displacement amplitude $A$. The pressure amplitude $p_\text{max}$ is directly proportional to the displacement amplitude, the wave number, and the bulk modulus $B$ of the medium:

$$p_\text{max} = B k A\quad\text{(sinusoidal sound wave, Eq. 16.5)}$$

Wave speed in a fluid (bulk modulus $B$, density $\rho$):
$$v = \sqrt{\frac{B}{\rho}}\quad\text{(longitudinal wave in a fluid, Eq. 16.7)}$$

For an ideal gas with adiabatic index $\gamma$, molar mass $M$, and temperature $T$:
$$v = \sqrt{\frac{\gamma R T}{M}}\quad\text{(sound wave in ideal gas, Eq. 16.10)}$$

For a longitudinal wave in a solid rod with Young's modulus $Y$:
$$v = \sqrt{\frac{Y}{\rho}}\quad\text{(Eq. 16.8)}$$

## Intensity and sound intensity level

Intensity $I$ is the time-average rate of energy transport per unit area. For a sinusoidal wave in a fluid:
$$I = \tfrac{1}{2}\sqrt{\rho B}\,\omega^2 A^2 = \frac{p_\text{max}^2}{2\rho v} = \frac{p_\text{max}^2}{2\sqrt{\rho B}}\quad\text{(Eqs. 16.12, 16.14)}$$

Sound intensity level $\beta$ (in dB) relative to reference $I_0 = 10^{-12}\;\mathrm{W/m^2}$:
$$\beta = (10\text{ dB})\log_{10}\!\frac{I}{I_0}\quad\text{(Eq. 16.15)}$$

## Standing sound waves in pipes

A closed end is a displacement node (pressure antinode); an open end is a displacement antinode (pressure node).

**Open pipe** (both ends open), length $L$:
$$f_n = \frac{n v}{2 L},\quad n = 1, 2, 3, \dots\quad\text{(Eq. 16.18)}$$

**Stopped (closed) pipe** (one end closed):
$$f_n = \frac{n v}{4 L},\quad n = 1, 3, 5, \dots\quad\text{(Eq. 16.22)}$$

Only odd harmonics are present in a stopped pipe. Resonance occurs when a driving frequency is near a normal mode.

## Interference

When two or more waves overlap, the resulting amplitude can be larger or smaller than the individual amplitudes, depending on whether the waves arrive in phase (constructive) or out of phase (destructive). For two coherent sources, path-length difference $\Delta r = m\lambda$ gives constructive interference; $\Delta r = (m + \tfrac{1}{2})\lambda$ gives destructive.

## Beats

When two tones with slightly different frequencies $f_a$ and $f_b$ are sounded together, the listener hears the amplitude modulated at the beat frequency:
$$f_\text{beat} = |f_a - f_b|\quad\text{(Eq. 16.24)}$$

## Doppler effect

For a moving source and moving listener, the source frequency $f_S$ and listener frequency $f_L$ are related through the source and listener velocities $v_S$ and $v_L$ (relative to the medium) and the sound speed $v$:
$$f_L = \frac{v + v_L}{v + v_S}\,f_S\quad\text{(Eq. 16.29)}$$

Sign convention: velocities are positive in the direction from listener toward source (L to S).

## Shock waves

If a sound source moves with speed $v_S > v$ (greater than the wave speed) it creates a shock wave. The wave front is a cone with half-angle
$$\sin\alpha = \frac{v}{v_S}\quad\text{(shock-wave Mach angle, Eq. 16.31)}$$

The Mach number is $v_S/v$.

---

## Key takeaways

- Sound in a fluid: $v = \sqrt{B/\rho}$; in a gas, temperature-dependent via $v\propto\sqrt{T}$.
- Intensity of a spherical source falls as $1/r^2$.
- Decibel scale is logarithmic: doubling intensity adds $\approx 3$ dB; 10× = +10 dB.
- Open pipes have all harmonics; stopped pipes have only odd ones.
- Doppler effect: listener moving toward source increases observed frequency.
- Shock wave forms only when source exceeds sound speed.
