'''
Description:  https://www.bilibili.com/video/BV1Yh411o7Sz?p=55
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-01 18:22:16
FilePath: /Spider/package/4selenium/07基于selenium实现12306登录.py
'''
#下述代码为超级鹰提供的示例代码
import requests
from hashlib import md5

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

# chaojiying = Chaojiying_Client('bobo328410948', 'bobo328410948', '899370')	#用户中心>>软件ID 生成一个替换 96001
# im = open('12306.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# print(chaojiying.PostPic(im, 9004)['pic_str']) # 返回坐标结果 字典
#上述代码为超级鹰提供的示例代码

#使用selenium打开登录页面
from selenium import webdriver
import time
from PIL import Image # 图像裁剪
from selenium.webdriver import ActionChains

# 打开登录页面
bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://kyfw.12306.cn/otn/login/init')
time.sleep(1)

#save_screenshot就是将当前页面进行截图且保存
bro.save_screenshot('aa.png') # 保存截图

#确定验证码图片对应的左上角和右下角的坐标（裁剪的区域就确定）
code_img_ele = bro.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img')
location = code_img_ele.location  # 验证码图片左上角的坐标 x,y==============================
print('location:',location)
size = code_img_ele.size  #验证码标签对应的长和宽========================================
print('size:',size)
#左上角和右下角坐标
rangle = (
int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
#至此验证码图片区域就确定下来了

i = Image.open('./aa.png') # 打开截图
code_img_name = './code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle) # 坐标裁剪
frame.save(code_img_name)

#将验证码图片提交给超级鹰进行识别==========================
chaojiying = Chaojiying_Client('bobo328410948', 'bobo328410948', '899370')	#用户中心>>软件ID 生成一个替换 96001
im = open('code.png', 'rb').read()		#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
print(chaojiying.PostPic(im, 9004)['pic_str'])
print("chaojiying.PostPic(im, 9004)['pic_str']")
result = chaojiying.PostPic(im, 9004)['pic_str']  # 返回对应坐标
# result = 248,67|104,141  # 测试
all_list = [] #要存储即将被点击的点的坐标  [[x1,y1],[x2,y2]]
if '|' in result:
    list_1 = result.split('|') # 竖线分割
    count_1 = len(list_1)
    for i in range(count_1):
        xy_list = []
        x = int(list_1[i].split(',')[0])
        y = int(list_1[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])  # AttributeError: 'tuple' object has no attribute 'split'
    y = int(result.split(',')[1])
    xy_list = []
    xy_list.append(x)
    xy_list.append(y)
    all_list.append(xy_list)
print(all_list)

#遍历列表，使用动作链对每一个列表元素对应的x,y指定的位置进行点击操作
for l in all_list:
    x = l[0]
    y = l[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    time.sleep(0.5)

# 输入账号密码登录
bro.find_element_by_id('username').send_keys('www.zhangbowudi@qq.com')
time.sleep(2)
bro.find_element_by_id('password').send_keys('bobo_15027900535')
time.sleep(2)
bro.find_element_by_id('loginSub').click()
time.sleep(30)
bro.quit()







