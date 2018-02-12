# -*- coding: utf-8 -*-
import scrapy


class ReutersSpider(scrapy.Spider):
    name = 'reuters'
    allowed_domains = ['reuters.com']
    start_urls = ['http://reuters.com/']

    def parse(self, response):
        pass
