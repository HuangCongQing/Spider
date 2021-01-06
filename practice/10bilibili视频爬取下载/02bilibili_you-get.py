'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 14:22:52
LastEditTime: 2021-01-06 13:15:21
FilePath: /Spider/practice/10bilibili视频爬取下载/02bilibili_you-get.py
'''
import sys
from you_get import common as you_get                #导入you-get库

# 单视频下载
directory = '/home/hcq/下载/collage'                          #设置下载目录
url = 'https://www.bilibili.com/video/BV194411G72j '      #需要下载的视频地址
sys.argv = ['you-get', '-o', directory, url, '-l']        #sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
you_get.main()

# # 自制视频列表下载
# directory = '/home/hcq/下载/collage'                          #设置下载目录
# urls = ['https://www.bilibili.com/video/BV194411G72j '   , 'https://www.bilibili.com/video/BV1Ai4y137pr?from=search', 'https://www.bilibili.com/video/BV1wi4y177qJ?from=search']   #需要下载的视频地址
# for url in urls:
#     print(url)
#     sys.argv = ['you-get', '-o', directory, url, '-l']          #sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
#     you_get.main()