# Callout survey - 2026-08-24

Read-only survey taken to inform manifest item I, the standard for named
callouts. Counts are for `L1/` and its subfolders. Nothing was changed.

---

## What exists

    .box              96 uses      the general callout container
      of which:
        .box               78      plain, no modifier
        .box.example        3
        .box.highlight      2
        (13 carry a .box-title, distributed across the above)

    .example-play      5 uses      dialogue-style in-play example
    .box-title        13 uses      the label inside a box

**Defined in CSS but never used anywhere:** `.box.gm-note`, `.box.warning`,
`.box.rule`. Three variants carrying styling nobody invokes. `gm-note` and
`example` are defined in *both* `onesrd.css` and `L1/style.css`; `warning` and
`highlight` only in the theme file; `rule` only in the structural file. Worth a
tidy pass, separately from item I. `@@*`

## The shape of the problem, in one observation

**Of 96 callouts, only 13 are titled. None of the 13 has an `id`.**

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

1. **Three tiers, not two.** Plain aside, worked example, named concept. The
   existing markup collapses all three into `.box` plus an optional label.
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
