#!/usr/bin/env python3
"""Stamp a real `description:` onto posts that have none.

    python3 _tools/write_descriptions.py            # dry run, prints what would change
    python3 _tools/write_descriptions.py --apply
    python3 _tools/write_descriptions.py --apply --force   # also rewrite existing ones

Why this exists
---------------
No post carried a `description:` -- all 2,358 of them. jekyll-seo-tag falls back
to `page.excerpt` when there is none, and a brief's excerpt is its opening `#`
heading, which restates the title. So every post shipped:

    <meta name="description" content="US AI vs China AI Brief - 2026-08-27" />
    <meta property="og:description" content="US AI vs China AI Brief - 2026-08-27" />

The meta description is the copy a searcher reads before deciding to click, and
og:description is the copy anyone sharing the link puts in front of their
network. Repeating the title in both spends that space saying nothing, and
across ~2,400 pages it makes every result look like every other one.

What it writes
--------------
The first two or three story headlines of the edition, joined with a middot --
the same signal _includes/post-lede.html already extracts for the homepage
cards, so a search result now previews the same thing the site does:

    description: "Zhipu's GLM-5.3-Flash Demonstrates China Can Scale AI on
                  Domestic Chips - Nvidia Ships First H200 AI Chips to China"

Posts with no story headings (essays, the old tutorials) fall back to their
first real paragraph of prose.

Run it after adding posts, alongside _tools/assign_series.py. It is idempotent:
a post that already has a non-empty `description:` is left alone unless
--force is passed.
"""
import os
import re
import sys

POST_DIRS = ("_posts", os.path.join("wdpress", "_posts"))

# Target length for the finished description. Google truncates the displayed
# snippet around 155-160 characters on desktop and shorter on mobile; there is
# no penalty for going over, but anything past this point is invisible.
TARGET = 155

HEADING = re.compile(r'^(#{1,4})\s+(.*?)\s*#*\s*$')

# Numbered story prefixes: "1. ", "10. ", "1) ". Leading decoration is stripped
# first -- the generator's templates sprinkle emoji and bullets ahead of the
# number ("📌 1. Official Release: ..."), which would otherwise leave a stray
# "1." glued to the front of the description.
LEAD_DECORATION = re.compile(r'^[^\w(\u3400-\u9fff]+', re.UNICODE)
NUM_PREFIX = re.compile(r'^\d{1,2}\s*[.)]\s*')

# Structural headings that name a section rather than a story. Matched as a
# substring, so "Top Stories (Max 10)" is caught along with "Top Stories".
SKIP_CONTAINS = (
    'top stories', 'top story', 'top headlines', 'executive summary',
    'key takeaways', 'table of contents', 'at a glance', 'in this edition',
    'quick hits', 'in brief', 'editor note', 'editors note', "editor's note",
    'key highlights', 'introduction / hook', 'introduction/hook',
    'summary of', 'what engineers should do', 'developer relevance',
    'innovation impact', 'further reading', 'bottom line', 'next steps',
    'key points', 'closing thought', 'final thought', 'in summary',
    'about the author', 'what this means for you',
    'source links', 'fact check', 'sources for', 'references for',
    'read more', 'related reading', 'methodology note',
)

# Bare section words. Exact match only: "summary" is a section heading on its
# own, but plenty of real headlines contain the word.
SKIP_EQUALS = (
    'headlines', 'summary', 'highlights', 'overview', 'takeaways', 'contents',
    'introduction', 'intro', 'news', 'stories', 'other news',
    'also in the news', 'sources', 'references', 'disclaimer',
    'trends', 'background', 'objective', 'objectives', 'architecture',
    'backend', 'frontend', 'conclusion', 'conclusions', 'results',
    'methodology', 'method', 'implementation', 'discussion', 'analysis',
    'outlook', 'notes', 'credits', 'appendix', 'glossary', 'related',
    'prerequisites', 'setup', 'installation', 'usage', 'faq', 'faqs',
    'tl;dr', 'tldr', 'deep dive', 'why it matters', 'context', 'scope',
    'motivation', 'problem', 'solution', 'approach', 'design', 'testing',
    'deployment', 'reference', 'resources', 'takeaway', 'recommendations',
)

# Body lines that are the brief template's field labels, not prose.
FIELD_LINE = re.compile(r'^\s*[*\-]?\s*\*{0,2}(source|summary|why it matters|url|link)'
                        r'\*{0,2}\s*[:：]', re.I)

# The Summary field specifically -- its text is the best prose in a brief, so
# the fallback path harvests it rather than discarding it with the other labels.
SUMMARY_LINE = re.compile(r'^\s*[*\-]?\s*\*{0,2}summary\*{0,2}\s*[:：]\s*(.+)$', re.I)

CJK = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]')


def is_story_headline(text):
    """Distinguish a story headline from a generic section label.

    The skip lists above catch the labels this corpus actually uses, but new
    ones keep appearing as the generator's templates change, so length carries
    the rest of the load. A real headline is a sentence fragment -- "Nvidia
    Ships First H200 AI Chips to China Under US Licensing Rules" -- while a
    section label is one to three words: "Background", "Key Highlights",
    "Developer Relevance". Four words is the cleanest split on this corpus.

    Chinese and Japanese headings have no spaces to count, so they are measured
    in characters instead.
    """
    if CJK.search(text):
        return len(CJK.findall(text)) >= 6
    return len(text.split()) >= 4


def strip_inline(text):
    """Reduce inline markdown to plain text."""
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)          # images
    text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)      # links -> label
    text = re.sub(r'`{1,3}([^`]*)`{1,3}', r'\1', text)        # code
    text = re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)      # bold / italic
    text = re.sub(r'_{2,3}([^_]+)_{2,3}', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)                       # stray html
    text = re.sub(r'&nbsp;?', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def normalise(text):
    """Punctuation- and space-free form, for comparing a heading to the title."""
    return re.sub(r'[^a-z0-9]', '', text.lower())


def split_front_matter(raw):
    """Return (front_matter_lines, body) or (None, None).

    Note the `.strip()` on the delimiter test: 14 posts in this repo write
    their front matter fences as "--- " with a trailing space, and an exact
    '---' comparison silently treats those files as having no front matter.
    """
    lines = raw.split('\n')
    if not lines or lines[0].strip() != '---':
        return None, None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            return lines[1:i], '\n'.join(lines[i + 1:])
    return None, None


def front_matter_value(fm_lines, key):
    pattern = re.compile(r'^' + re.escape(key) + r'\s*:\s*(.*)$')
    for line in fm_lines:
        m = pattern.match(line)
        if m:
            return m.group(1).strip().strip('"\'').strip()
    return None


def headlines(body, title):
    """Story headlines from the body, in order, scaffolding removed."""
    title_n = normalise(title or '')
    out = []
    in_fence = False
    for line in body.split('\n'):
        if line.lstrip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        text = strip_inline(m.group(2))
        text = NUM_PREFIX.sub('', LEAD_DECORATION.sub('', text))
        text = strip_inline(LEAD_DECORATION.sub('', text))
        if not text:
            continue
        low = text.lower()
        if low in SKIP_EQUALS:
            continue
        if any(s in low for s in SKIP_CONTAINS):
            continue
        text_n = normalise(text)
        if not text_n:
            continue
        # Drop headings that restate the title. Compared without punctuation so
        # that "Fintech+AI Brief - 2026-08-27" matches a title written
        # "Fintech AI Brief - 2026-08-27".
        if title_n and (text_n in title_n or title_n in text_n):
            continue
        if not is_story_headline(text):
            continue
        out.append(text)
    return out


def first_paragraph(body, title):
    """First real prose paragraph, for posts with no story headings."""
    title_n = normalise(title or '')
    buf = []
    in_fence = False
    for line in body.split('\n'):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not stripped:
            if buf:
                break
            continue
        if stripped.startswith('#') or stripped.startswith('---') or stripped.startswith('|'):
            if buf:
                break
            continue
        summary = SUMMARY_LINE.match(stripped)
        if summary:
            text = strip_inline(summary.group(1))
            if text:
                buf.append(text)
                break
            continue
        if FIELD_LINE.match(stripped):
            continue
        text = strip_inline(re.sub(r'^\s*[*\-+>]\s*', '', stripped))
        if not text:
            continue
        if title_n and normalise(text) == title_n:
            continue
        buf.append(text)
    return ' '.join(buf).strip()


def clip(text, limit=TARGET):
    """Trim to `limit`, never mid-word, never leaving dangling punctuation."""
    text = re.sub(r'\s+', ' ', text).strip()
    if len(text) <= limit:
        return text.rstrip(' ,;:-–—·')
    cut = text[:limit + 1]
    space = cut.rfind(' ')
    if space > limit * 0.5:
        cut = cut[:space]
    return cut.rstrip(' ,;:-–—·') + '…'


def build_description(body, title):
    heads = headlines(body, title)
    if heads:
        # Fill greedily and let clip() do the trimming, rather than stopping at
        # the last headline that fits whole. A snippet cut mid-headline with an
        # ellipsis is what search results look like anyway, and it puts a
        # second story's keywords in front of the reader instead of leaving
        # half the available space empty.
        picked = ''
        for head in heads[:4]:
            picked = head if not picked else picked + ' · ' + head
            if len(picked) >= TARGET:
                break
        return clip(picked)
    prose = first_paragraph(body, title)
    return clip(prose) if prose else ''


def yaml_quote(value):
    return '"' + value.replace('\\', '\\\\').replace('"', '\\"') + '"'


def rewrite(raw, description):
    """Insert or replace `description:` in the front matter.

    Placed straight after `series:` when there is one, otherwise after
    `title:`, so the front matter stays readable rather than growing a key at
    the bottom. Any existing `description:` line is removed first, which is
    what makes re-running safe.
    """
    lines = raw.split('\n')
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == '---')
    fm = lines[1:end]

    fm = [l for l in fm if not re.match(r'^description\s*:', l)]

    anchor = None
    for i, line in enumerate(fm):
        if re.match(r'^series\s*:', line):
            anchor = i
            break
        if anchor is None and re.match(r'^title\s*:', line):
            anchor = i

    insert_at = 0
    if anchor is not None:
        insert_at = anchor + 1
        # Step over the anchor key's continuation lines before inserting.
        #
        # Nine of the WordPress imports in wdpress/_posts wrap a long title
        # across two lines using YAML's plain multi-line scalar form:
        #
        #     title: Fresh chicken out-of-stock in Singapore because of ban
        #       by Malaysia
        #
        # An indented line belongs to the key above it, so inserting directly
        # after `title:` splits the key from its own value and the whole
        # document fails to parse ("did not find expected key while parsing a
        # block mapping"). Jekyll then drops the post from the build entirely.
        while insert_at < len(fm) and re.match(r'^[ \t]+\S', fm[insert_at]):
            insert_at += 1

    fm.insert(insert_at, 'description: ' + yaml_quote(description))

    return '\n'.join(lines[:1] + fm + lines[end:])


def main():
    apply = '--apply' in sys.argv
    force = '--force' in sys.argv

    considered = written = skipped_have = skipped_empty = no_fm = 0
    samples = []

    for directory in POST_DIRS:
        if not os.path.isdir(directory):
            continue
        for name in sorted(os.listdir(directory)):
            if not name.endswith(('.md', '.markdown', '.html')):
                continue
            path = os.path.join(directory, name)
            with open(path, encoding='utf-8', errors='replace') as fh:
                raw = fh.read()

            fm_lines, body = split_front_matter(raw)
            if fm_lines is None:
                no_fm += 1
                continue
            considered += 1

            existing = front_matter_value(fm_lines, 'description')
            title = front_matter_value(fm_lines, 'title') or ''
            if existing and not force:
                skipped_have += 1
                continue

            description = build_description(body or '', title)
            if not description:
                skipped_empty += 1
                continue
            if existing == description:
                skipped_have += 1
                continue

            written += 1
            if len(samples) < 6:
                samples.append((path, description))
            if apply:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(rewrite(raw, description))

    verb = 'wrote' if apply else 'would write'
    print(f'posts with front matter: {considered}   (files without: {no_fm})')
    print(f'{verb} description:       {written}')
    print(f'already had one:         {skipped_have}')
    print(f'no usable text:          {skipped_empty}')
    if samples:
        print('\nsamples:')
        for path, description in samples:
            print(f'  {os.path.basename(path)}')
            print(f'    ({len(description)} chars) {description}')
    if not apply and written:
        print('\ndry run. re-run with --apply to write.')


if __name__ == '__main__':
    main()
