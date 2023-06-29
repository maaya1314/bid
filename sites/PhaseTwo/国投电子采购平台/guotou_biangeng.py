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


class BidGT(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '国投电子采购平台-变更公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://www.sdicc.com.cn/cgxx/ggList?ggXingZhi=2'
        self.host = urlparse(url).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1
        payload = {
            'caiGouDanWei': '',
            'currentPage': page,
            'gcName': '',
            'zbFangShi': '',
            'xmLeiXing': '',
            'startTime': '',
            'endTime': '',
            'ggName': keyword,
        }
        content = self.req(url, req_type="post", data=payload, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        html = etree.HTML(content)

        pages = html.xpath("string(//button[last()-2])")
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        pages = int(pages)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            self.log.info("now start page :{}, {}".format(page, keyword))
            payload = {
                'caiGouDanWei': '',
                'currentPage': page,
                'gcName': '',
                'zbFangShi': '',
                'xmLeiXing': '',
                'startTime': '',
                'endTime': '',
                'ggName': keyword,
            }
            content = self.req(url, req_type="post", data=payload, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        # items = content.get("data")
        html = etree.HTML(content)
        items = html.xpath("//div[@id='table']/div[@class='tbody']/table//tr")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            # item_id = item.get("id")
            href_str = item.xpath("string(./@onclick)")
            href = re.findall("\('(.*?)',", href_str)[0]
            href_2 = re.findall(",'(.*?)'", href_str)[0]
            detail_url = 'https://www.sdicc.com.cn/cgxx/bgggDetail?shiXiangGuid={}&ggGuid={}'.format(href_2, href)
            # detail_url = urljoin(url, '/staticPage/' + href)
            # detail_url = 'https://www.cdt-ec.com/notice/moreController/moreall?id={}'.format(item_id)
            # detail_url = 'https://www.sdicc.com.cn/cgxx/bgggDetail?shiXiangGuid=316fd2f4-ada8-45a3-a6d5-1266569b73fe&ggGuid=72c7feb5-8e79-44c2-a0cd-bd7aba3ac874'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Proxy-Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            }
            try:
                detail_content = self.req(url=detail_url, headers=headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            # html = etree.HTML(detail_content)
            # content = html.xpath("string(//div[@id='main'])")
            # data['project_title'] = item.get("message_title")
            data['publish_time'] = item.xpath("string(./td[4])")
            # data['project_number'] = item.get("message_no")
            # data['tender_unit'] = item.get("bid_tenderer")
            # data['bid_end_time'] = item.get("deadline")
            self.detail_parse(detail_content, detail_url, data)

    


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        # "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            # ""
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidGT(debug=False)
    bid.process_item(params)
