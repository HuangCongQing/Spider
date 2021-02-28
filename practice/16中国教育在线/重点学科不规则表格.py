'''
Description:  http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266612.shtml
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-02-28 23:40:26
LastEditTime: 2021-03-01 01:40:57
FilePath: /Spider/practice/16中国教育在线/重点学科不规则表格.py
'''
import pandas as pd
url = 'http://www.cdgdc.edu.cn/xwyyjsjyxx/xwbl/zdjs/zdxk/zdxkmd/lsx/266612.shtml'

''' 生成txt文件 '''
# table = pd.read_html(url) 
# pd.set_option('display.max_rows', None)  # 显示全部的行
# with open("湖南大学学院与专业.txt", "wt", encoding='utf8') as out_file:  # 保存为txt文件
#     for i in table:
#         out_file.write(str(i)+'\n')



''' 生成csv文件 '''
print( pd.read_html(url)[0])
print( pd.read_html(url)[0][0].values) # dataframe和np.array的相互转换
print( pd.read_html(url)[0][0].values[1:-1]) # 去掉开头和结尾
for table in pd.read_html(url):
    # print(table)
    table.to_csv('重点学科不规则表格.csv', mode='a',encoding='utf-8',header=0,index=False)  # 循环添加