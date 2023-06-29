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
    "python zhaoshangju_caigou.py",
    "python zhaoshangju_pingbiaojieguo.py",
    "python zhaoshangju_xiangmujiegou.py",
    "python zhaoshangju_xiangmuzhongzhi.py",
    "python zhaoshangju_youxiaotoubiao.py",
]
