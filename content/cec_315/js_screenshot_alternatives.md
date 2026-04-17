# JS Screenshot Library Alternatives — v10 blank-white investigation

Context: `html-to-image@1.11.13` produces a blank white PNG when capturing
`.page` (CSS Grid, 5x3in, KaTeX-rendered math inside `<table>`s) from
`exam3_cheatsheet_v10.html`. Served over `http://localhost:8000` so CORS is
fine. Goal: find a drop-in replacement.

## Library scan (April 2026)

| Library | Approach | Latest | Stars | Drop-in? | KaTeX/SVG | Grid |
|---|---|---|---|---|---|---|
| html-to-image 1.11.13 (current) | foreignObject SVG | 1.11.13 (2023) | ~6.7k | — | mixed | mixed |
| **modern-screenshot** | foreignObject SVG (fork of html-to-image) | **4.7.0** (Apr 16 2026) | ~1.9k | near-identical API (`domToBlob`) | explicit SVG-fix features flag | yes |
| snapdom (@zumer/snapdom) | custom clone + inlined styles | 2.8.0 (Apr 8 2026) | ~7.7k | different API (`snapdom.toBlob`) | **known KaTeX bug (#331)** — styles lost | yes |
| html2canvas 1.4.1 | reimplements CSS layout | 1.4.1 (2022) | ~31k | different API, rasterizes differently | poor for KaTeX SVG glyphs, no foreignObject | partial |
| dom-to-image-more | foreignObject SVG (older fork) | stale | ~1k | same as html-to-image | similar issues, less active | limited |
| html2image-pro / katex-screenshot | niche / server-side wrappers | n/a | low | no | n/a | n/a |
| Puppeteer/Playwright-as-a-service | server-side | — | — | not inline | n/a | n/a |

Rationale highlights:

- **modern-screenshot** is a direct fork of html-to-image with ongoing 2026
  releases. It keeps the foreignObject SVG pipeline (which is why KaTeX
  custom-font glyphs render at all) but ships additional "features" fixups
  (SVG attribute normalization, scrollbar copy, character normalization) —
  several of these address reported blank-output bugs. Active as of
  Apr 16 2026 (v4.7.0).
- **snapdom** looks appealing (fast, 2026 releases) but its own issue
  tracker has an open KaTeX bug (zumerlab/snapdom#331) where KaTeX styles
  are dropped from the capture. Wrong tool for this document.
- **html2canvas** walks the DOM and re-draws with its own layout engine; it
  routinely mis-renders KaTeX's inline-SVG glyph sprites and CSS grid
  fractional tracks. Poor fit.
- **dom-to-image-more** is largely superseded by html-to-image (same
  architectural lineage, less maintenance). No reason to pick it over
  modern-screenshot.

## Ranked recommendation

1. **modern-screenshot** — same technique as current lib (so KaTeX fonts keep
   working), newer bug fixes, near drop-in, actively released.
2. **snapdom** — as a *secondary* fallback for the cases where
   foreignObject breaks entirely; accept the KaTeX styling risk because
   something-looking-wrong beats blank-white.
3. **html2canvas** — last-ditch. Will mangle math but it takes a completely
   different rendering path, so if the first two fail it may at least
   produce non-blank pixels.

## CDN URLs

```html
<!-- 1. modern-screenshot (primary) -->
<script src="https://cdn.jsdelivr.net/npm/modern-screenshot@4.7.0/dist/index.iife.js"></script>
<!-- global: window.modernScreenshot -->

<!-- 2. snapdom (secondary) -->
<script src="https://cdn.jsdelivr.net/npm/@zumer/snapdom@2.8.0/dist/snapdom.js"></script>
<!-- global: window.snapdom -->

<!-- 3. html2canvas (tertiary) -->
<script src="https://cdn.jsdelivr.net/npm/html2canvas@1.4.1/dist/html2canvas.min.js"></script>
<!-- global: window.html2canvas -->
```

## Drop-in swap snippets

Given the existing call:

```js
var blobPromise = htmlToImage.toBlob(page, renderOpts());
```

### (1) modern-screenshot — nearly identical

```js
// renderOpts() is reusable as-is; modern-screenshot supports
// backgroundColor, filter, cacheBust. `pixelRatio` maps to `scale`.
var opts = renderOpts();
opts.scale = opts.pixelRatio; delete opts.pixelRatio;
var blobPromise = modernScreenshot.domToBlob(page, opts);
```

### (2) snapdom

```js
// snapdom uses `dpr` instead of pixelRatio/scale. Filter signature is
// the same predicate. backgroundColor supported.
var blobPromise = snapdom.toBlob(page, {
  dpr: 3,
  backgroundColor: '#ffffff',
  embedFonts: true,
  filter: function (n) {
    return !(n.classList && n.classList.contains('no-print'));
  }
});
```

### (3) html2canvas — canvas-based, needs toBlob()

```js
var blobPromise = html2canvas(page, {
  scale: 3,
  backgroundColor: '#ffffff',
  useCORS: true,
  allowTaint: false,
  ignoreElements: function (el) {
    return el.classList && el.classList.contains('no-print');
  }
}).then(function (canvas) {
  return new Promise(function (resolve) { canvas.toBlob(resolve, 'image/png'); });
});
```

## Defensive "try A, fall back to B, fall back to C" pattern

Load all three libraries, then try them in order, only advancing on a
non-blank result. Simple heuristic for "blank": blob < 4 KB at 3x
pixelRatio for a 5x3in page is almost certainly white.

```js
function captureBlob(page, opts) {
  var MIN_BYTES = 4096;
  function tryModernScreenshot() {
    if (!window.modernScreenshot) return Promise.reject('not loaded');
    var o = Object.assign({}, opts, { scale: opts.pixelRatio });
    delete o.pixelRatio;
    return modernScreenshot.domToBlob(page, o);
  }
  function tryHtmlToImage() {
    if (!window.htmlToImage) return Promise.reject('not loaded');
    return htmlToImage.toBlob(page, opts);
  }
  function trySnapdom() {
    if (!window.snapdom) return Promise.reject('not loaded');
    return snapdom.toBlob(page, {
      dpr: opts.pixelRatio,
      backgroundColor: opts.backgroundColor,
      embedFonts: true,
      filter: opts.filter
    });
  }
  function tryHtml2Canvas() {
    if (!window.html2canvas) return Promise.reject('not loaded');
    return html2canvas(page, {
      scale: opts.pixelRatio,
      backgroundColor: opts.backgroundColor,
      useCORS: true,
      ignoreElements: function (el) { return !opts.filter(el); }
    }).then(function (c) {
      return new Promise(function (r) { c.toBlob(r, 'image/png'); });
    });
  }
  function validate(blob) {
    if (!blob || blob.size < MIN_BYTES) {
      throw new Error('blob too small (' + (blob && blob.size) + 'B) — likely blank');
    }
    return blob;
  }
  // Order: modern-screenshot -> html-to-image -> snapdom -> html2canvas
  return tryModernScreenshot().then(validate)
    .catch(function (e) { console.warn('modern-screenshot failed:', e); return tryHtmlToImage().then(validate); })
    .catch(function (e) { console.warn('html-to-image failed:', e); return trySnapdom().then(validate); })
    .catch(function (e) { console.warn('snapdom failed:', e); return tryHtml2Canvas().then(validate); });
}
```

Then the v10 copy flow becomes:

```js
var blobPromise = captureBlob(page, renderOpts());
return navigator.clipboard.write([
  new ClipboardItem({ 'image/png': blobPromise })
]);
```

## Other notes / gotchas

- KaTeX CSS must be loaded with `crossorigin="anonymous"` (already done in
  v10) so foreignObject-based libs can serialize the `@font-face` rules.
- `cacheBust: true` in html-to-image maps to `fetch.bypassingCache: true`
  in modern-screenshot (nested under `fetch`).
- modern-screenshot's `features` option (default `true`) turns on several
  SVG normalization patches not present in html-to-image 1.11.13 — this is
  the single most likely reason it succeeds where html-to-image produces
  blank output for KaTeX inline SVG.
- If blank output persists with modern-screenshot, temporarily set
  `debug: true` — it logs each clone/embed step.
- None of these libraries support iframes cross-origin, but v10 doesn't
  use iframes, so irrelevant here.
