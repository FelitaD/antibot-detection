# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash
from scrapy_splash import SplashRequest


class CulturaSpider(scrapy.Spider):
    name = 'cultura'
    allowed_domains = ['www.cultura.com']
    # start_urls = ['http://www.cultura.com/musique/genres-musicaux.html/']
    music = 'http://www.cultura.com/musique/genres-musicaux.html'
    zyte_smartproxy_enabled = True
    zyte_smartproxy_apikey = 'cf2ba4fea79d4babbb9eb625d0dcfb82'

    def start_requests(self):
        lua_script = '''
                    function main(splash, args)
                        url = args.url
                        assert(splash:go(url))
                        assert(splash:wait(5))
                        return splash:html()
                    end
                '''

        yield SplashRequest(
            url=self.music,
            callback=self.parse,
            endpoint='execute',
            args={
                'wait': 1,
                'html': 1,
                'png': 1,
                'lua_source': lua_script,
                'splash_headers': {
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,'
                              'image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept_encoding': 'gzip, deflate, br',
                    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                    'referer': 'https://www.google.com/',
                    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': 'macOS',
                    'sec-ch-fetch-dest': 'document',
                    'sec-ch-fetch-mode': 'navigate',
                    'sec-ch-fetch-site': 'same-origin',
                    'sec-ch-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, '
                                  'like Gecko) Chrome/94.0.4606.81 Safari/537.36',
                }
            },
        )

    def parse(self, response):
        print(response.body)
        print(response.request.headers)
