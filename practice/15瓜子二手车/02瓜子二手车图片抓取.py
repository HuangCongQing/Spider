'''
Description: 参考: https://blog.csdn.net/weixin_39679004/article/details/83024243
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-19 14:10:17
LastEditTime: 2021-01-19 14:11:28
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
        content = pq(self.sess.get(start_url).text)
        for each in content('ul[@class="carlist clearfix js-top"]  > li > a').items():
            url = each.attr.href
            if not url.startswith('http'):
                url = self.baseurl + url
                yield url

    def detail_page(self, detail_url):
        '''
        抓取详情信息
        :param detail_url:
        :return:
        '''
        # page_text = self.sess.get(detail_url).text
        content = pq(self.sess.get(detail_url).text)
        # fileName = 'index.html'
        # with open(fileName,'w',encoding='utf-8') as fp:
        #     fp.write(page_text)
        # print(content)
    #    print(content('ul[@class="assort clearfix"]').find('li').eq(3).find('span').text())
        # result = content('ul[@class="carlist clearfix js-top"] li[@class="two"] span').text()
        # result = content('ul[@class="carlist clearfix js-top"]').find('li').eq(2).find('span').text(),
        # print(result)

        data_dict = {
            'title': content('h2.titlebox').text().strip(),  # h1.titlebox  输出结果会为空!!!!??????
            'bordingdate': content('ul[@class="assort clearfix"] li[@class="one"] span').text(),
            'km': content('ul[@class="assort clearfix"] li[@class="two"] span').text(),
            'address': content('ul[@class="assort clearfix"]').find('li').eq(2).find('span').text(),
            'displacement': content('ul[@class="assort clearfix"]').find('li').eq(3).find('span').text(),
            'gearbox': content('ul[@class="assort clearfix"] li[@class="two"] span').text(),
            'price': content('span[@class="pricestype"]').text(),
        }
        if not data_dict['title']:
            #print(str(content).encode('ISO-8859-1').decode('utf-8'))
            return data_dict
        
        
        
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
            for detail_url in self.index_page(pageurl):
                result = self.detail_page(detail_url)
                print(result) # 结果
            print('*'*200)


if __name__ == '__main__':
    gzcrawler = GuaZiCrawler()
    gzcrawler.run()