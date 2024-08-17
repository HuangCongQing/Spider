import requests
from bs4 import BeautifulSoup
from lxml import etree
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re
import pandas as pd
from tqdm import tqdm

isis = {
    "ID5": [],
    "TITLE": [],
    "Date": [],
    "Lat/Lon": [],
    "Land use_Status of vegetation; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)": [],
    "Land use_Remarks on Land Use / Vegetation": [],
    "Land use_Major vegetation type; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)": [],
    "Land use_Land use or vegetation in the immediate vicinity of the site": [],
    "Land use_Major crops": [],
    "Classification_WRB 2006": [],
    "Classification_WRB 1998": [],
    "Classification_FAO-UNESCO-ISRIC 1974": [],
    "Classification_FAO-UNESCO-ISRIC 1988": [],
    "Chemical characteristics-Depth (cm)": [],
}


ids = ['AU003', 'AU004', 'AU005', 'AU006', 'AU008', 'AU009', 'AU010', 'AU011', 'AU015', 'AU017', 'AU018', 'AU019', 'AU023', 'AU024', 'AU025', 'AU029', 'AU031', 'AU033', 'AU039', None, 'BJ001', 'BJ002', 'BJ003', 'BJ004', 'BR001', 'BR002', 'BR003', 'BR004', 'BR005', 'BR006', 'BR007', 'BR008', 'BR009', 'BR010', 'BR011', 'BR012', 'BR013', 'BR014', 'BR015', 'BR016', 'BR017', 'BR018', 'BR019', 'BR020', 'BR021', 'BR022', 'BR023', 'BR024', 'BR025', 'BR026', 'BR027', 'BR028', 'BR029', 'BW002', 'BW003', 'BW004', 'BW005', 'BW006', 'BW007', 'BW1', 'BW2', 'BW3', 'BW4', 'BW5', 'BW6', 'BW7', 'CA004', 'CA013', 'CA014', 'CA017', 'CA018', 'CA021', 'CA022', 'CA023', 'CA024', 'CD001', 'CD002', 'CI001', 'CI002', 'CI003', 'CI004', 'CI005', 'CI006', 'CI007', 'CL001', 'CL002', 'CL003', 'CL004', 'CL005', 'CL006', 'CM001', 'CN001', 'CN002', 'CN003', 'CN004', 'CN005', 'CN006', 'CN007', 'CN008', 'CN009', 'CN010', 'CN011', 'CN012', 'CN013', 'CN014', 'CN015', 'CN017', 'CN018', 'CN019', 'CN020', 'CN021', 'CN022', 'CN023', 'CN024', 'CN025', 'CN026', 'CN027', 'CN028', 'CN029', 'CN030', 'CN031', 'CN032', 'CN033', 'CN034', 'CN035', 'CN036', 'CN037', 'CN038', 'CN039', 'CN040', 'CN041', 'CN042', 'CN043', 'CN044', 'CN045', 'CN046', 'CN047', 'CN048', 'CN049', 'CN050', 'CN051', 'CO001', 'CO002', 'CO003', 'CO004', 'CO005', 'CO006', 'CO007', 'CO008', 'CO009', 'CO010', 'CO011', 'CO012', 'CO013', 'CO014', 'CO015', 'CO016', 'CO017', 'CO018', 'CR001', 'CR002', 'CR003', 'CR004', 'CR005', 'CR006', 'CR007', 'CR008', 'CR009', 'CR010', 'CR011', 'CR012', 'CU001', 'CU002', 'CU003', 'CU004', 'CU005', 'CU006', 'CU007', 'CU008', 'CU009', 'CU010', 'CU011', 'CU012', 'CU013', 'CU014', 'CU015', 'CU016', 'CU017', 'CU018', 'CU019', 'CU020', 'CU021', 'CU022', 'DE002', 'DE003', 'DE004', 'DE005', 'DE006', 'DE007', 'DE008', 'DE009', 'DE011', 'DE012', 'DE013', 'DE014', 'DE015', 'DE016', 'DE017', 'DE019', 'EC001', 'EC002', 'EC003', 'EC004', 'EC005', 'EC006', 'EC007', 'EC008', 'EC009', 'EC010', 'EC011', 'EC012', 'EC013', 'EC014', 'EC015', 'EC016', 'EC017', 'EC018', 'EC019', 'EC020', 'ES001', 'ES002', 'ES003', 'ES004', 'ES005', 'ES006', 'ES007', 'ES008', 'ES009', 'ES010', 'ES011', 'ES012', 'ES013', 'ES014', 'ES015', 'ES016', 'ES017', 'ES018', 'ES019', 'ES020', 'FI001', 'FI002', 'FI003', 'FI004', 'FI005', 'FR003', 'FR004', 'FR005', 'FR006', 'FR007', 'FR008', 'FR009', 'FR010', 'FR011', 'FR012', 'FR014', 'FR015', 'GA001', 'GA002', 'GA003', 'GA004', 'GA005', 'GA006', 'GB001', 'GB002', 'GB003', 'GB004', 'GB005', 'GB006', 'GB007', 'GB008', 'GB009', 'GB010', 'GB011', 'GH002', 'GH003', 'GH004', 'GH005', 'GH006', 'GH007', 'GH008', 'GL005', 'GL006', 'GR001', 'GR002', 'GR003', 'GR004', 'GR005', 'GR006', 'GR007', 'GR008', 'GR009', 'GR012', 'GR013', 'GR015', 'HU001', 'HU002', 'HU003', 'HU004', 'HU005', 'HU006', 'HU007', 'HU008', 'HU009', 'HU010', 'HU011', 'HU012', 'HU013', 'HU014', 'HU015', 'HU016', 'HU017', 'HU018', 'HU019', 'HU020', 'ID001', 'ID002', 'ID003', 'ID004', 'ID005', 'ID006', 'ID007', 'ID008', 'ID009', 'ID011', 'ID012', 'ID013', 'ID014', 'ID015', 'ID016', 'ID017', 'ID018', 'ID019', 'ID020', 'ID021', 'ID022', 'ID023', 'ID024', 'ID025', 'ID026', 'ID027', 'ID028', 'ID029', 'ID032', 'ID033', 'ID034', 'ID035', 'ID036', 'ID037', 'ID038', 'ID039', 'ID040', 'ID041', 'ID042', 'ID043', 'ID044', 'ID045', 'ID046', 'ID047', 'ID048', 'ID049', 'ID050', 'IE001', 'IE002', 'IE003', 'IE004', 'IE006', 'IE007', 'IE009', 'IE010', 'IE011', 'IE012', 'IN001', 'IN002', 'IN003', 'IN004', 'IN005', 'IN006', 'IN007', 'IN008', 'IN009', 'IN010', 'IN011', 'IN012', 'IN013', 'IN016', 'IN018', 'IN019', 'IN021', 'IN025', 'IT001', 'IT002', 'IT003', 'IT004', 'IT005', 'IT006', 'IT007', 'IT008', 'IT009', 'IT010', 'IT011', 'IT012', 'IT013', 'IT014', 'IT015', 'IT016', 'IT017', 'JM001', 'JM002', 'JM003', 'JM004', 'JO001', 'JO002', 'JO003', 'JO004', 'JP001', 'JP002', 'JP003', 'JP004', 'KE001', 'KE002', 'KE003', 'KE004', 'KE006', 'KE007', 'KE008', 'KE009', 'KE010', 'KE011', 'KE012', 'KE013', 'KE014', 'KE015', 'KE016', 'KE017', 'KE018', 'KE019', 'KE020', 'KE021', 'KE022', 'KE023', 'KE024', 'KE025', 'KE026', 'KE027', 'KE028', 'KE029', 'KE030', 'KE031', 'KE032', 'KE033', 'KE034', 'KE035', 'KE036', 'KE037', 'KE038', 'KE039', 'KE040', 'KE041', 'KE042', 'KE043', 'KE044', 'KE045', 'KE046', 'KE047', 'KE048', 'KE049', 'KE050', 'KE051', 'KE052', 'KE053', 'KE055', 'KE056', 'KE057', 'KE058', 'KE059', 'KE060', 'KE061', 'KE062', 'KE063', 'KE064', 'KE065', 'KE066', 'KE067', 'KE068', 'KE069', 'KE070', 'LK001', 'LK002', 'LK003', 'LK004', 'ML001', 'ML002', 'ML003', 'ML004', 'ML005', 'ML006', 'ML007', 'ML008', 'MY001', 'MY002', 'MY003', 'MY004', 'MY005', 'MY006', 'MY007', 'MY058', 'MY059', 'MY060', 'MZ001', 'MZ002', 'MZ003', 'MZ004', 'MZ005', 'MZ006', 'MZ007', 'MZ008', 'MZ009', 'NA001', 'NA002', 'NA003', 'NA004', 'NA005', 'NA006', 'NA007', 'NA008', 'NA009', 'NA010', 'NA011', 'NE001', 'NE002', 'NE003', 'NE004', 'NG001', 'NG002', 'NG003', 'NG004', 'NG005', 'NG006', 'NG007', 'NG008', 'NG009', 'NG011', 'NG012', 'NG013', 'NG014', 'NG015', 'NG016', 'NG017', 'NG018', 'NG019', 'NG020', 'NG021', 'NG022', 'NG023', 'NG024', 'NG025', 'NG026', 'NG027', 'NG028', 'NG029', 'NI001', 'NI002', 'NI003', 'NI004', 'NI005', 'NI006', 'NI007', 'NI008', 'NI009', 'NI010', 'NI011', 'NL002', 'NL005', 'NL006', 'NL007', 'NL008', 'NL011', 'NL016', 'NL019', 'NL021', 'NL022', 'NL027', 'NL028', 'NL029', 'NL032', 'NL033', 'NL034', 'NL036', 'NL043', 'NL044', 'NL045', 'NL046', 'NL047', 'NL048', 'NL049', 'NL050', 'NL051', 'NL052', 'NL053', 'NL054', 'NL055', 'NL056', 'NL057', 'NO001', 'NO002', 'NO003', 'OM001', 'OM002', 'OM003', 'OM004', 'PE001', 'PE002', 'PE003', 'PE004', 'PE005', 'PE006', 'PE007', 'PE008', 'PE009', 'PE010', 'PE012', 'PE013', 'PE014', 'PE015', 'PE016', 'PE017', 'PE018', 'PE019', 'PE020', 'PE021', 'PE022', 'PE023', 'PE024', 'PE025', 'PE026', 'PE027', 'PE028', 'PE029', 'PE030', 'RU002', 'RU009', 'RU010', 'RU011', 'RU012', 'RU013', 'RU014', 'RU015', 'SK001', 'SK002', 'SK003', 'SK004', 'SK006', 'SK007', 'US002', 'US018', 'US019', 'US020', 'US026', 'US027', 'US028', 'UY001', 'UY002', 'UY003', 'UY004', 'UY005', 'UY006', 'UY007', 'UY008', 'UY009', 'UY010', 'WS001', 'WS002', 'WS003', 'WS004', 'WS005', 'ZA001', 'ZA002', 'ZA003', 'ZA005', 'ZA006', 'ZA007', 'ZA008', 'ZA009', 'ZA010', 'ZA011', 'ZA012', 'ZA013', 'ZA014', 'ZA015', 'ZA016', 'ZA017', 'ZA018', 'ZA019', 'ZA020', 'ZA021', 'ZM001', 'ZM002', 'ZM003', 'ZM004', 'ZM005', 'ZM006', 'ZM007', 'ZM008', 'ZM009', 'ZM010', 'ZM011', 'ZW002', 'ZW003', 'ZW004', 'ZW005', 'ZW006', 'ZW007', 'ZW008', 'ZW009', 'ZW010', 'ZW011', 'ZW012', 'ZW013']


def get_need_data(ID5):

    url = f'https://isis.isric.org/monoliths/reference-soil-{ID5}'
    # 获取数据
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,headers=headers)
    response.encoding = 'utf-8' 
    page_text = response.text
    # print(page_text)
    # with open('test.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)

    tree = etree.HTML(page_text)
    # 获取data
    # TITLE
    try: 
        TITLE  =  tree.xpath('//h2[contains(text(), "Reference soil")]/text()')[0]
    except:
        TITLE = "无标题"


    # 表格1 Date  &  Lat_Lon
    tr_list = tree.xpath('//div[@class="field field-name-field-general-information field-type-text-long field-label-above"]//table//tbody/tr')

    for tr in tr_list: 
        key = tr.xpath('./td/text()')[0] # 'Status of vegetation; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)'
        value = tr.xpath('./td/text()')[1] # 'degraded'
        if "Date" in key:
            Date = value
        if "Lat/Lon" in key:
            Lat_Lon = value

    # 表格2
    tr_list = tree.xpath('//div[@id="Land usedetail"]/table/tbody/tr')
    land_use1, land_use2, land_use3, land_use4, land_use5 = "", "", "", "", ""
    # tree.xpath('//div[@id="Land usedetail"]/table/tbody/tr')[0].xpath('./td/text()')[0]
    for tr in tr_list: 
        key = tr.xpath('./td/text()')[0] # 'Status of vegetation; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)'
        value = tr.xpath('./td/text()')[1] # 'degraded'
        if "Status of vegetation; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)" in key:
            land_use1 = value
        if "Remarks on Land Use / Vegetation" in key:
            land_use2 = value
        if "Major vegetation type; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)" in key:
            land_use3 = value
        if "Land use or vegetation in the immediate vicinity of the site" in key:
            land_use4 = value
        if "Major crops" in key:
            land_use5 = value

    # Classification_WRB 2006
    try:
        wrd2006 = tree.xpath('//p[contains(text(), "WRB 2006")]/following-sibling::div[1]//tr/td[1]/text()')[0]
    except:
        wrd2006 = ""

            
    # Classification_WRB 1998
    try:
        wrd1998 = tree.xpath('//p[contains(text(), "WRB 1998")]/following-sibling::div[1]//tr/td[1]/text()')[0]
    except:
        wrd1998 = ""
    # FAO-UNESCO-ISRIC 1974
        
    try:
        fao1974 = tree.xpath('//p[contains(text(), "FAO-UNESCO-ISRIC 1974")]/following-sibling::div[1]//tr/td[1]/text()')[0]
    except:
        fao1974 = ""
    # FAO-UNESCO-ISRIC 1988
    try:
        fao1988 = tree.xpath('//p[contains(text(), "FAO-UNESCO-ISRIC 1988")]/following-sibling::div[1]//tr/td[1]/text()')[0]
    except:
        fao1988 = ""

    # depth数据
    try:
        tr_list = tree.xpath('//td[contains(text(), "Depth (cm)")]')[1].xpath('./../../tr')[1:]
        depth = ""
        for tr in tr_list:
            depth +=tr.xpath('.//text()')[1] + ";\n"
        depth = depth[:-1]
    except:
        depth = "无信息"
    # print(depth)
        
    return ID5, TITLE, Date, Lat_Lon, land_use1, land_use2, land_use3, land_use4, land_use5, wrd2006, wrd1998, fao1974, fao1988, depth


def get_isis():
    # 存储数据初始化
    for ID5 in tqdm(ids):
        # ID5 = "ID034"
        print(ID5)
        ID5, TITLE, Date, Lat_Lon, land_use1, land_use2, land_use3, land_use4, land_use5, wrd2006, wrd1998, fao1974, fao1988, depth = get_need_data(ID5)

        # 处理数据
        """ 
        处理数据
        """
        isis["ID5"].append(ID5)
        isis["TITLE"].append(TITLE)
        isis["Date"].append(Date)
        isis["Lat/Lon"].append(Lat_Lon)
        isis["Land use_Status of vegetation; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)"].append(land_use1)
        isis["Land use_Remarks on Land Use / Vegetation"].append(land_use2)
        isis["Land use_Major vegetation type; Guidelines for soil description - Fourth edition (FAO, Rome, 2006)"].append(land_use3)
        isis["Land use_Land use or vegetation in the immediate vicinity of the site"].append(land_use4)
        isis["Land use_Major crops"].append(land_use5)
        isis["Classification_WRB 2006"].append(wrd2006)
        isis["Classification_WRB 1998"].append(wrd1998)
        isis["Classification_FAO-UNESCO-ISRIC 1974"].append(fao1974)
        isis["Classification_FAO-UNESCO-ISRIC 1988"].append(fao1988)
        isis["Chemical characteristics-Depth (cm)"].append(depth)

def save_csv(name, data):
    # 保存csv文件
    print('保存csv文件...')
    #字典中的key值即为csv中列名
    dataframe = pd.DataFrame(data)
    #将DataFrame存储为csv,index表示是否显示行名，default=True
    dataframe.to_csv(f"{name}.csv",index=False, sep=',')

    
if __name__ == "__main__":
    data = get_isis()
    save_csv("isis", data)
    print('爬取结束!')
