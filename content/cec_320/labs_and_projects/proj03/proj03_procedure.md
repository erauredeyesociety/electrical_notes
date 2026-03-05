# Proj 03 Procedure: Fixed-Point Arithmetic Operations

**Course:** CEC 320 / MP-EE4U
**Points:** 100 total (10 setup + 80 programming + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-ee4u-proj3-fixed-point-operations-26-02.pdf`
> - [known_base_projects.md](../known_base_projects.md) — ca4b_cls_projs base project

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Verify proj3_src/ and proj3_test/ files are in place (already done) |
| 2 | HUMAN | CubeIDE: Link .c files into proj3_src_test/, select Proj3Unity, build |
| 3 | HUMAN | Renode: Run proj3Unity to confirm build works (all tests should fail) |
| 4 | LLM | Implement PT1: mp_uq_and_q_mn_decoding() |
| 5 | HUMAN | Rebuild Proj3Unity, run in Renode |
| → | **ARTIFACT** | **A1:** Screenshot — test_mp_uq_and_q_mn_decoding PASSED (1 pass, 2 fail) |
| 6 | LLM | Implement PT2: mp_uq_and_q_mn_encoding() |
| 7 | HUMAN | Rebuild Proj3Unity, run in Renode |
| → | **ARTIFACT** | **A2:** Screenshot — 2 tests pass, 1 fail |
| 8 | LLM | Implement PT3: mp_q_mn_multiplication() |
| 9 | HUMAN | Rebuild Proj3Unity, run in Renode |
| → | **ARTIFACT** | **A3:** Screenshot — all 3 tests pass, 0 failures |
| 10 | LLM | Implement PT4: main App in ee4u_fixed_point_operations_app.c |
| 11 | HUMAN | Select Proj3App build config, build, run in Renode |
| → | **ARTIFACT** | **A4:** Screenshot — App output showing Q15 encode/multiply/print |
| 12 | LLM | Save code artifacts (c1.c, c2.c), update findings/report |
| 13 | HUMAN | Clean builds in CubeIDE |
| 14 | LLM | Create submission ZIP |

---

## Point Breakdown

| Section | Points | Description |
|---------|--------|-------------|
| 3.2 Getting Started | 10 | Project setup, build Proj3Unity |
| 3.3.1 PT1: mp_uq_and_q_mn_decoding | 20 | UQm.n and Qm.n decoding |
| 3.3.1 PT2: mp_uq_and_q_mn_encoding | 20 | UQm.n and Qm.n encoding |
| 3.3.1 PT3: mp_q_mn_multiplication | 20 | Qm.n multiplication |
| 3.3.3 PT4: Main App | 20 | Q15 operations, printf output |
| 3.4 Submission | 10 | Report + ZIP |

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Verify source files in proj3_src/ and proj3_test/ | CLAUDE CODE |
| Link .c files in CubeIDE proj3_src_test/ | HUMAN |
| Select build config and build | HUMAN |
| Run Renode simulation | HUMAN |
| Implement PT1-PT3 (3 functions) | CLAUDE CODE |
| Implement PT4 (main App) | CLAUDE CODE |
| Capture screenshots | HUMAN |
| Save code artifacts, update docs | CLAUDE CODE |
| Create submission ZIP | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Verify Source Files (Already Done)

Files are already in place from a previous extraction or pre-configuration:

**proj3_src/** (at `/opt/proj_mp/ca4b_cls_projs/proj3_src/`):
- `ee4u_fixed_point_fns.c` — 3 weak stub functions to implement
- `ee4u_fixed_point_fns.h` — header file
- `ee4u_fixed_point_operations_app.c` — app main (weak stub)
- `_mp_main.c` — dispatcher
- `ee4u_fixed_point_fns_soln.c` — solution file (DO NOT submit)
- `ee4u_fixed_point_operations_app_soln.c` — solution file (DO NOT submit)

**proj3_test/** (at `/opt/proj_mp/ca4b_cls_projs/proj3_test/`):
- `test_ee4u_fixed_point_fns.c` — 3 test functions (provided, do not modify)

**Renode scripts** (at `/opt/proj_mp/ca4b_cls_projs/renode/`):
- `proj3Unity_f412dsc.resc` — for unit tests
- `proj3App_f412dsc.resc` — for app

> **Note:** Solution files (`*_soln.c`) exist on the system. These are reference solutions — do NOT link them in CubeIDE or submit them. Only link the non-soln versions.

### A.2 Implement Programming Tasks

Implement 3 functions in `ee4u_fixed_point_fns.c` and the App in `ee4u_fixed_point_operations_app.c`. Done incrementally — see execution sequence above.

### A.3 Save Code Artifacts and Update Documentation

After all tasks pass, save code snippets to `proj03/c1.c` and `proj03/c2.c`.

---

## Part B: Human Tasks (GUI Required)

### B.1 Link Source Files in CubeIDE (10 pts)

The `proj3_src/` and `proj3_test/` files need to be linked into CubeIDE.

1. Open CubeIDE with the `ca4b_cls_projs` project
2. In Project Explorer, find `proj3_src_test/` folder
3. Right-click `proj3_src_test/` → **New → File**
4. Click **Advanced >>** → check **Link to file in the file system**
5. Link each of these files (one at a time):

| Source File (full path) | Destination |
|-------------------------|-------------|
| `/opt/proj_mp/ca4b_cls_projs/proj3_src/ee4u_fixed_point_fns.c` | proj3_src_test/ |
| `/opt/proj_mp/ca4b_cls_projs/proj3_src/ee4u_fixed_point_fns.h` | proj3_src_test/ |
| `/opt/proj_mp/ca4b_cls_projs/proj3_src/ee4u_fixed_point_operations_app.c` | proj3_src_test/ |
| `/opt/proj_mp/ca4b_cls_projs/proj3_src/_mp_main.c` | proj3_src_test/ |
| `/opt/proj_mp/ca4b_cls_projs/proj3_test/test_ee4u_fixed_point_fns.c` | proj3_src_test/ |

> **Important:** Do NOT link the `*_soln.c` files.

6. Select build configuration: **Proj3Unity** (dropdown next to hammer icon)
7. Build: **Ctrl+B** — should build with 0 errors

### B.2 Run Unit Tests in Renode

1. Open terminal:
   ```bash
   cd /opt/proj_mp/ca4b_cls_projs/renode/
   renode
   ```
2. In Renode Monitor window:
   ```
   s @proj3Unity_f412dsc.resc
   ```
3. Check UART output for test results
4. Initially all 3 tests should fail (weak stubs return 0)

### B.3 Incremental Build-Test-Screenshot Cycle

After each LLM implementation step:
1. In CubeIDE: **Ctrl+B** (rebuild Proj3Unity)
2. In Renode: Reset or re-run `s @proj3Unity_f412dsc.resc`
3. Capture screenshot at each artifact point (A1, A2, A3)

### B.4 Run the App (for A4)

1. In CubeIDE: Switch build config to **Proj3App**
2. Build: **Ctrl+B**
3. In Renode (may need to restart):
   ```
   s @proj3App_f412dsc.resc
   ```
4. Capture screenshot of App output (A4)

### B.5 Clean and Submit

1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. LLM creates submission ZIP
3. Rename report and ZIP with your name

---

## Programming Task Details

### PT1: mp_uq_and_q_mn_decoding (20 pts)

**Function signature:**
```c
float mp_uq_and_q_mn_decoding(uint32_t D, int s, int m, int n)
```

**Parameters:**
- `D`: encoded data (uint32_t)
- `s`: 0 for UQm.n (unsigned), 1 for Qm.n (signed)
- `m`: number of bits in whole number field
- `n`: number of bits in fraction field

**Return:** `f` — the decoded real number (float)

**Test cases (from Lecture 13):**
- Case 1 (Example 3): D=0xAD, s=0, m=5, n=3 → expected 21.625 (UQ5.3)
- Case 2 (Example 5): D=0xAD, s=1, m=4, n=3 → expected -10.375 (Q4.3)

### PT2: mp_uq_and_q_mn_encoding (20 pts)

**Function signature:**
```c
uint32_t mp_uq_and_q_mn_encoding(float f, int s, int m, int n)
```

**Parameters:**
- `f`: real number to encode
- `s`: 0 for UQm.n, 1 for Qm.n
- `m`: bits in whole number field
- `n`: bits in fraction field

**Return:** `D` — encoded data (uint32_t)

**Test cases:**
- Case 1 (Example 4): f=3.141593, s=0, m=4, n=12 → expected 0x3244 (UQ4.12)
- Case 2 (Example 7): f=-3.1234, s=1, m=5, n=10 → expected 0xFFFFF382 (Q5.10)

### PT3: mp_q_mn_multiplication (20 pts)

**Function signature:**
```c
float mp_q_mn_multiplication(float f1, float f2, int m, int n)
```

**Parameters:**
- `f1`, `f2`: real numbers (operands)
- `m`: bits in whole number field
- `n`: bits in fraction field

**Return:** product using Qm.n multiplication (NOT `f1 * f2` directly)

**Constraint:** `m + n <= 15` (no greater than 16-bit multiplications)

**Approach:** Encode both operands to Qm.n, multiply the encoded values, shift result right by n, decode back to float.

**Test case (Example 8):** f1=0.5, f2=0.25, m=0, n=15 → expected 0.125

### PT4: Main App (20 pts)

**Problem:** Given f1=0.5, f2=0.25, f3=-0.625 in Q15 format:
1. Encode f1, f2, f3 to Q15 → I1, I2, I3
2. Compute fA = f1 × f2 × f3 using `mp_q_mn_multiplication`
3. Compute fA_float = f1 × f2 × f3 using direct float multiplication
4. Print I1, I2, I3 in hex (format `0x%04X`)
5. Print fA and fA_float (format `%8.7f`)

**Requires:** Enable floating-point printf (FPU support per Section 9.11.2 of Companion)

---

## Submission Checklist

- [ ] A1: Screenshot — test_mp_uq_and_q_mn_decoding passes (1/3)
- [ ] A2: Screenshot — encoding test also passes (2/3)
- [ ] A3: Screenshot — all 3 tests pass (3/3)
- [ ] A4: Screenshot — App output with Q15 results
- [ ] C1: Code for 3 functions in ee4u_fixed_point_fns.c
- [ ] C2: Code for App in ee4u_fixed_point_operations_app.c
- [ ] Report PDF: `ee4u-proj3-report-lastname-firstname.pdf`
- [ ] Project ZIP: `ee4u-proj3-lastname-firstname.zip`
