# Report Generation Guide

**Purpose:** Guide for LLM-assisted generation of concise lab/project reports.

---

## Report Structure

Every report follows the 4-section template from [report-template.md](./report-template.md):

1. **Introduction** - Brief description of the lab/project in your own words
2. **Narrative** - What was different, problems encountered, how they were resolved
3. **Code Snippets and Screenshots** - Artifacts with captions and file references
4. **Discussions and Results** - Takeaways, learnings, answers to questions

---

## LLM Workflow for Report Generation

### Phase 1: Initialize Report

At the start of a lab/project, create `{labXX}_report.md` or `{projXX}_report.md` in the corresponding folder:

```markdown
# Lab XX Report: [Title]

**Course:** [Course code]
**Lab Start Date:** YYYY-MM-DD
**Report Date:** YYYY-MM-DD

---

## Introduction

[To be filled after completing the lab]

---

## Narrative

[To be filled as issues are encountered and resolved]

---

## Code Snippets and Screenshots

[To be filled as artifacts are collected]

---

## Discussions and Results

[To be filled after completing the lab]
```

### Phase 2: Track Artifacts During Execution

As artifacts are captured:

1. **Ask the user** if an artifact was saved and its filename
2. **Add markdown references** to the artifact in the report:
   ```markdown
   ### Artifact A1: Hello World Output

   ![A1 - UART2 Hello World](./a1.png)

   *Figure 1: UART2 window showing "Hello World!" and "Input a string:" output after successful build and Renode execution.*
   ```

3. **For code snippets**, include with filename reference:
   ```markdown
   ### Code: cc4d_hello_from_uart_app.c

   ```c
   void mp_app(void) {
       printf("Hello from UART!\n");
       // ... rest of code
   }
   ```

   *Code Snippet 1: Task 3 implementation - name greeting with tilde-to-space conversion*
   ```

### Phase 3: Fill Sections After Completion

After all tasks are complete:

1. **Introduction**: Summarize what the lab teaches (1-2 sentences)
2. **Narrative**: Document any issues encountered and how they were resolved
3. **Discussions and Results**: Key takeaways and learnings

---

## Report Conciseness Guidelines

- **Keep it brief**: Each section should be 2-5 sentences max
- **Focus on substance**: What was done, what was learned
- **Use bullet points** for lists of issues/solutions
- **Captions are important**: Every artifact needs a descriptive caption
- **Link don't embed**: Use markdown links to reference files in the same folder

---

## Artifact Reference Format

### Screenshots
```markdown
![Artifact ID - Brief Description](./filename.png)

*Figure N: Detailed caption explaining what the screenshot shows.*
```

### Code Files
```markdown
**File:** [filename.c](./filename.c)

```c
// Key code excerpt
```

*Code Snippet N: Description of what this code does.*
```

### External Files
```markdown
See [lab01_findings.md](./lab01_findings.md) for detailed execution log.
```

---

## Example: Minimal Complete Report

```markdown
# Lab 01 Report: Creating a "Hello from UART" Project

**Course:** MP-CC4D
**Lab Start Date:** 2026-02-04
**Report Date:** 2026-02-04

---

## Introduction

This lab teaches creating an STM32 project from scratch using CubeMX for configuration, CubeIDE for building, and Renode for simulation. The goal is to output messages via UART and read user input.

---

## Narrative

The main challenge was configuring include paths in CubeIDE. The `lib_src` folder had its own include path settings that overrode the project settings, causing "file not found" errors. This was resolved by editing the `.cproject` file directly and deleting the Debug folder to force makefile regeneration.

---

## Code Snippets and Screenshots

### Artifact A1: Initial UART Output

![A1 - Hello World](./a1.png)

*Figure 1: UART2 window showing "Hello World!" and "Input a string:" - confirms successful project setup.*

### Artifact A2: Name Greeting

![A2 - Name Greeting](./a2.png)

*Figure 2: UART2 window showing name input with tilde substitution working correctly.*

### Task 3 Code

**File:** [cc4d_hello_from_uart_app.c](./cc4d_hello_from_uart_app.c)

The `mp_str2name()` function converts tildes to spaces, allowing multi-word names to be entered via UART.

---

## Discussions and Results

**Key Learnings:**
- CubeMX generates project skeleton, but source files must be linked manually
- Eclipse CDT has per-folder build settings that can override project settings
- Renode provides hardware emulation without physical MCU

**Takeaway:** Understanding the STM32 toolchain workflow (CubeMX → CubeIDE → Renode) is essential for embedded development.
```

---

## Integration with LAB_PROJECT_ANALYSIS_PROCEDURE

When analyzing a new lab/project:

1. Create the report file with the template structure
2. As artifacts are captured, update the "Code Snippets and Screenshots" section
3. After completion, fill in Introduction, Narrative, and Discussions
4. Keep the report in the same folder as the procedure and findings documents
