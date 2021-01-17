'''
Description: 字符串匹配
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-17 20:18:30
LastEditTime: 2021-01-17 20:21:33
FilePath: /Spider/package/4re正则表达式/re基础/01string匹配.py
'''
#  python re 模块 findall 函数用法简述
# https://blog.csdn.net/Cashey1991/article/details/8875213?
import re
s = "adfad asdfasdf asdfas asdfawef asd adsfas "
 
reObj1 = re.compile('((\w+)\s+\w+)')
print(reObj1.findall(s))
# [('adfad asdfasdf', 'adfad'), ('asdfas asdfawef', 'asdfas'), ('asd adsfas', 'asd')]
 
reObj2 = re.compile('(\w+)\s+\w+')
print(reObj2.findall(s))
# ['adfad', 'asdfas', 'asd']
 
reObj3 = re.compile('\w+\s+\w+')
print(reObj3.findall(s))
# ['adfad asdfasdf', 'asdfas asdfawef', 'asd adsfas']

''' 
按以上代码例子讲解：


findall函数返回的总是正则表达式在字符串中所有匹配结果的列表，此处主要讨论列表中“结果”的展现方式，即findall中返回列表中每个元素包含的信息。


@1.当给出的正则表达式中带有多个括号时，列表的元素为多个字符串组成的tuple，tuple中字符串个数与括号对数相同，字符串内容与每个括号内的正则表达式相对应，并且排放顺序是按括号出现的顺序。

@2.当给出的正则表达式中带有一个括号时，列表的元素为字符串，此字符串的内容与括号中的正则表达式相对应（不是整个正则表达式的匹配内容）。

@3.当给出的正则表达式中不带括号时，列表的元素为字符串，此字符串为整个正则表达式匹配的内容

 '''