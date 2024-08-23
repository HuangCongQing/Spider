'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2024-08-23 21:14:07
LastEditTime: 2024-08-23 21:25:29
FilePath: \Spider-1\package\5selenium\00template.py
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import random
import sys

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options, service)

driver.get("https://baidu.com")
time.sleep(1)#加载等待
print(driver.title)
print(driver.page_source) # 页面源码数据
with open('result.html','w',encoding='utf-8') as fp:
    fp.write(driver.page_source)

# 1 定位###############
# 1.1通过属性
#通过id定位:
driver.find_element_by_id("kw")
# 通过name定位:
driver.find_element_by_name("wd")
# 通过class name定位:
driver.find_element_by_class_name("s_ipt")
# 通过tag name定位:
driver.find_element_by_tag_name("input")

# 1.2通过xpath定位（浏览器选中元素右键复制full xpath路径）
driver.find_element_by_xpath("//*[@id='kw']")
driver.find_element_by_xpath("//*[@name='wd']")
driver.find_element_by_xpath("//input[@class='s_ipt']")
driver.find_element_by_xpath("/html/body/form/span/input")
driver.find_element_by_xpath("//span[@class='soutu-btn']/input")
driver.find_element_by_xpath("//form[@id='form']/span/input")
driver.find_element_by_xpath("//input[@id='kw' and @name='wd']")

# 2 模拟操作事件###################
# 输入事件
driver.find_element_by_id('username').send_keys("*******") #账号
driver.find_element_by_id('password').send_keys("*******") #密码
# 点击事件
driver.find_element_by_xpath("//button[@class='auth_login_btn primary full_width'][@type='submit']").click()#点击按钮
print("Completed.")

driver.close()