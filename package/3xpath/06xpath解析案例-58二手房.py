'''
Description:  爬取58二手房中的房源信息  参考：
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-04 10:33:00
FilePath: /Spider/package/3xpath/06xpath解析案例-58二手房.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#需求：爬取58二手房中的房源信息
if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    #爬取到页面源码数据
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text  # 别忘了.text

    #数据解析
    tree = etree.HTML(page_text)
    #存储的就是li标签对象
    li_list = tree.xpath('//ul[@class="house-list-wrap"]/li')
    fp = open('58.txt','w',encoding='utf-8')
    for li in li_list:
        #局部解析
        title = li.xpath('./div[2]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
