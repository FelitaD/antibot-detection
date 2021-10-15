# -*- coding: utf-8 -*-
import scrapy
from scrapy-splash import


class CulturaSpider(scrapy.Spider):
    name = 'cultura'
    allowed_domains = ['www.cultura.com/musique/genres-musicaux.html']
    start_urls = ['http://www.cultura.com/musique/genres-musicaux.html/']

    def parse(self, response):
        pass
