'''
Description: https://blog.csdn.net/waple_0820/article/details/70049953
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 21:50:27
LastEditTime: 2021-01-16 21:52:29
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