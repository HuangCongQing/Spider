'''
Description:  协程  参考：https://www.bilibili.com/video/BV1Yh411o7Sz?p=45
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-09 16:35:12
FilePath: /Spider/多线程异步/04协程.py
'''
import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功,',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
c = request('www.baidu.com')
# asyncio.run(c)  # 3.7版本可以直接这样用

# #1. 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# #将协程对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# # 2. task的使用
# loop = asyncio.get_event_loop()
# #基于loop创建了一个task对象
# task = loop.create_task(c)
# print(task)
#
# loop.run_until_complete(task)
#
# print(task)

# # 3. future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)



def callback_func(task):
    #result返回的就是任务对象中封装的协程对象对应函数的返回值
    print(task.result()) # task.result()就是 request(url)中的url   即： www.baidu.com

# # 4. 绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数callback_func绑定到任务对象中
task.add_done_callback(callback_func)
loop.run_until_complete(task)

