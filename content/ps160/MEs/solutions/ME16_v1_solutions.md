# ME16: Sound — Walkthrough

**Module:** M16 (Sound) — see [m16/](../../m16/)

**Core equations**
- Sound speed in fluid: $v = \sqrt{B/\rho}$ ($B$ = bulk modulus)
- Sound speed in air vs T (K): $v = (331\ \text{m/s})\sqrt{T/273}$
- Sound intensity level (dB): $\beta = 10\log_{10}(I/I_0)$, $I_0 = 10^{-12}\ \text{W/m}^2$
- Inverse-square: $I_2/I_1 = (r_1/r_2)^2$ ⇒ $\beta_2 - \beta_1 = 20\log_{10}(r_1/r_2)$
- N identical incoherent sources: intensities add ⇒ $\Delta\beta = 10\log_{10}(N)$
- Beat frequency: $f_{\text{beat}} = |f_1 - f_2|$
- Constructive interference: path difference $\Delta = n\lambda$ ($n=0,1,2,...$); destructive: $(n+\tfrac12)\lambda$
- Open-open pipe: $f_n = nv/(2L)$, all $n$. Closed-open pipe: $f_n = nv/(4L)$, $n=1,3,5,...$
- Doppler: $f' = f\,\dfrac{v + v_o}{v - v_s}$ with $v_o>0$ if observer moves *toward* source; $v_s>0$ if source moves *toward* observer.

---

## Q1 — Bulk modulus from sound transit time

A sound pulse traverses 20.4 m of an unknown fluid in 14.6 ms; given the fluid density (778 kg/m³), back out the bulk modulus. The mechanical wave speed in a fluid is set by stiffness over inertia ($v=\sqrt{B/\rho}$), so once $v$ is measured we can solve for $B$.

$d = 20.4$ m, $t = 14.6$ ms, $\rho = 778$ kg/m³.
$$v = d/t = 20.4/0.0146 = 1397.26\ \text{m/s}$$
$$B = \rho v^2 = 778(1397.26)^2 = 1.5189\times 10^9\ \text{Pa} = \boxed{1.5189\ \text{GPa}}\ \checkmark$$

---

## Q2 — Travel time underwater

A subsea explosion 278 km from a Coast Guard receiver — how long until the sonar hears it? Compute the speed of sound in seawater from its bulk modulus and density, then divide distance by speed.

$\rho=1025$, $B=2.34\times 10^9$, $d=278{,}000$ m.
$$v = \sqrt{B/\rho} = \sqrt{2.282\times 10^6} = 1510.93\ \text{m/s}$$
$$t = d/v = 278000/1510.93 = \boxed{183.99\ \text{s}}\ \checkmark$$

---

## Q3 — Intensity from one siren, then doubled

A 123-dB siren at 11 m has a definite intensity (W/m²); two such sirens co-located add their (incoherent) intensities. Convert dB → I, then double it.

One siren at 11 m gives 123 dB:
$$I_1 = I_0\cdot 10^{123/10} = 10^{-12}\cdot 10^{12.3} = 1.9953\ \text{W/m}^2$$
Two sirens at the same location → intensities add:
$$I = 2I_1 = \boxed{3.9905\ \text{W/m}^2}\ \checkmark$$

---

## Q4 — Inverse square: dB at a new distance

A drill is 112 dB at 10 m; how loud at 37 m? For a point source in free field, intensity falls as $1/r^2$, which in dB form is $\Delta\beta = 20\log_{10}(r_1/r_2)$ — a simple subtraction without re-converting.

112 dB at 10 m → at 37 m:
$$\Delta\beta = 20\log_{10}(10/37) = 20\log_{10}(0.2703) = -11.364\ \text{dB}$$
$$\beta_{37} = 112 - 11.364 = \boxed{100.636\ \text{dB}}\ \checkmark$$

---

## Q5 — 61 cicadas at 25 m

Each cicada is 105 dB at 1 m. Two effects compound: distance dilutes intensity ($-20\log_{10} r$ from 1 m to 25 m), then 61 incoherent sources add ($+10\log_{10} 61$). Combine the two dB shifts with the original level.

Single cicada at 25 m: $\Delta\beta = 20\log_{10}(1/25) = -27.96$, so $\beta = 105 - 27.96 = 77.04$ dB.
Add 61 incoherent sources: $\Delta\beta = 10\log_{10}(61) = 17.853$.
$$\beta_{\text{total}} = 77.04 + 17.853 = \boxed{94.89\ \text{dB}}\ \checkmark$$

---

## Q6 — Three forks beat puzzle

Two beat measurements ($|f_A-f_C|=2$, $|f_B-f_C|=4$) each give two candidates for $f_C$ (one above, one below); only the value consistent with both constraints is the answer.

A=440, B=446; $|f_A - f_C| = 2$ ⇒ $f_C \in \{438, 442\}$; $|f_B - f_C| = 4$ ⇒ $f_C \in \{442, 450\}$.
Common: $\boxed{442\ \text{Hz}}$ ✓

---

## Q7 — Two speakers facing, first constructive right of center

Two in-phase speakers face each other 7 m apart; for a listener on the axis between them, the path difference is $\Delta = x - (7-x) = 2x-7$ (negative left of center, zero at the midpoint). Constructive maxima occur at $\Delta = n\lambda$, so the first $x$ to the right of center comes from $n=1$.

$T = 23°C = 296\ \text{K}$ ⇒ $v = 331\sqrt{296/273} = 344.67$ m/s. $\lambda = v/f = 344.67/347 = 0.9933$ m.

Listener at $x$ between the speakers (sp1 at 0, sp2 at 7): path difference $\Delta = x - (7-x) = 2x - 7$.

Constructive: $\Delta = n\lambda$ ⇒ $x = (7 + n\lambda)/2$. First $x > 3.5$: $n=1$ ⇒
$$x = (7 + 0.9933)/2 = \boxed{3.9966\ \text{m}}\ \checkmark$$

---

## Q8 — Minimum frequency for constructive at off-axis listener

Two in-phase speakers at $(0,2)$ and $(0,0)$ create different path lengths to a listener at $(5,0)$. The smallest frequency that gives constructive interference is the one whose wavelength exactly equals the path difference (so $n=1$; $n=0$ would require zero offset, which isn't the geometry here).

Sp1 at $(0,2)$, sp2 at $(0,0)$, listener at $(5,0)$. Distances: $r_1 = \sqrt{29} = 5.3852$ m; $r_2 = 5$ m.
$$\Delta = 0.3852\ \text{m}$$
Smallest constructive: $\lambda = \Delta$ (the $n=1$ case; $n=0$ would need zero path difference).
$$f_{\min} = v/\lambda = 344/0.3852 = \boxed{893.12\ \text{Hz}}\ \checkmark$$

---

## Q9 — Open–open pipe, $n=2$

A pipe open at both ends has antinodes at each end, so all integer harmonics are allowed: $f_n = nv/(2L)$. With temperature 14 °C the speed of sound is below the room-temperature 343 m/s value.

$T=14°C=287$ K ⇒ $v = 331\sqrt{287/273} = 339.41$ m/s.
$$f_2 = \dfrac{2v}{2L} = \dfrac{v}{L} = \dfrac{339.41}{0.8} = \boxed{424.23\ \text{Hz}}\ \checkmark$$

---

## Q10 — Closed–open pipe, first overtone

A pipe closed at one end (node there) and open at the other (antinode) supports only odd harmonics: $n=1,3,5,\ldots$. The "first overtone" therefore is $n=3$, *not* $n=2$.

$T=281$ K ⇒ $v = 331\sqrt{281/273} = 335.81$ m/s. Closed–open allows only odd $n$, so the first overtone is $n=3$:
$$f_3 = \dfrac{3v}{4L} = \dfrac{3(335.81)}{4(0.36)} = \boxed{699.61\ \text{Hz}}\ \checkmark$$

---

## Q11 — Doppler: train approaching stationary listener

The train (source) moves toward a stationary observer, so the wavefronts are compressed and the perceived frequency rises. Using the convention $v_s>0$ when the source moves toward the observer, $v_s = +20$ m/s and $v_o=0$.

Source toward observer: $v_s = +20$. Observer at rest: $v_o = 0$. $v=347$.
$$f' = 1056\cdot\dfrac{347}{347 - 20} = 1056\cdot\dfrac{347}{327} = \boxed{1120.59\ \text{Hz}}\ \checkmark$$

---

## Q12 — Doppler: motorcyclist receding from stationary horn

Source is at rest; observer flees away from it, so the observer outruns some wavefronts and hears a *lower* frequency. With "toward source" positive, $v_o = -36$ m/s.

Observer moving away: $v_o = -36$. Source at rest: $v_s = 0$. $v=344$.
$$f' = 685\cdot\dfrac{344 - 36}{344} = 685\cdot\dfrac{308}{344} = \boxed{613.31\ \text{Hz}}\ \checkmark$$

---

## Q13 — Doppler: ambulance ahead going faster east

Both vehicles head east, but the ambulance is ahead and pulling away. From the car's frame: source recedes ($v_s=-43$), observer chases the source ($v_o=+10$). Both effects push the heard frequency below the source frequency, but the chase partially compensates.

Both move east; ambulance has passed the car and pulls away.
Source recedes from observer: $v_s = -43$.
Observer chases source: $v_o = +10$.
$$f' = 1130\cdot\dfrac{343 + 10}{343 - (-43)} = 1130\cdot\dfrac{353}{386} = \boxed{1033.39\ \text{Hz}}\ \checkmark$$

---

## Q14 — Doppler: car ahead north faster than bicyclist behind

The car (source) drives north faster than the cyclist (observer) following behind, so the gap is opening. Source pulls away ($v_s=-25.8$), observer pursues ($v_o=+12.8$). Net effect: lower perceived frequency.

Car (source) pulls away from bicyclist (observer): $v_s = -25.8$.
Bicyclist chases source: $v_o = +12.8$. $v=344$.
$$f' = 916\cdot\dfrac{344 + 12.8}{344 + 25.8} = 916\cdot\dfrac{356.8}{369.8} = \boxed{883.80\ \text{Hz}}\ \checkmark$$

---

## Q15 — dB increase from $\times 19.3$ intensity

The decibel scale is logarithmic in intensity ratio, so any multiplicative change in $I$ adds a fixed dB amount independent of the starting level.

$$\Delta\beta = 10\log_{10}(19.3) = \boxed{12.856\ \text{dB}}\ \checkmark$$

---

## Q16 — Wind instrument vs temperature

A wind instrument's pitch is set by standing waves whose frequency is $f \propto v/L$. The pipe length $L$ barely changes with temperature, but the speed of sound rises with $\sqrt{T}$, so warmer air → higher pitch and cooler air → lower pitch. (This is why brass players warm up before performing.)

Pipe length is fixed → $f \propto v$, and $v$ rises with $T$. So:
- T rises ⇒ $f$ **increases** ✓
- T falls ⇒ $f$ **decreases** ✓

---

**All numeric answers match the source key.**
