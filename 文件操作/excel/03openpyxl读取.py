'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-05 10:33:12
LastEditTime: 2021-01-05 10:34:11
FilePath: /Spider/文件操作/excel/03openpyxl读取.py
'''
import openpyxl
#定义一个空列表
stu_num=[]
#打开目标execl，这里注意openpyxl能读取的execl后缀名是'.xlsx'文件
workbook1=openpyxl.load_workbook(r'/home/hcq/python/Spider/文件操作/excel/college.xlsx')
#选定目标sheet
worksheet1 = workbook1.active
for cell in worksheet1['A']:
    # print(cell.value)
    stu_num.append(cell.value)#这里用循环把A列每个cell的值写入开始定义的空列表
print(stu_num) # 获取一列
