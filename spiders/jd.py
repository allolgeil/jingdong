import re
import urllib.request
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
    allpddata = urllib.request.urlopen(req1).read().decode('utf-8','ignore')
    pat1 = ''#所有大频道
    allpd = re.compile(pat1).findall(allpddata)
    catall = []
    for i in allpd:
      thispd = 'http://'+i
      req2 = urllib.request.Request(thispd)
      req2.add_header('User-Agent',random.choice(ua))
      pddata = urllib.request.urlopen(req2).read().decode('utf-8','ignore')
      pat2 = 'href="//list.jd.com/list.html?cat=([0-9,]*?)[&"]'#补充内容href="//list.jd.com/list.html?cat=1713,3258,6569&go=0"
      catdata = re.compile(pat2).findall(pddata)
      for j in catdata:
        catall.append(j)
    #print(len(catall))
    #print(catall[0])
    catal2 = set(catall) #去重 功能
    #print(len(catall2))
    allurl = []
    x = 0
    for m in catall2:
      thispdnum = m
      req3 = urllib.request.Request('https://')#各个小频道url
      req3.add_header('User-Agent',random.choice(ua))
      listdata = urllib.request.urlopen(req3).read().decode('utf-8','ignore')
      pat3 = ''#各个小频道总页数
      allpage = re.compile(pat3).findall(listdata)
      if(len(allpage)>0):
        pass
      else:
        allpage = [1]
      allurl.append({thispdnum:allpage[0]})
      #测试
      if(x>2):
        break
      x+=1
    x = 0 
    for n in catall2:
      thispage = allurl[x][n]
      for p in range(1,int(thispage)+1):
        thispageurl = ''#各个小频道的url
        print(thispageurl)
        yield Request(thispageurl,callback=self.parse)
      x+=1
  def parse(self,response):
    pd = response.xpath()#频道xpath表达式
    if(len(pd)==0):
      pd = ['无','无']
    if(len(pd)==1):
      pda = pd[0]
      pd = [pda,'无']
    pd1 = pd[0]
    pd2 = pd[1]
    print(pd1)
    bookname = response.xpath('')#书名xpath表达式
    print(bookname[0])
    allskupat = ''#价格pattern
    allsku = re.compile(allskupat).findall(listdata)
    print(allsku)
    author = response.xpath('')#作者xpath
    pub = response.xpath('')#出版社
    seller = response.xpath('')#卖家
    for n in range(0,len(seller)):
      name = bookname[n+3]
      thissku = allsku[n]
      priceurl = ''#价格连接
      pricepat = ''#价格pattern
      price = re.compile(pricepat).findall(pricedata)[0]
      pnumurl = ''#数量url
      pnumdata = urllib.request.urlopen().read().decode('utf-8','ignore')
      pnumpat = ''#数量pattern
      pnum = re.compile(pnumpat).findall(pnumdata)
      thisauthor = author[n]
      thispub = pub[n]
      thisseller = seller[n]
      print(pd1)
      print(pd2)
      print(name)
      print(author)
      print(pub)
      print(seller)
