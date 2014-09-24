from scrapy.selector import Selector
from IntUIScrape.items import Craigslist
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http    import Request



class Craig(CrawlSpider):
    name = "craig"
    rules = ( Rule(SgmlLinkExtractor(allow=("search/vga/\?s=100&","/^s/", ), restrict_xpaths=('//a[@class="button next"]' ,)), callback="parse_items", follow=True), )

    def __init__(self, city, category):
        super(Craig, self).__init__()
        self.city = city
        self.start_urls = ['http://' + str(city) + '.craigslist.org/search/'+str(category)+"?query="]
        self.allowed_domains = [str(city)+".craigslist.org"]
        

    def parse_items(self, response):
        hxs = Selector(response)
        rows = hxs.xpath('//div[@class="content"]/p[@class="row"]')
        for row in rows:
            item = Craigslist()
            link = row.xpath('.//span[@class="pl"]/a')
            url = 'http://'+self.city+'.craigslist.org{}'.format(''.join(link.xpath("@href").extract()))
            item['title'] = link.xpath("text()").extract()
            item['link'] = url
            item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)

    def parse_item_page(self, response):
        hxs = Selector(response)

        item = response.meta['item']
        item['description'] = hxs.xpath('//section[@id="postingbody"]/text()').extract()
        return item

    def parse_start_url(self, response):
        hxs = Selector(response)
        rows = hxs.xpath('//div[@class="content"]/p[@class="row"]')
        for row in rows:
            item = Craigslist()
            link = row.xpath('.//span[@class="pl"]/a')
            url = 'http://'+self.city+'.craigslist.org{}'.format(''.join(link.xpath("@href").extract()))
            item['title'] = link.xpath("text()").extract()
            item['link'] = url
            item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)

class CraigSearch(CrawlSpider):
    name = "craigSearch"


    def __init__(self, city, searchString):
        super(CraigSearch, self).__init__()
        self.city = city
        self.searchString = searchString
        self.start_urls = ['http://'+city+'.craigslist.org/search/sss?query='+searchString+'&sort=rel']
        self.allowed_domains = [str(city)+".craigslist.org"]
        self.rules = ( Rule(SgmlLinkExtractor(allow=('search/sss?s=\d00&query='+ searchString+'&sort=rel', ), restrict_xpaths=('//a[@class="button next"]' ,)), callback="parse_items", follow=True), )

    def parse_items(self, response):
        hxs = Selector(response)
        rows = hxs.xpath('//div[@class="content"]/p[@class="row"]')
        for row in rows:
            item = Craigslist()
            link = row.xpath('.//span[@class="pl"]/a')
            url = 'http://'+self.city+'.craigslist.org{}'.format(''.join(link.xpath("@href").extract()))
            item['title'] = link.xpath("text()").extract()
            item['link'] = url
            item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)

    def parse_item_page(self, response):
        hxs = Selector(response)

        item = response.meta['item']
        item['description'] = hxs.xpath('//section[@id="postingbody"]/text()').extract()
        return item

    def parse_start_url(self, response):
        hxs = Selector(response)
        rows = hxs.xpath('//div[@class="content"]/p[@class="row"]')
        for row in rows:
            item = Craigslist()
            link = row.xpath('.//span[@class="pl"]/a')
            url = 'http://'+self.city+'.craigslist.org{}'.format(''.join(link.xpath("@href").extract()))
            item['title'] = link.xpath("text()").extract()
            item['link'] = url
            item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)

# 'http://'+city+'.craigslist.org/search/sss?query='+searchString+'&sort=rel'