# -*- coding: utf-8 -*-
'''
Created on 2017年8月24日

@author: hasee
'''
import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
from config import *
import pymongo
# 下里面就是mongodb的东西
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

# PhantomJS引入
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# 设置PhantomJS浏览器窗口大小
browser.set_window_size(1400, 900)

# browser = webdriver.Chrome(service_args=SERVICE_ARGS) #直接用的谷歌浏览器

# 操作简单复制到一个变量代替
wait = WebDriverWait(browser, 10)


def search():
    print('正在搜索')
    try:
        browser.get('https://www.taobao.com')
        # 选出css选择器
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q')) # EC是选择条件
        )
        # 搜索按钮
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        # send_keys 输入内容
        input.send_keys(KEYWORD)
        # 点击按钮提交 
        submit.click()
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()

# 跳到下一页
def next_page(page_number):
    print('正在翻页', page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        # 下判断是不是当前页
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)

# 得到宝贝信息
def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source # 得到整页的源代码
    doc = pq(html)  # 解析html
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except Exception:
        print('存储到MONGODB失败', result)


def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        print(total)
        for i in range(2, total + 1):
            next_page(i)
    except Exception:
        print('出错啦')
    finally:
        browser.close()# 关闭浏览器

if __name__ == '__main__':
    main()