requests模块
    - urllib模块
    - requests模块

requests模块：python中原生的一款基于网络请求的模块，功能非常强大，简单便捷，效率极高。
作用：模拟浏览器发请求。

如何使用：（requests模块的编码流程）
    - 指定url
        - UA伪装
        - 请求参数的处理
    - 发起请求
    - 获取响应数据
    - 持久化存储

环境安装：
    pip install requests

实战编码：
    - 需求：爬取搜狗首页的页面数据



实战巩固
    - 需求：爬取搜狗指定词条对应的搜索结果页面（简易网页采集器）
        - UA检测
        - UA伪装
    - 需求：破解百度翻译
        - post请求（携带了参数）
        - 响应数据是一组json数据
    - 需求：爬取豆瓣电影分类排行榜 https://movie.douban.com/中的电影详情数据

    - 作业：爬取肯德基餐厅查询http://www.kfc.com.cn/kfccda/index.aspx中指定地点的餐厅数据

    - 需求：爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
                http://125.35.6.84:81/xk/
        - 动态加载数据
        - 首页中对应的企业信息数据是通过ajax动态请求到的。

        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=e6c1aa332b274282b04659a6ea30430a
        http://125.35.6.84:81/xk/itownet/portal/dzpz.jsp?id=f63f61fe04684c46a016a45eac8754fe
        - 通过对详情页url的观察发现：
            - url的域名都是一样的，只有携带的参数（id）不一样
            - id值可以从首页对应的ajax请求到的json串中获取
            - 域名和id值拼接处一个完整的企业对应的详情页的url
        - 详情页的企业详情数据也是动态加载出来的
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById
            - 观察后发现：
                - 所有的post请求的url都是一样的，只有参数id值是不同。
                - 如果我们可以批量获取多家企业的id后，就可以将id和url形成一个完整的详情页对应详情数据的ajax请求的url

数据解析：
    聚焦爬虫
    正则
    bs4
    xpath