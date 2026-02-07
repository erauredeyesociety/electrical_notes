# Sample Findings Template

<!--
================================================================================
LLM INSTRUCTIONS - READ THIS SECTION CAREFULLY
================================================================================

This is a TEMPLATE for creating findings documents. When analyzing a lab or
project, COPY this template to the appropriate folder and RESTRUCTURE it based
on the actual artifacts required.

LOCATION: Copy to /opt/proj_mp/labs_and_projects/lab{XX}/lab{XX}_findings.md
      or: Copy to /opt/proj_mp/labs_and_projects/proj{XX}/proj{XX}_findings.md

HOW TO ADAPT THIS TEMPLATE:

1. ARTIFACT COUNT:
   - Count the actual artifacts required in the lab/project manual
   - Add or remove artifact sections as needed
   - Each artifact gets its own section with the same structure
   - IMPORTANT: Each artifact in the manual is a SEPARATE deliverable.
     Never combine or merge artifacts, even if two artifacts appear to
     capture the same output. Follow the manual to the letter.
   - Each artifact screenshot should show INCREMENTAL progress — only the
     current task implemented, with subsequent tests still failing. This
     proves work was done one task at a time.

2. ARTIFACT TYPES:
   - Screenshots: Use the "Screenshot Artifact" section format
   - Code Snippets: Use the "Code Snippet Artifact" section format
   - If an artifact is both (screenshot of code), use Screenshot format

3. SUBMISSION REQUIREMENTS:
   - Update the submission section based on what the manual requires
   - Common submissions: PDF report, ZIP of project folder
   - Note the exact naming convention from the manual

4. ARTIFACT FILE STORAGE:
   - Every artifact must also exist as an individual file in the lab/project folder
   - Screenshots: saved as {id}.png (e.g., a1a.png, a2a.png) by the human
   - Code snippets: saved as {id}.c (e.g., a1b.c, a2b.c) by the LLM
   - Code snippet .c files are incomplete snippets — just the relevant function(s)
   - The LLM creates code snippet files when populating the findings/report
   - See LAB_PROJECT_ANALYSIS_PROCEDURE.md → "Artifact File Storage" for full details

5. REMOVE ALL LLM INSTRUCTION COMMENTS:
   - Delete all <!-- comment --> blocks when creating the actual findings doc
   - The final document should be clean for the student to fill in

6. PLACEHOLDERS:
   - Replace {XX} with the lab/project number (e.g., 01, 02)
   - Replace {Title} with the actual lab/project title
   - Replace {Course} with the course code
   - Replace all other {placeholders} with actual values

================================================================================
END LLM INSTRUCTIONS
================================================================================
-->

# Lab/Proj {XX} Findings: {Title}

**Course:** {Course}
**Student:** ____________________
**Date:** ____________________

> **Related Documents:**
> - Procedure: [lab{XX}_procedure.md](./lab{XX}_procedure.md)
> - Original Manual: `{manual_filename}.pdf`

---

## Artifact Summary

<!--
LLM: Create one row per required artifact. Adjust the table based on actual requirements.
Common artifact types: Screenshot, Code Snippet
-->

| ID | Type | Description | Required For | Status |
|----|------|-------------|--------------|--------|
| A1 | Screenshot | {description} | Task {X} ({Y} pts) | [ ] |
| A2 | Screenshot | {description} | Task {X} ({Y} pts) | [ ] |
| C1 | Code | {filename} | Task {X} ({Y} pts) | [ ] |

<!--
LLM: Add or remove rows as needed. Use IDs like:
- A1, A2, A3... for screenshots (Artifacts)
- C1, C2, C3... for code snippets (Code)
-->

---

## Screenshot Artifacts

<!--
LLM: Create one section per screenshot artifact. Copy this block for each screenshot required.
-->

### A1: {Description}

**Required for:** Task {X} - {task_description} ({Y} pts)

**What to capture:**
<!-- LLM: Describe exactly what should be in the screenshot based on the manual -->
- {specific item 1}
- {specific item 2}

**Screenshot:**
<!-- Student: Paste screenshot here or note file path -->
```
[Paste screenshot or drag image file here]
```

**File saved to:** ____________________

**Notes:**
<!-- Student: Any observations, issues, or additional context -->


---

<!--
LLM: Repeat the above section for each screenshot artifact (A2, A3, etc.)
Example for A2:

### A2: {Description}

**Required for:** Task {X} - {task_description} ({Y} pts)

**What to capture:**
- {specific item 1}

**Screenshot:**
```
[Paste screenshot or drag image file here]
```

**File saved to:** ____________________

**Notes:**

---
-->

## Code Snippet Artifacts

<!--
LLM: Create one section per code file that needs to be included in the report.
-->

### C1: {filename}

**Required for:** Task {X} - {task_description} ({Y} pts)

**File path:** `/opt/proj_mp/{project_name}/{path_to_file}`

**Code:**
<!-- Student: Paste the final code here for the report -->
```c
// Paste your code here

```

**Notes:**
<!-- Student: Any explanations about the code -->


---

<!--
LLM: Repeat for each code snippet (C2, C3, etc.)
-->

## Submission Checklist

<!--
LLM: Update this section based on the actual submission requirements from the manual.
Include exact file naming conventions specified in the manual.
-->

### PDF Report

**Filename:** `{prefix}-report-{lastname}-{firstname}.pdf`

**Required contents:**
- [ ] A1: {description}
- [ ] A2: {description}
- [ ] C1: {filename} code

<!--
LLM: List all artifacts that go in the PDF report
-->

### Project ZIP

**Filename:** `{prefix}-proj-{lastname}-{firstname}.zip`

**Before zipping:**
1. In CubeIDE: Right-click project → **Build Configurations → Clean All**
2. Verify no Debug/ or Release/ build artifacts remain

**Project location:** `/opt/proj_mp/{project_name}/`

**Zip command:**
```bash
cd /opt/proj_mp/
zip -r {prefix}-proj-{lastname}-{firstname}.zip {project_name}/
```

---

## Artifact-to-Report Mapping

<!--
LLM: Create a clear mapping of which artifacts go where in the final report.
-->

| Report Section | Artifact ID | Description |
|----------------|-------------|-------------|
| Source Code | C1 | {filename} |
| Screenshot 1 | A1 | {description} |
| Screenshot 2 | A2 | {description} |

---

## Notes and Observations

<!-- Student: Use this section for any additional notes -->

### Issues Encountered


### Solutions Applied


### Questions for TA/Instructor


---

<!--
================================================================================
LLM FINAL CHECKLIST - Verify before saving the findings document:
================================================================================

[ ] Replaced all {placeholders} with actual values
[ ] Correct number of screenshot artifact sections (A1, A2, ...)
[ ] Correct number of code snippet sections (C1, C2, ...)
[ ] Artifact Summary table matches the sections
[ ] Submission filenames match the manual's naming convention
[ ] All file paths use full system paths (/opt/proj_mp/...)
[ ] Removed all LLM instruction comments
[ ] Document is clean and ready for student use

================================================================================
-->
