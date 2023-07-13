#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
import sys
import time
import re
import urllib3
from urllib.parse import *
import requests
import random
import datetime
from lxml.html import etree
sys.path.append('..')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_3 import Bid3
from bid_conf.conf_3 import parse_dict
urllib3.disable_warnings()
from playwright.sync_api import sync_playwright
from bid_tools import utils
import jsonpath


class BidZGDZ(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
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
        # self.keyword = keyword
        url_base = 'https://www.chinabidding.cn/public/2020/html/zbcglist.html'
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': '53gid2=11652134558001; 53gid0=11652134558001; 53gid1=11652134558001; TY_SESSION_ID=9bdf52f0-6c7e-4cef-874a-719598b3a1d8; visitor_type=old; 53uvid=1; onliner_zdfq72221204=0; browser_id=861067928; gr_user_id=8683edcf-4502-464f-83fb-490ff7a2b442; b5897e326c6777f3_gr_session_id=5203b96e-0cf7-4ba9-aedb-4e4d74fc859e; b5897e326c6777f3_gr_session_id_sent_vst=5203b96e-0cf7-4ba9-aedb-4e4d74fc859e; b5897e326c6777f3_gr_last_sent_sid_with_cs1=5203b96e-0cf7-4ba9-aedb-4e4d74fc859e; b5897e326c6777f3_gr_last_sent_cs1=569519; 53revisit=1687836068299; acw_tc=7b39758816878383020695208ed92d3c03cc6b2c78903055e84a35e6a8db22; b5897e326c6777f3_gr_cs1=569519; CBL_SESSION=60bd914408e36ba3648c92efeebaeb54ad38a5ba-___TS=1723838311099&___ID=7f2fdac4-f4f1-437a-8b0c-f29d6c654711; Hm_lvt_ebcee0764883fb81bcdd54df18970c94=1687836060,1687838308; Hm_lpvt_ebcee0764883fb81bcdd54df18970c94=1687838308; 53kf_72221204_from_host=www.chinabidding.cn; 53kf_72221204_keyword=; uuid_53kf_72221204=082d63992712dd4cf31c24afad90fa9e; 53kf_72221204_land_page=https%253A%252F%252Fwww.chinabidding.cn%252Fsk%252Fgaosugonglu%252F1.html; kf_72221204_land_page_ok=1',
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
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False)
            # page = browser.new_page()
            context = browser.new_context(storage_state="auth/state.json")
            # context = browser.new_context()
            page = context.new_page()
            url = url_base
            count = 0
            while count < 3:
                try:
                    page.goto(url)
                    page.wait_for_load_state("networkidle")
                    break
                except Exception as e:
                    count += 1
                    pass
            page.get_by_role("heading", name="建筑工程>", exact=True).get_by_role("link", name="建筑工程").click()
            page.get_by_text("最新中标").click()
            for page_count in range(10000):
                content = page.content()
                self.list_parse(content, url)

                page.get_by_role("link", name="下一页").click()
                time.sleep(2)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, maincontent, url):
        main_html = etree.HTML(maincontent)
        items = main_html.xpath('//div[@class="content"]/ul/li')
        for item in items:
            if self.exit_flag:
                return
            href_text = item.xpath('string(./@onclick)')
            href = utils.re_find_one("goNew\('(.*?)',", href_text)
            if href:
                detail_url = urljoin(url, href)
                title = item.xpath('string(//h5/@title)')
            else:
                continue
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
            data['title'] = str(title).strip()
            data['publish_time'] = item.xpath('string(.//span[@class="date"]/em)')
            data['content'] = content_text1.strip()
            data['source_code'] = str(source_code).strip()
            # 一级指标
            primary_indicators = main_html.xpath('string(//div[@class="sort1 cl"]/ul/li/a[@class="active"])')
            # 二级指标
            try:
                secondary_indicators = re.findall('采购与招标网</a>([\s\S]*?)<a', detail_content)[0]
            except:
                secondary_indicators = ''
            data['primary_indicators'] = primary_indicators
            data['secondary_indicators'] = secondary_indicators
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
            uuid = 'uuid'  # 唯一业务id，对url做md5取值
            url = 'url'  # 链接
            title = '标题'  # 标题
            publish_time = '时间'  # 发布时间
            area = '地区'  # 地区
            content = '正文'  # 正文
            announcement = '招标公告名'  # 招标公告名
            bid_time = '招标时间'  # 招标时间
            bid_condition = '招标条件'  # 招标条件
            entry_name = '项目名称'  # 项目名称
            construction_location = '建设地点'  # 建设地点
            construction_scale = '建设项目规模'  # 建设项目规模
            bid_control_price = '项目招标控制价'  # 项目招标控制价
            planned_duration = '计划工期'  # 计划工期
            bid_section = '标段划分'  # 标段划分
            bid_scope = '招标范围'  # 招标范围
            bid_qualification_reqirement = '投标人资格要求'  # 投标人资格要求
            bid_documents_collection = '招标文件的领取'  # 招标文件的领取
            bid_submission = '投标文件的递交'  # 投标文件的递交
            publish_announcements_media = '发布公告的媒介'  # 发布公告的媒介
            other_requirements = '其他要求或说明'  # 其他要求或说明
            tenderer = '招标人'  # 招标人
            tenderer_tel = '招标人联系方式'  # 招标人联系方式
            bid_agency = '招标代理'  # 招标代理
            bid_agency_tel = '招标代理联系方式'  # 招标代理联系方式
            bid_status = '招标状态'  # 招标状态
            bid_result = '中标结果'  # 中标结果
            bidder = '中标单位'  # 中标单位
            bid_price = '中标价'  # 中标价
            primary_indicators = '一级指标'
            secondary_indicators = '二级指标'
            source_code = '源码'

            # 之前写的字段采集代码
            publish_time = ''
            tenderer = ''
            bidder = ''
            bid_price = ''
            bid_agency_tel = ''
            bid_agency = ''
            bid_status = ''
            if 'fid' not in detail_url:
                detail_content = self.req(url=detail_url, headers=self.headers)
                if not detail_content or detail_content == 404 or detail_content == 400:
                    self.ignore_count += 1
                    self.log.error("{} no detail_content".format(detail_url))
                    continue
                detail_content = re.sub("<script[\s\S]*?/script>", "", detail_content, flags=re.I)
                detail_content = re.sub("<style[\s\S]*?/style>", "", detail_content, flags=re.I)
                html1 = etree.HTML(detail_content.replace('</p>', '\n</p>'))
                content_text1 = html1.xpath('string(//*[@id="content"]|//div[@id="infoDescription"])')
                html = etree.HTML(detail_content)
                content_text = html.xpath('string(//*[@id="content"]|//div[@id="infoDescription"])')
                detail_content_no_space = re.sub('\s+', '', detail_content)
                html_no_space = etree.HTML(detail_content_no_space)
            else:
                fid = utils.re_find_one('fid=(.*?)@', str(detail_url) + '@')
                json_url = 'https://www.chinabidding.cn/agency.info.Detail/show?fid=' + str(fid)
                detail_content = self.req(url=json_url, rsp_type='json', headers=self.headers)
                publish_time = detail_content['c_info']['info']['FPublishTime']
                # entry_name = detail_content['c_info']['info']['FTitle']
                tenderer = detail_content['c_info']['info']['FBidder']
                # bid_agency_tel = detail_content['c_info']['info']['FMobile']
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
                html = etree.HTML(detail_content)
                content_text = html.xpath('string(//*)')
                html_no_space = etree.HTML(detail_content)
            data = {}
            content_text = str(content_text).replace(' ', '').replace(' ', '')
            content_text1 = str(content_text1).replace(' ', '').replace(' ', '')
            data[TABField.uuid] = utils.get_md5(str(detail_url))  # uuid
            data[TABField.url] = detail_url
            # data[TABField.announcement] = item.xpath("string(./@title)")
            data[TABField.announcement] = item[0]
            area = html.xpath('string(//div[@class="xiaob"]//a[contains(@href,"https://www.chinabidding.cn/sa")])')
            if not area:
                area = html.xpath('string(//span[@class="area"])')
            publishTime_text = html.xpath('string(//div[@class="xiaob"])')
            if not publish_time:
                publish_time = utils.re_find_one('20\d+-\d+-\d+', publishTime_text)
            bid_condition = utils.re_find_one('一、招标条件([\s\S]*?)二、', content_text)
            if not bid_condition:
                bid_condition = utils.re_find_one('招标范围及质量要求[:：](.*?)\n', content_text)
            entry_name = html.xpath(
                'string(//span[contains(text(),"项目名称")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"项目名称")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工程名称")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"项目名称")]/ancestor::td[1]/following-sibling::td[1]|//*[contains(text(),"工程名称")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"项目及标段名称")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"项目及标段名称")]/ancestor::td[1]/following-sibling::td[1])')
            if '建设单位' in entry_name:
                entry_name = str(entry_name).replace('建设单位', '').strip()
            if not entry_name:
                entry_name = html_no_space.xpath(
                    'string(//span[contains(text(),"项目名称")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"项目名称")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工程名称")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"项目名称")]/ancestor::td[1]/following-sibling::td[1]|//*[contains(text(),"工程名称")]/ancestor::td[1]/following-sibling::td[1]|//span[contains(text(),"项目名称：")]/ancestor::p[1]|//*[text()="项目名称："]/../following-sibling::span[1])')
            if not entry_name:
                entry_name = html.xpath(
                    'string(//span[contains(text(),"项目名称：")]/ancestor::p[1]|//*[text()="项目名称："]/../following-sibling::span[1]|//p[contains(text(),"招标项目名称：")]|//p[contains(text(),"招标项目名称:")])')
            if entry_name:
                if '万元' in entry_name:
                    entry_name = ''
                else:
                    entry_name = str(entry_name).replace('招标项目名称', '').replace('项目名称', '').replace(':', '').replace('：',
                                                                                                                    '')
            if not entry_name:
                entry_name = html.xpath('string(//span[@name="psgsjbxx_XMMC"])')
            if not entry_name:
                entry_name = utils.re_find_one('项目名称[:：](.*?)<', detail_content)
                entry_name = self.clean_data(entry_name)
            if not entry_name:
                entry_name = utils.re_find_one('项目名称<.*?>[:：]([\s\S]*?)</p>', detail_content)
                entry_name = self.clean_data(entry_name)
            if not entry_name:
                entry_name = utils.re_find_one('项目名称[:：]([\s\S]*?)</[ph]', detail_content)
                entry_name = self.clean_data(entry_name)
            if not entry_name:
                entry_name = utils.re_find_one('工程名称[:：]([\s\S]*?)</[ph]', detail_content)
                entry_name = self.clean_data(entry_name)
            if not entry_name:
                entry_name = utils.re_find_one('工程名称[:：]([\s\S]*?)\n', content_text1)
                entry_name = self.clean_data(entry_name)

            construction_location = html.xpath(
                'string(//table/tbody/tr//span[text()="建设单位"]/ancestor::td[1]/following-sibling::td[1])')
            if not construction_location:
                construction_location = utils.re_find_one('工程地点[:：](.*?)</', detail_content)
                construction_location = self.clean_data(construction_location)
            if not construction_location:
                construction_location = utils.re_find_one('工程地点.*?[:：](.*?)</', detail_content)
                construction_location = self.clean_data(construction_location)
                if not construction_location:
                    construction_location = utils.re_find_one('工程地点.*?[:：](.*?)</p', detail_content)
                    construction_location = self.clean_data(construction_location)
            if not construction_location:
                construction_location = utils.re_find_one('建设地点[：:](.*?)</p>', detail_content)
                construction_location = self.clean_data(construction_location)
            if not construction_location:
                construction_location = utils.re_find_one('建设地址[：:](.*?)</p>', detail_content)
                construction_location = self.clean_data(construction_location)
            construction_scale = html.xpath(
                'string(//*[text()="规模"]/ancestor::p[1]|//table/tbody/tr//*[text()="结构类型及规模"]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"建设规模")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工程规模")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"工程规模")]/ancestor::td[1]/following-sibling::td[1])')
            if not construction_scale:
                construction_scale = html_no_space.xpath(
                    'string(//*[text()="规模"]/ancestor::p[1]|//table/tbody/tr//*[text()="规模"]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"规模")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工程规模")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"工程规模")]/ancestor::td[1]/following-sibling::td[1])')
            if not construction_scale:
                construction_scale = utils.re_find_one('招标内容及规模[:：]([\s\S]*?)</p>', detail_content)
                construction_scale = self.clean_data(construction_scale)
            else:
                construction_scale = str(construction_scale).replace('建筑规模', '').replace(':', '').strip()
            bid_control_price = html.xpath(
                'string(//table/tbody/tr//*[contains(text(),"最高限价")]/ancestor::td[1]/following-sibling::td[1])')
            if not bid_control_price:
                bid_control_price = html.xpath(
                    'string(//table/tbody/tr/td[contains(text(),"估算价") and contains(text(),"万元")]/following-sibling::td[1])')
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                else:
                    bid_control_price = bid_control_price
            if not bid_control_price:
                bid_control_price = html.xpath(
                    'string(//table/tbody/tr//*[contains(text(),"概算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"估算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"概（预）算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"预（概）算价")]/ancestor::td[1]/following-sibling::td[1])')
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                else:
                    bid_control_price = bid_control_price
            if not bid_control_price:
                bid_control_price = html_no_space.xpath(
                    'string(//table/tbody/tr//*[contains(text(),"概算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"估算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"概（预）算价")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"预（概）算价")]/ancestor::td[1]/following-sibling::td[1])')
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                else:
                    bid_control_price = bid_control_price
            if not bid_control_price:
                bid_control_price = html.xpath(
                    'string(//table/tbody/tr/td[contains(text(),"估算价") and contains(text(),"元")]/following-sibling::td[1])')
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '元'
                else:
                    bid_control_price = bid_control_price
            if not bid_control_price:
                bid_control_price = utils.re_find_one('限价：(.*?元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('项目控制价[：:](.*?元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算金额[：:](.*?元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
                if not bid_control_price:
                    bid_control_price = utils.re_find_one('预算价[:：](.*?元)', detail_content)
                    bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('估算价[:：](.*?元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算金额（元）[：:](.*?)\n', content_text)
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算总额[：:](.*?元)', content_text)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算</a>金额\(万元\)[:：](.*?)<br>', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                else:
                    bid_control_price = utils.re_find_one('预算</a>金额\(万元\)[:：]([\s\S]*?)<br',
                                                         re.sub('\s+', '', detail_content))
                    bid_control_price = self.clean_data(bid_control_price)
                    if bid_control_price:
                        bid_control_price = str(bid_control_price).strip() + '万元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算</a>金额（万元）[:：](.*?)<br', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                else:
                    bid_control_price = utils.re_find_one('预算</a>金额（万元）[:：](.*?)<br', re.sub('\s+', '', detail_content))
                    bid_control_price = self.clean_data(bid_control_price)
                    if bid_control_price:
                        bid_control_price = str(bid_control_price).strip() + '万元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算</a>金额\(万元\)[:：](.*?)</p>', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '万元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('预算</a>金额\(元\)[:：](.*?)</p>', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('招标控制价</a>[：:](.*?)[。，；]', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('工程计划投资(.*?元)', content_text)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('控制价为(.*?元)', content_text)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('项目预算(.*?元)', content_text)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('投资额约(.*?元)', content_text)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('投资金额[：:](.*?元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('招标控制价[：:](.*?)[。，；]', content_text)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('\d+\.概算投资[：:](.*?)\d+\.', content_text)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = html.xpath('string(//span[@name="psgsjbxx_CGYS"])')
                if bid_control_price:
                    bid_control_price = str(bid_control_price).strip() + '元'
            if not bid_control_price:
                bid_control_price = utils.re_find_one('工程造价.*?[:：](.*?)</p>', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if not bid_control_price:
                bid_control_price = utils.re_find_one('总投资[:：](.*?万元)', detail_content)
                bid_control_price = self.clean_data(bid_control_price)
            if bid_control_price:
                bid_control_price = re.sub('<.*?>', '', bid_control_price)
            if bid_control_price and '元' not in bid_control_price:
                if '万元' in detail_content:
                    bid_control_price = str(bid_control_price).strip() + '万元'
                elif '元' in detail_content:
                    bid_control_price = str(bid_control_price).strip() + '元'
                else:
                    bid_control_price = bid_control_price
            planned_duration = utils.re_find_one('中标供货期：(.*?天)', detail_content)
            planned_duration = self.clean_data(planned_duration)
            if not planned_duration:
                planned_duration = utils.re_find_one('计划工期[:：](.*?天)', detail_content)
                planned_duration = self.clean_data(planned_duration)
            if not planned_duration:
                planned_duration = html.xpath(
                    'string(//*[contains(text(),"计划供货期")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"工期")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工 期")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工期")]/following-sibling::td[1])')
            if not planned_duration:
                planned_duration = html.xpath(
                    'string(//*[text()="工期要求："]|//*[text()="工期要求："]/following-sibling::span[1])')
            if not planned_duration:
                planned_duration = html_no_space.xpath(
                    'string(//*[contains(text(),"计划供货期")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"工期")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工 期")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"工期")]/following-sibling::td[1])')
            if not planned_duration:
                planned_duration = html_no_space.xpath(
                    'string(//*[contains(text(),"工期要求：")]|//*[contains(text(),"工期要求：")]/following-sibling::span[1])')
            if planned_duration:
                planned_duration = str(planned_duration).replace('工期要求：', '').strip()
            if not planned_duration:
                planned_duration = utils.re_find_one('送货期限[:：](.*?)\n', content_text)
            if not planned_duration:
                planned_duration = utils.re_find_one('5、工期：([\s\S]*?)6、', content_text)
            if not planned_duration:
                planned_duration = utils.re_find_one('工期：([\s\S]*?)</p>', detail_content)
                planned_duration = self.clean_data(planned_duration)
            if not planned_duration:
                planned_duration = utils.re_find_one('工期：([\s\S]*?)[。；;，,\n]', content_text)
            if planned_duration:
                if '天\n' in planned_duration:
                    planned_duration = utils.re_find_one('(.*?天)\n', planned_duration)
            bid_section = utils.re_find_one('招标范围：(\s\S*?)<[bs]', detail_content)
            bid_section = self.clean_data(bid_section)
            if not bid_section:
                bid_section = utils.re_find_one('标段划分[：:]([\s\S]*?)</p>', detail_content)
                bid_section = self.clean_data(bid_section)
            bid_scope = utils.re_find_one('招标范围：([\s\S]*?)<[bs]', detail_content)
            bid_scope = self.clean_data(bid_scope)
            if not bid_scope:
                bid_scope = utils.re_find_one('招标范围[：:]([\s\S]*?)</p>', detail_content)
                bid_scope = self.clean_data(bid_scope)
            bid_qualification_reqirement = utils.re_find_one('投标人资格要求([\s\S]*?)<[bs]', detail_content)
            bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('三、投标人资格要求([\s\S]*?)四、', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('二、投标人资格要求([\s\S]*?)三、', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('二、申请人资格要求([\s\S]*?)三、', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('3.投标人资格条件([\s\S]*?)4.', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('3.投标人资格要求([\s\S]*?)4.', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('供应商基本要求：(.*?)</p>', detail_content)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('二、供应商的资格要求([\s\S]*?)三、公告发布媒体', content_text)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('供应商资格要求([\s\S]*?)\d+、', content_text)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('供应商资格及要求([\s\S]*?)\d+、', content_text)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('四、报价供应商资格条件([\s\S]*?)五、', content_text)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('（一）投标单位资质与合格条件要求[:：](.*?)（二）', content_text)
                bid_qualification_reqirement = self.clean_data(bid_qualification_reqirement)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('3.投标人资格要求([\s\S]*?)4.招标文件的获取', content_text)
            if not bid_qualification_reqirement:
                bid_qualification_reqirement = utils.re_find_one('4．投标人资格要求([\s\S]*?)5．', content_text)
            bid_documents_collection = html.xpath(
                'string(//span[contains(text(),"2.询价文件的获取")]/../following-sibling::p[1])')
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('招标文件的获取(\s\S*?)<[bs]', detail_content)
                bid_documents_collection = self.clean_data(bid_documents_collection)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('招标文件的获取(\s\S*?)\d+\.', content_text)
                bid_documents_collection = self.clean_data(bid_documents_collection)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('四、获取采购文件([\s\S]*?)五、', content_text)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('三、获取采购文件([\s\S]*?)四、', content_text)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('招标文件的获取([\s\S]*?)<p><strong>', detail_content)
                bid_documents_collection = self.clean_data(bid_documents_collection)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('招标文件获取[:：]([\s\S]*?)</p>', detail_content)
                bid_documents_collection = self.clean_data(bid_documents_collection)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('招标文件获取方法[:：]([\s\S]*?)（四）', content_text)
                bid_documents_collection = self.clean_data(bid_documents_collection)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('四、招标文件的获取([\s\S]*?)五、', content_text)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('四、文件获取([\s\S]*?)五、', content_text)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('6．招标文件的获取([\s\S]*?)7．', content_text)
            if not bid_documents_collection:
                bid_documents_collection = utils.re_find_one('获取谈判采购文件[:：]([\s\S]*?)\d+、', content_text)
            bid_submission = utils.re_find_one('投标文件的递交(\s\S*?)<[bs]', detail_content)
            bid_submission = self.clean_data(bid_submission)
            if not bid_submission:
                bid_submission = utils.re_find_one('投标文件的递交([\s\S]*?)<p><strong>', detail_content)
                bid_submission = self.clean_data(bid_submission)
            if not bid_submission:
                bid_submission = utils.re_find_one('递交投标（响应）文件截止时间、开标时间及地点([\s\S]*?)八、联系方式', content_text)
                bid_submission = self.clean_data(bid_submission)
            if not bid_submission:
                bid_submission = utils.re_find_one('五、投标文件的递交([\s\S]*?)六、评标办法', content_text)
            if not bid_submission:
                bid_submission = utils.re_find_one('投标文件递交方法[:：]([\s\S]*?){1}、', content_text)
            if not bid_submission:
                bid_submission = utils.re_find_one('\d+\.投标文件的[提递]交([\s\S]*?)\d+\.', content_text)

            publish_announcements_media = html.xpath(
                'string(//table/tbody/tr//*[contains(text(),"发布媒介")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"公示媒介")]/ancestor::td[1]/following-sibling::td[1])')
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('发布媒体：(.*?)[<，。]', detail_content)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('发布公告的媒介(.*?)[，。|<p]', detail_content)
                publish_announcements_media = self.clean_data(publish_announcements_media)
            if not publish_announcements_media or publish_announcements_media == '：':
                publish_announcements_media = utils.re_find_one('三、公告发布媒体(.*?)四、', content_text)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('七、发布公告的媒介[：:]([\s\S]*?)八、', content_text)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('发布公告的媒介([\s\S]*?)<strong>', detail_content)
                publish_announcements_media = self.clean_data(publish_announcements_media)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('七、发布公告的媒介([\s\S]*?)八、联系方式', content_text)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('\d+\.发布公告的媒介([\s\S]*?)\d+\.', content_text)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('公告媒体[:：](.*?)\n', content_text1)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('发布媒体[:：](.*?)\n', content_text1)
            if not publish_announcements_media:
                publish_announcements_media = utils.re_find_one('四、公告发布媒体([\s\S]*?)五、', content_text1)
            other_requirements = utils.re_find_one('其他补充事宜([\s\S]*?)</[ph]', detail_content)
            other_requirements = self.clean_data(other_requirements)
            if '七、' in other_requirements:
                other_requirements = utils.re_find_one('(.*?)七、', other_requirements)
            if not other_requirements:
                other_requirements = utils.re_find_one('其他补充事宜([\s\S]*?)<b', detail_content)
                other_requirements = self.clean_data(other_requirements)
                if '七、' in other_requirements:
                    other_requirements = utils.re_find_one('([\s\S]*?)七、', other_requirements)
            if not other_requirements:
                other_requirements = html.xpath('string(//td[text()="商务要求"]/following-sibling::td[1])')
            if other_requirements:
                other_requirements = str(other_requirements).strip().lstrip(':').lstrip('：').strip()
            if not tenderer:
                tenderer = html.xpath(
                    'string(//td[text()="招标人"]/following-sibling::td[1]|//span[@name="psgsjbxx_CGRMC"]|//p//span[text()="招标人："]/following-sibling::span[1]|//table/tbody/tr//span[text()="招标人"]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[text()="采购单位"]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"建设单位")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"建设单位")]/ancestor::td[1]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"招标单位")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"招标单位")]/ancestor::td[1]/following-sibling::td[1])')
            if not tenderer:
                tenderer = utils.re_find_one('招标人[：:]([\s\S]*?)</t', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
                if tenderer == '-':
                    tenderer = ''
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('招标人[：:]([\s\S]*?)\n', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('招标人[：:](.*?)</span', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('招标人[：:]</span><span>(.*?)</span>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('招标人[：:]([\s\S]*?)\n', content_text)
            if not tenderer:
                tenderer = utils.re_find_one('建设单位（招标人）[:：]([\s\S]*?)</p>', detail_content)
                tenderer = self.clean_data(tenderer)
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('采购单位[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer or len(tenderer) > 50:
                tenderer = utils.re_find_one('采购人.*?[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer or ';' in tenderer or '00时。' in tenderer:
                tenderer = utils.re_find_one('采购人[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer:
                tenderer = utils.re_find_one('采购单位名称[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer:
                tenderer = utils.re_find_one('采购单位[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer:
                tenderer = utils.re_find_one('招标机构[：:]([\s\S]*?)</p>', re.sub('\s+', '', detail_content))
                tenderer = self.clean_data(tenderer)
            if not tenderer:
                tenderer = utils.re_find_one('询价人[:：]([\s\S]*?)</p>', detail_content)
                tenderer = self.clean_data(tenderer)
            if not tenderer:
                tenderer = utils.re_find_one('采购人信息\n名称[：:](.*?)\n', content_text)
            tenderer_tel = html.xpath('string(//table/tbody/tr/td[text()="项目联系电话"]/following-sibling::td[1])')
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('招标人：[\s\S]*?电话[：:]([\s\S]*?)<p', re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if '具体联系方式请根据网站首页“联系我们”列表中查找相应客服经理电话' in tenderer_tel:
                tenderer_tel = ''
            if not tenderer_tel or len(tenderer_tel) > 50:
                tenderer_tel = utils.re_find_one('招标人：[\s\S]*?电话[：:](.*?)\n', content_text)
            if not tenderer_tel or len(tenderer_tel) > 50:
                tenderer_tel = utils.re_find_one('招标人：[\s\S]*?电话[：:]([\s\S]*?)\n', content_text)
            if not tenderer_tel or len(tenderer_tel) > 50:
                tenderer_tel = utils.re_find_one('招标人：[\s\S]*?联系方式[：:]([\s\S]*?)<p', re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel or len(tenderer_tel) > 50:
                tenderer_tel = utils.re_find_one('招标人[：:][\s\S]*?电话\(传真\)[：:](.*?)</span',
                                                re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel or len(tenderer_tel) > 50:
                tenderer_tel = utils.re_find_one('采购人（甲方）[\s\S]*?联系方式[：:]([\s\S]*?)<p',
                                                re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('建设单位（招标人）[\s\S]*?联系电话[：:]([\s\S]*?)<p',
                                                re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('采购人名称[\s\S]*?联系电话[：:]([\s\S]*?)<p', re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('采购人信息\n名称[：:].*?\n联系方式[:：](.*?)\n', content_text)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('采购人电话[：:]([\s\S]*?)</p', re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('招标机构[：:].*?电话[:：]([\s\S]*?)</p', re.sub('\s+', '', detail_content))
                tenderer_tel = self.clean_data(tenderer_tel)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('采购单位联系人和联系方式[:：](.*?)\n', content_text1)
            if not tenderer_tel or len(tenderer_tel) > 50 or '4008100100转4' in tenderer_tel:
                tenderer_tel = utils.re_find_one('采购人[:：].*?联系人[:：].*?电话[：:](\d+)', re.sub('\s+', '', content_text))
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('招标人[：:][\s\S]*?电话[:：](.*?)\n', content_text)
            if not tenderer_tel:
                tenderer_tel = utils.re_find_one('项目联系人及联系方式[:：](.*?)</p>', detail_content)
                tenderer_tel = self.clean_data(tenderer_tel)
            if tenderer_tel:
                if '。' in tenderer_tel:
                    tenderer_tel = utils.re_find_one('(.*?)[。）]', tenderer_tel)
                tenderer_tel = re.sub('<.*?>', '', tenderer_tel)
            if '具体联系方式请根据网站首页“联系我们”列表中查找相应客服经理电话' in tenderer_tel:
                tenderer_tel = ''
            if not bid_agency:
                bid_agency = html.xpath(
                    'string(//*[contains(text(),"代理机构")]/ancestor::td[1]/following-sibling::td[1]|//p//*[text()="招标代理机构："]/following-sibling::span[1]|//table/tbody/tr/td[text()="代理机构名称"]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"招标代理")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"招标代理")]/ancestor::td[1]/following-sibling::td[1])')
            if not bid_agency:
                bid_agency = utils.re_find_one('招标人：[\s\S]*?代理机构[：:]([\s\S]*?)<p', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('招标人：[\s\S]*?代理[：:]([\s\S]*?)<p', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('代理机构[：:](.*?)</', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('招标代理机构[：:](.*?)</span', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
                if not bid_agency:
                    bid_agency = utils.re_find_one('招标代理机构[：:](.*?)\n', content_text)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('招标代理[：:](.*?)</', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('运维公司名称[：:](.*?)</p', re.sub('\s+', '', detail_content))
                bid_agency = self.clean_data(bid_agency)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = utils.re_find_one('招标代理机构[:：](.*?)</p>', detail_content)
                bid_agency = self.clean_data(bid_agency)
                if not bid_agency:
                    bid_agency = utils.re_find_one('招标代理机构[：:](.*?)\n', content_text1)
            if not bid_agency or len(bid_agency) > 50:
                bid_agency = html.xpath(
                    'string(//td[text()="招标代理"]/following-sibling::td[1]|//span[@name="psgs_DLJGMC"])')
            if not bid_agency:
                bid_agency = utils.re_find_one('代理机构信息\n名称[:：](.*?)\n', content_text)
            bid_agency_tel = utils.re_find_one('招标人：[\s\S]*?代理[\s\S]*?电话[:：]([\s\S]*?)<p',
                                              re.sub('\s+', '', detail_content))
            bid_agency_tel = self.clean_data(bid_agency_tel)
            if tenderer_tel and bid_agency_tel:
                if str(bid_agency_tel) == str(tenderer_tel):
                    bid_agency_tel = utils.re_find_one('采购代理机构[\s\S]*?联系电话[\s\S]*?[:：]([\s\S]*?)</p',
                                                      re.sub('\s+', '', detail_content))
                    bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel or len(bid_agency_tel) > 100:
                bid_agency_tel = utils.re_find_one('招标人：[\s\S]*?代理[\s\S]*?联系方式[:：]([\s\S]*?)[<p，。;]',
                                                  re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel or len(bid_agency_tel) > 100:
                bid_agency_tel = utils.re_find_one('代理机构电话[:：]([\s\S]*?)</p', re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel or len(bid_agency_tel) > 100:
                bid_agency_tel = utils.re_find_one('运维公司名称[\s\S]*?联系电话[:：]([\s\S]*?)</p',
                                                  re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel:
                bid_agency_tel = utils.re_find_one('代理机构名称[:：].*?联系电话[:：]([\s\S]*?)</p',
                                                  re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel:
                bid_agency_tel = utils.re_find_one('代理机构[:：].*?电话\(传真\)[:：](.*?)</span',
                                                  re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if not bid_agency_tel:
                bid_agency_tel = utils.re_find_one('招标代理机构[:：].*?电话[:：]([\s\S]*?)</p', re.sub('\s+', '', detail_content))
                bid_agency_tel = self.clean_data(bid_agency_tel)
            if '具体联系方式请根据网站首页' in bid_agency_tel or '打印' in bid_agency_tel:
                bid_agency_tel = ''
            if not bid_agency_tel:
                bid_agency_tel = html.xpath(
                    'string(//table/tbody/tr/td[text()="代理机构联系方式"]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"招标代理联系电话")]/following-sibling::td[1])')
            if not bid_status:
                bid_status = html.xpath('string(//td[text()="状态"]/following-sibling::td[1])')
                bid_status = self.clean_data(bid_status)
            if not bid_status:
                if '采购已经结束' in detail_content:
                    bid_status = '已结束'
            if not bidder:
                bidder = html.xpath(
                    'string(//table/tbody/tr/td[contains(text(),"中标单位")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"中标人")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"中标人")]/ancestor::td[1]/following-sibling::td[1])')
            if not bidder:
                bidder = utils.re_find_one('中标单位名称[:：]([\s\S]*?)</p>', detail_content)
                bidder = self.clean_data(bidder)
            if not bidder:
                bidder = utils.re_find_one('中标单位[:：]([\s\S]*?)</p>', detail_content)
                bidder = self.clean_data(bidder)
            if not bidder:
                bidder = utils.re_find_one('中标单位[:：]([\s\S]*?)\d+、', re.sub('\s+', '', content_text))
                bidder = self.clean_data(bidder)
            if not bidder:
                bidder = utils.re_find_one('供应商名称[:：]([\s\S]*?)</p>', detail_content)
                bidder = self.clean_data(bidder)
            if not bidder:
                bidder = utils.re_find_one('供应商（乙方）[:：]([\s\S]*?)</p>', detail_content)
                bidder = self.clean_data(bidder)
            if not bid_price:
                bid_price = html.xpath(
                    'string(//table/tbody/tr/td[contains(text(),"中标价格")]/following-sibling::td[1]|//table/tbody/tr/td[contains(text(),"中标价")]/following-sibling::td[1]|//table/tbody/tr//*[contains(text(),"中标价")]/ancestor::td[1]/following-sibling::td[1])')
            if not bid_price:
                bid_price = utils.re_find_one('中标金额[:：]([\s\S]*?)</p>', detail_content)
            if not bid_price:
                bid_price = utils.re_find_one('中标价[:：]([\s\S]*?)</p>', detail_content)
                bid_price = self.clean_data(bid_price)
            if not bid_price:
                bid_price = utils.re_find_one('中标（成交）金额[:：]([\s\S]*?元)', detail_content)
                bid_price = self.clean_data(bid_price)
            if not bid_price:
                bid_price = utils.re_find_one('合同金额[:：](.*?)</p>', detail_content)
                bid_price = self.clean_data(bid_price)
            if not bid_price:
                bid_price = utils.re_find_one('合同金额（元）[:：](.*?)</p>', detail_content)
                bid_price = self.clean_data(bid_price)
                if bid_price:
                    bid_price = str(bid_price).strip() + '元'
            if not bid_price:
                bid_price = utils.re_find_one('投标报价</a>[:：]([\s\S]*?元)', re.sub('\s+', '', detail_content))
                bid_price = self.clean_data(bid_price)
            if not bid_price:
                bid_price = html.xpath('string(//span[contains(text(),"合同金额（元）：")]/../following-sibling::p[1])')
                bid_price = str(bid_price).replace('元', '').strip()
                try:
                    bid_price = float(bid_price)
                    bid_price = str(bid_price).strip() + '元'
                except Exception as e:
                    bid_price = ''
            if not bid_price:
                bid_price = html.xpath('string(//table/tbody/tr/td[text()="总中标金额"]/following-sibling::td[1])')
                bid_price = str(bid_price).replace('（人民币）', '').replace('￥', '').strip()
            if not bid_price:
                bid_price = utils.re_find_one('总成交金额（元）[:：](.*?)（人民币）', content_text)
                if bid_price:
                    bid_price = str(bid_price).strip() + '元'
            if bid_price:
                if '元' not in bid_price and '圆' not in bid_price:
                    if '万元' in content_text:
                        bid_price = str(bid_price).strip() + '万元'
                    else:
                        bid_price = str(bid_price).strip() + '元'
                else:
                    bid_price = bid_price
            if bidder and bid_price:
                bid_result = str(bidder) + ' ' + str(bid_price)
            else:
                bid_result = ''
            data[TABField.bid_time] = publish_time
            data[TABField.publish_time] = publish_time
            data[TABField.title] = item[0]
            data[TABField.area] = area
            data[TABField.content] = str(content_text1).replace('()DD000E;', '').replace('EE000E;', '').replace(
                'FF000E;', '').replace(' ', ' ').strip()
            if bid_condition:
                data[TABField.bid_condition] = bid_condition.strip()
            else:
                data[TABField.bid_condition] = ''
            if entry_name:
                data[TABField.entry_name] = str(entry_name).replace('项目名称：', '').replace('1、', '').strip()
            else:
                data[TABField.entry_name] = ''
            if construction_location:
                data[TABField.construction_location] = construction_location.strip()
            else:
                data[TABField.construction_location] = ''
            if construction_scale:
                data[TABField.construction_scale] = construction_scale.strip()
            else:
                data[TABField.construction_scale] = ''
            if bid_control_price:
                if '万元' in bid_control_price:
                    data[TABField.bid_control_price] = bid_control_price
                elif '元' in bid_control_price and '万元' not in bid_control_price:
                    try:
                        bid_control_price = float(
                            str(bid_control_price).replace('￥', '').replace(',', '').replace('元', '').strip()) / 10000
                        data[TABField.bid_control_price] = str(bid_control_price) + '万元'
                    except Exception as e:
                        data[TABField.bid_control_price] = str(bid_control_price).replace('\n\n\n', '\n').strip()
                        self.log.error('{}-{}价格转换错误:{}'.format(detail_url, bid_control_price, e))
                else:
                    data[TABField.bid_control_price] = bid_control_price
            else:
                data[TABField.bid_control_price] = ''
            if planned_duration:
                data[TABField.planned_duration] = planned_duration.strip()
            else:
                data[TABField.planned_duration] = ''
            if bid_section:
                data[TABField.bid_section] = bid_section.strip()
            else:
                data[TABField.bid_section] = ''
            if bid_scope:
                data[TABField.bid_scope] = bid_scope.strip()
            else:
                data[TABField.bid_scope] = ''
            if bid_qualification_reqirement:
                data[TABField.bid_qualification_reqirement] = bid_qualification_reqirement.strip()
            else:
                data[TABField.bid_qualification_reqirement] = ''
            if bid_documents_collection:
                data[TABField.bid_documents_collection] = bid_documents_collection.strip()
            else:
                data[TABField.bid_documents_collection] = ''
            if bid_submission:
                data[TABField.bid_submission] = bid_submission.strip()
            else:
                data[TABField.bid_submission] = ''
            if publish_announcements_media:
                data[TABField.publish_announcements_media] = publish_announcements_media.strip()
            else:
                data[TABField.publish_announcements_media] = ''
            if other_requirements:
                data[TABField.other_requirements] = other_requirements.strip()
            else:
                data[TABField.other_requirements] = ''
            if tenderer:
                data[TABField.tenderer] = tenderer.strip()
            else:
                data[TABField.tenderer] = ''
            if tenderer_tel:
                data[TABField.tenderer_tel] = tenderer_tel.strip()
            else:
                data[TABField.tenderer_tel] = ''
            if bid_agency:
                data[TABField.bid_agency] = bid_agency.strip()
            else:
                data[TABField.bid_agency] = ''
            if bid_agency_tel:
                data[TABField.bid_agency_tel] = bid_agency_tel.strip()
            else:
                data[TABField.bid_agency_tel] = ''
            if bid_status:
                data[TABField.bid_status] = bid_status.strip()
            elif bidder:
                data[TABField.bid_status] = '已结束'
            else:
                data[TABField.bid_status] = ''
            if bidder:
                data[TABField.bidder] = bidder.strip()
            else:
                data[TABField.bidder] = ''
            if bid_price:
                if '万元' in bid_price:
                    data[TABField.bid_price] = bid_price
                elif '元' in bid_price and '万元' not in bid_price:
                    try:
                        bid_price = float(str(bid_price).replace(',', '').replace('元', '').strip()) / 10000
                        data[TABField.bid_price] = str(bid_price) + '万元'
                    except Exception as e:
                        data[TABField.bid_price] = str(bid_price)
                        self.log.error('{}-{}价格转换错误:{}'.format(detail_url, bid_price, e))
                else:
                    data[TABField.bid_price] = bid_price.strip()
            else:
                data[TABField.bid_price] = ''
            if bid_result:
                data[TABField.bid_result] = bid_result.strip()
            else:
                data[TABField.bid_result] = ''
            # pprint.pprint(data)
            self.upload(data)


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
    keyword = ['']
    # bid = BidZGDZ(debug=False)
    # bid.process_item(params)
    BidZGDZ.run(keyword)
