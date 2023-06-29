#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2023/1/10 16:40
@Author: CZC
@File: sch.py
"""
site = "bid"

status = True

# 分 时 日 月 星期
cron = "30 1 * * *"

cmd = [
    "python guangdongnengyuan_gongcheng.py",
    "python guangdongnengyuan_wuzi.py",
    "python guangdongnengyuan_yiwancheng.py",
    "python guangdongnengyuan_zhaobiao.py",
    "python guangdongnengyuan_zhongbiao.py",
]
