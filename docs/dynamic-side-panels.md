# Proposal: Dynamic Side Panels ("Gutter Rails")

**Status:** Proposal / not yet implemented
**Scope:** L1 subsite (`/L1/`), with an eye toward reuse by future OneSRD games
**Author intent:** Use the empty left/right margins of the centered reading column
to display art (and, optionally, small promotional cards with links) — but only
*when the viewport genuinely has room*, and degrade gracefully to today's
centered single-column layout when it does not.

> This document is written to be read by a human (the site owner) **and** to be
> handed to an implementing agent (Kiro or Claude Code). The implementation
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
viewport that is roughly **(1920 − 780) / 2 ≈ 570px per side** of unused
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
   narrow screen, the page must look and read exactly like it does today. Side
   panels are an *addition* that appears only when conditions are met.
3. **No rulebook content in the gutters.** Per `/CLAUDE.md`'s Prime Directive,
   the side panels carry *art* and *promotional/navigational* material only —
   never rules text, never examples, never anything a reader must read to
   understand the game. Nothing in a gutter may be load-bearing for
   comprehension.
4. **Respect user preferences.** The existing prefs (`l1-theme`,
   `l1-fontsize`, `l1-navbg`, `l1-reducemotion`) must continue to work. Large
   font sizes and reduced-motion settings must be honored by the panel system.
5. **No inline styles.** All styling goes in CSS files per `/CLAUDE.md`. JS may
   only toggle classes / set CSS custom properties — never write style strings.
6. **Don't touch the untouchables without instruction.** `nav.js`, `config.js`,
   `nav.html`, `header.html`, and `onesrd.css` are listed as protected in
   `/CLAUDE.md`. See §8 for how this proposal stays inside those lines.

---

## 3. The three layout states

The viewport can be in one of three states with respect to gutter space. The
content column is a fixed 780px, so the math is simple and stable.

Let:

- `C` = content column width = **780px** (`--content-max`)
- `R` = minimum usable rail width (image box), proposed **220px**
- `G` = breathing-room gap between column and rail, proposed **32px** (2rem)
- `V` = available viewport width (excluding scrollbar)

| State | Condition (approx.) | Behavior |
|------|----------------------|----------|
| **0 — Single column** | `V < C + (R + G)`  → below ~1064px | Today's layout. Centered column, no rails. |
| **1 — One panel (asymmetric)** | `C + (R + G) ≤ V < C + 2·(R + G)` → ~1064–1348px | Enough combined margin for **one** rail. Shift the column off-center and open a single panel on the side with room. |
| **2 — Two panels (symmetric)** | `V ≥ C + 2·(R + G)` → ~1348px+ | Centered column with a rail on **both** sides. |

> The numbers above are starting proposals. Final breakpoints should be tuned
> visually during implementation (see §7 testing). The key idea is the
> **three states**, not the exact pixels.

### 3.1 The asymmetric ("State 1") case — the interesting one

This is the case the owner specifically called out: when the left and right
margins *added together* are enough for one panel but neither alone is. The
solution is to stop centering the column and instead bias it to one side,
pooling the freed space into a single wider gutter that can host one panel.

```
State 0 (narrow):            State 1 (one panel):           State 2 (wide):
                                                            
|  [   column   ]  |         | [  column  ] [ panel ] |     | [panel] [column] [panel] |
   centered                    column shifted left,           column centered,
   no panels                   panel opens on the right       panel each side
```

Whether the single panel opens on the **left** or the **right** should be a
deliberate choice, not random. Recommended default: open on the **right** (the
side a left-to-right reader's eye leaves last), with the column shifted left.
Make the side configurable (see §6 data model: `data-rail-side`).

---

## 4. Implementation approaches

Two routes are viable. They are **not** mutually exclusive — Approach A is the
recommended baseline; Approach B is an optional refinement layered on top.

### Approach A — CSS-first (recommended baseline)

Drive the three states with media-query breakpoints and CSS Grid. The browser
re-evaluates breakpoints automatically on resize, on Ctrl/Cmd +/- zoom (which
reflows in CSS pixels), and on resolution changes — so most of the variability
the owner worried about is handled for free, with zero JavaScript.

Conceptual structure (a new optional wrapper inside `#main`, *additive* to the
existing `.content-wrap`):

```html
<main id="main">
  <div class="reading-layout">            <!-- NEW optional wrapper -->
    <aside class="rail rail-left"  hidden></aside>
    <div class="content-wrap"> ... existing page body unchanged ... </div>
    <aside class="rail rail-right" hidden></aside>
  </div>
</main>
```

```css
/* State 0 is the default: rails stay [hidden], layout is the plain column. */

/* State 2 — symmetric, two rails */
@media (min-width: 1348px) {
  .reading-layout {
    display: grid;
    grid-template-columns: 1fr var(--content-max) 1fr;
    column-gap: var(--rail-gap, 2rem);
    align-items: start;
    max-width: calc(var(--content-max) + 2 * (var(--rail-w, 220px) + var(--rail-gap, 2rem)));
    margin-inline: auto;
  }
  .reading-layout .rail { display: block; }
}

/* State 1 — asymmetric, single rail on the right, column biased left */
@media (min-width: 1064px) and (max-width: 1347.98px) {
  .reading-layout {
    display: grid;
    grid-template-columns: var(--content-max) 1fr;  /* column + one rail */
    column-gap: var(--rail-gap, 2rem);
    align-items: start;
    max-width: calc(var(--content-max) + var(--rail-w, 220px) + var(--rail-gap, 2rem));
    margin-inline: auto;
  }
  .reading-layout .rail-right { display: block; }
  /* rail-left stays hidden */
}
```

**Pros:** bulletproof, no JS dependency, automatically correct under zoom and
font scaling, nothing to maintain.
**Cons:** keys off *viewport width* (a fixed breakpoint), not the *actual
measured* gutter; the left/right choice in State 1 is fixed in CSS rather than
chosen from real measurements.

### Approach B — JS measurement (optional refinement)

When you want the panels to react to *actually rendered* space (accounting for
scrollbar width, the user's font-size preference, container padding, etc.),
measure directly and toggle classes on `<html>`. CSS then responds to those
classes instead of (or in addition to) raw breakpoints.

Reliable primitives:

- `element.getBoundingClientRect()` on `.content-wrap` → real rendered left /
  right / width in CSS pixels.
- `document.documentElement.clientWidth` → viewport width **excluding** the
  scrollbar (compare with `window.innerWidth` to derive scrollbar width).
- `ResizeObserver` → fires on any size change including font-size-pref reflow;
  cleaner than the `resize` event.
- `window.visualViewport` → only needed if you care about mobile pinch-zoom
  (a desktop-oriented feature can ignore it).

Reference sketch (illustrative — final code lives in a new file, see §8):

```js
// resources/rails.js  (NEW file — does NOT modify nav.js/config.js)
(function () {
  const layout  = document.querySelector('.reading-layout');
  if (!layout) return;                       // page opted out → do nothing
  const content = layout.querySelector('.content-wrap');

  const RAIL_MIN = 220;   // keep in sync with --rail-w
  const GAP      = 32;    // keep in sync with --rail-gap

  function measure() {
    const docW = document.documentElement.clientWidth;   // excludes scrollbar
    const need = RAIL_MIN + GAP;
    const total = docW - content.offsetWidth;            // combined gutter
    const root = document.documentElement;

    root.classList.toggle('rails-2', total >= 2 * need);
    root.classList.toggle('rails-1', total >= need && total < 2 * need);
    // rails-0 = neither class set
  }

  const ro = new ResizeObserver(measure);
  ro.observe(content);
  ro.observe(document.documentElement);
  window.visualViewport?.addEventListener('resize', measure);
  measure();
})();
```

**Pros:** reacts to true available space; can make a smarter left/right
decision; can account for font-size pref and scrollbar.
**Cons:** more moving parts; must guard for JS-off (panels simply never appear,
which is acceptable per principle #2).

> **Recommendation:** ship Approach A first and confirm it feels right. Only add
> Approach B if/when you want measurement-driven behavior beyond fixed
> breakpoints. Do not build B without A as the fallback.

---

## 5. Behavior of zoom, font size, and resolution

The owner asked specifically how robust this is to user variability. Summary:

- **Browser zoom (Ctrl/Cmd +/-):** transparent. It changes the effective
  CSS-pixel viewport; layout reflows and both media queries and
  `getBoundingClientRect()` report the new values. No special handling.
- **Pinch zoom (touch):** does not reflow; it is a visual transform. Only
  `window.visualViewport` sees it. Safe to ignore for a desktop side-rail
  feature.
- **Font-size preference (`l1-fontsize` large/xl) and OS font scaling:** text
  gets *taller*, but because the column is a fixed `780px` the gutters do **not**
  change width. So "is there horizontal room?" stays accurate. The thing this
  affects is *vertical* alignment between a panel and a specific paragraph — so
  panels should be **self-contained and top-anchored within their section**, not
  pinned to line up with a particular sentence.
- **Screen resolution / DPI:** CSS pixels already abstract device pixels, so a
  HiDPI display reports the same CSS width as its logical resolution. Breakpoints
  behave as expected; serve high-resolution art via the CDN as usual.

---

## 6. Content model for panels

Panels are populated declaratively so an author can drop them into a page
without writing JS. Two panel types are proposed.

### 6.1 Art panel

```html
<aside class="rail rail-right" data-rail-side="right" hidden>
  <figure class="rail-art">
    <img data-src="art/raven-and-toad.jpg" alt="Descriptive alt text">
    <figcaption>Optional caption.</figcaption>
  </figure>
</aside>
```

- Uses the existing `data-src` → CDN resolution already implemented in
  `config.js` / `nav.js` (`img()` helper). **Reuse it; do not reinvent it.**
- `alt` text is required and must describe the art, not the rules.

### 6.2 Promo / mini-page card (optional, later phase)

A small card with a heading, blurb, and link — e.g. "New supplement," "Buy the
PDF," "Join the Discord." These are **promotional**, never rulebook content.

```html
<aside class="rail rail-right" hidden>
  <a class="rail-card" href="https://silentbardgames.com/...">
    <img data-src="promo/cover-thumb.jpg" alt="">
    <span class="rail-card-title">Level One: Companion</span>
    <span class="rail-card-blurb">Optional rules &amp; new roles.</span>
  </a>
</aside>
```

Keep promo content in the panel markup (or a small JSON/partial loaded the same
way `nav.js` loads `nav.html`) — **decided during implementation, with owner
sign-off**, since it touches the "how do we load shared content" question.

### 6.3 Suggested CSS custom properties (theme-able)

Add to L1 `style.css` (the theme layer), not `onesrd.css`:

```css
:root {
  --rail-w:   220px;   /* min usable rail width */
  --rail-gap: 2rem;    /* space between column and rail */
}
```

---

## 7. Accessibility & quality checklist

- [ ] Page reads correctly with **JS disabled** (no rails, plain column).
- [ ] Page reads correctly with **images disabled** (panels collapse cleanly).
- [ ] Panels are `<aside>` elements and are **after** the main content in DOM
      order, or otherwise marked so screen readers reach rules text first.
- [ ] Decorative-only art uses empty `alt=""`; meaningful art has real `alt`.
- [ ] No keyboard trap; promo links are reachable and have visible focus.
- [ ] `prefers-reduced-motion` and `l1-reducemotion="on"` suppress any panel
      reveal animation.
- [ ] All four themes (default / dark / high-contrast / plain) look correct.
- [ ] All three font sizes (normal / large / xl) keep the column readable and
      panels from colliding with text.
- [ ] `settings.html` still works "with all styles/images off" (per `/CLAUDE.md`).
- [ ] No layout shift / horizontal scrollbar introduced at any breakpoint.

---

## 8. Implementation guidance for the agent (Kiro / Claude Code)

**Read `/CLAUDE.md` first. These instructions inherit every rule in it.**

### What you MAY do

- Add **new** CSS rules to `/L1/style.css` (the theme layer) for `.reading-layout`,
  `.rail`, `.rail-art`, `.rail-card`, and the state breakpoints.
- Add structural defaults for `.reading-layout` / `.rail` to `/resources/onesrd.css`
  **only if explicitly approved** — otherwise keep it in `style.css` to avoid
  touching a protected shared file (see "do not touch" below).
- Create a **new** file `/resources/rails.js` for Approach B, loaded *after*
  `nav.js`, only if/when Approach B is requested.
- Wrap a page's existing `.content-wrap` in the new `.reading-layout` container
  and add empty `<aside class="rail …" hidden>` elements.
- Populate panels using the existing `data-src` CDN mechanism.

### What you MUST NOT do

- **Do not alter one word of rulebook content.** This work is layout/structure
  only. The Prime Directive in `/CLAUDE.md` is absolute.
- **Do not put rules text, examples, or comprehension-critical material in a
  panel.** Gutters are for art and promo only.
- **Do not modify `nav.js`, `config.js`, `nav.html`, or `header.html`** without
  an explicit instruction. The rail system is designed to need none of these
  changed. Reuse `config.js`'s `img()` / `data-src` resolution rather than
  duplicating it.
- **Do not add inline styles.** JS toggles classes / sets custom properties only.
- **Do not introduce a horizontal scrollbar** or any layout shift at any width.
- **Do not roll this out across all pages at once.** See workflow below.

### Workflow (per `/CLAUDE.md`)

1. **Confirm scope before editing multiple files.** Propose the exact file list
   first and wait for the owner's go-ahead.
2. **Prototype on ONE page** — recommend `start.html`, moving `reader.png` out of
   `.text-image-block` and into a right-hand art panel. Show the result.
3. Have the owner resize the window, use Ctrl +/- zoom, switch font size in
   `settings.html`, and cycle all four themes to confirm behavior.
4. Only after sign-off, extend the pattern to additional pages — still in small,
   verifiable batches, not a single sweep.
5. **Commit at the end of every work cycle in which files changed.** Push only
   when the owner explicitly says to push.
6. If anything about the source PDF, art placement, or wording is unclear,
   **stop and ask** — do not improvise content.

### Suggested phasing

| Phase | Deliverable |
|------|-------------|
| 1 | CSS-only (Approach A): `.reading-layout` + two-state (State 0 ↔ State 2) rails, prototyped on `start.html`. |
| 2 | Add the asymmetric **State 1** (single panel, shifted column). |
| 3 | (Optional) Approach B `rails.js` measurement-driven refinement. |
| 4 | (Optional) Promo / mini-page card panel type. |
| 5 | Roll out to remaining pages in batches, with per-batch review. |

---

## 9. Open questions for the owner

1. **Default single-panel side** in State 1 — right (recommended) or left?
2. **Rail width** — is 220px right, or do you want larger art (e.g. 260–300px)?
3. **Promo cards** — in scope now, or art-only for the first pass?
4. Should rails ever appear on **index/cover** and **settings** pages, or only on
   reading pages? (Recommend: reading pages only.)
5. For art selection: will you provide a per-page mapping of which art belongs in
   which gutter, or should the agent leave labeled placeholders for you to fill?
6. Approach A only for now, or do you want B (measurement) in the first build?
