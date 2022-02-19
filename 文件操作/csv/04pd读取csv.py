'''
Description: https://blog.csdn.net/waple_0820/article/details/70049953
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 21:50:27
LastEditTime: 2022-02-19 23:19:48
FilePath: /Spider/文件操作/csv/04pd读取csv.py
'''
import pandas as pd
data = pd.read_csv('03保存test.csv')
print(data)
# 会得到一个DataFrame类型的data，不熟悉处理方法可以参考pandas十分钟入门: https://www.cnblogs.com/chaosimple/p/4153083.html

''' 
   a_name  b_name
0       0       5
1       1       6
2       2       7
3       3       8
4       4       9
 '''
#  获得行数
print(len(data))
# 遍历每行的每个元素
for i  in range(0, len(data)):
   #  每列的表头
   print(data['a_name'][i], data['b_name'][i] )