'''
Description: 保存为csv文件
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 20:45:34
LastEditTime: 2021-01-16 21:49:36
FilePath: /Spider/文件操作/csv/02csv模块按照行保存为csv文件.py
'''
import csv

#python2可以用file替代open
with open("02保存test.csv","w") as csvfile: 
    writer = csv.writer(csvfile)

    #先写入columns_name(指定表头)
    writer.writerow(["index","a_name","b_name"])
    #写入多行用writerows
    writer.writerows([[0,1,3],[1,2,3],[2,3,4]])