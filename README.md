# aisengtech.com

Source for [aisengtech.com](https://aisengtech.com): AISeng Tech's consulting
pages, Sheng Gao's CV, and daily briefs on enterprise AI, fintech, payments and
AI governance.

Built with [Jekyll](https://jekyllrb.com/) and published to GitHub Pages by a
GitHub Actions workflow.

## Run it locally

Needs Ruby 3.3.6 (see `.ruby-version`).

```bash
bundle install
bundle exec jekyll serve
```

Then open http://127.0.0.1:4000. A local build skips Google Analytics and
AdSense; they load only when `JEKYLL_ENV=production`.

For a full production build, the same one the deploy runs:

```bash
JEKYLL_ENV=production bundle exec jekyll build
```

## Publishing

Push to `master`. [`.github/workflows/pages.yml`](.github/workflows/pages.yml)
builds the site, checks internal links, and deploys it only if the check
passes. Day-to-day work happens on `dev`.

GitHub Settings → Pages → Source must be set to **GitHub Actions**.

## Layout

| Path | What it holds |
| --- | --- |
| `_posts/` | Briefs and articles, one Markdown file each |
| `series/` | One page per recurring column; a post joins a column through its `series:` value |
| `wdpress/` | Posts and images imported from the old WordPress blog |
| `_layouts/`, `_includes/` | Page templates |
| `css/enhancements.css` | Site styles layered on the theme. `css/hux-blog.min.css` is generated from `less/`, so don't edit it by hand |
| `_templates/` | Post template and drafting prompts |
| `_tools/` | Maintenance scripts (below) |
| `deltabrief-site/`, `wraith-site/` | Landing pages for separate apps, served as-is |

## Writing a post

Copy [`_templates/post-template.md`](_templates/post-template.md) into
`_posts/` as `YYYY-MM-DD-short-title.md` and fill in the front matter. Keep the
file name to letters, digits and hyphens: the name becomes the URL, and spaces,
`&`, `?` or `#` make URLs that are hard to share or cannot be linked at all.

## Maintenance scripts

Each script dry-runs by default; read its header before using `--apply`.

| Script | What it does |
| --- | --- |
| `_tools/assign_series.py` | Sets `series:` on briefs from their titles |
| `_tools/write_descriptions.py` | Writes a `description:` for posts that have none |
| `_tools/resize_wdpress.py` | Shrinks WordPress images and fixes links to them |
| `_tools/make_logo.py` | Renders the logo and favicon set |

## Licence

Content (posts, pages, original images) is
[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/); code is
MIT. See [LICENSE](LICENSE).

The theme started from [Hux Blog](https://github.com/Huxpro/huxpro.github.io)
by way of [qiubaiying.github.io](https://github.com/qiubaiying/qiubaiying.github.io).
