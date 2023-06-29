#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
这个是模板配置文件,使用的时候复制一份命名为m_settings.py
切记不要上传m_settions.py
"""
import os

from pymongo import MongoClient


CAPTCHA_HOST = "http://172.18.180.225:9820/cap_ocr"

PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGDIR = os.path.join(PROJECTDIR, "logs")

LOCAL_FILE_BASE_DIR = os.path.join(PROJECTDIR, "data")
