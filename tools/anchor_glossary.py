#!/usr/bin/env python3
"""Give every glossary term a real anchor, so any page can link to a definition.

Problem
-------
L1/glossary.html is a well-formed <dl> of term/definition pairs, but no <dt>
carries an id. There is nothing for the rest of the book to link to at term
granularity: a page mentioning Conceit or Wager can only send the reader to the
top of the glossary and leave them to scroll.

What this does
--------------
Adds `id="slug"` to every <dt> that lacks one. The slug follows the same rule as
tools/anchor_sections.py -- tags stripped, entities unescaped, lowercased,
apostrophes dropped, runs of non-alphanumerics collapsed to hyphens -- and that
rule is imported rather than restated, so the two tools cannot drift apart.

A <dt> that already has an id keeps it. Slugs are de-duplicated within the page.

The id sits on the <dt> itself rather than in a preceding
`<span class="section-anchor">`, because a <dt> is already a discrete element
and the span would be redundant. Headings still use the span, since an anchor
placed on an <h2> scrolls the heading out of view.

Usage
-----
  python tools/anchor_glossary.py            # dry run: report only, no writes
  python tools/anchor_glossary.py --apply    # write the ids
"""

import re
import sys
from pathlib import Path

# Same directory, so a plain import works when run as python tools/<this>.
# Importing keeps one definition of the slug convention.
from anchor_sections import slugify, strip

REPO = Path(__file__).resolve().parent.parent
GLOSSARY = REPO / "L1" / "glossary.html"

DT_RE = re.compile(r'<dt(?:\s+id="([^"]+)")?\s*>(.*?)</dt>', re.DOTALL)


def build_plan(text):
    """Return [(term_text, slug, already_had_id)] in document order."""
    plan = []
    used = {}
    for m in DT_RE.finditer(text):
        existing, inner = m.group(1), m.group(2)
        slug = existing or slugify(inner)
        if not slug:
            plan.append((strip(inner).strip(), None, bool(existing)))
            continue
        if slug in used:
            used[slug] += 1
            slug = f'{slug}-{used[slug]}'
        else:
            used[slug] = 1
        plan.append((strip(inner).strip(), slug, bool(existing)))
    return plan


def main(argv):
    apply = '--apply' in argv
    text = GLOSSARY.read_text(encoding='utf-8')
    plan = build_plan(text)

    todo = [p for p in plan if p[1] and not p[2]]
    kept = [p for p in plan if p[2]]
    skipped = [p for p in plan if not p[1]]

    print(f'terms found: {len(plan)}')
    print(f'anchors to add: {len(todo)}')
    for term, slug, _ in todo:
        print(f'  {term!r} -> #{slug}')
    if kept:
        print(f'\nalready anchored, left alone: {len(kept)}')
        for term, slug, _ in kept:
            print(f'  {term!r} -> #{slug}')
    if skipped:
        print(f'\nno usable slug, left alone: {len(skipped)}')
        for term, _slug, _ in skipped:
            print(f'  {term!r}')

    if not apply:
        print('\n(dry run -- rerun with --apply to write)')
        return 0

    it = iter(plan)

    def add_id(m):
        inner = m.group(2)
        _term, slug, had = next(it)
        if had or not slug:
            return m.group(0)
        return f'<dt id="{slug}">{inner}</dt>'

    new = DT_RE.sub(add_id, text)
    if new == text:
        print('\nno change.')
        return 0
    # newline='\n' to match .gitattributes eol=lf; text mode would emit CRLF
    # on Windows and make the output platform-dependent.
    GLOSSARY.write_text(new, encoding='utf-8', newline='\n')
    print(f'\nWROTE: {GLOSSARY.relative_to(REPO)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
