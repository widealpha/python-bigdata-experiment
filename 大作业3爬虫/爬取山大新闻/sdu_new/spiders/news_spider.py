import scrapy
import jieba

from sdu_new.items import SduNewsItem


class NewsSpider(scrapy.Spider):
    name = "sdu_news"
    allowed_domains = ["www.view.sdu.edu.cn"]

    def start_requests(self):
        urls = [
            'https://www.view.sdu.edu.cn/xszh.htm',
            'https://www.view.sdu.edu.cn/xszh/201.htm',
            'https://www.view.sdu.edu.cn/xszh/200.htm',
            'https://www.view.sdu.edu.cn/xszh/199.htm',
            'https://www.view.sdu.edu.cn/xszh/198.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = SduNewsItem()
        item['title'] = ''
        item['content'] = ''
        item['keywords'] = []
        item['link'] = response.url

        item['title'] = response.css('title::text').get()
        if item['title']:
            item['keywords'] += jieba.lcut_for_search(item['title'])
        item['date'] = response.css('div.news_tit p::text')
        if item['date']:
            item['date'] = item['date'].get().replace('年', '-') \
                .replace('月', '-').replace('发布日期：', '').replace('日', '').strip()
        for sel in response.css('div.news_content p::text'):
            item['content'] += sel.extract()
            item['keywords'] += jieba.lcut_for_search(sel.extract())
        item['keywords'] = list(set(item['keywords']))
        yield item
        for next_page in response.css('ul.sublist li a::attr(href)').getall():
            yield response.follow(next_page, callback=self.parse)
