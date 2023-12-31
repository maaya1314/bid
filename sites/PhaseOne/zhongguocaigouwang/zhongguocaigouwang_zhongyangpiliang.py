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
sys.path.append('../../..')
sys.path.append('../../../..')
sys.path.append('../../../../..')

from bid_tools.loghandler import getLogger

from bid_conf.conf import parse_dict
from bid import Bid
urllib3.disable_warnings()


class BidZGCGW(Bid):

    def __init__(self, debug=True):
        Bid.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '中国采购网-中央批量集中采购'
        self.parse_dict = parse_dict.get(self.file_name)
        self.spare_2 = ""
        self.spare_1_dict = {
            "974": "公开招标",
            "975": "询价公告",
            "978": "竞争性谈判",
            "977": "单一来源",
            "979": "资格预审",
            "976": "邀请公告",
            "982": "中标公告",
            "981": "更正公告",
            "990": "其他公告",
            "984": "竞价招标",
            "985": "竞价结果",
        }

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url_dict = {
            "中央国家机关批量集中采购公告—招标": "http://www.ccgp.gov.cn/zydwplcg/zy/zyzb/",
            "中央国家机关批量集中采购公告—中标": "http://www.ccgp.gov.cn/zydwplcg/zy/zyzhb/",
            "中央直属机关批量集中采购公告—招标": "http://www.ccgp.gov.cn/zydwplcg/zz/zzzb/",
            "中央直属机关批量集中采购公告—中标": "http://www.ccgp.gov.cn/zydwplcg/zz/zzzhb/",
        }
        for spare_2, url in url_dict.items():
            self.spare_2 = spare_2
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
            content = self.req(url, req_type="get", rsp_type="content",  headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error(f"{url} no content")
                return
            # parsing home page
            self.list_parse(content, url)
            html = etree.HTML(content)
            # pages = html.xpath("string(//div[@class='pagigation']/p[@class='pager']/a[last()-1])")
            pages = re.findall("Pager\(\{size:(\d+),", content)
            if not pages:
                return
            pages = int(pages[0])
            url = url + 'index_{}.htm'
            for page in range(1, pages + 1):
                if self.exit_flag:
                    return
                self.log.info("now start page :{}, {}".format(page, keyword))
                list_url = url.format(page)
                content = self.req(list_url, req_type="get", rsp_type="content", anti_word="", headers=self.headers, timeout=TIMEOUT)
                if not content:
                    self.log.error("{} no content".format(list_url))
                    continue
                self.list_parse(content, list_url)
            self.log.info("{} 数据采集完毕！".format(self.spare_2))

    def list_parse(self, content, url):
        html = etree.HTML(content)
        items = html.xpath("//ul[@class='ulst']/li")
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        for item in items:
            if self.exit_flag:
                return
            data = {}
            href = item.xpath("string(./a/@href)")
            spare_1 = self.spare_1_dict.get(item.xpath("string(./span[1])"), item.xpath("string(./span[1])"))
            publish_time = item.xpath("string(./span[2])")
            project_location = item.xpath("string(./span[3])")
            tender_unit = item.xpath("string(./span[4])")
            detail_url = urljoin(url, href)
            # detail_url = item
            # detail_url = 'https://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=https://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(item)
            list_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            }
            # guid = re.findall('guid=(.*?)(?=&|$)', detail_url)[0]
            # actual_url = 'https://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=https://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(guid)
            # detail_url = 'http://www.ccgp.gov.cn/cggg/zygg/cjgg/202112/t20211219_17410596.htm'
            # detail_url = 'http://www.ccgp.gov.cn/cggg/zygg/zbgg/201806/t20180629_10188121.htm'
            detail_content = self.req(url=detail_url, req_type="get", anti_word="你访问的页面找不回来了", headers=list_headers, verify=False)
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data['spare_1'] = spare_1
            data['publish_time'] = publish_time
            data['project_location'] = project_location
            data['tender_unit'] = tender_unit
            self.detail_parse(detail_content, detail_url, data)

    def fix_data(self, data, detail_content):
        attachment_url = data.get("attachment_url", "")
        if not attachment_url:
            attachment_url_id = re.findall("class='bizDownload' href='' id='(.*?)'", detail_content)
            for aid in attachment_url_id:
                attachment_url += "http://download.ccgp.gov.cn/oss/download?uuid={};".format(aid)
            if not attachment_url:
                href = re.findall('href="/UploadFiles(.*?)"', detail_content)
                for h in href:
                    attachment_url += "," + "http://zzcg.ccgp.gov.cn{}".format(h)
        data['attachment_url'] = attachment_url

        tender_price = data.get("tender_price")
        if tender_price:
            tender_price = tender_price.replace("标包【1】:", "").replace("&yen;", "").replace("标包【2】:", "").strip()
            data['tender_price'] = tender_price
        data['spare_2'] = self.spare_2
        content = data.get('content')
        content = re.sub("!－－.*namespace>,?", "", content)
        content = content.replace("?xml:namespace>", "")
        data['content'] = content


if __name__ == '__main__':
    
    params = {
        "proxy_flag": False,

        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
            # "校准", "检定"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidZGCGW(debug=False)
    bid.process_item(params)
