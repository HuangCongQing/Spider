
'''
Description: 存储excel  参考如下
https://www.bilibili.com/video/BV12E411A7ZQ?p=25
https://blog.csdn.net/wzh365979633/article/details/107466480
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-04 21:41:17
LastEditTime: 2021-01-05 15:02:03
FilePath: /Spider/文件操作/excel/02.1xlwt存储99乘法表.py
'''


# _*_ coding:utf-8 _*_
 
#----------------------------------------------------------------------------
# import modules 
#----------------------------------------------------------------------------
import os
import xlwt			
 
#  设置样式,可有可无
# 使用方法:  data_sheet.write(i, 1, col1[i], set_style('Times New Roman', 220, True))
def set_style(name, height, bold = False):
	style = xlwt.XFStyle()   #初始化样式
	
	font = xlwt.Font()       #为样式创建字体
	font.name = name
	font.bold = bold
	font.color_index = 4
	font.height = height
	
	style.font = font
	return style
 
	
def write_excel():
	#创建工作簿
	workbook = xlwt.Workbook(encoding='utf-8')  
	#创建sheet
	data_sheet = workbook.add_sheet('demo')  
	# 测试数据
	for i in range(0,9):
    		for j in range(0,i+1):
    				data_sheet.write(i,j , "%d * %d = %d "%(i+1, j+1, (i+1)*(j+1)))
	
	#保存文件
	workbook.save('九九乘法表.xls')	
	
	
if __name__ == '__main__': 
	write_excel()
	print('创建xlsx文件成功')
 
 