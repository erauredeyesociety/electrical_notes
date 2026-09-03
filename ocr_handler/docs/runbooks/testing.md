# Running the tests

```sh
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH= uv run pytest
```

**Both environment variables are required on this machine.** ROS 2 Humble sits on the system `PYTHONPATH` and registers pytest plugins that fail to import (`ModuleNotFoundError: No module named 'yaml'`, raised from `/opt/ros/humble/.../launch/frontend/`). Collection dies before any test runs.

This is not a project problem and there is nothing to fix in the code — the plugins simply are not wanted. Disabling autoload and clearing `PYTHONPATH` isolates the venv.

Bare `uv run pytest` will fail with a ROS traceback. That is the symptom; this is the cause.

## What the floor covers

Seven tests, deliberately few. They lock the paths an agent may refactor unsupervised:

| Test | Locks |
| --- | --- |
| `test_reading_order_bands_before_columns` | Side-by-side items read left-to-right. Regression for a real bug that silently reversed an equation. |
| `test_empty_mask_yields_no_regions` | Degenerate input |
| `test_born_digital_pages_route_to_text_not_a_model` | Pages with a text layer never reach recognition |
| `test_annotated_pages_do_not_route_to_text` | The inverse |
| `test_producer_distinguishes_annotation_from_recompile` | The two kinds of `-plw` file stay distinguishable |
| `test_pairs_annotated_file_with_its_base` | Pairing for difference-based separation |
| `test_ink_separation_and_grouping_on_known_page` | Ink pixel count and 5-region grouping on the fixture page |

Tests needing the course PDFs skip cleanly when they are absent, so the suite stays green elsewhere.
