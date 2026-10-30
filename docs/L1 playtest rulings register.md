# L1 Playtest Rulings Register

The one place for rules rulings, clarifications and open design questions that came out of the Caria solo playtest (S01-S14, 2026-09-26 to 2026-10-30). Organized by TOPIC, not by session. Per-session gap logs now keep brief notes and point here.

Compiled 2026-10-22 by Lilita from: the S08 cumulative gap log (S1-S8), the pre-S09 Addendum (crafting, downtime, wands, familiars, followers), the S09-S14 gap logs, and Lee's standing rulings notes. Unlinked on purpose: nothing in the site points here yet.

## How to read an entry

Each entry: **[STATUS] Short title.** The ruling or question. *(Where it came from.)* -> Where it belongs in /L1.

- **[RULED]** -- Lee ruled it at or away from the table. Not yet in the repo text unless the target says "already in".
- **[IN BOOK]** -- the repo already says this; the playtest confirmed it (often after the GM missed it).
- **[UNCLEAR]** -- the repo covers it but reads two ways, or a sentence would stop a misread.
- **[OPEN]** -- no answer yet. Needs Lee.
- **[PROPOSAL @@*]** -- Lilita's suggestion. Noncanon until Lee says so.
- **[SUPERSEDED]** -- kept for history; the later ruling is named.
- **[CONFLICT]** -- two of Lee's own rulings disagree. Needs one line from Lee.

Updated 2026-10-22: the four conflicts in section 23 resolved.
Updated 2026-10-30: the late S14 rulings (Days 15-18) folded in.

Sources: S01-S14 = session; "Add." = the pre-S09 Addendum (2026-10-11 design talk); "notes" = Lee's standing rulings notes.

Maintenance: add new rulings under their topic, newest last, with the session tag. When Lee ratifies a proposal, change its tag. When text lands in the repo, change the target to "-> DONE: page.md".

---

## Contents

1. Core engine: rolls, opposition, effect
2. Extremes
3. Extra Effort
4. Luck Tokens
5. Boosts, Assists, Wagers, Synergy
6. Hooks
7. Karma and advancement
8. Harm, Down, recovery, death
9. Healing, medicine, privation, fatigue
10. Spellcraft: known, bound, unbound
11. Spellcraft: casting, improvisation, release
12. Spellcraft: Persistent, duration, the Dawn
13. Spellcraft: individual spells and Traits
14. Conjuring: the Sight, Wards, Rebukes
15. Spirits, familiars and the Accords
16. Folk charms and materials
17. Items and crafting
18. Companions, followers, apprentices
19. NPCs and opposition
20. Scenes, time and downtime
21. GM craft and procedure
22. Setting rulings with mechanical weight
23. Conflicts to resolve
24. Open questions index

---

## 1. Core engine: rolls, opposition, effect

- **[RULED] Everything rolls.** Difficulty and opposition are always rolled pools; the two sides compare results. Never a fixed target number ("you need N"); that creates "you can't possibly," which Lee dislikes. *(S06 Pt2; S11; notes)* -> core-mechanics.md: one plain early sentence, "Everything rolls. Difficulty is a pool, never a target number."
- **[RULED] Flat target numbers as an optional variant.** Not standard, but a table that can't swallow opposed rolls can play "D&D with WoD dice." *(S08)* -> a short variant sidebar, paired with "Everything rolls" so it reads as the exception.
- **[RULED] Effect is measured against the opposition's LEVEL, not its pool.** A pool includes skill, so Level <= pool: N dice means Level N only if untrained. Effect equal to Level = a good read with the finest detail held back; effect over Level = complete (the resistance is Down), even on a passive roll. This is why a separate oracle is rarely needed. *(S13; notes)* -> core-mechanics.md / resolving-combat.md, where effect is defined.
- **[RULED] A roll means there is something interesting to see; the dice say how much.** The GM needn't know the answer in advance; let the dice write it, or merely hint. *(S13)* -> gm-rules.md, "when to roll."
- **[RULED] Roll only when failure is interesting and consequences are meaningful.** Many beats run with no roll by design. *(S01, S05; notes)* -> gm-rules.md, stated early and plainly.
- **[RULED] No ladders.** Don't key outcomes to effect bands ("1-2 shows X, 3-4 shows Y"); that's Fate or old-school. Go back to an opposition roll: accumulate effect as progress, run mutual attrition, let Harm types carry the results. A GM may hack in old methods and it will work, but the canon move is the opposition roll. *(S09, S12; notes)* -> GM guide: "When stakes are a struggle against a force, give the force dice and fight it."
- **[RULED] Oracle drift.** When the GM reaches for a yes/no oracle, stop and ask who or what is resisting, and how L1's own model would handle it. Not a show-stopper. *(S12; notes)* -> GM guide paragraph. See also 21, the Bare Oracle.
- **[PROPOSAL @@*] Situation first.** Many "does X happen?" questions answer themselves from the clock, the place and the character. Use that before any roll. *(S12)* -> GM guide.
- **[RULED] Accumulated progress / attrition is the general tool.** Reading a damaged text: the erasure has a rating and rolls each exchange; the reader's effect accumulates; read whole once the total exceeds the rating; losses cost Complications (eyestrain). *(S12)* Social attrition: a room's doubt as a track (rating 4); effect accumulates across rolls; won when the total passes the rating. "Practically anything can be handled that way." *(S13)* Learned fear as a track (Benno's leg, rating 3), separate from the long physical work, which needs no rolls. *(S13)* -> accumulated-progress.md: a social example and a "long cure vs tonight's contest" example.
- **[IN BOOK] No time pressure, no roll.** accumulated-progress.md: "If there's no time pressure, why roll?" Used for reading an intact book overnight and similar. *(S13, S14)*
- **[RULED] Dice committed to an action are unavailable for defense.** A character who sets none aside gets NO defense roll; a character doing nothing always has base dice. This is why the Kamikaze Blitz works. *(S11; notes)* -> combat/actions text, bold, with the Blitz as the example.
- **[RULED] You can't both oppose and resist the same exchange.** An all-in opposition roll is the defense; to also resist, split EL first. *(S11; notes)* -> resistance-and-opposition.md.
- **[RULED] Intimidation is an attack.** A look, an accusation or an interrogation meant to frighten deals Complications. Social Harm carried whole scenes (a hearing played as combat). *(S11)* -> types-of-harm.md already says "as good as a crack to the head"; add a worked social example.
- **[PROPOSAL @@*] Detection and effect are separate rolls.** One roll answers one question; an Extreme on a reading roll doesn't bleed into whether the target noticed. *(S11, Lee's caution accepted)* -> GM guide.
- **[RULED] Perceiving something and Boosting off it are separate rolls.** No double-dipping one Token; the GM may allow the Boost as a free action. *(notes)*
- **[RULED] First principle for consequences: ask the player.** "He won by two -- what's that look like?" The player describes the result; the GM guides it for fairness. *(notes)* -> GM guide.
- **[OPEN] Excess effect against a destroyed barrier.** When a ward is broken with effect to spare, does the excess carry through to what it shielded? Played: spent on the barrier. *(S11)*
- **[OPEN] Opposition vs resistance in a spiritual clash.** When an NPC is "a working," whose EL opposes? *(S11)* -> conjuror.md.
- **[RULED] Scene-factor and gear Boosts.** A factor already present in the scene can be rolled as a free action if the GM agrees; its value adds to the action (as dice). Once the character spends time building it, it's a Boost action at her skill. *(S11, S12)* See 5.
- **[RULED] Searches are ATTRITION.** Hunting one thing through a crowd (a spirit seeking one man in a city) accumulates progress against the haystack's Level; a lost exchange Harms the searcher by the margin (a Complication, -1 EL) and he can keep searching. Same model as reading a damaged text (S12). "A search is a fight with the haystack." *(S14, Lee)* -> GM guide; actions-and-timing.md example.

## 2. Extremes

- **[IN BOOK] Extremes need 3+ dice.** A 2-die all-zero is a plain failure: no fumble, no side effect. Flat successes (Hook, Armor) never count toward an Extreme. *(S03, S11, S12; notes)* -> repeat in the GM crib.
- **[RULED] Extreme credit (karma.md option) in use.** An Extreme earmarks 1 Karma to the score rolled (or base Level if no Role was involved); synergy lets the player choose which. The earmarked advance completes automatically and does NOT use the session's improvement slot. *(S01, S10, S11)* -> karma.md: say it outright; sheet template line.
- **[UNCLEAR] One mark per skill per session, or one per Extreme?** Played: one per skill per session. An Extreme failure Tokened down to a common failure still counts as "rolled." *(S03)*
- **[RULED] A Token vs an Extreme Failure only makes it a common failure** -- it doesn't buy a best result. An Extreme Failure also excludes after-the-fact flat add-ons (Hook, Armor). *(S03)* -> luck.md and extreme-results.md.
- **[OPEN] Is a Token-bought top result an Extreme success?** Provisional: no -- Extremes are about the dice. *(S02, S03)* -> one line in luck.md.
- **[RULED] A Token beats the roll but doesn't negate the opponent's Extreme benefit.** *(notes)*
- **[RULED] The side effect of an Extreme success scales with the roll** (4 dice -> Boost 4). The player may propose a better side effect ("someone notices she's being merciful"). *(S11, S12)*
- **[RULED] Extreme success on a HOLD roll: lasting quality.** A pass/fail roll has nowhere to put extra effect, so the bonus is quality: the glamour so true "the Dawn cannot touch it" (lasts until lifted). *(S10)* -> extreme-results.md or spellcraft.md example.
- **[RULED] Extreme success on a casting's own Dawn roll resets its age to 1.** *(S13)* See 12.
- **[RULED] An opposition's Extreme failure lands on the opposition** (the borrowed cold let go of Teague's blisters). *(S12)*
- **[RULED] An Extreme on a casting may wake a mind** (a spell accidentally spawning a spirit), especially a Persistent or Enchanted effect on a living current. Bigger pools make Extremes rarer, so skilled casters are naturally less likely to do it. *(S04)* -> spells.md or beyond.md.
- **[RULED] NPC Extremes pay no Karma; the free Token goes to the GM's pocket.** *(S11)* Table rule since S11: an NPC's Extreme pays the GM a Token.
- **[OPEN] "A Token spent against an Extreme earns the roller Karma"** (extreme-results.md). Lee likes the reading but flags the rule for review. *(S11)*
- **[OPEN] A companion's Extreme: whose free Token, whose Karma?** Played: the Token to the PC (her bound spirit acting for her); Karma to the spirit's own score -- the skill used (Asher -> Aura Reading 1). *(S13)* -> extreme-results.md / karma.md, a companion line.
- **[OPEN] Extreme failure on a RECOVERY roll.** recovery.md: a plain failure does nothing; extreme-results.md: an Extreme failure must have a bad side effect. Played: a fall in the night, +1 Complication. *(S13)* -> recovery.md.
- **[OPEN] Extremes by impersonal opposition** (the Dawn, an Injury). Played as margin only, no Token. *(S13)* -> extreme-results.md, one line.
- **[RULED] Standard side effect: the CONFIDENCE BOOST.** A good roll's Extreme (or an opposition's Extreme failure) can count for its usual purpose AND as a Boost on the NEXT roll, dice scaled to the roll (3 dice -> Boost 3). It helps or it doesn't; it raises the odds of the next roll and, with a bigger pool, lowers the odds of another crit. Prefer it to "time for another roll," which is no boon when the dice go badly. *(S14, Lee)* -> extreme-results.md: list as a standard example.
- **[PROPOSAL @@*] Know the rate.** A 3-die opposition rolls all-blank 1 time in 8 and all-ones 1 time in 8 -- an Extreme of some kind a quarter of the time. GMs choosing a rating should know a 3 is lively. *(S14)* -> GM crib.

## 3. Extra Effort

- **[IN BOOK] Extra Effort (dice.md).** Add dice beyond EL; a total over EL fails completely (effect 0); extra dice forfeit Extremes. *(S12: EL14 + 4 = 18 dice, total 8, valid.)*
- **[RULED] On a recast, going over IS a zero** -- it destabilizes the spell. *(S09; supersedes the S08 "only a zero destabilizes")* -> spellcraft.md, one line, cross-linked to dice.md.
- **[RULED] A Token on an Extra Effort roll sets the result up to the EL**, not up to the number of dice rolled. *(S09)* -> luck.md example.
- **[RULED] At the crafting bench, Extra Effort follows the general rule.** *(S14)*

## 4. Luck Tokens

- **[RULED] Refresh.** One Token at the start of every scene if there's room (cap = Level). Tokens fully reset each session. Same for the GM. *(S06 Pt2, S11; notes)* -> bold it in luck.md and the GM guide. The GM missed it for ten sessions.
- **[RULED] GM starting Tokens** = max(number of players, highest PC Level) + a flat 1, plus 1 per scene if room. *(S01; notes)* -> luck.md needs the flat +1; fix the Operating Guide's "per additional player."
- **[RULED] Anyone can spend a Token on ANY roll** -- another PC's, a companion's, a spirit's, even the GM's roll against them. Player-facing luck, narrated as will, luck or divine intervention. A Conjuror may Token her spirit's roll ("He needs the confidence"). The GM may spend GM Tokens on a player's roll when deserved. *(S04, S08, S11, S14)* -> luck.md, say "any roll" outright.
- **[IN BOOK] A Token sets the result to any value up to EL** (player's choice; may set it lower). *(S08)*
- **[RULED] Tokens can exceed the cap** when gained from Extremes or GM kudos; over-cap Tokens persist without refresh until spent below the cap. *(S11, S12)*
- **[IN BOOK] A Token may be spent until the final resolution.** *(S02)* -> [OPEN] say when resolution is "final" for a social roll that plays out over a scene (S13: a Token after the crowd was narrated, treated as legal while the scene was open).
- **[RULED] Token and Hook trigger can stack on the same failure.** *(S06)*
- **[RULED] Token-pinning a spell's effect.** Cast, then pin the effect with a Token: it holds the duration without concentration, letting the caster release the binding and bind another spell. A pinned Token is ALLOCATED: it counts against the cap and blocks the refill until released. *(S01; notes)* -> luck.md / spellweaver.md (spellweaver.md says a released spell "winks out"; the pin is the exception). See also 17, Pinned Work.
- **[RULED] GM Tokens are for stakes, not routine** ("boss fight" scenes). *(S02)* **[PROPOSAL @@*]** Spend GM Tokens to keep an NPC in the story, not to cancel a success the player paid for. *(S11)*
- **[OPEN] Token economy in solo play.** S2 data: half the key rolls Token-resolved. Mostly a GM-not-spending effect. Proposed check-in only, no rule change. *(S02)*

## 5. Boosts, Assists, Wagers, Synergy

- **[RULED] Boosts add DICE, even after the fact.** *(S08)* -> actions-and-timing.md.
- **[RULED] A Boost uses the creator's skill**, not a flat rating on the object or circumstance. *(S12; notes)*
- **[RULED] Unwagered Boosts are one-shot and ephemeral.** One that goes unused lapses; it doesn't carry to a later scene or session (GM may except). *(S12)*
- **[RULED] Chained/stacked Boosts are intentional.** A Persistent Boost feeding a Boost roll feeding the final roll (EL14 on a festering thumb): the "wizard hanging back building a takedown." Important NPCs can do it too. GM guidance, not a cap. *(S06 Pt2; notes)*
- **[RULED] Diagnosis feeds treatment.** A diagnosis roll's effect may Boost the treatment that follows. *(S07)*
- **[RULED] Boost size: OPTIONAL GM guideline only** -- "a Boost adds no more dice than the EL it is boosting." Not canon unless it earns its keep. Contrast assist-rule.md's stricter cap (a gear Boost capped at the user's Role rank): outside help is limited by your skill to use it; your own knowledge isn't. *(S05)* -> if added, explain why the two caps differ.
- **[RULED] A spirit's help on a non-Conjuror roll is an ASSIST**, capped by the PC's rank in that Role (assist-rule.md). Asher on a Spellweaver casting = Assist capped at Spellweaver 4. *(S13)*
- **[RULED] Hook successes can pass through a Boost** to another character. *(S06)*
- **[RULED] Keyed Wards are Dedicated wagers**, capped at the relevant Role rank (wagered-actions.md). See 14.
- **[OPEN] Retro-wager.** Can a Token-raised effect be DEDICATED after the fact? Played: no named residual after the roll; the narrated margin instead. *(S13)* -> wagered-actions.md, one line.
- **[RULED] Persistent Wager is not the Persistent Trait.** The Wager is a standing Boost; the Trait keeps a spell running. Same word, different tools. *(S06 Pt2)* -> glossary note.
- **[IN BOOK, needs example] Role Synergy.** A Role counts if failing at THAT Role would visibly change the outcome. *(S05)* -> role-synergy.md: one worked example with inclusion and exclusion.
- **[IN BOOK] A Persistent Boost is wagered BEFORE the roll** (wagered-actions.md, Residual Effects): set the points aside, succeed with what's left, and they become a named bonus for the scene. A Boost rolled unwagered is one-shot. *(S14)*
- **[RULED] Boost, then wager -- separate rolls.** With time, a gathered Boost can feed a separate wager roll that locks a Persistent bonus into an item; that bonus can then feed further Boosts on the same work. "Time and patience allows a lot of double-dipping." *(S14, Lee)* [OPEN] Boost chains: the optional "a Boost adds no more dice than the EL it boosts" is the natural brake if one is wanted.
- **[RULED] A casting's effect can be a BOOST to mundane work.** A Veil glamour that hid a child's pain ("all the pain goes down the scarf into the potato") was rolled as its own casting, and its effect counted as a Boost to the surgery -- the patient doesn't scream or pull away. *(S14, Lee: the session's standout creative moment)* -> spellcraft.md or healer.md example.

## 6. Hooks

- **[RULED] When a trigger pays Karma.** Only when the Hook actually complicates or derails what the character is trying to do NOW; menace, color and foreshadowing don't pay. *(S01)* A delayed bill that lands later is the trigger in the session it lands. *(S02)* -> hooks.md, one threshold sentence.
- **[RULED] The Hook bonus is a per-scene BUDGET equal to rank**, spent in pieces across rolls (owner and exploiter alike). Each point usable once per scene. Once spent, "leaning on the Hook" colours the fiction but adds nothing. *(S04, S06, S11, Add.)* -> hooks.md: "once per scene" needs better wording; show splitting.
- **[RULED] Owner's points add to the RESULT (flat successes); the GM's pro bono application adds DICE** to the pool as a standing Boost when a situation is plainly about the Hook (free; doesn't touch her budget). *(S03, Add.)* -> hooks.md, borrowing armor.md's "after-the-fact extra EL that already rolled."
- **[RULED] The owner may tap the Hook after the roll**, like a Token, until resolution. *(S03)*
- **[OPEN -> mostly RULED] A Hook used AGAINST its owner.** Exploiters add the rank as DICE (a Boost from the fiction), declared before rolling; once per scene per exploiter; may be spent in pieces; can feed a Wagered Persistent Boost, which the GM may back with a Token. Each tap that complicates her is a trigger and pays her. "The character IS the power play." GM guide: exploiting Hooks is the GM's half of the bargain, not optional cruelty. *(S03, S04)* -> hooks.md: the against-you half (the repo's own open list has this too).
- **[RULED] A Hook's rank can never exceed Level.** *(S06 Pt2; notes)*
- **[RULED] Hook alterations are always FREE** and outside the improvement limit (a relief valve). Reducing a Hook still needs testing. *(S01, S05)*
- **[RULED] Spending Hook budget on presence** (accept a visible tell without taking a trigger) is a fitting use. *(S06)* [OPEN] whether it's a general option and how it interacts with trigger accounting.
- **[RULED] Self-triggering counts.** *(S06 Pt2)*
- **[RULED] A deferred Hook offer can stand**; the player chooses the moment ("make the consequence worth a Karma"). Offer once, plainly. *(S08, S11, S12)*
- **[RULED] Caria's trigger is UNWANTED attention, not necessarily negative** (fawning, smitten, suspicious, crude). "Overly fawning" counts. *(S10, Add.)*
- **[IN BOOK] Apology Karma** when no Hook triggered all session. *(S02, S09, S13)*
- **[RULED] Hooks as currency.** An NPC spirit's Hook can name its price (Shimmer, *A Keeper of Secrets*). *(S05)*
- **[OPEN] Karma up to Hook rank per session** (karma.md option, adopted S01) is the income knob that scales; watch it. *(S04)*
- **[RULED] A SELF-triggered Hook pays when it costs.** The player may lean into her own Hook; it pays Karma if the trigger is real and the consequence lands (brimstone flaring before a recording clerk and a frightened prisoner -- testimony for her enemies). *(S14)*
- **[RULED] Hook budget on social rolls when she WANTS the attention** (the sheet's own wording) -- applied pressing a confession. *(S14)*

## 7. Karma and advancement

- **[RULED] Costs.** Level costs the NEW Level ("higher"); pretty much everything else costs its CURRENT rating to advance [Lee, 2026-10-22]; a NEW Role or Maneuver costs 1. Level 1 is free; each Role rank brings a Maneuver rank. *(S01, S07, S13 read of spending-karma.md)* -> spending-karma.md: one clause, "a new Role or Maneuver costs 1." See 23 for a conflicting note.
- **[RULED] PLAYTEST RULE "Use it to grow it."** Each session ONE optional purchase: something NEW, or Level (Level always takes this slot). Beyond it, any number of paid improvements to Roles and Maneuvers USED this session. A new Maneuver counts as used if it would have applied to a roll actually made (bare Role or unarguable Synergy). "Used" means a roll that mattered. Fiction-only use defaults to the new-purchase slot. Raising an UNUSED existing score takes the slot. *(S07, S08, S09)* Lee, S11: growth "feels meaningful, probably better... about right."
- **[RULED] Outside the limit:** Hook rank-ups; Extreme-earmarked advances; in-play Enchantment (an item with its own costs); carry cap = cost of the next Level. *(S01, S03, S07)*
- **[RULED] Maneuver limit is a COUNT.** A Role holds no more Maneuvers than its rank (each Maneuver's rank capped by the Role). *(S11; notes)* -> maneuvers.md: "count, not ranks."
- **[RULED] Every Role rank, however bought, carries its Maneuver rank.** *(S05)* -> say so; sheet checklist.
- **[RULED] Stack and rename.** A new rank may fold into an existing Maneuver and broaden its name (Mediation -> Diplomacy 2), with GM consent. *(S05)* -> maneuvers.md.
- **[RULED] "Time value of money."** A Role's free Maneuver rank is worth most on the best Maneuver; pay for cheap ones separately. Choosing the character over the sheet is a real trade. Book text wanted, beside "It's Not About the Build." *(S11)*
- **[RULED] New Roles are always 1K**; opportunity cost, not a rule, steers away from thematically odd Roles. *(S11)*
- **[RULED] Karma accumulation.** Earn any amount in a session; the cap applies only to what carries. Early sessions may relax spending. Banked Karma as an emergency Succeed is good tension. *(S01, S09)*
- **[RULED] Double-length sessions:** two improvements, one attendance Karma. Test: a sleep break plus two distinct problem-sets, not hours. *(S04, S05)* Attendance is credited at session start (or at a mid-story break), not again at the end. *(S07)*
- **[RULED] Good Fun Karma** goes to moments other players would retell. [UNCLEAR] the solo reading (the moment the GM or player would retell). *(S02, S08; notes)*
- **[OPEN] Karma supply.** About 3.6 per session played (S1-S7). "Working well -- maybe too well?" The GM may pay Tokens instead of Karma as a dial. *(S04, S07)*
- **[OPEN] Advancement timing in continuous play.** Rules key to the session; fiction may run on without downtime. *(Add.)*
- **[RULED] Recovery Trope** can be pure framing: early purchases explained as skills she always had. *(S01)* The planned page's open questions (deadline; flashback vs forward) stand.

## 8. Harm, Down, recovery, death

- **[RULED] Harm counts against EL** (harm.md) -- Complication and Injury alike penalize any roll they sensibly apply to; they differ only in how they clear. Hindrances reduce EL but don't count toward Down. *(S06 Pt2; notes)* -> harm.md beside the type definitions.
- **[RULED] Down asymmetry is intentional.** Down when Harm exceeds Level; stay Down until it drops below. *(S01; notes)* -> feeling-down.md, one sentence.
- **[RULED] Harm stays undifferentiated until the recovery roll.** Don't pre-label Injury. A Veil is usually Hindrance/Complication; a fist usually Complication; a knife is just Harm until the roll. Players don't declare Harm type; the GM may as a plot device. *(S11; notes)* [OPEN] write down the split procedure (played: the recovery roll's result is the Complication portion that clears; the rest stays Injury).
- **[RULED] Illusions deal Complications.** Believe you're dead and you pass out. *(S10, S11)*
- **[RULED] Post-fight recovery** is offered after a fight or with medical care; Armor 1 grants a second one; a superficial cut clears once properly dressed. *(S11)*
- **[RULED -- working] Death threshold.** Remaining Injury greater than Level after the post-combat recovery roll = dead. For a spirit: dispersed, reforming in some nether, a spiritual coma possibly for centuries. GM keeps wriggle-room. [OPEN] confirm for PCs. *(S03)*
- **[UNCLEAR] Recovery when Harm exceeds Level.** Base Level can never beat an Injury total above it, so self-recovery is impossible without help. Intended? Does Harm's EL penalty apply to recovery rolls? *(S03)*
- **[RULED] Sickness as ongoing opposition, not a clock.** The illness rolls against the patient at set times (Ivro: 3d each dawn under strain); he resists with Level + Boosts; a loss = Injury by the margin; a tie or win = no new harm. "That's a dramatic tension decision." *(S10, S13)*
- **[RULED] Chronic illness is a permanent Hindrance on health rolls**; only supernatural intervention clears it; remission possible; a won dawn heals at most 1 Injury per day. *(S11)*
- **[MISSING] Spirit recovery rate.** Played: about 1 per day undisturbed, faster if it feeds. *(S03)*
- **[RULED] Disrupted manifestations are banished.** A manifest spirit whose form is violently disrupted is Down or Staggered and ejected to the far Dreamlands until summoned back by ritual or anchor, once recovered. *(S03)*
- **[IN BOOK] A Down spirit recovers like anyone** (recovery.md): it rolls its Level against its CURRENT Harm, as dice. One hit hard may need an Extreme to recover at all; it creeps back sooner or later, not always 1 a day. (The GM's first "1 per dawn" was retired.) *(S14, Lee)* -> conjuror.md, at "merely incapacitated until they can recover": point to recovery.md. Answers the "spirit recovery rate" question.
- **[IN BOOK] Care clears a Complication on any success** (recovery.md) -- a cough caught early, cleared in one treatment. *(S14)*

## 9. Healing, medicine, privation, fatigue

- **[RULED] Medicine is Gear.** Made as a Persistent Wager: a banked Boost against what it treats. Stores indefinitely; can spoil or be lost; a poor roll at use can read as "lost efficacy." Making = Apothecary; treating = Healer. *(S06 Pt2; notes)*
- **[RULED] Medicine as a pool.** A batch's effect is a pool of Boost the healer doles out in doses (at least 1 point per dose). Guidance kept: cap a single dose at the administering hand's relevant rank. Potency may set dose count. Batch sizes stay real ("Apothecary isn't Alchemy"). *(S06 Pt2, S07)*
- **[RULED] Treatment as Gear.** A good binding or splint is a standing Boost to recovery while it holds, with upkeep. Persuasion to follow a regimen can be kept as a standing Boost to the patient's discipline. *(S07)*
- **[RULED] Care is an Apothecary roll whose effect becomes a Boost on the patient's recovery,** capped at the healer's Healer rank (the Persistent wager cap). Mundane gear can add +1. *(S11, S13)*
- **[RULED] A spiritual residue in a wound can be contested by mundane care** (warmth and honest tending, as attrition against the residue's rating). *(S12)*
- **[RULED] Privation works like fatigue.** It accumulates; its real bite is that it PREVENTS recovery. Proper food or a tonic mainly ALLOWS the blocked recovery roll ("cough syrup for the scurvy -- and go eat some greens"). No rule split; GM methodology. *(S07)*
- **[RULED] Fatigue is overloading.** No dedicated rule: the GM warns, then raises Difficulty as the character keeps pushing; failures spiral into Harm. "The GM's opinion is the rule." Applies to the improvisation HOLD roll when a casting has two. *(S06 Pt2, S08; notes)* -> gm-rules.md; say which roll fatigue applies to.
- **[RULED] Sleep debt.** No flat paydown. Real sleep allows a standard recovery roll against the debt with situational modifiers; nightmares and hauntings OPPOSE the sleep itself; the GM may keep some debt in the narrative. "When unsure, allow the roll and modify it." *(S08)*
- **[RULED] A healer's honest prognosis can split one case into layers** with different mechanics (bone knit short = done; contracture = accumulated progress, no rolls; learned fear = tonight's contest). *(S13)*
- **[RULED] Cooking** is base Level until a Naturalist rank; an expert's guidance is a passed, rolled Boost. *(S06 Pt2)*
- **[RULED] See the Root (Trick).** Where a problem has a living or spiritual trace, Second Sight Boosts the analysis or diagnosis; against the mundane, psychometry at best. Diagnosis and treatment are separate rolls. *(S05, S12, S13)* Good model of a Trick naming its mechanism (tricks.md).

## 10. Spellcraft: known, bound, unbound

- **[RULED] Repertoire.** A Spellweaver knows one spell per Spellweaver Role rank, free, separate from Maneuvers. A Maneuver rank may be another spell, the same one (foolish), or anything else. Only bound spells cast at speed. *(S01; notes)* -> spellcraft.md: the known/bound distinction (spells.md still says "Spells are learned Maneuvers").
- **[RULED] A known spell adds no EL** ("a sword, not the skill"); it needs no book to bind. *(S01)*
- **[RULED] A bound rank can't cast or counter other spells** but still counts for knowledge rolls. *(S01)*
- **[RULED] Unbound Spellweaver ranks apply to everything in the Role.** An unbound known spell needs a full ritual, and all otherwise-unbound skill counts toward it. *(S05; supersedes the S04 sheet's "bare Level")*
- **[RULED] "Everything costs."** Binding a spell pulls its rank out of everything else in the Role -- Artifice and counterspelling drop too. *(S08)* -> spellcraft.md, where binding is explained.
- **[RULED] Swapping a binding** = release the bound rank (fast-cast or let it dissipate), then a full ritual. Never mid-fight. *(S01)*
- **[RULED] Known spells from other Roles.** A Maneuver rank in a non-casting Role can be a known spell (Cari: Loremaster -> Scry, Light). It works like a Spellweaver's free known spell: castable with Spellweaving, unbound -> full ritual, bindable. NO Synergy from the knowing Role. The Loremaster ROLE rank never applies to spells except for questions about them (maybe research). The MANEUVER rank adds only when countering THAT spell, and when answering questions about it. *(S01, S07, Add.)*
- **[RULED] Fume stays unbound** -- data point: at Spellweaver 4 the player kept a flexible rank over binding a fourth spell. "The lure of unbound-rank flexibility is doing its job." *(S08)*
- **[RULED] A spell embedded in an item lets the caster free the bound rank.** "That's slightly huge." *(S14)* See 17.

## 11. Spellcraft: casting, improvisation, release

- **[RULED] Improvised casting is TWO rolls, always.** (1) HOLD: a free-action resistance roll against the spell destabilizing, vs DL = 1 per added useful Trait (limiting Traits subtract); pass/fail; fail = the spell is lost until rebound. Hold EL = the spell's EL + Spell Improvisation. (2) CAST at full power; the hold doesn't reduce its effect. "I don't want to make it more effective by making it less effective." *(S04, S06 Pt2, S10, S11; notes)* -> shaping-effects.md: "then roll the cast normally."
- **[RULED] Required Traits count toward Difficulty.** Scry as written is DL5; playtest: Guidable optional (+1), so DL4 base. *(S11; notes)* -> the Difficult-spell text.
- **[RULED] Holding is not casting.** When the hold succeeds, the "casting" roll is the work itself (Scry: the seeking, at a GM-set DL). Scrying your own location is Astral Projection. *(S11)*
- **[RULED] Gathering mana** = a Spellweaver Boost on free/unbound ranks, opposed by the place. It goes on the hold or the cast, not both -- ask first; normally the cast. A poor source gives nothing (a dung fire tied). *(S06 Pt2, S13; notes)* [PROPOSAL @@*] An object soaked in a deed (Olwin's cudgel) as a gather source could lower the place's opposition or add a die when the spell matches the deed. *(S10)*
- **[PROPOSAL @@*] Bound ranks feed Boosts toward their own spell** (Stone Shape gather). *(S11)*
- **[RULED] Release.** A Release is a free action at a guaranteed value = bound ranks, no new roll; it UNBINDS (spends the binding, loses the spell until rebound) and dismisses outstanding effects. Aiming (target, Manifestation) is free description. *(S01, S11)*
- **[RULED] "Fast or shaped, not both."** An Improvised Release costs the action, keeps its guaranteed value, needs the hold roll vs the added Difficulty; a failed hold wastes it (effect 0). *(S01)*
- **[RULED] Dismissing is not Releasing.** Dismissing a standing effect gives nothing back (GM may require a roll to end it when it matters). A caster can always let go of her own Persistent spell; a binding is untouched. *(S09, S11; notes)* -> spellcraft.md beside Persistent.
- **[RULED] Moving a Persistent, Guidable effect is free; ATTACKING with it costs an action.** *(S11; notes)*
- **[RULED] A running Persistent effect can be used for new rolls** at the recast EL (traits.md: Persistent "might hold the spell active so that the caster can use it for new rolls"). S14: a Guidable Fax thawed frozen ground. *(S14)*
- **[RULED] Helping someone see through your own Veil** is a Spellcrafter Boost, same dice as casting, passed to them; they roll against the Veil. *(S06 Pt2)*
- **[UNCLEAR, resolved] "Going over" on a recast.** See 3: over EL is a zero. *(S08 -> S09)*
- **[RULED] No hold is needed when the use is within the spell's stated scope** (illusory harm is the Veil's own example). *(S10)*
- **[OPEN] Selective: +1 or -1?** A Selective Fax ("burns only dragons") used as a harmless light was counted useful (+1). Which way does Selective count when it makes a spell safer rather than stronger? *(S12)* -> traits.md.
- **[RULED] Reactive cuts both ways** -- an enhancement on a Ward (+1 Difficulty), a limitation on an attack or creature (-1). The useful-vs-limiting rule handles it by context. *(S01)* -> one example line.
- **[UNCOMMITTED] CHANNELLED** (Lee, S13: "good, I like that"). Casting THROUGH a bound spirit at any distance: the bond is the anchor, the spirit is the place; +1 DL like a Trait. Extended to perception in S14: channelling her own Sight down the bond. *(S13, S14)* -> traits.md candidate; conjuring.md.
- **[UNCOMMITTED] SUSPENDABLE and VARIABLE** (proposed for study). Suspendable: duration runs on, but the effect can be switched off and on. Variable: the effect can be turned down. [PROPOSAL @@*] watch Suspendable against Persistent's "cannot hold an effect against someone else's roll." *(S13)*

## 12. Spellcraft: Persistent, duration, the Dawn

- **[RULED] Persistent duration.** The scene is a convenience rule of thumb; the official duration is "until the GM says so" -- until there's a reason it shouldn't, or it becomes irrelevant. "The GM owns the candle-snuffer." The caster can tweak it within reason (brightness, torch-to-lantern). *(S02, S03, S06 Pt2; notes)*
- **[RULED] THE DAWN RULE (complete).** A Persistent casting resists each dawn: its STRENGTH vs N dice, N = its age in days. A LOSS dims it by the margin (to 0 = gone); a TIE holds; an EXTREME FAILURE on the casting's own roll SNUFFS it; an EXTREME SUCCESS resets its age to 1 [Lee, S13]. The GM may choose snuff or dim per casting from the fiction ("it's magic -- it doesn't even have to be consistent"). "Weeks is VERY unlikely." A dimmed casting tests at its new strength. *(S09, S10, S11, S13)* -> spellcraft.md beside Persistent: write the whole rule down.
- **[RULED] Framework strength.** When the casting roll produces the effect itself (a light, a ward, a Boost), that roll is the strength the Dawn tests. A separate FRAMEWORK roll, at the casting EL, is needed only when the casting roll is spent on something else (Scry's seeking). If it fails, spend a Token. *(S12)* -> spells.md under Persistent and Difficult spells.
- **[RULED] Persistent is a deterrent, not a guard.** It cannot hold an effect against someone else's roll (traits.md). If tampering is suspected, the caster may send a spirit for an improvised remote opposition roll. *(S13)*
- **[RULED] Permanence is bought.** Karma makes a spell permanent (Enchantment: spells.md, "costs similar to Role and Maneuver advancement"); a point spent on an entity creates a permanent anchor line (beyond.md). Permanent castings skip the Dawn. In-play Enchantment is outside the improvement limit. *(S03)*
- **[RULED] "The world tends to put things back."** When a spell ends, the world restores what it changed. *(S05)* [PROPOSAL @@*] corollaries: matter that can't resume its shape where it sits crumbles; only the spell's change reverts; permanence is bought; a place's genius that ACCEPTS the new shape may let it stay.
- **[RULED] DAWN: an Extreme FAILURE on the AGE dice** works like an Extreme success on the casting's own roll -- the casting's age resets to 1. *(S14, Lee: "maybe the functional result is the same?")* -> spellcraft.md, the Dawn rule.
- **[RULED] Spent castings go when their purpose does.** A Persistent wager made for one casting fades with its scene; lights and eyes set for a job are dismissed when the job is done -- "one less thing to keep track of." *(S14, Lee)*

## 13. Spellcraft: individual spells and Traits

- **[RULED] Stone Shape.** Reshaped stone REVERTS when the spell ends (in its own shape, where it lies); MOVED stone stays. It reshapes; it does not fling -- can't make stones fly or really roll; can morph stones together, draw a tongue of stone across the ground, and separate it into a shape. Duration "while she focuses"; touch not required; each new use is a recast. A cairn stacked from moved stones needs no spell. *(S05, S08, S09)* [MISSING] "within range" is undefined (twenty paces in plain sight played as fine). -> spells.md Stone Shape entry.
- **[IN BOOK] Phantasmal Veil.** A glamour; only Complications; the target doesn't know until they vanish. A WILLING target needs no roll (used as a translator: a forge's sounds shaped into a spirit's words). *(S10, S13)*
- **[RULED] Scry.** Required Traits per 11. Sympathy lowers seeking DLs (the dead woman's own mirror: -2) @@*. *(S11)*
- **[IN BOOK] Tanglebones** (Required Insidious). Metaphysics (Lee): a conduit that grants mindless spirit energy a free Manifestation channelled into hindering movement; no compulsion. The source flavours it AND binds it: Entangle (physical) can be hacked free (a legitimate, Hindered action; allies can Assist); Grasping Ghosts answers to Wards and spirit-lore; nerve-borne Tanglebones is the Insidious one. *(S04)*
- **[IN BOOK] Light** is a known spell commonly taught to apprentices ("it can't burn down the house"). *(S08)*
- **[RULED] Fax Iacta as a raking light** is a Spellweaving Boost to reading a damaged text. *(S12)*
- **[RULED] The Scry mirror can be TURNED** to look in other directions from the Eye; the image may be reversed. *(S14, Lee)* -> beyond.md (Scry).
- **[RULED] Veil on the senses.** A glamour can hide a sensation as well as add one (pain masked for surgery); a willing target needs no roll to be affected, but the cast's effect must beat the sensation's intensity. *(S14)* -> spells.md (Phantasmal Veil) example.

## 14. Conjuring: the Sight, Wards, Rebukes

- **[UNCLEAR] Opening the Third Eye** (conjuror.md: a full action and a DL0 roll). Played: roll only under pressure (combat, haste, a hostile spirit present). *(S01)*
- **[MISSING] Psychometry.** Reading emotional residue on objects; Aura Reading is named but not defined. [PROPOSAL @@*] auras cling to objects handled with strong feeling, readable at DL by age and intensity. *(S01)*
- **[RULED] It's the Lore, not the rock.** Material salt (or iron, silver) does nothing without attention and intent. A drawn circle is specific and holds; a circle sewn into a garment works only while invoked. *(S01)* -> conjuror.md, Abjuration.
- **[RULED] Keyed Wards are Wagers.** A generic Ward works on whatever it affects. A Ward Against X is a Dedicated wager: dice set aside count as automatic successes only against X, capped at the relevant Role rank. Being wrong costs naturally (wasted dice). *(S03)*
- **[RULED] Wards generally get Area free**; Persistent and Reactive as Traits. A Ward resists at its rolled value. A present caster may roll a Boost into a standing Ward, but then whatever tears at it can reach her. *(S01, S04)* -> conjuror.md: which modifiers come free with Wards.
- **[RULED] A caster's own Ward doesn't fight her own spells** -- a Ward is a filter, not a wall, and its maker sets the filter. *(S04)*
- **[UNCLEAR] Stacking wagered Wards** -- the Role-rank cap per Ward, or in total? Played per Ward. *(S04)*
- **[UNCOMMITTED] A Rebuke can travel a spirit's own hook-line.** "A spirit that hooks you has given you its address." *(S03)*
- **[RULED] Boost then Ward, as separate rolls** (a blood offering rolled as a Boost, then fed in). *(S04)*
- **[RULED] Location "Activation" instead of clocks.** A sleeping fey house starts at DL0; Sight successes bank as Activation dice; the house rolls Activation against later perception and navigation, and when it wins it wakes and can LIE (false visions). Lulling (Conjuror, a Performer lullaby, offerings) subtracts. *(S03)*
- **[ADOPTED] Lucid dreaming.** A visited sleeper rolls Conjuror (or base Level) vs the dream's hold; success = lucid. Candidate Maneuver: Lucid Dreaming. *(S04)*
- **[UNCLEAR] A True Name given in play** (before Karma). Played: a temporary +2 Boost to workings on that spirit; the Maneuver buyable at session end; the gift is a debt the giver prices. *(S04)*
- **[IN BOOK] Ward vs Rebuke in practice.** Pushing a spirit's influence off the lamps was a WARD (defence); "Sleep, and begone" was a REBUKE (offence, conjuror.md's default for a clash). A Rebuke that takes the spirit past its Level puts it Down: no grip on anything physical, in reach of a finisher. *(S14)*
- **[RULED] Astral DISPLAY.** Projected, a caster is unseen and intangible by default but, like any spirit, has a little Display: her Conjuror ranks let her will herself seen and heard. *(S14, Lee)* -> conjuring.md, beside spirit Display.

## 15. Spirits, familiars and the Accords

- **[RULED] Distance is irrelevant in the Borderlands** (Lee canon): spirits are thought and feeling, not space and time. No range limit on a bound spirit's mindspeech. *(S13)* -> conjuring.md (conjuror.md already calls range "purely conceptual" in spiritual conflict).
- **[RULED] Every spirit has Display and Manifestation built in** at base Role rank unless excluded; Possession needs the Maneuver. *(S08)* -> conjuring.md reads as if both need the Maneuver.
- **[RULED] A familiar's points model.** Points or Karma a PC spends on a spirit's True Name become points on the spirit's own sheet, spent by negotiation. The first True Name rank establishes the familiar (base Level 1 free). Its identity is its Role (Ember Sprite); no Overchannelling ("he IS fire"). Growth rank by rank under the Level ceiling. Its limits are learned, not built in. Spirits can also grow outside her points (Agreements; ranks of Fey or Demon). *(Add.)* -> conjuror.md: rewrite "True Name ranks can raise the base Level."
- **[RULED] True Name bonus on her own rolls** applies when compelling, recalling, reaching through a barrier, or DEFENDING the spirit -- "more like tapping a pre-existing Boost." Not a double-dip. *(Add.)* [OPEN] the double payout vs Beast Handler, to revisit. *(S08)*
- **[RULED] Spirits feed on freely given emotion** (let-go fear eaten like food). *(S13)*
- **[OPEN] A favour a spirit DESIRES isn't a favour.** Played: the debt waived where the spirit plainly wanted the thing. *(S13)*
- **[OPEN] Query the Candle at whose rating?** Played at the spirit's own knowledge (Asher's Level). *(S08)*
- **[PROPOSAL @@*] A spirit in a foreign flame or metal** rolls its EL against opposition; riding its PC's own costs nothing; Manifesting with no fire present at a raised DL. *(S11)*
- **[RULED] The Accords bind MINDS only.** Spells are mechanistic and sit outside the Accords; lending mindless energy a Manifestation owes nothing. Exception: a spell can accidentally spawn a mind, which is then under the Accords. *(S04)*
- **[RULED] Intention governs the Accords.** A gift accepted implies a debt among those who know them, unless excluded. Trickery weakens a debt, as compulsion weakens a Contract. Fey inflate tiny debts. *(S08)*
- **[RULED] "Met as paid"** -- two fingers on an open palm: "we meet square; nothing owed either way." The in-world answer to whether courtesy creates debt. *(S08)*
- **[RULED] The Merchanter's Rule.** In spirit commerce, value is worth to the recipient, not cost to the giver. Some offerings also matter for how precious they are to the giver. *(S01)*
- **[RULED] Guest-right.** Parties to an Agreement can't directly harm each other (an Agreement might let a host dine on a willing guest, tit for tat). *(S03)* A guest-gift grants standing guest-right both ways rather than a debt ("It is not a debt. It is a door.") -- [OPEN] to confirm as general. *(S09)*
- **[UNCLEAR] Is spoken thanks a gift that creates a debt?** Played: both, so neither. *(S03)*
- **[RULED] Over-giving creates counter-debt** (Min); a token payment concludes it. *(S05)*
- **[RULED] Escape clauses** ("barring pressing duty"): the parties may name a judge; absent that, fey read literally and ask. *(S03)*
- **[RULED] Renegotiation as clarification** carries no price when it serves the original intent; price scales with how far the new terms stray. Unclear terms are interpreted by the spirits per their Hooks. *(S06)*
- **[RULED] Faeries cannot lie** but can "talk round"; a fey house's glamour can still deceive perception (Activation). *(S08, S14)*
- **[UNCLEAR] adepts.md: Adept EL "as much of their base Level."** Only the Marcus example shows it means Level capped at rank. One clause would fix it. *(Add.)*
- **[RULED] What a demon is** (Averond): almost any fire spirit is commonly called one; true Demons are spirits of pure emotion (even "true, pure love"); any "angel" of Rikitak; Rikitak is final authority. *(S01)* -> setting overview.
- **[RULED] Offerings vs debts.** An easy, sincere gift (bread from her hand) is an OFFERING -- it builds the bond -- but pays no Accords debt; that wants a real sacrifice. "A gift of love, not blood... more bonding than bondage." *(S14, Lee)* -> conjuring.md, the Accords.

## 16. Folk charms and materials

- **[RULED] Folk charms.** Salt for the dead, silver for demons (the Death/demonic corruption), iron for fey. Old magic usable by anyone with intent and commitment; usually enough for a small spirit. A threshold works against any spirit if you have a right to it and believe it. Garlic is no better than roses, but neither is useless. Vulnerability tracks how far a being has leaned into its nature. *(S03, S08)* -> strong sidebar candidate.
- **[RULED] Iron vs fey without a practitioner.** Anyone holding iron and praying rolls base Level; on a success the iron's value (by quantity and arrangement) adds as automatic successes; it never helps someone who rolls none. Passive iron can be slipped round by lure or glamour; iron worked into a Ward adds fully. [PROPOSAL @@*] this is the existing Protected trait keyed to the fey's Vulnerable (iron). *(S03)*
- **[RULED] Iron and steel (Lee, 2026-10-22; reconciles S01 and S13).** Both are true; neither is deterministic. Iron is rare, valuable and sacred -- "more like silver than platinum," sacred the way a holy book commonly is: people cringe if you toss one or start pulling pages, and they notice, frown and maybe talk, but there's no iron gestapo, no pitchforks and torches. An iron-bound box or an iron-shod staff signals opulence and prestige, or something ominous, but it happens. An adventurer with a STEEL sword basically has a magic item, even unenchanted: it will have a name, even if it didn't. *(S01, S13, 2026-10-22)* -> setting overview; fix the Saltwind doc's line; settle Carterian/Carterion spelling.

## 17. Items and crafting

- **[RULED] Fiction sets the time and resources.** "You don't forge a katana in camp after dinner." No tie to downtime unless players choose to work on projects then. *(Add.; supersedes item-creation.md's "one roll per session")*
- **[RULED] Only the Traits the maker could add.** Traits are not skill: an item can't grant ranks without magic, and then it's a table ruling that always costs Karma. *(Add.)*
- **[RULED] The crafting Role isn't named by the rule** (Tinker, or Spellweaver Artifice, etc., by build, with GM approval). *(Add.; notes)*
- **[RULED] Lasting Work is STANDARD ATTRITION, "like any fight" (confirmed 2026-10-22).** The crafter's Harm counts against her EL; her effect wears the item's opposition down. "A setback doesn't mean you lose, but it really makes it more likely that you'll need to just scrap the work and start over." *(S14)* Lee, 2026-10-22: "never gets easier" was an attempt to keep every PC from churning out toys; it isn't needed once time and the Gear rule that STUFF BREAKS are accounted for. Making a sword Unbreakable is another Trait, driving the difficulty up -- and it still doesn't keep it from going overboard into the bay. -> item-creation.md: REMOVE "the opposition never gets easier" and its follow-on lines.
- **[RULED] Finishing.** A NEW item must have its resistance EL reduced to ZERO. When ADDING Traits to an existing item, "you can just take it to Down" / the opposition worn below the item's previous rank. *(S06 Pt2, S14)* [OPEN] what "Down" means for an item -- see 24.
- **[RULED] Failure.** Down = the project fails (time and materials gone; when improving, the ITEM is destroyed). Ceding is always open: lose the investment, keep the item. *(item-creation.md draft)*
- **[RULED] Tokens and Karma at the bench.** No Luck Tokens; Karma may stand in for a Token. Extra Effort per dice.md. *(item-creation.md draft; S14)*
- **[RULED] A spell in an item is a Trait.** The caster rolls as usual with her own EL (the item adds none). A failed cast fries it; Gear rules apply (disarmed, destroyed, stolen). An artificer can carry several, freeing bound ranks -- intended: "power increased significantly at the cost of dependence on the item." An item that itself carries RANKS needs real Karma and uses the Assist rule. *(Add.)*
- **[RULED] Required Traits ride along.** An embedded spell brings its spells.md "Required" Traits with it. *(S14)*
- **[RULED] Only baked Traits.** "An item cannot implement any Trait not built into it. In use, the caster still has to roll as usual, but can ONLY Improvise Traits baked into the item." *(S14)*
- **[RULED] Rating by rank -- ALL items, the common scale (Lee, 2026-10-22).** One scale for everything, no special exceptions "without a REALLY good reason." Each Trait in an item is a rank (for a spell item, the spell itself is rank 1); each Trait in the item (Required or baked) adds a rank; the RATING is what a Maneuver of that rank costs: 1, 2, 4, 7, 11, 16. Veil + Subtle + Area + Guidable + Persistent = rank 5 = rating 11. Fax + Persistent + Guidable = rank 3 = rating 4. Scry (five Required) = rank 6 = rating 16. "Minor items really easy, more powerful items a lot harder." Two- and three-Trait items are relatively minor but "still pretty damned handy": they FEEL like magic items, and still make you bump into their limits and want the legendary Thing-O-Power. Beyond three Traits the cost ramps drastically -- a real master, maybe with "a cabal of competent assistants passing Boosts." *(S14; 2026-10-22, supersedes the S06 triangular 1, 3, 6, 10 scale)* -> item-creation.md: replace the Level-progression pot with this.
- **[RULED] Rating-1 items are right for DISPOSABLES**; fragility (breaks on any failed cast; Gear rules) is largely the point of durable spell items. *(S14)*
- **[RULED] Pinned Work for disposables** (item-creation.md draft): a Wager on the Residual model, pinned by encumbering a Token; the effect is fixed and does not roll; trigger, effect and target declared; "the declaration is the item"; anyone can supply the Token knowingly. Answers "is a one-shot item a scroll?" for disposables. *(S06 Pt2, S14)* [OPEN] whether Pinned Work survives as its own mechanic beside "disposables are Boosts under the Gear rules." *(Add.)*
- **[RULED] Harm from crafting** -- probably no special rule: loss of nerve as a Hindrance, Complication, Injury or even a Hook, per the fiction. *(Add.)*
- **[UNCLEAR] Spending The Pot examples** use three different cost readings. Partly answered for spell items by "rating by rank." *(Add.)*
- **[OPEN] Releasing a spell from a durable item** -- does it spend the Trait and leave a plain stick? *(Add.)*
- **[OPEN] Whether Conjuror, Tinker and Spellweaver crafting pay in their own currencies** (Soulburn, fatigue, control). *(item-creation.md draft)*
- **[PROPOSAL @@*] Odds check (simulated, mutual attrition; Down at Harm > 5).** Artifice 8: rating 4 near-certain in ~3 evenings; 7 ~72%; 11 ~6%. Artifice 9: 7 ~87%; 11 ~16%. *(S14)*
- **[ADOPTED, wording open] The hag-stone ("little door").** Anyone looking through gets a narrow Second Sight glimpse at base Level; for the Sighted, a small Boost that pierces glamour or disguise. *(S06 Pt2)*

## 18. Companions, followers, apprentices

- **[RULED] Companions across Roles.** Beast Handler and Conjuror cover different parts of continuous rules: Maneuver points = training (Handler) or relationship (Conjuror); both may take extra Karma. The handler spends Karma on the animal's sheet and can act through it; the spirit spends its own points and rolls its own EL. Companion caps: can't outlevel the PC; can't be taught above the teacher. *(Add.)*
- **[RULED] Followers are Gear.** Points spent on a follower bind loyalty, availability and capability "for at least that many points' worth." Unpaid, he stays the GM's. The host Role limits other Maneuvers there (Loremaster for teaching, Performer for leading; a custom Mentor/Commander Role when it matters). *(Add.)*
- **[RULED] Not a puppet: two pools.** A follower grows on his own too; the more capable he is apart from her points, the less control she has, but the more he can do if he agrees. "No points devoted is a great way to have a student turn into a nemesis later." *(Add.)*
- **[RULED] Release and invested points.** A follower with a real Role rank can be set up on his own; invested points don't go away, and are worth more the less often he's called on. *(Add.)*
- **[OPEN] Companion Training timing and the apprentice model** in continuous play. *(S08, Add.)*
- **[RULED] The apprenticeship "Deal" is mortal only, for now.** *(S08)*

## 19. NPCs and opposition

- **[RULED] NPC frames: budgets, quick-start style.** A recurring NPC gets a frame when their numbers first matter: Level, defining Roles and Maneuvers, Hooks, companions and a Karma BUDGET. Unspent budget can be declared retroactively when the fiction calls for it, within the usual limits, never contradicting play; log every declaration. Size by place in the world and story, not by the PC. *(S09 frames file)*
- **[RULED] An NPC takes undifferentiated Harm** unless the GM designates the type as a plot device; a later recovery roll decides Complication vs Injury. The GM may Token NPC rolls. *(notes)*
- **[RULED] No invented backlash.** A fumble needs a roll that could legally have been made. *(S11)*
- **[MISSING] Rating opposition on the fly.** No guidance for a ghola, a fey house, a clerk's denial. [PROPOSAL @@*] a "typical opposition by threat" sidebar; and a short table of Difficulties for magic (Ward size, fuel, hostile ground). *(S01-S04 GM notes)*
- **[MISSING] DL anchors** for common tasks (0 trivial, 1-2 routine, 3-4 hard, 5+ heroic) @@*. *(S01)*

## 20. Scenes, time and downtime

- **[RULED] A scene is one camera shot.** Rapid moves between nearby sites in one continuous sequence are one scene; the GM may break a scene for fairness (a recovery, a time skip) or with a flashback. Scene breaks are a pacing tool. *(S11)*
- **[RULED] Downtime vs the table checkpoint.** Rules keyed to the session (advancement, Companion Training, crafting) and the fiction's opportunity (time to study, train, craft) usually coincide but are separate; nothing yet covers the table stopping while the fiction runs on. *(Add.)* Partly answered for crafting (fiction time).
- **[PROPOSAL @@*] Downtime structure (S14 arc).** Days in blocks, spikes in full; three slots a day; no roll for plain work; a spoiler-free day board. *(S14)*

## 21. GM craft and procedure

- **[RULED] Read the rule, the spell and the Role page before ruling.** The GM's recurring failure mode was reaching for fixed targets and invented shortcuts, and logging "gaps" the book already covered. *(S04-S14)*
- **[RULED] Partitioned NPC knowledge.** A Present line in the ledger for every beat; a who-knows-what table in the GM brief; a sourcing check (saw / was told / rumour / worked out) before an NPC states a fact; NPCs only copy what they've seen. *(S05, S06 Pt2, S08, Add.)*
- **[RULED] Provenance tags survive every summary.** [Lee] and @@* carry through; an untagged line is "the record has it," never "you said." *(Add.)*
- **[RULED] Decide the secret, write it, then describe it.** The truth is set before the roll. *(S04, S13)*
- **[RULED] After any memory break, read the ledger before narrating anything established.** Invent only into true blanks, and mark it @@*. *(S07, S08)*
- **[RULED] An in-fiction retcon beats a table stop** ("exactly the kind of thing an experienced GM would do"). *(S08)*
- **[RULED] Standing kit.** A character keeps her signs of office and personal gear unless play separates her from them. *(S08)*
- **[RULED] Write "if it stands / if Tokened" outcomes** for rolls that matter, deciding the consequence before the player chooses. *(S01-S04 GM notes)*
- **[MISSING] The Bare Oracle** (2d: 2 yes, 1 sign, 0 no) -- written up as its own design note (2026-10-05). Now used sparingly per "oracle drift" (1). [OPEN] weighting; whether players may call it. *(S03-S09, S12)*
- **[MISSING] Clocks.** L1 has none. The engine models most of them already (illness as opposition; Activation). [PROPOSAL @@*] the Purification List could become an opposition roll too. *(S03, S10)*
- **[RULED] Options teach the levers.** The optional rules exist mainly to show GMs where the dials are and how far they turn, so they can improvise something that "feels about right." The book should say so. *(S05)*
- **[PROPOSAL @@*] A one-page GM crib** of "things that always roll / never roll," and a "latent threads" box on a GM sheet. *(S04, S11)*
- **[RULED] Lost canon from another table:** improvise inside the known facts, mark it, let the person who was there correct it. *(S06)*
- **[RULED] Fixing a short pool:** keep the dice already rolled and roll only the missing ones. *(S06 Pt2)*
- **[RULED] Count the days before giving NPCs time words.** *(S10)*
- **[RULED] "Any time you find yourself fabricating a rule, it's probably already there somewhere and just not very clearly applied."** Before inventing a mechanic, find the general rule it's a case of; if the search fails, that's a gap-log entry, not a new rule. *(S14, Lee)* -> GM guide, top of the procedure list.
- **[RULED] The GM's recovery trope.** Found material can be read in fiction but left UNWRITTEN, to be filled later when a scene needs it -- never contradicting what was said. *(S14, Lee: "The recovery trope works for GMs too.")* -> GM guide beside the player's Recovery Trope.
- **[RULED] Show both sets of faces.** Dawn summaries and recovery rolls show the roll AND the opposition's dice ("3 against its 9" read as a flat number). *(S14)*

## 22. Setting rulings with mechanical weight

- **[RULED] Etiquette of the Order of Rikitak.** Never ASK a priest of the Order for help; tell him someone is hurt and he should come; aid requested carries a price ("fire teaches"). *(S02)*
- **[RULED] The Order's Colours** (Lee canon, S13): White Loremaster; Red Flame Adept; Orange Healer (corded sleeves); Yellow Spirit-Keeper; Green incendiary alchemist; Blue Spellweaving; grey and brown lay brothers; Black by special dispensation. Calling vs rank are separate lines. *(S02, S06 Pt2, S13)* -> the Tenets lore doc holds the full text.
- **[RULED] Nobody in Averond can see the future.** Eidolon's "prophecy" is planning, patience and presentation. *(S12)*
- **[RULED] Ganth is a stone's throw from the Monastery.** The region is small and compressed for play: one city, a town, scattered villages between the Mountain and the sea, strewn through woodland. *(S14; strikes the Gazetteer's "three weeks to Ganth")*
- **[PROPOSAL @@*] Secrets as spirit-coin.** Water KEEPS secrets (hoards them); fire CONSUMES them (a secret told to the flame is burned out of the teller). Same coin, opposite appetites. *(S01)*
- **[RULED] The Greater Pantheon behaves like Moorcock's Lords of Law and Chaos** -- occasional appearances, otherwise acting through agents. "Rikitak's house" doesn't mean Rikitak is there. *(notes)*
- **[RULED] CELESTIAL** is the liturgical language of all spirits and of the gods' priesthoods (anything else is an obscure cult's) and the lingua franca of the educated; common folk ask a priest to "speak for me." Other languages are local variants, used or hand-waved by table taste, like coinage; "Common" is common worldwide. *(S14, Lee)* -> setting overview.
- **[RULED] Years are NAMED and NUMBERED** ("the Year of the Shadowed Smith, 4287"). Saints and gods have pictographic RUNES. The Monastery's mountain is MOUNT CUNAE, "the cradle." *(S14, Lee)* -> setting overview; Book of Days.

---

## 23. Conflicts resolved

All four were settled by Lee on 2026-10-22. Kept here as a record; the rulings live in their sections.

1. **Iron** (S01 "merely rare" vs S13 "sacred") -> both true, neither deterministic. See 16.
2. **Advancement cost wording** -> Level costs the NEW value; pretty much everything else the CURRENT value. A standing note that said the reverse was a failed experiment, since dropped [Lee]. See 7.
3. **Item point scales** (S06 triangular vs S14 Maneuver cost) -> the common Maneuver-cost scale for ALL items. See 17.
4. **"The opposition never gets easier"** -> dropped; standard attrition. See 17.

## 24. Open questions index

Quick list of everything still [OPEN] or [UNCLEAR] above, by section.

- 1: excess effect through a destroyed barrier; whose EL opposes when the NPC is "a working."
- 2: Extreme mark per skill or per roll; Token-bought top result as Extreme; Karma for a Token spent against an Extreme; a companion's Extreme; Extreme failure on recovery; impersonal opposition rolling an Extreme.
- 4: when a social roll's resolution is "final" for a Token; solo Token economy.
- 5: retro-wager; a brake on Boost chains.
- 6: Hook budget spent on presence as a general option; Karma-up-to-rank income.
- 7: Good Fun in solo play; Karma supply; advancement timing in continuous play.
- 8: the Harm split procedure; death threshold for PCs; recovery when Harm exceeds Level.
- 11: Selective +1 or -1; Suspendable/Variable.
- 13: Stone Shape range.
- 14: the Third Eye DL0 roll; psychometry; stacking Wards; a True Name given in play.
- 15: adepts.md EL wording; Beast Handler vs True Name payout; desired favours; Query the Candle's rating; guest-gift generality; spoken thanks.
- 17: **what an item's "Level" is for Down** when adding Traits (Lee's 10-19 note: "worn below the item's previous rank" -- confirm); releasing a spell from a durable item; Pinned Work vs Boost-as-Gear; crafting currencies.
- 18: Companion Training timing.
- 19: opposition and DL anchors.
- 21: Bare Oracle weighting; clocks.
- 23: none open.
