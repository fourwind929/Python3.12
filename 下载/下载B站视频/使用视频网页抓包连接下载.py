import requests

url_video = input("请输入视频视频网址：")
url_audio = input("请输入视频音频网址：")

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头

import os
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
folder = download_folder
folder = download_folder  +  "/B站视频"
if not os.path.exists(folder):   # 如果路径不存在，则创建路径
    os.makedirs(folder)
os.chdir(folder)

open(".cache_video.mp4", "wb").write(requests.get(url_video, headers=dic).content)
open(".cache_audio.mp3", "wb").write(requests.get(url_audio, headers=dic).content)
# 下载视频和音频
print("视频和音频下载完成...")
print(f"{title}bilibiliTEMP_MPY_wvf_snd.mp3”是临时文件，请勿删除。下载完成后会自动删除。")

video = VideoFileClip(".cache_video.mp4")
audio = AudioFileClip(".cache_audio.mp3")

final_clip = video.set_audio(audio)# 合并视频和音频
final_clip.write_videofile(f"{title}.mp4")
# 导出视频

# 删除缓存文件
print("视频导出成功,正在删除缓存文件...")
os.remove(".cache_video.mp4")
os.remove(".cache_audio.mp3")