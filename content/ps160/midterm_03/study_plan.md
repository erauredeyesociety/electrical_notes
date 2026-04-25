# PS160 --- Midterm 3 (Final) Study Plan

**Exam context:** Comprehensive final, with **emphasis on Ch 33-36** (EM waves, geometric optics, interference, diffraction). Knowledge-question section will likely pull equations from the entire course. Problem section will be weighted toward the optics half.

**Inventory of available study materials** (in `ps160/`):

### Converted references (use these first)
- **Equation sheets**
  - [../midterm_01/equations.tex](../midterm_01/equations.tex) --- M12-M16 (mechanical, fluids, waves)
  - [../midterm_02/equations.tex](../midterm_02/equations.tex) --- M17-M20 (thermo)
  - [equations.tex](equations.tex) --- M33-M36 (optics, EM)
  - [master_equations.tex](master_equations.tex) --- all of the above in one document
- **Reviews (theory walkthroughs)**
  - [../midterm_01/review.md](../midterm_01/review.md)
  - [../midterm_02/review.md](../midterm_02/review.md)
  - [review.md](review.md)
- **Topics index**
  - [master_topics.md](master_topics.md)

### Source materials (originals)
- Official knowledge-question PDFs:
  - `../midterm_01/knowledge_ps160_mid01.pdf` (fluids, oscillations, waves, sound)
  - `../midterm_02/knowledge_ps160_mid02.pdf` (thermo)
- **Practice finals (highest-value resource — solve under exam conditions):**
  - [test_finalexam_DRAFT_ps160_2024_fall.pdf](test_finalexam_DRAFT_ps160_2024_fall.pdf) — 33 questions (Q1-10 knowledge, Q11-33 calculation), 230/271 best-score grading. Has answer key.
  - [test_final_ps160_2024_fall_answers.pdf](test_final_ps160_2024_fall_answers.pdf) — answers for the Fall calculation questions Q11-33.
  - [test_finalexam_ps160_2024_spring.pdf](test_finalexam_ps160_2024_spring.pdf) — 26 calculation questions, 250/300, no answer key (verify against agent-generated solutions).
  - Solutions (generated separately): `../MEs/solutions/midterm03_fall2024_practice_solutions.md` and `../MEs/solutions/midterm03_spring2024_practice_solutions.md`.
- Past exams (great problem practice):
  - `../midterm_01/MT1_make_up.pdf`
  - `../midterm_01/Worked Problems.pdf`
  - `../midterm_02/Midterm_2_sp_24.pdf`
  - `../midterm_02/Study_guide_mt2.pdf`
- Module-level content (PDFs + converted .md versions in each `mXX/` folder):
  - `m12/`, `m14/`, `m15/`, `m16/` --- fluids, oscillations, waves, sound
  - `m17/`, `m18/`, `m19/`, `m20/` --- thermo
  - `m33,34,35,36/` --- EM waves + optics + interference + diffraction (especially `M33-36_Review.pdf` / `.md`)
- Module exercise banks (HTML originals + LaTeX conversions in `MEs/tex/`):
  - `ME12`-`ME36`: main module exercises
  - `MQ12a/b`-`MQ36`: pop-quiz banks
  - `midterm1_v1`, `midterm2_v2`, `midterm3_final_v1`: sample midterms

---

## Practice-final-driven prep (highest-priority track)

**TL;DR:** The two practice finals (Fall 2024, Spring 2024) are now the single best predictor of exam content. Anchor the schedule around them.

Order of operations:

1. **Top priority — Fall 2024 practice under exam conditions.** Set a 2-hour timer (or whatever the exam window is). Closed book except the equation sheet and a calculator. Do *not* peek at the answer key. Then check against [test_final_ps160_2024_fall_answers.pdf](test_final_ps160_2024_fall_answers.pdf) and the agent-generated walkthrough at `../MEs/solutions/midterm03_fall2024_practice_solutions.md`.
2. **Second — Spring 2024 practice.** No official answer key. Solve cold, then verify each problem against your own work plus `../MEs/solutions/midterm03_spring2024_practice_solutions.md`.
3. **Memorize-formulas day.** The Fall exam's first 21 points are pure formula-write (Q1-10, all optics). These are *free points if you've memorized the equation sheet* — schedule a dedicated day for blank-page recall before either practice attempt.

### Coverage analysis from the practice finals

See [review.md § Practice Final Coverage Analysis](review.md#practice-final-coverage-analysis) for the full breakdown.

Topic priorities derived from the practice exams:

- **High frequency (drill hard):** wave-function diagnostic (20 pts each exam), ideal gas combined law, water-freezing entropy, two-mirror corner, concave-mirror image (20 pts), thin-film bubble, double-slit fringe geometry, Rayleigh telescope, Doppler.
- **Medium frequency:** Bernoulli, pendulum period, calorimetry, latent heat, $K_{tr}$, isothermal/adiabatic processes, Snell's law, Carnot.
- **Low frequency in practice (don't skip, but don't over-invest):** EM waves (M33), Brewster, Malus calculation, lensmaker's, two-lens system, microscope/telescope, gratings, Michelson.

### Weak-spot suggestions (revise based on practice scores)

- If you bomb optics knowledge (Q1-10): reread [review.md § Module 34](review.md#module-34--geometric-optics) and § 35 carefully and re-memorize equations.
- If you bomb the wave function (Q15): re-derive parts a-j from scratch — the relations ($\omega = 2\pi f$, $k = 2\pi/\lambda$, $v = \omega/k$, $v_{y,\max} = \omega A$, $v_y(x,t) = -A\omega\sin(kx-\omega t + \phi)$) are all on the equation sheet but you must know how to chain them.
- If you bomb thermo: rebuild the process table (W, Q, ΔU for isobaric/isochoric/isothermal/adiabatic) — that single table answers Q22, Q24, Q25 of Fall.
- If you bomb buoyancy / Bernoulli (Q11, Q12): work `../midterm_01/Worked Problems.pdf` fluids problems again. The "ice slab supports woman" type (Fall Q11) is novel — see review.md § Novel question types.

---

## Study schedule (~2 weeks before the exam)

Adjust pace based on how much time you have; at minimum compress this into one weekend.

### Week 1 --- Rebuild the foundations

**Day 1 (Mon) --- Fluids + Oscillations (M12, M14)**
- Read [../midterm_01/review.md](../midterm_01/review.md) sections 12 and 14
- Memorize fluids + SHM formulas (9-10 total) from [../midterm_01/equations.tex](../midterm_01/equations.tex)
- Practice: 3-4 problems from `midterm_01/Worked Problems.pdf` on fluids; work through `MEs/tex/ME12_v1.tex` and `MEs/tex/ME14_v1.tex`
- Write out the knowledge questions for fluids and oscillations without notes (see knowledge PDF)

**Day 2 (Tue) --- Waves + Sound (M15, M16)**
- Read [../midterm_01/review.md](../midterm_01/review.md) sections 15 and 16
- Memorize wave/sound formulas
- Practice: `MEs/tex/ME15_v1.tex`, `MEs/tex/ME16_v1.tex`, `MEs/tex/midterm1_v1.tex`
- Drill the knowledge questions for waves and sound
- Check your answers against `midterm_01/knowledge_ps160_mid01.pdf`

**Day 3 (Wed) --- Temperature + Heat (M17)**
- Read [../midterm_02/review.md](../midterm_02/review.md) section 17
- Practice: `MEs/tex/ME17_v1.tex`, MQs 17a, 17b
- Calorimetry problems from worked-problems set

**Day 4 (Thu) --- Kinetic theory (M18)**
- Read review section 18
- Memorize the $v_{\text{rms}}$, equipartition, Maxwell-Boltzmann story
- Practice: `MEs/tex/ME18_v1.tex`, MQs 18a, 18b
- Don't skip equipartition: degrees-of-freedom problems are easy points.

**Day 5 (Fri) --- First law, processes, $pV$ diagrams (M19)**
- Read review section 19
- Walk through the four canonical processes (isobaric, isochoric, isothermal, adiabatic), for each compute $Q$, $W$, $\Delta U$ on a generic ideal gas
- Practice: `MEs/tex/ME19_v1.tex`, MQs 19a, 19b
- Pick two different cycles (e.g. the ones in the MEs) and tabulate $Q$, $W$, $\Delta U$ leg-by-leg

**Day 6 (Sat) --- Second law, entropy, cycles (M20)**
- Read review section 20
- Memorize Carnot efficiency and the COP formulas
- Practice: `MEs/tex/ME20_v1.tex`, MQs 20a, 20b
- Take `MEs/tex/midterm2_v2.tex` as a timed practice exam; compare against `midterm_02/Midterm_2_sp_24.pdf`

**Day 7 (Sun) --- Review day 1. Rest or catch-up**
- Re-derive anywhere you stumbled earlier in the week
- Blank-page test: rewrite the full midterm 1 and midterm 2 equation sheets from memory; compare against the `.tex` files

### Week 2 --- Focus on the new material (Ch 33-36)

**Day 8 (Mon) --- EM waves (M33)**
- Read [review.md](review.md) section 33 thoroughly --- this is high-value because it's both new and load-bearing for M34-M36
- Memorize every equation in [equations.tex](equations.tex) § Electromagnetic Waves
- Conceptual: "Why is $E/B = c$?" and "Why does the Poynting vector point in the direction of propagation?" --- be able to say this out loud
- Practice: `MEs/tex/ME33_v1.tex`, `MEs/tex/MQ33a_v1.tex`, `MEs/tex/MQ33b_v1.tex`
- Classic 3-polarizer problem (see review Common Problem Archetypes)
- Work the relevant problems from `m33,34,35,36/M33-36_Review.pdf`

**Day 9 (Tue) --- Geometric optics (M34)**
- Read [review.md](review.md) section 34
- Drill sign conventions for mirrors and lenses until they're reflex
- Practice: `MEs/tex/ME34_v1.tex`, `MEs/tex/MQ34a_v1.tex`, `MEs/tex/MQ34b_v1.tex`
- Draw ray diagrams by hand for: converging lens with object outside $2f$, inside $f$, at $f$; diverging lens; concave mirror; convex mirror
- Two-lens systems (microscope, telescope) --- especially watch the sign of $s_2$

**Day 10 (Wed) --- Interference (M35)**
- Read [review.md](review.md) section 35
- Memorize the two-source and thin-film conditions
- Practice: `MEs/tex/ME35-36_v1.tex` (interference portion), `MEs/tex/MQ35_v1.tex`
- Thin-film reflection phase shift: work out 3 examples (soap film in air, oil on water, AR coating on glass)

**Day 11 (Thu) --- Diffraction (M36)**
- Read [review.md](review.md) section 36
- Single-slit, gratings, Rayleigh --- derive the $d\sin\theta = m\lambda$ rule for the grating from scratch
- Practice: `MEs/tex/ME35-36_v1.tex` (diffraction portion), `MEs/tex/MQ36_v1.tex`
- Combined double-slit + envelope problem, including "missing orders"
- Bragg's law X-ray problem

**Day 11.5 (Thu evening) --- Memorize-formulas day**
- The Fall 2024 practice final's first 21 points (Q1-10) are *pure formula-write* on optics. These are easy points if you've memorized — and zero points if you haven't.
- Closed-book blank-page test: write out the 10 optics formulas asked for: Snell + reflection law, $n=c/v$ + $\lambda_n = \lambda_0/n$, critical angle + Brewster, lens/mirror equation + $m = -s'/s$, lensmaker's + small-angle, Malus + magnifier angular magnification, phase difference $\Delta\phi = (2\pi/\lambda)\Delta L$, double-slit + grating constructive ($d\sin\theta = m\lambda$), two-source intensity $I = I_0\cos^2(\phi/2)$, thin-film $\Delta L = 2nt$ + Rayleigh $\sin\theta = 1.22\lambda/D$.
- Compare against [equations.tex](equations.tex) and [master_equations.tex](master_equations.tex) and re-drill anything you missed.

**Day 12 (Fri) --- Simulated final #1: Fall 2024 practice (closed book, timed)**
- Take [test_finalexam_DRAFT_ps160_2024_fall.pdf](test_finalexam_DRAFT_ps160_2024_fall.pdf) cold. Equation sheet + calculator only.
- Time yourself for the actual exam window. Best 230/271, so you can drop ~4 problems strategically.
- After the timer: check answers against [test_final_ps160_2024_fall_answers.pdf](test_final_ps160_2024_fall_answers.pdf) and `../MEs/solutions/midterm03_fall2024_practice_solutions.md`.
- Mark every problem you missed or were unsure of.

**Day 13 (Sat) --- Simulated final #2: Spring 2024 practice + targeted fix-up**
- Morning: take [test_finalexam_ps160_2024_spring.pdf](test_finalexam_ps160_2024_spring.pdf) cold. No official answer key — when checking, use your own work plus `../MEs/solutions/midterm03_spring2024_practice_solutions.md`.
- Afternoon: re-drill any concept you missed on either practice final. Use [review.md](review.md) and the source PDFs.
- Re-take the missed problems from scratch without notes.
- Pay special attention to the *novel* problem types flagged in [review.md § Novel question types](review.md#novel-question-types-not-previously-encountered-in-this-users-prep-materials): ice-slab buoyancy, max transverse speed, finding $L_f$, $v_{rms}$ after constant-V heat.

**Day 14 (Sun) --- Rest + skim**
- Light review: skim all three `equations.tex` sheets and [master_topics.md](master_topics.md)
- Make sure you know the physical constants in `master_equations.tex` § Physical Constants
- Re-skim the 10 optics formulas from Day 11.5 — these are guaranteed points
- Sleep well the night before

---

## Priority equations to drill (if you have only 30 minutes)

In this order --- highest expected-value first:

1. Maxwell's-equation-derived basics: $c = 1/\sqrt{\mu_0\varepsilon_0}$, $E/B = c$, $I = \tfrac{1}{2}c\varepsilon_0 E_{\max}^2$
2. Snell's law + critical angle + Brewster's angle
3. Mirror/lens equation + magnification, + sign convention
4. Two-source + thin-film interference conditions
5. $a\sin\theta = m\lambda$ (single-slit minimum), $d\sin\theta = m\lambda$ (grating/double-slit max)
6. Rayleigh $1.22\lambda/D$
7. Carnot efficiency $1 - T_C/T_H$
8. First law with process table ($W$, $Q$, $\Delta U$ for each process)
9. Ideal gas law + $v_{\text{rms}}$
10. Doppler + beat
11. Standing-wave formulas $f_n = nv/(2L)$ and $nv/(4L)$
12. Bernoulli + continuity
13. Pendulum/spring $\omega$ formulas

---

## Common traps to watch for

- **Sign of $m$ in mirror/lens:** The sign of $m = -s'/s$ tells you if the image is inverted. Don't forget the minus sign.
- **Single-slit $m = 0$ is a maximum, not a minimum.** The $a\sin\theta = m\lambda$ formula starts at $m = 1$.
- **Thin-film phase shift:** count the number of hard reflections (low-$n$ to high-$n$). An odd number flips the rule.
- **Doppler sign convention:** verify by sanity-checking: "listener running toward source should see higher frequency".
- **Ideal gas $\Delta U = nC_V\Delta T$ holds for *any* process**, not just isochoric. You still need the $nC_V$ not $nC_P$.
- **Decibel ratio:** intensity ratio, not amplitude ratio. Doubling amplitude is 4× intensity = $+6$ dB.
- **"Image on outgoing side" depends on the element type:** for a lens it's the opposite side of the object; for a mirror it's the same side.
- **Bragg's $\theta$ is measured from the plane**, not from the normal. That's the only equation in the course with that convention.
