# Lessons Learned — INDEX

**PRESCRIPTIVE** rules distilled from this project's own experience, in `WHEN → DON'T → BECAUSE` form,
each carrying the discovery that produced it.

| File | Covers |
| --- | --- |
| [lessons.md](./lessons.md) | **23 lessons** in seven groups. **Measurement** — vendoring without measuring; asymmetric bugs hide from samples; inherited headlines; a "control" that is not one; a peer claim is a hypothesis. **Measuring a measurement** — a control that *cannot fire* bounds nothing; enumerate a cost, don't reweight it; cluster the bootstrap by document; a page with no text and no images is not blank. **Detectors** — an unwired detector; two questions one score; recall is not a threshold; the content-free case; report what stayed quiet. **Detectors, continued** — a detector blind in the direction of its own target; two detectors must not disagree about the same glyph; a constant encodes the corpus it was tuned on. **Code** — name the rule for every change; ship the sweep not the number; spatial sort; don't model a page that has text. **Cost and hardware** — a GPU-pinned job still saturates the CPU; attribute load before acting on it. |

## The distinction that keeps this folder from becoming a second directives folder

A **directive** is a standing rule for how to work here. A **lesson** is a rule *plus the specific
failure that earned it*. If you cannot name the incident, it is a directive, not a lesson.

## Format

```
- **WHEN <situation>, DON'T <action> — <do this instead> — BECAUSE <consequence>.** <The concrete
  failure, with its measurement.> (YYYY-MM-DD) Source: <path>
```

Split at ~400 lines into `lessons_2.md` and index the parts.

---

**The three lessons this folder was opened owing** — spatial sort, don't model a page that already has
text, don't guess a tuned constant — are now in [lessons.md](./lessons.md) § Code. They were previously
misfiled as directives in [../directives/code-discipline.md](../directives/code-discipline.md), which
keeps them as standing rules; the lesson entries add the incident each one came from.
