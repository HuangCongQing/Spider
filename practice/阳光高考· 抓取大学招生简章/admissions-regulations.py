'''
Description: 招生简章
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-28 23:20:11
LastEditTime: 2021-03-29 11:38:08
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

    school_list = []
    class_regulations_list =[]
    for page in range(0,29): # 0-2800
        print("正在获取页数：", page + 1)
        #UA伪装：将对应的User-Agent封装到一个字典中
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
            'Cookie': 'PI=44; Hm_lvt_2610e5c202b60841b30a62960fbef0ad=1616894968,1616894993,1616924728,1616924739; Hm_lpvt_2610e5c202b60841b30a62960fbef0ad=1616997585'
        }
        url = 'https://gaokao.chsi.com.cn/zsgs/zhangcheng/listVerifedZszc--method-index,lb-1,start-'+ str(100*page) +  '.dhtml'
        # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        # print("访问url：", url)
        response = requests.get(url=url,headers=headers, timeout=60)
        response.encoding = 'utf-8' 
        page_text = response.text
        # print(page_text)
        tree = etree.HTML(page_text)
        tr_list  =  tree.xpath('//div[@class="width1000"]/table/tbody/tr/td/a')
        print('本页学校数量', len(tr_list))
        # print('本页学校', tr_list[0].text)
        # print(tr_list)
        for tr in tr_list: # 遍历每个学校
            school_name = tr.xpath('./text()')[0].replace(' ','').replace('\n', '').replace('\r', '') # 学校名
            link = tr.xpath('./@href')[0] # link
            # print("link: ", link)
            print("正在遍历高校: ", school_name)
            school_url = "https://gaokao.chsi.com.cn" + str(link)
            #UA伪装：将对应的User-Agent封装到一个字典中
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }
            # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
            #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
            response = requests.get(url=school_url,headers=headers,timeout=60)
            response.encoding = 'utf-8' 
            page_text = response.text
            # print(page_text)
            tree = etree.HTML(page_text)
            # 第二个zszcdel
            tr_list  =  tree.xpath('//div[@class="zszcdel"][2]/div[@class="right"]/table/tr')  # 每个学校都有招生简章list
            # print(tr_list)
            class_regulations = []
            # 遍历每个学校招生简章
            for tr in tr_list: 
                name = tr.xpath('./td[1]/a/text()')[0].replace(' ','').replace('\n', '').replace('\r', '') # 学校招生简章
                link = tr.xpath('./td[1]/a/@href')[0] # link
                time =  tr.xpath('./td[2]/text()')[0].replace(' ','').replace('\n', '').replace('\r', '')
                # print("name: ", name, "link: ", link, "time:", time) # name:  北京大学招生章程 link:  /zsgs/zhangcheng/listVerifedZszc--infoId-2355915097,method-view,schId-1.dhtml time:   2019-06-06 16:17
                #UA伪装：将对应的User-Agent封装到一个字典中
                headers = {
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
                }
                url = "https://gaokao.chsi.com.cn" + str(link)
                #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
                response = requests.get(url=url,headers=headers, timeout=60)
                response.encoding = 'utf-8' 
                page_text = response.text
                # print(page_text)
                tree = etree.HTML(page_text)
                # 第二个zszcdel
                msg  =  tree.xpath('//div[@class="content"]') # //text() 标签中非直系的文本内容（所有的文本内容）
                # print("msg:", len(msg))
                content = etree.tostring(msg[0], encoding='utf8', method='html').decode()
                # print("content:", len(content))
                print("content:", content)
                # 将学校的招生简章放在字典，把历年的招生简章放在数组里面
                class_regulation = {
                    'name':name,
                    'time':time,
                    'content':content,
                }
                class_regulations.append(class_regulation)
            # append
            school_list.append(school_name)
            class_regulations_list.append(class_regulations) # 每个学校的

    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'学校名':school_list,'历年招生章程':class_regulations_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"高校招生章程.csv",index=False, sep=',')
    print('爬取结束',)



if __name__ == "__main__":
    get_admissions_regulations()
