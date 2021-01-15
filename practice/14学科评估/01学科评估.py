'''
Description: 学科评估    网站：https://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?xkdm=01,02,03,04,05,06
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 20:19:18
LastEditTime: 2021-01-15 21:45:17
FilePath: /Spider/practice/14学科评估/01学科评估.py
'''

import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re

def get_subject(id):
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    param = {
        'yjxkdm': '0101'
        'xkdm':id
    }
    url = 'https://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp'
    # url = 'https://www.cdgdc.edu.cn/xwyyjsjyxx/xkpgjg/'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    # response = requests.get(url=url,headers=headers)
    # response.encoding = 'utf-8-sig' 
    # print(print(response.encoding))
    # page_text = response.text.encode('iso-8859-1').decode('gbk')
    page_text = response.content.decode('GBK')
    print(page_text)
    # tree = etree.HTML(page_text)
    # name = tree.xpath('//tbody/tr/td')
    # print(name)



if __name__ == "__main__":
    # class_id =['01,02,03,04,05,06', '07', '08', '09', '10', '11', '12', '13']
    id = '01,02,03,04,05,06'
    urls = get_subject(id)
    # urls = ['rw6z9nza7gduikyw', 'dvbww41vhzdiqaq9']
    # url = 'rw6z9nza7gduikyw'
    # get_contents(url)



    

