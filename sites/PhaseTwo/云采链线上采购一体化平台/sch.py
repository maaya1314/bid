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
cron = "15 0 * * *"

cmd = [
    "python yuncailian_diaoyan.py",
    "python yuncailian_jingjia.py",
]
