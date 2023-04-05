# https://github.com/VanilCitatka/china_parse_bot/blob/3bd9877adf/shop_parser/parser.py


#!/usr/bin/python3.9
import requests
import json
import datetime
from fake_useragent import UserAgent
import time
from random import randint
from to_csv.b_to_csv import b_main
from to_csv.c_to_csv import c_main
from to_csv.s_to_csv import s_main
from to_csv.w_to_csv import w_main


def createHeaders():
    # ua = UserAgent()
    # usag = ua.random
    headers = {
        'authority': 'www.szwego.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,de;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.szwego.com',
        'referer': 'https://www.szwego.com/static/index.html?t=1660503705068',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52',
        'wego-albumid': '',
        'wego-channel': 'net',
        'wego-staging': '0',
        'wego-uuid': '',
        'wego-version': '',
        'x-requested-with': 'XMLHttpRequest',
    }
    return headers


def createParams(alb: str, page: str, start_date: str):
    if page == '':
        params = {
            'albumId': f'{alb}',
            'searchValue': '',
            'searchImg': '',
            'startDate': f'{start_date}',
            'endDate': f'{datetime.date.today().strftime("%Y-%m-%d")}',
            'sourceId': '',
            'requestDataType': '',
            'transLang': 'en'
        }
    else:
        params = {
            'albumId': f'{alb}',
            'searchValue': '',
            'searchImg': '',
            'startDate': f'{start_date}',
            'endDate': f'{datetime.date.today().strftime("%Y-%m-%d")}',
            'sourceId': '',
            'slipType': '1',
            'timestamp': f'{page}',
            'requestDataType': '',
            'transLang': 'en'
        }
    return params


def createData(tag):
    data = {
        'tagList': f"[{tag}]"
    }
    return data


def downloadJson(alb, page, start_date):
    headers = createHeaders()
    params = createParams(alb, page, start_date)
    data = createData('')
    cookies = {
        'token': 'Mzk4MDk3Q0E5RTZCN0I1MkYwMTYwNDlCQUNFNkQ5QzVFOEZCOTI1OEEwOTA2MDc0QzUzRTVCNDVDMTg1RTgzRTZBNTY1MTZDQTNFNDFCRkI2ODZGRTgxRjQxRDU3MEZD',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221843714978b1d-0ab55794af05688-7d5d5476-1049088-1843714978d3f6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0MzcxNDk3OGIxZC0wYWI1NTc5NGFmMDU2ODgtN2Q1ZDU0NzYtMTA0OTA4OC0xODQzNzE0OTc4ZDNmNiJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221843714978b1d-0ab55794af05688-7d5d5476-1049088-1843714978d3f6%22%7D',
        'producte_run_to_dev_tomcat': '',
        'JSESSIONID': '7B6EC25F5883576484AD286AA2D83EA9',
    }
    url = 'https://www.szwego.com/album/personal/all'
    resp = requests.post(url, headers=headers, params=params, data=data, cookies=cookies)
    return resp.json()


def findPage(data):
    return data["result"]["pagination"]["pageTimestamp"]


def findLoadMore(data):
    return data["result"]["pagination"]["isLoadMore"]


async def collect_data(s_alb, s_start_date, msg):
    # try:
    alb_dict = {
        'A201803280031209720038067': 'b',
        'A2018031702370069766': 'c',
        'A2017120822295108026': 's',
        'A2017122802434822429': 'w'
    }

    LoadMore = True
    i = 1
    alb = s_alb
    page = ''
    category = alb_dict[f'{alb}']

    while LoadMore:
        data = downloadJson(alb, page, s_start_date)
        #тут вставить одну из трёх 把三个中的一个放进去。
        if category == 'b':
            b_main(data, i)
        elif category == 'c':
            c_main(data, i)
        elif category == 's':
            s_main(data, i)
        elif category == 'w':
            w_main(data, i)
        LoadMore = findLoadMore(data)
        if LoadMore == True:
            page = findPage(data)
        await msg.edit_text(f'Скачано: {i}{"."+"."*((2+i)%3)}')
        i += 1
        time.sleep(randint(1, 3))
    # except:
    #     print('сломалось')
    #     return False
    return True

def main():
    pass

if __name__ == '__main__':
    main()