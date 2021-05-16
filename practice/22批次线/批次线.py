# 批次线 https://gkcx.eol.cn/quanzhidao?localProvince=11&year=2020&schoolyear=2020&schoolpc=&luqutype=&schoolpro=北京





# 高考志愿帮 https://www.gkzyb.com/baike.html


import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd

def get_baike():
    print('开始爬取数据...')
    # 存储数据初始化
    label_list = []
    title_list =[]
    content_list =[]
    # 获取数据
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://gkcx.eol.cn/quanzhidao?localProvince=11&year=2020&schoolyear=2020&schoolpc=&luqutype=&schoolpro=北京'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    # 获取data
    # tab_con  =  tree.xpath('//div[@class="tabCon"]')
    tr_list1 = tree.xpath('//div[@class="filter_list"]/div[@class="tb_list"]/table/tr')#   一级学科表格
    print(tr_list1) # []
    for tr in tr_list1:
        names = tr.xpath('./td')
        for name in names:
            proviance_name = name.xpath('./tr').text#
            # proviance_list.append(proviance_name)
            print("省份", proviance_name)
    # 处理数据
    """ 
    处理数据
    """
    
    # 保存csv文件
    # print('保存csv文件...')
    # #字典中的key值即为csv中列名
    # dataframe = pd.DataFrame({'专业批次':label_list,'学校':title_list,'特色专业':content_list})
    # #将DataFrame存储为csv,index表示是否显示行名，default=True
    # dataframe.to_csv(r"特色专业数据20210516.csv",index=False, sep=',')
    # print('爬取结束',)


    
if __name__ == "__main__":
    get_baike()
