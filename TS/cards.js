/* ============================================================
   TESSERAE SORTIS — CARD MANIFEST & HELPERS
   Loaded after /TS/config.js (needs the global img() helper).

   The deck art lives on the CDN under cards/<code>.png at
   600x840 (5:7). Filenames are lowercase {rank}{suit}:
       as   = ace of spades        10h = ten of hearts
       qd   = queen of diamonds    jc  = jack of clubs
   Plus two jokers: joker1, joker2. (Card back: back.png — pending.)

   This module is pure data + URL helpers. No game logic lives
   here; the draw/spread/layout mechanics build on top of it.
   ============================================================ */

const TSCards = {

  RANKS: ['a', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k'],
  SUITS: ['c', 'd', 'h', 's'],

  SUIT_NAMES: { c: 'clubs', d: 'diamonds', h: 'hearts', s: 'spades' },
  RANK_NAMES: {
    a: 'ace', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
    j: 'jack', q: 'queen', k: 'king',
  },

  JOKERS: ['joker1', 'joker2'],
  BACK:   'back',   // cards/back.png — not yet uploaded

  /* "a","s" -> "as"   |   "10","h" -> "10h" */
  code(rank, suit) {
    return `${rank}${suit}`;
  },

  /* Full CDN URL for a card code: cardUrl("as") -> .../cards/as.png */
  cardUrl(codeStr) {
    return img(`cards/${codeStr}.png`);
  },

  /* Convenience: URL straight from rank + suit. */
  url(rank, suit) {
    return this.cardUrl(this.code(rank, suit));
  },

  /* Human-readable name: name("10","h") -> "ten of hearts" */
  name(rank, suit) {
    return `${this.RANK_NAMES[rank]} of ${this.SUIT_NAMES[suit]}`;
  },

  /* The 52 standard card codes, suit-major then rank order. */
  deck52() {
    const out = [];
    for (const s of this.SUITS) {
      for (const r of this.RANKS) {
        out.push(this.code(r, s));
      }
    }
    return out;
  },

  /* All 54 codes including both jokers. */
  deck54() {
    return [...this.deck52(), ...this.JOKERS];
  },

}; // end TSCards
