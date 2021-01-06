# 单视频下载
directory = '/home/hcq/下载/collage'                          #设置下载目录
url = 'https://www.bilibili.com/video/BV194411G72j '      #需要下载的视频地址
sys.argv = ['you-get', '-o', directory, url, '-l']          #sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
you_get.main()