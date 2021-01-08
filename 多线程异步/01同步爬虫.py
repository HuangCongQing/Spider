'''
Description:  
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-08 23:22:26
FilePath: /Spider/多线程异步/01同步爬虫.py
'''
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
urls = [
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar',  # 网站失效重新换
    'http://zjlt.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10229.rar',
    'http://xmdx.sc.chinaz.net/Files/DownLoad/jianli/201904/jianli10231.rar'
]

def get_content(url):
    print('正在爬取：',url)
    #get方法是一个阻塞的方法
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200 :
        return response.content

def parse_content(content):
    print('响应数据的长度为：',len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)