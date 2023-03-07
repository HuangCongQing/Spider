# -*- coding: utf-8 -*-

'''
Description: 微商数据官网：https://www.yuque.com/huangzhongqing/spider/lzl9csuyg7vz2032
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-02-25 11:40:38
LastEditTime: 2023-03-02 21:11:17
FilePath: \Spider-1\practice\27微商相册\01微商相册数据爬取_json.py
'''
import re
import requests
import json
import time
from urllib import parse
import glob
import os


# 获取全部参数的键值组成字典 https://blog.csdn.net/weixin_43721000/article/details/117219408
def get_mapping(link):
    # 获取全部参数的键值组成字典
    result = parse.urlparse(link)
    query_dict = parse.parse_qs(result.query)
    # print(query_dict)  
    # {'link_type': ['pc_home'], 'shop_id': ['_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig'], 'shop_name': ['朝露昙花']}
    return query_dict

def save_img(url, img_path=None):
    print("保存图片")
    #content返回的是二进制形式的图片数据
    # text（字符串） content（二进制）json() (对象)
    create_mkdir = os.path.dirname(img_path)
    os.makedirs(create_mkdir, exist_ok=True) #新建文件
    # print(f"create_mkdir: {create_mkdir}")
    img_data = requests.get(url=url).content
    with open(img_path,'wb') as fp:
        fp.write(img_data)


def process_json(json_data):
    need_data = json_data['result']['items']
    num_list = len(need_data)
    shop_list = []
    title_list = []
    imgsSrc_list = []
    print(f'商品条目：{num_list}')
    for i in range(num_list):
        # shop_name
        shop_name = need_data[i]['shop_name']
        # title
        title = need_data[i]['title']
        print(f'title: {title}')
        # imgsSrc(保存单独文件夹)
        imgsSrc = need_data[i]['imgsSrc']
        
        path = f'title'
        for j, src in enumerate(imgsSrc):
            # img_path = glob.glob("%s/%s.jpg"%(title,i))
            img_path = f"微商结果/{shop_name}/{i}({j}).jpg"
            print(img_path)
            save_img(src, img_path)


        # save
        shop_list.append(shop_name)
        title_list.append(title)
        imgsSrc_list.append(imgsSrc)

    result_dict = {
        'shop_name': shop_list,
        'title': title_list,
        'imgsSrc_list': imgsSrc_list,
    }
    print(result_dict)
    save_csv(result_dict, shop_name)


def save_csv(result_dict, name):
    import pandas as pd
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame(result_dict)
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(f"{name}.csv",index=False, sep=',')
    print('爬取结束',)


def get_content(url):
    #step_1:指定url
    url = url
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    # 重庆
    # cookie = {
    #     'JSESSIONID':'F56D575920B79C65D889F6F363B34273',
    #     'client_type':'net',
    #     'sajssdk_2015_cross_new_user': '1',
    #     'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig%22%2C%22first_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJfZHRIdEhHZE00UUVVdGhsbmRkeFlXRjZvN3Jld3h4N3JMQ185WmlnIiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4Njg2YWVkNzE3MTQxLTAyNTc5NGFmMDU2ODZmYy0xYTM0MzM3MC0xODIxMzY5LTE4Njg2YWVkNzE4NGEzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig%22%7D%2C%22%24device_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%7D',
    #     'token':'RjBFMkJCRDE4RDY4MkMxN0JBNDU2OUEwMjgwQTBEOUIwNkYzNzkwMEYwMjYyN0U0NzgzREVDRkY0RkJCN0U2ODY4NDBBNkI1N0JCNzhFOERFMTFCQzFDRTFEMTM0QTQ3',
    # }
    
    # 木兰
    cookie = {
        'client_type':'net',
        'token':'QjMzNTRFRUEwQ0Q2RTY0N0MzQUJFNUIzNDEyRUE3MzJGRTM1NDU1OURCMjBBMkVBRDZBMTY1MDIyRkM1RTU2OTg4ODMxMzcyMTExRUU2MkMyRTc0MTE5NjNCN0UyOERD',
        'sensorsdata2015jssdkcross':'%7B%22distinct_id%22%3A%22_dEqEqzcXuSZl5l_P3LLyeOwYEcLKbDZESq6m8Kw%22%2C%22first_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJfZEVxRXF6Y1h1U1psNWxfUDNMTHllT3dZRWNMS2JEWkVTcTZtOEt3IiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4Njg2YWVkNzE3MTQxLTAyNTc5NGFmMDU2ODZmYy0xYTM0MzM3MC0xODIxMzY5LTE4Njg2YWVkNzE4NGEzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22_dEqEqzcXuSZl5l_P3LLyeOwYEcLKbDZESq6m8Kw%22%7D%2C%22%24device_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%7D',
        'JSESSIONID':'3A026131D634371909427EBBD8B8ABDB',
    }
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url, headers=headers,cookies = cookie)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    # print(result)
    process_json(result)
    # print(result['result']['items'][0]['title'])


if __name__ == '__main__':
    origin_link = 'https://www.szwego.com/static/index.html?link_type=pc_home&shop_id=_dEqtHpPum5ywvAWXHH64sJhn25MKYbDTwnABNWQ&shop_name=%E5%A4%AA%E6%B4%8B#/album_home'
    query_dict = get_mapping(origin_link)
    shop_id =query_dict['shop_id'] # '_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig'
    shop_name = query_dict['shop_id'] #  '%25E6%259C%259D%25E9%259C%25B2%25E6%2598%2599%25E8%258A%25B1'
    url=f"https://www.szwego.com/album/moments?searchValue=&searchImg=&noCache=0&requestDataType=&link_type=pc_home&shop_id={shop_id}&shop_name={shop_name}"
    get_content(url) #