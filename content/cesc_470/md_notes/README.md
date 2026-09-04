# CESC 470 — study notes

**Computer Architecture** · Fall 2026 · Siyao Li · MWF 11:00–11:50, Lehman 369

Tutorials built from the class material: brief theory, worked examples, and
citations back to the source slide. Written for quiz prep.

| Notes | Covers | Source |
| --- | --- | --- |
| [`01_performance_and_cpu_time.md`](01_performance_and_cpu_time.md) | CPU time vs elapsed, clock cycles, the performance equation, CPI, Amdahl's law — **7 worked examples** | Module 01, PDF p51–88 |

Raw text extraction lives in [`../pdf_transcripts/`](../pdf_transcripts/).

---

## ⚠ Coverage gap

Module 01 is **62 of 88 pages image-only** — the text layer carries labels and
prose but not the diagram content. The quantitative material (performance, CPI,
Amdahl) came through nearly intact, which is the part quizzes test. What is
**not** covered here:

- the datapath / five-components diagram *(PDF p13)*
- the processor-performance-growth figure *(PDF p83)*
- execution-cycle and pipeline diagrams *(PDF p38ff)*
- most of the ISA examples *(PDF p21–35, partially recovered)*

**Open the PDF for those.** OCR to recover them is in progress —
[`../../../ocr_handler/`](../../../ocr_handler/).

Verify the gap yourself:

```sh
cd ~/electrical_notes/ocr_handler
uv run ocr-handler inspect "../content/cesc_470/Module 01 Introduction to computer technology & ISA (1).pdf"
```

---

## Course facts

From [`../cesc_470.pdf`](../cesc_470.pdf):

- **Textbook:** Hennessy & Patterson, Elsevier S&T, 2016, 1st ed.
- **Grading:** A 90–100 · B 80–89 · C 70–79 · D 60–69 · F <60
- **Homework:** must be **typed and submitted as PDF**.
- **Attendance:** not recorded, but *"factored into the quizzes"* — the quizzes
  draw on what happens in class, so these notes are a supplement to attending,
  not a substitute.
- **Make-up exams:** documented absences only, scheduled within 7 days.

### Student learning outcomes

1. Evaluate principles and trade-offs (cost/performance, speed/flexibility)
   using qualitative **and quantitative** methods. ← *Module 01*
2. Design an instruction set for a specific processor architecture.
3. Analyze hierarchical memory design, cache performance and optimization.
4. Optimize processor performance using basic and advanced pipelining.
5. Assess hardwired vs microprogrammed control.
6. Explain how multicore architecture improves parallelism and throughput.

---

## How these notes are written

- **Every formula cites its slide** by PDF page, so a claim can be checked
  against the source rather than trusted.
- **Every worked example is recomputed independently.** Where the deck prints an
  answer, the two are compared and agreement is stated; where it does not, the
  derivation is shown in full and labelled as derived.
- **Traps are called out explicitly** — the places where a plausible shortcut
  gives the wrong answer (e.g. more instructions still running faster).
