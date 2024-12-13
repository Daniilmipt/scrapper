BOT_NAME = 'habr_scraper'

SPIDER_MODULES = ['habr_scraper.spiders']
NEWSPIDER_MODULE = 'habr_scraper.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure user agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Configure item pipelines
ITEM_PIPELINES = {
   'habr_scraper.pipelines.SQLitePipeline': 300,
}