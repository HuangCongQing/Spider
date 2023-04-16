'''
Description: 测试
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 11:49:42
LastEditTime: 2023-04-17 00:09:29
FilePath: \Spider-1\test.py
'''


import re
import requests
import json
import time
from urllib import parse
import glob
import os
from tqdm import tqdm
import datetime # 时间戳
import random # 随机选择headers


# for page in range(1,141):
#     print(page)

# #  根据输入的内容构建url列表推导式【前21页内容】
# word = '挡风玻璃'
# urls = [
#     'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip&pn={}'.format(
#         str(i)) for i in range(0, 400, 20)]
# print(urls)



str  = "珍藏收老宫廷摆放纯铜纯手工打造紫铜鎏金鎏银镶嵌宝石地藏王菩萨一尊_重:3026克_高:30厘米_宽:22厘米_1000元_003380"
str =  re.sub("[\/\\\:\*\?\"\<\>\|]", '_',str) # 
print(str)