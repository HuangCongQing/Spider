'''
Description: re.search
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-17 20:59:13
LastEditTime: 2021-01-17 21:01:37
FilePath: /Spider/package/4re正则表达式/re基础/search.py
'''
import re

# =====得到page_text  方式1========================
f = open("index.html","r",encoding='utf-8')
page_text = f.read()
# page_text = requests.get(url=url,headers=headers).text
print(page_text)


# =====得到page_text  方式2========================
page_text = ''' 
<a class="recmd-left video" href="/article/123936592" rel="nofollow" target="_blank" onclick="_hmt.push(['_trackEvent','web-list-video','chick'])">
<img src="//qiubai-video-web.qiushibaike.com/ZHVL04ZEOPBIUZ9X_hd.jpg?imageView2/1/w/150/h/112" alt="因为一件事让我在学校">

<div class="recmd-tag">2:11</div>
</a>
'''

# 得到herf和src的值
ex = 'href="(.*?)" rel=.*?<img src="(.*?)" alt.*?'
result = re.search(ex,page_text,re.S) # 想要的是括号里面的(.*?)============================================
print(result.group(1)) # 通过group得到更匹配的值
