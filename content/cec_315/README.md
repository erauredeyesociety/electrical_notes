# CEC 315 — Signals and Systems

Course materials, notes, summaries, and exam prep for CEC 315 (Signals and Systems). The folder has been reorganized into self-contained per-exam directories plus shared resource folders (master documents, lecture summaries in Markdown and LaTeX, original lecture PDFs, homework, and practice problems).

Syllabus: [CEC315_2026_Syllabus.pdf](CEC315_2026_Syllabus.pdf)

---

## Folder Map

```
cec_315/
├── README.md                        <- this file
├── CEC315_2026_Syllabus.pdf         <- course syllabus
│
├── exam1/                           <- self-contained Exam 1 bundle (lectures 2-8)
│   ├── CEC_315_exam_1.pdf
│   ├── exam1_study_guide.md
│   ├── lectures/                    <- lecture PDFs 02-08
│   └── summaries/                   <- markdown summaries for lectures 02-04
│
├── exam2/                           <- self-contained Exam 2 bundle (lectures 9-15)
│   ├── cec315-EXAM2-1.pdf
│   ├── cec315-study-guide-lctrs9-15.pdf
│   ├── cheatsheet.md
│   ├── equations.md
│   ├── exam2_solutions.md
│   ├── study_guide_summary.md
│   ├── topics.md
│   ├── nblm_1.md
│   ├── part2_prob1.md
│   ├── hw_lctr9_11_solutions_summary.md
│   ├── hw_lctr12_15_solutions_summary.md
│   ├── examples/                    <- 5 worked example markdowns
│   ├── lectures/                    <- lecture PDFs 09-15
│   └── summaries/                   <- markdown summaries for lectures 09-15
│
├── exam3/                           <- self-contained Exam 3 bundle (lectures 16-23)
│   ├── exam3_study_guide.md
│   ├── exam3_notes.md / .tex
│   ├── exam3_cheatsheet.md / .tex
│   ├── exam3_sample_problems.md / .tex
│   ├── lectures/                    <- lecture PDFs 16-23
│   └── summaries/                   <- markdown summaries for lectures 16-23
│
├── master_docs/                     <- canonical homework + sample problem banks (md + tex)
├── lecture_summaries/               <- all 22 lecture summaries in Markdown
├── lecture_summaries_tex/           <- all 22 lecture summaries in LaTeX (Overleaf-ready)
├── all_lectures/                    <- complete archive of lecture PDFs (02-23)
├── hw_practice_problems/            <- practice problem sets + per-lecture exercises
├── homework/                        <- submitted homework assignments with solutions
│   ├── hw1/
│   ├── hw4/
│   └── hw6/
└── summaries/                       <- chapter-level summary documents
```

---

## Exam 1 — Lectures 2–8

**Coverage:** signal definitions and transformations, complex exponentials and sinusoids, key functions and system basics, basic system properties, DT LTI convolution, CT LTI properties, differential equations and singularity functions.

**Key files in [exam1/](exam1/):**
- [exam1_study_guide.md](exam1/exam1_study_guide.md) — study guide
- [CEC_315_exam_1.pdf](exam1/CEC_315_exam_1.pdf) — original exam PDF
- [exam1/lectures/](exam1/lectures/) — lecture PDFs 02–08
- [exam1/summaries/](exam1/summaries/) — Markdown summaries for lectures 02–04

**Relevant master docs / lecture summaries:**
- [master_sample_problems.md](master_docs/master_sample_problems.md) (Exam 1 section)
- [master_homework_problems.md](master_docs/master_homework_problems.md)
- Full summaries: [lctr02](lecture_summaries/lctr02_signal_definitions_transformations.md), [lctr03](lecture_summaries/lctr03_complex_exponential_sinusoidal.md), [lctr04](lecture_summaries/lctr04_key_functions_system_basics.md), [lctr05](lecture_summaries/lctr05_basic_system_properties.md), [lctr06](lecture_summaries/lctr06_dt_lti_convolution.md), [lctr07](lecture_summaries/lctr07_ct_lti_properties.md), [lctr08](lecture_summaries/lctr08_diff_eqns_singularity.md)

---

## Exam 2 — Lectures 9–15

**Coverage:** CT Fourier series, convergence properties and DTFS, frequency response and filtering, Fourier transforms, FT properties and convolution, magnitude/phase and filters, systems and Bode plots.

**Key files in [exam2/](exam2/):**
- [cec315-EXAM2-1.pdf](exam2/cec315-EXAM2-1.pdf) — original exam PDF
- [cec315-study-guide-lctrs9-15.pdf](exam2/cec315-study-guide-lctrs9-15.pdf) — instructor study guide
- [study_guide_summary.md](exam2/study_guide_summary.md) — condensed study guide
- [topics.md](exam2/topics.md) — topic checklist
- [cheatsheet.md](exam2/cheatsheet.md) — compact formula sheet
- [equations.md](exam2/equations.md) — equation bank
- [exam2_solutions.md](exam2/exam2_solutions.md) — worked solutions
- [nblm_1.md](exam2/nblm_1.md), [part2_prob1.md](exam2/part2_prob1.md) — problem walkthroughs
- [hw_lctr9_11_solutions_summary.md](exam2/hw_lctr9_11_solutions_summary.md), [hw_lctr12_15_solutions_summary.md](exam2/hw_lctr12_15_solutions_summary.md) — homework recap
- [exam2/examples/](exam2/examples/) — 5 worked example markdowns (eigenfunctions, Gibbs, FS properties, DTFS, frequency response)
- [exam2/lectures/](exam2/lectures/), [exam2/summaries/](exam2/summaries/)

**Relevant master docs / lecture summaries:**
- [master_sample_problems.md](master_docs/master_sample_problems.md) (Exam 2 section)
- Full summaries: [lctr09](lecture_summaries/lctr09_ct_fourier_series.md), [lctr10](lecture_summaries/lctr10_convergence_properties.md), [lctr11](lecture_summaries/lctr11_frequency_response_filtering.md), [lctr12](lecture_summaries/lctr12_fourier_transforms.md), [lctr13](lecture_summaries/lctr13_ft_properties_convolution.md), [lctr14](lecture_summaries/lctr14_magnitude_phase_filters.md), [lctr15](lecture_summaries/lctr15_systems_bode.md)

---

## Exam 3 — Lectures 16–23

**Coverage:** Laplace transform and ROC, inverse Laplace and properties, system analysis via unilateral Laplace, z-transform and ROC, inverse z-transform and properties, system analysis via unilateral z-transform, sampling, linear feedback systems.

**Key files in [exam3/](exam3/):**

- [SOLUTIONS_INDEX.md](exam3/SOLUTIONS_INDEX.md) — **one-stop jump table** for every Exam 3 solution set (homework, exercises, mock exam)
- [StudyGuide_Exam3.pdf](exam3/StudyGuide_Exam3.pdf) — **official instructor study guide PDF** (authoritative)
- [official_study_guide.md](exam3/official_study_guide.md) / [official_study_guide.tex](exam3/official_study_guide.tex) — transcribed & typeset version of the official PDF
- [exam3_study_guide.md](exam3/exam3_study_guide.md) / [exam3_study_guide.tex](exam3/exam3_study_guide.tex) — student study guide (augmented with instructor emphasis from the official guide)
- [exam3_notes.md](exam3/exam3_notes.md) / [exam3_notes.tex](exam3/exam3_notes.tex) — condensed notes
- [exam3_cheatsheet.md](exam3/exam3_cheatsheet.md) / [exam3_cheatsheet.tex](exam3/exam3_cheatsheet.tex) — one-page cheatsheet
- [exam3_sample_problems.md](exam3/exam3_sample_problems.md) / [exam3_sample_problems.tex](exam3/exam3_sample_problems.tex) — worked sample problems
- [exam3_flashcards.md](exam3/exam3_flashcards.md) / [exam3_flashcards.tex](exam3/exam3_flashcards.tex) — flashcards
- [exam3_pitfalls.md](exam3/exam3_pitfalls.md) / [exam3_pitfalls.tex](exam3/exam3_pitfalls.tex) — common pitfalls
- [exam3_practice_problems.md](exam3/exam3_practice_problems.md) / [exam3_practice_problems.tex](exam3/exam3_practice_problems.tex) — practice bank
- [mock_exam3.md](exam3/mock_exam3.md) / [mock_exam3.tex](exam3/mock_exam3.tex) + [mock_exam3_solutions.md](exam3/mock_exam3_solutions.md) / [mock_exam3_solutions.tex](exam3/mock_exam3_solutions.tex) — mock exam with solutions
- [exam3/lectures/](exam3/lectures/) — lecture PDFs 16–23
- [exam3/summaries/](exam3/summaries/) — markdown summaries for lectures 16–23

**Official homework / exercise solutions (instructor-provided, transcribed Spring 2026):**

- Laplace HW (lctr16-18): [homework/hw5/hw5_solutions.md](homework/hw5/hw5_solutions.md) / [.tex](homework/hw5/hw5_solutions.tex) — also [questions](homework/hw5/hw5_questions.md); source PDF [hw-lctr16-18-solutions.pdf](hw_practice_problems/hw-lctr16-18-solutions.pdf)
- z-transform HW (lctr19-21): [homework/hw6/hw6_official_solutions.md](homework/hw6/hw6_official_solutions.md) / [.tex](homework/hw6/hw6_official_solutions.tex); source PDF [hw-lctr19-21-solutions.pdf](hw_practice_problems/hw-lctr19-21-solutions.pdf)
- Lecture 22 sampling exercise: [lctr22-exercise-solutions.md](hw_practice_problems/lctr22-exercise-solutions.md) / [.tex](hw_practice_problems/lctr22-exercise-solutions.tex) + [source PDF](hw_practice_problems/lctr22-exercise-solutions.pdf)
- Lecture 23 feedback exercise: [lctr23-exercise-solutions.md](hw_practice_problems/lctr23-exercise-solutions.md) / [.tex](hw_practice_problems/lctr23-exercise-solutions.tex) + [source PDF](hw_practice_problems/lctr23-exercise-solutions.pdf)

**Relevant master docs / lecture summaries:**
- [master_sample_problems.md](master_docs/master_sample_problems.md) (Exam 3 section)
- [master_homework_problems.md](master_docs/master_homework_problems.md) (hw-lctr16-18, hw-lctr19-21, with integrated official answers)
- Full summaries (each now cross-links to its official solutions and instructor emphases): [lctr16](lecture_summaries/lctr16_laplace_transform_roc.md), [lctr17](lecture_summaries/lctr17_inverse_laplace_properties.md), [lctr18](lecture_summaries/lctr18_system_analysis_unilateral_laplace.md), [lctr19](lecture_summaries/lctr19_z_transform_roc.md), [lctr20](lecture_summaries/lctr20_inverse_z_transform_properties.md), [lctr21](lecture_summaries/lctr21_system_analysis_unilateral_z.md), [lctr22](lecture_summaries/lctr22_sampling.md), [lctr23](lecture_summaries/lctr23_linear_feedback_systems.md)

---

## Master Documents

Centralized problem banks spanning the entire course. Each pair (md + tex) is standalone.

| File | Description |
|---|---|
| [master_docs/master_sample_problems.md](master_docs/master_sample_problems.md) | Markdown master bank of sample/practice problems organized by exam and lecture |
| [master_docs/master_sample_problems.tex](master_docs/master_sample_problems.tex) | LaTeX version of the sample problem bank, Overleaf-ready |
| [master_docs/master_homework_problems.md](master_docs/master_homework_problems.md) | Markdown master bank of homework problems with solutions |
| [master_docs/master_homework_problems.tex](master_docs/master_homework_problems.tex) | LaTeX version of the homework problem bank, Overleaf-ready |

---

## Lecture Summaries

Every lecture has both a Markdown summary (for reading in an editor) and a standalone LaTeX version (for typeset PDF / Overleaf). Lectures 2–8 correspond to Exam 1, 9–15 to Exam 2, and 16–23 to Exam 3.

| # | Topic | Markdown | LaTeX |
|---|---|---|---|
| 02 | Signal definitions and transformations | [md](lecture_summaries/lctr02_signal_definitions_transformations.md) | [tex](lecture_summaries_tex/lctr02_signal_definitions_transformations.tex) |
| 03 | Complex exponential and sinusoidal signals | [md](lecture_summaries/lctr03_complex_exponential_sinusoidal.md) | [tex](lecture_summaries_tex/lctr03_complex_exponential_sinusoidal.tex) |
| 04 | Key functions and system basics | [md](lecture_summaries/lctr04_key_functions_system_basics.md) | [tex](lecture_summaries_tex/lctr04_key_functions_system_basics.tex) |
| 05 | Basic system properties | [md](lecture_summaries/lctr05_basic_system_properties.md) | [tex](lecture_summaries_tex/lctr05_basic_system_properties.tex) |
| 06 | DT LTI and convolution | [md](lecture_summaries/lctr06_dt_lti_convolution.md) | [tex](lecture_summaries_tex/lctr06_dt_lti_convolution.tex) |
| 07 | CT LTI properties | [md](lecture_summaries/lctr07_ct_lti_properties.md) | [tex](lecture_summaries_tex/lctr07_ct_lti_properties.tex) |
| 08 | Differential equations and singularity functions | [md](lecture_summaries/lctr08_diff_eqns_singularity.md) | [tex](lecture_summaries_tex/lctr08_diff_eqns_singularity.tex) |
| 09 | CT Fourier series | [md](lecture_summaries/lctr09_ct_fourier_series.md) | [tex](lecture_summaries_tex/lctr09_ct_fourier_series.tex) |
| 10 | Convergence properties (DTFS) | [md](lecture_summaries/lctr10_convergence_properties.md) | [tex](lecture_summaries_tex/lctr10_convergence_properties.tex) |
| 11 | Frequency response and filtering | [md](lecture_summaries/lctr11_frequency_response_filtering.md) | [tex](lecture_summaries_tex/lctr11_frequency_response_filtering.tex) |
| 12 | Fourier transforms | [md](lecture_summaries/lctr12_fourier_transforms.md) | [tex](lecture_summaries_tex/lctr12_fourier_transforms.tex) |
| 13 | FT properties and convolution | [md](lecture_summaries/lctr13_ft_properties_convolution.md) | [tex](lecture_summaries_tex/lctr13_ft_properties_convolution.tex) |
| 14 | Magnitude/phase and filters | [md](lecture_summaries/lctr14_magnitude_phase_filters.md) | [tex](lecture_summaries_tex/lctr14_magnitude_phase_filters.tex) |
| 15 | Systems and Bode plots | [md](lecture_summaries/lctr15_systems_bode.md) | [tex](lecture_summaries_tex/lctr15_systems_bode.tex) |
| 16 | Laplace transform and ROC | [md](lecture_summaries/lctr16_laplace_transform_roc.md) | [tex](lecture_summaries_tex/lctr16_laplace_transform_roc.tex) |
| 17 | Inverse Laplace and properties | [md](lecture_summaries/lctr17_inverse_laplace_properties.md) | [tex](lecture_summaries_tex/lctr17_inverse_laplace_properties.tex) |
| 18 | System analysis via unilateral Laplace | [md](lecture_summaries/lctr18_system_analysis_unilateral_laplace.md) | [tex](lecture_summaries_tex/lctr18_system_analysis_unilateral_laplace.tex) |
| 19 | z-transform and ROC | [md](lecture_summaries/lctr19_z_transform_roc.md) | [tex](lecture_summaries_tex/lctr19_z_transform_roc.tex) |
| 20 | Inverse z-transform and properties | [md](lecture_summaries/lctr20_inverse_z_transform_properties.md) | [tex](lecture_summaries_tex/lctr20_inverse_z_transform_properties.tex) |
| 21 | System analysis via unilateral z-transform | [md](lecture_summaries/lctr21_system_analysis_unilateral_z.md) | [tex](lecture_summaries_tex/lctr21_system_analysis_unilateral_z.tex) |
| 22 | Sampling | [md](lecture_summaries/lctr22_sampling.md) | [tex](lecture_summaries_tex/lctr22_sampling.tex) |
| 23 | Linear feedback systems | [md](lecture_summaries/lctr23_linear_feedback_systems.md) | [tex](lecture_summaries_tex/lctr23_linear_feedback_systems.tex) |

Original lecture PDFs are archived in [all_lectures/](all_lectures/).

Chapter-level summaries:
- [summaries/Chapter_1_Summary_Lessons_2-5.pdf](summaries/Chapter_1_Summary_Lessons_2-5.pdf)
- [summaries/nblm_chapters_1_to_9.md](summaries/nblm_chapters_1_to_9.md)

---

## Homework Practice

### [hw_practice_problems/](hw_practice_problems/)

Raw practice problem PDFs (and a few Markdown transcriptions) organized by chapter or lecture range.

- [hw-chapter01.pdf](hw_practice_problems/hw-chapter01.pdf) — chapter 1 practice problems
- [hw-lctr09-11.pdf](hw_practice_problems/hw-lctr09-11.pdf) + [hw-lctr09-11-solutions.pdf](hw_practice_problems/hw-lctr09-11-solutions.pdf)
- [hw-lctr12-15.pdf](hw_practice_problems/hw-lctr12-15.pdf) + [hw-lctr12-15-solutions.pdf](hw_practice_problems/hw-lctr12-15-solutions.pdf)
- [hw-lctr16-18.pdf](hw_practice_problems/hw-lctr16-18.pdf) + [hw-lctr16-18.md](hw_practice_problems/hw-lctr16-18.md) + [hw-lctr16-18-solutions.pdf](hw_practice_problems/hw-lctr16-18-solutions.pdf) (Exam 3 — Laplace; full transcribed solutions in [homework/hw5/](homework/hw5/))
- [hw-lctr19-21.pdf](hw_practice_problems/hw-lctr19-21.pdf) + [hw-lctr19-21.md](hw_practice_problems/hw-lctr19-21.md) + [hw-lctr19-21-solutions.pdf](hw_practice_problems/hw-lctr19-21-solutions.pdf) (Exam 3 — z-transform; official transcribed solutions in [homework/hw6/hw6_official_solutions.md](homework/hw6/hw6_official_solutions.md))
- Per-lecture exercises: [lctr03](hw_practice_problems/lctr03-exercise-euler-derivations.pdf), [lctr04](hw_practice_problems/lctr04-exercise.pdf), [lctr05](hw_practice_problems/lctr05-exercise.pdf), [lctr06](hw_practice_problems/lctr06-convolution-problems.pdf), [lctr07](hw_practice_problems/lctr07-convolution-problems.pdf), [lctr08](hw_practice_problems/lctr08-problems.pdf), [lctr22 (pdf)](hw_practice_problems/lctr22-exercise.pdf) / [md](hw_practice_problems/lctr22-exercise.md) + [solutions pdf](hw_practice_problems/lctr22-exercise-solutions.pdf) / [solutions md](hw_practice_problems/lctr22-exercise-solutions.md) / [solutions tex](hw_practice_problems/lctr22-exercise-solutions.tex), [lctr23 (pdf)](hw_practice_problems/lctr23-exercise.pdf) / [md](hw_practice_problems/lctr23-exercise.md) + [solutions pdf](hw_practice_problems/lctr23-exercise-solutions.pdf) / [solutions md](hw_practice_problems/lctr23-exercise-solutions.md) / [solutions tex](hw_practice_problems/lctr23-exercise-solutions.tex)

### [homework/](homework/)

Submitted homework assignments with solutions and supporting material.

- **[homework/hw1/](homework/hw1/)** — chapter 1 homework PDF
- **[homework/hw4/](homework/hw4/)** — lectures 12–15 homework: solutions ([hw4_solutions.md](homework/hw4/hw4_solutions.md)), per-lecture summaries (lecture12–15), original lecture PDFs, and [nblm_0309.md](homework/hw4/nblm_0309.md)
- **[homework/hw5/](homework/hw5/)** — lectures 16–18 Laplace homework (Exam 3): [hw5_questions.md](homework/hw5/hw5_questions.md), full official solutions [hw5_solutions.md](homework/hw5/hw5_solutions.md) / [hw5_solutions.tex](homework/hw5/hw5_solutions.tex)
- **[homework/hw6/](homework/hw6/)** — lectures 19–21 z-transform homework (Exam 3): questions ([hw6_questions.md](homework/hw6/hw6_questions.md)), student solutions in Markdown ([hw6_solutions.md](homework/hw6/hw6_solutions.md)) and LaTeX ([hw6_solutions.tex](homework/hw6/hw6_solutions.tex), [hw6_solutions_latex.md](homework/hw6/hw6_solutions_latex.md)), **official instructor solutions** ([hw6_official_solutions.md](homework/hw6/hw6_official_solutions.md) / [hw6_official_solutions.tex](homework/hw6/hw6_official_solutions.tex)), references ([hw6_references.md](homework/hw6/hw6_references.md)), and lecture summaries (lctr19–21)

---

## How to Build the LaTeX Documents

Every `.tex` file in this repository is **standalone and Overleaf-ready**. To produce a typeset PDF:

1. Open [Overleaf](https://www.overleaf.com/) and create a new blank project.
2. Copy the full contents of the desired `.tex` file (e.g. [exam3/exam3_notes.tex](exam3/exam3_notes.tex) or any file under [lecture_summaries_tex/](lecture_summaries_tex/)) into the project's `main.tex`.
3. Click "Recompile". No extra packages or custom class files are needed — each document includes its own preamble.

The same files also compile locally with `pdflatex <file>.tex` if a LaTeX distribution is installed.

---

## Study Roadmap for Exam 3

Suggested study order for Exam 3 (lectures 16–23: Laplace, z-transform, sampling, feedback):

1. **Read the official study guide first** — [exam3/official_study_guide.md](exam3/official_study_guide.md) is the authoritative instructor-provided guide (transcribed from [StudyGuide_Exam3.pdf](exam3/StudyGuide_Exam3.pdf)). It lists topic coverage, golden rules (CT poles in LHP, DT poles inside unit circle), the "always state ROC" rule, and the exam format (50 min, 100 pts: Part I 10 MC × 4 pts = 40, Part II multi-part problems = 60).
2. **Orient with the student study guide** — [exam3/exam3_study_guide.md](exam3/exam3_study_guide.md) (augmented with instructor emphasis from the official guide).
3. **Read the notes** — [exam3/exam3_notes.md](exam3/exam3_notes.md) / [.tex](exam3/exam3_notes.tex) for the condensed theory.
4. **Internalize the cheatsheet** — [exam3/exam3_cheatsheet.md](exam3/exam3_cheatsheet.md) / [.tex](exam3/exam3_cheatsheet.tex); aim to reproduce every formula from memory.
5. **Drill flashcards and pitfalls** — [exam3/exam3_flashcards.md](exam3/exam3_flashcards.md) and [exam3/exam3_pitfalls.md](exam3/exam3_pitfalls.md).
6. **Solve sample & practice problems** — [exam3/exam3_sample_problems.md](exam3/exam3_sample_problems.md) and [exam3/exam3_practice_problems.md](exam3/exam3_practice_problems.md) — do them without looking at solutions first.
7. **Work the homework sets with official solutions** (do problems cold, then check):
   - HW Lectures 16–18 (Laplace): [hw5_questions.md](homework/hw5/hw5_questions.md) → [hw5_solutions.md](homework/hw5/hw5_solutions.md)
   - HW Lectures 19–21 (z-transform): [hw6_questions.md](homework/hw6/hw6_questions.md) → [hw6_official_solutions.md](homework/hw6/hw6_official_solutions.md)
   - Lecture 22 Sampling exercise: [lctr22-exercise.md](hw_practice_problems/lctr22-exercise.md) → [lctr22-exercise-solutions.md](hw_practice_problems/lctr22-exercise-solutions.md)
   - Lecture 23 Feedback exercise: [lctr23-exercise.md](hw_practice_problems/lctr23-exercise.md) → [lctr23-exercise-solutions.md](hw_practice_problems/lctr23-exercise-solutions.md)
8. **Take the mock exam** — [mock_exam3.md](exam3/mock_exam3.md), then check [mock_exam3_solutions.md](exam3/mock_exam3_solutions.md).
9. **Refer back to lecture summaries as needed** — each summary ends with a "Worked Examples (from Official Solutions)" and "Instructor Emphasis" section linking to the relevant solution: [exam3/summaries/](exam3/summaries/) or [lecture_summaries/](lecture_summaries/) (lectures 16–23).
