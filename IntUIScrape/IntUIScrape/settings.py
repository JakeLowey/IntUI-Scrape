# -*- coding: utf-8 -*-

# Scrapy settings for IntUIScrape project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'IntUIScrape'

SPIDER_MODULES = ['IntUIScrape.spiders']
NEWSPIDER_MODULE = 'IntUIScrape.spiders'

COOKIES_ENABLED = False

ITEM_PIPELINES = {
	
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'IntUIScrape (+http://www.yourdomain.com)'
