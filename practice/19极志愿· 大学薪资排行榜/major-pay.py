# https://www.jizhy.com/44/rank/major-pay?diploma=7


'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-28 18:02:31
LastEditTime: 2021-03-29 20:01:22
FilePath: /Spider/practice/19极志愿· 大学薪资排行榜/school-pay.py
'''


import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd

def get_school_pay():
    # 存储数据初始化
    school_list = []
    pay_list =[]
    rank_list =[]
    # 获取数据
    # 本科url
    url_list = [
        "https://www.jizhy.com/open/major/salary-rank-list?page=1&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617001963002&platform=desktop&v=210&sign=F8737FE4D6AEB73C70147961CC165A91",
        "https://www.jizhy.com/open/major/salary-rank-list?page=2&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002724261&platform=desktop&v=210&sign=D5CB5FD0D3F5CD279B34EDF0D655D746",
        "https://www.jizhy.com/open/major/salary-rank-list?page=3&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002728906&platform=desktop&v=210&sign=5ACB8AD8190DAB9E043357DDF62EA656",
        "https://www.jizhy.com/open/major/salary-rank-list?page=4&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002746077&platform=desktop&v=210&sign=E12791D9D78E4BB853791FD1BDB02AAA",
        "https://www.jizhy.com/open/major/salary-rank-list?page=5&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002750206&platform=desktop&v=210&sign=03B67D7DFF789745A490D2D0B484CF88",
        "https://www.jizhy.com/open/major/salary-rank-list?page=6&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002869706&platform=desktop&v=210&sign=7A61BCED8307749A6469F00DBEE5A289",
        "https://www.jizhy.com/open/major/salary-rank-list?page=7&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002873969&platform=desktop&v=210&sign=DE42A6631469060AFA87AD2B748AA94D",
        "https://www.jizhy.com/open/major/salary-rank-list?page=8&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002878356&platform=desktop&v=210&sign=91BB2843D94B2802F5B0030904E370BD",
        "https://www.jizhy.com/open/major/salary-rank-list?page=9&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002884238&platform=desktop&v=210&sign=B4F550EB1B3DEB04A6C8A4A5914430B9",
        "https://www.jizhy.com/open/major/salary-rank-list?page=10&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617002888284&platform=desktop&v=210&sign=CC6856BE6EA6E086E5266EFADAFE7D49",
        "https://www.jizhy.com/open/major/salary-rank-list?page=11&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003014803&platform=desktop&v=210&sign=CF522358666F169186A145D01DABE005",
        "https://www.jizhy.com/open/major/salary-rank-list?page=12&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003018017&platform=desktop&v=210&sign=B87653D38024449B7369A8543E8F9976",
        "https://www.jizhy.com/open/major/salary-rank-list?page=13&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003022065&platform=desktop&v=210&sign=101E7D9616C09669FD512D30E4201BB7",
        "https://www.jizhy.com/open/major/salary-rank-list?page=14&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003025811&platform=desktop&v=210&sign=E985A35ADEB284637E901B1CB024B904",
        "https://www.jizhy.com/open/major/salary-rank-list?page=15&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003029657&platform=desktop&v=210&sign=2772CA9183AA0B503D08AB1403CD2277",
        "https://www.jizhy.com/open/major/salary-rank-list?page=16&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003107212&platform=desktop&v=210&sign=5B026482AE0E232E9F3077A6FF73B7B9",
        "https://www.jizhy.com/open/major/salary-rank-list?page=17&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003112059&platform=desktop&v=210&sign=B76601494C9DAAFCFAF9830559C320C4",
        "https://www.jizhy.com/open/major/salary-rank-list?page=18&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003115076&platform=desktop&v=210&sign=FA71B4432BABAA93C6FACE126E62B36B",
        "https://www.jizhy.com/open/major/salary-rank-list?page=19&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003117373&platform=desktop&v=210&sign=9F7379BD89A2566B9CD3BAA722A29124",
        "https://www.jizhy.com/open/major/salary-rank-list?page=20&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003120615&platform=desktop&v=210&sign=79545E622C8E3B3E8EF71FD72E9B0BDD",
        "https://www.jizhy.com/open/major/salary-rank-list?page=21&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003214975&platform=desktop&v=210&sign=10AACBAFC5DDE4AB41F2DCFE43D737FA",
        "https://www.jizhy.com/open/major/salary-rank-list?page=22&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003221635&platform=desktop&v=210&sign=3818330B2F06D04C76ED140EC030D157",
        "https://www.jizhy.com/open/major/salary-rank-list?page=23&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003225803&platform=desktop&v=210&sign=FD2A757A4692B302EB624879D7D91E7D",
        "https://www.jizhy.com/open/major/salary-rank-list?page=24&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003228352&platform=desktop&v=210&sign=CC18189DDB7E896E12B1C5DFDCF1D11E",
        "https://www.jizhy.com/open/major/salary-rank-list?page=25&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003230553&platform=desktop&v=210&sign=A5DB3C8C9FAEA33F995E2860F47715BE",
        "https://www.jizhy.com/open/major/salary-rank-list?page=26&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003312642&platform=desktop&v=210&sign=301026DAE38D8481F0BB3AE00E040795",
        "https://www.jizhy.com/open/major/salary-rank-list?page=27&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003317233&platform=desktop&v=210&sign=3187CCEB72C45B4D9EA81FAC9ACE9A28",
        "https://www.jizhy.com/open/major/salary-rank-list?page=28&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003319722&platform=desktop&v=210&sign=858DB497AD7ABC12A5451BAB12B7138D",
        "https://www.jizhy.com/open/major/salary-rank-list?page=29&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003323001&platform=desktop&v=210&sign=013962339D5925772CE9E93C626ED419",
        "https://www.jizhy.com/open/major/salary-rank-list?page=30&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003325803&platform=desktop&v=210&sign=A590B59065682F894E83D5C5C6330D70",
        "https://www.jizhy.com/open/major/salary-rank-list?page=31&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003391095&platform=desktop&v=210&sign=E8242EF014180948287171CD9D21BAE8",

    ]
    # 专科url
    
    url_list1 = [
        "https://www.jizhy.com/open/major/salary-rank-list?page=1&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003583486&platform=desktop&v=210&sign=59893843ED09E00983FC4DF6B4AA89E6",
        "https://www.jizhy.com/open/major/salary-rank-list?page=2&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003654091&platform=desktop&v=210&sign=EF0CBBD4CD07F81040563D88EA4DD7C7",
        "https://www.jizhy.com/open/major/salary-rank-list?page=3&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003657135&platform=desktop&v=210&sign=9A773249A45ED72E09C3D97A8BEBCBA3",
        "https://www.jizhy.com/open/major/salary-rank-list?page=4&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003660038&platform=desktop&v=210&sign=BBFABF5206E176CA23D260C8C6BA9F5C",
        "https://www.jizhy.com/open/major/salary-rank-list?page=5&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003663609&platform=desktop&v=210&sign=C6C95EECF382551244D052D7DB8ED973",
        "https://www.jizhy.com/open/major/salary-rank-list?page=6&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003727657&platform=desktop&v=210&sign=89EE286D57F6CEB77F619651BFDC1965",
        "https://www.jizhy.com/open/major/salary-rank-list?page=7&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1617003731361&platform=desktop&v=210&sign=67043FECDB3F473A7724E6BB31DF3443",

      
    ]
    for url in url_list1: # 0-2800
        print("正在获取：", url)
        #UA伪装：将对应的User-Agent封装到一个字典中
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }
        # url = 'https://www.jizhy.com/open/sch/salary-rank-list?page='+ str(page) +  '&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts='+ str(ts) +  '&platform=desktop&v=210&sign='+ str(sign)
        # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        # print("访问url：", url)
        response = requests.get(url=url,headers=headers, timeout=60)
        response.encoding = 'utf-8' 
        content = response.content
        # json格式转为字典
        result = json.loads(content)
        # print("结果：",result)
        # print("爬取专业数：",len(result['data']['item']))
        
        for item in range(0,len(result['data'])): 
            print("爬取薪资:", result['data'][item]['salary'])
            school = result['data'][item]['major_name']
            pay = result['data'][item]['salary']
            rank = result['data'][item]['major_rank']
            school_list.append(school)
            pay_list.append(pay)
            rank_list.append(rank)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'排名':rank_list,'专业':school_list,'毕业后五年月薪':pay_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"专业薪酬2020排行榜(专科).csv",index=False, sep=',')
    print('爬取结束',)

    
if __name__ == "__main__":
    get_school_pay()
