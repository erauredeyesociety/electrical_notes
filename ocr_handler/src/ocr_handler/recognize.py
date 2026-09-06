"""Recognition -- region or page to text. THE ONLY MODULE ALLOWED TO USE ML.

**Nothing is implemented here yet, and that is a decision, not an oversight.**
The engine is deliberately unchosen: ADR-0004 defers it to a head-to-head on
the fixture page, and docs/scope.md open decision 1 records the operator's own
steer that the candidate repos are not necessarily good solutions either.
Naming a model here now would bake in a choice the research pass has not made,
and every caller written against it would have to be rewritten.

So this module exists as ONE honest failure. It refuses loudly and says why.
What it must never do is return an empty string: `--mode ocr` on a page with
three images silently yielding nothing is indistinguishable from a blank page,
and docs/plans/text-layer-first.md section 7 exists precisely because
conflating those two is how a broken engine looks like a clean corpus.

When M3 lands, `available()` starts returning True and `recognize()` starts
returning text. No caller changes.
"""

from __future__ import annotations

from pathlib import Path

# Why the refusal, in one string, so the CLI and any future caller give the
# same answer rather than each inventing their own wording.
UNAVAILABLE = (
    "no recognition engine is selected — the choice is deliberately open "
    "(docs/decisions/0004-engine-choice-deferred-decide-by-head-to-head.md), "
    "and it is decided by a head-to-head on the fixture page, not by picking "
    "one here. Until then the only honest answer for these pages is that they "
    "were not read. Use --mode text for the text layer alone."
)


class EngineUnavailable(RuntimeError):
    """Raised instead of returning nothing. See the module docstring."""


def available() -> bool:
    """Is there an engine to run at all? False until M3."""
    return False


def engines() -> tuple[str, ...]:
    """Engine names `--engine` would accept. Empty until M3."""
    return ()


def recognize(pdf: Path, page: int, *, dpi: int = 200,
              engine: str | None = None) -> str:
    """Recognise one page. Raises `EngineUnavailable` until M3.

    `dpi` defaults to 200 because that is where handwritten subscripts became
    reliably readable; 150 lost them and 300 only cost time. Re-sweep if the
    renderer changes -- poppler at 200 dpi produced `c o s (w o n)` where
    PyMuPDF at 150/200/300 all produced `\\cos(\\omega_0 n)`.
    """
    raise EngineUnavailable(UNAVAILABLE)
