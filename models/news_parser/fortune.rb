class NewsParser::Fortune < NewsParser
  def parse
    Nokogiri::HTML(html).css('#article-body p').text.strip
  end

  def self.site
    'Fortune'
  end
end
