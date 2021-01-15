'''
Description: https://souky.eol.cn/api/newapi/assess_result
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 21:15:31
LastEditTime: 2021-01-15 21:50:46
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
    param = {
        'xid': 1,
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
    print(result[0]["code"])
    print(result[0]["name"])



if __name__ == "__main__":
    get_subject()



    

