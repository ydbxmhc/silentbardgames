# Superheroes in Level One -- DISCUSSION DRAFT

> ## `@@*` NOTHING IN THIS FILE IS CANON
>
> Every rule, mechanic, convention, and definition below was **proposed by Claude**
> during conversation on 2026-08-08. None of it has been reviewed, discussed at
> length, or formally decided by the author.
>
> **Treat all of it as a discussion agenda, not as rules.** The author has noted he
> will likely do things "very similar, but not exactly the same." Expect every item
> to change or be rejected.
>
> Canon requires an explicit, formal decision. When something here is ratified,
> move it out of this file and record it in the Decisions Log at the bottom with a
> date.

*Setting working title: **Vigil**. Actual setting material, once it exists, goes in*
*`setting-notes.md` in this folder -- not here.*

**Status key used below:**

- `PROPOSAL` -- Claude's suggestion, awaiting discussion
- `OBSERVATION` -- an inference drawn from existing published L1 rules; still needs
  confirmation that the inference is correct
- `OPEN QUESTION` -- identified gap, no proposal attached

---

## 1. The name

`OBSERVATION` -- The author selected **Vigil** in conversation. The reasoning
developed jointly:

Superheroes don't have a warrant, which is what makes them vigilantes -- so naming a
setting after the thing they lack points at the hole. *Vigil* names what they have
instead. *Vigilante* is Latin for watchman, someone keeping vigil, so the word already
carries the genre's ambiguity.

Three associations that came up as arguments in favor:

- A vigil is **unappointed**. Nobody assigns one and nobody can revoke it, which
  matches the self-deputized position of a hero. *Warrant* implies granted authority;
  *Vigil* implies assumed authority.
- A vigil is **grief**. You keep vigil over the dead and dying, and hero origins are
  almost uniformly bereavement.
- A vigil is **never won, only kept**.

*Reserved names agreed in the same conversation:*

- **Sanction** -- reserved as a character name. Contronym: both official approval and
  punishment. Suggested fit was a licensed enforcer or registration-program hero.
- **Warrant** -- reserved for a Western setting. Reads too strongly that way, and the
  repo already has Western material.

---

## 2. Powers as Conceits

`PROPOSAL` -- **Powers are Conceits. Skill is Roles.**

Reasoning: flight isn't a competency, it's a fact, and no rating expresses "he can fly"
usefully. But *fighting well while flying* is a Role with a Maneuver.

`OBSERVATION` -- the published rules may already support this. `nonhuman.md` gives a
demon who is **Immune To Fire** as a Conceit, which is functionally a superpower
handled as an unrated Truth. **Needs confirmation that this reading is what the author
intends.**

### 2a. Conceits grant no dice

`PROPOSAL` -- A Conceit provides **narrative permission only**, never a bonus. A hero's
EL comes from Level plus Roles plus Maneuvers like anyone else's.

Argument for it: this is the mechanism that would keep supers from inflating the math.
It splits the two things `mechanical-function.md` says a Role provides, granting the
permission half without the effectiveness half.

**This is the single most load-bearing proposal in the file and the one most worth
arguing about.** If it's wrong, most of what follows needs rework.

### 2b. Where the line falls

`PROPOSAL` -- a suggested test, not a rule:

- Qualitative truth that can't sensibly be rated -> Conceit
- Anything granting a rated bonus -> bought with Karma as a Role or Maneuver

Offered as consistent with the existing guidance that an inborn advantage still costs
something and the only genuinely free thing is a Hook. **Not verified against the
author's intent.**

---

## 3. Paying for Conceits

`PROPOSAL` -- **Conceits are paid for with Hooks rather than Karma**, on the reasoning
that every hero's power comes with a price and the price is what makes them a character.

### Suggested mechanism: reuse Hooks on Credit

`PROPOSAL` -- Hooks on Credit already lets a Hook start above rank 1, granting +1 Karma
per rank above 1 in exchange for a Hook the GM triggers hard and often. The suggestion
is to run it identically with one substitution: **the Conceit replaces the Karma
credit.**

| Power scale | Hook rank | Suggested return |
|---|---|---|
| Minor / narrow Truth | 1 | the Conceit |
| Serious power | 2 | the Conceit instead of +1 Karma |
| Defining, setting-scale power | 3+ | the Conceit instead of +2 Karma |

Arguments offered in favor:

- Reuses existing machinery rather than adding a subsystem.
- The GM lever scales with the power automatically.
- The Level cap does real work: a rank-3 Hook needs Level 3, costing 5K, so heavily
  powered heroes have a build floor and are exceptional-but-unskilled at low Karma.
- The credit debt clause would read, for a hero, as "you cannot simply decline to be
  who you are."

`OBSERVATION` -- **a powered hero built this way is mechanically a Pellan**: big
inherent advantage, credited high-rank Hook, cost paid in complications. If the Pellan
Atavism multi-trigger variance survives testing, it may belong here too. Both are
logged in `CLAUDE.md` as untested.

**Open counter-argument the author may want to weigh:** does the Conceit *fully* replace
the Karma credit, or should some Conceits cost Karma outright? Getting both a power and
extra Karma would be double-dipping, but getting neither may under-reward the Hook.

---

## 4. A suggested difficulty ladder

`PROPOSAL` -- an order of approach for building conversions, working up rather than
down. This is a working aid, not a rules claim.

**Rung 1 -- no Conceits at all.** Hawkeye, Black Widow, the Punisher. Would prove supers
work in unmodified L1.

**Rung 2 -- one clean Conceit.** Daredevil, Invisible Woman, Cyclops.

**Rung 3 -- a small bundle.** Spider-Man, Wolverine, Captain America.

**Rung 4 -- powers that attack the action economy.** Speedsters. Suspected to be a
*timing* problem rather than a power-level one, and the first rung that likely needs a
ruling rather than a build.

**Rung 5 -- the hard case.** Superman. Conceits broad enough that the Hook would have to
carry the character.

---

## 5. Illustrative builds

> **These are demonstrations of the proposals above, not proposed canon characters.**
> If the proposals in sections 2 and 3 change, these change with them. They exist to
> make the argument concrete enough to critique.

### Hawkeye -- illustrating Rung 1

No Conceits at all. A man with a bow.

```
5K   Level 3              3 Luck Tokens
4K   Sniper 3             Bow 3
1K   Warrior 1            Close-Quarters 1

Hook: Just a Guy, Standing Next to Gods 1 (free)

Tricks:
     The Right Shaft -- trick arrows are Gear. The Trick is only
       the habit of already having the correct one nocked, the way
       tricks.md describes a doctor keeping the right compound
       pre-mixed. Free-action Boost when the situation matches
       something he has carried for years.

     Called Shot -- Sniper(Bow) Wagered against a specific small
       target: a hand, a lock, a cable.
```

Sniper 3 costs 4K on top of Level 3's 5K, leaving exactly 1K -- the same squeeze Jayne
hits in `../Accord/firefly-reference.md`.

`PROPOSAL` -- the trick-arrow handling above: **arrows are Gear with traits, and the
Trick is only the declared habit.** Offered to keep it from becoming a free power.

### Daredevil -- illustrating Rung 2

```
Conceits (proposed):
     The World Is Sound -- hearing, smell, touch, and balance far
       past human.
     Blind -- the same Truth from the other side, not a drawback
       bolted on.

5K   Level 3              3 Luck Tokens
2K   Warrior 2            Acrobatic Fighting 2
2K   Athlete 2            Freerunning 2
1K   Loremaster 1         The Law 1

Hook: I Cannot Let It Happen 1 (free)

Tricks:
     Heartbeat -- Loremaster or Performer Boost to detect a lie or
       read fear within earshot. Not telepathy; he hears the pulse.

     The Rooftops -- Athlete(Freerunning) free-action Boost above
       street level.
```

Included partly to demonstrate the 2a claim: neither Conceit grants dice. His EL is
Level plus Warrior plus Athlete.

`OBSERVATION` -- *Loremaster(The Law)* treats a hero's day job as a Role rather than
flavor. Seems consistent with how Roles work, but worth confirming.

---

## 6. Open questions with no proposal attached

- `OPEN QUESTION` **Speedsters and the action economy.** A speedster wants more actions,
  not a bigger EL. Tools that might apply: Multiple Actions, Splitting Actions, free
  actions. Needs a ruling before anyone plays one.
- `OPEN QUESTION` **Gear-based heroes.** Iron Man, Batman's belt. Gear under the assist
  rule, a Conceit, or purchased Roles? A suit that *is* the character's power may need
  different treatment from a utility belt.
- `OPEN QUESTION` **Scale without Level inflation.** How a Superman-tier Conceit
  coexists at a table with a Rung 1 hero. "Conceits grant no dice" would help, but
  "he can move a mountain" still needs a handling convention.
- `OPEN QUESTION` **Do villains build the same way?** And if their Hooks are why they
  lose, should that be stated explicitly?
- `OPEN QUESTION` **Secret identity -- Hook, Conceit, or neither?**

---

## Decisions Log

*Formal rulings by the author. Empty until decisions are actually made. When an item
above is ratified, move it here with a date and delete or amend the proposal.*

| Date | Decision | Supersedes |
|---|---|---|
| -- | *(none yet)* | -- |
