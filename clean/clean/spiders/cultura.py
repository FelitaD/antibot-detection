# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash
from scrapy_splash import SplashRequest


class CulturaSpider(scrapy.Spider):
    name = 'cultura'
    allowed_domains = ['www.cultura.com/musique/genres-musicaux.html']
    # start_urls = ['http://www.cultura.com/musique/genres-musicaux.html/']
    music = 'http://www.cultura.com/musique/genres-musicaux.html/'

    def start_requests(self):
        yield SplashRequest(
            url=self.music,
            callback=self.parse,
            args={
                'wait': 1,
                'html': 1,
                'png': 1,
            },
        )

    def parse(self, response):
        print(response.body)