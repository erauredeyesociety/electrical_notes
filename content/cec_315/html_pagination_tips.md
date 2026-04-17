# HTML / CSS Pagination Tips for Non-Standard Page Sizes

Companion to the LaTeX notes. Scope: browser-previewed, multi-page
cheatsheets on 4x6 index cards with math. Targets Chromium (Chrome/Edge);
Firefox / Safari are second-class for `@page {size}`.

---

## 1. Paged.js — browser-side Paged Media polyfill

**What.** Reads CSS `@page` rules and `break-*` properties, clones
`<body>`, re-lays it into `.pagedjs_page` nodes so the browser shows and
prints actual discrete pages. Without it, `@page size` only reaches the
print dialog on Chromium; on screen you see one long scrolling canvas.

**Minimal include (CDN, auto-runs on `load`):**

```html
<script src="https://unpkg.com/pagedjs/dist/paged.polyfill.js"></script>
```

It **empties `<body>`** and replaces it with `.pagedjs_pages` containing
one `.pagedjs_page` per output page.

**DOM shape it wants.** Content directly inside `<body>`. Do NOT wrap
everything in a fixed-size `<div class="page">` with `overflow:hidden` —
Paged.js needs unconstrained flow to measure overflow. A fixed wrapper
clips content on screen and defeats pagination.

**Styling the paged preview:**

```css
.pagedjs_pages { background: #e5e5e5; padding: 0.5in 0; }
.pagedjs_page  { background: #fff; margin: 0 auto 0.5in;
                 box-shadow: 0 4px 14px rgba(0,0,0,.15); }
@page { @bottom-right { content: counter(page) " / " counter(pages); } }
```

**KaTeX ordering — the real pitfall.** Paged.js clones the rendered DOM.
If KaTeX hasn't run yet, Paged.js paginates based on *unrendered* `$...$`
strings and math never appears, or appears at the wrong height. **Render
math first, then load the polyfill:**

```html
<script src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/contrib/auto-render.min.js"></script>
<script>
  window.addEventListener('load', function () {
    renderMathInElement(document.body, {
      delimiters: [{left:'$$',right:'$$',display:true},
                   {left:'$', right:'$', display:false}],
      throwOnError: false
    });
    var s = document.createElement('script');
    s.src = 'https://unpkg.com/pagedjs/dist/paged.polyfill.js';
    document.head.appendChild(s);
  });
</script>
```

For cleaner control, set `window.PagedConfig = { auto: false }` before the
script tag and call `PagedPolyfill.preview()` manually.

**Known pitfalls:**

- **Floats are skipped during overflow detection** (`pagedjs#153`). A
  `float:left` aside that runs past one page clips or halts pagination.
  Replace floats with CSS grid / columns / flex for multi-page layouts.
- `break-inside: avoid` on a `<table>` can push the whole table to the
  next page instead of splitting (`pagedjs#202`).
- Firefox: no `@page {size}`. Paged.js still paginates but the print
  dialog forces Letter.
- Large docs (>30 pages) with heavy math are slow; Paged.js re-measures
  on every page.

Sources:
[Paged.js docs](https://pagedjs.org/en/documentation/2-getting-started-with-paged.js/),
[floats issue #153](https://github.com/pagedjs/pagedjs/issues/153),
[table issue #202](https://github.com/pagedjs/pagedjs/issues/202).

---

## 2. `@page size` — browser support matrix

Per MDN + caniuse, the `size` descriptor is Chromium-only on the web.

| Form                      | Chrome/Edge | Firefox | Safari |
|---------------------------|:-----------:|:-------:|:------:|
| `size: 6in 4in`           |      Y      |    N    |   N    |
| `size: letter landscape`  |      Y      |    N    |   N    |
| `size: 6in 4in landscape` |      Y\*    |    N    |   N    |
| `size: A4`                |      Y      |    N    |   N    |

`*` With an explicit length pair, `landscape` is ignored — Chromium uses
the pair literally. Put the long side first: `size: 6in 4in`.

```css
@page { size: 6in 4in; margin: 0.15in; }    /* 4x6 card, landscape */
```

**If the user picks a different paper in the print dialog**, Chromium
silently overrides your `@page size` and reflows to the dialog paper.
Leave paper on "Default", or drive export from headless Chrome
(Section 4) so the dialog is not involved.

Sources:
[MDN @page/size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page/size),
[caniuse](https://caniuse.com/mdn-css_at-rules_page_size).

---

## 3. `break-before`, `break-after`, `break-inside`

Modern names; legacy `page-break-*` as fallback for old Safari.

```css
section   { break-inside: avoid; page-break-inside: avoid; }
h2        { break-after: avoid;  page-break-after:  avoid; }
.new-page { break-before: page;  page-break-before: always; }
```

**When they silently fail:**

- Inside `display: grid` (`pagedjs#31`). Works on block children, not
  grid items.
- On floats — browsers treat floats as out-of-flow; `break-inside: avoid`
  rarely holds on a floated element.
- Across a `position: absolute` / `fixed` descendant — does not
  paginate; renders once on page 1 or clipped.
- When the element is taller than a page — browser splits anyway, no
  warning.

Source:
[MDN break-inside](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside).

---

## 4. Browser print-to-PDF quirks

**Chrome GUI.** `Ctrl+P` → More settings → Paper size. Custom sizes need
a printer driver; the "Save as PDF" target has no custom-paper UI. Rely
on `@page size` and leave Paper on Default. Margins: None lets
`@page margin` take over.

**Firefox / Safari.** No `@page {size}` support. Only route to 4x6 is an
OS-level PDF printer queue configured with custom paper.

**Headless Chromium — the reliable path.** Bypasses the dialog entirely:

```bash
google-chrome --headless=new --disable-gpu \
  --no-pdf-header-footer \
  --virtual-time-budget=10000 \
  --print-to-pdf=cheatsheet.pdf \
  file:///absolute/path/to/cheatsheet.html
```

- `--headless=new` — Chromium 120+ headless (old `--headless` is
  deprecated).
- `--no-pdf-header-footer` — omits date / URL / page-number chrome
  (supersedes `--print-to-pdf-no-header`).
- `--virtual-time-budget=10000` — wait 10 s of virtual time before
  snapshot; gives Paged.js + KaTeX time to finish. Tune up for heavy
  docs.
- Paper size: command-line flags cannot set arbitrary paper; use
  `@page size: 6in 4in` in CSS — headless Chromium respects it (unlike
  the GUI which applies the dialog paper).
- For margin / range control: drive via Puppeteer / CDP `Page.printToPDF`
  instead of flags.

PDF/X and PDF/A: Chromium does NOT produce ISO PDF/X or PDF/A. No
`--preset=PDF/X-1a` flag exists. If needed, post-process with Ghostscript
(`-dPDFX` + OutputIntent) or use PrinceXML / PDFreactor. Not relevant for
cheatsheets.

Sources:
[Chrome headless](https://developer.chrome.com/docs/chromium/headless),
[GUI vs headless](https://andre.arko.net/2025/05/25/chrome-headless-print-to-pdf/).

---

## 5. KaTeX vs MathJax for printed math

| Property              | KaTeX            | MathJax v3/v4          |
|-----------------------|------------------|------------------------|
| Render                | Fast, sync       | Slower, async          |
| Output                | HTML + CSS spans | HTML+CSS or SVG        |
| Paged.js              | Yes, if before   | Yes, await startup     |
| Prerender tool        | `katex-cli`      | `mathjax-node`         |
| WeasyPrint            | Yes (prerender)  | Yes (prerender)        |
| CDN bundle            | ~280 KB          | ~1+ MB                 |
| Macros / `\newcommand`| Limited          | Full                   |

**Verdict: KaTeX for cheatsheets.** Sync `renderMathInElement()` finishes
before Paged.js boots; smaller payload; clean spans paginate predictably.

**MathJax gotcha.** v3 is async by default. With Paged.js you must
`await MathJax.startup.promise` before dispatching the polyfill, or math
renders mid-pagination and shifts content heights.

**Prerender for WeasyPrint or archival:**

```bash
npx katex-cli < input.tex > rendered.html
# or Python: markdown-katex with no_inline_svg=True
```

Sources:
[KaTeX](https://katex.org/),
[markdown-katex](https://pypi.org/project/markdown-katex/).

---

## 6. Aspect-ratio-preserving screen preview

**Pattern A — let Paged.js own it.** `.pagedjs_page` already has exact
physical dimensions matching `@page size`:

```css
.pagedjs_page { box-shadow: 0 4px 14px rgba(0,0,0,.15);
                margin: 0 auto 0.5in; }
```

**Pattern B — design-time preview without Paged.js.** CSS custom
properties + `aspect-ratio`, swap paper size in one place:

```css
:root { --page-w: 6in; --page-h: 4in; --page-margin: 0.15in; }
@page { size: var(--page-w) var(--page-h); margin: var(--page-margin); }
.page-preview {
  width: var(--page-w);
  aspect-ratio: var(--page-w) / var(--page-h);  /* keeps shape if w shrinks */
  padding: var(--page-margin);
  background: #fff; box-shadow: 0 4px 14px rgba(0,0,0,.15);
}
```

**Thumbnail via `transform: scale()`** — use scale, never `zoom`
(non-standard, fails in Firefox):

```css
.thumb      { transform: scale(0.5); transform-origin: top left; }
.thumb-wrap { width:  calc(var(--page-w) * 0.5);
              height: calc(var(--page-h) * 0.5); overflow: hidden; }
```

`scale()` does not affect layout — the parent must reserve the scaled
footprint manually, or siblings overlap.

Sources:
[MDN aspect-ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio),
[MDN scale](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-function/scale).

---

## 7. WeasyPrint — no-JS alternative

Python HTML-to-PDF. Strong `@page` (custom sizes, running headers, named
pages) and no browser dependency. But no JavaScript — KaTeX/MathJax
cannot run live; prerender first.

```bash
pip install weasyprint
weasyprint cheatsheet.html cheatsheet.pdf
```

**Pick WeasyPrint over Chromium when:**

- Reproducible builds (no browser-version drift).
- Server / CI without GPU or X.
- Need running headers, custom counters, or `@page :first` styling that
  Chromium ignores.
- Hundreds of pages — WeasyPrint is typically faster on pure HTML.

**Pick Chromium when:**

- Any live JS (KaTeX, MathJax, charts).
- Fidelity to "what I see in the browser" is non-negotiable.

**Prerender pipeline for KaTeX + WeasyPrint:**

```bash
node prerender-katex.js cheatsheet.html > cheatsheet.rendered.html
weasyprint cheatsheet.rendered.html cheatsheet.pdf
```

`prerender-katex.js` is ~20 lines using the `katex` npm pkg + `jsdom`,
or use Python `markdown-katex` to skip Node.

Sources:
[WeasyPrint](https://doc.courtbouillon.org/weasyprint/stable/),
[KaTeX + WeasyPrint](https://pypi.org/project/markdown-katex/).

---

## 8. Example: 4x6 landscape index-card cheatsheet

Content directly in `<body>` (no fixed wrapper); Paged.js flows
`<section>` blocks into 4x6 pages.

```html
<!doctype html>
<html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/contrib/auto-render.min.js"></script>
<style>
  :root { --page-w: 6in; --page-h: 4in; --page-margin: 0.15in; }
  @page { size: var(--page-w) var(--page-h); margin: var(--page-margin);
          @bottom-right { content: counter(page) " / " counter(pages);
                          font: 7pt sans-serif; color: #666; } }
  html, body { margin: 0; font: 8pt/1.15 Georgia, serif; }
  h2      { font-size: 9pt; margin: 4pt 0 2pt; break-after: avoid; }
  section { break-inside: avoid; margin-bottom: 4pt; }
  table   { border-collapse: collapse; width: 100%; font-size: 7.5pt; }
  td      { padding: 0.5pt 3pt; vertical-align: top; }
  .pagedjs_pages { background: #e5e5e5; padding: 0.5in 0; }
  .pagedjs_page  { background: #fff; margin: 0 auto 0.5in;
                   box-shadow: 0 4px 14px rgba(0,0,0,.15); }
  @media print { .pagedjs_pages { background: none; padding: 0; }
                 .pagedjs_page  { box-shadow: none; margin: 0; } }
</style>
<script>
  window.addEventListener('load', function () {
    renderMathInElement(document.body, {
      delimiters: [{left:'$$',right:'$$',display:true},
                   {left:'$', right:'$', display:false}],
      throwOnError: false
    });
    var s = document.createElement('script');
    s.src = 'https://unpkg.com/pagedjs/dist/paged.polyfill.js';
    document.head.appendChild(s);
  });
</script>
</head><body>
<section><h2>Laplace pairs</h2>
  <table>
    <tr><td>$\delta(t)$</td><td>$1$</td></tr>
    <tr><td>$u(t)$</td><td>$1/s$</td></tr>
  </table>
</section>
<section><h2>ROC</h2>
  <p>Vertical strip in $s$-plane; never contains poles.
     Causal: $\Re\{s\}>\sigma_{\max}$. Stable: $j\omega$-axis in ROC.</p>
</section>
<!-- ... more <section> blocks. -->
</body></html>
```

**Multi-page overflow.** With content directly in `<body>`, Paged.js
measures each `<section>` and splits when the page is full.
`break-inside: avoid` keeps sections intact. A section taller than 4x6
splits mid-content — tolerable unless it cuts a table row.

**Testing:** open in Chromium → verify `.pagedjs_page` cards render →
`Ctrl+P` → Save as PDF → Paper: Default. Or CI: headless Chromium from
§4, then `pdfinfo out.pdf` to confirm `432 x 288 pts (6 x 4 inch)`.

---

## Decision tree: Paged.js vs WeasyPrint vs Chromium headless

```text
Need live, multi-page preview in the browser?
├─ YES → Paged.js (§1).
│        Accept: Chromium-only, floats break across pages, KaTeX first.
└─ NO (render offline, ship PDF):
   ├─ HTML has live JS (KaTeX, MathJax, charts)?
   │  ├─ YES → headless Chromium --print-to-pdf (§4),
   │  │        + Paged.js if multi-page or custom @page features.
   │  └─ NO  → WeasyPrint (§7). Prerender math if present.
   │           Faster, reproducible, no browser dependency.
   └─ Need PDF/X, PDF/A, or print-shop submission?
      → Render with WeasyPrint or Chromium, post-process with
        Ghostscript. Or pay for PrinceXML / PDFreactor.
```

**For CEC 315 cheatsheets:** Paged.js during authoring; headless
Chromium for the archival PDF. WeasyPrint is the fallback if Chromium
drift becomes a problem.

---

## Application reference

Concrete target:
[`exam3_cheatsheet_v10.html`](./exam3/exam3_cheatsheet_v10.html). That
file wraps all content in a single `<div class="page">` with fixed
dimensions and `overflow: hidden`. **That wrapper short-circuits
Paged.js — it sees one element with no overflow, emits one page, and
clips anything beyond 11x8.5in.** To switch to 4x6 multi-page:

- Set `:root { --page-w: 6in; --page-h: 4in; --page-margin: 0.15in; }`.
- **Remove the `<div class="page">` wrapper** (or drop its fixed
  `width`/`height`/`overflow`). Paged.js needs direct-body flow.
- Replace the float-based `<aside class="side-left">` / `side-right`
  with CSS Grid or Columns — Paged.js skips floats during overflow
  detection (`pagedjs#153`), so a multi-page float layout clips or
  misplaces content past page 1.
- Each `<section>` already has `break-inside: avoid`; keep that.
