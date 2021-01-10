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

#https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx
#模拟登录：验证码的识别，动态参数的处理，cookie相关的操作处理
s = requests.Session()
#1.验证码图片爬取到本地进行存储
url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
page_text = s.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
img_src = 'https://so.gushiwen.org'+tree.xpath('//*[@id="imgCode"]/@src')[0]
img_data = s.get(url=img_src,headers=headers).content
with open('./gushiwen.jpg','wb') as fp:
    fp.write(img_data)

#解析动态参数
__VIEWSTATE = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
__VIEWSTATEGENERATOR = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]

#将验证码图片提交给打码平台进行识别
code_text = getCodeText('./gushiwen.jpg',1004)
print(code_text)
#模拟登录
post_url = 'https://so.gushiwen.org/user/login.aspx?from=http%3a%2f%2fso.gushiwen.org%2fuser%2fcollect.aspx'
data = {
    #前两个参数是动态参数
    '__VIEWSTATE': __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.org/user/collect.aspx',
    'email': 'www.zhangbowudi@qq.com',
    'pwd': 'bobo328410948',
    'code': code_text,
    'denglu': '登录',
}
#s表示的session中已经存储了相关的cookie
response = s.post(url=post_url,data=data,headers=headers)
page_text = response.text
print(response.status_code)
with open('./gushiwenwang.html','w',encoding='utf-8') as fp:
    fp.write(page_text)