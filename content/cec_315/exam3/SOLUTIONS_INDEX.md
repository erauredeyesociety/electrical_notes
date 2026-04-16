# Exam 3 Solutions Index — CEC 315 (Lectures 16–23)

Quick jump table for every official, instructor-provided solution set covering Exam 3 material. Each entry links the problem statements, the transcribed markdown solutions, the Overleaf-ready LaTeX version, and the source PDF.

## Homework Solution Sets

| Topic | Lectures | Questions | Solutions (md) | Solutions (tex) | Source PDF |
|---|---|---|---|---|---|
| Laplace transform, inversion, properties, system analysis | 16–18 | [hw5_questions.md](../homework/hw5/hw5_questions.md) | [hw5_solutions.md](../homework/hw5/hw5_solutions.md) | [hw5_solutions.tex](../homework/hw5/hw5_solutions.tex) | [hw-lctr16-18-solutions.pdf](../hw_practice_problems/hw-lctr16-18-solutions.pdf) |
| z-transform, inversion, properties, system analysis | 19–21 | [hw6_questions.md](../homework/hw6/hw6_questions.md) | [hw6_official_solutions.md](../homework/hw6/hw6_official_solutions.md) (+ student set [hw6_solutions.md](../homework/hw6/hw6_solutions.md)) | [hw6_official_solutions.tex](../homework/hw6/hw6_official_solutions.tex) | [hw-lctr19-21-solutions.pdf](../hw_practice_problems/hw-lctr19-21-solutions.pdf) |
| Sampling practice | 22 | [lctr22-exercise.md](../hw_practice_problems/lctr22-exercise.md) | [lctr22-exercise-solutions.md](../hw_practice_problems/lctr22-exercise-solutions.md) | [lctr22-exercise-solutions.tex](../hw_practice_problems/lctr22-exercise-solutions.tex) | [lctr22-exercise-solutions.pdf](../hw_practice_problems/lctr22-exercise-solutions.pdf) |
| Feedback systems practice | 23 | [lctr23-exercise.md](../hw_practice_problems/lctr23-exercise.md) | [lctr23-exercise-solutions.md](../hw_practice_problems/lctr23-exercise-solutions.md) | [lctr23-exercise-solutions.tex](../hw_practice_problems/lctr23-exercise-solutions.tex) | [lctr23-exercise-solutions.pdf](../hw_practice_problems/lctr23-exercise-solutions.pdf) |
| Mock exam (student-written) | 16–23 | [mock_exam3.md](mock_exam3.md) | [mock_exam3_solutions.md](mock_exam3_solutions.md) | [mock_exam3_solutions.tex](mock_exam3_solutions.tex) | — |

## Official Instructor Study Guide

The authoritative exam 3 study guide is the instructor PDF [StudyGuide_Exam3.pdf](StudyGuide_Exam3.pdf). Transcribed (and Overleaf-compilable) versions:

- [official_study_guide.md](official_study_guide.md)
- [official_study_guide.tex](official_study_guide.tex)

## Exam Format Reminder (from the official guide)

- **50 minutes, 100 points.**
- Part I — 10 multiple-choice questions, 4 points each (40 pts).
- Part II — multi-part worked problems (60 pts).
- Instructor rule: **Always state the ROC with every transform.**

## Golden Rules

| Domain | Stability (causal) | Instability condition |
|---|---|---|
| Continuous-time (Laplace) | All poles in open LHP: $\mathrm{Re}\{s_i\} < 0$ | Any pole with $\mathrm{Re}\{s_i\} \ge 0$ |
| Discrete-time (z-transform) | All poles strictly inside unit circle: $|p_i| < 1$ | Any pole with $|p_i| \ge 1$ |
| Feedback systems (closed-loop) | Roots of $1 + KGH = 0$ satisfy the respective rule | $GH = -1$ (0 dB magnitude and $-180^{\circ}$ phase simultaneously) |

See [official_study_guide.md](official_study_guide.md) for the full topic list, transform pair tables, and common mistakes.
