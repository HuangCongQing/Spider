'''
Description:  参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=48
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-09 17:13:30
FilePath: /Spider/多线程异步/07aiohttp实现多任务异步协程.py
'''
#环境安装：pip install aiohttp
#使用该模块中的ClientSession
import requests
import asyncio
import time
import aiohttp

start = time.time()
# urls = [
#     'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#     'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/jay', 'http://127.0.0.1:5000/tom',
#
# ]
from multiprocessing.dummy import Pool
pool = Pool(2)

urls = []
for i in range(10):
    urls.append('http://127.0.0.1:5000/bobo')
print(urls)
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        #get()、post():
        #headers,params/data,proxy='http://ip:port'
        async with await session.get(url) as response: # 发送get请求
            #text()返回字符串形式的响应数据
            #read()返回的二进制形式的响应数据   不是content
            #json()返回的就是json对象
            #注意：获取响应数据操作之前一定要使用await进行手动挂起
            page_text = await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(tasks))

end = time.time()

print('总耗时:',end-start)


''' 
['http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo', 'http://127.0.0.1:5000/bobo']
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
Hello bobo
总耗时: 2.0302047729492188

 '''