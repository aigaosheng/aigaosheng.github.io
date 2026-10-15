# frozen_string_literal: true

# Build-time helpers for the post and page layouts.
#
# These used to be Liquid loops that ran on every one of ~3,300 pages:
#
#   - each post scanned all ~2,750 posts twice ("where: 'series'") for its
#     newer/older editions and its "More in <series>" list, and all pages once
#     for its series page;
#   - every page with a sidebar walked all ~2,500 tags to pick the featured ones.
#
# The featured-tags walk alone was 30 s of an 86 s build. Each answer below is
# computed once per build instead.
#
# Requires `safe: false` (see _config.yml). Classic GitHub Pages never ran
# _plugins/; the site is built by .github/workflows/pages.yml, which does.

require "cgi"

module AisengSite
  # Sets on each post in a series:
  #   series_url     URL of the series page under series/, if there is one
  #   series_newer   next newer edition in the same series (a post), or nil
  #   series_older   next older edition, or nil
  #   series_recent  up to five most recent other editions, newest first
  #
  # And site.data.featured_tags: [{ "name", "count" }] for the sidebar cloud,
  # tags used more than featured-condition-size times, capped at
  # featured-tags-max, in site.tags order.
  class SiteIndex < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      series_urls = {}
      site.pages.each do |page|
        name = page.data["series"]
        series_urls[name] ||= page.url if name
      end

      by_series = Hash.new { |h, k| h[k] = [] }
      site.posts.docs.each do |post|
        name = post.data["series"]
        by_series[name] << post if name
      end

      by_series.each do |name, posts|
        newest_first = posts.sort_by(&:date).reverse
        newest_first.each_with_index do |post, i|
          post.data["series_url"] = series_urls[name]
          post.data["series_newer"] = i.positive? ? newest_first[i - 1] : nil
          post.data["series_older"] = newest_first[i + 1]
          post.data["series_recent"] = newest_first.first(6).reject { |e| e.equal?(post) }.first(5)
        end
      end

      threshold = site.config["featured-condition-size"].to_i
      cap = site.config["featured-tags-max"]
      featured = site.tags.select { |_, posts| posts.size > threshold }
      featured = featured.first(cap.to_i) if cap
      site.data["featured_tags"] = featured.map { |name, posts| { "name" => name, "count" => posts.size } }
    end
  end

  # Marks mainly-Chinese posts `lang: zh-CN`, unless the post sets `lang:`
  # itself. That sets <html lang>, og:locale, and which Pagefind search index
  # the post goes into (Pagefind splits Chinese text into words only for pages
  # marked as Chinese).
  #
  # "Mainly Chinese": Han characters outnumber English words, counting a word
  # as five letters. Links, URLs and HTML tags are ignored. On the Oct 2026
  # archive this marks 65 of ~3,030 posts; the next-highest English post
  # scores under 0.25, so the 0.5 cut-off is not borderline.
  module Language
    HAN = /\p{Han}/
    LATIN = /[A-Za-z]/
    NOISE = %r{\]\([^)]*\)|https?://\S+|<[^>]+>}

    def self.chinese?(text)
      text = text.to_s.gsub(NOISE, "")
      han = text.scan(HAN).size
      return false if han.zero?

      han / (han + text.scan(LATIN).size / 5.0) >= 0.5
    end
  end

  Jekyll::Hooks.register :posts, :pre_render do |post, _payload|
    next if post.data.key?("lang")

    post.data["lang"] = "zh-CN" if Language.chinese?(post.content)
  end

  # Drops a post's opening <h1> when it only restates the title.
  #
  # The header in _layouts/post.html is the page's <h1>. About 1,000 posts
  # also open with an <h1> repeating the title, often with an emoji in front
  # or the date in a different form ("🤖🏢 ENTERPRISE AI DAILY BRIEF" under
  # "ENTERPRISE AI DAILY BRIEF April 2, 2026"), which put the title on screen
  # twice and gave the page two top-level headings.
  #
  # Counted as a restatement when, ignoring case, spaces, punctuation and
  # emoji, the two share their first 12 characters, or one is a prefix of the
  # other. An opening <h1> that is something else ("Investment Whitepaper" on
  # "How will AI transform Retail") is kept.
  module LeadHeading
    # Leading horizontal rules are skipped: some posts open with "---" above
    # the title heading. They go with it, as decoration of the old title.
    OPENING_H1 = %r{\A\s*(?:<hr\b[^>]*>\s*)*<h1\b[^>]*>(.*?)</h1>\s*}m

    def self.normalize(text)
      CGI.unescapeHTML(text.to_s.gsub(/<[^>]+>/, "")).downcase.gsub(/[^\p{L}\p{N}]+/, "")
    end

    def self.restates?(heading, title)
      h = normalize(heading)
      t = normalize(title)
      return false if h.empty? || t.empty?

      shared = h.each_char.zip(t.each_char).take_while { |a, b| a == b }.size
      shared >= [12, h.size, t.size].min
    end
  end

  # Moves every heading in a post body down one level (h1 -> h2 ... h5 -> h6)
  # when the body still has an <h1> after LeadHeading has run.
  #
  # About 220 posts were written with "#" for their section headings, so each
  # section was a top-level heading competing with the title. Shifting the
  # whole outline, rather than only the h1s, keeps the sections' own
  # sub-headings beneath them. Posts with their own <style> or <script> (the
  # interactive guides) are skipped, since their CSS and JS may target
  # specific heading levels.
  module HeadingLevels
    TAG = %r{<(/?)h([1-6])\b}

    def self.shift(html)
      return html unless html.match?(/<h1\b/)
      return html if html.match?(/<(?:style|script)\b/)

      html.gsub(TAG) { "<#{Regexp.last_match(1)}h#{[Regexp.last_match(2).to_i + 1, 6].min}" }
    end
  end

  Jekyll::Hooks.register :posts, :post_convert do |post|
    match = post.content.match(LeadHeading::OPENING_H1)
    post.content = match.post_match if match && LeadHeading.restates?(match[1], post.data["title"])
    post.content = HeadingLevels.shift(post.content)
  end
end
