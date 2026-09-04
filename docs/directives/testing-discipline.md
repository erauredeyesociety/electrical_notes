# Testing Discipline

**WHEN** you reach for `tests/persistent/` at this repo's root → **DON'T** build a unit-test suite →
**BECAUSE** the root repo ships **no application code**. It ships Markdown, LaTeX and PDFs, and the only
thing that can regress is *whether the artifacts still build*. A unit-test folder here would protect
nothing and get stale immediately.

## What the floor actually is here

The root repo's regression floor is **three build checks**, not assertions:

| Check | Command | Protects |
| --- | --- | --- |
| Site builds | `hugo --minify` | The published site. This is exactly what CI runs — [`.github/workflows/pages.yml`](../../.github/workflows/pages.yml). A broken build breaks the public site. |
| A solution `.tex` builds | [`docs/latex/build_tex.sh <path>`](../latex/build_tex.sh) | Every coursework `.tex` under the new doctrine. It deletes the PDF afterwards — build-check, not render. |
| Course tooling runs | `content/cesc_410/labs_and_projects/tools/check_inputs.py`, `check_artifacts.py` | Whether a lab's declared inputs and artifacts are actually present |

**None of these is scripted at the root today.** That is the gap — see [../roadmap.md](../roadmap.md) § Scripts.

## Rules

- **Build-check, do not render.** `build_tex.sh` builds a `.tex` and deletes the PDF unless `--keep` is
  passed. The question is "does it compile", not "does it look right"; looking right is the operator's
  job with the PDF open.
- **Per-problem files are standalone by design.** Each `pNN_*.tex` inputs the shared preamble, so any one
  problem can be checked alone and a break is localised to the problem that broke it. Do not collapse an
  assignment into one monolithic `.tex` to "simplify" the build — that destroys the property.
- **Child projects keep their own floors, and they are real.** `ocr_handler/tests/persistent/` is a
  behaviour-level pytest floor with its own runbook
  ([`ocr_handler/docs/runbooks/testing.md`](../../ocr_handler/docs/runbooks/testing.md)) and its own
  discipline. Never delete, skip or loosen one of those to make a change pass. A root-level session does
  not touch them.
- **`PYTHONPATH` is contaminated on this machine.** ROS 2 sits on the system `PYTHONPATH` and its pytest
  plugins break collection. Any pytest run in this repo goes as
  `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest`. Proven in
  [`ocr_handler/docs/runbooks/testing.md`](../../ocr_handler/docs/runbooks/testing.md); it applies to
  `content/cesc_410/labs_and_projects/dsp26/` too.
- **A check must assert a known-correct result, not liveness.** "`hugo` exited 0" is weak; "`hugo` exited
  0 **and** the expected course page exists in `public/`" is a check. Prefer the latter when writing one.
- **Heavy work stays out of the loop.** Rendering all 430 PDFs, rebuilding the whole site repeatedly, or
  running an OCR pass is operator-triggered, never part of a routine edit cycle.
- **Everything above the floor is throwaway.** A one-off script written to answer "how many PDFs have a
  text layer" produces information, not verification. Record the answer in `docs/findings/`; delete the
  script.

Hub: `~/llm-project-bootstrap/directives/testing-discipline.md` → guide `SESSION_CONDUCT.md` § Testing Rules
