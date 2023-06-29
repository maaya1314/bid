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


class BidZGHY(Bid3):
    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '中国海洋石油集团有限公司-非招标公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url_base = 'https://buy.cnooc.com.cn/cbjywebframe/services/PortalsWebservice/getMoreInfoCateList?response=application/json&callback=&pageIndex={}&pageSize=12&siteguid=&catenum=001004&title={}'
        self.host = urlparse(url_base).netloc
        self.headers = {
            'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Host': 'buy.cnooc.com.cn',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1

        url = url_base.format(page, self.keyword)
        content = self.req(url, req_type="get", headers=self.headers, timeout=TIMEOUT)
        json_str = content[1:-2]
        json_content = json.loads(json_str)
        if not json_content:
            self.log.error(f"{page} no content")
            return
        self.list_parse(json_content, url)
        while True:
            page += 1
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            self.log.info("now start page :{}, {}".format(page, keyword))
            url = url_base.format(page, self.keyword)
            content = self.req(url, req_type="get", headers=self.headers, timeout=TIMEOUT)
            json_str = content[1:-2]
            json_content = json.loads(json_str)
            if not json_content:
                self.log.error(f"{page} no content")
                return
            if json_content.get("Table")[0].get("title2"):
                self.log.error(json_content.get("Table")[0].get("title2"))
                break
            self.list_parse(json_content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        items = content.get("Table")
        # html = etree.HTML(content)
        # items = html.xpath("//form/table[1]//tr")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            # item_id = item.get("SNID")
            # href_str = item.xpath("string(./td[2]/a/@href)")
            href = item.get("Href")
            # href_2 = re.findall(",'(.*?)'", href_str)[0]
            detail_url = urljoin(url, href)
            # detail_url = 'https://buy.cnooc.com.cn/cbjyweb/001/001004/20220323/4660a38a-fcdd-49b4-8846-449964075322.html'
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
                content = self.req(url=detail_url, req_type='get', headers=headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            data['publish_time'] = item.get("infodate")
            data['project_title'] = item.get("title")
            self.detail_parse(content, detail_url, data)

    


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
    bid = BidZGHY(debug=False)
    bid.process_item(params)
