<!--
  =============================================================
  TESSERAE SORTIS — ORACLE: CONSOLIDATED MASTER (DRAFT FOR REVIEW)
  =============================================================
  This merges the two source drafts:
    - oracle_system_seed.md          ("The Quaerant's Oracle — Seed Draft")
    - solo_oracle_working_draft.md   ("Solo Oracle System — Working Draft")

  MERGE RULES USED (so you can audit the seams):
   1. Your wording is preserved verbatim. Nothing was rephrased or
      "improved." Section structure follows the seed's cleaner skeleton.
   2. Where the two drafts differed only trivially in phrasing, the more
      COMPLETE draft's wording was used, silently. (No content changed —
      just whichever sentence carried more.)
   3. Where they differ SUBSTANTIVELY, the spot is marked  @@DECISION
      with both options shown. Search "@@DECISION" to find all of them.
   4. The "menials"/"violent criminals" suit language is the one place a
      correction was applied rather than flagged-only: the corrected
      (working-draft) table is used, because both drafts' own design note
      says it should be. Marked anyway so you see it.
   5. Existing @@ notes/TODOs from both drafts are carried through.

  @@DECISION STATUS — all resolved by the author's edit pass:
     A. Title — "Tesserae Sortis" (title) / "The Quaerant's Oracle" (subtitle).
     B. Suit-domain table — corrected wording stands.
     C. Aperture stated twice — kept deliberately.
     D. Tower spread — centered-column layout chosen.
     E. Lexicon — rich prose canonical; per-card pages + tabular index planned.
  =============================================================
-->

<!-- @@DECISION A — RESOLVED: "Tesserae Sortis" is the title; "The
     Quaerant's Oracle" is the subtitle (author's edit pass). -->

# Tesserae Sortis
### The Quaerant's Oracle

A Card-Based Solo Oracle System
*System Reference Document*

Compatible with Level One TTRPG and adaptable to other systems, or usable alone.

---

## DESIGN PRINCIPLES

This oracle uses a standard 54-card deck (52 + 2 Jokers) as a complete interpretive system. Every meaningful element is encoded directly into the card face - no lookup tables required for basic play, though references are provided for convenience. The principles are consistent enough to learn and apply improvisationally, using as much or as little as you like on any given draw.

Three layers of meaning operate simultaneously on every card:
- **Color** provides binary direction (yes/no)
- **Suit** provides narrative texture and thematic domain
- **Rank** provides role/archetype association OR degree when relevant

The player controls interpretive depth by choosing which layers to read. A simple yes/no question reads color only. A full scene prompt reads all three layers together.

**The Aperture Principle**: The more specific your question, the more limited and specific the answer. The most open and freeform application is not a question at all, but a __prompt__: *"I do this. What happens?"* This is a feature, not a bug.

**Design note on suit associations**: This system uses visually intuitive suit mappings (a club is a weapon, a spade is a digging tool) rather than traditional cartomancy associations. Players comfortable with traditional or Tarot associations may substitute those freely - the system works either way. We did try to keep at least nominally in line with pseudo-traditional applications. 

---

## NOTATION

| Element | Notation |
|---|---|
| Ranks | A, 2-9, 0, J, Q, K |
| Suits | H, D, C, S |
| Color only | *r (red), *b (black) |
| Jokers | Xr (colored/red), Xb (black & white) |

Tens are written as **0** (single character, eliminates the only two-digit label, allows zero as a value).
Aces are **low** (value = 1) throughout.

**Examples**: AH, 0C, QS, 7D, Xr, Xb

<!-- BUILD NOTE (not rulebook content): on the CDN the card files are
     lowercase {rank}{suit}.png with ten = "10" (e.g. ah.png, 10c.png),
     and the jokers are Xr.png / Xb.png (capital X). The display notation
     above (A, 0) maps to filenames (a, 10) via TS/cards.js. -->

---

## THE CARDS

### Color: Direction

| Color | Meaning |
|---|---|
| Red | Yes |
| Black | No |

*Design note on color: Red=Yes, Black=No follows the existing coloring of a standard deck and traditional interpretation. This is worth naming plainly anyway, since "black" carrying negative connotation and "red/light" carrying positive connotation is a cultural trope. We didn't recolor a standard deck, because we don't mean for you to have to buy something new. We have tried to keep the suit domains and descriptions neutral and free of value judgment.*

### Suit: Narrative Texture & Thematic Domain

<!-- @@DECISION B — RESOLVED: corrected suit wording stands (Clubs
     "...raiders, coercion"; Spades "tradesfolk, tools..."). -->

| Suit | Texture | Domain |
|---|---|---|
| **H**earts | Yes, *and* - an additional beneficial result or lead | Social - romance, reputation, contacts, art, gifts, influence |
| **D**iamonds | Yes, *but* - an unwanted side effect accompanies success | Commercial - trade, cost, worth, value, municipal action |
| **C**lubs | No, *and* - failure triggers an unwanted side effect | Conflict - fighting, soldiers, guards, raiders, coercion |
| **S**pades | No, *but* - failure yields progress toward the goal | Labor - tradesfolk, tools, mechanisms, guilds, farming, mines, caravans |

*Design note: We chose visually intuitive suit associations (a club is a weapon, a spade is a digging tool) over traditional cartomancy mappings. Players already comfortable with traditional or Tarot associations should feel free to use those instead - the system works either way.*

*Additional layering (elemental, seasonal, directional) is valid and can be assigned on the fly or referenced from a table. Any binary or quaternary division maps cleanly here.*

### Rank: The Roles

| Rank | Role | Domain |
|---|---|---|
| A | Warrior | violence, brutality, physical confrontation |
| 2 | Sniper | Ranged precision, tactical positioning, action at distance |
| 3 | Performer | Emotional manipulation, social influence, entertainment |
| 4 | Sneak | Concealment, stealth, acting undetected |
| 5 | Naturalist | Wilderness, survival, tracking, environmental knowledge |
| 6 | Beast Handler | Animals, training, compromise, partnership |
| 7 | Athlete | Physical excellence, endurance, athletic feats |
| 8 | Healer | Medical matters, assistance, any care |
| 9 | Loremaster | Knowledge, reasoning, seeking or finding wisdom |
| 0 | Tinker | Craft, process, problem-solving, goods and services |
| J | Adept | Intuition, talent, spontaneity |
| Q | Conjuror | Spiritual matters, negotiation, making deals, matters unseen |
| K | Spellweaver | Formulaic wonders, rules that break rules, supremacy of wit |

Pip cards (A-0) represent mundane matters. Face cards (J, Q, K) represent wondrous or (at least seemingly) arcane moments.

Rank is not always relevant. When it matters, it either identifies the professional character of the result, or introduces a statement of degree.
When it doesn't, simply read color and suit and move on.

### The Jokers: Chaos & Permission

| Card | Meaning |
|---|---|
| **Xr** | Chaos with potential - weird, wonderful, disruptive; possibly a gift. |
| **Xb** | Chaos with teeth - extraordinary and probably dangerous; your gut says to be wary. |

Either Joker suspends the normal interpretive range. Go bigger. Go stranger. Go unexpected. The non-Joker cards in the same draw offer thematic guidance for the direction of the weirdness.

Drawing both Jokers in a single pull (with one other card for guidance) is rare enough (~0.2%) to feel significant. When it happens, pay attention. The story just shifted under your feet.

---

## THE RULES

### Rule #1: Play
As long as you're having fun and the story is moving, keep going. Don't interrupt a good thing.

### Rule #2: Draw
Any time the momentum sags, draw some inspiration. The oracle is here to restore flow, not interrupt it.

---

## ASKING THE ORACLE

<!-- @@DECISION C — RESOLVED: the Aperture Principle is kept in both
     places deliberately (brief intro + full treatment). -->

### The Aperture Principle
The player controls how much the oracle can do with any given draw.

**Narrow question → narrow answer.**
*"Does the market have a better sword I can buy?"* - Valid, but limits the oracle to answering exactly that. The cards get conscripted into a yes/no inventory check.

**Open prompt → open scene.**
*"I need a better sword - I head to the market."* - Lets the cards build an event rather than answer a question. The result will often surprise you.

The most open and freeform application isn't a question at all. It's a prompt: *"I do this. What happens?"*

Neither approach is wrong. Narrow questions are useful when you need a specific answer. Open prompts are useful when you want the story to go somewhere you didn't expect. Find your own comfort level and vary your aperture as the story demands.

**The more specific your question, the more limited and specific the answer. That's a feature, not a bug.**

---

## THE DRAWING OF THE THREE

Three cards is the cardinal response. Draw three, then ask: *how could these three cards be read to produce an interesting event for the story?*

Three cards provides:
- Enough direction to build a scene
- Enough variation to generate surprise
- Enough pattern for human instinct to work with
- Speed - draw, read, play

Single card draws are valid for simple questions when you don't want more than a direct answer. Three is the default.

**Probability note**: Each Joker appears with ~1.85% probability per single draw. Drawing three cards raises the chance of hitting at least one Joker to ~10-11%.

---

## THE SHUFFLE

Shuffle between every Drawing of the Three as a "soft" rule of thumb. This keeps the draw genuinely random and prevents the deck from becoming predictable.

When things get really interesting, take a moment to stop and savor the tension. Call for a reshuffle - it forces you to sit and think about what's happening rather than just dealing cards. **Any time you can say "I haven't seen many Hearts for a while" is a sign it's been too long since you shuffled.**

Forgetting to shuffle in a tense, fast-moving scene is fine. You can call it fate, but shuffling creates fate too. The same card appearing repeatedly is the deck telling you something - pay attention.

### Advanced Options @@(sidebar)
- **Multiple decks**: Shuffle two or three standard decks together to extend meaningful randomness and change Joker odds significantly.
- **Card removal**: Remove specific cards to deliberately adjust odds. Want two Xb and one Xr? Take one out of a two-deck stack. Experienced players can tune their deck to suit their campaign.

---

## POSITIONAL READING
*(Optional Tarot Layer)*

Standard playing cards don't reliably show orientation, so traditional Tarot reversals aren't directly available. As an optional layer, card position within a Drawing of the Three can do equivalent work:

- **First card**: The face of the situation - what's present and visible
- **Second card**: The pivot - the complication or turning point
- **Third card**: The shadow - consequence, hidden element, complication

No modification to the deck required.

### CONSECUTIVE CARD RULE

When two cards of the same suit or rank appear consecutively in any layout or draw sequence, lay the second card sideways to indicate a modified or complicated "inverted" reading. This introduces pseudo-reversals organically from the flow of play without requiring card marking.

---

## THE HAIL MARY

Sometimes three cards just don't fit together. That's fine. Don't force it.

Drop the card that's causing the trouble and read the other two. The irreconcilable draw is the oracle telling you something unexpected - treat the dropped card as a free Joker if that's useful, or simply ignore it and move on.

No redraw. No replacement. Keep playing.

---

## RESOLUTION MECHANICS

<!-- L1 rules; EL6 draws 6 cards, counts the reds. -->

The oracle generates story. Resolution mechanics determine whether a character's specific competencies change the outcome of a specific action.

**Most of the time, you don't need them.** The Draw carries the narrative weight and player decisions flow naturally from the story. Resolution mechanics are available on demand - zoom in when the outcome of a skill-dependent action matters enough to make the character's abilities relevant to the result.

### When to Invoke Resolution

Ask yourself: *does it matter whether this specific character succeeds or fails at this specific thing, and would a more or less competent character get a different result?*

If yes, invoke resolution. If the story works either way, keep drawing.

Good candidates for resolution: active combat, a critical negotiation, a risky stealth approach, a complex repair under pressure. Poor candidates: basic travel, anything where the character has no particular skill, or anything the oracle is already handling well.

### Hooks in Resolution

Once per scene, add your Hook's rank as a bonus to any diceless or pool resolution where the Hook is clearly relevant. A Hook of rank 2 adds 2 to your effective EL for that resolution - either raising your diceless threshold or adding cards to your pool draw. This can be split into smaller bonuses across multiple rolls within the same scene.

*Example: Calder's "Instinctively protects people who can't protect themselves" is rank 1. Hustling an injured Maret to safety could apply that +1 to his Athletics EL, raising his diceless threshold from 3 to 4 and his pool from 3 cards to 4.*

### Luck Tokens in Oracle Play

Luck Tokens work in oracle play exactly as in standard L1, with one additional application - a Token may be spent to convert any drawn card to Hearts. Same rank, best possible outcome: Yes, *and*.

Spend the Token *after* seeing the draw. You always know what you're buying.

**Oracle draw**: Spend a Token, get Hearts - Yes, *and* - same rank, best possible narrative outcome. A 9C becomes 9H. A 4S becomes 4H. Simple and unambiguous.

**Resolution roll**: Spend a Token for the best possible roll - maximum reds, optimal performance. This still might not be enough against opposition that significantly outclasses you. You're buying the best your character can do, not a guaranteed win.

The player has to read the situation before spending. Against manageable opposition a Token on a resolution roll may be overkill - save it for the oracle flip where it guarantees the narrative outcome you need. Against something that vastly outclasses you, even a perfect roll loses, and a Token on the oracle result might hand you a win that the numbers couldn't.

Some players feel that if a full resolution roll *could not* succeed, spending a Token for an oracle win is an unfair result. Others feel that Luck can always hand you a win regardless of the numbers. Both positions are valid. You're running your own game - use the tools the way that serves your story.

### Diceless Resolution

The simplest resolution method requires no separate roll at all. Compare the character's relevant EL directly against the rank value of the opposing card. Higher wins. Ties go to the defender.

The Drawing of the Three often produces multiple actors in a single scene - each pip card potentially representing a separate opponent or obstacle, resolved in sequence against the character's EL. Face cards don't carry numeric values but describe the nature and identity of what's present - they characterize the scene and its participants while the pip cards do the mechanical work.

*Example: A gate entry draw of 8C, 2C, KS produces three separate beats - the 2C gate guard (EL 2, conflict texture), the 8C commander who notices something wrong (EL 8, conflict texture), and the KS as a named significant figure whose involvement colors everything. Calder's Level 3 beats the guard easily but loses badly to the commander. The KS tells us why the situation resolves anyway.*

This also builds NPCs organically. When a card's value beats your EL in a social context, note it - that character just demonstrated a competency. Maret's 7H in a social scene is now her Performer EL until demonstrated otherwise.

### Setting Opposition from the Draw

When the oracle presents an opponent or obstacle requiring resolution and diceless comparison isn't sufficient:

**Pip cards (A through 0)**: Rank value is the opposing EL directly. Ace = 1 through 9, with 0 = 10.

**Face cards**: Use pip card values for EL. Read face cards for narrative context, NPC characterization, and scene texture. Face cards are almost always gifts - they build your world while the numbers do the mechanical work.

**In-context bonuses**: A yes/and draw describing a tactical advantage can be quantified by a quick color run. Draw cards one at a time until you hit black; count the reds. That's your situational bonus EL. The narrative describes where it came from.

### All Face Cards: The Vote

When a Drawing of the Three produces no pip cards at all, numeric resolution is impossible. Instead, the three cards *vote*. Majority determines success or failure; suits texture the result.

- **3 red**: Decisive success - suits describe how good
- **2 red, 1 black**: Success with complication - the black suit colors it
- **2 black, 1 red**: Failure with silver lining - the red suit colors it
- **3 black**: Decisive failure - suits describe how bad

Three No/ands is effectively a critical failure. Three No/buts is a thorough defeat with surprisingly generous consolation prizes. Three face cards in any draw strongly indicates seemingly miraculous or arcane involvement - fate itself is weighing in rather than simple skill opposition.

### The Resolution Roll 

You can emulate L1's Simple Pool when not using "diceless" contests.

Once opposing EL is established, both sides draw cards equal to their EL from the top of the deck. Count reds. Higher count wins. Effect equals winner's count minus loser's count. Ties go to the defender.

**Extra Effort**: Before drawing, a player may declare Extra Effort and draw additional cards beyond their EL. Each extra card raises the potential maximum but not the bust threshold - any total exceeding the original EL is a catastrophic failure (effective score of zero). The sweet spot is roughly EL plus up to half again; beyond that, bust risk climbs faster than expected gain.

*Example: Calder's EL is 7. Drawing 10 cards shifts the bell curve toward 5 reds without too dramatically increasing bust risk. Drawing 14 would push maximum potential higher but make a bust as likely as success.*

### Oracle and Resolution Working Together

The oracle's suit and texture colors the *shape* of a result independent of the resolution roll. A red card draw that nonetheless produces a failed roll means the character failed this specific task, but the broader situation still trends to their benefit. A black card draw with a successful roll means competence won the moment but the scene still turns against them. Both layers speak simultaneously and neither cancels the other.

When player creativity produces a solution that changes the tactical situation entirely - an improvised diversion, an unexpected use of environment, a piece of information that reframes the problem - the oracle resolves whether it works. The resolution mechanics handle what the character's *skills* determine. They serve different questions.

### Token Resolution - Pure Oracle Combat & Conflict

*A standalone resolution system requiring no external dice or mechanics. Compatible with any game system or none at all.*

Each participant in a conflict begins with a number of tokens equal to their relevant rating - skill level, competence rank, or any agreed measure of capability. Higher rating means more buffer, not guaranteed victory.

Each round, one or both sides draw a card. Apply the suit result before continuing:

| Suit | Effect |
|---|---|
| **Hearts** | You +1 token, opponent -1 token |
| **Diamonds** | You +1 token, opponent +1 token |
| **Spades** | You -1 token, opponent -1 token |
| **Clubs** | You -1 token, opponent +1 token |

When both sides draw simultaneously, apply both results before checking status. A Hearts draw against a Clubs draw produces a net swing of 4 - every token moves in the same direction. A Diamonds draw against a Spades draw cancels completely in tokens, though the story of mutual growth versus mutual attrition reads very differently.

**Down**: When a participant cannot pay a token they owe, they are Down. The conflict is resolved against them.

Conflicts end when someone is Down, surrenders, flees, or when story circumstances change the situation entirely. Not every conflict requires a Down result - an exit that doesn't require hitting zero is almost always available.

Skill provides a buffer, not a guarantee. A weaker opponent drawing well can grind down a stronger one. That's honest.

### Running Out of Numbers

If the deck runs long enough without a reshuffle that no pip cards remain available for opposition, the Vote is the only tool left. If you notice this approaching, it merits a reshuffle. If you don't notice in time - the Fates have spoken, and you live with the result. A deck running dry on numbers means the world has gone strange. Fate is making decisions without consulting the laws of physics.

---

## PLAY EXAMPLE - Session One: Ashfen

<!-- Present only in the working draft. Carried through verbatim.
     @@ Candidate for its own page / appendix when this becomes /TS/ pages. -->

*Calder, a disgraced soldier turned itinerant scholar, arrives at the market town of Ashfen. The following draws occurred across one session, showing the oracle carrying narrative weight without requiring resolution mechanics at any point.*

**Opening prompt**: "Calder arrives at Ashfen. Something feels wrong. What's happening in the market?"
Draw: 9C, 2S, 6C - Three black cards. A knowledgeable dangerous presence controls the square. Someone is watching with patience and precision. Trained muscle is available. The market is *owned*.

**Tavern scene**:
Draw: JS, KH, 7D - The working crowd is closed, but the tavernkeeper is an unexpected find - educated, warm, knows everything. Work is available but carries a hidden price.

**Kennelmaster investigation**:
Draw: 6C, KS, 6D - Trained animals deployed as weapons on the road. The same Spellweaver presence appears again. A Beast Handler in a commercial context knows what's out there and will talk - for a price.

**Getting out of the garrison**:
Draw: 9S, 6D, 7S - Nothing opens easily but nothing closes either. The kennelmaster's scent object brings the dogs to Calder. A patrol window exists.

**Who comes down the stairs**:
Draw: 8C, 2D, KS - The garrison commander himself. Methodical, professional, trained underneath the scholar's robes. The King of Spades appears for the fourth time.

*Note: The KS (Artificer's Workaround) appearing four times across an unshuffled sequence became the spine of the entire session - the same figure haunting every draw until he walked down those stairs. This is the deck telling a story. Pay attention when it repeats itself.*

**The commander's answer**:
Draw: AH, 3C, QS - He warned one person already at personal cost. His cover is completely burned. The Harpy's Bargain - a Conjuror working through existing channels - is the only path forward. Someone in the next town who can move where he cannot.

**Session end**: Calder has a quest, an uneasy patron, a woman who needs extracting, four dogs, and more questions than answers. Resolution mechanics were available throughout and never necessary.

---

## PLAY EXAMPLE - Session Two: The Road from Ashfen

*Showing resolution mechanics in play. Calder is Level 3, combat and investigation EL 7, stealth EL 5. He extracted the tavernkeeper between sessions.*

**Opening draw** (what happened during extraction): 8H, 6S, 3C - She came willingly with a packed bag. Getting the dogs through Ashfen's streets took longer than wanted. Someone was watching the tavern and saw them leave - and didn't move to stop them. Worse, somehow.

**Something is following them**:
Draw: AC, 9D, 4D - She doesn't know what it is but has seen it work before. Calder's border war experience identifies it as a bound construct, anchored to a physical object. There's a way past it but the cost lands on someone else.

*The message cylinder on Calder's belt is the anchor. The construct was sent to follow it.*

**Calder circles back through the trees** - Sneak, Shadowing, EL 5. Rather than invoke resolution for a scouting action that the story doesn't require him to fail, the player draws instead.

Draw: 4H, KS (fifth appearance), Xb - Calder gets eyes on it cleanly. It is not a man. It tracks by scent the same way the dogs do. The Artificer's Workaround appears for the fifth time - this is what the commander's three-year-old deal created. The Black Joker says the story just shifted again.

**Running for the river** - resolution mechanics earn their place. The construct is faster than Calder on open ground and closing.

Draw for opposition EL: 7S, JC, 5H - The JC (face card) is ignored for EL purposes. Two pip cards: 7 and 5. The 7S fits the construct's supernatural speed as opposition. The 5H is a yes/and - the dogs create a genuine scent diversion, quantified by a color run of five cards: b,r,r,r,r = 4 reds. Calder's EL shifts from 3 (Level only, no Athlete) to 7 with the dog bonus.

**The roll**: Calder declares Extra Effort, drawing 10 cards against the construct's 7.
- Calder: 0S QC AC KC 7C 5D 6H 3H 4H KD = **5 reds**
- Construct: 8S 8C QH 0D 6D 4D 8H = **5 reds**

Dead even. The construct negates Calder's lead and closes to the water's edge.

**Player creativity changes the situation**: Rather than spend a Luck Token, Calder throws the message cylinder downstream into the river. Three competing scent signals at the water's edge. The oracle resolves whether it works.

Draw: 6D, 0S, 8H - The gambit works but Diamonds insists on a cost - the tavernkeeper crosses but falls, injured. The construct isn't fully fooled but is methodically sorting signals, buying a window. The big dog helps the tavernkeeper stand. They cross. They move. The construct eventually chooses the cylinder downstream.

*The resolution mechanics determined the crunch moment. Player creativity resolved the impasse without burning a Token. The oracle colored the shape of everything around it.*

---

## CALDER - Sample Character (End of Session Two)

*Disgraced soldier, itinerant scholar. Fought in a border war, got curious about why it was happening, got drummed out for asking inconvenient questions.*

**Level 3** | **2 Karma** (1 session start + 1 triggered Hook this session)

| Ability | Rank | Maneuvers |
|---|---|---|
| Warrior | 2 | Swordplay 2 |
| Loremaster | 2 | Local Histories 2 |
| Sneak | 1 | Shadowing 1 |

**Combat EL**: 3+2+2 = **7**
**Investigation EL**: 3+2+2 = **7**
**Stealth EL**: 3+1+1 = **5**

**Hooks** (all rank 1):
- "Can't leave a question unanswered"
- "Instinctively protects people who can't protect themselves" *(triggered this session)*
- "Doesn't trust authority - any authority"

**Known NPCs:**
- **Maret** (tavernkeeper, unnamed until Session Two) - Performer EL 7 demonstrated. Carries a second list. Injured ankle. Hasn't explained everything yet.
- **The Ashfen Commander** - Spellweaver. Level unknown, EL unknown. Made a three-year-old deal he cannot unmake. Sent them toward a Conjuror in the next town.
- **The Construct** - Athletics EL 7 demonstrated. Tracks by scent, anchored to physical objects. Single-minded. Operational range unknown. Currently following a message cylinder downstream.

**Current situation**: One day out of Ashfen, dawn, moving on foot with four dogs and an injured Maret. Destination: the next town, and a Conjuror who can move where the commander cannot.

---

## CARD SPREADS

*A spread is a structured layout that assigns positional meaning to each card drawn. Where the Drawing of the Three reads cards as a group, a spread reads each card independently through the lens of its position. The position provides context; the card provides content.*

*The spreads below are inspired by traditional Tarot layouts, adapted for a standard deck without Major Arcana or reversals. Each spread description notes its inspiration where applicable.*

*When using any spread, observe the consecutive card rule: any time two cards of the same suit or rank appear consecutively in a layout, lay the second card sideways to indicate a modified or inverted reading.*

### Question Framing for Spreads

Spreads reward deliberate questions. Before drawing, the Quaerant should:

**Be specific but *not* binary.** "Will I succeed?" closes the reading before it opens. "What do I need to understand about my pursuit of X?" invites genuine revelation.

**State the stakes.** A reading without acknowledged stakes is just card drawing. Know what you're actually asking about and why it matters.
Traditional Tarot says to state *intention*. Traditional gaming says for there to be *stakes*, or you shouldn't bother to roll. If there are no significant stakes, the Quaerant knows the draw is merely a random nudge; if stakes are stated, the draw affects them directly. "If I don't manage to find a way to open this door before the water level rises above the handle we will probably drown. What do I see that might help?"

**__One__ question per reading.** The spread answers one thing deeply rather than several things shallowly.

**Invite surprise.** If you already know the answer you want, the reading will only confirm your bias. The best questions are genuinely open to unexpected responses.

---

### The Quaerant's Mirror

*The simplest possible reading. One card, one question, one answer.*

*(Inspired by single-card Tarot draws)*

Draw one card. Read it in full - color, suit, rank, and named interpretation. The Mirror shows exactly what it shows and nothing more. This reading requires the most interpretive skill of any spread; there is nothing else to balance against.

*Use when*: a specific focused question has a single answer worth knowing. Not for complex situations - for moments of clarity.

---

### The Three Card Spreads

*Three positions, three cards, one question. The same layout serves multiple interpretive frameworks - choose the one that fits the question.*

*(Inspired by traditional three-card Tarot spreads)*

Draw three cards and place them left to right. Interpret each through its position:

**Timeline**: Past - Present - Future
What shaped this situation, what is actually happening now, what is already building.

**Situation**: Problem - Obstacle - Resolution
What the core issue is, what stands in the way, what the path through looks like.

**Action**: Situation - Action - Outcome
What is true right now, what the Quaerant should consider doing, what follows from that action.

The three cards can also be read as a group using standard Drawing of the Three methodology when positional meaning feels too constraining.

---

### The Relationship Spread

*Three cards examining two people and the dynamic between them.*

*(Original)*

Draw three cards and place them left to right:

**Position 1 - The First Party**: What this person wants, fears, or brings to the relationship.
**Position 2 - The Dynamic**: What is actually happening between these two people. What neither may fully see.
**Position 3 - The Second Party**: What this person wants, fears, or brings to the relationship.

*Use when*: generating NPC motivations, understanding political tensions, examining any situation where two forces are in relationship with each other. The middle card is often the most revealing - it describes the space between rather than either party directly.

---

### The Quaerant's Tower

*A six-card spread for significant questions with real stakes. Named in honor of the Tarokka fortune-telling tradition from Ravenloft.*

*(Inspired by the Tower spread from the Ravenloft Tarokka deck, adapted for standard playing cards without Major Arcana or reversals)*

**Before shuffling - The Quaerant Card:**
Choose one card to represent the seeker and set it aside. This choice is meaningful - the card removed from the deck changes the probability distribution of what remains. A warrior who chooses the AC (Berserker's Rampage) to represent themselves removes conflict from the deck's Clubs. One who chooses AH (Champion's Glory) removes social generosity. The Quaerant is literally betting something on their self-image before the reading begins.

The choice can be made deliberately (selecting a card that feels true to the character) or randomly (drawing until a card feels right). Either method has a cost.

**The Question:**
State the question clearly before drawing. Follow the question framing guidelines above. The Tower rewards specific, open, stakes-acknowledged questions.

TOWER LAYOUT: 
```
              [6. POTENTIAL]

[2. OBSTACLE] [5. FUTURE  ]
laid across

[1. GOAL    ] [4. PRESENT ]

              [3. PAST     ]
```

**The Layout:**
Shuffle and cut the remaining deck. Lay cards in order:

**1. The Goal** - center left. What the Quaerant is actually trying to achieve. May not be what they think they're trying to achieve.

**2. The Obstacle** - laid sideways across the Goal. What stands between the Quaerant and their Goal. Treated as inverted - its energy is working against rather than with.

**3. The Past** - bottom right. The history that shaped this situation. What has already happened that cannot be changed.

**4. The Present** - middle right, above Past. What is actually happening now. The truth of the current moment.

**5. The Future** - top right, above Present. Events already building that have not yet arrived. Not fate - tendency.

**6. The Potential** - above or apart from the column. What becomes possible if the Quaerant acts with wisdom on what the spread reveals. This card is read last and interpreted through everything that preceded it.

*The cross on the left holds the immediate problem. The column on the right holds time. The Potential sits above both.*

---

### @@ Spreads Still to Consider
- Four and five card spreads *(under consideration)*
- Anything more complex than the Tower is probably beyond scope

---

## THE CARD LEXICON

*What follows is an interpretive reference for every card in the deck. Each entry combines Role, suit texture, and thematic domain into a named card with a brief reading.*

*These names and readings are offered as starting points, not constraints. The same card reads differently in every context - a Warrior draw in a social scene means something very different from a Warrior draw mid-combat. Let the name suggest an angle, then follow the story.*

*Non-L1 users: the Role associations can be set aside entirely. Read each card purely from its name, texture, and the brief interpretation provided.*

<!-- @@DECISION E — RESOLVED: rich prose (below) is the canonical lexicon;
     a tabular reference index + dedicated per-card pages are planned (see
     the build comment just below). The seed's compact table is stashed in
     TS/_stash/lexicon-table-synoptic.md as seed material for the index. -->

<!-- We need a single page with a columnar/tabular reference chart with the more simplistic representations, but each should link to a dedicated page with the fuller, more expansive text and the graphic of the card. The full page versions should include multiple interpretations where possible (Razor's Nick, immediately below), and examples of inverted/alternate versions. See https://labyrinthos.co/blogs/tarot-card-meanings-list/the-fool-meaning-major-arcana-tarot-card-meanings for one decent example; https://biddytarot.com/tarot-card-meanings/major-arcana/fool/ for another; https://www.thetarotlady.com/tarot-card-by-card-the-fool/ for a very different one. -->

*@@ Revision pass needed: each card should carry at least two valid interpretations. The name itself should support both readings without requiring explanation. Example: Razor's Nick could mean a nick in the razor's edge (the tool is compromised) or a nick caused by the razor (you paid in blood for the precision). Both readings are Yes/but. Both are Tinker. The ambiguity is the feature.*

---

### The Face Cards

Face cards represent arcane or exceptional forces. When face cards dominate a draw, something beyond the mundane is at work. Three face cards with no pip values invokes the Vote - the Fates themselves are weighing in.

The face cards are organized into three registers: the wild and intuitive (Jacks/Adepts), the institutional and powerful (Kings/Spellweavers), and the negotiating and transformative (Queens/Conjurors).

#### The Jacks - Adepts

*Intuitive power, internal fire, flexible and unpredictable. The Adept doesn't follow rules - the Adept follows instinct.*

**JH - Bard's Ode** *(Yes, and - Social)*
A gift freely given, a story that opens doors. Someone's charm or talent is working entirely in your favor, and the benefit ripples outward beyond what was asked. Accept it gracefully.

**JD - Prophet's Levy** *(Yes, but - Commercial)*
The vision was accurate, the path is clear - but the Prophet collects his due and you didn't get a say. Success arrived with an invoice attached. Pay it and move on.

**JC - Soothsayer's Hex** *(No, and - Conflict)*
The truth was spoken and it cut deep. Someone saw something they shouldn't have, and now the knowing has teeth. Things are worse for the revelation, not better.

**JS - Friar's Indulgence** *(No, but - Labor)*
You didn't earn this. The ledger says no, the merit says no, and yet here is a pass, slightly corrupt and entirely functional. Don't examine it too closely. Walk through.

---

#### The Queens - Conjurors

*Negotiation, transformation, deals with powers seen and unseen. The Conjuror works at the edges of what's possible - and charges accordingly.*

**QH - Enchantress' Boon** *(Yes, and - Social)*
A gift from someone who didn't have to give it. Charm, grace, and genuine generosity flowing your direction. Something social blooms unexpectedly. Enjoy it - these moments are rarer than they look.

**QD - Sibyl's Price** *(Yes, but - Commercial)*
The Sibyl's prophecies were always accurate and always costly. You got what you came for. The price was higher than quoted, and the Sibyl is already counting it out. Worth it, probably. Probably.

**QC - Witch's Curse** *(No, and - Conflict)*
Not merely opposition - deliberate, targeted, personal. Someone with real power decided you specifically are the problem. The conflict that follows has weight and intention behind it.

**QS - Harpy's Bargain** *(No, but - Labor)*
Unpleasant terms, uncomfortable company, a deal struck in circumstances nobody would have chosen. And yet the Harpy held up her end. You got something out of this. Perhaps more than you expected, if less than you wanted.

---

#### The Kings - Spellweavers

*Institutional authority, bound power, academic mastery. The Spellweaver operates through systems - guilds, writs, constructs, commissions. Powerful, impersonal, and thorough.*

**KH - Guildmaster's Favor** *(Yes, and - Social)*
Institutional approval, freely and publicly given. Someone with real organizational authority has decided you are useful, trustworthy, or simply worth backing. Doors open. People notice.

**KD - Magister's Fee** *(Yes, but - Commercial)*
The knowledge was accurate. The work was done correctly. And the Magister's invoice is already waiting on the desk. Academic authority always charges for its services, and the fee structure is non-negotiable.

**KC - Inquisitor's Writ** *(No, and - Conflict)*
The full weight of organized authority, properly documented, coming down. This isn't personal - it's institutional. Which makes it worse. The Inquisitor has paperwork.

**KS - Artificer's Workaround** *(No, but - Labor)*
Something bound and purposeful is working against you, methodically and without malice. But somewhere in the mechanism there's an improvised patch, a jury-rigged solution, a crack in the construct. It won't last. It doesn't need to.

---

### The Pip Cards

*The mundane world in all its texture. Pip cards represent everyday forces, skills, and people - the fabric of the story rather than its exceptional moments.*

*Names follow the [Role-evocative title] + [Texture-evocative noun] convention. Read each card from its name and brief interpretation, then let the story context do the rest. These are starting points, not constraints.*

*Cards are listed in order: H (Yes/and), D (Yes/but), S (No/but), C (No/and)*

---

#### The Aces - Warriors

*The bluntest instrument in the deck. Direct, physical, immediate. As opposition, an Ace represents a single guard, a common brawler, a drunk with a knife - low threat, high directness.*

**AH - Champion's Glory** *(Yes, and - Social)*
The fighter's triumph spills over into celebration. The crowd is cheering and something beyond victory arrives with it.

**AD - Mercenary's Wage** *(Yes, but - Commercial)*
The sword arm won the day. The invoice is already on the table. Victory arrived with a contract attached.

**AS - Duellist's Evasion** *(No, but - Labor)*
The blade arm failed but the footwork saved you. A skilled retreat, not a rout. You know more about your opponent now.

**AC - Berserker's Rampage** *(No, and - Conflict)*
Something let loose and made everything worse. The violence escalated past any useful point and kept going.

---

#### The Twos - Snipers

*Precision, patience, distance. As opposition, a 2 represents a watchman on a wall, a careful observer, someone who sees without being seen.*

**2H - Scout's Report** *(Yes, and - Social)*
Intelligence delivered cleanly, and more than was asked for. Someone was watching and what they saw benefits you.

**2D - Marksman's Reload** *(Yes, but - Commercial)*
The shot landed. Now there's a pause, a cost, a moment of vulnerability while the mechanism resets.

**2S - Catapult's Misfire** *(No, but - Labor)*
The mechanism failed but something useful landed in the chaos anyway. Perhaps not where intended. Perhaps better.

**2C - Arbalest's Volley** *(No, and - Conflict)*
Heavy, mechanical, and it's still coming. The assault didn't stop and it made things considerably worse.

---

#### The Threes - Performers

*Emotional manipulation, social influence, entertainment. The Performer register is warm, slippery, and deeply human.*

**3H - Actor's Roses** *(Yes, and - Social)*
The crowd threw flowers. The performance landed and then some - warmth and generosity flowing back from an appreciative audience.

**3D - Mentor's Critique** *(Yes, but - Commercial)*
The performance worked. Now here are the notes, the expectations, the required improvements. Success with an invoice of obligations attached.

**3S - Reviewer's Nostalgia** *(No, but - Labor)*
The review wasn't favorable, but something in the performance triggered a memory in someone who matters. An unexpected benefit from an accidental angle.

**3C - Heckler's Victory** *(No, and - Conflict)*
The performance failed and the room turned. The heckler has the crowd now. Social no/and at its most pointed.

---

#### The Fours - Sneaks

*Concealment, stealth, moving undetected. This register is quiet, shadowy, and carries real consequence.*

**4H - Spy's Package** *(Yes, and - Social)*
The intelligence arrived and something extra was tucked inside that nobody expected. More than was asked for, delivered cleanly.

**4D - Assassin's Compulsion** *(Yes, but - Commercial)*
The job is done. But now you're bound to something - a debt, a secret, a handler who knows what you did. The compulsion doesn't release.

**4S - Prisoner's Map** *(No, but - Labor)*
Failed, confined, seemingly stuck. And yet someone scratched a way out in the dark. It's there if you look.

**4C - Burglar's Ligature** *(No, and - Conflict)*
Caught and bound, and things are actively getting worse. The ligature is doing real work.

---

#### The Fives - Naturalists

*Wilderness survival, tracking, environmental knowledge. Grounded, physical, and honest about what nature provides and what it takes.*

**5H - Forager's Bounty** *(Yes, and - Social)*
Nature provided more than asked. The land is generous today and something extra came with the harvest.

**5D - Wayfarer's Pack** *(Yes, but - Commercial)*
You have what you need. It's heavy, it costs, and it slows you down. The pack is both resource and burden.

**5S - Herbalist's Antidote** *(No, but - Labor)*
The situation is bad but here is something specific that addresses the harm. Quiet, practical, bought time if nothing else.

**5C - Mountaineer's Avalanche** *(No, and - Conflict)*
Unstoppable, impersonal, and it absolutely made everything worse. The mountain didn't even notice you.

---

#### The Sixes - Beast Handlers

*Animal training, communication, and partnership. These cards read from the perspective of whoever draws them - the animal is sometimes ally, sometimes obstacle, sometimes predator.*

**6H - Ox Team's Calf** *(Yes, and - Social)*
The labor partnership produced something new and valuable beyond the work itself. A future asset arrived unexpectedly.

**6D - Courser's Re-shoeing** *(Yes, but - Commercial)*
You got where you needed to go. The horse needs attention before you go anywhere else. Time and coin and the farrier's schedule.

**6S - Hounds' Fault** *(No, but - Labor)*
The hunting term for losing the scent. The hounds failed the immediate task but their last heading is information worth following.

**6C - Grizzly's Pursuit** *(No, and - Conflict)*
You are the prey. The pursuit is relentless and it made everything worse. Distance is your only friend right now.

---

#### The Sevens - Athletes

*Physical excellence, endurance, athletic feats. Kinetic and human - the body's triumphs and failures under pressure.*

**7H - Victor's Laurels** *(Yes, and - Social)*
Classical and generous. The crowd is cheering and the laurels are real. Everything that comes with public triumph arrives at once.

**7D - Competitor's Fee** *(Yes, but - Commercial)*
You placed, you earned. The entry fee, the trainer, the equipment all have their hands out. Success with an immediate practical invoice.

**7S - Runner's Consolation** *(No, but - Labor)*
Didn't win, didn't place, but finished. There's something in that. Quiet dignity in the effort when the result wasn't there.

**7C - Dropout's Disgrace** *(No, and - Conflict)*
Not just losing but the public consequence of failing to finish. The crowd that cheered in 7H is silent or worse here.

---

#### The Eights - Healers

*Medical treatment, recovery, wound care. This register carries more weight than most - a failed Healer draw means someone might not recover.*

**8H - Nurse's Handfasting** *(Yes, and - Social)*
The healer and patient bound together through the act of care. A tie formed that wasn't there before, warm and lasting.

**8D - Remedy's Addiction** *(Yes, but - Commercial)*
The remedy worked. Now you need it and that need has teeth. The success keeps costing in ways that weren't on the label.

**8S - Hollow Leg** *(No, but - Labor)*
The medicine went in and nothing changed. The patient is still upright, still moving, still here. Failed healing that somehow left something intact.

**8C - Apothecary's Grief** *(No, and - Conflict)*
The treatment failed and the condition worsened. The professional who understands exactly what went wrong has to live with that knowledge.

---

#### The Nines - Loremasters

*Information synthesis, research, investigation. Cerebral and curious - and occasionally dangerous in the way that knowing things is dangerous.*

**9H - Librarian's Recommendation** *(Yes, and - Social)*
The research succeeded and the librarian liked you enough to send you somewhere better. Information that leads to more information.

**9D - Investigator's Attention** *(Yes, but - Commercial)*
You found what you were looking for. Someone noticed you looking. Professional interest is now aimed in your direction.

**9S - Sage's Rescheduling** *(No, but - Labor)*
The Sage couldn't see you today. The knowledge is delayed, not denied. The appointment exists. Progress without result.

**9C - Censor's Torch** *(No, and - Conflict)*
The knowledge existed, you found it, and now it's ash and you're known for having looked. Everything got worse the moment the torch fell.

---

#### The Tens - Tinkers

*Crafting, mechanical repair, technical problem-solving. Hands-on and practical - the satisfaction and frustration of making things work.*

**0H - Alchemist's Discovery** *(Yes, and - Social)*
The experiment worked and produced something nobody expected. Intellectual generosity flowing outward from a successful making.

**0D - Razor's Nick** *(Yes, but - Commercial)*
The tool is sharp, the work is done, and there's a small precise cost attached. Almost incidental. Almost.

**0S - Engineer's Salvage** *(No, but - Labor)*
The mechanism failed but the parts are recoverable. Something useful remains from the wreckage. Practical hope.

**0C - Miller's Fire** *(No, and - Conflict)*
The mill burned. Flour dust and millstones and the particular horror of grain fires that spread fast and take everything.

---

## @@TODO — TESSERAE SORTIS SUBSITE

**Editing & tone (whole subsite)**
- Working initialization copy; the whole text needs **multiple editing / revision passes** before publication.
- **Sensitivity watch** — catch and smooth subtle insensitivities without breaking the basic traditional feel of the rules.

**Build (page-out)**
- **Per-card pages**: add the multiple-interpretations + inverted/alternate sections to each frame.
- **Tabular reference index**: columnar code · name · one-liner chart linking to each card page (seed: `TS/_stash/lexicon-table-synoptic.md`).
- **"The machinery" page**: design-transparency + GM guidance (edit-notes N3; yourbias.is is CC BY-NC-ND — our own words only).

**Carried-through content TODOs**

- **Consecutive card rule**: Formalize completely. Currently described as principle only.
- **Lexicon revision pass**: Every card needs at least two valid interpretations supportable from the name alone without explanation.
- **Three card spreads**: Consider naming each variant formally (The Timeline, The Situation, The Action).
- **Additional spreads**: Four and five card options under consideration. Nothing more complex than the Tower likely within scope.
- **Tarot variant rules**: Full alternate version for players with a Tarot deck. Different day, separate section. Key differences: 14 cards per suit (Page added), 22 Major Arcana, reversals naturally available.
- **Integration notes**: Explicit callouts for Level One TTRPG use beyond what's covered in resolution mechanics.
- **Quick reference sheet**: Single page summary for actual play. Card meanings, spread layouts, resolution options.
- **Non-L1 resolution guidance**: How to adapt pool resolution for systems with different core mechanics, or use token resolution as complete standalone.
- **Introduction**: Design philosophy, Ford's safety glass principle, what makes this different from other oracle approaches (encoding meaning directly into card faces, aperture principle, oracle-as-event-generator rather than answer-machine).
