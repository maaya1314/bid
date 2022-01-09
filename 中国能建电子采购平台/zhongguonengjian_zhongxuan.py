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
sys.path.append('../..')
sys.path.append('../../..')
from bid_tools.loghandler import getLogger
from bid_conf.conf import parse_dict
from bid import Bid
urllib3.disable_warnings()


class BidCY(Bid):

    def __init__(self, debug=True):
        Bid.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '中国能建电子采购平台-中选公示'
        self.parse_dict = parse_dict.get(self.file_name)


    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url_dict = {
            "货物采购": "https://ec.ceec.net.cn/HomeInfo/ProjectList.aspx?InfoLevel=MgA=&bigType=WgBYAEcAUwA=&smallType=aAB3AA==&PageD={}",
            "工程分包": "https://ec.ceec.net.cn/HomeInfo/ProjectList.aspx?InfoLevel=MgA=&bigType=WgBYAEcAUwA=&smallType=ZwBjAA==&PageD={}",
            "服务采购": "https://ec.ceec.net.cn/HomeInfo/ProjectList.aspx?InfoLevel=MgA=&bigType=WgBYAEcAUwA=&smallType=ZgB3AA==&PageD={}",
        }
        for spare_1, url in url_dict.items():
            self.spare_1 = spare_1
            self.host = urlparse(url).netloc
            self.headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Proxy-Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            }
            page = 1
            homepage_url = url.format(page)
            content = self.req(homepage_url, req_type="get", headers=self.headers, encoding=False, timeout=TIMEOUT)
            if not content:
                self.log.error(f"{page} no content")
                return
            # html = etree.HTML(content)
            # pages = html.xpath("string(//option[last()])")
            pages_str = re.findall("共(\d+)页", content)
            if not pages_str:
                return
            pages = pages_str[0]
            self.log.info("all pages :{}, {}".format(pages, keyword))
            self.list_parse(content, url)
            pages = int(pages)
            if pages < 2:
                return
            for page in range(2, pages + 1):
                if self.exit_flag:
                    return
                next_url = url.format("{}".format(page))
                self.log.info("now start page :{}, {}".format(page, keyword))
                content = self.req(next_url, headers=self.headers, timeout=TIMEOUT)
                if not content:
                    self.log.error("{} no content".format(page))
                    continue
                self.list_parse(content, next_url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        # url_list = content.get("list")
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        html = etree.HTML(content)
        url_list = html.xpath("//div[@class='list01']/span[2]/a/@href")
        for item in url_list:
            if self.exit_flag:
                return
            detail_url = urljoin(url, item)
            # detail_url = 'https://ec.ceec.net.cn/HomeInfo/winDidDetails.aspx?threadID=d37b8e64-23c6-4006-880b-06f8938f3804'
            try:
                detail_content = self.req(url=detail_url, headers=self.headers, encoding=False, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            self.detail_parse(detail_content, detail_url)

    def fix_data(self, data, detail_content):
        data['spare_1'] = self.spare_1


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidCY(debug=False)
    bid.process_item(params)
