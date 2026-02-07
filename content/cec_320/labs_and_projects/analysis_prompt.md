# Lab/Project Analysis Prompt

**Purpose:** Copy and paste the prompt below to Claude or another LLM to analyze a new lab or project manual.

---

## Prerequisites (User Does This First)

1. **Place the manual PDF** in the labs_and_projects folder (the LLM will create the lab/project subfolder)

2. **Copy the prompt** below and paste it to the LLM.

---

## The Analysis Prompt

Copy everything below this line:

---

```
Please analyze the lab/project manual I'm providing and generate documentation.

## Reference Documents (READ THESE FIRST)

1. **Analysis Procedure:** `~/electrical_notes/content/cec_320/labs_and_projects/LAB_PROJECT_ANALYSIS_PROCEDURE.md`
   - Contains the full analysis methodology
   - Task classification rules (AUTOMATABLE vs HUMAN-REQUIRED)
   - Document templates and structure

2. **System Analysis:** `~/electrical_notes/content/cec_320/labs_and_projects/SYSTEM_ANALYSIS.md`
   - Environment setup details
   - Tool locations and paths
   - Project folder structure

3. **Findings Template:** `~/electrical_notes/content/cec_320/labs_and_projects/sample_findings.md`
   - Template for creating findings documents
   - Contains LLM instructions for adapting the template

4. **Known Issues:** `~/electrical_notes/content/cec_320/labs_and_projects/known_issues.md`
   - **REFERENCE IF STUCK:** Contains documented solutions for common issues
   - **UPDATE WHEN ISSUES OCCUR:** Add new issues and their solutions here
   - Includes both LLM/command-line and human GUI fix methods

5. **Report Generation Guide:** `~/electrical_notes/content/cec_320/labs_and_projects/report_generation_guide.md`
   - How to generate concise reports
   - Artifact reference format
   - 4-section template explanation

6. **Known Base Projects:** `~/electrical_notes/content/cec_320/labs_and_projects/known_base_projects.md`
   - Documents base projects that labs/projects build upon
   - Check if the manual references a known base project
   - Contains structure, build configs, and setup notes for each base project

## Input Materials

- **Manual location:** ~/electrical_notes/content/cec_320/labs_and_projects/
- **Manual filename:** {filename}.pdf
- **Supplementary files:** {list any images or additional files, or "none"}

## Your Tasks

### 1. Initialize Lab/Project Folder

Create the documentation folder structure:

```bash
# For labs:
mkdir -p ~/electrical_notes/content/cec_320/labs_and_projects/lab{XX}/

# For projects:
mkdir -p ~/electrical_notes/content/cec_320/labs_and_projects/proj{XX}/
```

Move the PDF into the folder:
```bash
mv ~/electrical_notes/content/cec_320/labs_and_projects/{manual}.pdf \
   ~/electrical_notes/content/cec_320/labs_and_projects/{lab_or_proj}{XX}/
```

### 2. Read and Analyze the Manual

- Read all pages of the PDF
- Identify all tasks and their point values
- List all required artifacts (screenshots, code snippets)
- Identify the source/reference project if mentioned
- Verify the source project exists in /opt/proj_mp/

### 3. Create the Procedure Document

**Save to:** `~/electrical_notes/content/cec_320/labs_and_projects/{lab_or_proj}{XX}/{lab_or_proj}{XX}_procedure.md`

**Include:**
- Task classification summary (CLAUDE CODE vs HUMAN for each step)
- Part A: Claude Code automated tasks (what automation will do)
- Part B: Human tasks with step-by-step GUI instructions
- All copy-paste commands (terminal commands, Renode Monitor commands)
- Submission checklist

**Important notes for procedure:**
- All CubeIDE/CubeMX projects go in `/opt/proj_mp/` (not in labs_and_projects/)
- Documentation and reports go in `~/electrical_notes/content/cec_320/labs_and_projects/`
- Renode is a GUI app - provide terminal commands AND Renode Monitor commands separately
- .ioc to project conversion ALWAYS requires CubeMX GUI
- Use full system paths (e.g., `/opt/proj_mp/project_name/`)

### 4. Create the Findings Document

**Template:** COPY `~/electrical_notes/content/cec_320/labs_and_projects/sample_findings.md`

**Save to:** `~/electrical_notes/content/cec_320/labs_and_projects/{lab_or_proj}{XX}/{lab_or_proj}{XX}_findings.md`

**Adapt the template:**
- Read the LLM instructions in the template
- Add/remove artifact sections based on actual requirements
- Screenshots = A1, A2, A3...
- Code snippets = C1, C2, C3...
- Update submission section with exact naming conventions from manual
- REMOVE all LLM instruction comments from final document

### 5. Initialize the Report File

**Save to:** `~/electrical_notes/content/cec_320/labs_and_projects/{lab_or_proj}{XX}/{lab_or_proj}{XX}_report.md`

Create the report skeleton per [report_generation_guide.md](./report_generation_guide.md):
- Header with course, dates
- Empty sections: Introduction, Narrative, Code Snippets and Screenshots, Discussions and Results
- Report will be filled in as the lab progresses

### 6. DO NOT Execute Automation Yet

- Only create the documentation
- I will review the documents
- Then I will request automation execution separately

## Issue Tracking

**During execution, if you encounter issues:**

1. **Check known_issues.md first** - The solution may already be documented
2. **If you solve a new issue**, document it in known_issues.md:
   - Symptom (what you observed)
   - Cause (root cause if known)
   - Solution (both LLM/command-line AND human GUI methods)
   - Date discovered, affected labs/projects
3. **For complex issues**, add detailed findings to `~/electrical_notes/content/cec_320/labs_and_projects/findings/`

## Output Summary

When done, provide:
1. Confirmation that folder was created and documents were created
2. List of identified artifacts
3. List of automatable vs human tasks
4. Any questions or ambiguities found in the manual
5. Note any potential issues to watch for (check known_issues.md for similar patterns)
```

---

## Quick Prompts

### If Context is Already Established

```
The lab{XX} manual is at ~/electrical_notes/content/cec_320/labs_and_projects/{manual}.pdf

Please:
1. Read ~/electrical_notes/content/cec_320/labs_and_projects/LAB_PROJECT_ANALYSIS_PROCEDURE.md
2. Read ~/electrical_notes/content/cec_320/labs_and_projects/known_issues.md (for reference)
3. Create lab{XX}/ folder and move the PDF
4. Analyze the manual
5. Create lab{XX}_procedure.md, lab{XX}_findings.md, and lab{XX}_report.md
```

### For Projects

```
The proj{XX} manual is at ~/electrical_notes/content/cec_320/labs_and_projects/{manual}.pdf

Please:
1. Read ~/electrical_notes/content/cec_320/labs_and_projects/LAB_PROJECT_ANALYSIS_PROCEDURE.md
2. Read ~/electrical_notes/content/cec_320/labs_and_projects/known_issues.md (for reference)
3. Create proj{XX}/ folder and move the PDF
4. Analyze the manual
5. Create proj{XX}_procedure.md, proj{XX}_findings.md, and proj{XX}_report.md
```

---

## After Analysis

### To Execute Automation

```
Please execute the automatable tasks (Part A) from ~/electrical_notes/content/cec_320/labs_and_projects/lab{XX}/lab{XX}_procedure.md

The target project should be created at /opt/proj_mp/{project_name}/

Remember: Check known_issues.md if you encounter any problems.
```

### To Update Findings and Report

```
I completed artifact A{X}. The screenshot is saved to ~/electrical_notes/content/cec_320/labs_and_projects/lab{XX}/a{X}.png

Please update both:
- lab{XX}_findings.md (artifact tracking)
- lab{XX}_report.md (add to Code Snippets and Screenshots section)
```

### To Document a New Issue

```
I encountered an issue during the lab:

[Describe the issue]

Please:
1. Check if this is already in known_issues.md
2. If not, add it with both LLM/command-line and human GUI solutions
3. If it's complex, create a detailed writeup in findings/
```

### To Re-analyze

```
Please re-analyze the manual in ~/electrical_notes/content/cec_320/labs_and_projects/lab{XX}/
Additional context: {your notes}
```

---

## Key Paths Reference

| Item | Path |
|------|------|
| Project root (CubeIDE projects) | `/opt/proj_mp/` |
| Documentation root | `~/electrical_notes/content/cec_320/labs_and_projects/` |
| Analysis procedure | `~/electrical_notes/content/cec_320/labs_and_projects/LAB_PROJECT_ANALYSIS_PROCEDURE.md` |
| System analysis | `~/electrical_notes/content/cec_320/labs_and_projects/SYSTEM_ANALYSIS.md` |
| **Known issues** | `~/electrical_notes/content/cec_320/labs_and_projects/known_issues.md` |
| **Known base projects** | `~/electrical_notes/content/cec_320/labs_and_projects/known_base_projects.md` |
| **Findings folder** | `~/electrical_notes/content/cec_320/labs_and_projects/findings/` |
| Report guide | `~/electrical_notes/content/cec_320/labs_and_projects/report_generation_guide.md` |
| Findings template | `~/electrical_notes/content/cec_320/labs_and_projects/sample_findings.md` |
| Lab docs | `~/electrical_notes/content/cec_320/labs_and_projects/lab{XX}/` |
| Project docs | `~/electrical_notes/content/cec_320/labs_and_projects/proj{XX}/` |
| Actual CubeIDE projects | `/opt/proj_mp/{project_name}/` |

---

## File Initialization Checklist

When starting a new lab/project, the LLM should create:

- [ ] `lab{XX}/` or `proj{XX}/` folder
- [ ] Move PDF into folder
- [ ] `lab{XX}_procedure.md` - Step-by-step procedure
- [ ] `lab{XX}_findings.md` - Artifact tracking
- [ ] `lab{XX}_report.md` - Report skeleton (4 sections)

During execution:
- [ ] Reference `known_issues.md` when problems occur
- [ ] Update `known_issues.md` with new issues and solutions
- [ ] Add complex findings to `findings/` folder
- [ ] Update report as artifacts are collected
