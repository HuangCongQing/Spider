'''
Description: 测试
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 11:49:42
LastEditTime: 2021-01-01 11:49:57
FilePath: /Spider/test.py
'''
from selenium import webdriver

browser = webdriver.Chrome()

def search():
    browser.get('https://www.taobao.com/')

def main():
    search()

if __name__ == '__main__':    
    main()