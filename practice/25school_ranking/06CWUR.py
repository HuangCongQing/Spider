'''
Description: CWUR世界大学排名中心https://cwur.org/2021-22.php 表格
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-03-19 02:36:22
LastEditTime: 2022-03-28 12:55:01
FilePath: \Spider-1\practice\25school_ranking\06CWUR.py
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

def get_ranking():
    print("正在获取所有数据... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = "https://cwur.org/2021-22/country/china.php"
    # url = 'https://cwur.org/2021-22.php'
    # 
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    rank_list = [] # 学科类别
    school_list = [] # 学科级别
    year_list = [] # 学科名

    tr_list1 = tree.xpath('//div[@class="table-responsive"]/table/tbody/tr')#   一级学科表格
    print(len(tr_list1)) # 2000个学校
    for tr in tr_list1:
        names = tr.xpath('./td')
        # item = list(map(lambda x: str(x.text), names))
        # print(item)
        # print(names[0].text, names[1].xpath('./a')[0].text) # 1986 Polytechnic Institute of Bragança
        # 国家筛选
        # print(names[2].text)
        # if(names[2].text != "China"):
        #     continue
        rank_list.append(names[0].text)
        school_list.append(names[1].xpath('./a')[0].text)
        year_list.append('2021')
    #     for name in names:
    #         class_name = tree.xpath('//div[@class="tabs"]/a')[i-1].text#
    #         class_list.append(class_name)
    #         # print("学科类别：", class_name)
    #         table_tit = tree.xpath('//div[@class="tabCon"][' + str(i) + ']/div[@class="tableTit"]')[page-1].text[0:8]# 国家一级重点学科名单(2007年批准) 点击学科名称查看开设院校
    #         # print("table_tit:", table_tit)
    #         table_list.append(table_tit)
    #         # print(name.text)
    #         tr_list.append(name.text)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'rank':rank_list,'school':school_list,'year':year_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"06CWUR世界大学排名2021.csv",index=False, sep=',')
    print('爬取结束',)



    


if __name__ == "__main__":
    get_ranking()
