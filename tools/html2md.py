#!/usr/bin/env python3
"""Deterministic HTML -> Markdown converter for the OneSRD / Level One site.

Purpose
-------
Create a Markdown sibling (foo.md) next to every foo.html, replicating the
page's *text* as precisely as possible. Markdown cannot reproduce exact visual
placement, but every word, heading, list, link, and emphasis is preserved
verbatim. No paraphrasing, no summarizing, no invented text -- the conversion
is purely structural (see /CLAUDE.md, the Prime Directive).

Method
------
- Parse with the stdlib html.parser (no third-party deps; never pip install).
- For a full page, convert only the <main> content region (the unique page
  body). Site chrome (#site-header, #drawer, #overlay, <script>, <style>) is
  excluded. Fragment files with no <main> (header.html, nav.html) convert
  their whole content.
- Walk the DOM and emit Markdown, mapping the site's known constructs
  (.box callouts, .page-header, .breadcrumb, .page-nav, .text-image-block,
  emphasis spans) to faithful Markdown equivalents.
- Rewrite internal link targets from .html to .md as they are written, so the
  Markdown corpus is navigable on its own (see rewrite_href). This is the same
  rule tools/relink_md.py applies; that tool remains for fixing files by hand.
- Hard-wrap paragraph text at MD_WIDTH columns, matching the house style of the
  hand-wrapped pages. Headings, list items, code fences and nav links are left
  on one line, because the hand-wrapped pages leave them that way.

Usage
-----
  python tools/html2md.py            # convert every *.html in the repo
  python tools/html2md.py FILE...    # convert only the given files

Both forms write the .md siblings in place; naming files only narrows the set.
"""

import re
import sys
import textwrap
from html.parser import HTMLParser
from pathlib import Path

# Column limit for wrapped paragraph text. Derived from the hand-wrapped pages,
# whose line lengths plateau at 78 and drop off sharply at 79.
MD_WIDTH = 78

# A wrapped continuation line must never begin with something CommonMark reads
# as a list marker: "- ", "* ", "+ ", "1. ", "1) ". The house style writes a
# spaced " - " freely, so a naive wrap can turn prose into a list.
LIST_MARKER_RE = re.compile(r'^([-*+]|\d+[.)])\s')

# A complete Markdown image construct, protected from hard-wrapping.
IMG_MD_RE = re.compile(r'!\[[^\]]*\]\([^)]*\)')

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "param", "source", "track", "wbr"}

INLINE = {"a", "em", "i", "strong", "b", "code", "span", "br", "sup", "sub",
          "small", "mark", "u", "abbr", "cite", "q", "time", "s", "del",
          "ins", "var", "kbd", "samp", "img"}

SKIP_TAGS = {"script", "style", "head", "title", "meta", "link"}
SKIP_IDS = {"site-header", "drawer", "overlay"}

BR = "\x00BR\x00"  # sentinel for <br>, restored to a hard break after cleanup


class Node:
    __slots__ = ("tag", "attrs", "children", "text", "is_text")

    def __init__(self, tag=None, attrs=None, text=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []
        self.text = text
        self.is_text = text is not None

    def cls(self):
        return self.attrs.get("class", "").split()


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node(tag="#root")
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag=tag, attrs=attrs)
        self.stack[-1].children.append(node)
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.stack[-1].children.append(Node(tag=tag, attrs=attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(Node(text=data))


# ----------------------------------------------------------------------------
# Inline rendering
# ----------------------------------------------------------------------------
def norm_ws(s):
    return re.sub(r"\s+", " ", s)


TAG_RE = re.compile(r"<[^>]+>")
ENTITY_RE = re.compile(r"&#\d+;|&[a-zA-Z]+;")
APOSTROPHE_ENTS = ("&#8217;", "&#39;", "&rsquo;", "&apos;")


def gh_slug(html_fragment):
    """Slugify heading text the way GitHub does when it auto-anchors a heading.

    Lowercase, drop everything that is not a letter, number, space or hyphen,
    then collapse whitespace to hyphens. Apostrophes vanish rather than becoming
    separators, which is why they are removed before the entity sweep.
    """
    s = html_fragment
    for ent in APOSTROPHE_ENTS:
        s = s.replace(ent, "")
    s = TAG_RE.sub("", s)
    s = ENTITY_RE.sub(" ", s)
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[-\s]+", "-", s)


# id -> markdown slug, per target page. Built lazily; a page is read at most
# once per run.
_ANCHOR_CACHE = {}

_HEAD_ID_RE = re.compile(r'<h([1-6])[^>]*\bid="([^"]+)"[^>]*>(.*?)</h\1>', re.S)
_SPAN_ANCHOR_RE = re.compile(
    r'<span[^>]*\bclass="[^"]*section-anchor[^"]*"[^>]*\bid="([^"]+)"[^>]*>'
    r'\s*</span>\s*<h([1-6])[^>]*>(.*?)</h\2>', re.S)
_DT_ID_RE = re.compile(r'<dt[^>]*\bid="([^"]+)"[^>]*>(.*?)</dt>', re.S)


def anchor_map(html_path):
    """Map each HTML id on a page to the anchor its Markdown mirror will have.

    The site sets ids deliberately and often shortens them -- id="hit-points"
    on a heading reading "Harm and Recovery", for instance. GitHub cannot
    reproduce a hand-set id; it slugs the heading text it is given. So a link
    copied verbatim into the mirror points at an anchor that will never exist.

    Ids this cannot reproduce (a <sup>, an <li>) are absent from the map, and
    the caller drops the fragment rather than emitting a link that dies.
    """
    key = str(html_path)
    if key in _ANCHOR_CACHE:
        return _ANCHOR_CACHE[key]
    mapping = {}
    try:
        text = html_path.read_text(encoding="utf-8")
    except OSError:
        _ANCHOR_CACHE[key] = mapping
        return mapping
    for anchor_id, _lvl, inner in _SPAN_ANCHOR_RE.findall(text):
        mapping[anchor_id] = gh_slug(inner)
    for _lvl, anchor_id, inner in _HEAD_ID_RE.findall(text):
        mapping[anchor_id] = gh_slug(inner)
    # <dt> terms become headings in the mirror (see definition_pairs), so their
    # ids are reproducible too.
    for anchor_id, inner in _DT_ID_RE.findall(text):
        mapping[anchor_id] = gh_slug(inner)
    _ANCHOR_CACHE[key] = mapping
    return mapping


def resolve_fragment(path_part, anchor):
    """Return the Markdown anchor for a fragment, or "" if unreproducible."""
    if not anchor or _CURRENT_PATH is None:
        return anchor
    target = (_CURRENT_PATH.parent / path_part) if path_part else _CURRENT_PATH
    target = target.with_suffix(".html") if path_part else target
    mapping = anchor_map(target)
    if not mapping:
        return anchor          # unreadable target: leave the link as written
    return mapping.get(anchor, "")


def rewrite_href(href):
    """Point an internal .html link at its .md sibling, preserving any anchor.

    External schemes are returned untouched, as are targets that are not .html
    at all (images, PDFs, directory links). Fragments are re-resolved to the
    anchor the Markdown will actually carry; one that cannot exist is dropped so
    the link still lands on the right page.
    """
    if href.startswith(("http://", "https://", "mailto:")):
        return href
    path_part, sep, anchor = href.partition("#")
    if sep:
        anchor = resolve_fragment(path_part, anchor)
        sep = "#" if anchor else ""
    if path_part.endswith(".html"):
        path_part = path_part[:-len(".html")] + ".md"
    return path_part + sep + anchor


# Path of the page currently being converted, so image sources can be resolved
# against the right game's config.js. None when convert() is called on a bare
# string, in which case data-src is emitted unchanged, as before.
_CURRENT_PATH = None
_CDN_CACHE = {}

CDN_RE = re.compile(r"""CDN_BASE\s*:\s*['"]([^'"]+)['"]""")


def cdn_base_for(path):
    """Find the CDN base for a page by locating the nearest config.js above it.

    The site injects image sources at runtime: HTML carries data-src="foo.png"
    and config.js prepends SiteConfig.CDN_BASE. The bare filename therefore
    resolves to nothing beside the .md sibling. Reading the base from config.js
    rather than hard-coding it keeps the author's stated intent intact -- change
    CDN_BASE in one place and every reference follows, mirrors included.
    """
    if path is None:
        return None
    for parent in [path.parent, *path.parents]:
        cfg = parent / "config.js"
        if cfg in _CDN_CACHE:
            return _CDN_CACHE[cfg]
        if cfg.exists():
            m = CDN_RE.search(cfg.read_text(encoding="utf-8"))
            base = m.group(1).rstrip("/") if m else None
            _CDN_CACHE[cfg] = base
            return base
    return None


def url_escape(src):
    """Percent-encode characters that break a Markdown link target.

    Only spaces occur in practice ("the tale.jpg"), and only untouched ones are
    encoded, so an already-encoded path is left alone.
    """
    return src.replace(" ", "%20") if "%" not in src else src


def img_md(node):
    data_src = node.attrs.get("data-src")
    src = data_src or node.attrs.get("src", "")
    alt = node.attrs.get("alt", "")
    if data_src and not src.startswith(("http://", "https://", "/")):
        base = cdn_base_for(_CURRENT_PATH)
        if base:
            src = f"{base}/{src}"
    return f"![{alt}]({url_escape(src)})"


FN_HREF_RE = re.compile(r'^#fn(\w+)$')


def footnote_ref(sup_node):
    """Return a GFM footnote reference for <sup><a href="#fnN">N</a></sup>.

    Markdown has real footnote syntax, and GitHub renders it with a numbered
    marker, a collected notes section, and a return link -- all the things the
    site's hand-built footnotes do. Emitting [^N] therefore preserves the
    behaviour instead of leaving "#fn1" pointing at nothing, which is what a
    literal copy produced.

    Returns None if this <sup> is not a footnote reference.
    """
    links = [c for c in sup_node.children if not c.is_text and c.tag == "a"]
    if len(links) != 1:
        return None
    m = FN_HREF_RE.match(links[0].attrs.get("href", ""))
    return f"[^{m.group(1)}]" if m else None


def render_footnotes(node):
    """Render <section class="footnotes"> as GFM footnote definitions.

    The section's own "Notes" heading is dropped: GitHub emits its own heading
    for the collected footnotes, and GFM relocates every definition to the foot
    of the document, so keeping it would leave a heading stranded over nothing.
    This is the one place the converter drops a heading, and it does so because
    the target format supplies the equivalent itself.

    The hand-written return arrow is dropped for the same reason -- GFM
    generates a backlink automatically.
    """
    out = []
    for ol in _descendants(node):
        if ol.is_text or ol.tag != "li":
            continue
        fid = ol.attrs.get("id", "")
        if not fid.startswith("fn"):
            continue
        kept = [c for c in ol.children
                if c.is_text or c.tag != "a"
                or not c.attrs.get("href", "").startswith("#ref")]
        holder = Node(tag="#inline")
        holder.children = kept
        text = finalize(render_inline(holder))
        if text:
            out.append(f"[^{fid[2:]}]: {text}")
    return out


def _descendants(node):
    for ch in node.children:
        yield ch
        if not ch.is_text:
            yield from _descendants(ch)


def render_inline(node):
    out = []
    for ch in node.children:
        if ch.is_text:
            out.append(norm_ws(ch.text))
            continue
        t = ch.tag
        inner = render_inline(ch)
        if t in ("em", "i", "cite", "var", "q"):
            out.append(f"*{inner}*" if inner.strip() else inner)
        elif t in ("strong", "b"):
            out.append(f"**{inner}**" if inner.strip() else inner)
        elif t in ("code", "kbd", "samp"):
            out.append(f"`{inner}`")
        elif t == "br":
            out.append(BR)
        elif t == "a":
            href = rewrite_href(ch.attrs.get("href", ""))
            out.append(f"[{inner}]({href})" if href and inner.strip() else inner)
        elif t == "img":
            out.append(img_md(ch))
        elif t == "sup":
            ref = footnote_ref(ch)
            out.append(ref if ref else f"^{inner}")
        elif t == "sub":
            out.append(f"~{inner}")
        elif t == "span":
            c = ch.cls()
            if "nav-chevron" in c:
                continue  # decorative arrow
            if "term" in c or "speaker" in c:
                out.append(f"**{inner}**" if inner.strip() else inner)
            elif "mechanic" in c or "gm-voice" in c:
                out.append(f"*{inner}*" if inner.strip() else inner)
            else:
                out.append(inner)
        else:
            out.append(inner)
    return "".join(out)


def finalize(text):
    text = text.replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    # tidy spaces around hard-break sentinels, then restore them
    text = re.sub(r" *" + re.escape(BR) + r" *", BR, text)
    text = text.replace(BR, "  \n")
    return text.strip()


def wrap_block(text, width=MD_WIDTH):
    """Hard-wrap paragraph text, leaving Markdown structure intact.

    Each existing line wraps independently, so a hard break (a line ending in
    two spaces) stays a hard break. Long unbreakable runs -- URLs, link targets
    -- are never split, and hyphenated words are never broken apart.

    If a continuation line would open with a list marker, the width is nudged
    down until it does not; otherwise CommonMark would read the paragraph's
    tail as a new list.
    """
    out = []
    for line in text.split("\n"):
        hard_break = line.endswith("  ")
        stripped = line.strip()
        if not stripped:
            out.append("")
            continue
        # Keep whole image constructs on one line. Wrapping inside ![alt](src)
        # still renders, but it splits the alt text across a newline, which
        # confuses anything reading the Markdown with a line-oriented pattern.
        # Ordinary links are deliberately left wrappable: the hand-wrapped
        # pages break inside link text, and that is the house style.
        shelf = []

        def stow(m):
            shelf.append(m.group(0))
            return f"\x00IMG{len(shelf) - 1}\x00"

        stripped = IMG_MD_RE.sub(stow, stripped)
        for w in range(width, max(width - 12, 20), -1):
            pieces = textwrap.wrap(
                stripped, width=w,
                break_long_words=False, break_on_hyphens=False,
            ) or [stripped]
            if not any(LIST_MARKER_RE.match(p) for p in pieces[1:]):
                break
        if shelf:
            pieces = [re.sub(r"\x00IMG(\d+)\x00",
                             lambda m: shelf[int(m.group(1))], p)
                      for p in pieces]
        if hard_break:
            pieces[-1] += "  "
        out.extend(pieces)
    return "\n".join(out)


# ----------------------------------------------------------------------------
# Block rendering
# ----------------------------------------------------------------------------
BLOCK_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "div",
              "section", "article", "header", "footer", "nav", "aside",
              "figure", "figcaption", "blockquote", "pre", "hr", "table",
              "details", "dl", "main",
              # html/body matter only for files with no <main> of their own --
              # the print digest in WIP/. Without them the whole document is
              # treated as one inline run and every heading is swallowed.
              "html", "body"}

# Table structure. These are handled by render_table rather than by the generic
# container path, which would otherwise fuse every cell into one paragraph.
TABLE_TAGS = {"thead", "tbody", "tfoot", "tr", "th", "td", "caption"}

LABEL_SPANS = {"box-title", "nav-section-label", "drawer-logo"}


def is_block(node):
    if node.is_text:
        return False
    if node.tag in BLOCK_TAGS:
        return True
    if node.tag == "span" and (set(node.cls()) & LABEL_SPANS):
        return True
    return False


def render_children_blocks(node):
    """Return a list of Markdown block strings for a container's children."""
    blocks = []
    buf = []

    def flush():
        if buf:
            para = finalize("".join(buf))
            if para:
                blocks.append(wrap_block(para))
            buf.clear()

    for ch in node.children:
        if ch.is_text:
            # Keep inter-element whitespace as a single space so inline runs
            # stay separated; finalize() trims it at block edges.
            buf.append(norm_ws(ch.text))
            continue
        if is_block(ch):
            flush()
            blocks.extend(render_block(ch))
        else:
            buf.append(render_inline_child(ch))
    flush()
    return blocks


def render_inline_child(ch):
    """Render a single inline child by wrapping it in a throwaway parent."""
    holder = Node(tag="#inline")
    holder.children.append(ch)
    return render_inline(holder)


def list_items(node, ordered, depth):
    lines = []
    n = 1
    for li in node.children:
        if li.is_text or li.tag != "li":
            continue
        inline_parts = []
        nested = []
        for c in li.children:
            if not c.is_text and c.tag in ("ul", "ol"):
                nested.append(c)
            elif not c.is_text and c.tag == "p":
                inline_parts.append(render_inline(c))
            elif c.is_text:
                if c.text.strip():
                    inline_parts.append(norm_ws(c.text))
            else:
                inline_parts.append(render_inline_child(c))
        indent = "  " * depth
        marker = f"{n}. " if ordered else "- "
        item_text = finalize(" ".join(p for p in inline_parts if p.strip()))
        # keep multi-line items aligned under the marker
        item_text = item_text.replace("\n", "\n" + indent + " " * len(marker))
        lines.append(f"{indent}{marker}{item_text}")
        for sub in nested:
            lines.append(list_items(sub, sub.tag == "ol", depth + 1))
        n += 1
    return "\n".join(lines)


def definition_pairs(node):
    """Render a <dl> as one block per term/definition pair.

    No Markdown definition-list syntax renders reliably on GitHub, so each pair
    becomes an ordinary paragraph: the <dt> content, already bold in the source,
    followed by its <dd>. Nothing is invented -- the only difference from the
    default treatment is that the pairs stop running together into one blob.

    A <dt> with no <dd>, or a stray <dd>, is emitted on its own rather than
    dropped.

    A <dt> that carries an id becomes a heading instead. The site anchors its
    glossary terms so the rest of the book can link straight to a definition,
    and a bold paragraph has no anchor at all -- every such link died on arrival
    in the mirror. As a heading, GitHub auto-anchors it, and the existing links
    resolve with no rewriting: all 51 glossary ids already equal the slug of
    their own term text, verified 2026-08-24.
    """
    blocks = []
    term = None
    for ch in node.children:
        if ch.is_text or ch.tag not in ("dt", "dd"):
            continue
        inline = finalize(render_inline(ch))
        if ch.tag == "dt":
            if term:
                blocks.append(term)
            if ch.attrs.get("id"):
                # Level 2: the only <dl> in the book sits under a lone <h1>.
                blocks.append(f"## {strip_redundant_bold(inline)}")
                term = None
            else:
                term = inline
            continue
        blocks.append(f"{term} {inline}".strip() if term else inline)
        term = None
    if term:
        blocks.append(term)
    return [b if b.startswith("## ") else wrap_block(b) for b in blocks if b]


def _table_rows(node, rows):
    """Collect <tr> rows from a table, descending through thead/tbody/tfoot."""
    for ch in node.children:
        if ch.is_text:
            continue
        if ch.tag == "tr":
            cells = []
            header = False
            for cell in ch.children:
                if cell.is_text or cell.tag not in ("th", "td"):
                    continue
                if cell.tag == "th":
                    header = True
                # A pipe inside a cell would break the row; escape it.
                text = finalize(render_inline(cell)).replace("\n", " ")
                cells.append(text.replace("|", "\\|"))
            if cells:
                rows.append((header, cells))
        elif ch.tag in ("thead", "tbody", "tfoot"):
            _table_rows(ch, rows)


def render_table(node):
    """Render a <table> as a GFM pipe table.

    Markdown has no rowspan or colspan, so a merged cell simply occupies one
    column; nothing is invented and no text is dropped. A table whose first row
    is not a header still needs a header row for GFM to recognise it, so an
    empty one is emitted rather than fabricating column names.
    """
    rows = []
    caption = None
    for ch in node.children:
        if not ch.is_text and ch.tag == "caption":
            caption = finalize(render_inline(ch))
    _table_rows(node, rows)
    if not rows:
        return []

    width = max(len(cells) for _, cells in rows)
    pad = lambda cells: cells + [""] * (width - len(cells))

    first_is_header, first_cells = rows[0]
    if first_is_header:
        head, body = pad(first_cells), rows[1:]
    else:
        head, body = [""] * width, rows

    lines = ["| " + " | ".join(head) + " |",
             "|" + "|".join([" --- "] * width) + "|"]
    for _, cells in body:
        lines.append("| " + " | ".join(pad(cells)) + " |")

    out = ["\n".join(lines)]
    if caption:
        out.insert(0, f"**{caption}**")
    return out


WHOLLY_BOLD_RE = re.compile(r'^\*\*(.+)\*\*$', re.S)


def strip_redundant_bold(text):
    """Drop bold that wraps an entire heading, because headings are already bold.

    The glossary marks every term <strong> inside its <dt>, which is right in
    HTML -- a definition term is not bold by default. Once that term becomes a
    Markdown heading the emphasis is pure noise: "## **Adept**".

    Italic is deliberately left alone. A heading is bold by default but never
    italic, so <em> around a whole heading is a real stylistic choice, not
    redundancy -- "Can I Try Again?" and "Where Are My Hit Points???" are voiced
    that way on purpose.

    Only an unambiguous wrap is stripped: if the inner text carries its own **
    the markers may not pair the way they appear to, so it is left untouched.
    """
    m = WHOLLY_BOLD_RE.match(text.strip())
    if not m or "**" in m.group(1):
        return text
    return m.group(1)


def render_block(node):
    t = node.tag
    c = node.cls()

    if t == "section" and "footnotes" in c:
        return render_footnotes(node)

    if t == "table":
        return render_table(node)

    if t in TABLE_TAGS:
        # Reached only if the markup nests these outside a <table>; render the
        # contents rather than dropping them.
        return render_children_blocks(node)

    if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(t[1])
        return [f"{'#' * level} {strip_redundant_bold(finalize(render_inline(node)))}".rstrip()]

    if t == "p":
        text = finalize(render_inline(node))
        return [wrap_block(text)] if text else []

    if t == "hr":
        return ["---"]

    if t == "img":
        return [img_md(node)]

    if t == "span":  # only label spans reach here
        text = finalize(render_inline(node))
        if "box-title" in c or "nav-section-label" in c:
            return [f"**{text}**"] if text else []
        return [text] if text else []

    if t in ("ul", "ol"):
        ordered = (t == "ol") or ("step-list" in c)
        body = list_items(node, ordered, 0)
        return [body] if body.strip() else []

    if t == "dl":
        return definition_pairs(node)

    if t == "blockquote":
        inner = render_children_blocks(node)
        if not inner:
            inner = [wrap_block(finalize(render_inline(node)))]
        return [quote("\n\n".join(b for b in inner if b))]

    if t == "pre":
        text = "".join(_raw_text(node))
        return ["```\n" + text.strip("\n") + "\n```"]

    # Callout boxes -> blockquote
    if t == "div" and (set(c) & {"box", "example-play", "roll-block",
                                 "gm-note", "example", "rule", "warning",
                                 "highlight"}):
        inner = render_children_blocks(node)
        return [quote("\n\n".join(b for b in inner if b))]

    # Prev/next page navigation -> labeled link list
    if t == "nav" and "page-nav" in c:
        return render_page_nav(node)

    # details/summary (nav groups)
    if t == "details":
        out = []
        for ch in node.children:
            if not ch.is_text and ch.tag == "summary":
                s = finalize(render_inline(ch))
                if s:
                    out.append(f"**{s}**")
            else:
                if not ch.is_text:
                    out.extend(render_block(ch) if is_block(ch)
                               else [finalize(render_inline_child(ch))])
        return [b for b in out if b]

    # Transparent containers: render children in order
    return render_children_blocks(node)


def render_page_nav(node):
    links = []
    for a in node.children:
        if a.is_text or a.tag != "a":
            continue
        href = rewrite_href(a.attrs.get("href", ""))
        label = title = ""
        for s in a.children:
            if s.is_text:
                continue
            sc = s.cls()
            if "page-nav-label" in sc:
                label = finalize(render_inline(s))
            elif "page-nav-title" in sc:
                title = finalize(render_inline(s))
        text = f"{label}: {title}".strip(": ")
        links.append(f"- [{text}]({href})")
    return ["---", "\n".join(links)] if links else []


def quote(text):
    return "\n".join(("> " + ln).rstrip() if ln else ">"
                     for ln in text.split("\n"))


def _raw_text(node):
    if node.is_text:
        return [node.text]
    out = []
    for ch in node.children:
        out.extend(_raw_text(ch))
    return out


# ----------------------------------------------------------------------------
# Page extraction + driver
# ----------------------------------------------------------------------------
def find_main(node):
    if not node.is_text and node.tag == "main":
        return node
    for ch in node.children:
        if not ch.is_text:
            found = find_main(ch)
            if found:
                return found
    return None


def prune_chrome(node):
    """Remove script/style/head and chrome elements by id, in place."""
    kept = []
    for ch in node.children:
        if ch.is_text:
            kept.append(ch)
            continue
        if ch.tag in SKIP_TAGS:
            continue
        if ch.attrs.get("id") in SKIP_IDS:
            continue
        prune_chrome(ch)
        kept.append(ch)
    node.children = kept


def convert(html, path=None):
    global _CURRENT_PATH
    _CURRENT_PATH = path
    builder = TreeBuilder()
    builder.feed(html)
    root = builder.root
    main = find_main(root)
    target = main if main is not None else root
    if main is None:
        prune_chrome(target)
    blocks = render_children_blocks(target)
    body = "\n\n".join(b for b in blocks if b.strip())
    return body.rstrip() + "\n"


def iter_html_files(repo):
    for p in sorted(repo.rglob("*.html")):
        if ".git" in p.parts:
            continue
        yield p


def main(argv):
    repo = Path(__file__).resolve().parent.parent
    if argv:
        files = [Path(a).resolve() for a in argv]
    else:
        files = list(iter_html_files(repo))
    for html_path in files:
        md = convert(html_path.read_text(encoding="utf-8"), html_path)
        md_path = html_path.with_suffix(".md")
        # newline="\n" is required: .gitattributes pins the repo to eol=lf, but
        # text mode would translate to os.linesep and emit CRLF on Windows,
        # making the tool's output differ by platform.
        md_path.write_text(md, encoding="utf-8", newline="\n")
        print(f"{html_path.relative_to(repo)} -> {md_path.relative_to(repo)}")
    print(f"\n{len(files)} file(s) converted.")


if __name__ == "__main__":
    main(sys.argv[1:])
