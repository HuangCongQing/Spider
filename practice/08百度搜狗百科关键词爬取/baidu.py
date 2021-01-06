'''
Description:  百度关键词爬取  https://www.yuque.com/huangzhongqing/spider/zpdk9z
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-12-28 10:05:14
LastEditTime: 2020-12-30 09:59:55
FilePath: /Spider/08百度搜狗百科关键词爬取/baidu.py
'''
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup


def baike( word ) :
       def test_url( soup ) :      		# 检测是否收录该词条，返回 True or False
              result = soup.find( text=re.compile("百度百科未收录该词条") )
              if result :
                     return False
              else:
                     return True

       def summary( soup ) :
              # h1标签的文本（百科的主标题）
              word = soup.h1.text   # 此处word含义转变 , 不要弄混
              # h2标签的文本（百科的副标题）
              if soup.h2 :
                     word += soup.h2.text

              print( word )

               #（百科的简介）
              if soup.find( class_="lemma-summary" ) : 
                     print( soup.find( class_="lemma-summary" ).text )

       def start( word ):
              keyword = urllib.parse.urlencode( {"word" : word} )  	# 解析，用于组成URL
              
              response = urllib.request.urlopen( "http://baike.baidu.com/search/word?%s" % keyword )
              html = response.read()
              soup = BeautifulSoup( html , "html.parser" )

              if test_url( soup ) :
                     summary( soup )
  
       try :
              start( word )
       except AttributeError :
              print("百度百科未收录该词条")


if(__name__ == "__main__") :
       content = str( input("请输入关键词  :  ") )
       baike(content)
