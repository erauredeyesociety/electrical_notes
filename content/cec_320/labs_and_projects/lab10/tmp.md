Lab10 State
LLM side — done:

Zip extracted to /opt/proj_mp/ge1s_more_ldr_n_str_n_mov/ (single-level, no flattening needed)
Task 8 edits applied to all 3 files (header, asm, test)
New mp_array_pos_sum_cst_ptr_s uses blt to skip negatives
Test expects {0, 9} (first 3 all negative → 0; full 7 → 0+1+3+5 = 9)
arm-none-eabi-as verified it assembles clean
Code artifact saved at lab10/c1.s
Your Steps (debugger walkthrough, then Task 8 Unity run)
Remember: Per manual §10.1 this lab is NOT graded — submit only if instructor overrides.

Setup
CubeIDE → File → Open Projects from File System → /opt/proj_mp/ge1s_more_ldr_n_str_n_mov/ge1s_more_ldr_n_str_n_mov_g431n32/STM32CubeIDE
Open ge1s_more_ldr_n_str_n_mov_app.c in the editor
Tasks 1–7 — Debugger GUI walkthrough (A1–A7)
Full click-by-click in lab10_procedure.md:156-220:

A1 — Debug config → build → Run As → PuTTY/tio screenshot → a1.png
A2 — Breakpoint at _app.c line 18 → Debug As → halted at green arrow → a2.png
A3 — Memory view at 0x20000200, Format Row=8 Col=1 → a3.png
A4 — Step Over (F6) to line 22 → re-capture Memory view → a4.png
A5 — Step Into (F5) mp_initialize_r1_to_r6_s → Step Over to store_r1_to_r6_local_0 → Registers view R0–R6 → a5.png
A6 — Step Return (F7) → Step Over to line 31 → Variables view, set var32 to Hex → a6.png
A7 — Expressions view: add regs + reservation (first 10) → a7.png
Breakpoint tip: If A2 doesn't halt, open Breakpoints view → Remove All (old breakpoints from other projects can exceed the limit) → re-set.

Task 8 — Unity run (A8, A9)
Switch to Unity build config → Ctrl+B
Run As → STM32 C/C++ Application
Serial shows new test_mp_array_pos_sum_cst_ptr_s passing alongside the others
A8 — serial screenshot → a8.png
A9 — editor screenshot of the new asm function → a9.png
Optional submission
If required: paste all 9 screenshots into one PDF (no naming convention given in manual).

When you're done with screenshots, ping me and I'll mark the findings complete.