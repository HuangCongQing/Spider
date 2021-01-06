# /*
#  * @Author: HCQ
#  * @Date: 2018-05-26 22:10:15
#  * @Last Modified by: HCQ
#  * @Last Modified time: 2018-05-26 22:16:41
#  */
# /*
# 简介
# 通过 Python 制作网络爬虫，爬取豆瓣电影评论，并分析然后制作豆瓣影评的云图
# 参考链接：https: // mp.weixin.qq.com/s/uTIhyNVE7W6mGMneSKQNlw
#  */
import jieba
import requests
import pandas as pd
import time
import random
from lxml import etree

# 我想从影评首页开始爬取，爬取入口是：https: // movie.douban.com/subject/24773958/comments?status = P，然后依次获取页面中下一页的 url 地址以及需要爬取的内容，接着继续访问下一个页面的地址。


def start_spider():
   base_url = 'https://movie.douban.com/subject/24773958/comments'
   start_url = base_url + '?start=0'

   number = 1
   html = request_get(start_url)

   while html.status_code == 200:
       # 获取下一页的 url
       selector = etree.HTML(html.text)
       nextpage = selector.xpath(
           "//div[@id='paginator']/a[@class='next']/@href")
       nextpage = nextpage[0]
       next_url = base_url + nextpage
       # 获取评论
       comments = selector.xpath("//div[@class='comment']")
       marvelthree = []
       for each in comments:
           marvelthree.append(get_comments(each))

       data = pd.DataFrame(marvelthree)
       # 写入csv文件,'a+'是追加模式
       try:
           if number == 1:
               csv_headers = ['用户', '是否看过', '五星评分', '评论时间', '有用数', '评论内容']
               data.to_csv('./Marvel3_yingpping.csv', header=csv_headers,
                           index=False, mode='a+', encoding='utf-8')
           else:
               data.to_csv('./Marvel3_yingpping.csv', header=False,
                           index=False, mode='a+', encoding='utf-8')
       except UnicodeEncodeError:
           print("编码错误, 该数据无法写到文件中, 直接忽略该数据")

       data = []

       html = request_get(next_url)


# 我在请求头中增加随机变化的 User-agent, 增加 cookie。最后增加请求的随机等待时间，防止请求过猛被封 IP。
def request_get(url):
    '''
    使用 Session 能够跨请求保持某些参数。
    它也会在同一个 Session 实例发出的所有请求之间保持 cookie
    '''
    timeout = 3
    UserAgent_List = [
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
    ]

    header = {
        'User-agent': random.choice(UserAgent_List),
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/subject/24773958/?from=showing',
    }

    session = requests.Session()

    cookie = {
        'cookie': "wsgxhse46y5uthdsgzrefg",
        # 'cookie': "你的 cookie 值",
    }

    time.sleep(random.randint(5, 15))  
    response = requests.get(url, headers=header, cookies=cookie, timeout = 3)  # cookies值
    if response.status_code != 200:
        print(response.status_code)
    return response

# 数据获取：
def get_comments(eachComment):
    commentlist = []
    user = eachComment.xpath("./h3/span[@class='comment-info']/a/text()")[0]  # 用户
    watched = eachComment.xpath("./h3/span[@class='comment-info']/span[1]/text()")[0]  # 是否看过
    rating = eachComment.xpath("./h3/span[@class='comment-info']/span[2]/@title")  # 五星评分
    if len(rating) > 0:
        rating = rating[0]

    comment_time = eachComment.xpath("./h3/span[@class='comment-info']/span[3]/@title")  # 评论时间
    if len(comment_time) > 0:
        comment_time = comment_time[0]
    else:
        # 有些评论是没有五星评分, 需赋空值
        comment_time = rating
        rating = ''

    votes = eachComment.xpath("./h3/span[@class='comment-vote']/span/text()")[0]  # "有用"数
    content = eachComment.xpath("./p/text()")[0]  # 评论内容

    commentlist.append(user)
    commentlist.append(watched)
    commentlist.append(rating)
    commentlist.append(comment_time)
    commentlist.append(votes)
    commentlist.append(content.strip())
    # print(list)
    return commentlist

# 制作云图
def split_word():
        with codecs.open('Marvel3_yingpping.csv', 'r', 'utf-8') as csvfile:
            reader = csv.reader(csvfile)
            content_list = []
            for row in reader:
                try:
                    content_list.append(row[5])
                except IndexError:
                    pass

            content = ''.join(content_list)

            seg_list = jieba.cut(content, cut_all=False)
            result = '\n'.join(seg_list)
            print(result)

# 运行
if __name__ == '__main__':
    start_spider()
    request_get()
    get_comments()
    split_word()
