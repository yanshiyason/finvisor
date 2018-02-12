# -*- coding: utf-8 -*-
import pdb
from scrapy import Request, Spider
from scrapy.linkextractors import LinkExtractor
from news_crawler.items.reuters import ArticleItem, ArticleMeta

class ReutersSpider(Spider):
    name = 'reuters'
    allowed_domains = ['reuters.com']

    article_link_extractor = LinkExtractor(
        allow=('/article/'),
        allow_domains=('reuters.com')
    )

    custom_settings = {
        'ITEM_PIPELINES': {
           'news_crawler.pipelines.mongo.MongoPipeline': 900,
        },
    }

    def start_requests(self):
        urls = [
            'https://www.reuters.com/news/technology',
            'https://www.reuters.com/investing/news',
            'https://www.reuters.com/finance',
            'https://www.reuters.com/finance/deals',
            'https://www.reuters.com/finance/markets',
        ]

        for url in urls:
            yield Request(
                url=url,
                headers={
                'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
                'referer': 'https://jp.reuters.com/',
                'authority': 'www.reuters.com',
                'cookie': 'lastVisited=www.reuters.com',
                },
                callback=self.parse
            )

    def parse(self, response):
        print("--- PARSE ---")
        article_links = self.article_link_extractor.extract_links(response)

        print("--- articles length: ", len(article_links), " ---")

        for link in article_links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        article = ArticleParser.parse(response)
        if article != None:
            print("--- YIELDING ARTICLE ---")
            yield article


class ArticleParser(object):
    @classmethod
    def parse(cls, response):
        title         = response.css('meta[name="analyticsAttributes.title"]::attr(content)').extract_first()
        description   = response.css('meta[name="description"]::attr(content)').extract_first()
        stock_symbols = response.css('a[href*=stocks\/overview\?symbol]::text').extract()
        content_type  = response.css('meta[name="analyticsAttributes.contentType"]::attr(content)').extract_first()
        author        = response.css('meta[name="analyticsAttributes.author"]::attr(content)').extract_first()
        canonical     = response.css('link[rel="canonical"]::attr(href)').extract_first()
        article_date  = response.css('meta[name="analyticsAttributes.articleDate"]::attr(content)').extract_first()
        edition       = response.css('meta[name="analyticsAttributes.edition"]::attr(content)').extract_first()
        keywords      = response.css('meta[name="keywords"]::attr(content)').extract_first().split(",")
        image_src     = response.css('link[rel="image_src"]::attr(href)').extract_first()
        journalist    = response.css('a[href*=\/journalists\/]::text').extract_first()

        # `p`s with classes are just noise
        article_paragraphs = response.xpath('descendant-or-self::p[not(@class)]/text()').extract()

        if title == None:
            pass

        return ArticleItem(
            title=title,
            description=description,
            meta=ArticleMeta(
                stock_symbols=stock_symbols,
                content_type=content_type,
                author=author,
                canonical=canonical,
                article_date=article_date,
                edition=edition,
                keywords=keywords,
            ),
            image_src=image_src,
            journalist=journalist,
            text=article_paragraphs,
        )
