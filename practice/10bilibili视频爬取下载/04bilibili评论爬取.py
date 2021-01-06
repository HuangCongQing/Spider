'''
Description:   参考：https://blog.csdn.net/qq_44861455/article/details/105642871
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-06 10:21:09
LastEditTime: 2021-01-06 10:22:36
FilePath: /Spider/10bilibili视频爬取下载/04bilibili评论爬取.py
'''
import requests
from bs4 import BeautifulSoup
import json
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#视频id
oid = 36613746
#评论页数
pn = 1
#排序种类 0是按时间排序 2是按热度排序
sort = 2

while True:
    url =f'https://api.bilibili.com/x/v2/reply?pn={pn}&type=1&oid={oid}&sort={sort}'
    reponse = requests.get(url,headers=headers)
    a = json.loads(reponse.text)
    if pn==1:
        count = a['data']['page']['count']
        size = a['data']['page']['size']
        page = count//size+1
        print(page)
    for b in a['data']['replies']:
        print(b['content']['message'])
        print('-'*10)
    if pn!=page:
        pn += 1
    else:
        break
