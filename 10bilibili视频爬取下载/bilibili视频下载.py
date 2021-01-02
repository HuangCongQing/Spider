'''
Description: 视频下载 https://www.yuque.com/pythonpachong/learn/mkymo0
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-02 23:15:13
LastEditTime: 2021-01-02 23:18:08
FilePath: /Spider/10bilibili视频爬取下载/bilibili视频下载.py
'''
# -*- coding:utf-8 -*-
import re
import requests
import json
from jsonpath import jsonpath

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
}


def get_down_url(url):
    mp4_urls = []
    if re.search(r'av\d*', url):
        aid = re.search(r'av(\d*)', url).group()[2:]
        cid_url = 'https://www.bilibili.com/widget/getPageList?aid={}'.format(aid)
        cid_resp = requests.get(url=cid_url, headers=headers).json()
        cid = jsonpath(cid_resp, "$..cid")[0]
        bilbil_url = 'https://www.xbeibeix.com/api/bilibiliapi.php?aid={}&cid={}'.format(aid, cid)
        mp4_resp = requests.get(url=bilbil_url, headers=headers)
        # 响应时间
        # print(mp4_resp.elapsed)
        mp4_url = jsonpath(mp4_resp.json(), "$['url']")[0]
        mp4_urls.append(mp4_url)
        return mp4_urls
    else:
        bv_path = (re.search(r'BV\w*', url).group())
        av_url = 'https://api.bilibili.com/x/web-interface/view?bvid={}'.format(bv_path)
        av_resp = requests.get(url=av_url).json()
        aid = jsonpath(av_resp, "$['data']['aid']")[0]
        if re.search(r'\?p=\d*', url):
            p_tag = re.search(r'\?p=\d*', url).group()
            pid = int(re.search(r'\d+', p_tag).group()) - 1
            cid = jsonpath(av_resp, "$['data']['pages'][{}]['cid']".format(pid))[0]
            bilbil_url = 'https://www.xbeibeix.com/api/bilibiliapi.php?aid={}&cid={}'.format(aid, cid)
            mp4_resp = requests.get(url=bilbil_url, headers=headers)
            mp4_url = jsonpath(mp4_resp.json(), "$['url']")[0]
            mp4_urls.append(mp4_url)
        else:
            cids = jsonpath(av_resp, "$['data']['pages'][*]['cid']")
            for cid in cids:
                bilbil_url = 'https://www.xbeibeix.com/api/bilibiliapi.php?aid={}&cid={}'.format(aid, cid)
                mp4_resp = requests.get(url=bilbil_url, headers=headers)
                mp4_url = jsonpath(mp4_resp.json(), "$['url']")[0]
                mp4_urls.append(mp4_url)
        return mp4_urls


def down_mp4(port, key, video_urls):
    # video_urls = [
    #     "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_634b1aeaeb595b2e6fba89229ab2ad6a.mp4",
    #     "https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_b102d23686622da5134068cb3616b562.mp4"
    # ]
    aria2_url = "http://localhost:{}/jsonrpc".format(port)

    for index, videoss in enumerate(video_urls):
        jsonreq = json.dumps({
            "jsonrpc": "2.0",
            "method": "aria2.addUri",
            "id": index,
            "params": [
                "token:{}".format(key),
                [video_urls[index]],
                {}
            ]
        })

        c = requests.post(url=aria2_url, data=jsonreq)


if __name__ == '__main__':
    # aav_url = 'https://www.bilibili.com/video/av200764552'
    bv_url = 'https://www.bilibili.com/video/BV1g4411H78N?p=1'
    bv_url2 = 'https://www.bilibili.com/video/BV1AQ4y1N71n/?spm_id_from=333.788.videocard.1'
    # down_mp4(2800, 'werqrqrasfatertg', get_down_url(bv_url2))
    get_down_url(bv_url)