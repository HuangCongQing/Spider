'''
Description: python 爬虫如何获取js里面的内容  ,参考：https://blog.csdn.net/hanchaobiao/article/details/73150405
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 19:20:17
LastEditTime: 2021-01-15 19:22:19
FilePath: /Spider/文件操作/json/02获取js里面的内容.py
'''
# 在编写爬虫软件获取所需内容时可能会碰到所需要的内容是由javascript添加上去的 在获取的时候为空 
# 比如我们在获取新浪新闻的评论数时使用普通的方法就无法获取

import requests
import json

comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fyfzhac1650783')
comments.encoding = 'utf-8'
print(comments)
jd = json.loads(comments.text.strip('var data=')) #移除改var data=将其变为json数据
print(jd['result']['count']['total'])  # 58