# Deltabrief web pages

The three URLs App Store Connect asks for, as static self-contained pages.

| File | App Store Connect field |
| --- | --- |
| `privacy.html` | **Privacy Policy URL** — required, cannot be left blank |
| `support.html` | **Support URL** — required |
| `index.html` | **Marketing URL** — optional, but it is where the App Store "Developer Website" link goes |

No build step, no JavaScript, no external requests. The CSS is inlined into each page (an identical
copy of `assets/deltabrief.css`, kept there for editing) so the pages survive being moved between
hosts; the only external files are the two icons under `assets/`, so keep that folder alongside them.
Both light and dark appearance are handled.

## Fill these in before publishing

Three placeholders need real values. Grep for them:

```bash
grep -rn "goseng123@gmail.com\|Aisengtech\|href=\"#\"" .
```

1. **`goseng123@gmail.com`** — appears in all three pages. Use an address you actually read.
   Anything on a domain you own is fine; a personal work address is not a good idea on a public page.
2. **`© 2026 Aisengtech`** — replace with the legal name or entity that owns the app, matching the
   Copyright field in App Store Connect.
3. **`href="#"` on the hero button in `index.html`** — the App Store link, which only exists once the
   app is live. Until then either leave it or change the button text to "Coming soon".

The support page promises a reply "within two business days". Change it if that is not a promise you
want to make.

## Deploying to aisengtech.com

The site is Jekyll on GitHub Pages (`aigaosheng/aigaosheng.github.io`, branch `master`). Jekyll
copies HTML files that have no YAML front matter through untouched, so these work as-is. Put them in
a folder at the repo root:

```
deltabrief/
  index.html
  privacy.html
  support.html
  assets/
```

which publishes as `https://aisengtech.com/deltabrief/`, `…/deltabrief/privacy.html` and
`…/deltabrief/support.html`. Those are the URLs to paste into App Store Connect.

Two things to check after the first push: that `_config.yml` does not `exclude` the folder, and that
the pages load over **https** with no redirect chain — App Store Connect validates the URL, and
`www.aisengtech.com` 301-redirects to the apex, so enter the apex form directly.

## Verifying before you submit

```bash
python3 -m http.server 8000 --directory .
```

Then open `http://localhost:8000/index.html`. Check both appearances (macOS System Settings →
Appearance) and a narrow window — the layout is responsive down to 320 px.

Apple's reviewer will open the privacy and support URLs. A 404 on either is a rejection, and it is a
depressingly common one.
