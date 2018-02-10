class NewsParser
  attr_reader :html

  def initialize(html)
    @html = html
  end

  def parse
    raise 'please override me'
  end

  # site's name same in news-api response
  def site
    raise 'please override me'
  end
end
