#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re

# import execjs
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree

from libs.base import TaskBase

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
from sites.PhaseFour.华电采购.libs import util
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
        self.file_name = '非招标公告-竞争性谈判报告'
        # self.parse_dict = parse_dict.get(self.file_name)
        self.collection_name = 'chdtp_com_jzxtpbg'
        self.key_field = 'article_url'

    def get_cookies_and_content(self, url):
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
            try:
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
            except Exception as e:
                pass
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

    def run(self):
        TIMEOUT = 60
        url = "https://www.chdtp.com/webs/displayNewsCgxxAction.action?cgggtype=0"
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.chdtp.com',
            'Referer': 'https://www.chdtp.com/pages/wzglS/homepage/index.jsp',
            'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.3'
        }
        # with sync_playwright() as playwright:
        #     browser = playwright.chromium.launch(headless=False)
        #     context = browser.new_context()
        #     page = context.new_page()
        #     js = """
        #         Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
        #     """
        #     page.add_init_script(js)  # 执行规避webdriver检测
        #     for i in range(2):
        #         page.goto(url)
        #         page.wait_for_load_state("networkidle")
        #         page.reload()
        #         time.sleep(3)
        #     storage_state = context.storage_state()
        #     cookie = ''
        #     for cookie_info in storage_state['cookies']:
        #         cookie_text = cookie_info['name'] + '=' + cookie_info['value']
        #         cookie += cookie_text + ';'
        #     self.headers['Cookie'] = cookie.rstrip(';')
        #     context.close()
        #     browser.close()
        #
        # url_base = 'https://www.chdtp.com/webs/displayNewsCgxxAction.action?cgggtype=0'
        #
        # url = url_base.format(1)
        # self.log.info("开始采集第1页：{}".format(url))
        # # content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, timeout=TIMEOUT,
        # #                    verify=False)
        # self.max_retries = 1
        # content = self.req(url=url, headers=self.headers, timeout=TIMEOUT)
        # # data = {
        # #     'cgggtype': "0",
        # #     'jump': "2",
        # #     'page.pageSize': "20",
        # #     'page.currentpage': "1",
        # #     'page.totalCount': "37787"
        # # }
        # # url = 'https://www.chdtp.com/webs/displayNewsCgxxAction.action'
        # # data = json.dumps(data)
        # # content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT, verify=False)
        # while True:
        #     if isinstance(content, tuple):
        #         if content[0] == 412 or content[0] == 400:
        #             self.get_cookies_and_content(url)
        #             content = self.req(url=url, headers=self.headers, timeout=TIMEOUT)
        #         else:
        #             self.log.info("未找到：" + url)
        #             return
        #     else:
        #         break
        # if not content:
        #     return
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
        #         'cgggtype': "0",
        #         'jump': str(num-1) if num-1 > 0 else "1",
        #         'page.pageSize': "20",
        #         'page.currentpage': str(num),
        #         'page.totalCount': str(total)
        #     }
        #     url = 'https://www.chdtp.com/webs/displayNewsCgxxAction.action'
        #     data = json.dumps(data)
        #     self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
        #     content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT, verify=False)
        #     if isinstance(content, tuple):
        #         if content[0] == 412:
        #             self.get_cookies_and_content(url)
        #             content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT,
        #                                verify=False)
        #         else:
        #             self.log.info("未找到：" + url)
        #             continue
        #     self.list_parse(content, url)
        # self.log.info("{} 数据采集完毕！".format(self.file_name))

        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            js = """
                Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
            """
            page.add_init_script(js)  # 执行规避webdriver检测
            page.goto(url)
            page.wait_for_load_state("networkidle")
            storage_state = context.storage_state()
            cookie = ''
            for cookie_info in storage_state['cookies']:
                cookie_text = cookie_info['name'] + '=' + cookie_info['value']
                cookie += cookie_text + ';'
            self.headers['Cookie'] = cookie.rstrip(';')
            # Get_the_data(page.content())
            content = page.content()

            while True:
                next_page_flag = self.list_parse(content, url)
                time.sleep(random.randint(60, 120))
                if next_page_flag:
                    page.locator('xpath=//span[@class="page"]/input[3]').click()
                    page.wait_for_load_state("networkidle")
                else:
                    break

            context.close()
            browser.close()

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
            # detail_content = self.req(url=detail_url, headers=self.headers)
            # if isinstance(detail_content, tuple):
            #     if detail_content[0] == 412:
            #         self.get_cookies_and_content(url)
            #         detail_content = self.req(url=detail_url, headers=self.headers)
            #     else:
            #         self.log.info("未找到：" + url)
            #         continue
            # if not detail_content or isinstance(detail_content, tuple):
            #     self.log.error("{} no detail_content".format(detail_url))
            #     continue
            # source_code = detail_content
            # detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            # detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            # html = etree.HTML(detail_content)
            # html1 = etree.HTML(re.sub('</p>', '</p>\n', detail_content))
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            # content_text1 = html1.xpath('string(//div[@class="box"]/div/table)')
            data = {}
            publish_time = item.xpath('string(./td[4])').replace('[', '').replace(']', '')
            data['article_url'] = detail_url
            data['标题'] = title
            data['时间'] = publish_time
            # data['正文'] = content_text1.strip()
            # data['源码'] = str(source_code).strip()
            data['所属频道'] = self.file_name
            # data[TABField.announcement] = item.xpath("string(./@title)")
            # done_fields = []
            # self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)
            self.upload(data)

        if not list_html.xpath('//span[@class="page"]/input[@src="images/page/page-next.jpg" and @disabled]'):
            return True
        else:
            return False

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