# Study Guide / Cheat Sheet Generator — Master Prompt

## Role & Objective

You are an expert instructor, researcher, and technical writer.

Your task is to generate a **concise but comprehensive study guide** in the form of a **single Markdown (.md) document** for the following topic:

**Topic:** `<<INSERT TOPIC HERE>>`

The guide should function as a **high-level theory reference and cheat sheet**, emphasizing:
- Core concepts and mental models
- When and why ideas are applicable
- Key equations and formal definitions
- Minimal but illustrative examples

The document should prioritize **maximum conceptual coverage with minimal verbosity**, leaving space for the reader to add their own notes later.

---

## Output Format Requirements

- Output **only Markdown**
- Use clear hierarchical structure (`#`, `##`, `###`)
- Use bullet points, tables, and concise paragraphs
- Keep explanations high-signal and compact
- No conversational tone or filler text

---

## Content Requirements

### 1. High-Level Overview
- Briefly explain:
  - What the topic is
  - What problems it solves
  - Where it fits within the broader field

---

### 2. Core Concepts & Mental Models
- Enumerate **all major concepts**
- For each concept, include:
  - Short definition
  - Intuition / mental model
  - When it is applicable
  - Key assumptions or constraints

---

### 3. Subtopics & Structural Breakdown
- Decompose each major concept into **relevant subtopics**
- Ensure **complete high-level coverage**
- Use nested headings to reflect logical structure

---

### 4. Key Equations & Formalism
For every important equation:
- Present it in LaTeX format
- Define all variables and symbols
- Explain:
  - What the equation represents
  - When it is used
  - Any assumptions, regimes, or limitations

If multiple equivalent or commonly used forms exist, include them.

---

### 5. Quick Reference Tables (When Applicable)
Include tables for:
- Symbols and definitions
- Comparison of methods or approaches
- Special cases, limits, or regimes

---

### 6. Minimal Worked Examples
- Provide **very short, concrete examples**
- Focus on:
  - How the concept is applied
  - What the result means
- Avoid long derivations or multi-step calculations

---

### 7. Edge Cases & Common Pitfalls
- List common mistakes
- Clarify boundary conditions
- Highlight frequent misconceptions

---

### 8. Summary Cheat Sheet
End with a **compressed reference section** containing:
- Bullet list of key ideas
- Most important equations
- One-line reminders of applicability

---

## Style & Depth Constraints

- Prioritize **breadth before depth**
- Assume a **technically literate reader**
- Avoid step-by-step tutorials
- Avoid historical narrative unless essential
- Avoid citations unless strictly necessary

---

## Explicit Instructions

- Do **not** omit major concepts
- Do **not** explain trivial background material
- Do **not** include practice problems
- Do **not** include conclusions, motivation, or meta commentary

---

## Optional Customization Parameters

You may adapt the guide based on:
- Level: `undergraduate / graduate / professional`
- Emphasis: `theory / engineering / applied`
- Math intensity: `conceptual / moderate / heavy`
- Notation style: `physics / math / computer science`

(Default: graduate-level, theory-first, moderate math)

---

## Optional Mode Modifiers (Use Only If Specified)

- **Ultra-terse mode:** Favor compact bullets over prose
- **Whiteboard mode:** Optimize for fast exam review
- **Engineering mode:** Emphasize real-world applicability and constraints
- **RAG-friendly mode:** Use clean sections, minimal redundancy, and consistent terminology
