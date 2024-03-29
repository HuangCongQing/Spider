'''
Description: 基本用法  https://www.bilibili.com/video/BV1Yh411o7Sz?p=50
药监局网站：http://scxk.nmpa.gov.cn:81/xk/
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 14:20:11
LastEditTime: 2021-01-01 14:48:22
FilePath: /Spider/package/4selenium/02selenium基本用法.py
'''
from selenium import webdriver
from lxml import etree  # 解析数据
from time import sleep # 延时5s

#实例化一个浏览器对象（传入浏览器的驱动程序）  如果闪退，是因为驱动版本不对
bro = webdriver.Chrome(executable_path='./chromedriver')  # chromedriver路径

#让浏览器发起一个指定url对应请求
bro.get('http://scxk.nmpa.gov.cn:81/xk/')  # 药监局网站：http://scxk.nmpa.gov.cn:81/xk/

# #page_source获取浏览器当前页面的页面源码数据=========================
page_text = bro.page_source

# #解析企业名称(使用 lxml)
tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')  # li标签
# print(li_list)
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)  # 停5s后关闭浏览器
bro.quit() # 关闭浏览器