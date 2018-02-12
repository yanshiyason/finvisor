# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ArticleMeta(Item):
    stock_symbols = Field()
    content_type = Field()
    author = Field()
    canonical = Field()
    article_date = Field()
    edition = Field()
    keywords = Field()

class ArticleItem(Item):
    title = Field()
    description = Field()
    meta = Field()
    image_src = Field()
    journalist = Field()
    text = Field()
