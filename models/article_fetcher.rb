class ArticleFetcher
  attr_reader :post

  def initialize(post)
    @post = post
  end

  def article
    @article ||= begin
      # find parser capable of parsing this website's articles
      raise NoParserError, "no parser for \"#{post.site}\"" unless parser
      parser.new(html).parse
    end
  end

  def html
    RestClient.get(post.url).body
  end

  def parser
    NewsParser.descendants.detect { |p| p.site == post.site }
  end

  # create uuid from article's url
  def uuid
    Digest::SHA1.hexdigest(post.url)
  end

  def create_article
    if Article.where(uuid: uuid).count.positive?
      MainLogger.info 'Article was already created'
      return
    end

    MainLogger.info "fetching: #{post.title}"

    Article.new(uuid: uuid, meta: post.as_json, data: text_analysis.as_json).save!
  end

  def text_analysis
    @text_analysis ||= get_analysis(article)
  end

  private

  def client
    @client ||= Google::Cloud::Language.new
  end

  def get_analysis(content)
    options = {
      extract_syntax: false,
      extract_entities: true,
      extract_document_sentiment: true,
      extract_entity_sentiment: true,
      classify_text: true
    }
    document = {
      content: content,
      type: :PLAIN_TEXT
    }
    client.annotate_text(document, options)
  end
end
