# L1 System Digest - Core Mechanics Reference

*Working reference for cross-system conversion work on The Conjuror's Manifest.*

**Status:** paraphrase, not canon. The `.md` files in `SilentBardGames/L1/` are the source of truth; this digest exists so a fresh session can load L1's grain in one file instead of thirty. Where this document and the repo disagree, **the repo wins.** Items marked `@@` are open questions for the author.

**Built from:** `mechanics.md`, `dice.md`, `resistance-and-opposition.md`, `resistance.md`, `actions-and-timing.md`, `multiple-actions.md`, `wagered-actions.md`, `resolving-combat.md`, `roles.md`, `the-nature-of-roles.md`, `mechanical-function.md`, `maneuvers.md`, `harm.md`, `types-of-harm.md`, `feeling-down.md`, `hooks.md`, `hooks-how-they-work.md`, `threats.md`, `quick-reference.md`, and `Demicon/20260501_REFERENCE_Quick_Reference.html`.

---

## 0. The One Thing That Breaks Outside Intuition

**You roll UNDER your own Effective Level, not over a target number.**

> Success is a result **greater than 0 and not greater than your EL.**

Roll as high as you can *without exceeding your own competence*. Rolling over your EL is not a partial success or a near miss - it is total failure, zero effect, regardless of opposition.

Every other system in the Manifest rolls high against a target. Anyone arriving from 5e, Fate, Cortex, Shadowdark, Daggerheart, or Boundless will import the wrong instinct and calibrate everything wrong. **Read this section twice before writing a conversion.**

Consequences worth internalizing:

- Competence is a *ceiling*, not a floor. Growth widens the band you can safely roll in.
- There is no "critical hit" in the usual sense - the best possible roll is exactly your EL.
- Overreach is a real, mechanical risk that scales with ambition (see Extra Effort).
- A high-EL character is not just more likely to succeed; they have more *room*.

---

## 1. Effective Level

> **EL = Level + Role + Maneuvers + Modifiers**

Your result minus opposition or resistance is your **Effect** - what actually happens.

**Caps and gates:**

| Rule | Effect |
|---|---|
| No relevant Role | Roll at Base EL = **Level only** |
| Role rank | Cannot exceed your Level |
| Maneuver rank | Cannot exceed its parent Role rank |
| **Training gate** | If a task *cannot be done without training*, you may only add as much **base Level** as your rank in the relevant Role - your best, if you have more than one |
| Dedicated (wagered) effect | Can never dedicate more points than your rank in the relevant Role |
| Below EL 1 | Task is impossible |

**The training gate is the single most important rule for creature design.** It is what makes an authored seam possible: a Level 6 entity with a Role at rank 2 brings almost nothing to a contest that Role gates. See §10.

Ties favor the defender.

---

## 2. Dice

Any dice with an even split of odd and even faces. Three supported modes:

**Simple Pool.** Roll dice equal to your EL, count the odds. EL 8 = eight dice, five odd = result 5. Cannot exceed EL, so it is "safe" but rarely optimal.

**Extra Effort.** Add dice beyond your EL. More dice pull the result toward the middle, improving the odds of a solid mid-range outcome - but now you *can* exceed your EL and fail completely. Player-controlled risk/reward. Also forfeits critical successes (see `extreme-results.md`, not yet digested).

**AnyDice (zero-base).** Notation: `3d[0-7]` is three zero-based eight-sided dice. On standard dice, read the top face as zero. Choose any combination whose range and curve you like. `4d[0-5]` (range 0-20, avg 10) is comparatively safe; `3d[0-7]` (range 0-21) is swingier.

The system also runs **without dice** - compare ELs directly and play it as pure tactics.

---

## 2a. Extreme Results (optional rule)

Requires **at least three dice**. Works with Simple Pool.

**Extreme Failure** - every die rolls zero. Not merely a failure: the turn is **over**, any other actions in progress are **aborted**, and there is an immediate bad consequence scaling with the number of dice (drop a weapon at three; break it higher up; at the extreme, *no passive resistance rolls for the turn*). **A Luck Token cannot save it.** Karma can, but only downgrades it to a simple fail.

**Extreme Success** - every die shows its individual maximum **and** the total is *exactly* your EL. Best possible result plus a beneficial side effect scaling with dice count (disarm at three; assign results as a post-roll split higher up; at the extreme, *the target gets no opposition or resistance at all*). Awards a **free Luck Token** if there's room; if an opponent spends a Luck Token to resist it, immediate **Karma**.

**The inverse scaling is deliberate.** More competent characters get *fewer* extremes of either kind. Extremes are accidents of chance, not skill. Optimal play actually *forgoes* extreme successes by shaping non-matching pools with Extra Effort - which forfeits the upside while **keeping the extreme-fail exposure** on zero-based dice.

### Why this matters for creature design

In Simple Pool, "all dice at maximum" and "total exactly EL" are the *same event*, so both extremes sit at **1 / 2^EL**:

| EL | Chance of either extreme |
|---|---|
| 3 | 1 in 8 |
| 6 | 1 in 64 |
| 12 | 1 in 4,096 |
| 24 | 1 in 16,777,216 |

> **This sharpens every authored seam, and it isn't written down anywhere.** Forcing a powerful creature onto its weak Role does not merely shrink its numbers - it drags it back into the range where **catastrophe is possible again.**
>
> Malisondre at 24 dice cannot fumble; the odds are one in seventeen million. Drag her onto air and she rolls **6**, where extreme failure is **1 in 64** - and extreme failure means her turn ends and anything in progress aborts, mid-manifestation. The seam is not just "her pool collapses." It is "her pool collapses *and she can now trip over her own feet.*"

> **Malisondre would never roll for miracles, and that's characterization from mechanics.** A thousand-year tactician shapes non-matching pools for reliable mid-range results, deliberately forfeiting extreme successes. That is precisely the *"win slowly"* craft note, now with teeth. **The PCs get the windfalls; the ancient broker grinds.** Exactly the right distribution of lightning.

> **And the weakest thing in the book is the most spectacular.** The Hanged Man is Level 1 + Spectre 1 + Display 1 = **EL 3**, sitting exactly on the three-dice threshold. He rolls an extreme **one time in eight** - and he's *Blanket*, so it lands on everyone present at once. "Level measures force, never threat" has rarely been better illustrated. Worth a line in his entry.

**No token loop - an extreme must be *naturally rolled*** (author). Paying a token isn't rolling a value, it's buying one. And this is the same reason Extra Effort disqualifies extreme successes: with more dice than EL you cannot naturally have every die at maximum *and* total your EL. One principle covers both cases:

> **An extreme is a property of the natural roll.** Bought results and padded pools are disqualified by definition.

`@@ Add that word to the page.` The text never says "naturally," and it's the word carrying the whole rule.

## 2b. Luck Tokens - correct rules

*From `luck.md`. Supersedes the summary in §9 below where they differ.*

**Characters:** begin each session with Tokens equal to base Level. Gain one at the start of every scene **if they have room**; never more than Level. GM may award more for good play.

**NPCs never hold Tokens individually.** The **GM** holds a pool and spends it on behalf of the opposition on any test.

> **GM pool** = the number of players, *or* the highest PC Level, whichever is greater - **and one per scene** thereafter.

So Malisondre does **not** have six tokens. The GM's pool covers her, and it covers everything else in the scene too. Her entry should say nothing about tokens; it isn't a creature stat.

**Spending a Token:** best possible result (usable *after* seeing the opposition's roll, before resolution is decided; may deliberately choose less) · **Plot Armor** · absorb and negate a point of Harm · power a Maneuver that requires one · power a potent spell.

> **And the one that matters most for every Court booklet:**
> *"They also make great bargaining chips for deals with spirits… 'Grant me the breath of thy life for a minute's span…' More powerful spirits will want actual Karma; weak ones will be happy with booze, or incense."*
>
> **There is a currency ladder for spirit negotiation already in the rules:** trinkets and incense → Luck Tokens → **Karma**.
>
> - **Agnes** is a weak spirit who wants pretty things. Her entire existence is a bargaining position, and she is cheap. That is *why* she can be turned from curse to companion.
> - **Malisondre** is powerful, so her price is **actual Karma** - the players' advancement currency. Dealing with her costs them progress they have earned. Expensive, legible, and it makes every negotiation a genuine sacrifice.
>
> This belongs in every Court booklet and is currently in none of them.

`@@ DISCREPANCY - your rule vs. the page.` You described the GM pool as *"the number of players, OR the highest level, whichever is more, **plus one**"* - four Level 1s giving 5, two Level 5s giving 6. **`luck.md` has no "+1"**; it reads 4 and 5 respectively. One of them needs correcting, and I don't know which is the intent.

`@@ Your worry was unfounded:` `luck.md` **does** already say the GM "also gets one Token per scene."

**The spending lists are illustrative examples, not exhaustive menus** (author). Divergence between pages is therefore expected and fine - both carry the two that matter (best possible result, Plot Armor). Do not treat the difference as errata.

**One genuine fabrication, now removed.** `quick-reference` carried a *"Wager Auto-Succeed - spend a Token to automatically succeed on a Persistent Wager roll, the wagered dice become a full scene Boost without rolling."* No such rule exists in `luck.md` or `wagered-actions.md`; it appears to have been introduced by a bad summarization. **Deleted from `L1/quick-reference.md` and `L1/quick-reference.html` on author instruction; committed.**

`@@ STILL PRESENT ELSEWHERE:` the same fabricated entry is in **`Lili's Bottle/Demicon/20260501_REFERENCE_Quick_Reference.html`** - the folded Demicon 2026 player handout. Untouched, since that's a separate printed artifact and may already be in people's hands. Your call.

`@@ Minor wording difference, probably harmless:` `luck.md` grants a scene Token "if they have room," `quick-reference` says "if you spent one last scene." Functionally close, not identical.

---

## 3. Opposition vs Resistance

The distinction that runs the whole action economy.

**Resistance** is passive. **Free action** - does not consume a turn, so it can be used repeatedly. It reduces incoming effect but generates **no effect back**. Excess is lost. Locks, walls, poison, gritting your teeth through a punch.

**Opposition** is a contest. Both sides roll, higher wins, the *difference* is the winner's effect. **Costs a turn** - which is exactly why the goblin can hurt you "on your turn."

> Any defense that cannot hurt your attacker back is **resistance**, not opposition.

Opposition is the default framing, and initiative is typically irrelevant - everyone acts and rolls simultaneously. Opposition is really just a compression of act-then-resist, act-then-resist into one exchange.

`@@ Open rules item already logged in SilentBardGames: the resist-or-oppose choice applies to *any* imposed effect, not just blows. Players don't realize they may oppose a dazzle or a Boost. Flagged in that repo's CLAUDE.md as needing one clarifying line on the Resistance page.`

---

## 4. The Two-Axis Combat Model

Each exchange, EL is a budget divided along two axes:

- **Offense** - allocated *per target*. An attack aims at someone specific.
- **Defense** - **one pool, reusable for the whole exchange**, rolled fresh against every point of effect that reaches you.

That asymmetry is the tactical heart of the system.

**Two layers a careful foe imposes.** Against someone who both swings and guards, you must clear both:

1. **The contest** - your offense vs. their offense; higher roll wins, difference is effect.
2. **The defense** - whatever leaks through then meets their separately allocated defense pool, rolled fresh.

**Why a little defense is an enormous bargain.** One defense allocation turns aside the whole room, repeatedly, as a free action. The swashbuckler against twenty henchmen is mechanically correct, not a genre concession.

**Why offense also protects you.** Points aimed at a foe force *them* to hold defense back or eat the effect. A creature with strong offense and no defensive skill is still well-guarded whenever it can **oppose** - its attack's margin keeps it safe. *It is only fragile against attacks it cannot answer.*

**The all-out attacker is the easiest target on the field.** Any foe you did not engage, against whom you allocated no defense, hits you with **no roll to stop it at all** - only Armor, Plot Armor, or a Luck Token saves you.

> *This paragraph is the single most useful thing in L1 for designing creatures. A creature's true vulnerability is not low defense - it is any attack it cannot oppose.*

---

## 5. Splitting

Divide EL among multiple actions; each portion becomes that action's EL. EL 8 against two goblins = two rolls at EL 4.

Points allocated **exclusively to defense** remain usable as a free action, repeatedly.

**Cross-Role splits use a non-obvious rule.** Calculate the EL for each Role. Assign points starting with the **lowest** EL, then **reduce ALL your ELs by that amount.** Repeat with the next lowest remaining.

*Worked example from `multiple-actions.md`:* Performer EL 10, Warrior EL 20. Assign 8 to rally the gang (Performer) - both ELs drop by 8, leaving Performer 2, Warrior 12. Assign 6 from Warrior to attack - both drop by 6; Performer is eliminated, Warrior becomes 6. Remaining 6 Warrior points go to active defense.

The effect: **your Roles share one budget.** Spending from any Role drains all of them. Total assignable is bounded by your highest EL, not their sum. This is why a broad character is not simply an additive character.

**Barrage caveat.** Multiple attacks on the same target with the same ability gain little numerically. The advantage of splitting is tactical flexibility, not raw output.

---

## 6. Wagering

Remove wagered points from EL *before* rolling. If the action succeeds and generates any effect after opposition, add the dedicated points to the result. **Wagered points count only if the roll succeeds without them.** Applied after opposition.

Four uses:

**Dedicated Effect** (the called-shot rule). Specify what the points do - Injury instead of Complication, a named result, a narrative consequence. Capped at your rank in the relevant Role. Side effects require their own separate allocation.

**Persistent Boost.** Wager points, succeed with the rest, get a named bonus addable to relevant ELs for the rest of the scene.

**Residual condition.** Set someone on fire and the fire rolls on its own each round while they fight to put it out.

**Contingent split.** Action B only happens if A succeeds; otherwise those points are wasted.

*Worked example:* Warrior EL 10 wagers 3 as dedicated Harm, rolls the remaining 7, gets a 5. Target defends with 4, leaving 1 point of effect - the 3 wagered points all count, total 4. But if the target's armor boosts resistance by 1, that cancels the single unmodified point, and **all 3 wagered points are wasted.**

---

## 7. Harm

There are no hit points. Harm is a direct modifier reducing EL.

| Type | Recovery | Counts toward Down? |
|---|---|---|
| **Hindrance** | Never by rolls - only narrative action | **No** - situational, not damage |
| **Complication** | Disappears on *any* successful recovery roll | Yes |
| **Injury** | Daily recovery rolls, heals slowly | Yes |
| **Temporary Hook** | Until resolved in fiction | Behaves as a Hook, grants no Karma |

**Harm does not mean damage.** It is anything impeding a character or removing their **agency**. Lost nerve, ruined reputation, a convincing illusion, a successful intimidation - all legitimate Harm. If the character doesn't care about a given axis, apply one they do.

**Down:** when Injury + Complications *exceeds* base Level. Only passive resistance (and any Free Actions the GM allows). Down does not necessarily mean unconscious - it may mean charmed, fleeing, or otherwise stripped of agency. Recover by dropping total Harm back below Level.

**Staggered** (optional, less lethal): keep acting while you have positive EL in *any* Role. Fail to produce positive effect two turns running and resist against current Harm to stay conscious.

**Recovery:** post-conflict roll (free, sorts Complication from Injury), armor second roll (converts remaining Injury to Complications), daily roll (reduces Injury). No food or shelter means no recovery rolls at all, plus daily privation resistance.

---

## 8. Hooks

Motivations, drives, fears, complications. Three functions: drive the story, provide mechanical bonus, generate Karma.

- **Once per scene**, add the Hook's current rank to any relevant roll. The GM may also apply it free when it obviously fits.
- Complicating your life earns **Karma** (once per session); further triggers that session yield a **Luck Token**.
- Rank up after the session; **max rank = Level.**
- **Imposed Hooks** can be the result of losing a resistance roll - Harm as forced behavior.
- Hooks degrade when resisted (roughly one rank per session if unfed) and may be renamed as they fade.

`@@ Logged as an open item in SilentBardGames: the site only states the character-side half. The reciprocal - an opponent or the GM may apply your Hook's rank against you, or to the situation's DL - is implied but never stated as a mechanic. Relevant to every creature in the Manifest that works through a victim's own attachments (Agnes above all).`

---

## 9. Luck Tokens

1 per Level at start; +1 per scene if you spent one last scene. One Karma Token acts as an emergency supertoken.

Spend to: take the **best possible roll** (even after seeing opposition); **Plot Armor** (gear absorbs all damage from one hit, gear rating reduced by that amount); **Story Point** (declare a plausible fact, negotiated); **Wager Auto-Succeed**.

---

## 10. Worked Arithmetic - Malisondre

The apex creature in The Dead, used here as the reference calculation for the whole Manifest.

**Sheet:** Level 6 · Shade 6 (Display 6, Manifestation 6) · Succubus 5 (Possession 5, Aura Reading 5) · Performer 6 · Loremaster 5 · Sylph 2 (Manifestation 2)

**Manifest pool = 24.**

```
Level          6
Shade          6
Display        6
Manifestation  6
              ──
              24   before Boosts or Hooks
```

Split across the two axes per §4 - Manifestation as the reusable defensive soak, Display as per-target offense. Allocated, never spent whole.

**The seam = 6.** Force a contest only a Sylph can answer:

```
Level (capped at Sylph rank)   2
Sylph                          2
Manifestation (Sylph)          2
                              ──
                               6
```

The training gate does the work twice: it caps her Maneuver at Role rank, *and* it caps how many Level dice she may add to Sylph-specific actions. Twenty-four collapses to six. She never invested further in Sylph because she has the same capability elsewhere, better - which is exactly why the seam exists and why it is *authored* rather than a designer oversight.

**Generalized:** any creature's seam is `2 × (low Role rank) + (its Maneuver, if any)`. To find a creature's soft spot, look for the lowest-ranked Role on its sheet and ask what contest only that Role can answer.

---

## 11. Tier Calibration Ladder

For comparing across systems, anchor to the published examples in `threats.md`:

| Level | Example | Shape |
|---|---|---|
| 1 | Lone adolescent wolf; Hanged Man Spectre | Trivial / single-trick |
| 2 | Lone adult wolf; **Agnes** | Competent, narrow |
| 3 | Lone alpha wolf | Genuinely dangerous solo |
| 4 | Wolf hunting pack; **Vane** | Group-as-single-opponent, or a real threat |
| 6 | **Malisondre** | Apex; a situation rather than an encounter |

Remember the governing principle: **Level measures force, never threat.** Agnes at Level 2 compounds into something terrifying through patience and Hook manipulation. Compare *tiers and shapes* across systems, never raw numbers.

---

## 12. The Accords

Binding on all spirits and Halflings - directly load-bearing for every Court booklet.

- An established Agreement precludes the Participants directly harming each other.
- A Debt or Contract Accepted constitutes an established Agreement.
- A favor Accepted implies a Debt Accepted unless explicitly excluded.
- Payment Accepted precludes future litigation or revenge.
- Proper Payment Refused implies a Continuance of the Agreement.
- Improper Payment offered may be freely Refused without Consequence.
- An Agreement Concluded is wiped clean.
- Breaking these Accords by one Participant Absolves the other from all Obligation.
- No further Agreements may be made by the Participants until Restitution is made.
- A substitute Agreement May be Accepted as Restitution.
- Spirits and Agreements are likewise Bound to the Form they Assume.

A Contract established by Compulsion weakens these. Faeries cannot lie; ghosts cannot cross an unbroken circle of salt; anyone may bargain on behalf of another's debt if willing to pay the price themselves.

---

## 13. Traits

**Traits** are special properties on gear, spells, and creatures. **Conceits** are *unrated* Traits - narrative truths with no number attached (*Immune To Fire* rather than *Resistant +3*).

Compatible Traits stack. Most Traits need no writeup at all - *Stationary* means what it says. The catalogue exists for the ones worth a repeatable label, so a GM can write one word on an index card and the table knows what it's facing.

Note also: creatures routinely take a "Role" that is simply what they are - *Bear*, *Sylph*, *Spectre* - and then take Maneuvers under it. Much of what other systems handle with special abilities, L1 handles this way rather than with Traits.

**Behavioral:** *Reactive* (acts only when triggered) · *Ablative* (degrades with use rather than discrete charges)

**Combat:** *Inexorable* (allows **no** resistance roll - very dangerous, should be rare and thematically bounded) · *Insidious* (cannot be **opposed**, only resisted - bypasses active defense) · *Subtle* (effect not obvious to those who can't perceive the Borderlands) · *Contagious* (spawns a copy on any successful victim) · *Constrained* (limited to specific die types - the ogre who rolls nothing but a d12)

**Area Effect:** *Targetable* (default - split EL among targets) · *Blanket* (one roll applies equally to everyone; no splitting) · *Selective* (affects only targets meeting stated criteria)

**Defense / vulnerability:** *Immune* · *Vulnerable* · *Hardened* (subtracts from incoming effect **before** resistance) · *Protected* (adds to resisted effect **after** a successful resistance roll) · *Resistant* (adds to the **EL of resistance rolls**) · *Worsened* (adds directly to incoming successful effect) · *Sensitive* (adds to the **EL of effects targeting** this entity) · *Susceptible* (provides EL for environmental exposure, or adds to active attacks of that type)

**Spell-specific:** *Immutable* · *Vancian* · *Persistent* · *Guidable* · *Status*

### The Hanged Man decoded

His three Traits check out exactly against the catalogue: **Reactive** (fires on proximity, has no will of his own) · **Insidious** (his dread cannot be opposed, only endured) · **Blanket** (one roll strikes everyone present at full force). The Manifest's annotation is accurate.

### Notes toward the site refactor

*The author has said Traits are not sacrosanct and the site is being refactored. These are offered in that spirit.*

`@@ "Veiled" - WITHDRAWN as a Trait, on the author's call, and he is right.` `magick/conjuring.md` already establishes incorporeality as a *general property of all spirits*, stated once in the correct place: they remain "subject to effects that can bridge the veil, though only mental and spiritual powers can do this." It falls out of the fiction and needs no keyword. Standing principle recorded below.

**Design principle (author's, recorded here so it stops getting re-litigated):**
> **Prefer direct terms to negations, and omit anything that falls naturally out of the fiction.** "Not-substance" says less than *Spirit*. A Trait earns its place only when it is a repeatable label a GM would scribble on an index card - not when the fiction already carries it.

`@@ "Veiled" may still be worth adding for something else.` The word suggests *concealed by a glamour*, which is a real and distinct effect - and Display explicitly produces Glamours. Under consideration, deliberately not decided. Give it time and evaluation.

`@@ NAMING COLLISION - author agrees, wants a better word.` ***Inexorable*** and ***Insidious*** sit adjacent, both begin with "In-", both restrict the defender, and they mean *different severities of the same idea* (no resistance at all vs. no opposition but resistance permitted). On a sticky note mid-fight these will be confused, which defeats the purpose of the whole system. *Insidious* is the commoner case and the keeper; *Inexorable* is the one to rename.

Candidates, favouring direct terms over negations per the principle above: **Absolute** (clean, states what it is rather than what it forbids, shares no opening with *Insidious*) · **Overwhelming** (evocative but long for an index card) · **Sovereign** (thematically apt for spirits and Accords, possibly too ornate). *Unstoppable* and *Undeniable* are both negations and should probably be skipped on principle.

`@@ WORDING - Protected. Author confirms it means LESS damage.` So the rating increases the amount a successful resistance cancels. The current text - "adds to Resisted effect after a successful Resistance roll" - parses the other way just as easily. Suggested rewording: *"adds to the amount of effect a successful resistance cancels."*

`@@ SUSCEPTIBLE does two jobs.` It supplies EL for **environmental exposure** *and* adds to **active attacks** of that type. Those are different mechanics wearing one name. Consider splitting, or state plainly that it's deliberately dual-purpose.

`@@ The defensive family may be one or two Traits too many.` Eight entries - Immune, Vulnerable, Hardened, Protected, Resistant, Worsened, Sensitive, Susceptible - with a near-mirror structure that the presentation doesn't expose. There's a clean table hiding in here (flat-before-resistance / modifies-resistance-EL / after-successful-resistance / absolute, each with a defensive and a vulnerability side), and laying it out that way would make the gaps and overlaps visible. Note that *Protected* currently has no vulnerability mirror and *Susceptible* has no defensive one.

`@@ CONSTRAINED is undersold - author agrees.` Given the roll-under core, forcing a creature onto a fixed large die is brutal: a *Constrained* d12 ogre at EL 8 auto-fails on any roll of 9 through 11 and cannot use a Simple Pool to play safe. That's an elegant "immensely strong, hopelessly clumsy" engine described as a flavor note. Deserves a worked example.

> **Earmarked:** *Constrained* lands on **Goblins**, in the **Halfling slots of the Fae Court**. Carry this forward to the Fae booklet - goblinkind are already established in `magick/conjuring.md` as Fae Halflings who see with both physical and spiritual senses at once, which pairs beautifully with a Trait about *how* they roll rather than what they can do.

`@@ Shorthand consistency.` Stat blocks write the Trait as **Blanket**; the catalogue lists it as **Area Effect: Blanket**. Either bless the short form in the catalogue or use the long form in blocks.

`@@ Zombie Conceit wording.` "Immune to Complications; *all* damage treated as Complications unless explicitly Wagered as Injury or Hindrance." It does parse, and it's a lovely use of the wager rule - called shots become the only meaningful attack. But it reads as self-contradictory on first pass and takes three readings to resolve. Worth rewording for the booklet.

---

## 14. Spirits and Conjuring

*From `magick/conjuring.md` and `roles/conjuror.md`. Load-bearing for every Court booklet.*

### What a spirit is, mechanically

**Spirits are defined by their Hooks far more than by statistics.** Weak spirits may have **no Level at all** - existing almost entirely as a Hook. "A ghostly apparition unaware of its own death, just a tragic impression left on a desolate property." Powerful spirits have a **Role that *is* their nature** (Spectre, Shade, Sylph), and accumulate additional Roles through pacts and bargains as they grow.

**Three states:**

1. **Withdrawn** to the native spiritual realm - a **DL0 / free action** unless bound or Warded. Utterly *gone*, immune to anything limited by physical space or distance, and **cannot return without an anchor, a summoning, or a thinning of the veil.** Both remove them from the scene entirely.
2. **Incorporeal but present** - the default preference. Perceives the physical world dimly; reachable only by effects that bridge the veil, and only by mental and spiritual powers.
3. **Physically present** - via Manifestation or Possession. See below.

**What spirits see of us:** not our bodies, but the shadow our aura casts on the spiritual realm - stylized self-images of how we see *ourselves*. This is why they seem to know our secrets: our darkest fears, greatest regrets, and fondest hopes are what's actually visible to them. *This is the mechanical justification for every Dead creature that seems to know too much.*

**Halflings** exist fully in both worlds at once. They **cannot be bound** like pure spirits (their physicality prevents it) but **can enter binding contracts**. Possession is **impossible** against them. Goblinkind see in complete darkness because they perceive with both senses simultaneously.

### Courts

**The Dead** (ghosts, shades, ancestral spirits - retain memory and personality, driven by emotional states that outlasted death; Halfling Dead include Zombies, Ghouls, Revenants) · **Elementals** (embodied forces; Halflings skew Earth - Rock Trolls, Dryads) · **Fae** (dreams, stories, impossibilities; cannot lie but delight in misleading truths; Halflings include Spriggans, Merrows, Hags) · **Demons** (corruption and spiritual debt; Halflings include Cambions, Rakshasa) · **Angels** (rare Halflings: Grigori, Nephelim)

### The three ways to touch the world

**Display** - projects a shadow of power across the veil. Low ranks: images, sounds, temperature, smells. High ranks: full Glamours that seem entirely real. **Direct Harm from Display is *always* Hindrance or Complication.** A wound caused *by* a Glamour *is* a Glamour and vanishes with the illusion. But deception can absolutely lead a victim into real danger - walking out a high window still hurts when you land.

**Manifestation** - a genuine physical form. Medium follows spirit type and Hooks: fire elementals from flame and ash, demons from bone and spilled blood, **ghosts from ectoplasm generated by strong emotion** - easier to disrupt, immensely flexible in form.

> **The cross-application rule - this is where Malisondre's 24 comes from.**
> While Manifest, a spirit applies **all Manifestation ranks to Display** (making it more substantial) **and all Display ranks to Manifestation** (making it more accurate).
>
> Malisondre: Level 6 + Shade 6 + Display 6 + **Manifestation 6 cross-applied** = **24**, and the same 24 on the other axis. One budget, split between Manifestation-as-defense and Display-as-offense, exactly per §4. The Lessons Learned note about running both together is this rule.

> **The manifest seam nobody wrote down.** *"The physical form a spirit creates is typically the persistent Boost resulting from a Wagered roll, meaning its integrity is the number of points they wagered. Conjurors who understand this can attempt to directly counter the Boost to disrupt the Manifestation."*
>
> Every manifesting spirit in every Court booklet has this vulnerability. A Conjuror does not have to out-fight Malisondre's manifest form - they can attack the **Boost** that holds it together. This belongs in her entry and is currently absent.

Manifest forms are **subject to physical Harm**; taken Down, the form dissipates and the shock drives the spirit back to the spiritual realm, whence it cannot return without summoning or an anchor. And per the Accords: **a Manifest spirit must obey the rules of the form it has chosen.** Manifest as a man, take Harm as a man. Experienced spirits therefore choose *clever* forms - flame and smoke, crystal and living vine - and the GM routinely assigns a Manifestation its own "armor" with Hook-style disadvantages to match.

**Possession** - requires the Maneuver; cannot be attempted without at least one rank. Works **through the victim's Hooks**, battering emotion through exposed gears until host and possessor blur. Slow, patient, tedious - and spirits are not subject to time as we are. Poor against Conjurors and Halflings; most mortals are too spiritually oblivious to be valid targets for any but the most powerful entities. Commonest among **Demons and the Dead**, rarest among Elementals, **impossible for Halflings**. Extraction requires careful exorcism. Enchanted items can be possessed directly, and rare natural Anchors form for this.

> *"If the doll isn't where you left it, be suspicious."*

### Spiritual conflict

Fought on the plane of will. Range, proximity, and duration are purely conceptual - two wills close and grapple until one gives way. **The two-axis model of §4 governs it unchanged:**

- **Rebuke** = the Conjuror's offense, the assertion of will
- **Ward** = the Conjuror's defense, the aura held firm
- **Aura Hardening** = armor for these contests
- Default is **opposition** fought with Rebuke. Pour everything into Ward and you weather it as a reusable defense, dealing nothing back - but nothing resolves until someone presses.

**Third Eye / Second Sight:** full action, DL0 roll. The Conjuror becomes temporarily *like a Halfling* - present in both realms. Sees emotional scars, threads of possession, glamours, hidden motivations. Costs: substantial penalties to physical tasks, and **vulnerability to direct spiritual harm from still-incorporeal entities** - but brings full Role strength to bear in spiritual conflict.

> *Note how cleanly this validates Malisondre's stated behaviour - "she will find the one set of eyes that can see her clearly and address them first." The one character who can perceive her is, by opening the Third Eye, precisely the one who has just made themselves vulnerable to her. That is not flavour; it is the rules working.*

**Spirits cannot be destroyed** without truly exceptional means - only inconvenienced. Staggered or Down, a spirit loses any physical presence and drifts adjacent to the world, actionable by those who can touch the spiritual realm. Three finishers:

- **Exorcism** - pushes them fully into the spirit realm; no return without anchor or summoning.
- **Extraction** - squeeze out information, most often the **True Name**. Failure pushes them out of reach (but they can return once recovered).
- **Binding** - *requires* the True Name. Creates a Contract Hook. Dangerous: a hostile bound spirit will pervert every order to the exact letter of its wording. The same applies to "negotiated" contracts obtained by blackmail or threat.

### Contract Hooks run backwards

A Contract creates a special Hook on the spirit. **Unlike mortal Hooks, which degrade when resisted, a Contract Hook is reduced when a service is *rendered*** - unless separate payment is offered and accepted for that service. When the last service is rendered the spirit may Close the Contract, which **requires it to leave the mortal realm entirely**. Declining to close is an implicit agreement to another service, which **reinstates the last rank**.

True Name plus Contract Hook lets a Conjuror call the spirit to attendance as a free action, anywhere not explicitly prevented. Maneuver ranks spent on a spirit's True Name represent ongoing sacrifice and offering, and **can raise the base Level of a weak but friendly spirit.**

### Tricks

*From `tricks.md`.* A Trick is a named habit - no Karma cost, no rank, grants nothing the character doesn't already own. It declares **in advance** *how* they tend to apply tools already on the sheet: a habitual Boost, a habitual Wager, a routine cross-Role combination. Three marks of a good one: it reads as behaviour, it has a declared trigger, and **it names the mechanism it invokes.** If it wants a number, it's a Maneuver. If it does something the Roles can't justify, it's a power and costs Karma.

Note the two-edged bit: *"A Trick the Warrior uses in every fight becomes a reputation someone could also use to set him up for a Boost of their own."*

### Malisondre's manifestation Trick - worked arithmetic

Her habit: **Boost first, then Wager heavily.** She does not simply manifest; she prepares, then commits.

```
Base manifest pool                                    24
  Boost action first (24 dice, expect ~12)           +12
                                                    ────
  EL for the manifestation roll                      ~36
  Wager for Manifestation integrity                  -20
                                                    ────
  Rolled at                                          ~16   (needs >0, ≤16)
```

Failure odds on a 16-die Simple Pool are roughly one in 65,000. She is not gambling; she is paying two actions for a manifest form with **integrity 20** and then still fielding her full 24 every exchange thereafter.

**Why it matters at the table.** The manifest form's integrity *is* the wagered points (per `magick/conjuring.md`), so a Conjuror who counters the Boost is contesting a **20**, not a 6. She is no lightweight. Equally, the Trick is public information the moment anyone watches her do it once - and per the tricks page, a known habit is a handle. A prepared party can interrupt the *Boost*, before the wager ever happens, which is far cheaper than fighting the finished form.

### The wager cap - RESOLVED, and it unifies with the training gate

**The cap does apply to Manifestation.** Author's ruling: *"You can never dedicate more points than your rank in the relevant Role"* governs anything you could **only** do with a Role - and Manifestation is Role-gated. Her manifest presence is therefore capped at **6**, and a Sylph manifestation at **2**.

This is the same principle as the training gate in §1, not a second rule:

> **Where a Role gates the action, that Role's rank caps what you may commit to it** - both the base Level you may add, and the points you may wager.

Which cleanly explains the Tricks examples. *Mercy Shot* wagers "up to her Sniper rank" because a dedicated Hindrance from a rifle shot is Sniper work. *The Bead* (aiming) and *Grapple* wager uncapped because **anyone can aim or grab** - no Role gates them, so nothing caps them. Both readings were partly right; the gate is the deciding factor, not the wager's purpose.

*Prior draft of this section argued the opposite. Corrected.*

### Two modes of Manifestation

This is the part that needs careful presentation, because readers arrive assuming "manifestation = a body you can punch," and that is not what it is.

**Mode A - the effect *is* the manifestation.** She manifests only for the duration of a single effect. Safer: there is no persistent presence to counter and no standing target. Weaker: nothing accumulates, each action stands alone.

**Mode B - a stable, Wager-supported presence.** Wager up to the Role cap for a persistent Boost. The presence lasts the scene, and **this is what lets things stack.** It *is* a Boost, which is precisely why a Conjuror can counter it (`magick/conjuring.md`), and why being Manifest unlocks the cross-application rule that builds the 24.

**Two different numbers doing two different jobs - do not conflate them:**

| Number | What it is |
|---|---|
| **24** | Her action pool each exchange while Manifest (Level 6 + Shade 6 + Display 6 + Manifestation 6 cross-applied), split across offense and defense |
| **6** | The wagered integrity of the persistent presence that keeps her Manifest at all |

Six is not "her hit points." It is the cost of staying in the room.

### The shell game, exactly as the rules write it

Her prose has her as "one of the flickering figures, or several, or the poison fog at your ankles, or the very air you are trying to breathe," with servants and phantoms in her wake, "some real and biting, some only the idea of a threat."

That is **Display 6 versus Manifestation 6**, and the distinction is mechanical:

- **Display** produces Glamours that seem entirely real but deal only **Hindrance or Complication**, and any wound they cause vanishes with the illusion.
- **Manifestation** produces something that can actually bite - real Injury, real physical presence, subject to real Harm.
- Only Second Sight tells them apart. *Which is why she closes the seeing eyes first.*

> **The elegant woman walking and talking is almost certainly a Display.** The Manifestation is the fog.

### This resolves the "Form Is Only Makeup" problem

Flagged earlier as a possible contradiction with the Accords. It isn't one.

The Accords bind a spirit to *the form it assumes* - its **Manifestation**. A Display is not an assumed form; it is a projection. So:

- **Glamours are free.** Shed, changed, multiplied at will. "Form is only makeup" is true of these.
- **The Manifestation binds her.** Manifest as a man and take Harm as a man.

Therefore the sharp play, and it is entirely hers: **manifest as something whose rules are cheap to be bound by.** Fog cannot be stabbed. Air cannot be grappled. Then Display everything impressive. She is bound to the fog's rules, and the fog's rules are excellent.

**RULING (author):** the 6-point Boost is **why** she gets to combine Display and Manifestation. It is not an additional +6 on top. No double-count: the 24 already reflects it. The rule is simply the Wager-as-embodiment given the spotlight, with a little Conceit for ambience - no new subsystem.

### Consistency audit of the manifestation model

*Stress-tested against `resolving-combat.md`, `multiple-actions.md`, `wagered-actions.md`, `feeling-down.md`, and `magick/conjuring.md`. It holds. Notes on the two soft spots follow.*

**Multiple manifestations are possible and strictly worse - which is the correct answer.** Each needs its own wager, each capped at 6. Three forms cost 18 of her 24, leaving 6 to act with. And redundancy is an illusion: breaking *any* form shocks her back to the spirit realm, so N forms means N ways to suffer the same banishment, not N lives. The conclusion "better to spend those points on pure defense" is therefore **derivable from the rules**, not merely wise - which is the mark of a design that hangs together.

**Her near-invulnerability is real, and its limit is exact.** Defense is a reusable soak rolled fresh against every incoming point (§4), so a large allocation makes her extraordinarily hard to touch. Per `resolving-combat.md`, a creature like this "is only fragile against attacks it cannot answer." Her deep defensive pool does nothing against a **Role-gated contest she must answer at Sylph 2.** The armour and the seam are the same sentence, read from two directions.

**Banishment is temporary for her, and that is why she's a situation.** Breaking a form drives a spirit back, "whence they cannot return without the assistance of summoning or an anchor." Her Presence is **Anchored** - a clause in Tahanos's contract. She has an anchor. So the party can remove her from the scene and cannot remove her from the campaign. "At least for a time" is doing precise mechanical work.

> **The best thing in the design, and it should be stated nowhere in the text.** Her habitual clever play - manifest as something airy, cheap for the Accords to bind - walks her straight onto the one axis where she is weakest. A thousand years of a trick that has always worked, with a hole she has never been forced to notice. Let the table find it.

### "Her element is air" - RESOLVED (author): it is a domain statement

Not a power claim. She is **multi-domained**, and the original text named all three:

> Her Demon is **Succubus**. Her Ghost is **Shade**. Her Element is **Air**.

**Demons in Averond are usually spirits of Fire.** Her being Air is a deviation, and the deviation is the point. The line got mangled and softened somewhere in the mockup rewrite.

*Corroboration that the original design was coherent:* her surviving Fate and Cortex blocks already carry **"Brimstone Is a Borrowed Coat"** and **"Brimstone Costume: +2 Provoke vs. those expecting fire."** Brimstone is a *costume* precisely because she is not a fire demon. The stunts and the domain line were built together; only the prose was damaged.

And this deepens the seam rather than excusing it. Air is not incidental to her - it is genuinely part of what she *is*, expressed mechanically as **Sylph 2**. She holds a domain she never developed.

### Disruption vs. Down - two separate roads (author's ruling)

**These are different removals with opposite cost and duration profiles.**

| | **Disrupt the form** | **Take the spirit Down** |
|---|---|---|
| Threshold | The **wagered integrity** (2 as air, 6 as ectoplasm) | Harm exceeding **base Level** (7 for her) |
| Who can do it | Anyone who can harm the form on its own terms | Only those who can direct Harm at the spirit itself |
| Effect | Driven out past the Borderlands | Genuinely Down |
| Duration | Short - **with an anchor, possibly back within a day or two** | Long |

**Harm to the Manifest form *is* Harm to the spirit.** They are bound to the rules of the form they have chosen; the damage is not to a puppet. But because disruption triggers at the *wagered* number rather than at Down, a disrupted spirit is usually carrying far less Harm than a defeated one - which is exactly why she recovers so much faster.

Disruption is a shortcut: difficult to reach, but it doesn't last.

> **The risk curve this creates, which is the elegant part.** The wager is simultaneously the form's **durability** and her **exposure**.
>
> - **Air, wagering 2.** Nearly impossible to meaningfully damage - what do you stab? - but two points ends it, and she walks away with two points of Harm. Cheap to break, cheap to survive.
> - **Ectoplasm, wagering 6.** Sturdier and far easier to land a blow on, but six points is *one short of Down for her*. Expensive to break, and very nearly ruinous when it goes.
>
> Every manifestation is therefore a real decision, and the decision is legible to a table that pays attention. She is not choosing a costume; she is choosing how much of herself to put in the room.

**And she still rolls defense either way.** That pool is not Sylph-gated - defending a manifestation is Shade work - so it can run well past the Sylph ceiling of 6. Twelve points of active resistance standing between an attacker and those two fatal points is entirely plausible. **But it can be done.**

### Excess Harm - RULED (author): it becomes a Hindrance

Overage beyond the form's integrity does not vanish, and does not Down her. **It lands as a Hindrance** - and per `types-of-harm.md`, a Hindrance cannot be recovered by any roll. It must be resolved through the story.

**The story that resolves it is reporting back to Tahanos.**

Everything else is the normal recovery rules. She makes her rolls like anyone. The Anchor means she returns; heavier Harm simply means she takes longer about it.

**Do not overstate this.** *No* road destroys her, and that is not a property of the Hindrance rule - it is simply what being a spirit means. `magick/conjuring.md`: *"Without truly exceptional means they cannot be destroyed, but they can certainly be inconvenienced."* Taking her Down does not destroy her either; it incapacitates her and opens the three finishers (Exorcism, Extraction, Binding). Destruction requires something extravagant and specific, and it is not on the menu by default.

So the two roads are not "cannot finish her" versus "can." They are:

- **Break the form** → banishment for a time.
- **Take the spirit Down** → incapacitated, and now reachable for Exorcism, Extraction, or Binding.

The real win is **Binding**, or the Accords play - never a corpse.

### The banishment Hindrance - a general spirits rule

Forcible banishment from an overage leaves a Hindrance, and **the default Hindrance is a span of time that must pass.** The GM is expected to invent something with character rather than count points: *a year and a day*, *until the next eclipse*, *until the river freezes*. Folkloric by design.

This is deliberately a **narrative dial, not a formula.** Consistent with `types-of-harm.md` - Hindrances are removed through the story, never by rolls.

### Malisondre's version, and what it costs her

Hers is *you answer to the boss*. **Tahanos is not a kind creditor.** He will declare her banished for a century unless she sinks herself deeper - becoming less independent, more purely the arm of his whims.

> **The nastiest and best consequence in the entry.** Her remaining seam is that she is "still capable of wanting something for herself," and "cannot resist a contest she might lose against someone clever enough to make the stakes real." That last scrap of the soul who signed the bargain is *exactly* what Tahanos's price erodes.
>
> So a party that keeps beating on Malisondre is progressively converting her into a purer instrument of her patron - more dangerous, less negotiable, and stripped of the very seam they might have exploited. **The violent solution actively destroys the diplomatic one.**
>
> This is the GM craft note *"make the right choice cost the most"* running in reverse, and it should never be explained to the players. Let them notice that she is less willing to deal than she used to be, and let them work out why.

`@@ TODO - general spirits rule, not a Malisondre rule.` **When** do spirits get their recovery rolls? Sunrise, sunset, midnight - probably varying by type of spirit. Wants writing into the spirits section of the source. Nice bit of worldbuilding doing mechanical work.

### Implications for The Dead - things currently missing

### Malisondre's contract - the inversion (author's clarification)

Contract Hooks count down **when tasks are agreed done**, not merely performed - and a contract **can always be renegotiated.**

**Her existence runs on power Tahanos gave her.** The contract is the conduit. Closing it requires leaving the mortal realm entirely. Therefore:

> **Malisondre is structurally incentivized never to finish anything.**

That single fact explains the whole character. She is a *broker* rather than a resolver because brokering **generates** obligation instead of discharging it. Ten centuries of never quite concluding. "She is not an encounter, she is a situation" is not a metaphor - situations are precisely the things that do not conclude, and she has an existential stake in keeping it that way.

The Accords hand her the tools for it:

- *"A favor Accepted implies a Debt Accepted unless explicitly excluded"* - she can manufacture fresh obligation from generosity.
- *"Proper Payment Refused implies a Continuance of the Agreement"* - **she can refuse payment to keep an agreement alive.** This is her defensive move and it is written into the Accords.
- Renegotiation is always available - she adds services before the last one can be agreed done.

**The lever inverts, and gets far more interesting.** The way to threaten Malisondre is not to kill her; it is to drive her contract toward *completion*. Force services to be rendered **and agreed done**. Or offer a payment she cannot Properly Refuse. Beating her is an Accords problem, not a combat problem - which is exactly the kind of undoing "that is a table's work" was pointing at.

`@@ The Manifest says her undoing "is not written here; that is a table's work."` Fair as authorial restraint - but the *system* has a standard answer (Stagger or Down her, Extract the True Name, Bind) and a table that knows the rules will find it. The entry should probably acknowledge the standard road exists and say why it's harder in her case, rather than leaving a silence a rules-lawyer will read as an oversight.

`@@ "Form Is Only Makeup" needs checking against the Accords.` The Accords bind a spirit to the rules of the form it assumes. Her prose says form is shed the moment it stops buying - true between manifestations, but while manifest she is bound. Worth one clarifying line so the two don't appear to contradict.

`@@ The Hanged Man is Display 1 - so his Harm is Hindrance or Complication only, by rule.` The Manifest describes dread that makes victims flee and carry an aversion afterward, which is a clean Complication read. Worth confirming the other systems' blocks didn't quietly upgrade it to real damage.

`@@ Agnes has Possession 2, and Possession works through the victim's Hooks.` The published rulebook says so explicitly - "if any Hook can be manipulated toward Possession she will take every chance that doesn't expose her." The Manifest's version lost that. It is the mechanical heart of her entire arc. Recover it.

`@@ The Zombie is a Halfling, and Possession is impossible against Halflings.` Worth a line - it means a zombie is one of the few things Agnes or Malisondre simply cannot take.

---

## 15. Notes for Cross-System Conversion

**What L1 has that the others don't** - these are the features that require creative hackery when translating *out*, and should be flagged honestly in the Manifest rather than glossed:

| L1 feature | Nearest analogue elsewhere | Honest verdict |
|---|---|---|
| Roll-under-your-own-ceiling | None | No system on our list does this |
| Reusable defense soak vs unlimited attackers | Fate's defend action (but per-exchange, not free) | Closest is Fate; still not the same |
| Cross-Role shared budget | None | Roles draining each other has no counterpart |
| Wagering / called shots capped at Role rank | 5e called shots (variant), Cortex effect dice | Partial only |
| Harm as pure EL modifier, no HP | Fate consequences; Cortex complications | Reasonable fit both ways |
| Hooks | Fate Aspects; Cortex Distinctions; Shadowdark ability tags | Strong fit - the family resemblance is real |

**The honest framing for the book.** L1 sits at a higher level of abstraction than most of its neighbors, and generality absorbs specificity in one direction more readily than the other. Anything another system expresses as a modifier, tag, advantage, or trait has an obvious home here as +EL, a Trait, or a Hook. The reverse requires inventing structure L1 deliberately doesn't have.

State this as a structural property, demonstrate it repeatedly, and let readers draw their own conclusions. Do **not** assert superiority in the published text.

Corollary discipline, already in Lessons Learned and worth repeating: *never declare a system can't do something until the toolbox is empty.* That has been wrong more often than right.

---

## 16. Open Questions and Annotations

`@@ CANON OVERLAP - intentional, per the author.` The Hanged Man and Agnes already appear in the rulebook's Threats appendix (`L1/threats.md`). These were placed as **placeholders** - something concrete for the examples - and they are where the whole project started. The plan: the Manifest versions get rewritten and polished, then flow **back** into the rulebook as the upgraded canon, possibly carrying a small cross-system demo with them. Not a conflict to resolve; a round trip to complete.

`@@ NAME - SETTLED.` **Gallows Hill.** Applied across The Dead, Lessons Learned, and the Session Seed. He is now "The Hanged Man of Gallows Hill" - a shade on-the-nose, but the tone earns it.

`@@ Salvage from the rulebook before overwriting.` The published Agnes prose is *richer* than the Manifest's in specific places worth keeping: the barrette is **garnet and pewter**; she died of **ague and grippe**; and there is a full paragraph on how she works PC Hooks toward Possession that the Manifest lacks. Harvest before replacing.

`@@ Not yet digested:` `extreme-results.md` (critical success/failure), `kamikaze-blitz.md`, `accumulated-progress.md`, `luck.md`, `armor.md`, `gear-traits.md`, `karma.md`, `glossary.md`, the Roles catalogue, and all of `magick/`. Pull these as specific creatures require them. **`magick/conjuring.md` will matter early** - it holds the Accords, the nature of spirits, and reaching across the Veil, all load-bearing for every Court booklet.

`@@ For the site, later:` this digest's §0 and §4 are arguably better on-ramps than the current `mechanics.md` / `resolving-combat.md` openings for readers arriving from other systems. Consider a short "If You're Coming From Another System" page. The roll-under rule in particular deserves a louder warning than it currently gets - it is the single most counterintuitive thing in L1 and it appears mid-paragraph.
