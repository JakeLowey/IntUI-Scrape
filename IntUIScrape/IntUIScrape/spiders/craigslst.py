from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from IntUIScrape.items import Craigslist
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http    import Request
import re
import urlparse

class Craig(CrawlSpider):
    name = "craig"
    allowed_domains = ["albany.craigslist.org"]
    start_urls = ["http://albany.craigslist.org/vga/"]
# ,"craigslist.org/vga/","craigslist.org/vgm/"
    rules = (
        Rule(SgmlLinkExtractor(allow=("index\d00\.html", ), restrict_xpaths=('//a[@class="button next"]' ,)), callback="parse_items", follow=True), )

    # def parse(self, response):
    #     hxs = HtmlXPathSelector(response)
    #     links = hxs.select("//a/@href").extract()
    #     # f = open('workfile.txt', 'a')

    #     #We stored already crawled links in this list
    #     crawledLinks    = []

    #     #Pattern to check proper link
    #     linkPattern     = re.compile("^(?:ftp|http|https):\/\/(?:[\w\.\-\+]+:{0,1}[\w\.\-\+]*@)?(?:[a-z0-9\-\.]+)(?::[0-9]+)?(?:\/|\/(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+)|\?(?:[\w#!:\.\?\+=&amp;%@!\-\/\(\)]+))?$")

    #     for link in links:
    #         # If it is a proper link and is not checked yet, yield it to the Spider
    #         link = urlparse.urljoin(get_base_url(response).strip(), link)
    #         work = linkPattern.match(link)
    #         # f.write(link + " " + str(work) + "\n")
    #         if work and not link in crawledLinks and response.meta['depth'] <= 3:
    #             # f.write(link + str(work) + "\n")
    #             crawledLinks.append(link)
    #             yield Request(link, self.parse)

    #     titles = hxs.select("//span[@class='p1']")
    #     # items = []
    #     for title in titles:
    #         item = Craigslist()
    #         item ["title"] = title.select("a/text()").extract()
    #         item ["link"] = title.select("a/@href").extract()
    #         # item ["image_urls"] = title.select()
    #         yield item

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//div[@class="content"]/p[@class="row"]')
        f = open('workfile.txt', 'a')
        f.write(str(hxs.select('//div[@class="content"]/span[@class="next"]/text()').extract()))
        for row in rows:
            item = Craigslist()
            link = row.xpath('.//span[@class="pl"]/a')
            url = 'http://albany.craigslist.org{}'.format(''.join(link.xpath("@href").extract()))
            item['title'] = link.xpath("text()").extract()
            item['link'] = url
            item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()

            
            yield Request(url=url, meta={'item': item}, callback=self.parse_item_page)

    def parse_item_page(self, response):
        hxs = HtmlXPathSelector(response)

        item = response.meta['item']
        item['description'] = hxs.select('//section[@id="postingbody"]/text()').extract()
        return item




class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["albany.craigslist.org"]
    start_urls = ["http://albany.craigslist.org/vga/"]

    rules = (Rule (SgmlLinkExtractor(allow=("index\d00\.html", ),restrict_xpaths=('//a[@class="button next"]',))
    , callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//span[@class="pl"]')
        items = []
        for titles in titles:
            item = Craigslist()
            item ["title"] = titles.select("a/text()").extract()
            item ["link"] = titles.select("a/@href").extract()
            items.append(item)
        return(items)