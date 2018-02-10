class NewsParser::Bloomberg < NewsParser
  def parse
    Nokogiri::HTML(html).css('article p').text.strip
  end

  def self.site
    'Bloomberg'
  end
end
