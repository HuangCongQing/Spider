'''
Description:  参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=38
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-10 16:47:28
FilePath: /Spider/package/1request-advanced/03代理操作.py
'''
#需求：
import requests
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

# page_text = requests.get(url=url,headers=headers).text # 不使用代理  
# 本机IP: 124.202.215.98北京市北京 鹏博士
page_text = requests.get(url=url,headers=headers,proxies={"http":'58.220.95.34:10174	'}).text  # 使用代理

with open('ip.html','w',encoding='utf-8') as fp:
    fp.write(page_text)

#反爬机制：  封ip
#反反爬策略：使用代理进行请求发送