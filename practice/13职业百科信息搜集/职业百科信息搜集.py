'''
Description: 职业百科信息收集   网站：https://xz.chsi.com.cn/occupation/index.action
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 12:43:59
LastEditTime: 2021-01-17 21:54:31
FilePath: /Spider/practice/13职业百科信息搜集/职业百科信息搜集.py
'''
import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re

def get_links():
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://xz.chsi.com.cn/ajax/occuindexqt.action'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.post(url=url,headers=headers)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    print(len(result))
    class_names = []
    names = []
    urls = []
    for i in range(len(result)):  # 23次
        print("循环获取url  ... ..")
        info = result[i]["occInfos"]
        # print(len(info))
        for j in range(len(info)):  # 23次
            id = info[j]['id']
            name = info[j]['name']
            # print(id)
            urls.append(id)
            names.append(name)
            class_names.append(result[i]['ktname'])
    # print(urls)
    return urls, names, class_names
    # tree = etree.HTML(page_text)
    # tr_list = tree.xpath('//div[@class="zhiye"]')
    # print("获取链接：", len(tr_list))


def get_contents(id):
    print("正在获取各职位数据... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'https://xz.chsi.com.cn/occupation/occudetail.action?id=' + id
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    detail_page_text = requests.post(url=url,headers=headers).text
    print(detail_page_text)
    # 正则re
    # ex = '"zhiyname":"(.*?)","zhiydesc"'  # 得到销售代表的数据
    # json_data = re.findall(ex,detail_page_text, re.S)# 正则
    ex = '"data: {(.*?)'  # 得到销售代表的数据
    json_data = re.findall(ex,detail_page_text, re.S)# 正则
    print(json_data)

    # BeautifulSoup
    # detail_soup = BeautifulSoup(detail_page_text,'lxml')
    # container = detail_soup.find('div',class_='xz-part-label')
    # print(container)
    # containers.append(container)


    # lxml
    # tree = etree.HTML(detail_page_text)
    # tr_list = tree.xpath('//div[@class="zhiye"]')
    # print("获取链接：", len(tr_list))

if __name__ == "__main__":
    urls, names, class_names = get_links()
    print(class_names)
    # urls = ['rw6z9nza7gduikyw', 'dvbww41vhzdiqaq9']
    # url = 'rw6z9nza7gduikyw'
    # get_contents(url)



    

