'''
Description: https://www.bilibili.com/video/BV1Yh411o7Sz?p=54
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-01 17:03:12
FilePath: /Spider/package/4selenium/06谷歌无头浏览器&反检测.py
'''
from selenium import webdriver
from time import sleep
#实现无可视化界面
from selenium.webdriver.chrome.options import Options
#实现规避检测
from selenium.webdriver import ChromeOptions

#实现无可视化界面的操作
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#实现规避检测（Chrome79以后版本，用这个方法不能规避检测）
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])

#如何实现让selenium规避被检测到的风险
bro = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options,options=option)

#无可视化界面（无头浏览器） phantomJs（已停止维护）
bro.get('https://www.baidu.com')

print(bro.page_source) # 输出页面资源======================
sleep(2)
bro.quit()