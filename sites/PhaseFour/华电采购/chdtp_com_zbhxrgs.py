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

sys.path.append('../../PhaseTwo')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_7 import Bid7
from bid_conf.conf_7 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
from bid_tools import utils
import jsonpath
import math


class BidZGDZ(Bid7):
    def __init__(self, debug=True):
        Bid7.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '华电采购平台-中标候选人公示'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        url = "https://www.chdtp.com/webs/displayNewZbhxrgsZxzxAction.action?zbtype=2"
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'zZ6ZmsgRSJCBO=60R6H6cJmQTXEzerDXIUiC3QrehF4Xe9Zo6bXSiEk1oKxE897.EC1bfuOAhMExNlDX6CuE6_zZ.3opVqk6E.omfG; BIGipServerpool_web=1443080384.20480.0000; JSESSIONID=0000k7LgM5k3LoGHkn_i51_7zDD:1fak1ippc; zZ6ZmsgRSJCBP=0hM1ZWzb5saeZfZ7Ag15LfC5q1YHbcSHA5LoV_lpc_St7rVG4GXf_vnkQqnMhPvpLUPIqDxI.Vr13XFeLk34b_papRbYV9IyWyVoZbxeViLwIsRr9HRXby39M4zhbZQnRC3sB4iLDB6RuIhMuhWy7Sh_vlDoQqWrK9hhqItPMPsKDMadZl1Ac967iabxU4Dnhs52vZiPCVgo8Tw_UaY8wWhvB0h1nImZ7HHyMVSqxYnBIy1NwYVSG5pdij803rpAN8dfZCqH6R1i7LylGmsltqH7Wk1mCqGHeMnw4Im1wLdm2W8Iy2TPlDXpOmQUeKKo8gvBoim_4s6Qf2F8YHylbEjySOul94gvE6a5GzVhgpRo3czb9BcUMY8a4ZyHVH.oygZ1jthm0NrjKYPMbluxB3wUCz8SJAB9LnV_YR6A8KZL',
            'Host': 'www.chdtp.com',
            'Referer': 'https://www.chdtp.com/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        }
        # with sync_playwright() as playwright:
        #     browser = playwright.firefox.launch(headless=False)
        #     context = browser.new_context()
        #     page = context.new_page()
        #     page.goto(url)
        #     page.wait_for_load_state("networkidle")
        #     storage_state = context.storage_state()
        #     cookie = ''
        #     for cookie_info in storage_state['cookies']:
        #         cookie_text = cookie_info['name'] + '=' + cookie_info['value']
        #         cookie += cookie_text + ';'
        #     self.headers['Cookie'] = cookie.rstrip(';')
        #     context.close()
        #     browser.close()
        # # form_data = {
        # #     'type': '103',
        # #     'searchWay': 'onTitle',
        # #     'search': '',
        # #     'ifend': 'in',
        # #     'start': 0,
        # #     'limit': 50
        # # }
        # url_base = 'https://www.chdtp.com/webs/queryWebZbgg.action?zbggType={}'
        # url = url_base.format(2)
        # self.log.info("开始采集第1页：{}".format(url))
        # # content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, timeout=TIMEOUT,
        # #                    verify=False)
        # content = self.req(url=url, headers=self.headers, timeout=TIMEOUT)
        # html = etree.HTML(content)
        # all_re_page = html.xpath('string(//span[@class="page"])')
        # all_re_page = utils.re_find_one('(?<=第).*?(?=页，)', all_re_page)
        # all_re_page = utils.re_find_one('[^/]+(?!.*/)', all_re_page)
        # if all_re_page:
        #     all_re_page = int(all_re_page)
        # else:
        #     all_re_page = 1
        # pages = all_re_page
        # self.log.info("总页数：{},开始采集第1页：{}".format(all_re_page, url))
        # self.list_parse(content, url)
        # for num in range(2, pages + 1):
        #     data_base = 'jump=1&page.pageSize=20&page.currentpage={}&page.totalCount=13094'
        #     url = 'https://www.chdtp.com/webs/displayNewZbhxrgsZxzxAction.action'
        #     data = data_base.format(num)
        #     self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
        #     content = self.req(url=url, req_type='post', headers=self.headers, data=data, timeout=TIMEOUT, verify=False)
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

            while True:
                content = page.content()
                _cur_page = utils.re_find_one("第 (\d+)/\d+ 页，共\d+条记录", content)
                next_page_flag = self.list_parse(content, url)
                self.log.info(f"page {_cur_page} completed !")
                time.sleep(random.randint(60, 120))
                if next_page_flag:
                    page.locator('xpath=//span[@class="page"]/input[3]').click()
                    page.wait_for_load_state("networkidle")
                else:
                    break

            context.close()
            browser.close()
        time.sleep(2)
        # with sync_playwright() as playwright:
        #     browser = playwright.firefox.launch(headless=False)
        #     context = browser.new_context()
        #     page = context.new_page()
        #     js = """
        #         Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
        #     """
        #     page.add_init_script(js)  # 执行规避webdriver检测
        #     while True:
        #         try:
        #             data_list = self.db.db[self.collection_name].find({'所属频道': self.file_name}).batch_size(20)
        #             for d in data_list:
        #                 if d.get('正文', '') == 'abcdefghijklmnopqrstuvwxyz1234567890':
        #                     url = d['article_url']
        #                     page.goto(url)
        #                     page.wait_for_load_state("networkidle")
        #                     content = page.content()
        #                     data = {}
        #                     data['article_url'] = url
        #                     data['project_title'] = d['标题']
        #                     data['publish_time'] = d['时间']
        #                     # data['源码'] = str(source_code).strip()
        #                     data['content'] = content.strip()
        #                     data['channel'] = self.file_name
        #                     self.detail_parse(content, url, data, done_fields=[])
        #                     time.sleep(random.randint(40, 60))
        #             if not data_list.alive:
        #                 # print("等待数据更新...")
        #                 # time.sleep(60)
        #                 data_list.close()
        #                 break
        #             data_list.close()
        #         except Exception as e:
        #             print("error:", e)
        #             data_list.close()
        #             time.sleep(10)
        #             continue

    def list_parse(self, maincontent, url):
        urlbase = 'https://www.chdtp.com/staticPage/'
        list_html = etree.HTML(maincontent)
        # items = list_html.xpath('//form[@name="resultForm"]//table//tr/td[2]/a[1]')
        items = list_html.xpath('//form[@name="resultForm"]//table//tr')
        for item in items:
            if self.exit_flag:
                return
            title = item.xpath("string(./td[2]/a[1]/@title)")
            href_text = item.xpath("string(./td[2]/a[1]/@href)")
            href = utils.re_find_one("'(.*?)'", href_text)
            if not href:
                continue
            detail_url = urlbase + href
            # title = item.xpath("string(./@title)")
            # href_text = item.xpath("string(./@href)")
            # href = utils.re_find_one("'(.*?)'", href_text)
            # detail_url = urljoin(urlbase, href)
            # detail_content = self.req(url=detail_url, headers=self.headers)
            # if not detail_content or detail_content == 404 or detail_content == 400:
            #     self.log.error("{} no detail_content".format(detail_url))
            #     continue
            # source_code = detail_content
            # detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            # detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            # html = etree.HTML(detail_content)
            # html1 = etree.HTML(re.sub('</p>', '</p>\n', detail_content))
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            # content_text1 = html1.xpath('string(//title/following-sibling::div)')
            data = {}
            publish_time = item.xpath('string(./td[@class="td_4"])').replace('[', '').replace(']', '')
            data['article_url'] = detail_url
            data['project_title'] = title
            data['publish_time'] = publish_time
            data['content'] = 'abcdefghijklmnopqrstuvwxyz1234567890'  # 占位，防止底层报错
            # data['source_code'] = str(source_code).strip()
            data['channel'] = self.file_name
            # data[TABField.announcement] = item.xpath("string(./@title)")
            # done_fields = []
            # self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)
            self.upload(data, output_type='db')

        if not list_html.xpath('//span[@class="page"]/input[@src="images/page/page-next.jpg" and @disabled]'):
            return True
        else:
            return False

    def detail_parse(self, detail_content, detail_url, data=None, done_fields=None):
        if not data:
            data = {}
        detail_content = detail_content.replace(" ", " ").replace("&nbsp;", " ")
        html = etree.HTML(detail_content)
        # html_string = html.xpath("string(.)")
        for key, items in self.parse_dict.items():
            # 正则优先
            if not data.get(key):
                data[key] = ""
            re_list = items.get('re')
            for r in re_list:
                if not r:
                    continue
                if data.get(key) and data.get(key, "") not in ("详见公告正文", "null"):
                    break
                try:
                    re_value = re.findall(r, detail_content)
                    for v in re_value:
                        v = re.sub("<[\s\S]*?>", "", v).replace("\r", "").replace("\n", "").replace('&nbsp;',
                                                                                                    '').strip()
                        # 补丁
                        if key == "project_number" and v and len(v) > 40 and 'ec.ceec.net.cn' not in detail_url and \
                                'www.e-bidding.org' not in detail_url:
                            v = ""
                        elif key == "phone" and v and (len(v) > 30 or len(v) < 6):
                            v = ""
                        data[key] = v
                        break
                except:
                    data[key] = ""

            xpath_list = items.get("xpath")
            temp_result = ""
            for x in xpath_list:
                if not x:
                    continue
                if data.get(key):
                    break
                try:
                    if key == 'content':
                        # new_detail_content = re.sub("<p[\s\S]*?>", "    ", detail_content).replace("</p>", "    ").replace("</br>", "    ").replace("<br>", "    ")
                        new_detail_content = re.sub("<p[\s\S]*?>", "<p>     ", detail_content).replace("</p>",
                                                                                                       "</p>     ") \
                            .replace("</br>", "     ").replace("<br>", "     ").replace("<br/>", "     ")
                        new_detail_content = re.sub("<h\d[\s\S]*?>", "<h1>     ", new_detail_content)
                        new_detail_content = re.sub("</h\d>", "</h1>     ", new_detail_content)
                        new_detail_content = re.sub('<div class="dg-flex"[\s\S]*?>', '<div class="dg-flex">     ',
                                                    new_detail_content)
                        new_detail_content = re.sub('<div class="dg-flex-item"[\s\S]*?>',
                                                    '<div class="dg-flex-item">     ', new_detail_content)
                        new_detail_content = re.sub('<.*? class="dg-flex-item"[\s\S]*?>',
                                                    '<.*? class="dg-flex-item">     ', new_detail_content)
                        new_detail_content = re.sub("<script[\s\S]*?/script>", "     ", new_detail_content)
                        new_detail_content = re.sub("<style[\s\S]*?/style>", "     ", new_detail_content)
                        new_detail_content = re.sub("<div[\s\S]*?layout-grid-mode[\s\S]*?>", "<div>     ",
                                                    new_detail_content)
                        # new_detail_content = detail_content
                        content_html = etree.HTML(new_detail_content)
                        x_xpath_value = content_html.xpath(x)
                    else:
                        x_xpath_value = html.xpath(x)
                    if isinstance(x_xpath_value, list):
                        for v in x_xpath_value:
                            temp_result = v if isinstance(v, str) else v.xpath("string(.)")
                            if temp_result:
                                if key == 'attachment_url':
                                    temp_result = urljoin(detail_url, temp_result)
                                if not data.get(key):
                                    data[key] += temp_result.replace("\r", "").replace("\n", "").strip()
                                else:
                                    if key == "content":
                                        # 5个空格为了兼容后面实体抽取段落换行
                                        data[key] += "     " + temp_result.replace("\r", "").replace("\n", "").strip()
                                    else:
                                        data[key] += "," + temp_result.replace("\r", "").replace("\n", "").strip()
                    elif isinstance(x_xpath_value, str):
                        temp_result = x_xpath_value
                        if temp_result:
                            data[key] = temp_result.replace("\r", "").replace("\n", "").strip()
                            break

                except:
                    data[key] = ""
        content = data.get("content")
        content = re.sub('function.*?\{[\s\S]*?\}', "", content)
        data['content'] = content

        article_title = data.get("project_title")
        result_data = self.bid_company_parser.do_parser(content, article_title)
        win_money, budget_money = self.bid_money_parser.do_parser(content)
        result_data['win_bid_price'] = win_money
        result_data['tender_price'] = budget_money
        if result_data:
            # nlp_tender_unit = result_data.get("zhaobiao")
            # nlp_bid_winner = result_data.get("zhongbiao")
            # nlp_agency = result_data.get("")
            if done_fields:
                for field in done_fields:
                    result_data.pop(field)
            for result_key, result_value in result_data.items():
                if not data.get(result_key):
                    if result_value:
                        data[result_key] = result_value
            # data.update(result_data)
            # if "tender_unit" not in done_fields:
            #     data['tender_unit'] = nlp_tender_unit
            # if "bid_winner" not in done_fields:
            #     data['bid_winner'] = nlp_bid_winner
            # if "agency" not in done_fields:
            #     data['agency'] = nlp_agency

        publish_time = data.get("publish_time")
        if publish_time:
            publish_time = self.format_time(publish_time)
            data['publish_time'] = publish_time

        bid_finish_time = data.get("bid_finish_time")
        if bid_finish_time:
            bid_finish_time = self.format_time(bid_finish_time)
            data['bid_finish_time'] = bid_finish_time

        bid_end_time = data.get("bid_end_time")
        if bid_end_time:
            bid_end_time = self.format_time(bid_end_time)
            data['bid_end_time'] = bid_end_time

        win_bid_announcement_time = data.get("win_bid_announcement_time")
        if not win_bid_announcement_time:
            final_content = content[-30:]
            win_bid_announcement_time = "" if not re.findall("\d{4}.*?日", final_content) else \
            re.findall("\d{4}.*?日", final_content)[0]
        if win_bid_announcement_time:
            win_bid_announcement_time = self.format_time(win_bid_announcement_time)
            data['win_bid_announcement_time'] = win_bid_announcement_time

        attachment_url = data.get("attachment_url")

        if attachment_url:
            if not attachment_url.startswith("http"):
                attachment_url = urljoin(detail_url, attachment_url)
                # attachment_url = attachment_url if attachment_url.startswith('http') else 'http:' + attachment_url
                data['attachment_url'] = attachment_url

        phone = data.get("phone")
        if phone:
            phone_list = re.findall(r'\d[a-zA-Z0-9\-、－—\转\(\)（）/ ]{1,}', phone)
            phone = phone if not phone_list else phone_list[0]
            phone = phone.replace("电话", "").replace("：", "").replace("联系方式", "").replace("联系", "") \
                .replace("项目负责", "").replace("人", "").strip()
            if phone.endswith("（"):
                try:
                    phone = re.findall('[0-9-]{1,}', phone)[0]
                except:
                    phone = ""
            if len(phone) < 6:
                phone = ''
            if ("）" in phone and "（" not in phone) or ("（" in phone and "）" not in phone):
                phone.replace("）", "").replace("（", "")
            data["phone"] = phone

        tender_price = data.get("tender_price")
        ddcontent = etree.tostring(html, encoding='unicode')
        if tender_price:
            tender_price = tender_price.replace(",", "")
            price_list = re.findall("([0-9\.]{1,})", tender_price)
            if price_list:
                new_tender_price = price_list[0]
                try:
                    if '万' in new_tender_price or (100 < int(float(new_tender_price)) < 10000 and (
                            '万元' in detail_content or '万元' in ddcontent or '万</span>元' in detail_content or '万</span>元' in ddcontent)):
                        new_tender_price = "{}元".format(int(float(new_tender_price) * 10000))
                    else:

                        new_tender_price = "{}元".format(int(float(new_tender_price)))
                except Exception as e:
                    self.log.error("error new_tender_price:{}".format(new_tender_price))
                    new_tender_price = ""
                if new_tender_price == '0':
                    new_tender_price = ""
            else:
                new_tender_price = ""
            data['tender_price'] = new_tender_price
        if tender_price in (0, "0"):
            data['tender_price'] = ""

        win_bid_price = data.get("win_bid_price")
        if win_bid_price:
            win_bid_price = win_bid_price.replace(",", "")
            price_list = re.findall("([0-9\.]{1,})", win_bid_price)
            if price_list:
                new_win_bid_price = price_list[0]
                if len(new_win_bid_price) < 5:
                    new_win_bid_price = ""
                try:
                    if '万' in win_bid_price or (100 < int(float(new_win_bid_price)) < 10000 and (
                            '万元' in detail_content or '万元' in ddcontent or '万</span>元' in detail_content or '万</span>元' in ddcontent)):
                        new_win_bid_price = "{}元".format(int(float(new_win_bid_price) * 10000))
                    else:
                        new_win_bid_price = "{}元".format(int(float(new_win_bid_price)))
                except Exception as e:
                    self.log.error("error new_win_bid_price:{}".format(new_win_bid_price))
                    new_win_bid_price = ""
            else:
                new_win_bid_price = ""
            data['win_bid_price'] = new_win_bid_price

        project_leader = data.get("project_leader")
        if project_leader:
            project_leader = project_leader.replace("\t", "").replace(" ", "").replace("联系人", "").replace("：",
                                                                                                          "").replace(
                ":", "") \
                .replace("联系", "").replace("采购人", "").replace("方式", "").replace("电话", "").replace("招标", "").replace(
                "项目", "") \
                .replace("手机", "").replace("号码", "") \
                .replace("证书编号", "").replace("、", "").replace("中标", "").replace("证明书扫描件", "").replace("；", "").strip()
            project_leader = re.sub("[0-9-，（）。]", "", project_leader)
            project_leader = project_leader.split("电　话")[0]
            project_leader = project_leader.split("受理时间")[0]
            data['project_leader'] = project_leader

        tender_unit = data.get("tender_unit")
        if tender_unit:
            tender_unit = tender_unit.replace("\t", "").replace(" ", "").replace(" ", "").replace("项目类别：施工", "") \
                .replace("采购人", "").replace("：", "").replace("单位名称", "").replace("名称", "").replace("招标人", "").strip()
            if len(tender_unit) > 25:
                tender_unit = tender_unit.split("联系")[0].split("地址")[0].split("项目")[0]
            if len(tender_unit) > 35:
                try:
                    tender_unit = re.findall(".*?公司", tender_unit)[0]
                except:
                    tender_unit = ""
            data['tender_unit'] = tender_unit

        agency = data.get("agency")
        if agency:
            agency = agency.replace("\t", "").replace(" ", "").replace("采购", "").replace("招标代理机构", "") \
                .replace("代理机构", "").replace("：", "").replace("名称", "").replace('（盖章）', "").strip()
            if len(agency) > 25:
                try:
                    agency = re.findall(".*?公司", agency)[0]
                    if len(agency) > 20:
                        agency = ''
                except:
                    agency = ""
            if len(agency) < 5:
                agency = ""
            data['agency'] = agency

        industry_type = data.get("industry_type")
        if industry_type:
            industry_type = industry_type.replace("项目类型", "").replace("：", "").replace("\r", "").replace("\n",
                                                                                                         "").strip()
            data['industry_type'] = industry_type

        bid_winner = data.get("bid_winner")
        if bid_winner:
            bid_winner = bid_winner.replace("：", "").replace("\r", "").replace("\n", "").replace("【", "").replace("】",
                                                                                                                  "") \
                .replace("；", "").replace("，", "").replace("。", "").replace("1、", "").replace('（小微型企业）', '').strip()
            if 5 > len(bid_winner) > 25:
                try:
                    bid_winner = re.findall(".*公司", bid_winner)[0]
                except:
                    bid_winner = ""
            data['bid_winner'] = bid_winner

        project_number = data.get("project_number")
        if project_number:
            project_number = project_number.replace("：", "").replace("\r", "").replace("\n", "").replace("项目", "") \
                .replace("编号", "").replace("招标", "").replace("。", "").replace("【", "").replace("】", "") \
                .replace("[", "").replace("]", "").replace("；", "").replace("已开标", "").replace('第二次', '') \
                .replace(',', "").strip()
            project_number = project_number.split("成交")[0]
            project_number = project_number.split("作")[0]
            if project_number.endswith("）"):
                project_number = project_number[:-1]
            if project_number.endswith("（"):
                project_number = project_number[:-1]
            if project_number.endswith(")"):
                project_number = project_number[:-1]
            if project_number.endswith("-"):
                project_number = project_number[:-1]
            if project_number.endswith("("):
                project_number = project_number[:-1]
            try:
                pn_list = re.findall('[a-zA-Z0-9-//（）]{1,}', project_number)
                pn = "".join(pn_list)
                if len(pn) < 4 or len(pn_list) > 3:
                    project_number = ""
                if re.findall("[\u4e00-\u9fa5]{3,}", project_number):
                    project_number = ""
            except:
                project_number = ""
            # if len(project_number) > 40:
            #     project_number = ""
            data['project_number'] = project_number

        tender_unit = data.get("tender_unit")
        project_title = data.get("project_title")
        if project_title and not tender_unit:
            try:
                project_title = re.sub("\d{4}年", "", project_title)
                tender_unit = re.findall("([^A-Za-z0-9_]{4,20}?[司|厂|所|局])", project_title)[0]
                if len(tender_unit) < 5:
                    tender_unit = ""
            except Exception as e:
                # self.log.error(e)
                tender_unit = ""
            data['tender_unit'] = tender_unit.replace("[", "").replace("]", "").replace("【", "").replace("】", "")
        project_overview = data.get("project_overview")
        if project_overview and len(project_overview) < 10:
            project_overview = ""
        data['project_overview'] = project_overview
        data['keyword'] = self.keyword
        data['article_url'] = detail_url
        data['harvested_time'] = datetime.datetime.now().strftime("%Y-%m-%d")  # 爬取时间
        # data['harvested_time'] = '2022-07-09'  # 爬取时间
        # data['channel'] = self.file_name.split('-')[-1]
        data['source'] = self.file_name.replace(data.get("channel"), "")[0:-1]
        duration = data.get("duration")
        if duration:
            if not re.match("\d+", duration):
                data['duration'] = ""
        project_name = data.get('project_name', '')
        if not project_name or ('<' in project_name and '>' in project_name):
            data['project_name'] = data['project_title']
        # if publish_time < self.query_time:
        #     self.log.info(f"文章发文时间 {publish_time} 早于查询时间 {self.query_time} ，跳过")
        #     self.exit_counts += 1
        #     if self.exit_counts == 20:
        #         self.exit_flag = True
        #     return
        self.exit_counts = 0
        self.fix_data(data, detail_content)
        self.upload(data, output_type='db')


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

    # BidZGDZ.run(keyword)
