'''
Description:  搜索框输入，网页点击，滑动  https://www.bilibili.com/video/BV1Yh411o7Sz?p=51
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 15:15:27
LastEditTime: 2021-01-01 15:49:58
FilePath: /Spider/package/4selenium/03其他自动化操作.py
'''
from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.taobao.com/')


#标签定位
search_input = bro.find_element_by_id('q')
#标签交互
search_input.send_keys('Iphone')


#执行一组js程序
bro.execute_script(r'window.scrollTo(0,document.body.scrollHeight)') # 滚动一屏的高度
sleep(2)
#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

# ========================进入百度页面

bro.get('https://www.baidu.com')
sleep(2) # 等待2s
#回退
bro.back() # 点击返回按钮
sleep(2)
#前进
bro.forward()

sleep(5)

bro.quit()

