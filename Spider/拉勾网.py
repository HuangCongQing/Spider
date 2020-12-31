# -*- coding: utf-8 -*-
'''
Created on 2017年8月22日

@author: hasee
'''
from bs4 import BeautifulSoup
import requests
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
import pymysql
from time import sleep
import re
what1 = '数据挖掘'
what2 ='全职'
what3 = '北京'
what1 = urllib.parse.quote(what1)
what2  = urllib.parse.quote(what2)
what3  = urllib.parse.quote(what3)
driver=webdriver.PhantomJS()
# driver=webdriver.Chrome(executable_path='E:\package\Chrome64_48.0.2564.109\chromedriver.exe')
url = 'https://www.lagou.com/jobs/list_%s?px=default&gx=%s&city=%s#order' % (what1,what2,what3)
url2 = 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=sug&fromSearch=true&suginput=shuju'
driver.implicitly_wait(100)
driver.get(url)
bs = BeautifulSoup(driver.page_source)
req = bs.find('ul',class_ = 'item_con_list',style ='display: block;')
urllinks = req.find_all('a',class_='position_link')
import queue
que = queue.Queue()
for i in urllinks:
    print(i.get('href'))
    que.put(i.get('href'))
link_next = driver.find_element_by_xpath("//span[@class='pager_next ']")
link_next.click()
times = 0
while True:
    times += 1
    driver.implicitly_wait(10)
    bs = BeautifulSoup(driver.page_source)
    req = bs.find('ul',class_ = 'item_con_list',style ='display: block;')
    urllinks = req.find_all('a',class_='position_link')
    for i in urllinks:
        print(i.get('href'))
        que.put(i.get('href'))
    print(times)
    if times  == 3:
        break
    link_next = driver.find_element_by_xpath("//span[@class='pager_next ']")
    link_next.click()
    sleep(3)


driver2 = webdriver.PhantomJS()
# driver2=webdriver.Chrome(executable_path='E:\package\Chrome64_48.0.2564.109\chromedriver.exe')
while que:
    try :
        newurl = que.get()
        driver2.get(newurl)
        driver2.implicitly_wait(100)
        bs2 = BeautifulSoup(driver2.page_source)

        job_info = bs2.find('div', class_='job-name')
        company = job_info.find('div', class_='company')
        reg1 = re.compile("<[^>]*>")
        ###部门
        company = reg1.sub('', company.prettify())
        ####职位
        job = job_info.find('span', class_='name')
        reg2 = re.compile("<[^>]*>")
        job = reg2.sub('', job.prettify()).strip('\n')
        ###工资 、地点 、经验、学历
        job_req = bs2.find('dd', class_='job_request')
        all_info = []
        for i in job_req.find_all('span'):
            reg3 = re.compile("<[^>]*>")
            new_in = reg3.sub('', i.prettify())
            all_info.append(new_in)

        salary = all_info[0]
        mod = re.compile('/')
        salary = mod.sub('', salary).strip('\n')

        address = all_info[1]
        address = mod.sub('', address).strip('\n')
        exp = all_info[2]
        exp = mod.sub('', exp).strip('\n')
        edu = all_info[3]
        edu = mod.sub('', edu).strip('\n')
        ###job_detail
        job_det = bs2.find('dl', class_='job_detail', id='job_detail')
        ###职位诱惑
        job_lu = job_det.find('dd', class_='job-advantage').find('p')
        reg4 = re.compile("<[^>]*>")
        job_lu = reg4.sub('', job_lu.prettify())
        ###工作责任与要求
        job_zong = job_det.find('dd', class_='job_bt')
        job_res = job_zong.find('div')
        reg5 = re.compile("<[^>]*>")
        job_res = str(reg5.sub('', job_res.prettify()).strip('\n').strip())
        ###工作地址
        job_ad = bs2.find('dd', class_='job-address clearfix').find('div', class_='work_addr')
        reg6 = re.compile("<[^>]*>")
        job_ad = reg6.sub('', job_ad.prettify()).strip('\n')
        job_con = bs2.find('dl', class_='job_company', id='job_company')
        ###公司名称
        com_name = job_con.find('dt').find('a').find('img').get('alt')
        ###公司类型
        com_cat = job_con.find('ul', class_='c_feature').find_all('li')
        all_info2 = []
        for i in com_cat:
            reg7 = re.compile("<[^>]*>")
            new_in = reg7.sub('', i.prettify())
            all_info2.append(new_in)
        com_cat = all_info2[0].strip('\n')
        lingyu  = '领域'
        dev = '发展阶段'
        gui ='规模'

        a1 = re.compile(lingyu)
        a2 = re.compile(dev)
        a3 = re.compile(gui)
        com_cat = a1.sub('',com_cat).strip()
        com_qua = all_info2[1].strip('\n')
        com_qua = a2.sub('',com_qua).strip()
        com_peo = all_info2[-2].strip('\n')
        com_peo = a3.sub('',com_peo).strip()
        db = pymysql.connect('localhost', 'root', 'xin123456789', 'test')
        db.encoding = 'utf-8'
        cursor = db.cursor()
        cursor.execute('set names utf8')

        sql = "INSERT INTO lagou_wajue (job_name,com_name,com_addr,com_cat,com_qua,com_peo,exp1,edu,salary,com_resp) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') "
        cursor.execute(sql % (job, com_name, address, com_cat, com_qua, com_peo, exp, edu, salary, job_res))

        db.commit()
        cursor.close()
        db.close()
    except:
        print('该页面无法获取')


driver.close()
driver2.close()