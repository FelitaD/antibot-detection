# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash
from scrapy_splash import SplashRequest


class CulturaSpider(scrapy.Spider):
    name = 'cultura'
    allowed_domains = ['www.cultura.com']
    # start_urls = ['http://www.cultura.com/musique/genres-musicaux.html/']
    music = 'http://www.cultura.com/musique/genres-musicaux.html/'
    zyte_smartproxy_enabled = True
    zyte_smartproxy_apikey = 'cf2ba4fea79d4babbb9eb625d0dcfb82'

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
        print(response.request.headers)