import scrapy

class Jdgoods Item(scrapy.Item):
  pdnum = scrapy.Field()
  pd1 = scrapy.Field()
  pd2 = scrapy.Field()
  name = scrapy.Field()
  price = scrapy.Field()
  pnum = scrapy.Field()
  author = scrapy.Field()
  pub = scrapy.Field()
  seller = scrapy.Field()
