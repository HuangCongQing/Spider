'''
Description: 爬取图片 参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=17
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 20:39:03
LastEditTime: 2021-01-03 20:47:42
FilePath: /Spider/package/4re正则表达式/00爬取图片.py
'''


#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
if __name__ == "__main__":
    #如何爬取图片数据
    url = 'https://pic.qiushibaike.com/system/pictures/12172/121721055/medium/9OSVY4ZSU4NN6T7V.jpg'
    #content返回的是二进制形式的图片数据
    # text（字符串） content（二进制）json() (对象)
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg','wb') as fp:
        fp.write(img_data)