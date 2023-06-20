import  requests
import json
import pandas as pd
from tqdm import tqdm

def save_csv(**kwargs):
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame(kwargs)
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"09武书连中国大学排名2023.csv",index=False, sep=',')

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Host': 'mallapi.wurank.net',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.wurank.net/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        "Content-Type":"application/json" # fix: response status code 415

    }

    rank_list = [] # 学科类别
    school_list = [] # 学科级别
    year_list = [] # 学科名
    cur_year = 2023

    for page in tqdm(range(1, 42)):
        PageIndex = page
        PageSize = 20
        filter = f"intYear={cur_year}"
        sort =  "intVictorOrder=0"
        # payloadData数据
        payloadData = {
                    'PageIndex':PageIndex,
                    'PageSize': PageSize,
                    'filter': f'{filter}',
                    'sort': f'{sort}',
        }
        data = json.dumps(payloadData)

        post_url = 'https://mallapi.wurank.net/RankApi/SearchApi/GetChineseUniDataPageList/chineseunidata'
        response = requests.post(url=post_url,headers=headers, data=data)
        # print(response.status_code)
        json_data = json.loads(response.text)
        # print(len(json_data['data']))
        for cur_data in json_data['data']:
            # print(cur_data[ "victororder"])
            # print(cur_data[ "schchnname"])
            rank_list.append(cur_data[ "victororder"] if cur_data[ "victororder"] != 0 else '700+')
            school_list.append(cur_data[ "schchnname"])
            year_list.append(cur_year)
    
    # 保存csv文件
    kwargs = {'rank':rank_list,
            'school':school_list,
            'year':year_list}
    save_csv(**kwargs)
    
    
    # json_data = response.json()
    # print(json_data)