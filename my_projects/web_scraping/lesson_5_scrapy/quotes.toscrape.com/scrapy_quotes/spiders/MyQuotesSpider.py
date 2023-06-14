import scrapy


class MyquotesspiderSpider(scrapy.Spider):
    name = "MyQuotesSpider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        pass
 