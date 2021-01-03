聚焦爬虫:爬取页面中指定的页面内容。
    - 编码流程：
        - 指定url
        - 发起请求
        - 获取响应数据
        - 数据解析
        - 持久化存储

数据解析分类：
    - 正则
    - bs4
    - xpath（***）

数据解析原理概述：
    - 解析的局部的文本内容都会在标签之间或者标签对应的属性中进行存储
    - 1.进行指定标签的定位
    - 2.标签或者标签对应的属性中存储的数据值进行提取（解析）

正则解析：

<div class="thumb">

<a href="/article/121721100" target="_blank">
<img src="//pic.qiushibaike.com/system/pictures/12172/121721100/medium/DNXDX9TZ8SDU6OK2.jpg" alt="指引我有前进的方向">
</a>

</div>

ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'


bs4进行数据解析
    - 数据解析的原理：
        - 1.标签定位
        - 2.提取标签、标签属性中存储的数据值
    - bs4数据解析的原理：
        - 1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        - 2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    - 环境安装：
        - pip install bs4
        - pip install lxml
    - 如何实例化BeautifulSoup对象：
        - from bs4 import BeautifulSoup
        - 对象的实例化：
            - 1.将本地的html文档中的数据加载到该对象中
                    fp = open('./test.html','r',encoding='utf-8')
                    soup = BeautifulSoup(fp,'lxml')
            - 2.将互联网上获取的页面源码加载到该对象中
                    page_text = response.text
                    soup = BeatifulSoup(page_text,'lxml')
        - 提供的用于数据解析的方法和属性：
            - soup.tagName:返回的是文档中第一次出现的tagName对应的标签
            - soup.find():
                - find('tagName'):等同于soup.div
                - 属性定位：
                    -soup.find('div',class_/id/attr='song')
            - soup.find_all('tagName'):返回符合要求的所有标签（列表）
        - select：
            - select('某种选择器（id，class，标签...选择器）'),返回的是一个列表。
            - 层级选择器：
                - soup.select('.tang > ul > li > a')：>表示的是一个层级
                - oup.select('.tang > ul a')：空格表示的多个层级
        - 获取标签之间的文本数据：
            - soup.a.text/string/get_text()
            - text/get_text():可以获取某一个标签中所有的文本内容
            - string：只可以获取该标签下面直系的文本内容
        - 获取标签中属性值：
            - soup.a['href']

xpath解析：最常用且最便捷高效的一种解析方式。通用性。

    - xpath解析原理：
        - 1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        - 2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
    - 环境的安装：
        - pip install lxml
    - 如何实例化一个etree对象:from lxml import etree
        - 1.将本地的html文档中的源码数据加载到etree对象中：
            etree.parse(filePath)
        - 2.可以将从互联网上获取的源码数据加载到该对象中
            etree.HTML('page_text')
        - xpath('xpath表达式')
    - xpath表达式:
        - /:表示的是从根节点开始定位。表示的是一个层级。
        - //:表示的是多个层级。可以表示从任意位置开始定位。
        - 属性定位：//div[@class='song'] tag[@attrName="attrValue"]
        - 索引定位：//div[@class="song"]/p[3] 索引是从1开始的。
        - 取文本：
            - /text() 获取的是标签中直系的文本内容
            - //text() 标签中非直系的文本内容（所有的文本内容）
        - 取属性：
            /@attrName     ==>img/src


作业：
    爬取站长素材中免费简历模板


        ，






