'''
Description: 爬取视频封面
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-06 13:26:47
LastEditTime: 2022-02-20 00:25:00
FilePath: /Spider/practice/10bilibili视频爬取下载/06bilibili下载视频和封面.py
'''
import requests
import json
import time
import pandas as pd
import sys
from you_get import common as you_get                #导入you-get库
import os

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

def get_content(url, path, title):
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
    #请求到了图片的二进制数据
    img_data = requests.get(url=img_link,headers=headers).content
    # #生成图片名称
    # img_name = img_link.split('/')[-1]
    #图片存储的路径
    # now_time = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
    imgPath =  path+title+'.jpg'
    with open(imgPath,'wb') as fp:
        fp.write(img_data)
        print(imgPath,'下载成功！！！')
    
if __name__ == "__main__":
    # save path
    directory = '/home/hcq/下载/collage/'
    # 1 得到url
    data = pd.read_csv('/home/hcq/python/Spider/practice/10bilibili视频爬取下载/学校视频url.csv')    
    # 遍历每行的每个元素
    for i  in range(0, len(data)):
        #  每列的表头
        print(data['school'][i], data['title'][i], data['url'][i] )
        path = directory + str(data['school'][i])+'/'
        if os.path.isdir(path):  ##不用加引号，如果是多级目录，只判断最后一级目录是否存在
            print('dir exists')
            pass
        else:
            print('dir not exists 新建文件夹：%s'%(data['school'][i]) )
            os.mkdir(path)
        # 2 下载视频 name title url
        # directory = '/home/hcq/下载/collage'                          #设置下载目录
        # url = 'https://www.bilibili.com/video/BV194411G72j '      #需要下载的视频地址
        url = data['url'][i]
        print("下载视频")
        sys.argv = ['you-get', '-o', path, url, '-l']          #sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
        you_get.main()

        # 3 下载封面 
        # bv = "BV194411G72j"
        bv = url.split('/')[-1].split('?')[0] # https://www.bilibili.com/video/BV1zK4y1s7a5?from=search
        aid = get_aid(bv)
        url = 'https://api.bilibili.com/x/web-interface/view?aid=' + str(aid)
        get_content(url, path,  data['title'][i]) # 得到单个视频封面
        print('爬取数据结束！！！')