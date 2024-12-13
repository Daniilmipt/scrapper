import scrapy

class HabrArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    collected_at = scrapy.Field()