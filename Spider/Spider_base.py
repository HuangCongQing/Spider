# -*- coding: utf-8 -*-
'''
Created on 2017年8月22日

@author: hasee
'''
import requests
# 引入异常处理模块
from requests.exceptions import RequestException
import re


def get_one_page(url):
    try:# 获取数据异常判断
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('', re.S)
    items= re.findall(pattern, html)
    print(items)
# 下生成字典的形式
#     for item in items:
#         yield{
#             'index': item[0]
#             }

def main():
    url = "https://user.qzone.qq.com/1756260160/infocenter"
    html = get_one_page(url)
#     输出整个
    print(html)
    # 输出匹配好的
#     parse_one_page(html)

#     for item in parse_one_page(html):
#         print(item)
    
    

if __name__ == '__main__':
    main()



