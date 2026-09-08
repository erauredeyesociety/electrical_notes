# Commenting standard

## There are two copies of the code, and they have different jobs

This is the thing to get straight, because it removes the tension entirely.

| | **Working copy** (`dsp26/` in this repo) | **Submitted copy** (the zip) |
| --- | --- | --- |
| Comments | **Heavy — comment freely** | Stripped |
| Docstrings | Yes | Stripped |
| Audience | us, six months from now | the TA |
| Job | explain the DSP, so the code is a study aid | be correct and readable |
| Produced by | you, as you work | `tools/make_submission.sh` |

**You never hand-edit code for submission.** `make_submission.sh` copies `dsp26/` to a throwaway staging directory, strips it there, prepends a `# CESC 410L -- Lab N / name / date` header, and zips that. **The working tree is never modified** — your commented source stays exactly as written.

So: **comment as much as is genuinely useful.** It costs nothing at hand-in.

### This is verified, not asserted

The stripper was checked against the real Lab 0 code by running the *stripped* copy and confirming it produces **byte-identical figures** (4/4 md5 match). It also re-parses its own output and compares ASTs, refusing to emit anything where stripping changed the code rather than just the comments.

Typical effect: `sinusoids.py` 173 → 110 lines, `recipes.py` 102 → 62.

### Two things survive stripping

- **`DEVIATION FROM HANDOUT` blocks — the whole block**, not just the marker line. This is disclosure that handout code was modified, and the reasoning has to travel with it.
- The `last 4 digits` ERAU-ID marker, one line only.

Details and options: [`submission_requirements.md`](submission_requirements.md).

---

## Standalone means the working copy

A working file should be readable cold, without this repo's documentation open — someone opens it and can follow what each step does and why.

The *submitted* copy is not expected to carry that; it is code answering a handout the TA already has. Both are appropriate to their reader.

---

## The rule

**Comment the step, not the syntax.**

```python
# GOOD -- names the operation
# Take the DFT of the sparse signal and shift zero-frequency to the centre
# so the spectrum plots symmetrically about 0 Hz.
X_s = np.fft.fft(x_s)
X_F = np.abs(np.fft.fftshift(X_s))
```

```python
# BAD -- restates the code
X_s = np.fft.fft(x_s)   # call fft on x_s
```

```python
# BAD -- explains Python, not the lab
for i in range(len(Am)):   # loop over the list
```

The reader knows Python. They may not know why you are shifting the spectrum, or why there are two sample rates.

---

## Density

**One comment per logical step**, not per line. A "step" is a thing you would name aloud when explaining the function: *take the transform*, *find the peaks*, *label each peak with its complex value*.

Three to six comments in a twenty-line function is about right. A comment on every line is noise, and it reads as generated rather than written.

---

## What earns a comment

| Earns one | Doesn't |
| --- | --- |
| Why a value is what it is (`Ns = Nd/16` — why 16?) | Assignment of an obvious name |
| A DSP operation being performed | Standard library calls with clear names |
| A non-obvious index or slice (`X_s[0:Ns2]` — why half?) | Loop bookkeeping |
| Units and conventions (Hz vs rad/s, one-sided vs two-sided) | Imports |
| Anything that surprised you while writing it | Anything you'd delete on reread |
| A deviation from the handout | — |

**If it surprised you, comment it.** That is the highest-value comment in any file, and it is the raw material for the report's Narrative section.

---

## Module docstrings

Every module opens with a short docstring: what it is, which lab, and its role.

```python
"""Sinusoid generation and time/frequency-domain plotting.

Lab 0. Lower-level plotting helpers called by recipes.py -- each builds one
figure with the waveform on top and its magnitude spectrum below.
"""
```

For automation modules, say so explicitly on the first line:

```python
"""Verify a lab's output artifacts.

AUTOMATION CODE -- never submitted. See reference_docs/code_separation.md.
"""
```

That one line is what keeps the boundary visible from inside the file.

---

## Math

Where a function implements an equation, put the equation in the docstring. LaTeX notation is fine — it is readable as text and pastes straight into the report.

```python
def plot_one_sinusoid_td_fd(Am, Fr, Ph, ...):
    """Plot one sinusoid in time and frequency.

    Signal:   x(t) = Am * cos(2*pi*Fr*t + Ph)
    Spectrum: X[k] = sum_{n=0}^{N-1} x[n] * exp(-j*2*pi*k*n/N)

    A real sinusoid gives two spectral lines, at +Fr and -Fr, each of
    magnitude Am*N/2.
    """
```

This is the bridge to the LaTeX report — the docstring math becomes the report's `\begin{equation}` block with almost no rewriting.

---

## Section banners

For files with several independent parts (like `app_cli.py`, one command per lab), separate them:

```python
########################################################################
# Lab 0 -- sinusoids
```

The handout already uses this style. Keep it.

---

## Deviations

Always marked, always explaining what the handout had and what broke:

```python
# DEVIATION FROM HANDOUT: handout has `plt.figure(1)` here.
# This function is called twice; pyplot returns the SAME Figure for a
# repeated number, so the second call drew on top of the first.
```

See [`code_separation.md`](code_separation.md#deviations-from-the-handout).

**Do not wait for permission to make the fix.** Whether to *keep* a deviation is a human judgment call;
whether to make it is not. Fix it, mark it, log it in the lab README, and hand the decision over as a
block that says what the handout had, what broke, what you changed it to, and — the part usually left
out — **whether the handout's version runs at all.** A deviation that fixes a crash is a different
decision from one that changes how a figure looks, and the human cannot tell which they are being asked
about unless you say. The block format is `H8` in [`../prompt.md`](../prompt.md#human-only); the
standard behind it is [`human-task-instructions.md`](../../../../docs/directives/human-task-instructions.md).

**The marker phrase is load-bearing.** Only write `DEVIATION FROM HANDOUT` in a `#` comment in the file
that actually deviates. Naming it in a docstring — even to point at a deviation elsewhere — aborts
packaging, because docstrings are stripped and the guard counts the phrase before and after
([KI-14](known_issues.md#ki-14--naming-deviation-from-handout-in-a-docstring-aborts-packaging)).

---

## What not to do

- **Don't comment out code and leave it.** Delete it; git remembers.
- **Don't write a comment that will go stale.** A comment naming a line number or a byte size will be wrong within a week.
- **Don't restate the docstring** at the first line of the body.
- **Don't apologise or narrate.** No `# TODO: this is ugly`, no `# not sure why this works`. If you are not sure why it works, find out and then comment the answer — that is the comment worth having.

---

**Related:** [`code_separation.md`](code_separation.md) · [`report_guide.md`](report_guide.md) · [`../prompt.md`](../prompt.md)
