'''
Description: 爬取不规则表格 https://www.cnblogs.com/cttcarrotsgarden/p/10769097.html
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-02-28 23:21:10
LastEditTime: 2021-03-01 00:11:58
FilePath: /Spider/package/使用tips必看/爬取不规则表格.py
'''
import pandas as pd
url = 'http://www.hnu.edu.cn/xyxk/xkzy/zylb.htm'

''' 生成txt文件 '''
# table = pd.read_html(url) 
# pd.set_option('display.max_rows', None)  # 显示全部的行
# with open("湖南大学学院与专业.txt", "wt", encoding='utf8') as out_file:  # 保存为txt文件
#     for i in table:
#         out_file.write(str(i)+'\n')



''' 生成csv文件 '''
for table in pd.read_html(url):
    print(table[0]) # 学院
    print(table[1]) # 专业名称
    table.to_csv('table.csv', mode='a',encoding='utf-8',header=0,index=False)