'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 20:46:02
LastEditTime: 2021-01-01 21:38:42
FilePath: /Spider/08百度搜狗百科关键词爬取/sougou_selenium.py
'''
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

from selenium import webdriver
from time import sleep


def test_url( soup ) :      		# 检测是否收录该词条，返回 True or False
        result = soup.find( text=re.compile("站内没有找到") )
        print("result: ", result)
        if result :
                print("站内没有找到 ")
                return False
        else:
                return True

def summary( soup ) :
        print(soup.h1.text)
        # h1标签的文本（百科的主标题）
        word = soup.h1.text   # 此处word含义转变 , 不要弄混
        # h2标签的文本（百科的副标题）
        if soup.h1 :
                word += soup.h1.text

        print( word )

        #（百科的简介）
        if soup.find( class_="abstract_main" ) : 
                print( soup.find( class_="abstract_main" ).text )



bro = webdriver.Chrome(executable_path='/home/hcq/python/Spider/package/4selenium/chromedriver')

bro.get('https://baike.sogou.com//')

#标签定位
search_input = bro.find_element_by_id('searchText')
#标签交互
search_input.send_keys('体育旅游')
#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn_enter')
btn.click()
sleep(2)
element = bro.find_elements_by_link_text("中国普通高等学校本科专业")[0]
element.click()
# 中国普通高等学校本科专业


# #page_source获取浏览器当前页面的页面源码数据=========================
page_text = bro.page_source
print(page_text)
sleep(3)
bro.quit()


# 处理网页
html = page_text
soup = BeautifulSoup( html , "html.parser" )
print(soup)

if test_url( soup ) :
        summary( soup )



