# -*- coding: utf-8 -*-
import scrapy
from scrapy_xici.items import ScrapyXiciItem

class XiciIpSpider(scrapy.Spider):
    name = 'xici_ip'
    allowed_domains = ['xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']
    def start_requests(self):
        urls = []
        for i in range(1,3):
            url = scrapy.Request('http://www.xicidaili.com/nn/%s'%i)
            urls.append(url)
        return urls
    def parse(self, response):
        reqs = response.xpath('//*[@id="ip_list"]')
        req = reqs[0].xpath('tr')
        items = []
        for i in req[1:]:
            xici_item = ScrapyXiciItem()
            xici_item['IP'] = i.xpath('td[2]/text()')[0].extract()
            xici_item['PORT'] = i.xpath('td[3]/text()')[0].extract()
            xici_item['POSTION'] = i.xpath('string(td[4])')[0].extract().strip()
            xici_item['TYPE'] = i.xpath('td[5]/text()')[0].extract()
            xici_item['ATTR'] = i.xpath('td[6]/text()')[0].extract()
            xici_item['SPEED'] = i.xpath('td[7]/div/@title').re('\d{0,2}\.\d{0,}')[0]
            xici_item['LAST_CHECK_TIME'] = i.xpath('td[10]/text()')[0].extract()
            items.append(xici_item)
        return items
