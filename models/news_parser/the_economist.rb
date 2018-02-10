class NewsParser::TheEconomist < NewsParser
  def parse
    Nokogiri::HTML(html).css('article p').text.strip
  end

  def self.site
    'The Economist'
  end
end
