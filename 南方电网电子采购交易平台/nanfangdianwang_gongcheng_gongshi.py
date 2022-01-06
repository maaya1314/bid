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
        self.file_name = '南方电网电子采购交易平台-工程-公示公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://ecsg.com.cn/api/tender/tendermanage/gatewayNoticeQueryController/queryGatewayNoticeListPagination'
        self.host = urlparse(url).netloc
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'Accept': '*/*',
            'Content-Type': 'application/json;charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Origin': 'https://ecsg.com.cn',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        payload = '{{"projectLevel1ClassifyId":"1","noticeType":"3","noticeTitle":"{}","publishTime":"","organizationInfoName":"","pageNo":{},"pageSize":20}}'
        page = 1
        list_payload = payload.format(keyword, page).encode()
        content = self.req(url, req_type="post", rsp_type="json", data=list_payload, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        total = content.get("count")
        if not total:
            self.log.debug("total counts:{}, {}".format(total, keyword))
            return
        pages = total // 20 + 1
        self.log.info("all pages :{}, {}".format(page, keyword))
        self.list_parse(content, url)
        pages = int(pages)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            list_payload = payload.format(keyword, page).encode()
            content = self.req(url, req_type="post", rsp_type="json", data=list_payload, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        url_list = content.get("list")
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        for item in url_list:
            if self.exit_flag:
                return
            object_id = item.get("objectId")
            objectType = item.get("objectType")
            # detail_url = urljoin(url, item)
            detail_payload = '{{objectId: "{}", objectType: "{}"}}'.format(object_id, objectType)
            detail_url = 'https://ecsg.com.cn/api/tender/tendermanage/gatewayNoticeQueryController/getNotice'
            try:
                detail_content = self.req(url=detail_url, req_type="post", rsp_type='json', data=detail_payload,
                                          headers=self.headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_payload))
                continue

            data = {}
            publish_time = detail_content.get("publishTime")
            data['project_title'] = detail_content.get("noticeTitle")
            data['agency'] = item.get("organizationInfoName")
            data['publish_time'] = time.strftime("%Y-%m-%d", time.localtime(publish_time / 1000))
            detail_str = detail_content.get("noticeContent")
            actual_url = 'https://ecsg.com.cn/cms/NoticeDetail.html?objectId={}&objectType={}&typeid=4'.format(
                object_id, objectType)
            self.detail_parse(detail_str, actual_url, data)

    def fix_data(self, data, detail_content):
        agency = data.get("agency")
        if agency and "代理" not in detail_content:
            data['agency'] = ""
        project_title = data.get("project_title")
        project_number = data.get("project_number")
        if project_title and (not project_number or len(project_number) < 9):
            try:
                project_number = re.findall("[A-Za-z][a-zA-Z0-9-]+", project_title)[0]
            except:
                project_number = ""
            data['project_number'] = project_number


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidCY(debug=False)
    bid.process_item(params)
