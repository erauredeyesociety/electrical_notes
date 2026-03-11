# Proj 04 Procedure: Half Precision IEEE 754 Numbers

**Course:** CEC 320
**Points:** 100 (80 programming + 10 app + 10 submission)

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `mp-ee4u--proj4-half-precision-ieee754-26-03.pdf`

---

## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Extract ZIP to `/opt/proj_mp/`, implement both functions |
| 2 | HUMAN | CubeIDE: Import project, build Unity config |
| 3 | HUMAN | Renode: Run Unity tests |
| → | **ARTIFACT** | **A1:** Screenshot of 5 tests passing |
| 4 | HUMAN | CubeIDE: Build Application config |
| 5 | HUMAN | Renode: Run App |
| → | **ARTIFACT** | **A2:** Screenshot of App output |
| 6 | LLM | Save code artifact, finalize report, create ZIP |

---

## Overview

This project implements encoding and decoding of **half-precision IEEE 754** floating-point numbers (IEEE 754-2008):
- Sign: 1 bit
- Exponent: 5 bits (bias = 15)
- Fraction: 10 bits

Two functions in `ee4u_half_precision_ieee754_fns.c`:
1. **`mp_hp_ieee754_encoding`** — float → {sign, exponent, fraction} fields
2. **`mp_hp_ieee754_decoding`** — {sign, exponent, fraction} fields → float

5 Unity tests (16 pts each = 80 pts):
- Encoding: too-big number (→ infinity), normal number (-31.875), tiny/denormalized number (2^-18)
- Decoding: normal number, tiny/denormalized number

**Setup approach:** The manual offers two options. We use **Option 2** — the standalone `ee4u_half_precision_ieee754.zip` project which has pre-configured F412dsc build configs (Debug, Unity, Application) and Renode scripts.

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| Extract ZIP to `/opt/proj_mp/` | File operation | CLAUDE CODE |
| Implement `mp_hp_ieee754_encoding` | Code writing | CLAUDE CODE |
| Implement `mp_hp_ieee754_decoding` | Code writing | CLAUDE CODE |
| Import project in CubeIDE | GUI wizard | HUMAN |
| Build Unity config | GUI button | HUMAN |
| Run Renode (Unity tests) | GUI application | HUMAN |
| Capture A1 screenshot | OS interaction | HUMAN |
| Build Application config | GUI button | HUMAN |
| Run Renode (App) | GUI application | HUMAN |
| Capture A2 screenshot | OS interaction | HUMAN |
| Save code artifact, report, ZIP | File operation | CLAUDE CODE |

---

## Part A: Claude Code Automated Tasks

### A.1 Extract Project ZIP

Extract `ee4u_half_precision_ieee754.zip` to `/opt/proj_mp/`:

```bash
cd /opt/proj_mp/
unzip ~/electrical_notes/content/cec_320/labs_and_projects/proj04/ee4u_half_precision_ieee754.zip
```

### A.2 Implement Both Functions

Edit `/opt/proj_mp/ee4u_half_precision_ieee754/src/ee4u_half_precision_ieee754_fns.c`:

**Function 1: `mp_hp_ieee754_encoding`** — Encode a float into half-precision IEEE 754 fields.

Cases:
- **Too big** (|f| > hp_float_max): set to infinity (exp=31, frac=0)
- **Normal** (|f| >= hp_float_min_norm): compute biased exponent and fraction
- **Denormalized** (|f| < hp_float_min_norm): exp=0, fraction = f / 2^(1-bias) * 2^n_frac

**Function 2: `mp_hp_ieee754_decoding`** — Decode half-precision fields back to float.

Cases:
- **exp == 31**: infinity (or NaN if frac != 0)
- **exp == 0, frac != 0**: denormalized: value = (-1)^sign * frac/2^n_frac * 2^(1-bias)
- **exp == 0, frac == 0**: zero
- **Normal**: value = (-1)^sign * (1 + frac/2^n_frac) * 2^(exp-bias)

### A.3 Save Code Artifact and Create ZIP

After tests pass, save code to `c1.c`, populate report, create submission ZIP.

---

## Part B: Human Tasks (GUI Required)

### B.1 Import Project in CubeIDE

1. Open CubeIDE (workspace: `/opt/proj_mp/`)
2. **File → Open Projects from File System...**
3. Click **Directory...** → navigate to:
   ```
   /opt/proj_mp/ee4u_half_precision_ieee754/ee4u_half_precision_ieee754_f412dsc/STM32CubeIDE
   ```
4. Ensure the project checkbox is selected → **Finish**

### B.2 Build Unity Configuration

1. Click the **hammer dropdown** arrow → select **Unity**
2. Build: **Ctrl+B**
3. Verify build succeeds with no errors

### B.3 Run Renode (Unity Tests)

1. Open terminal:
   ```bash
   cd /opt/proj_mp/ee4u_half_precision_ieee754/renode/
   renode
   ```
2. In Renode Monitor, type:
   ```
   s @unity_ee4u_half_precision_ieee754_f412dsc.resc
   ```
3. Wait for UART2 window to show test results
4. **→ ARTIFACT A1:** Screenshot showing all 5 tests passing (0 failures)
5. Save as `a1.png` in `~/electrical_notes/content/cec_320/labs_and_projects/proj04/`

### B.4 Build Application Configuration

1. Click the **hammer dropdown** arrow → select **Application**
2. Build: **Ctrl+B**
3. Verify build succeeds

### B.5 Run Renode (App)

1. In Renode Monitor (quit and restart if needed):
   ```bash
   cd /opt/proj_mp/ee4u_half_precision_ieee754/renode/
   renode
   ```
2. Type:
   ```
   s @app_ee4u_half_precision_ieee754_f412dsc.resc
   ```
3. Wait for UART2 window to show App output (encoded fields + decoded values)
4. **→ ARTIFACT A2:** Screenshot showing App running result
5. Save as `a2.png` in `~/electrical_notes/content/cec_320/labs_and_projects/proj04/`

### B.6 Clean and Create Submission ZIP

1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. Tell Claude Code to create the ZIP

---

## Submission Checklist

- [ ] A1: Screenshot of all 5 Unity tests passing
- [ ] A2: Screenshot of App output
- [ ] C1: Code for both functions (`ee4u_half_precision_ieee754_fns.c`)
- [ ] Report: `ee4u-proj4-report-lastname-firstname.pdf`
- [ ] ZIP: `ee4u-proj4-lastname-firstname.zip`
