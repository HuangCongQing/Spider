'''
Description: 搜狗百科本科专业信息爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-12-30 17:35:35
LastEditTime: 2020-12-30 18:10:19
FilePath: /Spider/08百度搜狗百科关键词爬取/sougou.py
'''

'''
Description:  百度关键词爬取  https://www.yuque.com/huangzhongqing/spider/zpdk9z
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-12-28 10:05:14
LastEditTime: 2020-12-30 18:03:02
FilePath: /Spider/08百度搜狗百科关键词爬取/baidu.py
'''
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup


def baike( word ) :
       def test_url( soup ) :      		# 检测是否收录该词条，返回 True or False
              result = soup.find( text=re.compile("站内没有找到") )
              # print("result: ", result)
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
              keyword = urllib.parse.urlencode( {"word" : word} )  	# 解析，用于组成URL
              
              response = urllib.request.urlopen( "https://baike.sogou.com/v321023.htm?fromTitle=%s" % keyword )
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
       baike(content)
