# Lab and Project Analysis Procedure

**Document Purpose:** Reference guide for Claude Code to analyze labs/projects, identify automatable vs human tasks, and generate procedure and findings documents.

**Last Updated:** 2026-02-04

---

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [Output Documents](#output-documents)
3. [Alternating Workflow Model](#alternating-workflow-model)
4. [Analysis Workflow](#analysis-workflow)
5. [Task Classification](#task-classification)
6. [What Claude Code Can Do](#what-claude-code-can-do)
7. [What Requires Human Interaction](#what-requires-human-interaction)
8. [Creating Procedure Documents](#creating-procedure-documents)
9. [Creating Findings Documents](#creating-findings-documents)
10. [Report Generation](#report-generation)
11. [Issue Tracking](#issue-tracking)
12. [Common Patterns](#common-patterns)
13. [Terminology Reference](#terminology-reference)

---

## Reference Documents

| Document | Purpose |
|----------|---------|
| [report-template.md](./report-template.md) | Official 4-section report template |
| [report_generation_guide.md](./report_generation_guide.md) | LLM guide for generating reports |
| [known_issues.md](./known_issues.md) | **Documented issues and solutions - CHECK FIRST when stuck** |
| [findings/](./findings/) | Detailed technical findings and research |
| [SYSTEM_ANALYSIS.md](./SYSTEM_ANALYSIS.md) | Environment and toolchain setup |
| [analysis_prompt.md](./analysis_prompt.md) | Prompt template for starting new labs/projects |

---

## Folder Structure

### Directory Layout

```
/opt/proj_mp/                              # PROJECT ROOT
├── labs_and_projects/                     # DOCUMENTATION ONLY
│   ├── LAB_PROJECT_ANALYSIS_PROCEDURE.md  # This document
│   ├── SYSTEM_ANALYSIS.md                 # Environment setup
│   ├── analysis_prompt.md                 # Prompt template for LLM
│   ├── lab01/                             # Lab 01 documentation
│   │   ├── lab01_procedure.md             # Procedure document
│   │   ├── lab01_findings.md              # Findings/artifacts tracking
│   │   ├── lab01_report.md                # Generated report (for submission)
│   │   ├── *.c                            # Code artifacts
│   │   ├── *.png                          # Screenshot artifacts (A1, A2, etc.)
│   │   ├── *.pdf                          # Original lab PDF
│   │   └── *.jpg                          # Supplementary images
│   ├── lab02/                             # Lab 02 documentation
│   ├── proj01/                            # Project 01 documentation
│   └── ...
│
├── cc1s_uart_redirect/                    # Actual CubeIDE/CubeMX project
├── cc4d_hello_from_uart/                  # Actual CubeIDE/CubeMX project
└── [other projects]/                      # All projects at this level
```

### Key Principles

1. **Documentation folders** (`labs_and_projects/`) contain ONLY:
   - Procedure documents
   - Findings documents
   - Original PDFs and reference images
   - NO code, NO CubeIDE projects

2. **Project folders** (`/opt/proj_mp/`) contain:
   - Actual CubeIDE/CubeMX projects
   - Source code
   - Build outputs

---

## Output Documents

For each lab or project analysis, create TWO documents:

### 1. Procedure Document

**Naming Convention:**
- Labs: `lab{XX}_procedure.md` (e.g., `lab01_procedure.md`)
- Projects: `proj{XX}_procedure.md` (e.g., `proj01_procedure.md`)

**Purpose:** Actionable step-by-step guide separating:
- Claude Code automated tasks
- Human GUI tasks (with copy-paste commands)

**Contents:**
- Overview and point breakdown
- Task classification summary (who does what)
- Part A: Claude Code tasks (what automation does)
- Part B: Human tasks (step-by-step GUI instructions)
- Submission checklist

### 2. Findings Document

**Naming Convention:**
- Labs: `lab{XX}_findings.md` (e.g., `lab01_findings.md`)
- Projects: `proj{XX}_findings.md` (e.g., `proj01_findings.md`)

**Purpose:** User tracks artifacts for report submission:
- Screenshots (with descriptions)
- Code snippets (with file paths)
- Answers to questions
- Notes and observations

**Contents:**
- Artifact tracking table
- Screenshot placeholders with descriptions
- Code snippet sections
- Submission mapping (which artifact goes where in report)

---

## Alternating Workflow Model

### Core Principle

Work naturally alternates between LLM and human based on **task dependencies**, not a rigid "all LLM first, all human second" approach.

```
LLM ──► HUMAN ──► LLM ──► HUMAN ──► LLM ──► HUMAN
```

### Why Alternation?

GUI applications produce outputs that subsequent tasks depend on:

| GUI Action | Creates | Needed By |
|------------|---------|-----------|
| CubeMX Generate Code | `STM32CubeIDE/` folder | Renode script paths, source linking |
| CubeIDE Build | `.elf` file | Renode simulation |
| CubeIDE Import | Project in workspace | Adding paths, linking files |

**Key insight:** When output from one GUI becomes input to another operation (LLM or GUI), that's a natural handoff point.

### Handoff Points

Common handoff patterns in STM32 projects:

1. **LLM → Human:** "Files are ready, open CubeMX"
2. **Human → LLM:** "CubeMX generated code, copy the source files"
3. **LLM → Human:** "Source files ready, configure CubeIDE"
4. **Human → LLM:** "Build succeeded, write the next code"
5. **LLM → Human:** "Code updated, rebuild and test"

### TLDR Sequence Table

Every procedure document should start with a **TLDR Sequence Table** showing the alternating workflow. **Artifact capture points must be explicit rows** marked with `→ ARTIFACT` to make them impossible to miss:

```markdown
## TLDR - Execution Sequence

| Step | Who | Task |
|------|-----|------|
| 1 | LLM | Create folders, copy .ioc |
| 2 | HUMAN | CubeMX: Save As → Generate |
| 3 | LLM | Copy lib/, src/, update scripts |
| 4 | HUMAN | CubeIDE: Import, configure, build |
| 5 | HUMAN | Renode: Run simulation |
| → | **ARTIFACT** | **A1:** Screenshot of [expected output] |
| 6 | LLM | Write additional code |
| 7 | HUMAN | Rebuild, Renode: Test |
| → | **ARTIFACT** | **A2:** Screenshot of [expected output] |
```

This table provides:
- **At-a-glance understanding** of the full workflow
- **Clear ownership** of each step
- **Explicit artifact rows** that stand out visually
- **No confusion** about when to capture artifacts

### Artifact Tracking - Shared Responsibility

**IMPORTANT:** Both the human AND the LLM must track artifacts throughout the workflow:

**LLM Responsibilities:**
- Identify all artifacts from the PDF during analysis
- Insert explicit `→ ARTIFACT` rows in the sequence table
- Remind the human when an artifact capture point is reached
- Update findings document when artifacts are captured
- Track artifact status in the execution log

**Human Responsibilities:**
- Capture screenshots at marked artifact points
- Save artifacts with clear filenames
- Inform LLM when artifacts are captured
- Provide artifact file locations for findings document

### Artifact Identification

When creating procedure documents, identify artifacts by looking for:

1. **Explicit mentions** in the PDF:
   - "Take a screenshot" → Screenshot artifact
   - "This is Artifact X" → Named artifact
   - "Include in report" → Required submission item

2. **Assign consistent IDs:**
   - `A1, A2, A3...` for screenshots/visual artifacts
   - `Code` or `C1, C2...` for code snippets

3. **Document expected output** - What should each artifact show?

4. **Mirror in findings document** - Every artifact in procedure must appear in `lab{XX}_findings.md`

---

## Analysis Workflow

### Phase 1: Document Ingestion

When given a lab/project PDF or description:

1. **Read all pages** of the PDF document
2. **Check for supplementary materials** (images, whiteboard photos, reference projects)
3. **Identify the source/reference project** if one is mentioned (e.g., `cc1s_uart_redirect`)
4. **Verify source project exists** in `/opt/proj_mp/`

### Phase 2: Task Extraction

Extract and categorize all tasks:

```
For each task in the document:
  1. Identify the action (create, copy, edit, build, run, etc.)
  2. Identify the tool required (filesystem, CubeMX, CubeIDE, Renode, terminal)
  3. Classify as AUTOMATABLE or HUMAN-REQUIRED
  4. Note any dependencies on previous tasks
  5. Identify required artifacts (screenshots, code, answers)
```

### Phase 3: Create Procedure Document

Generate `lab{XX}_procedure.md` or `proj{XX}_procedure.md`:

1. List all tasks with classification
2. Detail Claude Code automated tasks
3. Provide step-by-step human GUI instructions
4. Include all copy-paste commands (terminal and Renode)
5. Create submission checklist

### Phase 4: Create Findings Document

Generate `lab{XX}_findings.md` or `proj{XX}_findings.md`:

1. List all required artifacts
2. Create placeholder sections for each
3. Map artifacts to submission requirements
4. Leave space for user to fill in

### Phase 5: Execute Automation (on request)

Only when user requests, execute automatable tasks:

1. Create folder structures
2. Copy files
3. Rename files
4. Edit text files (source code, scripts, configs)

---

## Task Classification

### Decision Tree

```
Is the task a file operation (create/copy/rename/edit)?
├── YES: File in USER CODE section of CubeMX-generated file?
│   ├── YES → AUTOMATABLE (but note regeneration risk)
│   └── NO → AUTOMATABLE
└── NO: Does task require a GUI window?
    ├── YES → HUMAN-REQUIRED
    └── NO: Is it an interactive terminal session?
        ├── YES → HUMAN-REQUIRED (but provide copy-paste commands)
        └── NO → AUTOMATABLE
```

### Classification Matrix

| Action | Tool | Classification | Notes |
|--------|------|----------------|-------|
| Create folder | Filesystem | AUTOMATABLE | `mkdir -p` |
| Copy files | Filesystem | AUTOMATABLE | `cp -r` |
| Rename files | Filesystem | AUTOMATABLE | `mv` |
| Edit .c/.h files | Text editor | AUTOMATABLE | Direct file write |
| Edit .resc scripts | Text editor | AUTOMATABLE | Direct file write |
| Edit main.c USER CODE | Text editor | AUTOMATABLE | Safe within markers |
| Open .ioc file | CubeMX | HUMAN-REQUIRED | GUI application |
| Save Project As | CubeMX | HUMAN-REQUIRED | GUI dialog |
| Generate Code | CubeMX | HUMAN-REQUIRED | GUI button |
| Import project | CubeIDE | HUMAN-REQUIRED | GUI wizard |
| Create folder in IDE | CubeIDE | HUMAN-REQUIRED | GUI context menu |
| Add include paths | CubeIDE | HUMAN-REQUIRED | GUI properties |
| Link source files | CubeIDE | HUMAN-REQUIRED | GUI drag-drop |
| Build project | CubeIDE | HUMAN-REQUIRED | GUI button |
| Run debugger | CubeIDE | HUMAN-REQUIRED | GUI interface |
| Start Renode | Terminal/GUI | HUMAN-REQUIRED | GUI app launched from terminal |
| Run .resc script | Renode GUI | HUMAN-REQUIRED | Commands typed in Renode Monitor |
| Interact with Renode | Renode GUI | HUMAN-REQUIRED | UART windows, simulation control |
| Upload to board | CubeIDE/STLink | HUMAN-REQUIRED | Hardware interaction |
| Take screenshot | OS | HUMAN-REQUIRED | Manual capture |

---

## What Claude Code Can Do

### Fully Automatable

1. **Project Structure Setup**
   ```bash
   mkdir -p /opt/proj_mp/project_name/{subproject,lib,src,renode}
   ```

2. **File Operations**
   - Copy reference files
   - Rename files to new project name
   - Edit source code files
   - Update Renode scripts

3. **Documentation Generation**
   - Create procedure documents
   - Create findings document templates
   - Generate step-by-step human guides

4. **Code Writing**
   - Write complete `.c` and `.h` files
   - Modify existing source files
   - Update configurations

### Provide Copy-Paste Commands For

1. **Renode Execution**
   ```bash
   cd /opt/proj_mp/project_name/renode/
   renode
   ```
   ```
   s @debug_project_name.resc
   ```

2. **Submission Preparation**
   ```bash
   cd /opt/proj_mp/
   zip -r project-lastname-firstname.zip project_name/
   ```

---

## What Requires Human Interaction

### CubeMX Operations

**IMPORTANT:** Converting a `.ioc` file into a CubeIDE project ALWAYS requires CubeMX GUI. There is no command-line alternative.

| Operation | Why Manual | Human Steps |
|-----------|------------|-------------|
| Open .ioc | GUI app launch | Double-click .ioc or File→Open |
| Save Project As | Dialog interaction | File→Save Project As→Navigate→Save |
| Configure peripherals | GUI pinout/config | Click pins, set parameters |
| Generate Code | Button click + options | Click GENERATE CODE→Choose action |

### CubeIDE Operations

| Operation | Why Manual | Human Steps |
|-----------|------------|-------------|
| Import project | Wizard interaction | File→Import→Select folder→Finish |
| Create folder | Context menu | Right-click→New→Folder→Name→Finish |
| Add include paths | Properties dialog | Properties→C/C++ General→Paths and Symbols→Add |
| Link files | Drag-drop + dialog | Drag files→Drop→Select "Link to files" |
| Build | Button click | Click hammer icon (or Ctrl+B) |
| Debug | Launch config | Click debug icon, configure if needed |

### Renode (Simulation)

**IMPORTANT:** Renode is a GUI application launched from terminal. Claude Code provides copy-paste commands, but the human must execute them and interact with the Renode GUI windows.

| Operation | Why Manual | Human Steps |
|-----------|------------|-------------|
| Start Renode | GUI application | Run `renode` in terminal (opens GUI) |
| Load script | Renode Monitor GUI | Type `s @script.resc` in Monitor window |
| Interact with UART | UART window GUI | Type input, view output in UART window |
| Control simulation | Renode Monitor GUI | Start, pause, reset commands |

### Hardware (Physical Board)

| Operation | Why Manual | Human Steps |
|-----------|------------|-------------|
| Upload to board | Hardware + GUI | Connect USB, click download/debug in CubeIDE |
| Debug on board | Hardware + GUI | Set breakpoints, step through in CubeIDE |
| View serial output | Hardware + terminal | Use serial monitor (minicom, screen, etc.) |

### Other Human Tasks

| Operation | Why Manual | Human Steps |
|-----------|------------|-------------|
| Take screenshots | OS interaction | Use screenshot tool, save file |
| Create PDF report | Document editing | Compile screenshots + code into PDF |
| Zip for submission | File management | Clean build, then zip project folder |

---

## Writing Guidelines for Human Tasks

When documenting human tasks in procedure documents, follow these guidelines:

### Always Use Full System Paths

**IMPORTANT:** When telling humans to copy, link, or navigate to files, always use complete absolute paths from the root filesystem.

**Bad (ambiguous):**
```
Drag these files to the lib_src folder:
- lib/mp_uart_redirect.c
- src/_mp_main.c
```

**Good (unambiguous):**
```
Drag these files to the lib_src folder in CubeIDE:

| Source File (full path) | Destination |
|-------------------------|-------------|
| /opt/proj_mp/project_name/lib/mp_uart_redirect.c | lib_src folder |
| /opt/proj_mp/project_name/src/_mp_main.c | lib_src folder |
```

### Path Table Format

For file operations involving multiple files, use a table format:

| Source (FROM) | Destination (TO) |
|---------------|------------------|
| `/full/path/to/source/file.c` | `/full/path/to/destination/` or `folder in GUI` |

### Why This Matters

- Humans may have multiple terminal windows or file managers open
- Relative paths are ambiguous without context
- Full paths can be copy-pasted directly into file managers
- Prevents confusion between source project and target project files

---

## Creating Procedure Documents

### Template Structure

```markdown
# Lab/Proj {XX} Procedure: {Title}

**Course:** {course}
**Points:** {total}

> **Reference Documents:**
> - [LAB_PROJECT_ANALYSIS_PROCEDURE.md](../LAB_PROJECT_ANALYSIS_PROCEDURE.md)
> - Original PDF: `{filename}.pdf`

---

## Task Classification Summary

| Step | Description | Who Does It |
|------|-------------|-------------|
| ... | ... | CLAUDE CODE / HUMAN |

---

## Part A: Claude Code Automated Tasks

> These tasks are performed by Claude Code. Human verifies completion.

### A.1 {Task}
...

---

## Part B: Human Tasks (GUI Required)

> Follow steps exactly. Copy-paste commands where provided.

### B.1 {Task}
...

---

## Submission Checklist

- [ ] Artifact 1
- [ ] Artifact 2
- [ ] ...
```

---

## Creating Findings Documents

### Template Location

**Use the template at:** `/opt/proj_mp/labs_and_projects/sample_findings.md`

The template contains:
- LLM instructions for adapting to specific labs/projects
- Sections for screenshot artifacts (A1, A2, A3...)
- Sections for code snippet artifacts (C1, C2, C3...)
- Submission checklist and artifact-to-report mapping

### How to Use the Template

1. **Copy** `sample_findings.md` to the lab/project folder
2. **Rename** to `lab{XX}_findings.md` or `proj{XX}_findings.md`
3. **Read** the LLM instruction comments in the template
4. **Adapt** the number of artifact sections based on requirements
5. **Remove** all LLM instruction comments from the final document

### Artifact Types

| Type | ID Format | Description |
|------|-----------|-------------|
| Screenshot | A1, A2, A3... | Screen captures of output, GUI, results |
| Code Snippet | C1, C2, C3... | Source code to include in report |

### Submission Components

Most labs/projects require:
1. **PDF Report** - Contains screenshots and code snippets
2. **ZIP File** - Clean CubeIDE project folder (build artifacts removed)

---

## Report Generation

### Overview

After completing a lab/project, generate a concise report following the 4-section template.

**Reference Documents:**
- [report-template.md](./report-template.md) - Official template with section descriptions
- [report_generation_guide.md](./report_generation_guide.md) - Detailed LLM workflow

### Report Sections

| Section | Content | Length |
|---------|---------|--------|
| Introduction | What the lab teaches, in your own words | 1-2 sentences |
| Narrative | Issues encountered, how resolved | 2-5 sentences |
| Code Snippets and Screenshots | Artifacts with captions | As needed |
| Discussions and Results | Takeaways, learnings | 2-4 bullet points |

### LLM Workflow

1. **Initialize**: At lab start, create `{labXX}_report.md` with template structure
2. **Track**: As artifacts are captured, add markdown links to report
3. **Complete**: After lab completion, fill Introduction, Narrative, and Discussions sections
4. **Keep concise**: Each section should be brief and substantive

### Artifact References in Reports

```markdown
### Artifact A1: Description

![A1 - Brief Title](./a1.png)

*Figure 1: Detailed caption explaining what this shows.*
```

```markdown
### Code: filename.c

**File:** [filename.c](./filename.c)

*Code Snippet 1: What this code does.*
```

---

## Issue Tracking

### When Problems Occur

**FIRST:** Check [known_issues.md](./known_issues.md) - the solution may already be documented.

**If you solve a new issue:**

1. **Document in known_issues.md** with:
   - **Symptom:** What you observed
   - **Cause:** Root cause if known
   - **Solution A (LLM/Command-Line):** How to fix via terminal/automation
   - **Solution B (Human GUI):** How to fix via CubeIDE/CubeMX GUI
   - **Date discovered:** When found
   - **Affected labs/projects:** Which ones this applies to

2. **For complex issues**, add detailed findings to `findings/` folder and reference from known_issues.md

### Issue Categories

| Category | Examples | Where to Document |
|----------|----------|-------------------|
| Build errors | Include paths, missing files | known_issues.md |
| CubeIDE quirks | Folder settings, import problems | known_issues.md |
| CubeMX issues | Code generation, project conversion | known_issues.md |
| Renode problems | Script paths, peripheral config | known_issues.md |
| Complex investigations | Multi-step debugging, research | findings/ folder |

### Known Issue Template

```markdown
### Issue: [Brief description]

**Symptom:** [What you observe]

**Cause:** [Root cause if known]

**Solution A: LLM/Command-Line Fix**
[Steps for automation/terminal fix]

**Solution B: Human GUI Fix**
[Steps for GUI fix in CubeIDE/CubeMX]

**Date discovered:** YYYY-MM-DD
**Affected labs/projects:** [list]
```

---

## Common Patterns

### Pattern: Copy-and-Modify Project

1. Copy structure from reference project → CLAUDE CODE
2. Rename files to new project name → CLAUDE CODE
3. Update .ioc via CubeMX Save As → HUMAN
4. Generate code → HUMAN
5. Import to CubeIDE → HUMAN
6. Add user code → CLAUDE CODE
7. Build and test → HUMAN

### Pattern: Code Modification Only

1. Edit source file → CLAUDE CODE
2. Rebuild → HUMAN
3. Test → HUMAN

---

## Terminology Reference

### Hardware Terms

| Term | Meaning |
|------|---------|
| MCU | Microcontroller Unit (the chip) |
| MPB | Microprocessor Board (the development board) |
| Board | Same as MPB - the physical hardware |
| Upload to board | Flash/program the MCU with compiled code |
| F412dsc | STM32F412 Discovery board |
| G431n32 | STM32G431 Nucleo-32 board |

### Software Terms

| Term | Meaning |
|------|---------|
| .ioc | CubeMX Input/Output Configuration file |
| .elf | Executable and Linkable Format - the compiled binary |
| .resc | Renode script file |
| HAL | Hardware Abstraction Layer (ST's driver library) |
| USER CODE | Safe zones in generated files for custom code |

### Project Naming Convention

Format: `ccXY_project_name_board`

- `cc` = Related to lecture
- `X` = Type (4 = runs on Renode)
- `Y` = Class (d = needs Debug config)
- `_board` = Target hardware (f412dsc, g431n32)

---

## Checklist: Analyzing a New Lab/Project

When asked to analyze a new lab or project:

- [ ] Read the PDF completely
- [ ] Check for whiteboard images or supplementary files
- [ ] Identify the reference/source project
- [ ] Verify source project exists in `/opt/proj_mp/`
- [ ] List all tasks from the document
- [ ] Classify each task (AUTOMATABLE vs HUMAN)
- [ ] Identify all required artifacts
- [ ] Create `lab{XX}_procedure.md` or `proj{XX}_procedure.md`
- [ ] Create `lab{XX}_findings.md` or `proj{XX}_findings.md`
- [ ] Wait for user to request automation execution
