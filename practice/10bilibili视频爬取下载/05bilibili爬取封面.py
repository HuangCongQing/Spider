'''
Description: 爬取视频封面
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-06 13:26:47
LastEditTime: 2021-01-06 20:20:22
FilePath: /Spider/practice/10bilibili视频爬取下载/05bilibili爬取封面.py
'''
import requests
import json


def get_aid(bv):
    table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr={}
    for i in range(58):
        tr[table[i]]=i
    s=[11,10,3,8,4,6]
    xor=177451812
    add=8728348608
    r=0
    for i in range(6):
        r+=tr[bv[s[i]]]*58**i
    aid = (r-add)^xor
    return aid

def get_content(url):
    #step_1:指定url
    url = url
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url, headers=headers)
    #step_3:获取响应数据.text返回的是字符串形式的响应数据
    content = response.content
    result = json.loads(content)
    # print(content,result)
    img_link  = result['data']['pic']
    print(img_link) # http://i2.hdslb.com/bfs/archive/e4c22d45b5c9832d66c3e6baedcf4a17c9e28191.png
    
if __name__ == "__main__":
    bv = "BV194411G72j"
    aid = get_aid(bv)
    url = 'https://api.bilibili.com/x/web-interface/view?aid=' + str(aid)
    get_content(url) # 得到单个视频封面
    print('爬取数据结束！！！')