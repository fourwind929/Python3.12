from unittest import result
import requests
import re
from moviepy.editor import *
import os

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

print("请输入保存路径(不输入直接enter确定则默认下载到~/Downloads/B站视频):")
folder = input()    # 输入保存路径
if folder == "":
    folder = download_folder  +  "/B站视频"

if not os.path.exists(folder):
    os.makedirs(folder)

os.chdir(folder)

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"cookie":"__51vcke__KSHU1VNqce379XHB=e2d5e8e9-ef05-5edd-9cac-7149be0a7205; __51vuft__KSHU1VNqce379XHB=1725097450942; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22184f38a8-33a0-5bad-9bd2-3d87efd67d63%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201725119999999%2C%20%22ct%22%3A%201725119341589%7D; __51uvsct__KSHU1VNqce379XHB=3; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725097452,1725119342; HMACCOUNT=1589301F85258CBA; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1725097452,1725119342; Hm_lvt_8e745928b4c636da693d2c43470f5413=1725097452,1725119342; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1725121061; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725121061; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1725121061"
    ,"referer":"https://www.bilibili.com/"
}#请求头

# url = "https://www.bilibili.com/video/BV1PDWdeSEh8/"

print("请输入BV号,如BVxxxxxxxxxx：")
x = input()
obj_BV = re.compile(r'BV[a-zA-Z0-9]{10}')
if not obj_BV.match(x):
    print("输入的BV号不合法！")
    exit()
 
url = f"https://www.bilibili.com/video/{x}/"

response = requests.get(url, headers=dic)#发送请求
# print(response.text)

obj_title = re.compile(r'<title data-vue-meta="true">(?P<title>.*?)</title>',re.S)#获取标题
obj_video = re.compile(r'<style id="setSizeStyle"></style>.*?baseUrl":.*?"(?P<video>.*?)"',re.S)#获取视频链接
obj_audio = re.compile(r'"audio":.*?"baseUrl":.*?"(?P<audio>.*?)"',re.S)#获取视频音频连接

result_title = obj_title.search(response.text)
title = result_title.group("title")
print("是否下载标题为：",title,"的视频？(y/n)")
if input(":") == "n":
    exit()

print("开始下载...")
# 获取标题

result_video = obj_video.search(response.text)
result_audio = obj_audio.search(response.text)
url_video = result_video.group("video")
url_audio = result_audio.group("audio")
# 获取视频链接和音频链接

open(".cache_video.mp4", "wb").write(requests.get(url_video, headers=dic).content)
open(".cache_audio.mp3", "wb").write(requests.get(url_audio, headers=dic).content)
# 下载视频和音频
print("视频和音频下载完成...")
print(f"{title}bilibiliTEMP_MPY_wvf_snd.mp3”是临时文件，请勿删除。")

video = VideoFileClip(".cache_video.mp4")
audio = AudioFileClip(".cache_audio.mp3")

final_clip = video.set_audio(audio)# 合并视频和音频
final_clip.write_videofile(f"{title}.mp4")

# 删除缓存文件
print("视频导出成功,正在删除缓存文件...")
os.remove(".cache_video.mp4")
os.remove(".cache_audio.mp3")

# 导出视频
print("完成!")