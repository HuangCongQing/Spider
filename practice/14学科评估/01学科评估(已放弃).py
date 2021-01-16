'''
Description: 学科评估  已放弃  网站：https://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp?xkdm=01,02,03,04,05,06
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-15 20:19:18
LastEditTime: 2021-01-16 16:44:51
FilePath: /Spider/practice/14学科评估/01学科评估.py
'''

import requests
from bs4 import BeautifulSoup
from lxml import etree
import xlwt	# 存储
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
import json
import re

def get_subject(id):
    print("正在获取所有链接... ...")
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    param = {
        'yjxkdm': '0101',
        'xkdm': id
    }
    url = 'https://www.cdgdc.edu.cn/webrms/pages/Ranking/xkpmGXZJ2016.jsp'
    # url = 'https://www.cdgdc.edu.cn/xwyyjsjyxx/xkpgjg/'
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    # response = requests.get(url=url,headers=headers)
    # response.encoding = 'utf-8-sig' 
    # print(print(response.encoding))
    # page_text = response.text.encode('iso-8859-1').decode('gbk')
    page_text = response.content.decode('GBK')
    print(page_text)
    # tree = etree.HTML(page_text)
    # name = tree.xpath('//tbody/tr/td')
    # print(name)



if __name__ == "__main__":
    # class_id =['01,02,03,04,05,06', '07', '08', '09', '10', '11', '12', '13']
    id = '01,02,03,04,05,06'
    urls = get_subject(id)
    # urls = ['rw6z9nza7gduikyw', 'dvbww41vhzdiqaq9']
    # url = 'rw6z9nza7gduikyw'
    # get_contents(url)

''' 

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta content="{qqqqqr4hProJ8Z.CPsh{BQdwcuVoi1RQ1OrjQlLGQOTC1lNlswpYblKxDiVl0sb7YQrTGmUaM8TNelK9IRArwlUaoRGw9lUZqAArZrvVsQrAvsPYoEGw_rvZpwYN0lUAswGqqqqqqr0YylAobUAWKOH0e5pmKoa2Qr1qqqqqr0hzrCkcLWeIY08http:geMoMZedn.5tELCKR8l4Qa:80qqqqqr7r0De309c5lrM7jqqq!x7z,aac,amr,asm,avi,bak,bat,bmp,bin,c,cab,css,csv,com,cpp,dat,dll,doc,dot,docx,exe,eot,fla,flc,fon,fot,font,gdb,gif,gz,gho,hlp,hpp,htc,ico,ini,inf,ins,iso,js,jar,jpg,jpeg,json,java,lib,log,mid,mp4,mpa,m4a,mp3,mpg,mkv,mod,mov,mim,mpp,msi,mpeg,obj,ocx,ogg,olb,ole,otf,py,pyc,pas,pgm,ppm,pps,ppt,pdf,pptx,png,pic,pli,psd,qif,qtx,ra,rm,ram,rmvb,reg,res,rtf,rar,so,sbl,sfx,swa,swf,svg,sys,tar,taz,tif,tiff,torrent,txt,ttf,vsd,vss,vsw,vxd,woff,woff2,wmv,wma,wav,wps,xbm,xpm,xls,xlsx,xsl,xml,z,zip,apk,plist,ipar0k674QIEft7VCyshzl70n41MfHXV_ds_xJHKyJjLKivFFw7NKaqqq tYUrNDs7rEqRTrnalWlf6oOasWp04K6VsWVR6EaL1iSE_oOoIcjJT4ksXWh26eO4JDF97na8vlJZ6SfvsrZ9GXSBEkZWH_nnvxdgWLCUZWWgSyGoqmzW_TnhcqJw9_SO_miGl5vB2H8Q_gcknkiLUyp.rEea44skdiZaS6sMoRw7lTCkmREqqdqhvxJrf4pMODXl66cIikWJ44SHNrWGQykjorx3Z9ps03MLDvADnltVOOKcORELC7PhuMxGPGs5LiIg82bnu35QwGqCJx4aGyPcDxyA_vpCGxM03BnuNDXaMNubBrLLnL15DotWyzPK9ht05zacmE.WgCDCZhElgaqHFR.zzLO8Zht78GcFGk4GZaA87H_WaX6IMEy0yPkkkw49lFseWlvLFKpZnEo3oAngacV763OQLFqVhyq8Nf_fDtLRNpnzoj0Ut1083179040%0AY9FEbJNxOa4iqVilnfTWqgsmcZSVAQPrcaap67ehSEzrD0oJq3zJbTiqqZghuG7WOWlc1acx13xxkVUJ13.rbJcDfQ0mPTUha9zlpS13uVGTah4x.zT_fITqi9kBuoAlQJa0ccL8eqB516fM8q0gn6JMMWJ6PhqojSauuHlmFZYL1IfDdG.jnkw3_QFZksuh3aBTc6ioEeO_pMOweQX4njMtzqEg6hlW5N0_GsPrLT4_ndlhwyz6ss3h8fz2roAJIRTe1uQqH32unI48xqACnioo.rO5rjzJtGz_15uhF7QyDiMwLQ4bA5ED4ZJfrDIrxZMjS8uJRLqevXih_WzXCCCJhVzfC6yDxmSOpKQDM9ifA5gcjGx9Osp8x0PLKHwDL30f16DhygzGrur3gazBajwQ_Q421P7kZ00Lo1sc4E1.OkM8_lBOPCAMRW09PCPMPEvKcJEm07TJSYDJCZS31egDDlhFqSt3k3R3uwPhPW7R1yeouyG8G2QQvAa3cSOx90qsuJix6Q6R1Y2quSgpcSYh9TXskwHhv2XrnzAJpA.KkwCxqACFsm0hpVssrLUwmmGcS2QJTZXDcSqh2LIDCrVmG071OGxQDA03O3El2q4hv3Hcq
 '''

    

