'''
Description:  https://blog.csdn.net/qiang12qiang12/article/details/71752222
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 17:44:54
LastEditTime: 2021-01-16 20:40:47
FilePath: /Spider/package/6wordcloud&jieba/03中文词云(wordcloud&jieba).py
'''
#-*-coding:utf-8-*-
 
###生成txt文件的词云
 
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import PIL.Image as image
import numpy as np
from cv2 import imread
import matplotlib.pyplot as plt
 
text = open("test.txt","rb").read()
#结巴分词
wordlist = jieba.cut(text,cut_all=True)
wl = " ".join(wordlist)   #  空格分词
# print(wl)#输出分词之后的txt
 
 
#把分词后的txt写入文本文件
#fenciTxt  = open("fenciHou.txt","w+")
#fenciTxt.writelines(wl)
#fenciTxt.close()
 
mask =plt.imread('heart.jpg')
#设置词云
wc = WordCloud(
                background_color = "black", #设置背景颜色
                # width=990,              #设置图片的宽度
                # height=440,              #设置图片的高度
                # margin=10,               #设置图片的边缘
               mask = mask,  #设置背景图片
            #    mask =imread("love.png"),  #设置背景图片  png不起作用
               max_words = 2000, #设置最大显示的字数
               #stopwords = "", #设置停用词
               font_path = "alibaba.ttf",
        #设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size = 50,  #设置字体最大值
               random_state = 30, #设置有多少种随机生成状态，即有多少种配色方案
               scale=3,  # 数字越大越清晰 
    )
myword = wc.generate(wl)#生成词云
 
#改变字体颜色
img_colors = ImageColorGenerator(mask)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)

 
#展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()