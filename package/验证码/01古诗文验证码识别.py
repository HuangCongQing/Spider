'''
Description: https://www.bilibili.com/video/BV1Yh411o7Sz?p=31
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-10 14:28:21
FilePath: /Spider/package/验证码/01古诗文验证码识别.py
'''
import requests
from lxml import etree
from CodeClass import YDMHttp


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


#将验证码图片下载到本地
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = requests.get(url=url,headers=headers).text
#解析验证码图片img中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = requests.get(url=code_img_src,headers=headers).content
#将验证码图片保存到了本地
with open('./code.jpg','wb') as fp:
    fp.write(img_data)


#调用打码平台的示例程序进行验证码图片数据识别
code_text = getCodeText('code.jpg',1004)

print('识别结果为：',code_text)
