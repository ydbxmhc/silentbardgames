# Gutter Rails (Side Panels) - Implementation & Handoff

**Status:** Implemented and live on the branch. Rails appear on all standard L1
content pages.
**Audience:** A fresh Claude Code / Kiro session picking this up cold. Read
`/CLAUDE.md` first - every rule there applies here.
**Original design rationale:** `docs/dynamic-side-panels.md` (the proposal; this
file is the as-built reference and supersedes it where they differ).

---

## 1. What this is

The reading column is a fixed 780px, centered, which leaves wide empty margins
("gutters") on large screens. The gutter-rails feature fills that space, when it
is available, with optional panels: the Table of Contents, the Settings
controls, promo cards (itch / Kickstarter), or art. Panels are independent
per side, the reader's choices persist across pages, and everything degrades
cleanly to the normal single-column page on narrow screens or with JS off.

It is a **progressive enhancement**. Nothing about the base reading experience
depends on it.

---

## 2. How it works (data flow)

```
config.js   → defines SiteConfig (BASE_PATH, CDN_BASE) and L1Prefs (incl. the
              new `rails` and `railside` prefs). Loaded first on every page.
nav.js      → after injecting header.html + nav.html, appends a <script> tag for
              rails.js. This is the ONLY thing that loads rails on every page.
rails.js    → self-injects the layout: finds #main > .content-wrap, wraps it in
              a .reading-layout, and adds a left and right <aside class="rail">.
              Then fetches panels.json and renders each rail from saved state.
panels.json → the data feed: the list of panel "sources", the art pool, and the
              default source for each side.
style.css   → the three-state CSS (single column / one panel / two panels),
              rail controls, and injected-content styling.
```

Because `nav.js` loads `rails.js`, **pages need no per-page markup or script** - 
the cover (`index.html`) and fragment files have no `.content-wrap`, so
`rails.js` no-ops there automatically.

---

## 3. The three layout states (CSS, in `L1/style.css`)

Driven by media queries keyed off viewport width. The reading column is a fixed
`--content-max` (780px), so the math is stable.

| State | Width (approx.) | Behavior |
|-------|-----------------|----------|
| 0 | < 1060px | Single centered column, no rails (identical to a normal page). |
| 1 | 1060-1339px | One panel fits. Column shifts to one side; the single rail fills the freed margin. Which side is kept = the `railside` pref (default **left**). |
| 2 | ≥ 1340px | A panel on each side; column stays centered. |

Rails **grow to fill** their gutter (no fixed cap on the rail itself). Inside,
card-style content (art, promos) is capped at `--card-max` and centered, while
the TOC fills the whole rail (`.rail-wide`). The panels are `position: sticky`
so they stay in view while scrolling - this requires the grid to use
`align-items: stretch` (a sticky child needs a parent taller than itself; a
non-stretch grid cell shrinks to content and kills sticky).

Tunable CSS variables (in `:root`, `L1/style.css`):
- `--rail-w` (240px) - minimum rail width; **sets the breakpoint thresholds**.
  If you change it, update the `@media` px (queries can't read `var()`):
  State1 = `780 + rail-w + gap`, State2 = `780 + 2*(rail-w + gap)`.
- `--rail-gap` (2rem) - gap between column and rail.
- `--card-max` (340px) - cap for art/promo cards.

---

## 4. The panel source model (`L1/panels.json`)

```json
{
  "defaults": { "left": "toc", "right": "random" },
  "art": ["reader.png", "corner-dice.jpg", "Raven_and_Toad-BW.jpg", "cover-fullBox.png"],
  "sources": [
    { "id": "toc",      "label": "Table of Contents", "kind": "fragment", "src": "toc.html",      "extract": "ul.toc",          "rewrite": true },
    { "id": "settings", "label": "Display Settings",  "kind": "fragment", "src": "settings.html", "extract": ".settings-group", "wire": "settings" },
    { "id": "itch",     "label": "Get the PDF",       "kind": "fragment", "src": "panels/itch.html",        "promo": true },
    { "id": "ks",       "label": "Kickstarter",       "kind": "fragment", "src": "panels/kickstarter.html", "promo": true },
    { "id": "random",   "label": "Art",               "kind": "random",                                    "promo": true }
  ]
}
```

Source fields:
- `id` - stable identifier (persisted per side; survives manifest reordering).
- `label` - caption shown under the panel.
- `kind` - `fragment` (fetch + inject HTML), `art` (single CDN image via `src`),
  or `random` (random image from the `art` pool).
- `src` - for fragments, resolved against `BASE_PATH` unless absolute. For
  `kind:"art"`, a CDN filename.
- `extract` - CSS selector; inject only the matched element(s) from the fetched
  page, not the whole document. Used to pull the live TOC out of `toc.html` and
  the live controls out of `settings.html` (single source of truth).
- `rewrite: true` - rewrite the extracted fragment's relative `<a href>`s by
  prepending `BASE_PATH` (the same thing `nav.js` does for drawer links).
- `wire: "settings"` - after injecting, bind the controls to `L1Prefs` (see §6).
- `promo: true` - eligible for the `pushPromo()` action (see §7).

`src`/`extract` work with `data-src` CDN images too: `rails.js` resolves any
`img[data-src]` inside an injected fragment (the `config.js` / `nav.js` pattern).

---

## 5. Per-rail persistence

Each side stores its state in `localStorage`:
- `l1-rail-left`, `l1-rail-right` - JSON `{ id, pinned, open }`. So "TOC parked
  on the left, pinned" survives navigation. Stored by source `id`, not index.

Global prefs (managed by `L1Prefs`, see §6):
- `l1-rails` - `on` | `off` (show rails at all).
- `l1-railside` - `left` | `right` (which side wins in State 1; default `left`).

---

## 6. Settings integration (`config.js` + `settings.html` + `rails.js`)

The Settings page and the in-rail Settings panel are the **same controls** - 
the panel is extracted live from `settings.html` via `extract: ".settings-group"`,
so they can't drift.

- `config.js` - `L1Prefs.DEFAULTS` gained `rails: 'on'` and `railside: 'left'`.
  `L1Prefs` persists to `localStorage` under the `l1-` prefix and applies each
  pref as a `data-*` attribute on `<html>`.
- `settings.html` - gained a "Side Panels" group (show/hide checkbox + left/right
  radio). Its inline `<script>` initializes, live-previews, saves, and resets
  them alongside the existing prefs. (Inline scripts run on the standalone page.)
- `rails.js` `wireSettings()` - because injected `<script>` never runs, the host
  re-binds the injected controls to `L1Prefs` after injection. It handles theme
  + fontsize radios, the `railside` radios, and the checkboxes (navbg / motion /
  rails) identified by their group `<h2>` text. IDs are stripped on injection to
  avoid duplicate-`id` collisions when two Settings panels are open.

**Important behavior:** `rails`/`railside` take effect on the **next page load**,
not live. They control the *layout* that `rails.js` builds on load. Theme and
text-size still apply live (they're pure CSS `data-*` attributes). If a live
on/off toggle is wanted later, route rail visibility through an `html[data-rails]`
attribute in CSS instead of reading the pref once at load.

---

## 7. JS API

`rails.js` exposes `window.OneSRDRails.pushPromo()` - retargets every un-pinned,
open rail to a random `promo` source. Not wired to any UI on the live site yet;
intended for a future owner control or timed rotation. Pinning a panel (the ★
button) protects it from this.

---

## 8. File inventory

| File | Role | Protected? |
|------|------|-----------|
| `resources/rails.js` | The whole feature: layout injection, fetch/extract/inject, controls, persistence, settings binding. | No (new file) |
| `L1/panels.json` | Source feed + art pool + defaults. | No |
| `L1/panels/itch.html` | Promo fragment (placeholder href - replace with real itch URL). | No |
| `L1/panels/kickstarter.html` | Promo fragment (placeholder href). | No |
| `L1/style.css` | Rail CSS appended at the end (clearly sectioned). | No (theme layer) |
| `resources/nav.js` | One appended block that loads `rails.js`. | **Yes** - touched on explicit instruction. |
| `L1/config.js` | Added `rails`/`railside` to `L1Prefs.DEFAULTS`. | **Yes** - touched on explicit instruction. |
| `L1/settings.html` | Added "Side Panels" group + script wiring. | **Yes** - touched on explicit instruction. |

The throwaway demo (`docs/side-panel-demo.html` + `docs/panels/`, `docs/promos/`)
has been removed.

---

## 9. Testing

`fetch()` is blocked on `file://`, so test over http:

```bash
python -m http.server 8000     # from the repo root
# then open http://localhost:8000/L1/start.html
```

Check:
- A normal page (`/L1/dice.html`) and a nested one (`/L1/roles/warrior.html`) - 
  rails appear; pinned/source choices carry across pages.
- The cover (`/L1/index.html`) - no rails (no `.content-wrap`).
- The TOC panel - real contents, links navigate.
- The Settings panel - changing theme/text-size restyles live and persists;
  toggling Side Panels / side takes effect on the next page load.
- Narrow the window - collapses to the normal single column.

---

## 10. Open follow-ups (not done)

1. **Real promo URLs.** `L1/panels/itch.html` and `kickstarter.html` use
   placeholder hrefs (`itch.io`, `kickstarter.com`). Drop in the real links.
2. **Redundant panels.** Rails currently also show on `toc.html` and
   `settings.html` (a TOC beside the TOC page). Harmless; suppress with a
   per-page opt-out (e.g. a `body[data-no-rails]` check in `rails.js`) if wanted.
3. **Live on/off.** See §6 - currently load-time. Optional.
4. **Promo policy.** Promos are reader-cycleable today. If they should be
   owner-pushed only, filter them out of the `< >` cycle and drive them via
   `OneSRDRails.pushPromo()`.
5. **Image optimization / CDN.** Unrelated to rails but relevant: the R2 art is
   served from the dev endpoint and is unoptimized. Custom domain + resized art
   would speed everything up (see chat history / `config.js` CDN note).
6. **Multi-game.** `rails.js` and the `nav.js` loader live in shared
   `/resources/`. A future game needs its own `<game>/panels.json` and the rail
   CSS vars in its own `style.css`; the JS already keys off `SiteConfig.BASE_PATH`.

---

## 11. Conventions (from `/CLAUDE.md`)

- **No rulebook content in rails** - art, navigation, and promos only. Nothing a
  reader must read to understand the game.
- **No inline styles** - JS toggles classes / sets attributes; CSS lives in
  stylesheets.
- **Don't modify** `nav.js`, `config.js`, `settings.html`, `nav.html`,
  `header.html`, `onesrd.css` without explicit instruction. The three that were
  touched here (`nav.js`, `config.js`, `settings.html`) were done on the owner's
  explicit go for this feature; keep changes there minimal and additive.
- **Reuse, don't duplicate** - the TOC and Settings panels are extracted from the
  real pages, not re-authored. Keep it that way.
