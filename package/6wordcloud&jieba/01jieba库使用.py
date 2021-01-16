'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 17:43:40
LastEditTime: 2021-01-16 20:34:49
FilePath: /Spider/package/6wordcloud&jieba/01jieba库使用.py
'''
import jieba
 
# text = open("test.txt","rb").read()
text = '发了困难看能否看上你分离开阿金发我我发往就鞥而过南人生观你是大V收代理费'
#结巴分词
wordlist = jieba.cut(text,cut_all=True)
wl = " ".join(wordlist)   #  空格分词
print(wl)#输出分词之后的txt