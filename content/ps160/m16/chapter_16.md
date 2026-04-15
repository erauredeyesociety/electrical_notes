# Chapter 16 — Sound and Hearing

## 1. Sound Waves

The most general definition of sound is that it is a **longitudinal wave in a medium**. The simplest sound waves are sinusoidal waves which have definite frequency, amplitude, and wavelength. The human ear is sensitive to waves in the audible range.

| Frequency (Hz)    | Classification |
|-------------------|----------------|
| $0$ – $20$        | infrasonic     |
| $20$ – $20{,}000$ | audible        |
| $> 20{,}000$      | ultrasonic     |

The equation describing the displacement of molecules from their equilibrium position while a sound wave propagates in the $+x$ direction is:

$$y(x, t) = A \cos(kx - \omega t)$$

**N.B.**: The $y$ displacement of the molecules from their equilibrium position is along the $x$ direction (longitudinal motion).

The change in volume $\Delta V$ of a small cylindrical slice of cross-section $S$ is:

$$\Delta V = S\,(y_2 - y_1) = S\,[\,y(x + \Delta x, t) - y(x, t)\,]$$

The fractional change in volume is:

$$\frac{dV}{V} = \lim_{\Delta x \to 0}\frac{S\,[\,y(x + \Delta x, t) - y(x, t)\,]}{S\,\Delta x} = \frac{\partial y(x,t)}{\partial x}$$

Using the bulk modulus $B = -p(x,t)/(dV/V)$, we rewrite this as a **pressure wave**:

$$p(x, t) = -B\,\frac{\partial y(x, t)}{\partial x} = B\,k\,A\,\sin(kx - \omega t)$$

where the **pressure amplitude** is:

$$p_{\max} = B\,k\,A$$

### 1.1 Perception of Sound Waves

The physical characteristics of a sound wave are directly related to the perception of that sound by a listener. Perceptions include **loudness** (related to pressure amplitude) and **pitch** (related to frequency). Different instruments (e.g., a clarinet vs. an alto recorder) sounding at the same pitch produce very different waveforms $p(t)$, giving each instrument its characteristic **timbre**. Fourier analysis decomposes these waveforms into harmonic content.

**Example 1 (Ex. 16.1 follow-up):** For 1000 Hz sound waves in air, a displacement amplitude of $1.2 \times 10^{-8}\,\text{m}$ produces a pressure amplitude of $3.0 \times 10^{-2}\,\text{Pa}$.

(a) What is the wavelength of these waves?
(b) What displacement amplitude is needed for the pressure amplitude to reach the pain threshold $30\,\text{Pa}$?
(c) For what wavelength and frequency will a displacement amplitude of $1.2 \times 10^{-8}\,\text{m}$ produce a pressure amplitude of $1.5 \times 10^{-3}\,\text{Pa}$?

---

## 2. Speed of Sound Waves

A sound wave in a bulk fluid causes compressions and rarefactions of the fluid. A general expression for the speed of sound is:

$$v = \sqrt{\frac{\text{restoring force returning the system to equilibrium}}{\text{inertia resisting the return to equilibrium}}}$$

### Derivation via Momentum–Impulse Theorem

Consider a piston of cross-section $A$ pushing on gas molecules with velocity $v_y$. After time $t$, the disturbance has traveled a distance $vt$.

**Longitudinal momentum imparted to the gas:**

$$\text{Momentum} = (\rho\,v\,t\,A)\,v_y \tag{1}$$

The bulk modulus relates stress and strain:

$$B = -\frac{\Delta p}{\Delta V/V_0} = -\frac{-\Delta p}{-A v_y t/(A v t)}$$

$$\Delta p = B\,\frac{v_y}{v}$$

**Longitudinal impulse from the piston:**

$$\text{Impulse} = (\Delta p\,A)\,t = \frac{B\,A\,v_y\,t}{v} \tag{2}$$

Setting momentum equal to impulse:

$$\rho\,v\,t\,A\,v_y = \frac{B\,A\,v_y\,t}{v} \quad\Longrightarrow\quad v^2 = \frac{B}{\rho}$$

### Results

$$\boxed{\;v = \sqrt{\frac{B}{\rho}}\;} \qquad \text{(longitudinal wave in a fluid)} \tag{3}$$

$$\boxed{\;v = \sqrt{\frac{Y}{\rho}}\;} \qquad \text{(longitudinal wave in a solid rod, with Young's modulus } Y) \tag{4}$$

### 2.1 Speed of Sound in Gases

For an ideal gas, the bulk modulus is:

$$B = \gamma\,p_0$$

where $p_0$ is the equilibrium pressure and $\gamma = 1.4$ for diatomic molecules (N$_2$, O$_2$). The ratio $B/\rho$ depends only on absolute temperature, giving:

$$\boxed{\;v = \sqrt{\frac{\gamma R T}{M}}\;}$$

where $R = 8.314\,\text{J/(mol·K)}$, $T$ is absolute temperature (K), and $M$ is the molar mass.

**Example 10:** (a) Show that the fractional change in sound speed from a small temperature change is

$$\frac{dv}{v} = \frac{1}{2}\,\frac{dT}{T}.$$

(b) If $v = 344\,\text{m/s}$ at $20^\circ\text{C}$, what is the change in $v$ for a $1.0^\circ\text{C}$ change in temperature?

---

## 3. Sound Intensity

We write the sound intensity in terms of the displacement amplitude $A$ or the pressure amplitude $p_{\max}$. The instantaneous intensity is the product (force/area)$\times$velocity:

$$I(x,t) = p(x,t)\,v_y(x,t) = [\,p_{\max}\sin(kx - \omega t)\,]\,[\,A\omega\sin(kx - \omega t)\,]$$

$$I(x,t) = B\,k\,A^2\,\omega\,\sin^2(kx - \omega t) \tag{5}$$

Time-averaging $\sin^2 \to \tfrac{1}{2}$:

$$I_\text{av} = \tfrac{1}{2}\,B\,k\,A^2\,\omega \tag{6}$$

Equivalent forms for a sinusoidal wave:

$$I_\text{av} = \tfrac{1}{2}\sqrt{\rho B}\;\omega^2\,A^2 \qquad\text{and}\qquad I_\text{av} = \frac{p_{\max}^2}{2\sqrt{\rho B}}$$

### 3.1 The Decibel Scale

Because the ear's dynamic range is enormous, a logarithmic intensity scale called the **sound intensity level** $\beta$ is used:

$$\boxed{\;\beta = (10\,\text{dB})\,\log_{10}\!\left(\frac{I}{I_0}\right)\;} \tag{7}$$

where $I_0 = 10^{-12}\,\text{W/m}^2$ is the threshold of hearing at 1000 Hz. Sound intensity levels are measured in decibels (dB).

**Example 15:** A sound wave in air at $20^\circ\text{C}$ has frequency $320\,\text{Hz}$ and displacement amplitude $5.00 \times 10^{-3}\,\text{mm}$. Calculate (a) pressure amplitude in Pa, (b) intensity in W/m$^2$, (c) sound intensity level in dB.

---

## 4. Standing Sound Waves and Normal Modes

Standing sound waves are produced in a pipe of length $L$ when traveling waves reflect from the ends. Reflection behavior depends on whether the end is open or closed:

- **Open end**: displacement **antinode**, pressure **node**.
- **Closed end**: displacement **node**, pressure **antinode**.

### Open pipe (both ends open)

$$\lambda_n = \frac{2L}{n}, \qquad f_n = n\,\frac{v}{2L} \qquad (n = 1, 2, 3, \ldots) \tag{8}$$

All integer harmonics are present.

### Stopped pipe (one end closed)

$$\lambda_n = \frac{4L}{n}, \qquad f_n = n\,\frac{v}{4L} \qquad (n = 1, 3, 5, \ldots) \tag{9}$$

Only odd harmonics are present.

**Example 27:** The longest pipe in most medium-size pipe organs is $4.88\,\text{m}$. What is the fundamental frequency if the pipe is (a) open at both ends; (b) stopped (open at only one end)?

---

## 5. Resonance

A system driven at one of its normal-mode frequencies responds with a large amplitude — this is resonance.

**Example 30:** You have a stopped pipe of adjustable length next to a taut $62.0\,\text{cm}$, $7.25\,\text{g}$ wire under tension $4110\,\text{N}$. Adjust the pipe's length so that, when sounding its fundamental, it drives the wire in its **second overtone** with large amplitude. How long should the pipe be?

---

## 6. Interference of Sound Waves

Consider two loudspeakers driven by a common source. A listener hears the superposition of two pressure waves. Strictly, the outgoing waves are spherical with amplitudes falling as $1/r$, but in many problems we treat amplitudes as approximately equal. The total pressure at point $P$ is $\Delta p = \Delta p_1 + \Delta p_2$, and the interference type depends on the phase difference $\Delta\phi$:

$$\frac{\Delta\phi}{2\pi} = \frac{\Delta L}{\lambda}$$

$$\Delta L = m\lambda, \qquad (m = 0, 1, 2, \ldots) \quad\text{constructive} \tag{10}$$

$$\Delta L = \left(m + \tfrac{1}{2}\right)\lambda, \qquad (m = 0, 1, 2, \ldots) \quad\text{destructive} \tag{11}$$

Interference effects are most pronounced for a single frequency.

**Example 33:** Speakers $A$ and $B$ are driven by the same amplifier in phase. Speaker $B$ is $2.00\,\text{m}$ to the right of $A$. Point $Q$ lies on the line extension, $1.0\,\text{m}$ right of $B$. Find the lowest frequency for (a) constructive and (b) destructive interference at $Q$.

### 6.1 Beats

For two pressure waves of equal amplitude and slightly different frequencies $\omega_1 \approx \omega_2$:

$$\Delta p_1(t) = \Delta p_m \sin(\omega_1 t), \qquad \Delta p_2(t) = -\Delta p_m \sin(\omega_2 t)$$

By superposition:

$$\Delta p(t) = 2\,\Delta p_m\,\sin\!\left(2\pi\,\frac{f_1 - f_2}{2}\,t\right)\,\cos\!\left(2\pi\,\frac{f_1 + f_2}{2}\,t\right) \tag{12}$$

using

$$\sin A - \sin B = 2 \sin\!\left(\frac{A - B}{2}\right)\cos\!\left(\frac{A + B}{2}\right).$$

The slow sine envelope modulates the amplitude between loud and quiet. The time between successive loud maxima is

$$t = \frac{1}{|f_1 - f_2|},$$

giving a **beat frequency**:

$$\boxed{\;f_\text{beat} = |f_1 - f_2|\;} \tag{13}$$

**Example 40:** Two organ pipes, open at one end but closed at the other, are each $1.14\,\text{m}$ long. One is lengthened by $2.00\,\text{cm}$. Find the beat frequency between their fundamentals.

### 6.2 The Doppler Effect

The pitch heard by a listener changes when the source, listener, or both are moving relative to the medium.

**Moving Listener, Source at Rest.** The listener moving toward the source intercepts additional waves per unit time:

$$f' = \frac{v\,t/\lambda + v_L\,t/\lambda}{t} = \frac{v + v_L}{\lambda} = \left(\frac{v + v_L}{v}\right)f$$

$$\boxed{\;f' = \left(\frac{v \pm v_L}{v}\right) f\;} \qquad (+\text{ if listener moves toward source}) \tag{14}$$

**Moving Source, Listener at Rest.** The source's motion compresses (or stretches) the wavelength to $\lambda' = (v - v_s)T$, so

$$f' = \frac{v}{\lambda'} = \frac{v}{(v - v_s)T} = \left(\frac{v}{v - v_s}\right)f$$

$$\boxed{\;f' = \left(\frac{v}{v \mp v_s}\right) f\;} \qquad (-\text{ if source moves toward listener}) \tag{15}$$

**Both moving.** Combining the two effects:

$$\boxed{\;f' = \left(\frac{v \pm v_L}{v \mp v_s}\right) f\;} \tag{16}$$

**N.B.** $v_L$ and $v_s$ are measured with respect to the medium (typically air). The upper signs correspond to motion toward the other party.

**Example 44:** (a) A source producing $1.00\,\text{kHz}$ waves moves toward a stationary listener at $\tfrac{1}{2}$ the speed of sound. What frequency is heard? (b) Instead, the source is at rest and the listener approaches at $\tfrac{1}{2}$ the speed of sound. Compare the two answers and explain the difference physically.

---

## 7. Shock Waves

When a source moves faster than the speed of sound ($v_s > v$), the wavefronts pile up into a cone whose half-angle satisfies:

$$\boxed{\;\sin\alpha = \frac{v\,t}{v_s\,t} = \frac{v}{v_s}\;} \qquad\text{(shock wave)} \tag{17}$$

The ratio $v_s/v$ is called the **Mach number**.

**Example 53:** A jet flies overhead at Mach 1.70 at altitude $1250\,\text{m}$.
(a) Find the shock-wave cone angle $\alpha$.
(b) How long after the jet passes directly overhead do you hear the sonic boom? Neglect altitude variation of the speed of sound.

**Example 63:** A ship's sonar operates at $18.0\,\text{kHz}$. Speed of sound in water at $20^\circ\text{C}$ is $1482\,\text{m/s}$.
(a) Wavelength of the emitted waves?
(b) Frequency difference between the directly radiated waves and those reflected from a whale traveling directly toward the stationary ship at $4.95\,\text{m/s}$? *(Note: the whale acts as both a moving listener and then a moving source in reflection — apply the Doppler equation twice.)*
