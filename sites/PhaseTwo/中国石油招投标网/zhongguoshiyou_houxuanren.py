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
        self.file_name = '中国石油招投标网-公开招标中标候选人公示'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://www.cnpcbidding.com/cms/pmsbidInfo/listPageOut'
        self.host = urlparse(url).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Length': '111',
            'Content-Type': 'application/json;charsetset=UTF-8',
            'Host': 'www.cnpcbidding.com',
            'Origin': 'https://www.cnpcbidding.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.cnpcbidding.com/html/1/index.html',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1
        payload = {
            "url": "./list.html",
            "pid": "180",
            "pageSize": 15,
            "categoryId": "181",
            "title": keyword,
            "projectType": "",
            "pageNo": page
        }
        content = self.req(url, req_type="post", rsp_type='json', json=payload, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        pages = content.get("totalPage")
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
                "url": "./list.html",
                "pid": "180",
                "pageSize": 15,
                "categoryId": "181",
                "title": keyword,
                "projectType": "",
                "pageNo": page
            }
            content = self.req(url, req_type="post", rsp_type='json', json=payload, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        items = content.get("list")
        # html = etree.HTML(content)
        # items = html.xpath("//form/table[1]//tr")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            item_id = item.get("id")
            # href_str = item.xpath("string(./td[2]/a/@href)")
            # href = re.findall("\('(.*?)',", href_str)[0]
            # href_2 = re.findall(",'(.*?)'", href_str)[0]
            # detail_url = urljoin(url, '/staticPage/' + href)
            detail_url = 'https://www.cnpcbidding.com/cms/pmsbidInfo/detailsOut'
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
            payload = {
                "url": "./page.html",
                "pid": "180",
                "categoryId": "181",
                "projectType": "",
                "dataId": item_id
            }
            try:
                detail_json = self.req(url=detail_url, req_type='post', json=payload, rsp_type='json', headers=headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_json:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            bid_winner = ""
            detail_items = detail_json.get("list", {})
            if not detail_items:
                return
            for detail_item in detail_items:
                tendername = "" if not detail_item.get("tendername") else detail_item.get("tendername")
                if bid_winner:
                    bid_winner += "," + tendername
                else:
                    bid_winner += tendername
                data['project_title'] = detail_item.get("projectname")
                data['publish_time'] = detail_item.get('lastmodifydate')
                data['project_number'] = detail_item.get("projectcode")
                data['tender_unit'] = detail_item.get("projecttendername")
                data['agency'] = detail_item.get("tenderagencyname")
                data['bid_winner'] = bid_winner
                data['project_leader'] = detail_item.get("assignedusername")
                data['phone'] = detail_item.get("resultcontactphone")
                data['bid_finish_time'] = detail_item.get("opentenderdate")
                data['win_bid_announcement_time'] = detail_item.get("publicitydatestart")
                detail_url = "{}#detail_id={}".format(detail_url, item_id)
            for k, v in data.items():
                if not v:
                    data[k] = ""
            detail_content = "<html><body>{}</body></html>".format(",".join(data.values()))
            attachment_url = ''
            attachment_items = [] if not detail_json.get("attachmentList", []) else detail_json.get("attachmentList", [])
            for attachment in attachment_items:
                attachment_id = attachment.get("ATTACHMENTID")
                if attachment_url:
                    attachment_url += "," + "https://www.cnpcbidding.com/pmsbid/download?id={}&skip=true".format(attachment_id)
                else:
                    attachment_url += "https://www.cnpcbidding.com/pmsbid/download?id={}&skip=true".format(attachment_id)
            data['attachment_url'] = attachment_url
            done_fields = ['project_number', 'tender_unit', 'bid_winner', 'agency', 'phone', 'project_leader', 'bid_finish_time']
            if data.get('project_title'):
                self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)
            time.sleep(60 * 5)




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
