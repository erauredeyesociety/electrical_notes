# CEC 315 — Master Sample Problems (Lectures 2–23)

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Scope:** Every worked example / sample problem presented across Lectures 2–23.

This document collects every worked example from the course lectures, organized
by exam. Exam 3 (Part III) covers Lectures 16–23 and is the focus of the most
detail, since it is the upcoming exam.

---

## Table of Contents

### Part I — Exam 1 Material (Lectures 2–8)
- [Lecture 2 — Signal Definitions and Transformations](#lecture-2--signal-definitions-and-transformations)
- [Lecture 3 — Complex Numbers, Exponential and Sinusoidal Signals](#lecture-3--complex-numbers-exponential-and-sinusoidal-signals)
- [Lecture 4 — Key Functions and System Basics](#lecture-4--key-functions-and-system-basics)
- [Lecture 5 — Basic System Properties](#lecture-5--basic-system-properties)
- [Lecture 6 — Discrete-Time LTI Systems and Convolution Sum](#lecture-6--discrete-time-lti-systems-and-convolution-sum)
- [Lecture 7 — Continuous-Time LTI Systems and Properties](#lecture-7--continuous-time-lti-systems-and-properties)
- [Lecture 8 — Differential/Difference Equations and Singularity Functions](#lecture-8--differentialdifference-equations-and-singularity-functions)

### Part II — Exam 2 Material (Lectures 9–15)
- [Lecture 9 — CT Fourier Series](#lecture-9--ct-fourier-series)
- [Lecture 10 — Convergence, Properties, and DT Fourier Series](#lecture-10--convergence-properties-and-dt-fourier-series)
- [Lecture 11 — Frequency Response and Filtering](#lecture-11--frequency-response-and-filtering)
- [Lecture 12 — Fourier Transforms (CT and DT)](#lecture-12--fourier-transforms-ct-and-dt)
- [Lecture 13 — FT Properties, Convolution, and Systems](#lecture-13--ft-properties-convolution-and-systems)
- [Lecture 14 — Magnitude, Phase, Group Delay, and Filters](#lecture-14--magnitude-phase-group-delay-and-filters)
- [Lecture 15 — First/Second-Order Systems and Bode Plots](#lecture-15--firstsecond-order-systems-and-bode-plots)

### Part III — Exam 3 Material (Lectures 16–23)
- [Lecture 16 — Laplace Transform and ROC](#lecture-16--laplace-transform-and-roc)
- [Lecture 17 — Inverse Laplace and Properties](#lecture-17--inverse-laplace-and-properties)
- [Lecture 18 — System Analysis with the Unilateral Laplace Transform](#lecture-18--system-analysis-with-the-unilateral-laplace-transform)
- [Lecture 19 — z-Transform and ROC](#lecture-19--z-transform-and-roc)
- [Lecture 20 — Inverse z-Transform and Properties](#lecture-20--inverse-z-transform-and-properties)
- [Lecture 21 — DT System Analysis and the Unilateral z-Transform](#lecture-21--dt-system-analysis-and-the-unilateral-z-transform)
- [Lecture 22 — Sampling](#lecture-22--sampling)
- [Lecture 23 — Linear Feedback Systems](#lecture-23--linear-feedback-systems)

---

# Part I — Exam 1 Material (Lectures 2–8)

## Lecture 2 — Signal Definitions and Transformations

*Topic tag:* Signals, CT vs DT, transformations, energy/power, periodicity, even/odd*

Lecture 2 is a definitional/overview lecture and contains no explicit numbered worked examples. It introduces CT vs. DT signals, energy/power classification, time transformations (shift, reversal, scaling), periodic signals, and even/odd decomposition. No sample problems are assigned.

---

## Lecture 3 — Complex Numbers, Exponential and Sinusoidal Signals

*Topic tag:* Euler's relation, complex sinusoids, spectrum, derivations*

### Lecture 3 — Example 1: Derive trig identities from Euler's formula
**Topic tag:** Euler's formula / identity derivation.

**Problem.** Using $e^{j\theta}=\cos\theta+j\sin\theta$, derive the angle-sum and product-to-sum identities for $\cos(\alpha\pm\beta)$, $\sin(\alpha\pm\beta)$, $\cos\alpha\cos\beta$, $\cos\alpha\sin\beta$, and $\sin\alpha\sin\beta$.

**Solution.** Start from $e^{j(\alpha+\beta)}=e^{j\alpha}e^{j\beta}$. Expand both sides with Euler:

$$\cos(\alpha+\beta)+j\sin(\alpha+\beta)=(\cos\alpha+j\sin\alpha)(\cos\beta+j\sin\beta).$$

Multiply the right side:

$$=(\cos\alpha\cos\beta-\sin\alpha\sin\beta)+j(\sin\alpha\cos\beta+\cos\alpha\sin\beta).$$

Equating real and imaginary parts gives:

$$\boxed{\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta,\qquad \sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta.}$$

Replacing $\beta\to -\beta$ and using $\cos(-\beta)=\cos\beta$, $\sin(-\beta)=-\sin\beta$:

$$\boxed{\cos(\alpha-\beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta,\qquad \sin(\alpha-\beta)=\sin\alpha\cos\beta-\cos\alpha\sin\beta.}$$

**Product-to-sum.** Write $\cos\alpha=(e^{j\alpha}+e^{-j\alpha})/2$, $\sin\alpha=(e^{j\alpha}-e^{-j\alpha})/(2j)$. Multiplying:

$$\cos\alpha\cos\beta=\tfrac{1}{4}(e^{j\alpha}+e^{-j\alpha})(e^{j\beta}+e^{-j\beta})=\tfrac{1}{2}\big[\cos(\alpha+\beta)+\cos(\alpha-\beta)\big].$$

$$\sin\alpha\sin\beta=\tfrac{1}{2}\big[\cos(\alpha-\beta)-\cos(\alpha+\beta)\big].$$

$$\cos\alpha\sin\beta=\tfrac{1}{2}\big[\sin(\alpha+\beta)-\sin(\alpha-\beta)\big].$$

---

## Lecture 4 — Key Functions and System Basics

*Topic tag:* Impulse/step, sampling, CT vs DT fundamental functions*

### Lecture 4 — Example 1: CT integrator with three impulses
**Topic tag:** Integration of impulses $\to$ steps.

**Problem.** A CT integration system has $y(t)=\int_0^t x(\tau)\,d\tau$. Input $x(t)=\delta(t+1)+\delta(t-1)+\delta(t-3)$. Find $y(t)$ in terms of shifted unit steps and sketch.

**Solution.** The integral of $\delta(t-t_0)$ from $0$ to $t$ equals $u(t-t_0)$ when $t_0\ge 0$, and equals $1$ (i.e., $u(t-t_0)$ restricted) when $t_0<0$. The impulse at $t=-1$ lies outside the integration interval $[0,t]$ for all $t\ge 0$, so it contributes $1$ for $t\ge 0$ (the integrator starts from $0$, but the impulse at $-1$ is *before* the start; the integral is $0$ for $t\ge 0$ from that impulse).

Computing piecewise:

- For $0\le t<1$: no impulse in $[0,t]$, so $y(t)=0$.
- For $1\le t<3$: only $\delta(t-1)$ in range, so $y(t)=1$.
- For $t\ge 3$: both $\delta(t-1)$ and $\delta(t-3)$ in range, so $y(t)=2$.

$$\boxed{y(t)=u(t-1)+u(t-3).}$$

The waveform is a two-step staircase: $0$ for $t<1$, $1$ for $1\le t<3$, $2$ for $t\ge 3$.

### Lecture 4 — Example 2: CT differentiator on a rectangular pulse
**Topic tag:** Derivative of step $\to$ impulse.

**Problem.** A CT differentiator $y(t)=dx/dt$ has input $x(t)=1$ for $0<t<2$ and $0$ otherwise. Find $y(t)$.

**Solution.** Rewrite $x(t)=u(t)-u(t-2)$. Differentiate using $du(t)/dt=\delta(t)$:

$$\boxed{y(t)=\delta(t)-\delta(t-2).}$$

The output consists of a positive impulse at $t=0$ (the rising edge) and a negative impulse at $t=2$ (the falling edge).

---

## Lecture 5 — Basic System Properties

*Topic tag:* Memory, invertibility, causality, stability, time invariance, linearity.*

### Lecture 5 — Example 1: Classify two systems
**Topic tag:** Properties of DT systems.

**Problem.** Consider
$$T_1(x[n])=\frac{1}{x[n+1]}, \qquad T_2(x[n])=x[n]+0.5\,x[n+1].$$
Determine whether each system is invertible, causal, BIBO stable, time invariant, linear, memoryless.

**Solution.**

**$T_1$:**
- *Invertible:* Yes. From $y[n]=1/x[n+1]$ we recover $x[n+1]=1/y[n]$, so $x[n]=1/y[n-1]$ (valid when $x[n+1]\neq0$).
- *Causal:* No. $y[n]$ depends on the future value $x[n+1]$.
- *BIBO stable:* No. If $x[n+1]\to 0$ then $y[n]\to\infty$ — an input bounded by $\epsilon$ can make the output unbounded.
- *Time invariant:* Yes. Let $x_1[n]=x[n-n_0]$. Then $T_1(x_1)[n]=1/x_1[n+1]=1/x[n+1-n_0]=y[n-n_0]$.
- *Linear:* No. The reciprocal is nonlinear: $T_1(ax)=1/(a x[n+1])=(1/a)\,T_1(x)\neq a\,T_1(x)$.
- *Memoryless:* No. The output depends on $x[n+1]\neq x[n]$.

**$T_2$:**
- *Invertible:* Yes (it is an FIR filter with nonzero coefficient at the advance term; can be inverted by iterating backwards).
- *Causal:* No. Uses $x[n+1]$.
- *BIBO stable:* Yes. $|y[n]|\le |x[n]|+0.5|x[n+1]|\le 1.5\,\|x\|_\infty$.
- *Time invariant:* Yes.
- *Linear:* Yes. $T_2(ax_1+bx_2)=a\,T_2(x_1)+b\,T_2(x_2)$.
- *Memoryless:* No. Uses $x[n+1]$.

### Lecture 5 — Example 2: Sketch transformed signals (convolution preparation)
**Topic tag:** Signal transformations.

**Problem.** Sketch $x_1[n]=(0.5)^n u[n]$, $x_2[n]=x_1[n-2]$, $x_3[n]=x_2[-n]$.

**Solution.** $x_1[n]$ is a right-sided decaying geometric sequence: $x_1[0]=1$, $x_1[1]=0.5$, $x_1[2]=0.25,\ldots$, zero for $n<0$. $x_2[n]=x_1[n-2]$ is the same shape delayed by 2: $x_2[2]=1$, $x_2[3]=0.5$, $x_2[4]=0.25,\ldots$, zero for $n<2$. $x_3[n]=x_2[-n]$ reverses $x_2$ about $n=0$: $x_3[-2]=1$, $x_3[-3]=0.5$, $x_3[-4]=0.25,\ldots$, zero for $n>-2$. So $x_3[n]$ is a left-sided decaying geometric sequence supported on $n\le -2$.

---

## Lecture 6 — Discrete-Time LTI Systems and Convolution Sum

*Topic tag:* DT convolution sum, flip-and-slide, properties.*

### Lecture 6 — Example 1: Step-by-step convolution $\{1,2,3\}*\{1,1\}$
**Topic tag:** Direct convolution of finite DT signals.

**Problem.** Compute $y[n]=x[n]*h[n]$ for $x[n]=\{1,2,3\}$ at $n=0,1,2$ and $h[n]=\{1,1\}$ at $n=0,1$.

**Solution.**

**Length:** $N+M-1=3+2-1=4$ samples at $n=0,1,2,3$.

$$y[0]=\sum_k x[k]h[-k]=x[0]h[0]+x[1]h[-1]+x[2]h[-2]=(1)(1)+(2)(0)+(3)(0)=1.$$
$$y[1]=x[0]h[1]+x[1]h[0]+x[2]h[-1]=(1)(1)+(2)(1)+(3)(0)=3.$$
$$y[2]=x[0]h[2]+x[1]h[1]+x[2]h[0]=(1)(0)+(2)(1)+(3)(1)=5.$$
$$y[3]=x[0]h[3]+x[1]h[2]+x[2]h[1]=(1)(0)+(2)(0)+(3)(1)=3.$$

$$\boxed{y[n]=\{1,3,5,3\}\ \text{for } n=0,1,2,3.}$$

**Sanity check:** $(\sum x)(\sum h)=(6)(2)=12=\sum y=1+3+5+3$. ✓

### Lecture 6 — Example 2: Convolution with the unit step (accumulator)
**Topic tag:** Accumulation $h[n]=u[n]$.

**Problem.** If $h[n]=u[n]$ and $x[n]=\{1,2,3\}$ at $n=0,1,2$, compute $y[n]=x[n]*u[n]$.

**Solution.** For causal $x$ and $h=u$:

$$y[n]=\sum_{k=-\infty}^{n}x[k].$$

So $y[0]=1$, $y[1]=1+2=3$, $y[2]=1+2+3=6$, $y[3]=6$ (and stays at 6 for $n\ge 2$). The step response accumulates the input.

### Lecture 6 — Example 3: Convolution with a delayed impulse
**Topic tag:** Delay property.

**Problem.** Compute $y[n]=x[n]*\delta[n-n_0]$.

**Solution.** By the sifting property of the impulse:

$$\boxed{y[n]=x[n-n_0].}$$

The output is the input delayed by $n_0$ samples.

### Lecture 6 — Example 4: Convolution $h[n]$ and $x[n]=\{0.5,2\}$
**Topic tag:** Sum-of-echoes interpretation.

**Problem.** Given $h[n]=\{1,1,1\}$ at $n=0,1,2$ and $x[n]=\{0.5,2\}$ at $n=0,1$, compute $y[n]=x[n]*h[n]$ using the echo view.

**Solution.** Each input sample triggers a scaled, shifted copy of $h$:
- $x[0]=0.5\Rightarrow 0.5 h[n]=\{0.5,0.5,0.5\}$ at $n=0,1,2$.
- $x[1]=2\Rightarrow 2 h[n-1]=\{2,2,2\}$ at $n=1,2,3$.

Summing:
$$y[0]=0.5, \quad y[1]=0.5+2=2.5, \quad y[2]=0.5+2=2.5, \quad y[3]=2.$$

$$\boxed{y[n]=\{0.5,\,2.5,\,2.5,\,2\}\ \text{for } n=0,1,2,3.}$$

### Lecture 6 — Example 5: Convolution $h[n]=\alpha^n u[n]$ with $x[n]=u[n]$
**Topic tag:** Geometric-series sum; step response of an IIR filter.

**Problem.** Let $x[n]=u[n]$ and $h[n]=\alpha^n u[n]$ with $|\alpha|<1$. Find $y[n]=x[n]*h[n]$.

**Solution.** For $n\ge 0$:
$$y[n]=\sum_{k=0}^{n}\alpha^{n-k}\cdot 1=\alpha^n\sum_{k=0}^{n}\alpha^{-k}=\alpha^n\cdot\frac{1-\alpha^{-(n+1)}}{1-\alpha^{-1}}=\frac{1-\alpha^{n+1}}{1-\alpha}.$$

$$\boxed{y[n]=\frac{1-\alpha^{n+1}}{1-\alpha}\,u[n].}$$

As $n\to\infty$, $y[n]\to 1/(1-\alpha)$, the DC gain of the filter.

---

## Lecture 7 — Continuous-Time LTI Systems and Properties

*Topic tag:* CT convolution integral, flip/shift, impulse response, properties.*

### Lecture 7 — Example 1: Sifting property $\int(t^2+3t)\delta(t-2)\,dt$
**Topic tag:** Delta sifting.

**Problem.** Evaluate $\displaystyle\int_{-\infty}^{\infty}(t^2+3t)\delta(t-2)\,dt$.

**Solution.** The impulse is active at $t=2$, so substitute $t=2$ into the test function: $(2)^2+3(2)=4+6=\boxed{10}$.

### Lecture 7 — Example 2: Sifting property $\int e^{-3t}\delta(t+1)\,dt$
**Topic tag:** Delta sifting.

**Problem.** Evaluate $\displaystyle\int_{-\infty}^{\infty}e^{-3t}\delta(t+1)\,dt$.

**Solution.** The impulse is at $t=-1$. Evaluate $e^{-3t}$ at $t=-1$: $e^{-3(-1)}=\boxed{e^3}$.

### Lecture 7 — Example 3: Convolution of two rectangular pulses
**Topic tag:** Graphical convolution with case analysis.

**Problem.** Let $x(t)=u(t)-u(t-1)$ (width-1 pulse) and $h(t)=u(t)-u(t-2)$ (width-2 pulse). Find $y(t)=x(t)*h(t)$.

**Solution.** Supports: $x\ne 0$ on $[0,1]$, $h(t-\tau)\ne 0$ on $[t-2,t]$. Critical values of $t$: $0,1,2,3$. Five cases:

- **Case 1 ($t<0$):** no overlap, $y(t)=0$.
- **Case 2 ($0\le t<1$):** $h$ entering, overlap on $[0,t]$, $y(t)=\int_0^t 1\cdot 1\,d\tau=t$.
- **Case 3 ($1\le t<2$):** full overlap with $x$, $y(t)=\int_0^1 1\cdot 1\,d\tau=1$.
- **Case 4 ($2\le t<3$):** $h$ exiting, overlap on $[t-2,1]$, $y(t)=\int_{t-2}^{1}1\,d\tau=3-t$.
- **Case 5 ($t\ge 3$):** no overlap, $y(t)=0$.

$$\boxed{y(t)=\begin{cases}0,&t<0\\ t,&0\le t<1\\ 1,&1\le t<2\\ 3-t,&2\le t<3\\ 0,&t\ge 3\end{cases}}$$

This is a trapezoidal pulse, as expected from convolving two rectangles.

### Lecture 7 — Example 4: Exponential convolved with unit step
**Topic tag:** CT convolution with step.

**Problem.** Let $x(t)=e^{-at}u(t)$ with $a>0$ and $h(t)=u(t)$. Find $y(t)=x(t)*h(t)$.

**Solution.** For $t<0$, no overlap so $y(t)=0$. For $t\ge 0$:

$$y(t)=\int_0^t e^{-a\tau}\cdot 1\,d\tau=\left[\frac{-1}{a}e^{-a\tau}\right]_0^t=\frac{1}{a}\bigl(1-e^{-at}\bigr).$$

$$\boxed{y(t)=\frac{1}{a}\bigl(1-e^{-at}\bigr)u(t).}$$

This is the running integral of the exponential, approaching $1/a$ as $t\to\infty$.

### Lecture 7 — Example 5: Step response from an impulse response
**Topic tag:** Step response $= \int h$.

**Problem.** Given $h(t)=e^{-t}u(t)$, find the step response $s(t)$.

**Solution.** $s(t)=\int_{-\infty}^{t}h(\tau)\,d\tau=\int_0^t e^{-\tau}\,d\tau=1-e^{-t}$ for $t\ge 0$.

$$\boxed{s(t)=(1-e^{-t})u(t).}$$

---

## Lecture 8 — Differential/Difference Equations and Singularity Functions

*Topic tag:* First-order ODEs/difference eqs, impulse/step responses, singularity functions.*

### Lecture 8 — Example 1: Impulse response of $y'+2y=x$
**Topic tag:** First-order ODE, impulse response.

**Problem.** Find $h(t)$ for $\dfrac{dy}{dt}+2y=x$.

**Solution.** Set $x(t)=\delta(t)$. For $t>0$, the equation is homogeneous: $h'+2h=0\Rightarrow h(t)=Ce^{-2t}$. Integrate both sides of $h'+2h=\delta$ from $0^-$ to $0^+$: the jump in $h$ at $0$ is $h(0^+)-h(0^-)=1$. With $h(0^-)=0$, get $h(0^+)=1=C$.

$$\boxed{h(t)=e^{-2t}u(t).}$$

**Quick formula:** For $y'+ay=bx$, $h(t)=be^{-at}u(t)$.

### Lecture 8 — Example 2: Step response of $y'+2y=3x$
**Topic tag:** Total solution = homogeneous + particular.

**Problem.** Solve $\dfrac{dy}{dt}+2y=3x$ with $x(t)=u(t)$ and $y(0^-)=0$.

**Solution.**
- Homogeneous: $y_h=Ce^{-2t}$.
- Particular (constant input 3): try $y_p=K$: $2K=3\Rightarrow K=3/2$.
- Total: $y(t)=Ce^{-2t}+3/2$.
- Apply IC $y(0)=0$: $0=C+3/2\Rightarrow C=-3/2$.

$$\boxed{y(t)=\frac{3}{2}\bigl(1-e^{-2t}\bigr)u(t).}$$

### Lecture 8 — Example 3: Impulse response by iteration
**Topic tag:** First-order difference equation.

**Problem.** Find $h[n]$ for $y[n]=\tfrac12 y[n-1]+x[n]$.

**Solution.** Set $x[n]=\delta[n]$ and initial rest $h[n]=0$ for $n<0$. Iterate:
$$h[0]=\tfrac12(0)+1=1,\ h[1]=\tfrac12(1)+0=1/2,\ h[2]=1/4,\ h[3]=1/8,\ldots$$

$$\boxed{h[n]=\left(\tfrac12\right)^n u[n].}$$

**Quick formula:** For $y[n]=\alpha y[n-1]+bx[n]$, $h[n]=b\alpha^n u[n]$; stable iff $|\alpha|<1$.

### Lecture 8 — Example 4: Step response by iteration
**Topic tag:** Iterative computation.

**Problem.** Find $s[n]$ for $y[n]=\tfrac12 y[n-1]+x[n]$ with $x[n]=u[n]$.

**Solution.** Iterate from $s[-1]=0$:
$$s[0]=0+1=1,\ s[1]=\tfrac12+1=3/2,\ s[2]=\tfrac34+1=7/4,\ s[3]=\tfrac78+1=15/8,\ldots$$

$$\boxed{s[n]=2-\left(\tfrac12\right)^n=2\bigl(1-(1/2)^{n+1}\bigr),\quad n\ge 0.}$$

The output approaches $2$ as $n\to\infty$ (DC gain).

### Lecture 8 — Example 5: Derivative of $(t+1)u(t)$
**Topic tag:** Product rule with singularity functions.

**Problem.** Compute $\dfrac{d}{dt}\bigl[(t+1)u(t)\bigr]$.

**Solution.** Product rule:
$$\frac{d}{dt}[(t+1)u(t)]=1\cdot u(t)+(t+1)\delta(t).$$
Using $(t+1)\delta(t)=(0+1)\delta(t)=\delta(t)$:

$$\boxed{\frac{d}{dt}[(t+1)u(t)]=u(t)+\delta(t).}$$

The step accounts for the slope of the ramp; the impulse accounts for the jump at $t=0$.

---

# Part II — Exam 2 Material (Lectures 9–15)

## Lecture 9 — CT Fourier Series

*Topic tag:* Eigenfunctions, CTFS analysis/synthesis, coefficients by inspection.*

### Lecture 9 — Example 1: Eigenfunction in action — $\cos(2t)$ through $h(t)=e^{-t}u(t)$
**Topic tag:** LTI eigenfunction property.

**Problem.** System $h(t)=e^{-t}u(t)$, input $x(t)=\cos(2t)$. Find the output.

**Solution.** Compute $H(j2)=\int_0^\infty e^{-\tau}e^{-j2\tau}\,d\tau=1/(1+j2)$.
Magnitude: $|H(j2)|=1/\sqrt{1+4}=1/\sqrt 5\approx 0.447$.
Phase: $\angle H(j2)=-\arctan(2)\approx -63.4°$.

$$\boxed{y(t)=0.447\cos(2t-63.4°).}$$

The frequency is preserved; only magnitude and phase change (eigenfunction property).

### Lecture 9 — Example 2: Delay system as eigenfunction check
**Topic tag:** Pure delay.

**Problem.** $y(t)=x(t-3)$, input $x(t)=e^{j2t}$. Find the output.

**Solution.** $h(t)=\delta(t-3)$, $H(s)=e^{-3s}$. At $s=j2$: $H(j2)=e^{-j6}$, so $|H|=1$, $\angle H=-6$ rad. Output $y(t)=e^{-j6}e^{j2t}=e^{j2(t-3)}$. ✓

### Lecture 9 — Example 3: DT eigenfunction — two-point average
**Topic tag:** DT LTI eigenfunction.

**Problem.** System $y[n]=\tfrac12 x[n]+\tfrac12 x[n-1]$, input $x[n]=e^{j\pi n/3}$. Find output.

**Solution.** $H(z)=\tfrac12+\tfrac12 z^{-1}$. At $z=e^{j\pi/3}$:
$$H(e^{j\pi/3})=\tfrac12+\tfrac12\left(\tfrac12-j\tfrac{\sqrt3}{4}\right)=\tfrac34-j\tfrac{\sqrt3}{4}.$$
$|H|=\sqrt{9/16+3/16}=\sqrt{3/4}\approx 0.866$. Output: $y[n]=0.866\,e^{j(\pi n/3+\angle H)}$.

### Lecture 9 — Example 4: Period and frequency conversions
**Topic tag:** Unit conversions.

**Problem.** (a) $T=0.01$ s. Find $\omega_0$, $f_0$. (b) $T=1$ s.

**Solution.** (a) $\omega_0=2\pi/0.01=200\pi\approx 628.3$ rad/s, $f_0=100$ Hz. (b) $\omega_0=2\pi\approx 6.28$ rad/s, $f_0=1$ Hz.

### Lecture 9 — Example 5: DC coefficient as signal average
**Topic tag:** CTFS $a_0$ = average value.

**Problem.** A periodic signal with $T=4$ equals $3$ on $(0,1)$ and $-1$ on $(1,4)$. Find $a_0$. Repeat when $x=3$ on $(0,2)$ and $-1$ on $(2,4)$.

**Solution.** Case 1: $a_0=\tfrac14[\int_0^1 3\,dt+\int_1^4(-1)\,dt]=\tfrac14[3-3]=0$.
Case 2: $a_0=\tfrac14[6-2]=1$.

### Lecture 9 — Example 6: Fourier series of $x(t)=\sin(\omega_0 t)$
**Topic tag:** Read coefficients from Euler.

**Problem.** Find the CTFS coefficients of $x(t)=\sin(\omega_0 t)$.

**Solution.** Using $\sin(\omega_0 t)=\frac{1}{2j}e^{j\omega_0 t}-\frac{1}{2j}e^{-j\omega_0 t}$:
$$a_1=\frac{1}{2j}=-\frac{j}{2},\quad a_{-1}=-\frac{1}{2j}=\frac{j}{2},\quad a_k=0\ \text{for }|k|\ne 1.$$

$|a_1|=|a_{-1}|=1/2$; $\angle a_1=-\pi/2$, $\angle a_{-1}=+\pi/2$. Conjugate symmetry $a_{-k}=a_k^*$ ✓.

### Lecture 9 — Example 7: CTFS by inspection (multi-term signal)
**Topic tag:** Multiple harmonics.

**Problem.** Find the CTFS of $x(t)=1+\sin(\omega_0 t)+2\cos(\omega_0 t)+\cos(2\omega_0 t+\pi/4)$.

**Solution.** Expand each term via Euler and collect coefficients of $e^{jk\omega_0 t}$:

$$a_0=1,\quad a_1=1-\frac{j}{2},\quad a_{-1}=1+\frac{j}{2},\quad a_2=\frac12 e^{j\pi/4},\quad a_{-2}=\frac12 e^{-j\pi/4},\quad a_k=0\ \text{for }|k|>2.$$

$|a_1|=\sqrt{1+1/4}=\sqrt{5}/2\approx 1.118$, $\angle a_1\approx -26.6°$. $|a_2|=1/2$, $\angle a_2=45°$.

### Lecture 9 — Example 8: Periodic square wave ($T=4$, $T_1=1$)
**Topic tag:** CTFS via analysis integral.

**Problem.** Square wave: $x(t)=1$ for $|t|<1$, $x(t)=0$ for $1<|t|<2$, period $T=4$. Find $a_k$.

**Solution.** $\omega_0=2\pi/4=\pi/2$. DC: $a_0=\frac14\int_{-1}^{1}1\,dt=\tfrac12$.

For $k\ne 0$:
$$a_k=\frac{1}{4}\int_{-1}^{1}e^{-jk(\pi/2)t}\,dt=\frac{1}{4}\cdot\frac{-2j\sin(k\pi/2)}{-jk\pi/2}=\frac{\sin(k\pi/2)}{k\pi}.$$

$$\boxed{a_k=\frac{\sin(k\pi/2)}{k\pi},\ k\ne 0;\qquad a_0=\tfrac12.}$$

Values: $a_{\pm1}=1/\pi\approx 0.318$; $a_{\pm2}=0$; $a_{\pm3}=-1/(3\pi)\approx -0.106$; $a_{\pm4}=0$; $a_{\pm5}=1/(5\pi)$. Even harmonics vanish.

### Lecture 9 — Example 9: Converting between complex and trigonometric forms
**Topic tag:** Representations.

**Problem.** From Example 6: $a_1=-j/2$ for $\sin(\omega_0 t)$. Convert to trig form.

**Solution.** $A_1=|a_1|=1/2$, $\theta_1=\angle a_1=-\pi/2$. The trig form is $x(t)=a_0+2A_1\cos(\omega_0 t+\theta_1)=\cos(\omega_0 t-\pi/2)=\sin(\omega_0 t)$ ✓.

---

## Lecture 10 — Convergence, Properties, and DT Fourier Series

*Topic tag:* Dirichlet/Gibbs, properties, DTFS.*

### Lecture 10 — Example 1: Parseval's relation for a square wave
**Topic tag:** Power conservation.

**Problem.** Square wave oscillating between $\pm 1$ with period $T$. Verify Parseval's relation.

**Solution.** Time domain: $(1/T)\int_T |x|^2\,dt=1$ (the signal is always $\pm 1$).
Frequency domain: coefficients $a_k=2/(jk\pi)$ for $k$ odd, $a_k=0$ for $k$ even, $a_0=0$.
$$\sum_k |a_k|^2=2\sum_{k\text{ odd }>0}\frac{4}{k^2\pi^2}=\frac{8}{\pi^2}\left(1+\frac{1}{9}+\frac{1}{25}+\cdots\right)=\frac{8}{\pi^2}\cdot\frac{\pi^2}{8}=1.\ \checkmark$$

### Lecture 10 — Example 2: Triangular wave coefficients via differentiation property
**Topic tag:** Differentiation $\leftrightarrow jk\omega_0\,a_k$.

**Problem.** Find the CTFS coefficients of the triangular wave with $T=4$ (ramps between $-1$ and $+1$).

**Solution.** Differentiate: $g(t)=dx/dt$ is a square wave alternating $\pm 1$ with period $T=4$. Known square-wave coefficients: $d_k=2/(jk\pi)$ for $k$ odd. The differentiation property gives $d_k=jk\omega_0\,a_k$, so
$$a_k=\frac{d_k}{jk\omega_0}=\frac{d_k}{jk(\pi/2)}=\frac{2 d_k}{jk\pi}=\frac{2}{jk\pi}\cdot\frac{2}{jk\pi}=\frac{4}{(jk\pi)^2}=-\frac{4}{k^2\pi^2}\quad (k\ \text{odd}).$$

And $a_k=0$ for even $k\ne 0$, $a_0=0$ (symmetric).

$$\boxed{a_k=\begin{cases}-4/(k^2\pi^2),&k\text{ odd}\\0,&k\text{ even}\end{cases}}$$

Triangular wave decays as $1/k^2$, faster than the square wave's $1/k$, because it is smoother.

### Lecture 10 — Example 3: DT sine wave DTFS coefficients
**Topic tag:** DT Fourier series.

**Problem.** Find the DTFS coefficients of $x[n]=\sin(2\pi n/N)$.

**Solution.** Expand via Euler: $\sin(2\pi n/N)=\frac{1}{2j}e^{j(2\pi/N)n}-\frac{1}{2j}e^{-j(2\pi/N)n}$. Compare with $x[n]=\sum_{k=\langle N\rangle}a_k e^{jk(2\pi/N)n}$:
$$a_1=\frac{1}{2j}=-\frac{j}{2},\quad a_{-1}=\frac{j}{2},\quad\text{all others}=0.$$
Since DTFS coefficients are periodic with period $N$: $a_{N-1}=a_{-1}=j/2$, etc.

### Lecture 10 — Example 4: DT periodic square wave
**Topic tag:** Finite geometric sum.

**Problem.** DT square wave: $x[n]=1$ for $|n|\le N_1$, $0$ otherwise within one period of length $N$. Find $a_k$.

**Solution.** Using the analysis sum and summing the finite geometric series:
$$a_k=\begin{cases}\dfrac{1}{N}\cdot\dfrac{\sin\bigl[2\pi k(N_1+\tfrac12)/N\bigr]}{\sin(\pi k/N)},&k\ne 0,\pm N,\ldots\\[4pt](2N_1+1)/N,&k=0,\pm N,\ldots\end{cases}$$

---

## Lecture 11 — Frequency Response and Filtering

*Topic tag:* $b_k=a_k H(jk\omega_0)$, LTI filtering of periodic inputs.*

### Lecture 11 — Example 1: CT system with multi-harmonic periodic input
**Topic tag:** Output Fourier coefficients.

**Problem.** System $h(t)=e^{-t}u(t)$ with input $x(t)=1+\sin(\omega_0 t)+2\cos(\omega_0 t)+\cos(2\omega_0 t+\pi/4)$, $\omega_0=2\pi$. Find the output Fourier coefficients $b_k=a_k H(jk\omega_0)$.

**Solution.** Frequency response: $H(j\omega)=1/(1+j\omega)$. Input coefficients (from Lecture 9): $a_0=1$, $a_1=1-j/2$, $a_{-1}=1+j/2$, $a_2=\tfrac12 e^{j\pi/4}$, $a_{-2}=\tfrac12 e^{-j\pi/4}$.

$$b_0=1\cdot\frac{1}{1+0}=1,$$
$$b_1=\left(1-\frac{j}{2}\right)\cdot\frac{1}{1+j2\pi},\qquad b_{-1}=\left(1+\frac{j}{2}\right)\cdot\frac{1}{1-j2\pi},$$
$$b_2=\frac12 e^{j\pi/4}\cdot\frac{1}{1+j4\pi},\qquad b_{-2}=\frac12 e^{-j\pi/4}\cdot\frac{1}{1-j4\pi}.$$

Magnitudes: $|H(j0)|=1$, $|H(j2\pi)|\approx 0.16$, $|H(j4\pi)|\approx 0.079$. The system strongly attenuates higher harmonics (lowpass behavior).

### Lecture 11 — Example 2: RC lowpass filter
**Topic tag:** RC circuit, cutoff frequency.

**Problem.** Find the frequency response of the RC circuit $RC\,dv_C/dt+v_C(t)=v_s(t)$ (output = capacitor voltage).

**Solution.** Substitute $v_s(t)=e^{j\omega t}$, $v_C(t)=H(j\omega)e^{j\omega t}$. Plug into the ODE:
$$RC\cdot j\omega H(j\omega)+H(j\omega)=1\Rightarrow H(j\omega)(1+j\omega RC)=1$$
$$\boxed{H(j\omega)=\frac{1}{1+j\omega RC}.}$$
Magnitude $|H|=1/\sqrt{1+(\omega RC)^2}$, phase $-\arctan(\omega RC)$. Cutoff $\omega_c=1/(RC)$ at $|H|=1/\sqrt 2$ (−3 dB), phase $-45°$.

### Lecture 11 — Example 3: RC highpass filter
**Topic tag:** Same circuit, different output.

**Problem.** Use the same RC circuit but take resistor voltage $v_R$ as output.

**Solution.** $G(j\omega)=\dfrac{j\omega RC}{1+j\omega RC}$. At $\omega=0$: $G=0$. As $\omega\to\infty$: $G\to 1$. Highpass with the same cutoff $\omega_c=1/(RC)$. Note $|H|^2+|G|^2=1$ at every frequency.

### Lecture 11 — Example 4: DT moving-average two-point filter
**Topic tag:** FIR filter.

**Problem.** $y[n]=\tfrac12(x[n]+x[n-1])$. Find $H(e^{j\omega})$ and classify.

**Solution.** $H(e^{j\omega})=\tfrac12(1+e^{-j\omega})=e^{-j\omega/2}\cos(\omega/2)$. $|H|=|\cos(\omega/2)|$. At $\omega=0$: $|H|=1$ (passes DC). At $\omega=\pi$: $|H|=0$ (rejects Nyquist). Lowpass.

### Lecture 11 — Example 5: DT two-point difference (highpass)
**Topic tag:** Simple FIR highpass.

**Problem.** $y[n]=\tfrac12(x[n]-x[n-1])$. Find $H(e^{j\omega})$.

**Solution.** $H(e^{j\omega})=\tfrac12(1-e^{-j\omega})=j\,e^{-j\omega/2}\sin(\omega/2)$. $|H|=|\sin(\omega/2)|$. At $\omega=0$: $|H|=0$ (blocks DC). At $\omega=\pi$: $|H|=1$ (passes Nyquist). Highpass.

---

## Lecture 12 — Fourier Transforms (CT and DT)

*Topic tag:* CTFT, DTFT, basic transform pairs.*

### Lecture 12 — Example 1: FT of $e^{-at}u(t)$, $a>0$
**Topic tag:** Right-sided decaying exponential.

**Problem.** Compute $X(j\omega)$ for $x(t)=e^{-at}u(t)$.

**Solution.**
$$X(j\omega)=\int_0^\infty e^{-at}e^{-j\omega t}dt=\int_0^\infty e^{-(a+j\omega)t}dt=\frac{1}{a+j\omega}.$$

$|X(j\omega)|=1/\sqrt{a^2+\omega^2}$, $\angle X=-\arctan(\omega/a)$. For $a=2$: $|X(0)|=0.5$; $|X(j2)|=1/\sqrt 8\approx 0.354$, $\angle =-45°$.

### Lecture 12 — Example 2: FT of $e^{-a|t|}$, $a>0$
**Topic tag:** Two-sided exponential.

**Problem.** Compute $X(j\omega)$ for $x(t)=e^{-a|t|}$.

**Solution.** Split at $t=0$:
$$X(j\omega)=\int_{-\infty}^{0}e^{at}e^{-j\omega t}dt+\int_0^{\infty}e^{-at}e^{-j\omega t}dt=\frac{1}{a-j\omega}+\frac{1}{a+j\omega}=\boxed{\frac{2a}{a^2+\omega^2}.}$$

Purely real and even (since $x(t)$ is real and even).

### Lecture 12 — Example 3: FT of the unit impulse
**Problem.** $x(t)=\delta(t)$.
**Solution.** $X(j\omega)=\int\delta(t)e^{-j\omega t}dt=e^0=1$. The impulse contains all frequencies equally.

### Lecture 12 — Example 4: FT of a rectangular pulse
**Topic tag:** Sinc in frequency.

**Problem.** $x(t)=1$ for $|t|\le T_1$, $0$ otherwise.

**Solution.**
$$X(j\omega)=\int_{-T_1}^{T_1}e^{-j\omega t}dt=\frac{2\sin(\omega T_1)}{\omega}.$$
At $\omega=0$ (L'Hôpital): $X(0)=2T_1$. For $T_1=1$: $X(0)=2$, first zero at $\omega=\pi$.

### Lecture 12 — Example 5: FT of $e^{j\omega_0 t}$
**Topic tag:** Complex exponential $\leftrightarrow$ impulse.

**Solution.** $e^{j\omega_0 t}\overset{\mathcal F}{\longleftrightarrow}2\pi\delta(\omega-\omega_0)$.

### Lecture 12 — Example 6: FT of $\cos(\omega_0 t)$ and $\sin(\omega_0 t)$
**Topic tag:** Cosine/sine as two impulses.

**Solution.** Using Euler:
$$\cos(\omega_0 t)\leftrightarrow\pi[\delta(\omega-\omega_0)+\delta(\omega+\omega_0)],\qquad \sin(\omega_0 t)\leftrightarrow\frac{\pi}{j}[\delta(\omega-\omega_0)-\delta(\omega+\omega_0)].$$

### Lecture 12 — Example 7: DTFT of the unit impulse
**Problem.** $x[n]=\delta[n]$.
**Solution.** $X(e^{j\omega})=\sum_n\delta[n]e^{-j\omega n}=1$.

### Lecture 12 — Example 8: DTFT of $a^n u[n]$, $|a|<1$
**Topic tag:** Geometric series.

**Solution.**
$$X(e^{j\omega})=\sum_{n=0}^{\infty}(ae^{-j\omega})^n=\frac{1}{1-ae^{-j\omega}}.$$
Magnitude: $|X|=1/\sqrt{1+a^2-2a\cos\omega}$. For $a=0.8$: at $\omega=0$, $|X|=5$ (max); at $\omega=\pi$, $|X|=1/1.8\approx 0.556$ (min). Lowpass shape.

### Lecture 12 — Example 9: DTFT of a rectangular window $\{1,1,\ldots,1\}$, $0\le n\le M$
**Topic tag:** Dirichlet kernel.

**Solution.**
$$X(e^{j\omega})=\sum_{n=0}^{M}e^{-j\omega n}=\frac{1-e^{-j\omega(M+1)}}{1-e^{-j\omega}}=e^{-j\omega M/2}\frac{\sin(\omega(M+1)/2)}{\sin(\omega/2)}.$$

For $M=4$ (5 samples): $X(e^{j0})=5$, first zero at $\omega=2\pi/5$.

### Lecture 12 — Example 10: DTFT of a DT cosine
**Solution.** $\cos(2\pi n/N)\leftrightarrow \pi\delta(\omega-2\pi/N)+\pi\delta(\omega+2\pi/N)$, repeated every $2\pi$.

---

## Lecture 13 — FT Properties, Convolution, and Systems

*Topic tag:* Properties, convolution-multiplication, differential-equation systems.*

### Lecture 13 — Example 1: Time shifting — delayed exponential pulse
**Topic tag:** $x(t-t_0)\leftrightarrow e^{-j\omega t_0}X(j\omega)$.

**Problem.** From Lecture 12: $e^{-2t}u(t)\leftrightarrow 1/(2+j\omega)$. Find the FT of $x(t)=e^{-2(t-3)}u(t-3)$.

**Solution.** $x(t)=g(t-3)$ where $g(t)=e^{-2t}u(t)$. By the time-shift property:
$$\boxed{X(j\omega)=e^{-j3\omega}\cdot\frac{1}{2+j\omega}.}$$
Magnitude is unchanged; phase acquires an extra $-3\omega$ term.

### Lecture 13 — Example 2: Frequency shifting — modulation
**Topic tag:** $e^{j\omega_0 t}x(t)\leftrightarrow X(j(\omega-\omega_0))$.

**Problem.** $x(t)=e^{-|t|}$, so $X(j\omega)=2/(1+\omega^2)$. Find the FT of $y(t)=e^{-|t|}\cos(5t)$.

**Solution.** Use $\cos(5t)=\tfrac12 e^{j5t}+\tfrac12 e^{-j5t}$:
$$Y(j\omega)=\frac12 X(j(\omega-5))+\frac12 X(j(\omega+5))=\frac{1}{1+(\omega-5)^2}+\frac{1}{1+(\omega+5)^2}.$$
The spectrum splits into two copies at $\omega=\pm 5$ (AM-radio effect).

### Lecture 13 — Example 3: Duality — sinc $\to$ ideal lowpass
**Topic tag:** Duality property.

**Problem.** Find the FT of $x(t)=\sin(Wt)/(\pi t)$.

**Solution.** We know rect $\leftrightarrow$ sinc. By duality:
$$X(j\omega)=\begin{cases}1,&|\omega|\le W\\0,&|\omega|>W\end{cases}.$$
A sinc in time yields an ideal rectangular lowpass in frequency.

### Lecture 13 — Example 4: Convolution property — finding system output
**Topic tag:** Partial fractions in $j\omega$.

**Problem.** System $h(t)=e^{-3t}u(t)$, input $x(t)=e^{-2t}u(t)$. Find $y(t)$.

**Solution.** $H=1/(3+j\omega)$, $X=1/(2+j\omega)$, so $Y=1/[(2+j\omega)(3+j\omega)]$. Partial fractions:
$$Y=\frac{A}{2+j\omega}+\frac{B}{3+j\omega}.$$
Setting $j\omega=-2$: $A=1$. Setting $j\omega=-3$: $B=-1$. So $Y=\frac{1}{2+j\omega}-\frac{1}{3+j\omega}$.

$$\boxed{y(t)=(e^{-2t}-e^{-3t})u(t).}$$

**Check:** $y(0)=0$ ✓. $y(1)=e^{-2}-e^{-3}\approx 0.085$.

### Lecture 13 — Example 5: DT convolution property example
**Topic tag:** Partial fractions in $e^{-j\omega}$.

**Problem.** $h[n]=(0.5)^n u[n]$, $x[n]=(0.8)^n u[n]$. Find $y[n]$.

**Solution.** $Y(e^{j\omega})=\frac{1}{(1-0.5e^{-j\omega})(1-0.8e^{-j\omega})}$. Partial fractions:
$$Y=\frac{A}{1-0.5e^{-j\omega}}+\frac{B}{1-0.8e^{-j\omega}}.$$
Setting $e^{-j\omega}=2$ (i.e., $1/0.5$): $A(1-0.8\cdot 2)=1\Rightarrow A=-5/3$.
Setting $e^{-j\omega}=1.25$: $B(1-0.5\cdot 1.25)=1\Rightarrow B=8/3$.

$$\boxed{y[n]=-\frac{5}{3}(0.5)^n u[n]+\frac{8}{3}(0.8)^n u[n].}$$

**Check:** $y[0]=-5/3+8/3=1$ ✓.

### Lecture 13 — Example 6: Second-order CT system from differential equation
**Topic tag:** $d/dt\to j\omega$.

**Problem.** $\dfrac{d^2y}{dt^2}+5\dfrac{dy}{dt}+6y=x(t)$. Find $H(j\omega)$ and $h(t)$.

**Solution.** $(j\omega)^2 Y+5(j\omega)Y+6Y=X\Rightarrow H(j\omega)=\frac{1}{(j\omega+2)(j\omega+3)}$. Partial fractions: $H=\frac{1}{j\omega+2}-\frac{1}{j\omega+3}$.

$$\boxed{h(t)=(e^{-2t}-e^{-3t})u(t).}$$

Both poles in the LHP, so the system is stable.

### Lecture 13 — Example 7: Second-order DT system from difference equation
**Topic tag:** $z^{-1}\leftrightarrow e^{-j\omega}$.

**Problem.** $y[n]-1.2\,y[n-1]+0.32\,y[n-2]=x[n]$. Find $H(e^{j\omega})$ and $h[n]$.

**Solution.** $Y(1-1.2e^{-j\omega}+0.32e^{-j2\omega})=X$, so
$$H(e^{j\omega})=\frac{1}{1-1.2e^{-j\omega}+0.32e^{-j2\omega}}.$$

Factor denominator: roots of $z^2-1.2z+0.32=0$ are $z=0.8,0.4$. So
$$H=\frac{1}{(1-0.8e^{-j\omega})(1-0.4e^{-j\omega})}=\frac{A}{1-0.8e^{-j\omega}}+\frac{B}{1-0.4e^{-j\omega}}.$$
$A=2$, $B=-1$.

$$\boxed{h[n]=2(0.8)^n u[n]-(0.4)^n u[n].}$$

Both poles have $|z|<1$, so the system is stable. $h[0]=2-1=1$ ✓.

---

## Lecture 14 — Magnitude, Phase, Group Delay, and Filters

*Topic tag:* Linear phase = pure delay, group delay, ideal filters.*

### Lecture 14 — Example 1: Nonlinear-phase distortion of a two-component signal
**Topic tag:** Linear vs nonlinear phase.

**Problem.** Input $x(t)=\cos(t)+\cos(3t)$. Pass through System A ($\angle H=-2\omega$, linear phase) and System B ($\angle H(\omega_1)=-2$, $\angle H(\omega_2)=-9$, nonlinear phase). Compare outputs.

**Solution.** *System A:* Both components delayed by $t_d=2$:
$$y_A(t)=\cos(t-2)+\cos(3(t-2))=\cos(t-2)+\cos(3t-6).$$
Exact delayed copy of the input.

*System B:* Component at $\omega_1=1$ delayed by $2/1=2$ s; component at $\omega_2=3$ delayed by $9/3=3$ s:
$$y_B(t)=\cos(t-2)+\cos(3t-9)=\cos(t-2)+\cos(3(t-3)).$$
The components arrive at different times $\Rightarrow$ phase distortion.

### Lecture 14 — Example 2: Group delay of first-order lowpass
**Topic tag:** $\tau(\omega)=-d\angle H/d\omega$.

**Problem.** $H(j\omega)=1/(1+j\omega/\omega_c)$, $\omega_c=3$ rad/s. Find $\tau(\omega)$.

**Solution.** $\angle H=-\arctan(\omega/\omega_c)$. Differentiate:
$$\tau(\omega)=-\frac{d}{d\omega}[-\arctan(\omega/\omega_c)]=\frac{1/\omega_c}{1+(\omega/\omega_c)^2}=\frac{\omega_c}{\omega_c^2+\omega^2}.$$

At $\omega=0$: $\tau=1/\omega_c=1/3\approx 0.333$ s (max). At $\omega=\omega_c=3$: $\tau=1/6\approx 0.167$ s. At $\omega=10$: $\tau=3/109\approx 0.028$ s. Not constant — nonlinear phase.

### Lecture 14 — Example 3: Ideal lowpass impulse response
**Topic tag:** Inverse FT of rectangle with linear phase.

**Problem.** $H(j\omega)=e^{-j\omega t_d}$ for $|\omega|\le\omega_c$, zero otherwise. Find $h(t)$.

**Solution.**
$$h(t)=\frac{1}{2\pi}\int_{-\omega_c}^{\omega_c}e^{-j\omega t_d}e^{j\omega t}d\omega=\frac{1}{2\pi}\int_{-\omega_c}^{\omega_c}e^{j\omega(t-t_d)}d\omega=\frac{\sin(\omega_c(t-t_d))}{\pi(t-t_d)}=\frac{\omega_c}{\pi}\operatorname{sinc}\!\left(\frac{\omega_c(t-t_d)}{\pi}\right).$$

This sinc is noncausal (extends to $t<0$), so ideal lowpass filters are physically unrealizable.

---

## Lecture 15 — First/Second-Order Systems and Bode Plots

*Topic tag:* Standard forms, Bode plots, second-order characterization.*

### Lecture 15 — Example 1: First-order system, $\omega_c=100$ rad/s
**Topic tag:** Key frequency values, Bode reading.

**Problem.** $H(j\omega)=1/(1+j\omega/100)$. Compute $|H|$ and $\angle H$ at $\omega=10,100,1000,10000$.

**Solution.**
- $\omega=10$: $|H|=1/\sqrt{1.01}=0.995\ (-0.04$ dB), $\angle H=-\arctan(0.1)=-5.7°$.
- $\omega=100=\omega_c$: $|H|=1/\sqrt 2=0.707\ (-3$ dB), $\angle H=-45°$.
- $\omega=1000=10\omega_c$: $|H|=1/\sqrt{101}\approx 0.0995\ (-20$ dB), $\angle H\approx -84.3°$.
- $\omega=10000=100\omega_c$: $|H|=0.01\ (-40$ dB).

### Lecture 15 — Example 2: Comparing CT and DT first-order systems
**Topic tag:** $-3$ dB bandwidth of DT first-order.

**Problem.** DT filter $y[n]=a y[n-1]+(1-a)x[n]$ with $a=0.9$. Find the $-3$ dB frequency.

**Solution.** $|H|^2=1/2\Rightarrow\omega_{-3\text{dB}}=\arccos\!\left(\frac{2a^2-a^2+2a-1}{2a}\right)$. For $a=0.9$: $\omega_{-3}\approx 0.325$ rad/sample $\approx\pi/10$.

### Lecture 15 — Example 3: Automobile suspension (second-order CT)
**Topic tag:** Full characterization.

**Problem.** $m\ddot y+b\dot y+ky=b\dot x+kx$, $m=500$ kg, $b=2000$ N·s/m, $k=20000$ N/m. Characterize.

**Solution.** Replace $d/dt\to j\omega$ and divide by $k$:
$$H(j\omega)=\frac{1+j\omega/10}{1-\omega^2/40+j\omega/10}.$$
From standard form $\omega_n=\sqrt{k/m}=\sqrt{40}\approx 6.32$ rad/s, $\zeta=b/(2\sqrt{mk})=2000/(2\sqrt{10^7})\approx 0.316$.

Underdamped ($\zeta<1$). DC: $H(0)=1$. Resonance peak at $\omega\approx\omega_n$:
$$|H(j\omega_n)|=\frac{\sqrt{1+(0.632)^2}}{2(0.316)}\approx\frac{1.183}{0.632}\approx 1.87.$$

The car body oscillates at nearly twice the road disturbance amplitude at resonance.

### Lecture 15 — Example 4: Full-pipeline CT example
**Topic tag:** Equation → output via FT.

**Problem.** $\dfrac{d^2y}{dt^2}+5\dfrac{dy}{dt}+4y=2x(t)$, $x(t)=e^{-t}u(t)$. Find $y(t)$.

**Solution.**
$$H(j\omega)=\frac{2}{(j\omega+1)(j\omega+4)},\quad X(j\omega)=\frac{1}{1+j\omega}.$$
$$Y=\frac{2}{(1+j\omega)^2(4+j\omega)}.$$
Partial fractions:
$$Y=\frac{A}{1+j\omega}+\frac{B}{(1+j\omega)^2}+\frac{C}{4+j\omega}.$$
Set $j\omega=-1$: $B(3)=2\Rightarrow B=2/3$. Set $j\omega=-4$: $C(9)=2\Rightarrow C=2/9$. Compare constant terms: $4A+8/3+2/9=2\Rightarrow A=-2/9$.

Inverse FT (using $1/(a+j\omega)\leftrightarrow e^{-at}u(t)$ and $1/(a+j\omega)^2\leftrightarrow t\,e^{-at}u(t)$):

$$\boxed{y(t)=\left(-\frac{2}{9}e^{-t}+\frac{2}{3}t e^{-t}+\frac{2}{9}e^{-4t}\right)u(t).}$$

Checks: $y(0)=-2/9+0+2/9=0$ ✓. $y(\infty)=0$ ✓.

### Lecture 15 — Example 5: DT FIR lowpass filter design
**Topic tag:** Moving-average/sinc-truncated filter.

**Problem.** Sampling at $f_s=1000$ Hz, pass $f\le 50$ Hz, attenuate $f\ge 100$ Hz.

**Solution.** Normalized: $\omega_p=0.1\pi$, $\omega_s=0.2\pi$, $\Delta\omega=0.1\pi$. Rule of thumb: $M\approx 4\pi/\Delta\omega=40$. Use a 41-tap filter. Ideal lowpass truncated: $h[n]=\sin(\omega_c(n-20))/[\pi(n-20)]$ with $\omega_c=0.15\pi$, $h[20]=\omega_c/\pi=0.15$. Linear phase FIR, group delay 20 samples (20 ms).

---

# Part III — Exam 3 Material (Lectures 16–23)

## Lecture 16 — Laplace Transform and ROC

*Topic tag:* Bilateral Laplace, ROC, fundamental transform pairs.*

### Lecture 16 — Example 1: Right-sided exponential $e^{-at}u(t)$
**Topic tag:** Fundamental Laplace pair.

**Problem.** Compute the Laplace transform of $x(t)=e^{-at}u(t)$.

**Solution.**
$$X(s)=\int_0^\infty e^{-at}e^{-st}dt=\int_0^\infty e^{-(s+a)t}dt.$$
Convergence requires $\operatorname{Re}\{s+a\}>0$, i.e. $\operatorname{Re}\{s\}>-\operatorname{Re}\{a\}$. When this holds:
$$X(s)=\left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_0^{\infty}=\frac{1}{s+a}.$$

$$\boxed{e^{-at}u(t)\overset{\mathcal L}{\longleftrightarrow}\frac{1}{s+a},\quad \operatorname{Re}\{s\}>-\operatorname{Re}\{a\}.}$$

Special case $a=3$: ROC $\sigma>-3$, ROC is the right half-plane to the right of the pole at $s=-3$.

### Lecture 16 — Example 2: Left-sided exponential $-e^{-at}u(-t)$
**Topic tag:** Same algebraic expression, different ROC.

**Problem.** Compute the Laplace transform of $x(t)=-e^{-at}u(-t)$.

**Solution.**
$$X(s)=-\int_{-\infty}^{0}e^{-at}e^{-st}dt=-\int_{-\infty}^{0}e^{-(s+a)t}dt.$$
Convergence as $t\to-\infty$ requires $\operatorname{Re}\{s+a\}<0$, i.e. $\operatorname{Re}\{s\}<-\operatorname{Re}\{a\}$. When it converges:
$$X(s)=-\left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_{-\infty}^{0}=\frac{1}{s+a}.$$

$$\boxed{-e^{-at}u(-t)\overset{\mathcal L}{\longleftrightarrow}\frac{1}{s+a},\quad \operatorname{Re}\{s\}<-\operatorname{Re}\{a\}.}$$

**Key point:** Same $X(s)=1/(s+a)$ as Example 1, but *opposite ROC*. The ROC is essential.

### Lecture 16 — Example 3: Two-sided signal $e^{-3t}u(t)+2e^{2t}u(-t)$
**Topic tag:** Strip ROC.

**Problem.** Find $X(s)$ and ROC.

**Solution.** Linearity:
$$e^{-3t}u(t)\leftrightarrow\frac{1}{s+3},\quad\sigma>-3.$$
$$2e^{2t}u(-t)=-2[-e^{2t}u(-t)]\leftrightarrow\frac{-2}{s-2},\quad\sigma<2.$$
Intersect ROCs:
$$\boxed{X(s)=\frac{1}{s+3}-\frac{2}{s-2},\quad -3<\operatorname{Re}\{s\}<2.}$$
Valid strip since $-3<2$.

### Lecture 16 — Example 4: Sum of two right-sided exponentials
**Topic tag:** Combining over common denominator.

**Problem.** $x(t)=3e^{-2t}u(t)-2e^{-5t}u(t)$.

**Solution.**
$$X(s)=\frac{3}{s+2}-\frac{2}{s+5}=\frac{3(s+5)-2(s+2)}{(s+2)(s+5)}=\frac{s+11}{(s+2)(s+5)}.$$
ROC: intersection of $\sigma>-2$ and $\sigma>-5$ is $\sigma>-2$. The zero at $s=-11$ lies in the ROC.

### Lecture 16 — Example 5: Impulse $\delta(t)$
**Problem.** $x(t)=\delta(t)$.
**Solution.** $X(s)=\int\delta(t)e^{-st}dt=1$, ROC: all $s$ (finite-duration signal).

### Lecture 16 — Example 6: Unit step $u(t)$
**Problem.** $x(t)=u(t)$.
**Solution.** Set $a=0$ in Example 1: $u(t)\leftrightarrow 1/s$, ROC $\operatorname{Re}\{s\}>0$. The pole is at $s=0$ on the $j\omega$-axis; since the $j\omega$-axis is *not* in the ROC, the Fourier transform of $u(t)$ does not follow by simply setting $s=j\omega$.

### Lecture 16 — Example 7: Growing exponential $e^{2t}u(t)$
**Problem.** $x(t)=e^{2t}u(t)$.
**Solution.** $a=-2$: $X(s)=1/(s-2)$, ROC $\operatorname{Re}\{s\}>2$. This signal has no Fourier transform (the $j\omega$-axis is not in the ROC), but the Laplace transform exists.

### Lecture 16 — Example 8: Fourier from Laplace (valid case)
**Problem.** $e^{-3t}u(t)\leftrightarrow 1/(s+3)$, ROC $\sigma>-3$. Find $X(j\omega)$.
**Solution.** Since $\sigma=0$ is in the ROC, substitute $s=j\omega$: $X(j\omega)=1/(j\omega+3)$.

### Lecture 16 — Example 9: Fourier from Laplace (invalid case)
**Problem.** $e^{2t}u(t)\leftrightarrow 1/(s-2)$, ROC $\sigma>2$. Find $X(j\omega)$.
**Solution.** $\sigma=0<2$ is *not* in the ROC, so the FT substitution is invalid. The Fourier transform does not exist.

---

## Lecture 17 — Inverse Laplace and Properties

*Topic tag:* Partial fractions, repeated/complex poles, geometric pole-zero analysis, properties.*

### Lecture 17 — Example 1: Distinct real poles (right-sided)
**Topic tag:** Cover-up method.

**Problem.** Find $x(t)$ given
$$X(s)=\frac{2s+6}{(s+1)(s+3)},\quad\operatorname{Re}\{s\}>-1.$$

**Solution.** Partial fractions:
$$\frac{2s+6}{(s+1)(s+3)}=\frac{A}{s+1}+\frac{B}{s+3}.$$
Set $s=-1$: $2(-1)+6=A(-1+3)\Rightarrow 4=2A\Rightarrow A=2$.
Set $s=-3$: $2(-3)+6=B(-3+1)\Rightarrow 0=-2B\Rightarrow B=0$.
So $X(s)=2/(s+1)$. ROC to the right of $s=-1\Rightarrow$ right-sided:

$$\boxed{x(t)=2e^{-t}u(t).}$$

**Check:** Initial value theorem: $\lim_{s\to\infty}sX(s)=\lim(2s^2+6s)/(s^2+4s+3)=2=x(0^+)$ ✓.

### Lecture 17 — Example 2: Distinct real poles, mixed (two-sided) ROC
**Topic tag:** Strip ROC.

**Problem.** Find $x(t)$ given
$$X(s)=\frac{5s+17}{(s+1)(s-3)},\quad -1<\operatorname{Re}\{s\}<3.$$

**Solution.** Partial fractions:
$$\frac{5s+17}{(s+1)(s-3)}=\frac{A}{s+1}+\frac{B}{s-3}.$$
$s=-1$: $5(-1)+17=A(-1-3)\Rightarrow 12=-4A\Rightarrow A=-3$.
$s=3$: $5(3)+17=B(3+1)\Rightarrow 32=4B\Rightarrow B=8$.

ROC assignment: the pole at $s=-1$ has ROC to its right $\Rightarrow$ right-sided. The pole at $s=3$ has ROC to its left $\Rightarrow$ left-sided.

$$\frac{-3}{s+1}\to -3e^{-t}u(t),\qquad \frac{8}{s-3}\to -8e^{3t}u(-t).$$

$$\boxed{x(t)=-3e^{-t}u(t)-8e^{3t}u(-t).}$$

### Lecture 17 — Example 3: Repeated poles
**Topic tag:** Partial fraction expansion for $(s-p)^n$.

**Problem.** Find $x(t)$ given
$$X(s)=\frac{4s+5}{(s+1)^2(s+3)},\quad\operatorname{Re}\{s\}>-1.$$

**Solution.** For a double pole at $s=-1$:
$$\frac{4s+5}{(s+1)^2(s+3)}=\frac{A}{s+1}+\frac{B}{(s+1)^2}+\frac{C}{s+3}.$$
Multiply through: $4s+5=A(s+1)(s+3)+B(s+3)+C(s+1)^2$.

- Set $s=-3$: $4(-3)+5=C(-3+1)^2=4C\Rightarrow C=-7/4$.
- Set $s=-1$: $4(-1)+5=B(-1+3)=2B\Rightarrow B=1/2$.
- Compare $s^2$ coefficients: $0=A+C\Rightarrow A=7/4$.

$$X(s)=\frac{7/4}{s+1}+\frac{1/2}{(s+1)^2}+\frac{-7/4}{s+3}.$$

All right-sided (ROC $\sigma>-1$). Using $1/(s+a)^2\leftrightarrow te^{-at}u(t)$:

$$\boxed{x(t)=\frac{7}{4}e^{-t}u(t)+\frac{1}{2}t e^{-t}u(t)-\frac{7}{4}e^{-3t}u(t).}$$

### Lecture 17 — Example 4: Complex conjugate poles
**Topic tag:** Complete the square, damped sinusoid.

**Problem.** Find $x(t)$ given
$$X(s)=\frac{2s}{s^2+4s+13},\quad\operatorname{Re}\{s\}>-2.$$

**Solution.** Complete the square: $s^2+4s+13=(s+2)^2+9=(s+2)^2+3^2$. Poles at $s=-2\pm j3$.

Rewrite numerator: $2s=2(s+2)-4$:
$$X(s)=\frac{2(s+2)}{(s+2)^2+9}-\frac{4}{(s+2)^2+9}=2\cdot\frac{s+2}{(s+2)^2+3^2}-\frac{4}{3}\cdot\frac{3}{(s+2)^2+3^2}.$$

Using the pairs
$$\frac{s+a}{(s+a)^2+\omega_d^2}\leftrightarrow e^{-at}\cos(\omega_d t)u(t),\quad\frac{\omega_d}{(s+a)^2+\omega_d^2}\leftrightarrow e^{-at}\sin(\omega_d t)u(t):$$

$$\boxed{x(t)=\left[2e^{-2t}\cos(3t)-\frac{4}{3}e^{-2t}\sin(3t)\right]u(t).}$$

Damped sinusoid: envelope $e^{-2t}$, oscillation at $\omega_d=3$ rad/s.

### Lecture 17 — Example 5: First-order frequency response magnitude
**Topic tag:** Geometric evaluation.

**Problem.** $H(s)=1/(s+a)$, $a>0$. Find $|H(j\omega)|$.

**Solution.** Distance from $j\omega$ to the pole at $-a$ is $\sqrt{a^2+\omega^2}$:
$$|H(j\omega)|=\frac{1}{\sqrt{a^2+\omega^2}}.$$
Larger $a$ $\Rightarrow$ pole further from $j\omega$-axis $\Rightarrow$ flatter, lower peak, wider response.

### Lecture 17 — Example 6: $s$-domain shifting
**Topic tag:** $e^{s_0 t}x(t)\leftrightarrow X(s-s_0)$.

**Problem.** Find the Laplace transform of $e^{-3t}\cos(5t)u(t)$.

**Solution.** Start with $\cos(5t)u(t)\leftrightarrow s/(s^2+25)$, ROC $\sigma>0$. Replace $s$ by $s+3$:

$$\boxed{e^{-3t}\cos(5t)u(t)\leftrightarrow\frac{s+3}{(s+3)^2+25},\quad\operatorname{Re}\{s\}>-3.}$$

### Lecture 17 — Example 7: Differentiation in $s$
**Topic tag:** $-tx(t)\leftrightarrow dX/ds$.

**Problem.** Derive the Laplace transform of $t e^{-2t}u(t)$.

**Solution.** Start with $e^{-2t}u(t)\leftrightarrow 1/(s+2)$. Then
$$-t e^{-2t}u(t)\leftrightarrow\frac{d}{ds}\!\left(\frac{1}{s+2}\right)=\frac{-1}{(s+2)^2}.$$
Multiply by $-1$:

$$\boxed{t e^{-2t}u(t)\leftrightarrow\frac{1}{(s+2)^2},\quad\sigma>-2.}$$

### Lecture 17 — Example 8: Initial and final value theorems
**Topic tag:** Boundary behavior without inverting.

**Problem.** $X(s)=\dfrac{10}{s(s+2)(s+5)}$, ROC $\sigma>0$. Find $x(0^+)$ and $x(\infty)$.

**Solution.** Initial value:
$$x(0^+)=\lim_{s\to\infty}sX(s)=\lim\frac{10}{(s+2)(s+5)}=0.$$

Final value (check: $sX(s)=10/[(s+2)(s+5)]$ has poles at $s=-2,-5$, both LHP ✓):
$$x(\infty)=\lim_{s\to 0}sX(s)=\frac{10}{(2)(5)}=1.$$

$x(t)$ starts at 0, settles at 1 (step response).

---

## Lecture 18 — System Analysis with the Unilateral Laplace Transform

*Topic tag:* Transfer function, stability/causality, block diagrams, IVPs.*

### Lecture 18 — Example 1: Differential equation → $H(s)$
**Topic tag:** Replace $d^k/dt^k\to s^k$.

**Problem.** $\dfrac{d^2y}{dt^2}+5\dfrac{dy}{dt}+6y=2\dfrac{dx}{dt}+x$. Find $H(s)$, poles, zeros, stability.

**Solution.** $(s^2+5s+6)Y=(2s+1)X$, so
$$H(s)=\frac{2s+1}{s^2+5s+6}=\frac{2s+1}{(s+2)(s+3)}.$$
Poles: $s=-2,-3$ (LHP). Zero: $s=-1/2$. Causal and stable.

### Lecture 18 — Example 2: Stability classification table
**Topic tag:** Pole-based stability check.

**Problem.** Classify each as stable, marginally stable, or unstable (causal):

| $H(s)$ | Poles | Classification |
|---|---|---|
| $1/(s+3)$ | $s=-3$ | Stable |
| $1/(s-2)$ | $s=2$ | Unstable |
| $1/(s^2+4)$ | $s=\pm j2$ | Marginally stable |
| $(s+1)/[(s+2)(s+5)]$ | $s=-2,-5$ | Stable |
| $1/[(s+1)(s-1)]$ | $s=\pm 1$ | Unstable |

### Lecture 18 — Example 3: Complete pipeline — differential equation to output
**Topic tag:** Full analysis.

**Problem.** $\dfrac{dy}{dt}+3y=x(t)$, $x(t)=e^{-t}u(t)$. Find $y(t)$.

**Solution.**
1. $H(s)=1/(s+3)$, ROC $\sigma>-3$ (stable, causal ✓).
2. $X(s)=1/(s+1)$, ROC $\sigma>-1$.
3. $Y(s)=1/[(s+3)(s+1)]$, ROC $\sigma>-1$.
4. Partial fractions: $1/[(s+3)(s+1)]=A/(s+3)+B/(s+1)$. Set $s=-3$: $A=-1/2$. Set $s=-1$: $B=1/2$.
5. Both terms right-sided:
$$\boxed{y(t)=\frac{1}{2}\bigl(e^{-t}-e^{-3t}\bigr)u(t).}$$

**Checks:** $y(0^+)=0$ ✓. $y(\infty)=0$ ✓. $y'(0^+)=\tfrac12(-1+3)=1=x(0^+)$ (from ODE) ✓.

### Lecture 18 — Example 4: First-order IVP with the unilateral transform
**Topic tag:** Zero-input response.

**Problem.** Solve $\dfrac{dy}{dt}+3y=0$, $y(0^-)=5$.

**Solution.** Unilateral Laplace: $[sY-y(0^-)]+3Y=0\Rightarrow (s+3)Y=5\Rightarrow Y=5/(s+3)$. Invert:

$$\boxed{y(t)=5e^{-3t}u(t).}$$

Checks: $y(0)=5$ ✓; $y'(0)=-15=-3 y(0)$ ✓ (matches ODE).

### Lecture 18 — Example 5: Second-order IVP
**Topic tag:** Multiple derivatives with ICs.

**Problem.** Solve $\dfrac{d^2y}{dt^2}+5\dfrac{dy}{dt}+6y=2u(t)$, $y(0^-)=1$, $y'(0^-)=0$.

**Solution.** Unilateral transform:
$$\mathcal L_u\{y''\}=s^2Y-sy(0^-)-y'(0^-)=s^2 Y-s.$$
$$\mathcal L_u\{5y'\}=5[sY-y(0^-)]=5sY-5.$$
$$\mathcal L_u\{6y\}=6Y,\qquad\mathcal L_u\{2u(t)\}=2/s.$$

Combine:
$$s^2Y-s+5sY-5+6Y=\frac{2}{s}\Rightarrow (s^2+5s+6)Y=\frac{2}{s}+s+5.$$
$$Y(s)=\frac{s^2+5s+2}{s(s+2)(s+3)}.$$

Partial fractions:
$$\frac{s^2+5s+2}{s(s+2)(s+3)}=\frac{A}{s}+\frac{B}{s+2}+\frac{C}{s+3}.$$
$s=0$: $2=A(2)(3)\Rightarrow A=1/3$.
$s=-2$: $4-10+2=B(-2)(1)\Rightarrow -4=-2B\Rightarrow B=2$.
$s=-3$: $9-15+2=C(-3)(-1)\Rightarrow -4=3C\Rightarrow C=-4/3$.

$$\boxed{y(t)=\left[\frac{1}{3}+2e^{-2t}-\frac{4}{3}e^{-3t}\right]u(t).}$$

**Checks:** $y(0)=1/3+2-4/3=1$ ✓. $y'(0)=0-4+4=0$ ✓. $y(\infty)=1/3$ (step DC gain $H(0)=1/6$, $2\cdot 1/6=1/3$ ✓).

### Lecture 18 — Example 6: ZSR + ZIR decomposition
**Topic tag:** Total response split.

**Problem.** For the previous problem, decompose $y$ into zero-state and zero-input responses.

**Solution.**
*ZSR* (set $y(0^-)=0$, $y'(0^-)=0$, keep input $2u(t)$):
$$Y_{ZS}(s)=\frac{2/s}{(s+2)(s+3)}=\frac{2}{s(s+2)(s+3)}.$$

*ZIR* (zero input, keep ICs):
$$Y_{ZI}(s)=\frac{s+5}{(s+2)(s+3)}.$$

Sum: $Y_{ZS}+Y_{ZI}=\dfrac{s^2+5s+2}{s(s+2)(s+3)}$ ✓ matches total response.

---

## Lecture 19 — z-Transform and ROC

*Topic tag:* Bilateral z-transform, unit circle, ROC properties.*

### Lecture 19 — Example 1: Right-sided geometric $a^n u[n]$
**Topic tag:** Geometric series, exterior ROC.

**Problem.** Compute $X(z)$ for $x[n]=a^n u[n]$.

**Solution.**
$$X(z)=\sum_{n=0}^{\infty}a^n z^{-n}=\sum_{n=0}^{\infty}(az^{-1})^n.$$
Converges iff $|az^{-1}|<1$, i.e. $|z|>|a|$. Then

$$\boxed{a^n u[n]\overset{\mathcal Z}{\longleftrightarrow}\frac{1}{1-az^{-1}}=\frac{z}{z-a},\quad |z|>|a|.}$$

Pole at $z=a$, zero at $z=0$.

### Lecture 19 — Example 2: Decaying geometric ($a=0.5$)
**Problem.** $x[n]=(0.5)^n u[n]$.
**Solution.** $X(z)=1/(1-0.5 z^{-1})$, ROC $|z|>0.5$.
**Sanity checks:** At $z=1$ (DC): $X(1)=1/0.5=2=\sum_{n=0}^{\infty}(0.5)^n$ ✓. At $z=-1$ (Nyquist): $X(-1)=1/1.5=2/3$ ✓.

### Lecture 19 — Example 3: Growing geometric ($a=2$)
**Problem.** $x[n]=2^n u[n]$.
**Solution.** $X(z)=1/(1-2z^{-1})$, ROC $|z|>2$. Unit circle $|z|=1<2$ is *not* in ROC $\Rightarrow$ DTFT does not exist, consistent with $\sum 2^n$ diverging.

### Lecture 19 — Example 4: Left-sided geometric $-a^n u[-n-1]$
**Topic tag:** Interior ROC.

**Problem.** Compute the z-transform of $x[n]=-a^n u[-n-1]$.

**Solution.**
$$X(z)=-\sum_{n=-\infty}^{-1}a^n z^{-n}=-\sum_{m=1}^{\infty}(a^{-1}z)^m.$$
Converges iff $|z/a|<1$, i.e. $|z|<|a|$. Sum of geometric starting at $m=1$:
$$X(z)=-\frac{z/a}{1-z/a}=\frac{1}{1-az^{-1}}.$$

$$\boxed{-a^n u[-n-1]\leftrightarrow\frac{1}{1-az^{-1}},\quad |z|<|a|.}$$

Same algebraic expression as Example 1, but interior ROC.

### Lecture 19 — Example 5: Left-sided, $a=3$
**Problem.** $x[n]=-(3)^n u[-n-1]$. Find $X(z)$.
**Solution.** $X(z)=1/(1-3z^{-1})$, ROC $|z|<3$. Unit circle is inside ROC, so DTFT exists.

### Lecture 19 — Example 6: Unit impulse and delayed impulse
**Problem.** $\delta[n]$ and $\delta[n-k]$.
**Solution.** $\delta[n]\leftrightarrow 1$, ROC: all $z$. $\delta[n-k]\leftrightarrow z^{-k}$, ROC: $|z|>0$ for $k\ge 1$.

### Lecture 19 — Example 7: Unit step $u[n]$
**Problem.** $x[n]=u[n]$.
**Solution.** Special case $a=1$: $u[n]\leftrightarrow 1/(1-z^{-1})=z/(z-1)$, ROC $|z|>1$. Pole on unit circle, so DTFT needs special derivation.

### Lecture 19 — Example 8: Two-sided signal with annular ROC
**Topic tag:** Ring ROC.

**Problem.** $x[n]=(0.5)^n u[n]+2(3)^n u[-n-1]$.

**Solution.** Right-sided: $(0.5)^n u[n]\leftrightarrow 1/(1-0.5 z^{-1})$, $|z|>0.5$.
Left-sided: $2(3)^n u[-n-1]=-2[-3^n u[-n-1]]\leftrightarrow -2/(1-3z^{-1})$, $|z|<3$.

$$\boxed{X(z)=\frac{1}{1-0.5 z^{-1}}-\frac{2}{1-3z^{-1}},\quad 0.5<|z|<3.}$$

Annular ring; unit circle is inside, so DTFT exists.

### Lecture 19 — Example 9: Sum of two right-sided terms
**Problem.** $x[n]=3(0.4)^n u[n]-2(0.8)^n u[n]$.

**Solution.**
$$X(z)=\frac{3}{1-0.4 z^{-1}}-\frac{2}{1-0.8 z^{-1}}=\frac{3(1-0.8 z^{-1})-2(1-0.4 z^{-1})}{(1-0.4 z^{-1})(1-0.8 z^{-1})}=\frac{1-1.6 z^{-1}}{(1-0.4 z^{-1})(1-0.8 z^{-1})}.$$

ROC: intersection $|z|>0.4\cap|z|>0.8=|z|>0.8$. Poles: $z=0.4,0.8$. Zero: $z=1.6$.

**Check:** $X(1)=(-0.6)/[(0.6)(0.2)]=-5$. Direct: $3/0.6-2/0.2=5-10=-5$ ✓.

### Lecture 19 — Example 10: Finite-duration sequence
**Problem.** $x[n]=\{2,-1,3,0,4\}$ at $n=0,\ldots,4$. Find $X(z)$.
**Solution.** $X(z)=2-z^{-1}+3z^{-2}+4z^{-4}$, ROC: all $z\ne 0$.
**Check:** $X(1)=2-1+3+0+4=8=\sum x[n]$ ✓.

---

## Lecture 20 — Inverse z-Transform and Properties

*Topic tag:* Partial fractions in $z^{-1}$, geometric evaluation, properties.*

### Lecture 20 — Example 1: Distinct real poles, right-sided
**Topic tag:** Basic inverse z-transform.

**Problem.** Find $x[n]$ given
$$X(z)=\frac{3-z^{-1}}{(1-0.5 z^{-1})(1-0.25 z^{-1})},\quad|z|>0.5.$$

**Solution.** Partial fractions:
$$\frac{3-z^{-1}}{(1-0.5 z^{-1})(1-0.25 z^{-1})}=\frac{A}{1-0.5 z^{-1}}+\frac{B}{1-0.25 z^{-1}}.$$
Multiply through: $3-z^{-1}=A(1-0.25 z^{-1})+B(1-0.5 z^{-1})$.
- $z^{-1}=2$ (kills the 0.5 factor): $3-2=A(1-0.5)\Rightarrow 1=0.5A\Rightarrow A=2$.
- $z^{-1}=4$: $3-4=B(1-2)\Rightarrow -1=-B\Rightarrow B=1$.

Both poles inside ROC $\Rightarrow$ both right-sided:

$$\boxed{x[n]=2(0.5)^n u[n]+(0.25)^n u[n].}$$

**Check:** $x[0]=2+1=3=X(z)|_{z\to\infty}$ ✓ (initial value).

### Lecture 20 — Example 2: Mixed ROC (two-sided signal)
**Topic tag:** Annular ROC assignment.

**Problem.** Find $x[n]$ given
$$X(z)=\frac{1}{(1-2z^{-1})(1-0.5 z^{-1})},\quad 0.5<|z|<2.$$

**Solution.** Partial fractions:
$$X(z)=\frac{A}{1-2z^{-1}}+\frac{B}{1-0.5 z^{-1}}.$$
Multiply by $(1-2z^{-1})$ and set $z^{-1}=1/2$: $1/(1-0.5\cdot 0.5)=A\Rightarrow 1/(1-0.25)=A\Rightarrow A=4/3$.
Multiply by $(1-0.5 z^{-1})$ and set $z^{-1}=2$: $1/(1-4)=B\Rightarrow B=-1/3$.

ROC assignment:
- Pole at $z=2$ ($|z|=2$): ROC is interior ($|z|<2$) $\Rightarrow$ left-sided. So $(4/3)/(1-2z^{-1})\to -(4/3)2^n u[-n-1]$.
- Pole at $z=0.5$: ROC is exterior $\Rightarrow$ right-sided. So $(-1/3)/(1-0.5 z^{-1})\to -(1/3)(0.5)^n u[n]$.

$$\boxed{x[n]=-\frac{4}{3}\cdot 2^n u[-n-1]-\frac{1}{3}(0.5)^n u[n].}$$

### Lecture 20 — Example 3: Repeated poles
**Topic tag:** $(n+1)a^n u[n]$ pair.

**Problem.** Find $x[n]$ given $X(z)=1/(1-0.5 z^{-1})^2$, $|z|>0.5$.

**Solution.** Use the pair $1/(1-az^{-1})^2\leftrightarrow(n+1)a^n u[n]$:

$$\boxed{x[n]=(n+1)(0.5)^n u[n].}$$

**Check:** $x[0]=1$, $x[1]=2\cdot 0.5=1$, $x[2]=3\cdot 0.25=0.75$, etc.

### Lecture 20 — Example 4: Complex conjugate poles — damped sinusoid
**Topic tag:** $r^n\cos(\omega_0 n)$ pair.

**Problem.** Find $x[n]$ given
$$X(z)=\frac{1-0.8\cos(0.4\pi) z^{-1}}{1-2(0.8)\cos(0.4\pi) z^{-1}+0.64 z^{-2}},\quad|z|>0.8.$$

**Solution.** Match with pair $r^n\cos(\omega_0 n)u[n]\leftrightarrow\dfrac{1-r\cos(\omega_0)z^{-1}}{1-2r\cos(\omega_0)z^{-1}+r^2 z^{-2}}$. Identify $r=0.8$, $\omega_0=0.4\pi$. Poles at $z=0.8 e^{\pm j0.4\pi}$.

$$\boxed{x[n]=(0.8)^n\cos(0.4\pi n)u[n].}$$

Damped discrete-time sinusoid: envelope $(0.8)^n$, oscillation frequency $0.4\pi$ rad/sample.

### Lecture 20 — Example 5: Time-shifting property
**Problem.** $x[n]=(0.5)^n u[n]\leftrightarrow 1/(1-0.5 z^{-1})$, $|z|>0.5$. Find the z-transform of $y[n]=x[n-3]$.
**Solution.** $Y(z)=z^{-3}\cdot\dfrac{1}{1-0.5 z^{-1}}=\dfrac{z^{-3}}{1-0.5 z^{-1}}$, ROC $|z|>0.5$. The delay adds three zeros at $z=0$.

### Lecture 20 — Example 6: Initial and final value theorems
**Topic tag:** Boundary behavior for causal sequences.

**Problem.** $X(z)=\dfrac{5}{(1-z^{-1})(1-0.6 z^{-1})}$, $|z|>1$. Find $x[0]$ and $x[\infty]$.

**Solution.**
*Initial value:* $x[0]=\lim_{z\to\infty}X(z)=5/[(1)(1)]=5$.

*Final value:* Check: $(1-z^{-1})X(z)=5/(1-0.6 z^{-1})$ has a single pole at $z=0.6$ (inside unit circle) ✓.
$$x[\infty]=\lim_{z\to 1}(1-z^{-1})X(z)=\frac{5}{1-0.6}=12.5.$$

$x[n]$ starts at 5, settles at 12.5.

---

## Lecture 21 — DT System Analysis and the Unilateral z-Transform

*Topic tag:* Difference equation → $H(z)$, stability, unilateral transform, IVPs.*

### Lecture 21 — Example 1: Difference equation → $H(z)$
**Topic tag:** Replace delays with $z^{-k}$.

**Problem.** $y[n]-0.8\,y[n-1]+0.15\,y[n-2]=x[n]+2 x[n-1]$. Find $H(z)$, poles, zero.

**Solution.** Transform:
$$(1-0.8 z^{-1}+0.15 z^{-2})Y=(1+2z^{-1})X\Rightarrow H(z)=\frac{1+2 z^{-1}}{1-0.8 z^{-1}+0.15 z^{-2}}.$$

Factor the denominator from $z^2-0.8 z+0.15=0$: $z=(0.8\pm\sqrt{0.04})/2=(0.8\pm 0.2)/2$. Poles: $z_1=0.5$, $z_2=0.3$. Zero: $z=-2$.

$$\boxed{H(z)=\frac{1+2z^{-1}}{(1-0.5 z^{-1})(1-0.3 z^{-1})}.}$$

Both poles inside unit circle $\Rightarrow$ causal and stable.

### Lecture 21 — Example 2: Stability classification

| $H(z)$ | Pole $|p|$ | Causal+stable? |
|---|---|---|
| $1/(1-0.5 z^{-1})$ | 0.5 | Yes |
| $1/(1-1.2 z^{-1})$ | 1.2 | No (unstable) |
| $1/(1-z^{-1})$ | 1.0 | Marginally stable |
| $1/[(1-0.3 z^{-1})(1+0.7 z^{-1})]$ | 0.3, 0.7 | Yes |

### Lecture 21 — Example 3: Full pipeline — difference equation to output
**Topic tag:** Complete DT analysis.

**Problem.** $y[n]-0.5\,y[n-1]=x[n]$ with $x[n]=(0.8)^n u[n]$. Find $y[n]$.

**Solution.**
1. $H(z)=1/(1-0.5 z^{-1})$, $|z|>0.5$.
2. $X(z)=1/(1-0.8 z^{-1})$, $|z|>0.8$.
3. $Y(z)=1/[(1-0.5 z^{-1})(1-0.8 z^{-1})]$, $|z|>0.8$.
4. Partial fractions:
$$\frac{1}{(1-0.5 z^{-1})(1-0.8 z^{-1})}=\frac{A}{1-0.5 z^{-1}}+\frac{B}{1-0.8 z^{-1}}.$$
Set $z^{-1}=2$: $1=A(1-1.6)\Rightarrow A=-5/3$.
Set $z^{-1}=1.25$: $1=B(1-0.625)\Rightarrow B=8/3$.
5. Both right-sided:

$$\boxed{y[n]=\left[-\frac{5}{3}(0.5)^n+\frac{8}{3}(0.8)^n\right]u[n].}$$

**Checks:** $y[0]=-5/3+8/3=1=x[0]$ ✓. $y[1]=-5/6+32/15=-25/30+64/30=39/30=1.3$; from ODE $y[1]=0.5\cdot 1+0.8=1.3$ ✓.

### Lecture 21 — Example 4: First-order difference equation with IC
**Topic tag:** Unilateral time-shift property.

**Problem.** $y[n]-0.6\,y[n-1]=(0.5)^n u[n]$, $y[-1]=4$.

**Solution.** Unilateral transform uses $\mathcal Z_u\{y[n-1]\}=z^{-1}Y+y[-1]$:
$$Y-0.6(z^{-1}Y+4)=\frac{1}{1-0.5 z^{-1}}.$$
$$(1-0.6 z^{-1})Y-2.4=\frac{1}{1-0.5 z^{-1}}.$$
$$Y=\frac{1}{(1-0.5 z^{-1})(1-0.6 z^{-1})}+\frac{2.4}{1-0.6 z^{-1}}.$$

Partial fractions on the first term:
$z^{-1}=2$: $A=1/(1-1.2)=-5$.
$z^{-1}=5/3$: $B=1/(1-5/6)=6$.

$$Y=\frac{-5}{1-0.5 z^{-1}}+\frac{6+2.4}{1-0.6 z^{-1}}=\frac{-5}{1-0.5 z^{-1}}+\frac{8.4}{1-0.6 z^{-1}}.$$

$$\boxed{y[n]=[-5(0.5)^n+8.4(0.6)^n]u[n].}$$

**Checks:** $y[0]=-5+8.4=3.4$. From ODE: $y[0]=0.6\cdot 4+1=3.4$ ✓. $y[1]=-2.5+5.04=2.54$. From ODE: $y[1]=0.6\cdot 3.4+0.5=2.54$ ✓.

### Lecture 21 — Example 5: Second-order zero-input response
**Topic tag:** Multiple ICs.

**Problem.** $y[n]-0.7\,y[n-1]+0.1\,y[n-2]=0$, $y[-1]=1$, $y[-2]=0$.

**Solution.** Unilateral time-shift formulas:
$$\mathcal Z_u\{y[n-1]\}=z^{-1}Y+y[-1]=z^{-1}Y+1.$$
$$\mathcal Z_u\{y[n-2]\}=z^{-2}Y+y[-2]+y[-1]z^{-1}=z^{-2}Y+z^{-1}.$$

Substitute into the difference equation:
$$Y-0.7(z^{-1}Y+1)+0.1(z^{-2}Y+z^{-1})=0.$$
$$(1-0.7 z^{-1}+0.1 z^{-2})Y=0.7-0.1 z^{-1}.$$

Factor: $z^2-0.7 z+0.1=0\Rightarrow z=(0.7\pm 0.3)/2$, so $z=0.5,0.2$.
$$Y(z)=\frac{0.7-0.1 z^{-1}}{(1-0.5 z^{-1})(1-0.2 z^{-1})}.$$

Partial fractions:
$z^{-1}=2$: $(0.7-0.2)=A(1-0.4)\Rightarrow 0.5=0.6A\Rightarrow A=5/6$.
$z^{-1}=5$: $(0.7-0.5)=B(1-2.5)\Rightarrow 0.2=-1.5B\Rightarrow B=-2/15$.

$$\boxed{y[n]=\left[\frac{5}{6}(0.5)^n-\frac{2}{15}(0.2)^n\right]u[n].}$$

Pure zero-input response (no external input). Both modes decay since both poles are inside the unit circle.

**Check:** $y[0]=5/6-2/15=25/30-4/30=21/30=0.7$. From ODE: $y[0]=0.7\cdot 1-0.1\cdot 0=0.7$ ✓.

---

## Lecture 22 — Sampling

*Topic tag:* Nyquist rate, reconstruction, aliasing.*

### Lecture 22 — Example 1(a): Nyquist rate of a sum of sinusoids
**Problem.** $x(t)=1+\cos(2000\pi t)+\sin(4000\pi t)$.
**Solution.** Highest frequency $\omega_M=4000\pi$ rad/s $=2000$ Hz. Nyquist rate $=2\omega_M=8000\pi$ rad/s $=4000$ Hz.

### Lecture 22 — Example 1(b): Nyquist rate of a sinc
**Problem.** $x(t)=\sin(4000\pi t)/(\pi t)$.
**Solution.** This is $4000\operatorname{sinc}(4000 t)$ whose FT is a rectangle of width $8000\pi$ centered at $0$. So $\omega_M=4000\pi$, Nyquist rate $=8000\pi$ rad/s $=4000$ Hz.

### Lecture 22 — Example 1(c): Nyquist rate of a squared sinc
**Problem.** $x(t)=[\sin(4000\pi t)/(\pi t)]^2$.
**Solution.** Squaring in time $=$ convolving spectra. Rectangle of width $8000\pi$ convolved with itself gives a *triangle* of width $16000\pi$. So $\omega_M=8000\pi$, Nyquist rate $=16000\pi$ rad/s $=8000$ Hz.
**Lesson:** Squaring a signal doubles its bandwidth.

### Lecture 22 — Example 2: Checking which sampling periods work
**Problem.** $x(t)$ is the output of an ideal lowpass filter with $\omega_c=1000\pi$ rad/s. Which sampling periods work?
(a) $T=0.5$ ms, (b) $T=2$ ms, (c) $T=0.1$ ms.

**Solution.** $\omega_M=1000\pi$ rad/s, required $\omega_s>2000\pi$ rad/s, i.e. $T<2\pi/(2000\pi)=10^{-3}$ s $=1$ ms.
- (a) $T=0.5$ ms $<1$ ms ✓ (oversampled 2×).
- (b) $T=2$ ms $>1$ ms ✗ (aliasing).
- (c) $T=0.1$ ms $\ll 1$ ms ✓ (oversampled 10×).

### Lecture 22 — Example 3: Sampling at exactly the Nyquist rate fails
**Problem.** $x(t)=\sin(\omega_s t/2)$ sampled at $\omega_s$.
**Solution.** Samples: $x(nT)=\sin(\omega_s/2\cdot 2\pi n/\omega_s)=\sin(\pi n)=0$ for every $n$. All samples are zero. This is why $\omega_s>2\omega_M$ must be a *strict* inequality.

### Lecture 22 — Example 4: Aliasing of a 5 Hz cosine sampled at 6 Hz
**Problem.** $x(t)=\cos(2\pi\cdot 5 t)$, $f_s=6$ Hz.
**Solution.** Nyquist rate $=10$ Hz $>f_s=6$ Hz, undersampled. Aliased frequency: $f_\text{alias}=|f_s-f_0|=|6-5|=1$ Hz. The 5 Hz tone folds to 1 Hz.

### Lecture 22 — Practice Problems (answers summarized)

**P1.** $\omega_M=5000\pi$. Nyquist rate $=10000\pi$ rad/s $=5000$ Hz; $T_\max<0.2$ ms.

**P2.** False. Equality is not sufficient (Example 3).

**P3.** Multiplication in time by a periodic impulse train $\leftrightarrow$ convolution in frequency with a frequency-domain impulse train $\Rightarrow$ spectral replicas.

**P4.** No. Overlapping replicas are additively mixed; the information is permanently lost.

**P5.** Anti-aliasing filter: lowpass filter placed *before* the sampler to bandlimit the input to below $\omega_s/2$.

**P6.** $x(t)=\cos(600\pi t)+\cos(1800\pi t)$. Highest $\omega_M=1800\pi$. Nyquist rate $=3600\pi$ rad/s $=1800$ Hz.

**P7.** $\omega_M=3000\pi$, $T=2\times 10^{-4}\Rightarrow\omega_s=2\pi/T=10000\pi>6000\pi=2\omega_M$. No aliasing.

**P8.** $\cos(2\pi\cdot 900 t)$ at $f_s=1000$. $f_s/2=500$, $f_0=900>500\Rightarrow$ aliased to $|1000-900|=100$ Hz.

**P9.** $f_s=1500$. $f_s/2=750<900$, still aliased: $|1500-900|=600$ Hz.

**P10.** $x(t-5)$: same Nyquist rate $\omega_0$ (time-shift preserves spectrum magnitude). $x(2t)$: time compression doubles the bandwidth, Nyquist rate becomes $2\omega_0$.

**P11.** Because the sampled spectrum is scaled by $1/T$; the filter must have gain $T$ to restore the original amplitude.

**P12.** The zero-order hold is a staircase approximation; its FT introduces a $\operatorname{sinc}$ distortion in the passband and aliases outside it. Not exact.

**P13.** 25 rev/s filmed at 24 fps: the blade effectively appears to rotate at $|25-24|=1$ rev/s (backward or forward depending on direction) — the "wagon-wheel effect".

**P14.** $\omega_M=10000\pi$, Nyquist rate $=20000\pi$ rad/s $=10000$ Hz. $f_s=8000$ Hz is *not* sufficient. Minimum valid $f_s>10000$ Hz.

**P15.** Use an anti-aliasing lowpass filter before sampling to bandlimit the signal. Any energy above $\omega_s/2$ is filtered out beforehand.

---

## Lecture 23 — Linear Feedback Systems

*Topic tag:* Closed-loop formula, Nyquist, gain/phase margins.*

### Lecture 23 — Example 1: Cascade + feedback
**Problem.** $H_1=1/(s+1)$, $H_2=1/(s+3)$, feedback $G=2$. Find $Q(s)=Y/X$.

**Solution.** Cascade: $H_1 H_2=1/[(s+1)(s+3)]=1/(s^2+4s+3)$. Then
$$Q(s)=\frac{H_1 H_2}{1+G\cdot H_1 H_2}=\frac{1/(s^2+4s+3)}{1+2/(s^2+4s+3)}=\frac{1}{s^2+4s+5}.$$

Poles: $s^2+4s+5=0\Rightarrow s=-2\pm j$. Both LHP $\Rightarrow$ **stable**.

### Lecture 23 — Example 2: Unity feedback with adjustable gain
**Problem.** Forward $H(s)=K/(s+2)$, unity feedback. Find closed-loop pole vs. $K$.

**Solution.**
$$Q(s)=\frac{K/(s+2)}{1+K/(s+2)}=\frac{K}{s+2+K}.$$
Closed-loop pole at $s=-(2+K)$.

| $K$ | Pole | Comment |
|---|---|---|
| 0 | $-2$ | No feedback effect |
| 8 | $-10$ | Faster, stable |
| $-3$ | $+1$ | Unstable |

Stable when $K>-2$.

### Lecture 23 — Example 3: Stabilizing an unstable plant
**Problem.** Plant $H(s)=3/(s-1)$ (unstable), unity feedback gain $K$.
**Solution.**
$$Q(s)=\frac{3K/(s-1)}{1+3K/(s-1)}=\frac{3K}{s-1+3K}.$$
Closed-loop pole at $s=1-3K$. Stable iff $1-3K<0$, i.e. $K>1/3$. For $K=1$: pole at $s=-2$ (stable, fast).

### Lecture 23 — Example 4: Drawing a Nyquist plot
**Problem.** $G(s)H(s)=1/[(s+1)(s/2+1)]$. Plot.

**Solution.** Evaluate at $s=j\omega$:

| $\omega$ | $|GH|$ | $\angle GH$ | Point |
|---|---|---|---|
| 0 | 1 | 0° | $(1,0)$ |
| 1 | 0.632 | $-71.6°$ | $(0.20,-0.60)$ |
| 2 | 0.316 | $-108.4°$ | $(-0.10,-0.30)$ |
| $\infty$ | 0 | $-180°$ | $(0,0)$ |

The curve starts at $(1,0)$, sweeps through the lower half-plane, and returns to the origin as $\omega\to\infty$. Mirror image for $\omega<0$.

### Lecture 23 — Example 5: Nyquist stability check
**Problem.** The Nyquist curve crosses the negative real axis at $(-0.5,0)$. Open-loop is stable. Is the closed loop stable for $K=1$? Find $K_\max$.

**Solution.** For $K=1$, critical point $-1/K=-1$. The curve only reaches $-0.5$, so $-1$ is not encircled $\Rightarrow$ **stable**. Instability begins at $-1/K=-0.5$, so $K_\max=2$.

### Lecture 23 — Example 6: Gain and phase margin calculation
**Problem.** From a Bode plot: at $\omega_2=10$ rad/s, $|GH|=0$ dB, $\angle GH=-135°$. At $\omega_1=31$ rad/s, $|GH|=-12$ dB, $\angle GH=-180°$.
(a) Phase margin? (b) Gain margin? (c) Stable? (d) Max tolerable time delay?

**Solution.**
(a) $\mathrm{PM}=180°+\angle GH(\omega_2)=180°-135°=45°$.
(b) $\mathrm{GM}=-|GH(\omega_1)|_\text{dB}=0-(-12)=12$ dB. Linearly: $10^{12/20}=4$.
(c) Both margins positive $\Rightarrow$ **stable**.
(d) A time delay $\tau$ adds phase $-\omega\tau$. At the gain crossover $\omega_2=10$:
$$\omega_2\tau_\max=\mathrm{PM}\text{ (in radians)}=45°\cdot\pi/180°=0.785\ \text{rad}.$$
$$\tau_\max=0.785/10=0.0785\ \text{s}\approx 79\ \text{ms}.$$

### Lecture 23 — Example 7: Problem 1 — Cascade + unity feedback
**Problem.** Forward path $\tfrac{2}{s+1}$ and $\tfrac{1}{s+4}$ in cascade, unity feedback. Find $Q$.
**Solution.** Cascade: $\tfrac{2}{(s+1)(s+4)}=\tfrac{2}{s^2+5s+4}$.
$$Q=\frac{2/(s^2+5s+4)}{1+2/(s^2+5s+4)}=\frac{2}{s^2+5s+6}=\frac{2}{(s+2)(s+3)}.$$
Stable.

### Lecture 23 — Example 8: Problem 2 — Parallel + feedback
**Problem.** Two parallel paths $3/(s+2)$ and $1/(s+5)$, feedback gain 4.
**Solution.** Parallel: $\tfrac{3}{s+2}+\tfrac{1}{s+5}=\tfrac{3(s+5)+(s+2)}{(s+2)(s+5)}=\tfrac{4s+17}{(s+2)(s+5)}$.
$$Q=\frac{(4s+17)/[(s+2)(s+5)]}{1+4(4s+17)/[(s+2)(s+5)]}=\frac{4s+17}{(s+2)(s+5)+4(4s+17)}=\frac{4s+17}{s^2+23s+78}.$$

### Lecture 23 — Example 9: Problem 3 — Nested loops
**Problem.** Forward path $1/s$. Inner feedback gain 3, outer unity feedback.
**Solution.** Inner loop: $\dfrac{1/s}{1+3/s}=\dfrac{1}{s+3}$. Outer: $\dfrac{1/(s+3)}{1+1/(s+3)}=\dfrac{1}{s+4}$.

### Lecture 23 — Example 10: Problem 4 — Unity feedback first-order
**Problem.** $H(s)=K/(s+5)$, $G=1$.
(a) $Q=K/(s+5+K)$, pole $s=-(5+K)$.
(b) Stable for $K>-5$.
(c) Pole at $-10$ requires $5+K=10\Rightarrow K=5$.

### Lecture 23 — Example 11: Problem 5 — Unity feedback second-order
**Problem.** $H=K/[(s+1)(s+2)]$, $G=1$.
(a) Characteristic equation: $(s+1)(s+2)+K=s^2+3s+2+K=0$.
(b) Stable when all roots have negative real part. By Routh (or direct): both coefficients must be positive: $2+K>0\Rightarrow K>-2$. (The $s^1$ coefficient is 3, always positive.)

### Lecture 23 — Example 12: Problem 6 — DT feedback
**Problem.** $H(z)=Kz^{-1}/(1-0.8 z^{-1})$, unity feedback.
**Solution.** Closed-loop denominator: $1-0.8 z^{-1}+K z^{-1}=1+(K-0.8)z^{-1}$. Multiply by $z$: $z+(K-0.8)=0\Rightarrow z=0.8-K$. Stable iff $|0.8-K|<1\Rightarrow -0.2<K<1.8$. For $K>0$: $0<K<1.8$.

### Lecture 23 — Example 13: Problem 7 — Margins from Bode data
**Problem.** At $\omega_2=5$ rad/s, $|GH|=0$ dB, $\angle GH=-150°$. At $\omega_1=20$ rad/s, $|GH|=-8$ dB, $\angle GH=-180°$.
**Solution.**
(a) $\mathrm{PM}=180°-150°=30°$.
(b) $\mathrm{GM}=8$ dB (factor $10^{8/20}\approx 2.51$).
(c) Both positive $\Rightarrow$ stable.
(d) $\tau_\max=(30°\cdot\pi/180°)/\omega_2=0.524/5\approx 105$ ms.

### Lecture 23 — True/False Problems

**P8.** "Negative feedback always stabilizes a system." **False.** Too much gain can push closed-loop poles into the RHP (Example 3 of lecture text: audio feedback squeal).

**P9.** "Phase margin $60°$ $\Rightarrow$ stable." **True** (assuming only one gain-crossover frequency and stable open loop). A positive phase margin means the Nyquist curve does not encircle $-1$.

**P10.** "A Nyquist plot is constructed by evaluating $G(j\omega)H(j\omega)$ and plotting in the complex plane." **True.**

---

*End of master sample problems document.*
