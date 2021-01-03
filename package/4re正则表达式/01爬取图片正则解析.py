'''
Description: 参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=19
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-03 21:20:07
FilePath: /Spider/package/4re正则表达式/01爬取图片正则解析.py
'''
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == "__main__":
    #创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    url = 'https://www.qiushibaike.com/pic/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    page_text = requests.get(url=url,headers=headers).text

    ''' 
    <a class="recmd-left video" href="/article/123936592" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">
    <img src="//qiubai-video-web.qiushibaike.com/ZHVL04ZEOPBIUZ9X_hd.jpg?imageView2/1/w/150/h/112" alt="因为一件事让我在学校">

    <div class="recmd-tag">2:11</div>
    </a>
    '''
    #使用聚焦爬虫将页面中所有的糗图进行解析/提取（想要的是括号里面的(.*?)）============================================================
    ex = '<a class="recmd-left video" href=".*?" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])"><img src="(.*?)" alt.*?'
    img_src_list = re.findall(ex,page_text,re.S)
    print(img_src_list) # 匹配信息
    # for src in img_src_list:
    #     #拼接出一个完整的图片url
    #     src = 'https:'+src
    #     #请求到了图片的二进制数据
    #     img_data = requests.get(url=src,headers=headers).content
    #     #生成图片名称
    #     img_name = src.split('/')[-1]
    #     #图片存储的路径
    #     imgPath = './qiutuLibs/'+img_name
    #     with open(imgPath,'wb') as fp:
    #         fp.write(img_data)
    #         print(img_name,'下载成功！！！')


