class NewsParser::BusinessInsider < NewsParser
  def parse
    doc = Nokogiri::HTML(html)
    doc.css('.image-container').remove
    doc.css('[itemtype="http://schema.org/Article"]').remove
    doc.css('.post p').text.strip
  end

  def self.site
    'Business Insider'
  end
end
