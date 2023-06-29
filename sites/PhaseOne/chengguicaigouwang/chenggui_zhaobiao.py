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
from tenacity import retry, stop_after_attempt, wait_fixed
sys.path.append('../../..')
sys.path.append('../../../..')
sys.path.append('../../../../..')

from bid_tools.loghandler import getLogger

from bid_conf.conf import parse_dict
from bid import Bid
urllib3.disable_warnings()


class BidCG(Bid):

    def __init__(self, debug=True):
        Bid.__init__(self, debug)
        self.log = getLogger(self.__class__.__name__, console_out=True, level="debug")
        self.user_agent_list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"]
        self.headers = {}
        self.keyword = ""
        self.exit_flag = False
        self.exit_counts = 0
        self.file_name = '城轨采购网-招标与采购'
        self.parse_dict = parse_dict.get(self.file_name)

    def run(self, keyword):
        TIMEOUT = 60
        self.keyword = keyword
        url = 'https://www.mtrmart.com/Purchase/Notice/SearchNewList?title={}&category=&noticeType=&noticeTypeStr=&NoSinglesource=&companyValue=&isInProgress=n&isOneYear=n&page={}&pageSize=30'
        self.host = urlparse(url).netloc
        self.headers = {
            'Host': self.host,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        }
        page = 1
        home_page_url = url.format(keyword, page)
        content = self.req(home_page_url, req_type="get", rsp_type="content",  headers=self.headers, timeout=TIMEOUT)
        if not content:
            self.log.error(f"{home_page_url} no content")
            return
        # parsing home page
        self.list_parse(content, home_page_url)
        html = etree.HTML(content)
        pages = html.xpath("string(//ul[@class='pagination']/li[last()-1]/a)")
        if not pages:
            return
        pages = int(pages)
        for page in range(2, pages + 1):
            if self.exit_flag:
                return
            self.log.info("now start page :{}, {}".format(page, keyword))
            list_url = url.format(keyword, page)
            content = self.req(list_url, req_type="get", rsp_type="content", anti_word="", headers=self.headers, timeout=TIMEOUT)
            if not content:
                self.log.error("{} no content".format(list_url))
                continue
            self.list_parse(content, list_url)
        self.log.info("{} 数据采集完毕！".format(self.file_name))

    def list_parse(self, content, url):
        html = etree.HTML(content)
        url_list = html.xpath("//li/h6/span[@class='titleSpan']/@onclick")
        # url_list = re.findall(',\'(.*?)\'\);" class="titleSpan"', content)
        for item in url_list:
            if self.exit_flag:
                return
            # detail_url = urljoin(url, item)
            # detail_url = item
            detail_type = re.findall("gotoPage\('(\d+)',", item)[0]
            href = re.findall(",'(.*?)'\);", item)[0]
            """
            if (type == "1" || type == "2")//比价公告
                window.open("/Purchase/Notice/NewDetail?Id=" + id);
            else if (type == "3") //在线询价
                window.open('https://work.mtrmart.com/Modules/SpareParts/SparePartsDispatch.ashx?ID=' + id + "&AddNew=0");
            else if (type == "4")//招标项目
                window.open("/Bids/BidsNotice/NewDetail?Id=" + id);
            else if (type == "5")//单一来源公示
                window.open("/SingleSourceNotice/Notice/NewDetail?Id=" + id);
            """
            if detail_type == "3":
                detail_url = 'https://work.mtrmart.com/Modules/SpareParts/SparePartsDispatch.ashx?ID=' + href + "&AddNew=0"
                continue
            elif detail_type == "4":
                detail_url = 'https://www.mtrmart.com/Bids/BidsNotice/NewDetail?Id={}'.format(href)
            elif detail_type == "5":
                detail_url = 'https://www.mtrmart.com/SingleSourceNotice/Notice/NewDetail?Id={}'.format(href)
            else:  # if detail_type in ("1", "2"):
                detail_url = 'https://www.mtrmart.com/Purchase/Notice/NewDetail?Id={}'.format(href)
            list_headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-encoding': 'gzip, deflate',
                'accept-language': 'zh-CN,zh;q=0.9',
                'cache-control': 'no-cache',
                'pragma': 'no-cache',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            }
            # guid = re.findall('guid=(.*?)(?=&|$)', detail_url)[0]
            # actual_url = 'https://common.dzzb.ciesco.com.cn/xunjia-zb/gonggaoxinxi/gongGao_view.html?guid={}&callBackUrl=https://dzzb.ciesco.com.cn/html/crossDomainForFeiZhaoBiao.html'.format(guid)
            # detail_url = 'https://www.mtrmart.com/SingleSourceNotice/Notice/NewDetail?Id=78cbce89-f45b-45ba-8c52-adbc81a2e2d8'
            detail_content = self.req(url=detail_url, req_type="get", anti_word="你访问的页面找不回来了", headers=list_headers, verify=False)
            if not detail_content:
                self.log.error("{} no detail_content".format(detail_url))
                continue
            self.detail_parse(detail_content, detail_url)
            time.sleep(random.randint(5, 10))

    def fix_data(self, data, detail_content):
        '"re": ["联系电话：[\s\S]*?>(.*?)<", ""],"re": ["联系人：([\s\S]*?)联系电话", ""],'
        html = etree.HTML(detail_content)
        project_leader = data.get("project_leader")
        if project_leader:
            try:
                new_pl = re.findall("联系人[:|：]([\s\S]*?)联系电话", project_leader)[0].replace("\r", "").replace("\n", "").strip()
            except:
                new_pl = project_leader
            data["project_leader"] = new_pl
        phone = data.get("phone")
        if phone:
            try:
                new_phone = re.findall("联系电话[:|：]([\s\S]*?)$", phone)[0].replace("\r", "").replace("\n", "").strip()
            except:
                new_phone = phone
            data['phone'] = new_phone
        attachment_url = data.get("attachment_url")
        if attachment_url and not attachment_url.startswith("'http'"):
            attachment_url = 'https://www.mtrmart.com{}'.format(attachment_url)
            data['attachment_url'] = attachment_url

        project_location = data.get("project_location")
        if project_location:
            try:
                new_location = re.findall("联系地址[：|:]([\s\S]*?[省|市])", project_location)
                if not new_location:
                    new_location = re.findall("项目地点[：|:]([\s\S]*?[省|市])", project_location)
                new_location = new_location[0].replace("\r", "").replace("\n", "").strip()
            except:
                new_location = ""
            data["project_location"] = new_location

        publish_time = data.get("publish_time")
        if publish_time and publish_time == '0001-01-01':
            publish_time = ""
        if not publish_time:
            p_list = html.xpath("//div[@id='noticeContent']/p")
            p_list.reverse()
            for p in p_list:
                try:
                    publish_time = self.format_time(p.xpath("string(.)"))
                    if publish_time:
                        break
                except:
                    publish_time = ""
        data['publish_time'] = publish_time

        bid_end_time = data.get("bid_end_time")
        if bid_end_time and bid_end_time == '0001-01-01':
            bid_end_time = ''
            data['bid_end_time'] = bid_end_time


    @retry(reraise=True, stop=stop_after_attempt(10), wait=wait_fixed(2))
    def req(self, url, req_type="get", rsp_type="content", anti_word="", **kwargs):
        if not kwargs.get("timeout"):
            kwargs["timeout"] = 60
        session = requests.session()
        if kwargs.get("headers"):
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        else:
            kwargs["headers"] = {}
            kwargs["headers"]["User-Agent"] = random.choice(self.user_agent_list)
        if self.proxy_flag:
            kwargs['proxies'] = self.get_proxy()  # 更换代理
            # kwargs['proxies'] = self.get_proxy_bak()

        if req_type == "get":
            response = session.get(url, **kwargs)
            response.encoding = 'utf8'
        elif req_type == "post":
            response = session.post(url, **kwargs)
        else:
            self.log.error(f"error req_type: {req_type}")
            raise Exception
        if not response or response.status_code not in (200, 302):
            self.log.error(f"error response, {response.status_code}")
            self.log.error(url)
            raise Exception
        if not rsp_type or rsp_type == "content":
            content = response.text
        elif rsp_type == "json":
            content = response.json()
        else:
            self.log.error(f"error content:{response.content}")
            raise Exception
        if anti_word and anti_word in content:
            self.log.error(f"anti_word: {anti_word}")
            raise Exception
        # 根据实际情况设置休眠时间
        # time.sleep(random.randint(2, 5))
        return content


if __name__ == '__main__':
    
    params = {
        "proxy_flag": True,
        "query_time": "",
        "MainKeys": [
            "计量", "校准", "检定", "标物", "标准物质", "设备维保", "搬迁", "放射", "医疗", "实验室", "检测", "标定", "检验", "水", "生态", "污", "碳", "废", "声", "农", "排", "土", "气"
            # "校准", "检定"
        ],
        # "time_sleep": (5, 10)
    }
    bid = BidCG(debug=False)
    bid.process_item(params)
