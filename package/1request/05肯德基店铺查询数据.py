'''
Description: 不出结果 https://www.bilibili.com/video/BV1Yh411o7Sz?p=10
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 17:58:46
LastEditTime: 2021-01-03 20:00:19
FilePath: /Spider/package/1request/05肯德基店铺查询数据.py
'''
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import json

if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': 1,
        'pageSize': 10,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }
    response = requests.post(url=url,data=data,headers=headers)

    list_data = response.text# 
    print(list_data)