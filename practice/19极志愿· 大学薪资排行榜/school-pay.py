'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-28 18:02:31
LastEditTime: 2021-03-29 20:01:22
FilePath: /Spider/practice/19极志愿· 大学薪资排行榜/school-pay.py
'''


import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd

def get_school_pay():
    # 存储数据初始化
    school_list = []
    pay_list =[]
    # 获取数据
    url_list = [
        "https://www.jizhy.com/open/sch/salary-rank-list?page=2&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616920394813&platform=desktop&v=210&sign=C68954F81BBFD6C84465E136483B2081"
    ]
    for url in url_list: # 0-2800
        print("正在获取：", url)
        #UA伪装：将对应的User-Agent封装到一个字典中
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }
        # url = 'https://www.jizhy.com/open/sch/salary-rank-list?page='+ str(page) +  '&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts='+ str(ts) +  '&platform=desktop&v=210&sign='+ str(sign)
        # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        # print("访问url：", url)
        response = requests.get(url=url,headers=headers, timeout=60)
        response.encoding = 'utf-8' 
        content = response.content
        # json格式转为字典
        result = json.loads(content)
        print("结果：",result)
        # print("爬取专业数：",len(result['data']['item']))

    # for page in range(0,1): # 0-2800
    #     print("正在获取页数：", page + 1)
    #     #UA伪装：将对应的User-Agent封装到一个字典中
    #     headers = {
    #         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    #     }
    #     ts = ""
    #     sign = ""
    #     url = 'https://www.jizhy.com/open/sch/salary-rank-list?page='+ str(page) +  '&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts='+ str(ts) +  '&platform=desktop&v=210&sign='+ str(sign)
    #     # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
    #     #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    #     # print("访问url：", url)
    #     response = requests.get(url=url,headers=headers, timeout=60)
    #     response.encoding = 'utf-8' 
    #     page_text = response.text
    #     # print(page_text)
    #     tree = etree.HTML(page_text)
    #     tr_list  =  tree.xpath('//div[@class="width1000"]/table/tbody/tr/td/a')
    


if __name__ == "__main__":
    get_school_pay()