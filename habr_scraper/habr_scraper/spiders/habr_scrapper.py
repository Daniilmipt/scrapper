import scrapy
from habr_scraper.items import HabrArticleItem
from datetime import datetime

class HabrSpider(scrapy.Spider):
    name = 'habr'
    allowed_domains = ['habr.com']
    start_urls = ['https://habr.com/ru/feed/']

    def parse(self, response):
        # Extract all article links with titles
        articles = response.css('a.tm-title__link')
        
        for article in articles:
            item = HabrArticleItem()
            item['title'] = article.css('span::text').get()
            item['url'] = 'https://habr.com' + article.attrib['href']
            item['collected_at'] = datetime.now().isoformat()
            
            yield item