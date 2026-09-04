# Testing Discipline

**WHEN** you add a module the CLI depends on → **DON'T** leave the floor pointing elsewhere →
**BECAUSE** this project already did exactly that: the 7-test floor covers `pdfops` and `ink`, and
`cli.py` imports neither. **The shipped command has no test.** That is a floor protecting the wrong code.

- **The floor is `tests/persistent/`. 3–7 behaviour-level tests, and never more without a reason.**
  Never delete, skip or loosen one to make a change pass.
- **Behaviour, not implementation.** `test_reading_order_bands_before_columns` currently asserts on
  `ink._reading_order`, a private function — route it through `ink.regions` instead. A refactor should
  not churn the floor.
- **At least one test must run on a machine with no course PDFs.** Five of seven skip today. Use a
  synthetic PDF built in the test for anything that only needs a shape, not real handwriting.
- **Determinism is a prerequisite.** Any recognition engine runs at `temperature=0`, or it cannot be
  regression-tested at all.
- **A fixture that is not in the repository is not a fixture.** The S2 success criterion points into a
  gitignored `tmp/`.
- **Run it as** `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest` — ROS 2 sits on the system
  `PYTHONPATH` and its pytest plugins break collection. [../runbooks/testing.md](../runbooks/testing.md).
- Everything above the floor is throwaway: spikes and refactor guards produce information, not
  verification. Delete after use; promote at most one assertion.

Hub: `~/llm-project-bootstrap/directives/testing-discipline.md` → guide `SESSION_CONDUCT.md` § Testing Rules
