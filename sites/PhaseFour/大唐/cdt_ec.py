#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re

# import execjs
import fitz
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree

from libs.base import TaskBase
from sites.PhaseFour.大唐.libs import util
from sites.PhaseFour.大唐.libs.util import re_find_one

sys.path.append('../../PhaseTwo')
sys.path.append('../../..')
sys.path.append('../../../..')
# from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
# from bid_6 import Bid6
# from bid_conf.conf_6 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright

import jsonpath
import math


base_dict = {
    # "scale": {
    #     "re": [''],
    #     "xpath": [
    #         "//*[string()='结构类型及规模']/following-sibling::*[1]",
    #         "//*[string()='项目规模']/following-sibling::*[1]",
    #
    #     ],
    # },
    # "project_title": {
    #     "re": [''],
    #     "xpath": [
    #         "//div[@class='v3-notice-detail-left-title']",  # 云采招阳
    #         "//div[@class='article-title']",  # 中煤
    #         "//h1[@class='s-title']",  # 中国南方电网--阳光电子商务
    #         "//div[@class='headline']/dl/dt",
    #         'string(//h3)',  # 光大
    #         "//div[@class='app']/h2",  # 中招
    #     ]
    # },  # 项目标题
    # "project_number": {
    #     "re": [
    #         '询价编号：(.+?)<',
    #         '采购单编号：(.+?)<',
    #         '标段（包）编号：(.+?)<',
    #         '项目编号：(.+?)</p',
    #         '招标编号：(.+?)</span></p>',
    #         '编号：((?!\<).+?)<',
    #         '编号：([\s\S]+?)(?!<[\s\S]*?>)(采购)?项目名称',
    #         '编号：(.+?)(?=）|\))',
    #         '采购编号：(.+?)）',
    #         '采购编号：(.+?)</span',
    #         '招标编号：(.+?)</span></span>',
    #         '编号：(.+?)</span>',
    #         '项目编号：(.+?)<',
    #         '招标编号<a></a>：<span style="text-decoration:underline;">（(.*?)）',
    #         '项目标号：(.+?)<',
    #     ],
    #     "xpath": [
    #         "//h5/@title",
    #         "//*[string()='采购项目编码']/following-sibling::*[1]",
    #         "//span[contains(text(),'项目编号')]/following-sibling::span[1]",
    #         "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
    #         "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
    #         "//span[contains(text(),'采购项目编号')]/..",
    #         "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]",
    #         '//td[contains(string(), "招标编号")]/../following::*[1]//td[count(//td[contains(string(), "招标编号")]/preceding-sibling::*) + 1]',
    #     ]
    # },  # 项目编号
    # "tender_unit": {
    #     "re": [
    #         '招 标 人：(.+?)<',
    #         '招标人[：|为](.*?)</span>',
    #         '招标人名称：(.+?)</span></p>',
    #         '招标人名称：(.+?)<',
    #         '招标人[：|为](.+?)</span></span>',
    #         '招标人：(.*?)</span>',
    #         '采 购.*?人：(.+?)</span>',
    #         '采购机构：(.+?)</span>',
    #         '招标人或其招标代理机构名称：(.+?)</span></span>',
    #         '招标人或其招标代理机构名称：(.+?)</span>',
    #         '采购组织：(.+?)<',
    #     ],
    #     "xpath": [
    #         "string(//span[text()='招标人：']/following-sibling::*[1])",
    #         'string(//span[contains(string(), "招标人：")]/following-sibling::*)',
    #         "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
    #         "//span[contains(string(),'招标人：')]",
    #         "//span[contains(string(),'采 购 人：')]",
    #         "//span[contains(string(),'采购人：')]",
    #         "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
    #     ]
    # },  # 招标单位
    # "tender_price": {
    #     "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
    #     "xpath": [
    #         '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
    # },  # 标的金额
    # "publish_time": {
    #     "re": [''],
    #     "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
    # },  # 发布时间 需正则两步以上
    # "project_leader": {
    #     "re": [
    #         '联 系 人：(.+?)<',
    #         '联系方式：[\s\S]*?联系人：(.+?)</p',
    #         '招标采购中心联系人：(.+?)电话',
    #         '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
    #         '（签名）：(.+?)</span>',
    #         '主要负责人或授权的项目负责人：(.+?)</span>',
    #     ],
    #     "xpath": [
    #         'string(//*[text()="项目联系人："]/following-sibling::*)',
    #         'string(//*[text()="联系人："]/following-sibling::*)',
    #         'string(//th[contains(string(), "联系人")]/following-sibling::*)',
    #         '//span[contains(string(), "联 系 人：")]/following::*[1]',
    #         '//span[contains(string(), "联 系 人：")]/following-sibling::*',
    #         'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
    #         'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
    #         "string(//span[contains(string(),'联 系 人：')])",
    #         "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
    #         # "string(//span[contains(string(),'联系人：')])",
    #     ]
    # },  # 招标项目负责人 需正则两步以上
    # "phone": {
    #     "re": [
    #         '电<.*?>话：(.+?)</p',
    #         '联系方式[\s\S]*?电话：([\s\S]*?)</p',
    #         '联系方式[\s\S]*?联系人[\s\S]*?电话：(.+?)</p',
    #         '联系方式：[\s\S]*?电话：(.+?)</p',
    #         '电.?话：(.+?)<',
    #         '联系方式：(.+?)</p',
    #     ],
    #     "xpath": [
    #         'string(//*[text()="联系电话："]/following-sibling::*)',
    #         'string(//*[text()="手机号码："]/following-sibling::*)',
    #         'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
    #         'string(//th[contains(string(), "联系电话")]/following-sibling::*)',
    #         '//span[contains(string(), "电 话：")]/following::*[1]', '//p[contains(string(), "电 话：")]',
    #         "//span[contains(string(),'联系电话：')]/following-sibling::*",
    #         "//td[contains(string(),'联系电话：')]/following-sibling::*[1]",
    #         "//span[contains(text(),'电  话')]",
    #         'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系电话：")])',
    #         "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
    #         "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
    #         "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
    #         "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
    #         "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
    #         "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
    #         "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
    # },  # 联系电话
    # "project_location": {
    #     "re": [
    #         '招标项目所在地区：(.+?)\s'
    #     ],
    #     "xpath": ['']
    # },  # 项目所在地
    # "industry_type": {
    #     "re": [''],
    #     "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
    # },  # 项目行业类型
    # "article_url": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 文章URL
    # "source": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 信息来源
    # "content": {
    #     "re": [''],
    #     "xpath": [
    #         "//div[@id='printHtml']",  # 元博网
    #         "//section[@id='divContent']",  # 孚日
    #         "//textarea",  # 海尔
    #         "//div[@class='detail_box qst_box']",  # 中国华能
    #         "//div[@class='container pt-2 pb-5']",  # 四川五洲
    #         "//div[@class='detail__content content-mode-left']",  # 广东省网上超市
    #         "//div[@class='contain-main']/div[@class='er-main']/div[@class='er-container']",  # 雄安
    #         "//div[@class='v3-notice-detail-box']",  # 云采招阳
    #         "//div[@class='main-text']",  # 中煤
    #         "//div[@class='form-content']",  # 中国海洋石油集团有限公司
    #         "//div[@class='main-text']",  # 航空工业电子采购平台
    #         "//div[@class='article-area']",  # 中国海洋石油集团有限公司
    #         "//div[@class='liststyle']",  # 大唐集团电子商务平台
    #         "//div[@id='moreall-gg']",  # 大唐集团电子商务平台
    #         "//div[@class='wrap']",  # 中招联合招标采购平台
    #         "//section[@class='article']",  # 西电集团电子采购平台
    #         "//div[@id='ninfo-con-txt']",  # 深圳市国际招标有限公司
    #         "//div[@class='neirong']",  # 中国一汽电子招标采购交易平台
    #         "//div[@class='main_top main_top_CG']",   # 中国华电集团电子商务平台
    #         "//div[@class='WordSection1']",  # 中招联合招标采购平台
    #         "//div[@class='dg-notice-detail']",  # 国家开发投资公司电子采购平台
    #         # "//div[@class='ewb-article-info']/table",  # 深圳市政府采网
    #         "//div[@class='ewb-article-info']/div[@class='body']",  # 深圳市政府采网
    #         # "//div[@class='ewb-article-info']//tbody",
    #         "//div[@class='ewb-article-info']",  # 深圳市政府采网
    #         "//div[@id='container']/div[@id='main']/div[@class='block'][1]|//div[@id='container']/div[@id='sidebar']/ul/div[@class='timeline']/div[@class='dotbox']",  # 光大环境招标采购电子交易平台
    #         "//div[@id='container']",  # 大唐集团电子商务平台
    #         "//div[@class='block'][1]|//div[@id='container']/div[@id='sidebar']/ul|//div[@class='ZhongBiaoContent']/ul",  # 光大环境招标采购电子交易平台
    #         "//div[@class='notice-content-left']",   # 云采链线上采购一体化平台
    #         # "//div[@class='content-header-wrapper']",  # 云采链线上采购一体化平台
    #         "//div[@class='Section0']",  # 国义
    #         "//div[@class='Section1']",
    #         "string(.)",
    #         "//p",
    #         "//td[@class='text_zx']",
    #         "//tr[@class='firstRow']/td",
    #     ]
    # },  # 正文
    # "bid_finish_time": {
    #     "re": [
    #         '报名时间[\s\S]*?开始：(.+?)<',
    #         '开标时间[\s\S]{,10}开始：(.+?)<',
    #         '开标时间变更为(.+?)(?=上午|下午)',
    #         '开标时间：(.+?)(?=上午|下午)',
    #         '开标时间：(.+?)</span></p>',
    #     ],
    #     "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
    #               "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
    #               "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
    #               "//span[contains(text(),'开标时间：')]",
    #               "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
    # },  # 开标时间
    # "bid_end_time": {
    #     "re": [
    #         '投标时间[\s\S]*?结束：(.+?)<',
    #         '投标时间[\s\S]{,10}结束：(.+?)<',
    #         '延期开标：(.+?)<',
    #         '现变更为.{,6}投标文件递交截止时间：(.+?)(?=（|<)',
    #         '投标文件递交截止时间：(.+?)(?=（|<)',
    #         '递交截止时间：(.+?)<',
    #         '截止时间：(.+?)<',
    #     ],
    #     "xpath": [
    #         "//span[contains(text(),'投标截止及开标时间')]",
    #         "//span[text()='投标文件开始递交时间：']/..",
    #         '//th[contains(string(), "投标文件递交截止时间")]/../following::*[1]//td[count(//th[contains(string(), "投标文件递交截止时间")]/preceding-sibling::*) + 1]',
    #     ]
    # },  # 投标截止时间

    "项目概况": {
        "re": [
            '项目概况与招标范围：([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '项目概况与招标范围:([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '项目概况与采购范围：([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '项目概况与采购范围:([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '(项目概况和招标范围[\s\S]+?)投标人资格要求',
            '(项目概况与招标范围[\s\S]+?)投标人资格要求',
            '(项目概况[\s\S]+?)投标人资格要求',
            '项目概况([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '(项目概况与招标范围：[\s\S]+?)\n',
            '(项目概况：[\s\S]+?)\n',
            '概况：([\s\S]*?)（二）',
            # '概况：([\s\S]*?)</p>',
            '(项目概况[\s\S]*?)\n',
        ],

        "xpath": [
            "//span[text()='项目概况：']/following-sibling::*[1]",
            "//label[text()=' 项目概况：']/following-sibling::*[1]",
            # "//span[contains(text(),'项目概况')]",
        ]
    },  # 项目概况
    "投标人资格要求": {
        "re": [
            '投标人的资格要求：([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '投标人资格要求：([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '供应商资格条件([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '资质要求([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '具备下列条件([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '投标人资格要求(.+?)(?=2\. |3\. |4\. |5\. |6\. |7\. |8\. |9\. )',
            '投标人资格要求(.+?)(?=2\.<|3\.<|4\.<|5\.<|6\.<|7\.<|8\.<|9\.<)',
            '投标人资格条件(.+?)(?=2、 |3、 |4、 |5、 |6、 |7、 |8、 |9、 )',
            '投标人资格条件(.+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '(资格要求：[\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '资格要求<.*?>：([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
            '投标人资格要求(.+?)<strong>',
            '主要商务要求[\s\S]{0,20}?更正为([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',

        ],
        "xpath": [
            "//*[string()='资质（资格）要求说明']/following-sibling::*[1]",
            "//label[text()=' 资格要求：']/following-sibling::*[1]",
            "//span[text()='供应商基本要求：']/following-sibling::*[1]|//span[text()='供应商资质要求：']/following-sibling::*[1]|//span[text()='供应商业绩要求：']/following-sibling::*[1]|//span[text()='供应商其他要求：']/following-sibling::*[1]",
            'string(//span[text()="供应商资质要求："]/following-sibling::*//a/@href)',
        ]
    },  # 投标人资格要求
    "投标文件的递交": {
        "re": [
            '投标文件的递交：([\s\S]+?)[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '投标文件的递交:([\s\S]+?)[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
        ],
        "xpath": []
    },  # 投标文件的递交
    "招标文件的领取": {
        "re": [
            '招标文件的获取：([\s\S]+?)[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '招标文件的获取:([\s\S]+?)[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
        ],
        "xpath": []
    },  # 招标文件的领取
    "招标条件": {
        "re": [
            '招标条件：([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
            '招标条件:([\s\S]+?)\n[汉字ma汉字|汉字ro汉字|汉字shi汉字]',
        ],
        "xpath": []
    },  # 招标条件
    "招标范围": {
        "re": [
            '招标范围：([\s\S]+?)[汉字shi汉字|汉字ro汉字|汉字ma汉字]',
            '招标范围:([\s\S]+?)[汉字shi汉字|汉字ro汉字|汉字ma汉字]',
        ],
        "xpath": []
    },  # 招标范围
    "计划工期": {
        "re": [
            '计划工期：?([\s\S]+?)\n[汉字ma汉字|汉字ro汉字]',
            '计划工期:?([\s\S]+?)\n[汉字ma汉字|汉字ro汉字]',
            '计划工期：?([\s\S]+?)汉字shi汉字',
            '计划工期:?([\s\S]+?)汉字shi汉字',
            '交[货|付]期：([\s\S]+?)\n汉字ro汉字',
            '交[货|付]期:([\s\S]+?)\n汉字ro汉字',
            '交[货|付]期：([\s\S]+?)汉字shi汉字',
            '交[货|付]期:([\s\S]+?)汉字shi汉字',
            '供货期：([\s\S]+?)\n汉字ro汉字',
            '供货期:([\s\S]+?)\n汉字ro汉字',
            '供货期：([\s\S]+?)汉字shi汉字',
            '供货期:([\s\S]+?)汉字shi汉字',
            '计划服务工期：?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '计划服务工期:?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '计划服务工期：?([\s\S]+?)汉字shi汉字',
            '计划服务工期:?([\s\S]+?)汉字shi汉字',
            '服务期限：?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '服务期限:?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '服务期限：?([\s\S]+?)汉字shi汉字',
            '服务期限:?([\s\S]+?)汉字shi汉字',
            '协议期限：?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '协议期限:?([\s\S]+?)\n[汉字ro汉字|汉字ma汉字]',
            '协议期限：?([\s\S]+?)汉字shi汉字',
            '协议期限:?([\s\S]+?)汉字shi汉字',
            '服务期:([\s\S]+?)\n汉字ro汉字',
            '服务期[：|为]([\s\S]+?)汉字shi汉字',
            '服务期:([\s\S]+?)汉字shi汉字',
            '工期：?([\s\S]+?)[汉字shi汉字,汉字ro汉字,汉字ma汉字]',
            '完成时间：?([\s\S]+?)[汉字shi汉字,汉字ro汉字,汉字ma汉字]',
            '工期要求：([\s\S]+?)[汉字shi汉字,汉字ro汉字,汉字ma汉字]',
            '周期：([\s\S]+?)[汉字shi汉字,汉字ro汉字,汉字ma汉字]',
            '服务期要求：?([\s\S]+?)[汉字ro汉字,汉字shi汉字,汉字ma汉字]',
            '服务有效期：?([\s\S]+?)[汉字ro汉字,汉字shi汉字,汉字ma汉字]',
            '期限：?([\s\S]+?)[汉字ro汉字,汉字shi汉字,汉字ma汉字]',
        ],
        "xpath": [
            '//th[contains(string(), "工期")]/../following::*[1]//td[count(//th[contains(string(), "工期")]/preceding-sibling::*)]',
        ],
    },  # 计划工期
    "招标人": {
        "re": [
            '招标人：([\s\S]+?)\n汉字ro汉字',
            '招标人:([\s\S]+?)\n汉字ro汉字',
            '招标人\n：([\s\S]+?)\n汉字ro汉字',
            '招\n标\n人\n：\n([\s\S]+?)\n汉字ro汉字',
            '招标人：([\s\S]+?)\n汉字shi汉字',
            '招标人:([\s\S]+?)\n汉字shi汉字',
            '采购单位：([\s\S]+?)\n汉字ro汉字',
            '采购单位:([\s\S]+?)\n汉字ro汉字',
            '采购单位：([\s\S]+?)\n汉字shi汉字',
            '采购单位:([\s\S]+?)\n汉字shi汉字',
            '采购人：([\s\S]+?)\n汉字ro汉字',
            '采购人:([\s\S]+?)\n汉字ro汉字',
            '采购人：([\s\S]+?)\n汉字shi汉字',
            '采购人:([\s\S]+?)\n汉字shi汉字',
            '招标方：([\s\S]+?)\n汉字ro汉字',
            '招标方:([\s\S]+?)\n汉字ro汉字',
            '招标方：([\s\S]+?)\n汉字shi汉字',
            '招标方:([\s\S]+?)\n汉字shi汉字',
            '招 标 人：([\s\S]+?)\n',
            '招标人[：|为](.*?)\n',
            '招标人名称：([\s\S]+?)\n',
            '招标人[：|为]([\s\S]+?)\n',
            '招标人：(.*?)\n',
            '采 购.*?人：([\s\S]+?)\n',
            '采购机构：([\s\S]+?)\n',
            '招标人或其招标代理机构名称：([\s\S]+?)\n',
            '招标人或其招标代理机构名称：([\s\S]+?)\n',
            '采购组织：([\s\S]+?)\n',
        ],
        "xpath": [],
    },  # 招标人
    "招标代理": {
        "re": [
            '招标代理：([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]',
            '招标代理:([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]',
            '采购代理：?([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]'
            '采购代理机构：?([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]'
            '招标代理机构：([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]',
            '招标代理机构:([\s\S]+?)\n[汉字ro汉字, 汉字shi汉字]',
            '招标代理机构：([\s\S]+?)\n',
            '招标代理机构名称：([\s\S]+?)\n',
        ],
        "xpath": [],
    },  # 招标代理
    "联系电话": {
        "re": [
            '电<.*?>话：(.+?)</p',
            '联系方式[\s\S]*?电话：([\s\S]*?)</p',
            '联系方式[\s\S]*?联系人[\s\S]*?电话：(.+?)</p',
            '联系方式：[\s\S]*?电话：(.+?)</p',
            '电.?话：(.+?)<',
            '联系方式：(.+?)</p',
        ],
        "xpath": [
            'string(//*[text()="联系电话："]/following-sibling::*)',
            'string(//*[text()="手机号码："]/following-sibling::*)',
            'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
            'string(//th[contains(string(), "联系电话")]/following-sibling::*)',
            '//span[contains(string(), "电 话：")]/following::*[1]', '//p[contains(string(), "电 话：")]',
            "//span[contains(string(),'联系电话：')]/following-sibling::*",
            "//td[contains(string(),'联系电话：')]/following-sibling::*[1]",
            "//span[contains(text(),'电  话')]",
            'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系电话：")])',
            "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
            "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
            "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
            "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
            "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
            "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
            "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
    },  # 联系电话

    # "bid_winner": {
    #     "re": [
    #         '成交单位：(.+?)</span></p>',
    #         '成交单位：(.+?)</span></span>',
    #         '成交人名称：(.+?)</span>',
    #         '成交单位：(.+?)</span>',
    #         '成交供应商：(.+?)</p',
    #     ],
    #     "xpath": [
    #         '//td[string()="中标单位名称"]/../following::*[1]/td[count(//td[string()="中标单位名称"]/preceding-sibling::td) + 1]',
    #         '//*[text()="成交候选人名称："]/following-sibling::*',
    #         '//*[text()="中标人名称："]/following-sibling::*',
    #         "//*[text()='成交人名称：']/following-sibling::*[1]",
    #         'string(//span[contains(string(), "成交人：")]/following-sibling::*)',
    #         "//td[contains(string(), '中标人名称')]/../following::*[1]/td[count(//td[contains(string(), '中标人名称')]/preceding-sibling::td) + 1]",
    #         "//td[contains(string(), '成交供应商')]/../following::*[1]/td[count(//td[contains(string(), '成交供应商')]/preceding-sibling::td) + 1]",
    #         "//td[contains(string(), '中标候选人名称')]/../following::*[1]/td[count(//td[contains(string(), '中标候选人名称')]/preceding-sibling::td) + 1]",
    #         "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
    #         "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
    #         "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
    #         "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
    #     ]
    # },  # 中标人
    # "win_bid_price": {
    #     "re": [
    #         '最终报价（单价报价之和）：(.+?)。',
    #         '',
    #     ],
    #     "xpath": [
    #         "//*[text()='成交价(元)：']/following-sibling::*[1]",
    #         '//td[string()="中标价格"]/../following::*[1]/td[count(//td[string()="中标价格"]/preceding-sibling::td) + 1]',
    #         '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
    #         "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
    #     ]
    # },  # 中标金额
    # "win_bid_announcement_time": {
    #     "re": [
    #         '公告日期：(.+?)<',
    #     ],
    #     "xpath": [
    #         "//*[text()='公告开始时间：']/following-sibling::*[1]",
    #         "//*[text()='公示开始时间：']/following-sibling::*[1]",
    #
    #     ]
    # },  # 中标公告发布时间
    # "channel": {
    #     "re": [''],
    #     "xpath": ['//div[@class="home"]']
    # },  # 所属频道
    # "attachment_url": {
    #     "re": [
    #         'var pdf ="(.*?)"',
    #     ],
    #     "xpath": [
    #         # '//span[text()="附件下载："]/following-sibling::*//a/@href',
    #         # "//a[text()='下载']/@href",
    #         # "//a[text()='-点此下载-']/@href",
    #         # "//*[text()='下载']/parent::*/@href",
    #         # "//div[contains(text(), '附件') and contains(string(), 'docx')]//a/@href",
    #         # "//a[contains(text(), '附件') and (contains(text(), 'doc') or contains(text(), 'xls') or contains(text(), 'zip'))]/@href",
    #         # '//span[text()="附件1："]/following-sibling::*//@href',
    #
    #         # "//a[contains(string(),'下载')]/@href",
    #         # "//iframe[@id='pdfContainer']/@src",  # 光大
    #     ]
    # },  # 附件链接
    # "keyword": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 关键词
    # "harvested_time": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 采集时间
    # "spare_1": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 跟进记
    # "spare_2": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 跟进
    # "spare_3": {
    #     "re": [''],
    #     "xpath": ['']
    # },  # 预留字段3

}


parse_dict = {
    # "元博网-最新中标": base_dict,
    # "元博网-最新招标": base_dict,
    # "华能采购-招标公告": base_dict,
    # "华能采购-中标结果公告": base_dict,
    # '华电采购平台-招标公告':base_dict,
    '大唐招标-招标公告': base_dict
}

class BidZGDZ(TaskBase):
    def __init__(self, debug=True):
        super(BidZGDZ, self).__init__()
        # Bid6.__init__(self, debug)
        # self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '大唐招标-招标公告'
        # self.parse_dict = parse_dict.get(self.file_name)
        self.collection_name = 'cdt_ec'
        self.key_field = 'article_url'
        self.parse_dict = parse_dict.get(self.file_name)

    def get_cookies_and_content(self, url):
        # self.log.error("error response, url:{}".format(url))
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            context = browser.new_context()
            page = context.new_page()
            js = """
                Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
            """
            page.add_init_script(js)  # 执行规避webdriver检测
            page.goto(url)
            page.wait_for_load_state("networkidle")
            try:
                # 检测滑块，滑动滑块
                slider = page.locator('xpath=//span[@id="nc_1_n1z"]').bounding_box()
                page.mouse.move(x=slider['x'], y=slider['y'] + slider['height'] / 2)
                page.mouse.down()
                time.sleep(random.randint(3, 5))
                page.mouse.move(x=slider['x'] + random.randint(380, 420), y=slider['y'] + slider['height'] / 2)
                page.mouse.up()
                # page.reload()
                page.wait_for_load_state("networkidle")
                time.sleep(random.randint(3, 5))
            except Exception as e:
                pass
            storage_state = context.storage_state()
            cookie = ''
            for cookie_info in storage_state['cookies']:
                cookie_text = cookie_info['name'] + '=' + cookie_info['value']
                cookie += cookie_text + ';'
            self.headers['Cookie'] = cookie.rstrip(';')
            # Get_the_data(page.content())
            content = page.content()
            context.close()
            browser.close()
            return content

    @staticmethod
    def parsePDF(filePath):
        with fitz.open(filePath) as doc:
            text = ""
            for page in doc.pages():
                text += page.get_text()
            return text

    def run(self):
        TIMEOUT = 60
        url = "https://www.cdt-ec.com/notice/moreController/toMore?globleType=0&u_atoken=bd98cf7d-3271-4d10-bcd1-53985611740d&u_asession=01BuiPL1QWNmkRSCU_7-9jSqP7gZDlqZZTyXQW6Oymwkvr8f6KthKvfem1Pje0EaySX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K_k8_f1sFSkMCz8-3xLuHXW2l7GVvsUm1O1dQ3kAgydYmBkFo3NEHBv0PZUm6pbxQU&u_asig=05TLfL3h27z5sjRpO60Xhk4NU5x1hxO5pXcnkMYI-iwfnqqZasNftsuao-LeBRXrDAsgDAkPR7w6_tBqvulSN4MStFNgpPTFNmvzItC1YhFzvoBJug2FrzMO9kw20NPq916nATnqDTA9rbUZra1k9Iprzf2M1vHluuylPfr6S5_BP9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzcwzUxtlGDS7V6wN5_VesTeekrb8TAhSyrzElM7NYJIGaSuCIIsUrXvoQJBX3FajR-3h9VXwMyh6PgyDIVSG1W-sw6WMUGO1N3pj-xJWUPZCt2lto9GC4itIM2Ocb80SNOTnPjAx-GeZ09rrLQNMFmHVgXVlJdrPsvJ382Qlq5NomWspDxyAEEo4kbsryBKb9Q&u_aref=jHPCJD1H%2F51p%2F8%2Bj2zOlm%2FckGhw%3D"
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN, zh, q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '49',
            'Content - Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie': 'JSESSIONID=CD27FE5A77F0989B28BA1983948A8846; acw_tc=2760778216917460279581058e2f47232cc7998fa63b5b202125a78adda5f2; acw_sc__v2=64d5feeb69150546794168b3c7ed70d8d6c0f029; ssxmod_itna=QqAxy7Dtiti=GQqiQDXYao0IpniRD0ljj6ioZnm140vWqPGzDAxn40iDtraTmDbghAKGb7GP2xvYiDeLPGC9B5dqbF0Ro05WDCPGnDB9DUAADYACDt4DTD34DYDio5DLDmeD+UsKDd06TN/GT=D3qDwDB=DmqG23miDA4tLDxUl/824keDSKYNomDtDjqGgDBLKtcbDGqaaxgXl/QWDbhPcbQrDtqD9GlU08eDHId0ZtL9GYGp5YG+6bG+KCO4K88GQzzDtl2GQ/xqtQYfKKD+TGt1iDD3oDxw3zBxxD; ssxmod_itna2=QqAxy7Dtiti=GQqiQDXYao0IpniRD0ljj6ioZnmxn93r4xDs==KDLGIQ7yD8QpoFKkD8r+=q2bWCH+7yY/0IuAe9=70=obFC7iQi94doFWIYokjB2mh=TZASPpwdcEM1oaVIzr4Tdk5+KStVDCXkGu04oSNfm80qwdr03RU3ofxodbTKMjQYojXKyQbf/unRK+Y3yMTbop3=o8ETNTFt6OUQd8YZF1A1ra3ZiZX1v=NiHMixN+3vc1OcnTf0jZSRiZgRUok+9oQmPqo6ovfh/FTUOZlU2giXwyZYVF+0j5socvfpRv/pAKBBIdcU7Ztx+0IeYSO6IciS1eM2j11mwlDiD+3rj/0td4A0j0i+wGAId=I=oP4ArcQKWn2qg05YwFbR/QrCUodFbo8TWtuk8wxlD7fA20TREx7fn8RnzUR3ZjaDG2ShxIuF0hxm+et0=YrQU5oyrHZDND2HRfKYMxCeF5uF22x4TKUi767CdM7DxOeLKBSxtR4DL8uDG=0rGi75q=mLxKRZl3F67wddh80+ghFl4tWrKbDru8=CCzDxDFqD+EriiDQzy6DIdiD4A40GPkTKnUSr7MX0SGG9CHGzqKzwFOeCCTCnSMxjSh8k4YD=',
            'Host': 'www.cdt-ec.com',
            'Origin': 'https://www.cdt-ec.com',
            'Referer': 'https://www.cdt-ec.com/notice/moreController/toMore?globleType=0&u_atoken=17d82ce5-f9da-40d4-951e-56821d58a723&u_asession=01u3UQZcH0xovwQqUhnnKf1xdlAD7KcYpnVOcsDamk_wHXqWuWWfydVuQ-d6MFcXlPX0KNBwm7Lovlpxjd_P_q4JsKWYrT3W_NKPr8w6oU7K8Q4XSVjBdxeXWCLt5cKk6EJplDo7Akhkufk3kqWTOsm2BkFo3NEHBv0PZUm6pbxQU&u_asig=05jvzEToeIBylYTqO6AnQYpw_4H5WpqN1mDaVHeB5DApSE3g5TGF2vTlTeUs1qzVLpa3a9S-KH-3F322hKmYvsINYXqBqACq1l21wqK9nhjL4rDez-SFj0aMG1WfN7avP0CpanW1x_-FAfodylcuECnvzj1pzOFhOsO2dpdDJqmpX9JS7q8ZD7Xtz2Ly-b0kmuyAKRFSVJkkdwVUnyHAIJzTgKKFXEmKxprwQ7aOz9ko8-4PHYIYN0xgGU3DjUZmrPmamEEsKt2ZpuVEq9_MM2K-3h9VXwMyh6PgyDIVSG1W_1ixwfGuq6BepahKs3ItE4YGYDqHeX90h_yD6KfDquy4QA5UJDP1UNHkTJ9v3S9C5GtqWWOids5ubnpceSO867mWspDxyAEEo4kbsryBKb9Q&u_aref=3qBl9SbuduYAC8zceLeKADF0Va0%3D',
            'Sec-Ch-Ua': '"Google Chrome";v="113","Chromium";v="113", "Not-A.Brand";v="24"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 113.0.0.0Safari / 537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        self.get_cookies_and_content(url)
        time.sleep(5)

        url_base = 'https://www.cdt-ec.com/notice/moreController/getList'
        form_data = {
            'page': 1,
            'limit': 10,
            'messagetype': 0,
            'startDate': '',
            'endDate': ''
        }

        url = url_base.format(1)
        self.log.info("开始采集第1页：{}".format(url))
        content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                           timeout=TIMEOUT, verify=False)
        # print(content)
        total = int(content['count'])
        all_re_page = total // 10 + 1
        if all_re_page:
            all_re_page = int(all_re_page)
        else:
            all_re_page = 1
        pages = all_re_page
        self.log.info("总页数：{},开始采集第1页：{}".format(all_re_page, url))
        # self.list_parse(content, url)
        for num in range(17, pages + 1):
            form_data = {
                'page': num,
                'limit': 10,
                'messagetype': 0,
                'startDate': '',
                'endDate': ''
            }
            self.log.info("总页数：{},开始采集第{}页：{}".format(all_re_page, num, url))
            content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                               timeout=TIMEOUT, verify=False)
            if isinstance(content, tuple):
                if content[0] == "412":
                    self.get_cookies_and_content(url)
                    content = self.req(url=url, req_type='post', headers=self.headers, data=form_data, rsp_type="json",
                                       timeout=TIMEOUT, verify=False)
                else:
                    self.log.info("未找到：" + url)
                    continue
            if not content:
                self.log.info(f"page {num} 无返回数据：" + url)
                break
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, maincontent, url):
        items = maincontent['data']

        for item in items:
            if self.exit_flag:
                return
            # title = item.xpath("string(./td[2]/a[1]/@title)")
            # href_text = item.xpath("string(./td[2]/a[1]/@href)")
            # href = util.re_find_one("'(.*?)'", href_text)
            # detail_url = urljoin(urlbase, href)
            title = item['message_title']
            href = item['id']
            detail_url = "https://www.cdt-ec.com/notice/moreController/moreall?id=" + href
            detail_content = self.get_cookies_and_content(detail_url)

            detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
            detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
            # content_text = html.xpath('string(//div[@class="detail_box qst_box"])')
            # content_text1 = html.xpath('string(//div[@class="box"]/div/table)')
            data = {}
            publish_time = item['publish_time']
            data['article_url'] = detail_url
            data['标题'] = title
            data['时间'] = publish_time
            data['项目编号'] = item['message_no']
            data['所属频道'] = self.file_name
            # data[TABField.announcement] = item.xpath("string(./@title)")
            done_fields = []
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)

    def detail_parse(self, detail_content, detail_url, data=None, done_fields=None):
        if not data:
            data = {}
        url = data.get("article_url")
        uuid = util.get_md5(url)
        data['uuid'] = uuid

        html = etree.HTML(detail_content)
        data['项目名称'] = html.xpath('string(//div[@id="moreall"]/h1)').strip().replace('\t', '').replace('\n', ' ')
        pdf_url = html.xpath('string(//embed[@id="embedid"]/@src)')
        pdf_url = pdf_url.split('file=')[-1].replace('%26', '&').replace('%3D', '=')
        data['pdf_link'] = pdf_url
        if not pdf_url:
            print('no pdf_url!')
            return
        pdf_content = self.req(url=pdf_url, rsp_type="content")
        time.sleep(random.randint(2, 3))
        if isinstance(pdf_content, tuple):
            if pdf_content[0] == "412":
                self.get_cookies_and_content(detail_url)
                pdf_content = self.req(url=pdf_url, rsp_type="content")
            else:
                self.log.info("未找到：" + pdf_url)
                return
        if not pdf_content or isinstance(pdf_content, tuple):
            self.log.error("{} no detail_content".format(detail_url))
            return

        source_code = pdf_content
        data['源码'] = str(source_code).strip()
        with open("a.pdf", mode="wb") as f:
            f.write(pdf_content)  # 内容写入文件
        article = self.parsePDF("a.pdf")
        data['正文'] = article
        article = article.replace(' ', '').replace('\r', '').replace('\xa0', '').replace('\t', '').replace('\n', '\n|s|').strip()
        # 段落分割1
        at_list = article.split('|s|')
        addition = ''
        for at in range(len(at_list)):
            # 补充上一换行规则内容
            if addition:
                if not re.match('\d+', at_list[at]):
                    at_list[at] = addition + at_list[at]
                addition = ''
            at_list[at] = at_list[at].strip() + '\n'
            if len(at_list[at]) < 4:
                addition = at_list[at].strip()
                at_list[at] = ''
                continue
            # 一级标题
            if re.match('\d{1,2}\.', at_list[at]):
                if not re.match('\d{1,2}\.\d{1,2}', at_list[at]):
                    at_list[at] = '汉字ma汉字' + at_list[at]
            elif re.match('\d{1,2}', at_list[at]):
                # 不允许开头超过3个数字
                if not re.match('\d{3}', at_list[at]) and not re.match('\d{1,2}\.\d{1,2}', at_list[at]):
                    at_list[at] = '汉字ma汉字' + at_list[at]
            # 二级标题
            if re.match('\d{1,2}\.\d{1,2}', at_list[at].strip()):
                at_list[at] = '汉字shi汉字' + at_list[at]
            # 无各级标题情况
            if re.match('[\s\S]{1,}：[\s\S]{1,}', at_list[at]) or re.match('[\s\S]{1,}:[\s\S]{1,}', at_list[at]):
                at_list[at] = '汉字ro汉字' + at_list[at]
        article = ''.join(at_list)
        # print(article)

        if article:
            for key, items in self.parse_dict.items():
                # 正则优先
                if not data.get(key):
                    data[key] = ""
                re_list = items.get('re')
                for r in re_list:
                    if not r:
                        continue
                    if data.get(key) and data.get(key, "") not in ("详见公告正文", "null"):
                        break
                    try:
                        re_value = re.findall(r, article)
                        for v in re_value:
                            v = re.sub("<[\s\S]*?>", "", v).replace("\r", "").replace("\n", "").replace('&nbsp;', '').strip()
                            # 补丁
                            if key == "project_number" and v and len(v) > 40 and 'ec.ceec.net.cn' not in detail_url and \
                                    'www.e-bidding.org' not in detail_url:
                                v = ""
                            elif key == "phone" and v and (len(v) > 30 or len(v) < 6):
                                v = ""
                            if v:
                                data[key] = v.replace('汉字ma汉字', '').replace('汉字shi汉字', '').replace('汉字ro汉字', '')
                                break
                    except:
                        data[key] = ""
            phone = data.get("联系电话")
            if phone:
                phone_list = re.findall(r'\d[a-zA-Z0-9\-、－—\转\(\)（）/ ]{1,}', phone)
                phone = phone if not phone_list else phone_list[0]
                phone = phone.replace("电话", "").replace("：", "").replace("联系方式", "").replace("联系", "") \
                    .replace("项目负责", "").replace("人", "").strip()
                if phone.endswith("（"):
                    try:
                        phone = re.findall('[0-9-]{1,}', phone)[0]
                    except:
                        phone = ""
                if len(phone) < 6:
                    phone = ''
                if ("）" in phone and "（" not in phone) or ("（" in phone and "）" not in phone):
                    phone.replace("）", "").replace("（", "")

                data['招标人联系方式'] = phone
                data['招标代理联系方式'] = phone

        if not data.get('项目概况', '') or len(data.get('项目概况', '')) < 20:
            data['项目概况'] = html.xpath('string(//div[@id="moreall"]/table)').replace(' ', '').replace('\r', '').replace('\xa0', '').replace('\t', '').replace('\n', ' ').strip()

        paragraph_list = article.replace('汉字shi汉字', '').replace('汉字ro汉字', '').split('汉字ma汉字')
        if len(paragraph_list) > 1:
            temp_list = paragraph_list[0].split('\n')
            zhaobiaoren_flag = False
            for i in temp_list:
                if zhaobiaoren_flag:
                    data['招标人'] = i
                    zhaobiaoren_flag = False
                    continue
                # 处理标题行出现招标相关信息
                if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人') or i.startswith('招标方'):
                    if not data.get('招标人', ''):
                        data['招标人'] = i
                        if i == '招标人' or i == '':
                            zhaobiaoren_flag = True
                elif i.startswith('招标代理机构'):
                    if not data.get('招标代理', ''):
                        data['招标代理'] = i
                elif i.startswith('招标编号'):
                    if not data.get('项目编号', ''):
                        data['项目编号'] = i

            for i in range(len(paragraph_list)):
                col_list = paragraph_list[i].split('\n')
                if '招标条件' in col_list[0] and not data.get('招标条件', ''):
                    data['招标条件'] = ''
                    for j in col_list[1:]:
                        data['招标条件'] += j
                elif '项目概况与招标范围' in col_list[0] or '项目概况与采购范围' in col_list[0]:
                    at_list = paragraph_list[i].split('\n')
                    for j in at_list:
                        if '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j and not data.get('计划工期', ''):
                            data['计划工期'] = j.split('计划工期：')[-1]
                    for at in range(len(at_list)):
                        if re.match('\d{1}\.\d{1}', at_list[at].strip()):
                            at_list[at] = '|s|' + at_list[at]
                    paragraph_list[i] = '\n'.join(at_list)
                    son_list = paragraph_list[i].split('|s|')
                    if len(son_list) > 1:
                        for j in son_list[1:]:  # 去掉标题行
                            if '招标编号：' in j and not data.get('项目编号', ''):
                                # if not data.get('项目编号', ''):
                                data['项目编号'] = j.split('招标编号：')[-1]
                            elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j and not data.get('计划工期', ''):
                                data['计划工期'] = j.split('计划工期：')[-1]
                            elif '招标范围：' in j and not data.get('招标范围', ''):
                                data['招标范围'] = j.split('招标范围：')[-1]
                    else:
                        for j in at_list:
                            if '招标编号：' in j and not data.get('项目编号', ''):
                                # if not data.get('项目编号', ''):
                                data['项目编号'] = j.split('招标编号：')[-1]
                            elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j and not data.get('计划工期', ''):
                                data['计划工期'] = j.split('计划工期：')[-1]
                            elif '招标范围：' in j and not data.get('招标范围', ''):
                                data['招标范围'] = j.split('招标范围：')[-1]
                elif ('投标人资格要求' in col_list[0] or '投标人的资格要求' in col_list[0]) and not data.get('投标人资格要求', ''):
                    data['投标人资格要求'] = ''
                    for j in col_list[1:]:
                        data['投标人资格要求'] += j
                elif '招标文件的获取' in col_list[0] and not data.get('招标文件的获取', ''):
                    data['招标文件的领取'] = ''
                    for j in col_list[1:]:
                        data['招标文件的领取'] += j
                elif '投标文件的递交' in col_list[0] and not data.get('投标文件的递交', ''):
                    data['投标文件的递交'] = ''
                    for j in col_list[1:]:
                        data['投标文件的递交'] += j
                elif '联系方式' in col_list[0]:
                    flag = '招标'
                    for j in col_list[1:]:
                        if '招标人：' in j or '采购单位' in j or '采购人' in j or '招标方' in j:
                            flag = '招标'
                            if not data.get('招标人', '') and not data.get('招标人', ''):
                                data['招标人'] = j.replace('招标人：', '')
                        elif '招标代理：' in j or '招标代理机构：' in j and not data.get('招标代理', ''):
                            flag = '招标代理'
                            if not data.get('招标代理', ''):
                                data['招标代理'] = j.replace('招标代理机构：', '').replace('招标代理：', '')
                        elif '电话：' in j:
                            if flag == '招标':
                                if not data.get('招标人联系方式', ''):
                                    data['招标人联系方式'] = j.replace('电话：', '')
                            else:
                                if not data.get('招标代理联系方式', ''):
                                    data['招标代理联系方式'] = j.replace('电话：', '')
                elif '提出异议、投诉的渠道和方式' in col_list[0]:
                    # for j in col_list[1:]:
                    #     pass
                    pass
                elif '监督部门' in col_list[0]:
                    # for j in col_list[1:]:
                    #     pass
                    pass
                else:
                    pass
        else:
            at_list = paragraph_list[0].split('\n')
            zhaobiaoren_flag = False
            for i in at_list:
                if zhaobiaoren_flag:
                    data['招标人'] = i
                    zhaobiaoren_flag = False
                    continue
                # 处理标题行出现招标相关信息
                if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人'):
                    if not data.get('招标人', ''):
                        data['招标人'] = i
                        if i == '招标人' or i == '':
                            zhaobiaoren_flag = True
                elif i.startswith('招标代理机构'):
                    if not data.get('招标代理', ''):
                        data['招标代理'] = i
                elif i.startswith('招标编号'):
                    if not data.get('项目编号', ''):
                        data['项目编号'] = i
                elif i.startswith('招标条件'):
                    if not data.get('招标条件', ''):
                        data['招标条件'] = i
                elif i.startswith('计划工期') or i.startswith('工期') or i.startswith('交货期') or i.startswith('供货期') or i.startswith('协议期限') or i.startswith('服务期'):
                    if not data.get('计划工期', ''):
                        data['计划工期'] = i
                elif i.startswith('招标编号'):
                    if not data.get('招标编号', ''):
                        data['招标编号'] = i
                elif i.startswith('招标范围'):
                    if not data.get('招标范围', ''):
                        data['招标范围'] = i
            # data['项目名称'] = data['标题']

        # print(data)
        self.upload(data)

        # html = etree.HTML(detail_content)
        # data['项目名称'] = html.xpath('string(//div[@id="moreall"]/h1)')
        # data['项目概况'] = html.xpath('string(//div[@id="moreall"]/table)')
        # pdf_url = html.xpath('string(//embed[@id="embedid"]/@src)')
        # pdf_url = pdf_url.split('file=')[-1].replace('%26', '&').replace('%3D', '=')
        # data['pdf_link'] = pdf_url
        # if not pdf_url:
        #     print('no pdf_url!')
        #     return
        # pdf_content = self.req(url=pdf_url, rsp_type="content")
        # time.sleep(random.randint(10, 15))
        # if isinstance(pdf_content, tuple):
        #     if pdf_content[0] == "412":
        #         self.get_cookies_and_content(detail_url)
        #         pdf_content = self.req(url=pdf_url, rsp_type="content")
        #     else:
        #         self.log.info("未找到：" + pdf_url)
        #         return
        # if not pdf_content or isinstance(pdf_content, tuple):
        #     self.log.error("{} no detail_content".format(detail_url))
        #     return
        #
        # source_code = pdf_content
        # data['源码'] = str(source_code).strip()
        # with open("a.pdf", mode="wb") as f:
        #     f.write(pdf_content)  # 内容写入文件
        # article = self.parsePDF("a.pdf")
        # article = article.replace(' ', '')
        # data['正文'] = article
        # # article = article.replace('1. ', '|s|1. ').replace('2. ', '|s|2. ').replace('3. ', '|s|3. ').\
        # #     replace('4. ', '|s|4. ').replace('5. ', '|s|5. ').replace('6. ', '|s|6. ').replace('7. ', '|s|7. ').\
        # #     replace('8. ', '|s|8. ').replace('9. ', '|s|9. ').replace('10. ', '|s|10. ')
        #
        # # 分割段落
        # at_list = article.split('\n')
        # for at in range(len(at_list)):
        #     if re.match('\d{1,2}\.', at_list[at]):
        #         if not re.match('\d{1,2}\.\d{1,2}', at_list[at]):
        #             at_list[at] = '|s|' + at_list[at]
        #     elif re.match('\d{1,2}', at_list[at]):
        #         # 不允许开头超过3个数字
        #         if not re.match('\d{3}', at_list[at]) and not re.match('\d{1,2}\.\d{1,2}', at_list[at]):
        #             at_list[at] = '|s|' + at_list[at]
        # article = '\n'.join(at_list)
        # paragraph_list = article.split('|s|')
        # if len(paragraph_list) > 1:
        #     temp_list = paragraph_list[0].split('\n')
        #     data['标题'] = ''
        #     title_flag = True
        #     for i in temp_list:
        #         if title_flag:
        #             data['标题'] += i.strip()
        #             if data['标题'].endswith('招标公告') or data['标题'].endswith('公告') or data['标题'].endswith('公示') \
        #                     or data['标题'].endswith('通知'):
        #                 title_flag = False
        #             continue
        #         # 处理标题行出现招标相关信息
        #         if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人') or i.startswith('招标方'):
        #             if not data.get('招标人', ''):
        #                 data['招标人'] = i
        #         elif i.startswith('招标代理机构'):
        #             data['招标代理'] = i
        #         elif i.startswith('招标编号'):
        #             data['项目编号'] = i
        #
        #     # paragraph_list[0].replace('\n', '')
        #
        #     # data['项目名称'] = data['标题']
        #     for i in range(len(paragraph_list)):
        #         col_list = paragraph_list[i].split('\n')
        #         if '招标条件' in col_list[0]:
        #             data['招标条件'] = ''
        #             for j in col_list[1:]:
        #                 data['招标条件'] += j
        #         elif '项目概况与招标范围' in col_list[0] or '项目概况与采购范围' in col_list[0]:
        #             at_list = paragraph_list[i].split('\n')
        #             for j in at_list:
        #                 if '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j:
        #                     data['计划工期'] = j.split('计划工期：')[-1]
        #             for at in range(len(at_list)):
        #                 if re.match('\d{1}\.\d{1}', at_list[at].strip()):
        #                     at_list[at] = '|s|' + at_list[at]
        #             paragraph_list[i] = '\n'.join(at_list)
        #             son_list = paragraph_list[i].split('|s|')
        #             if len(son_list) > 1:
        #                 for j in son_list[1:]:  # 去掉标题行
        #                     if '招标编号：' in j:
        #                         # if not data.get('项目编号', ''):
        #                         data['项目编号'] = j.split('招标编号：')[-1]
        #                     elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j:
        #                         data['计划工期'] = j.split('计划工期：')[-1]
        #                     elif '招标范围：' in j:
        #                         data['招标范围'] = j.split('招标范围：')[-1]
        #             else:
        #                 for j in at_list:
        #                     if '招标编号：' in j:
        #                         # if not data.get('项目编号', ''):
        #                         data['项目编号'] = j.split('招标编号：')[-1]
        #                     elif '计划工期：' in j or '交货期' in j or '供货期' in j or '协议期限' in j or '服务期' in j or '工期' in j:
        #                         data['计划工期'] = j.split('计划工期：')[-1]
        #                     elif '招标范围：' in j:
        #                         data['招标范围'] = j.split('招标范围：')[-1]
        #         elif '投标人资格要求' in col_list[0] or '投标人的资格要求' in col_list[0]:
        #             data['投标人资格要求'] = ''
        #             for j in col_list[1:]:
        #                 data['投标人资格要求'] += j
        #         elif '招标文件的获取' in col_list[0]:
        #             data['招标文件的领取'] = ''
        #             for j in col_list[1:]:
        #                 data['招标文件的领取'] += j
        #         elif '投标文件的递交' in col_list[0]:
        #             data['投标文件的递交'] = ''
        #             for j in col_list[1:]:
        #                 data['投标文件的递交'] += j
        #         elif '联系方式' in col_list[0]:
        #             flag = '招标'
        #             for j in col_list[1:]:
        #                 if '招标人：' in j or '采购单位' in j or '采购人' in j or '招标方' in j:
        #                     flag = '招标'
        #                     if not data.get('招标人', ''):
        #                         data['招标人'] = j.replace('招标人：', '')
        #                 elif '招标代理：' in j or '招标代理机构：' in j:
        #                     flag = '招标代理'
        #                     if not data.get('招标代理', ''):
        #                         data['招标代理'] = j.replace('招标代理机构：', '').replace('招标代理：', '')
        #                 elif '电话：' in j:
        #                     if flag == '招标':
        #                         if not data.get('招标人联系方式', ''):
        #                             data['招标人联系方式'] = j.replace('电话：', '')
        #                     else:
        #                         if not data.get('招标代理联系方式', ''):
        #                             data['招标代理联系方式'] = j.replace('电话：', '')
        #         elif '提出异议、投诉的渠道和方式' in col_list[0]:
        #             # for j in col_list[1:]:
        #             #     pass
        #             pass
        #         elif '监督部门' in col_list[0]:
        #             # for j in col_list[1:]:
        #             #     pass
        #             pass
        #         else:
        #             pass
        # else:
        #     at_list = paragraph_list[0].split('\n')
        #     data['标题'] = ''
        #     title_flag = True
        #     for i in at_list:
        #         if title_flag:
        #             data['标题'] += i.strip()
        #             if data['标题'].endswith('招标公告') or data['标题'].endswith('公告') or data['标题'].endswith('公示') \
        #                     or data['标题'].endswith('通知'):
        #                 title_flag = False
        #             continue
        #         # 处理标题行出现招标相关信息
        #         if i.startswith('招标人') or i.startswith('采购单位') or i.startswith('采购人'):
        #             if not data.get('招标人', ''):
        #                 data['招标人'] = i
        #         elif i.startswith('招标代理机构'):
        #             data['招标代理'] = i
        #         elif i.startswith('招标编号'):
        #             data['项目编号'] = i
        #         elif i.startswith('招标条件'):
        #             data['招标条件'] = i
        #         elif i.startswith('计划工期') or i.startswith('工期') or i.startswith('交货期') or i.startswith('供货期') or i.startswith('协议期限') or i.startswith('服务期'):
        #             data['计划工期'] = i
        #         elif i.startswith('招标编号'):
        #             data['招标编号'] = i
        #         elif i.startswith('招标范围'):
        #             data['招标范围'] = i
        #     data['项目名称'] = data['标题']
        #
        # print(data)
        # self.upload(data)


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        "query_time": "",
        "MainKeys": [
            ""
            # "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    keyword = ''
    bid = BidZGDZ(debug=True)
    bid.process_item(params)