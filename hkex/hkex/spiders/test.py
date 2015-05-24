# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.selector import Selector,HtmlXPathSelector
import sys,re
from hkex.__init__ import StockCode



from hkex.items import HkexItem


class HkexcSpider(CrawlSpider):
    name = 'hkexc1'
    allowed_domains = ['gtimg.cn']
    #start_urls = ['http://www.hkexnews.hk/listedco/listconews/mainindex/SEHK_LISTEDCO_DATETIME_TODAY_C.HTM']
    start_urls = ['http://news.gtimg.cn/notice_more.php?q=hk00717&page=1']
    #for i in a.code:
        #start_urls = ['http://news.gtimg.cn/notice_more.php?q=hk%s&page=1' % i]

    #start_urls = StockCode.urls
    #rules = [
           #   Rule(LinkExtractor(allow=('http://news.gtimg.cn/notice_more.php?q=hk00717&page=\d+'),), callback='get_parse',follow=True)
            #  ]
    
    #def parse(self,response):
    #    type = sys.getfilesystemencoding()
    #    content = response.body
    #    print response.body
    #    print content.decode('UTF-8').encode(type)
    def parse(self,response):
        urls = []  #初始化列表
        #获取页数的总数
        pages = re.findall("'total':\d+",response.body,flags=0)[0]  
        pages = pages[-1]
        #把每一页的网址写入列表
        for page in range(1,int(pages)+1):
            page = response.url + '&page=%d' % page
            urls.append(page)
        #生成迭代器
        for url in urls:
            yield Request(url=url,callback=self.get_parse)
            
            
                
    
    def get_parse(self, response):
        items = []
        content = re.findall('\[.*\]',response.body,flags=0)
        for i in content:
            item = HkexItem()

            #由于抓取的直接是unicode编码，要进行处理
            title = "".join(re.findall('\\\\.*\\\\\w+',i,flags=0))
            title = title.replace('\\\\','\\')
            title = "u'%s'"%title
            title = eval(title)
            item['title'] = title.encode('utf-8')
            item['date'] = "".join(re.findall('\d{4}-\d{2}-\d{2}',i,flags=0)).encode('utf-8')
            #收录网页地址
            item['url'] = "".join(re.findall('http://stock.*-\d+-\d+',i,flags=0))            
            items.append(item)
        return items
        


            



        #items = []
        
        #hxs=Selector(response)
        #sites=hxs.xpath('//tr')
        #for i in response.xpath("//td[@class='arial12black']/text()").extract():
        #for i in sites:
            
            #item = HkexItem()
            #item['number'] = i.xpath("td[@class='arial12black']/text()").extract()
            #item['name'] = i.xpath('td/nobr/text()').extract()
            #item['title'] = i.xpath('td/div[@id="hdLine"]/text()').extract()
            #item['content'] = i.xpath('td/a[@class="news"]/text()').extract()

        #for site in sites:        
            #item['number'] = Selector(response=site).xpath('//td[@class="arial12black"]/text()').extract()
            #item['name'] = site.select('nobr/text()').extract()
            #item['title'] = site.select('//div[@id="hdLine"]/text()').extract()
            #item['content'] = site.select('a[@class="news"]/text()').extract()
        #print item
        #a = Selector(response=response).xpath('//div[@class="aria112back"]').extract()
        #print a
            #items.append(item)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return items
