#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2021/11/21 下午6:38
@Author: CZC
@File: jsonToexcel.py
"""
import json
import pandas as pd
from openpyxl import load_workbook
import os
import datetime


class jsonToExcel(object):
    def __init__(self, file_name, local=False):
        self.data_list = []
        self.id_list = []
        self.file_name = file_name
        self.columns_list = []
        self.local = local

    def upload(self):
        # temp_list = [list(i.values()) for i in self.data_list]
        if self.columns_list:
            columns = self.columns_list
        else:
            columns = list(self.data_list[0].keys())
        temp_list = []
        for i in self.data_list:
            tmp2 = []
            for j in columns:
                value = str(i.get(j, "")).replace('None', '0')
                tmp2.append(value)
            temp_list.append(tmp2)
        # temp_list = [[i.get(j) for j in columns] for i in self.data_list]
        sheet_name = 'Sheet1'
        file_name = "./outputs/{}.xlsx".format(self.file_name)
        if not os.path.exists(file_name):
            pd.DataFrame(temp_list, columns=columns).to_excel(file_name, index=None)
            return
            # file_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        df = pd.DataFrame(temp_list, columns=columns)  # 列表数据转为数据框
        df1 = pd.DataFrame(pd.read_excel(file_name, sheet_name=sheet_name))  # 读取原数据文件和表
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        book = load_workbook(file_name)
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        df_rows = df1.shape[0]  # 获取原数据的行数
        df.to_excel(writer, sheet_name=sheet_name, startrow=df_rows + 1, index=False, header=False)  # 将数据写入excel中的aa表,从第一个空行开始写
        writer.save()  # 保存
        self.data_list = []

    def read_file(self):
        with open('./inputs/{}.json'.format(self.file_name), 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = json.loads(line.replace("\n", "").replace("&nbsp;", "").replace("\r", ""))
                if line.get("_id"):
                    line.pop("_id")
                # line.pop("url")
                yield line

    def run(self):
        counts = 0
        if self.local:
            for d in self.read_file():
                counts += 1
                self.data_list.append(d)
                if counts % 1000 == 0:
                    print(counts)
        else:
            pass
        self.upload()
        print(counts)


if __name__ == '__main__':
    jte = jsonToExcel('', False)
    jte.run()
