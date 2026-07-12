# Print Booklet Split - Plan

**Status:** design plan, not yet executed. Print-only restructure. The website is NOT affected.
**Date:** 2026-07-12

## Why

The single ~156-page SRD is too much to present as one object. Split it into standalone,
saddle-stitch booklets, one per major department. Smaller books bind cheaply and
approachably, each reads as a coherent volume, and the line could support modular
crowdfunding later.

**Not** split by tier or level. Level One is flat - a Boost is a Boost at Level 1 or
Level 10, the engine does not gain gears as you climb - so a depth split (the "blue box"
model) has nothing to cut along. The split is by topic / department.

## The ruler: saddle-stitch

- Page counts must be multiples of 4.
- Practical ceiling ~64pp before the staple fails and the center pages creep. Target
  comfortably under it.
- Avoid sub-16pp pamphlets; fold them into a neighbor.
- **Movable full-page art = shims.** Keep two or three full-page illustrations "loose"
  and drop one into whichever booklet sits short of a fold, to true every booklet to a
  multiple of 4 without writing or cutting a word.

## Shared front-matter

Every booklet **except Core** opens with a condensed mechanics primer (~2-4pp): EL,
making a roll, Boost, Wager, resist vs. oppose, Harm. Seed it from the existing Quick
Reference page. This keeps each booklet usable at the table without re-teaching - or
duplicating - the whole engine. Full duplication would drift out of sync across booklets
and away from the website, which stays the source of truth.

## The four booklets (page-accurate against the current print source)

| Booklet | Source pages | Content pp | + primer | Notes |
|---|---|---|---|---|
| **Core** | 9-48 | ~40 | - (it *is* the mechanics) | Intro + Core Mechanics + Gear + Karma + Building a Character. The spine; the standalone Kickstarter. Already a multiple of 4. |
| **Roles & Maneuvers** | 49-96 | ~48 | ~52 | Mundane roles only (supernatural moved to Magick). Clean slice - supernatural sat at the tail. |
| **Magick** | 97-112 + 127-149 | ~39 | ~44 | System + the three practitioners (Adept, Spellweaver, Conjuror) bound together. One grimoire. |
| **Running the Game** | 113-126 + 150-156 | ~21 | ~24 (≈28 w/ shim) | GM material + appendices (Threats, Glossary, Builds, Safety). Smallest; bulked by the bestiary. |

All four sit inside the staple's comfort zone.

## Deltas to fold in during the refactor

The website has grown past the print source. These are **canon on the web but not yet in
the print doc**, and must land in the right booklet:

**Into Core (Characters section):**
- **Tricks** - now canon (`L1/tricks.html` + `.md`, live on the web). Slots after the
  Hooks chain, before Nonhuman.
- **Hooks on Credit** - web page, absent from the print TOC.
- One line in **Building a Character** naming Tricks alongside Hooks as a standard,
  no-cost part of building a character (author to write - rulebook prose).

**Into Core (Gear section):**
- **Gear Traits** - web page, not in print.
- **The Assist Rule** - web page, not in print.
- **Reach** - Weapons subsection present on the web.

**Rules clarifications (settled, need wording in the source):**
- **Resist vs. oppose on imposed effects** - one clarifying line or margin note on the
  Resistance page (Core). The choice applies to *any* imposed effect, not just blows.
- **Release "no reroll"** - reword the Spellweaver Release definition (Magick) from
  "no roll" to "no *reroll*"; the banked value is the caster's stored roll, contestable
  like any result (resist to cancel, or oppose it).

**Budget check:** these add roughly +3-4pp to Core (40 -> ~44). Still staples; reclaim
room from the filler-art half-pages if needed.

## Production notes

- Booklets are print compilations **derived from the website** (the source of truth).
  Keep them derived to avoid divergence.
- **Start with Core** - it stands alone, it funds itself, and every other booklet is
  measured against it.
- Watch **Traits**: it lives in the GM booklet but is referenced from Core (gear traits)
  and Magick (spell-specific traits). Mind the cross-references, or repeat the short
  definition where needed.

## Deferred / to decide

- Whether Roles wants further subdivision if it ever grows past the staple ceiling.
- Kickstarter strategy: dependent booklets crowdfund poorly - nobody backs a book they
  cannot use without a Core they do not own. Fund Core (standalone); release or bundle
  the rest. Per-booklet micro-campaigns mainly build a track record, which cuts both
  ways, since late or failed campaigns publish just as loudly as delivered ones.
