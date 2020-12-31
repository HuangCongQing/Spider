#config.py
MONGO_URL='localhost'
MONGO_DB='toutiao'
MONGO_TABLE='toutiao'

group_start=1
group_end=10
KEYWORD='街拍'

import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re
from config import * #注意要把config.py文件放在环境变量的目录下
import pymongo
import os
from hashlib import md5
from multiprocessing import Pool

client=pymongo.MongoClient(MONGO_URL) #声明MongoDB对象
db=client[MONGO_DB] #定义db


def get_page_index(offset,keyword): #抓取索引页内容
    data={
        'offset': offset, #offset是可变的
        'format': 'json',
        'keyword': keyword,#keyword是可以定义的
        'autoload':'true',
        'count': '20',                                         
        'cur_tab': 3
    }
#data是从XHR项目返回结果的Headers>Query String Parameters里的数据，Query String Parameters指的就是通过在URL中携带的方式提交的参数，也就是PHP中$_GET里的参数
    url='https://www.toutiao.com/search_content/?'+urlencode(data) #urlencode可以把字典对象变成url的请求参数
    try:
        response=requests.get(url)  #请求url
        if response.status_code==200:
            return response.text
        return None
    except RequestException: #所有requests的异常
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data=json.loads(html) #对字符串进行解析，把字符串转化成json对象
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')  #构造一个生成器，把所有的article_url解析出来

def get_page_detati(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错',url)
        return None

def parse_page_detail(html,url): #解析子页面
    soup=BeautifulSoup(html,'lxml') #用BeautifulSoup来解析获取的子页面html代码
    titie=soup.select('title')[0].get_text() #CSS选择器
    print(titie)
    images_pattern=re.compile('gallery: (.*?),\n',re.S)  #用正则来匹配出gallery里面的数据
    result=re.search(images_pattern,html)
    if result:
        #print(result.group(1))
        data=json.loads(result.group(1)) #对字符串进行解析，把字符串转化成json对象
        if data and 'sub_images' in data.keys(): #判断里面是否含有我们想要的数据
            sub_images=data.get('sub_images')
            images=[item.get('url') for item in sub_images]
            for image in images:download_imagg(image)
            return {
                'title':titie,
                'url':url,
                'images':images
            }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储成功到MongoDB',result)
        return True
    return False

def download_imagg(url):
    print('正在下载',url)
    try:
        response=requests.get(url)
        if response.status_code==200:
            #return response.text
            save_image(response.content)
        return None
    except RequestException:
        print('请求图片出错',url)
        return None

def save_image(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb')as f:
            f.write(content)
            f.close()



def main(offset):
    html=get_page_index(offset,KEYWORD)
    #print(html)
    for url in parse_page_index(html):
        #print(url)
        html=get_page_detati(url)  #利用for循环，提取出所有的article_url
        if html:
            #parse_page_detail(html)
            result=parse_page_detail(html,url)
            #print(result)
            if result:save_to_mongo(result)


if __name__=='__main__':
    #main()
    groups=[i*10 for i in range(group_start,group_end+1)]
    pool=Pool()
    pool.map(main,groups)