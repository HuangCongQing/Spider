'''
Description: 参考: https://blog.csdn.net/weixin_39679004/article/details/83024243
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-19 14:10:17
LastEditTime: 2021-01-19 20:19:34
FilePath: /Spider/practice/15瓜子二手车/02瓜子二手车图片抓取.py
'''

# -*- coding: utf-8 -*-
import re
import requests
import os
import time
from selenium import webdriver
from lxml import etree
import json
import csv

from pyquery import PyQuery as pq
from execute_script import excuteScript

headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}


class GuaZiCrawler():

    def __init__(self):
        self.baseurl = 'https://www.guazi.com'
        self.sess = requests.Session()
        self.sess.headers = headers
        self.start_url = 'https://www.guazi.com/qd/buy/'


    def anti_value(self):
        '''
        获取antipas参数需要的key和value
        :return:
        '''
        content = self.sess.get(self.baseurl).text.encode('ISO-8859-1').decode('utf-8')
        params = re.findall(r"value=anti\('(.*?)','(.*?)'\)", content)[0]
        return params

    def caculate_antipas(self):
        '''
        计算antipas参数
        :return: 
        '''
        params = self.anti_value()
        antipas = excuteScript(params[0], params[1])
        self.sess.cookies.set('antipas', antipas)

    def page_url(self):
        self.caculate_antipas()
        '''
        获取翻页链接
        :param start_url:
        :return:
        '''
        content = pq(self.sess.get(self.start_url).text)
        page_num_max = max([int(each.text()) for each in content('ul[@class="pageLink clearfix"]  > li > a').items() if re.match(r'\d+', each.text())])
        print("总页面:", page_num_max)
        page_url_list = []
        for i in range(1,page_num_max+1,1):
            base_url = 'https://www.guazi.com/qd/buy/o{}/'.format(i)
            page_url_list.append(base_url)

        return page_url_list

    def index_page(self, start_url):
        '''
        抓取详情页链接
        :param start_url:
        :return:
        '''
        
        page_text = self.sess.get(start_url).text
        # print(page_text)
        #数据解析
        tree = etree.HTML(page_text)
        #存储的就是li标签对象
        li_list = tree.xpath('//ul[@class="carlist clearfix js-top"] /li/a') # 
        # print(li_list)
        for li in li_list:
            #局部解析
            img_src = li.xpath('./img/@src')[0]
            img_name = li.xpath('./@title')[0]  # 生成图片名称
            print(img_src)
            #请求到了图片的二进制数据
            img_data = requests.get(url=img_src,headers=headers).content
            # #生成图片名称
            # img_name = img_src.split('/')[-1]
            #图片存储的路径
            imgPath = './imgs/'+img_name+'.jpg'
            with open(imgPath,'wb') as fp:
                fp.write(img_data)
                print(img_name,'下载成功！！！')

        
    def download_record(city=None, url=None, name=None):
        path = "./download_img_url.csv"
        if name:
            now_time = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
            with open(path, 'a') as f:
                write = csv.writer(f)
                write.writerow([city,url,name,now_time])
        else:
            with open(path, 'r') as fp:
                csv_content = csv.reader(fp)
                img_url = set(i[1] for i in csv_content)
            return img_url


    def run(self):
        for pageurl in self.page_url():
            self.index_page(pageurl)
            print('*'*200) # 20个*号


if __name__ == '__main__':
    gzcrawler = GuaZiCrawler()
    gzcrawler.run()