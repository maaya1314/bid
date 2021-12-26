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

    },
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

    },
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

    },
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
    },
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
            "xpath": ['//div[@id=“main”]/div/h3']
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
            "xpath": ['//div[@id="container"]/div[@id="main"]']
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
            "xpath": ['//span[contains(text(),"招标机构：")]/..','//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="名称："]/../following-sibling::span[1]']
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
            "xpath": ['//span[contains(text(),"联系人")]/../..','//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="联系人："]/../following-sibling::span[1]']
        },  # 招标项目负责人
        "phone": {
            "re": [''],
            "xpath": ['//span[contains(text(),"联系人")]/../..','//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="系方式"]/../following-sibling::span[1]']
        },  # 联系电话
        "project_location": {
            "re": [''],
            "xpath": ['//span[contains(text(),"招标单位信息")]/../../../following-sibling::p/span/span[text()="地址："]/../following-sibling::span[1]']
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
            "xpath": ['//span[contains(text(),"招标代理机构")]/../..','//span[contains(text(),"代理机构信息")]/../../../following-sibling::p/span/span[text()="代理机构："]/../following-sibling::span[1]']
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
            "xpath": ['']
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
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目负责人：")]/following-sibling::td[1]',
                      '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目经理：")]/following-sibling::td[1]',
                      '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系人：")]/following-sibling::td[1]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系电话：")]/following-sibling::td[1]',
                      '//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系方式：")]/following-sibling::td[1]']
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
            "xpath": [''] # //th[contains(text(),"中标候选单位名称")]/following-sibling::td[1] 评标不等于中标
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
                      ]
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['//th[contains(text(),"评标时间")]/following-sibling::td[1]']
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
            "xpath": ['//th[contains(text(),"采购人地址")]/following-sibling::td[1]']
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
            "xpath": ['//th[contains(text(),"标段编号")]/following-sibling::td[1]', '//th[contains(text(),"采购项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['']
        },  # 招标单位 金额单位而不是公司单位
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
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"项目经理")]/following-sibling::td[1]']
        },  # 招标项目负责人 页面上的都是投标负责人不采集
        "phone": {
            "re": [''],
            "xpath": ['//span[@class="sub-title"][text()="项目概况"]/..//th[contains(text(),"联系电话")]/following-sibling::td[1]']
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
            "xpath": ['//*[contains(text(),"项目名称")]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目编号")]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//*[contains(text(),"采购人信息")]/following-sibling::*[contains(text(),"名")]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['//*[contains(text(),"预算金额")]/span']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目联系方式")]/following-sibling::*[contains(text(),"项目联系人")]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目联系方式")]/following-sibling::*[contains(text(),"电　话")]']
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
            "re": ['获取采购文件[\s\S]*?时间[：|>](.*?)至'],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": ['获取采购文件[\s\S]*?时间[：|>].*?至(.*?)[<|（]'],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['//*[contains(text(),"采购代理机构信息")]/following-sibling::*[contains(text(),"名")]']
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
            "xpath": ['//p[contains(text(),"当前位置")]']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a']
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
            "xpath": ['//p[contains(text(),"项目名称")]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目编号")]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//p[contains(text(),"采购人信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电")]']
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
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
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
            "xpath": ['//p[contains(text(),"当前位置")]']
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

    },
    "中国采购网-中央单位采购公告": {
        "project_title": {
            "re": [''],
            "xpath": ["//h2[@class='tc']", '//strong[contains(text(),"项目名称")]/../span']
        },  # 项目标
        "project_number": {
            "re": ['项目编号：(.*?)[（|<]'],
            "xpath": ['//strong[contains(text(),"项目编号")]/../span']
        },  # 项目编
        "tender_unit": {
            "re": ['预算金额：.*?(万元|元).*?<'],
            "xpath": ['']
        },  # 招标单位
        "tender_price": {
            "re": ['>预算金额：(.*?)<'],
            "xpath": ['']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": ['项目联系人：(.*?)[（|<]'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"项目联系人")]',
                      '//div[contains(text(),"项目联系人")]/following-sibling::div[1]']
        },  # 招标项目负责
        "phone": {
            "re": ['电　话：(.*?)[<|，]'],
            "xpath": ['//p[contains(text(),"项目联系方式")]/following-sibling::p[contains(text(),"电　话")]',
                      'string(//div[contains(text(),"项目联系方式")]/following-sibling::div[1])']
        },  # 联系电
        "project_location": {
            "re": ['地　址：(.*?)[（|<]'],
            "xpath": ['//div[contains(text(),"地址：")]/following-sibling::div[1]']
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
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概
        "agency": {
            "re": ['采购代理机构信息[\s\S]*?名 称：(.*?)[（|<]'],
            "xpath": ['//p[contains(text(),"采购代理机构信息")]/following-sibling::p[contains(text(),"名")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": ['供应商名称：(.*?)[（|<]'],
            "xpath": ['']
        },  # 中标
        "win_bid_price": {
            "re": ['中标（成交）金额：(.*?)<'],
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
            "xpath": ['//*[contains(text(),"项目名称")]/following-sibling::td[1]']
        },  # 项目标
        "project_number": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目编号")]/following-sibling::td[1]']
        },  # 项目编
        "tender_unit": {
            "re": [''],
            "xpath": ['//*[contains(text(),"采购人信息")]/../../../following-sibling::p//*[contains(text(),"采购人名称")]']
        },  # 招标单
        "tender_price": {
            "re": [''],
            "xpath": ['']
        },  # 标的金
        "publish_time": {
            "re": [''],
            "xpath": ['//span[@id="pubTime"]'],
        },  # 发布时
        "project_leader": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目联系方式")]/../../../following-sibling::p//*[contains(text(),"项目联系人")]/..']
        },  # 招标项目负责
        "phone": {
            "re": [''],
            "xpath": ['//*[contains(text(),"项目联系方式")]/../../../following-sibling::p//*[contains(text(),"联系电话")]/../..']
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
            "re": [''],
            "xpath": ['']
        },  # 开标时
        "bid_end_time": {
            "re": [''],
            "xpath": ['']
        },  # 投标截止时
        "project_overview": {
            "re": [''],
            "xpath": ['']
        },  # 项目概
        "agency": {
            "re": [''],
            "xpath": ['//*[contains(text(),"采购执行机构信息")]/../../../following-sibling::p//*[contains(text(),"采购人名称")]']
        },  # 代理机
        "bid_evaluation_rule": {
            "re": [''],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [''],
            "xpath": ['//span[contains(text(),"包")][contains(text(),"公司")]']
        },  # 中标
        "win_bid_price": {
            "re": [''],
            "xpath": ['//span[contains(text(),"包")][contains(text(),"人民币")]/../following-sibling::span[1]']
        },  # 中标金
        "win_bid_announcement_time": {
            "re": [''],
            "xpath": ['']
        },  # 中标公告发布时
        "channel": {
            "re": [''],
            "xpath": ['//p[contains(text(),"当前位置")]']
        },  # 所属频
        "attachment_url": {
            "re": [''],
            "xpath": ['//td[contains(text(),"附件")]//a']
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
            "re": ['([\s\S]+?)(?=项目编号)'],
            "xpath": ['//div[@class="titleXianmu"]']
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
            "xpath": ['//span[contains(text(),"联 系 人")]', '//span[contains(text(),"联系人")]/..',
                      '//span[contains(text(),"招")]/../../following-sibling::p/span/span[contains(text(),"联")]/../..']
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
            "xpath": ['//div[text()="截止时间"]/../span']
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
            "xpath": ['//div[@id="page-wrap"]/div[@id="container"]']
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
            "xpath": ['//th[text()="项目概况"]/following-sibling::td[1]']
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
    },
    "彩云电子招标采购平台-中标公告": {
        "project_title": {
            "re": ['([\s\S]+?)(?=项目编号)'],
            "xpath": ['//div[@class="titleXianmu"]']
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
            "xpath": ['//div[text()="截止时间"]/../span']
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
    },
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
    }
}
