#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/5/28 2:34 下午
@Author: CZC
@File: utils.py
"""
import hashlib
import re


def re_find_one(pattern, string):
    try:
        datas = re.findall(pattern, string)
        return datas[0]
    except:
        return ""


def get_md5(string):
    m2 = hashlib.md5()
    m2.update(string.encode())
    return m2.hexdigest()
