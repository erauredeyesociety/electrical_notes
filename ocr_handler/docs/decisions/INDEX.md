# Decisions — ADRs

One-screen records of *why*. **ADRs are immutable** — write a new one to supersede, never edit an old
one. A wrong idea is kept together with the reason it lost, so nobody re-attempts it.

| ADR | Decision | Status |
| --- | --- | --- |
| [0001](./0001-pymupdf-is-the-only-pdf-library.md) | PyMuPDF is the only PDF library | Accepted — **not yet satisfied**; `pdfops.py` still uses poppler |
| [0002](./0002-numpy-scipy-pillow-not-opencv.md) | numpy + scipy + Pillow, not OpenCV or scikit-image | Accepted |
| [0003](./0003-text-layer-first-and-one-extractor.md) | Text-layer first, and one extractor for every course | Accepted (operator direction) |
| [0004](./0004-engine-choice-deferred-decide-by-head-to-head.md) | The recognition engine is deliberately unresolved | Accepted — a decision about *how to decide* |
| [0005](./0005-intermediate-representation-reopened.md) | Intermediate representation, adopted from Unlimited-OCR | **Under review** — do not build against it |

> ADRs 0001, 0002 and 0004 were transcribed 2026-09-04 from `todo.md`, where they had been living. A
> decision recorded only in a volatile index is a decision waiting to be lost.
