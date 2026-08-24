# Link and anchor audit - 2026-08-24

> **RESOLVED the same day.** Every defect below was a generator bug, and all of
> them are fixed. Post-fix audit: `L1/` **0 broken nav targets, 0 broken anchors,
> 0 missing images**, and `TS/` came clean too as a side effect - its 54 broken
> targets, 43 broken anchors and 55 missing card images all resolved without
> touching the game. See "Resolution" at the foot of this file. The baseline
> below is kept as the record of what was wrong.

Read-only baseline taken before the refactor begins, so that new breakage stays
distinguishable from old. Nothing was changed. Repeat the run after each batch of
edits to see what moved.

Scope: every `.html` and `.md` in the repo except `.git`, `_to_delete`,
`_scratch`, `.kiro`. External links were collected but not fetched.

    412 files    4762 nav links    65 image embeds    84 external

Every internal `href` was resolved against the filesystem, and every `#fragment`
against the ids that actually exist on its target page.

---

## Headline: the live L1 site is clean

    L1/     230 files    3538 nav links
            BROKEN NAV TARGETS ....... 0
            BROKEN HTML ANCHORS ...... 0

Not one dead page link. Not one dead anchor in any `.html` file. The nav drawer,
the TOC, every prev/next chain, every cross-reference, and all 51 glossary
anchors added on 2026-08-20 resolve correctly.

**Every defect found in `L1/` is in the `.md` mirrors, and only there.** The
mirrors are reachable through GitHub and by direct URL, not through the site, so
none of this is visible to a reader on silentbardgames.com. It is still worth
fixing, because the mirrors are the corpus the planned Lunr index will be built
from.

---

## The 18 broken anchors in `L1/*.md` - two root causes

### Cause A: hand-set HTML ids do not match GitHub's heading slugs (5)

The HTML uses a short, deliberate id. The Markdown mirror keeps that id in the
link but has no way to produce it, because GitHub slugs the *full heading text*.

| Link, as written in the mirror | Heading in the mirror | Slug GitHub actually generates |
| --- | --- | --- |
| `actions-and-timing.md#free-action-boosts` (x2) | Free Action Access to Pre-existing Boosts | `free-action-access-to-pre-existing-boosts` |
| `quickstart.md#character-drives` | Character Drives and Methods | `character-drives-and-methods` |
| `dice.md#rather-not` | (target heading differs) | - |
| `harm.md#hit-points` | (target heading differs) | - |

The HTML side of each of these is correct and should not be touched. The fix
belongs in the mirror generator, which needs to rewrite fragments to the slug the
Markdown will actually produce. `@@*`

### Cause B: anchors on non-heading elements have no Markdown equivalent (13)

| Target | Count | What it is in HTML |
| --- | --- | --- |
| `glossary.md#conceit` | 9 | `<dt id="conceit">` - a definition term |
| `#fn1` / `#ref1` | 4 | footnote round-trip, `<sup id="ref1">` and its return link |

Markdown has no `<dt>` and no footnote anchor, so `html2md.py` emits the link and
silently drops the destination. Note what this means for the 2026-08-20 glossary
work: **all 51 term anchors exist in `glossary.html` and none of them survive
into `glossary.md`.** The nine Conceit references repointed that day are correct
on the site and dead in the mirror.

Sources: `assist-rule`, `gear`, `gear-traits`, `nonhuman` (x4), `oddball-rule`,
`traits` for Conceit; `accumulated-progress` and `multiple-actions` for the
footnotes.

Two possible fixes, both for the author to choose between: have `html2md.py` emit
an explicit `<a id="..."></a>` before the term, which GitHub honours, or accept
that mirrors lose sub-heading anchors and have the generator degrade those links
to page-level. `@@*`

---

## The 10 missing images in `L1/*.md`

Every image in every mirror is broken, for one reason - and it is not the one it
first looks like. The HTML does not contain the R2 host at all. It writes
`<img data-src="lilli.png">`, and `config.js` prepends `SiteConfig.CDN_BASE` at
load time (`nav.js` does the same for injected fragments). So `html2md.py` reads
`data-src`, finds a bare filename, and faithfully emits a bare filename - which
resolves to nothing beside the `.md`.

The generator therefore needs to know the CDN base, not merely stop stripping
something. Cleanest is to read it from `config.js` rather than hard-code it, so
the author's stated intent - *"Change CDN_BASE here to update all image
references sitewide"* - keeps holding for the mirrors too. `@@*`

    L1/core-loop.md                waywright_imp_girl_300_DPI_-_no_Background.png
    L1/core-loop.md                corner-dice.jpg
    L1/index.md                    cover-fullBox.png
    L1/mechanics.md                odd_dice-vintage.jpg
    L1/panels/itch.md              cover-fullBox.png
    L1/quickstart.md               the tale.jpg
    L1/quickstart.md               lilli.png
    L1/mechanics.md                odd_dice-vintage.jpg
    L1/resistance-and-opposition.md  Resist-cropped.jpg
    L1/start.md                    reader.png
    L1/start.md                    Sketchy-lil.png

One extra wrinkle: `the tale.jpg` contains a space, which needs `%20` or angle
brackets in Markdown regardless of the host question.

A second, unrelated wrinkle spotted in the same markup: that image carries an
inline `style="width:80%; height:auto; ..."` attribute, on a page in a repo whose
steering file says *"Never add inline styles."* Pre-existing, not touched, and
flagged rather than fixed. It wants a class. `@@*`

---

## `WIP/core-rules-digest.html` - 324 dead links, and a provenance clue

Every internal link in the digest points at a `.md` file that does not exist
beside it: `roles.md`, `maneuvers.md`, `karma.md`, `actions-and-timing.md#free-actions`,
and so on, twenty-one distinct targets across 324 occurrences.

Harmless in itself. The digest is a print artifact, its stylesheet sets
`a{color:inherit;text-decoration:none}`, and nobody clicks a printed page.

**But it tells us where the digest came from.** Those are Markdown link targets
sitting in an HTML file. The digest was assembled from Markdown - either the
mirrors or a source document - and never had its hrefs converted. That is a
useful fact for reconciling it against the site (manifest item E): the digest is
downstream of a Markdown snapshot, and the divergences we find are most likely
author edits made *in the digest* after that snapshot was taken. Worth
confirming before we start ruling on which side is canon. `@@*`

Its 12 broken anchors are the same `.md`-fragment problem and need no separate
treatment.

---

## Out of scope, recorded so it is not lost

**`TS/` - the other game.** 140 files, and it is in noticeably worse repair than
`L1/`: 54 broken nav targets, 43 broken anchors, 55 missing images. The missing
images are the whole card deck (`cards/ah.png` through `cards/kc.png` plus the
two jokers) referenced from `TS/cards.md` and from each individual card mirror.
Same mirror-generator causes, most likely, plus whatever else. Not today's work.
Flagging it because "the site is clean" is only true of `L1/`.

**`Settings/` - 3 broken targets,** all in `Settings/Averond/work_remaining.md`:
`hooks.md`, `../hooks.md`, and a literal `...`. Repo-internal planning notes, not
published. Cosmetic.

**`docs/` - clean.** Zero of everything.

---

## What this changes about the plan

1. **The rename (manifest item A) starts from a clean baseline.** Any anchor or
   nav breakage that appears in `L1/*.html` after it is unambiguously ours.
2. **Nothing needs fixing before the rename.** The site is sound. The mirror
   defects are pre-existing, non-visible, and orthogonal.
3. **All three mirror defects are generator bugs, not content bugs.** They belong
   with manifest item G, and fixing them means one careful pass over
   `html2md.py` followed by a full regeneration - not 28 hand edits. Hand-editing
   the mirrors would be undone by the next regeneration anyway.
4. **The regenerate-and-diff CI gate already logged in `CLAUDE.md` would have
   caught none of this**, because the mirrors regenerate to exactly the wrong
   output they already contain. The gate stops *drift*; it does not stop
   *systematic* generator error. Both are worth having, and they are separate
   jobs. `@@*`

---

## Resolution - 2026-08-24

Six fixes, all in `tools/`. No page content was touched; 80 `.md` mirrors were
regenerated from unchanged HTML.

### 1. Headings vanishing in files with no `<main>` (was G1)

**Cause, and it was not `<section>`.** `html` and `body` were missing from
`BLOCK_TAGS`. Any file without a `<main>` of its own therefore had its entire
document tree rendered as a single *inline* run, swallowing every heading.

**Two files were affected, not one.** `WIP/core-rules-digest.md` recovered **73
headings from zero**, unblocking the digest diff (manifest item E). And
`Settings/Averond/levelone_averond_setting.md` had the same injury - the whole
setting document was one wall of prose, and now carries its real structure.

### 2. Tables (was G2)

Added `render_table`, emitting GFM pipe tables. `assist-rule.md`'s reference
table, previously fused into `ItemTreatment A mundane sworddoesn't need
anything...`, now renders as a real table. Rowspan and colspan have no Markdown
equivalent; a merged cell occupies one column and no text is dropped.

### 3. Images (was G4, first face)

`html2md.py` now reads `CDN_BASE` from the **nearest `config.js` above the
page**, so `data-src="lilli.png"` becomes the full R2 URL. Reading it rather than
hard-coding it keeps the author's stated intent - change `CDN_BASE` once and
every reference follows, mirrors included. It also works per-game without
special-casing, which `TS/` immediately benefited from.

Spaces are percent-encoded, so `the tale.jpg` resolves.

### 4. Cross-page fragments (was G4, second face)

The site sets short, deliberate ids that GitHub cannot reproduce, because GitHub
slugs the heading *text*. The converter now builds an id-to-slug map per target
page and rewrites fragments accordingly:

    actions-and-timing.md#free-action-boosts
      -> actions-and-timing.md#free-action-access-to-pre-existing-boosts

It also reads the `<span class="section-anchor">` markers that
`anchor_sections.py` inserts, resolving them to the heading that follows. A
fragment that genuinely cannot exist in Markdown is **dropped**, so the link
still lands on the correct page instead of dying in place.

### 5. Glossary anchors (was G4, third face)

A `<dt>` carrying an id now becomes a heading rather than a bold paragraph, so
GitHub auto-anchors it.

**Verified before implementing:** all 51 glossary ids already equal the GitHub
slug of their own term text, exactly, with zero mismatches. So the nine
`glossary.md#conceit` links resolve with **no link rewriting at all** - the
anchors simply exist now.

*Open cosmetic question for the author:* terms render as `## **Adept**`, keeping
the `<strong>` from the source inside a heading that is already bold. Faithful,
slightly redundant. Say the word and the emphasis is stripped inside headings.

### 6. Footnotes - now native GFM

The site's hand-built footnotes translate to real Markdown footnote syntax:
`<sup><a href="#fn1" id="ref1">1</a></sup>` becomes `[^1]`, and the definition
list becomes `[^1]: ...`. GitHub then supplies the numbered marker, the collected
notes section, and the return link by itself.

**One deliberate omission, flagged for the record:** the `<h4>Notes</h4>` heading
inside `<section class="footnotes">` is dropped, because GFM emits its own
heading and relocates every definition to the foot of the document - keeping it
would strand a heading over nothing. This is the only place the converter drops a
heading, and it does so because the target format supplies the equivalent.

### Also fixed in passing

Image constructs are no longer split by the hard-wrapper. `![A sketchy little\nfigure](...)`
still rendered, but the broken alt text defeated line-oriented tooling - including
this audit's own script. Ordinary links are still allowed to wrap, because the
hand-wrapped pages break inside link text and that is the house style.

### What remains, and why

`WIP/core-rules-digest.html` still shows **324 broken targets and 12 broken
anchors**, and they are now the only findings left in the repo apart from three
stale references in `Settings/Averond/work_remaining.md`.

These are the digest's `.md` link targets - `roles.md`, `karma.md` - which do not
exist beside it in `WIP/`. Harmless: it is a print artifact whose stylesheet sets
`a{color:inherit;text-decoration:none}`, and nobody clicks a printed page. Left
alone deliberately rather than missed. `@@*`

---

## Reproducing this

The audit script lives outside the repo for now, at the session scratch path. If
it earns a permanent home it belongs in `tools/`, where it can grow a `--check`
mode and join the CI gate. Say the word and I will install it. `@@*`
