'''
Description: 职业百科信息收集   网站：https://xz.chsi.com.cn/occupation/index.action
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 12:43:59
LastEditTime: 2021-01-15 13:07:40
FilePath: /Spider/practice/13职业百科信息搜集/职业百科信息搜集.py
'''
import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json

def get_links():
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://xz.chsi.com.cn/ajax/occuindexqt.action'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.post(url=url,headers=headers)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    print(result)
    # tree = etree.HTML(page_text)
    # tr_list = tree.xpath('//div[@class="zhiye"]')
    # print("获取链接：", len(tr_list))


def get_contents(urls):
    print("正在获取各职位数据... ...")

if __name__ == "__main__":
    urls = get_links()



    

