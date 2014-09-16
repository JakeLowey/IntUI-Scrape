from scrapy.selector import Selector
from IntUIScrape.items import dynamic_item
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http    import Request



class Craig(CrawlSpider):
    name = "dynam"


    def __init__(self, *args, **kwargs):
        super(Craig, self).__init__(**kwargs)
        fields = []
        for key, value in kwargs:
            fields.append(key)
        dynItem = dynamic_item("dynItem", fields)

        self.start_urls = kwargs['star_urls']
        self.allowed_domains = kwargs['allowed_domains']
        self. rules = ( Rule(SgmlLinkExtractor(allow=("index\d00\.html", ), restrict_xpaths=('//a[@class="button next"]' ,)), callback="parse_items", follow=True), )


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

# 'http://'+city+'.craigslist.org/search/sss?query='+searchString+'&sort=rel'