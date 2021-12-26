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
from pymongo import UpdateOne, InsertOne
import requests
from lxml import etree
from tenacity import retry, stop_after_attempt, wait_fixed

from bid_tools.loghandler import getLogger
import pandas as pd
from openpyxl import load_workbook
from bid_tools.connectdb import MongoDB, TestDB
import atexit


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
        self._in_work()

    def _in_work(self):
        self.db = MongoDB(TestDB)
        if not self.debug:
            self.collection_name = self.true_collection_name
        else:
            indexs = self.db.db[self.collection_name].index_information()
            index_name = "{}_-1_{}-1".format(self.key_field, self.key_field_2)
            if index_name not in indexs:
                self.db.db[self.collection_name].create_index([(self.key_field, -1), (self.key_field_2, -1)], unique=True)

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
        self.check_upload_db()

    def run(self, keyword):
        self.keyword = keyword

    def format_time(self, time_str):
        try:
            time_str = datetime.datetime.strptime(time_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            return time_str
        except:
            pass
        try:
            findall = re.findall("[0-9-: /年月日时分秒]+", time_str)
            extract_time = findall[0].strip()
        except:
            return ""
        try:
            format_time = datetime.datetime.strptime(extract_time, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
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
        return ""

    def detail_parse(self, detail_content, detail_url, data=None):
        if not data:
            data = {}
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
                        v = re.sub("<.*?>", "", v).replace("\r", "").replace("\n", "").replace('&nbsp;', '').strip()
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
                                data[key] += temp_result.replace("\r", "").replace("\n", "").strip()
                    elif isinstance(x_xpath_value, str):
                        temp_result = x_xpath_value
                        if temp_result:
                            data[key] = temp_result.replace("\r", "").replace("\n", "").strip()
                            break

                except:
                    data[key] = ""

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

        attachment_url = data.get("attachment_url")
        if attachment_url:
            attachment_url = attachment_url if attachment_url.startswith('http') else 'http:' + attachment_url
            data['attachment_url'] = attachment_url

        phone = data.get("phone")
        if phone:
            phone_list = re.findall(r'\d[a-zA-Z0-9\-、－—\转\(\)（）]{1,}', phone)
            phone = phone if not phone_list else phone_list[0]
            data["phone"] = phone

        tender_price = data.get("tender_price")
        if tender_price:
            price_list = re.findall("([0-9\.]{1,})", tender_price)
            if price_list:
                if '万' in tender_price or '万元' in detail_content:
                    new_tender_price = "{}元".format(float(price_list[0]) * 10000)
                else:
                    new_tender_price = "{}元".format(price_list[0])
            else:
                new_tender_price = ""
            data['tender_price'] = new_tender_price

        win_bid_price = data.get("win_bid_price")
        if win_bid_price:
            price_list = re.findall("([0-9\.]{1,})", win_bid_price)
            if price_list:
                if '万' in win_bid_price:
                    new_win_bid_price = "{}元".format(float(price_list[0]) * 10000)
                else:
                    new_win_bid_price = "{}元".format(price_list[0])
            else:
                new_win_bid_price = ""
            data['win_bid_price'] = new_win_bid_price

        project_leader = data.get("project_leader")
        if project_leader:
            project_leader = project_leader.replace("  ", "").strip()
            data['project_leader'] = project_leader

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

    def upload(self, data, output_type="db"):
        if output_type == 'db':
            self.upload_db(data)
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
        self.items_list.append(data)
        if self.counts % 10 == 0:
            self.log.info("have stored items count:{}".format(self.counts))
        if len(self.items_list) % 10 == 0:
            if not self.debug:
                insert_operations = []
                for item in self.items_list:
                    op = InsertOne(item)
                    insert_operations.append(op)
                self.db.db[self.collection_name].bulk_write(insert_operations, ordered=False)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []
            else:
                update_operations = []
                for item in self.items_list:
                    key_field = item.get(self.key_field)
                    key_field_2 = item.get(self.key_field_2)
                    op = UpdateOne({self.key_field: key_field, self.key_field_2: key_field_2}, {'$set': item}, upsert=True)
                    update_operations.append(op)
                self.db.db[self.collection_name].bulk_write(update_operations, ordered=False)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []

    def check_upload_db(self):
        if self.items_list:
            if not self.debug:
                insert_operations = []
                for item in self.items_list:
                    op = InsertOne(item)
                    insert_operations.append(op)
                self.db.db[self.collection_name].bulk_write(insert_operations, ordered=False)
                self.log.info("write db counts: {} done".format(self.counts))
                self.items_list = []
            else:
                update_operations = []
                for item in self.items_list:
                    key_field = item.get(self.key_field)
                    key_field_2 = item.get(self.key_field_2)
                    op = UpdateOne({self.key_field: key_field, self.key_field_2: key_field_2}, {'$set': item}, upsert=True)
                    update_operations.append(op)
                self.db.db[self.collection_name].bulk_write(update_operations, ordered=False)
                self.log.info("update db counts: {} done".format(self.counts))
                self.items_list = []

    def get_proxy(self):
        params = {
            'taskId': 'out_team',
            'supplierCode': 'uuhttp',
            'token': '81bd5a5b-3aca-40ac-a085-9d659d40309b'  # 更改token参数。
        }
        res = requests.get('http://rs.ip.skieer.com/api/v1/proxy/get', params=params, timeout=20)
        if res.status_code != 200:
            raise Exception('获取代理失败')
        content = json.loads(res.content)
        data = content['data'][0] if len(content['data']) > 0 else {}
        if not data:
            raise Exception('获取代理失败')
        host = data['host']
        port = data['port']
        proxies = {"http": "http://{}:{}".format(host, port), "https": f"http://{host}:{port}"}
        return proxies

    @retry(reraise=True, stop=stop_after_attempt(10), wait=wait_fixed(2))
    def req(self, url, req_type="get", rsp_type="content", anti_word="", encoding=True, **kwargs):
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