# -*- coding: utf-8 -*-
'''
Created on 2017年8月23日

@author: hasee
'''

# https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D  网址

import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
# from config import * #注意要把config.py文件放在环境变量的目录下
# import pymongo
import os
# from hashlib import md5
# from multiprocessing import Pool




def get_page_index(offset,keyword): #抓取索引页内容
    data={
        'offset': offset, #offset是可变的
        'format': 'json',
        'keyword': keyword,#keyword是可以定义的
        'autoload':'true',
        'count': '20',                                         
        'cur_tab': 3
    }
#data是从XHR项目返回结果的Headers>Query String Parameters里的数据，Query String Parameters指的就是通过在URL中携带的方式提交的参数，也就是PHP中$_GET里的参数
    url='https://www.toutiao.com/search_content/?'+urlencode(data) #urlencode可以把字典对象变成url的请求参数
    try:
        response=requests.get(url)  #请求url
        if response.status_code==200:
            return response.text
        return None
    except RequestException: #所有requests的异常
        print('请求索引页出错')
        return None
    

def parse_page_detail(html): #解析子页面
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def main():
    html=get_page_index(0,'街拍')
#     print(html)
    for url in parse_page_detail(html):
        print(url)

if __name__=='__main__':
    main()
