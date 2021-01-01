'''
Description: 搜狗百科本科专业信息爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-12-30 17:35:35
LastEditTime: 2021-01-01 20:30:42
FilePath: /Spider/08百度搜狗百科关键词爬取/sougou.py
'''
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
# from selenium import webdriver
# from time import sleep


def baike( word ) :
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

       def start( word ):
              keyword = urllib.parse.urlencode( {"fromTitle" : word} )  	# 解析，用于组成URL
              print(keyword)
              
              response = urllib.request.urlopen( "https://baike.sogou.com/?fromTitle=%s" % keyword )
              html = response.read()
              soup = BeautifulSoup( html , "html.parser" )
            #   print(soup)

              if test_url( soup ) :
                     summary( soup )
  
       try :
              start( word )
       except AttributeError :
              print("站内没有找到")


if(__name__ == "__main__") :
       content = str( input("请输入关键词  :  ") )
       # content = "体育旅游"
       baike(content)
