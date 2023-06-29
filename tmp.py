#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/5/28 3:57 下午
@Author: CZC
@File: tmp.py
"""
# pip install esmre-0.5.2
import re

from esmre import esm


def esm_test():
    index = esm.Index()
    index.enter("宝马")
    index.enter("马")
    index.enter("奔驰")
    index.enter("保时捷")
    index.fix()

    target = "哎呀，今天在楼下看到了宝马，我老家倒是有养马的，以前的邻居有个奔驰，不对是保时捷，大爷的，都是马"
    res = dict(map(lambda t: (t[1], t[0]), index.query(target)))
    print(res)


def es_connect():
    # 推荐使用  elasticsearch  需要注意版本问题
    from elasticsearch import Elasticsearch
    host = '120.196.62.61'
    port = '9200'
    es_index = 'mongo_to_es'
    es_header = [{'host': host, 'port': port, 'verify_certs': False}]
    es_header = [{'host': host, 'port': port}]
    client = Elasticsearch(es_header)
    print(client.info)  # es信息
    # 创建索引
    query = {'query': {'match_all': {}}, "size": 1000}
    all_doc = client.search(index='mongo_to_es', body=query)
    print(all_doc)
    results = all_doc.get("hits", {}).get("hits", {})
    for item in results:
        doc_id = item["_id"]
        client.delete(index=es_index, doc_type=es_index, id=doc_id)
    allDoc = client.search(index='mongo_to_es', body=query)
    result = client.indices.create(index='mongo_to_es')
    print(result)
    # 删除索引
    result = client.indices.delete(index='user')
    print(result)
    # 更新数据  必须的用
    '''
    不用doc包裹会报错
    ActionRequestValidationException[Validation Failed: 1: script or doc is missing
    '''
    data = {'doc': {'userid': '1', 'username': 'lqz', 'password': '123ee', 'test': 'test'}}
    result = client.update(index='news', doc_type='_doc', body=data, id=1)
    print(result)
    # 删除数据
    result = client.delete
    print(result)

    # 查询           查询 原生咋查，这里就可以咋用
    # 查找所有文档
    query = {'query': {'match_all': {}}}
    #  查找名字叫做lxx的所有文档
    query = {'query': {'term': {'name': 'lxx'}}}
    # 查找年龄大于11的所有文档
    query = {'query': {'range': {'price': {'gt': 100}}}}
    allDoc = client.search(index='books', body=query)
    print(allDoc)


if __name__ == '__main__':
    es_connect()