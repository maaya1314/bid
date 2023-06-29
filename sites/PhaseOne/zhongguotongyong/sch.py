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
cron = "41 19 * * *"

cmd = [
    "python zhongguotongyong_biangeng.py",
    "python zhongguotongyong_jieguogonggao.py",
    "python zhongguotongyong_zhaobiao.py",
    "python zhongguotongyong_zige.py",
]
