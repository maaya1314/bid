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


class BidYG(Bid):

    def __init__(self, debug=True):
        Bid.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '广东能源商务网-物资招标'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        # url = 'http://www.e-bidding.org/cms/category/bulletinList.html?dates=300&categoryId=88&tabName=%E6%8B%9B%E6%A0%87%E6%8A%95%E6%A0%87&page={}&word={}'
        url = 'http://gegb2b.gdydb2b.com/Tender/ShowTenderList.aspx?type=Tender&mode=4&pre=0'
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
        first_content = self.req(url, req_type="get", rsp_type="content", headers=self.headers, timeout=TIMEOUT)
        first_html = etree.HTML(first_content)

        # ctl00_ContentPlaceHolder1_RadScriptManager1_TSM = first_html.xpath("string(//input[@name='ctl00_ContentPlaceHolder1_RadScriptManager1_TSM']/@value)")
        # ctl00_ContentPlaceHolder1_RadScriptManager1_TSM = re.findall('_TSM_CombinedScripts_(.*?)"', first_content)
        # __EVENTTARGET = first_html.xpath("string(//input[@name='__EVENTTARGET']/@value)")
        __EVENTARGUMENT = first_html.xpath("string(//input[@name='__EVENTARGUMENT']/@value)")
        __VIEWSTATE = first_html.xpath("string(//input[@name='__VIEWSTATE']/@value)")
        __VIEWSTATEGENERATOR = first_html.xpath("string(//input[@name='__VIEWSTATEGENERATOR']/@value)")
        __VIEWSTATEENCRYPTED = first_html.xpath("string(//input[@name='__VIEWSTATEENCRYPTED']/@value)")
        __EVENTVALIDATION = first_html.xpath("string(//input[@name='__EVENTVALIDATION']/@value)")
        post_data = {
            # "ctl00_ContentPlaceHolder1_RadScriptManager1_TSM": ctl00_ContentPlaceHolder1_RadScriptManager1_TSM,
            # "ctl00_ContentPlaceHolder1_RadScriptManager1_TSM":"",
            "__EVENTTARGET": "ctl00$ContentPlaceHolder1$pager",
            "__EVENTARGUMENT": __EVENTARGUMENT,
            "__VIEWSTATE": __VIEWSTATE,
            "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
            "__VIEWSTATEENCRYPTED": __VIEWSTATEENCRYPTED,
            "__EVENTVALIDATION": __EVENTVALIDATION,
            'KeyWord': '输入招标名称进行搜索',
            # 'ctl00$ContentPlaceHolder1$txtSearchCode': '',
            # 'ctl00$ContentPlaceHolder1$txtSearchSummary': keyword,
            # 'ctl00$ContentPlaceHolder1$ddlCompany': '',
            # 'ctl00$ContentPlaceHolder1$ddlSearchStatus': '',
            # 'ctl00$ContentPlaceHolder1$ddlSearchTE_POType': '',
            # 'ctl00$ContentPlaceHolder1$txtTimeS': '',
            # 'ctl00$ContentPlaceHolder1$txtTimeE': '',
            # 'ctl00$ContentPlaceHolder1$ddlSearchTE_Pub': '',
            # 'ctl00$ContentPlaceHolder1$pager_input': '1',
            # 'ctl00$ContentPlaceHolder1$btnSearch': '提交查询',
        }
        home_page_url = url
        content = self.req(home_page_url, req_type="post", rsp_type="content",  data=post_data, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{home_page_url} no content")
            return
        # parsing home page
        html = etree.HTML(content)
        pages_str = html.xpath("string(//a[@class='linkbai'][last()]/@title)")
        try:
            pages = int(re.findall("\d+", pages_str)[0])
        except:
            pages = 0
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, home_page_url)
        if not pages:
            return
        if pages < 2:
            return
        pages = int(pages)
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            # ctl00_ContentPlaceHolder1_RadScriptManager1_TSM = re.findall('_TSM_CombinedScripts_(.*?)"', first_content)
            # __EVENTARGUMENT = html.xpath("string(//input[@name='__EVENTARGUMENT']/@value)")
            __VIEWSTATE = html.xpath("string(//input[@name='__VIEWSTATE']/@value)")
            __VIEWSTATEGENERATOR = html.xpath("string(//input[@name='__VIEWSTATEGENERATOR']/@value)")
            __VIEWSTATEENCRYPTED = html.xpath("string(//input[@name='__VIEWSTATEENCRYPTED']/@value)")
            __EVENTVALIDATION = html.xpath("string(//input[@name='__EVENTVALIDATION']/@value)")
            post_data = {
                # "ctl00_ContentPlaceHolder1_RadScriptManager1_TSM": ctl00_ContentPlaceHolder1_RadScriptManager1_TSM,
                "__EVENTTARGET": "ctl00$ContentPlaceHolder1$pager",
                "__EVENTARGUMENT": page,
                "__VIEWSTATE": __VIEWSTATE,
                "__VIEWSTATEGENERATOR": __VIEWSTATEGENERATOR,
                "__VIEWSTATEENCRYPTED": __VIEWSTATEENCRYPTED,
                "__EVENTVALIDATION": __EVENTVALIDATION,
                'KeyWord': '输入招标名称进行搜索',
                # 'ctl00$ContentPlaceHolder1$txtSearchCode': '',
                # 'ctl00$ContentPlaceHolder1$txtSearchSummary': keyword,
                # 'ctl00$ContentPlaceHolder1$ddlCompany': '',
                # 'ctl00$ContentPlaceHolder1$ddlSearchStatus': '',
                # 'ctl00$ContentPlaceHolder1$ddlSearchTE_POType': '',
                # 'ctl00$ContentPlaceHolder1$txtTimeS': '',
                # 'ctl00$ContentPlaceHolder1$txtTimeE': '',
                # 'ctl00$ContentPlaceHolder1$ddlSearchTE_Pub': '',
                # 'ctl00$ContentPlaceHolder1$pager_input': '1',
                # 'ctl00$ContentPlaceHolder1$btnSearch': '提交查询',
            }
            content = self.req(url, req_type="post", rsp_type="content", anti_word="", data=post_data, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(url))
                continue
            self.list_parse(content, url)
            html = etree.HTML(content)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        html = etree.HTML(content)
        url_list = re.findall("javascript:btnEdit_Click\('.*?',0,'(.*?)'\)", content)
        # url_list = re.findall('guid=(.*?)(?=&|$)', content)
        for item in url_list:
            if self.exit_flag:
                return
            # detail_url = urljoin(url, item)
            # code = item.xpath("string(.)")
            detail_url = "http://gegb2b.gdydb2b.com/Tender/TenderItem.aspx?type=Inquiry&pre=0&TenderCode={}".format(item)
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
            # actual_url = 'http://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=http://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(guid)
            detail_content = self.req(url=detail_url, req_type="get", anti_word="你访问的页面找不回来了", headers=list_headers, verify=False)
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            self.detail_parse(detail_content, detail_url)

    
        # content = data.get("content")
        # if content:
        #     content = re.sub("(\$[\s\S]*?)我要报名", "我要报名", content)
        #     data['content'] = content


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
    bid = BidYG(debug=False)
    bid.process_item(params)
