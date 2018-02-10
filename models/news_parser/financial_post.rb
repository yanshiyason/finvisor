class NewsParser::FinancialPost < NewsParser
  def parse
    doc = Nokogiri::HTML(html)
    doc.css('a[href="http://www.bloomberg.com"]').remove
    doc.css("[itemprop='articleBody'] p").text
  end

  def self.site
    'Financial Post'
  end
end
