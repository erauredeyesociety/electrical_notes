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

**Day 12 (Fri) --- Simulated final, closed book**
- Use `MEs/tex/midterm3_final_v1.tex` as your practice final
- Time yourself; mark every problem where you're unsure
- Before checking, spend 15 minutes trying to solve anything you missed, *with* the equation sheet

**Day 13 (Sat) --- Targeted fix-up**
- Review any problem you missed on Friday's practice final
- Re-drill the corresponding concept in [review.md](review.md) and the source PDFs
- Re-take the missed problems from scratch without notes

**Day 14 (Sun) --- Rest + skim**
- Light review: skim all three `equations.tex` sheets and [master_topics.md](master_topics.md)
- Make sure you know the physical constants in `master_equations.tex` § Physical Constants
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
