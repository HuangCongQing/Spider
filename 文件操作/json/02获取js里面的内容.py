'''
Description: python 爬虫如何获取js里面的内容  ,参考：https://blog.csdn.net/hanchaobiao/article/details/73150405
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 19:20:17
LastEditTime: 2021-03-13 21:37:24
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

# 原始数据如下：开头多个var data=
''' 
var data={"result": {"status": {"msg": "", "code": 0}, "count": {"thread_show": 0, "qreply": 34, "qreply_show": 0, "total": 58, "show": 7}, "replydict": {}, "language": "ch", "encoding": "gbk", "top": [], "cmntlist": [{"comment_imgs": "", "code": "0", "show_loc": "1", "parent_mid": "0", "news_mid_source": "0", "layer": "0", "rank": "0", "mid": "593F88A1-DA0464CE-88C4BB08-86C-90A", "parent_nick": "", "video": "", "thread2": "", "vote": "0", "uid": "2294594312", "area": "\u6c5f\u82cf\u82cf\u5dde", "channel_source": "", "content": "\u5982\u679c\u53bb\u4e86\u88ab\u6740\uff0c\u8d23\u4efb\u81ea\u8d1f\u3002\u641e\u4e0d\u597d\u628a\u4f60\u5f04\u6210\u4e2a\u2018\u975e\u6cd5\u4f20\u6559\u7684\u2019\u3002", "nick": "2294594312", "hot": "0", "status_uid": "0", "content_ext": "None", "ip": "", "media_type": "0", "config": 

 '''