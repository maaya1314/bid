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
from tenacity import retry, stop_after_attempt, wait_fixed
sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')

from bid_tools.loghandler import getLogger

from bid_conf.conf import parse_dict
from bid import Bid
urllib3.disable_warnings()


class BidZG(Bid):

    def __init__(self, debug=True):
        Bid.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '中国采购与招标网-招标公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        # url = 'https://www.e-bidding.org/cms/category/bulletinList.html?dates=300&categoryId=88&tabName=%E6%8B%9B%E6%A0%87%E6%8A%95%E6%A0%87&page={}&word={}'
        url = 'http://www.e-bidding.org/cms/category/bulletinList.html?searchDate=1996-12-14&dates=300&categoryId=88&exactSearch=&industryName=&status=&tabName=%E6%8B%9B%E6%A0%87%E5%85%AC%E5%91%8A&page={}&word={}'
        self.host = urlparse(url).netloc
        self.headers = {
            'Host': self.host,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        }
        page = 1
        home_page_url = url.format(page, keyword)
        content = self.req(home_page_url, req_type="get", rsp_type="content",  headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{home_page_url} no content")
            return
        # parsing home page
        self.list_parse(content, home_page_url)
        html = etree.HTML(content)
        pages = html.xpath("string(//div[@class='pages']/label[1])")
        if not pages:
            return
        pages = int(pages)
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            list_url = url.format(page, keyword)
            content = self.req(list_url, req_type="get", rsp_type="content", anti_word="", headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(list_url))
                continue
            self.list_parse(content, list_url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        html = etree.HTML(content)
        url_list = html.xpath("//ul[@class='newslist']/li/a/@href")
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        for item in url_list:
            if self.exit_flag:
                return
            # detail_url = urljoin(url, item)
            detail_url = item
            # detail_url = 'https://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=https://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(item)
            list_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'upgrade-insecure-requests': '1',
                'cookie': 'XUNJIAZBSESSION=98dc91b1-5523-4ff4-a0a2-5caaeb879111; SF_cookie_64=27399467; style=blue_theme; SF_cookie_14=64309118; Hm_lvt_ecae00c58d422d4792fafb5d505b43b1=1639398337; Hm_lpvt_ecae00c58d422d4792fafb5d505b43b1=1639398346',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            }
            # guid = re.findall('guid=(.*?)(?=&|$)', detail_url)[0]
            # actual_url = 'https://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=https://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(guid)
            detail_content = self.req(url=detail_url, req_type="get", anti_word="你访问的页面找不回来了", headers=list_headers, verify=False)
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            self.detail_parse(detail_content, detail_url)

    def fix_data(self, data, detail_content):
        content = data.get("content")
        if content:
            content = re.sub("(\$[\s\S]*?)我要报名", "我要报名", content)
            data['content'] = content

    @retry(reraise=True, stop=stop_after_attempt(10), wait=wait_fixed(2))
    def req(self, url, req_type="get", rsp_type="content", anti_word="", **kwargs):
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60
        session = requests.session()
        if kwargs.get("headers"):
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        else:
            kwargs["headers"] = {}
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        if self.proxy_flag:
            session.proxies = self.get_proxy()  # 更换代理
        if req_type == "get":
            response = session.get(url, **kwargs)
            response.encoding = 'utf8'
        elif req_type == "post":
            response = session.post(url, **kwargs)
        else:
            self.log.error(f"error req_type: {req_type}")
            raise Exception
        if not response or response.status_code not in (200, 302):
            self.log.error(f"error response, {response.status_code}")
            raise Exception
        if not rsp_type or rsp_type == "content":
            content = response.text
        elif rsp_type == "json":
            content = response.json()
        else:
            self.log.error(f"error content:{response.content}")
            raise Exception
        if anti_word and anti_word in content:
            self.log.error(f"anti_word: {anti_word}")
            raise Exception
        # 根据实际情况设置休眠时间
        # time.sleep(random.randint(2, 5))
        return content


if __name__ == '__main__':
    
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验"
            # "校准", "检定"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidZG(debug=False)
    bid.process_item(params)
