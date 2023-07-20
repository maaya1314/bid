#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2022/5/28 5:46 下午
@Author: CZC
@File: bid_money_parser.py
"""
import re
from esmre import esm
from bid_conf import conf_3
from bid_tools import utils
import sys

sys.path.append('..')
sys.path.append('../..')
sys.path.append('../../..')


class Bid_money_parser(object):
    def __init__(self):
        self.min_money = 100  # 可以屏蔽一些未过滤掉的数量信息
        self.max_money = 10000000000
        self.content_length = 30
        self.deal_num = 2
        self.money_regex = re.compile('\d+.\d+')
        self.money_wan_regex = re.compile('\d+.\d+万')
        self.table_money_regex = re.compile(r'^[1234567890,\.万元]+$')
        self.budget_index = esm.Index()
        for keyword in conf_3.bid_budget_keyword_list:
            self.budget_index.enter(keyword)
        self.budget_index.fix()

        self.money_index = esm.Index()
        for keyword in conf_3.bid_money_keyword_list:
            self.money_index.enter(keyword)
        self.money_index.fix()

        self.money_regex = re.compile(u'\d+\.\d+|\d+')
        self.money_map = {u"亿": 100000000, u"万": 10000, u"百万": 1000000, u"M": 1000000,
                          u"千": 1000, u'百': 100, u'佰': 100, u'十': 10}
        self.money_type_list = [u'美元', u'欧元', u'港元', u'港币', u'英镑', u'澳元', u'日元', u'元']
        self.chs_money_map = {u'一': '1', u'二': '2', u'三': '3', u'四': '4', u'五': '5', u'六': '6', u'七': '7', u'八': '8',
                              u'九': '9', u'十': '10',
                              u'零': '0', u'壹': '1', u'贰': '2', u'叁': '3', u'肆': '4', u'伍': '5', u'陆': '6', u'柒': '7',
                              u'捌': '8', u'玖': '9', u'拾': '10',
                              u'万': u'万sep', u'千': u'千sep', u'百': u'百sep', u'佰': u'佰sep',
                              }

        self.money_type_kv = {u'美元': u'美元', u"USD": u"美元",
                              u"元": u"人民币", u"RMB": u"人民币", u"人民币": u"人民币",
                              u'欧元': u'欧元', u"EUR": u"欧元",
                              u'镑': u'英镑', u"GBP": u"英镑",
                              u'日元': u'日元', u"JPY": u"日元",
                              u'韩币': u'韩币', u"KRW": u"韩币",
                              u'港币': u'港币', u'HKD': u'港币'}

    def do_parser(self, content, parser_select=None):
        '''获取正文中金额'''
        money_list = []
        budget_money_list = []
        if not content:
            return money_list, budget_money_list
        # content = content.encode('utf8')
        content = re.sub(" {4,}", "\r\n", content)
        content = content.replace(" ", "")
        content = content.replace("　", "")
        content = content.replace(',', '').replace('，', '').replace(' ', '')

        # 1 获取中标金额
        money_list = self.get_money(content, self.money_index, self.content_length, conf_3.bid_money_keyword_list)
        for num in range(self.deal_num):
            if not money_list:
                money_list = self.get_money(content, self.money_index, self.content_length + (num + 1) * 15, conf_3.bid_money_keyword_list)
            else:
                break

        if money_list:
            money_list = self.norm_money_list(money_list)

        # 2 获取招标预算金额
        budget_money_list = self.get_money(content, self.budget_index, self.content_length, conf_3.bid_budget_keyword_list)
        for num in range(self.deal_num):
            if not budget_money_list:
                budget_money_list = self.get_money(content, self.budget_index, self.content_length + num * 15, conf_3.bid_budget_keyword_list)
            else:
                break
        if budget_money_list:
            budget_money_list = self.norm_money_list(budget_money_list)
        # return money_list, budget_money_list
        budget_money = "" if not budget_money_list else "".join(budget_money_list[0])
        win_money = "" if not money_list else "".join(money_list[0])
        return win_money, budget_money

    def get_money(self, content, esm_index, content_length, conf_keyword_list=None):
        money_list = []
        money_ret = esm_index.query(content)
        if money_ret:
            find_flag = False
            for ret in money_ret:
                # pos = int(ret[0][0] // 2.5) - 10
                # relate_content = content[pos:pos + content_length]
                pos = ret[0][0]
                result_content = content.encode('utf-8')[pos:pos + content_length]
                relate_content = result_content.decode("utf-8", 'ignore')
                money = utils.re_find_one('\d+(?:\\.\d+)?万', relate_content)
                if money:
                    if money == "365":
                        continue
                    money, unit = self.transfer_money(money)
                    money = money
                    money_list.append((money, unit))
                    find_flag = True
                    # todo 暂时只取一个就跳出
                    break
            if not find_flag:
                for keyword in conf_keyword_list:
                    find_flag2 = False
                    keyword_split_list = content.split(keyword)
                    keyword_pos_list = [len(x) for x in keyword_split_list]
                    pos_list = []
                    start_pos = 0
                    for i in range(len(keyword_pos_list)):
                        start_pos += keyword_pos_list[i] + len(keyword)
                        pos_list.append(start_pos)
                    for pos in pos_list:
                        relate_content = content[pos:pos + content_length]
                        if '万元' in relate_content:
                            find_flag2 = True
                        money_yuan_list = re.findall('(\d+(?:\\.\d+)?)', relate_content)
                        for money_yuan in money_yuan_list:
                            if money_yuan == '365':
                                continue
                            if len(str(int(float(money_yuan)))) < 5 and not find_flag2:
                                money_yuan = ''
                            if money_yuan:
                                yuan_split = relate_content.split(money_yuan)[0]
                                relate_find = utils.re_find_one('\t{3,5}\S+\t{3,5}', yuan_split)
                                if relate_find:
                                    money_yuan = None
                            if money_yuan:
                                if find_flag2:
                                    money_yuan = money_yuan + '万'
                                money_yuan, unit = self.transfer_money(money_yuan)
                                money_yuan = money_yuan
                                money_list.append((money_yuan, unit))
                                # todo 暂时只取一个就跳出
                                break
        return money_list

    def get_table_sum_money(self, content):
        content = content.replace(' ', '').replace(' ', '').replace('：', '')  # 注意前面两个空格不一样
        # 表格内以大于2个\t元素为分割,一般表格形式才会出现多个\t连在一起的情况
        content_list = re.split('\t{2,}', content)
        ret_list = []
        for item in content_list:
            # 有除了数字、逗号、句号除了"万"、"元"意外的汉字的元素均为非金额,则置空
            # print item
            if len(self.table_money_regex.findall(item)) > 0:
                ret_list.append(item)
                # if item.__contains__('.'):
                #     ret_list.append(item)
                # else:
                #     ret_list.append('')
            else:
                ret_list.append('')
        ret_sum = 0
        max_list = []
        sep_list = []
        line_count = 0
        for item in ret_list:
            if item != '':
                try:
                    flag = False
                    item = item.replace('元', '')
                    if item.__contains__('万'):
                        item = item.replace('万', '')
                        flag = True
                    if flag:
                        float_item = float(item) * 10000
                    else:
                        float_item = float(item)
                except:
                    float_item = 0.0

                sep_list.append(float_item)
            else:
                if sep_list == []:
                    continue
                # 同一行的多个数字元素,取值最大的一列(一般价格比数量等要高)
                line_count += 1
                # 连续3个空格时,认为是下一行
                if line_count >= 3:
                    max_list.append(max(sep_list))
                    line_count = 0
                    sep_list = []
        for item in max_list:
            ret_sum += item
        return str(ret_sum)

    def norm_money_list(self, money_list):
        '''根据特性格式化金额，过滤干扰数字'''
        result_list = []
        for item in money_list:
            if len(item) != 2:
                continue
            digit = item[0]
            if digit and float(digit) > self.min_money and float(digit) < self.max_money:
                result_list.append(item)

        result_list = list(set(result_list))
        return result_list

    def transfer_money(self, src_money):
        '''转换3000万人民币成30000000'''
        money = ''
        money_unit = ''

        try:
            src_money = src_money.replace(',', '')
            ret = utils.re_find_one(self.money_regex, src_money)
            if ret:
                try:
                    digit = float(ret)
                except:
                    digit = 0
            else:
                return (src_money, money_unit)
        except:
            return (src_money, money_unit)

        flag = False
        for key, value in self.money_map.items():
            if key in src_money:
                if money == '' or money < digit * value:
                    money = digit * value
                flag = True
                # break

        if not flag:
            money = digit

        found = False
        for money_type in self.money_type_list:
            if money_type in src_money:
                money_unit = money_type
                found = True
                break
        if not found:
            money_unit = u'元'

        # money = str(money)
        money = '{:.2f}'.format(money)
        return (money, money_unit)


if __name__ == "__main__":

    import time

    obj = Bid_money_parser()

    begin_time = time.time()

    # content = '亳州市体育公园项目施工中标公示 招标人   建安投资控股集团有限公司   工程名称  亳州市体育公园项目施工（BZGC2016202）   招标方式  公开招标   开标时间  2016年10月19日9:30   中标单位名称  第一中标候选人：江苏南通三建集团股份有限公司 第二中标候选人：中国建筑第八工程局有限公司 第三中标候选人：中铁电气化局集团有限公司   中标价  第一中标候选人报价：壹亿零柒佰玖拾伍万捌仟贰佰玖拾壹元柒角贰分（小写：107958291.72元） 第二中标候选人报价：壹亿零伍佰玖拾万零肆仟陆佰肆拾元伍角陆分（小写：105904640.56元） 第三中标候选人报价：壹亿零壹佰捌拾玖万捌仟捌佰玖拾元陆角贰分（小写：101898890.62元）   项目负责人  第一中标候选人项目负责人：黄敏逵 第二中标候选人项目负责人：王先文 第三中标候选人项目负责人：朱鼎亚   第一中标候选人 业绩奖项  1、企业工程奖项： ①闸北区文化馆和大宁社区文化活动中心工程，荣获2012—2013年度中国建设鲁班奖（国家优质工程），颁发时间：2013年12月； ②镇江皇冠假日酒店工程，荣获2013—2014年度国家优质工程奖，颁发时间：2014年11月； 2、项目经理奖项： ①高速·滨湖时代广场C-01地块C3#—C7#楼及商业土建总施工，竣工日期：2014年11月； 3、施工企业奖项： ①荣获2015年度全国优秀施工企业，由中国施工业管理协会颁发，颁发时间：2016年3月； ②全国建筑业先进企业称号，由中国建筑业协会颁发，颁发时间：2011年12月。   第二中标候选人 业绩奖项  1、企业工程奖项： ①利通广场工程，荣获2012—2013年度中国建筑工程鲁班奖（国家优质工程奖），颁发时间：2013年12月。 ②上海浦东发展银行合肥综合中心工程，荣获2014—2015年度国家优质工程奖，颁发时间：2015年11月。 2、项目经理奖项： ①双山保儿片区旧村改造项目A-9-5地块（凯德MALL·新都心项目），竣工日期：2016年6月。 3、施工企业奖项： ①荣获2015年度全国优秀施工企业，由中国施工业管理协会颁发，颁发时间：2016年3月； ②全国建筑业先进企业称号，由中国建筑业协会颁发，颁发时间：2014年11月。   第三中标候选人 业绩奖项  1、项目经理奖项： ①新建铁路天津至秦皇岛客运专线唐山站房、滨海北站房、滦河站房工程标段施工，竣工日期：2013年6月。 2、施工企业奖项： ①全国建筑业先进企业称号，由中国建筑业协会颁发，颁发时间：2016年10月。   公示时间  至2016年10月25日   质疑（异议）联系电话  招标人：0558-5582632 招标机构：0558-5991108   投诉电话  市招管局：0558-5991109   备注  领取中标通知书时，请提供下列材料： 1. 企业住所地或亳州检察机关出具的该企业无行贿犯罪记录证明。 2.电子版综合治税信息表格，下载地址：http://www.bzztb.gov.cn/BZWZ/综合治税信息填报表格式_工程类.xls'
    content = '鼎城区人民法院鼎城法院采购A4纸采购项目的协议供货成交公告\t\t\t\t\t\t\t\t公告时间：2018年11月20日\t\t\t\t\t\t\t\t        鼎城区人民法院对鼎城法院采购A4纸采购项目进行协议采购，结果如下：\t\t\t\t一、采购编号：\t\t\t\t湘财采计[2018]012509号\t\t\t\t\t\t\t\t二、成交结果：\t\t\t\t\t\t\t\t\t \t\t\t\t\t成交供应商：常德澳伊文化有限责任公司\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t品目类别\t\t\t\t\t\t\t\t\t品目分类\t\t\t\t\t\t\t\t\t品目名称\t\t\t\t\t\t\t\t\t商品名称\t\t\t\t\t\t\t\t\t规格型号/技术指标\t\t\t\t\t\t\t\t\t数量\t\t\t\t\t\t\t\t\t成交金额(元)\t\t\t\t\t\t\t\t\t单位\t\t\t\t\t\t\t\t\t交货地点\t\t\t\t\t\t\t\t\t交货日期\t\t\t\t\t\t\t\t\t售后要求\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA090101-复印纸\t\t\t\t\t\t\t\t\t\tA4纸\t\t\t\t\t\t\t\t\t\t金铭洋复印纸70克A4\t\t\t\t\t\t\t\t\t\t70gA4/70gA4/210*297mm,500张/包\t\t\t\t\t\t\t\t\t\t480\t\t\t\t\t\t\t\t\t\t      12,000.00\t\t\t\t\t\t\t\t\t\t包\t\t\t\t\t\t\t\t\t\t常德市鼎城区人民法院（武陵镇临沅路418号）\t\t\t\t\t\t\t\t\t\t2018-11-22\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t三、投诉与质疑\t\t\t\t5个工作日之内，若有异议，向采购人质疑。 \t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t采购人：鼎城区人民法院\t\t\t\t  \t\t\t地址： \t\t\t\t  \t\t\t联系人：采购用户电话：07367373188'
    content = '冷水江市人民检察院办公用品采购采购项目的协议供货成交公告\t\t\t\t\t\t\t\t公告时间：2018年11月20日\t\t\t\t\t\t\t\t        冷水江市人民检察院对办公用品采购采购项目进行协议采购，结果如下：\t\t\t\t一、采购编号：\t\t\t\t湘财采计[2018]011839号\t\t\t\t\t\t\t\t二、成交结果：\t\t\t\t\t\t\t\t\t \t\t\t\t\t成交供应商：冷水江市五星数码科技有限公司\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t品目类别\t\t\t\t\t\t\t\t\t品目分类\t\t\t\t\t\t\t\t\t品目名称\t\t\t\t\t\t\t\t\t商品名称\t\t\t\t\t\t\t\t\t规格型号/技术指标\t\t\t\t\t\t\t\t\t数量\t\t\t\t\t\t\t\t\t成交金额(元)\t\t\t\t\t\t\t\t\t单位\t\t\t\t\t\t\t\t\t交货地点\t\t\t\t\t\t\t\t\t交货日期\t\t\t\t\t\t\t\t\t售后要求\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA0201060104-针式打印机\t\t\t\t\t\t\t\t\t\t针式打印机\t\t\t\t\t\t\t\t\t\t标拓证卡打印机\t\t\t\t\t\t\t\t\t\tBP-900K/证卡打印机，24针，打印宽度：94列，打印厚度：4mm，拷贝能力：1+6副本，色带架寿命：1000万字符，平均无故障时间：大于等于12000小时\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t       2,880.00\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA0201060102-激光打印机\t\t\t\t\t\t\t\t\t\t激光打印机\t\t\t\t\t\t\t\t\t\t联想激光打印机\t\t\t\t\t\t\t\t\t\tCS1811/联想激光打印机\tCS1811\t黑白每分钟18页+彩色每分钟4页打印速度，高效便捷获取彩色输出；600dpi物理分辨率，清晰打印各种内容体积小巧，放置桌面无负担？\t\t\t\t\t\t\t\t\t\t3\t\t\t\t\t\t\t\t\t\t       5,199.99\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA090201-鼓粉盒\t\t\t\t\t\t\t\t\t\t鼓粉盒\t\t\t\t\t\t\t\t\t\t原装粉盒\t\t\t\t\t\t\t\t\t\tTN223（C）青色碳粉/适用柯尼卡美能达C226/256/266彩色数码复合机；\t\t\t\t\t\t\t\t\t\t2\t\t\t\t\t\t\t\t\t\t         860.00\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA090202-粉盒\t\t\t\t\t\t\t\t\t\t粉盒\t\t\t\t\t\t\t\t\t\t原装粉盒\t\t\t\t\t\t\t\t\t\tTN324（K）黑色碳粉/适用于柯尼卡美能达C308/368系列彩机，印量28000页（A4幅面，5%覆盖率）\t\t\t\t\t\t\t\t\t\t2\t\t\t\t\t\t\t\t\t\t       1,560.00\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t成交供应商：冷水江市五星数码科技有限公司\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t品目类别\t\t\t\t\t\t\t\t\t品目分类\t\t\t\t\t\t\t\t\t品目名称\t\t\t\t\t\t\t\t\t商品名称\t\t\t\t\t\t\t\t\t规格型号/技术指标\t\t\t\t\t\t\t\t\t数量\t\t\t\t\t\t\t\t\t成交金额(元)\t\t\t\t\t\t\t\t\t单位\t\t\t\t\t\t\t\t\t交货地点\t\t\t\t\t\t\t\t\t交货日期\t\t\t\t\t\t\t\t\t售后要求\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA02010104-台式计算机\t\t\t\t\t\t\t\t\t\t台式计算机\t\t\t\t\t\t\t\t\t\t联想THINKCENTRE\t\t\t\t\t\t\t\t\t\tThinkCentre M820z-D027/型号：ThinkCentre M820z-D027机型：21.5英寸WVA(LED背光) 一体机主板：21.5\"\" B360 150W 90% NT PRCCPU:  Intel Core i5-8500 3G 6C内存：4GB DDR4 2666 SoDIMM硬盘：500GB HD 7200RPM 2.5\"\" SATA3显卡：集成显卡系统：出厂预装正版Windows 10 Home 64，微软正版可查其他：小仰角（-5-45度）多功能底座For21.5，键盘鼠标，2W*2杜比音箱服务: 联想IT资产环保处置服务基础版保修：原厂ThinkCentre M AIO尊享服务_3年，提供原厂针对项目的售后服务承诺函原件（加盖原厂公章）\"\t\t\t\t\t\t\t\t\t\t2\t\t\t\t\t\t\t\t\t\t       9,680.00\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t货物\t\t\t\t\t\t\t\t\t\tA0201060401-液晶显示器\t\t\t\t\t\t\t\t\t\t液晶显示器\t\t\t\t\t\t\t\t\t\t联想液晶显示器\t\t\t\t\t\t\t\t\t\t商用21.5W LED宽屏液晶显示器(T2224r)/型号：商用21.5W LED宽屏液晶显示器(T2224r)参数：VGA+DVI接口；3年保修服务；二级能效；支持背挂小Q，只需壁挂套件；3年保修服务\t\t\t\t\t\t\t\t\t\t1\t\t\t\t\t\t\t\t\t\t       1,080.00\t\t\t\t\t\t\t\t\t\t批\t\t\t\t\t\t\t\t\t\t冷水江市人民检察院\t\t\t\t\t\t\t\t\t\t2018-05-01\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t三、投诉与质疑\t\t\t\t5个工作日之内，若有异议，向采购人质疑。 \t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t采购人：冷水江市人民检察院\t\t\t\t  \t\t\t地址： \t\t\t\t  \t\t\t联系人：张建电话：07385318515'
    content = '湖南省农村经营管理服务站示范家庭农场牌匾印制采购项目的定点服务成交公告\t\t\t\t\t\t\t\t公告时间：2018年11月20日\t\t\t\t\t\t\t\t\t\t\t\t        湖南省农村经营管理服务站对示范家庭农场牌匾印制采购项目进行定点采购，结果如下：\t\t\t\t一、采购编号：\t\t\t\t湘财采计[2018]013160号\t\t\t\t\t\t\t\t二、成交结果：\t\t\t\t\t\t\t\t\t \t\t\t\t\t成交供应商：长沙长大成彩印有限公司\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t品目类别\t\t\t\t\t\t\t\t\t品目分类\t\t\t\t\t\t\t\t\t品目名称\t\t\t\t\t\t\t\t\t数量\t\t\t\t\t\t\t\t\t单位\t\t\t\t\t\t\t\t\t成交金额(元)\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t服务\t\t\t\t\t\t\t\t\t\tC08140101-单证印刷服务\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t300\t\t\t\t\t\t\t\t\t\t本\t\t\t\t\t\t\t\t\t\t      79,800.00\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t三、投诉质疑：\t\t\t\t5个工作日之内，若有异议，向采购人质疑。\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t采购人：湖南省农村经营管理服务站\t\t\t\t  \t\t\t地址： \t\t\t\t  \t\t\t联系人：陈俊波电话：88621707\t\t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t  \t\t  \t\t  \t\t\t\t\t  本公告期限为1个工作日'
    content = "湖南轻工高级技工学校  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t新校区监控、广播系统设备采购及安装  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t公开招标中标公告  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t  \t\t\t公告日期：2018年11月20日  \t\t\t  \t\t\t  \t\t\t\t        \t\t\t\t\t  \t\t\t\t\t\t受湖南轻工高级技工学校的委托，湖南中投项目管理有限公司代理机构对  \t\t\t\t\t  \t\t\t\t\t新校区监控、广播系统设备采购及安装项目采购项目进行公开招标，经评标委员会评审，采购人确认，现将中标信息公告如下：  \t\t\t\t  \t\t\t  \t\t\t   \t\t\t一、采购项目信息  \t\t\t项目名称：新校区监控、广播系统设备采购及安装项目  \t\t\t政府采购计划编号：湘财采计[2018]011589号  \t\t\t采购项目编号：297520181030209  \t\t\t采购方式：公开招标  \t\t\t采购项目内容与数量：  \t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t包号品目分类品目名称单位数量  \t\t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t1  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\tA02091107-视频监控设备  \t\t\t\t\t\t\t\t新校区监控、广播系统设备采购及安装项目  \t\t\t\t\t\t\t\t批  \t\t\t\t\t\t\t\t1  \t\t\t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t   \t\t\t  \t\t\t   \t\t\t二、开标定标日期  \t\t\t1、招标公告日期：2018年10月30日  \t\t\t2、投标截止日期：2018年11月20日  \t\t\t3、开标日期：2018年11月20日  \t\t\t4、评审小组名单：陈明义、阳西述、杨为民、黄芳杰、吕国斌。  \t\t\t5、监标人：唐金跃、夏占青  \t\t\t   \t\t\t三、供应商投标情况  \t\t\t  \t\t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t包1：  \t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t供应商信息 \t\t\t\t\t\t\t\t\t\t资格审查结果 \t\t\t\t\t\t\t\t\t\t符合性审查结果 \t\t\t\t\t\t\t\t\t\t报价 \t\t\t\t\t\t\t\t\t\t评标价 \t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t评分 \t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t推荐排名 \t\t\t\t\t\t\t\t\t\t是否成交候选人 \t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t湖南力唯中天科技发展有限公司\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t   1,798,196.00\t \t\t\t\t\t\t\t\t\t\t   1,798,196.00\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t97.45\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t1\t \t\t\t\t\t\t\t\t\t\t是 \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t北京亿海兰特科技发展有限公司\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t   1,828,000.00\t \t\t\t\t\t\t\t\t\t\t   1,828,000.00\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t63.51\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t2\t \t\t\t\t\t\t\t\t\t\t是 \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t湖南继善高科技有限公司\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t审核通过\t \t\t\t\t\t\t\t\t\t\t   1,817,175.00\t \t\t\t\t\t\t\t\t\t\t   1,817,175.00\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t55.94\t \t\t\t\t\t\t\t\t\t\t\t \t\t\t\t\t\t\t\t\t\t3\t \t\t\t\t\t\t\t\t\t\t是 \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t   \t\t\t  \t\t\t四、中标供应商供货明细  \t\t\t  \t\t\t\t  \t\t\t\t  \t\t\t\t\t包号供货明细  \t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t\t\t1  \t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t中标供应商湖南力唯中天科技发展有限公司  \t\t\t\t\t\t\t\t\t联系方式  \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t联系人：阳杰波  \t\t\t\t\t\t\t\t\t\t电话：17373151635  \t\t\t\t\t\t\t\t\t\t地址：湖南省长沙市岳麓区先导路179号湘江时代商务广场A2栋6层  \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t货物名称品牌数量单价参数物品代码生产厂商服务要求报价  \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\t视频监控设备  \t\t\t\t\t\t\t\t\t\t\t   \t\t\t\t\t\t\t\t\t\t\t1  \t\t\t\t\t\t\t\t\t\t\t1798196  \t\t\t\t\t\t\t\t\t\t\t详见招标文件  \t\t\t\t\t\t\t\t\t\t\t   \t\t\t\t\t\t\t\t\t\t\t/  \t\t\t\t\t\t\t\t\t\t\t   \t\t\t\t\t\t\t\t\t\t\t   1,798,196.00  \t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t  \t\t\t\t\t  \t\t\t\t\t   \t\t\t\t  \t\t\t\t  \t\t\t\t\t 代理服务费收取方式：中标（成交）供应商支付代理服务费   \t\t\t\t  \t\t\t\t  \t\t\t\t\t   收费标准：以中标通知书中确定的中标总金额按计价格[2002]1980号文件之规定的向中标单位收取。  \t\t\t\t  \t\t\t\t  \t\t\t\t\t   代理服务费总金额：24000元  \t\t\t\t  \t\t\t\t   \t\t\t  \t\t\t\t\t五、评审小组成员名单\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t评审小组职务\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t姓名\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t产生方式\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t参与过程\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t备注\t\t  \t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t 评委\t\t  \t\t\t\t\t 陈明义\t\t  \t\t\t\t\t随机抽取\t\t  \t\t\t\t\t全过程\t\t  \t\t\t\t\t \t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t 评委\t\t  \t\t\t\t\t 阳西述\t\t  \t\t\t\t\t随机抽取\t\t  \t\t\t\t\t全过程\t\t  \t\t\t\t\t \t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t 评委\t\t  \t\t\t\t\t 杨为民\t\t  \t\t\t\t\t随机抽取\t\t  \t\t\t\t\t全过程\t\t  \t\t\t\t\t \t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t 主任评委\t\t  \t\t\t\t\t 黄芳杰\t\t  \t\t\t\t\t随机抽取\t\t  \t\t\t\t\t全过程\t\t  \t\t\t\t\t \t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  \t\t\t\t\t 评委\t\t  \t\t\t\t\t 吕国斌\t\t  \t\t\t\t\t随机抽取\t\t  \t\t\t\t\t全过程\t\t  \t\t\t\t\t \t\t  \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t注：产生方式注明是随机抽取或自行选定；参与过程注明是确定供应商、谈判或全过程。\t\t\t\t\t\t\t\t\t\t\t \t  \t\t\t六、质疑  \t\t\t投标供应商如对此公告有异议的，请于此公告发布之日起七个工作日内，以书面形式向采购人、代理机构提出质疑。  \t\t\t   \t\t\t  \t\t\t\t  \t\t\t\t\t  \t\t\t\t\t\t采购人：湖南轻工高级技工学校\t\t\t  \t\t\t地址：湖南省醴陵市醴陵大道\t\t\t  \t\t\t联系人：李老师电话：073123237186\t\t\t  \t\t\t\t\t\t  \t\t\t\t代理机构：湖南中投项目管理有限公司\t\t\t  \t\t\t\t地址：长沙市雨花区万家丽中路一段469号华雅财富大厦9楼906室\t  \t\t\t\t\t\t联系人：罗芳邮编：410000\t  \t\t\t\t\t\t电话：18008431216传真：0731-89767828\t\t\t  \t\t\t  \t\t\t\t\t  \t\t\t\t  \t\t\t  \t\t\t  \t\t  \t\t  \t\t\t\t\t  本公告期限为1个工作日"
    # content = "标段信息 标段编号 标段名称 采购方式 预算金额(元)投标供应商名称1 “大服务综合受理平台”应用软件采购 竞争性谈判279000 湖南科创信息技术股份有限公司,湖南智远数通科技股份有限公司,湖南天大天财科技股份有限公司 长沙市公安局“大服务综合受理平台”应用软件采购结果公告长沙市公安局的“大服务综合受理平台”应用软件采购竞争性谈判采购项目于结束 ，现将成交结果公告如下。一、项目名称　　 采购项目名称： 长沙市公安局“大服务综合受理平台”应用软件采购 　　预算金额(元)： 279000 二、项目编号　　政府采购编号： CSCG-201711080001　　委托代理编号：HNXZ-2017-GD-XMZB-1362三、邀请供应商的情况、谈判情况、成交供应商名称、地址和成交金额(一)、邀请供应商的情况　1、供应商产生方式：供应商库抽取 　2、采取采购人、评审专家推荐方式的推荐意见采购人推荐意见评审专家推荐意见供应商名称/供应商名称/推荐意见/推荐意见/（二）、谈判情况   序号供应商名称最终报价评审结果1 湖南科创信息技术股份有限公司272000.00第一成交候选人2 湖南智远数通科技股份有限公司275000.00第二成交候选人3 湖南天大天财科技股份有限公司276000.00第三成交候选人（三）、成交供应商名称、地址和成交金额标段1 中标，标段名称： “大服务综合受理平台”应用软件采购　成交供应商名称：湖南科创信息技术股份有限公司　地址：长沙市岳麓区（高新区）青山路678号科创软件园　成交金额(元)：272000备注： /四、谈判小组成员名单   序号评审小组职务姓名产生方式参与过程备注1 主任评委陈晖随机抽取全过程/2 评委成员曾瑶辉随机抽取全过程/3 评委成员陈建中随机抽取全过程/注：产生方式注明是随机抽取或自行选定；参与过程注明是确定供应商、谈判或全过程。五、公告期限：年 月 日 时至 年 月 日 时止（1个工作日）。六、参与采购活动的供应商认为成交结果使自己权益受到损害的，可以在知道或者应知其权益受到损害之日起7个工作日内以书面形式向采购人或采购代理机构提出质疑。七、采购人和采购代理机构名称、联系人和联系方式：采购人名称：长沙市公安局采购代理机构名称：湖南省湘咨工程咨询有限责任公司电话：18900768925电话：0731-85892066地址：解放西路140号地址：长沙市东二环一段1139号湖南国际商务中心五楼联系人：王警官 联系人：戴先生附件：1、竞争性谈判文件2、成交供应商的最后报价一览表及报价文件。相关公告[长沙市公安局“大服务综合受理平台”应用软件采购竞争性谈判邀请公告]附件下载1、“大服务综合受理平台”应用软件采购竞争性谈判文件.pdf2、成交供应商最后报价一览表.pdf\r\n[打印本页]　\r\n[关闭本页]"
    # content = "标段信息 标段编号 标段名称 采购方式 预算金额(元)投标供应商名称1 更换机房部分老旧精密空调 竞争性谈判878800 湖南和成暖通设备科技有限公司,长沙钧华机电设备有限公司,湖南睿垒贸易有限公司 长沙市公安局交通警察支队科信大队申报更换机房部分老旧精密空调采购项目结果公告长沙市公安局交通警察支队的科信大队申报更换机房部分老旧精密空调采购项目竞争性谈判采购项目于结束 ，现将成交结果公告如下。一、项目名称　　 采购项目名称： 长沙市公安局交通警察支队科信大队申报更换机房部分老旧精密空调采购项目 　　预算金额(元)： 878800 二、项目编号　　政府采购编号： CSCG-201810090017　　委托代理编号：DCCG-201810001三、邀请供应商的情况、谈判情况、成交供应商名称、地址和成交金额(一)、邀请供应商的情况　1、供应商产生方式：公告邀请　2、采取采购人、评审专家推荐方式的推荐意见采购人推荐意见评审专家推荐意见供应商名称/供应商名称/推荐意见/推荐意见/（二）、谈判情况   序号供应商名称最终报价评审结果1 湖南和成暖通设备科技有限公司770000.00元第一名2 长沙钧华机电设备有限公司790000.00元第二名3 湖南睿垒贸易有限公司800000.00元第三名（三）、成交供应商名称、地址和成交金额标段1 中标，标段名称： 更换机房部分老旧精密空调　成交供应商名称：湖南和成暖通设备科技有限公司　地址：长沙市雨花区　成交金额(元)：770000备注： /四、谈判小组成员名单   序号评审小组职务姓名产生方式参与过程备注1 主任评委黄胜全随机抽取全过程/2 成员许小云随机抽取全过程3 业主评委邓袁钦自行选定全过程注：产生方式注明是随机抽取或自行选定；参与过程注明是确定供应商、谈判或全过程。五、公告期限：年 月 日 时至 年 月 日 时止（1个工作日）。六、参与采购活动的供应商认为成交结果使自己权益受到损害的，可以在知道或者应知其权益受到损害之日起7个工作日内以书面形式向采购人或采购代理机构提出质疑。七、采购人和采购代理机构名称、联系人和联系方式：采购人名称：长沙市公安局交通警察支队采购代理机构名称：湖南德成项目管理有限公司电话：0731-88878807，88878130电话：0731-89905369地址：长沙市岳麓区枫林路1号地址：长沙市岳麓区桐梓坡西路138号长房时代国际1603室联系人：邹警官、彭警官联系人：龙青、张梦兰、禹艳春、夏舒婷附件：1、竞争性谈判文件2、成交供应商的最后报价一览表及报价文件。相关公告[长沙市公安局交通警察支队科信大队申报更换机房部分老旧精密空调采购项目竞争性谈判邀请公告]附件下载1、成交供应商的最后报价一览表及报价文件.pdf2、长沙市公安局交通警察支队科信大队申报更换机房部分老旧精密空调采购项目 终稿.doc\r\n[打印本页]　\r\n[关闭本页]"
    # content = "标段信息 标段编号 标段名称 采购方式 预算金额(元)投标供应商名称1 不动产登记系统二期软件开发采购 公开招标8230000 广东南方数码科技股份有限公司,, 长沙市不动产登记中心不动产登记系统二期软件开发采购结果公告湖南合晟项目管理有限公司 受长沙市不动产登记中心的委托，对不动产登记系统二期软件开发采购项目进行公开招标招标，现将采购结果公告如下。一、采购项目情况　　 采购项目名称： 不动产登记系统二期软件开发采购 　　政府采购编号： CSCG-201811010032　　委托代理编号：HNHS-2018ZF033　　招标公告日期：　　投标截止日期：　　开标日期： 　　评标方法： 综合评分法 二、项目标段结果信息标段号品目分类品目名称单位数量状态1 C02010302-行业应用软件开发服务 行业应用软件开发服务 项 1 中标 三、供应商投标情况(供应商名称、报价、评分、资格性审查结果 符合性审查结果 排名 是否成交候选人) 序号供应商名称中标（入围）金额评分资格性符合性审查表备注1广东南方数码科技股份有限公司  8192150.00元 96.78 分符合第一中标候选人2 广州奥格智能科技有限公司8173500.00元 51.4分符合第二中标候选人3武大吉奥信息技术有限公司 8207900.00元 41.16分符合第三中标候选人四、中标人供货明细标段中标候选人名称中标候选人地址中标金额状态供货明细一广东南方数码科技股份有限公司   长沙市雨花区人民东路46号铭诚国际518室 8,192,150.00元中标详见附件五、流废标情况说明：无六、评标委员会成员名单：王唤良（主任评委） 杨练 罗小珠 唐江桦 何康华（业主评委）七、其他情况说明：无八、公告期限：年 月 日 时至 年 月 日 时止（1个工作日）。九、投标人认为中标结果使自己权益受到损害的，可以在知道或者应知其权益受到损害之日起7个工作日内以书面形式向采购人或采购代理机构提出质疑。十、采购项目联系人姓名和电话：采购人名称：长沙市不动产登记中心采购代理机构名称：湖南合晟项目管理有限公司电话：0731-84529095电话：0731-88611642地址：芙蓉区晚报大道150号地址：湖南省长沙市岳麓区银盆岭街道岳麓大道2号滨江金座1栋601室联系人：李恩华联系人：付小兰附件：投标人开标一览表和分项报价表。相关公告[长沙市不动产登记中心不动产登记系统二期软件开发采购公开招标公告]附件下载1、开标一览表及分项价格表2.doc\r\n[打印本页]　\r\n[关闭本页]"
    content = "标段信息 标段编号 标段名称 采购方式 预算金额(元)投标供应商名称1 桥梁检测 公开招标1471678.39 湖南中大建设工程检测技术有限公司,湖南联智桥隧技术有限公司,长沙理工大公路工程试验检测中心 长沙市路桥征费维护管理处2018年城区部分桥梁检测项目结果公告湖南道勤项目管理有限公司 受长沙市路桥征费维护管理处的委托，对2018年城区部分桥梁检测项目项目进行公开招标招标，现将采购结果公告如下。一、采购项目情况　　 采购项目名称： 2018年城区部分桥梁检测项目 　　政府采购编号： CSCG-201808300020　　委托代理编号：HNDQZFCG-2018050　　招标公告日期：　　投标截止日期：　　开标日期： 　　评标方法： 综合评分法 二、项目标段结果信息标段号品目分类品目名称单位数量状态1 C1099-其他工程咨询管理服务 其他工程咨询管理服务 项目 1 中标 三、供应商投标情况(供应商名称、报价、评分、资格性审查结果 符合性审查结果 排名 是否成交候选人) 供应商名称中标（入围）金额（元）评分资格性审查结果符合性审查结果排名是否中标候选人湖南中大建设工程检测技术有限公司1354755.8483.00合格合格1是湖南联智桥隧技术有限公司1411037.5354.65合格合格2是长沙理工大公路工程试验检测中心1124149.0350合格合格3是四、中标人供货明细标段中标候选人名称中标候选人地址中标金额状态报价明细一湖南中大建设工程检测技术有限公司湖南省长沙市岳麓区学士街道学士路755号1354755.8中标详见开标一览表及分项价格表五、流废标情况说明：无六、评标委员会成员名单：娄平（主任评委）、罗立武、陈益军、卜乐奇、罗建章。七、其他情况说明：无八、公告期限：年 月 日 时至 年 月 日 时止（1个工作日）。九、投标人认为中标结果使自己权益受到损害的，可以在知道或者应知其权益受到损害之日起7个工作日内以书面形式向采购人或采购代理机构提出质疑。十、采购项目联系人姓名和电话：采购人名称：长沙市路桥征费维护管理处采购代理机构名称：湖南道勤项目管理有限公司电话：88807341电话：0731-84486998地址：银杉路382号地址：长沙市开福区芙蓉中路一段新时代广场北栋501联系人：敖学谦联系人：范薇附件：投标人开标一览表和分项报价表。相关公告[长沙市路桥征费维护管理处2018年城区部分桥梁检测项目公开招标公告]附件下载1、中标单位开标一览表、分项报价表.pdf"
    # content = "湖南省公路管理局本级  					  				  			  			  				  					  						  						2018年全省自然村通水泥(沥青)路建设检测  					  				  			  			  				  					  						公开招标中标公告  					  				  			  			  			公告日期：2018年11月21日  			  			  				        					  						受湖南省公路管理局本级的委托，湖南中弘招标咨询有限公司代理机构对  					  					2018年全省自然村通水泥(沥青)路建设检测采购项目进行公开招标，经评标委员会评审，采购人确认，现将中标信息公告如下：  				  			  			   			一、采购项目信息  			项目名称：2018年全省自然村通水泥(沥青)路建设检测  			政府采购计划编号：湘财采计[2018]011131号  			采购项目编号：292620181024458  			采购方式：公开招标  			采购项目内容与数量：  			  				  					  						包号品目分类品目名称单位数量  						  							  								  									1  								  								C0908-其他专业技术服务  								技术检测服务  								项  								1  							  						  					  				  			  			   			  			   			二、开标定标日期  			1、招标公告日期：2018年10月30日  			2、投标截止日期：2018年11月20日  			3、开标日期：2018年11月20日  			4、评审小组名单：娄斌武、郭云开、邓均初、陈栋梁、朱银花。  			5、监标人：谢忠杰、黄良龙  			   			三、供应商投标情况  			  				  				  					  							  						包1：  						  															 									 										供应商信息 										资格审查结果 										符合性审查结果 										报价 										评标价 										 											评分 										 										推荐排名 										是否成交候选人 									 																																				 										湖南交院试验检测有限责任公司	 										审核通过	 										审核通过	 										   2,494,775.00	 										   2,494,775.00	 											 										82.94	 											 										1	 										是 																																															 										长沙中核工程检测技术有限公司	 										审核通过	 										审核通过	 										   2,497,512.00	 										   2,497,512.00	 											 										74.93	 											 										2	 										是 																																															 										湖南致力工程科技有限公司	 										审核通过	 										审核通过	 										   2,478,353.00	 										   2,404,002.41	 											 										57.2	 											 										3	 										是 																																			  							  														  					  					  				  			  			   			  			四、中标供应商供货明细  			  				  				  					包号供货明细  					  						  							1  							  								  									中标供应商湖南交院试验检测有限责任公司  									联系方式  									  										联系人：蒋芳超  										电话：13618463864  										地址：长沙市雨花区香樟路110号湖南交通职业技术学院教学楼1楼  									  									货物名称品牌数量单价参数物品代码生产厂商服务要求报价  									  										  											其他专业技术服务  											   											1  											2494775  											   											   											湖南交院试验检测有限责任公司  											   											   2,494,775.00  										  									  								  							  						  					  					   				  				  					 代理服务费收取方式：中标（成交）供应商支付代理服务费   				  				  					   收费标准：采购金额的1%  				  				  					   代理服务费总金额：25000元  				  				   			  					五、评审小组成员名单													  							  								  						评审小组职务		  								  								  						姓名		  								  								  						产生方式		  								  								  						参与过程		  								  								  						备注		  								  							  																								  					 评委		  					 娄斌武		  					随机抽取		  					全过程		  					 		  																																						  					 评委		  					 郭云开		  					随机抽取		  					全过程		  					 		  																																						  					 评委		  					 邓均初		  					随机抽取		  					全过程		  					 		  																																						  					 评委		  					 陈栋梁		  					随机抽取		  					全过程		  					 		  																																						  					 主任评委		  					 朱银花		  					随机抽取		  					全过程		  					 		  																																														注：产生方式注明是随机抽取或自行选定；参与过程注明是确定供应商、谈判或全过程。											 	  			六、质疑  			投标供应商如对此公告有异议的，请于此公告发布之日起七个工作日内，以书面形式向采购人、代理机构提出质疑。  			   			  				  					  						采购人：湖南省公路管理局本级			  			地址：长沙市八一路520号			  			联系人：谢忠杰、黄良龙电话：0731-84412576			  						  				代理机构：湖南中弘招标咨询有限公司			  				地址：湖南省长沙市岳麓区洋湖街道潇湘南路一段208号柏利大厦写字楼南栋12层12012号	  						联系人：蒋依林邮编：410000	  						电话：0731-85058982传真：0731-85058982			  			  					  				  			  			  		  		  					  本公告期限为1个工作日"
    content = "竞争性谈判成交公告  			  		  		  		  		公告日期：2018年11月21日  		  		  					                  湖南农业大学  的  教职工住宅区防水维修工程  竞争性谈判采购项目于   2018年11月20日  结束，现将成交结果公告如下：			一、项目名称采购项目名称：   湖南农业大学教职工住宅区防水维修工程项目           预算金额：   950,000.00   元       			二、编号：			        1、政府采购计划编号：  湘财采计[2018]012118号                          			        2、采购代理编号 ：  100072921     			三、邀请供应商的情况			        1、供应商产生方式：（）公告邀请   （ ）供应商库抽取  （√ ）采购人、专家推荐			        2、采取采购人、评审专家推荐方式的推荐意见 					 						       包1：       											  					  						  						供应商名称  						  						  						采购人推荐意见  						  						  						评审专家推荐意见  						  					  					  					  					 湖南国楚工程有限公司   					    					 符合谈判要求   					  					  					  					 湖南东方雨虹防腐保温防水工程有限公司   					    					 符合谈判要求   					  					  					  					 湖南同远新材料科技有限公司   					 符合谈判要求   					    					  					  												 					  				四、谈判情况			       包1：								  					  						  						供应商名称  						  						  						最终报价  						  						  						评审结果  						  					  					  					  					 湖南国楚工程有限公司  					      703,900.00  					 中标供应商  					  					  					  					 湖南东方雨虹防腐保温防水工程有限公司  					      725,600.00  					 有效投标人  					  					  					  					 湖南同远新材料科技有限公司  					      780,000.00  					 有效投标人  					  					  									 						五、成交供应商名称、地址和成交金额		       包1：								 	       成交供应商名称： 湖南国楚工程有限公司					       联  系  人：刘欣良               电                       话：07308683662					       地                       址：湖南省岳阳市岳阳楼区天伦金三角银座A栋518        					       成交金额：703900  元。				           报价明细：              供应商报价：703900 元							  					  						  						采购品目  						  						  						品牌  						  						  						数量  						  						  						单价  						  						  						参数说明  						  						  						  						生产厂家  						  					  						  						商品名称  						  						  						服务要求  						  						  						报价  						  					  					  					  					B0504-防水工程  					  					  					  					  					  					  					  					  					  					   					 1  					 703900  					   					  					 湖南国楚工程有限公司  					  					 住宅区防水维修工程项目  					   					 703,900.00  					  					  								  					 代理服务费收取方式：   				  				  					   收费标准：  				  				  					   代理服务费总金额：元  									 								六、谈判小组成员名单  					  						  						评审小组职务  						  						  						姓名  						  						  						产生方式  						  						  						参与过程  						  						  						备注  						  					  											  					 成员  					 黄胆剑  					 随机抽取  					 全过程  					   																					  					 组长  					 李惠  					 随机抽取  					 全过程  					   																					  					 用户代表  					 李中秋  					 自行选定  					 全过程  					   																					       注：产生方式注明是随机抽取或自行选定；参与过程注明是确定供应商、谈判或全过程。												七、采购人和采购代理机构名称、联系人和联系方式       1、采购人名称： 湖南农业大学                                                               地址：长沙市芙蓉区农大路1号                                                                    联系人：马老师                                 联系电话： 0731-84618118                             2、代理机构名称：                                                              地址：                                                                        联系人：                                 联系电话：                       八、本公告自发布之起7个工作日内，参与采购活动的供应商认为采购过程和成交结果使自己权益受到损害的，可以以书面形式向采购人、代理机构提出质疑。   			  本公告期限为1个工作日"
    money_list, budget_money_list = obj.do_parser(content, parser_select='ccgp-hunan')
    print(money_list)

    for money in money_list:
        print("money:", money[0], money[1], type(money))

    for money in budget_money_list:
        print("budget:", money)
