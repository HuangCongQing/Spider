'''
Description: re.findall 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-17 19:50:56
LastEditTime: 2021-01-17 20:58:49
FilePath: /Spider/package/4re正则表达式/re基础/findall.py
'''

# 下面代码块来自于： package/4re正则表达式/01爬取图片正则解析.py


import requests
import re

# =====得到page_text  方式1========================
# f = open("index.html","r",encoding='utf-8')
# page_text = f.read()
# # page_text = requests.get(url=url,headers=headers).text
# print(page_text)


# =====得到page_text  方式2========================
page_text = ''' 
<a class="recmd-left video" href="/article/123936592" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">
<img src="//qiubai-video-web.qiushibaike.com/ZHVL04ZEOPBIUZ9X_hd.jpg?imageView2/1/w/150/h/112" alt="因为一件事让我在学校">

<div class="recmd-tag">2:11</div>
</a>
'''
#使用聚焦爬虫将页面中所有的糗图进行解析/提取（想要的是括号里面的(.*?)）============================================================
ex = '<img src="(.*?)" alt.*?'
img_src_list = re.findall(ex,page_text,re.S) # 想要的是括号里面的(.*?)============================================
print(img_src_list)  # ['//qiubai-video-web.qiushibaike.com/ZHVL04ZEOPBIUZ9X_hd.jpg?imageView2/1/w/150/h/112']
print(img_src_list[0])   # //qiubai-video-web.qiushibaike.com/ZHVL04ZEOPBIUZ9X_hd.jpg?imageView2/1/w/150/h/112
