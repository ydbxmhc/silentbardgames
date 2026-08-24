# Callout taxonomy - draft for the author to shoot at

**Status: entirely proposal.** `@@*` applies to this whole document. Nothing here
is settled, class names are deliberately left as placeholders, and the count of
types is almost certainly one or two too many on purpose - it is easier to merge
tiers than to discover a missing one after sweeping 83 callouts.

Companion: `docs/callout-survey-2026-08-24.md` for the data this rests on.

---

## The central proposal: two axes, not one list

Everything currently lives on one axis - "is it a `.box`?" - which is why one
class is doing seven jobs. The fix is to split what a callout **is** from what a
callout **does**.

**Axis 1: type.** What it looks like, where it sits, how a reader meets it.
**Axis 2: role.** Whether skipping it costs the reader a rule.

Type is visual and structural. Role is editorial. They are independent, and
conflating them is exactly the trap. This also answers the toggle problem
directly - see the bottom of this file.

---

## Axis 1 - the proposed types

### 1. Footnote

**Already exists and already works.** `<sup><a href="#fn1" id="ref1">1</a></sup>`
in the text, `<section class="footnotes">` at the page foot with an `<h4>Notes</h4>`,
an `<ol>`, and a return arrow on each item. Used on `accumulated-progress.html`
and `multiple-actions.html`.

Nothing to design. It needs **documenting** as the house convention, and it needs
the `html2md` fix so `#fn1` survives into the mirrors (audit item G4).

One small question: that `<h4>Notes</h4>` is a real heading, so it enters the page
outline and the digest's heading list. Intended, or should it be a styled label?

### 2. Aside

Brief, in-flow, unnamed. A parenthetical the author wants set apart but not
elevated. No title, no anchor, no TOC presence.

This is what most of the current plain `.box` uses outside `action/` actually are.

### 3. Sidebar

Parallel enrichment. Longer than an aside, usually titled, and **skippable
without losing a rule** - colour, history, design commentary, "why we did it this
way." Some will want anchors so they can be linked; none need TOC entries by
default.

### 4. Callout

The named tier. A titled, addressable, **load-bearing** block carrying an idea the
reader will cite and return to. Real heading element, an `id`, and a TOC entry.

Six exist: *The Power of Good Representation*, *Don't be a Pain!*, *Hodges' Rule
of Thumb*, *Class-ic Tropes?*, *A Trick Is Not a New Power*, *The Shared Shape*.
The Recovery Trope will be the seventh.

*Hodges' Rule of Thumb* is the case that proves the tier: a **named rule**, in a
rulebook, that nothing can currently link to.

### 5. Worked example

Setup, then resolution, in numbers. Two of the three existing ones already carry
an explicit *"Worked Example -"* prefix, which is a convention that started
without anyone declaring it.

Readers want these findable **as a class** ("show me the worked examples") more
than individually. That suggests a collected index somewhere rather than
scattered TOC entries.

### 6. In-play dialogue

The GM-and-player voice. `.example-play` today, five uses, plus the entire spine
of the Kessa page on `starting-out.html`. Distinct from a worked example: it
teaches through conversation rather than arithmetic.

**Possible merge:** this and *worked example* could be one type with two
presentation modes. They share a purpose and differ in voice.

### 7. Mechanical annotation

The *In Action* tier. 64 of 83 callouts. Narrative beat, then the numbers that
produced it, alternating down the page.

Needs a name and a class so it can be styled and handled as a group. **Should not
get TOC entries** - sixty-four would drown the table, and nobody navigates to
"the fourth dice roll in the Athlete vignette."

The survey found it subdivides further: character stat block, opposition stat
block, resolution commentary, and editorial aside. Whether those are four
variants of one type or evidence of a missing distinction is an author call. The
editorial one (*"This is a Sneak example, not Healer, so we summarize"*) is not
mechanics at all and probably belongs in type 2.

---

## Where I would merge, if seven is too many

- **Aside and sidebar** may be one type with a size or placement variant. The
  honest difference between them is length and whether it has a title.
- **Worked example and in-play dialogue** may be one *example* type with two
  voices.

That would take seven to five: footnote, aside/sidebar, callout, example,
mechanical annotation. Five feels closer to a book's real vocabulary. The author
should cut, not Claude.

---

## Axis 2 - role, and why the toggle needs it

The author's objection to the toggle was exactly right: once one tier is
hideable, you need somewhere to put the things you *never* want hidden. But that
is not a reason for another type. It is the reason role has to be its own axis.

**Load-bearing** - skipping it costs the reader a rule. Never hidden.
**Enrichment** - skipping it costs the reader depth, not rules. Safe to hide.

That property does not follow from the type. The same mechanical annotation is
*enrichment* on an *In Action* page, where the rule it demonstrates is stated
properly elsewhere, and *load-bearing* in `quick-reference.html`, where the box
is the only statement of the rule. One type, two roles, two behaviours.

So: mark role explicitly on each callout, and let the toggle key off **role**
rather than type. Nothing gets hidden because of what it looks like; things get
hidden because they were declared skippable.

### And the toggle should not ship yet

The author's own diagnosis is the reason. The *In Action* stories exist mostly to
carry the callouts, several need extensive rewrites, and their real purpose is
exposition rather than fiction.

A reading toggle only pays off where **both layers stand alone** - where the
story is worth reading without the math, and the math is followable without the
story. On most *In Action* pages today, neither is true. Hiding the mechanics
would leave a thin story; hiding the story would leave orphaned arithmetic.

Which makes the toggle **downstream of the rewrite**, not part of this refactor.
Build the class now, because it costs nothing extra and the rewrite will want it.
Build the toggle after the pages can carry it. Logged as manifest item J.

---

## Open questions for the author

1. Seven types, or five? Which merges do you accept?
2. Names. All of them. The book's vocabulary is yours; anything Claude proposes
   will read like a stylesheet.
3. Does the callout tier take `<h3>` or `<h4>`, and does it keep the current
   small-label look while behaving like a heading?
4. Do worked examples get a collected index page, or is being styled as a class
   enough?
5. Does *role* get marked in markup (a class, a `data-` attribute), or is it a
   documented editorial judgment that only the toggle would ever need to read?
6. How does each type print in the half-letter digest? It currently styles
   `blockquote` for all of this and has no variants at all.
