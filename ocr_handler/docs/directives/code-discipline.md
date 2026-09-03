# Code discipline

**WHEN** adding a module → **DON'T** exceed ~300 lines → **BECAUSE** past that it is doing two jobs and nobody re-reads it.

**WHEN** a page already has a text layer → **DON'T** run a model over it → **BECAUSE** extraction is exact and recognition is lossy. Check first; it is one function call.

**WHEN** picking a constant → **DON'T** guess → **BECAUSE** a swept and documented value survives review. Every tuned constant here names the measurement that produced it.

**WHEN** tempted to add a CLI flag → **DON'T** → **BECAUSE** the brief is `file`, `page`, procedure, format. Options are where small tools go to die.

**WHEN** a model would be convenient → **DON'T** reach for it before the deterministic path is exhausted → **BECAUSE** `pdfops` and `ink` must keep working with no GPU.

**WHEN** sorting spatial items → **DON'T** sort by `(y, x)` → **BECAUSE** side-by-side items rarely share a top edge and come back reversed. Band by vertical overlap first. Cost us a silently reversed equation.
