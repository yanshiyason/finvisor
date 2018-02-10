class NewsParser::BbcNews < NewsParser
  def parse
    Nokogiri::HTML(html).css("[property='articleBody']").css('p').text
  end

  def self.site
    'BBC News'
  end
end
