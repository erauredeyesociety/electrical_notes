# Module 01 — Performance, CPU Time, CPI, and Amdahl's Law

**CESC 470 Computer Architecture** · Fall 2026 · Instructor: Siyao Li

Study guide for the quantitative half of Module 01 — the part that gets tested.
Every formula is cited to its source slide, and every worked example is checked.

> **Sources.** Slide numbers cite
> [`Module 01 Introduction to computer technology & ISA (1).pdf`](<../Module 01 Introduction to computer technology & ISA (1).pdf>)
> by **PDF page**, and the deck's own printed slide number where it differs.
> Course details from [`cesc_470.pdf`](../cesc_470.pdf) (syllabus).
>
> ⚠ **This deck is 62/88 pages image-only.** These notes cover what the text
> layer carries — which is, fortunately, nearly all the quantitative material.
> Diagram-only slides (the datapath drawings, the performance-growth graph) are
> noted where they matter. See
> [`../pdf_transcripts/`](../pdf_transcripts/) for the raw extraction.

**Relevant learning outcome (syllabus p2, SLO 1):** *"Evaluate the principles
and trade-offs (cost/performance, speed/flexibility) behind the design of modern
computer systems, using both qualitative and quantitative methods."*

---

## 1. Which "time" are we talking about?

The first trap. Three different quantities get loosely called "time"
*(PDF p53, slide 30)*:

| Term | Includes | Excludes |
| --- | --- | --- |
| **Elapsed time** (wall clock, response time, latency) | everything — disk, memory, I/O waits, *other programs* | nothing |
| **CPU time** | user CPU time + system CPU time | I/O waits, other programs |
| **User CPU time** ← *our focus* | only the lines of code in **your** program | OS calls, I/O waits, other programs |

$$\text{elapsed time} = \underbrace{\text{user CPU time} + \text{system CPU time}}_{\text{CPU time}} + \text{wait time}$$

**Response time vs throughput** *(PDF p52, slide 29)* — these are different goals
and can trade against each other:

- **Response time** — how long *one* job takes. An individual user's concern.
- **Throughput** — how many jobs per unit time. A systems manager's concern.

> The slide poses two questions. Upgrading a machine with a **faster processor**
> improves *both* response time and throughput. **Adding another machine** to the
> lab improves *throughput only* — no single job runs any faster.

---

## 2. Clock cycles

Execution time is counted in **cycles** *(PDF p54, slide 31)*:

$$\text{cycle time} = \frac{1}{\text{clock rate}}, \qquad
  \text{clock rate} = \frac{1}{\text{cycle time}}$$

Clock rate is in Hz (cycles/second); cycle time in seconds.

**Slide's example.** A 200 MHz clock:
$$\frac{1}{200 \times 10^{6}} = 5 \times 10^{-9}\ \text{s} = 5\ \text{ns}$$

---

## 3. The performance equation

The central formula *(PDF p55–56, slide 32)*. Read it as units cancelling:

$$\frac{\text{seconds}}{\text{program}}
= \frac{\text{cycles}}{\text{program}} \times \frac{\text{seconds}}{\text{cycle}}$$

$$\boxed{\;\text{CPU time} = \text{CPU clock cycles} \times \text{cycle time}
      = \frac{\text{CPU clock cycles}}{\text{clock rate}}\;}$$

**The design consequence** the slide draws out: to improve performance you can
only do one of two things — **reduce the cycles** a program needs, or **reduce
the cycle time** (equivalently, raise the clock rate).

### Bringing in instruction count

Not every instruction takes one cycle *(PDF p58–61, slides 33–34)*:
multiplication costs more than addition, floating point more than integer, and a
memory access more than a register access. So we introduce **CPI** — average
**C**ycles **P**er **I**nstruction:

$$\text{CPU clock cycles} = \text{instruction count} \times \text{CPI}$$

$$\boxed{\;\text{CPU time} = \text{IC} \times \text{CPI} \times \text{cycle time}\;}$$

These are the **three factors** — and they are not independent *(p61)*: changing
the cycle time usually means changing the hardware, which changes how many cycles
instructions need.

When instructions fall into classes with different costs, CPI is a weighted
average:

$$\text{CPI} = \frac{\sum_{i} (\text{CPI}_i \times C_i)}{\sum_i C_i}
  \qquad C_i = \text{count of class } i$$

**Vocabulary check** *(PDF p77, slide 44)*: cycle time (s/cycle), clock rate
(cycles/s), CPI (cycles/instruction), MIPS (millions of instructions/s). A
floating-point-heavy program has a *higher* CPI; a program of simple
instructions scores *higher* MIPS.

---

## 4. Worked examples

### Example 1 — Target clock rate *(PDF p67, slide 36)*

> Our favourite program runs in **10 s** on computer **A**, which has a **400 MHz**
> clock. We want machine **B** to run it in **6 s**. The faster technology forces
> a design change making B need **1.2×** as many clock cycles as A. What clock
> rate should we target?

**Step 1 — cycles on A.** Rearrange the performance equation:
$$\text{cycles}_A = \text{CPU time}_A \times \text{clock rate}_A
 = 10\ \text{s} \times 400\times10^{6}\ \text{Hz} = 4.0\times10^{9}$$

**Step 2 — cycles on B.** Given, B needs 1.2× as many:
$$\text{cycles}_B = 1.2 \times 4.0\times10^{9} = 4.8\times10^{9}$$

**Step 3 — required rate.**
$$\text{clock rate}_B = \frac{\text{cycles}_B}{\text{CPU time}_B}
= \frac{4.8\times10^{9}}{6\ \text{s}} = 800\times10^{6}\ \text{Hz}$$

> **Answer: 800 MHz.** Note it is **not** simply $400 \times \frac{10}{6} = 667$ MHz —
> the 1.2× cycle penalty has to be paid for as well. Missing that penalty is the
> intended trap.

---

### Example 2 — Relative performance *(PDF p70, slide 38)*

> If computer A runs a program in **10 s** and computer B runs the same program in
> **15 s**, how much faster is A than B?

Performance is the reciprocal of execution time, so the ratio inverts:

$$\frac{\text{performance}_A}{\text{performance}_B}
= \frac{\text{time}_B}{\text{time}_A} = \frac{15}{10} = 1.5$$

> **Answer: A is 1.5× faster than B.** Always divide the *slower* time by the
> *faster* time — a ratio below 1 means you inverted it.

---

### Example 3 — Elapsed vs user CPU time *(PDF p70, slide 38)*

> A task runs alone. It runs **5 ms**, waits **4 ms** while the OS runs disk-access
> instructions, the CPU is **idle 2 ms** waiting for data, then it runs **10 ms**
> and completes.

Sort each interval into the right bucket:

| Interval | Duration | Kind |
| --- | ---: | --- |
| task running | 5 ms | user CPU |
| OS running disk-access instructions | 4 ms | **system** CPU |
| CPU idle, waiting on disk | 2 ms | wait |
| task running | 10 ms | user CPU |

$$\text{elapsed} = 5+4+2+10 = \mathbf{21\ ms}$$
$$\text{user CPU time} = 5+10 = \mathbf{15\ ms}$$

> **Answers: elapsed = 21 ms, user CPU time = 15 ms.**
>
> ⚠ The 4 ms of OS work is **system** CPU time — real CPU work, but not *yours*.
> It counts toward **CPU time** (15+4 = 19 ms) but **not** user CPU time. The
> 2 ms idle counts toward neither. Sorting these three buckets is the whole point
> of the question.

---

### Example 4 — CPI comparison, same ISA *(PDF p73–74, slides 40–41)*

> Two implementations of the **same ISA**. Machine A: cycle time **10 ns**, CPI
> **2.0**. Machine B: cycle time **20 ns**, CPI **1.2**. Which is faster, and by
> how much?

Per instruction, $\text{CPU time} = \text{CPI} \times \text{cycle time}$:

$$\text{A} = 2.0 \times 10\ \text{ns} = 20\ \text{ns/instruction}$$
$$\text{B} = 1.2 \times 20\ \text{ns} = 24\ \text{ns/instruction}$$

$$\frac{24}{20} = 1.2$$

> **Answer: A is faster, by 1.2×.**
>
> **The follow-up question matters:** if two machines share the same ISA running
> the same program, the **instruction count is always identical** — the ISA
> defines the instructions, so the same compiled program issues the same ones.
> Clock rate, CPI, and execution time may all differ. That is exactly why
> instruction count cancels here and comparing $\text{CPI} \times \text{cycle time}$
> alone is valid.

---

### Example 5 — Choosing a code sequence *(PDF p75–76, slides 42–43)*

> Three instruction classes costing **A = 1**, **B = 2**, **C = 3** cycles.
> Sequence 1 has 5 instructions: **2×A, 1×B, 2×C**.
> Sequence 2 has 6 instructions: **4×A, 1×B, 1×C**.
> Which is faster, by how much, and what is each CPI?

**Sequence 1:**
$$\text{cycles} = (2)(1) + (1)(2) + (2)(3) = 2 + 2 + 6 = 10,
\qquad \text{CPI} = \tfrac{10}{5} = 2.0$$

**Sequence 2:**
$$\text{cycles} = (4)(1) + (1)(2) + (1)(3) = 4 + 2 + 3 = 9,
\qquad \text{CPI} = \tfrac{9}{6} = 1.5$$

Same machine ⇒ same cycle time, so cycles alone decide:

$$\frac{10}{9} \approx 1.11$$

> **Answer: Sequence 2 is faster by ≈1.11× (10/9); CPI = 2.0 and 1.5.**
>
> ⚠ **Sequence 2 has MORE instructions (6 vs 5) and is still faster.** Instruction
> count alone never decides — this is the whole reason CPI exists. Beware "fewer
> instructions must be faster" and beware comparing CPI alone (1.5 < 2.0 happens
> to agree here, but on different instruction counts it need not).

---

### Example 6 — Amdahl's law *(PDF p86–87, slides 49–50)*

$$\boxed{\;\text{execution time after} =
\text{time}_{\text{unaffected}} + \frac{\text{time}_{\text{affected}}}{n}\;}$$

> A program runs in **100 s**, of which **multiply** accounts for **80 s**. How much
> must multiplication speed up to make the program **4×** faster? What about **5×**?

**4× faster** means a target of $100/4 = 25$ s. Unaffected time is
$100 - 80 = 20$ s:

$$20 + \frac{80}{n} = 25 \;\Longrightarrow\; \frac{80}{n} = 5
  \;\Longrightarrow\; n = 16$$

**5× faster** means a target of $100/5 = 20$ s:

$$20 + \frac{80}{n} = 20 \;\Longrightarrow\; \frac{80}{n} = 0$$

> **Answers: 4× requires multiplication to be 16× faster. 5× is IMPOSSIBLE.**
>
> Even with infinitely fast multiplication the program still takes the
> untouched 20 s, so 5× (=20 s) is the unreachable limit. **The unaffected
> fraction sets a hard ceiling** — this is the core lesson, and the design
> principle it motivates: *make the common case fast* *(p86)*.

---

### Example 7 — Try it yourself *(PDF p88, slide 51)*

> Floating-point instructions are made **twice as fast**, but only **10%** of the
> time was originally spent on them. How much faster is the new machine?

Take total time as 1: unaffected 0.9, affected 0.1, $n=2$.

$$\text{new time} = 0.9 + \frac{0.1}{2} = 0.95
\qquad\Rightarrow\qquad
\text{speedup} = \frac{1}{0.95} \approx 1.0526$$

> **Answer: ≈1.05× — about a 5% improvement**, from doubling the speed of
> something that was 10% of the workload. Amdahl's law again: optimising the
> uncommon case buys almost nothing.

---

## 5. Qualitative material likely to appear

**Classes of computers** *(PDF p8)* — personal/desktop (good performance to a
single user at low cost), plus server, embedded, and warehouse-scale classes.

**Von Neumann / stored-program computer** *(PDF p16–17)* — programs are bit
sequences *just like data*, so both live in the same memory. The five classic
components *(p13, diagram)*: **Control Unit**, **Datapath** (ALU + registers) —
together the **CPU** — plus **Memory**, **Input**, and **Output**, connected by a
common address/data/control **bus**.

**ISA vs organization** *(PDF p23–31)*:

- **ISA** — "the abstract interface between hardware and the lowest-level
  software" *(p23)*; the programmer-visible contract: instructions, registers,
  addressing modes, data types.
- **Organization** — how that contract is *implemented* in hardware.
- $\text{computer architecture} = \text{ISA} + \text{hardware organization}$ *(p29)*.
- One ISA, many organizations — exactly the premise of Example 4.

**Why high-level languages** *(PDF p36–37)* — productivity, portability across
ISAs, and compiler optimisation, at the cost of distance from the hardware.

**Execution cycle** *(PDF p38)* — fetch → decode → execute → memory → writeback.

**Performance enhancement methods** *(PDF p82, slide 46)* — make the common case
fast; parallelism; prediction (guess and start work early, provided
misprediction recovery is cheap and accuracy is high); fast memory via caching.

**The multicore turn** *(PDF p85, slide 48)* — power limits ended clock scaling.
Since 2002 single-program response-time improvement fell from ~1.5×/year to
<1.2×/year, pushing everyone to multiple cores per chip. The slide's 2011 table:

| | AMD Barcelona | Intel Nehalem | IBM Power 6 | Sun Niagara 2 |
| --- | --- | --- | --- | --- |
| Cores/chip | 4 | 4 | 2 | 8 |
| Clock rate | 2.5 GHz | ~2.5 GHz | 4.7 GHz | 1.4 GHz |
| Power | 120 W | ~100 W | ~100 W | 94 W |

*(Note the deck's own figures are dated — it says "in 2011". The trend is the point.)*

---

## 6. Formula sheet

$$\text{CPU time} = \text{IC} \times \text{CPI} \times \text{cycle time}
 = \frac{\text{IC} \times \text{CPI}}{\text{clock rate}}$$

$$\text{cycle time} = \frac{1}{\text{clock rate}} \qquad
\text{CPI} = \frac{\text{total cycles}}{\text{IC}} \qquad
\text{CPI}_{\text{avg}} = \frac{\sum_i \text{CPI}_i C_i}{\sum_i C_i}$$

$$\text{speedup} = \frac{\text{time}_{\text{old}}}{\text{time}_{\text{new}}}
\qquad
\text{MIPS} = \frac{\text{IC}}{\text{execution time} \times 10^{6}}$$

$$\text{Amdahl:}\quad \text{time}_{\text{new}} =
\text{time}_{\text{unaffected}} + \frac{\text{time}_{\text{affected}}}{n}
\qquad
\text{speedup}_{\max} = \frac{1}{\text{fraction}_{\text{unaffected}}}$$

### Traps, collected

1. **Ratios invert.** Performance is 1/time, so A-vs-B speedup is $t_B/t_A$.
2. **A cycle-count penalty must be paid for** (Example 1: 800 MHz, not 667).
3. **More instructions can still be faster** (Example 5).
4. **User CPU ≠ CPU ≠ elapsed** (Example 3) — sort OS work and idle separately.
5. **Amdahl has a hard ceiling** — $1/\text{fraction}_{\text{unaffected}}$ (Example 6).
6. **Same ISA ⇒ same instruction count**, so it cancels (Example 4).

---

## Verification

All seven examples were recomputed independently; each matches the deck where
the deck gives an answer (Ex. 4 → 1.2×; Ex. 5 → CPI 2.0/1.5; Ex. 6 → n=16 and
5× impossible). Examples 1, 2, 3, and 7 have no printed answer in the deck —
those are derived here and shown step by step.

**Related:** [`../pdf_transcripts/`](../pdf_transcripts/) · [`README.md`](README.md)
