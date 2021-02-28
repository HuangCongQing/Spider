'''
Description: 重点学科 http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266612.shtml
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-23 22:20:12
LastEditTime: 2021-03-01 02:15:16
FilePath: /Spider/practice/16中国教育在线/重点学科(研究生网站) 循环.py
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
import numpy as np

def get_subject():
    print("正在获取所有数据... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    urls = ['http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266529.shtml']
    class_lists = [] # 学科类别
    table_lists = [] # 学科级别
    tr_lists = [] # 学科名
    schools_lists = [] # 学校名
    
    for url in urls:
        print(url)
        url_class = url.split('/')[-2] # lsx
        print(url_class)
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8' 
        page_text = response.text
        # print(page_text)
        tree = etree.HTML(page_text)
        class_list = [] # 学科类别
        table_list = [] # 学科级别
        tr_list = [] # 学科名
        schools_list = [] # 学校名

        tab_con  =  tree.xpath('//div[@class="cdcy"]/table/tr/td')   # 没有tbody=========================================
        print(tab_con)
        ids = []
        for tabs in tab_con[1]:
            if tabs:
                id =  tabs.xpath('./@id')[0]
                ids.append(id)
                print(id)
        # 遍历id列表
        for id in ids:
            url = 'http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/'    + str(url_class) +'/' + str(id)  +'.shtml'
            class_names = pd.read_html(url)[0][0].values[1:-1] # 一二级学科  类别
            class_names = class_names[~np.isin(class_names,'类别')] 
            print(class_names)
            subject_names = pd.read_html(url)[0][1].values[1:-1] # 学科名称   学科代码及名称
            subject_names = subject_names[~np.isin(subject_names,'学科代码及名称')] 
            school_names = pd.read_html(url)[0][2].values[1:-1] # 学校名字  学校名称
            school_names = school_names[~np.isin(school_names,'学校名称')] 


            print(len(class_names), len(subject_names), len(school_names))
            table_list.extend(class_names)
            tr_list.extend(subject_names)
            schools_list.extend(school_names)

            class_list =['人文社科类']*len(schools_list) # 添加相同数量类别
    
       
        table_lists.extend(table_list)
        tr_lists.extend(tr_list)
        schools_lists.extend(schools_list)
        class_lists.extend(class_list) # 添加相同数量类别


    # # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'学科类别':class_lists,'类别':table_lists,'学科代码及名称':tr_lists,'学校名称':schools_lists})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"重点学科(研究生网站)循环.csv",index=False, sep=',')
    
    print('爬取结束',)



    


if __name__ == "__main__":
    get_subject()
