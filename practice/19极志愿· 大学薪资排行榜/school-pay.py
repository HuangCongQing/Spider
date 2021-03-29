'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-03-28 18:02:31
LastEditTime: 2021-03-29 20:01:22
FilePath: /Spider/practice/19极志愿· 大学薪资排行榜/school-pay.py
'''


import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd

def get_school_pay():
    # 存储数据初始化
    school_list = []
    pay_list =[]
    # 获取数据
    # 本科url
    url_list = [
        "https://www.jizhy.com/open/sch/salary-rank-list?page=1&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995018315&platform=desktop&v=210&sign=0DFCDBCB869FBD104A53F87CBD8607CA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=2&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616920394813&platform=desktop&v=210&sign=C68954F81BBFD6C84465E136483B2081",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=3&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616992846730&platform=desktop&v=210&sign=1120C348FA3C7166989063CA309F6B5D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=4&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616992851578&platform=desktop&v=210&sign=097107B821C6C644B4A38E2ED6867BB5",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=5&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993195173&platform=desktop&v=210&sign=AB49297A1549CD5E4B2EB1194AB55B32",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=6&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993200073&platform=desktop&v=210&sign=FFF060BDFFCEEE824BA756FF4757D5BA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=7&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993204032&platform=desktop&v=210&sign=DED3E50BD7774CAB69DFD589888D5DDB",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=8&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993208164&platform=desktop&v=210&sign=0450643623BA615F1A77117359C4F949",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=9&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993931654&platform=desktop&v=210&sign=F7A1D431B6378DD4C7309494B63A7D08",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=10&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993940375&platform=desktop&v=210&sign=83D9BB93C49CC953FC4C6AE892B50DAD",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=11&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993978810&platform=desktop&v=210&sign=AEB11E678F4F7BA9724B0225FCC1FE85",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=12&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993988351&platform=desktop&v=210&sign=C8CBAC0A580EEBA4F856043F7DFBCEF1",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=13&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993991998&platform=desktop&v=210&sign=5DB321FB702E2A59B4388B106D9C887E",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=14&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993995131&platform=desktop&v=210&sign=3C6824D3C3823B3C8C30B022FBBF8517",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=15&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616993997900&platform=desktop&v=210&sign=9FD787AECFA4F943CEDCE333D6116A21",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=16&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994083836&platform=desktop&v=210&sign=8B2DC0FDBB47581B1963C0595E9C37C2",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=17&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994088177&platform=desktop&v=210&sign=4503DCA76C8E92DC52E629BD42C7BCDA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=18&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994090656&platform=desktop&v=210&sign=DEB7AC2C00462230EEDC859EF264B16E",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=19&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994095051&platform=desktop&v=210&sign=64374F716E827B3E4BFA3D9F6BDDABE3",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=20&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994101134&platform=desktop&v=210&sign=B32BC8FC01D210C4AB7C192389D006C5",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=21&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994350804&platform=desktop&v=210&sign=40A7FCEBD7688A14BFC853A89628A422",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=22&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994354343&platform=desktop&v=210&sign=2AB662254BDF3B7A3EFF7173AE5480D3",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=23&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994357846&platform=desktop&v=210&sign=D1979DB69BE50B41173E774DC986B222",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=24&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994360943&platform=desktop&v=210&sign=2A66214F374CEF78C6C6ABABB0EBD50B",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=25&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994363764&platform=desktop&v=210&sign=4CEBC2DFBFAE6267EC8D5CDCECF1E2DE",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=26&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994435630&platform=desktop&v=210&sign=13E175F005BD4C896745184721A46D8A",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=27&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994441959&platform=desktop&v=210&sign=F4973433067EDA93BBDB18E2982AAAD3",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=28&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994445147&platform=desktop&v=210&sign=C51639B4F1260BB661ACF2BD076FEE9D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=29&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994447678&platform=desktop&v=210&sign=A9E6115ED910454567C405DD422933C9",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=30&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994450129&platform=desktop&v=210&sign=694F944600458D7204EF6ABE10EF5CD2",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=31&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994510446&platform=desktop&v=210&sign=0FF0211E3CF495905B99C7E736A943FA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=32&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994514238&platform=desktop&v=210&sign=6421837D51445D1B742838B25F2021EB",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=33&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994516594&platform=desktop&v=210&sign=2D72A2AF04AC144E2BCB51F4E958ECFA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=34&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994519640&platform=desktop&v=210&sign=F367A0CC0E3083A48530ACDD71A8E039",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=35&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994522331&platform=desktop&v=210&sign=6F8DCBFDB40909E1419EE5E995AD566C",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=36&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994603795&platform=desktop&v=210&sign=8285F49160097FDD6E99C72802B39F5A",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=37&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994607949&platform=desktop&v=210&sign=5F055C4C49E0B8A8B3CB617BFD3B6C82",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=38&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994611060&platform=desktop&v=210&sign=783F7C41764C83555411BD8622FE6A7E",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=39&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994613460&platform=desktop&v=210&sign=1B25953E5285064A3EF0F3C8E4FDB3CF",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=40&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994616012&platform=desktop&v=210&sign=98C7F18B8651D3EA2DD4619BC3AA660C",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=41&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994676972&platform=desktop&v=210&sign=529F19B06BC3F94A52B9829A1D948D3C",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=42&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994681670&platform=desktop&v=210&sign=2BDD6C0C4642D5F1BC78A1F162057DB7",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=43&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994684882&platform=desktop&v=210&sign=331686503FC71ECBA75823C838FEA169",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=44&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994687689&platform=desktop&v=210&sign=9F8B6367C5169119A61139DD2581BF60",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=45&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994690691&platform=desktop&v=210&sign=D63DCF4E3A762793A731EA3D6020461C",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=46&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994795390&platform=desktop&v=210&sign=8300D03F2F80441838323089733E10BD",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=47&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994798587&platform=desktop&v=210&sign=188915B7FF67685B2A0461DFFE76B724",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=48&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994801298&platform=desktop&v=210&sign=9C11DA855EC88EF982660087C1E73933",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=49&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994804823&platform=desktop&v=210&sign=8FFC5D81EDFABADC09A6DB242938F78E",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=50&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994808753&platform=desktop&v=210&sign=81D09D57AAFA56C77B7392528A2855C7",

    ]
    # 专科url
    
    url_list1 = [
        "https://www.jizhy.com/open/sch/salary-rank-list?page=1&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616994932427&platform=desktop&v=210&sign=A8FF3B24803FB0B9350F1B8EA2D588BD",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=2&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995121125&platform=desktop&v=210&sign=01494A28E8FF801D5673FBC424AF846D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=3&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995131610&platform=desktop&v=210&sign=540419B42C45C9528229605295C93C84",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=4&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995134300&platform=desktop&v=210&sign=04922E8FE8B85D0D3B821405EFE7FDDE",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=5&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995138208&platform=desktop&v=210&sign=BF27F7D598B5CC2429D02A9371865697",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=6&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995198247&platform=desktop&v=210&sign=38E9990C6C60606ACD796BC7FA640D7D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=7&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995201372&platform=desktop&v=210&sign=A28B478206B9673F75A7D0D5C41ECD13",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=8&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995204468&platform=desktop&v=210&sign=1CFBB3576B054725C893745F42D9F145",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=9&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995389437&platform=desktop&v=210&sign=F0F7273145ED400D4D533DCB20F5DC28",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=10&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995391946&platform=desktop&v=210&sign=9F491592F865310FCB99A5966F76A2B1",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=11&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995473582&platform=desktop&v=210&sign=E8FE262D5D816885AAFF69FBEB83FAA7",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=12&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995476251&platform=desktop&v=210&sign=955C922C05B46C7101BF2A6931CE320D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=13&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995478418&platform=desktop&v=210&sign=B1A77B30BB78C1CD12AC69E8DE347488",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=14&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995480886&platform=desktop&v=210&sign=FD24B26B79DFF0A189C20EAB2E848E49",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=15&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995482996&platform=desktop&v=210&sign=8757CDB8741EFC5AE73565C1F5F92C33",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=16&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995492309&platform=desktop&v=210&sign=051AC84B25C880032B3F084878E81D5D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=17&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995495260&platform=desktop&v=210&sign=CD34D6E0B1594B69DCB381906D54EEBA",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=18&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995595377&platform=desktop&v=210&sign=3803CA636581F86CBF2E5B3D723A683F",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=19&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995598262&platform=desktop&v=210&sign=7131BB3218CCAE098F1F017A42080EE4",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=20&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995600763&platform=desktop&v=210&sign=CE22D71D7C2BD4F498E25EFE33FC0DD0",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=21&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995644350&platform=desktop&v=210&sign=E5F46546B4671A5568B393575BABF46D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=22&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995646568&platform=desktop&v=210&sign=1B0AEF890D8CEDA960422C83C57F2CDB",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=23&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995648678&platform=desktop&v=210&sign=4E7C4D084AC84C8D32B3D606562EBA0B",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=24&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995651428&platform=desktop&v=210&sign=BE6E2BC426761D7783E22919D36C20F1",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=25&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995654401&platform=desktop&v=210&sign=FD11296813A03CFC44BFEDA6CADD7FAF",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=26&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995740271&platform=desktop&v=210&sign=7CD3B36E1DFE47ADFAE7DAEBDE89363F",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=27&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995743010&platform=desktop&v=210&sign=04AF64F76F5F1594E95F282086D3E0AB",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=28&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995745432&platform=desktop&v=210&sign=40A4ED2ACF121BD911EC62D5B13F8216",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=29&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995747791&platform=desktop&v=210&sign=C57109EB71186001E2F0F03E7920C00D",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=30&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995750662&platform=desktop&v=210&sign=876BB6B37A276D542AB2142D7256EDC9",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=31&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995809072&platform=desktop&v=210&sign=474CA5C42F2EB8CEBE63C93436EDD630",
        "https://www.jizhy.com/open/sch/salary-rank-list?page=32&page_len=20&diploma_id=5&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts=1616995811972&platform=desktop&v=210&sign=ADB4AE2ABBF2D7025B8EC6EB63BBC66D",
    ]
    for url in url_list1: # 0-2800
        print("正在获取：", url)
        #UA伪装：将对应的User-Agent封装到一个字典中
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }
        # url = 'https://www.jizhy.com/open/sch/salary-rank-list?page='+ str(page) +  '&page_len=20&diploma_id=7&wenli=0&app_id=98357f659cf8fb6001cff80f7c6b85f2&ts='+ str(ts) +  '&platform=desktop&v=210&sign='+ str(sign)
        # url = 'https://api.eol.cn/gkcx/api/?access_token=&keyword=&level1=' + str(1)  + '&level2=&page='+ str(26) +'&signsafe=&size=30&uri=apidata/api/gkv3/special/lists'
        #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
        # print("访问url：", url)
        response = requests.get(url=url,headers=headers, timeout=60)
        response.encoding = 'utf-8' 
        content = response.content
        # json格式转为字典
        result = json.loads(content)
        # print("结果：",result)
        # print("爬取专业数：",len(result['data']['item']))
        
        for item in range(0,len(result['data'])): 
            print("爬取薪资:", result['data'][item]['salary'])
            school = result['data'][item]['sch_name']
            pay = result['data'][item]['salary']
            school_list.append(school)
            pay_list.append(pay)
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'学校':school_list,'薪资':pay_list})
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(r"中国大学薪资2020排行榜(专科).csv",index=False, sep=',')
    print('爬取结束',)

    
if __name__ == "__main__":
    get_school_pay()