'''
Description: 4 US News世界大学排名 todo2022
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-03-19 01:06:15
LastEditTime: 2022-03-28 13:19:35
FilePath: \Spider-1\practice\25school_ranking\04USNews.py
'''

from pandas import DataFrame,Series
import pandas as pd
import requests
from bs4 import BeautifulSoup
import bs4
 
allUniv = {'rank':[],'school':[],'year':[]}
# USNEWS
# url = 'http://www.qianmu.org/2022USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
#  2021世界大学学术排名 06CWUR世界大学排名2021 不行
# url = 'http://www.qianmu.org/ranking/904.htm'

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
#提取html的函数
 
def fillUnivList(soup):
    #data00 = soup.find_all('div',class_ = "rankItem")
    data0 = soup.find_all('tbody')
    data = data0[0].find_all('tr')
    for tr in data[1:]:
        ltd = tr.find_all('td')
        if len(ltd) == 0:
            continue
        # 中国判断
        if (ltd[3].text != "中国" and ltd[3].text != "香港" and ltd[3].text != "澳门"):
            continue
        allUniv['rank'].append(ltd[0].string)
        # allUniv['school'].append(ltd[1].string) 
        # text以获取某一个标签中所有的文本内容(即使不属于直系内容)
        allUniv['school'].append(ltd[1].text) # <td><a href="http://www.qianmu.org/澳洲国立大学" target="_blank">澳洲国立大学</a></td>
        # allUniv['国家'].append(ltd[3].string)
        allUniv['year'].append("2022")
        # print("学校",ltd[1],ltd[1].text )
        # print("排名: %s,学校 %s"%(ltd[0].string, ltd[1].string))
#将需要的信息放在一个字典的几个相应的列表中的函数，便于生成DataFrame
       
def printUnivList(num,scope = "World"):
    if scope == "World":
        printWorldUnivlist(num)
    elif scope == "China":
        printChinaUnivlist(num)
#通过传入数字和排名种类打印出相应排名，默认打印世界排名
 
def printWorldUnivlist(num):
    
    print("{1:^2}   {2:{0}<30}".format(chr(12288),"排名","学校名称"))
    for i in range(0,num):  
        try:
            print("{1:^4}    {2:{0}<60}".format(chr(12288),df.ix[i]['排名'],df.ix[i]['学校名称']))
        except:
            continue
#打印世界排名前num的大学
 
def printChinaUnivlist(num):
    print("{1:^2}   {2:{0}<30}".format(chr(12288),"排名","学校名称"))
    df_china = df[df['国家'] == '中国']
    for i in range(0,num):
        print("{1:^4}    {2:{0}<60}".format(chr(12288),df_china.index[i],df_china.iloc[i]['学校名称']))
#打印中国排名前num的大学
 
 
html = getHTMLText(url)
soup = BeautifulSoup(html,'html.parser')
fillUnivList(soup) # ==========================
df = DataFrame(allUniv)
# for indexs in df.index:
#     try:
#         df['国家'].ix[indexs] = (df['国家'].ix[indexs]).strip()
#     except:
#         continue
df.to_csv(r"04usnews22.csv",index=False, sep=',')