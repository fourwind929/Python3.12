from math import e
import requests
import re
from moviepy.editor import *
# import os

# download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# obj_path = re.compile(r'^[A-Za-z]:\$[^\\:*?"<>|]+\$*[^\\:*?"<>|]*$')

# print("不可下载分P视频，只下载单P视频。")
# print("请输入保存路径(不输入直接enter确定则默认下载到~/Downloads/B站视频):")
# print("路径必须为绝对路径，且不能包含中文、空格、特殊字符，不得以/结尾。")
# print("注：路径必须存在，否则程序会自动创建。")

# folder = input()    # 输入保存路径
# if folder == "":
#     folder = download_folder  +  "/B站视频"
# else:
#     while not obj_path.match(folder):
#         print("输入的路径不合法！")
#         folder = input("请重新输入保存路径：")
# if not os.path.exists(folder):   # 如果路径不存在，则创建路径
#     os.makedirs(folder)

# os.chdir(folder)

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"referer":"https://www.bilibili.com/"
}#请求头

# obj_title = re.compile(r'<title data-vue-meta="true">(?P<title>.*?)</title>',re.S)#获取标题
# obj_video = re.compile(r'<style id="setSizeStyle"></style>.*?baseUrl":.*?"(?P<video>.*?)"',re.S)#获取视频链接
# obj_audio = re.compile(r'"audio":.*?"baseUrl":.*?"(?P<audio>.*?)"',re.S)#获取视频音频连接
obj_title_test = re.compile(r'<title>(?P<title_test>.*?)</title>',re.S)#获取标题

url = ("https://www.bilibili.com/video/BVluV2MYFEoT/")

response = requests.get(url, headers=dic)#发送请求
response.encoding = 'utf-8'

result_title_test = obj_title_test.search(response.text)
title_test = result_title_test.group("title_test")
if "出错啦!" in title_test:
    print("视频不存在或已被删除！")

