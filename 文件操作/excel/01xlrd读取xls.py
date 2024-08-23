'''
Description: 读取excel  https://blog.csdn.net/weixin_30383279/article/details/96566508?
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-04 21:19:39
LastEditTime: 2021-01-05 11:12:31
FilePath: /Spider/文件操作/excel/01xlrd读取.py
'''


# _*_ coding:utf-8 _*_
 
#----------------------------------------------------------------------------
# import modules 
#----------------------------------------------------------------------------
import os
import xlrd
from datetime import date,datetime
 
#打开Excel文件
workbook = xlrd.open_workbook('/home/hcq/python/Spider/文件操作/excel/附件3：学生信息汇总.xls')
 
#输出Excel文件中所有sheet的名字
print(workbook.sheet_names()) # ['Sheet1', 'Sheet2', 'Sheet3']
 
# 获取一个工作表
table = workbook.sheets()[0]          #通过索引顺序获取
# table = workbook.sheet_by_index(0) #通过索引顺序获取
# table = workbook.sheet_by_name(u'Sheet1')#通过名称获取

# 获取整行和整列的值（数组）　　
print(table.row_values(0)) # 行
print(table.col_values(1)[1:])  # 列（去除第一个）  ['黄深度', '是大V辅导费', 'DVD发', '电饭煲']