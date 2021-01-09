'''
Description: 参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=47
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-09 17:00:22
FilePath: /Spider/多线程异步/06多任务异步协程02.py
'''
import requests
import asyncio
import time

start = time.time()
urls = [
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]

async def get_page(url):
    print('正在下载',url)
    #requests.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
    #aiohttp:基于异步网络请求的模块
    response = requests.get(url=url)
    print('下载完毕：',response.text)

tasks = [] # 任务列表

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks)) # 不能直接使用tasks

end = time.time()

print('总耗时:',end-start)

''' 
正在下载 http://127.0.0.1:5000/bobo
下载完毕： Hello bobo
正在下载 http://127.0.0.1:5000/jay
下载完毕： Hello jay
正在下载 http://127.0.0.1:5000/tom
下载完毕： Hello tom
总耗时: 6.012814044952393  ？？？？？？？？？？？？？？？？？？？？
 '''