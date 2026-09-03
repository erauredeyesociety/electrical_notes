# Roadmap

Lean milestones and file-path refs only. Design detail lives in `plans/`, findings in `findings/`, external teardowns in `research/`.

---

> Session detail lives in [`archives/session_records/`](archives/session_records/INDEX.md). This file stays an index.

## M1 — Non-ML backbone ✅ done

Classify, render, separate ink, crop regions. No GPU anywhere.

- `src/ocr_handler/pdfops.py` — inspect / producer / render / pair
- `src/ocr_handler/ink.py` — colour + diff masks, region grouping, crop
- Verified on real lectures — see [`archives/session_records/2026-09-02_initialize-and-teardown.md`](archives/session_records/2026-09-02_initialize-and-teardown.md)

## M2 — Emit and CLI  ← next

- `emit.py` — Markdown and LaTeX from one intermediate
- `cli.py` — `file`, `page`, procedure, `--format latex|markdown`
- **Must-not-break:** page classification and reading order. Both have a test in `tests/persistent/`.

## M1b — PyMuPDF migration  ← inserted by research

Structural ink extraction makes this worth doing before M2. See [`research/INDEX.md`](research/INDEX.md).

- `pdfops.py` on PyMuPDF; drop poppler subprocess calls
- `ink.structural_regions()` — annotation images by count-difference against the base

## M3 — Recognition

**Engine not chosen — three candidates measured, decide by head-to-head.** See [`research/INDEX.md`](research/INDEX.md).

- `recognize.py` — image region → LaTeX, behind one swappable interface so the loser is cheap to replace

## M4 — Assembly

Final PDF with equations as text and figures embedded; intermediate crops deletable afterwards.

## M5 — Batch

Directory in, documents out. Only after one document works end to end.

---

## Deferred frontier

Generalising beyond this course's material. Captured, deliberately sequenced last — see [`scope.md`](scope.md) blacklist.

---

## Scripts

- Install: `uv sync`
- Test: `uv run pytest tests/persistent/`
- No deploy target; this is a local tool.
