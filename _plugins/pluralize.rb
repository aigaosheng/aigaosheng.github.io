module Jekyll
  module PluralizeFilter
    def pluralize(input)
      input.to_i == 1 ? '' : 's'
    end
  end
end

Liquid::Template.register_filter(Jekyll::PluralizeFilter)
