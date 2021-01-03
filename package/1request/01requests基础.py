'''
Description:   https://www.bilibili.com/video/BV1Yh411o7Sz?p=5
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-03 16:18:41
FilePath: /Spider/package/1request/01request基础.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#- 需求：爬取搜狗首页的页面数据
import requests
if __name__ == "__main__":
    #step_1:指定url
    url = 'https://www.sogou.com/'
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #step_3:获取响应数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    #step_4:持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')
