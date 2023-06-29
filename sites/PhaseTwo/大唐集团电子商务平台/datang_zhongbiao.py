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
from requests.utils import dict_from_cookiejar

sys.path.append('..')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
from bid_conf.conf_2 import parse_dict
from bid_2 import Bid2
urllib3.disable_warnings()
from selenium import webdriver


class Bid2DT(Bid2):

    def __init__(self, debug=True):
        Bid2.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '大唐集团电子商务平台-中标结果'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        home_url = 'https://www.cdt-ec.com/notice/moreController/toMore?globleType=3'
        home_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'www.cdt-ec.com',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        }
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 隐藏浏览器
        options.add_argument("service_args=['–ignore-ssl-errors=true', '–ssl-protocol=TLSv1']")  # Python2/3
        self.driver = webdriver.Firefox(options=options)
        # if isinstance(proxy, Proxy):
        #     if proxy.scheme == 'http':
        #         options.set_preference('network.proxy.type', 1)  # Proxy type: manual
        #         options.set_preference('network.proxy.http', proxy.host)
        #         options.set_preference('network.proxy.http_port', proxy.port)
        #         self.logger.info(f"Firefox will launch with proxy: {proxy.as_uri()}")
        #     else:
        #         self.logger.warning(f"Not use proxy({proxy.as_uri()}): proxy type `{proxy.scheme}` not yet supported")
        self.driver.implicitly_wait(10)  # 隐性等待，最长等30秒
        self.driver.get(home_url)
        # home_cookies = self.driver.get_cookies()
        # self.cookies = ""
        # for c in home_cookies:
        #     self.cookies += "{}={};".format(c.get("name"), c.get("value"))
        time.sleep(10)
        search = self.driver.find_element_by_xpath("//input[@id='title']")
        search.send_keys(self.keyword)
        time.sleep(1)
        confirm = self.driver.find_element_by_xpath("//button[@class='layui-btn layui-btn-primary'][1]")
        confirm.click()
        self.list_parse()
        try:
            next_page_button = self.driver.find_element_by_xpath("//a[@class='layui-laypage-next']")
        except Exception as e:
            self.log.error(e)
            next_page_button = False
        page = 1
        while next_page_button:
            page += 1
            self.log.info("now start page :{}, {}".format(page, keyword))
            next_page_button.click()
            self.list_parse()
            try:
                next_page_button = self.driver.find_element_by_xpath("//a[@class='layui-laypage-next']")
            except Exception as e:
                self.log.error(e)
                break
        self.log.info("{} 数据采集完毕！".format(self.file_name))
        self.driver.quit()

    def list_parse(self):
        time.sleep(10)
        content = self.driver.page_source
        url = self.driver.current_url
        first_handle = self.driver.current_window_handle
        tab_items = self.driver.find_elements_by_xpath("//a[@class='layui-table-link']")
        html = etree.HTML(content)
        html_items = html.xpath("//div[@class='layui-table-body layui-table-main']/table[@class='layui-table']//tr")
        if not html_items:
            self.log.error("{} no items".format(self.keyword))
        if not tab_items:
            self.log.error("{} no items".format(self.keyword))
        for index, item in enumerate(tab_items):
            try:
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.driver.execute_script(js)
                time.sleep(1)
                item.click()
                time.sleep(10)
            except Exception as e:
                self.log.error(e)
                continue
            time.sleep(1)
            handles = self.driver.window_handles
            self.driver.switch_to_window(handles[-1])
            detail_content = self.driver.page_source
            detail_url = self.driver.current_url
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            if self.exit_flag:
                return
            data = {}
            data['project_title'] = html_items[index].xpath("string(./td[1]//a)")
            data['publish_time'] = html_items[index].xpath("string(./td[2])")
            data['project_number'] = html_items[index].xpath("string(./td[1]//div/ul[@class='newsinfo']/li[1]/span)")
            data['tender_unit'] = html_items[index].xpath("string(./td[1]/div/ul[@class='newsinfo']/li[2]/span)")
            data['bid_end_time'] = html_items[index].xpath("string(./td[1]/div/ul[@class='newsinfo']/li[3]/span)")
            self.detail_parse(detail_content, detail_url, data)
            self.driver.close()
            self.driver.switch_to_window(first_handle)

    


if __name__ == '__main__':
    params = {
        # "proxy_flag": False,
        "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            # ""
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = Bid2DT(debug=False)
    bid.process_item(params)
