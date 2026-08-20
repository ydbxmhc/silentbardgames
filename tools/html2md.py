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


def rewrite_href(href):
    """Point an internal .html link at its .md sibling, preserving any anchor.

    External schemes and bare in-page anchors are returned untouched, as are
    targets that are not .html at all (images, PDFs, directory links).
    """
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return href
    path_part, sep, anchor = href.partition("#")
    if path_part.endswith(".html"):
        path_part = path_part[:-len(".html")] + ".md"
    return path_part + sep + anchor


def img_md(node):
    src = node.attrs.get("data-src") or node.attrs.get("src", "")
    alt = node.attrs.get("alt", "")
    return f"![{alt}]({src})"


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
            out.append(f"^{inner}")
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
        for w in range(width, max(width - 12, 20), -1):
            pieces = textwrap.wrap(
                stripped, width=w,
                break_long_words=False, break_on_hyphens=False,
            ) or [stripped]
            if not any(LIST_MARKER_RE.match(p) for p in pieces[1:]):
                break
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
              "details", "dl", "main"}

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


def render_block(node):
    t = node.tag
    c = node.cls()

    if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
        level = int(t[1])
        return [f"{'#' * level} {finalize(render_inline(node))}".rstrip()]

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


def convert(html):
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
        md = convert(html_path.read_text(encoding="utf-8"))
        md_path = html_path.with_suffix(".md")
        # newline="\n" is required: .gitattributes pins the repo to eol=lf, but
        # text mode would translate to os.linesep and emit CRLF on Windows,
        # making the tool's output differ by platform.
        md_path.write_text(md, encoding="utf-8", newline="\n")
        print(f"{html_path.relative_to(repo)} -> {md_path.relative_to(repo)}")
    print(f"\n{len(files)} file(s) converted.")


if __name__ == "__main__":
    main(sys.argv[1:])
