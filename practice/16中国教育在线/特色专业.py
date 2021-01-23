'''
Description: 特色专业 https://www.eol.cn/e_html/gk/tszy/index.shtml
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-23 22:53:47
LastEditTime: 2021-01-24 00:38:20
FilePath: /Spider/practice/16中国教育在线/特色专业.py
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
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.eol.cn/e_html/gk/tszy/index.shtml'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    class_list = []
    school_list = []
    sub_list = []
    tab_con  =  tree.xpath('//div[@class="tabCon"]')
    # print(tab_con)
    for i in range(len(tab_con)):
        tr_list = tree.xpath('//div[@class="tabCon"][' + str(i+1) + ']/table/tr')[1:]# 第七批
        # print(tr_list)
        for tr in tr_list:
            name = tr.xpath('./td//text()')
            class_name = tree.xpath('//div[@class="tabCon"][' + str(i+1) + ']/div')[0].text[0:3] # 第七批 名字
            class_list.append(class_name)
            class_list.append(class_name)
            # print(name[0])
            school_list.append(name[0])
            school_list.append(name[2])
            sub_list.append(name[1])
            sub_list.append(name[3])
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'专业批次':class_list,'学校':school_list,'特色专业':sub_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"特色专业数据.csv",index=False, sep=',')
    print('爬取结束',)



    


if __name__ == "__main__":
    get_subject()
