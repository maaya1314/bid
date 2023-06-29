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
sys.path.append('..')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_3 import Bid3
from bid_conf.conf_3 import parse_dict
urllib3.disable_warnings()


class BidXDJT(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '西电集团电子采购平台-招标公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        home_url = 'http://eps.xd.com.cn:8881/'
        self.headers = {
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
        }
        response, self.session = self.req(home_url, rsp_type='res_and_ses', headers=self.headers)
        cookies = response.cookies
        self.cookies = ''
        for k, v in cookies.items():
            self.cookies += "{}={};".format(k, v)
        self.headers['cookie'] = self.cookies
        home_content = response.text
        home_html = etree.HTML(home_content)
        onclick = home_html.xpath("string(//li[2]/a/@onclick)")
        href = re.findall("'(.*?)'", onclick)[0]
        caigou_url = urljoin(home_url, href)
        self.headers['Referer'] = caigou_url
        caigou_content = self.req(caigou_url, req_type="get", headers=self.headers, timeout=TIMEOUT)
        caigou_html = etree.HTML(caigou_content)
        zhaobiao_href = caigou_html.xpath("string(//ul[@class='list-unstyled menu']/li[2]/a/@href)")
        url = urljoin(caigou_url, zhaobiao_href)
        page = 1
        content = self.req(url, req_type="get", headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        pages_href = re.findall('var url = "(.*?newsGroupId.*?);', content)[0].replace('"+', "").replace('" + page + "', "{}")
        pages = re.findall("totalPages: (\d+),", content)[0]
        pages_url = urljoin(url, pages_href).replace(pages, "{}")
        self.log.info("all pages :{}, {}".format(pages, keyword))
        if not pages:
            return
        self.list_parse(content, url)
        pages = int(pages.strip())
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            self.log.info("now start page :{}, {}".format(page, keyword))
            url = pages_url.format(page)
            content = self.req(url, req_type="get", headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        # items = content.get("list")
        html = etree.HTML(content)
        items = html.xpath("//div[@class='col-xs-9 news-list']/ul[@class='list-unstyled']/li")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            # item_id = item.get("id")
            href = item.xpath("string(./a/@href)")
            # detail_url = re.findall("urlOpen\('(.*?)'\)", href_str)[0]
            # href_str = item.xpath("string(./@onclick)")
            # href = re.findall("\('(.*?)',", href_str)[0]
            # href_2 = re.findall(",'(.*?)'", href_str)[0]
            detail_url = urljoin(url, href)
            # detail_url = 'https://www.sdicc.com.cn/cgxx/bgggDetail?shiXiangGuid={}&ggGuid={}'.format(href_2, href)

            try:
                detail_content = self.req(url=detail_url, req_type='get', headers=self.headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            data['project_title'] = item.xpath("string(./a)").replace("\n", "").replace("\r", "").replace("NEW", "")
            data['publish_time'] = item.xpath("string(./span[@class='date'])").replace("\n", "").replace("\r", "").replace("\t", "")
            # data['tender_unit'] = item.xpath("string(./a[@class='Blue'])")
            # data['bid_end_time'] = item.xpath("string(./a/ul[@class='newsinfo']/li[3]/span)")
            # detail_content = detail_content.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;nbsp;", "")
            self.detail_parse(detail_content, detail_url, data)

    def fix_data(self, data, detail_content):
        attr_url = re.findall('var url = "(.*?ExportSupQuoteBidExcelTemplateHomePage.*?)\';', detail_content)[0]
        attachment_url = attr_url.replace('" + \'', "")
        data['attachment_url'] = attachment_url


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidXDJT(debug=False)
    bid.process_item(params)
