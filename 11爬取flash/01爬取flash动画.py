'''
Description: 参考：https://blog.csdn.net/fengzhiwu3/article/details/83513181
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-05 16:01:06
LastEditTime: 2021-01-05 16:07:43
FilePath: /Spider/11爬取flash/01爬取flash动画.py
'''
import requests
import os
#url = 'http://pic.baike.soso.com/p/20121204/bki-20121204204856-1238434277.jpg'
#url = 'http://demo.sc.chinaz.com//Files/DownLoad/flash2/201810/Xflash119.swf'
url = 'http://demo.sc.chinaz.com//Files/DownLoad/flash2/201810/flash6539.swf'
root = '11爬取flash'#根目录  注意修改
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):#判断根目录是否存在
        os.mkdir(root)          #建立根目录
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content) # 二进制流
            f.close()
            print('爬取成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')