#!/usr/bin/env python3
"""dedash.py - eradicate non-ASCII dashes from HTML source.

Em-dashes appear as the numeric entity &#8212;, the named entity &mdash;, or the
literal character U+2014; en-dashes as &#8211;, &ndash;, or U+2013. The house
style is a plain ASCII hyphen. This tool rewrites both while leaving arrows
(&#8592; / &#8594;) and everything else untouched.

Em-dash spacing rules (matching the author's hand-written style):
  word --- word   -> word - word     (spaced both sides)
  word---word     -> word - word     (tight between words gets spaced)
  <tag>--- Text   -> <tag>- Text      (lead-in dash keeps tight to the tag)
  ^--- Text       -> - Text           (line-leading dash)

En-dashes take a bare hyphen with the surrounding spacing left exactly as
written. They are used both spaced (as a parenthetical, like an em-dash) and
tight, for ranges -- "1060-1339px", "A-E" -- where forcing " - " would be
wrong. Preserving the spacing is correct for both.

Usage:
  python tools/dedash.py [PATHS...]          fix files in place
  python tools/dedash.py --check [PATHS...]  report only, exit 1 if any found

With no PATHS, defaults to every text file in the repo (recursively):
.html, .md, .txt, .css, .js, .json. The .git directory is skipped.
"""
import re
import sys
from pathlib import Path

EMDASH = re.compile(r'(.?)([ \t]*)(?:&#8212;|&mdash;|\u2014)([ \t]*)')

# Bare forms, for counting. EMDASH above consumes surrounding context and so
# cannot be used to tally occurrences.
EMDASH_ANY = re.compile(r'&#8212;|&mdash;|\u2014')
ENDASH_ANY = re.compile(r'&#8211;|&ndash;|\u2013')

TEXT_EXTS = {'.html', '.md', '.txt', '.css', '.js', '.json'}


def _repl(m):
    prev, lead, _trail = m.group(1), m.group(2), m.group(3)
    if lead:
        # there was whitespace before the dash -> spaced hyphen
        return prev + ' - '
    if prev == '>':
        # lead-in dash tight against an opening tag, e.g. <em>--- Text
        return prev + '- '
    if prev == '':
        # line-leading dash
        return '- '
    # tight between two non-space characters -> give it room
    return prev + ' - '


def dedash_text(text):
    text = EMDASH.sub(_repl, text)
    # Spacing preserved deliberately -- see the module docstring on ranges.
    return ENDASH_ANY.sub('-', text)


def find_dashes(text):
    """Return (em, en) counts of non-ASCII dashes present."""
    return len(EMDASH_ANY.findall(text)), len(ENDASH_ANY.findall(text))


def default_targets():
    root = Path('.')
    return sorted(
        p for p in root.rglob('*')
        if p.is_file() and p.suffix.lower() in TEXT_EXTS
        and '.git' not in p.parts
    )


def main(argv):
    check = False
    args = []
    for a in argv:
        if a == '--check':
            check = True
        else:
            args.append(a)

    targets = [Path(a) for a in args] if args else default_targets()

    offenders = 0
    changed = 0
    for p in targets:
        if not p.is_file():
            print(f'skip (not a file): {p}', file=sys.stderr)
            continue
        original = p.read_text(encoding='utf-8')
        em, en = find_dashes(original)
        count = em + en
        if count == 0:
            continue
        offenders += 1
        if check:
            print(f'{p}: {em} em-dash(es), {en} en-dash(es)')
            continue
        p.write_text(dedash_text(original), encoding='utf-8')
        changed += 1
        print(f'dedashed: {p} ({count})')

    if check:
        if offenders:
            print(f'\n{offenders} file(s) still contain non-ASCII dashes.')
            return 1
        print('clean: no non-ASCII dashes found.')
        return 0

    print(f'\n{changed} file(s) rewritten.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
