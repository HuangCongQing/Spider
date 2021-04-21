
'''
Description: https://www.mxc.la/trade/easy#BDP_USDT
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 12:43:59
LastEditTime: 2021-01-15 13:09:38
FilePath: /Spider/文件操作/json/01json处理.py
'''


import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt  # 存储
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd
from tqdm import *

def get_coin_pay():
    # 存储数据初始化
    p_list = []
    q_list =[]
    T_list =[]
    t_list =[]

    print("正在获取所有data... ...")
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        #   'Host': 'www.mxc.la',
        'Referer': 'https://www.mxc.la/trade/easy',
        # 'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        # 'Cookie': "_ga=GA1.2.796343481.1618981015; _gid=GA1.2.1137290540.1618981015; __zlcmid=13ijyJ1eBCHrOpL; aliyungf_tc=55a0a4103a49dd83fa2f7b31bea1732efc0ce169c03cf37b56225ec28e8f085a; uc_token=; _gat_gtag_UA_177925109_1=1",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    param = {
        'symbol': 'BDP_USDT'
    }
    url = 'https://www.mxc.la/api/platform/spot/market/deals'
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)
    response.encoding = 'utf-8'
    content = response.content
    # json格式转为字典
    result = json.loads(content)
    # print(result)
    # tree = etree.HTML(page_text)
    # tr_list = tree.xpath('//div[@class="zhiye"]')
    # print("获取链接：", len(tr_list))
    result = result['data']
    for item in tqdm(range(0,len(result['data']))): 
        # print("爬取p:", result['data'][item]['p'])
        p = result['data'][item]['p']
        q = result['data'][item]['q']
        T = result['data'][item]['T']
        t = result['data'][item]['t']
        p_list.append(p)
        q_list.append(q)
        T_list.append(T)
        t_list.append(t)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'p_list':p_list,'q_list':q_list,'T_list':T_list,'t_list':t_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"coin.csv",index=False, sep=',')
    print('爬取结束',)


if __name__ == "__main__":
    get_coin_pay()
