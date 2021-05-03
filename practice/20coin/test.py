import requests
from bs4 import BeautifulSoup
from lxml import etree
# 导入线程池模块对应的类
# from multiprocessing.dummy import Pool
import json
import re
import pandas as pd
import time

i = 0
all_time = 0.000
while 1:
    start_time = time.time()
    url_total =  "https://api-cn.etherscan.com/api?module=account&action=tokenbalance&contractaddress=0xf3dcbc6d72a4e1892f7917b7c43b74131df8480e&address=0x80a0102a1e601c55fd3f136128bb2d222a879ff3&tag=latest&apikey=PARGXUSPDXCDU952NPQ25DNEIJ569PKAZM"
    # url_total = "https://download.csdn.net/download/weixin_38680957/12851257?utm_medium=distribute.pc_relevant_t0.none-task-download-2%7Edefault%7EOPENSEARCH%7Edefault-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-download-2%7Edefault%7EOPENSEARCH%7Edefault-1.control"
    headers = {
        #   'Host': 'www.mxc.la',
        # 'Referer': 'https://www.mxc.la/trade/easy',
        # 'X-Requested-With': 'XMLHttpRequest',
        # 'Connection': 'keep-alive',
        # 'Cookie': "_ga=GA1.2.796343481.1618981015; _gid=GA1.2.1137290540.1618981015; __zlcmid=13ijyJ1eBCHrOpL; aliyungf_tc=55a0a4103a49dd83fa2f7b31bea1732efc0ce169c03cf37b56225ec28e8f085a; uc_token=; _gat_gtag_UA_177925109_1=1",
        'Connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

    }
    try:
        response = requests.get(url_total,headers=headers, timeout=30, verify=False)
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        print("ZZzzzz...")
        time.sleep(0.3)
        print("Was a nice sleep, now let me continue...")
        continue
    # requests.adapters.DEFAULT_RETRIES = 5
    url_total_html = response.text
    # number = re.findall(r"\d+\.?\d*", url_total_html)
    # bdp = int(number[1])
    # a = bdp * 0.000000000000000001
    # print(a)
    # print("123")
    response.close() # # 关闭，很重要,确保不要过多的链接
    time.sleep(0.6)
    i = i+1
    print("循环次数:", i)
    # 时间
    end_time = time.time()
    time_diff = end_time - start_time
    all_time  = all_time + time_diff
    print('当前循环时间差:', time_diff)
    print('总时间:', all_time)
    # except requests.exceptions.ConnectionError:
    #     requests.status_code = "Connection refused"