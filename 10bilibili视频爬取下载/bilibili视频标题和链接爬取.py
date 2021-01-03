'''
Description: bilibili视频标题和链接爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 14:57:10
LastEditTime: 2021-01-03 15:56:02
FilePath: /Spider/10bilibili视频爬取下载/bilibili视频标题和链接爬取.py
'''
import requests,lxml,jieba,codecs,re,json
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

word =  "重庆邮电大学 宣传片 最新"  	# 解析，用于组成URL
keyword = urllib.parse.urlencode( {"keyword" : word} )  	# 解析，用于组成URL
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url="https://search.bilibili.com/all?%s" % keyword , headers=headers)  
response = urllib.request.urlopen(req )  
html = response.read().decode('utf-8')
soup = BeautifulSoup( html , "lxml" )  # lxml解析
print(soup)