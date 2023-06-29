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
cron = "30 2 * * *"

cmd = [
    "python zhaocaiyun_biangeng.py",
    "python zhaocaiyun_liubiaogonggao.py",
    "python zhaocaiyun_zhaobiao.py",
    "python zhaocaiyun_zhongbiaogonggao.py",
    "python zhaocaiyun_zhongbiaogongshi.py",
]
