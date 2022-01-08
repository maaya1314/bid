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
        self.file_name = '国e招标采购平台-业务公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://www.ebidding.com/portal/announcement/allTitle?type=&df=&department=&industry=&bidType=&guanjianzi={}&openMode=&showDateSort=1&platformType=&on=false&page={}'
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
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
        page = 1
        homepage_url = url.format(keyword, page)
        content = self.req(homepage_url, req_type="get", rsp_type="json", headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        pages = content.get("result", {}).get("totalPages")
        if not pages:
            return
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            next_url = url.format(keyword, page)
            content = self.req(next_url, rsp_type="json", headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        url_list = content.get("result", {}).get("content", [])
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        for item in url_list:
            if self.exit_flag:
                return
            article_id = item.get("etId")
            htmlContentId = item.get("htmlContentId")
            html_type = item.get("type")
            tenderType = item.get("tenderType")
            # detail_url = urljoin(url, item)
            sn_id = item.get("snID")
            if not article_id:
                detail_url = f'https://www.ebidding.com/portal/announcement/oa/htmlContent?type={html_type}&snId={sn_id}'
                # detail_url = "https://www.ebidding.com/portal/announcement/oa/detail?&type=%E6%8B%9B%E6%A0%87%E5%85%AC%E5%91%8A&snId=35076"
                try:
                    detail_content = self.req(url=detail_url, encoding=False, headers=self.headers)
                    # detail_content = detail_content.encode('utf-8').decode('gbk')
                except Exception as e:
                    self.log.exception(e)
                    continue
                if not detail_content:
                    self.log.error("{} no detail_content".format(detail_url))
                    detail_url = f'https://www.ebidding.com/portal/announcement/oa/detail?&type={html_type}&snId={sn_id}'
                    try:
                        detail_content = self.req(url=detail_url, rsp_type='json', headers=self.headers, verify=False)
                    except Exception as e:
                        self.log.exception(e)
                        continue
                    if not detail_content:
                        self.log.error("{} no detail_content".format(detail_url))
                        continue
                    actual_url = f'https://www.ebidding.com/portal/html/index.html#page=main:notice_details?&tenderType={tenderType}&snID={sn_id}&type={html_type}'

                    try:
                        data = {}
                        if not detail_content.get("result"):
                            continue
                        data['project_title'] = detail_content.get('result').get("title")
                        data['publish_time'] = detail_content.get('result').get("showDate")
                        data['tender_unit'] = detail_content.get('result').get("tendereeName")
                        data['project_number'] = detail_content.get('result').get("code")
                        data['spare_1'] = detail_content.get('result').get("type")
                        detail_str = detail_content.get('result').get("txtContent")
                        self.detail_parse(detail_str, actual_url, data)
                    except:
                        self.log.debug("new case:{}".format(actual_url))
                    continue
                self.detail_parse(detail_content, detail_url)
            else:
                detail_url = f'https://www.ebidding.com/portal/announcement/ebd/{html_type}/{article_id}/{htmlContentId}'
                try:
                    detail_content = self.req(url=detail_url, rsp_type='json', headers=self.headers, verify=False)
                except Exception as e:
                    self.log.exception(e)
                    continue
                if not detail_content:
                    self.log.error("{} no detail_content".format(detail_url))
                    continue
                actual_url = f'https://www.ebidding.com/portal/html/index.html#page=main:notice_details?&tenderType={tenderType}&etId={article_id}&type={html_type}&htmlContentId={htmlContentId}'
                data = {}
                data['project_title'] = detail_content.get('result').get("title")
                data['publish_time'] = detail_content.get('result').get("showDate")
                data['tender_unit'] = detail_content.get('result').get("tendereeName")
                data['project_number'] = detail_content.get('result').get("code")
                data['spare_1'] = detail_content.get('result').get("type")
                detail_str = detail_content.get('result').get("htmlContent")
                self.detail_parse(detail_str, actual_url, data)

    def fix_data(self, data, detail_content):
        html = etree.HTML(detail_content)
        publish_time = data.get("publish_time")
        if not publish_time:
            p_list = html.xpath("//p[@class='p']")
            p_list.reverse()
            for p in p_list:
                try:
                    publish_time = self.format_time(p.xpath("string(.)"))
                    if publish_time:
                        break
                except:
                    publish_time = ""
            data['publish_time'] = publish_time
        attachment_url = data.get("attachment_url")
        if attachment_url:
            if 'http' not in attachment_url:
                article_url = data.get("article_url")
                attachment_url = urljoin(article_url, attachment_url)
                data['attachment_url'] = attachment_url


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidCY()
    bid.process_item(params)
