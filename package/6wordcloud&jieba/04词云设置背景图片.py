'''
Description: 参考：https://blog.csdn.net/fly910905/article/details/77763086
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-16 20:12:07
LastEditTime: 2021-01-16 20:26:08
FilePath: /Spider/package/6wordcloud&jieba/04词云设置背景图片.py
'''
"""
@author:FLY
@software:PyCharm
@time:2017/08/24
"""
import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = ''
with open('test.txt', 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
        print(line)
# sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串
text += ' '.join(jieba.cut(line))
backgroud_Image = plt.imread('heart.jpg')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(
    background_color='white',# 设置背景颜色
    mask=backgroud_Image,# 设置背景图片
    font_path= "alibaba.ttf",  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=2000, # 设置最大现实的字数
    stopwords=STOPWORDS,# 设置停用词
    max_font_size=150,# 设置字体最大值
    random_state=30# 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(text)
print('开始加载文本')
#改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
d = path.dirname(__file__)
# os.path.join()：  将多个路径组合后返回
wc.to_file(path.join(d, "h11.jpg"))
print('生成词云成功!')