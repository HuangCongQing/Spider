# -*- coding: utf-8 -*-
'''
Created on 2017年8月24日

@author: hasee
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyquery import PyQuery as pq
import re
from builtins import range

browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
wait = WebDriverWait(browser, 10)

def search():
    try:
        browser.get('https://user.qzone.qq.com/1756260160/infocenter')
 
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#img_out_1756260160')))
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#fct_631386761_311_0_1503558122_0_1 > div.f-single-head.f-aside > div.user-info > div.f-nick > a')))
        return total.text
    except TimeoutException:
        return search()



def main():
    total = search() 
    # 输出 共 100 页  下正则表达式，获取数字

    print(total)

    
if __name__ == '__main__':
    main()