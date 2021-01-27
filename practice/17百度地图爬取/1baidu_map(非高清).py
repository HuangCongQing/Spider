'''
Description: 百度地图爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-27 18:43:38
LastEditTime: 2021-01-27 20:55:29
FilePath: /Spider/practice/17百度地图爬取/baidu_map.py
'''
# -*- encoding: utf-8 -*-

"""
@File    : 图片自动下载器(百度图片).py
@Time    : 2019/10/22 8:38
@Author  : 封茗囧菌
@Software: PyCharm
      
      转载请注明原作者
	  创作不易，仅供分享

"""
import requests
import re
import os

#   定义一个变量用来保存下载图片的张数
i = 1

#  定义下载图片的方法
def downloadPic(url):
    global i  # 使用global声明这是一个全局变量,方法内无法直接使用全局变量
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    html = requests.get(url=url,headers=headers,allow_redirects=False).text
    # pic_url = re.findall('"ObjURL":"(.*?)",', html, re.S)
    pic_url = re.findall('"hoverURL":"(.*?)",', html, re.S)

    for each in pic_url:
        print("正在下载第" + str(i) + "张图片,图片地址:" + each)

        try:
            pic = requests.get(each, timeout=5)  # 可能有些图片存在网址打不开的情况,这里设置一个5秒的超时控制
        except Exception:  # 出现异常直接跳过
            print("【错误】当前图片无法下载")
            continue  # 跳过本次循环

        #  定义变量保存图片的路径
        string = 'practice/17百度地图爬取/imgs/' + word + "/" + str(i) + ".jpg"
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':  # 主程序
    word = '挡风玻璃'

    #  先根据搜索的关键字判断存放该类别的文件夹是否存在,不存在则创建
    road = "practice/17百度地图爬取/imgs" + word

    if not os.path.exists(road):
        os.mkdir(road)
        ''' 
        https://image.baidu.com/search/acjson?tn=resultjson_com&logid=15929772079715400218&ipn=rj&ct=201326592&is=&fp=result&queryWord=' + word + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=' + word + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}
        '''
    #  根据输入的内容构建url列表推导式【前21页内容】
    urls = [
        'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=15929772079715400218&ipn=rj&ct=201326592&is=&fp=result&queryWord=' + word + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word=' + word + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}'.format(
            str(i)) for i in range(0, 60, 30)]

    for url in urls:
        downloadPic(url)

    print("下载完成!")