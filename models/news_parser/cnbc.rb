class NewsParser::Cnbc < NewsParser
  def parse
    Nokogiri::HTML(html).css('article p').text.strip
  end

  def self.site
    'CNBC'
  end
end
