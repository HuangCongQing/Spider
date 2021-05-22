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
from tqdm import tqdm

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
    url = 'https://www.gkzyb.com/baike.html'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    # 获取data
    tab_con  =  tree.xpath('//div[@class="baikeMain"]/div[@class="baikeList"]')
    # 处理数据
    for tab in tab_con:
        modTitle = tab.xpath('./div[@class="modTitle"]/h2//text()')[0]
        print("modTitle", modTitle)
        li_lsit = tab.xpath('./div[@class="modContent"]/ul/li')
        url_list = []
        for tr in li_lsit:
            title = tr.xpath('.//text()')[0]
            url1 =  tr.xpath('./a/@href')[0]
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
                tab_content  =  tree.xpath('//div[@class="baikeArticle"]')[0]
                # print("tab_content", tab_content)
                tab_content = etree.tostring(tab_content, encoding='utf8', method='html').decode()
                ex = '(.*?)<div class="clear">'  # 得到销售代表的数据
                tab_content = re.findall(ex,tab_content, re.S)[0]# 正则
                tab_content = tab_content + "</div>"
                # print("tab_content", tab_content)
            except:
                print("此链接没所需内容！！！")
                continue
            # print("content", content)
            label_list.append(modTitle)
            title_list.append(title)
            content_list.append(tab_content)
        
    
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'类别':label_list,'百科名':title_list,'百科内容':content_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"高考百科（高考志愿帮）20210521.csv",index=False, sep=',')
    print('爬取结束',)


    
if __name__ == "__main__":
    get_baike()
