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
from redis import StrictRedis
from elasticsearch import Elasticsearch, helpers
from pymongo import UpdateOne, InsertOne
import requests
from lxml import etree
from tenacity import retry, stop_after_attempt, wait_fixed

from bid_tools.loghandler import getLogger
import pandas as pd
from openpyxl import load_workbook


class RedisConf(object):
    host = "125.88.221.92"
    port = 6379
    db = 1
    password = "yongli@123"
    name = "yny_proxies_list"


class Proxies(object):
    def __init__(self):  #
        self.redis_conn = StrictRedis(host=RedisConf.host, port=RedisConf.port, db=RedisConf.db, password=RedisConf.password)
        # self.redis_pool = ConnectionPool(host=RedisConf.host, port=RedisConf.port, password=RedisConf.password, db=RedisConf.db)
        # self.redis_conn = Redis(connection_pool=self.redis_pool)
        self.redis_name = RedisConf.name

    def get_proxy(self):
        while 1:
            proxy_lens = self.redis_conn.llen(self.redis_name)
            proxy_index = random.choice(range(proxy_lens))
            proxy = self.redis_conn.lindex(self.redis_name, proxy_index)
            proxy = json.loads(proxy)
            if not proxy:
                time.sleep(0.01)
                continue
            break
        # log.info(f">>> 线程获取： {getcurrentname()} : {proxy}")
        return proxy


class Bid(object):
    def __init__(self, debug=True):
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.columns_list = []
        self.file_name = sys.argv[0].split("/")[-1].replace(".py", "")
        self.time_sleep = ()
        self.parse_dict = ""
        self.items_list = []
        self.counts = 0
        self.collection_name = 'guangdian_test'
        self.true_collection_name = 'guangdian'
        self.key_field = "article_url"
        self.key_field_2 = "keyword"
        self.debug = debug
        self.es_index = 'mongo_to_es'
        self._in_work()

    def _in_work(self):
        host = '120.196.62.61'
        port = '9200'
        es_header = [{'host': host, 'port': port, 'verify_certs': False}]
        self.es = Elasticsearch(es_header)

    def process_item(self, params):
        if not self.parse_dict:
            self.log.error("error conf site name {}".format(self.file_name))
            return
        try:
            query_time = int(params.get("query_time"))
        except:
            query_time = 9999
            self.log.info("not query_time value: {}, set query_time:{}".format(params.get('query_time'), query_time))
        cur_time = datetime.datetime.now()
        self.query_time = str((cur_time + datetime.timedelta(days=-query_time)).strftime('%Y-%m-%d'))
        self.proxy_flag = params.get("proxy_flag")
        self.time_sleep = params.get('time_sleep')
        keyword_list = params.get("MainKeys")
        for keyword in keyword_list:
            self.run(keyword)
        self.check_upload_es()

    def run(self, keyword):
        self.keyword = keyword

    def format_time(self, time_str):
        time_str = time_str.replace("：", "").replace("时间", "").strip()
        try:
            time_str = datetime.datetime.strptime(time_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            return time_str
        except:
            pass
        try:
            findall = re.findall("[0-9-: /年月日时分秒\.]+", time_str)
            extract_time = findall[0].strip()
        except:
            return None
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y.%m.%d').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y/%m/%d').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y-%m-%d%H:%M:%S').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y-%m-%d %H:%M').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y/%m/%d %H:%M:%S').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y%m%d %H:%M').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y年%m月%d日').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y年%m月%d日%H时%M分%S秒').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y年%m月%d日%H时%M分').strftime('%Y-%m-%d')
            return format_time
        except:
            pass
        return None

    def detail_parse(self, detail_content, detail_url, data=None):
        if not data:
            data = {}
        detail_content = detail_content.replace(" ", " ").replace("&nbsp;", "")
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
                                        data[key] += temp_result.replace("\r", "").replace("\n", "").strip()
                                    else:
                                        data[key] += "," + temp_result.replace("\r", "").replace("\n", "").strip()
                    elif isinstance(x_xpath_value, str):
                        temp_result = x_xpath_value
                        if temp_result:
                            data[key] = temp_result.replace("\r", "").replace("\n", "").strip()
                            break

                except:
                    data[key] = ""

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
            else:
                new_tender_price = ""
            data['tender_price'] = new_tender_price

        win_bid_price = data.get("win_bid_price")
        if win_bid_price:
            win_bid_price = win_bid_price.replace(",", "")
            price_list = re.findall("([0-9\.]{1,})", win_bid_price)
            if price_list:
                new_win_bid_price = price_list[0]
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
                .replace("证书编号", "").replace("、", "").replace("中标", "").strip()
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
                except:
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
            if len(bid_winner) > 25:
                try:
                    bid_winner = re.findall(".*?公司", bid_winner)[0]
                except:
                    bid_winner = ""
            data['bid_winner'] = bid_winner

        project_number = data.get("project_number")
        if project_number:
            project_number = project_number.replace("：", "").replace("\r", "").replace("\n", "").replace("项目", "")\
                .replace("编号", "").replace("招标", "").replace("。", "").replace("【", "").replace("】", "")\
                .replace("[", "").replace("]", "").replace("；", "").replace("已开标", "").replace('第二次', '').strip()
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
                # if 7 < len(pn_list[0]) < 25:
                #     project_number = pn_list[0]
            except:
                project_number = ""
            if len(project_number) > 30 and 'ec.ceec.net.cn' not in detail_url and 'www.e-bidding.org' not in detail_url:
                project_number = ""
            data['project_number'] = project_number

        tender_unit = data.get("tender_unit")
        project_title = data.get("project_title")
        if project_title and not tender_unit:
            try:
                project_title = re.sub("\d{4}年", "", project_title)
                tender_unit = re.findall("([\u4e00-\u9fa5]+?公司|[\u4e00-\u9fa5]+?局)", project_title)[0]
            except:
                tender_unit = ""
            data['tender_unit'] = tender_unit

        data['keyword'] = self.keyword
        data['article_url'] = detail_url
        data['harvested_time'] = datetime.datetime.now().strftime("%Y-%m-%d")  # 爬取时间
        data['source'] = self.file_name.split('-')[0]
        data['channel'] = self.file_name.split('-', 1)[-1]
        # if publish_time < self.query_time:
        #     self.log.info(f"文章发文时间 {publish_time} 早于查询时间 {self.query_time} ，跳过")
        #     self.exit_counts += 1
        #     if self.exit_counts == 20:
        #         self.exit_flag = True
        #     return
        self.exit_counts = 0
        self.fix_data(data, detail_content)
        self.upload(data)

    def fix_data(self, data, detail_content):
        pass

    def format_data(self, data):
        detail_url = data.get('article_url')
        content = data.get("content")
        publish_time = data.get("publish_time")
        if publish_time:
            publish_time = self.format_time(publish_time)
            data['publish_time'] = publish_time
        else:
            data['publish_time'] = None

        bid_finish_time = data.get("bid_finish_time")
        if bid_finish_time:
            bid_finish_time = self.format_time(bid_finish_time)
            data['bid_finish_time'] = bid_finish_time
        else:
            data['bid_finish_time'] = None

        bid_end_time = data.get("bid_end_time")
        if bid_end_time:
            bid_end_time = self.format_time(bid_end_time)
            data['bid_end_time'] = bid_end_time
        else:
            data['bid_end_time'] = None


        win_bid_announcement_time = data.get("win_bid_announcement_time")

        if not win_bid_announcement_time:
            final_content = content[-30:]
            win_bid_announcement_time = "" if not re.findall("\d{4}.*?日", final_content) else \
            re.findall("\d{4}.*?日", final_content)[0]
        if win_bid_announcement_time:
            win_bid_announcement_time = self.format_time(win_bid_announcement_time)
            data['win_bid_announcement_time'] = win_bid_announcement_time
        else:
            data['win_bid_announcement_time'] = None

        attachment_url = data.get("attachment_url")

        if attachment_url:
            if not attachment_url.startswith("http"):
                attachment_url = urljoin(detail_url, attachment_url)
                # attachment_url = attachment_url if attachment_url.startswith('http') else 'http:' + attachment_url
                data['attachment_url'] = attachment_url

        attachment_url = data.get("attachment_url")

        if attachment_url:
            if not attachment_url.startswith("http"):
                attachment_url = urljoin(detail_url, attachment_url)
                # attachment_url = attachment_url if attachment_url.startswith('http') else 'http:' + attachment_url
                data['attachment_url'] = attachment_url

    def upload(self, data, output_type="es"):
        self.format_data(data)
        if output_type == 'db':
            self.upload_db(data)
            return
        elif output_type == 'es':
            self.upload_es(data)
            return
        for k, v in data.items():
            self.log.debug("{}: {}".format(k, v))
        if self.columns_list:
            columns = self.columns_list
        else:
            # columns = list(self.data_list[0].keys())
            columns = list(data.keys())

        temp_list = [list(data.values())]
        sheet_name = 'Sheet1'
        if data.get('post_type') == "comment":
            file_name = "{}-评论.xlsx".format(data.get("site_name", self.file_name))
            if not os.path.exists(file_name):
                pd.DataFrame(temp_list, columns=columns).to_excel(file_name, index=None)
                return
        else:
            file_name = "{}{}-{}.xlsx".format(data.get("site_name", self.file_name), "-修复", datetime.datetime.now().strftime("%Y-%m-%d"))
            if not os.path.exists(file_name):
                pd.DataFrame(temp_list, columns=columns).to_excel(file_name, index=None)
                return
        # file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        df = pd.DataFrame(temp_list, columns=columns)  # 列表数据转为数据框
        df1 = pd.DataFrame(pd.read_excel(file_name, sheet_name=sheet_name))  # 读取原数据文件和表
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        book = load_workbook(file_name)
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        df_rows = df1.shape[0]  # 获取原数据的行数
        df.to_excel(writer, sheet_name=sheet_name, startrow=df_rows + 1, index=False,
                    header=False)  # 将数据写入excel中的aa表,从第一个空行开始写
        writer.save()  # 保存
        if self.time_sleep:
            time.sleep(random.randint(self.time_sleep[0], self.time_sleep[1]))

    def upload_db(self, data):
        self.counts += 1
        # self.db[self.collection].update_one({'url': url}, {'$set': temp_dict}, upsert=True)
        for k, v in data.items():
            self.log.debug("{}: {}".format(k, v))
        if not data.get('project_title'):
            self.log.debug('null {}'.format(data.get('article_url')))
        if not data.get('content'):
            self.log.debug('null {}'.format(data.get('article_url')))
        self.items_list.append(data)
        if self.counts % 10 == 0:
            self.log.info("have stored items count:{}".format(self.counts))
        if len(self.items_list) % 10 == 0:
            if not self.debug:
                self.log.info("col name: {}".format(self.collection_name))
                insert_operations = []
                for item in self.items_list:
                    op = InsertOne(item)
                    insert_operations.append(op)
                while True:
                    try:
                        self.db.db[self.collection_name].bulk_write(insert_operations, ordered=False)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []
            else:
                update_operations = []
                for item in self.items_list:
                    key_field = item.get(self.key_field)
                    key_field_2 = item.get(self.key_field_2)
                    op = UpdateOne({self.key_field: key_field, self.key_field_2: key_field_2}, {'$set': item}, upsert=True)
                    update_operations.append(op)
                while True:
                    try:
                        self.db.db[self.collection_name].bulk_write(update_operations, ordered=False)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []

    def upload_es(self, data):
        self.counts += 1
        for k, v in data.items():
            self.log.debug("{}: {}".format(k, v))
        if not data.get('project_title'):
            self.log.debug('null {}'.format(data.get('article_url')))
        if not data.get('content'):
            self.log.debug('null {}'.format(data.get('article_url')))
        self.items_list.append(data)
        if self.counts % 10 == 0:
            self.log.info("sending counts:{} ...".format(self.counts))
        if len(self.items_list) % 10 == 0:
            if not self.debug:
                self.log.info("col name: {}".format(self.collection_name))
                insert_operations = []
                for item in self.items_list:
                    insert_operations.append(item)
                while True:
                    try:
                        helpers.bulk(self.es, insert_operations, index=self.es_index, raise_on_error=True)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []
            else:
                update_operations = []
                for item in self.items_list:
                    update_operations.append(item)
                while True:
                    try:
                        helpers.bulk(self.es, update_operations, index=self.es_index, raise_on_error=True)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []

    def check_upload_es(self):
        if self.items_list:
            if not self.debug:
                insert_operations = []
                for item in self.items_list:
                    insert_operations.append(item)
                while True:
                    try:
                        helpers.bulk(self.es, insert_operations, index=self.es_index, raise_on_error=True)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []
            else:
                update_operations = []
                for item in self.items_list:
                    update_operations.append(item)
                while True:
                    try:
                        helpers.bulk(self.es, update_operations, index=self.es_index, raise_on_error=True)
                        break
                    except Exception as e:
                        self.log.exception(e)
                        time.sleep(10)
                self.log.info("update db counts: {} done".format(self.counts))
                self.items_list = []

    def get_proxy(self, proxy_type="base"):
        if proxy_type == "base":
            return self.get_xxdl()
        return self.get_xxdl()

    def get_xxdl(self):
        max_retry = 5
        retry_counts = 0
        proxy_dict = {}
        while retry_counts < max_retry:
            retry_counts += 1
            time.sleep(0.01)
            try:
                p = Proxies()
                proxy_dict = p.get_proxy()
            except Exception as e:
                self.log.error("get proxies failed {}".format(e))

            return proxy_dict

    @retry(reraise=True, stop=stop_after_attempt(10), wait=wait_fixed(2))
    def req(self, url, req_type="get", rsp_type="content", anti_word="", encoding=True, req_again=False, **kwargs):
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60
        if 'https' in url and not kwargs.get("verify"):
            kwargs["verify"] = False
        session = requests.session()
        if kwargs.get("headers"):
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        else:
            kwargs["headers"] = {}
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        if self.proxy_flag:
            proxies = self.get_proxy()
            kwargs['proxies'] = proxies  # 更换代理
            # session.proxies = proxies
        try:
            if req_type == "get":
                response = session.get(url, **kwargs)
                if encoding:
                    response.encoding = 'utf8'
            elif req_type == "post":
                response = session.post(url, **kwargs)
            else:
                self.log.error(f"error req_type: {req_type}")
                self.log.error(url)
                raise Exception
            if req_again:
                cookies = response.cookies
                self.cookies = ''
                for k, v in cookies.items():
                    self.cookies += "{}={};".format(k, v)
                kwargs['headers']['cookie'] = self.cookies
                if req_type == "get":
                    response = session.get(url, **kwargs)
                elif req_type == "post":
                    response = session.post(url, **kwargs)
                kwargs['headers'].pop('cookie')
        except Exception as e:
            self.log.error(url)
            self.log.exception(e)
            raise Exception
        if not response or response.status_code not in (200, 302):
            self.log.error(f"error response, {response.status_code}")
            self.log.error(url)
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

if __name__ == "__main__":
    bid = Bid()
    time_str = '开始：2022-01-02 17:30'
    ts = bid.format_time(time_str)
    print(ts)