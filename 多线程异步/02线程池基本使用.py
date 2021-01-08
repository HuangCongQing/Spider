'''
Description: 线程池基本使用
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-08 23:40:29
FilePath: /Spider/多线程异步/02线程池基本使用.py
'''
# import time
# #使用单线程串行方式执行
#
# def get_page(str):
#     print("正在下载 ：",str)
#     time.sleep(2)
#     print('下载成功：',str)
#
# name_list =['xiaozi','aa','bb','cc']
#
# start_time = time.time()
#
# for i in range(len(name_list)):
#     get_page(name_list[i])
#
# end_time = time.time()
# print('%d second'% (end_time-start_time))

import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载 ：",str)
    time.sleep(2)  # 2s
    print('下载成功：',str)

name_list =['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4)
#将列表中每一个列表元素传递给get_page进行处理。
pool.map(get_page,name_list)  # 函数 ，参数,   若有返回值一定是个列表
pool.close()
pool.join()
end_time = time.time()
print(end_time-start_time) # 2.006852149963379



