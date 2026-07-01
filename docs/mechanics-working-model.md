# Level One -- Mechanics Working Model (tactical proof-out scratchpad)

**What this is:** the corrected, consolidated understanding of Level One's
resolution and combat economy, built collaboratively while proving out tactical
play. It is a WORKING SCRATCHPAD, not rulebook content, and it reflects the
author's clarifications on top of the current site text (some of which is known
to be unclear or to diverge from intent -- see Open Flags). A fresh session
should be able to read this and have the model correct. ASCII only.

**Goal of the larger task:** prove the system's tactical depth works as intended
using a worked skirmish, agree on the model, THEN write clarification page(s).
Two audiences to serve at once: (1) rules-light players who want simple
roll-and-compare, and (2) tactics-minded players who want deep, realistic
combat -- which the system already supports with NO special rules.

---

## 0. Working assumptions for this discussion
- **Dice:** Simple Pool (optionally Extra Effort) for every example. Other dice
  schemes only reshape the bell curve, not the tactics.
- **Qualitative first.** Actual probability math is a possible later afterthought.
- **Iterative narration is load-bearing:** declare intent -> roll -> interpret
  what the rolls mean in the fiction. Order within an exchange follows the
  story, not a fixed initiative.

---

## 1. Core resolution
- **EL (Effective Level)** = base Level + applicable Role rank(s) + Maneuvers +
  situational boosts - Harm/penalties. Use your best Role if more than one
  applies. If something needs training, only add base Level up to your rank in
  the relevant Role. EL < 1 = impossible until boosted above 0.
- **Rolling (Simple Pool):** roll a pool of dice and count "successes" (odd
  numbers on even/odd dice). A result must be **> 0 and <= your EL**. Rolling
  **over** your EL = total failure, 0 effect (only possible with Extra Effort /
  larger pools).
- **Higher within range = better:** a higher roll is more effect and harder to
  resist/oppose. A 1 succeeds but is weak.
- **Effect = your roll - opposition/resistance.** Ties go to the defender
  (effect must *exceed* to land). If one side fails and the other succeeds, the
  winner gets their whole rolled result.

---

## 2. The EL budget: TWO buckets
Per exchange, your EL is a **budget** you divide into exactly two kinds of thing:
- **Offense** -- points aimed at *specific targets* (an attack is per-target unless modified by or in the fiction).
- **Defense** -- ONE pool, **reusable** all exchange.

That's the whole allocation. "Opposition" and "resistance" are NOT a third
bucket; they are how a pairwise interaction *resolves* (Section 3).

A new round / **exchange** begins when the GM refreshes available EL.

---

## 3. Opposition vs. resistance (emergent) + the TWO-LAYER model
For each attacker/target pair, resolution depends on what each side allocated:

- **Opposition** (both aimed offense at each other): the two **offense** rolls
  are compared; the **difference** goes to the winner as effect. Either side can
  deal effect. (This is the clash of blades / riposte layer.)
- **Resistance** (target did NOT aim offense back, but has allocated defense):
  the attacker's offense rolls against the target's **defense** pool.
  Cancels only -- never deals effect back. Free in the sense that the allocated
  pool is **reusable** and costs no separate turn, BUT it must have been allocated.
- **Both** (loser of an opposed roll *also* has declared defense): roll opposition
  normally; roll resistance separately against any that gets through.
- **No allocation either way** (target aimed no offense at the attacker AND
  allocated no defense): any effect from an attack lands with **no reduction** --
  only Armor / Plot Armor! / Luck Tokens can ameliorate.

**KEY POINT -- both layers can apply in one engaged exchange:**
1. **Layer 1, the contest:** your offense vs their offense -> difference to the
   winner.
2. **Layer 2, defense:** whatever effect leaks through to you is then resisted
   by your *separately allocated* defense pool, rolled fresh.

So to actually harm a foe who both swings and guards, an attacker must clear
**two hurdles: win the contest AND beat the defense roll.** (Layer 1 = the
riposte; Layer 2 = the shield-block / duck-and-cover. They are different
allocations and both apply.)

- **Defense is the reusable universal soak.** One defense allocation rolls fresh
  against *every* point of effect (subject to reasonable applicability in the fiction)
  that reaches you this exchange -- whether it leaked through an opposition contest
  or came from an unengaged attacker.
- **Offense carries threat / deterrence.** Aiming points at a foe incentivizes
 *them* to hold defense back (or eat your effect), taxing their budget. Your attack
  protects you indirectly by making the enemy split too.
- Worked micro-example (author's): EL10, allocate 5 offense + 5 defense vs one
  engaged foe. Offense rolls 2, foe rolls 3 -> foe wins the contest by 1. Your
  5-defense then rolls to resist that 1. If defense >= 1, no harm lands.

---

## 4. Splitting (multiple actions / targets)
- Divide your EL among intended actions; each slice is that action's EL.
  EL8 -> two attacks at EL4. Roll in whatever order serves the story.
- **EL allocated exclusively for defense** is reusable as a free action
  (the swashbuckler vs a room of henchmen). Only applies against attacks you
  *knew were coming*; an undetected attack caps your defense at base Level
  "luck" and may strip Maneuver bonuses (no deliberate dodge, though the GM may
  allow circumstantial bonuses like a shield if it makes sense that it was in the
  way).
- **Cross-Role splits:** plain-language rule = "split your points without
  spending more on any one action than you have skill for." Procedure: a shared
  attention budget (= your top EL); each action capped by its Role's EL; assign
  starting from the LOWEST EL and decrement ALL remaining ELs by each amount
  assigned (so a low Role's points can run out). Example: Performer EL10 +
  Warrior EL20 -> 8 to rally (both -8: Perf 2 / War 12) -> 6 to attack (both -6:
  Perf gone / War 6) -> 6 left to defense. Total spent 20 = top EL.
- **Barrage caveat:** multiple attacks on the SAME target with the SAME ability
  gain very little numeric benefit; better to combine into one roll and shape
  the dice pool. Splitting's value is **tactical flexibility** (different
  targets / abilities / reserving defense), not raw damage.

---

## 5. Wagering (dedicate points for guaranteed/typed effect)
- Remove wagered points from EL before rolling. If the roll succeeds and yields
  **any** effect after opposition/resistance **without** the wagered points,
  the wagered points all count as successes and are added **after** opposition.
  Can't succeed without them -> they're wasted.
- Uses:
  - **Persistent Boost** (lasts the scene): wager points into a named bonus
    addable to later relevant rolls.
  - **Residual effect:** e.g. set someone on fire; the fire rolls on its own
    each exchange while they fight it.
  - **Contingent split:** action B only if A succeeds first (catch the bottle,
    *then* throw it).
  - **Dedicated Effect ("called shot"):** wager points to specify the effect
    (e.g., Injury instead of Complication, even unarmed, with narration). 
    Side effects need their own wagered points.
- **Cap:** never dedicate more points than your **rank** in the relevant Role
  unless the task could be done without the Role at all.
  (See F1 -- split cap may use a different basis.)

---

## 6. Harm, Down, recovery
- **Harm reduces EL directly** -> it shrinks your *budget*, so a wounded fighter
  splits less and rolls lower across the board (built-in death spiral).
- **Three types (+ one):**
  - **Hindrance** -- situational; removed only by story action; does NOT count
    toward Down; healing usually doesn't touch it.
  - **Complication** -- temporary; *any* successful recovery roll clears it;
    counts toward Down. (Fatigue, fear, lost nerve, convincing illusions.)
  - **Injury** -- lasting; daily recovery rolls; counts toward Down.
  - **(Imposed Hook / Temporary Hook)** -- behavioral condition; acts as a Hook,
    grants no Karma.
  - Harm = loss of *agency*, not just physical damage (psychological, social).
- **UNDIFFERENTIATED HARM (clarified in play):** when Harm lands it is just
  *points*; its TYPE (Injury vs Complication vs a mere graze + fright) is NOT
  decided at the moment of the hit. The fiction of the source ("it's an arrow")
  does NOT pre-classify it as Injury. The nature is resolved later, at the
  **post-fight recovery roll** -- the same 2 points might turn out to be a real
  wound, or "it only grazed him and scared him witless." Track raw Harm during
  the fight; differentiate at recovery.
- **Down:** when Injury + Complications **exceeds** base Level -> resistance /
  (GM approved) free actions only until total drops back below Level. 
  (See F3 for "what counts when.") 
  **Staggered** optional variant: keep acting while you have any positive
  EL, with consciousness checks after two fully-failed turns.
- **Recovery:** no recovery mid-fight without Magick. "Second Wind" = a
  Persistent Boost that masks hurts for the scene, not real healing. Daily
  Injury recovery rolls against the Injury total; most Role bonuses don't apply.

---

## 7. Dice pools (assumed Simple Pool here)
- **Simple Pool:** roll EL dice, count odds. Cannot exceed EL (safe).
- **Extra Effort:** add dice beyond EL -> results cluster toward the middle
  (more reliable mid-value) but can now overshoot EL = total fail, and forfeits
  extreme successes.
- **Extreme Results (optional, needs >= 3 dice):** all dice zero = catastrophic
  fail (turn over, aborts other actions, no Luck Token; Karma can downgrade to a
  simple fail). All dice max AND total exactly = EL = extreme success (free Luck
  Token + bonus). More competent characters get extremes *less* often, by design.

---

## 8. Safety valves: Luck Tokens & Armor
- **Luck Tokens** (start *session* with = base Level, cap = Level, get 1/scene
  up to cap): set a roll to best-possible (even after seeing opposition), 
  **Plot Armor!** (equipment takes ALL a hit's damage but is destroyed),
  negate one point of incoming Harm, power a Maneuver/spell, bargain with spirits. 
  GM has a token pool too: max of (#PCs or highest PC Level) +1.
- **One token = ONE use; the uses are mutually exclusive per hit (clarified in
  play).** Spending a token to set your roll to best-possible denies you Plot
  Armor! and the single-point negate on that same hit, and vice versa. This makes
  token choice situationally constrained -- often there is *no* clean option,
  which is by design. (Karth's dilemma vs the arrow: best-possible roll only
  bought -1, a single negate only -1, and Plot Armor! cleared it all but cost the
  robe -- see play log.)
- **Tokens can be spent RETROACTIVELY, always (clarified in play).** You may
  apply a token after seeing the roll, the opposition, or even after an
  unrolled/forgotten allocation has resolved -- the universal "rewind" safety
  valve. (Used to settle Mel's un-rolled Ward at best-possible after the fact.)
  Usually not allowed once the item is agreed as resolved, so it doesn't force
  another player to change actions, or make everyone wait while something gets
  retconned. (Mel's retcon was to rectify mutual GM/Player error.)
- **Armor** reduces/absorbs Harm; can only be tapped this way once/scene. Otherwise
  you need to use a Token and possibly destroy the armor. The whole design ethos is
  *"the point is not to get hit."*

---

## 9. Derived tactical principles (the stuff to "drive home")
- **Two hurdles to harm a competent foe:** win the contest AND beat their
  defense. Self-preserving skilled fighters are brick walls.
- **Defense = reusable universal soak** -> enormously valuable against MANY
  attackers; one allocation guards against the whole mob.
- **Offense = threat/deterrence** -> forces foes to spend defense, taxing them.
  Even if both sides allocate offense only, the system assumes sane avoidance,
  not careless and suicidal behavior. 
  (But see *Kamikaze Blitz* below.)
- **All-in offense = naked:** any foe you didn't engage, with no defense
  allocated, hits you with no roll at all.
- **Harm death-spiral:** every point of Harm shrinks the budget you have to
  fight AND defend with next exchange.
- **Split depth tradeoff:** thin slices = low ELs = few dice = swingy, can't
  crit (< 3 dice), little raw benefit vs one target; the win is hitting multiple
  targets / doing multiple things / reserving defense.
- **Down isn't gone:** a Downed foe can still resist (free), so focus-firing
  removes their offense but not their nuisance value.
- **Offense doubles as defense in opposition; fragility is a resistance-case
  property, not a Down threshold.** A strong-offense / no-defensive-skill PC
  (Karth, Fire EL6) is well-guarded whenever he can OPPOSE -- his margin protects
  him, and a visceral threat (fire to the eyes) forces foes into that contest. He
  is fragile only against what he cannot oppose: unengaged ranged attackers,
  surprise, sneaks (the resistance case, where he has no allocated defense to
  fund). Two identical-on-paper PCs (Karth & Mel, both L2 / Down 3) thus split
  into glass cannon vs. tank purely on defensive skill + armor. The **Kamikaze
  Blitz** is the designed counter -- opting out of opposition collapses this
  offense-as-defense, forcing even a fire-wielder onto a defense pool he lacks.
- The same engine runs the simple game (assign a DL, roll, compare, narrate) and
  the deep one (multi-target offense + reusable defense + wagers + dice shaping)
  with no extra rules -- that duality is the thesis.

### Kamikaze Blitz (opt-out gambit) -- the *see-above* reference
**Premise (already in the rules):** opposition is a *condensation* -- a single
contest standing in for what is really separate attack and defend rolls. The
rules say so; this gambit just takes them at their word and **opts out of the
condensation**, demanding pure attack/defend resolution for the engagement.

**What opting out does:**
- **Your attack dice no longer protect you. Only allocated *defense* dice soak.**
  In opposition your offense does double duty (successes reduce damage, even if you 
  lose overall); opt out and that free *offensive* protection is *gone*.
- Resolution becomes two independent rolls: my attack vs your defense, your
  attack vs my defense. **Both sides can land full effect in the same beat** --
  opposition forbids this (only the winner deals). This is the bushido / mutual-
  kill case. Characters, even NPCs, may choose this at any time!
- Net effect: **more swing, more lethality, more luck-dependence.** NOTE this is
  NOT a *statistical* equivalent of opposition -- opposition is systematically
  *safer* because offense pulls double duty. Aggregate damage thrown is in the
  same neighborhood over many fights, but damage *received* is greater without
  opposition. The per-fight distribution is deadlier and spread across both combatants.
  The lethality IS the point.

**The Blitz itself (the zealot / sacrifice gambit):**
- Opt out of opposition in favor of every attack requiring a dedicated defense roll.
  Allocate **ZERO defense**; pour the entire budget into attack (full EL as a pure 
  attack -- vs an even split, this alone is a big swing).
- Offering *no* defense at all is so reckless it grants the possibility of a
  **free-action boost to the attack** -- the all-or-nothing commitment, weaponized.
  This is what makes a blitz a credible threat instead of mere suicide, so even a
  careful foe cannot blithely tank it.
- **How the boost works:** offering no defense is effectively a kind of psychological

  ambush -- nobody expects a foe to simply let himself be killed -- so it grants an
  instantly-available, no-prep **free-action Boost**. Roll the Boost right now as a free
  action and add its successes as bonus dice to your EL for the attack. (Yes, this raises
  the ceiling: EL6 + a 4-success boost = roll AND keep up to EL10, standard rules.)
  Its value scales with your own skill and ability to capitalize, so a dangerous warrior's
  death-strike is truly dangerous. Extra Effort is a *separate, stackable* option (Section 7)
  you may layer on the boost and/or the attack, with its own overshoot risk; do not conflate the two.

**Worked example -- ai-uchi at the daimyo's door:**
- **Kazuo** (L2 / Warrior 2 / Swords 2 -> EL6), no armor, wakizashi broken, luck
  nearly spent, but will NOT let the assassin reach his lord. 
  **Komi** (L3 / Warrior 3 / Katana 3 -> EL9), armored (men-yoroi), known by reputation.
  Kazuo is outclassed and knows it, so after a couple of defensive exchanges he chooses an
  honorable *ai-uchi* ("mutual destruction") over defeat.
- **Kamikaze Boost:** Kazuo rolls his free-action Boost with 2 Extra Effort dice
  -> **4 successes**. Added to EL: his attack is now at **EL10**.
- **Attack:** he rolls EL10 with 4 more Extra Effort dice (14 dice) -> **8** (<=10,
  no overshoot).
- **Komi**, not expecting a man to throw his life away, engages normally: 4 attack / 5 defense.
  Kazuo opted out of opposition, so Komi is forced into pure attack/defend:
  - Komi's katana goes into Kazuo's shoulder -- Kazuo doesn't even try to deflect (no defense). 
    Komi's 4 attack -> **2**; Kazuo (no armor) takes **2**, and at Down>2 he **survives**, barely.
  - Kazuo's **8** lands; Komi's 5 defense rolls only **3**, cutting it to **5** on the one-point
    men-yoroi mask. Unless Komi (the GM) spends a Token for **Plot Armor!**, 4 > his Down-3 drops him,
    and the younger samurai has a story to tell about the night he saved his daimyo.

For the record, if Kazuo is a PC, the GM should seriously consider NOT spending the Token.
The Kamikaze Gambit generally earns its win. 

**Emergent dynamics worth keeping:**
- "**The more defense you apply, the less damage we both do.**" At roughly matching
  EL, a pure defender vs a blitzer, the blitzer is largely soaked but takes little or
  no harm in return as defense dice are dice not spent attacking. It's still not a
  stalemate, as defending never does Harm, even on an excess win, while attacking does.
  Two blitzers -> mutual slaughter (both "win"). The defense knob dials the whole
  engagement's lethality, but pure defense is a stall for time in an otherwise losing
  battle.
- **Distinct from "all-in offense = naked":** the dumb-naked attacker generally stays
  opted *in* for opposition and eats a margin-riposte; the blitzer *opts out*, so there
  is no riposte -- just pure blows traded against whatever defense each side bought.

**RESOLVED:**
- **Boost basis:** the boost is a free-action Boost *roll* whose
  successes add as dice to (and raise the ceiling of) your attack EL. It is NOT
  Extra Effort; Extra Effort stays a separate, stackable option.
- **Consent:** the defender *cannot* refuse the opt-out and insist on opposition.
  The *actor* declaring the blitz forces pure A/D for that pairing -- you cannot *make*
  someone's offense protect them against your abandon.
- By definition the blitzer also forfeits the reusable free-defense entirely for
  the exchange -- they are open to *every* other attacker too, not just the duel.

---

## 10. Open flags (unresolved / needs editing before we write pages)

### F1 -- Allocation cap basis: Role EL vs Role rank
Split rules read as capping an action at the Role's **EL** (Performer EL10 ->
up to 10). Wagering caps dedicated points at the Role's **rank**. EL and rank
differ. Is the split cap rank or EL? Are they meant to differ? Author flagged
for a careful look. Watch for it in examples.

  All actions that *require* a Role to perform them cap at Role rank.  
  Wagers *optionally* cap at the relevant Role rank, for tables that feel Wagered
  Boosts are too powerful and unbalancing their game.  
  Splits are just dividing up actions, so the rule is making sure points of Warrior
  aren't used in a roll of a Performer action. Don't conflate these.

  In the Splitting example, the PC has Performer EL10 and Warrior EL20. They can
  allocate up to 10 points toward Performer actions because *that's all they've got.*
  Their Warrior EL is good enough that it can still do a little more though; the 
  point is that Warrior EL is reduced by the Performer allocation as a *distraction*.
  They are a good enough Warrior that they can do those things even while devoting
  attention to rallying the troops. 

  The "rallying the troops" is really *probably* a Wagered Boost, by the way.
  That Wager *can* be part of a split, but it makes no sense the other way around.

### F2 -- Is base-Level defense free, or must defense be allocated?
Current text (`multiple-actions.md`, `resistance.md`) overstates: reads as
defense always available, free, at base Level minimum. **Intent:** defense must
be ALLOCATED; spend everything on offense and you have NO resistance. "Free"
means an allocated defense is reusable and costs no separate turn. An
always-available base-Level defense is at most an OPTIONAL table rule. Surprise/
undetected attack caps allocated defense at base Level (luck), no Maneuvers.

  Agreed. We need to survey the existing pages for statements like this which are
  misleading and make adjustments accordingly.

### F3 -- "Down = free actions only": what applies when?
Largely GM judgment by design, but the boundary of allowed actions when Down
could use clearer guidance/examples.

  Agreed, and again, we should find and mark places that need more clarity.
  This rule is primarily intended to allow noncombat characters targeted as
  early attrition to participate more. The old Loremaster who quickly succumbs
  to a broken leg and cracked ribs can still cough out a few useful observations
  that support the party, but he can't go make a roll to climb the ledge and push
  the button to stop the trap, etc.

### F4 -- Two buckets, two layers; opposition vs. resistance is emergent
Pages declare opposition and/or resistance per interaction.
(`resistance.md`: "if you punch back ... that's opposition ... it takes a turn")
Text hides that you allocate BOTH offense and defense and BOTH layers fire in a
single engaged exchange. The either/or framing is probably the ROOT of the
confusion. The unified two-axis model is never stated plainly and
is the core of what the clarification page(s) must make explicit.

  Yes yes yes. Absolutely.

---

## Working example: the party (Demicon demo PCs)
Levels 2-4, Down thresholds 3-5 -> deadly and swingy; ideal for showing the
value of defense allocation and the harm death-spiral.

- **Bel Silverhand** -- Performer, Level 4. Base EL4 (no Role). Performer EL5,
  +Lute EL6; Hook +2 (1/scene) -> max EL8. Down 5. Luck 4. SUPPORT/boost engine
  (War Chant boosts fighting allies at EL5, one Wager per ally in sequence;
  Background Music EL6 boosts another's roll). Not a front-liner.
- **Karth a Sennon** -- Adept(Fire)/Healer/Loremaster, Level 2. Base EL2.
  Adept Fire EL4 / Manifestation EL6; Healer EL4 (Trauma EL6, Burns EL5);
  Loremaster EL4 (Demonology EL6). Hook +2 -> max EL8. Down 3 (fragile). Luck 2.
  Glass cannon -- see Overchanneling.
- **"Mauler" Maren Smithson** -- Warrior/Athlete, Level 3. Base EL3. Warrior EL5
  (Brawler EL7, Staff EL6), Athlete EL5 (Strength EL7). Hook +2 -> max EL9.
  Armor Leather 2. Down 4. Luck 3. Front-line grappler; Reach staff; nonlethal
  default (Complications unless deliberate Injury).
- **Mellisana** -- Warrior/Conjuror templar, Level 2. Base EL2. Warrior EL4
  (Shields EL6, Swords EL6), Conjuror EL4 (Detect EL5, Wards EL5, Rebuke EL4).
  Hook +2 -> max EL8. Brigandine 3 + Kite Shield 2. Down 3. Luck 2. The split
  sword-and-shield tank.



Opposition + scene still TBD (sheets imply a supernatural / Accords encounter
at a bounty celebration).

## New mechanical wrinkles surfaced by the demo sheets (track for consistency)
- **Mellisana's sheet validates the two-bucket / two-layer model** and states it
  more clearly than the rules pages: "Committing dice to offense reduces all
  skills by that amount ... commit 4 to attack, 2 remain for defense. Pure
  defense is a free action: those 2 dice resist every hit she sees coming, again
  and again." Bears on F1/F2/F4:
  - Defense capacity = the LEFTOVER EL of the relevant *defensive skill* after
    committing to offense ("without Shield training, the reduction leaves
    nothing -- the skill is the key"). Steers F1: the skill's EL both funds and
    caps the split; no skill -> no defense to hold.
  - Reusable defense ("again and again ... every hit she sees coming") confirms
    F2 intent (allocated, reusable, only vs. attacks you saw coming).
  - Cross-role defensive split ("Warrior dice catch the chairs, Conjuror dice
    catch the demon") = separate defense pools per threat type.
- **Armor application is inconsistent across sheets** -- needs a unified rule:
  - Maren: armor rating added as "Simple Pool dice that already succeeded,"
    ONCE per scene, after a roll armor could help.
  - Mellisana (as a Warrior): can SPLIT her armor rating across multiple uses in
    a scene; shield rating is a separate pool. Is the multi-use split a Warrior
    privilege or general?
  - Both: Plot Armor! (Luck/Karma) = armor absorbs a whole hit; rating drops by
    the amount absorbed unless Karma was spent.
  - **RESOLVED (in play):** an armor **tap** = **one free success per rank added
    to your EL and your roll** (matches Maren's "dice that already succeeded").
    **Plot Armor!** via a Luck Token = armor absorbs the WHOLE hit and its rating
    **drops by the amount absorbed** (destroyed if that takes it below 0 -- e.g.
    a rank-1 robe absorbing 2 is over-absorbed and ruined); with **Karma** the
    rating does NOT drop. Still open: whether multi-use splitting of armor is a
    Warrior-only privilege.
- **Overchanneling / Power Threshold (Adept)** -- Threshold = Level + Adept rank
  + Endurance maneuver. Communion never triggers it.
  - **Threshold base = Role + Level (clarified in play).** The harsher variant
    "anything over your Adept *rank* overchannels" was considered and **rejected
    as too punishing for most campaigns**; use Role + Level (+ Endurance
    maneuver). Karth: 2 + 2 + 1 = **Threshold 5**.
  - **Overage is ROLL-based, not EL-based (clarified in play).** Self-Harm = the
    margin the Manifestation **roll** clears **above Threshold**, resisted by
    Endurance. A low roll = weak effect but little/no backlash; a big roll hits
    hard AND bites back. (Karth's Area fire: Threshold 4, rolled 3 -> overage 0 ->
    no self-Harm. A roll of 7 would have been overage 3.)
    NOTE: this supersedes the earlier "Fire EL6 -> 1 self-Harm per full cast"
    EL-based shorthand.
- **Reach (weapon)** -- longer weapon gets a free-action Longer Reach Boost each
  turn; foe may oppose with a free action; reach winner holds shorter-reach foes
  out of melee; if the foe wins, they get Inside Reach and negate it.
- **Grapple / Lock** -- wagered persistent boost to seize/hold; a Lock imposes a
  movement Hindrance and escape needs a SPECIFIC roll (not just any success);
  Reversal is a free-action counter.
- NOTE: War Chant, Grapple, Whirlwind, etc. are character/maneuver-level
  illustrations, not core rules -- handy concrete test cases, but the core things
  to prove are the offense/defense split, opposition vs. resistance (two layers),
  and harm/Down.

---

## Opposition: goblin war party + demonic totem
A wandering goblin war party emboldened by a minor demon posing as a war totem.
NPC-simplified Roles (Raider, Archer), Maneuvers (Sword, Bow, Sneaky).

**Totem (Level 2, Demon 2, Display 2, Manifestation 2):**
- **Display = illusion** -- depends on the victim's perception/reaction; beaten
  by will (resistance); lands as **Complications** (fear, false images, lost
  nerve). EL6.
- **Manifestation = real physical effect** -- exists regardless of belief;
  physically resisted/avoided; can be **Injury**. EL6.
- Generic Demon EL4. Bound by the Accords. Neutralizing the totem is the
  highest-leverage PC play.

**Goblin roster (10):**
- 1 Leader, L3, melee, EL7.
- Lt #1, L2, BOW, EL5.
- Lt #2 & #3, L2, melee, EL5.
- 2 Grunt archers, L1, BOW ONLY (no melee), EL3.
- 4 Grunt melee, L1, EL3.
- Ranged threat = 3 bows (Lt#1 EL5 + 2 grunt-archers EL3): bypasses melee
  opposition (resistance only) and can focus the fragile.
- "Dumb goblin" default = all offense, no defense -> hit for their level but
  trivially hurt back and naked (F4). "Smart goblin" = focus-fire the fragile,
  archers from range, Sneaky surprise (F2 cap), totem morale.

**BIG: goblins are Halflings** -- present in the spirit realm AND physically, so
the supernatural toolkit works on the GOBLINS, not just the totem: Mellisana can
Ward/Rebuke them at range and her Holy Sword (vs. Halflings) lands material +
supernatural at once; Karth's Demonology applies. The PCs' main answer to range.

**Per-PC ranged / improvisational toolkit (the "smart play"):**
- Karth -- Fire EL6, the one strong conventional ranged attack (self-Harm via
  Overchanneling; Down 3).
- Mellisana -- Conjuror powers reach the Halfling goblins at range
  (Detect/Wards/Rebuke); best anti-totem.
- Bel -- "hurl insults," Performer verbal attacks up to EL8 -> Complications
  (lost nerve); potential mass-demoralize/rout once the totem's morale is gone.
- Maren -- can throw a rock (Warrior, short range); least ranged, melee anchor.

**Threat thesis (confirms author's read):** easy if goblins charge mindlessly;
dangerous via the bypass vectors (range, surprise/Sneaky, focus-fire the
Down-at-3 PCs) amplified by the totem. PCs' smart counter = the supernatural /
social layer (fire, at-range conjuring, demoralization) + pulling the totem
linchpin. Exactly the "deep tactics, as-is" thesis.

## F5 -- RESOLVED: multi-target needs a Trait
Default: EL **splits per target**. One roll hits many ONLY if the attack has a
relevant **Trait** such as **Area**. Trait availability is fiction-gated.

## F6 -- How each class adds Traits to an effect (e.g., Area)
- **Spellweaver (DEFINED):** add Traits at casting; each raises the spell's
  Difficulty (DL); roll resistance vs. that DL or the spell **destabilizes and
  is lost before it casts**. Hold it (succeed) and cast for effect normally with
  the modified spell. (= the existing "Difficult spells" mechanic, spells.md.)
  CLARIFIED: a successful Difficult cast just makes the **Traits take effect** --
  it does NOT also make the spell Inexorable. Inexorable is its own Trait, paid
  for separately. (spells.md's current wording conflates these and needs fixing
  in the editing pass.)
- **Adept (PROPOSED -- just invented, validate):** each Trait added lowers the
  Adept's Power Threshold by 1; at 0, further Traits add to the DL of the
  Endurance roll resisting the Overchanneling Harm. (Karth: Threshold 5; an Area
  fireball overchannels more -> more self-Harm.)
- **Conjuror (RESOLVED -- concrete model; page text written in shaping-effects):**
  the Conjuror pays in the RELATIONSHIP or in scars on the psyche, not the body
  (Adept) or memory/rank (Spellweaver). Two cases:
  - **Direct Conflict** (the Conjuror's OWN Working -- Ward or Rebuke): like the
    Spellweaver, resist the accumulated trait-difficulty; like the Adept, the
    unresisted overreach is HARM -- here **Soulburn**, a Hindrance that weakens
    ALL spirit-interactions until resolved. At post-conflict recovery, GM + player
    may negotiate converting the Soulburn Hindrance into an **Imposed Hook**.
  - **Borrowed Power** (a contracted/bound spirit produces the effect): the
    spirit's own nature shapes it; the Conjuror's cost for more is NEGOTIATION --
    a steeper bargain in offerings / Karma / Luck Tokens (pre-arranged is cheaper,
    on-the-fly much dearer). Compel it instead and the spirit gets a stronger
    chance to pervert/slip the terms, scaling with traits forced. Failure = a
    recalcitrant / angry / literal / loosed spirit, not self-harm or a lost spell.
  - Trait applicability (Conjuror): Area Ward = honor spatial locality when applied
    to spatial concepts; Guidable N/A to Wards; Selective usually a wash ("only
    spirits" is free; "only demons" = a difficulty REDUCTION); Inexorable = a
    breaching spirit eats that portion as unresistable Harm; Persistent = standing
    wall without a Wager. Area Rebuke can hit several spirits/Halflings and
    Inexorable applies, but Guidable/Persistent do not (a Rebuke is pure will, not
    a construct to steer).
  - **NEW CONCEPT -- Soulburn:** a Hindrance from spiritual overreach, convertible
    to an Imposed Hook at recovery. Depends on Imposed Hooks being made clear.
- **Engine dependency -- Exorcism as spiritual "Brawling" (TASK):** the Conjuror
  directly engages an entity; range / proximity / duration are purely conceptual;
  **Rebuke = offense, Ward = defense, default = OPPOSITION with Rebuke.** Must be
  stated explicitly on the Conjuror page (roles/conjuror).
- **Follow-on TASKS (author-flagged):**
## OUTSTANDING BACKLOG (author-confirmed; do shortest -> most involved)
Order preference: simplest first. Do NOT drop any of these.
- **5 (DONE) -- 3 new proposal pages landed + reviewed.** On-voice, correct vs the
  model; "Unbound" stripped from the conjuring TOC label; "spacial"->"spatial" and
  the Kamikaze "Down-above-2" phrasing fixed; each page's subsections anchored and
  added to the TOC as sub-entries (nav stays page-level, matching its style).
  KNOWN forward-dependency: Shaping Effects references Soulburn -> Imposed Hook,
  which item 1 must define.
- **3 (DONE) -- `spells.md`/spells.html Difficulty section rewritten.** Auto-
  Inexorable conflation removed; a successful Difficult cast just puts the Traits
  in force. CANONICAL Inexorable rule now stated: **point-for-point** (one
  Inexorable Trait = one unresistable point), still **Counterspellable**, and
  Inexorable points are **resisted last**. Introduced the named act **Improvise**
  (pushing a spell with added Traits). `traits.html` reconciled: the *Difficult*
  entry EXPUNGED (its mechanic lives on spells now) and the muddying "think of
  them as Roles or Maneuvers for non-player stuff" intro sentence removed. The
  *Inexorable* Combat-Trait entry left as-is (it's the effect definition, not the
  conflation).
- **4 (small-med) -- clarity fixes to existing core pages** (the survey):
  `resistance.md` ("punch back... takes a turn" -> shows it REQUIRES the split),
  `multiple-actions.md` ("at worst base Level" overstates F2),
  `wagered-actions.md` (rank-cap nuance). Clarity, clarity, clarity.
- **2 (DECIDED; rewrites pending approval) -- Adept Overchanneling standard.**
  CANON: **Threshold = base Level + Adept rank, but base Level counts only up to
  the Adept rank** (the standard "trained-only feat" cap). Level 4 / Adept 2 ->
  Threshold 4. Maneuvers and Boosts do NOT raise the Threshold (they raise EL,
  which is what lets you overreach); Extra Effort adds dice, not EL, so it never
  creates overchannel effect. **The Overchannel RESISTANCE roll uses the FULL,
  uncapped Level** + Adept rank + any *Endurance* Maneuver (shrugging off the burn
  is the whole self, not just the Art) -- so a high-Level/low-rank Adept overreaches
  easily but resists well. **Endurance is NOT in the Threshold**, only the resist
  roll. TUNING DIAL (harsher): Threshold = Adept rank alone. Luck Tokens always at
  full Level.
  - Rewrites needed (proposed, awaiting author OK): `roles/adept` "Price of Power"
    (threshold def + resist-roll full-Level); `magick/adepts` "Nontrivial Magic" +
    Marcus example (reworked to Threshold); `action/adept` Astrape -- LEAVE the
    numbers, add a parenthetical that her table uses the optional strict dial
    (Threshold = rank alone).
- **SWEEP DONE (base-Level cap in examples).** Scanned every in-action + magick
  example. Result: the cap (base Level added <= Role rank) only bites on
  **training-ONLY tasks** (essentially magic); tasks anyone can attempt (climb,
  shoot, persuade, hide, treat) correctly use full Level. Findings:
  - **Only real violations: the Adept magic examples.** `action/adept` (Astrape):
    "EL9" -> EL8, "EL7" (Communion) -> EL6 (Level 4 > Adept rank 3). `magick/adepts`
    (Marcus) Level 4/Adept 3. Both already on the docket (Astrape = leave + strict
    parenthetical; Marcus = reworked).
  - **Everything else is clean** -- and *why* is worth noting: nearly every example
    PC is built with **base Level == primary Role rank** (Korinne L3/Athlete3,
    Marta L2/Lore2, Berlis L3/Sweaver3, Whisper L3/Sneak3, Vera L3/Sniper3,
    Olberict L3/Tinker3, Tam L1/Healer1), so no over-add is possible. The few with
    Level > a role rank (Gareth L4/Performer3; the L4/Sneak2 spy) are doing
    untrained-attemptable social/stealth, where full Level is correct.
  - **Spellweaver (Berlis) RESOLVED -- two ranks, name them both.** A Spellweaver
    casting has TWO relevant rank values: **effective/available rank** (ranks not
    bound into other spells) = the Role bonus added to *this* cast; and
    **mastered/true rank** (full trained rank) = the cap on how much **base Level**
    may be added. Berlis (L3 / Sweaver 3, 1 free) = base Level 3 (capped at mastered
    3) + Spellweaver 1 (effective) + maneuver -- the example is correct. A Level 4
    Berlis would still bring only 3 base Level. TODO (small): state this explicitly
    on `roles/spellweaver` ("Binding the Powers") and make the general cap line
    (mechanics: "add base Level up to your rank") say **mastered** rank.
  - **Minor nit FIXED:** `action/naturalist` "Level 2 + Weather Sense 2 = EL6"
    now reads "Level 2 + Naturalist 2 + Weather Sense 2 = EL6" (2+2+2).
- **1 (most involved) -- Imposed Hooks, soup to nuts.** Add explicit verbiage on
  `harm.md` / `types-of-harm.md` / the Hooks pages: what receiving an Imposed
  Hook means, how it operates in play, how it is recovered. Prerequisite for the
  Conjuror "Soulburn -> Imposed Hook" path already referenced on Shaping Effects.
  Needs a read of the Hooks chapter + a design pass with the author.

### (reference) originally-logged task notes
  1. DONE -- **Exorcism** elaborated on `roles/conjuror` as a new "Spiritual
     Conflict" subsection (Brawling analogy; range/proximity/duration conceptual;
     **Rebuke = offense, Ward = defense, default opposition with Rebuke**; grind
     the spirit to Staggered/Down to open the three finishers; Aura Hardening =
     armor, Third Eye brings full Role strength).
  2. Revisit `harm.md` / `types-of-harm.md` / the Hooks pages to make **Imposed
     Hooks** clear: what receiving one means, how they operate in play, how they
     recover. (Prerequisite for Soulburn's recovery path.)
  3. Fix `spells.md`'s Inexorable wording (already logged) -- it conflates a
     successful Difficult cast with auto-Inexorable.

## Site-infra tasks (raised while writing the proposal pages)
- **B -- Anchor sweep: DONE.** `tools/anchor_sections.py` added `id` anchors
  ABOVE 90+ subsection headings across 20 pages and repointed the TOC sub-links;
  `.section-anchor` + heading `scroll-margin-top` CSS (in style.css) lands jumps
  below the fixed header. Verified all 106 fragment links resolve, no dup ids.
  Also fixed a load-time reflow race in `rails.js` (re-resolve `location.hash`
  after the layout is built) so anchored jumps land cleanly.
- **C -- TOC-at-self in the rail: DONE.** `rails.js` `markTocCurrent()` highlights
  the current page/section in the injected TOC and scrolls the rail's own box to
  it, on render and on hashchange; `.toc-current` CSS marks it.

## F7 -- Kamikaze Blitz tuning (see the gambit in Section 9)
- **Boost basis: RESOLVED** -- free-action Boost *roll*; its successes add as dice
  to (and raise the ceiling of) the attack EL. Distinct from Extra Effort, which
  remains separate and stackable.
- **Consent:** does the actor declaring the blitz unilaterally force pure
  attack/defend for that pairing (recommended default), or can the defender
  insist on opposition?
- Confirm the blitzer is open to ALL attackers that exchange (no reusable defense
  at all), not just the duel partner.

---

## ORIENTATION (mode) -- live state is at the END of this file
- **Mode:** systems analyst / sounding board. The author drives the examples; I
  do NOT write rulebook content or invent examples/breakdowns. Iterate over many
  turns, agree on the model, THEN write clarification page(s); later consider
  back-porting to the source PDF.
- **LIVE TODO = the "## OUTSTANDING BACKLOG" section** (mid-file) -- that is the
  authoritative to-do list, shortest-first. The "CURRENT STATE & NEXT STEP"
  section at the very bottom is a HISTORICAL snapshot from the end of the
  proof-out phase; treat it and the play log as background, not the task list.

---

## SKIRMISH PLAY LOG (worked demo in progress)

**Opening fiction (established).** The 4 PCs are on foot heading **west** to
regain the road, having earlier split from other companions who struck **north**
toward the city. Marching order: **Mel on point** (heaviest armor),
**Maren rearguard**, **Bel and Karth side by side** in the middle, chatting
philosophy/morality. Mel's unease has her squinting and scanning -- a tell the
goblin leader reads as "they're as close as they'll get," so he springs the
ambush.

**Surprise roll (Simple Pool, count odds).** Goblins (leader EL7 +2 Hook
"Goblin, Halfling" = EL9) rolled **6**; PCs rolled base Level -- Bel 2, Karth 2,
Maren 2, **Mel 3** (base 2 + Conjuror rank 2). Goblins beat everyone -> full
surprise; PCs get base-Level resistance only, **no Maneuvers** (F2 cap). Mel's
3 was best of the party (her unease nearly paid off) but the goblins clearly won
-- ruling: give it to them.

**Opening archer volley (3 bows fire with complete surprise, random targets).**
- Lt#1 (EL5) -> Mel: rolled **1**; Mel resisted **2 of 2**. Miss, skips off armor.
- Grunt A (EL3) -> Maren: rolled **1**; Maren resisted **2**. Wide.
- Grunt B (EL3) -> Karth: **maxed 3 of 3**; Karth resisted **1**. **Leak 2.**
  (The weakest archer hits his ceiling and tags the most fragile PC -- textbook
  small-pool swing landing on the worst target. Karth Downs at 3.)

**Karth's response.** Spent **1 Luck Token on Plot Armor!**: his rank-1 robe
absorbed the whole 2 Harm and was **over-absorbed -> destroyed**; he tears the
fouled robe off in fear of a poisoned point. Result: **0 Harm**, but Karth is now
**without any armor** for the encounter and down to **Luck 1/2**. He'll look for a
chance to **self-Hook** to restock a token. (No good option existed -- exactly the
intended constraint.)

### PARTY STATE entering round 2 (armor = sheet values)
- **Bel** -- L4, Luck 4/4, **gambeson = armor 1** (default travelling gear),
  Harm 0. Untouched; weapons/voice coming up. "Lucky Bard."
- **Karth** -- L2, Luck **1/2**, armor **0** (his thick robes WERE the default
  rank-1 gear; over-absorbed 2 via Plot Armor! and were destroyed -- volley
  outcome consistent), Harm 0. Down 3. Glass cannon; wants a self-Hook restock.
- **Maren** -- L3, Luck 3/3, **Leather 2**, Harm 0.
- **Mel** -- L2, Luck 2/2, **Brigandine 3 + Kite Shield 2** (separate pool),
  Harm 0. Fully alert; Maneuvers (Shields/Wards/Rebuke/Detect) back online.
- **GM Tokens: 5** (Bel's L4 + 1). No obligation to spend except to make the
  story fun.
- **DEFAULT ARMOR RULE (established):** unless a sheet specifies otherwise, a
  PC's ordinary **travelling gear / sturdy clothes counts as armor rank 1** --
  good cloth can still turn an edge. Specified armor overrides (Maren Leather 2,
  Mel Brigandine 3 + Kite 2). Earlier session's "Mel 2, everyone else 1"
  superseded.

### GOBLIN posture for round 2 (author's setup)
- Melee goblins **array forward as a prepared line**, screening the 3 archers
  behind them.
- **Melee allocation: irrelevant until challenged.** If a PC closes, they
  **oppose viciously = incautiously = offense-heavy, little/no defense.** (Naked
  to a riposte -- the F4 "dumb goblin" trap.)
- **Archers: devoting their ENTIRE EL to attack** (no defense) and keep firing
  each exchange -- no PC has a bow, so they hold range with impunity. They think
  they have one or two more free shots to soften the party. They don't realize
  these are **10-Karma PCs**.
- Totem held back (exact position TBD).
- **Author's read:** forcing the charge may backfire -- the PCs' real answer is
  the supernatural / ranged / social layer (Karth's Fire, Mel's conjuring
  reaching the Halfling goblins at range, Bel's demoralization) plus pulling the
  totem linchpin. They need not make a "stupid charge." Round 2 tests that.

### ROUND 2 -- formation & declarations (PARTIAL; full allocations pending)
- **Bel** refuses to be lined up: "Don't line us up!" Steps out from behind
  Maren so Maren keeps the option to dodge (can't, if shielding someone behind).
  Bel trusts being a low-value target + his absurd luck -- stands apart, solo.
- **Maren** -- moved to **screen Karth alongside Mel** (Mel: "Protect the
  priest!"). Cloak wrapped around off-hand as a makeshift shield. Intends to
  devote his **ENTIRE EL to defense** -- catching any arrows that come in on his
  cloak-wrapped greaves (covering for Karth). Nodded with a frown at Bel.
- **Mel** -- draws sword, unshoulders kite shield into position; stands with
  Maren as the screen in front of Karth.
- **Karth** -- stands behind/between the two fighters, **focuses past them at the
  archers** (readying his ranged answer).
- **PENDING:** author returning home to declare full **actions + dice
  allocations** for everyone before any rolls. DO NOT roll until then.


### EXCHANGE 2 -- RESULT (played)

**Bel (resolved earlier):** EL8 (Performer 6 incl Lute +Hook 2), wagered 6 into a
standing *Inspiration* Boost; 2-die carrier rolled [0,1] = 1 success -> lands.
**Boost (6) given entirely to Karth**, who split it 2 to his Fire attack
(EL6 -> 8) and 4 to Endurance (4 -> 8). Bel keeps 4/4 Luck.

**Mel:** declared a defensive **Ward, Area by default** -- a barrier to the
Halfling goblins' passage and *spirit* sight (physical sight/hearing intact;
discomfits them like losing an eye). Cost: 4 dice. Does NOT stop arrows. Also 2
dice held in personal defense. Sword laid across the shield (salute), shield up.
- **PROCEDURE FIX:** the Ward is a rolled action and was initially mis-applied as
  a flat "+4 defense dice" without a roll. Retroactively legitimized: Mel
  **spent a Luck Token** (2 -> 1) to set the Warding roll to best-possible = **4
  successes**, so the strength-4 effect (barrier + 4 defense lent to every ally)
  stands and Exchange 2's zero-Harm outcome holds.
- **NOT a wager** (no points split into wager + carrier). A plain Ward lasts
  **one exchange** and **falters next exchange unless re-rolled** (may come up
  weaker or, rarely, stronger).

**Archer volley (all-offense) vs Maren & Mel, defenders +4 Ward dice:**
- Lt#1 EL5 hit 3 at Maren; Maren's 9-die defense (5 Warrior EL + 4 Ward) rolled
  a weak 2 -> leak 1 -> Maren taps 1 of Leather 2 -> **0 Harm**.
- Both grunt archers rolled 1 -> fully resisted. **Party takes nothing.**

**Karth's Area fire, EL8, rolled 3 successes, onto the whole cluster:**
- **Archers (spent all EL on offense -> NAKED):** 3 - leather 1 = **2 each**.
  Both L1 grunt archers DOWN (Harm 2 > Lvl 1); Lt#1 (L2) seared to 2 Harm,
  standing but EL now 5-2 = 3. Bow threat gutted off a mediocre roll.
- **Melee (unspent EL -> retroactive resist at BASE LEVEL only vs fire):**
  Leader 1 Harm, Lt#3 1, GruntM1/M3/M4 1 each, GruntM2 (rolled 0 resist) took 2
  -> DOWN; Lt#2 resisted clean, untouched.
- **Overchannel:** roll 3 vs Threshold 4 -> overage 0 -> **no self-Harm**. The
  4 Endurance dice were unneeded insurance (still correct play).

**Tally after exchange 2:** PCs untouched (Maren's 1 soaked). Goblins: **3 DOWN**
(2 grunt archers + 1 grunt melee), **Lt#1 archer crippled (2 Harm)**, and Leader
+ Lt#3 + 3 grunt-melee each carrying 1 Harm (budgets shrinking = death spiral
begun on the goblin side). The all-in-offense party paid the F4 price; the
supernatural/ranged answer beat the "charge our line" bait with no one charging.

### CLARIFICATIONS captured this exchange
- **Wager/commit cap basis (F1, RESOLVED):** the cap is the relevant **skill's
  EL**, NOT Role rank. AND the cap only applies when the act *requires* the skill
  (e.g. improvising a barely-known song). A general action anyone could attempt
  (Bel's rally) is not rank-capped; the specialist just adds +1 die for Role and
  +1 for Maneuver. So Bel legally wagered 6.
- **Retroactive defense from UNSPENT EL (extends F2):** a target who allocated
  nothing may retroactively spend unspent EL to resist an incoming effect, but
  capped at **base Level** when their Roles/Maneuvers don't apply to that effect
  (fire vs melee skills -- same cap logic as surprise). EL already **spent on
  offense cannot be reclaimed** -> all-in attackers are fully naked (the archers).
- **Ward = rolled action, not a wager; one-exchange unless re-rolled.** A Ward's
  successes = its strength (barrier value + defense lent to allies). To make it a
  PERSISTENT wall you must actually **wager** (split points into wager + a carrier
  roll); a plain Warding allocation resolves and fades that exchange. An Area
  defensive Ward lends its strength to EVERY ally's defense, even those who
  allocated none (reusable-soak principle), but only while it stands.
- **A failed-to-roll allocation can be covered retroactively by a Luck Token**
  (best-possible result), at the cost of the token -- used to settle Mel's Ward.
- **Warrior armor splitting in use:** Maren tapped 1 of his Leather 2 (not the
  whole rating) to soak 1 leak, consistent with the open "Warriors may split
  armor across uses" note.

---

## Existing-page survey -- where each clarification lands
Reference list for the editing pass (do when time allows). [read] = checked this
pass; [verify] = still needs a look. Quoted bits are the page's own words.

### F4 -- two buckets / two layers (the core writing target)
- `resistance.md` [read] -- "If you punch back with that roll, that's not
  resistance, it's opposition, and it would take a turn." Intent is CORRECT and is
  NOT either/or: punching back costs you an allocation (a "turn"), which is exactly
  WHY you split offense + a reusable defense. Reword so it shows that REQUIREMENT
  rather than reading as mutual exclusion.
- `resistance-and-opposition.md` [read] -- presents Opposition vs Resistance as
  either/or per interaction; never states "win the contest AND beat the defense."
  Add the two-axis / two-layer model.
- `actions-and-timing.md` [read] -- "Direct Opposition" ALREADY says opposition
  "is really just a compression of the usual sequence ... both sides roll
  simultaneously ... but you can always do it the long way if you want," and that
  simultaneous action "is one way both combatants can kill each other." This is
  the textual backbone for the two-axis model AND the Kamikaze opt-out -- surface
  it, don't reinvent it.
- `mechanics.md` (Dice & Tests) [read] -- "effect = roll minus opposition/
  resistance, ties to defender" is a good launch point to seed the framing.
- NEW PAGE "Resolving Combat: a two-axis model" -- the definitive F4 statement,
  anchored on the goblin skirmish.

### F2 -- defense must be ALLOCATED (base-Level-free is only optional)
- `multiple-actions.md` [read] -- "You can almost always defend as a free action
  ... at worst you should always be able to use base Level" overstates. Clarify:
  defense must be allocated; always-on base-Level defense is at most an optional
  "luck" table rule; surprise caps it.
- `resistance.md` [read] -- "Resistance is virtually always a free action ... use
  it again, and again" -- clarify "free/reusable" describes an ALLOCATED defense.

### F1 -- cap basis (skill EL vs Role rank)
- `wagered-actions.md` [read] -- "You can never dedicate more points than your
  rank in the relevant Role." Reconcile: rank cap applies to acts that REQUIRE
  the Role; add "unless the task could be done without the Role at all," and note
  the wager rank-cap is an optional balance lever.
- `multiple-actions.md` [read] -- the Performer/Warrior split example is fine; add
  the gloss that a split only stops you spending one Role's points on another's
  action (it is NOT a rank cap).

### F3 -- Down = free actions only (boundary / examples)
- `feeling-down.md` [read] -- states "only passive resistance ... GM may allow
  Free Actions." Add the author's intent + example: the downed Loremaster can
  still cough out useful observations but can't climb the ledge to hit the switch.
  (Staggered variant already lives here.)

### F5 -- multi-target needs a Trait (RESOLVED; already in the rules)
- `traits.md` [read] -- "Area Effect: Targetable (default) / Blanket / Selective"
  already defines exactly this. No new rule -- just CROSS-REFERENCE from the
  combat pages so "splits per target by default" shows where attacks are taught.

### F6 -- Overchanneling / Adept Threshold (INTERNAL CONFLICT in existing pages)
- `roles/adept.md` [read] -- "The Price of Power": DEFAULT Threshold = base Level
  + Adept rank (+ relevant Maneuvers), with "base Level alone, or even Adept rank"
  offered as HARSHER options. **Already matches our F6 resolution**; also already
  states undifferentiated Harm ("won't know how bad ... until ... recovery") and
  roll-based overage. Treat as canonical.
- `magick/adepts.md` [read] -- "Nontrivial Magic" / Marcus example overchannels
  off RANK only (L4/Adept3, resists 7-3 = 4). CONTRADICTS the rule above.
- `action/adept.md` [read] -- Astrape example also burns off RANK ("only has 3
  Role ranks, so the overchanneled 4 points burn"). Same fix: bring both worked
  examples in line with Level + rank.
- Conjuror Trait path (F6 -- DIRECTION AGREED, refining; see the F6 block):
  `roles/conjuror.md` [read], `magick/conjuring.md` [read], `action/conjuror.md`
  [read] -- no explicit "Conjuror adds Traits at a cost" mechanic in the existing
  pages (unlike Spellweaver DL / Adept Threshold); Wards are spell-defined
  (Selective Supernatural). Framework now proposed (pay in the relationship: price
  / perversion for spirit-work, thinner-wall for the Conjuror's own rituals).
  BONUS confirmations: conjuring.md says a spirit's Manifestation IS "the
  persistent Boost resulting from a Wagered roll ... integrity = points wagered"
  (validates totem-as-wagered-persistent-effect and our "persistent = wager"
  rule), and confirms Display (Complications, vanish) vs Manifestation (real,
  takes Harm) and Halflings/goblinkind in both realms.

### Armor (our open "Warrior multi-split?" is largely answered here)
- `armor.md` [read] -- already matches our tap rule ("once per scene ... treat as
  after-the-fact extra EL that already rolled Simple Pool dice successfully") and
  Plot Armor! (absorb all, reduce rating, Karma spares, destroyed if exceeded). It
  ALSO distinguishes Maneuver-based armor EL usable on SPLITS (the Warrior
  benefit) from the once/scene flat tap -- which answers our open question.
  Reconcile our doc to it; likely no rule change, just make the two uses explicit.

### Luck Tokens (mostly already consistent)
- `luck.md` [read] -- already has retroactive use ("at any time ... even after the
  dice ... as long as the final resolution hasn't been decided") and our caveat.
  Optional add: the "one token = one use per hit" mutual-exclusivity from Karth's
  dilemma.

### Undifferentiated Harm (present but scattered -- state it once, plainly)
- `roles/adept.md` [read], `what-do-i-roll.md` [read], `advanced-options.md`
  [read] all reference unclassified Harm resolved at recovery. `harm.md` [read]
  ("no hit points; harm is a modifier") and `types-of-harm.md` [read] define the
  types but never say Harm STARTS undifferentiated -- state it plainly on one of
  them; `recovery.md` [read] is where differentiation happens, so link it there.
  (`armor.md`'s second-recovery Injury->Complication conversion ties in.)

### Kamikaze Blitz / opposition opt-out (new optional rule)
- `actions-and-timing.md` [read] -- "do it the long way" + "both combatants can
  kill each other" ALREADY license the opt-out; the gambit just names it and adds
  the free-action boost reward. Cite as the anchor.
- `advanced-options.md` [read] -- natural HOME for the opt-out gambit (already
  houses Lethality / Realistic Healing toggles).
- `traits.md` [read] -- relate to existing `Insidious` ("cannot be opposed, only
  resisted") and `Inexorable` ("no Resistance"); the blitz is the player-side
  cousin -- forcing pure attack/defend by abandoning your own defense.
- `gear-traits.md` [read] -- the free-action Boost mechanic (unrated Traits) is
  the model for the Kamikaze boost roll; same family.

### Reach / Grapple (consistency check)
- `roles/warrior-maneuvers.md` [read] -- "Reach" lives under the *Polearms*
  maneuver (reconcile our "Reach (weapon)" wording); "Combat Reflexes" already
  grants "resistance to surprise attacks" (relevant to the F2 surprise cap);
  "Armored Combat" is the Warrior armor-leverage maneuver (ties to the armor-split
  note). Grapple/Lock is NOT detailed here -- stays a maneuver-level illustration
  unless a dedicated writeup turns up [verify elsewhere].

### Additional confirmations (no change needed; cite as support)
- `actions-and-timing.md` [read] -- Boosts, Wagered duration, and "free-action
  access to pre-existing Boosts" (environmental boosts added to a roll).
- `assist-rule.md` [read] -- a companion/item Boost is capped by YOUR relevant
  Role rank; the rank-cap-on-borrowed-power pattern echoes F1 and models
  "covering" an ally (Maren screening Karth).
- `extreme-results.md` [read] -- a big Extreme success can strip a target's
  opposition/resistance entirely (the F4 "naked" extreme); Extra Effort forgoes
  extremes (matches our dice notes).

---

## CURRENT STATE & NEXT STEP (HISTORICAL proof-out snapshot -- the live TODO is the "OUTSTANDING BACKLOG" section above)

### SCENE END -- take stock
- **Exchange 3 (brief):** PCs let them go; spend an exchange on precautionary
  rolls (Mel re-Ward/Detect, Karth ready, Bel watchful, Maren guarding) while the
  strength-4 blood-mist burns off. It fades to reveal the ruined corpses; no
  pursuit. **Scene over.**
- **Party aftermath:** all four **unharmed** -- no recovery rolls needed.
  Resources spent across the whole fight: **Karth** lost his robe (armor 0) and 1
  Luck (1/2); **Mel** 1 Luck (1/2); **Bel** his 1/scene Hook and 6 EL wagered into
  Inspiration (both refresh next scene; Luck still 4/4); **Maren** nothing but a
  cloak. GM spent 0 of 5 tokens.
- **Refresh at next scene:** Luck Tokens reset to = Level; Bel's Hook and wagered
  EL return; Karth still needs to repair/replace armor and may self-Hook to
  restock. The Inspiration boost and Mel's Ward both expire with the scene.
- **Field:** 3 goblin dead, others fled wounded under the totem's screen; the
  **totem/demon escaped intact** (still bound by the Accords). Corpses + demonic
  taint left for Loremaster/Detect follow-up if the author wants a denouement.

### What the demo PROVED (the thesis)
- **Deep tactics emerged from the core engine with NO special rules.** "Set up
  fortifications (Ward) + artillery (fire) and still hold actions" was just
  ordinary allocation.
- **F4 was the decisive moment:** the archers went all-in offense, allocated zero
  defense, ignored Karth -> naked -> gutted by a *mediocre* fire roll. This is the
  single best argument for fixing the either/or opposition-vs-resistance framing.
- **Defense as reusable universal soak** (Mel's one Ward shielding everyone, even
  un-allocated Bel/Karth) and **offense as threat** both showed up naturally.
- **Harm = budget shrink / death spiral** demonstrated on the goblin side.
- **Small-pool swing** (grunt maxing EL3 onto fragile Karth; Karth's own low fire
  roll) gave the dice-texture lesson.
- **Resource scarcity made real decisions** (Karth's no-good-options token
  dilemma; situational token mutual-exclusivity; retroactive token rescues).
- **The supernatural/social layer answered a ranged ambush** exactly as the
  thesis predicted (Ward-as-terrain, Area fire, goblins-are-Halflings).

### FLAG STATUS after the demo
- **F1 RESOLVED** -- commit/wager cap = the relevant skill's EL, and only applies
  to skill-gated acts; general actions aren't rank-capped.
- **F2 confirmed + extended** -- defense must be allocated; surprise/effect-vs-
  -wrong-skill caps it at base Level; retroactive defense only from UNSPENT EL.
- **F4 (CORE)** -- richly demonstrated; this skirmish is the worked example to
  anchor the clarification page. Still the top writing target.
- **F5 RESOLVED** -- multi-target needs an Area-type Trait (Karth's fire, Mel's
  Ward both shown).
- **F6 advanced** -- overchannel is roll-based; Threshold = Role+Level; Traits
  lower it (Area -1). Conjuror trait path still only lightly touched.
- **F3 STILL OPEN** -- "Down = free actions only" never tested (no PC Downed;
  goblins just removed). Needs its own example or prose.
- **Armor** -- tap = free success/rank; Plot Armor! degrades by amount absorbed
  (Karma spares it). OPEN: is multi-use armor splitting Warrior-only?

### NEXT -- shift from proving to WRITING
The proof-out is essentially complete. Recommended next phase: outline the
clarification page(s), top priority being the page the author has titled
**"Resolving Combat: a two-axis model"** -- the F4 fix. The two axes = (1) how
much offense you aim at each foe, and (2) how much defense you hold as reusable
soak; "axis" invites the reader to see the tradeoff. Use this skirmish as the
worked example and serve both the rules-light and tactics audiences in one text.
Per mode, do NOT draft rulebook prose until the author green-lights it; start
with an agreed outline. Secondary pages/sections: armor unification,
overchannel/Traits (F6), Down (F3).

