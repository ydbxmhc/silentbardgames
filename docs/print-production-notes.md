# Print Production - Session Notes & Method

**Date:** 2026-07-12
**Context:** Building the print booklet line for *Level One* from the website source.
Companion to `print-booklet-plan.md`.

## Goals

- Turn the single ~156pp SRD into a line of standalone, saddle-stitch **digest
  (5.5 x 8.5)** booklets. Print only; the website stays the source of truth and is
  unchanged.
- Keep every booklet *derived from the website text* - verbatim prose (the Prime
  Directive), reflowed for print, not rewritten.
- Make the pipeline reproducible locally with near-zero install.

## Done this session

**Tricks (now canon):**
- Developed genre example Tricks (fantasy / sci-fi / horror); refined "The Opener"
  and the resist-vs-oppose reasoning.
- Built `L1/tricks.html` + `.md`; wired into `nav.html`, `nav.md`, `toc.html`,
  `toc.md`, and the prev/next chain between Hooks on Credit and Nonhuman. Live.
- Logged two rules clarifications for the source refactor: resist-vs-oppose applies
  to *any* imposed effect; Release is "no *reroll*," not "no roll."

**Print plan:** `print-booklet-plan.md` - four booklets (Core, Roles & Maneuvers,
Magick, Running the Game), page-accurate, with the web deltas to fold in.

**Pipeline + calibration:**
- Chose **WeasyPrint** (Python, no browser) for automated builds/proofs in the
  workspace; **Paged.js** (loads in the user's own Chrome, zero install) for local
  preview and print. The *same CSS* drives both.
- Measured real digest page counts (text only): Warrior chapter 10pp (its vignette is
  an outlier), Sneak 4pp; **all ten mundane Roles = 80pp** (busts the 64pp staple ->
  Roles must split by category); **Core = 77pp** (busts -> splits back into Mechanics +
  Characters, vindicating the original instinct).
- Built the **Core Rules** digest working copy (Getting Started + Core Mechanics, Gear
  pulled to the GM book): **~34pp**, fits one booklet comfortably.
- Laid out **page 1** as the template page.

## Method & tooling notes

- Text is pulled straight from the `.md` mirrors; a cleaner strips breadcrumb /
  category / nav / hr lines; images stripped except deliberately placed art.
- **Digest inflation:** letter -> digest is roughly 1.3-2x more pages (digest is
  exactly half a letter sheet). Predicted 62-96pp for Roles; measured 80. Method holds.
- **Vignettes drive Roles size:** the "In Action" stories run ~5x the rules bulk and
  vary wildly (Sneak 409 words vs Warrior 2053). *Where the vignettes live* is the real
  Roles-sizing lever, not the trim.
- **Saddle-stitch ruler:** page counts in multiples of 4, ~64pp practical ceiling.
  Movable full-page art = shims to hit the multiple.
- **Art layout techniques (all CSS, proven on page 1):** `float` with text wrap;
  negative top margin to nudge a float up; `<br>` for a line break without paragraph
  spacing; `mix-blend-mode: multiply` to warm a gray-backed sketch into the parchment;
  `mask-image` radial gradient to feather a hard image edge to nothing; `transform:
  rotate` for a "tossed sketch" tilt.
- **Sandbox can't reach R2:** the PDF proof shows sized placeholders for art; the real
  images load in the user's Chrome via the HTML working copy. So local review = the
  HTML opened in Chrome.
- **Workflow that worked:** one page at a time - tighten spacing to fit, review the
  HTML in Chrome, iterate in small nudges.

## Tooling rationale (why this, not Canva or a DTP app)

This is long-form, reflowable, single-source typesetting across many pages and several
booklets. Canva - and manual DTP like InDesign or Affinity - is *per-page manual
layout*: excellent for covers, character sheets, posters, and marketing, but wrong for
interiors that must reflow from a source and regenerate on every edit. The CSS pipeline
keeps print *derived from the website*, preserves the text verbatim, and re-flows
automatically. Use Canva for the **cover and the marketing**, not the **guts**.

## Open / next

- Finish the remaining Core pages one at a time; then the other booklets (Roles as ~4
  category booklets; Magick incl. the supernatural roles; Running the Game incl. Gear +
  appendices).
- Fold the web deltas into the *source* (Tricks, Hooks on Credit, Gear Traits, Assist
  Rule; the two rules clarifications; the chargen mention).
- **Web/print divergence:** page 1 now uses a trimmed print intro. Reconcile intentional
  divergences later, or accept them as print-specific.
- Art at **300dpi** for print (web art is screen-res); bleed + crop marks at export;
  imposition is downstream (POD usually handles it from a reader-order PDF).
- Commit from Windows (sandbox git can't write to the repo here).


## Later edits

**2026-07-14 - combat-chain order settled (web + print agree).** The website moved
*The Kamikaze Blitz* out of the Harm & Recovery tail into the combat run, directly
after *Resolving Combat* (chain: Resolving Combat -> The Kamikaze Blitz -> Luck Tokens;
Advanced Options -> Gear closes the gap). It reads as combat-resolution content, not
recovery. `WIP/core-rules-digest.html` was reordered to match, so the Core booklet and
the site agree - no intentional divergence here. Advanced Options stays in Harm &
Recovery on both (its content really is healing/recovery options).
