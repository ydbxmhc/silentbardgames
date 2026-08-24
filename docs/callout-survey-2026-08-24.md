# Callout survey - 2026-08-24

Read-only survey taken to inform manifest item I, the standard for named
callouts. Counts are for `L1/` and its subfolders. Nothing was changed.

---

## What exists

**Corrected 2026-08-24.** An earlier count in this file said "96 callouts, 78
untitled." That was wrong: it counted `class="box"` and `class="box-title"` as
separate items, when a titled callout contains both. Parsing the actual `<div>`
elements gives:

    83 callouts total
       13  titled     (carry a <span class="box-title">)
       70  untitled

    by area:                    titled   untitled   total
      L1/ (top level)                8          6      14
      L1/action/                     3         64      67
      L1/magick/                     2          0       2

    modifiers in use:  .box (plain), .box.example (3), .box.highlight (2)
    related:           .example-play (5 uses), dialogue-style in-play example

**Defined in CSS but never used anywhere:** `.box.gm-note`, `.box.warning`,
`.box.rule`. Three variants carrying styling nobody invokes. `gm-note` and
`example` are defined in *both* `onesrd.css` and `L1/style.css`; `warning` and
`highlight` only in the theme file; `rule` only in the structural file. Worth a
tidy pass, separately from item I. `@@*`

## The 70 untitled callouts are not miscellaneous

**64 of the 70 are in `L1/action/` - 91%.** The author's hypothesis, tested
2026-08-24 and confirmed: these are a distinct category the taxonomy is missing,
where mechanics are detailed *after* the relevant story text in the *In Action*
vignettes.

They are not asides. On an *In Action* page they are roughly half the content and
the entire pedagogical point: narrative beat, then the numbers that produced it.
Calling them `.box` files them alongside decorative sidebars, which is why they
have no name, no styling of their own, and no way to be treated as a group.

Sampling `athlete`, `sneak` and `spellweaver` shows the category is itself not
monolithic. At least four things wear the same markup: `@@*`

| Kind | Example, abbreviated |
| --- | --- |
| **Character stat block** - opens the vignette | *"Level 3, SpellWeaver 3, Fax Iacta 1, Stone Shape 1, Mage Light 1"* |
| **Opposition stat block** - the obstacle's sheet | *"The Thornwall crossing is a Level 3 difficulty challenge. The mountain's 'Roles' are Hostile Terrain 3 and Winter Conditions 2..."* |
| **Resolution commentary** - the dice math, inline | *"With Level 3 + Athlete 3 + Competition Strategy 3 = EL9 she wagers 3 and rolls EL6 for a 1..."* |
| **Editorial aside** - the author to the reader | *"This is a Sneak example, not Healer, so we summarize..."* |

The last of those is not mechanics at all. It is a note about the *example's*
scope, and it probably belongs to a different tier entirely.

Distribution is uneven and may itself be worth a look: `athlete.html` carries 15
boxes, `warrior` and `healer` 9 each, while `conjuror.html` has none at all.

**The remaining 6 untitled callouts**, all outside `action/`, are genuinely
miscellaneous: two in `nonhuman-as-a-hook` giving GM advice on bloodline
bonuses, and four in `quick-reference` restating core rules and key definitions.
Small enough to rule on individually.

---

## The shape of the problem, in one observation

**Of 83 callouts, only 13 are titled. None of the 13 has an `id`.**

`.box-title` is a `<span>`, styled at `0.72rem`, uppercase, letter-spaced - a
*label*, deliberately smaller than body text. It is not a heading and does not
pretend to be one. Which means:

- `anchor_sections.py` cannot see it. That tool matches `<h2>` through `<h4>`.
- The TOC generator cannot see it, for the same reason.
- Nothing can link to it, because there is no anchor to link to.

So a named callout is currently a dead end: a reader can find it by scrolling
past it, and by no other means.

---

## The 13 titled callouts, classified

Reading them together, they are not one kind of thing. They are three. `@@*`

### Named concepts - want an anchor and a TOC entry (6)

| Page | Title |
| --- | --- |
| `chargen.html` | The Power of Good Representation |
| `crafting-good-hooks.html` | Don't be a Pain! |
| `nonhuman.html` | Hodges' Rule of Thumb |
| `the-nature-of-roles.html` | Class-ic Tropes? |
| `tricks.html` | A Trick Is Not a New Power |
| `magick/shaping-effects.html` | The Shared Shape |

These are the species the Recovery Trope belongs to. Each names an idea a reader
will want to cite, return to, or send someone a link to. *Hodges' Rule of Thumb*
is the clearest case - it is a **named rule**, and it is currently unlinkable.

### Worked examples - a genus of their own (3)

| Page | Title |
| --- | --- |
| `kamikaze-blitz.html` | Worked Example - Ai-uchi at the Daimyo's Door |
| `resolving-combat.html` | Worked Example - One Engaged Foe |
| `quick-reference.html` | Without Food & Shelter |

Two already share an explicit "Worked Example -" prefix, which is a convention
trying to happen. These probably want to be findable, but as a *class* ("show me
the worked examples") more than as individual named ideas. That is a different
TOC treatment from the group above, and possibly a different visual one.

### Not names at all (4)

| Page | Title |
| --- | --- |
| `action/healer.html` | Extreme Recovery Failure! |
| `action/healer.html` | A Changed Man |
| `action/warrior.html` | "Brother Thomas" is a retired cavalry sergeant, now a friar in his old age. |
| `magick/adepts.html` | Example |

Narrative beats inside the *In Action* vignettes, plus one generic label. The
Brother Thomas one is a full sentence used as a title, which is a hint that
`.box-title` is currently doing at least two unrelated jobs: naming a thing, and
captioning a thing. These want no anchor and no TOC presence.

---

## What this suggests for the standard

Not a decision - the author's. Laying out what the data implies. `@@*`

1. **At least four tiers, not two.** Plain aside, worked example, named concept,
   and - by far the largest - **mechanical annotation** on the *In Action* pages.
   The existing markup collapses all of them into `.box` plus an optional label.
   The mechanical tier is 64 of 83 callouts and has no name at all.

   A consequence worth stating plainly: the mechanical tier should almost
   certainly **not** get TOC entries. Sixty-four would drown the table of
   contents, and nobody wants to navigate to "the fourth dice roll in the
   Athlete vignette." It wants a *name and a class*, so it can be styled and
   handled as a group. That is a different requirement from the named-concept
   tier, which wants exactly the opposite. `@@*`

   One idea, flagged as entirely Claude's and unratified: because the mechanical
   tier is separable from the narrative around it, it could be **toggleable** -
   a reader following the story reads the story, a reader studying the system
   turns the numbers on. `L1Prefs` and `settings.html` already exist to carry
   exactly that kind of preference. Cheap to build once the class exists,
   impossible before. Raise it or discard it as you see fit. `@@*`
2. **The named tier needs a real heading**, not a `<span>`. That is what makes it
   visible to `anchor_sections.py`, to the TOC generator, and to a screen reader
   moving by heading. It is also the honest markup: a named callout *is* a
   subsection that happens to be boxed.
3. **Which raises the visual question.** `.box-title` is currently smaller than
   body text. A named callout promoted to `<h3>` or `<h4>` would inherit heading
   size unless the class overrides it. The author may want it to keep looking
   like a label while behaving like a heading - entirely doable, but it is a
   deliberate choice rather than a default.
4. **The outline question.** If a named callout carries an `<h3>`, it lands in
   the page's heading outline between its neighbours. That may be exactly right,
   or it may clutter a page that uses `<h3>` for real subsections. An `<h4>`
   reserved for callouts, or an explicit `class="box-title"` on a heading
   element, sidesteps it.
5. **Retrofit cost is small.** Six callouts in the named tier, three in the
   worked-example tier. Whatever is decided, applying it to what already exists
   is an afternoon, not a project.
6. **The digest needs a matching decision.** `WIP/core-rules-digest.html` styles
   `blockquote` for this role and has no named variant at all. Whatever standard
   lands has to survive into print, or the two copies diverge in a *third* way on
   top of the text drift already logged as manifest item E.

---

## Adjacent findings, not part of item I

- **`.example-play` and `.box.example` overlap.** Five uses of the first, three
  of the second, both meaning roughly "an example." They are styled differently
  and used inconsistently. Worth deciding whether they are one thing or two.
- **Three dead CSS variants** as noted above.
- **`.quiet` is used 498 times**, by a wide margin the most common class in the
  book. Noted only because it makes any future audit of class usage read oddly;
  no action implied.
