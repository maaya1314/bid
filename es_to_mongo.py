#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2021/12/13 7:03 下午
@Author: CZC
@File: es_to_mongo.py
"""
import sys
import time
from logging.handlers import RotatingFileHandler
from threading import Thread

import pymongo
from elasticsearch import Elasticsearch
from pymongo import InsertOne

sys.path.append("..")
import logging
import os

PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGDIR = os.path.join(PROJECTDIR, "logs")


# 每一个task实例一个logger
def getLogger(task_name="root", level=logging.INFO, console_out=False):
    logger = logging.getLogger(task_name)
    if isinstance(level, str):
        level = level.lower()
    if level == "debug":
        level = logging.DEBUG
    elif level == "info":
        level = logging.INFO
    elif level == "warning":
        level = logging.WARNING
    elif level == "error":
        level = logging.ERROR
    else:
        level = logging.INFO

    if not os.path.exists(LOGDIR):
        os.makedirs(LOGDIR)
    LOG_FILE = LOGDIR + "/%s.log" % task_name
    fmt = "%(asctime)s - %(filename)s[line:%(lineno)d] %(levelname)s - %(message)s"
    formatter = logging.Formatter(fmt)
    #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        handler = RotatingFileHandler(LOG_FILE, maxBytes=64 * 1024 * 1025, backupCount=5)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        if console_out is True:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter(fmt)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
    logger.setLevel(level)
    return logger


class GrgDB(object):
    MONGODB_SERVER = "172.19.0.22"
    MONGODB_PORT = 27017
    MONGODB_DB = "grgtest"
    MONGO_USER = ""
    MONGO_PSW = ""


class MongoDB(object):
    def __init__(self, mongodb):
        if hasattr(mongodb, 'authSource'):
            authSource = 'admin'
        else:
            authSource = mongodb.MONGODB_DB
        mongo_url = 'mongodb://{0}:{1}@{2}:{3}/?authSource={4}&authMechanism=SCRAM-SHA-1'.format(mongodb.MONGO_USER,
                                                                                                 mongodb.MONGO_PSW,
                                                                                                 mongodb.MONGODB_SERVER,
                                                                                                 mongodb.MONGODB_PORT,
                                                                                                 authSource)
        if not mongodb.MONGO_USER:
            mongo_url = 'mongodb://{0}:{1}/?authSource={2}&authMechanism=SCRAM-SHA-1'.format(mongodb.MONGODB_SERVER,
                                                                                             mongodb.MONGODB_PORT,
                                                                                             authSource)
        self.client = pymongo.MongoClient(mongo_url)
        # self.client = pymongo.MongoClient(mongodb.MONGODB_SERVER, mongodb.MONGODB_PORT)
        self.db = self.client[mongodb.MONGODB_DB]

    def __del__(self):
        self.client.close()


class EsToMongo(object):
    def __init__(self, debug=True):
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.columns_list = []
        self.file_name = sys.argv[0].split("/")[-1].replace(".py", "")
        self.time_sleep = ()
        self.parse_dict = ""
        self.items_list = []
        self.counts = 0
        self.collection_name = 'guangdian'
        self.key_field = "article_url"
        self.key_field_2 = "keyword"
        self.debug = debug
        self.es_index = 'mongo_to_es'
        self.scan_running = True
        self.scan_thread = Thread(target=self.run)
        self.scan_thread.daemon = True
        self._in_work()

    def _in_work(self):
        self.db = MongoDB(GrgDB)
        # host = '120.196.62.61'
        host = '127.0.0.1'
        port = '9200'
        es_header = [{'host': host, 'port': port, 'verify_certs': False}]
        self.es = Elasticsearch(es_header)

    def run(self):
        query = {'query': {'match_all': {}}, "size": 5000}
        while self.scan_running:
            try:
                all_doc = self.es.search(index=self.es_index, body=query)
                results = all_doc.get("hits", {}).get("hits", {})
                for item in results:
                    doc = item.get("_source")
                    self.upload_db(doc)
                    doc_id = item["_id"]
                    self.es.delete(index=self.es_index, doc_type=self.es_index, id=doc_id)
                # self.es.delete_by_query(index=self.es_index, body=query, doc_type=self.es_index)
                self.check_upload_db()

            except Exception as e:
                self.log.exception(e)
            time.sleep(60)

    def start(self):
        self.scan_running = True
        self.scan_thread.start()
        while self.scan_running:
            time.sleep(1)

    def upload_db(self, data):
        self.counts += 1
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

    def check_upload_db(self):
        if self.items_list:
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


if __name__ == "__main__":
    etm = EsToMongo()
    etm.start()
