#!/usr/bin/env python
# -*- coding: utf-8 -*-
base_dict = {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h1[@class='s-title']",  # 中国南方电网--阳光电子商务
                "//div[@class='headline']/dl/dt",
                'string(//h3)',  # 光大
                "//div[@class='app']/h2",  # 中招
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '询价编号：(.+?)<',
                '采购单编号：(.+?)<',
                '标段（包）编号：(.+?)<',
                '项目编号：(.+?)</p',
                '招标编号：(.+?)</span></p>',
                '编号：((?!\<).+?)<',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)(采购)?项目名称',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
                '招标编号<a></a>：<span style="text-decoration:underline;">（(.*?)）',
                '项目标号：(.+?)<',

            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]",
                      '//td[contains(string(), "招标编号")]/../following::*[1]//td[count(//td[contains(string(), "招标编号")]/preceding-sibling::*) + 1]',
                      ]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招 标 人：(.+?)<',
                '招标人[：|为](.*?)</span>',
                '招标人名称：(.+?)</span></p>',
                '招标人名称：(.+?)<',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
                '采购组织：(.+?)<',
            ],
            "xpath": [
                "string(//span[text()='招标人：']/following-sibling::*[1])",
                'string(//span[contains(string(), "招标人：")]/following-sibling::*)',
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联 系 人：(.+?)<',
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                'string(//*[text()="项目联系人："]/following-sibling::*)',
                'string(//*[text()="联系人："]/following-sibling::*)',
                'string(//th[contains(string(), "联系人")]/following-sibling::*)',
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
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
        "project_location": {
            "re": [
                '招标项目所在地区：(.+?)\s'
            ],
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
            "xpath": [
                "//div[@class='form-content']",  # 中国海洋石油集团有限公司
                "//div[@class='main-text']",  # 航空工业电子采购平台
                "//div[@class='article-area']",  # 中国海洋石油集团有限公司
                "//div[@class='liststyle']",  # 大唐集团电子商务平台
                "//div[@id='moreall-gg']",  # 大唐集团电子商务平台
                "//div[@class='wrap']",  # 中招联合招标采购平台
                "//section[@class='article']",  # 西电集团电子采购平台
                "//div[@id='ninfo-con-txt']",  # 深圳市国际招标有限公司
                "//div[@class='neirong']",  # 中国一汽电子招标采购交易平台
                "//div[@class='main_top main_top_CG']",   # 中国华电集团电子商务平台
                "//div[@class='WordSection1']",  # 中招联合招标采购平台
                "//div[@class='dg-notice-detail']",  # 国家开发投资公司电子采购平台
                # "//div[@class='ewb-article-info']/table",  # 深圳市政府采网
                "//div[@class='ewb-article-info']/div[@class='body']",  # 深圳市政府采网
                # "//div[@class='ewb-article-info']//tbody",
                "//div[@class='ewb-article-info']",  # 深圳市政府采网
                "//div[@id='container']/div[@id='main']/div[@class='block'][1]|//div[@id='container']/div[@id='sidebar']/ul/div[@class='timeline']/div[@class='dotbox']",  # 光大环境招标采购电子交易平台
                "//div[@id='container']",  # 大唐集团电子商务平台
                "//div[@class='block'][1]|//div[@id='container']/div[@id='sidebar']/ul|//div[@class='ZhongBiaoContent']/ul",  # 光大环境招标采购电子交易平台
                "//div[@class='notice-content-left']",   # 云采链线上采购一体化平台
                # "//div[@class='content-header-wrapper']",  # 云采链线上采购一体化平台
                "//div[@class='Section0']",  # 国义
                "//div[@class='Section1']",
                "string(.)",
                "//p",
                "//td[@class='text_zx']",
                "//tr[@class='firstRow']/td",
            ]
        },  # 正文
        "bid_finish_time": {
            "re": [
                '报名时间[\s\S]*?开始：(.+?)<',
                '开标时间[\s\S]{,10}开始：(.+?)<',
                '开标时间变更为(.+?)(?=上午|下午)',
                '开标时间：(.+?)(?=上午|下午)',
                '开标时间：(.+?)</span></p>',
            ],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [
                '投标时间[\s\S]*?结束：(.+?)<',
                '投标时间[\s\S]{,10}结束：(.+?)<',
                '延期开标：(.+?)<',
                '现变更为.{,6}投标文件递交截止时间：(.+?)(?=（|<)',
                '投标文件递交截止时间：(.+?)(?=（|<)',
                '递交截止时间：(.+?)<',
                '截止时间：(.+?)<',
            ],
            "xpath": [
                "//span[contains(text(),'投标截止及开标时间')]",
                "//span[text()='投标文件开始递交时间：']/..",
                '//th[contains(string(), "投标文件递交截止时间")]/../following::*[1]//td[count(//th[contains(string(), "投标文件递交截止时间")]/preceding-sibling::*) + 1]',
            ]
        },  # 投标截止时间
        "project_overview": {
            "re": [
                '(项目概况和招标范围[\s\S]+?)投标人资格要求',
                '(项目概况与招标范围[\s\S]+?)投标人资格要求',
                '(项目概况[\s\S]+?)投标人资格要求',
                '项目概况([\s\S]+?)(?=一、|二、|三、|四、|五、|六、|七、|八、|九、)',
                '(项目概况与招标范围：[\s\S]+?)<strong>',
                '(项目概况：[\s\S]+?)<strong>',
                '概况：([\s\S]*?)（二）',
                # '概况：([\s\S]*?)</p>',
                '(项目概况[\s\S]*?)<strong>',
                   ],

            "xpath": [
                "//span[text()='项目概况：']/following-sibling::*[1]",
                "//label[text()=' 项目概况：']/following-sibling::*[1]",
                # "//span[contains(text(),'项目概况')]",
            ]
        },  # 项目概况
        "agency": {
            "re": [
                '招标代理机构：(.+?)<h',
                '招标代理机构：(.+?)<br',
                '招标代理机构名称：(.+?)<',
                '招标代理机构：(.+?)</span>(?=</span>|</p>)',
            ],
            "xpath": [
                "string(//span[text()='代理机构：']/following-sibling::*[1])",
                '//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]',
            ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
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
                "//label[text()=' 资格要求：']/following-sibling::*[1]",
                "//span[text()='供应商基本要求：']/following-sibling::*[1]|//span[text()='供应商资质要求：']/following-sibling::*[1]|//span[text()='供应商业绩要求：']/following-sibling::*[1]|//span[text()='供应商其他要求：']/following-sibling::*[1]",
                'string(//span[text()="供应商资质要求："]/following-sibling::*//a/@href)',
            ]
        },  # 评标规则
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                '成交供应商：(.+?)</p',
            ],
            "xpath": [
                '//*[text()="成交候选人名称："]/following-sibling::*',
                '//*[text()="中标人名称："]/following-sibling::*',
                "//*[text()='成交人名称：']/following-sibling::*[1]",
                'string(//span[contains(string(), "成交人：")]/following-sibling::*)',
                "//td[contains(string(), '中标人名称')]/../following::*[1]/td[count(//td[contains(string(), '中标人名称')]/preceding-sibling::td) + 1]",
                "//td[contains(string(), '成交供应商')]/../following::*[1]/td[count(//td[contains(string(), '成交供应商')]/preceding-sibling::td) + 1]",
                "//td[contains(string(), '中标候选人名称')]/../following::*[1]/td[count(//td[contains(string(), '中标候选人名称')]/preceding-sibling::td) + 1]",
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标人
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                "//*[text()='成交价(元)：']/following-sibling::*[1]",
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
        },  # 中标金额
        "win_bid_announcement_time": {
            "re": [
                '公告日期：(.+?)<',
            ],
            "xpath": [
                "//*[text()='公告开始时间：']/following-sibling::*[1]",
                "//*[text()='公示开始时间：']/following-sibling::*[1]",

            ]
        },  # 中标公告发布时间
        "channel": {
            "re": [''],
            "xpath": ['//div[@class="home"]']
        },  # 所属频道
        "attachment_url": {
            "re": [
                'var pdf ="(.*?)"',
            ],
            "xpath": [
                '//span[text()="附件下载："]/following-sibling::*//a/@href',
                "//a[text()='下载']/@href",
                "//a[text()='-点此下载-']/@href",
                "//*[text()='下载']/parent::*/@href",
                "//div[contains(text(), '附件') and contains(string(), 'docx')]//a/@href",
                "//a[contains(text(), '附件') and (contains(text(), 'doc') or contains(text(), 'xls') or contains(text(), 'zip'))]/@href",
                '//span[text()="附件1："]/following-sibling::*//@href',

                # "//a[contains(string(),'下载')]/@href",
                # "//iframe[@id='pdfContainer']/@src",  # 光大
            ]
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

    }
"""
@Time: 2022/4/15 4:19 下午
@Author: CZC
@File: conf_2.py
"""
parse_dict = {
    # 一期补充
    "中国能建电子采购平台-招标公告": base_dict,
    "中国能建电子采购平台-中标公示": base_dict,

    "中国华电集团电子商务平台-招标公告": base_dict,
    "中国华电集团电子商务平台-中标候选人公示": base_dict,
    "中国华电集团电子商务平台-中标结果公示": base_dict,
    "中国石油招投标网-招标公告（物质、工程、服务）": base_dict,
    "中国石油招投标网-公开招标中标候选人公示": base_dict,
    "中国石油招投标网-公开招标中标结果公示": base_dict,
    "光大环境招标采购电子交易平台-采购公告": base_dict,
    "光大环境招标采购电子交易平台-变更公告": base_dict,
    "光大环境招标采购电子交易平台-中标候选人公示": base_dict,
    "光大环境招标采购电子交易平台-采购结果公示": base_dict,
    "光大环境招标采购电子交易平台-终止公告": base_dict,
"大唐集团电子商务平台-招标公告": base_dict,
"大唐集团电子商务平台-变更公告": base_dict,
"大唐集团电子商务平台-中标候选人公示": base_dict,
"大唐集团电子商务平台-采购公告": base_dict,
"大唐集团电子商务平台-采购结果": base_dict,
"大唐集团电子商务平台-中标结果": base_dict,

"国投电子采购平台-招标（预审）公告": {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h3[@class='dg-notice-title']",
                "//div[@class='headline']/dl/dt",
                '//h3',
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '项目编号：(.+?)</p',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)项目名称',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招标人[：|为](.*?)</span>',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
            ],
            "xpath": [
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [
                '电<.*?>话：(.+?)</p',
                '联系方式：[\s\S]*?电话：(.+?)</p',
            ],
            "xpath": [
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
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
            "xpath": [
                "//div[@class='dg-notice-detail']",
                "//p",]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间
        "project_overview": {
            "re": ['(项目概况与招标范围.+?)投标人资格要求', '(项目概况与招标范围：.+?)<strong>', '(项目概况：.+?)<strong>', '概况：([\s\S]*?)（二）',
                   '概况：([\s\S]*?)</p>', '项目概况([\s\S]*?)<strong>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.+?)</span>(?=</span>|</p>)'],
            "xpath": ['//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]', ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
                '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '投标人资格要求(.+?)<strong>',

            ],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                ''
            ],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
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
"国投电子采购平台-变更公告": {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h3[@class='dg-notice-title']",
                "//div[@class='headline']/dl/dt",
                '//h3',
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '项目编号：(.+?)</p',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)项目名称',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招标人[：|为](.*?)</span>',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
            ],
            "xpath": [
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [
                '电<.*?>话：(.+?)</p',
                '联系方式：[\s\S]*?电话：(.+?)</p',
            ],
            "xpath": [
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
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
            "xpath": [
                "//div[@class='dg-notice-detail']",
                "//p",]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间
        "project_overview": {
            "re": ['(项目概况与招标范围.+?)投标人资格要求', '(项目概况与招标范围：.+?)<strong>', '(项目概况：.+?)<strong>', '概况：([\s\S]*?)（二）',
                   '概况：([\s\S]*?)</p>', '项目概况([\s\S]*?)<strong>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.+?)</span>(?=</span>|</p>)'],
            "xpath": ['//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]', ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
                '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '投标人资格要求(.+?)<strong>',

            ],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                ''
            ],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
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
"国投电子采购平台-中标候选人": {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h3[@class='dg-notice-title']",
                "//div[@class='headline']/dl/dt",
                '//h3',
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '项目编号：(.+?)</p',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)项目名称',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招标人[：|为](.*?)</span>',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
            ],
            "xpath": [
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [
                '电<.*?>话：(.+?)</p',
                '联系方式：[\s\S]*?电话：(.+?)</p',
            ],
            "xpath": [
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
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
            "xpath": [
                "//div[@class='dg-notice-detail']",
                "//p",]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间
        "project_overview": {
            "re": ['(项目概况与招标范围.+?)投标人资格要求', '(项目概况与招标范围：.+?)<strong>', '(项目概况：.+?)<strong>', '概况：([\s\S]*?)（二）',
                   '概况：([\s\S]*?)</p>', '项目概况([\s\S]*?)<strong>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.+?)</span>(?=</span>|</p>)'],
            "xpath": ['//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]', ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
                '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '投标人资格要求(.+?)<strong>',

            ],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                ''
            ],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
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
"国投电子采购平台-结果公告": {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h3[@class='dg-notice-title']",
                "//div[@class='headline']/dl/dt",
                '//h3',
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '项目编号：(.+?)</p',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)项目名称',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招标人[：|为](.*?)</span>',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
            ],
            "xpath": [
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [
                '电<.*?>话：(.+?)</p',
                '联系方式：[\s\S]*?电话：(.+?)</p',
            ],
            "xpath": [
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
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
            "xpath": [
                "//div[@class='dg-notice-detail']",
                "//p",]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间
        "project_overview": {
            "re": ['(项目概况与招标范围.+?)投标人资格要求', '(项目概况与招标范围：.+?)<strong>', '(项目概况：.+?)<strong>', '概况：([\s\S]*?)（二）',
                   '概况：([\s\S]*?)</p>', '项目概况([\s\S]*?)<strong>'],
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.+?)</span>(?=</span>|</p>)'],
            "xpath": ['//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]', ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
                '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '投标人资格要求(.+?)<strong>',

            ],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                ''
            ],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
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
"国投电子采购平台-非招标采购公告": {
        "project_title": {
            "re": [''],
            "xpath": [
                "//h3[@class='dg-notice-title']",
                "//div[@class='headline']/dl/dt",
                '//h3',
            ]
        },  # 项目标题
        "project_number": {
            "re": [
                '项目编号：(.+?)</p',
                '编号：(.+?)(?=）|\))',
                '采购编号：(.+?)）',
                '采购编号：(.+?)</span',
                '招标编号：(.+?)</span></span>',
                '编号：([\s\S]+?)(?!<[\s\S]*?>)项目名称',
                '编号：(.+?)</span>',
                '项目编号：(.+?)<',
            ],
            "xpath": ["//span[contains(text(),'项目编号')]/following-sibling::span[1]",
                      "//span[contains(text(),'项目编号')]/../following-sibling::span[1]",
                      "//span[contains(text(),'项目编号：')]", "//span[contains(text(),'采购编号')]/..",
                      "//span[contains(text(),'采购项目编号')]/..",
                      "//span[contains(text(),'项目编号')]/../../following-sibling::span[1]"]
        },  # 项目编号
        "tender_unit": {
            "re": [
                '招标人[：|为](.*?)</span>',
                '招标人[：|为](.+?)</span></span>',
                '招标人：(.*?)</span>',
                '采 购.*?人：(.+?)</span>',
                '采购机构：(.+?)</span>',
                '招标人或其招标代理机构名称：(.+?)</span></span>',
                '招标人或其招标代理机构名称：(.+?)</span>',
            ],
            "xpath": [
                "//span[contains(string(),'招 标 人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
                "//span[contains(string(),'招标人：')]",
                "//span[contains(string(),'采 购 人：')]",
                "//span[contains(string(),'采购人：')]",
                "//p[contains(string(),'采购人：')]", '//span[contains(string(), "招 标 人：")]/following-sibling::*',
            ]
        },  # 招标单位
        "tender_price": {
            "re": ['采购金额[：|为](.+?)</span></span>', '估算额[：|为](.+?)</span></span>'],
            "xpath": [
                '//td[contains(string(), "概算价（万元）")]/../following::*[1]/td[count(//td[contains(string(), "概算价（万元）")]/preceding-sibling::td) + 1]']
        },  # 标的金额
        "publish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'发布日期')]", "//th[contains(text(),'公示开始时间')]/following-sibling::td[1]"]
        },  # 发布时间 需正则两步以上
        "project_leader": {
            "re": [
                '联系方式：[\s\S]*?联系人：(.+?)</p',
                '招标采购中心联系人：(.+?)电话',
                '联系方式[\s\S]*?联[\s\S]*?系[\s\S]*?人：(.+?)</span>',
                '（签名）：(.+?)</span>',
                '主要负责人或授权的项目负责人：(.+?)</span>',
            ],
            "xpath": [
                '//span[contains(string(), "联 系 人：")]/following::*[1]',
                '//span[contains(string(), "联 系 人：")]/following-sibling::*',
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系人：")]/following-sibling::*[1])',
                'string(//span[contains(string(), "招标人：")]/following::*//span[contains(string(), "联系人：")])',
                "string(//span[contains(string(),'联 系 人：')])",
                "//td[contains(string(),'项目联系人：')]/following-sibling::*[1]",
                "string(//span[contains(string(),'联系人：')])",
            ]
        },  # 招标项目负责人 需正则两步以上
        "phone": {
            "re": [
                '电<.*?>话：(.+?)</p',
                '联系方式：[\s\S]*?电话：(.+?)</p',
            ],
            "xpath": [
                'string(//strong[contains(string(), "招标人")]/following::*//span[contains(string(), "联系电话：")]/following-sibling::*[1])',
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
            "xpath": [
                "//div[@class='dg-notice-detail']",
                "//p",]
        },  # 正文
        "bid_finish_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'开标时间')]/../../following-sibling::p[1]",
                      "//span[contains(text(),'提交投标文件截止时间及开标时间')]/../../..",
                      "//span[contains(text(),'开标时间')]/../../following-sibling::td[1]",
                      "//span[contains(text(),'开标时间：')]",
                      "//span[contains(text(),'开标时间')]/../../../following-sibling::p//span[contains(text(),'时间')]/../.."]
        },  # 开标时间
        "bid_end_time": {
            "re": [''],
            "xpath": ["//span[contains(text(),'投标截止及开标时间')]", "//span[text()='投标文件开始递交时间：']/.."]
        },  # 投标截止时间
        "project_overview": {
            "re": [
                '(项目概况和招标范围[\s\S]+?)投标人资格要求',
                '(项目概况与招标范围[\s\S]+?)投标人资格要求',
                '(项目概况与招标范围：[\s\S]+?)<strong>',
                '(项目概况：[\s\S]+?)<strong>',
                '概况：([\s\S]*?)（二）',
                   '概况：([\s\S]*?)</p>',
                '(项目概况[\s\S]*?)<strong>'
            ]
            ,
            "xpath": ["//span[contains(text(),'项目概况')]"]
        },  # 项目概况
        "agency": {
            "re": ['招标代理机构：(.+?)</span>(?=</span>|</p>)'],
            "xpath": ['//span[contains(string(), "招标代理：")]/following-sibling::*[1]',
                      "string(//span[contains(string(),'招标代理机构：')])",
                      "//span[string()='招标代理机构信息']/../../../following-sibling::p//span[contains(text(),'名称')]",
                      "//span[contains(text(),'招标代理机构')]/../following-sibling::span[1]",
                      '//p[contains(string(), "招标代理机构：")]', ]
        },  # 代理机构
        "bid_evaluation_rule": {
            "re": [
                '投标人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '申请人资格要求([\s\S]+?)(?=一、|二、|三、|四、|五、)',
                '投标人资格要求(.+?)<strong>',

            ],
            "xpath": ['']
        },  # 评标规
        "bid_winner": {
            "re": [
                '成交单位：(.+?)</span></p>',
                '成交单位：(.+?)</span></span>',
                '成交人名称：(.+?)</span>',
                '成交单位：(.+?)</span>',
                ''
            ],
            "xpath": [
                "//td[contains(string(), '供应商名称')]/../following::*[1]/td[count(//td[contains(string(), '供应商名称')]/preceding-sibling::td) + 1]",
                "//td[string()='成交供应商']/../following::*[1]/td[count(//td[string()='成交供应商']/preceding-sibling::td) + 1]",
                "//td[string()='成交单位']/../following::*/td[count(//td[string()='成交单位']/preceding-sibling::td) + 1]",
                "string(//td[string()='投标人']/../following::*/td[count(//table[1]//td[string()='投标人']/preceding-sibling::td) + 1])",
            ]
        },  # 中标
        "win_bid_price": {
            "re": [
                '最终报价（单价报价之和）：(.+?)。',
                '',
            ],
            "xpath": [
                '//td[contains(string(), "成交金额")]/../following::*[1]/td[count(//td[contains(string(), "成交金额")]/preceding-sibling::td) + 1]',
                "string(//td[contains(string(), '投标总报价')]/../following::*/td[count(//table[1]//td[contains(string(), '投标总报价')]/preceding-sibling::td) + 1])",
            ]
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
"云采链线上采购一体化平台-竞价公告": base_dict,
"云采链线上采购一体化平台-调研公告": base_dict,

"华润电力供应商门户-寻源信息查询（物资、工程服务、副产品采购、燃料）": base_dict,
"华润电力供应商门户-采购结果公示": base_dict,
"中化国家招标有限责任公司招标网-招标公告": base_dict,
"中化国家招标有限责任公司招标网-评标结果公告": base_dict,
"国义-招标公告及资格预审公告": base_dict,
"国义-各类招标结果公示或公告": base_dict,
"国义-更正公告": base_dict,
"中国海洋石油集团有限公司-招标公告": base_dict,
"中国海洋石油集团有限公司-中标公示": base_dict,
"中国海洋石油集团有限公司-结果公告": base_dict,
"中国海洋石油集团有限公司-非招标公告": base_dict,
"中招联合招标采购平台-招标公告": base_dict,
"中招联合招标采购平台-变更公告": base_dict,
"中招联合招标采购平台-结果公示": base_dict,
"中国电子进出口电子商务平台-招标公告": base_dict,
"中国电子进出口电子商务平台-变更公告": base_dict,
"中国电子进出口电子商务平台-中标公示": base_dict,
"航空工业电子采购平台-招标公告": base_dict,
"航空工业电子采购平台-变更公告": base_dict,
"航空工业电子采购平台-中标公示": base_dict,
"航空工业电子采购平台-中标结果公告": base_dict,
"深圳市政府采网-招标公告": base_dict,
"深圳市政府采网-更正公告": base_dict,
"深圳市政府采网-中标结果公示": base_dict,
"深圳市政府采网-成交结果公示": base_dict,
"深圳市政府采网-终止公告": base_dict,
"竞采星竞价采购网-招标公告": base_dict,
"竞采星竞价采购网-结果公示": base_dict,
"竞采星竞价采购网-结果公告（中标、终止、流标、废标）": base_dict,
"中国一汽电子招标采购交易平台-招标/预审公告": base_dict,
"中国一汽电子招标采购交易平台-变更公告": base_dict,
"中国一汽电子招标采购交易平台-异常公告": base_dict,
"中国一汽电子招标采购交易平台-中标候选人公示": base_dict,
"中国一汽电子招标采购交易平台-中标结果公告": base_dict,
"深圳市国际招标有限公司-招标公告": base_dict,
"深圳市国际招标有限公司-资格预审公告": base_dict,
"深圳市国际招标有限公司-变更公告": base_dict,
"深圳市国际招标有限公司-采购结果公告": base_dict,
"国家开发投资公司电子采购平台-招标（预审）公告": base_dict,
"国家开发投资公司电子采购平台-非招标采购公告": base_dict,
"国家开发投资公司电子采购平台-变更公告": base_dict,
"国家开发投资公司电子采购平台-候选人公示": base_dict,
"国家开发投资公司电子采购平台-结果公告": base_dict,
"中国南方电网--阳光电子商务-招标公告": base_dict,
"中国南方电网--阳光电子商务-非招标公告": base_dict,
"中国南方电网--阳光电子商务-公示公告": base_dict,
"中国南方电网--阳光电子商务-流标公告": base_dict,
"中国南方电网--阳光电子商务-寻源公告": base_dict,
"西电集团电子采购平台-招标公告": base_dict,
"西电集团电子采购平台-变更公告": base_dict,


}

bid_budget_keyword_list = [
    '采购预算',
    '项目金额',
    '预算资金',
    '预算金额',
    '限价金额',
    '预算价',
    '承包',
    '项目估算',
    '招标金额',
    '投标最高限价',
    '最高限价',
    '招标总投资',
    '评标价',
    '投标总报价',
    '投资约为',
    '招标控制价',
    '招标规模',
    '项目规模',
    '项目概算',
    '项目总投资',
    '投资金额',
    '标底价',
    '总投资合计',
    '财政支付上限',

]

bid_money_keyword_list = [
    '中标金额',
    '中标价格',
    '中选价格',
    '成交金额',
    '中标价',
    '中标合同额',
    '合同金额',
    '中标服务费金额',
    '成交总价',
    '中选金额',
    '中标（成交）金额',
    '中标(成交)金额',
    '成交价',
    '中标总金额',
    '成交标的金额',
    '投标价',
    '报价总金额',
    '投标报价',
    # '报价',
    # '价格',
    '中标总价',
    '标价',

]

zhaobiao_company_keyword_list = [
    '招标机构名称',
    '招标人名称',
    '采购单位',
    '采购商',
    '招标人',
    '招募人',
    '招标单位',
    '建设单位',
    '采购人',
    '项目单位',
    '招租人',
    '采购项目名称',
    '招标（采购）人',
    '发包人'

]

zhongbiao_company_keyword_list = [
    '中选机构名称',
    '中选单位',
    '中选供应商',
    '入围候选人',
    '供应商名称',
    '成交供应商',
    '中标单位',
    '中标供应商',
    '中标（成交）供应商',
    '中签单位',
    '中标人',
    '采购人',
    '中标人名称',
    '成交人',
    '发布结果',
    '成交单位',
    '中标企业',
    '中标结果',
    '中标商',
    '乙方',
    '第一中标候选人',
    '成交候选供应商',
    '中标候选人',
    '中选候选人',
    '中标候选人排名',
    '第一名',
    '成交候选人',
    '一标段',
    '二标段',
    '三标段',
    '四标段',
    '五标段',
    '六标段',
]

agent_keyword_list = [
    '代理机构',
    '代理人',
    '招标代理',
    '招标机构',
    '代理公司',
    '采购代理',
    '采购机构名称',
    '采购代理机构',
    '发布机构',

]

company_pattern_list = [
    '(\S*)受(\S+)委托',
]

zhaobiao_company_end_list = [
    '小学',
    '中学',
    '大学',
    '幼儿园',
    '学校',
    '学院',
    '委员会',
    '监狱',
    '银行',
    '集团',
    '政府',
    '院',
    '局',
    '司',
    '所',
    '厅',
    '部',
    '村委会',
    '委',
    '馆',
    '示范区',
    '开发区',
    '中心',
    '检查场',
    '油田',
    '气象台',
    '商务厅',
    '厂',
    '图书馆',
    '办事处',
    '管理站',
    '大队',
    '监测站',
    '合作联社',
    '推广站 ',
    '管理处',
    '博物馆',
    '文化馆',
    '经营总站 ',
    '卫计办',
    '办公室',
    '园林处',
    '管理段',
    '一中',
    '总站',
    '管理队',

]

zhongbiao_company_end_list = [
    '公司',
    '研究所',
    "检测所",
    '商城',
    '园艺场',
    '设计院',
    '研究院',
    '工程处',
    '商行',
    '厂',
    '中心',
    '渔场',
    '门诊部',
    '事务所',
    '局',
    '小学',
    '中学',
    '大学',
    '幼儿园',
    '学校',
    '学院',
    '委员会',
    '监狱',
    '银行',
    '集团',
]

agent_company_end_list = [
    '公司',
    '工程处',
    '中心',
    '局',
]

project_leader_keyword_list = [
    '采购单位联系人',
    '联系人',
    '负责人',
    '（签名）：',
    '姓名',
    '采购执行人',
    '联系人及联系电话',
    '联系人及电话',
    # '联 系 人',
    # '联系 人',
    # '联 系人',
]

project_leader_ban_list = [
    "代理机构联系人",
    "代理机构\r\n联系人",
    "南网科研院",

]

phone_keyword_list = [
    '电话',
    '手机号码',
    '联系方式',
    # '电 话',
    '联系电话',
    '联系人',
]

phone_ban_list = [
    '代理机构联系电话',
    '投诉电话',
    '客服电话',
    '4008800114',  # 中国石油
    "400-809-0101",
]

project_number_keyword_list = [
    '项目编号',
    '采购编号',
    # ' 话',
    "采购项目编码",
    '文件编号',
    '招标编号',
    '标段（包）编号',
    '采购单编号',
    '询价编号',
    '项目标号',
    '编号:',
    '编号：',
    '编号',
]

bid_finish_time_keyword_list = [
    # '报名时间',
    '开始递交时间',
    '投标响应开始时间',
    '评标日期',
    '报价日期',
    '开标日期',
    '开标时间',
    '评标时间',
    '报价时间',
    '谈判时间',
    '谈判日期',
    '谈判（开启）时间',
    '磋商日期',
    '磋商时间',
    '磋商会议时间',
    '磋商会议日期'
]

bid_end_time_keyword_list = [
    '延期开标',
    # '截止时间',
    '报价截止时间',
    '报价截止日期',
    '投标响应截止时间',
    '投标文件送达截止时间',
    '投标截止时间',
    '投标时间[\s\S]{1,15}?结束：',
    '投标截止日期',
    '报名截止时间',
    '报名截止日期',
    '递交截止时间',
    '递交截止日期',
    '递交的截止时间',
    '递交的截止日期',
    '递交响应文件时间',
    '递交响应文件日期',
    '定标日期',
    '申请文件的截止时间',
    '申请文件的截止日期',
    '定标时间',
    '投标文件截止时间',
    '投标文件截止日期',
]

win_bid_announcement_time_keyword_list = [
    '公告发布时间',
    '公告时间',
    '公告日期',
    '公示开始时间',
    '公示开始日期',
    '公示时间'
    # '公示结束时间'
]
