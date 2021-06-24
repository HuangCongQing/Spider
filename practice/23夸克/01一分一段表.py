
# https://quark.sm.cn/api/rest?uc_param_str=dnntnwvepffrgibijbprsvdsdicheiniut&from=gaokao_share&method=QuarkGaoKao2020.index&format=html#/grade-interval?location=%E5%9B%9B%E5%B7%9D&student_rank=110757&score=500&aos=%E7%90%86%E7%A7%91&subjects=%E7%90%86%E7%A7%91&fromPT=share





import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd
import tqdm

def get_score():
    print('开始爬取数据...')
    # 存储数据初始化
    # 参数
    lists_numbers = []
    lists_score = []
    lists_sum = []
    
    lists_aos = []
    lists_location = []
    # 获取数据
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'cookie': 'sm_uuid=bd2dbc6997b57f485ca9ff20f6b86ad0%7C%7C%7C1615118650; sm_diu=bd2dbc6997b57f485ca9ff20f6b86ad0%7C%7C11eef17471c3abfcac%7C1624423149; PHPSESSID=aandevlo1hb3407k1p85dqafv8; sm_sid=a986bc52b80ad1cd753c1c3edf085c3b; phid=dab2f2cd098d3ab7df6c44f27c376997',
        'referer': 'https://quark.sm.cn/api/rest?uc_param_str=dnntnwvepffrgibijbprsvdsdicheiniut&from=gaokao_share&method=QuarkGaoKao2020.index&format=html',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    aos= ['理科', '文科']
    year = '2021'
    location = ['北京', '天津', '上海', '重庆', '河北', '山西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东', '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '内蒙古', '广西', '西藏', '宁夏', '新疆']
    for item1 in location: 
        for item2 in aos: 
            url = 'https://quark.sm.cn/api/rest?format=json&uc_param_str=dnntnwvepffrgibijbprsvdsdicheiniut&method=QuarkGaoKao2020.getScoreRanksNew&aos='+ str(item2) + '&year=' + str(year)+ '&location='+str(item1)+'&score='
            #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
            response = requests.get(url=url, headers=headers)
            response.encoding = 'utf-8' 
            content = response.content
            # json格式转为字典
            result = json.loads(content)
            # print(result)
            print("爬取省份：",item1)
            print("爬取分数段总数：",len(result['data']['scores_and_ranks']))
            for item in result['data']['scores_and_ranks']: 
                lists_numbers.append(item["numbers"])
                lists_score.append(item["score"])
                lists_sum.append(item["sums"])
                lists_aos.append(item2)
                lists_location.append(item1)
    
    dest = []
    for e in lists_location:
        if e not in dest:
            dest.append(e)
    print("分数线已出省：", [*dest])
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'省份':lists_location,'年份':2021,'文理综合':lists_aos,'当前分数人数':lists_numbers,'分数':lists_score,'总人数':lists_sum})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"一分一段表（2021）.csv",index=False, sep=',')
    print('爬取结束',)
    """ 
    处理数据
    """
    
    # 保存csv文件
    # print('保存csv文件...')
    # #字典中的key值即为csv中列名
    # dataframe = pd.DataFrame({'专业批次':label_list,'学校':title_list,'特色专业':content_list})
    # #将DataFrame存储为csv,index表示是否显示行名，default=True
    # dataframe.to_csv(r"特色专业数据20210516.csv",index=False, sep=',')
    # print('爬取结束',)


    
if __name__ == "__main__":
    get_score()

