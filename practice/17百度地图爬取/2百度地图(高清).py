'''
Description:  参考：https://www.jianshu.com/p/ade4c6fc9c55
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-27 20:36:15
LastEditTime: 2021-01-27 20:43:25
FilePath: /Spider/practice/17百度地图爬取/2百度地图.py
'''

import requests
import re
import time
import os
import urllib.parse
from lxml import etree
import json
page_num=30
photo_dir="practice/17百度地图爬取/imgs"


def getDetailImage(word):
    num=0
    url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={0}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={0}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={1}&rn="+str(page_num)+"&gsm=1e&1552975216767="
    while num<2:
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        page_url=url.format(urllib.parse.quote(word),num*page_num)
        print(page_url)
        response=requests.get(url=page_url,headers=headers,allow_redirects=False)
       
        regex = re.compile(r'\\(?![/u"])')
        json_data=json.loads(regex.sub(r"\\\\", response.text))#问题在于编码中是\xa0之类的，当遇到有些 不用转义的\http之类的，则会出现以上错误
        for item in json_data['data']:
            try :
                params={
                    "word":word,
                    "di":item['di'],
                    "tn":"baiduimagedetail",
                    "cs":item['cs'],
                    "os":item['os'],
                }
                detail_url="http://image.baidu.com/search/detail"
                response=requests.get(detail_url,params=params)
                selector = etree.HTML(response.text)
                pic_url=selector.xpath("//img[@id='hdFirstImgObj']/@src")[0]
                print(pic_url)
                name=pic_url.split('/')[-1]
                headers={
                    "Referer":page_url,
                }
            
                html=requests.get(pic_url,headers=headers)
                print(html)
                with open(os.path.join(word_dir,name),'wb')as f:
                    f.write(html.content)
            except:
                pass
            
        num=num+1
        

if __name__ == "__main__":
    word = '挡风玻璃'
    word_dir=os.path.join(photo_dir,word)
    if not os.path.exists(word_dir):
        os.mkdir(word_dir)
    getDetailImage(word)
    
                

