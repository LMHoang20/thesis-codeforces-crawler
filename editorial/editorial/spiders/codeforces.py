import scrapy


class CodeforcesSpider(scrapy.Spider):
    name = "codeforces"
    allowed_domains = ["codeforces.com"]
    start_urls = ["https://codeforces.com"]

    def parse(self, response):
        pass
