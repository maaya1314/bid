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
cron = "0 2 * * *"

cmd = [
    "python yangguangcaigou_gongchengzhaobiao.py.py",
    "python yangguangcaigou_wuzizhaobiao.py.py",

]
