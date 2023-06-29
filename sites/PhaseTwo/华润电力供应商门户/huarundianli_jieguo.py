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
from bid_conf.conf_2 import parse_dict
from bid_2 import Bid2
urllib3.disable_warnings()


class Bid2HRDL(Bid2):

    def __init__(self, debug=True):
        Bid2.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '华润电力供应商门户-采购结果公示'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://b2b.crpower.com.cn/ispweb/pcux5PonRl/getRlNoticeByList.do'
        self.host = urlparse(url).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'Host': 'b2b.crpower.com.cn',
            # 'Origin': 'https://b2b.crpower.com.cn',
            'Pragma': 'no-cache',
            'Referer': 'https://b2b.crpower.com.cn/ispweb/pcux5PonHeaders/souringIndex.do',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1
        payload = {
            'data': '{{"queryAll":"{}","start":"","end":""}}'
                .format(self.keyword),
            'take': '60',
            'skip': '0',
            'page': page,
            'pageSize': '60',
        }
        content = self.req(url, req_type="post", rsp_type='json', data=payload, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        total = content.get("totalCount")
        pages = total // 20 + 1 if not total % 20 == 0 else total // 20
        # pages = content.get("totalPage")
        # pages = int(pages)
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            self.log.info("now start page :{}, {}".format(page, keyword))
            payload = {
                'data': '{{"queryAll":"{}","start":"","end":""}}'.format(self.keyword),
                'take': '60',
                'skip': '0',
                'page': page,
                'pageSize': '60',
            }
            content = self.req(url, req_type="post", rsp_type='json', json=payload, headers=self.headers,
                               timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        items = content.get("data")
        # html = etree.HTML(content)
        # items = html.xpath("//form/table[1]//tr")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            item_id = item.get("attribute5")
            # href_str = item.xpath("string(./td[2]/a/@href)")
            # href = re.findall("\('(.*?)',", href_str)[0]
            # href_2 = re.findall(",'(.*?)'", href_str)[0]
            # detail_url = urljoin(url, '/staticPage/' + href)
            detail_url = 'https://b2b.crpower.com.cn/ispweb/pcux5PonRl/getNoticeResultDetailById.do?sid={}'.format(item_id)
            # headers = {
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            #     'Accept-Encoding': 'gzip, deflate',
            #     'Accept-Language': 'zh-CN,zh;q=0.9',
            #     'Cache-Control': 'no-cache',
            #     'Pragma': 'no-cache',
            #     'Proxy-Connection': 'keep-alive',
            #     'Upgrade-Insecure-Requests': '1',
            #     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            # }
            # payload = {
            #     "url": "./page.html",
            #     "pid": "198",
            #     "categoryId": "199",
            #     "projectType": "",
            #     "dataId": item_id
            # }
            try:
                # detail_json = self.req(url=detail_url, req_type='post', json=payload, rsp_type='json', headers=headers, verify=False)
                detail_item = self.req(url=detail_url, req_type='get', rsp_type='json', headers=self.headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_item:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            detail_content = detail_item.get("bulletincontent")
            if not detail_content:
                detail_content = "<html><body></body></html>"
            data['project_title'] = item.get("sourceTitle")
            data['publish_time'] = item.get("publishDate")
            data['project_number'] = item.get("sourceNum")
            data['tender_unit'] = item.get("orgName")
            # detail
            data['project_leader'] = detail_item.get("buyerName")
            data['phone'] = detail_item.get("buyerPhone")
            # data['publish_time'] = detail_item.get("publishDate")
            # data['project_overview'] = "{};{}".format(detail_item.get('qualificationRequirements'), detail_item.get('performanceRequirements'))
            data['bid_winner'] = detail_item.get("supplierName")
            data['win_bid_announcement_time'] = detail_item.get("bidApproveDate")
            # data['bid_winner'] = detail_item.get("tendername")
            # data['project_leader'] = detail_item.get("assignedusername")
            # data['phone'] = detail_item.get("resultcontactphone")
            # data['bid_finish_time'] = detail_item.get("opentenderdate")
            # detail_url = "{}#detail_id={}".format(detail_url, item_id)
            self.detail_parse(detail_content, detail_url, data)

    


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            # "采购"
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = Bid2HRDL(debug=False)
    bid.process_item(params)
