'''
Description:  参考 https://www.bilibili.com/video/BV1Yh411o7Sz?p=27
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-04 13:32:12
FilePath: /Spider/package/3xpath/08xpath解析案例-全国城市名称爬取.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from lxml import etree
#项目需求：解析出所有城市名称https://www.aqistudy.cn/historydata/
if __name__ == "__main__":
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    # }
    # url = 'https://www.aqistudy.cn/historydata/'
    # page_text = requests.get(url=url,headers=headers).text
    #
    # tree = etree.HTML(page_text)
    # host_li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # #解析到了热门城市的城市名称
    # for li in host_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #
    # #解析的是全部城市的名称
    # city_names_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in city_names_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    #
    # print(all_city_names,len(all_city_names))

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    #解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/          热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a  全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)
    print(all_city_names,len(all_city_names))