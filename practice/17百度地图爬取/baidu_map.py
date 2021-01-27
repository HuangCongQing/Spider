'''
Description: 百度地图爬取
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-27 18:43:38
LastEditTime: 2021-01-27 19:55:45
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
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

    for each in pic_url:
        print("正在下载第" + str(i) + "张图片,图片地址:" + each)

        try:
            pic = requests.get(each, timeout=5)  # 可能有些图片存在网址打不开的情况,这里设置一个5秒的超时控制
        except Exception:  # 出现异常直接跳过
            print("【错误】当前图片无法下载")
            continue  # 跳过本次循环

        #  定义变量保存图片的路径
        string = 'G:/Python/Crawler/百度图片下载器/' + word + "/" + str(i) + ".jpg"
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

    #  根据输入的内容构建url列表推导式【前21页内容】
    urls = [
        'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip&pn={}'.format(
            str(i)) for i in range(0, 400, 20)]

    for url in urls:
        downloadPic(url)

    print("下载完成!")