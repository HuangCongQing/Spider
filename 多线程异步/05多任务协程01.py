'''
Description: 多任务协程
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-09 16:48:00
FilePath: /Spider/多线程异步/05多任务协程01.py
'''
import asyncio
import time

async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码，那么就无法实现异步。
    # time.sleep(2)  # 相当于耗时2s
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)

start = time.time()
urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]

#任务列表：存放多个任务对象
stasks = []
for url in urls:
    c = request(url) # 返回的一个协程对象
    task = asyncio.ensure_future(c)  # task 任务对象
    stasks.append(task)

loop = asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks)) #封装到wait里面

print(time.time()-start) # 2.0020551681518555


