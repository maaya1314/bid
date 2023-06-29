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
    "python nanfangdianwang_fuwu_gongshi.py",
    "python nanfangdianwang_fuwu_zhaobiao.py",
    "python nanfangdianwang_gongcheng_gongshi.py",
    "python nanfangdianwang_gongcheng_zhaobiao.py",
    "python nanfangdianwang_huowu_gongshi.py",
    "python nanfangdianwang_huowu_zhaobiao.py",
]
