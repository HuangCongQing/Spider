'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2024-08-25 00:03:31
LastEditTime: 2024-08-25 00:15:13
FilePath: \Spider-1\package\5selenium\002cookies.py
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless') # 不显示图形界面
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options, service)

driver.get("https://www.baidu.com/")
time.sleep(1)#加载等待
print(driver.title)
# print(driver.page_source) # 页面源码数据
# with open('baidu.html','w',encoding='utf-8') as fp:
#     fp.write(driver.page_source)


# 获取cookie
cookies = driver.get_cookies()
for cookie in cookies:
    # 值打印cookie中的name和value
    print("%s -> %s" % (cookie['name'], cookie['value']))
# 获取一个cookie的指定属性值
print("cookie的指定属性值: ", driver.get_cookie("BA_HECTOR")['domain'])
# cookie的指定属性值:  {'domain': '.baidu.com', 'expiry': 1724602253, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '28a58k218g210l648k0kala09isgir1jck1ge1v'}


print()
# 设置cookie
cookies = {'value': 'xxxxx',            
           'name': 'ketangpai_home_remember'}





# 4.操作cookie
# 4.1 获取cookie
cookies = driver.get_cookies()
for cookie in cookies:
    # 值打印cookie中的name和value
 
    print("%s -> %s" % (cookie['name'], cookie['value']))
 
 
 
print("=======================")
 
# 4.2 获取一个cookie的指定属性值
# 参数是一个cookie中name的属性值
# 没有找到返回None
 
print(driver.get_cookie("BAIDUID"))
 
 
 
print("=======================")
 
# 4.3 添加cookie
cookie = {"name": "key-aaaaaaa", "value": "value-aaaaaaa"}
 
driver.add_cookie(cookie)
 
 
 
# 添加后再次获取
cookies = driver.get_cookies()
 
for cookie in cookies:
 
    print("%s -> %s" % (cookie['name'], cookie['value']))
 
 
 
print("=======================")

# 4.4 删除指定cookie
# 根据name删除
 
driver.delete_cookie("key-aaaaaaa")
 
# 删除后再次获取
cookies = driver.get_cookies()
for cookie in cookies:
    print("%s -> %s" % (cookie['name'], cookie['value']))
 
 
 
print("=======================")
 
# 4.5 删除全部cookie
driver.delete_all_cookies()
 
print(driver.get_cookies())
 
 
 
# 5.关闭浏览器
time.sleep(2)
 
driver.close()