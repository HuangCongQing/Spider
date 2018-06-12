# /* 网址：https://zhuanlan.zhihu.com/p/36803496
#  * @Author: HCQ 
#  * @Date: 2018-06-03 21:52:59 
#  * @Last Modified by:   HCQ 
#  * @Last Modified time: 2018-06-03 21:52:59 
#  */

# 首先是导入我们要用到的包：
import warnings
warnings.filterwarnings("ignore")  # 忽略警告信息
import jieba  # 这里我们用jieba分词
import pandas as pd  # 分词需要用到的包
import numpy
import codecs
import re  # 正则表达式
import matplotlib  # 用于创建图表的绘图包
import matplotlib.pyplot as plt
from urllib import request
from bs4 import BeautifulSoup as bs
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)  # 指定图片像素
from wordcloud import WordCloud  # 词云包

# 爬取评论函数
def getCommentsById(movieId, pageNum):  # 用电影ID和页数作为参数
    eachCommentList = []
    if pageNum > 0:
         start = (pageNum-1) * 20
    else:
        return False
    requrl = 'https://movie.douban.com/subject/' + movieId + \
        '/comments' + '?' + 'start=' + str(start) + '&limit=20'
    print(requrl)
    resp = request.urlopen(requrl)
    html_data = resp.read().decode('utf-8')
    soup = bs(html_data, 'html.parser')
    comment_div_lits = soup.find_all('div', class_='comment')
    for item in comment_div_lits:
        if item.find_all('p')[0].string is not None:
            eachCommentList.append(item.find_all('p')[0].string)
    return eachCommentList

# 获取评论并显示词云图


def main():
    #循环获取复联3的前10页评论，超过10页会报错error : HTTP 403 Forbidden，因为只是爬着玩的，就先不管了
    commentList = []
    for i in range(10):
        num = i + 1
        commentList_temp = getCommentsById(
            '24773958', num)  # 打开复联3的豆瓣网页，找到movieId=24773958
        commentList.append(commentList_temp)
    #将列表中的数据转换为字符串
    comments = ''
    for k in range(len(commentList)):
        comments = comments + (str(commentList[k])).strip()

    #数据清洗
    #使用正则表达式去除标点符号
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    filterdata = re.findall(pattern, comments)
    cleaned_comments = ''.join(filterdata)
    #使用结巴分词进行中文分词
    segment = jieba.lcut(cleaned_comments)
    words_df = pd.DataFrame({'segment': segment})
    #去掉停用词，stopwords.txt是中文停用词表，随便百度一下就可以找到，放在程序的原根目录里     stopwords=pd.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
    words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
    #统计词频
    words_stat = words_df.groupby(by=['segment'])[
                                  'segment'].agg({"计数": numpy.size})
    words_stat = words_stat.reset_index().sort_values(
        by=["计数"], ascending=False)
    #用词云进行显示，heiti.ttf是字体文件，同样需要放在根目录
    wordcloud=WordCloud(font_path="heiti.ttf",background_color="white",max_font_size=80)
    word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}

    word_frequence_list = []
    for key in word_frequence:
        temp = (key,word_frequence[key])
        word_frequence_list.append(temp)
    wordcloud=wordcloud.fit_words(word_frequence)
    plt.imshow(wordcloud)
    plt.show()    #对图片进行显示
