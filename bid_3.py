#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2021/12/13 7:03 下午
@Author: CZC
@File: bid.py
"""
import json
import random
import re
import sys
import os
import datetime
import time
from urllib.parse import urljoin

from pymongo import UpdateOne, InsertOne
import requests
from lxml import etree
from tenacity import retry, stop_after_attempt, wait_fixed
from bid import Bid
from bid_tools.loghandler import getLogger
import pandas as pd
from openpyxl import load_workbook
from bid_tools.connectdb import MongoDB, TestDB
from bid_nlp_parser import Bid_company_parser
from bid_money_parser import Bid_money_parser
from bid_conf.conf_3 import phone_ban_list
import atexit
MAX_RETRY = 10
TIMEOUT = 60


class Bid3(Bid):
    def __init__(self, debug=True):
        Bid.__init__(self)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.columns_list = []
        self.file_name = sys.argv[0].split("/")[-1].replace(".py", "")
        self.time_sleep = ()
        self.parse_dict = ""
        self.items_list = []
        self.counts = 0
        self.max_pages = 1
        self.collection_name = 'guangdian_test'
        self.true_collection_name = 'guangdian'
        self.key_field = "article_url"
        self.key_field_2 = "keyword"
        self.debug = debug
        self.bid_company_parser = Bid_company_parser()
        self.bid_money_parser = Bid_money_parser()
        self._in_work()

    def detail_parse(self, detail_content, detail_url, data=None, done_fields=None):
        if not data:
            data = {}
        detail_content = detail_content.replace(" ", " ").replace("&nbsp;", " ")
        # 全局处理ban word
        for ban in phone_ban_list:
            detail_content = detail_content.replace(ban, "")
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
                        v = re.sub("<[\s\S]*?>", "", v).replace("\r", "").replace("\n", "").replace('&nbsp;', '').strip()
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
                        new_detail_content = re.sub("<p[\s\S]*?>", "<p>     ", detail_content).replace("</p>", "</p>     ")\
                            .replace("</br>", "     ").replace("<br>", "     ").replace("<br/>", "     ")
                        new_detail_content = re.sub("<h\d[\s\S]*?>", "<h1>     ", new_detail_content)
                        new_detail_content = re.sub("</h\d>", "</h1>     ", new_detail_content)
                        new_detail_content = re.sub('<div class="dg-flex"[\s\S]*?>', '<div class="dg-flex">     ', new_detail_content)
                        new_detail_content = re.sub('<div class="dg-flex-item"[\s\S]*?>', '<div class="dg-flex-item">     ', new_detail_content)
                        new_detail_content = re.sub('<.*? class="dg-flex-item"[\s\S]*?>', '<.*? class="dg-flex-item">     ', new_detail_content)
                        new_detail_content = re.sub("<script[\s\S]*?/script>", "     ", new_detail_content)
                        new_detail_content = re.sub("<style[\s\S]*?/style>", "     ", new_detail_content)
                        new_detail_content = re.sub("<div[\s\S]*?layout-grid-mode[\s\S]*?>", "<div>     ", new_detail_content)
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
                if result_value:
                    data[result_key] = result_value
            # data.update(result_data)
                # if "tender_unit" not in done_fields:
                #     data['tender_unit'] = nlp_tender_unit
                # if "bid_winner" not in done_fields:
                #     data['bid_winner'] = nlp_bid_winner
                # if "agency" not in done_fields:
                #     data['agency'] = nlp_agency

        phone = data.get("phone")
        if phone:
            phone_list = re.findall(r'\d[a-zA-Z0-9\-、－—\转\(\)（）/ ]{1,}', phone)
            phone = phone if not phone_list else phone_list[0]
            phone = phone.replace("电话", "").replace("：", "").replace("联系方式", "").replace("联系", "")\
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
                    if '万' in tender_price or '万元' in detail_content or '万元' in ddcontent or '万</span>元' in detail_content or '万</span>元' in ddcontent:
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
        if tender_price in (0, "0") or "中标" in self.file_name:
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
                    if '万' in win_bid_price or '万元' in detail_content or '万元' in ddcontent or '万</span>元' in detail_content or '万</span>元' in ddcontent:
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
            project_leader = project_leader.replace("\t", "").replace(" ", "").replace("联系人", "").replace("：", "").replace(":", "")\
                .replace("联系", "").replace("采购人", "").replace("方式", "").replace("电话", "").replace("招标", "").replace("项目", "")\
                .replace("手机", "").replace("号码", "")\
                .replace("证书编号", "").replace("、", "").replace("中标", "").replace("证明书扫描件", "").replace("；", "").strip()
            project_leader = re.sub("[0-9-，（）。]", "", project_leader)
            project_leader = project_leader.split("电　话")[0]
            project_leader = project_leader.split("受理时间")[0]
            data['project_leader'] = project_leader

        tender_unit = data.get("tender_unit")
        if tender_unit:
            tender_unit = tender_unit.replace("\t", "").replace(" ", "").replace(" ", "").replace("项目类别：施工", "")\
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
            agency = agency.replace("\t", "").replace(" ", "").replace("采购", "").replace("招标代理机构", "")\
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
            industry_type = industry_type.replace("项目类型", "").replace("：", "").replace("\r", "").replace("\n", "").strip()
            data['industry_type'] = industry_type

        bid_winner = data.get("bid_winner")
        if bid_winner:
            bid_winner = bid_winner.replace("：", "").replace("\r", "").replace("\n", "").replace("【", "").replace("】", "")\
                .replace("；", "").replace("，", "").replace("。", "").replace("1、", "").replace('（小微型企业）', '').strip()
            if 5 > len(bid_winner) > 25:
                try:
                    bid_winner = re.findall(".*公司", bid_winner)[0]
                except:
                    bid_winner = ""
            data['bid_winner'] = bid_winner

        project_number = data.get("project_number")
        if project_number:
            project_number = project_number.replace("：", "").replace("\r", "").replace("\n", "").replace("项目", "")\
                .replace("编号", "").replace("招标", "").replace("。", "").replace("【", "").replace("】", "")\
                .replace("[", "").replace("]", "").replace("；", "").replace("已开标", "").replace('第二次', '')\
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
            data['tender_unit'] = tender_unit
        project_overview = data.get("project_overview")
        if project_overview and len(project_overview) < 10:
            project_overview = ""
        data['project_overview'] = project_overview

        data['keyword'] = self.keyword
        data['article_url'] = detail_url
        data['harvested_time'] = datetime.datetime.now().strftime("%Y-%m-%d")  # 爬取时间
        # data['harvested_time'] = '2022-07-09'  # 爬取时间
        data['channel'] = self.file_name.split('-')[-1]
        data['source'] = self.file_name.replace(data.get("channel"), "")[0:-1]

        # if publish_time < self.query_time:
        #     self.log.info(f"文章发文时间 {publish_time} 早于查询时间 {self.query_time} ，跳过")
        #     self.exit_counts += 1
        #     if self.exit_counts == 20:
        #         self.exit_flag = True
        #     return
        self.exit_counts = 0
        self.fix_data(data, detail_content)
        self.upload(data)


if __name__ == "__main__":
    bid = Bid3()
    time_str = '开始：2022-01-02 17:30'
    ts = bid.format_time(time_str)
    print(ts)