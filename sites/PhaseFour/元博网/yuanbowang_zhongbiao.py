#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re

import execjs
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree
sys.path.append('../../PhaseTwo')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_5 import Bid5
from bid_conf.conf_5 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
from bid_tools import utils
import jsonpath


def encrypt_js(js_content):
    js_txt = """
        const CryptoJS = require('crypto-js');
        function convert3(txt) {
        var a = '4b4e31356d6638344c6e61326c3030347361646572364d72',
            b = CryptoJS.enc.Hex.parse("436d396432667338346c3364324e3673");
        a = CryptoJS.enc.Hex.parse(a);
        var txtC = CryptoJS.AES.decrypt(CryptoJS.format.Hex.parse(txt), a, {
            iv: b,
            mode: CryptoJS.mode.CBC,
            padding: CryptoJS.pad.Pkcs7
        })
        var c = CryptoJS.enc.Utf8.stringify(txtC);
        return JSON.parse(c);
    }
        """
    ctx1 = execjs.compile(js_txt)
    encrypt_str = ctx1.call('convert3', js_content)
    return encrypt_str


class BidZGDZ(Bid5):
    def __init__(self, debug=True):
        Bid5.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '元博网-最新中标'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url_base = 'https://www.chinabidding.cn/public/2020/html/zbcglist.html'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': '53gid2=12259327787007; 53uvid=1; onliner_zdfq72221204=0; visitor_type=old; 53gid0=12259327787007; 53gid1=12259327787007; gr_user_id=4ad3d1fb-d1d3-47b3-a672-78aa3cf1e9d7; Hm_lvt_ebcee0764883fb81bcdd54df18970c94=1686832234; browser_id=-1621326260; 53revisit=1686832249935; 53kf_72221204_from_host=www.chinabidding.cn; 53kf_72221204_keyword=https%3A%2F%2Fwww.chinabidding.cn%2F%3Futm_term%3D%25E5%2585%2583%25E5%258D%259A%25E7%25BD%2591%26utm_source%3Dso.pc%26utm_campaign%3D42704430%26utm_content%3D707217345%26utm_keyid%3D54505029031%26ggw_id%3D2102; uuid_53kf_72221204=2f8e4583dcba70ba31f2fbab1b64b724; 53kf_72221204_land_page=https%253A%252F%252Fwww.chinabidding.cn%252Fsk%252Fhuodian%252F; kf_72221204_land_page_ok=1; my_acc_reauto_time=1686832333939; invite_53kf_totalnum_7=9; pop_status=1; b5897e326c6777f3_gr_last_sent_cs1=569519; b5897e326c6777f3_gr_session_id=03841276-94c7-43bd-99d7-57d8e14d5307; b5897e326c6777f3_gr_last_sent_sid_with_cs1=03841276-94c7-43bd-99d7-57d8e14d5307; b5897e326c6777f3_gr_session_id_sent_vst=03841276-94c7-43bd-99d7-57d8e14d5307; acw_tc=7b39758316893278426722723efacaf0c6f3c942c6956b4f67169f0d6a927f; b5897e326c6777f3_gr_cs1=569519; CBL_SESSION=0ec0edff92774957e5134d05c6259be67e96d617-___TS=1725328246368&___ID=74040369-d6fd-46c6-9d5a-7e6d3d9c6ea9; Hm_lpvt_ebcee0764883fb81bcdd54df18970c94=1689328247',
            'Host': 'www.chinabidding.cn',
            'Referer': 'https://www.chinabidding.cn/sk/gaosugonglu/1.html',
            'Sec-Ch-Ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'
        }
        page = 1
        url_base = 'https://www.chinabidding.cn/yuan/zbcg/ZbcgChannel/getDataList?key=%E5%BB%BA%E7%AD%91%E5%B7%A5%E7%A8%8B&search_key=4000005&table_type=1&page={}'
        url = url_base.format(page)
        content = self.req(url, req_type="get", headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        content = encrypt_js(content)
        # pages = content.get("result", {}).get("totalPages")
        # note 手动限定最大页数
        pages = 20
        if not pages:
            return
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            next_url = url.format(page)
            content = self.req(next_url, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            content = encrypt_js(content)
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, json_content, url):
        items = json_content.get("list")
        for item in items:
            if self.exit_flag:
                return
            href = item.get("url")
            if not href:
                continue
            detail_url = urljoin(url, href)
            title = item.get("title")
            publish_time = item.get("date")
            area = item.get("area")
            tenderer = ''
            bidder = ''
            bid_price = ''
            bid_agency_tel = ''
            bid_agency = ''
            bid_status = ''
            if 'fid' not in detail_url:
                detail_content = self.req(url=detail_url, headers=self.headers)
                if not detail_content or detail_content == 404 or detail_content == 400:
                    self.log.error("{} no detail_content".format(detail_url))
                    continue
                source_code = detail_content
                detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
                detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
                html1 = etree.HTML(detail_content.replace('</p>', '\n</p>'))
                content_text1 = html1.xpath('string(//*[@id="content"]|//div[@id="infoDescription"])')
            else:
                fid = utils.re_find_one('fid=(.*?)@', str(detail_url) + '@')
                json_url = 'https://www.chinabidding.cn/agency.info.Detail/show?fid=' + str(fid)
                detail_content = self.req(url=json_url, rsp_type='json', headers=self.headers)
                source_code = detail_content
                # publish_time = detail_content['c_info']['info']['FPublishTime']
                # entry_name = detail_content['c_info']['info']['FTitle']
                tenderer = detail_content['c_info']['info']['FBidder']
                bid_agency_tel = detail_content['c_info']['info']['FMobile']
                try:
                    bid_agency = detail_content['c_info']['info']['FBiddingAgency']
                except:
                    bid_agency = ''
                bid_status = detail_content['c_info']['purchase']
                if bid_status == []:
                    bid_status = '招标中'
                else:
                    bid_status = '已开标'
                try:
                    bidder = ','.join(jsonpath.jsonpath(detail_content['c_info']['purchase'], '$..FTitle'))
                except:
                    bidder = detail_content['c_info']['purchase']
                try:
                    bid_price = str(detail_content['c_info']['purchase'][0]['FAmount']).strip() + str(
                        detail_content['c_info']['purchase'][0]['FUnit'])
                except:
                    try:
                        bid_price = str(detail_content['c_info']['purchase'][1]['FAmount']) + str(
                            detail_content['c_info']['purchase'][1]['FUnit'])
                    except:
                        bid_price = ''
                detail_content = detail_content['c_info']['content']
                html1 = etree.HTML(detail_content.replace('</p>', '\n</p>'))
                content_text1 = html1.xpath('string(//*)')
            data = {}
            data['project_title'] = title
            data['publish_time'] = publish_time
            data['content'] = content_text1.strip()
            # data['source_code'] = str(source_code).strip()
            # 一级指标
            # primary_indicators = main_html.xpath('string(//div[@class="sort1 cl"]/ul/li/a[@class="active"])')
            # 二级指标
            # try:
            #     secondary_indicators = re.findall('采购与招标网</a>([\s\S]*?)<a', detail_content)[0]
            # except:
            #     secondary_indicators = ''
            # data['primary_indicators'] = primary_indicators
            # data['secondary_indicators'] = secondary_indicators

            if tenderer:
                data['tenderer'] = str(tenderer).strip()
            if bidder:
                data['bidder'] = str(bidder).strip()
            if bid_price:
                data['bid_price'] = str(bid_price).strip()
            if bid_agency:
                data['bid_agency'] = str(bid_agency).strip()
            if bid_status:
                data['bid_status'] = str(bid_status).strip()
            if bid_agency_tel:
                data['bid_agency_tel'] = str(bid_agency_tel).strip()
            
            self.detail_parse(detail_content, detail_url, data)

            # 字段
            # uuid = 'uuid'  # 唯一业务id，对url做md5取值
            # url = 'url'  # 链接
            # title = '标题'  # 标题
            # publish_time = '时间'  # 发布时间
            # area = '地区'  # 地区
            # content = '正文'  # 正文
            # announcement = '招标公告名'  # 招标公告名
            # bid_time = '招标时间'  # 招标时间
            # bid_condition = '招标条件'  # 招标条件
            # entry_name = '项目名称'  # 项目名称
            # construction_location = '建设地点'  # 建设地点
            # construction_scale = '建设项目规模'  # 建设项目规模
            # bid_control_price = '项目招标控制价'  # 项目招标控制价
            # planned_duration = '计划工期'  # 计划工期
            # bid_section = '标段划分'  # 标段划分
            # bid_scope = '招标范围'  # 招标范围
            # bid_qualification_reqirement = '投标人资格要求'  # 投标人资格要求
            # bid_documents_collection = '招标文件的领取'  # 招标文件的领取
            # bid_submission = '投标文件的递交'  # 投标文件的递交
            # publish_announcements_media = '发布公告的媒介'  # 发布公告的媒介
            # other_requirements = '其他要求或说明'  # 其他要求或说明
            # tenderer = '招标人'  # 招标人
            # tenderer_tel = '招标人联系方式'  # 招标人联系方式
            # bid_agency = '招标代理'  # 招标代理
            # bid_agency_tel = '招标代理联系方式'  # 招标代理联系方式
            # bid_status = '招标状态'  # 招标状态
            # bid_result = '中标结果'  # 中标结果
            # bidder = '中标单位'  # 中标单位
            # bid_price = '中标价'  # 中标价
            # primary_indicators = '一级指标'
            # secondary_indicators = '二级指标'
            # source_code = '源码'


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

    # BidZGDZ.run(keyword)
