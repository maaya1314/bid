#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: CZC
@File: connectdb.py
"""
import datetime
import sys
import pymongo
from bid_tools.loghandler import getLogger
from pymongo.errors import WriteError
logger = getLogger(__name__, console_out=True, level="debug")


class TestDB(object):
    MONGODB_SERVER = "mdb.dataservice.skieer.com"
    MONGODB_PORT = 8011
    MONGODB_DB = "grgtest"
    MONGO_USER = "grgtest"
    MONGO_PSW = "d&1wsxec1*"


class BidAppDB(object):
    MONGODB_SERVER = "125.88.221.92"
    MONGODB_PORT = 6601
    MONGODB_DB = "bid"
    authSource = True
    MONGO_USER = "work"
    MONGO_PSW = "Gg82RG6k5D"



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
        self.client = pymongo.MongoClient(mongo_url)
        # self.client = pymongo.MongoClient(mongodb.MONGODB_SERVER, mongodb.MONGODB_PORT)
        self.db = self.client[mongodb.MONGODB_DB]
        # self.db.authenticate(mongodb.MONGO_USER, mongodb.MONGO_PSW)
        # self.collection = db[mongodb.MONGODB_COLLECTION]

        # 建立索引
        # self.collection.ensure_index([("_utime", pymongo.ASCENDING)])
        # self.collection.ensure_index([("_in_time", pymongo.ASCENDING)])
        # self.collection.ensure_index([("_record_id", pymongo.ASCENDING)])

    def __del__(self):
        self.client.close()

    def find_data(self, value, collection, query_name=None):
        coll = self.db[collection]
        if not query_name:
            query_name = '_id'
        cursor = coll.find({query_name: value}, no_cursor_timeout=True)
        data_list = list(cursor)
        if data_list:
            return True
        return False

    def insert_item(self, collection, value, doc=None):
        coll = self.db[collection]
        _in_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # coll.insert({'_id': value})
        if not doc:
            coll.update_one({'_id': value}, {'$set': {'_id': value, '_in_time': _in_time}}, upsert=True)
        else:
            if not isinstance(doc, dict):
                return
            doc['_in_time'] = _in_time
            coll.update_one({'_id': value}, {'$set': doc}, upsert=True)

    def get_company(self, collection, query=None):
        if not query:
            query = {}
        coll = self.db[collection]
        cursor = coll.find(query, no_cursor_timeout=True)
        for doc in cursor:
            keyword = '{}'.format(doc.get('_id'))
            yield keyword

    def get_keyword(self, province, collection):
        coll = self.db[collection]
        cursor = coll.find({}, no_cursor_timeout=True)
        for doc in cursor:
            keyword = '{}{}'.format(province, doc.get('_id'))
            yield keyword

    def insert_items(self, items, collection):
        collection = self.db[collection]
        for item in items:
            if not item:
                continue

            logger.info(item)
            cursor = collection.find({'_record_id': item['_record_id']})
            cursor = list(cursor)
            if cursor:
                if item.get('_in_time'):
                    del item['_in_time']
                collection.update({'_record_id': item['_record_id']}, {'$set': dict(item)}, upsert=True)
            else:
                collection.insert(dict(item))

    def insert_batch_data(self, collection, data_list, update_item=None, is_order=False, insert=False):
        count = 0
        if data_list is None:
            return count

        length = len(data_list)
        if length <= 0:
            return count


        try:
            bulk = self.db[collection].initialize_ordered_bulk_op() if is_order else self.db[collection].initialize_unordered_bulk_op()
            for item in data_list:
                if update_item:
                    item = update_item
                if insert:
                    bulk.insert(item)
                else:
                    _id = item.get('_id')
                    bulk.find({'_id': _id}).upsert().update({'$set': item})
                count += 1
            bulk.execute({'w': 0})
            if not update_item:
                logger.info('insert_logs: {length}'.format(length=len(data_list)))
        except WriteError as e:
            logger.error('mongo写入异常:')
            logger.exception(e)
            sys.exit(1)
        except Exception as e:
            logger.error("mongo操作异常: ")
            logger.exception(e)
            raise e
        return count
