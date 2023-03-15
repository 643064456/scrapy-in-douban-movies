import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from spider.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']

    def start_requests(self):
        for page in range(10):
            yield Request(url=f'https://movie.douban.com/top250?start={page * 25}&filter=')

    def parse(self, response: HtmlResponse, **kwargs):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for list_item in list_items:
            detail_url = list_item.css('div > div.info > div.hd > a::attr(href)').get()
            movie_item = MovieItem()
            movie_item['title'] = list_item.css('span.title::text').get() or ''
            movie_item['rating_num'] = list_item.css('span.rating_num::text').get() or ''
            yield Request(url=detail_url, callback=self.detail_parse, cb_kwargs={'item': movie_item})

    def detail_parse(self, response, **kwargs):
        movie_item = kwargs['item']
        sel = Selector(response)
        movie_item['mold'] = sel.css('span[property="v:genre"]::text').getall() or ''
        movie_item['duration'] = sel.css('span[property="v:runtime"]::attr(content)').get() or ''
        yield movie_item

