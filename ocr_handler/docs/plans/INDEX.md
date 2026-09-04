# Plans — INDEX

Tactical *how* artifacts. The roadmap points here by path; detail never goes in the roadmap.

**Naming.** A point-in-time plan (a sprint plan, a trade study) is dated `YYYY-MM-DD-<slug>.md`. A
**living document** that is continuously updated is named by concept only — a date in the filename of a
document that never stops changing invites a dated near-duplicate later.

Delivered plans move to [../archives/plans/](../archives/plans/INDEX.md).

| File | Type | Summary |
| --- | --- | --- |
| [text-layer-first.md](./text-layer-first.md) | ACTIVE-SPEC | **Start here for M2.** The four-mode extraction contract — `text` / `ocr` / `both` / `auto` — with the CLI surface, the JSONL intermediate, the side-by-side comparison view, the five signals a reviewer uses to decide which output is better, and the three distinct "OCR returned nothing" cases. Grounded in the corpus census: 67% of pages need no recognition, and 482 pages must never be sent to a model at all. Ends with six open questions it deliberately does not answer. |
| [doctrine-compliance.md](./doctrine-compliance.md) | ACTIVE-SPEC | The bootstrap-doctrine gap list as a checklist with file paths. Skeleton is right; the memory folders were empty and the test floor protects the wrong code path. Four integrity items to do first — an untracked module, an untested CLI, two live classifiers for one concept, and a success fixture that is not in the repository. |
