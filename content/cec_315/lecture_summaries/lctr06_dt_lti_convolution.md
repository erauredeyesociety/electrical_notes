# Lecture 6 — Discrete-Time LTI Systems and the Convolution Sum

**Course:** CEC 315 — Signals and Systems (Spring 2026)
**Instructor:** Rogelio Gracia Otalvaro
**Source PDF:** `all_lectures/cec315-lctr06-dt-lti-convolution.pdf`
**Exam coverage:** Exam 1

---

**Lctr 6: Discrete-Time LTI Systems and Convolution Sum**

Rogelio Gracia Otalvaro

Spring 2026

**Focus:** Section 2.1 (Pages 76 to 96)

---

## 6.1 Introduction to LTI Systems

> **Why This Matters**
>
> Every time you hear an echo in a room, adjust the equalizer on your music, apply a filter to a photo, or use noise-cancellation headphones, **convolution** is happening behind the scenes. Understanding convolution allows you to analyze, design, and predict the behavior of these systems. This is one of the most important concepts in signal processing!

Linear Time-Invariant (LTI) systems are the central object of this course. Two key properties make them fundamentally useful:

- Many physical processes can be accurately modeled as LTI systems.
- LTI systems can be analyzed in considerable detail using a small, elegant set of tools (convolution, transfer functions, transforms).

**Examples of physical processes modeled as LTI:**

- RC/RL/RLC circuits around an operating point
- Mass–spring–damper mechanical systems
- Audio reverb and echo effects
- Communication channel models

> **The Big Idea**
>
> If we know how an LTI system responds to a single impulse, we can determine how it responds to **any** input. This is the power of the **impulse response** and **convolution**.

## 6.2 Representation of Discrete-Time Signals in Terms of Impulses

Any discrete-time signal $x[n]$ can be expressed as a linear combination of shifted unit impulses:

$$\boxed{\,x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]\,}$$

This representation is crucial because:

- For any specific value of $n$, only **one** term on the right-hand side is nonzero (the one with $k=n$).
- The term $x[k]\,\delta[n-k]$ equals $x[k]$ when $n = k$ and zero otherwise.

In other words, the formula simply says "$x[n]$ at time $n$ equals $x[n]$" — but written in a form that lets us exploit linearity and time invariance.

### 6.2.1 Reminder: The Discrete Unit Impulse Function

The discrete unit impulse (unit sample) is defined as:

$$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}$$

**Key properties:**

- **Sifting property** (involves a sum):

$$\sum_{n=-\infty}^{\infty} x[n]\,\delta[n-k] = x[k]$$

  *Intuition:* the impulse "sifts out" only the value of $x[n]$ at $n=k$.

- **Shifted impulse:** $\delta[n-k]$ is 1 at $n = k$ and 0 otherwise.

- **Identity for convolution:**

$$x[n] * \delta[n] = x[n]$$

  *Intuition:* convolving with an impulse returns the original signal (like multiplying by 1).

- **Sampling property** (multiplication, not summation):

$$x[n]\,\delta[n] = x[0]\,\delta[n]$$

  More generally: $x[n]\,\delta[n-k] = x[k]\,\delta[n-k]$.

> **Common Mistake**
>
> Don't confuse the **sifting property** (involves a sum — collapses a whole signal to a number) with the **sampling property** (involves a multiplication — produces a scaled impulse). They look similar but are different operations.

### 6.2.2 Graphical Interpretation

*[Figure 2.1: A discrete-time signal $x[n]$ decomposed into a weighted sum of shifted impulses. The top panel shows $x[n]$ as a stem plot with values $\ldots, x[-2], x[-1], x[0], x[1], x[2], \ldots$. Each subsequent panel shows one term $x[k]\,\delta[n-k]$ — a single stem at position $k$ with height $x[k]$. Adding the panels reconstructs the original signal.]*

Each term $x[k]\,\delta[n-k]$ represents the value of the signal at time $k$, "placed" at position $n = k$.

## 6.3 The Discrete-Time Unit Impulse Response

For an LTI system, if we know its response to a unit impulse $\delta[n]$, we can determine its response to **any** input.

### 6.3.1 Definition of Impulse Response

> **Definition — Impulse Response**
>
> The **unit impulse response** $h[n]$ of a discrete-time LTI system is the output when the input is the unit impulse:
>
> $$h[n] = T\{\delta[n]\}$$
>
> where $T\{\cdot\}$ represents the system transformation.

### 6.3.2 Response to Shifted Impulses

Due to **time invariance**, if the input is $\delta[n-k]$ (a shifted impulse), the output is $h[n-k]$ (a shifted impulse response):

$$T\{\delta[n-k]\} = h[n-k]$$

*[Figure 2.2: Graphical interpretation. The top panel shows an input $x[n]$ with a few nonzero samples. The middle row shows individual shifted impulse responses $h_{-1}[n], h_0[n], h_1[n]$ corresponding to the impulse at each time — all of them are identical in *shape* and differ only by a time shift. This is exactly the content of time invariance.]*

## 6.4 The Convolution Sum

### 6.4.1 Derivation Step by Step

This derivation is important — it shows **why** convolution works for LTI systems.

**Step 1: Decompose the input into impulses.**

Any input $x[n]$ can be written as a weighted sum of shifted impulses:

$$x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]$$

**Step 2: Apply the system.**

$$y[n] = T\{x[n]\} = T\!\left\{\sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]\right\}$$

**Step 3: Use LINEARITY.**

Because the system is linear, we can move the sum (and the constants $x[k]$) outside:

$$y[n] = \sum_{k=-\infty}^{\infty} x[k]\,T\{\delta[n-k]\}$$

**Step 4: Use TIME-INVARIANCE.**

Because the system is time-invariant, the response to a shifted impulse $\delta[n-k]$ is a shifted impulse response $h[n-k]$:

$$T\{\delta[n-k]\} = h[n-k]$$

**Step 5: Combine to get the convolution sum.**

$$\boxed{\,y[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]\,}$$

This is the **convolution sum** and is denoted:

$$y[n] = x[n] * h[n]$$

> **Key Insight**
>
> The convolution sum tells us: **the output of an LTI system is completely determined by its impulse response $h[n]$.** If you know $h[n]$, you can find the output for any input!

### 6.4.2 Two Ways to Interpret Convolution

**Interpretation 1 — Sum of Echoes (Input-Side View).**

Think of each input sample $x[k]$ as triggering its own "echo" of the impulse response. The output is the sum of all these echoes:

- Input $x[0]$ triggers response $x[0]\,h[n]$ (starting at $n=0$).
- Input $x[1]$ triggers response $x[1]\,h[n-1]$ (starting at $n=1$).
- Input $x[2]$ triggers response $x[2]\,h[n-2]$ (starting at $n=2$).
- … and so on.

The overall output is the superposition of all these echoes.

*[Figure 2.3: Shows $h[n]$, an input $x[n]$ with $x[0]=0.5$ and $x[1]=2$, the two echoes $0.5\,h[n]$ and $2\,h[n-1]$, and their sum $y[n]$.]*

**Interpretation 2 — Flip-and-Slide (Computational View).**

To compute $y[n]$ for a specific value of $n$:

1. **Flip:** take $h[k]$ and flip it to get $h[-k]$.
2. **Shift:** shift by $n$ to get $h[n-k]$.
3. **Multiply and sum:** multiply $x[k]$ by $h[n-k]$ for each $k$ and add up all products.

### 6.4.3 Step-by-Step Convolution Procedure

To compute $y[n] = x[n]*h[n]$:

1. **Change variable:** express both signals as functions of the dummy variable $k$: $x[k]$ and $h[k]$.
2. **Flip one signal:** flip $h[k]$ about $k=0$ to obtain $h[-k]$.
3. **Shift the flipped signal:** shift $h[-k]$ by $n$ units to get $h[n-k]$.
   - If $n > 0$: shift to the right.
   - If $n < 0$: shift to the left.
4. **Multiply point-by-point:** for each $k$, compute the product $x[k]\cdot h[n-k]$.
5. **Sum all products:** add up all products to get $y[n]$.
6. **Repeat:** do steps 3–5 for each value of $n$ you need.

*[Figure 2.4: Illustrates $h[n-k]$ as a function of $k$ for several values of $n$. As $n$ increases, the flipped-and-shifted $h$ slides to the right across $x[k]$. The green "overlap region" is where the product is nonzero.]*

> **Common Mistake**
>
> A very common mistake is forgetting to **flip** before shifting. If you just shift without flipping, you'll get the wrong answer! Remember: the argument is $h[n-k]$, **not** $h[n+k]$.

## 6.5 Examples of Convolution

### 6.5.1 Worked Example: Computing Convolution Step by Step

Let's compute $y[n] = x[n]*h[n]$ for:

$$x[n] = \{1,2,3\}\text{ for }n=0,1,2\quad(\text{zero elsewhere})$$
$$h[n] = \{1,1\}\text{ for }n=0,1\quad(\text{zero elsewhere})$$

**Step 1: Determine the range of the output.**

> **Key Insight — Length of Convolution**
>
> If $x[n]$ has $N$ samples and $h[n]$ has $M$ samples, the output $y[n]$ has $N + M - 1$ samples.

Here $N=3$, $M=2$, so $y[n]$ has $3+2-1 = 4$ samples. The output ranges from $n=0$ (first nonzero of $x$ plus first nonzero of $h$, $= 0+0$) to $n=3$ (last nonzero of $x$ plus last nonzero of $h$, $= 2+1$).

**Step 2: Compute each output sample.** Use $y[n] = \sum_k x[k]\,h[n-k]$.

For $n=0$:

$$y[0] = \sum_k x[k]\,h[0-k] = x[0]h[0] + x[1]h[-1] + x[2]h[-2] = (1)(1) + 0 + 0 = \mathbf{1}$$

For $n=1$:

$$y[1] = x[0]h[1] + x[1]h[0] + x[2]h[-1] = (1)(1) + (2)(1) + 0 = \mathbf{3}$$

For $n=2$:

$$y[2] = x[0]h[2] + x[1]h[1] + x[2]h[0] = 0 + (2)(1) + (3)(1) = \mathbf{5}$$

For $n=3$:

$$y[3] = x[0]h[3] + x[1]h[2] + x[2]h[1] = 0 + 0 + (3)(1) = \mathbf{3}$$

**Result:**

$$\boxed{\,y[n] = \{1,\,3,\,5,\,3\}\text{ for }n=0,1,2,3\,}$$

*[Figure: Stem plot of $x[n]=\{1,2,3\}$, $h[n]=\{1,1\}$, and the convolution result $y[n]=\{1,3,5,3\}$, with additional panels showing the flip-and-slide overlap for each output sample.]*

> **Key Insight — Sanity Check**
>
> The sum of all input samples times the sum of all impulse response samples should equal the sum of all output samples:
>
> $$(1+2+3)\times(1+1) = 6\times 2 = 12$$
>
> $$1 + 3 + 5 + 3 = 12\;\checkmark$$
>
> This is a quick and useful sanity check for your calculations!

### 6.5.2 Example: Convolution with a Decaying Exponential

Consider $x[k] = \alpha^k\,u[k]$ (a right-sided decaying exponential with $|\alpha|<1$) and $h[n] = u[n]$ (a unit step). The convolution sum becomes a finite/geometric sum that evaluates to:

$$y[n] = \sum_{k=0}^{n} \alpha^k = \frac{1 - \alpha^{n+1}}{1 - \alpha}\,u[n]$$

*[Figure 2.6 & 2.7: Graphical interpretation of the flip-and-shift for this example, and the resulting output, which starts at $y[0]=1$ and asymptotes to $\tfrac{1}{1-\alpha}$.]*

### 6.5.3 Example: Convolution with the Unit Step (Accumulator)

If $h[n] = u[n]$, then the convolution gives:

$$y[n] = x[n]*u[n] = \sum_{k=-\infty}^{n} x[k]$$

This represents the **accumulation** (running sum) of the input signal.

**Why?** Since $u[n-k] = 1$ for all $k \leq n$ and $u[n-k] = 0$ for $k > n$:

$$y[n] = \sum_{k=-\infty}^{\infty} x[k]\,u[n-k] = \sum_{k=-\infty}^{n} x[k]\cdot 1$$

**Example:** If $x[n] = \{1,2,3\}$ for $n=0,1,2$:

$$y[0] = 1, \quad y[1] = 1+2 = 3, \quad y[2] = 1+2+3 = 6, \quad y[3] = 6\;(\text{stays at } 6)$$

### 6.5.4 Example: Convolution with a Shifted Impulse (Delay)

If $h[n] = \delta[n - n_0]$ (a shifted impulse), then:

$$y[n] = x[n]*\delta[n-n_0] = x[n-n_0]$$

The output is simply the input **delayed** by $n_0$ samples. This is why $\delta[n-n_0]$ is called a "delay element."

## 6.6 Properties of the Convolution Sum

These properties are extremely useful for simplifying calculations and understanding system interconnections.

### 6.6.1 Commutativity

$$x[n]*h[n] = h[n]*x[n]$$

**Meaning:** you can flip either signal when computing convolution — the result is the same. This is useful because you can choose to flip whichever signal is simpler.

### 6.6.2 Associativity

$$(x[n]*h_1[n])*h_2[n] = x[n]*(h_1[n]*h_2[n])$$

**Meaning:** for **cascade (series)** connections of LTI systems, the order doesn't matter, and you can combine the impulse responses first:

$$h_{\text{equivalent}}[n] = h_1[n]*h_2[n]$$

*[Figure: Block diagram. Two LTI systems in series $h_1 \to h_2$ are equivalent to a single LTI system with $h_1 * h_2$.]*

### 6.6.3 Distributivity

$$x[n]*(h_1[n] + h_2[n]) = x[n]*h_1[n] + x[n]*h_2[n]$$

**Meaning:** for **parallel** connections of LTI systems, you can add the impulse responses:

$$h_{\text{equivalent}}[n] = h_1[n] + h_2[n]$$

*[Figure: Block diagram. Two LTI systems in parallel with outputs summed are equivalent to a single LTI system with $h_1 + h_2$.]*

### 6.6.4 Identity Element

$$x[n]*\delta[n] = x[n]$$

**Meaning:** convolving with $\delta[n]$ leaves the signal unchanged (like multiplying by 1).

### 6.6.5 Shift Property

$$x[n]*\delta[n - n_0] = x[n - n_0]$$

**Meaning:** convolving with a shifted impulse delays the signal by $n_0$ samples.

## 6.7 Summary and Key Formulas

| Concept | Formula / Definition |
|---|---|
| Signal decomposition | $x[n] = \sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]$ |
| Impulse response | $h[n] = T\{\delta[n]\}$ |
| Convolution sum | $y[n] = x[n]*h[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]$ |
| Output length | $x[n]$ has $N$ samples and $h[n]$ has $M$ samples $\Rightarrow y[n]$ has $N+M-1$ samples |
| Commutativity | $x[n]*h[n] = h[n]*x[n]$ |
| Associativity | $(x*h_1)*h_2 = x*(h_1*h_2)$ |
| Distributivity | $x*(h_1 + h_2) = x*h_1 + x*h_2$ |
| Identity | $x[n]*\delta[n] = x[n]$ |

## 6.8 Common Mistakes to Avoid

1. **Forgetting to flip:** the most common error! Remember: $h[n-k]$ means flip $h[k]$ **first**, then shift.
2. **Wrong limits:** when computing the sum, only include terms where **both** $x[k]$ and $h[n-k]$ are nonzero.
3. **Confusing $n$ and $k$:**
   - $n$ is the output time index (the variable you're solving for).
   - $k$ is the dummy summation variable.
4. **Forgetting signal supports:** always identify where each signal is nonzero before computing.
5. **Sign errors with shifts:** $h[n-k]$ for $n=3$ and $k=1$ gives $h[3-1] = h[2]$, not $h[-2]$ or $h[4]$.

> **Key Insight — Sanity Check**
>
> Always verify that $\sum_n y[n] = \left(\sum_n x[n]\right)\cdot\left(\sum_n h[n]\right)$. If this doesn't hold, you made an error somewhere!

Rogelio Gracia Otalvaro

---

## Practice Problems Summary

1. **Signal decomposition:** Express $x[n] = \{\ldots, x[-1], x[0], x[1], \ldots\}$ as $\sum_k x[k]\,\delta[n-k]$. This is the foundation for deriving convolution.
2. **Derivation of convolution sum:** Apply linearity and time invariance to the decomposed input to obtain $y[n] = \sum_k x[k]\,h[n-k]$.
3. **Worked Example 6.5.1:** Convolve $x[n]=\{1,2,3\}$ with $h[n]=\{1,1\}$. Result: $y[n] = \{1,3,5,3\}$ for $n=0,1,2,3$. Sanity check: $6 \times 2 = 12 = 1+3+5+3$. $\checkmark$
4. **Decaying exponential example:** $\alpha^n u[n] * u[n] = \frac{1-\alpha^{n+1}}{1-\alpha}\,u[n]$, which asymptotes to $1/(1-\alpha)$.
5. **Accumulator example:** $x[n]*u[n] = \sum_{k=-\infty}^{n} x[k]$ — convolving with a unit step produces the running sum.
6. **Delay example:** $x[n]*\delta[n-n_0] = x[n-n_0]$, illustrating the shift/delay property.
7. **Cascade property:** For two LTI systems in series, $h_{\text{eq}} = h_1 * h_2$ (apply associativity).
8. **Parallel property:** For two LTI systems in parallel, $h_{\text{eq}} = h_1 + h_2$ (apply distributivity).
