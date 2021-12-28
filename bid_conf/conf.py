#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2021/12/11 3:47 下午
@Author: CZC
@File: conf.py
"""
parse_dict = {
    "中招国际招标有限公司-采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目名称")]/following-sibling::td[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//th[contains(text(),"公告开始时间")]/following-sibling::td[1]", "//th[contains(text(),"公示开始时间")]/following-sibling::td[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//th[contains(text(),"联系人")]/following-sibling::td[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//th[contains(text(),"联系方式")]/following-sibling::td[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },  # 日兴
    "中国采购与招标网-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="topTitle"]/h3']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[text()="招标人"]/../td']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "报名时间")]/following-sibling::*[1]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//th[text()="项目区域"]/following-sibling::td[1]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[text()="所属行业"]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="container"]/div[@class="white-bg"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "开标时间")]/following-sibling::*[1]']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['//th[text()="概况"]/following-sibling::td[1]']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//th[text()="代理机构"]/following-sibling::td[1]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },  # 通过未上线
    "城规采购网-招标与采购": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h5[@class='tit']", ""]
        },  # 项目标题
        "project_number": {
            "re": ["", ""],
            "xpath": ["//td[@class='title'][contains(text(),'项目编号')]/following-sibling::td[1]",
                      "//td[@class='title'][contains(text(),'公示编号')]/following-sibling::td[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//div[@class='base-item']/h5[@class='tit']/b", ""]
        },  # 招标单位
        "tender_price": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 标的金额
        "publish_time": {
            "re": ["", ""],
            "xpath": [
                "//td[@class='title'][contains(text(),'报名开始时间')]/following-sibling::td[1]",
                "//td[@class='title'][contains(text(),'公示开始时间')]/following-sibling::td[1]",
                "//input[@id='hid_PublishDate']/@value"]
        },  # 发布时间
        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'联系人')]/..", ""]
        },  # 招标项目负责人
        "phone": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'联系电话')]/..", "//span[@lang][contains(text(),'联系方式')]/.."]
        },  # 联系电话
        "project_location": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'联系地址')]/..", ""]
        },  # 项目所在地
        "industry_type": {
            "re": ["", ""],
            "xpath": ["//td[@class='title'][contains(text(),'招标类型')]/following-sibling::td[1]",
                      "//td[@class='title'][contains(text(),'采购类别')]/following-sibling::td[1]",
                      "//td[@class='title'][contains(text(),'项目类型')]/following-sibling::td[1]"]
        },  # 项目行业类型
        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 文章URL
        "source": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 信息来源
        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='tab-content']/div[@id='noticeContent']", ""]
        },  # 正文
        "bid_finish_time": {
            "re": ["", ""],
            "xpath": ["//td[@class='title'][contains(text(),'报名开始时间')]/following-sibling::td[1]",
                      "//td[@class='title'][contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 开标时间
        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//td[@class='title'][contains(text(),'报名截止时间')]/following-sibling::td[1]",
                      "//td[@class='title'][contains(text(),'公示结束时间')]/following-sibling::td[1]"]
        },  # 投标截止时间
        "project_overview": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 项目概况
        "agency": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'代理机构名称')]/..", "//span[@lang][contains(text(),'招标代理机构')]/.."]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 评标规则
        "bid_winner": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'中价候选人名称')]/..", "//span[@lang][contains(text(),'候选人名称')]/.."]
        },  # 中标人
        "win_bid_price": {
            "re": ["", ""],
            "xpath": ["//span[@lang][contains(text(),'中价金额')]/..", ""]
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 中标公告发布时间
        "channel": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 所属频道
        "attachment_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 附件链接
        "keyword": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 关键词
        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 采集时间
        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 预留字段1
        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 预留字段2
        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },  # 预留字段3

    },  # 2
    "中国采购与招标网-变更公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="topTitle"]/h3']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//div[@class="topTitle"]/h3/b']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[text()="招标人"]/following-sibling::td[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "报名时间")]/following-sibling::*[1]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//th[text()="项目区域"]/following-sibling::td[1]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[text()="所属行业"]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="container"]/div[@class="white-bg"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "开标时间")]/following-sibling::*[1]']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['//th[text()="概况"]/following-sibling::td[1]']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//th[text()="代理机构"]/following-sibling::td[1]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 通过未上线
    "中国采购与招标网-中标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[contains(@class,"topTitle")]/h3']
        },  # 项目标题
        "project_number": {
            "re": ['(?<=<b>\[)(.+?)(?=\]<\/b>)'],
            "xpath": ['//div[contains(@class,"topTitle")]/h3/b']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@id="main"]/div/h3']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//div[@id='container' or @class='container topTitle']"]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },
    "中国采购与招标网-废标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[contains(@class,"topTitle")]/h3']
        },  # 项目标题
        "project_number": {
            "re": ['(?<=<b>\[)(.+?)(?=\]<\/b>)'],
            "xpath": ['//div[contains(@class,"topTitle")]/h3/b']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标机构：")]/..',
                      '//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="名称："]/../following-sibling::span[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@id="main"]/div/h3']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['',
                      '']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['',
                      '']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": [
                '//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="地址："]/../following-sibling::span[1]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="container"]/div/div[@id="container"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "开标时间")]/following-sibling::*[1]']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(?=</span>)(.+?)<'],
            "xpath": ['//span[contains(text(),"招标代理机构")]/../..',
                      '//span[contains(text(),"代理机构信息")]/../../../following-sibling::p/span/span[text()="代理机构："]/../following-sibling::span[1]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": ['load\("(.*?)"\)'],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },
    "招商局集团电子招标交易平台-采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目名称")]/following-sibling::td[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[contains(string(),"采购人名称")]/following-sibling::td[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//th[contains(text(),"公告开始时间")]/following-sibling::td[1]',
                '//th[contains(text(),"公示开始时间")]/following-sibling::td[1]',
            ]
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['string(//th[contains(text(),"联系人")]/following-sibling::td[1])']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['string(//th[contains(text(),"联系方式")]/following-sibling::td[1])']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['//th[contains(string(),"代办机构名称")]/following-sibling::td[1]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['/']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "招商局集团电子招标交易平台-评标结果公示": {
        "project_title": {
            "re": ['标段名称:([\s\S]*?)<'],
            "xpath": ['//th[contains(text(),"采购项目名称")]/following-sibling::td[1]/span',
                      '//th[contains(text(),"采购项目名称")]/following-sibling::td[1]',
                      "//span[@class='title']"]
        },  # 项目标
        "project_number": {
            "re": ['标段编号:([\s\S]*?)<'],
            "xpath": ['//th[contains(text(),"采购项目编号")]/following-sibling::td[1]',
                      '//th[contains(text(),"标段编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": ['公示开始时间:([\s\S]*?)<'],
            "xpath": ['//th[contains(text(),"公告开始时间")]/following-sibling::td[1]',
                      '//th[contains(text(),"公示开始时间")]/following-sibling::td[1]'],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": [
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目负责人：")]/following-sibling::td[1]',
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目经理：")]/following-sibling::td[1]',
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系人：")]/following-sibling::td[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": [
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系电话：")]/following-sibling::td[1]',
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系方式：")]/following-sibling::td[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['//th[contains(text(),"中标候选单位名称")]/following-sibling::td[1]']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['//th[contains(text(),"投标报价")]/following-sibling::td[1]']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['//th[contains(text(),"公示开始时间")]/following-sibling::td[1]']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "招商局集团电子招标交易平台-项目结果公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目名称")]/following-sibling::td[1]/span',
                      '//th[contains(string(),"采购项目名称")]/following-sibling::td[1]/span',
                      '//th[contains(text(),"采购项目名称")]/following-sibling::td[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目编号")]/following-sibling::td[1]',
                      '//th[contains(string(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": ['//th[contains(string(),"公示开始时间")]/following-sibling::td[1]'],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目经理")]/following-sibling::td[1]',
                      '//th[contains(text(),"联系人")]/following-sibling::td[1]',
                      ]
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//th[contains(text(),"联系电话")]/following-sibling::td[1]',
                      '//th[contains(text(),"手机号")]/following-sibling::td[1]',
                      '//th[contains(text(),"联系方式")]/following-sibling::td[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['//th[contains(text(),"中标人")]/following-sibling::td[1]',
                      '//td[@class="bj"][contains(text(), "供应商名称")]/../following::*/td[count(//td[@class="bj"][contains(text(), "供应商名称")]) + 1]'
                      ]
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['//th[contains(text(),"中标价")]/following-sibling::td[1]',]
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['//th[contains(text(),"公示开始时间")]/following-sibling::td[1]', '//th[contains(text(),"评标时间")]/following-sibling::td[1]']

        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "招商局集团电子招标交易平台-项目终止": {
        "project_title": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目名称")]/following-sibling::td[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//th[contains(text(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": ["//p[@class='kdg']/font[@class='red']"],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目经理")]/following-sibling::td[1]',
                      '//th[contains(text(),"联系人")]/following-sibling::td[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//th[contains(text(),"联系电话")]/following-sibling::td[1]',
                      '//th[contains(text(),"联系方式")]/following-sibling::td[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']  # //th[contains(text(),"采购人地址")]/following-sibling::td[1]
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['//th[contains(text(),"中标人")]/following-sibling::td[1]',
                      ]
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "招商局集团电子招标交易平台-有效投标人公示": {
        "project_title": {
            "re": [''],
            "xpath": ['//th[contains(text(),"标段名称")]/following-sibling::td[1]', "//span[@class='title']"]
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//th[contains(text(),"标段编号")]/following-sibling::td[1]',
                      '//th[contains(text(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[contains(string(),"采购人名称")]/following-sibling::td[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']  # //th[contains(text(),"投标报价")]/following-sibling::td[1] 投标金额不采集
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//th[contains(text(),"公告开始时间")]/following-sibling::td[1]',
                '//th[contains(text(),"公示开始时间")]/following-sibling::td[1]',
            ],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": [
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目经理")]/following-sibling::td[1]']
        },  # 招标项目负责人 页面上的都是投标负责人不采集
        "phone": {
            "re": [''],
            "xpath": [
                '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系电话")]/following-sibling::td[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="template"]']
        },  # 正
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/../table']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['string(//th[contains(text(),"公示开始时间")]/following-sibling::td[1])']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "中国采购网-地方单位采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ["//h2[@class='tc']", '//strong[contains(text(),"项目名称")]/../span']
        },  # 项目标
        "project_number": {
            "re": ['项目编号：(.+?)(?=（|<)'],
            "xpath": ['//strong[contains(text(),"项目编号")]/../span']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['>预算金额：(.+?)<', '金额：</b> (.*?)<'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": ['项目联系人(.*?)</tr>', '项目联系人：(.+?)(?=（|<)', '负责人: (.+?) '],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]',
                      '//div[contains(text(),"项目联系人")]/following-sibling::div[1]']
        },  # 招标项目负责
        "phone": {
            "re": ['电　话：(.*?)(?=<|，)', '项目联系电话(.*?)</tr>', '项目联系电话：(\d[a-zA-Z0-9\-、－—\转\(\)（）]+?)(?=<|，)', '负责人: (.*?) <'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电　话")]',
                      'string(//div[contains(text(),"项目联系方式")]/following-sibling::div[1])',
                      '']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="vF_detail_content_container"]']
        },  # 正
        "bid_finish_time": {
            "re": ['开标时间：(.+?)<'],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目概况")]/following-sibling::p[1]']
        },  # 项目概
        "agency": {
            "re": ['采购代理机构信息[\s\S]*?名.?称：(.+?)<'],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": ['资格要求：</strong>([\s\S]*?)<strong', '供应商资格条件</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": ['第一包供应商名称：(.+?)<', '供应商名称：(.+?)(?=（|<)', '//table/thead/tr/th[contains(string(), "中标供应商名称")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "中标供应商名称")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": ['中标（成交）金额：(.+?)<', '>总中标金额.*?>￥(.+?)<', '//table/thead/tr/th[contains(string(), "总价(元)")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "总价(元)")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a/@href']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "中国采购网-其他采购信息": {
        "project_title": {
            "re": [''],
            "xpath": ["//h2[@class='tc']", '//strong[contains(text(),"项目名称")]/../span']
        },  # 项目标
        "project_number": {
            "re": ['项目编号：(.+?)(?=（|<)'],
            "xpath": ['//strong[contains(text(),"项目编号")]/../span']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['>预算金额：(.+?)<', '金额：</b> (.*?)<'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": ['项目联系人(.*?)</tr>', '项目联系人：(.+?)(?=（|<)', '负责人: (.+?) '],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]',
                      '//div[contains(text(),"项目联系人")]/following-sibling::div[1]']
        },  # 招标项目负责
        "phone": {
            "re": ['电　话：(.*?)(?=<|，)', '项目联系电话(.*?)</tr>', '项目联系电话：(\d[a-zA-Z0-9\-、－—\转\(\)（）]+?)(?=<|，)', '负责人: (.*?) <'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电　话")]',
                      'string(//div[contains(text(),"项目联系方式")]/following-sibling::div[1])',
                      '']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="vF_detail_content_container"]']
        },  # 正
        "bid_finish_time": {
            "re": ['开标时间：(.+?)<'],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目概况")]/following-sibling::p[1]']
        },  # 项目概
        "agency": {
            "re": ['采购代理机构信息[\s\S]*?名.?称：(.+?)<'],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": ['资格要求：</strong>([\s\S]*?)<strong', '供应商资格条件</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": ['第一包供应商名称：(.+?)<', '供应商名称：(.+?)(?=（|<)', '//table/thead/tr/th[contains(string(), "中标供应商名称")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "中标供应商名称")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": ['中标（成交）金额：(.+?)<', '>总中标金额.*?>￥(.+?)<', '//table/thead/tr/th[contains(string(), "总价(元)")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "总价(元)")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a/@href']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "中国采购网-中央单位采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ["//h2[@class='tc']", '//strong[contains(text(),"项目名称")]/../span']
        },  # 项目标
        "project_number": {
            "re": ['项目编号：(.+?)(?=（|<)'],
            "xpath": ['//strong[contains(text(),"项目编号")]/../span']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['>预算金额：(.+?)<', '金额：</b> (.*?)<'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": ['项目联系人(.*?)</tr>', '项目联系人：(.+?)(?=（|<)', '负责人: (.+?) '],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]',
                      '//div[contains(text(),"项目联系人")]/following-sibling::div[1]']
        },  # 招标项目负责
        "phone": {
            "re": ['电　话：(.*?)(?=<|，)', '项目联系电话(.*?)</tr>', '项目联系电话：(\d[a-zA-Z0-9\-、－—\转\(\)（）]+?)(?=<|，)', '负责人: (.*?) <'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电　话")]',
                      'string(//div[contains(text(),"项目联系方式")]/following-sibling::div[1])',
                      '']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="vF_detail_content_container"]']
        },  # 正
        "bid_finish_time": {
            "re": ['开标时间：(.+?)<'],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目概况")]/following-sibling::p[1]']
        },  # 项目概
        "agency": {
            "re": ['采购代理机构信息[\s\S]*?名.?称：(.+?)<'],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": ['资格要求：</strong>([\s\S]*?)<strong', '供应商资格条件</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": ['第一包供应商名称：(.+?)<', '供应商名称：(.+?)(?=（|<)', '//table/thead/tr/th[contains(string(), "中标供应商名称")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "中标供应商名称")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": ['中标（成交）金额：(.+?)<', '>总中标金额.*?>￥(.+?)<', '//table/thead/tr/th[contains(string(), "总价(元)")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "总价(元)")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a/@href']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "中国采购网-中央批量集中采购": {
        "project_title": {
            "re": [''],
            "xpath": ["//h2[@class='tc']", '//strong[contains(text(),"项目名称")]/../span']
        },  # 项目标
        "project_number": {
            "re": ['项目编号：(.+?)(?=（|<)'],
            "xpath": ['//strong[contains(text(),"项目编号")]/../span']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['>预算金额：(.+?)<', '金额：</b> (.*?)<'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": ['项目联系人(.*?)</tr>', '项目联系人：(.+?)(?=（|<)', '负责人: (.+?) '],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]',
                      '//div[contains(text(),"项目联系人")]/following-sibling::div[1]']
        },  # 招标项目负责
        "phone": {
            "re": ['电　话：(.*?)(?=<|，)', '项目联系电话(.*?)</tr>', '项目联系电话：(\d[a-zA-Z0-9\-、－—\转\(\)（）]+?)(?=<|，)', '负责人: (.*?) <'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电　话")]',
                      'string(//div[contains(text(),"项目联系方式")]/following-sibling::div[1])',
                      '']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//div[@class="vF_detail_content_container"]']
        },  # 正
        "bid_finish_time": {
            "re": ['开标时间：(.+?)<'],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目概况")]/following-sibling::p[1]']
        },  # 项目概
        "agency": {
            "re": ['采购代理机构信息[\s\S]*?名.?称：(.+?)<'],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": ['资格要求：</strong>([\s\S]*?)<strong', '供应商资格条件</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": ['第一包供应商名称：(.+?)<', '供应商名称：(.+?)(?=（|<)', '//table/thead/tr/th[contains(string(), "中标供应商名称")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "中标供应商名称")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": ['中标（成交）金额：(.+?)<', '>总中标金额.*?>￥(.+?)<', '//table/thead/tr/th[contains(string(), "总价(元)")]/../following::*[1]//td[count(//table/thead/tr/th[contains(string(), "总价(元)")]/preceding-sibling::*) + 1]'],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a/@href']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "彩云电子招标采购平台-异常公告": {
        "project_title": {
            "re": [''],
            "xpath": ["//div[@class='container']/span[2]", '//div[@class="titleXianmu"]']
        },  # 项目标题
        "project_number": {
            "re": [''],
            "xpath": ['//div[text()="招标编号"]/../span']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//div[text()="招标业主"]/../span']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[text()="发布时间"]/../span']
        },  # 发布时间
        "project_leader": {
            "re": ['>联 系 人: (.*?)<', '联系人：(.*?)<'],
            "xpath": [''],
            # "xpath": ['//span[contains(text(),"联 系 人")]', '//span[contains(text(),"联系人")]/..',
            #           '//span[contains(text(),"招")]/../../following-sibling::p/span/span[contains(text(),"联")]/../..']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"联 系 人")]/../following-sibling::p/span[contains(text(),"联系电话")]',
                      '//span[contains(text(),"联 系 人")]/../following-sibling::p/span[contains(text(),"话")]',
                      '//span[contains(text(),"联系人")]/../../following-sibling::p[1]/span/span[contains(text(),"联系电话")]/../following-sibling::span',
                      '//span[contains(text(),"招")]/../../following-sibling::p/span/span[contains(text(),"电")]/../..',
                      '//span[contains(text(),"联系人")]/../../following-sibling::p/span[contains(text(),"话")]/following-sibling::span[1]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//div[text()="所属地区"]/../span']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="container "]/div[2]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ['']  # //div[text()="截止时间"]/../span
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已完成
    "彩云电子招标采购平台-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[contains(@class,"topTitle")]/h3']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//div[contains(@class,"topTitle")]/h3/b']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[text()="招标人"]/../td']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": ['(?<=开始：)([\s\S]+?)(?=结束：)'],
            "xpath": ['//h4[text()="参与时间"]/../div']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//th[text()="招标人"]/../following-sibling::tr/th[text()="联系人"]/../td']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//th[text()="项目区域"]/following-sibling::td[1]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[text()="所属行业"]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="topTitle" or @id="container"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "开标时间")]/following-sibling::*[1]']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['//div[@class="dot"]/h4[contains(text(), "投标时间")]/following-sibling::*[1]']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['//th[text()="项目概况"]/following-sibling::td[1]', "//h3[text()='项目概况']/..", ]
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//th[text()="代理机构"]/following-sibling::td[1]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已完成
    "彩云电子招标采购平台-中标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="container"]/span[2]', '//div[@class="titleXianmu"]']
        },  # 项目标题
        "project_number": {
            "re": [''],
            "xpath": ['//div[text()="招标编号"]/../span']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//div[text()="招标业主"]/../span']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[text()="发布时间"]/../span']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//div[text()="所属地区"]/../span']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="container "]/div[2]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ['']  # //div[text()="截止时间"]/../span  招标才需要
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['//iframe[@id="pdfContainer"]/@src']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已完成
    "阳光采购网-工程招标": {
        "project_title": {
            "re": [''],
            "xpath": ['//tr[3]/td[2]']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//tr[@class="tabledowntitle"][1]/td[2]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//tr[2]/td[2]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//tr[4]/td[4]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//tr[6]/td[4]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//td[@class="searchborder"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    "阳光采购网-物资招标": {
        "project_title": {
            "re": [''],
            "xpath": ['//tr[3]/td[2]']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//tr[@class="tabledowntitle"][1]/td[2]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//tr[2]/td[2]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//tr[4]/td[4]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//tr[6]/td[4]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//td[@class="searchborder"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    "国e招标采购平台-业务公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@align="center"]/h1']
        },  # 项目标题
        "project_number": {
            "re": [''],
            "xpath": ['']
        },  # 项目编号#列表采集
        "tender_unit": {
            "re": ['(?<=<span name="issue_tendereeName">)([\s\S]+?)(?=<\/span>)'],
            "xpath": ['//p[@id="tendereeName-p"]/span[@name="issue_tendereeName"]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@name="issue_date"]']
        },  # 发布时间
        "project_leader": {
            "re": ['(?<=联系人:)([\s\S]+?)(?=<)', '(?<=联系人：)([\s\S]+?)(?=<)', '(?<=招标人:)([\s\S]+?)(?=<)',
                   '(?<=招标人：)([\s\S]+?)(?=<)', '(?<=比选人名称:)([\s\S]+?)(?=<)', '(?<=比选人名称：)([\s\S]+?)(?=<)',
                   '(?<=名称:)([\s\S]+?)(?=<)', '(?<=名称：)([\s\S]+?)(?=<)'],
            "xpath": ['//div[@class="details"]//*[contains(text(),"联系人")]',
                      '//div[@class="details"]//*[contains(text(),"联系人")]/..',
                      '//div[@class="details"]//*[contains(text(),"招标人")]/..',
                      '//div[@class="details"]//*[contains(text(),"名称")]']
        },  # 招标项目负责人
        "phone": {
            "re": ['(?<=电话:)([\s\S]+?)(?=<)', '(?<=电话：)([\s\S]+?)(?=<)', '(?<=联系方式:)([\s\S]+?)(?=<)',
                   '(?<=联系方式：)([\s\S]+?)(?=<)', '(?<=传真:)([\s\S]+?)(?=<)', '(?<=传真：)([\s\S]+?)(?=<)',
                   '(?<=手机:)([\s\S]+?)(?=<)', '(?<=手机：)([\s\S]+?)(?=<)'],
            "xpath": ['//div[@class="details"]//*[contains(text(),"电话")]',
                      '//div[@class="details"]//*[contains(text(),"电话")]/..',
                      '//div[@class="details"]//*[contains(text(),"联系方式")]',
                      '//div[@class="details"]//*[contains(text(),"传真")]',
                      '//div[@class="details"]//*[contains(text(),"手机")]']
        },  # 联系电话
        "project_location": {
            "re": ['(?<=地址:)([\s\S]+?)(?=<)', '(?<=地址：)([\s\S]+?)(?=<)'],
            "xpath": ['//div[@class="details"]//*[contains(text(),"地址：")]',
                      '//div[@class="details"]//*[contains(text(),"地址:")]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型#列表采集
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="details"]']
        },  # 正文
        "bid_finish_time": {
            "re": ['(?<=开标时间:)([\s\S]+?)(?=<)', '(?<=开标时间：)([\s\S]+?)(?=<)'],
            "xpath": ['//div[@class="details"]//*[contains(text(),"开标时间：")]',
                      '//div[@class="details"]//*[contains(text(),"开标时间:")]']
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": ['(?<=招标代理机构:)([\s\S]+?)(?=<)', '(?<=招标代理机构：)([\s\S]+?)(?=<)', '(?<=招标代理机构联系人:)([\s\S]+?)(?=<)',
                   '(?<=招标代理机构联系人：)([\s\S]+?)(?=<)'],
            "xpath": ['//div[@class="details"]//*[contains(text(),"招标代理机构：")]',
                      '//div[@class="details"]//*[contains(text(),"招标代理机构:")]',
                      '//div[@class="details"]//*[contains(text(),"招标代理机构联系人：")]',
                      '//div[@class="details"]//*[contains(text(),"招标代理机构联系人:")]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道#列表采集
        "attachment_url": {
            "re": [''],
            "xpath": ['//div[@id="online_affixLink"]/a', '//div[@class="details"]//a[@href]']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },
    "南方电网电子采购交易平台-货物-公示公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": ['采购项目编号：(.+?)(?=）|<)'],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": [''],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]"
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[contains(string(), '成交单位')]/../following::*/td[count(//td[contains(string(), '成交单位')]/preceding-sibling::td) + 1]",
                "//span[contains(string(),'招 标 人：')]",
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
            ]
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [''],
            "xpath": ["string(//span[contains(string(),'联 系 人：')])",
                      "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                      "string(//span[contains(string(),'联系人：')])"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [''],
            "xpath": ["//span[contains(string(),'联系电话：')]/following-sibling::*",
                      "//td[contains(string(),'联系电话：')]/following-sibling::*[1]",
                      "//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//p"]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ["//span[contains(string(),'招标代理机构：')]", "//span[contains(string(),'采购代理机构：')]",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ["//span[contains(string(),'价：')]/following-sibling::*[1]"]
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },  # 已修
    "南方电网电子采购交易平台-货物-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": ['招标人：(.*?)</span>'],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['人民币(.*?万元)'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": ['联<.*?>系<.*?>人：.*?宋体;\\">(.*?)</span>'],
            "xpath": ["//span[contains(text(),'招 标 人')]", "//span[contains(text(),'招标人名称')]",
                      "//span[contains(text(),'招标人')]",
                      "//span[text()='招标人信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采购人')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采 购')]/following-sibling::span",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联']/../..",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'招')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采 购')]/following-sibling::span[1]"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": ['电<.*?>话：.*?(.*?)</span>'],
            "xpath": ["//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//p"]
        },  # 正文
        "bid_finish_time": {
            "re": ['开标时间[\s\S]*?时间：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": ['截止时间：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": ['概况：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.*?)</span></strong>'],
            "xpath": ["//span[contains(text(),'招标代理机构')]", "//span[contains(text(),'采购代理机构')]",
                      "//span[text()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      "//span[contains(text(),'代理')]/../.."]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": ['投标人资格要求</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "南方电网电子采购交易平台-工程-公示公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": ['采购项目编号：(.+?)(?=）|<)'],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": [''],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]"
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[contains(string(), '成交单位')]/../following::*/td[count(//td[contains(string(), '成交单位')]/preceding-sibling::td) + 1]",
                "//span[contains(string(),'招 标 人：')]",
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
            ]
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [''],
            "xpath": ["string(//span[contains(string(),'联 系 人：')])",
                      "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                      "string(//span[contains(string(),'联系人：')])"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [''],
            "xpath": ["//span[contains(string(),'联系电话：')]/following-sibling::*",
                      "//td[contains(string(),'联系电话：')]/following-sibling::*[1]",
                      "//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//p"]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ["//span[contains(string(),'招标代理机构：')]", "//span[contains(string(),'采购代理机构：')]",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ["//span[contains(string(),'价：')]/following-sibling::*[1]"]
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },# 已修
    "南方电网电子采购交易平台-工程-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": ['项目编号：</span>(.*?)(?=）|<)'],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": ['招标人[：|为](.*?)</span>', '招标人[：|为](.*?)</span></span>'],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['人民币(.*?万元)'],
            "xpath": ['//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": ['联<.*?>系<.*?>人：(.*?)</p>'],
            "xpath": ["//span[contains(text(),'招 标 人')]", "//span[contains(text(),'招标人名称')]",
                      "//span[contains(text(),'招标人')]",
                      "//span[text()='招标人信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采购人')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采 购')]/following-sibling::span",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联']/../..",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'招')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'采 购')]/following-sibling::span[1]"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": ['电<.*?>话：(.*?)招标代理机构'],
            "xpath": ["//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//p"]
        },  # 正文
        "bid_finish_time": {
            "re": ['开标时间[\s\S]*?时间：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": ['截止时间：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": ['概况：([\s\S]*?)（二）', '概况：([\s\S]*?)</p>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.*?)</span>(?=</span>|</p>)'],
            "xpath": ["//span[contains(text(),'招标代理机构')]", "//span[contains(text(),'采购代理机构')]",
                      "//span[text()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      "//span[contains(text(),'代理')]/../.."]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": ['投标人资格要求</strong>([\s\S]*?)<strong'],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "南方电网电子采购交易平台-服务-公示公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": ['采购项目编号：(.+?)(?=）|<)'],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": [''],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]"
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[contains(string(), '成交单位')]/../following::*/td[count(//td[contains(string(), '成交单位')]/preceding-sibling::td) + 1]",
                "//span[contains(string(),'招 标 人：')]",
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
            ]
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [''],
            "xpath": ["string(//span[contains(string(),'联 系 人：')])",
                      "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                      "string(//span[contains(string(),'联系人：')])"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [''],
            "xpath": ["//span[contains(string(),'联系电话：')]/following-sibling::*",
                      "//td[contains(string(),'联系电话：')]/following-sibling::*[1]",
                      "//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//p"]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ["//span[contains(string(),'招标代理机构：')]", "//span[contains(string(),'采购代理机构：')]",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ["//span[contains(string(),'价：')]/following-sibling::*[1]"]
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },# 已修
    "南方电网电子采购交易平台-服务-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h3']
        },  # 项目标题
        "project_number": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号  需正则两步以上
        "tender_unit": {
            "re": [''],
            "xpath": ["//span[contains(string(),'招 标 人：')]", "//p[contains(string(),'采 购 人：')]", "//span[contains(string(),'采 购 人：')]", ]
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [''],
            "xpath": ["//p[contains(string(),'联 系 人：')]"]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [''],
            "xpath": ["//span[contains(text(),'电话')]/..", "//span[contains(text(),'电  话')]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'联系方式')]/../following-sibling::p//span[contains(text(),'电话')]/..",
                      "//span[contains(text(),'招标人')]/../../../following-sibling::p//span[text()='联系方式：']/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../../following-sibling::p//span[contains(text(),'联')]/../following-sibling::span[1]",
                      "//span[contains(text(),'联系方式')]/../../following-sibling::p//span[contains(text(),'电')]/..",
                      "//span[contains(text(),'联系电话：')]/../following-sibling::span[1]"]
        },  # 联系电话  需正则两步以上
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//th[contains(text(),"项目类型")]/following-sibling::td[1]']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ["//div[@class='edit-container']"]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间  需正则两步以上
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间  需正则两步以上
        "project_overview": {
            "re": [''],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ["//span[contains(text(),'招标代理机构')]", "//span[contains(text(),'采购代理机构')]",
                      "//span[text()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      "//span[contains(text(),'代理')]/../.."]
        },  # 代理机构  需正则两步以上
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3

    },
    "广州国企阳光采购服务平台-变更澄清公告": {
      "project_title": {
        "re": ["", ""],
        "xpath": ["//h4"]
      },

      "project_number": {
        "re": ["", ""],
        "xpath": ["//span[text()='采购编号']/ancestor::td[1]/following-sibling::td[1]",
                  "//span[contains(text(),'项目编号')]/..", "//span[contains(text(),'项目编号')]"]
      },

      "tender_unit": {
        "re": ["", ""],
        "xpath": ["//span[contains(text(),'招标人名称')]", "//span[contains(text(),'招标代理机构：')]/following-sibling::span[1]",
                  "//span[contains(text(),'采购人名称：')]"]
      },

      "tender_price": {
        "re": ["", ""],
        "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]", "//span[contains(text(),'最高限价：')]",
                  "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                  "//span[contains(text(),'最高限价：')]/following-sibling::span[1]"]
      },

      "publish_time": {
        "re": ["", ""],
        "xpath": ["//h4/following-sibling::p[1]/span[1]"]
      },

      "project_leader": {
        "re": ["", ""],
        "xpath": ["//span[contains(text(),'联系人：')]", "//span[contains(text(),'联 系 人：')]",
                  "//span[contains(text(),'招标代理机构联系人：')]",
                  "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系人')]/ancestor::p[1]"]
      },

      "phone": {
        "re": ["", ""],
        "xpath": [
            "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'电话：')]/ancestor::p[1]",
            "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]"]
      },

      "project_location": {
        "re": ["", ""],
        "xpath": [
            "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
            "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]"]
      },

      "industry_type": {
        "re": ["", ""],
        "xpath": ["//span[contains(text(),'项目类别')]"]
      },

      "article_url": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "source": {
        "re": ["", ""],
        "xpath": ["//h4/following-sibling::p[1]/span[1]"]
      },

      "content": {
        "re": ["", ""],
        "xpath": ["//div[@class='content_txt']"]
      },

      "bid_start_time": {
        "re": ["", ""],
        "xpath": [
            "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
      },

      "bid_end_time": {
        "re": ["", ""],
        "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                  "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
      },

      "project_overview": {
        "re": ["", ""],
        "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]"]
      },

      "agency": {
        "re": ["", ""],
        "xpath": [
            "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
            "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
      },

      "bid_evaluation_rule": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "bid_winner": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "win_bid_price": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "win_bid_announcement_time": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "channel": {
        "re": ["", ""],
        "xpath": ["//strong[text()='当前位置：']/../.."]
      },

      "attachment_url": {
        "re": ["", ""],
        "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
      },

      "keyword": {
        "re": ["", ""],
        "xpath": ["//div[@class='content_txt']"]
      },

      "harvested_time": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "spare_1": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "spare_2": {
        "re": ["", ""],
        "xpath": ["", ""]
      },

      "spare_3": {
        "re": ["", ""],
        "xpath": ["", ""]
      },
    },
    "广州国企阳光采购服务平台-采购公告": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h4"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//span[text()='采购编号']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'项目编号')]/..", "//span[contains(text(),'项目编号')]"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'招标人名称')]",
                      "//span[contains(text(),'招标代理机构：')]/following-sibling::span[1]",
                      "//span[contains(text(),'采购人名称：')]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'联系人：')]", "//span[contains(text(),'联 系 人：')]",
                      "//span[contains(text(),'招标代理机构联系人：')]",
                      "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系人')]/ancestor::p[1]"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目类别')]"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                      "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//strong[text()='当前位置：']/../.."]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "广州国企阳光采购服务平台-采购结果公告": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h4"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/following-sibling::span[1]", "//span[contains(text(),'项目编号')]",
                      "//span[contains(text(),'项目编号')]/.."]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人名称：')]/ancestor::p[1]",
                      "//span[contains(text(),'采购人: ')]/ancestor::p[1]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人名称：')]/ancestor::p[1]",
                      "//span[contains(text(),'采购人: ')]/ancestor::p[1]"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'联系方式：')]/ancestor::p[1]",
                      "//span[contains(text(),'联系电话')]/ancestor::p[1]"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目类别')]"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                      "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//strong[text()='当前位置：']/../.."]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "广州国企阳光采购服务平台-采购结果公示": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h4"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//span[text()='采购编号']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'项目编号')]/..", "//span[contains(text(),'项目编号')]"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'招标人名称')]",
                      "//span[contains(text(),'招标代理机构：')]/following-sibling::span[1]",
                      "//span[contains(text(),'采购人名称：')]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'联系人：')]", "//span[contains(text(),'联 系 人：')]",
                      "//span[contains(text(),'招标代理机构联系人：')]",
                      "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系人')]/ancestor::p[1]"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'电话：')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'联系电话：')]/ancestor::p[1]"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目类别')]"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                      "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标') and contains(text(),'人') and contains(text(),'信息')]/ancestor::p[1]/following-sibling::*//span[text()='单位名称']/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[text()='中标候选人']/ancestor::tr[1]/following-sibling::tr//span[text()='单位名称']/ancestor::tr[1]/td[2]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='报价人名称']/ancestor::tr[1]/following-sibling::tr[1]/td[2]//span[last()]",
                "//span[contains(text(),'成交供应商候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='单位名称']/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'中标候选人')]/ancestor::p[1]/following-sibling::*//span[text()='投标单位']/ancestor::tr[1]/following-sibling::tr[1]/td[2]//span[last()]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='投标人名称']/ancestor::td[1]/following-sibling::td[1]//span[last()]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='中标人候选人']/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标候选人')]/ancestor::p[1]/following-sibling::p[1]//span[last()]"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标') and contains(text(),'人') and contains(text(),'信息')]/ancestor::p[1]/following-sibling::*//span[text()='单位名称']/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[text()='中标候选人']/ancestor::tr[1]/following-sibling::tr//span[text()='投标总价（万元）']/ancestor::tr[1]/td[2]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='报价人名称']/ancestor::tr[1]/following-sibling::tr[1]/td[3]",
                "//span[contains(text(),'中标候选人')]/ancestor::p[1]/following-sibling::*//span[text()='投标单位']/ancestor::tr[1]/following-sibling::tr[1]/td[3]//span[last()]",
                "//span[contains(text(),'成交供应商候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='单位名称']/ancestor::tr[1]/following-sibling::tr[1]/td[2]//span[last()]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='投标报价（元）']/ancestor::td[1]/following-sibling::td[1]",
                "//span[contains(text(),'候选人信息')]/ancestor::p[1]/following-sibling::*//span[text()='中标人候选人']/ancestor::tr[1]/following-sibling::tr[1]/td[2]//span[last()]",
                "//span[text()='中标候选人']/ancestor::tr[1]/following-sibling::tr//span[text()='单位名称']/ancestor::tr[1]/following-sibling::tr[1]/td[2]"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//strong[text()='当前位置：']/../.."]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "广州国企阳光采购服务平台-城轨采购网公告": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h4"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购编号：')]/..", "//span[contains(text(),'项目编号')]/..",
                      "//span[contains(text(),'项目编号')]", "//p[contains(text(),'项目编号：')]"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人：')]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]",
                      "//span[contains(text(),'控制价：')]/../span[contains(text(),'元')]/.."]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人名称：')]/ancestor::p[1]",
                      "//span[contains(text(),'采购人: ')]/ancestor::p[1]",
                      "//span[contains(text(),'联系人：')]/ancestor::p[1]", "//span[contains(text(),'采购人：')]",
                      "//span[contains(text(),'联系人')]/ancestor::p[1]"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'联系方式：')]/ancestor::p[1]",
                      "//span[contains(text(),'联系电话')]/ancestor::p[1]",
                      "//span[contains(text(),'电话')][not(contains(text(),'事宜'))]/ancestor::p[1]",
                      "//p[contains(text(),'电话')][not(contains(text(),'事宜'))]"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'地址')][not(contains(text(),'电子设备') or contains(text(),'事宜'))]",
                "//p[contains(text(),'地址')][not(contains(text(),'串通'))]"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目类别')]"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                      "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]",
                      "//span[contains(text(),'项目概况')]/ancestor::p[@class='western'][1]/following-sibling::p[1]"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'中标单位')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'推荐中价候选人名称')]/ancestor::p[1]/following-sibling::p[1]//span[last()]",
                "//p[contains(text(),'推荐中价候选人名称：')]/span",
                "//tbody//span[text()='中标候选人']/ancestor::tbody[1]//span[text()='单位名称']/ancestor::td[1]/following-sibling::td[1]",
                "//span[contains(text(),'推荐中价候选人名称：')]/ancestor::span[1]/following-sibling::span[1]//span[last()]"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'中标单位')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'推荐中价候选人名称')]/ancestor::p[1]/following-sibling::p[1]//span[last()]",
                "//tbody//span[text()='中标候选人']/ancestor::tbody[1]//span[contains(text(),'投标报价')]/ancestor::td[1]/following-sibling::td[1]",
                "//span[contains(text(),'推荐中价候选人名称：')]/ancestor::span[1]/following-sibling::span[last()]//span[last()]"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//strong[text()='当前位置：']/../.."]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "广州国企阳光采购服务平台-广州发展电子采购平台公告": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//h4"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购编号：')]/..", "//span[contains(text(),'项目编号')]/..",
                      "//span[contains(text(),'项目编号')]", "//p[contains(text(),'项目编号：')]"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人：')]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]",
                      "//span[contains(text(),'控制价：')]/../span[contains(text(),'元')]/.."]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'采购人名称：')]/ancestor::p[1]",
                      "//span[contains(text(),'采购人: ')]/ancestor::p[1]",
                      "//span[contains(text(),'联系人：')]/ancestor::p[1]", "//span[contains(text(),'采购人：')]",
                      "//span[contains(text(),'联系人')]/ancestor::p[1]", "//p[contains(text(),'联系人')]"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'联系方式：')]/ancestor::p[1]",
                      "//span[contains(text(),'联系电话')]/ancestor::p[1]",
                      "//span[contains(text(),'电话')][not(contains(text(),'事宜'))]/ancestor::p[1]",
                      "//p[contains(text(),'电话')][not(contains(text(),'事宜'))]"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'联系事项')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'地址')]/ancestor::p[1]",
                "//span[contains(text(),'地址')][not(contains(text(),'电子设备') or contains(text(),'事宜'))]",
                "//p[contains(text(),'地址')][not(contains(text(),'串通'))]"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目类别')]"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'开标') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'截止') and contains(text(),'时间')]/span",
                      "//span[contains(text(),'截止') and contains(text(),'月') and contains(text(),'年') and contains(text(),'时间')]"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//span[contains(text(),'项目概况')]/ancestor::p[contains(@style,'text')][1]/following-sibling::p[1]",
                      "//span[contains(text(),'项目概况')]/ancestor::p[@class='western'][1]/following-sibling::p[1]"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'联系方式')]/ancestor::h2[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::p//span[contains(text(),'招标代理机构名称')]/ancestor::p[1]",
                "//span[contains(text(),'联系方式')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'代理机构')]/following-sibling::span[1]"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'中标单位')]/ancestor::tr[1]/following-sibling::tr[1]/td[1]//span[last()]",
                "//span[contains(text(),'推荐中价候选人名称')]/ancestor::p[1]/following-sibling::p[1]//span[last()]",
                "//p[contains(text(),'推荐中价候选人名称：')]/span",
                "//tbody//span[text()='中标候选人']/ancestor::tbody[1]//span[text()='单位名称']/ancestor::td[1]/following-sibling::td[1]",
                "//span[contains(text(),'推荐中价候选人名称：')]/ancestor::span[1]/following-sibling::span[1]//span[last()]",
                "//tbody//p[text()='公示内容']/ancestor::tbody[1]//p[text()='单位名称']/ancestor::td[1]/following-sibling::td[1]"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": [
                "//span[contains(text(),'中标人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'中标人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交人信息')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'成交人')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'成交供应商候选人')]/ancestor::p[1]/following-sibling::*//span[contains(text(),'单位名称')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'中标单位')]/ancestor::tr[1]/following-sibling::tr[1]/td[2]",
                "//span[contains(text(),'推荐中价候选人名称')]/ancestor::p[1]/following-sibling::p[1]//span[last()]",
                "//tbody//span[text()='中标候选人']/ancestor::tbody[1]//span[contains(text(),'投标报价')]/ancestor::td[1]/following-sibling::td[1]",
                "//span[contains(text(),'推荐中价候选人名称：')]/ancestor::span[1]/following-sibling::span[last()]//span[last()]",
                "//tbody//p[text()='公示内容']/ancestor::tbody[1]//p[contains(text(),'投标报价')]/ancestor::td[1]/following-sibling::td[1]"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//h4/following-sibling::p[1]/span[1]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//strong[text()='当前位置：']/../.."]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[contains(text(),'相关附件')]/following-sibling::ul"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@class='content_txt']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "中国能建电子采购平台-招标公告": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody/tr[1]"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody//td[contains(text(), '采购项目编号：')]"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody//td[contains(text(), '招标采购单位：')]"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//span[text()='最高限价']/ancestor::td[1]/following-sibling::td[1]",
                      "//span[contains(text(),'最高限价：')]",
                      "//span[contains(text(),'最高投标限价（人民币）：')]/following-sibling::span[1]",
                      "//span[contains(text(),'最高限价：')]/following-sibling::span[1]"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody//td[contains(text(), '公告发布时间：')]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@id='panelZW2']"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },  # 搜索有问题，待定
    "中国能建电子采购平台-中选公示": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']/table/tbody/tr[1]"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//td[contains(text(), '公示发布日期：')]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//td[contains(text(), '公示发布日期：')]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "中国能建电子采购平台-中标公示": {
        "project_title": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']/table/tbody/tr[1]"]
        },

        "project_number": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "tender_unit": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "tender_price": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "publish_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody//td[contains(text(), '公告发布时间：')]"]
        },

        "project_leader": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "phone": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "project_location": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "industry_type": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "article_url": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "source": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "content": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_start_time": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_end_time": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "project_overview": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "agency": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_evaluation_rule": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "bid_winner": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "win_bid_price": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "win_bid_announcement_time": {
            "re": ["", ""],
            "xpath": ["//div[@id='zwPanel']//tbody//td[contains(text(), '公告发布时间：')]"]
        },

        "channel": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "attachment_url": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "keyword": {
            "re": ["", ""],
            "xpath": ["//div[@align='center']//td[contains(text(),'公示内容：')]/pre"]
        },

        "harvested_time": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_1": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_2": {
            "re": ["", ""],
            "xpath": ["", ""]
        },

        "spare_3": {
            "re": ["", ""],
            "xpath": ["", ""]
        },
    },
    "招采云电子招投标交易平台-变更公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="xqview"]/h2']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//th[contains(text(),"招标人")]/following-sibling::td[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@class="fbsj"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": [
                '//th[contains(text(),"招标人")]/../following-sibling::tr[3]/th[contains(text(),"联系人")][1]/following-sibling::td[1]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": [
                '//th[contains(text(),"招标人")]/../following-sibling::tr[4]/th[contains(text(),"电话")][1]/following-sibling::td[1]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//th[contains(text(),"招标代理机构")]/following-sibling::td']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="wrap"]/a[last()]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # （网址一样，在菜单栏逐个点击即可）
    "招采云电子招投标交易平台-流标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="xqview"]/h2']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//span[contains(text(),"项目编号")]/../following-sibling::span',
                      '//span[contains(text(),"采购项目编号")]/../..', '//span[contains(text(),"招标编号")]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人信息")]/../../following-sibling::p[1]',
                      '//span[contains(text(),"采购人信息")]/../following-sibling::p[1]/span[1]/span[contains(text(),"名")]/../..',
                      '//span[contains(text(),"采购人")]/following-sibling::span']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@class="fbsj"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目联系人")]/../../following-sibling::p[1]',
                      '//span[contains(text(),"采购人")]/../following-sibling::p[3]/span[contains(text(),"联")]/..',
                      '//span[contains(text(),"采购人联系方式")]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人信息")]/../../following-sibling::p[3]',
                      '//span[contains(text(),"采购人联系方式")]/following-sibling::span',
                      '//span[contains(text(),"采购人")]/../following-sibling::p[4]/span[contains(text(),"电")]/..']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购代理机构信息（如有）")]/../../following-sibling::p[1]',
                      '//span[contains(text(),"采购代理机构信息")]/../../following-sibling::p[1]',
                      '//span[contains(text(),"招标代理机构名称")]', '//span[contains(text(),"招标代理机构")]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="wrap"]/a[last()]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },
    "招采云电子招投标交易平台-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="xqview"]/h2']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//span[contains(text(),"采购项目编号")]',
                      '//span[contains(text(),"项目编号")]/../following-sibling::span[1]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人名称")]',
                      '//span[contains(text(),"采购人信息")]/../../following-sibling::p[1]',
                      '//th[contains(text(),"招标人")]/following-sibling::td[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目预算金额")]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@class="fbsj"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购单位联系人")]/../following-sibling::span',
                      '//span[contains(text(),"采购人信息")]/../../following-sibling::p[3]',
                      '//th[contains(text(),"招标人")]/../following-sibling::tr[3]/th[contains(text(),"联系人")][1]/following-sibling::td[1]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购单位联系电话")]/../following-sibling::span',
                      '//span[contains(text(),"采购人信息")]/../../following-sibling::p[3]',
                      '//th[contains(text(),"招标人")]/../following-sibling::tr[4]/th[contains(text(),"电话")][1]/following-sibling::td[1]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目概况")]/../../following-sibling::p[1]']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购代理机构全称")]/../following-sibling::span',
                      '//span[contains(text(),"采购代理机构信息")]/../../following-sibling::p[1]',
                      '//th[contains(text(),"招标代理机构")]/following-sibling::td']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="wrap"]/a[last()]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # （网址一样，在菜单栏逐个点击即可）
    "招采云电子招投标交易平台-中标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="xqview"]/h2', '//span[contains(text(),"项目名称")]/../..']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//div[@class="viewcon"]/p[1]', '//span[contains(text(),"项目编号")]/../..']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[contains(text(),"采购人名称")]', '//span[contains(text(),"采购人信息")]/../following-sibling::p[1]',
                      '//div[@class="viewcon"]/p[2]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@class="fbsj"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//td[contains(text(),"采购人联系方式")]', '//span[contains(text(),"采购人信息")]/../following-sibling::p[3]',
                      '//div[@class="viewcon"]/p[2]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//td[contains(text(),"采购人联系方式")]', '//span[contains(text(),"采购人信息")]/../following-sibling::p[3]',
                      '//div[@class="viewcon"]/p[2]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//td[contains(text(),"采购代理机构全称")]',
                      '//span[contains(text(),"采购代理机构信息")]/../../following-sibling::p[1]',
                      '//div[@class="viewcon"]/p[2]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['//td[contains(text(),"成交供应商名称")]/../following-sibling::tr[1]/td[1]',
                      '//span[contains(text(),"供应商名称")]/../..', '//div[@class="viewcon"]/p[1]']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['//td[contains(text(),"成交供应商名称")]/../following-sibling::tr[1]/td[3]',
                      '//span[contains(text(),"中标（成交）金额")]/../..', '//div[@class="viewcon"]/p[1]']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="wrap"]/a[last()]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },
    "招采云电子招投标交易平台-中标公示": {
        "project_title": {
            "re": [''],
            "xpath": ['//div[@class="xqview"]/h2']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标人")][not(contains(text(),"联系人"))]/../../../following-sibling::td[1]',
                      '//span[contains(text(),"招标人")]/../following-sibling::td[1]',
                      '//span[contains(text(),"招")][not(contains(text(),"标"))]/..',
                      '//span[contains(text(),"业主单位名称")]/../../../following-sibling::td']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//p[@class="fbsj"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标人联系人")]/../../../following-sibling::td[1]',
                      '//span[contains(text(),"招标人联系方式")]/../following-sibling::span[1]',
                      '//span[contains(text(),"业主单位联系人")]/../../../following-sibling::td']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": [
                '//span[contains(text(),"招标人联系人")]/../../../../following-sibling::tr[1]/td[1]//span[contains(text(),"联系电话")]/../../../following-sibling::td[1]',
                '//span[contains(text(),"招标人联系方式")]/../following-sibling::span[3]',
                '//span[contains(text(),"业主单位联系电话")]/../../../following-sibling::td']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['//span[contains(text(),"开标时间")]/../following-sibling::td[1]',
                      '//span[contains(text(),"开标时间")]/../../../following-sibling::td']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标代理机构")]/../following-sibling::td[1]',
                      '//span[contains(text(),"代理机构")][not(contains(text(),"联系"))][not(contains(text(),"地址"))]',
                      '//span[contains(text(),"招标代理机构")][not(contains(text(),"经理"))][not(contains(text(),"联系人"))]/../../../following-sibling::td']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['//span[contains(text(),"第一中标候选人")]/../../../following-sibling::td[1]',
                      '//span[contains(text(),"排名")]/../../following-sibling::tr[1]/td[1]//span[contains(text(),"1")]/../following-sibling::td[1]',
                      '//span[contains(text(),"第一中标候选人")]/../../following-sibling::p[1]',
                      '//span[contains(text(),"第一中标候选人")]/../../../following-sibling::td[1]']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['//span[contains(text(),"第一中标候选人")]/../../../following-sibling::td[2]',
                      '//span[contains(text(),"排名")]/../../following-sibling::tr[1]/td[1]//span[contains(text(),"1")]/../following-sibling::td[3]',
                      '//span[contains(text(),"第一中标候选人")]/../../following-sibling::p[3]',
                      '//span[contains(text(),"第一中标候选人")]/../../../following-sibling::td[2]']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="wrap"]/a[last()]']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="viewcon"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # （网址一样，在菜单栏逐个点击即可）
    "中国通用招标网-变更公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h1[@class="TxtCenter Padding10 Top15']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//span[contains(text(),"采购编号")]/ancestor::p/../following-sibling::td',
                      '//SPAN[CONTAINS(TEXT(),"项目编号")]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人名称")]/ancestor::p/../following-sibling::td',
                      '//span[contains(text(),"采购人：")]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": [
                '//span[contains(text(),"采购人")]/../../../../../../following-sibling::p[2]//span[contains(text(),"联系人")]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目联系人")]/ancestor::p/../following-sibling::td',
                      '//span[contains(text(),"采购人")]/../../../../../../following-sibling::p[3]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//span[contains(text(),"所属行业")]/span']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]', '']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购代理机构")]/ancestor::p/../following-sibling::td',
                      '//span[contains(text(),"采购代理机构")]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 项目行业类型只有列表有，空的就是没的
    "中国通用招标网-结果公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//h1[@class="TxtCenter Padding10 Top15']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//span[contains(text(),"采购编号")]', '//span[contains(text(),"招标编号为")]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人：")]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人联系方式")]', '//span[contains(text(),"联系人")]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人联系方式")]/../../../../following-sibling::p',
                      '//span[contains(text(),"联系电话")]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//span[contains(text(),"所属行业")]/span']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购代理机构全称")]', '//div[@class="Contnet Jknr"]',
                      '//span[contains(text(),"代理机构")]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['//span[contains(text(),"第一包")]/../../../../following-sibling::p[1]/span']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 项目行业类型只有列表有，空的就是没的
    "中国通用招标网-招标采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//H1[@class="TxtCenter Padding10 Top15"]']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//SPAN[CONTAINS(TEXT(),"采购编号")]', '//p[contains(text(),"项目编号")]',
                      '//span[contains(text(),"招标编号")]/..']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购人")][not(contains(text(),"地址"))]', '//span[contains(text(),"招标人：")]',
                      '//span[contains(text(),"招 标 人")]/../..']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购预算")]/../../../../../../../../../following-sibling::tr/td[3]',
                      '//span[contains(text(),"含税最高限价")]/../../../following-sibling::tr/td[5]',
                      '//span[contains(text(),"本项目预算")]/../..']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目负责人")]',
                      '//span[contains(text(),"招标人")]/../following-sibling::p[2]/span[contains(text(),"联系人")]',
                      '//span[contains(text(),"招 标 人"")]/../../../../../following-sibling::P[2]//span[contains(text(),"联 系 人")]/../..']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目负责人")]',
                      '//span[contains(text(),"招标人")]/../following-sibling::p[3]/span[contains(text(),"电话")]',
                      '//span[contains(text(),"招 标 人")]/../../../../../following-sibling::P[3]//span[contains(text(),"电")]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//span[contains(text(),"项目所在地区")]']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//span[contains(text(),"所属行业")]/span']  # 项目行业类型只有列表有，空的就是没的
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"采购代理机构")][not(contains(text(),"地址"))][not(contains(text(),"联系"))]',
                      '//span[contains(text(),"招标代理机构：")]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 项目行业类型只有列表有，空的就是没的
    "中国通用招标网-资格预审": {
        "project_title": {
            "re": [''],
            "xpath": ['//H1[@class="TxtCenter Padding10 Top15"]']
        },  # 项目标题
        "project_number": {
            "re": ['<b>\[(.*?)\]</b'],
            "xpath": ['//p[contains(text(),"招标编号")]', '//div[contains(text(),"招标编号")]']
        },  # 项目编号
        "tender_unit": {
            "re": [''],
            "xpath": ['//span[contains(text(),"审 查 人")]/..', '//p[contains(text(),"招标人：")]',
                      '//div[contains(text(),"资格预审单位")]/../following-sibling::td[1]/div[1]',
                      '//div[contains(text(),"招标人：")]', '//a[contains(text(),"招标人")]/../../../following-sibling::tr[1]']
        },  # 招标单位
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//div[@class="Padding10 TxtCenter Gray BorderTopDot Top10"]']
        },  # 发布时间
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@height="222"]//span[contains(text(),"联 系 人")]/..',
                      '//p[contains(text(),"招标人：")]/../../following-sibling::tr[1]/td[1]',
                      '//div[contains(text(),"联系人")]/../following-sibling::td[1]/div[1]',
                      '//div[contains(text(),"招标人：")]/../../following-sibling::tr[1]/td[1]',
                      '//div[contains(text(),"联系人")]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//td[@height="222"]//span[contains(text(),"电  ")]/..',
                      '//p[contains(text(),"招标人：")]/../../following-sibling::tr[2]/td[1]',
                      '//div[contains(text(),"联系人")]/../following-sibling::td[3]/div[1]',
                      '//div[contains(text(),"招标人：")]/../../following-sibling::tr[2]/td[1]',
                      '//div[contains(text(),"电话")]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['']
        },  # 项目所在地
        "industry_type": {
            "re": [''],
            "xpath": ['//span[contains(text(),"所属行业")]/span']
        },  # 项目行业类型
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章URL
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来源
        "content": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ['']
        },  # 开标时间
        "bid_end_time": {
            "re": ['投标时间[\s\S]*?结束：([\s\S]*?)<'],
            "xpath": ['']
        },  # 投标截止时间
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概况
        "agency": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标代理机构")]/..', '//p[contains(text(),"招标代理机构")]',
                      '//div[contains(text(),"资格预审单位")]/../following-sibling::td[1]/div[2]',
                      '//div[contains(text(),"招标人：")]/../following-sibling::td',
                      '//div[contains(text(),"招标代理机构")]/../../following-sibling::tr[1]']
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规则
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标人
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频道
        "attachment_url": {
            "re": [''],
            "xpath": ['']
        },  # 附件链接
        "keyword": {
            "re": [''],
            "xpath": ['//div[@class="Contnet Jknr"]']
        },  # 关键词
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时间
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段1
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段2
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 项目行业类型只有列表有，空的就是没的
    "广东能源商务网-工程招标": {
        "project_title": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "标题")]/following-sibling::*[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标编号")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单号")]/following-sibling::*[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标单位")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单位")]/following-sibling::*[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//td[@class="tabledowntitle"][contains(string(), "发布时间")]/following-sibling::*[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "采购联系人")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(),"提交人")]/following-sibling::*[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "采购手机号码")]/following-sibling::*[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "地区")]/following-sibling::*[1]']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "所属行业")]/following-sibling::*[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//span[text()="招标公告"]/../../../following-sibling::tr[1]']
        },  # 正
        "bid_start_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "开始时间")]/following-sibling::*[1]']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "结束时间")]/following-sibling::*[1]']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"项目概况")]/following-sibling::*[1]']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    # "广东能源商务网-煤炭灰、石膏招标公告": {
    #     "project_title": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
    #     },  # 项目标
    #     "project_number": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"招标编号")]/following-sibling::*[1]']
    #     },  # 项目编
    #     "tender_unit": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"招标单位")]/following-sibling::*[1]']
    #     },  # 招标单
    #     "tender_price": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 标的金
    #     "publish_time": {
    #         "re": [''],
    #         "xpath": [
    #             '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
    #     },  # 发布时
    #     "project_leader": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]']
    #     },  # 招标项目负责
    #     "phone": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
    #     },  # 联系电
    #     "project_location": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
    #     },  # 项目所在
    #     "industry_type": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
    #     },  # 项目行业类
    #     "article_url": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 文章UR
    #     "source": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 信息来
    #     "content": {
    #         "re": [''],
    #         "xpath": ['//span[text()="招标公告"]/../../../following-sibling::tr[1]']
    #     },  # 正
    #     "bid_start_time": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
    #     },  # 开标时
    #     "bid_end_time": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
    #     },  # 投标截止时
    #     "project_overview": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 项目概
    #     "agency": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 代理机
    #     "bid_evaluation_rule": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 评标规
    #     "bid_winner": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标
    #     "win_bid_price": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标金
    #     "win_bid_announcement_time": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标公告发布时
    #     "channel": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 所属频
    #     "attachment_url": {
    #         "re": [''],
    #         "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
    #     },  # 附件链
    #     "keyword": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 关键
    #     "harvested_time": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 采集时
    #     "spare_1": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 跟进记
    #     "spare_2": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 跟进
    #     "spare_3": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 预留字段3
    # },  # 无数据
    # "广东能源商务网-煤炭招标公告": {
    #     "project_title": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
    #     },  # 项目标
    #     "project_number": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"招标编号")]/following-sibling::*[1]']
    #     },  # 项目编
    #     "tender_unit": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"招标单位")]/following-sibling::*[1]']
    #     },  # 招标单
    #     "tender_price": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 标的金
    #     "publish_time": {
    #         "re": [''],
    #         "xpath": [
    #             '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
    #     },  # 发布时
    #     "project_leader": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]']
    #     },  # 招标项目负责
    #     "phone": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
    #     },  # 联系电
    #     "project_location": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
    #     },  # 项目所在
    #     "industry_type": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
    #     },  # 项目行业类
    #     "article_url": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 文章UR
    #     "source": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 信息来
    #     "content": {
    #         "re": [''],
    #         "xpath": ['//span[text()="招标公告"]/../../../following-sibling::tr[1]']
    #     },  # 正
    #     "bid_start_time": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
    #     },  # 开标时
    #     "bid_end_time": {
    #         "re": [''],
    #         "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
    #     },  # 投标截止时
    #     "project_overview": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 项目概
    #     "agency": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 代理机
    #     "bid_evaluation_rule": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 评标规
    #     "bid_winner": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标
    #     "win_bid_price": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标金
    #     "win_bid_announcement_time": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 中标公告发布时
    #     "channel": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 所属频
    #     "attachment_url": {
    #         "re": [''],
    #         "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
    #     },  # 附件链
    #     "keyword": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 关键
    #     "harvested_time": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 采集时
    #     "spare_1": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 跟进记
    #     "spare_2": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 跟进
    #     "spare_3": {
    #         "re": [''],
    #         "xpath": ['']
    #     },  # 预留字段3
    # },  # 无数据
    "广东能源商务网-物资招标": {
        "project_title": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标编号")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单号")]/following-sibling::*[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标单位")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单位")]/following-sibling::*[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(),"提交人")]/following-sibling::*[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//span[text()="招标公告"]/../../../following-sibling::tr[1]']
        },  # 正
        "bid_start_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"项目概况")]/following-sibling::*[1]']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    "广东能源商务网-已完成的采购": {
        "project_title": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标编号")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单号")]/following-sibling::*[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标单位")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单位")]/following-sibling::*[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(),"提交人")]/following-sibling::*[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ['//span[text()="招标公告"]/../../../following-sibling::tr[1]']
        },  # 正
        "bid_start_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"项目概况")]/following-sibling::*[1]']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    "广东能源商务网-招标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标编号")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单号")]/following-sibling::*[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标单位")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单位")]/following-sibling::*[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(),"提交人")]/following-sibling::*[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ["//td[@class='searchborder']"]
        },  # 正
        "bid_start_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"项目概况")]/following-sibling::*[1]']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
    "广东能源商务网-中标公告": {
        "project_title": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"标题")]/following-sibling::*[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标编号")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单号")]/following-sibling::*[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(), "招标单位")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(), "询价单位")]/following-sibling::*[1]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": [
                '//td[@class="tabledowntitle"][contains(string(),"发布时间")]/following-sibling::*[1]']
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购联系人")]/following-sibling::*[1]',
                      '//td[@class="tabledowntitle"][contains(string(),"提交人")]/following-sibling::*[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"采购手机号码")]/following-sibling::*[1]']
        },  # 联系电
        "project_location": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"地区")]/following-sibling::*[1]']
        },  # 项目所在
        "industry_type": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"所属行业")]/following-sibling::*[1]']
        },  # 项目行业类
        "article_url": {
            "re": [''],
            "xpath": ['']
        },  # 文章UR
        "source": {
            "re": [''],
            "xpath": ['']
        },  # 信息来
        "content": {
            "re": [''],
            "xpath": ["//td[@class='searchborder']"]
        },  # 正
        "bid_start_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"开始时间")]/following-sibling::*[1]']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"结束时间")]/following-sibling::*[1]']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"项目概况")]/following-sibling::*[1]']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"中标单位")]/following-sibling::*[1]']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['//td[@class="tabledowntitle"][contains(string(),"中标金额")]/following-sibling::*[1]']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//tbody/tr[contains(@class,"tr")]/td/a']
        },  # 附件链
        "keyword": {
            "re": [''],
            "xpath": ['']
        },  # 关键
        "harvested_time": {
            "re": [''],
            "xpath": ['']
        },  # 采集时
        "spare_1": {
            "re": [''],
            "xpath": ['']
        },  # 跟进记
        "spare_2": {
            "re": [''],
            "xpath": ['']
        },  # 跟进
        "spare_3": {
            "re": [''],
            "xpath": ['']
        },  # 预留字段3
    },  # 已修
}
