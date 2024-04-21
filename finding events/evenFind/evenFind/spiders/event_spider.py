from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
class CrawlingSpieder(CrawlSpider):
    #scrapy crawl event_spider
    numberOfPage = 4
    name = 'event_spider'
    allowed_domains = ['www.eventbrite.com']
    start_urls = ['https://www.eventbrite.com/d/md--college-park/']
    user_agent = '*'
    rules =(
        Rule(LinkExtractor(allow=("/e/","/d/md--college-park/events--today/"),deny=("/l/","/ttd/")), callback='parse_item', follow=True ),

    )

    def morePage(self, start_urls):
        for i in range(1, self.numberOfPage+1):
            start_urls.append("https://www.eventbrite.com/d/md--college-park/events--today/?page="+i)

    def parse_item(self, response):

        yield{
            "name": response.css("h1::text").get(),
            "link": response.url,
            "description": response.css("p::text").getall()
        }




def run_spider():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    })

    process.crawl(CrawlingSpieder)
    process.start()

    # Read the output file and return the data
    with open('output.json', 'r') as file:
        data = file.read()

    return data