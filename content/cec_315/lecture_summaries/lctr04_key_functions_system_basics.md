# Lecture 4 — Fundamental Functions and System Concepts

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Jianhua Liu
**Source PDF:** `all_lectures/cec315-lctr04-key-fns-n-sys-basics.pdf`
**Exam coverage:** Exam 1

**Focus:** Sections 1.4 and 1.5 (Pages 30 to 43)

We will get started with DT fundamental functions (signals), since they are easier to understand. After that, we will discuss CT fundamental functions (signals). We will discuss basic concepts of systems as well.

## 4.1 Discrete-Time Unit Impulse and Step

We discuss two most used fundamental DT functions: unit impulse and unit step.

### 4.1.1 DT unit impulse (unit sample)

$$\delta[n] = \begin{cases} 0, & n \neq 0 \\ 1, & n = 0 \end{cases} = \begin{cases} 1, & n = 0 \\ 0, & \text{otherwise} \end{cases}.$$

See Fig. 1.28, duplicated below, for the waveform.

*[Figure: DT unit impulse $\delta[n]$ — a single stem of height 1 at $n = 0$, zero elsewhere.]*

### 4.1.2 DT unit step

$$u[n] = \begin{cases} 0, & n < 0, \\ 1, & n \geq 0. \end{cases}$$

See Fig. 1.29, duplicated below, for the waveform.

*[Figure: DT unit step $u[n]$ — stems of height 1 for $n \geq 0$, zero for $n < 0$.]*

### 4.1.3 Expressing DT unit impulse in terms of DT unit step

Based on the following two unit steps, one is a delayed version of the other:

*[Figure: Two unit step plots — $u[n]$ and $u[n-1]$ — shown for visual comparison.]*

we can see that the unit impulse can be expressed as the difference between them:

$$\delta[n] = u[n] - u[n-1].$$

### 4.1.4 Expressing DT unit step in terms of DT impulses

Based on the following delayed unit impulses:

*[Figure: Stem plots of delayed unit impulses $\delta[n], \delta[n-1], \delta[n-2], \ldots$]*

we can see that the unit step can be expressed as the summation of them:

$$u[n] = \sum_{k=0}^{\infty} \delta[n-k].$$

On the other hand, if we let $m = n - k$, then

$$k = 0 \Rightarrow m = n \text{ and } k \to \infty \Rightarrow m \to -\infty.$$

This leads to

$$u[n] = \sum_{m=-\infty}^{n} \delta[m].$$

The above can also be seen graphically, as shown below (Fig. 1.30 of the book):

*[Figure 1.30: Graphical illustration of $u[n]$ as the running sum of $\delta[m]$ from $m = -\infty$ up to $m = n$.]*

## 4.2 DT Sampling Properties

### 4.2.1 Sampling a value of a signal

We can multiple a signal by an impulse to samples its value

$$x[n]\delta[n-k] = x[k]\delta[n-k].$$

Note the change of the independent variable of $x[\cdot]$ above, as shown below:

*[Figure: Illustration that $x[n]\delta[n-k]$ is nonzero only at $n = k$, where it equals $x[k]$.]*

### 4.2.2 Expressing a signal as summation of shifted sampled values

Consider an arbitrary DT signal $x[n]$, drawing below:

*[Figure: Stem plot of an arbitrary DT signal $x[n]$.]*

Extending the 1st expression of unit step in terms of unit impulse, discussed above, we have

$$x[n] = \sum_{k=-\infty}^{\infty} x[k]\delta[n-k].$$

It turns out that the above expression is especially important in the derivation of the **convolution** operation, which will be discussed later.

## 4.3 Continuous-Time Unit Impulse and Step

We see before that the DT unit impulse is 1 when $n = 0$ and 0 otherwise. This is called **Kronecker delta**. Correspondingly, we have the CT unit impulse, which is called the **Dirac delta**.

### 4.3.1 Definition of CT unit impulse

The Dirac delta is defined by two equations:

$$\delta(t) = \begin{cases} \infty, & t = 0 \\ 0, & t \neq 0 \end{cases},$$

$$\int_{-\infty}^{\infty} \delta(t)\, dt = 1.$$

Comments about the meaning of *terms* of the DT and CT **unit impulses**:

- Meaning of **unit** of DT and CT unit impulses:
  - For the DT unit impulse, its non-zero value is unit, 1.
  - For the CT unit impulse, its inclusive integration value is unit, 1.
- Meaning of **impulse** of DT and CT unit impulses:
  - For the DT unit impulse, it is a single sample value.
  - For the CT unit impulse, it is a very narrow impulse.

The CT unit impulse can be seen as an idealization of unit-area pulses with *arbitrary shape*.

### 4.3.2 Seeing CT unit impulse as an idealization of rectangular pulses

See the drawing below:

*[Figure: Sequence of rectangular pulses of width $\Delta$ and height $1/\Delta$, each with unit area, becoming narrower and taller as $\Delta \to 0$, idealized to $\delta(t)$.]*

### 4.3.3 Seeing CT unit impulse as an idealization of triangle pulses

See the drawing below:

*[Figure: Sequence of triangular pulses with base width $\Delta$ and height $2/\Delta$, each with unit area, becoming narrower and taller as $\Delta \to 0$, idealized to $\delta(t)$.]*

### 4.3.4 CT unit step

$$u(t) = \begin{cases} 1, & t > 0 \\ 0, & t < 0 \end{cases}.$$

Note that the value of $u(t)$ at $t = 0$ is not defined; this leads to flexibilities.

### 4.3.5 Relating CT unit impulse and CT unit step

#### 4.3.5.1 CT unit impulse as the derivative of CT unit step

$$\delta(t) = \frac{du(t)}{dt}.$$

Note that this is equivalent to $\delta[n] = u[n] - u[n-1]$.

#### 4.3.5.2 CT unit step as the integral of CT unit impulse

$$u(t) = \int_{-\infty}^{t} \delta(\tau)\, d\tau.$$

Note that this is equivalent to $u[n] = \sum_{m=-\infty}^{n} \delta[m]$.

### 4.3.6 Sampling with CT unit impulse

As a **theoretical preparation** of **Shannon sampling** theory, we have

$$x(t)\delta(t - \tau) = x(\tau)\delta[t - \tau].$$

Observe the similarity between the DT and CT sampling.

In **practice**, sampling of a CT signal is done as shown below:

*[Figure: Illustration of practical CT sampling — a continuous signal $x(t)$ multiplied by an impulse train, producing a sampled signal.]*

## 4.4 Introduction to Systems

### 4.4.1 Definition of systems

A system is a process/operation in which input signals are transformed to—or cause the system to respond, resulting in—output signals. See below for notations:

*[Figure: Block diagram notations — a CT system box with input $x(t)$ and output $y(t)$, and a DT system box with input $x[n]$ and output $y[n]$.]*

### 4.4.2 Impulse responses

The impulse response of a system is its output when the input is a DT/CT unit impulse $\delta[n]$ or $\delta(t)$.

### 4.4.3 Examples of simple DT systems

- $y[n] = x[n] + \alpha y[n-1]$ where $\alpha$ is typically 0.75 to 0.95. This is a low-pass filter that can be used for filtering out noise. Note that we use $y[n-1]$ on the right-hand side, which leads to an **IIR (infinite impulse response)** filter.
- $y[n] = x[n] - \beta x[n-1]$ where $\beta$ is typically 0.95 to 0.97. This is a **pre-emphasis** filter (high-pass filter) often used before speech recognition. Note that we use $x[n-1]$ on the right-hand here, which leads to an **FIR (finite impulse response)** filter.

## 4.5 Interconnections of Systems

See Figs. 1.42 and 1.43.

### 4.5.1 Series (cascade)

Output of System 1 is the input to System 2.

### 4.5.2 Parallel

The same input is applied to both systems, and their outputs are added.

### 4.5.3 Feedback

The output of System 1 is fed into System 2, whose output is added back to the external input.

## 4.6 Exercises

**Exercise 1**: Consider a CT integration system with the following operation between its input $x(t)$ and output $y(t)$:

$$y(t) = \int_0^t x(\tau)\, d\tau.$$

Assume the input is $x(t) = \delta(t+1) + \delta(t-1) + \delta(t-3)$.

- Determine the expression of $y(t)$ in terms of shifted and scaled versions of fundamental functions.
- Sketch the waveform of both input and output.

**Exercise 2**: Consider a CT differentiation system with the following relation between its input $x(t)$ and output $y(t)$:

$$y(t) = \frac{dx(t)}{dt}.$$

Assume the input is

$$x(t) = \begin{cases} 1, & 0 < t < 2 \\ 0, & \text{otherwise} \end{cases}.$$

- Determine the expression of $y(t)$ in terms of shifted and scaled versions of fundamental functions.
- Sketch the waveform of both the input and output.

## Practice Problems Summary

- **Exercise 1:** Given a CT integrator with input made up of three shifted impulses, derive and sketch the output in terms of shifted unit steps.
- **Exercise 2:** Given a CT differentiator fed a rectangular pulse, express and sketch the output as a sum of shifted impulses.
