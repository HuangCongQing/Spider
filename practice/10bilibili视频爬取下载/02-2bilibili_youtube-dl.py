'''
Description: youtube-dl 下载视频
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-01-03 14:22:52
LastEditTime: 2021-01-06 21:52:48
FilePath: /Spider/practice/10bilibili视频爬取下载/02-2bilibili_youtube-dl.py
'''
# import youtube_dl 

# options = {
# 'format': 'bestaudio/best', # choice of quality
# 'extractaudio' : True, # only keep the audio
# # 'audioformat' : "mp3", # convert to mp3
# # 'outtmpl':  '/home/hcq/下载/collage/%(id)s'  , # name the file the ID of the video
# 'noplaylist' : True, # only download single song, not playlist

# }
# url = 'https://www.bilibili.com/video/BV194411G72j '      #需要下载的视频地址
# with youtube_dl.YoutubeDL(options) as ydl:
#     ydl.download(url)


from youtube_dl import YoutubeDL

video =  'https://www.bilibili.com/video/BV194411G72j '      #需要下载的视频地址

#  参数设置
youtube_dl_opts = {
    
}
with YoutubeDL(youtube_dl_opts) as ydl:
      info_dict = ydl.extract_info(video, download=True)  # download=True
      video_url = info_dict.get("url", None)
      video_id = info_dict.get("id", None)
      video_title = info_dict.get('title', None)