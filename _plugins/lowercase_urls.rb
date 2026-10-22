# frozen_string_literal: true

# Force every post URL to lowercase so that filenames or explicit permalinks
# with uppercase letters never produce mixed-case URLs on case-sensitive hosts
# (GitHub Pages / Linux).
#
# Does NOT generate redirect pages (that made the build 100x slower).  Instead
# the 404 page carries a small script that lowercases the current path and
# retries — so old uppercase bookmarks still land on the right page.

module AisengSite
  class LowercaseUrls < Jekyll::Generator
    priority :highest

    def generate(site)
      site.posts.docs.each do |post|
        original = post.data["permalink"] || post.url

        normalised = original
          .gsub(" ", "-")
          .unicode_normalize(:nfkc)
          .downcase
          .gsub(/[^a-z0-9\-\/\.]/, "")
          .squeeze("-")

        normalised = normalised.sub(%r{/*$}, "/") unless normalised.end_with?(".html")

        next if normalised == original

        post.data["permalink"] = normalised
        post.instance_variable_set(:@url, nil)
      end
    end
  end
end
