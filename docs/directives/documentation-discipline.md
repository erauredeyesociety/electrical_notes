# Documentation Discipline

**WHEN** you learn something durable about this repo → **DON'T** leave it in a root-level `tmp*.md` →
**BECAUSE** this repo already proved the failure mode: `tmp_ocr_child.md` sat in the repository root
holding `/Ink`-object measurements recorded nowhere else, and `ocr_handler`'s own directives had to name
it as the anti-pattern ([../../ocr_handler/docs/directives/documentation-discipline.md](../../ocr_handler/docs/directives/documentation-discipline.md)).
Four such files are still in the root today — see [../DRIFT_REPORT.md](../DRIFT_REPORT.md) § 3.

**Route by type — the load-bearing split is INTERNAL vs EXTERNAL:**

| Content | Folder |
| --- | --- |
| Discoveries about **this repo** — its layout, its build, its own scripts, its Hugo config (path:line) | [`docs/findings/`](../findings/INDEX.md) |
| Teardowns of things **outside** this repo — Hugo/hextra, tectonic, pandoc, upstream tools | [`docs/research/`](../research/INDEX.md) |
| Prescriptive rules distilled from our own experience, WHEN→DON'T→BECAUSE | [`docs/lessons_learned/`](../lessons_learned/INDEX.md) |
| Why a choice was made | [`docs/decisions/`](../decisions/INDEX.md) — immutable ADRs; supersede with a new one, never edit |
| Tactical how-to for work not yet done | [`docs/plans/`](../plans/INDEX.md) |
| Repeatable operator procedures — build the site, build a `.tex`, extract a PDF | [`docs/runbooks/`](../runbooks/INDEX.md) |
| Standing rules for how to work here | [`docs/directives/`](./INDEX.md) |
| Dated per-session narrative | [`docs/session_records/`](../session_records/INDEX.md) → [`archives/session_records/`](../archives/session_records/INDEX.md) when stale |

- **Three doc trees, and they do not mix.** Root `docs/` governs the repo as a whole.
  `ocr_handler/docs/` and `docs-rag/` govern their own child projects. **Per-course** `reference_docs/`
  folders (`content/<course>/reference_docs/` for the shared macros;
  `content/cesc_410/labs_and_projects/reference_docs/` for lab-specific material) hold
  course-local material — templates, macros, submission rules — and stay there because they ship
  alongside the coursework they serve. Never copy between trees; **cite by path**.
- **Never the repository root.** The only permitted root `.md` is `README.md`. `tmp*.md` is tolerated by
  the hub guide as *scratch*; it is not a home for measurements, requirements, or operator direction.
- **Supersede in place; name by concept, not by date.** Before writing a new doc, grep `docs/` for the
  concept and update the existing file at its existing path. Dated siblings guarantee bloat. Things that
  stay dated and immutable: ADRs, session records, archived roadmaps, archived operator notes.
- **Cite, don't recopy.** A finding about the LaTeX workflow cites
  `docs/latex/build_tex.sh` and `content/cesc_410/hw/reference_docs/hw_workflow.md` by path. It does not
  restate them — they change, and the copy will not.
- **Every docs folder has an `INDEX.md`.** Add it in the same pass that creates the folder, never later.
- **A doc is only formal after the thing it describes is stable.** During active development, write
  findings, ADRs and session records — not user guides for a workflow still being invented.
- **Contradictions are recorded, not resolved by preference.** Where a per-course `reference_docs/` rule
  and a root directive disagree, write both down in `docs/findings/` and name which one is authoritative
  for which folder.

Hub: `~/llm-project-bootstrap/directives/documentation-discipline.md` → guide `DOCUMENTATION_STANDARDS.md`
