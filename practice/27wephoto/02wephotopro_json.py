# -*- coding: utf-8 -*-

'''
Description: 微商数据官网：https://www.yuque.com/huangzhongqing/spider/lzl9csuyg7vz2032
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-02-25 11:40:38
LastEditTime: 2023-03-13 02:26:23
FilePath: \Spider-1\practice\27wephoto\02wephotopro_json.py
'''
import re
import requests
import json
import time
from urllib import parse
import glob
import os
from tqdm import tqdm
from datetime import datetime # 时间戳

# 全局变量~~~~~~~~~~
print("=======请根据自己需要输出以下4个问题结果(*^▽^*):========")
# 在直接回车的情况下，input函数保存的是空字符串--""
# filter1
expire_time = input("1 请输入爬取的开始日期(e.g.2023-03-10)”:")
# expire_time = '2020-4-06'
if expire_time =="":
    expire_time = int(1268379831000) # 2010-03-12 15:43:51
else:
    expire_time +=' 00:00:00.123'
    s_t = datetime.strptime(expire_time, "%Y-%m-%d %H:%M:%S.%f")  # 返回元祖
    # expire_time = int(time.mktime(s_t) * 1000)
    expire_time = int(time.mktime(s_t.timetuple()) * 1000.0 + s_t.microsecond / 1000.0)
# print()
# filter2不爬取的好友列表
no_users = input("2 请输入不爬取的好友列表(e.g. 好友名字1,好友名字2)注意：中间‘,’隔开 好友名字要完整”:")
no_users = no_users.split(',')
# filter3
is_long_term_shop = input("3 是否只提取“长期有货的商品？(Y【default】 or N)”:")
# filter4
is_sale = input("4 是否不提取“已售”？(Y【default】 or N)”:")
filter_dict = {
    'expire_time':expire_time,
    'no_users':no_users,
    'is_long_term_shop':is_long_term_shop,
    'is_sale':is_sale,
}
# print(filter_dict)



# 替换 URL 中的 query 字段 https://blog.csdn.net/qq_37144341/article/details/120993382
# url='https://xxx.cn/comments/hotflow?mid=456116456616146&max_id=123456789&count=20'
# next_page = replace_field(url, 'max_id', '987654321')
# print(next_page)
def replace_field(url, name, value):
    result = parse.urlparse(url)
    query = result.query
    query_pair = parse.parse_qs(query)
    query_pair[name] = value
    new_query = parse.urlencode(query_pair, doseq=True)
    new_parse = result._replace(query=new_query)
    new_url = parse.urlunparse(new_parse)
    return new_url

# 获取全部参数的键值组成字典 https://blog.csdn.net/weixin_43721000/article/details/117219408
def get_mapping(link):
    # 获取全部参数的键值组成字典
    result = parse.urlparse(link)
    # print(result)
    query_dict = parse.parse_qs(result.query)
    # print(query_dict)  
    # {'link_type': ['pc_home'], 'shop_id': ['_dtHtHGdM4QEUthlnddxYWF6o7rewxx7rLC_9Zig'], 'shop_name': ['朝露昙花']}
    return query_dict

def save_img(url, img_path=None):
    # print("保存图片")
    #content返回的是二进制形式的图片数据
    # text（字符串） content（二进制）json() (对象)
    create_mkdir = os.path.dirname(img_path)
    os.makedirs(create_mkdir, exist_ok=True) #新建文件
    # print(f"create_mkdir: {create_mkdir}")
    img_data = requests.get(url=url).content
    with open(img_path,'wb') as fp:
        fp.write(img_data)

# 某个好友的所有朋友圈遍历
def process_json(json_data):
    # print(json_data)
    if json_data['success'] is False:
        # print(json_data['errmsg'])
        return
    need_data = json_data['result']['items']
    num_list = len(need_data)
    id_list = []
    item_list = []
    money_list = []
    shop_list = []
    title_list = []
    imgsSrc_list = []
    print(f'商品条目：{num_list}')
    num_valid = 0
    # 遍历1个好友的朋友圈（商品）数量
    for i in tqdm(range(num_list)):
        # shop_name
        shop_name = need_data[i]['shop_name']
        # title
        title = need_data[i]['title']

        # filter 时间过期就continue
        print(type(need_data[i]['time_stamp']))
        cur_stamp = need_data[i]['time_stamp']
        print(f"时间对比  {cur_stamp} v.s. {filter_dict['expire_time']}")
        if  cur_stamp < filter_dict['expire_time']:
            print(f'!!!好友【{shop_name}】的此商品不满足时间爬取条件，已跳过')
            continue
        else:
            print(f'!!!好友【{shop_name}】的此商品满足时间爬取条件')


        # valid_shop = False
        if ("长期有货" not in title ) and  filter_dict['is_long_term_shop'] in ["", "Y"]:
            print(f'!!!好友【{shop_name}】的此商品不满足长期有货条件，已跳过')
            continue
        if ("已售"  in title ) and  filter_dict['is_sale'] in ["", "Y"]:
            print(f'!!!好友【{shop_name}】的此商品已售，已跳过')
            continue
        num_valid +=1
        # print(f'title: {title}')
        # imgsSrc(保存单独文件夹)
        imgsSrc = need_data[i]['imgsSrc']
        
        path = f'title'
        for j, src in enumerate(imgsSrc):
            # img_path = glob.glob("%s/%s.jpg"%(title,i))
            img_path = f"微商结果/{shop_name}/{i+1}({j+1}).jpg"
            # print(img_path)
            save_img(src, img_path)


        # save
        id_list.append(i+1)
        item_list.append(' ')
        money_list.append(' ')
        shop_list.append(shop_name)
        title_list.append(title)
        # imgsSrc_list.append(imgsSrc)

    print(f"满足条件【长期有货】的商品数量：{num_valid}")

    result_dict = {
        '序号': id_list,
        '物件名称': item_list,
        '价格': money_list,
        '待处理数据': title_list,
        # 'shop_name': shop_list,
        # 'imgsSrc_list': imgsSrc_list,
    }
    if len(id_list) == 0:
        print("!!!没有合法数据保存文件")
    else:
        # print(result_dict)
        shop_path = f"微商结果/{shop_name}.csv"
        save_csv(result_dict, shop_path)


def save_csv(result_dict, path):
    import pandas as pd
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame(result_dict)
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(path,index=False, sep=',', encoding = 'utf_8_sig') # fix 乱码


def get_single_page_shop_list(shop_list):
    name_id_mapping = dict()
    for i in range(len(shop_list)):
       shop_name = shop_list[i]["shop_name"]
       shop_id = shop_list[i]["shop_id"]
    #    print(f"shop_name: {str(shop_name)}")
       if shop_name in '我的相册':
            continue
       name_id_mapping[shop_name] = shop_id

    return name_id_mapping
    

def get_shop_id(url, headers, cookie):
    shop_id_list = []
    shop_name_list = []
    query_dict = get_mapping(url)
    
    response = requests.get(url=url, headers=headers,cookies = cookie)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    # 得到参数
    total_page = result['total_page']
    for i in range(total_page):
        # print(f"url: {url}")
        page_index = i+1
        url_new = replace_field(url, 'page_index', page_index)
        # print(f"url_new: {url_new}")
        response_new = requests.get(url=url, headers=headers,cookies = cookie)
        response_new.encoding = 'utf-8' 
        content_new = response_new.content
        # json格式转为字典
        result_new = json.loads(content_new)
        # print(result_new)

        name_id_mapping = get_single_page_shop_list(result_new['result']['shop_list'])
        shop_id_list += name_id_mapping.values()
        shop_name_list += name_id_mapping.keys()


    return shop_name_list, shop_id_list

def get_content(url, headers, cookie):
    #step_1:指定url
    url = url
    #step_2:发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url, headers=headers, cookies = cookie)
    response.encoding = 'utf-8' 
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    # print(result)
    process_json(result)
    # print(result['result']['items'][0]['title'])

# 需要修改cookie参数
def get_header_and_cookie():

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
    return headers, cookie


if __name__ == '__main__':
    headers, cookie = get_header_and_cookie()
    friends_link = "https://www.szwego.com/service/album/get_album_list.jsp?act=attention_enc&search_value=&page_index=1&tag_id="
    shop_name_list, shop_id_list = get_shop_id(friends_link, headers, cookie)
    # print(f"shop_id_list: {shop_id_list}")
    print(f"好友列表：{shop_name_list}")
    print(f"好友总条目：{len(shop_id_list)}")

    for i, shop_id in enumerate(shop_id_list):
        print(f"开始爬取好友 {i+1}【{shop_name_list[i]}】的数据...")
        if shop_name_list[i] in no_users:
            print(f"好友【{shop_name_list[i]}】的数据已过滤~")
            continue
        # origin_link = "https://www.szwego.com/album/personal/all?&albumId=_d4nEqZvegdnC9XAeqotJLk9reJ7Sf7C4mSZ9DUA&searchValue=&searchImg=&startDate=&endDate=&sourceId=&requestDataType="
        # query_dict = get_mapping(origin_link)
        # albumId = query_dict['albumId']
        albumId = shop_id
        url = f"https://www.szwego.com/album/personal/all?&albumId={albumId}&searchValue=&searchImg=&startDate=&endDate=&sourceId=&requestDataType="
        get_content(url, headers, cookie) #
        print(f"爬取好友【{shop_name_list[i]}】的数据结束")
    
    print('爬取结束',)