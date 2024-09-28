from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class UniversalSpider(CrawlSpider):
    name = 'universal_spider'
    
    def __init__(self, *args, **kwargs):
        self.allowed_domains = kwargs.get('allowed_domains', [])
        self.start_urls = kwargs.get('start_urls', [])
        
        # Default to 'books.toscrape.com' if none are provided
        if not self.allowed_domains:
            self.allowed_domains = ['toscrape.com']
        if not self.start_urls:
            self.start_urls = ['http://books.toscrape.com/']
        
        UniversalSpider.rules = (
            Rule(LinkExtractor(), callback='parse_item', follow=True),
        )
        super(UniversalSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        yield {
            "url": response.url,
            "title": response.css("title::text").get(),
            "body": response.css("body").get(),
        }
