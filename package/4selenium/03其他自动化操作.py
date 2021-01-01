'''
Description:  搜索框输入，网页点击，滑动  https://www.bilibili.com/video/BV1Yh411o7Sz?p=51
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 15:15:27
LastEditTime: 2021-01-01 15:18:17
FilePath: /Spider/package/4selenium/03其他自动化操作.py
'''
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.taobao.com/')

bro.find_element_by_id('q')
