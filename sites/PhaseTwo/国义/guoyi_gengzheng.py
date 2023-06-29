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


class BidZGSY(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '国义-更正公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url_base = 'https://www.gmgit.com/Handlers/Default/Notice_Clarify_List.ashx?categoryA=%E5%9B%BD%E9%99%85%E5%9B%BD%E5%86%85&categoryB=%E7%AE%A1%E8%BE%96%E9%83%A8%E9%97%A8&categoryC=%E8%A1%8C%E4%B8%9A%E5%88%86%E7%B1%BB&wd={}&thisPage={}&rowsEachPage=15&_=1652849742730'
        self.host = urlparse(url_base).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '111',
            'Content-Type': 'application/json;charsetset=UTF-8',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        uni_keyword = str(self.keyword.encode('unicode_escape')).replace("b'", "").replace("\'", "").replace("\\\\", "%25")
        page = 1
        payload = {
            'categoryA': '国际国内',
            'categoryB': '管辖部门',
            'categoryC': '行业分类',
            'wd': uni_keyword,
            'thisPage': page,
            'rowsEachPage': '15',
        }
        url = url_base.format(uni_keyword, page)
        content = self.req(url, req_type="get", json=payload, rsp_type='json', headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        pages = content.get("TotalPages")
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
                'categoryA': '国际国内',
                'categoryB': '管辖部门',
                'categoryC': '行业分类',
                'wd': self.keyword,
                'thisPage': page,
                'rowsEachPage': '15',
            }
            url = url_base.format(uni_keyword, page)
            content = self.req(url, req_type="get", rsp_type='json', json=payload, headers=self.headers, timeout=TIMEOUT)
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
            item_id = item.get("ID")
            SNCode = item.get("SNCode").strip()
            # href_str = item.xpath("string(./td[2]/a/@href)")
            # href = re.findall("\('(.*?)',", href_str)[0]
            # href_2 = re.findall(",'(.*?)'", href_str)[0]
            # detail_url = urljoin(url, '/staticPage/' + href)
            # item_id, SNCode = 0, 'NtcID131411'
            detail_url = 'https://www.gmgit.com/Handlers/Bid/Notice_Clarify_Detail.ashx?ID={}&tempid={}'.format(item_id, SNCode)
            ori_detail_url = 'https://www.gmgit.com/Bid/ClarifyDetail?ID={}&tempid={}'.format(item_id, SNCode)
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
                detail_json = self.req(url=detail_url, req_type='get', rsp_type='json', headers=headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_json:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            detail_item = detail_json.get("data", {})
            if not detail_item:
                return
            detail_content = detail_item.get("HTMContent")
            if not detail_content:
                detail_content = detail_item.get("TxtContent")
            # data['project_leader'] = detail_json.get("PrjManager")
            data['attachment_url'] = detail_item.get("ET_AffixLink")
            data['project_title'] = detail_item.get("Title")
            data['publish_time'] = detail_item.get("ShowDate")
            # data['project_number'] = detail_item.get("Code")
            # data['tender_unit'] = detail_item.get("projecttendername")
            # data['agency'] = detail_item.get("tenderagencyname")
            # data['bid_winner'] = detail_item.get("tendername")
            # data['phone'] = detail_item.get("resultcontactphone")
            # data['bid_finish_time'] = detail_item.get("opentenderdate")
            # done_fields = ['project_leader', 'project_number']
            self.detail_parse(detail_content, ori_detail_url, data)

    


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
    bid = BidZGSY(debug=False)
    bid.process_item(params)
