# -*- coding: utf-8 -*-

'''
Description: 微商数据官网：https://www.yuque.com/huangzhongqing/spider/lzl9csuyg7vz2032
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-02-25 11:40:38
LastEditTime: 2023-07-04 18:44:27
FilePath: /lmv/home/chongqinghuang/Downloads/02wephotopro_json.py
'''

import re
import requests
import json
import time
from urllib import parse
import os
from tqdm import tqdm
import datetime # 时间戳
import random # 随机选择headers


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
    create_mkdir = os.path.dirname(img_path) # 目录
    os.makedirs(create_mkdir, exist_ok=True) #新建文件
    # print(f"create_mkdir: {create_mkdir}")
    # fix:requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer'))
    # 我的问题我使用 requests库进行请求，可能是没有限制频率睡眠，导致出错
    nums_circle = 10
    for i in range(nums_circle):
        try:
            headers, cookie = get_header_and_cookie()
            img_data = requests.get(url=url, headers=headers, cookies=cookie).content
            # print(f'保存图片目录：{img_path}')
            with open(img_path,'wb') as fp:
                fp.write(img_data)
            # 
            break
        except Exception as e:
            print(f"[{i+1}]尝试重新连接【INFO：{e}】")
            if i == nums_circle-1:
                print(f"此图片（{url}）不下载，跳过~")

            if i < nums_circle:
                time.sleep(0.5)
    # time.sleep(0.2)
    # old
    # headers, cookie = get_header_and_cookie()
    # img_data = requests.get(url=url, headers=headers, cookies=cookie).content
    # with open(img_path,'wb') as fp:
    #     fp.write(img_data)

# 输入毫秒级的时间，转出正常格式的时间
# https://blog.csdn.net/qq_38486203/article/details/80239762
# 13位是毫秒时间戳
# 10位是秒时间戳。
def timeStamp(timeNum):
    timeStamp = float(int(timeNum)/1000)
    timeArray = time.localtime(timeStamp)
    # otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    # print(f'年月日时间戳{otherStyleTime}')
    return otherStyleTime

def validateTitle(filename):
    # 去除空格 \r ]n
    filename.replace(' ','').replace('\n', '_').replace('\r', '').strip()
    filename = '_'.join(filename.split()) # 多行字符串转换为单行字符串
    # 非法字符
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    filename = re.sub(rstr, "_", filename)  # 替换为下划线
    # 处理中文标点符号
    punctuation = """！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
    re_punctuation = "[{}]+".format(punctuation)
    filename = re.sub(re_punctuation, "", filename)
    # 表情替换
    p = re.compile(u'['u'\U0001F300-\U0001F64F' u'\U0001F680-\U0001F6FF' u'\u2600-\u2B55 \U00010000-\U0010ffff]+')
    filename = re.sub(p,'',filename) # 正则匹配，将表情符合替换为空''
    # 返回
    return filename

# 某个好友的所有朋友圈遍历
def process_json(json_data, cur_items, **kargs):
    num = kargs['num']
    # print(json_data)
    if json_data['success'] is False:
        # print(json_data['errmsg'])
        return
    need_data = json_data['result']['items']
    num_list = len(need_data)
    id_list = []
    item_list = []
    money_list = []
    # shop_list = []
    title_list = []
    time_list = []

    if num_list == 0:
        return id_list, item_list, money_list, title_list, time_list
    print(f'>>>page{num+1}商品条目：{num_list}') # 
    num_valid = 0
    # 遍历1个好友的朋友圈（商品）数量
    print(f"要爬取当前pages的商品数量：{num_list}")
    for i in tqdm(range(num_list)):
        # shop_name
        shop_name = need_data[i]['shop_name']
        # title
        title = need_data[i]['title']

        # filter 时间过期就continue
        # print(type(need_data[i]['time_stamp']))
        cur_stamp = need_data[i]['time_stamp']
        cur_tag = None
        if 'tags' in need_data[i].keys():
            cur_tag = need_data[i]['tags'][0]['tagName'] 
        cur_time = timeStamp(cur_stamp)
        # # print(f"时间对比  {cur_stamp} v.s. {filter_dict['start_date']}")
        # if  cur_stamp < filter_dict['start_date']:
        #     print(f'!!!好友【{shop_name}】的此商品不满足时间爬取条件，已跳过')
        #     continue
        # else:
        #     print(f'!!!好友【{shop_name}】的此商品满足时间爬取条件')


        # valid_shop = False
        # if  ("货号A" not in title ):
        #     continue # 不下载
        # if  ("寿山石" in title ):
        #     continue
        # if  ("成批" in title ):
        #     continue
        # if ("长期有货" not in title ) and  filter_dict['is_long_term_shop'] in ["", "Y"]:
        #     print(f'!!!好友【{shop_name}】的此商品不满足长期有货条件，已跳过')
        #     continue
        # if ("已售"  in title or "已出" in title  or "售出" in title  or "售完" in title ) and  filter_dict['is_sale'] in ["", "Y"]:
        #     print(f'!!!好友【{shop_name}】的此商品已售/已出/售出/售完，已跳过')
        #     continue

        # 包含筛选
        if filter_dict['is_include'] == '':
            pass
        elif  all([w not in title and w for w in filter_dict['is_include'].split('，')]) :
            print("不满足【必须包含】条件")
            continue
        # 不包含筛选
        if filter_dict['is_no_include'] == '':
            pass
        elif  all([w in title and w for w in filter_dict['is_no_include'].split('，')]):
            print("不满足【不能包含】条件")
            continue
        
        if filter_dict['select_tags'] == '':
            pass
        elif (cur_tag not in select_tags):
            print(f'!!!tag[{cur_tag}]不满足【{select_tags}】条件，已跳过')
            continue
        
        # 金额筛选
        if filter_dict['select_money'] == '':
            pass
        else:
            # 匹配格式（当前匹配 元|个|件）
            Regx = re.compile("(([1-9]\\d*[\\d,，]*\\.?\\d*)|(0\\.[0-9]+))(/|元|个|件|百万|万元|亿元|万|亿)")
            match_result =  Regx.search(title)
            get_money = -1
            if match_result != None:
                get_money = float(re.findall("\d+",match_result.group())[0])
            min_money = float(filter_dict['select_money'][0])
            max_money = float(filter_dict['select_money'][1])
            need_flag = (get_money >= min_money) and (get_money <= max_money)
            if get_money == -1:
                    print(f'!!!没有匹配到金额[{get_money}]，请询问开发人员（黄重庆）匹配建议，已跳过')
                    continue
            elif not need_flag:
                    print(f'!!!金额[{get_money}]不满足【{min_money}~{max_money}】条件，已跳过')
                    continue

        # print(f'tag:{cur_tag}')
        num_valid +=1
        # print(f'title: {title}')
        # imgsSrc(保存单独文件夹)
        imgsSrc = need_data[i]['imgsSrc']
        # 序号
        sequence_number = num_valid + cur_items
        print(f"序号：{sequence_number}({cur_time})")
        
        # path = f'title'
        for j, src in enumerate(imgsSrc):
            # img_path = glob.glob("%s/%s.jpg"%(title,i)).
            filename = title
            # print(f"start: {filename}")
            filename =  validateTitle(filename) # 
            # print(f"end: {filename}")
            # img_path = f"微商结果/{shop_name}/{start_date}~{end_date}/img/{sequence_number}_{filename}_({j+1}).jpg"
            img_path = f"微商结果/{shop_name}/{start_date}~{end_date}/img/{sequence_number}({j+1}).jpg"
            # print(img_path)
            if not os.path.isfile(img_path):
                save_img(src, img_path)
            else:
                print("图片已下载过，跳过~")


        # save
        id_list.append(sequence_number)
        item_list.append(' ')
        money_list.append(' ')
        # shop_list.append(shop_name)
        title_list.append(title)
        # imgsSrc_list.append(imgsSrc)
        time_list.append(cur_time)

    print(f"满足当前日期所有条件的商品数量：{num_valid}")

    # result_dict = {
    #     '序号': id_list,
    #     '物件名称': item_list,
    #     '价格': money_list,
    #     '待处理数据': title_list,
    #     # 'shop_name': shop_list,
    #     # 'imgsSrc_list': imgsSrc_list,
    # }
    return id_list, item_list, money_list, title_list, time_list
    # return result_dict


def save_csv(result_dict, path):
    import pandas as pd
    from pandas.io.excel import ExcelWriter
    import os
    
    create_mkdir = os.path.dirname(path)
    os.makedirs(create_mkdir, exist_ok=True) #新建文件
    # 保存csv文件
    print(f'保存文件(path: {path})...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame(result_dict)
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    if path.split('.')[-1] == 'csv':
        dataframe.to_csv(path, index=False, sep=',', encoding = 'utf_8_sig') # fix 乱码
    elif path.split('.')[-1] == 'xlsx':
        dataframe.to_excel(path, sheet_name="data", index=False) # fix 乱码
    else:
        raise Exception("No match file!")
    # # 转excel
    # name = os.path.split(path)[1].split('.')[0]
    # excel_path = os.path.join(os.path.split(path)[0], f"{name}.xlsx")
    # with ExcelWriter(excel_path) as ew:
    #     #将csv文件转换为excel文件
    #     pd.read_csv(path).to_excel(ew, sheet_name="data", index=False)
    #     print(f"保存路径: {excel_path}")
    # os.remove(path) # 删除csv文件




def get_single_page_shop_list(shop_list):
    name_id_mapping = dict()
    total_goods = []
    for i in range(len(shop_list)):
       shop_name = shop_list[i]["shop_name"]
       shop_id = shop_list[i]["shop_id"]
    #    print(f"shop_name: {str(shop_name)}")
       if shop_name in '我的相册':
            continue
       name_id_mapping[shop_name] = shop_id
       total_goods.append(shop_list[i]["total_goods"])

    return name_id_mapping, total_goods
    

def get_shop_id(url, headers, cookie):
    shop_id_list = []
    shop_name_list = []
    total_goods_list = []
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

        name_id_mapping, total_goods = get_single_page_shop_list(result_new['result']['shop_list'])
        shop_id_list += name_id_mapping.values()
        shop_name_list += name_id_mapping.keys()
        total_goods_list += total_goods


    return shop_name_list, shop_id_list, total_goods_list

# post请求
# def get_content(url, headers, cookie, method = 'post',**kargs):
#     #step_1:指定url
#     url = url
#     #step_2:发起请求
#     #get方法会返回一个响应对象
#     # response = requests.get(url=url, headers=headers, cookies = cookie)
#     response = eval(f"requests.{method}")(url=url, headers=headers, cookies = cookie)
    
#     response.encoding = 'utf-8' 
#     content = response.content
#     # json格式转为字典
#     result = json.loads(content)
#     # print(result)
#     process_json(result, **kargs)
#     # print(result['result']['items'][0]['title'])

# 需要修改cookie参数
def get_header_and_cookie():

    #UA伪装：将对应的User-Agent封装到一个字典中
    # headers = {
    #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    # }
    
    UserAgent_List = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    ]

    
    headers = {
        'user-agent': random.choice(UserAgent_List),
        'authority': 'www.szwego.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,de;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.szwego.com',
        'referer': 'https://www.szwego.com/static/index.html?t=1660503705068',
        'wego-albumid': '',
        'wego-channel': 'net',
        'wego-staging': '0',
        'wego-uuid': '',
        'wego-version': '',
        'x-requested-with': 'XMLHttpRequest',
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
        'client_type': 'net',
        'token': 'QjMzNTRFRUEwQ0Q2RTY0N0MzQUJFNUIzNDEyRUE3MzJGRTM1NDU1OURCMjBBMkVBRDZBMTY1MDIyRkM1RTU2OTg4ODMxMzcyMTExRUU2MkMyRTc0MTE5NjNCN0UyOERD',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22_dEqEqzcXuSZl5l_P3LLyeOwYEcLKbDZESq6m8Kw%22%2C%22first_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfbG9naW5faWQiOiJfZEVxRXF6Y1h1U1psNWxfUDNMTHllT3dZRWNMS2JEWkVTcTZtOEt3IiwiJGlkZW50aXR5X2Nvb2tpZV9pZCI6IjE4Njg2YWVkNzE3MTQxLTAyNTc5NGFmMDU2ODZmYy0xYTM0MzM3MC0xODIxMzY5LTE4Njg2YWVkNzE4NGEzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22_dEqEqzcXuSZl5l_P3LLyeOwYEcLKbDZESq6m8Kw%22%7D%2C%22%24device_id%22%3A%2218686aed717141-025794af05686fc-1a343370-1821369-18686aed7184a3%22%7D',
        'producte_run_to_dev_tomcat': '',
        'JSESSIONID': '3A026131D634371909427EBBD8B8ABDB',
    }
    return headers, cookie



def findPage(data):
    return data["result"]["pagination"]["pageTimestamp"]


def findLoadMore(data):
    return data["result"]["pagination"]["isLoadMore"]

def createParams(alb: str, page: str, start_date: str, end_date:str):
    if page == '':
        params = {
            'albumId': f'{alb}',
            'searchValue': '',
            'searchImg': '',
            'startDate': f'{start_date}',
            # 'endDate': f'{datetime.date.today().strftime("%Y-%m-%d")}',
            'endDate': f'{end_date}',
            'sourceId': '',
            'requestDataType': '',
            'transLang': 'en'
        }
    else:
        params = {
            'albumId': f'{alb}',
            'searchValue': '',
            'searchImg': '',
            'startDate': f'{start_date}',
            'endDate': f'{end_date}', # f'{datetime.date.today().strftime("%Y-%m-%d")}',
            'sourceId': '',
            'slipType': '1',
            'timestamp': f'{page}',
            'requestDataType': '',
            'transLang': 'en'
        }
    return params


def createData(tag):
    data = {
        'tagList': f"[{tag}]"
    }
    return data



def download_json(alb, page, start_date, end_date):
    headers, cookies= get_header_and_cookie()
    params = createParams(alb, page, start_date,end_date)
    data = createData('')
    url = 'https://www.szwego.com/album/personal/all'
    resp = requests.post(url, headers=headers, params=params, data=data, cookies=cookies)
    return resp.json()

def update_dict(result_dict, id_list, item_list, money_list, title_list, time_list):
    # result_dict = {
    #     '序号': [],
    #     '物件名称': [],
    #     '价格': [],
    #     '待处理数据': [],
    #     # 'shop_name': shop_list,
    #     # 'imgsSrc_list': imgsSrc_list,
    # }
    if len(id_list) == 0:
        return
    result_dict['序号'] += id_list
    result_dict['物件名称'] += item_list
    result_dict['价格'] += money_list
    result_dict['待处理数据'] += title_list
    result_dict['日期'] +=time_list


if __name__ == '__main__':
    headers, cookie = get_header_and_cookie()
    # 朋友圈API
    friends_link = "https://www.szwego.com/service/album/get_album_list.jsp?act=attention_enc&search_value=&page_index=1&tag_id="
    shop_name_list, shop_id_list, total_goods = get_shop_id(friends_link, headers, cookie)
    # print(f"shop_id_list: {shop_id_list}")
    print(f"好友列表：{shop_name_list}")
    print(f"好友总条目：{len(shop_id_list)}")

    
    loca=time.strftime('%Y-%m-%d') # 
    # loca=time.strftime('%Y-%m-%d-%H-%M-%S')

    # 全局变量~~~~~~~~~~
    print("=======请根据自己需要输出以下几个个问题结果(*^▽^*):========")
    # 在直接回车的情况下，input函数保存的是空字符串--""
    # filter1
    start_date = input("1.1 请输入爬取的开始日期(e.g.2023-03-10)”:")
    end_date = input("1.2 请输入爬取的结束日期(e.g.2023-04-06)”:")
    # start_date = '2020-4-06'
    if start_date =="":
        # start_date = int(1268379831000) # 2010-03-12 15:43:51
        start_date = '2010-03-12' # 2010-03-12 15:43:51
    if end_date =="":
        # end_date = int(1268379831000) # 2010-03-12 15:43:51
        end_date = f'{datetime.date.today().strftime("%Y-%m-%d")}'
    # else:
    #     start_date +=' 00:00:00.123'
    #     s_t = datetime.datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S.%f")  # 返回元祖
    #     # start_date = int(time.mktime(s_t) * 1000)
    #     start_date = int(time.mktime(s_t.timetuple()) * 1000.0 + s_t.microsecond / 1000.0)
    # print()
    # filter2不爬取的好友列表
    no_users = input("2.1 请输入不爬取的好友列表(e.g. 好友名字1,好友名字2) 注意：中间‘，’隔开 好友名字要完整”:")
    no_users = no_users.split('，')
    if not (set(no_users).issubset(set(shop_name_list))) and no_users[0] != '':
        raise ValueError(f'{no_users} 不包含在好友列表里！')
    print(f"不爬取的好友列表：{no_users}")
    yes_users = input("2.2 请输入要爬取的好友列表(e.g. 好友名字1,好友名字2) 若直接回车，则默认下载所有。注意：中间‘，’隔开 好友名字要完整”:")
    yes_users = yes_users.split('，')
    if not (set(yes_users).issubset(set(shop_name_list))) and yes_users[0] != '':
        raise ValueError(f'{yes_users} 不包含在好友列表里！')
    print(f"要爬取的好友列表：{yes_users}")
    # # filter3
    # is_long_term_shop = input("3 是否只提取“长期有货”的商品？(Y【default】 or N)”:")
    # # filter4
    # is_sale = input("4 是否不提取“已售/已出/售出/售完”？(Y【default】 or N)”:")
    # filter3
    is_include = input("3 请输入必须包含的文字列表(e.g. 货号A) 若直接回车，则默认不筛选。注意：中间‘，’隔开:")
    
    print(f"必须包含的文字列表：{is_include}")
    # filter4
    is_no_include = input("4 请输入不能包含的文字列表(e.g. 寿山石，成批，已售，已出，售出，售完) 若直接回车，则默认不筛选。注意：中间‘，’隔开:")
    print(f"不能包含的文字列表：{is_no_include}")
    # 金额大小
    select_money = input("5 请输入价格区间(e.g. 10，300) 若直接回车，则默认不筛选：")
    if select_money != '':
        select_money = select_money.split('，')
        print(f"价格曲线：{select_money}")
        assert len(select_money) == 2, f"不符合要求:{select_money}，请注意，是中文下的逗号"
    # 
    select_tags = input("6 请输入筛选的分类名tag(e.g. 长期有货，已售完) 若直接回车，则默认不筛选：")
    print(f"筛选tag：{select_tags}")
    if select_tags != '':
        select_tags = select_tags.split('，')
    filter_dict = {
        'start_date':start_date,
        'end_date':end_date,
        'no_users':no_users,
        'yes_users':yes_users,
        'is_include':is_include,
        'is_no_include':is_no_include,
        'select_tags':select_tags,
        'select_money':select_money,
    }
    # print(filter_dict)


    for i, shop_id in enumerate(shop_id_list):
        if shop_name_list[i] in filter_dict['no_users']:
            print(f"好友【{shop_name_list[i]}】的数据已过滤~")
            continue
        # 如果yes_users  is '' 或者 yes_users 有2个名字，则
        if (shop_name_list[i] in filter_dict['yes_users']) or (filter_dict['yes_users'][0]  ==  ''):
            # 筛选后的输出
            print(f"好友 {i+1}【{shop_name_list[i]}】(总商品：【{total_goods[i]}】,但实际爬取商品经过时间过滤会少)爬取ing...")
            # origin_link = "https://www.szwego.com/album/personal/all?&albumId=_d4nEqZvegdnC9XAeqotJLk9reJ7Sf7C4mSZ9DUA&searchValue=&searchImg=&startDate=&endDate=&sourceId=&requestDataType="
            # query_dict = get_mapping(origin_link)
            # albumId = query_dict['albumId']
            albumId = shop_id
            LoadMore = True
            num = 0
            page = '' 
            t = time.time()
            timestamp = int(round(t * 1000)) # 13位 时间戳 (毫秒) "1678890967997"
            print(f"遍历pages ing")

            # result dict
            result_dict = {
                '序号': [],
                '物件名称': [],
                '价格': [],
                '待处理数据': [],
                '日期': [],
                # 'shop_name': shop_list,
                # 'imgsSrc_list': imgsSrc_list,
            }
            # id_list_all, item_list_all, money_list_all, title_list_all = [], [], [], []
            shop_name = ''
            cur_items = 0
            is_good_friend = 1
            while LoadMore:
                # 当前配置的数据
                data = download_json(albumId, page, start_date, end_date)
                if shop_name == '':
                    try:
                        print()
                        shop_name = data['result']['items'][0]['shop_name']
                    except Exception as e:
                        print(f"ERROR:\n 无数据原因： {data}") # 删除好友
                        is_good_friend = 0 # 不是好朋友
                        break
                
                kargs = {
                    'num': num,
                    }
                # !!!!!!!!!重要处理步骤process_json
                id_list, item_list, money_list, title_list, time_list = process_json(data, cur_items,  **kargs)

                update_dict(result_dict, id_list, item_list, money_list, title_list, time_list)
                cur_items = len(result_dict['序号']) # 每次都得到序号总数
                print(f"当前合法朋友圈条数：{cur_items}")
                
                LoadMore = findLoadMore(data)
                if LoadMore == True:
                    page = findPage(data)

                num  += 1
                time.sleep(random.randint(1, 3))
            # 保存csv文件
            # print(result_dict)
            if is_good_friend == 1:
                # shop_path = f"微商结果/{shop_name}/{start_date}~{end_date}/{shop_name}_item{len(result_dict['序号'])}_{start_date}~{end_date}.csv"
                shop_path = f"微商结果/{shop_name}/{start_date}~{end_date}/{shop_name}({len(result_dict['序号'])}件)_{start_date}~{end_date}.xlsx"
                # if not os.path.isfile(shop_path):
                #     save_csv(result_dict, shop_path)
                # else:
                #     print("excel表格已生成过，跳过~")
                save_csv(result_dict, shop_path)
            else:
                print(f"此好友数据有问题，不保存excel表格！")

            # 修改文件夹和文件名字
            print("修改文件夹名字...")
            old_img_folder = f"微商结果/{shop_name}/{start_date}~{end_date}/img"
            new_img_floder = old_img_folder + f"({len(result_dict['序号'])})"
            if not  os.path.isfile(new_img_floder):
                os.rename(old_img_folder,new_img_floder)
            old_folder = f"微商结果/{shop_name}/{start_date}~{end_date}"
            new_folder = old_folder + f"({len(result_dict['序号'])})"
            if not  os.path.isdir(new_folder):
                os.rename(old_folder,new_folder)
            
            print(f'修改后的文件夹路径(path: {new_folder})...')
            
            
            print(f"爬取好友【{shop_name_list[i]}】的数据结束")
    
    print('爬取结束end',)
