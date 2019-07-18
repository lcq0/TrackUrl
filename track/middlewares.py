# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

import random
from scrapy.conf import settings

class TrackSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
    # ip


class ProxyMiddleware(object):
    ip_list = settings['IP_LIST']

    def process_request(self, request, spider):
        ip = random.choice(self.ip_list)
        request.meta['proxy'] = ip


from selenium import webdriver
from scrapy.http import HtmlResponse
from track import settings

class JSPageMiddleware(object):

    # 通过chrome 动态访问
    def process_request(self, request, spider):
        if spider.name == "track_spider":
            # request.url = settings['domain']
            url = settings.domain
            spider.browser.get(url)
            # import time
            # time.sleep(3)
            # print("访问：{0}".format(request.url))
            # # spider.browser.find_element_by_xpath('//div[@class="btn-wrapper fl"]/a[@class="query-submit-btn"]').click()
            #
            # # spider.browser.find_element_by_xpath('//div[@class="CodeMirror-sizer"]').send_keys("1.RS912523242CH")
            # # spider.browser.find_element_by_xpath('//form/div"]').send_keys("RS912523242CH")
            # spider.browser.find_element_by_xpath('//input[@name="mailNo"]').send_keys("90747786567")
            # # spider.browser.find_element_by_xpath('//div[@class="form-group has-feedback m-l-lg m-r-lg m-t-xs m-b-none"]/input[@name="pwdNormal"]').send_keys("你自己的密码")
            # time.sleep(2)
            # spider.browser.find_element_by_xpath('//div[@class="hidden-xs yq-tools-big"]/button[2]').click()
            # # spider.browser.find_element_by_xpath('//form/a[@class="btn btn-default"]"]/button[2]').click()
            # spider.browser.find_element_by_xpath(
            #     '//div[@class="btn-wrapper fl"]/input[@class="query-submit-btn"]').click()
            # time.sleep(2)
            # print(spider.browser.page_source)
            return HtmlResponse(url=spider.browser.current_url, body=spider.browser.page_source, encoding="utf-8")
