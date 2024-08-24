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


# 切换页面
# 记录一下当前handle(为了跳转回该页面做铺垫)
currentHandle = driver.current_window_handle
# 获取当前所有打开的窗口句柄列表。
window_handles = driver.window_handles
# 切换到新的页面
driver.switch_to.window(window_handles[1])

# 切换回老页面
driver.switch_to.window(currentHandle)