'''
Description:  参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=35
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-10 16:06:28
FilePath: /Spider/package/1request-advanced/02登录后爬取当前用户的相关的用户信息.py
'''
#编码流程：
#1.验证码的识别，获取验证码图片的文字数据
#2.对post请求进行发送（处理请求参数）
#3.对响应数据进行持久化存储

from CodeClass import YDMHttp
import requests
from lxml import etree
#封装识别验证码图片的函数
def getCodeText(imgPath,codeType):
    # 普通用户用户名
    username = 'bobo328410948'

    # 普通用户密码
    password = 'bobo328410948'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 6003

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '1f4b564483ae5c907a1d34f8e2f2776c'

    # 图片文件：即将被识别的验证码图片的路径
    filename = imgPath

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = codeType

    # 超时时间，秒
    timeout = 20
    result = None
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login();
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance();
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        print('cid: %s, result: %s' % (cid, result))
    return result

#创建一个session对象
session = requests.Session()

#1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'http://www.renren.com/SysHome.do'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(code_img_data)


#使用云打码提供的示例代码对验证码图片进行识别  (已失效)
# result = getCodeText('code.jpg',1000)
# print(result) # 验证码==================================================================
#post请求的发送（模拟登录）
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019431046983'
data = {
    'email': '18875141356',
    'icode': '', # 验证码 a. 密码账号输入错误3次才需要验证码，一般情况下不用验证码也能登录==================================================================
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '88a390533a44df8018d6b481f18c357895a876ac4c79c35768895a74d5ae6993',
    'rkey': 'd11c3e47ad56c6b124063a8c06f9f1d7',
    'f':'http%3A%2F%2Fwww.renren.com%2F975698146%2Fnewsfeed%2Fphoto',
}
#使用session进行post请求的发送
response = session.post(url=login_url,headers=headers,data=data)
print(response.status_code)

#爬取当前用户的个人主页对应的页面数据========================================================================
detail_url = 'http://www.renren.com/975698146/profile'
#手动cookie处理
# headers = {
#     'Cookie':'xxxx'
# }
#使用携带cookie的session进行get请求的发送
detail_page_text = session.get(url=detail_url,headers=headers).text
with open('bobo.html','w',encoding='utf-8') as fp:
    fp.write(detail_page_text)
