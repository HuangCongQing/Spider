
'''
Description: 存储excel 参考:https://blog.csdn.net/wangkai_123456/article/details/50457284?
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-04 21:41:17
LastEditTime: 2021-01-05 11:36:35
FilePath: /Spider/文件操作/excel/02xlwt存储.py
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
	row0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']
	row1 = [u'测试', '15:50:33-15:52:14', 22706, 4190202]
	col0 = [u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID']
	col1 = [u'测试', '15:50:33-15:52:14', 22706, 4190202]
	
	#生成第一行和第二行
	# for i in range(len(row0)):
	# 	data_sheet.write(0, i, row0[i], set_style('Times New Roman', 220, True))
	# 	data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))
	#生成第一列和第二列
	for i in range(len(col0)):
		data_sheet.write(i, 0, col0[i], set_style('Times New Roman', 220, True)) # set_style 设置属性
		data_sheet.write(i, 1, col1[i])
	
	#保存文件
	workbook.save('02xlwt存储demo.xls')	
	
	
if __name__ == '__main__': 
	write_excel()
	print('创建demo.xlsx文件成功')
 
 