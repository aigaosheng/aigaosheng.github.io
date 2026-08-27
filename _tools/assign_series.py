#!/usr/bin/env python3
"""Stamp a canonical `series:` key onto recurring-brief posts.

    python3 _tools/assign_series.py            # dry run, prints what would change
    python3 _tools/assign_series.py --apply

Why this exists
---------------
Roughly ten briefs are published a day across ~15 recurring columns, but the
same column has been titled many different ways over time -- "AI Fintech
Brief", "AI+Fintech Brief", "AI + Fintech Brief" and "Fintech AI Brief" are all
one column. Readers had no way to follow a single beat, and `categories:` was
`[]` on 2,260 of 2,325 posts.

This derives the column from the title and writes it to `series:`, which
_layouts/series.html, series.html, index.html and _layouts/post.html all read.
Posts whose titles are not editions of a column (essays, old tutorials) are
deliberately left without a series.

Run it after adding posts. It is idempotent: an existing `series:` is replaced,
so re-running never duplicates the key. New columns are added by extending
RULES below AND adding a page under series/ with a matching `series:` value --
the /series/ index is driven by those pages, not by this file.
"""
import os
import re
import sys


MONTH = r'(?:jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec)[a-z]*\.?'

DATE_PATTERNS = [
    re.compile(r'\d{4}[-/]\d{1,2}[-/]\d{1,2}'),
    re.compile(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'),
    re.compile(MONTH + r'\s+\d{1,2}(?:st|nd|rd|th)?\s*[-–—]?\s*\d{0,2}\s*,?\s*(?:20\d{2})?', re.I),
    re.compile(r'\d{1,2}(?:st|nd|rd|th)?\s*[-–—]?\s*\d{0,2}\s+' + MONTH + r'\s*,?\s*(?:20\d{2})?', re.I),
    re.compile(r'\bweek\s+(?:of|ending)\b', re.I),
    re.compile(r'\blast\s+24\s+hours?\b', re.I),
    re.compile(r'\bpast\s+\d+\s+(?:days?|hours?)\b', re.I),
    re.compile(r'\b20(?:1[5-9]|2[0-9])\b'),
]

# Markers that make a title a recurring edition rather than a one-off essay.
# Deliberately narrow: an essay subtitle that merely says "Report" or "Frontier"
# is not an edition of a column, so only explicit bulletin nouns and cadence
# words qualify.
STRONG = (r'brief|briefing|briefs|newsletter|digest|roundup|round-up|bulletin|'
          r'dispatch|pulse|wrap|market report|market review|market daily')
CADENCE = r'daily|weekly|monthly|quarterly'
PERIODICAL = re.compile(r'\b(?:' + STRONG + r'|' + CADENCE + r')\b', re.I)

# The column name is the head of the title; everything after the first strong
# separator is that edition's own subtitle. Matching the whole string made
# "China Market Daily - AI Surge Lifts Tech, Regulators Watch Closely" classify
# as governance, so topic rules run against the head first.
HEAD_SPLIT = re.compile(r'[—–:|(]|-\s|\bvs\.?\b', re.I)

def clean_title(t):
    s = t
    for pat in DATE_PATTERNS:
        s = pat.sub(' ', s)
    s = s.replace('*', ' ')
    s = re.sub(r'\s{2,}', ' ', s).strip()
    s = re.sub(r'[—–\-:|,;(){}\[\]&+]+\s*$', '', s).strip()
    return s

def head(t):
    """The column-name portion: text before the first strong separator."""
    m = HEAD_SPLIT.search(t)
    h = t[:m.start()] if m else t
    return re.sub(r'[—–\-:|,;&+]+\s*$', '', h).strip()

# Ordered, most specific first; first match wins.
RULES = [
    ('Market Reports',               r'market\s+(report|review|daily|snapshot|wrap|brief|outlook|update)|'
                                     r'(daily|weekly)\s+market|\bmarkets?$|\bmarkets\b|\bequit|\bindices\b|\bbourse'),
    ('AI Company Watch',             r'openai|anthropic|\bgoogle\b|microsoft|\bmeta\b|nvidia|deepseek|'
                                     r'\bqwen\b|hugging\s?face|mistral|\bxai\b|\bapple\b|amazon|'
                                     r'perplexity|bytedance|minimax|moonshot|\bkimi\b|baidu|'
                                     r'alibaba|tencent|cohere|\bgrok\b|\bibm\b|\boracle\b|'
                                     r'ai\s+compan|top\s+ai\s+comp'),
    ('Quantum Computing',            r'quantum'),
    ('Singapore',                    r'singapore|fintechnews\.sg|\bsg\b|\bsea\b|southeast asia'),
    ('AI Governance & Regulation',   r'governance|\bgrc\b|compliance|regulat|policy|antitrust|\blaw\b'),
    ('Tokenized Assets',             r'token|\brwa\b|real[\s-]?world asset|stablecoin|\bcrypto|bitcoin'),
    ('Payments',                     r'payment|\bcards?\b|acquir|remittance|cross[\s-]?border|wallet'),
    ('AI & Fintech',                 r'fintech|\bbank|financ|insur|lending|\bwealth'),
    ('US & China AI',                r'\bchina\b|chinese|\bus ai\b|u\.s\.|\bamerica|\bhong kong\b'),
    ('Enterprise AI',                r'enterprise|\bcio\b|\bb2b\b|corporate'),
    ('Investment & Startups',        r'invest|startup|start-up|venture|\bvc\b|funding|\bm&a\b|\bipo\b|'
                                     r'accelerator|angel'),
    ('AI Security & Risk',           r'security|cyber|threat|\bfraud\b|attack|vulnerab|\brisk\b'),
    ('AI & Society',                 r'society|social media|impact on life|\bjobs\b|labor|labour|'
                                     r'education|\bhuman'),
    ('AI Research & Open Source',    r'research|open[\s-]?source|\bllm\b|\bpapers?\b|\bmodels?\b|'
                                     r'\bbenchmark|\barxiv\b|agentic|\bagents?\b'),
    ('AI Industry News',             r'\bai\b|artificial intelligence|\btech\b|technology|\bgpu\b|'
                                     r'semiconductor|chip|robot'),
]
RULES = [(name, re.compile(pat, re.I)) for name, pat in RULES]

def classify(title):
    """Canonical series name, or None for one-off posts."""
    if not title:
        return None
    cleaned = clean_title(title)
    if not PERIODICAL.search(cleaned):
        return None
    for candidate in (head(cleaned), cleaned):
        for name, pat in RULES:
            if pat.search(candidate):
                return name
    return None


# ---------------------------------------------------------------- front matter

def split_fm(txt):
    """Return (pre, fm_lines, rest_lines) or None. `pre` keeps leading blanks."""
    lines = txt.split('\n')
    i = 0
    while i < len(lines) and lines[i].strip() == '':
        i += 1
    if i >= len(lines) or lines[i].strip() != '---':
        return None
    for j in range(i + 1, len(lines)):
        if lines[j].strip() == '---':
            return lines[:i + 1], lines[i + 1:j], lines[j:]
    return None


def title_of(fm_lines):
    for ln in fm_lines:
        m = re.match(r'^title:\s*(.*)$', ln)
        if m:
            t = m.group(1).strip()
            if len(t) >= 2 and t[0] == t[-1] and t[0] in '"\'':
                t = t[1:-1]
            return t
    return None


def run(root, apply_changes):
    changed, no_fm, same = [], 0, 0
    for name in sorted(os.listdir(root)):
        path = os.path.join(root, name)
        if not os.path.isfile(path) or not name.lower().endswith(('.md', '.markdown', '.html')):
            continue
        txt = open(path, encoding='utf-8', errors='replace').read()
        parts = split_fm(txt)
        if parts is None:
            no_fm += 1
            continue
        pre, fm, rest = parts
        series = classify(title_of(fm))
        stripped = [ln for ln in fm if not re.match(r'^series:\s', ln)]
        if series is None:
            new_fm = stripped
        else:
            idx = next((k for k, ln in enumerate(stripped)
                        if re.match(r'^title:\s', ln)), -1)
            # Double-quoted: several series names contain '&'.
            new_fm = stripped[:idx + 1] + ['series: "%s"' % series] + stripped[idx + 1:]
        out = '\n'.join(pre + new_fm + rest)
        if out == txt:
            same += 1
            continue
        changed.append((name, series))
        if apply_changes:
            open(path, 'w', encoding='utf-8').write(out)

    print('%s  %s' % ('APPLIED ' if apply_changes else 'DRY RUN ', root))
    print('  changed: %d   already correct: %d   no front matter: %d'
          % (len(changed), same, no_fm))
    for name, series in changed:
        print('    %-28s <- %s' % (series or '(no series)', name))
    return len(changed)


if __name__ == '__main__':
    apply_changes = '--apply' in sys.argv
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = 0
    for root in ('_posts', os.path.join('wdpress', '_posts')):
        full = os.path.join(here, root)
        if os.path.isdir(full):
            total += run(full, apply_changes)
    if not apply_changes and total:
        print('\nre-run with --apply to write these.')
