'''
Description: 抓取掌上高考专业信息（除了开设院校，其余的信息全都要） https://gkcx.eol.cn/special
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-13 21:13:44
LastEditTime: 2021-03-13 23:57:42
FilePath: /Spider/practice/18掌上高考专业信息/掌上高考专业信息爬取.py
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
    special_list = []
    info_list = []
    level1_list = []
    for page in range(1,27): # 本科25页，专科26
        for level in range(1,3):
            print("正在获取页数：", page)
            #UA伪装：将对应的User-Agent封装到一个字典中
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }
            url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(level)  + '&level2=&page='+ str(page) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
            # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
            #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
            response = requests.get(url=url,headers=headers)
            response.encoding = 'utf-8' 
            content = response.content
            # json格式转为字典
            result = json.loads(content)
            print("爬取专业数：",len(result['data']['item']))
            # print(result['data']['item'][0]['special_id'])
            for item in range(0,len(result['data']['item'])): 
                print("爬取专业:", result['data']['item'][item]['name'])
                #UA伪装：将对应的User-Agent封装到一个字典中
                level1_name = result['data']['item'][item]['level1_name'] # 专业名
                special = result['data']['item'][item]['name'] # 专业名
                headers = { 
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                }
                url = 'https://static-data.eol.cn/www/special/'+ str( result['data']['item'][item]['special_id']) +'/pc_special_detail.json'
                #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
                response = requests.get(url=url,headers=headers)
                response.encoding = 'utf-8' 
                content = response.content
                # json格式转为字典
                result1 = json.loads(content)
                # print(result1)
                level1_list.append(level1_name)
                special_list.append(special)
                info_list.append(result1)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'本专科':level1_list,'专业':special_list,'特色专业信息集合':info_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"掌上高考专业数据.csv",index=False, sep=',')
    print('爬取结束',)



if __name__ == "__main__":
    get_subject()
