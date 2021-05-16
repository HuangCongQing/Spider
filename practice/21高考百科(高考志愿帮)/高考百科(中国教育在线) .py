# 中国教育在线：https://www.eol.cn/e_html/gk/baike/index.shtml


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
    # 存储数据初始化
    label_list = []
    title_list =[]
    content_list =[]
    # 获取数据
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://www.eol.cn/e_html/gk/baike/index.shtml'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    # 获取data
    tab_con  =  tree.xpath('//div[@class="main-jiaoyubu"]')
    # 处理数据
    for tab in tab_con:
        modTitle = tab.xpath('./div[@class="xiala"]/h4//text()')[0]
        print("modTitle", modTitle)
        li_lsit = tab.xpath('./div[@class="dianjichuxian"]/div[@class="layout"]/a')
        for tr in li_lsit:
            title = tr.xpath('.//text()')[0]
            url1 =  tr.xpath('./@href')[0]
            if url1.find("https") == -1: # 不包含
                url1 = "https:" + str(url1)
            else:
                url1 = url1
            # print("url",url1)
            print("正在爬取百科：",title)
            #UA伪装：将对应的User-Agent封装到一个字典中
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
            }
            # url = 'https://www.gkzyb.com/baike.html'
            #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
            response = requests.get(url=url1,headers=headers)
            response.encoding = 'utf-8' 
            page_text = response.text
            # print(page_text)
            tree = etree.HTML(page_text)
            # 获取data
            try:
                if url1.find("gaokao.eol.cn/") != -1: # 不包含
                    tab_content  =  tree.xpath('//div[@class="article"]')
                elif url1.find("daxue.eol.cn/") != -1:
                    tab_content  =  tree.xpath('//div[@class="con"]')
                elif url1.find("www.eol.cn/e_html/") != -1:
                    tab_content  =  tree.xpath('//div[@class="conBox"]')
                else:
                    tab_content  =  tree.xpath('//div[@class="container box"]')
                content = etree.tostring(tab_content[0], encoding='utf8', method='html').decode()
                print("--爬取链接内容")
            except:
                print("--此链接没所需内容！！！")
                continue
            # print("content", content)
            label_list.append(modTitle)
            title_list.append(title)
            content_list.append(content)
        
    
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'类别':label_list,'百科名':title_list,'百科内容':content_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"高考百科（中国教育在线）20210517.csv",index=False, sep=',')
    print('爬取结束',)


    
if __name__ == "__main__":
    get_baike()
