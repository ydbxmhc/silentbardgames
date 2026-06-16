#!/usr/bin/env python3
"""Rewrite .html hrefs in *.md files to .md hrefs.

Only touches Markdown link targets of the form:
  [text](some/path.html)
  [text](some/path.html#anchor)

External links (http/https/mailto) and already-.md links are left alone.
Anchors are preserved: foo.html#bar -> foo.md#bar

Usage:
  python tools/relink_md.py            # all *.md in the repo
  python tools/relink_md.py FILE...    # specific files only
"""

import re
import sys
from pathlib import Path

# Matches markdown links: [any text](the-href)
# Capture group 1 = href value
LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')


def rewrite_href(href):
    """Return href with .html -> .md, or unchanged if not applicable."""
    # Leave external and anchor-only links alone
    if href.startswith(('http://', 'https://', 'mailto:', '#')):
        return href
    # Split off any #anchor
    if '#' in href:
        path_part, anchor = href.split('#', 1)
        anchor = '#' + anchor
    else:
        path_part, anchor = href, ''
    if path_part.endswith('.html'):
        path_part = path_part[:-5] + '.md'
    return path_part + anchor


def rewrite_file(path):
    original = path.read_text(encoding='utf-8')

    def replace_link(m):
        text = m.group(1)
        href = m.group(2)
        new_href = rewrite_href(href)
        return f'[{text}]({new_href})'

    rewritten = LINK_RE.sub(replace_link, original)
    if rewritten != original:
        path.write_text(rewritten, encoding='utf-8')
        return True
    return False


def iter_md_files(repo):
    for p in sorted(repo.rglob('*.md')):
        if '.git' in p.parts:
            continue
        yield p


def main(argv):
    repo = Path(__file__).resolve().parent.parent
    if argv:
        files = [Path(a).resolve() for a in argv]
    else:
        files = list(iter_md_files(repo))
    changed = 0
    for md_path in files:
        if rewrite_file(md_path):
            print(f'relinked: {md_path.relative_to(repo)}')
            changed += 1
        else:
            print(f'unchanged: {md_path.relative_to(repo)}')
    print(f'\n{changed}/{len(files)} file(s) updated.')


if __name__ == '__main__':
    main(sys.argv[1:])
