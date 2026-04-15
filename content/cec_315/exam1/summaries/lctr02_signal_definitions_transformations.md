# Lecture 2 — Signal Definitions and Transformations

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Jianhua Liu
**Source PDF:** `all_lectures/cec315-lctr02-sig-def-tran.pdf`
**Exam coverage:** Exam 1

**Focus:** Sections 1.1 and 1.2 (Pages 1 to 13)

## 2.1 Definition of a Signal

Signals describe a wide variety of physical phenomena through patterns of variation.

Mathematically, signals are represented as functions of one or more independent variables.

This course focuses on signals involving a single independent variable, generally referred to as "time".

## 2.2 Continuous-Time (CT) vs. Discrete-Time (DT) Signals

### 2.2.1 Continuous-Time Signals

Defined for a continuum of values of the independent variable, denoted as $x(t)$ using parentheses. $t$ is time.

*[Figure 1.3: Example of a recording of speech. Adapted from Applications of Digital Signal Processing, A.V. Oppenheim, ed. (Englewood Cliffs, N.J.: Prentice-Hall, Inc., 1978), p. 121. The signal represents acoustic pressure variations as a function of time for the spoken words "should we chase." The top line of the figure corresponds to the word "should," the second line to the word "we," and the last two lines to the word "chase." Approximate beginnings and endings of each successive sound in each word are indicated. Time span shown is 200 msec.]*

### 2.2.2 Discrete-Time Signals

Defined only at discrete times (integer values), denoted as $x[n]$ using brackets.

*[Figure 1.6: An example of a discrete-time signal: The weekly Dow-Jones stock market index from January 5, 1929, to January 4, 1930. Stem plot with values roughly in the 200–400 range.]*

### 2.2.3 Bridging CT and DT Signals

DT signals often arise from sampling continuous-time phenomena. So, we can sample $x(t)$ to obtain $x[n]$ using a Analog to Digital (A/D) converter (ADC) or Ideal Continuous to Discrete converter.

*[Figure: Block diagram — $x(t)$ enters an "Ideal C to D converter" block (with $T_S = 1/f_S$ as a side input) and outputs $x[n] = x(nT_S)$.]*

*[Figure: Side-by-side plots of $x(t)$ (continuous waveform, amplitudes roughly $-0.1$ to $0.2$, $t$ from $-10$ to $10$) and the sampled $x[n]$ at $f_S = 5\,\text{Hz}$ (stem plot, $n$ from $-40$ to $40$).]*

We can reconstruct $x(t)$ from $x[n]$ using a Digital to Analog (D/A) converter (DAC) or Ideal Discrete to Continuous converter.

*[Figure: Block diagram — $x[n]$ enters an "Ideal D to C converter" block (with $T_S = 1/f_S$ as a side input) and outputs $x(t)$.]*

*[Figure: Side-by-side plots showing $x[n]$ at $f_S = 5\,\text{Hz}$ (stem plot) being reconstructed into $x(t)$ (continuous waveform).]*

Mathematical conditions and implementations will be discussed later.

## 2.3 Signal Energy and Power

Terminology is borrowed from physical systems (like resistors or automobile motion).

### 2.3.1 DC Power Consumed on a Resistor

### 2.3.2 DC Power Consumed on a Resistor

### 2.3.3 Total Energy

- Expressed as $E_\infty$
- Obtained as the integral of $|x(t)|^2$ for CT signals or the sum of $|x[n]|^2$ for DT signals over an infinite interval.

### 2.3.4 Average Power

- Expressed as $P_\infty$
- Obtained as the time-average of the signal energy over an infinite interval.

### 2.3.5 Signal Classification Based on Energy and Power

Signals are classified into three groups:

- finite total energy ($P_\infty = 0$),
- finite average power ($E_\infty = \infty$),
- neither.

## 2.4 Transformations of the Independent Variable

### 2.4.1 Time Shift

Shifting a signal $x(t)$ to $x(t - t_0)$ represents a delay (if $t_0 > 0$) or an advance (if $t_0 < 0$).

See Figures 1.8 and 1.9.

### 2.4.2 Time Reversal

Reflecting a signal about $t = 0$ or $n = 0$ to produce $x(-t)$ or $x[-n]$.

See Figures 1.10 and 1.11.

### 2.4.3 Time Scaling

Linearly stretching or compressing the time axis, such as $x(2t)$ or $x(t/2)$.

See Figure 1.12.

## 2.5 Periodic Signals

A signal is periodic if there is a positive value ($T$ for CT, $N$ for DT) such that $x(t) = x(t + T)$ or $x[n] = x[n + N]$ for all time.

### 2.5.1 Fundamental Period ($T_0$ or $N_0$):

The smallest positive value for which the periodicity condition holds.

See Figures 1.14 and 1.15.

### 2.5.2 Recall Pulse-Width Modulation

### 2.5.3 Sinusoidal Signals

## 2.6 Even and Odd Signals

### 2.6.1 Even Signals

Symmetrical about the origin, where $x(t) = x(-t)$.

### 2.6.2 Odd Signals

Anti-symmetrical about the origin, where $x(t) = -x(-t)$.

See Figure 1.17.

### 2.6.3 Decomposing a Signal into a Sum of an Even Part and an Odd Part

See Figure 1.18.

## Practice Problems Summary

This lecture contains no explicit numbered Examples, Exercises, or Practice Problems — it is a definitions/overview lecture covering signal types, energy/power, transformations, periodicity, and even/odd decomposition. Referenced figures (1.3, 1.6, 1.8, 1.9, 1.10, 1.11, 1.12, 1.14, 1.15, 1.17, 1.18) are illustrative only.
