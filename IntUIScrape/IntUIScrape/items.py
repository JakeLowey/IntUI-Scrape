# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy.item import Item, Field, DictItem


# class IntuiscrapeItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class Craigslist(Item):
  title = Field()
  link = Field()
  price = Field()
  description = Field()
  image_urls = Field()
  lat = Field()
  lon = Field()


def dynamic_item(class_name, field_list):
    field_dict = {}
    for field_name in field_list:
        field_dict[field_name] = Field()
    return type(class_name, (DictItem,), field_dict)