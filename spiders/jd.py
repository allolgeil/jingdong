# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jingdong.items import JingdongItem
from lxml import etree
from scrapy.http import Request

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    #start_urls = ['http://jd.com/']

    def start_requests(self):
        ua = ['Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/55.0',
              'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)']
        req1 = urllib.request.Request('https://book.jd.com/')
        req1.add_header('User-Agent', random.choice(ua))
        allpddata = urllib.request.urlopen(req1).read().decode('utf-8', 'ignore')
        pat1 = '"(https:\/\/book.jd.com\/library\/life.html)$'
        allpd = re.compile(pat1).findall(allpddata)
        catall = []
        try:
            for i in range(len(allpd)):
                thispd = allpd[i]
                thispd2 = thispd.replace('\\','')
                req2 = urllib.request.Request(thispd2)
                req2.add_header('User-Agent', random.choice(ua))
                pddata = urllib.request.urlopen(req2).read().decode('utf-8', 'ignore')
                print(len(pddata))
        except Exception as err:
            print(err)
    def parse(self, response):
        pass
