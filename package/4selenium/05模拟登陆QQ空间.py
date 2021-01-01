'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-01 16:39:32
FilePath: /Spider/package/4selenium/05模拟登陆QQ空间.py
'''
from selenium import webdriver
from time import sleep

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')

# 1 点击输入账号密码标签
''' 
<iframe id="login_frame" name="login_frame" height="100%" scrolling="no" width="100%" frameborder="0" src="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&amp;daid=5&amp;&amp;hide_title_bar=1&amp;low_login=0&amp;qlogin_auto_login=1&amp;no_verifyimg=1&amp;link_target=blank&amp;appid=549000912&amp;style=22&amp;target=self&amp;s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&amp;pt_qr_app=手机QQ空间&amp;pt_qr_link=https%3A//z.qzone.com/download.html&amp;self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&amp;pt_qr_help_link=https%3A//z.qzone.com/download.html&amp;pt_no_auth=0"></iframe>
 '''
bro.switch_to.frame('login_frame') # 切换到iframe

a_tag = bro.find_element_by_id("switcher_plogin") # 定位到输入账号密码标签
a_tag.click() # 点击标签

# 2  在切换后的页面输入账号密码，点击登录
userName_tag = bro.find_element_by_id('u')
password_tag = bro.find_element_by_id('p')
sleep(1)
userName_tag.send_keys('328410948') # 账号
sleep(1)
password_tag.send_keys('123456789') # 密码
sleep(1)
btn = bro.find_element_by_id('login_button') # 点击登录按钮
btn.click()
# 3 拖动滑块验证登录

# TODO

sleep(3)

bro.quit()