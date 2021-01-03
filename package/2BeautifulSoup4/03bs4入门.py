'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-03 21:31:19
FilePath: /Spider/package/2BeautifulSoup4/03bs4入门.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html','r',encoding='utf-8')  # test.html测试文档
    soup = BeautifulSoup(fp,'lxml')
    # print(soup)
    # print(soup.a) #soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.div)
    #find('tagName'):等同于soup.div
    # print(soup.find('div'))  #print(soup.div)
    # print(soup.find('div',class_='song').string)
    # print(soup.find_all('a'))
    # print(soup.select('.tang'))
    print(soup.select('.tang > ul a')[0]['href'])