import requests
from moviepy.editor import *

# x1 = input("请输入B站视频链接：")
# x2 = input("请输入B站视频音乐链接：")

url_video = input("请输入B站视频链接：")
url_audio = input("请输入B站视频音乐链接：")

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"cookie":"__51vcke__KSHU1VNqce379XHB=e2d5e8e9-ef05-5edd-9cac-7149be0a7205; __51vuft__KSHU1VNqce379XHB=1725097450942; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22184f38a8-33a0-5bad-9bd2-3d87efd67d63%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201725119999999%2C%20%22ct%22%3A%201725119341589%7D; __51uvsct__KSHU1VNqce379XHB=3; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725097452,1725119342; HMACCOUNT=1589301F85258CBA; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1725097452,1725119342; Hm_lvt_8e745928b4c636da693d2c43470f5413=1725097452,1725119342; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1725121061; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725121061; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1725121061"
    ,"referer":"https://www.bilibili.com/"
}#请求头

response_video = requests.get(url_video,headers=dic)

open("video.mp4","wb").write(response_video.content)

response_audio = requests.get(url_audio,headers=dic)

open("audio.mp3","wb").write(response_audio.content)

video = VideoFileClip("video.mp4")
audio = AudioFileClip("audio.mp3")

final_clip = video.set_audio(audio)

final_clip.write_videofile("final.mp4")