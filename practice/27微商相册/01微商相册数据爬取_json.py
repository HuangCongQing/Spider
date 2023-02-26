# -*- coding: utf-8 -*-

'''
Description: 微商数据官网：https://www.yuque.com/huangzhongqing/spider/lzl9csuyg7vz2032
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-02-25 11:40:38
LastEditTime: 2023-02-27 00:45:22
FilePath: \Spider-1\practice\27微商相册\01微商相册数据爬取_json.py
'''
import re
import requests
import json
import time
from urllib import parse


def get_mapping(link):
    pass
    return 

def get_content(url):
    #step_1:指定url
    url = url
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    cookie = {
        'JSESSIONID':'F56D575920B79C65D889F6F363B34273',
        'client_type':'net',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig%22%2C%22first_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJfZHRIdEhHZE00UUVVdGhsbmRkeFlXRjZvN3Jld3h4N3JMQ185WmlnIiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4Njg2YWVkNzE3MTQxLTAyNTc5NGFmMDU2ODZmYy0xYTM0MzM3MC0xODIxMzY5LTE4Njg2YWVkNzE4NGEzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig%22%7D%2C%22%24device_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%7D',
        'token':'RjBFMkJCRDE4RDY4MkMxN0JBNDU2OUEwMjgwQTBEOUIwNkYzNzkwMEYwMjYyN0U0NzgzREVDRkY0RkJCN0U2ODY4NDBBNkI1N0JCNzhFOERFMTFCQzFDRTFEMTM0QTQ3',
    }
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url, headers=headers,cookies = cookie)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    # print(result)
    print(result['result']['items'][0]['title'])


if __name__ == '__main__':
    origin_link = 'https://www.szwego.com/static/index.html?link_type=pc_home&shop_id=_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig&shop_name=%E6%9C%9D%E9%9C%B2%E6%98%99%E8%8A%B1#/album_home'
    map_dict = get_mapping(origin_link)
    shop_id = '_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig'
    shop_name = '%25E6%259C%259D%25E9%259C%25B2%25E6%2598%2599%25E8%258A%25B1'
    url=f"https://www.szwego.com/album/moments?searchValue=&searchImg=&noCache=0&requestDataType=&link_type=pc_home&shop_id={shop_id}&shop_name={shop_name}"
    get_content(url) #