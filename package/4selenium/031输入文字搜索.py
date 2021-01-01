'''
Description:  搜索框输入文字搜索滑动  https://www.bilibili.com/video/BV1Yh411o7Sz?p=51
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 15:15:27
LastEditTime: 2021-01-01 15:34:21
FilePath: /Spider/package/4selenium/031输入文字搜索.py
'''
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.taobao.com/')

#标签定位
search_input = bro.find_element_by_id('q')
#标签交互（输入文字）
search_input.send_keys('Iphone')

#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
# btn = bro.find_element_by_css_selector('.btn-search')
btn.click()


sleep(5)
bro.quit() # 退出



