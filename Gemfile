source 'https://rubygems.org'

# The github-pages meta-gem was dropped because its last release (232) pins
# jekyll-remote-theme 0.4.3, which caps rubyzip below 3.0 and so can never pick
# up the fix for CVE-2026-85396 (GHSA-47m2-wp7j-p9vc). The gems below are the
# subset this site uses, pinned to the versions github-pages 232 ships, so local
# builds match the GitHub Pages build. GitHub Pages itself ignores this file.
gem "jekyll", "3.10.0"
gem "jekyll-theme-primer", "0.6.0"
gem "jekyll-sass-converter", "1.5.2"
gem "kramdown", "2.4.0"
gem "kramdown-parser-gfm", "1.1.0"
gem "rouge", "3.30.0"
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-feed", "0.17.0"
  gem "jekyll-seo-tag", "2.8.0"
  gem "jekyll-paginate", "1.1.0"
  # Enabled by default on GitHub Pages
  gem "jekyll-coffeescript", "1.2.2"
  gem "jekyll-commonmark-ghpages", "0.5.1"
  gem "jekyll-gist", "1.5.0"
  gem "jekyll-github-metadata", "2.16.1"
  gem "jekyll-relative-links", "0.6.1"
  gem "jekyll-optional-front-matter", "0.3.2"
  gem "jekyll-readme-index", "0.3.0"
  gem "jekyll-default-layout", "0.1.5"
  gem "jekyll-titles-from-headings", "0.5.3"
end

gem "jekyll-octicons"
gem "jemoji"
