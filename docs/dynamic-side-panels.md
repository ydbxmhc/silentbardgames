# Proposal: Dynamic Side Panels ("Gutter Rails")

**Status:** Refined spec / not yet implemented
**Scope:** L1 subsite (`/L1/`), designed for reuse by future OneSRD games
**Hosting context:** GitHub Pages (static) today; AWS migration planned
**Author intent:** Use the empty left/right margins of the centered reading
column to display art and optional promotional cards -- but only *when the
viewport genuinely has room*, degrading cleanly to today's single-column
layout when it does not.

> This document is written to be read by a human (the site owner) **and** to
> be handed to an implementing agent (Kiro or Claude Code). The implementation
> guidance section is written as direct instructions to that agent and is bound
> by the rules in `/CLAUDE.md`. Read `/CLAUDE.md` before implementing anything
> here.

---

## 1. The problem

Every L1 content page renders its body inside a fixed-width centered column:

```css
/* resources/onesrd.css */
:root { --content-max: 780px; }
.content-wrap { max-width: var(--content-max); margin: 0 auto; padding: 0 1.5rem; }
```

On a wide display this leaves large empty "gutters" on each side. On a 1920px
viewport that is roughly **(1920 - 780) / 2 = 570px per side** of unused
parchment. Today's images (e.g. `reader.png` on `start.html`) are placed
*inside* the 780px column via `.text-image-block`, which narrows the reading
text instead of using the empty space.

**Goal:** move decorative art (and optional promo cards) out into the gutters
when space allows, without ever compromising the readability of the central
text column and without changing a single word of rulebook content.

---

## 2. Design principles (non-negotiable)

1. **Content first, always.** The 780px reading column and its text are the
   product. Side panels are decorative/secondary. If anything has to give, the
   side panels disappear, not the text.
2. **Progressive enhancement.** With JavaScript off, with images off, or on a
   narrow screen, the page must look and read exactly like it does today.
3. **No rulebook content in the gutters.** Per `/CLAUDE.md`'s Prime Directive,
   the side panels carry *art* and *promotional/navigational* material only --
   never rules text, never examples, never anything a reader must read to
   understand the game.
4. **Respect user preferences.** The existing prefs (`l1-theme`, `l1-fontsize`,
   `l1-navbg`, `l1-reducemotion`) must continue to work. Add `l1-rails` to
   this family (see §6).
5. **No inline styles.** All styling goes in CSS files per `/CLAUDE.md`. JS may
   only toggle classes / set CSS custom properties -- never write style strings.
6. **Don't touch the untouchables without instruction.** `nav.js`, `config.js`,
   `nav.html`, `header.html`, and `onesrd.css` are protected in `/CLAUDE.md`.
   This spec is designed to need none of those changed. See §9.

---

## 3. The three layout states

Let:
- `C` = content column width = **780px** (`--content-max`)
- `R` = minimum usable rail width, proposed **220px** (`--rail-w`)
- `G` = gap between column and rail, proposed **2rem / 32px** (`--rail-gap`)
- `V` = available viewport width (excluding scrollbar)

| State | Condition (approx.) | Behavior |
|-------|---------------------|----------|
| **0 -- Single column** | `V < C + R + G` -- below ~1064px | Today's layout. Centered column, no rails. |
| **1 -- One panel (asymmetric)** | `C + (R+G) <= V < C + 2*(R+G)` -- ~1064-1348px | Enough combined margin for one rail. Shift column off-center; open a single panel on the preferred side. |
| **2 -- Two panels (symmetric)** | `V >= C + 2*(R+G)` -- ~1348px+ | Centered column with a rail on both sides. |

### 3.1 The asymmetric case (State 1)

When only one panel fits, stop centering the column and bias it toward one
side, pooling the freed space into a single wider gutter:

```
State 0 (narrow):      State 1 (one panel):            State 2 (wide):

| [   column   ] |     | [ column ] [ panel ] |     | [panel] [ column ] [panel] |
  centered             column shifted left,            column centered,
  no panels            panel opens on the right        panel each side
```

Which side the single panel opens on is controlled by `--rail-side` (see §4).
Default recommendation: **right** (the side a left-to-right reader's eye
leaves last), with the column shifted left.

---

## 4. CSS variables -- the knobs

These are the adjustable variables. They live in `onesrd.css` as neutral
defaults and are overridable per game in `style.css`:

```css
/* resources/onesrd.css -- defaults */
:root {
  --rail-w:   220px;    /* width of each panel */
  --rail-gap: 2rem;     /* space between column and panel */
  --rail-side: right;   /* State 1 preferred side: left | right | auto */
                        /* auto = measure at runtime and decide (JS path) */
}
```

`--rail-side: auto` defers the left/right decision to JS measurement (Approach
B below). `left` or `right` is a pure-CSS decision requiring no JS. For the
first implementation, use `right` -- it can be changed with a single variable.

Breakpoints are derived from the variables above:
- State 1 threshold: `--content-max + --rail-w + --rail-gap` ~ 1064px
- State 2 threshold: `--content-max + 2*(--rail-w + --rail-gap)` ~ 1348px

---

## 5. Implementation approaches

### Approach A -- CSS-first (recommended baseline)

Drive the three states with media-query breakpoints and CSS Grid. Handles
zoom, resolution changes, and viewport resize automatically with zero JS.

New optional wrapper inside `#main` (additive -- pages without it are
unaffected):

```html
<main id="main">
  <div class="reading-layout">
    <aside class="rail rail-left"  hidden></aside>
    <div class="content-wrap"> ...existing page body unchanged... </div>
    <aside class="rail rail-right" hidden></aside>
  </div>
</main>
```

```css
/* State 2 -- symmetric, two rails */
@media (min-width: 1348px) {
  .reading-layout {
    display: grid;
    grid-template-columns: 1fr var(--content-max) 1fr;
    column-gap: var(--rail-gap);
    align-items: start;
    max-width: calc(var(--content-max) + 2 * (var(--rail-w) + var(--rail-gap)));
    margin-inline: auto;
  }
  .reading-layout .rail { display: block; }
}

/* State 1 -- asymmetric, single rail on the right */
@media (min-width: 1064px) and (max-width: 1347.98px) {
  .reading-layout {
    display: grid;
    grid-template-columns: var(--content-max) 1fr;
    column-gap: var(--rail-gap);
    align-items: start;
    max-width: calc(var(--content-max) + var(--rail-w) + var(--rail-gap));
    margin-inline: auto;
  }
  .reading-layout .rail-right { display: block; }
}
```

### Approach B -- JS measurement (optional refinement)

Measure actual rendered space via `ResizeObserver` +
`getBoundingClientRect()`, then toggle `html.rails-1` / `html.rails-2`
classes that CSS responds to. More accurate than fixed breakpoints (accounts
for scrollbar width, font-size pref reflow, etc.). Implement after Approach A
is confirmed working.

---

## 6. Panel content -- the manifest

Panel content is loaded dynamically from a static JSON file fetched once per
session. This is the single source of truth for what can appear in rails.

### 6.1 panels.json

Location: `/L1/panels.json` (served as a static file by GitHub Pages; no
server required).

```json
{
  "panels": [
    {
      "id": "cover-art",
      "type": "art",
      "src": "cover-thumb.jpg",
      "alt": "Level One RPG cover art",
      "caption": null,
      "weight": 10
    },
    {
      "id": "buy-pdf",
      "type": "promo",
      "title": "Get the PDF",
      "blurb": "Full print-ready rulebook with art.",
      "href": "https://silentbard.itch.io/",
      "src": "promo/buy-thumb.jpg",
      "alt": "",
      "weight": 5
    },
    {
      "id": "raven-toad",
      "type": "art",
      "src": "art/Raven_and_Toad-BW.jpg",
      "alt": "A raven and a toad",
      "caption": null,
      "weight": 8
    }
  ]
}
```

`weight` drives a non-uniform random draw -- higher weight = more likely to
be picked. The client normalizes weights to probabilities, shuffles, and
draws without replacement until the list is exhausted, then reshuffles.

`SiteConfig.PANELS_URL` in `config.js` points at this file. **Do not
hardcode the path in `rails.js`** -- read it from `SiteConfig`.

### 6.2 Per-page panel hints

A page can hint which panel IDs are thematically appropriate by adding a
`data-rail-prefer` attribute to `<main>`. The rail loader checks this first;
if any of the preferred IDs exist in the manifest it uses one of them,
otherwise falls back to the weighted random draw.

```html
<main id="main" data-rail-prefer="warrior-art,combat-art">
```

This attribute is optional and additive -- pages without it get random panels.

### 6.3 Client-side templates

Two panel types, stamped out in JS from manifest entries (no extra fetches,
no new template file format):

**art:**
```html
<figure class="rail-art">
  <img src="{CDN}/{src}" alt="{alt}">
  <!-- figcaption only if caption is non-null -->
</figure>
```

**promo:**
```html
<a class="rail-card" href="{href}">
  <img src="{CDN}/{src}" alt="{alt}">
  <span class="rail-card-title">{title}</span>
  <span class="rail-card-blurb">{blurb}</span>
</a>
```

Both use the existing `SiteConfig.CDN_BASE` for image URLs -- same pattern as
`img()` in `config.js`. Do not introduce a second CDN base variable.

---

## 7. User controls

### 7.1 Cycle button

A small button injected by JS into each active panel. Picks the next item
from the shuffled manifest (skipping the current one):

```html
<button class="rail-cycle-btn" aria-label="Show next panel content">&#8635;</button>
```

### 7.2 Dismiss / off preference

A dismiss button collapses the rail and saves `l1-rails: off` to
`localStorage`, consistent with the existing `L1Prefs` pattern in `config.js`.
Rails stay off across pages until the user re-enables them (via Settings page
or a "show panels" button that appears when rails are off).

Add to `L1Prefs.DEFAULTS` in `config.js`:
```js
rails: 'on',   // 'on' | 'off'
```

Add to `settings.html`: a checkbox "Show side panels when space allows."

### 7.3 Behavior under zoom / font size

- **Browser zoom (Ctrl/Cmd +/-):** transparent -- CSS pixels reflow, media
  queries re-evaluate. No special handling needed.
- **Pinch zoom:** visual transform only; ignore for this feature.
- **`l1-fontsize` large/xl:** text gets taller but the column stays 780px wide,
  so gutter width is unaffected. Panels should be top-anchored within their
  section, not pinned to align with a specific paragraph.
- **OS font scaling / high DPI:** CSS pixels abstract device pixels; breakpoints
  behave as expected.

---

## 8. Hosting notes (GitHub Pages + future AWS)

### GitHub Pages (current)

- Pure static hosting. `panels.json` is just a file in the repo. No server
  needed for the panel system as designed.
- **GitHub Actions** (free, runs on push) is worth setting up for:
  - Auto-running `tools/html2md.py` + `tools/relink_md.py` so markdown copies
    never drift from HTML. A simple workflow triggered on any `L1/**/*.html`
    change would handle this.
  - Lint / link-check runs before deploy.
- **Jekyll** (GitHub's built-in SSG) is available but not recommended here --
  the hand-rolled HTML is cleaner and more controlled than templating would be
  for this project's needs.
- Custom domain is already wired via `CNAME`. No change needed.

### AWS migration (future)

When server-side capability is needed the natural stack is:

- **CloudFront + S3** for static assets (same pattern as current R2 CDN -- just
  a different origin). Assets already on R2 can stay there; CloudFront can
  proxy multiple origins.
- **Lambda + API Gateway** (or Lambda function URLs) for any dynamic endpoints:
  - Personalized panel selection (e.g. "owns the PDF" users see different promo
    cards). Could integrate with itch.io's purchase API or a simple webhook.
  - Future: user accounts, saved preferences server-side, etc.
- The `panels.json` approach is forward-compatible: today it's a static file;
  later the same URL can be a Lambda that returns personalized JSON. The client
  code changes nothing.

### itch.io integration (near-future)

The `buy-pdf` promo card is the natural bridge. Two options:

1. **Static:** just a link to the itch.io page. Works today, zero effort.
2. **Dynamic (future, needs server):** use itch.io's purchase verification API
   to detect returning buyers and swap the promo card for a "thank you / new
   content" card instead of the buy prompt. Requires a Lambda to hold the API
   key safely.

Start with option 1. Design the `panels.json` schema to support both (the
`href` field already does).

---

## 9. Build dependency order

Each step depends only on what came before. Do not skip ahead.

```
1. CSS variables
   -- Add --rail-w, --rail-gap, --rail-side to onesrd.css defaults
   -- Add/override values in L1/style.css
           |
           v
2. panels.json manifest
   -- Create /L1/panels.json with initial art + promo entries
   -- Add SiteConfig.PANELS_URL to config.js
           |
           v
3. rails.js (new file: /resources/rails.js)
   -- Fetches manifest, applies weighted random draw
   -- Wraps .content-wrap in .reading-layout on pages that have it
   -- Stamps out panel HTML from templates
   -- Checks data-rail-prefer hints
   -- Checks l1-rails pref; exits early if 'off'
           |
           v
4. CSS layout rules
   -- .reading-layout grid for States 1 and 2 in L1/style.css
   -- .rail, .rail-art, .rail-card visual styles
           |
           v
5. Cycle + dismiss buttons
   -- JS injects .rail-cycle-btn and .rail-dismiss-btn
   -- Dismiss saves l1-rails pref; Settings page gets a toggle
           |
           v
6. Per-page data-rail-prefer hints (optional, any time after step 3)
           |
           v
7. Approach B: ResizeObserver measurement (optional refinement of step 3/4)
```

---

## 10. Accessibility and quality checklist

- [ ] Page reads correctly with JS disabled (no rails, plain column).
- [ ] Page reads correctly with images disabled (panels collapse cleanly).
- [ ] Panels are `<aside>` elements after main content in DOM order, or
      `aria-hidden="true"` if purely decorative.
- [ ] Decorative-only art uses empty `alt=""`; meaningful art has real `alt`.
- [ ] No keyboard trap; promo links are reachable and have visible focus.
- [ ] `prefers-reduced-motion` and `l1-reducemotion="on"` suppress any panel
      reveal animation.
- [ ] All four themes (default / dark / high-contrast / plain) look correct.
- [ ] All three font sizes (normal / large / xl) keep the column readable.
- [ ] `settings.html` still works "with all styles/images off."
- [ ] No horizontal scrollbar introduced at any breakpoint.
- [ ] No layout shift (CLS) on initial load.

---

## 11. Implementation guidance for the agent (Kiro / Claude Code)

**Read `/CLAUDE.md` first. These instructions inherit every rule in it.**

### What you MAY do

- Add new CSS rules to `/L1/style.css` for `.reading-layout`, `.rail`,
  `.rail-art`, `.rail-card`, and the state breakpoints.
- Add structural defaults for `.reading-layout` / `.rail` to
  `/resources/onesrd.css` **only if explicitly approved**.
- Create `/resources/rails.js` (new file, loaded after `nav.js`).
- Create `/L1/panels.json` (new file).
- Add `SiteConfig.PANELS_URL` and `l1-rails` pref to `config.js` **only for
  those two targeted additions** -- do not otherwise restructure that file.
- Wrap a page's existing `.content-wrap` in `.reading-layout` and add empty
  `<aside class="rail ..." hidden>` elements.

### What you MUST NOT do

- **Do not alter one word of rulebook content.** Layout/structure only.
- **Do not put rules text or comprehension-critical content in a panel.**
- **Do not modify `nav.js`, `nav.html`, or `header.html`** without explicit
  instruction.
- **Do not add inline styles.**
- **Do not introduce a horizontal scrollbar or layout shift.**
- **Do not roll out across all pages at once.** Prototype on `start.html`
  first, get sign-off, then extend in small batches.

### Workflow

1. Confirm exact file list before editing multiple files.
2. Prototype on `start.html` -- move `reader.png` out of `.text-image-block`
   and into a right-hand art panel.
3. Owner tests: resize, zoom, font size, all four themes.
4. After sign-off, extend to additional pages in small batches.
5. Commit at end of every work cycle with file changes. Push only when told.

### Suggested phasing

| Phase | Deliverable |
|-------|-------------|
| 1 | CSS variables + two-state (0/2) grid layout on `start.html`. |
| 2 | State 1 asymmetric single-panel + `--rail-side` control. |
| 3 | `panels.json` manifest + `rails.js` dynamic content loading. |
| 4 | Cycle + dismiss buttons + `l1-rails` pref + Settings toggle. |
| 5 | Per-page `data-rail-prefer` hints on appropriate pages. |
| 6 | (Optional) Approach B ResizeObserver measurement. |
| 7 | (Optional) GitHub Actions workflow to keep markdowns in sync. |
| 8 | (Future/AWS) Personalized panel endpoint replacing static JSON. |

---

## 12. Open questions for the owner

1. **Default single-panel side** in State 1 -- right (recommended) or left?
2. **Rail width** -- is 220px right, or do you want larger art (260-300px)?
3. **Promo cards** -- in scope for Phase 3, or art-only for the first pass?
4. Should rails appear on **index/cover** and **settings** pages, or reading
   pages only? (Recommend: reading pages only.)
5. For art selection: will you provide a per-page `data-rail-prefer` mapping,
   or leave all pages on weighted-random for now?
6. itch.io link in promo card: static link only for now, or worth noting the
   future purchase-detection path in the manifest schema now so it doesn't
   have to be redesigned later? (It already is, per §6.1 above.)

---

## 13. Search

Search is a natural addition to a static rulebook site and requires no server.
The approach is: build a search index at deploy time (or manually), ship it as
a JSON file, and query it entirely in the browser. For a rulebook-sized site
the entire text index is well under 500KB -- practical to download once and
cache.

The search bar lives in the site header (next to the menu button), opens a
modal or inline dropdown on activation, and shows page title + highlighted
text excerpt for each result. No new page required.

### Option A -- Lunr.js (simplest, self-contained)

[Lunr.js](https://lunrjs.com/) is a small (~8KB) client-side full-text search
library. You pre-build an index with a Python script, ship it as a static
JSON file, and Lunr queries it in the browser at runtime.

**How it fits this project:**

- Index builder: a new `tools/build_search_index.py` script, walking the same
  HTML DOM as `html2md.py` and extracting text from each page's `<main>`.
  Output: `/L1/search-index.json`. Same pattern as `panels.json` -- just a
  static file GitHub Pages serves normally.
- Runtime: `search.js` (new file, loaded after `nav.js`) downloads the index
  once, wires up a search input injected into the header, and renders results.
- Lunr itself can be self-hosted on the existing R2 CDN -- no external runtime
  dependency.
- Re-run the index builder whenever pages change. Can be added to a GitHub
  Actions workflow alongside `html2md.py` and `relink_md.py`.

**Pros:** simple, no build toolchain, pure Python + vanilla JS, fits existing
architecture exactly, easy to understand and maintain.

**Cons:** index is pre-built so new/changed pages require a manual re-run (or
Actions automation). Lunr's relevance ranking is basic -- good enough for a
rulebook, not Google.

**Effort:** low. Most of the DOM-walking logic is already written in
`html2md.py`. Index builder is probably an afternoon. Search UI is another
afternoon.

### Option B -- Pagefind (slicker, better results)

[Pagefind](https://pagefind.app/) is a modern static search tool that runs as
a post-build step, auto-crawls your rendered HTML, and generates its own
optimized index shards with built-in excerpt highlighting and result scoring.
Used by many static sites (Hugo, Eleventy, plain HTML).

**How it fits this project:**

- Run `pagefind --site .` (or `--site L1/`) after every deploy. It reads the
  HTML and writes a `pagefind/` directory of index shards.
- A tiny JS snippet in each page (or injected by `search.js`) loads Pagefind's
  own UI component or its bare API.
- Natural home in a GitHub Actions deploy workflow: build step runs Pagefind,
  then Pages deploys the result including the index.

**Pros:** better result quality with highlighted excerpts out of the box;
handles multi-game expansion (indexes the whole site, not just L1) naturally;
index shards are lazy-loaded so large indexes don't slow initial page load.

**Cons:** requires a build step -- not "just commit a file." Needs either a
GitHub Actions workflow or a manual local run before pushing. Adds a new tool
to the dependency chain (though Pagefind is a single binary / npx call with
no lockfile impact if run only in CI). Slightly more moving parts to explain
to a future contributor.

**Effort:** medium. Pagefind itself is nearly zero config. The work is setting
up the GitHub Actions workflow cleanly and wiring the UI into the existing
header without touching `nav.js` or `header.html` structure unexpectedly.

### Recommendation

Start with **Lunr.js** (Option A). It fits the existing "no build pipeline"
architecture, reuses code already written, and is entirely comprehensible. If
search quality or index size becomes a problem later, migrating to Pagefind is
straightforward -- the UI wiring is nearly identical, only the index format
changes.

Add a GitHub Actions workflow at the same time (whether for Lunr or Pagefind)
so the index, the markdowns, and any link rewrites all stay in sync
automatically on every push.

### Agent implementation notes

- **Do not modify `nav.js` or `header.html`** to add the search bar. Instead,
  `search.js` injects the search input element into `#site-header` after the
  header has loaded (same lifecycle as how `nav.js` injects header content).
  Or, preferably, add the search input placeholder to `header.html` directly
  and have `search.js` activate it -- cleaner separation. Confirm approach
  with owner before touching `header.html`.
- Index builder must use the same "extract `<main>` content only" rule as
  `html2md.py` -- no chrome, no nav, no scripts indexed.
- The Prime Directive applies to indexed content too: the index reflects the
  page text verbatim, no summarizing or rephrasing.
- Self-host the Lunr script on the R2 CDN (add its URL to `SiteConfig`) rather
  than loading it from a third-party CDN. Consistent with existing asset
  strategy and avoids external runtime dependencies.
