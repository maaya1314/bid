#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree
from selenium.webdriver.support.wait import WebDriverWait

sys.path.append('..')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_3 import Bid3
from bid_conf.conf_3 import parse_dict
urllib3.disable_warnings()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class BidCY(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '云采链线上采购一体化平台-调研公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 隐藏浏览器
        options.add_argument("service_args=['–ignore-ssl-errors=true', '–ssl-protocol=TLSv1']")  # Python2/3
        self.driver = webdriver.Firefox(options=options)
        driver_url = 'http://www.choicelink.cn/channels/4796.html'
        # options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # self.driver = webdriver.Firefox(options=options, proxy=proxy)
        # self.driver.set_page_load_timeout(TIMEOUT)
        self.driver.implicitly_wait(10)  # 隐性等待，最长等30秒
        self.driver.get(driver_url)
        time.sleep(10)
        channel = self.driver.find_element_by_xpath("//div[@id='tab-second']")
        channel.click()
        time.sleep(1)
        search = self.driver.find_element_by_xpath("//div[@class='search-input']/input")
        search.send_keys(self.keyword)
        time.sleep(1)
        confirm = self.driver.find_element_by_xpath("//div[@class='search-input']/button[@class='ripple']")
        confirm.click()
        url_base = 'https://siteserver.choicelink.cn/api/LjSiteServer/GetRKSiteServerList?pageSize=30&offset={}&query=SiteId%3D%274795%27+AND+ChannelId+IN(%275146%27,%275147%27,%275148%27,%275149%27)+AND+title+LIKE+%27%25{}%25%27'
        self.host = urlparse(url_base).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1
        url = url_base.format((page - 1) * 30, quote(keyword))
        content = self.req(url, rsp_type='json', headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        total = content.get("totalCount")
        if not total:
            self.log.debug("{} not data".format(keyword))
            return
        pages = total // 30 + 1 if not total % 30 == 0 else total // 30
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        if pages < 2:
            self.driver.quit()
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            url = url_base.format((page - 1) * 30, keyword)
            self.log.info("now start page :{}, {}".format(page, keyword))
            content = self.req(url, rsp_type='json', headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            next_page_button = self.driver.find_element_by_xpath("//button[@class='btn-next']")
            next_page_button.click()
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))
        self.driver.quit()

    def list_parse(self, content, url):
        first_handle = self.driver.current_window_handle
        tab_items = self.driver.find_elements_by_xpath("//div[@class='project-name-wrapper']/span[2]")
        if not tab_items:
            self.log.error("{} no items".format(self.keyword))
        json_items = content.get("items")
        if not json_items:
            self.log.error("{} no items".format(self.keyword))
        if len(json_items) < len(tab_items):
            tab_items = tab_items[:len(json_items) + 1]
        for index, tab_item in enumerate(tab_items):
            try:
                tab_item.click()
                time.sleep(10)
            except Exception as e:
                self.log.error(e)
                continue
            time.sleep(1)
            # self.driver.set_page_load_timeout(30)
            # wait = WebDriverWait(self.driver, 30, 0.2)
            # wait.until(lambda x: x.find_element_by_xpath("//table"))
            # "//div[@class='content-title']"
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            # ActionChains(self.driver).key_down(Keys.COMMAND).send_keys("w").key_up(Keys.COMMAND).perform()
            # ActionChains(self.driver).key_down(Keys.ALT).send_keys("w").key_up(Keys.ALT).perform()
            # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        # html = etree.HTML(content)
        # items = html.xpath("//form/table[1]//tr")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
            if self.exit_flag:
                return
            # object_id = json_items[index].get("id")
            # channelId = json_items[index].get('channelId')
            # siteId = json_items[index].get("siteId")
            # todo
            # detail_url = 'http://z.choicelink.cn/api/v1/stl/content?siteId={}&contentId={}&channelId={}'.format(siteId, object_id, channelId)
            # headers = {
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #     'Accept-Encoding': 'gzip, deflate',
            #     'Accept-Language': 'zh-CN,zh;q=0.9',
            #     'Cache-Control': 'no-cache',
            #     'Pragma': 'no-cache',
            #     'Proxy-Connection': 'keep-alive',
            #     'Upgrade-Insecure-Requests': '1',
            #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            #     'X-SS-API-KEY': 'dc28fbeb-0a0d-4934-bc79-522c6382c187',
            # }
            # try:
            #     detail_content = self.req(url=detail_url, rsp_type='json', headers=headers, verify=False)
            # except Exception as e:
            #     self.log.exception(e)
            #     continue
            detail_content = ''
            try:
                iframe = self.driver.find_elements_by_xpath("//iframe[@frameborder='0']")
                for ifr in iframe:
                    self.driver.switch_to.frame(ifr)
                    detail_content = self.driver.page_source
                    self.driver.switch_to_default_content()
                if not iframe:
                    detail_content = self.driver.page_source
            except Exception as e:
                self.log.error(e)
            detail_url = self.driver.current_url
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            data['project_title'] = json_items[index].get("title")
            data['publish_time'] = json_items[index].get("addDate")
            data['tender_unit'] = json_items[index].get("purchaseName")
            data['tender_price'] = json_items[index].get("projectBudget")
            # data['agency'] = json_items[index].get("platformName")
            # data['bid_finish_time'] = json_items[index].get("uppriceFromTime")
            data['bid_end_time'] = json_items[index].get("uppriceToTime")
            # detail_json_content = detail_content.get("value", {}).get("content")
            done_fields = ['tender_unit', 'bid_end_time', 'tender_price']
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)
            self.driver.close()
            self.driver.switch_to_window(first_handle)

    def fix_data(self, data, detail_content):
        html = etree.HTML(detail_content)
        href = html.xpath('string(//td[@id="files"]/a/@id)')
        if href:
            attachment_content_url = 'http://api.choicelink.cn/OnLineUpload/api/services/app/AbpAliOss/GetDownUrl?id={}'.format(href)
            attachment_content = self.req(attachment_content_url, rsp_type='json', headers=self.headers)
            attachment_url = attachment_content.get("result")
            data['attachment_url'] = attachment_url


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            # ""
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidCY(debug=False)
    bid.process_item(params)
