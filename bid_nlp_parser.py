#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/5/28 2:13 下午
@Author: CZC
@File: bid_nlp_parser.py
"""
import re
from functools import cmp_to_key

from esmre import esm
from bid_conf import conf_3
from bid_tools import utils
import sys
import os
sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')
PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Bid_company_parser(object):
    def __init__(self):
        self.company_length_limit = 30  # unicode
        self.zhongbiao_offset = 100  # utf8
        self.zhaobiao_offset = 90  # uft8
        self.agent_offset = 80  # utf8
        self.project_leader_offset = 20
        self.min_offset = 5
        self.min_leader_offset = 2
        self.min_time_offset = 4
        self.phone_offset = 30
        self.min_phone_offset = 5
        self.project_number_offset = 40
        self.end_time_offset = 22
        self.finish_time_offset = 22
        self.win_bid_announcement_time_offset = 22
        self.project_name_offset = 50
        self.duration_offset = 4
        self.bid_scope_offset = 100
        self.receive_offset = 100
        self.submit_offset = 100
        self.medium_offset = 100
        # self.end_list = ['，', '。', '；', ';', ' ', '；', '\t', '\r\n']
        self.common_end_list = [',', '/', '\d', '，', '。', '；', ';', ' ', '；', '\s', "$"]
        self.phone_end_list = ["”", ',', '，', '。', '；', ';', ' ', '；', '（', '\s', "$"]
        self.project_leader_end_list = [',', '/', '\d', '，', '。', '；', ';', ' ', '；', '\s', "$"]
        self.project_number_end_list = ["”", "）", '、', ',', '，', '。', '；', ';', ' ', '；', '\s', "$", "[\u4e00-\u9fa5]"]
        self.time_end_list = ['、', ',', '，', '。', '；', ';', ' ', '；', '\s', "$", "（", "\(", "至"]
        self.duration_end_list = [',', '/', '，', '。', '；', ';', ' ', '；', '\s', '天', "$"]


        self.zhaobiao_company_index = esm.Index()
        self.agent_company_index = esm.Index()
        self.zhongbiao_company_index = esm.Index()
        self.bid_type_zhongbiao_index = esm.Index()

        self.init_index(self.zhaobiao_company_index, conf_3.zhaobiao_company_keyword_list)
        self.init_index(self.agent_company_index, conf_3.agent_keyword_list)
        self.init_index(self.zhongbiao_company_index, conf_3.zhongbiao_company_keyword_list)

        # self.person_pre_list = open('{}/Bid/bid_conf/person_pre.conf'.format(PROJECTDIR), encoding='utf-8').read().split('\n')[:-1]
        self.person_pre_list = open('{}/Bid/bid_conf/person_pre.conf'.format(PROJECTDIR)).read().split('\n')[:-1]
        # 建立多模匹配自动机
        self.company_pre_index = esm.Index()
        # pre_list = open('{}/Bid/bid_conf/company_pre.txt'.format(PROJECTDIR), encoding='utf-8').read().split('\n')[:-1]
        pre_list = open('{}/Bid/bid_conf/company_pre.txt'.format(PROJECTDIR)).read().split('\n')[:-1]
        for company_pattern in pre_list:
            if company_pattern != '':
                self.company_pre_index.enter(company_pattern)
        self.company_pre_index.fix()
        self.company_length_limit = 36
        self.replace_str = [',', '.', '，', '。', '：', ':', '、', '；', ';', ' ', '；']

    def init_index(self, esm_index, company_keyword_list):
        for keyword in company_keyword_list:
            esm_index.enter(keyword)
        esm_index.fix()

    def do_parser(self, content, title):
        '''获取公司'''

        # 1 根据关键字查找公司名

        zhongbiao_company_list = self.get_company_list(content, self.zhongbiao_company_index, conf_3.zhongbiao_company_end_list, self.zhongbiao_offset)
        if not zhongbiao_company_list:
            for step in range(50, 101, 25):
                # note 特殊处理
                # content = "中标单位" + content.split("中标单位")[-1]
                content = content.replace("中标结果公告", "")
                zhongbiao_company_list = self.get_company_list(content, self.zhongbiao_company_index, conf_3.zhongbiao_company_end_list, self.zhongbiao_offset + step)
                if zhongbiao_company_list:
                    break
        zhaobiao_company_list = self.get_company_list(content, self.zhaobiao_company_index, conf_3.zhaobiao_company_end_list, self.zhaobiao_offset)
        agent_company_list = self.get_company_list(content, self.agent_company_index, conf_3.agent_company_end_list, self.agent_offset)

        zhaobiao_company = None
        if zhaobiao_company_list:
            if len(zhaobiao_company_list) >= 2:
                find_flag = False
                for item in zhaobiao_company_list:
                    if '公司' not in item:
                        zhaobiao_company = item
                        find_flag = True
                        break
                if not find_flag:
                    zhaobiao_company = zhaobiao_company_list[0]
            else:
                zhaobiao_company = zhaobiao_company_list[0]

        agent = ''
        if agent_company_list:
            for agen in agent_company_list:
                if agen not in zhaobiao_company_list:
                    agent = agen
                    break
            if agent == '':
                agent = agent_company_list[0]

        # 2 若招标或者代理公司未找到，则匹配(\S*)受(\S+)委托
        ret = utils.re_find_one('(\S*)受(\S+)委托', content)
        if ret:
            tmp_agent = self.get_one_company(ret[0], conf_3.agent_company_end_list)
            tmp_zhaobiao_company = self.get_one_company(ret[1], conf_3.zhaobiao_company_end_list)
            agent = tmp_agent if tmp_agent else agent
            zhaobiao_company = tmp_zhaobiao_company if tmp_zhaobiao_company else zhaobiao_company

        # 3 若招标公司还未找到，则从标题中寻找
        if not zhaobiao_company:
            zhaobiao_company = self.get_one_company(title, conf_3.zhaobiao_company_end_list)
        # todo note 临时补丁，中标只选一家
        if zhongbiao_company_list:
            zhongbiao_company_list = sorted(zhongbiao_company_list, key=cmp_to_key(self.len_compare))
            zhongbiao_company_list = [zhongbiao_company_list[-1]]
        result_data = self.filter_company_list(zhaobiao_company, zhongbiao_company_list, agent)

        # result_data["tender_unit"] = result_data["zhaobiao"]
        # result_data["agency"] = result_data["agent"]

        # result_data["bid_winner "] = result_data["zhongbiao"]
        # for i in range(len(result_data["zhongbiao"])):
        #     result_data["zhongbiao"][i] = result_data["zhongbiao"][i]

        project_leader = self.get_leader_result(content, conf_3.project_leader_keyword_list, self.project_leader_offset, self.project_leader_end_list)
        result_data['project_leader'] = project_leader
        phone = self.get_phone_result(content, conf_3.phone_keyword_list, self.phone_offset, self.phone_end_list)
        result_data['phone'] = phone
        project_number = self.get_project_number_result(content, conf_3.project_number_keyword_list, self.project_number_offset, self.project_number_end_list)
        result_data['project_number'] = project_number
        bid_finish_time = self.get_time_result(content, conf_3.bid_finish_time_keyword_list, self.finish_time_offset, self.time_end_list)
        result_data['bid_finish_time'] = bid_finish_time
        bid_end_time = self.get_time_result(content, conf_3.bid_end_time_keyword_list, self.end_time_offset, self.time_end_list)
        result_data['bid_end_time'] = bid_end_time
        win_bid_announcement_time = self.get_time_result(content, conf_3.win_bid_announcement_time_keyword_list, self.win_bid_announcement_time_offset, self.time_end_list)
        result_data['win_bid_announcement_time'] = win_bid_announcement_time
        project_name = self.get_common_result(content, conf_3.project_name_keyword_list, self.project_name_offset, self.common_end_list)
        result_data['project_name'] = project_name
        duration = self.get_duration_result(content, conf_3.duration_keyword_list, self.duration_offset, self.duration_end_list)
        result_data['duration'] = duration
        bid_scope = self.get_common_result(content, conf_3.bid_scope_keyword_list, self.bid_scope_offset, self.common_end_list)
        result_data['bid_scope'] = bid_scope
        receive = self.get_common_result(content, conf_3.receive_keyword_list, self.receive_offset,
                                           self.common_end_list)
        result_data['receive'] = receive
        submit = self.get_common_result(content, conf_3.submit_keyword_list, self.submit_offset, self.common_end_list)
        submit = submit.split("截止时间：")[-1]
        result_data['submit'] = submit
        medium = self.get_common_result(content, conf_3.medium_keyword_list, self.medium_offset, self.common_end_list)
        result_data['medium'] = medium
        bid_agency_tel = self.get_phone_result(content, conf_3.bid_agency_tel_keyword_list, self.phone_offset, self.phone_end_list)
        result_data['bid_agency_tel'] = bid_agency_tel

        return result_data

    def get_company_list(self, content, esm_index, end_list, offset):
        '''获取包含招标中标公司列表'''
        company_list = []
        if not content:
            return []

        content = content.replace(' ', '')
        content = content.replace('\t', '').replace(' ', '')
        # content = content.encode('utf-8')

        ret_list = esm_index.query(content)
        if ret_list:
            forward_offset = 60
            while not company_list and forward_offset:
                for ret in ret_list:
                    # pos = int(ret[0][0] // 2.5) - forward_offset + 20
                    # r1 = content.split(ret[1])[0]
                    # l1 = len(r1)
                    # r2 = content.split(ret[1])[1]
                    # l2 = len(r2)
                    # result_content = content[pos:pos + offset]
                    pos = ret[0][0]
                    result_content = content.encode('utf-8')[pos - offset//2:pos + offset]
                    result_content = result_content.decode("utf-8", 'ignore')
                    company = self.get_one_company(result_content, end_list)
                    if company:
                        company_list.append(company)
                forward_offset -= 20
        # company_list = list(set(company_list))
        return_list = []
        for company in company_list:
            if company not in return_list:
                return_list.append(company)
        return return_list

    def get_one_company(self, content, company_end_list):
        '''匹配一个公司返回'''
        for item in self.replace_str:
            content = content.replace(item, ' ')
        company_pre_ret = self.company_pre_index.query(content)

        pattern_list = []
        for ret in company_pre_ret:
            for end in company_end_list:
                pattern = '(' + ret[1] + '\S*' + end + ')'
                # pattern = ret[1] + '.*?' + end
                pattern_list.append(pattern)

        pattern_list = list(set(pattern_list))
        pattern_list.append("中标人 (\S*?公司)")
        pattern_list.append("招标人 (\S*?公司)")
        company_list = []
        for pattern in pattern_list:
            if not isinstance(content, str):
                pattern = pattern
            rets = re.findall(pattern, content)
            for ret in rets:
                if ret in conf_3.company_ban_list:
                    continue
                ret_lens = len(ret)
                if ret and self.min_offset <= len(ret) < self.company_length_limit:
                    company_list.append(ret)

        company_list = self.norm_company_list(company_list)
        company_list = self.rectify_multimode_company_list(company_list, content)
        if company_list:
            company_list = sorted(company_list, key=cmp_to_key(self.len_compare))
            return company_list[-1]
        return ''

    def len_compare(self, x, y):
        return len(x) - len(y)

    def filter_company_list(self, zhaobiao_company, zhongbiao_company_list, agent):
        '''格式化中标公司'''
        if agent and zhaobiao_company and agent == zhaobiao_company:
            result_data = {
                "tender_unit": zhaobiao_company,
                "bid_winner": ','.join(zhongbiao_company_list),
                "agency": agent
            }
            return result_data

        zhongbiao_company_list = [x for x in zhongbiao_company_list if x not in [zhaobiao_company] and x not in [agent]]
        zhongbiao_company = ",".join(zhongbiao_company_list)

        result_data = {
            "tender_unit": zhaobiao_company,
            "bid_winner": zhongbiao_company,
            "agency": agent
        }

        return result_data

    def norm_company_list(self, company_list):
        '''去除公司列表中所有子集,如 佛山市顺德区龙江镇教育局  顺德区龙江镇教育局'''
        result_list = []
        for company1 in company_list:
            found = False
            for company2 in company_list:
                if company1 == company2:
                    continue

                if company1 in company2:
                    found = True
                    break
            if not found:
                result_list.append(company1)
        result_list = list(set(result_list))
        return result_list

    def rectify_multimode_company_list(self, company_list, content):
        new_company_list = []
        for company in company_list:
            if ('）' in company and '（' not in company) or (')' in company and '(' not in company):
                re_str = " (.*?{})".format(company.replace(")", "）"))
                company = utils.re_find_one(re_str, content)
            new_company_list.append(company)
        return new_company_list

    def get_project_number_result(self, content, keyword_list, offset, end_list, pre_regular=None):
        result_list = []
        result = ''
        # content = content.replace(":", "")
        # content = content.replace("：", "")
        content = re.sub(" {4,}", "\n", content)
        content = content.replace(" ", "")
        content = content.replace("　", "")
        content = content.replace("\t", "")
        # content = re.sub('(?=\S) (?=\S)', "", content)
        for key in keyword_list:
            for end in end_list:
                re_state = '{}[\s:：]{{0,2}}(.+?){}'.format(key, end)
                results = re.findall(re_state, content)
                for result in results:
                    result = result.replace("\r", "").replace("\n", "").strip()
                    if re.findall("[\u4e00-\u9fa5]{3,}", result):
                        continue
                    if result and self.min_offset < len(result) < offset:
                        result_list.append(result)
                    else:
                        result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        # result = ",".join(result_list)
        return result

    def get_leader_result(self, content, keyword_list, offset, end_list):
        result_list = []
        result = ""
        # content = content.replace(":", "")
        # content = content.replace("：", "")
        content = re.sub(" {4,}", "\n", content)
        content = content.replace(" ", "")
        content = content.replace("　", "")
        content = content.replace("\t", "")
        for ban in conf_3.project_leader_ban_list:
            content = content.replace(ban, "")
        # content = re.sub('(?=\S) (?=\S)', "", content)
        stop_flag = False
        for key in keyword_list:
            for end in end_list:
                if not stop_flag:
                    re_state = '{}[\s:：]{{0,2}}(.+?){}'.format(key, end)
                    results = re.findall(re_state, content)
                    for result in results:
                        result = result.replace("\r", "").replace("\n", "").strip()
                        if result and self.min_leader_offset <= len(result) < offset and result[0] in self.person_pre_list:
                            result_list.append(result)
                            stop_flag = True
                        else:
                            result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        return result

    def get_phone_result(self, content, keyword_list, offset, end_list, pre_regular=None):
        result_list = []
        result = ""
        content = content.replace(":", "")
        content = content.replace("：", "")
        content = re.sub(" {5,}", "\n", content)
        for ban in conf_3.phone_ban_list:
            content = content.replace(ban, "")
        content = content.replace(" ", "")
        content = content.replace("　", "")
        # content = re.sub('(?=\S) (?=\S)', "", content)
        stop_flag = False
        for key in keyword_list:
            for end in end_list:
                re_state = '{}[\s\S]{{0,15}}?(\d\d.+?){}'.format(key, end)
                results = re.findall(re_state, content)
                for result in results:
                    result = result.replace("\r", "").replace("\n", "").strip()
                    if result and self.min_phone_offset < len(result) < offset:
                        if len(re.findall("[\u4e00-\u9fa5]", result)) < 2:
                            result_list.append(result)
                    else:
                        result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        return result

    def get_time_result(self, content, keyword_list, offset, end_list, pre_regular=None):
        result_list = []
        result = ''
        # content = content.replace(":", "")
        # content = content.replace("：", "")
        content = re.sub(" {4,}", "\n", content)
        content = content.replace(" ", "")
        content = content.replace("\t", "")
        # 针对变更公告
        content = re.sub("时间[\s\S]{10,25}?变更为", "时间", content)
        # content = re.sub('(?=\S) (?=\S)', "", content)
        for key in keyword_list:
            for end in end_list:
                if not pre_regular:
                    re_state = '{}[\s\S]{{0,15}}?(\d{{4}}.+?|\d{{1,2}}月.+?){}'.format(key, end)
                    result = utils.re_find_one(re_state, content)
                    # if not result:
                    #     re_state = '{}[\s\S]{{0,15}}?(\d{{1,2}}月.+?){}'.format(key, end)
                    #     result = utils.re_find_one(re_state, content)
                else:
                    re_state = '{}[\s\S]?({}.+?){}'.format(key, pre_regular, end)
                    result = utils.re_find_one(re_state, content)
                if result:
                    result_check = re.findall("[\u4e00-\u9fa5]{4,}", result)
                    if not result_check and self.min_time_offset < len(result) < offset:
                        result_list.append(result)
                    else:
                        result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        return result

    def get_duration_result(self, content, keyword_list, offset, end_list):
        result_list = []
        result = ""
        # content = content.replace(":", "")
        # content = content.replace("：", "")
        content = re.sub(" {4,}", "\n", content)
        content = content.replace(" ", "")
        content = content.replace("　", "")
        content = content.replace("\t", "")
        for ban in conf_3.project_leader_ban_list:
            content = content.replace(ban, "")
        # content = re.sub('(?=\S) (?=\S)', "", content)
        stop_flag = False
        for key in keyword_list:
            for end in end_list:
                if not stop_flag:
                    re_state = '{}[\s:：]{{0,2}}(\d+)[\s\S]*?{}'.format(key, end)
                    results = re.findall(re_state, content)
                    for result in results:
                        result = result.replace("\r", "").replace("\n", "").strip()
                        if result and 2 <= len(result) < offset:
                            result_list.append(result)
                            stop_flag = True
                        else:
                            result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        return result

    def get_common_result(self, content, keyword_list, offset, end_list):
        result_list = []
        result = ""
        # content = content.replace(":", "")
        # content = content.replace("：", "")
        content = re.sub(" {4,}", "\n", content)
        content = content.replace(" ", "")
        content = content.replace("　", "")
        content = content.replace("\t", "")
        for ban in conf_3.project_leader_ban_list:
            content = content.replace(ban, "")
        # content = re.sub('(?=\S) (?=\S)', "", content)
        stop_flag = False
        for key in keyword_list:
            for end in end_list:
                if not stop_flag:
                    re_state = '{}[\s:：]{{0,2}}(.+?){}'.format(key, end)
                    results = re.findall(re_state, content)
                    for result in results:
                        result = result.replace("\r", "").replace("\n", "").strip()
                        if result and self.min_offset <= len(result) < offset:
                            result_list.append(result)
                            stop_flag = True
                        else:
                            result = ''
        result_list = list(set(result_list))
        if result_list:
            result_lens = [len(i) for i in result_list]
            min_len = min(result_lens)
            result = result_list[result_lens.index(min_len)]
        return result