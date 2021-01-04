'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-04 10:28:13
FilePath: /Spider/package/3xpath/05xpath解析基础.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from lxml import etree
if __name__ == "__main__":
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    r = tree.xpath('/html/body/div')   #  3个Element对象 [<Element div at 0x7fcb3819b4c8>, <Element div at 0x7fcb3819b5c8>, <Element div at 0x7fcb3819b608>]
    # r = tree.xpath('/html//div') # 等价于上面/html/body/div
    # r = tree.xpath('//div')  #  # 等价于上面
    # r = tree.xpath('//div[@class="song"]')
    # r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
    r = tree.xpath('//li[7]//text()') # ['度蜜月']
    # r = tree.xpath('//div[@class="tang"]//text()')
    # r = tree.xpath('//div[@class="song"]/img/@src')

    print(r)
