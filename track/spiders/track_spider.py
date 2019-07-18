# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from selenium.webdriver.chrome.options import Options
from track import settings

class TrackSpiderSpider(scrapy.Spider):
    name = 'track_spider'
    allowed_domains = ['www.asiabill.com']
    #入口URL
    start_urls = ['https://www.asiabill.com']
    key1 = 'asiabill.com'
    key2 = 'http'
    url_list = []
    url_list_out = []

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path="E:/GoogleD/chromedriver_win32_new/chromedriver.exe")
        super(TrackSpiderSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候 关闭chrome

        print("spider closed")
        self.browser.quit()

    def parse(self, response):
        from lxml import etree
        html = response.text.encode('utf-8')
        selector = etree.HTML(html)
        item_list = selector.xpath("//a/@href")
        for it in item_list:
            # print(it)
            temp = str(it)
            if temp.find(self.key1) < 0:
                if temp.find(self.key2) >= 0:
                    self.url_list_out.append(temp)
                    # print('外部链接：'+temp)
                else:
                    t_url = settings.domain+temp
                    # print('内部链接：'+t_url)
                    if t_url not in self.url_list:
                        self.url_list.append(t_url)
                        yield scrapy.Request(t_url, callback=self.parse)
                    else:
                        continue
            else:
                if temp == settings.domain or temp == settings.domain+'/':
                    continue
                else:
                    if temp not in self.url_list:
                        self.url_list.append(temp)
                        yield scrapy.Request(temp, callback=self.parse)
                    else:
                        continue
            print(self.url_list)
            # next_link = response.xpath("//span[@class='next']/link/@href").extract()
            # if next_link:
            #     next_link = next_link[0]
            #     yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)
        # kuaidi = response.xpath('//table[@class="json_data asc"]/tbody')
        # for kuai in kuaidi:
        #     shouci = kuai.xpath('tr[@class=" odd  first "]')
        #     for shou in shouci:
        #         shijian = shou.xpath('td[@class="col-1"]/text()').extract()
        #         dizhi = shou.xpath('td[@class="col-3"]/text()').extract()
        #         print(shijian)
        #         print(dizhi)
        #     guocheng = kuai.xpath('tr[@class=" even "]')
        #     for guo in guocheng:
        #         shijian1 = guo.xpath('td[@class="col-1"]/text()').extract()
        #         dizhi1 = guo.xpath('td[@class="col-3"]/text()').extract()
        #         print(shijian1)
        #         print(dizhi1)
        #     guocheng1 = kuai.xpath('tr[@class=" odd "]')
        #     for guo1 in guocheng1:
        #         shijian3 = guo1.xpath('td[@class="col-1"]/text()').extract()
        #         dizhi3 = guo1.xpath('td[@class="col-3"]/text()').extract()
        #         print(shijian3)
        #         print(dizhi3)
        #     jieshu = kuai.xpath('tr[@class]=" odd  last  sign "')
        #     for jie in jieshu:
        #         shijian2 = jie.xpath('td[@class="col-1"]/text()').extract()
        #         print(shijian2)
        #         dizhi2 = jie.xpath('td[@class="col-3"]/text()').extract()
        #         print(dizhi2)

