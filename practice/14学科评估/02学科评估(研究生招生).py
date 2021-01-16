'''
Description: https://souky.eol.cn/api/newapi/assess_result
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 21:15:31
LastEditTime: 2021-01-16 21:29:38
FilePath: /Spider/practice/14学科评估/02学科评估(研究生招生).py
'''

import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re

def get_subject():
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    class_list = []  # 类别
    subject_list = [] # 学科
    number_list = [] # 序号
    code_list = [] # 学校代码
    sname_list =[] # 校名
    result_list = [] # 评选结果
    percent_list = [] # 百分比
    for page in range(1,3): # 1~111
        param = {
            'xid': page,
            'flag':1
        }
        url = 'https://souky.eol.cn/api/newapi/assess_result'
        # url = 'https://www.cdgdc.edu.cn/xwyyjsjyxx/xkpgjg/'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        response = requests.get(url=url,params=param,headers=headers)
        response.encoding = 'utf-8' 
        content = response.content
        # json格式转为字典
        result = json.loads(content)
        # print(result)

        class_subject = {
            '01': '人文社科类',
            '02': '人文社科类',
            '03': '人文社科类',
            '04': '人文社科类',
            '05': '人文社科类',
            '06': '人文社科类',
            '07': '理学',
            '08': '工学',
            '09': '农学',
            '10': '医学',
            '12': '管理学',
            '13': '艺术学',
        }
        print(class_subject[result[0]["code"][0:2]])
        # print(result[0]["code"])
        # print(result[0]["code"][0:2]) # 根据此得到大类
        print('\t', result[0]["name"]) # 哲学
        for i in range(len(result[1])): 
            class_list.append(class_subject[result[0]["code"][0:2]])
            subject_list.append(result[0]["name"])
            number_list.append(result[1][i]['rid'])
            code_list.append(result[1][i]['scode'])
            sname_list.append(result[1][i]['sname'])
            result_list.append(result[1][i]['result'])
            percent_list.append(result[1][i]['percent'])
            # print('正在遍历学校')
        # print(class_list)
    # 保存csv文件
    print('保存csv文件...')

    print('爬取结束')
if __name__ == "__main__":
    get_subject()



    

