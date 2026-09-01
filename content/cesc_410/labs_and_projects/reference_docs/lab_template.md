# Lab NN — <title>

<!--
Copy to labNN/README.md and fill in as you work, not afterwards.

This is a REPRODUCTION LOG. Someone should redo the lab from this file without
opening the handout. Commands verbatim, in order, with what they printed.

The report is a different document -- see reference_docs/report_guide.md.
Delete these comments.
-->

**Handout:** [`<file>.md`](<file>.md) · **Started:** YYYY-MM-DD · **Status:** in progress / done / submitted

**Goal:** one or two sentences.

---

## Inputs

Every file the handout names or links to. **Check this before starting** — a missing starter zip or dataset is the most common reason a lab stalls, and only a human can fetch it from Canvas.

| File | Purpose | Status |
| --- | --- | --- |
| `<name>.md` / `.pdf` | handout | ✅ present |
| `<name>.zip` | starter code | ❌ **missing — download from Canvas** |

---

## Code

Lab code lives in the shared package, not here — see [`../README.md`](../README.md#why-code-and-docs-are-split).

| File | What it does |
| --- | --- |
| `dsp26/src/dsp26/labN_<topic>/<file>.py` | … |
| `dsp26/src/dsp26/app_cli.py` | adds the `<command-name>` command |

---

## Reproduce

Every command, in order, exactly as run.

```sh
export PATH="$HOME/.local/bin:$PATH"    # if uv is not already on PATH
cd dsp26
uv sync
```

```sh
# headless: plt.show() is a no-op, so save instead
MPLBACKEND=Agg uv run dsp26 <command> --folder-name ../labNN
```

Output:

```
<paste actual output>
```

Verify:

```sh
cd .. && uv run --project dsp26 python tools/check_artifacts.py labNN/figs
```

---

## Artifacts

`figs/` is gitignored — regenerate with the command above.

| # | File | Shows |
| --- | --- | --- |
| 1 | `figs/<name>.png` | … |

---

## Deviations from the handout

Anything changed from the handout code, and why. Each one is also marked in the source with a `DEVIATION FROM HANDOUT:` comment. **This section feeds the report's Narrative — a graded section.** If it could recur, add it to [`../reference_docs/known_issues.md`](../reference_docs/known_issues.md).

| # | Change | Why |
| --- | --- | --- |
| 1 | … | … |

*None* — if the handout code worked as written.

---

## Handout questions

Handouts bury questions between code blocks and they are graded. Collect them while reading.

1. **Q:** …
   **A:** …

---

## Needs a human

| Task | Status |
| --- | --- |
| Set ERAU ID (`grep -rn myID dsp26/src/`) | ⬜ |
| Live demo at lab meeting | ⬜ |
| Write report — copy [`report_template.tex`](../reference_docs/report_template.tex), then `tools/render_reports.sh labNN` ([guide](../reference_docs/report_guide.md)) | ⬜ |
| Submit to Canvas before the next meeting | ⬜ |

---

## Notes

Anything that would otherwise be lost — a surprise, a wrong turn, something to check next time.
