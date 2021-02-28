'''
Description: 重点学科 http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266612.shtml
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-23 22:20:12
LastEditTime: 2021-02-28 23:12:05
FilePath: /Spider/practice/16中国教育在线/重点学科(研究生网站).py
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

def get_subject():
    print("正在获取所有数据... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266529.shtml'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    class_list = [] # 学科类别
    table_list = [] # 学科级别
    tr_list = [] # 学科名

    tab_con  =  tree.xpath('//div[@class="tabCon"]')
    # print(tab_con)
    for i in range(len(tab_con)):
        i = i+1 # 索引是从  1   开始的。
        for page in range(1,3):
            tr_list1 = tree.xpath('//div[@class="tabCon"][' + str(i) + ']/table[' + str(page) + ']/tr')#   一级学科表格
            # print(tr_list[0].text)
            for tr in tr_list1:
                names = tr.xpath('./td/a')
                for name in names:
                    class_name = tree.xpath('//div[@class="tabs"]/a')[i-1].text#
                    class_list.append(class_name)
                    # print("学科类别：", class_name)
                    table_tit = tree.xpath('//div[@class="tabCon"][' + str(i) + ']/div[@class="tableTit"]')[page-1].text[0:8]# 国家一级重点学科名单(2007年批准) 点击学科名称查看开设院校
                    # print("table_tit:", table_tit)
                    table_list.append(table_tit)
                    # print(name.text)
                    tr_list.append(name.text)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'学科类别':class_list,'学科级别':table_list,'学科名':tr_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"重点学科数据.csv",index=False, sep=',')
    print('爬取结束',)



    


if __name__ == "__main__":
    get_subject()
