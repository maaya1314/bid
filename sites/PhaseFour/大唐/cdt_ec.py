#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re

# import execjs
import fitz
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree

from libs.base import TaskBase
from sites.PhaseFour.大唐.libs import util

sys.path.append('../../PhaseTwo')
sys.path.append('../../..')
sys.path.append('../../../..')
# from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
# from bid_6 import Bid6
# from bid_conf.conf_6 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright

import jsonpath
import math


class BidZGDZ(TaskBase):
    def __init__(self, debug=True):
        super(BidZGDZ, self).__init__()
        # Bid6.__init__(self, debug)
        # self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '大唐招标-招标公告'
        # self.parse_dict = parse_dict.get(self.file_name)
        self.collection_name = 'chdtp_com_jzxtpbg'
        self.key_field = 'article_url'

    # def get_cookies(self, content, url):
    #     self.log.error("error response, {}, url:{}".format(content[0], url))
    #     with sync_playwright() as playwright:
    #         browser = playwright.firefox.launch(headless=False)
    #         context = browser.new_context()
    #         page = context.new_page()
    #         page.goto(url)
    #         page.wait_for_load_state("networkidle")
    #         storage_state = context.storage_state()
    #         cookie = ''
    #         for cookie_info in storage_state['cookies']:
    #             cookie_text = cookie_info['name'] + '=' + cookie_info['value']
    #             cookie += cookie_text + ';'
    #         self.headers['Cookie'] = cookie.rstrip(';')
    #         context.close()
    #         browser.close()

    @staticmethod
    def parsePDF(filePath):
        with fitz.open(filePath) as doc:
            text = ""
            for page in doc.pages():
                text += page.get_text()
            return text

    def run(self):
        TIMEOUT = 60
        url = "https://www.chdtp.com/pages/wzglS/cgxx/caigou.jsp"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN, zh, q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '49',
            'Content - Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'JSESSIONID=CD27FE5A77F0989B28BA1983948A8846; acw_tc=2760778216917460279581058e2f47232cc7998fa63b5b202125a78adda5f2; acw_sc__v2=64d5feeb69150546794168b3c7ed70d8d6c0f029; ssxmod_itna=QqAxy7Dtiti=GQqiQDXYao0IpniRD0ljj6ioZnm140vWqPGzDAxn40iDtraTmDbghAKGb7GP2xvYiDeLPGC9B5dqbF0Ro05WDCPGnDB9DUAADYACDt4DTD34DYDio5DLDmeD+UsKDd06TN/GT=D3qDwDB=DmqG23miDA4tLDxUl/824keDSKYNomDtDjqGgDBLKtcbDGqaaxgXl/QWDbhPcbQrDtqD9GlU08eDHId0ZtL9GYGp5YG+6bG+KCO4K88GQzzDtl2GQ/xqtQYfKKD+TGt1iDD3oDxw3zBxxD; ssxmod_itna2=QqAxy7Dtiti=GQqiQDXYao0IpniRD0ljj6ioZnmxn93r4xDs==KDLGIQ7yD8QpoFKkD8r+=q2bWCH+7yY/0IuAe9=70=obFC7iQi94doFWIYokjB2mh=TZASPpwdcEM1oaVIzr4Tdk5+KStVDCXkGu04oSNfm80qwdr03RU3ofxodbTKMjQYojXKyQbf/unRK+Y3yMTbop3=o8ETNTFt6OUQd8YZF1A1ra3ZiZX1v=NiHMixN+3vc1OcnTf0jZSRiZgRUok+9oQmPqo6ovfh/FTUOZlU2giXwyZYVF+0j5socvfpRv/pAKBBIdcU7Ztx+0IeYSO6IciS1eM2j11mwlDiD+3rj/0td4A0j0i+wGAId=I=oP4ArcQKWn2qg05YwFbR/QrCUodFbo8TWtuk8wxlD7fA20TREx7fn8RnzUR3ZjaDG2ShxIuF0hxm+et0=YrQU5oyrHZDND2HRfKYMxCeF5uF22x4TKUi767CdM7DxOeLKBSxtR4DL8uDG=0rGi75q=mLxKRZl3F67wddh80+ghFl4tWrKbDru8=CCzDxDFqD+EriiDQzy6DIdiD4A40GPkTKnUSr7MX0SGG9CHGzqKzwFOeCCTCnSMxjSh8k4YD=',
            'Host': 'www.cdt-ec.com',
            'Origin': 'https://www.cdt-ec.com',
            'Referer': 'https://www.cdt-ec.com/notice/moreController/toMore?globleType=0&u_atoken=17d82ce5-f9da-40d4-951e-56821d58a723&u_asession=01u3UQZcH0xovwQqUhnnKf1xdlAD7KcYpnVOcsDamk_wHXqWuWWfydVuQ-d6MFcXlPX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K8Q4XSVjBdxeXWCLt5cKk6EJplDo7Akhkufk3kqWTOsm2BkFo3NEHBv0PZUm6pbxQU&u_asig=05jvzEToeIBylYTqO6AnQYpw_4H5WpqN1mDaVHeB5DApSE3g5TGF2vTlTeUs1qzVLpa3a9S-KH-3F322hKmYvsINYXqBqACq1l21wqK9nhjL4rDez-SFj0aMG1WfN7avP0CpanW1x_-FAfodylcuECnvzj1pzOFhOsO2dpdDJqmpX9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzTgKKFXEmKxprwQ7aOz9ko8-4PHYIYN0xgGU3DjUZmrPmamEEsKt2ZpuVEq9_MM2K-3h9VXwMyh6PgyDIVSG1W_1ixwfGuq6BepahKs3ItE4YGYDqHeX90h_yD6KfDquy4QA5UJDP1UNHkTJ9v3S9C5GtqWWOids5ubnpceSO867mWspDxyAEEo4kbsryBKb9Q&u_aref=3qBl9SbuduYAC8zceLeKADF0Va0%3D',
            'Sec-Ch-Ua': '"Google Chrome";v="113","Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 113.0.0.0Safari / 537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        url_base = 'https://www.cdt-ec.com/notice/moreController/getList'
        form_data = {
            'page': 1,
            'limit': 10,
            'messagetype': 0,
            'startDate': '',
            'endDate': ''
        }

        url = url_base.format(1)
        self.log.info("开始采集第1页：{}".format(url))
        content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, timeout=TIMEOUT,
                           verify=False)
        print(content)
        # content = self.req(url=url, headers=self.headers, timeout=TIMEOUT)
        # html = etree.HTML(content)
        # all_re_page = html.xpath('string(//span[@class="page"])')
        # total = html.xpath('string(//span[@class="page"])')
        # all_re_page = util.re_find_one('(?<=第).*?(?=页，)', all_re_page)
        # all_re_page = util.re_find_one('[^/]+(?!.*/)', all_re_page)
        # total = util.re_find_one('(?<=共).*?(?=条记录)', total)
        # total = int(total)
        # if all_re_page:
        #     all_re_page = int(all_re_page)
        # else:
        #     all_re_page = 1
        # pages = all_re_page
        # self.log.info("总页数：{},开始采集第1页：{}".format(all_re_page, url))
        # self.list_parse(content, url)
        # for num in range(2, pages + 1):
        #     data = {
        #         'cgggtype': 0,
        #         'jump': 1,
        #         'page.pageSize': 20,
        #         'page.currentpage': num,
        #         'page.totalCount': total
        #     }
        #     url = 'https://www.chdtp.com/webs/displayNewsCgxxAction.action'
        #     self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
        #     content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT, verify=False)
        #     if isinstance(content, tuple):
        #         if content[0] == "412":
        #             self.get_cookies(content, url)
        #             content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT,
        #                                verify=False)
        #         else:
        #             self.log.info("未找到：" + url)
        #             continue
        #     self.list_parse(content, url)
        # self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, maincontent, url):
        urlbase = 'https://www.chdtp.com/staticPage/'
        list_html = etree.HTML(maincontent)
        items = list_html.xpath('//form[@name="resultForm"]//table//tr')
        for item in items:
            if self.exit_flag:
                return
            title = item.xpath("string(./td[2]/a[1]/@title)")
            href_text = item.xpath("string(./td[2]/a[1]/@href)")
            href = util.re_find_one("'(.*?)'", href_text)
            detail_url = urljoin(urlbase, href)
            detail_content = self.req(url=detail_url, headers=self.headers)
            if isinstance(detail_content, tuple):
                if detail_content[0] == "412":
                    self.get_cookies(detail_content, url)
                    detail_content = self.req(url=detail_url, headers=self.headers)
                else:
                    self.log.info("未找到：" + url)
                    continue
            if not detail_content or isinstance(detail_content, tuple):
                self.log.error("{} no detail_content".format(detail_url))
                continue
            source_code = detail_content
            detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            html = etree.HTML(detail_content)
            html1 = etree.HTML(re.sub('</p>', '</p>\n', detail_content))
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            content_text1 = html1.xpath('string(//div[@class="box"]/div/table)')
            data = {}
            publish_time = item.xpath('string(./td[4])').replace('[', '').replace(']', '')
            data['article_url'] = detail_url
            data['标题'] = title
            data['时间'] = publish_time
            data['正文'] = content_text1.strip()
            data['源码'] = str(source_code).strip()
            data['所属频道'] = self.file_name
            # data[TABField.announcement] = item.xpath("string(./@title)")
            done_fields = []
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)

    def detail_parse(self, detail_content, detail_url, data=None, done_fields=None):
        # print(data)
        if not data:
            data = {}
        detail_content = detail_content.replace(" ", " ").replace("&nbsp;", " ")
        html = etree.HTML(detail_content)
        url = data.get("article_url")
        uuid = util.get_md5(url)
        data['uuid'] = uuid
        main_list = html.xpath('//div[@class="box"]/div[2]/table/tr')
        # print("table_list:", len(main_list))

        # data['项目名称'] = data['标题']
        purchase_name = util.re_find_one("采购组织机构：<a[\s\S]*?>([\s\S]*?)</a>", detail_content)
        data['招标人'] = purchase_name.strip()

        for i in main_list:
            temp = i.xpath('string(.//div[@class="tabmenu"])')
            if '基本信息' in temp:
                temp_list = i.xpath('.//div[@class="tabmenu"]/following-sibling::div//tr')
                for j in temp_list:
                    if "采购单号" in j.xpath('string(./td[@class="td_1"])'):
                        data['项目编号'] = j.xpath('string(./td[@class="td_2"])').strip()
                    elif "备注" in j.xpath('string(./td[@class="td_1"])'):
                        data['其他要求或说明'] = j.xpath('string(./td[@class="td_2"])').strip()
            elif '资格条件' in temp:
                data['招标条件'] = i.xpath('string(.//div[@class="tabmenu"]/following-sibling::div)').strip()
            elif '采购清单' in temp:
                temp_list = i.xpath('.//div[@class="tabmenu"]/following-sibling::div//tr[1]/td')
                col = len(temp_list)
                temp = 0
                cg1, cg2 = -1, -1
                for j in temp_list:
                    if '采购范围' in j.xpath('string(.)').strip():
                        cg1 = temp
                    elif '计划名称' in j.xpath('string(.)').strip():
                        cg2 = temp
                    temp += 1
                temp_list = i.xpath('.//div[@class="tabmenu"]/following-sibling::div//tr/td')
                temp = 0
                cg1_list, cg2_list = [], []
                for j in temp_list:
                    if 0 <= cg1 == temp % col:
                        if j.xpath('string(./@title)'):
                            cg1_list.append(j.xpath('string(./@title)').replace('\r', '').replace('\n', ' ').strip())
                    elif 0 <= cg2 == temp % col:
                        if j.xpath('string(./@title)'):
                            cg2_list.append(j.xpath('string(./@title)').replace('\r', '').replace('\n', ' ').strip())
                    temp += 1
                data['招标范围'] = '|'.join(cg1_list)
                data['项目名称'] = '|'.join(cg2_list)
        # print(data)
        self.upload(data)


if __name__ == '__main__':
    params = {
        "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    keyword = ''
    bid = BidZGDZ(debug=True)
    bid.process_item(params)