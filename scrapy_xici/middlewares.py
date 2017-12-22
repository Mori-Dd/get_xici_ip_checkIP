# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy_xici.proxy import GetIp
from scrapy import signals
ips = GetIp().get_ips()
class ScrapyXiciSpiderMiddleware(object):

    http_n = 0
    https_n = 0
    def process_request(self,request,spider):
        if request.url.startswith('http://'):
            n = ScrapyXiciSpiderMiddleware.http_n
            n=n if n<len(ips['http']) else 0
            request.meta['proxy'] = 'http://%s'%(ips['http'][n])
            ScrapyXiciSpiderMiddleware.http_n += 1
        if request.url.startswith('https://'):
            n = ScrapyXiciSpiderMiddleware.http_n
            n=n if n<len(ips['https']) else 0
            request.meta['proxy'] = 'https://%s'%(ips['https'][n])
            ScrapyXiciSpiderMiddleware.http_n += 1