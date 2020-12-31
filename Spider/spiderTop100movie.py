# -*- coding: utf-8 -*-
'''
Created on 2017年8月21日

@author: hasee
'''
import json
import requests
# 引入异常处理模块
from requests.exceptions import RequestException
import re
# 多线程，秒传
from multiprocessing import Pool


def get_one_page(url):
    try:# 获取数据异常判断
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


# 解析网页
def parse_one_page(html):
    # .*? 匹配任意字符
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?in'
                         'teger">(.*?)</i>.*?fraction">(.*?)</i>', re.S) # re.S匹配任意字符

    items = re.findall(pattern, html)
#这一步生成的其实是由元组组成的列表，列表的每一个元素是元组，元组则有前面正则表达式提取的电影名称，地址，演员名，上映时间，排序，评分等，这个列表怎么用，是一个很重要的问题
    print(items)
    # 将解析的结果格式化
    # 字典的形式，yield生成器
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],# 切片，去掉一些东西
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }

# 存储到文件里
def write_to_file(content): # encoding='utf-8'，，ensure_ascii=False，编码 编成汉字
    with open("Top100Movie.txt", 'a', encoding='utf-8') as f:
        #当重新打开的时候，由于文件是gbk编码的，默认用gbk去打开，而此时打开的是unicode，所以无法打开，解决的方法是改变目标文件的编码
        f.write(json.dumps(content, ensure_ascii=False)+'\n')# 字典传字符串
        f.close()


# 以offset作为参数，实现分页抓取数据
def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    #     获得完整的网页
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
#     for i in range(10):
#         main(i*10)

# 下面利用进程池爬数据，速度快
    pool = Pool()
    pool.map(main,[x*10 for x in range(10)])




