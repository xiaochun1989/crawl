# -*- coding: utf-8 -*-

# Scrapy settings for hkex project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hkex'

SPIDER_MODULES = ['hkex.spiders']
NEWSPIDER_MODULE = 'hkex.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'hkex (+http://www.yourdomain.com)'
# 设置等待时间缓解服务器压力 并隐藏自己
DOWNLOAD_DELAY = 0.25
COOKIES_ENABLES=False  #禁用cookie
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
        'hkex.spiders.hkex_middle.hkex_AgentMiddleware' :400
    }
RANDOMIZE_DOWNLOAD_DELAY = True
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1653.0 Safari/537.36'

# 配置使用的数据管道
ITEM_PIPELINES = ['hkex.pipelines.hkexPipeline']


MONGODB_SERVER = 'localhost'  # 这里都是默认的设置，不需要修改
MONGODB_PORT = 27017
MONGODB_DB = 'hkexdb'
MONGODB_COLLECTION = 'hkex'