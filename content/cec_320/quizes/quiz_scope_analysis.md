# CEC 320 — Quiz Scope Analysis

Date of analysis: 2026-04-19

Hypothesis: each quiz is scoped by a contiguous block of homeworks, and each HW is scoped by a contiguous block of lectures. If true, mapping HW blocks to quizzes lets us deduce the scope of future quizzes.

---

## 1. Quiz-to-HW-to-Lecture table

| Quiz  | HWs covered | Lectures covered | Evidence |
|-------|-------------|------------------|----------|
| Qz 1  | HW 1, (HW 2) | Lctr 2–5 | `qz1a-uart-arch-mem-ptr-soln-2025-01.pdf` filename: "uart-arch-mem-ptr" = UART (L2) + MCU arch (L3) + data rep / memory (L4) + pointers (L5). HW1 (`uart-n-mcu-arch-n-num-expr`) covers L2–3; HW2 (`data-mem-ptr-unity`) covers L4–5. |
| Qz 2  | HW 3, 4, 5 | Lctr 6–9, 13 | `qz2_prep.md` header: "Homeworks 3, 4, & 5 \| Lectures 6–9, 12–13". HW3 = GPIO + bitwise (L6–7); HW4 = interrupt + preemption (L8–9); HW5 = real numbers / fixed-point (L13). (Lctr 10–12 are absent / exam week.) |
| Qz 3 (confirmed) | HW 6, 7, 8 | Lctr 14–18 | `qz3_cheatsheet.md` header: "HWs 6, 7, 8 \| Lectures 14–18". HW6 = mixed C+ASM / EABI (L14–15); HW7 = shifts + bitwise logic (L16–17); HW8 = NZCV / CCS / branch (L18, slight L19 spillover). |
| Qz 4 (predicted) | HW 9, 10, 11, 12 | Lctr 19–26 | By process of elimination — these are the only remaining HWs. See detailed mapping below. |

### Quiz 4 detailed HW → Lecture mapping (from filename stems)

| HW | Filename stem | Lecture(s) |
|----|--------------|-----------|
| HW 9  | `gcge--ldr-str` | Lctr 20 (immediate-offset LDR/STR), Lctr 21 (reg-offset LDR/STR + MOV). `lctr20/21/22/23_summary.md` files live in `hw9/`. |
| HW 10 | `gggm--c-ptr-n-ldr-str-n-fn-call` | Lctr 22 (increment ops for ptrs/vars) and Lctr 23 (calling ASM from ASM). The `ggm` infix matches lctr22 (`gg`) and lctr23 (`gm`) file codes. |
| HW 11 | `hche--if-based-flow-control` | Lctr 24 (combo branch + conditional execution / IT) and Lctr 25 (if-else in C/ASM). Contents confirm CMP / CEX / PL / NL approaches. |
| HW 12 | `hghi--loops` | Lctr 26 (loops in ASM). String-swap / loop problems. |

So Qz 4 scope = **HW 9–12, Lctr 19 review + Lctr 20–26** (Lctr 19 is a natural spillover bridge already introduced in Qz 3).

---

## 2. Proportionality / scope check

| Quiz | # HWs | # Lectures | Lec/HW |
|------|-------|------------|--------|
| Qz 1 | 2 | 4 (L2–5) | 2.0 |
| Qz 2 | 3 | 5 (L6–9, L13) | ~1.7 |
| Qz 3 | 3 | 5 (L14–18) | ~1.7 |
| Qz 4 | 4 | 7 (L20–26) | ~1.75 |

Qz 4 has one more HW than Qz 2/3, but the lecture-per-HW density is consistent. Lectures 20–23 are all load/store/move/function-call (highly related), and 24–26 are all control flow (highly related) — so the material is cohesive, not overloaded. No strong signal of "overflow to a Qz 5."

---

## 3. Has Quiz 4 already happened?

**Prediction: NO — Quiz 4 has not happened yet.** Strong evidence:

- **No `quiz4/` folder exists.** `find` under `content/cec_320` shows only `quiz3/` as a quiz subfolder. Student consistently creates a `qzN_cheatsheet.md` + `qzN_init.md` before/around the quiz date (pattern set by `quiz3/`).
- **HW 12 PDF arrived today (2026-04-19 18:02).** A quiz covering HW 12 cannot meaningfully happen before HW 12 is even distributed. Typical class cadence: HW released → worked → due → quiz.
- **HW 11 solutions finalized 2026-04-16.** That is only 3 days ago. At the quiz-2 / quiz-3 cadence, students had several days to a week between final HW of a block and the quiz.
- **HW 12 has no solutions/work files yet** — only the raw problem PDF.

Most likely quiz 4 date: ~1–2 weeks out from today, after HW 12 is solved.

---

## 4. Is there a Quiz 5, or does the final absorb the rest?

**Prediction: No Quiz 5. Quiz 4 is the final scheduled quiz; remaining material (if any) rolls into the final exam.**

Evidence:

- **Lecture ceiling.** `LECTURE_INDEX.md` lists lectures 2–26 (with gaps at 10–12). Lecture 27 is mentioned in the task framing but absent from the index — likely a forward reference the instructor has not delivered. Lctr 26 (loops) is the natural capstone of the ASM control-flow thread.
- **HW ceiling.** HW 12 exists; no HW 13 artifacts, references, or placeholders exist anywhere in the tree.
- **Quiz cadence ≈ one quiz per HW block of 3 HWs.** HW 9–12 is 4 HWs, not 3, suggesting this block is intentionally the last and slightly larger. A 5th quiz would need HW 13+, which doesn't exist.
- **Scope progression.** Qz 1 → Qz 2 → Qz 3 → Qz 4 corresponds neatly to the four major course phases: (1) intro + pointers, (2) peripherals + interrupts + real numbers, (3) ASM fundamentals + flags, (4) load/store + control flow. This is a clean 4-unit structure.

Caveat: if the instructor adds Lctr 27 and a HW 13 in the final week (less likely given current state), a 5th quiz or a late-added quiz-4-extension could appear. Watch for new HW drops after HW 12.

---

## 5. Confidence summary

| Claim | Confidence |
|-------|-----------|
| Qz 4 scope = HW 9–12 / Lctr 20–26 | **High** (only remaining HWs; filename-stem → lecture mapping is consistent) |
| Qz 4 has not happened yet | **Very high** (no quiz4 folder; HW12 PDF is 1 day old) |
| No Qz 5; final absorbs overflow | **Medium-high** (consistent with 4-unit cadence and no HW13, but depends on instructor adding/not adding Lctr 27+) |

Ambiguities that could not be fully resolved:
- Whether Lctr 19 is nominally in Qz 3 or Qz 4. HW 8 (Qz 3) touches branch/CCS (L19), but the cheatsheet says "Lectures 14–18." Lctr 19 material likely gets re-examined in Qz 4 alongside the heavier control-flow lectures.
- Lctr 27 existence — referenced in user's task framing but not in `LECTURE_INDEX.md`. If delivered late, could shift scope boundaries.
