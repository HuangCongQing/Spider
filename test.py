'''
Description: 测试
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 11:49:42
LastEditTime: 2021-01-27 20:00:35
FilePath: /Spider/test.py
'''
for page in range(1,141):
    print(page)

#  根据输入的内容构建url列表推导式【前21页内容】
word = '挡风玻璃'
urls = [
    'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip&pn={}'.format(
        str(i)) for i in range(0, 400, 20)]
print(urls)