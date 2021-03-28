'''
Description: 招生简章
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-28 23:20:11
LastEditTime: 2021-03-29 00:53:50
FilePath: /Spider/practice/阳光高考· 抓取大学招生简章/admissions-regulations.py
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

def get_admissions_regulations():
    for page in range(0,1): # 0-2800
        print("正在获取页数：", page)
        #UA伪装：将对应的User-Agent封装到一个字典中
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        url = 'https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1.start-'+ str(10*page) +  '.dhtml'
        # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8' 
        page_text = response.text
        # print(page_text)
        tree = etree.HTML(page_text)
        tr_list  =  tree.xpath('//div[@class="width1000"]/table/tbody/tr/td/a')
        print('本页学校数量', len(tr_list))
        # print(tr_list)
        for tr in tr_list: # 遍历每个学校
            name = tr.xpath('./text()') # 学校名
            link = tr.xpath('./@href')[0] # link
            # print("link: ", link)
            school_url = "https://gaokao.chsi.com.cn" + str(link)
            #UA伪装：将对应的User-Agent封装到一个字典中
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }
            # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
            #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
            response = requests.get(url=school_url,headers=headers)
            response.encoding = 'utf-8' 
            page_text = response.text
            # print(page_text)
            tree = etree.HTML(page_text)
            # 第二个zszcdel
            tr_list  =  tree.xpath('//div[@class="zszcdel"][2]/div[@class="right"]/table/tr/td/a')
            # print(tr_list)
            for tr in tr_list: # 遍历每个学校
                name = tr.xpath('./text()') # 学校名
                link = tr.xpath('./@href')[0] # link
                # print("link: ", link)
                #UA伪装：将对应的User-Agent封装到一个字典中
                headers = {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                }
                url = "https://gaokao.chsi.com.cn" + str(link)
                #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
                response = requests.get(url=url,headers=headers)
                response.encoding = 'utf-8' 
                page_text = response.text
                # print(page_text)
                tree = etree.HTML(page_text)
                # 第二个zszcdel
                content  =  tree.xpath('//div[@class="content"]//text()') # //text() 标签中非直系的文本内容（所有的文本内容）
                print("content:", content)



if __name__ == "__main__":
    get_admissions_regulations()
