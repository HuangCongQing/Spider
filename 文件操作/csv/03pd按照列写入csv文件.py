'''
Description: 参考：https://blog.csdn.net/weixin_43245453/article/details/90054820?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 21:40:14
LastEditTime: 2021-01-16 21:41:20
FilePath: /Spider/文件操作/csv/03python按照列写入csv文件.py
'''
import pandas as pd
#a和b的长度必须保持一致，否则报错
a = [x for x in range(5)]
b = [x for x in range(5,10)]
#字典中的key值即为csv中列名
dataframe = pd.DataFrame({'a_name':a,'b_name':b})

#将DataFrame存储为csv,index表示是否显示行名，default=True
dataframe.to_csv(r"03保存test.csv",sep=',')

