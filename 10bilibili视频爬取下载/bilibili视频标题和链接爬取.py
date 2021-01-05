'''
Description: bilibili视频标题和链接爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 14:57:10
LastEditTime: 2021-01-05 12:41:31
FilePath: /Spider/10bilibili视频爬取下载/bilibili视频标题和链接爬取.py
'''
import requests
import re
from bs4 import BeautifulSoup
import openpyxl
import xlwt			# 存储excel

def read_excel():
    #定义一个空列表
    stu_num=[]
    #打开目标execl，这里注意openpyxl能读取的execl后缀名是'.xlsx'文件
    workbook1=openpyxl.load_workbook(r'/home/hcq/python/Spider/文件操作/excel/college.xlsx')
    #选定目标sheet
    worksheet1 = workbook1.active
    for cell in worksheet1['A']:
        # print(cell.value)
        stu_num.append(cell.value)#这里用循环把A列每个cell的值写入开始定义的空列表
    # print(stu_num)
    return stu_num

def get_details(schools):
    url_all = []
    title_all = []
    no_info = 0
    for school in schools:
        # print(school) # 北京大学
        word = school +  " 宣传片 最新"  	# 解析，用于组成URL
        # print(word)
        url = 'https://search.bilibili.com/all'
        param = {
            'keyword':word
        }
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        response = requests.get(url=url,params=param,headers=headers)
        html = response.text
        soup = BeautifulSoup( html , "lxml" )  # lxml解析
        # print(soup)
        # print(soup.select('.mixin-list > ul a')[0]['href'])  
        li = soup.select('.mixin-list > ul > li')
        # print("li长度：",len(li))
        if len(li) > 0:
            li1 = soup.select('.mixin-list > ul > li')[0]  # 数组为空   IndexError: list index out of range
            url_link = 'https:' +  li1.a['href']  # 视频链接
            title =  li1.a['title'] # 视频标题
            # 封面为空
            # print(soup.select('.lazy-img > img')[0]) # <img alt="" src=""/>??????
            # img_link = 'https:' +  soup.select('.lazy-img > img')[0]['src']
            # print(url_link)
            print( title,  "  已爬取")
            url_all.append(url_link)
            title_all.append(title)
        else:
            no_info = no_info + 1
            url_all.append('')
            title_all.append('')
            print(school, " 没有相关视频，未爬取")
    print("没有获得相关学校视频链接总数：", no_info)
    return schools, url_all,  title_all


def write_excel(schools_all, url_all,  title_all ):
	#创建工作簿
	workbook = xlwt.Workbook(encoding='utf-8')  
	#创建sheet
	data_sheet = workbook.add_sheet('bilibili爬取')  
	# 测试数据
	col0 = schools_all
	col1 = url_all
	col2 = title_all
	
	#生成第一列和第二列
	for i in range(len(col0)):
		data_sheet.write(i, 0, col0[i]) # set_style 设置属性
		data_sheet.write(i, 1, col1[i])
		data_sheet.write(i, 2, col2[i])
	
	#保存文件
	workbook.save('bilibili视频标题和链接爬取.xls')	
	

if __name__ == "__main__":
    college = read_excel()
    # print(college[0])
    schools_all, url_all,  title_all = get_details(college)
    # print(url_all, title_all)
    write_excel(schools_all, url_all,  title_all )
    print("爬取完毕，共爬取",len(schools_all), "学校" )
    
    
