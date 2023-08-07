#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re

# import execjs
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree
sys.path.append('../../PhaseTwo')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_7 import Bid7
from bid_conf.conf_7 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
from bid_tools import utils
import jsonpath
import math

class BidZGDZ(Bid7):
    def __init__(self, debug=True):
        Bid6.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '华电采购平台-中标候选人公示'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        url = "https://www.chdtp.com/webs/displayNewZbhxrgsZxzxAction.action?zbtype=2"
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'zZ6ZmsgRSJCBO=60R6H6cJmQTXEzerDXIUiC3QrehF4Xe9Zo6bXSiEk1oKxE897.EC1bfuOAhMExNlDX6CuE6_zZ.3opVqk6E.omfG; BIGipServerpool_web=1443080384.20480.0000; JSESSIONID=0000k7LgM5k3LoGHkn_i51_7zDD:1fak1ippc; zZ6ZmsgRSJCBP=0hM1ZWzb5saeZfZ7Ag15LfC5q1YHbcSHA5LoV_lpc_St7rVG4GXf_vnkQqnMhPvpLUPIqDxI.Vr13XFeLk34b_papRbYV9IyWyVoZbxeViLwIsRr9HRXby39M4zhbZQnRC3sB4iLDB6RuIhMuhWy7Sh_vlDoQqWrK9hhqItPMPsKDMadZl1Ac967iabxU4Dnhs52vZiPCVgo8Tw_UaY8wWhvB0h1nImZ7HHyMVSqxYnBIy1NwYVSG5pdij803rpAN8dfZCqH6R1i7LylGmsltqH7Wk1mCqGHeMnw4Im1wLdm2W8Iy2TPlDXpOmQUeKKo8gvBoim_4s6Qf2F8YHylbEjySOul94gvE6a5GzVhgpRo3czb9BcUMY8a4ZyHVH.oygZ1jthm0NrjKYPMbluxB3wUCz8SJAB9LnV_YR6A8KZL',
            'Host': 'www.chdtp.com',
            'Referer': 'https://www.chdtp.com/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            storage_state = context.storage_state()
            cookie = ''
            for cookie_info in storage_state['cookies']:
                cookie_text = cookie_info['name'] + '=' + cookie_info['value']
                cookie += cookie_text + ';'
            self.headers['Cookie'] = cookie.rstrip(';')
            context.close()
            browser.close()
        # form_data = {
        #     'type': '103',
        #     'searchWay': 'onTitle',
        #     'search': '',
        #     'ifend': 'in',
        #     'start': 0,
        #     'limit': 50
        # }
        url_base = 'https://www.chdtp.com/webs/queryWebZbgg.action?zbggType={}'
        url = url_base.format(2)
        self.log.info("开始采集第1页：{}".format(url))
        # content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, timeout=TIMEOUT,
        #                    verify=False)
        content = self.req(url=url, headers=self.headers, timeout=TIMEOUT)
        html = etree.HTML(content)
        all_re_page = html.xpath('string(//span[@class="page"])')
        all_re_page = utils.re_find_one('(?<=第).*?(?=页，)', all_re_page)
        all_re_page = utils.re_find_one('[^/]+(?!.*/)', all_re_page)
        if all_re_page:
            all_re_page = int(all_re_page)
        else:
            all_re_page = 1
        pages = all_re_page
        self.log.info("总页数：{},开始采集第1页：{}".format(all_re_page, url))
        self.list_parse(content, url)
        for num in range(2, pages + 1):
            data_base = 'jump=1&page.pageSize=20&page.currentpage={}&page.totalCount=13094'
            url = 'https://www.chdtp.com/webs/displayNewZbhxrgsZxzxAction.action'
            data = data_base.format(num)
            self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
            content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT, verify=False)
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, maincontent, url):
        urlbase = 'https://www.chdtp.com/staticPage/'
        list_html = etree.HTML(maincontent)
        items = list_html.xpath('//form[@name="resultForm"]//table//tr/td[2]/a[1]')
        for item in items:
            if self.exit_flag:
                return
            title = item.xpath("string(./@title)")
            href_text = item.xpath("string(./@href)")
            href = utils.re_find_one("'(.*?)'", href_text)
            detail_url = urljoin(urlbase, href)
            detail_content = self.req(url=detail_url, headers=self.headers)
            if not detail_content or detail_content == 404 or detail_content == 400:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            source_code = detail_content
            detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            html = etree.HTML(detail_content)
            html1 = etree.HTML(re.sub('</p>', '</p>\n', detail_content))
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            content_text1 = html1.xpath('string(//title/following-sibling::div)')
            data = {}
            publish_time = html.xpath('string(//div[@class="headline"]//dd)').replace('发布时间：', '')
            data['article_url'] = detail_url
            data['project_title'] = title
            data['publish_time'] = publish_time
            data['content'] = content_text1.strip()
            data['source_code'] = str(source_code).strip()
            # data[TABField.announcement] = item.xpath("string(./@title)")
            done_fields = []
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)


if __name__ == '__main__':
    params = {
        "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    keyword = ''
    bid = BidZGDZ(debug=True)
    bid.process_item(params)

    # BidZGDZ.run(keyword)
