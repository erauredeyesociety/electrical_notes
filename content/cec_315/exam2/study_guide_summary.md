# Study Guide Summary: Lectures 9–15

---

## Lecture 9: LTI Eigenfunctions and CT Fourier Series
- Complex exponentials are eigenfunctions of LTI systems: input $e^{st}$ → output $H(s)e^{st}$
- **Strategy:** decompose → multiply by eigenvalue → reassemble
- CT FS: $a_k = (1/T)\int_T x(t)e^{-jk\omega_0 t}dt$, synthesis: $x(t) = \sum a_k e^{jk\omega_0 t}$
- $a_0$ = DC (average value), conjugate symmetry $a_{-k} = a_k^*$ for real signals
- **Inspection trick:** expand sines/cosines via Euler, read off coefficients directly

## Lecture 10: Convergence, Properties, DTFS
- **Dirichlet conditions:** absolutely integrable, finite extrema, finite discontinuities
- **Gibbs:** ~9% overshoot at jumps, does NOT vanish with more harmonics
- **Spectral decay:** discontinuous → $1/k$; continuous → $1/k^2$; generally $1/k^{m+1}$
- **Properties:** linearity, time shift ($a_k e^{-jk\omega_0 t_0}$), differentiation ($jk\omega_0 a_k$), Parseval
- **DTFS:** $N$ harmonics only, no convergence issues, coefficients periodic $a_{k+N} = a_k$

## Lecture 11: Frequency Response and Filtering
- $H(j\omega)$: amplitude scaling + phase shift at each frequency
- Output for periodic input: $b_k = a_k \cdot H(jk\omega_0)$
- Filter types: lowpass, highpass, bandpass; ideal vs. real
- RC lowpass: $\omega_c = 1/(RC)$, $-3$ dB point
- **Time-frequency trade-off:** sharp cutoff ↔ slow step response

## Lecture 12: Fourier Transforms (CT and DT)
- CTFT: $X(j\omega) = \int x(t)e^{-j\omega t}dt$; inverse with $1/(2\pi)$
- Key pairs: $e^{-at}u(t) \leftrightarrow 1/(a+j\omega)$, $\delta(t) \leftrightarrow 1$, rect $\leftrightarrow$ sinc
- Periodic signals: $X(j\omega) = \sum 2\pi a_k \delta(\omega - k\omega_0)$
- DTFT: periodic in $\omega$ with period $2\pi$; $a^n u[n] \leftrightarrow 1/(1-ae^{-j\omega})$
- **Sanity check:** $X(0) = \int x(t)dt$ (total area)

## Lecture 13: FT Properties and Convolution
- **Convolution property (most important):** $y = x*h \leftrightarrow Y = X \cdot H$
- Time shift: magnitude unchanged, adds linear phase $-\omega t_0$
- Freq shift: $e^{j\omega_0 t}x(t) \leftrightarrow X(j(\omega-\omega_0))$
- Differentiation: $d/dt \leftrightarrow j\omega$ (amplifies high freq)
- Multiplication: $xy \leftrightarrow (1/2\pi)(X*Y)$
- **Systems from equations:** $d^n/dt^n \to (j\omega)^n$; delay $\to e^{-j\omega k}$
- **4-step pipeline:** transform → multiply → PFE → invert

## Lecture 14: Magnitude, Phase, Filters
- Polar form: $|X|$ and $\angle X$; dB = $20\log_{10}|H|$
- Phase carries structure, magnitude carries energy
- **Linear phase** $= -\omega t_d$ → pure delay, no distortion
- Group delay: $\tau(\omega) = -d(\angle H)/d\omega$; constant = linear phase
- Ideal lowpass → sinc impulse response → noncausal, unrealizable
- Nonideal specs: passband/stopband edges, transition band, ripple
- **Bandwidth × rise time ≈ constant**

## Lecture 15: First/Second-Order Systems, Bode Plots
- **1st-order LP:** $H = 1/(1+j\omega/\omega_c)$; $-3$ dB at $\omega_c$; $-20$ dB/dec slope
- Bode asymptotes: flat below $\omega_c$, $-20$ dB/dec above; phase $0°$ to $-90°$
- **2nd-order:** $H = \omega_n^2/[(j\omega)^2 + 2\zeta\omega_n(j\omega) + \omega_n^2]$
- At $\omega_n$: $|H| = 1/(2\zeta)$, $\angle H = -90°$ always
- Resonance at $\omega_r = \omega_n\sqrt{1-2\zeta^2}$ only if $\zeta < 1/\sqrt{2}$
- %OS $= 100e^{-\pi\zeta/\sqrt{1-\zeta^2}}$, $t_s \approx 4/(\zeta\omega_n)$
- Bode: $-40$ dB/dec high-freq slope, phase $0° \to -180°$
- **Damping:** $\zeta < 1$ underdamped, $= 1$ critical, $> 1$ overdamped

## Key Exam Focus Areas
1. Computing FS coefficients (by integration and by inspection)
2. Gibbs phenomenon (9% overshoot, doesn't vanish)
3. FT computation from definition and using properties
4. Convolution property + PFE pipeline
5. Magnitude/phase evaluation, dB, group delay
6. Second-order system parameters ($\omega_n$, $\zeta$, %OS, $t_s$)
7. Bode plot asymptotes and slopes
