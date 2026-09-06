# Session records — INDEX

Dated per-session narrative, `YYYY-MM-DD_<description>.md`. Immutable: written once, not revised.
Records rotate to [../archives/session_records/](../archives/session_records/INDEX.md) when stale.

| Date | Session | Outcome |
| --- | --- | --- |
| [2026-09-06](./2026-09-06_repair-audit-recall-and-validity.md) | **Part 1** — the repair audit, the recall fix, the validity gate<br>**Part 2** (appended, same session) — M2 converged, the mask question closed, the recall result audited | MinerU's repair suite **audited and rejected** — 11 defects; over our own outputs it changes 4 of 44 UniMERNet and 6 of 6 PaddleOCR-VL readings, and **every change is damage**. `ocr-handler check` ships the engine-agnostic acceptance gate. Recall 35.3% → **68.2%** with strict precision *rising* 84.8% → **93.1%** — and the standing hypothesis about why recall was low turned out half wrong. **Part 2:** M2 delivered (the `482 blank pages` figure was a conflation — really **24**; 406 of them carry vector content); the `/Ink`-vs-raster contradiction **closed** after blocking M4 for days (it is rasters, 0 `/Subtype/Ink`); the mask survives all three strata but P1's constants erode P3's ink by **67–77%**; and an adversarial replication found the recall change's priced cost understated by 43% — *"no true positive lost"* is false corpus-wide. |
| 2026-09-02 | Initialize, build the backbone, tear down Baidu Unlimited-OCR | Rotated → [../archives/session_records/2026-09-02_initialize-and-teardown.md](../archives/session_records/2026-09-02_initialize-and-teardown.md) |

---

## ✅ The `session_records/` vs `archives/session_records/` question — settled 2026-09-06

This folder's previous INDEX said it was empty because a convention was never settled, and deferred to
the operator. **Resolved in favour of this folder**, matching the parent tree. The contradiction is in
the bootstrap, not here: `guides/DOCUMENTATION_STANDARDS.md` (lines 35, 252–253) specifies live records
here **rotating into** `archives/`, while `PROMPTS.md` § Save Progress writes directly to `archives/`.
The lifecycle version wins — the prompt cites that guide as its own authority, and writing straight to
`archives/` would mean nothing is ever live.

The 2026-09-02 record stays in `archives/`: it is genuinely stale, so that is where it belongs anyway.
Full reasoning and the upstream note: [parent INDEX](../../../docs/session_records/INDEX.md).
Tracked in [../plans/doctrine-compliance.md](../plans/doctrine-compliance.md) § C, now closed.
