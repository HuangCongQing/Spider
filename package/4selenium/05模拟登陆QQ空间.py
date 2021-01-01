'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-01 16:29:24
FilePath: /Spider/package/4selenium/05模拟登陆QQ空间.py
'''
from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')

bro.switch_to.frame('login_frame')

a_tag = bro.find_element_by_id("switcher_plogin")
a_tag.click()


userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('328410948')
sleep(1)
password_tag.send_keys('123456789')
sleep(1)
btn = bro.find_element_by_id('login_button')
btn.click()

sleep(3)

bro.quit()