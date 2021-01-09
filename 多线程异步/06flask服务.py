'''
Description: flask服务
# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-01 13:56:16
LastEditTime: 2021-01-09 16:52:05
FilePath: /Spider/多线程异步/flask服务.py
'''
from flask import Flask
import time

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return 'Hello bobo'

@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'

@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'

if __name__ == '__main__':
    app.run(threaded=True)