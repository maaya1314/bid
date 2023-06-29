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

sys.path.append('..')
sys.path.append('../../..')
sys.path.append('../../../..')
from bid_tools.loghandler import getLogger
# from bid_conf.conf_2 import parse_dict
# from bid_2 import Bid
from bid_3 import Bid3
from bid_conf.conf_3 import parse_dict

urllib3.disable_warnings()


class BidGT(Bid3):

    def __init__(self, debug=True):
        Bid3.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '中国一汽电子招标采购交易平台-变更公告'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://etp.faw.cn/gg/bgggList?zbLeiXing=1&xmLeiXing=&ggStartTimeEnd=&gongGaoType=6&isNew=1'
        self.js_str = """
        
        var keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv" + "wxyz0123456789+/" + "=";
        function setSecrect(cname,cvalue) {
                var encodeSixF1 = encodeSixF(cvalue);
                return encodeSixF1;
                secrect_cookie = cname + "=" + encodeSixF1 + ";path=/";
                return secrect_cookie;
            }
        function encodeSixF(input) {
            var output = "";
            var chr1, chr2, chr3 = "";
            var enc1, enc2, enc3, enc4 = "";
            var i = 0;
            do {
                chr1 = input.charCodeAt(i++);
                chr2 = input.charCodeAt(i++);
                chr3 = input.charCodeAt(i++);
                enc1 = chr1 >> 2;
                enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
                enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
                enc4 = chr3 & 63;
                if (isNaN(chr2)) {
                    enc3 = enc4 = 64;
                } else if (isNaN(chr3)) {
                    enc4 = 64;
                }
                output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2) + keyStr.charAt(enc3) + keyStr.charAt(enc4);
                chr1 = chr2 = chr3 = "";
                enc1 = enc2 = enc3 = enc4 = "";
            } while (i < input.length);

            if(output!=null && output.indexOf("=")!=-1){
                var reg=new RegExp('=',"g");
                var outputNew=output.replace(reg,"r1e2p3l4");
                output=outputNew;
            }

            return output+"+*+";
        }
    function allData(detailUrl,ggGuid,xxSource,gongGaoType) {
        var url = "https://etp.faw.cn:443/"+detailUrl;
        return setSecrect("secrectID",url);
        }

    function guoJiJiDian(ggGuid,ggLeiXing) {
        var url = "https://etp.faw.cn:443/gg/toXinXiDetail1";
        return setSecrect("secrectID",url);
        }

    function feiZhao(ggGuid,xxSource,gongGaoType) {
        var url = "https://etp.faw.cn:443/gg/toXinXiDetail1";
        return setSecrect("secrectID",url);
        }

    function zhaoBiao(methodType,ggGuid) {
        var url ="";
        if(methodType==1){
            url = "https://etp.faw.cn:443/gg/ggDetail";
        }else if(methodType==2){
            url = "https://etp.faw.cn:443/gg/bgggDetail";
        }
        return setSecrect("secrectID",url);
        }

    function yiChang(zbYiChangGuid) {
        var url = "https://etp.faw.cn:443/gg/zbycDetail";
        return setSecrect("secrectID",url);
        }
    function zbHouXuanRen(methodType,ggGuid){
        var url ="";
        if(methodType==1){
            url = "https://etp.faw.cn:443/gg/zbycDetail";
        }else if(methodType==2){
            url = "https://etp.faw.cn:443/gg/zbhxrDetail";
        }
        return setSecrect("secrectID",url);
        }

    function zbjgDetail(ggGuid,xinXiLaiYuanValue) {
        var url = "https://etp.faw.cn:443/gg/zbjgDetail";
        return setSecrect("secrectID",url);
                }
        """
        self.host = urlparse(url).netloc
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Pragma': 'no-cache',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        page = 1
        payload = {
            'ggName': self.keyword,
            'currentPage': page,
        }
        content = self.req(url, req_type="post", data=payload, headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{page} no content")
            return
        html = etree.HTML(content)

        pages = html.xpath("string(//li[@class='number'][last()])")
        if not pages: pages = 1
        self.log.info("all pages :{}, {}".format(pages, keyword))
        self.list_parse(content, url)
        pages = int(pages)
        if pages < 2:
            return
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            if page > self.max_pages:
                break
            self.log.info("now start page :{}, {}".format(page, keyword))
            payload = {
                'ggName': self.keyword,
                'currentPage': page,
            }
            content = self.req(url, req_type="post", data=payload, headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(page))
                continue
            self.list_parse(content, url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        # items = content.get("data")
        html = etree.HTML(content)
        items = html.xpath("//div[@class='zl-page-list']/div/div/div[@class='zl-col-6']")
        # url_list = re.findall("toGetContent\('(.*?)'\)", content)
        for item in items:
            if self.exit_flag:
                return
            # item_id = item.get("id")
            href_str = item.xpath("string(./div/@onclick)")
            href_type = re.findall("(.*?)\(", href_str)[0]
            href = re.findall("\((.*?),", href_str)[0]
            href_2 = re.findall(",'(.*?)'", href_str)[0]
            detail_url = 'https://etp.faw.cn/gg/bgggDetail?guid={}&statusCode={}&isNew=1'.format(href_2, href)
            # detail_url = 'https://etp.faw.cn/gg/bgggDetail?guid=60100311-d7fc-4aa9-afb6-820a317ddc74&statusCode=2&isNew=1'
            # detail_url = urljoin(url, '/staticPage/' + href)
            # detail_url = 'https://www.cdt-ec.com/notice/moreController/moreall?id={}'.format(item_id)
            ctx1 = execjs.compile(self.js_str)
            encrypt_str = ctx1.call(href_type, int(href), href_2)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'no-cache',
                'Pragma': 'no-cache',
                'Proxy-Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
                'cookie': "secrectID={}".format(encrypt_str),
            }
            try:
                detail_content = self.req(url=detail_url, headers=headers, verify=False)
            except Exception as e:
                self.log.exception(e)
                continue
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            data = {}
            # html = etree.HTML(detail_content)
            # content = html.xpath("string(//div[@id='main'])")
            data['project_title'] = item.xpath("string(.//div[@class='title'])").strip()
            data['publish_time'] = item.xpath("string(./div/div[3]/div[@class='zl-desc-item'])").replace("发布时间：", "").strip()
            data['project_number'] = item.xpath("string(.//div[@class='zl-desc-item clamp-1'])").replace("项目编号：", "").strip()
            data['tender_unit'] = item.xpath("string(./div/div[5]/div[@class='zl-desc-item'])")
            # data['bid_end_time'] = item.get("deadline")
            done_fields = ['tender_unit', 'project_number']
            self.detail_parse(detail_content, detail_url, data, done_fields=done_fields)

    


if __name__ == '__main__':
    params = {
        "proxy_flag": False,
        # "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            # ""
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
        ],
        # "time_sleep": (2, 5)
    }
    bid = BidGT(debug=False)
    bid.process_item(params)
