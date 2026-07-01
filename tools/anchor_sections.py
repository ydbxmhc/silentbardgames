#!/usr/bin/env python3
"""Give in-page subsections real anchors, and point TOC/nav sub-links at them.

Problem
-------
Many Table-of-Contents and nav-drawer entries point at a *subsection* of a page
using a bare `page.html` link (no #fragment), because that subsection was never
broken out into its own page. Readers clicking those land at the top of the page
instead of the section.

What this does
--------------
1. Reads `L1/toc.html` and `L1/nav.html`, finds every link to a bare
   `page.html` (no fragment).
2. A bare link is a *page* link if its text matches that page's <h1> -- leave it.
   Otherwise it's a *subsection* link: find the heading (h2/h3/h4) on the target
   page whose text matches the link text.
3. For a matched heading with no id, insert an anchor ABOVE it
   (`<span class="section-anchor" id="slug"></span>`) so the heading stays
   visible on landing (paired with scroll-margin-top in CSS). A heading that
   already has an id keeps it (reused as the slug).
4. Rewrite the TOC/nav link to `page.html#slug`.

Dedicated pages are left exactly as they are. Anything that can't be matched is
reported, not guessed.

Usage
-----
  python tools/anchor_sections.py            # dry run: report only, no writes
  python tools/anchor_sections.py --apply    # write anchors + rewrite links
"""

import html
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
L1 = REPO / "L1"

LINK_RE = re.compile(r'<a\s+href="([^"]+)"((?:\s+[^>]*?)?)>(.*?)</a>', re.DOTALL)
H1_RE = re.compile(r'<h1[^>]*>(.*?)</h1>', re.DOTALL)
HEAD_RE = re.compile(
    r'^([ \t]*)(<h([2-4])(?:\s+id="([^"]+)")?\s*>(.*?)</h\3>)[ \t]*$',
    re.MULTILINE | re.DOTALL,
)


def strip(s):
    return re.sub(r'<[^>]+>', '', s)


def norm(s):
    s = html.unescape(strip(s)).lower().replace("'", "").replace("\u2019", "")
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def slugify(s):
    s = html.unescape(strip(s)).lower().replace("'", "").replace("\u2019", "")
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


def page_path(href):
    """Resolve a TOC/nav href (relative to L1/) to a file path."""
    rel = href.split('#')[0]
    return (L1 / rel).resolve()


def load_page_index(cache, path):
    """Return (h1_norm, headings) for a page; headings = list of dicts."""
    if path in cache:
        return cache[path]
    if not path.exists():
        cache[path] = (None, [])
        return cache[path]
    text = path.read_text(encoding="utf-8")
    m = H1_RE.search(text)
    h1n = norm(m.group(1)) if m else None
    headings = []
    used = {}
    for hm in HEAD_RE.finditer(text):
        existing_id, inner = hm.group(4), hm.group(5)
        slug = existing_id or slugify(inner)
        if not slug:
            continue
        if slug in used:                       # de-dupe within a page
            used[slug] += 1
            slug = f"{slug}-{used[slug]}"
        else:
            used[slug] = 1
        headings.append({
            "norm": norm(inner), "slug": slug,
            "has_id": bool(existing_id), "raw": hm.group(2), "indent": hm.group(1),
        })
    cache[path] = (h1n, headings)
    return cache[path]


def main(argv):
    apply = "--apply" in argv
    cache = {}
    # page path -> set of slugs whose heading needs an anchor inserted
    anchors_needed = {}
    matched, unmatched = [], []

    nav_files = [L1 / "toc.html", L1 / "nav.html"]

    # ---- pass 1: scan links, decide matches (no writes) ----
    for navf in nav_files:
        text = navf.read_text(encoding="utf-8")
        seen = set()                            # first bare-page link = the page itself
        for lm in LINK_RE.finditer(text):
            href, _attrs, inner = lm.group(1), lm.group(2), lm.group(3)
            if href.startswith(("http", "/", "#", "mailto:")) or "#" in href:
                continue
            if not href.endswith(".html"):
                continue
            if href not in seen:
                seen.add(href)
                continue                        # dedicated-page link: leave as-is
            tpath = page_path(href)
            _h1, headings = load_page_index(cache, tpath)
            if not headings:
                unmatched.append((navf.name, href, strip(inner).strip(), "page not found"))
                continue
            ltext = norm(inner)
            hit = next((h for h in headings if h["norm"] == ltext), None)
            if not hit:
                unmatched.append((navf.name, href, strip(inner).strip(), "no heading match"))
                continue
            matched.append((navf.name, href, strip(inner).strip(), hit["slug"]))
            if not hit["has_id"]:
                anchors_needed.setdefault(tpath, {})[hit["slug"]] = True

    # ---- report ----
    print(f"MATCHED subsection links: {len(matched)}")
    for f, href, text, slug in matched:
        print(f"  [{f}] {text!r} -> {href}#{slug}")
    print(f"\nUNMATCHED (left untouched): {len(unmatched)}")
    for f, href, text, why in unmatched:
        print(f"  [{f}] {text!r} -> {href}   ({why})")
    print(f"\nPages getting new anchors: {len(anchors_needed)}")
    for p, slugs in anchors_needed.items():
        print(f"  {p.relative_to(REPO)}: {sorted(slugs)}")

    if not apply:
        print("\n(dry run -- rerun with --apply to write)")
        return

    # ---- pass 2: insert anchors above headings ----
    changed = []
    for tpath, slugs in anchors_needed.items():
        text = tpath.read_text(encoding="utf-8")

        def ins(hm):
            existing_id, inner, indent, raw = hm.group(4), hm.group(5), hm.group(1), hm.group(2)
            slug = existing_id or slugify(inner)
            if existing_id or slug not in slugs:
                return hm.group(0)
            return f'{indent}<span class="section-anchor" id="{slug}"></span>\n{indent}{raw}'

        new = HEAD_RE.sub(ins, text)
        if new != text:
            tpath.write_text(new, encoding="utf-8")
            changed.append(tpath)

    # ---- pass 2b: rewrite TOC/nav links ----
    want = {(f, href, text): slug for (f, href, text, slug) in matched}
    for navf in nav_files:
        text = navf.read_text(encoding="utf-8")

        def rew(lm):
            href, attrs, inner = lm.group(1), lm.group(2), lm.group(3)
            slug = want.get((navf.name, href, strip(inner).strip()))
            if not slug:
                return lm.group(0)
            return f'<a href="{href}#{slug}"{attrs}>{inner}</a>'

        new = LINK_RE.sub(rew, text)
        if new != text:
            navf.write_text(new, encoding="utf-8")
            changed.append(navf)

    print("\nWROTE:")
    for c in changed:
        print(f"  {c.relative_to(REPO)}")


if __name__ == "__main__":
    main(sys.argv[1:])
