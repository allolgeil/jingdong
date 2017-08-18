import re
import random
from jdgood.items import JdgoodsItem
from lxml import etree
from scrapy.http import Request

class GoodSpider(scrapy.Spider):
  name = 'good'
  allowed_domains = ['jd.com']
  def start_requests(self):
    ua = ['Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/55.0',
         'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
         'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)']
    req1 = urllib.request.Request('https://book.jd.com/')
    req1.add_header('User-Agent',random.choice(ua))
    allpddata = urllib.request.urlopen(req1).red().decode('utf-8','ignore')
    pat1 = ''#补充内容
    allpd = re.compile(pat1).findall(allpddata)
    catall = []
    for i in allpd:
      thispd = 'http://'+i
      req2 = urllib.request.Request(thispd)
      req2.add_header('User-Agent',random.choice(ua))
      pddata = urllib.request.urlopen(req2).read().decode('utf-8','ignore')
      pat2 = ''#补充内容
      catdata = re.compile(pat2).findall(pddata)
      for j in catdata:
        catall.append(j)
    #print(len(catall))
    #print(catall[0])
    catal2 = set(catall)
    #print(len(catall2))
    allurl = []
    x = 0
    for m in catall2:
      thispdnum = m
      req3 = urllib.request.Request('https://')#补充内容
      req3.add_header('User-Agent',random.choice(ua))
      listdata = urllib.request.urlopen(req3).read().decode('utf-8','ignore')
      pat3 = ''#补充内容
      all
  def parse(self,response):
    
