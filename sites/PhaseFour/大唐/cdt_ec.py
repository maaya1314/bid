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
from sites.PhaseFour.大唐.libs.util import re_find_one

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
        self.collection_name = 'cdt_ec'
        self.key_field = 'article_url'

    def get_cookies_and_content(self, url):
        # self.log.error("error response, url:{}".format(url))
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            js = """
                Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
            """
            page.add_init_script(js)  # 执行规避webdriver检测
            page.goto(url)
            page.wait_for_load_state("networkidle")
            # 检测滑块，滑动滑块
            slider = page.locator('xpath=//span[@id="nc_1_n1z"]').bounding_box()
            page.mouse.move(x=slider['x'], y=slider['y'] + slider['height'] / 2)
            page.mouse.down()
            time.sleep(random.randint(3, 5))
            page.mouse.move(x=slider['x'] + random.randint(380, 420), y=slider['y'] + slider['height'] / 2)
            page.mouse.up()
            # page.reload()
            page.wait_for_load_state("networkidle")
            time.sleep(random.randint(3, 5))
            storage_state = context.storage_state()
            cookie = ''
            for cookie_info in storage_state['cookies']:
                cookie_text = cookie_info['name'] + '=' + cookie_info['value']
                cookie += cookie_text + ';'
            self.headers['Cookie'] = cookie.rstrip(';')
            # Get_the_data(page.content())
            content = page.content()
            context.close()
            browser.close()
            return content

    @staticmethod
    def parsePDF(filePath):
        with fitz.open(filePath) as doc:
            text = ""
            for page in doc.pages():
                text += page.get_text()
            return text

    def run(self):
        TIMEOUT = 60
        url = "https://www.cdt-ec.com/notice/moreController/toMore?globleType=0&u_atoken=bd98cf7d-3271-4d10-bcd1-53985611740d&u_asession=01BuiPL1QWNmkRSCU_7-9jSqP7gZDlqZZTyXQW6Oymwkvr8f6KthKvfem1Pje0EaySX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K_k8_f1sFSkMCz8-3xLuHXW2l7GVvsUm1O1dQ3kAgydYmBkFo3NEHBv0PZUm6pbxQU&u_asig=05TLfL3h27z5sjRpO60Xhk4NU5x1hxO5pXcnkMYI-iwfnqqZasNftsuao-LeBRXrDAsgDAkPR7w6_tBqvulSN4MStFNgpPTFNmvzItC1YhFzvoBJug2FrzMO9kw20NPq916nATnqDTA9rbUZra1k9Iprzf2M1vHluuylPfr6S5_BP9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzcwzUxtlGDS7V6wN5_VesTeekrb8TAhSyrzElM7NYJIGaSuCIIsUrXvoQJBX3FajR-3h9VXwMyh6PgyDIVSG1W-sw6WMUGO1N3pj-xJWUPZCt2lto9GC4itIM2Ocb80SNOTnPjAx-GeZ09rrLQNMFmHVgXVlJdrPsvJ382Qlq5NomWspDxyAEEo4kbsryBKb9Q&u_aref=jHPCJD1H%2F51p%2F8%2Bj2zOlm%2FckGhw%3D"
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

        self.get_cookies_and_content(url)
        time.sleep(5)

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
        content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                           timeout=TIMEOUT, verify=False)
        # print(content)
        total = int(content['count'])
        all_re_page = total // 10 + 1
        if all_re_page:
            all_re_page = int(all_re_page)
        else:
            all_re_page = 1
        pages = all_re_page
        self.log.info("总页数：{},开始采集第1页：{}".format(all_re_page, url))
        self.list_parse(content, url)
        for num in range(2, pages + 1):
            form_data = {
                'page': num,
                'limit': 10,
                'messagetype': 0,
                'startDate': '',
                'endDate': ''
            }
            self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
            content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                               timeout=TIMEOUT, verify=False)
            if isinstance(content, tuple):
                if content[0] == "412":
                    self.get_cookies_and_content(url)
                    content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                                       timeout=TIMEOUT, verify=False)
                else:
                    self.log.info("未找到：" + url)
                    continue
            if not content:
                self.log.info(f"page {num} 无返回数据：" + url)
                break
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, maincontent, url):
        items = maincontent['data']

        for item in items:
            if self.exit_flag:
                return
            # title = item.xpath("string(./td[2]/a[1]/@title)")
            # href_text = item.xpath("string(./td[2]/a[1]/@href)")
            # href = util.re_find_one("'(.*?)'", href_text)
            # detail_url = urljoin(urlbase, href)
            title = item['message_title']
            href = item['id']
            detail_url = "https://www.cdt-ec.com/notice/moreController/moreall?id=" + href
            # detail_content = self.req(url=detail_url, headers=self.headers)
            # if isinstance(detail_content, tuple):
            #     if detail_content[0] == "412":
            #         self.get_cookies_and_content(detail_url)
            #         detail_content = self.req(url=detail_url, headers=self.headers)
            #     else:
            #         self.log.info("未找到：" + url)
            #         continue
            # if not detail_content or isinstance(detail_content, tuple):
            #     self.log.error("{} no detail_content".format(detail_url))
            #     continue
            # detail_content = self.req_simulation(detail_url)
            detail_content = self.get_cookies_and_content(detail_url)

            detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            # content_text1 = html.xpath('string(//div[@class="box"]/div/table)')
            data = {}
            publish_time = item['publish_time']
            data['article_url'] = detail_url
            data['标题'] = title
            data['时间'] = publish_time
            data['所属频道'] = self.file_name
            # data[TABField.announcement] = item.xpath("string(./@title)")
            done_fields = []
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)

    def detail_parse(self, detail_content, detail_url, data=None, done_fields=None):
        if not data:
            data = {}
        url = data.get("article_url")
        uuid = util.get_md5(url)
        data['uuid'] = uuid

        html = etree.HTML(detail_content)
        pdf_url = html.xpath('string(//embed[@id="embedid"]/@src)')
        pdf_url = pdf_url.split('file=')[-1].replace('%26', '&').replace('%3D', '=')
        if not pdf_url:
            print('no pdf_url!')
            return
        pdf_content = self.req(url=pdf_url, rsp_type="content")
        time.sleep(random.randint(10, 15))
        if isinstance(pdf_content, tuple):
            if pdf_content[0] == "412":
                self.get_cookies_and_content(detail_url)
                pdf_content = self.req(url=pdf_url, rsp_type="content")
            else:
                self.log.info("未找到：" + pdf_url)
                return
        if not pdf_content or isinstance(pdf_content, tuple):
            self.log.error("{} no detail_content".format(detail_url))
            return

        source_code = pdf_content
        data['源码'] = str(source_code).strip()
        with open("a.pdf", mode="wb") as f:
            f.write(pdf_content)  # 内容写入文件
        article = self.parsePDF("a.pdf")
        article = article.replace(' ', '')
        data['正文'] = article
        # article = article.replace('1. ', '|s|1. ').replace('2. ', '|s|2. ').replace('3. ', '|s|3. ').\
        #     replace('4. ', '|s|4. ').replace('5. ', '|s|5. ').replace('6. ', '|s|6. ').replace('7. ', '|s|7. ').\
        #     replace('8. ', '|s|8. ').replace('9. ', '|s|9. ').replace('10. ', '|s|10. ')

        # 分割段落
        at_list = article.split('\n')
        for at in range(len(at_list)):
            if re.match('\d{1}\.', at_list[at]):
                if not re.match('\d{1}\.\d{1}', at_list[at]):
                    at_list[at] = '|s|' + at_list[at]
            elif re.match('\d{1}', at_list[at]):
                # 不允许开头为2个数字,只能1个数字
                if not re.match('\d{2}', at_list[at]) and not re.match('\d{1}\.\d{1}', at_list[at]):
                    at_list[at] = '|s|' + at_list[at]
        article = '\n'.join(at_list)
        paragraph_list = article.split('|s|')
        if len(paragraph_list) > 1:
            temp_list = paragraph_list[0].split('\n')
            data['标题'] = ''
            title_flag = True
            for i in temp_list:
                if title_flag:
                    data['标题'] += i.strip()
                    if data['标题'].endswith('招标公告') or data['标题'].endswith('公告') or data['标题'].endswith('公示') \
                            or data['标题'].endswith('通知'):
                        title_flag = False
                    continue
                # 处理标题行出现招标相关信息
                if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人') or i.startswith('招标方'):
                    if not data.get('招标人', ''):
                        data['招标人'] = i
                elif i.startswith('招标代理机构'):
                    data['招标代理'] = i
                elif i.startswith('招标编号'):
                    data['项目编号'] = i

            # paragraph_list[0].replace('\n', '')

            data['项目名称'] = data['标题']
            for i in range(len(paragraph_list)):
                col_list = paragraph_list[i].split('\n')
                if '招标条件' in col_list[0]:
                    data['招标条件'] = ''
                    for j in col_list[1:]:
                        data['招标条件'] += j
                elif '项目概况与招标范围' in col_list[0] or '项目概况与采购范围' in col_list[0]:
                    at_list = paragraph_list[i].split('\n')
                    for j in at_list:
                        if '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j:
                            data['计划工期'] = j.split('计划工期：')[-1]
                    for at in range(len(at_list)):
                        if re.match('\d{1}\.\d{1}', at_list[at].strip()):
                            at_list[at] = '|s|' + at_list[at]
                    paragraph_list[i] = '\n'.join(at_list)
                    son_list = paragraph_list[i].split('|s|')
                    if len(son_list) > 1:
                        for j in son_list[1:]:  # 去掉标题行
                            if '招标编号：' in j:
                                # if not data.get('项目编号', ''):
                                data['项目编号'] = j.split('招标编号：')[-1]
                            elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j:
                                data['计划工期'] = j.split('计划工期：')[-1]
                            elif '招标范围：' in j:
                                data['招标范围'] = j.split('招标范围：')[-1]
                    else:
                        for j in at_list:
                            if '招标编号：' in j:
                                # if not data.get('项目编号', ''):
                                data['项目编号'] = j.split('招标编号：')[-1]
                            elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j:
                                data['计划工期'] = j.split('计划工期：')[-1]
                            elif '招标范围：' in j:
                                data['招标范围'] = j.split('招标范围：')[-1]
                elif '投标人资格要求' in col_list[0] or '投标人的资格要求' in col_list[0]:
                    data['投标人资格要求'] = ''
                    for j in col_list[1:]:
                        data['投标人资格要求'] += j
                elif '招标文件的获取' in col_list[0]:
                    data['招标文件的获取'] = ''
                    for j in col_list[1:]:
                        data['招标文件的获取'] += j
                elif '投标文件的递交' in col_list[0]:
                    data['投标文件的递交'] = ''
                    for j in col_list[1:]:
                        data['投标文件的递交'] += j
                elif '联系方式' in col_list[0]:
                    flag = '招标'
                    for j in col_list[1:]:
                        if '招标人：' in j or '采购单位' in j or '采购人' in j or '招标方' in j:
                            flag = '招标'
                            if not data.get('招标人', ''):
                                data['招标人'] = j.replace('招标人：', '')
                        elif '招标代理：' in j or '招标代理机构：' in j:
                            flag = '招标代理'
                            if not data.get('招标代理', ''):
                                data['招标代理'] = j.replace('招标代理机构：', '').replace('招标代理：', '')
                        elif '电话：' in j:
                            if flag == '招标':
                                if not data.get('招标人联系方式', ''):
                                    data['招标人联系方式'] = j.replace('电话：', '')
                            else:
                                if not data.get('招标代理联系方式', ''):
                                    data['招标代理联系方式'] = j.replace('电话：', '')
                elif '提出异议、投诉的渠道和方式' in col_list[0]:
                    # for j in col_list[1:]:
                    #     pass
                    pass
                elif '监督部门' in col_list[0]:
                    # for j in col_list[1:]:
                    #     pass
                    pass
                else:
                    pass
        else:
            at_list = paragraph_list[0].split('\n')
            data['标题'] = ''
            title_flag = True
            for i in at_list:
                if title_flag:
                    data['标题'] += i.strip()
                    if data['标题'].endswith('招标公告') or data['标题'].endswith('公告') or data['标题'].endswith('公示') \
                            or data['标题'].endswith('通知'):
                        title_flag = False
                    continue
                # 处理标题行出现招标相关信息
                if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人'):
                    if not data.get('招标人', ''):
                        data['招标人'] = i
                elif i.startswith('招标代理机构'):
                    data['招标代理'] = i
                elif i.startswith('招标编号'):
                    data['项目编号'] = i
                elif i.startswith('招标条件'):
                    data['招标条件'] = i
                elif i.startswith('计划工期') or i.startswith('工期') or i.startswith('交货期') or i.startswith('供货期') or i.startswith('协议期限') or i.startswith('服务期'):
                    data['计划工期'] = i
                elif i.startswith('招标编号'):
                    data['招标编号'] = i
                elif i.startswith('招标范围'):
                    data['招标范围'] = i
            data['项目名称'] = data['标题']

        print(data)
        self.upload(data)


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
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