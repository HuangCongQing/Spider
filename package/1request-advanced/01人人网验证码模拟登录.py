'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-10 13:43:56
FilePath: /Spider/package/1request-advanced/01人人网验证码模拟登录.py
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


#1.对验证码图片进行捕获和识别
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'http://www.renren.com/SysHome.do'
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0] # 验证码图片地址
code_img_data = requests.get(url=code_img_src,headers=headers).content
with open('./code.jpg','wb') as fp:
    fp.write(code_img_data)

#使用云打码提供的示例代码对验证码图片进行识别
result = getCodeText('code.jpg',1000)
print(result)
#post请求的发送（模拟登录）
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019431046983'
data = {
    'email': 'www.zhangbowudi@qq.com',
    'icode': result,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '06768edabba49f5f6b762240b311ae5bfa4bcce70627231dd1f08b9c7c6f4375',
    'rkey': '1028219f2897941c98abdc0839a729df',
    'f':'https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Dgds6TUs9Q1ojOatGda5mVsLKC34AYwc5XiN8OuImHRK%26wd%3D%26eqid%3D8e38ba9300429d7d000000035cedf53a',
}
response = requests.post(url=login_url,headers=headers,data=data)
print(response.text)
print(response.status_code)

# login_page_text = response.text
#
#
# with open('renren.html','w',encoding='utf-8') as fp:
#     fp.write(login_page_text)
