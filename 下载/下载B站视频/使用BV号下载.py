from math import e
import requests
import re
from moviepy.editor import *
import os

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

obj_path = re.compile(r'^[A-Za-z]:\$[^\\:*?"<>|]+\$*[^\\:*?"<>|]*$')

print("不可下载分P视频，只下载单P视频。")
print("请输入保存路径(不输入直接enter确定则默认下载到~/Downloads/B站视频):")
print("路径必须为绝对路径，且不能包含中文、空格、特殊字符，不得以/结尾。")
print("注：路径必须存在，否则程序会自动创建。")

folder = input()    # 输入保存路径
if folder == "":
    folder = download_folder  +  "/B站视频"
else:
    while not obj_path.match(folder):
        print("输入的路径不合法！")
        folder = input("请重新输入保存路径：")
if not os.path.exists(folder):   # 如果路径不存在，则创建路径
    os.makedirs(folder)

os.chdir(folder)

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"referer":"https://www.bilibili.com/"
}#请求头

obj_title_find = re.compile(r'<title data-vue-meta="true">(?P<title>.*?)</title>',re.S)#获取标题
obj_video = re.compile(r'<style id="setSizeStyle"></style>.*?baseUrl":.*?"(?P<video>.*?)"',re.S)#获取视频链接
obj_audio = re.compile(r'"audio":.*?"baseUrl":.*?"(?P<audio>.*?)"',re.S)#获取视频音频连接
obj_title_findErro = re.compile(r'<title>(?P<title_find1>.*?)</title>',re.S)#获取标题
obj_BV = re.compile(r'^BV[a-zA-Z0-9]{10}$')

restart = "y"
while restart == "y":

    reinput = "y"
    print("请输入BV号,如BVxxxxxxxxxx：")
    bv = input("请输入BV号：")

    while reinput == "y":

        while not obj_BV.match(bv):
            print("输入的BV号不符合格式！")
            bv = input("请重新输入BV号：")
        
        url = f"https://www.bilibili.com/video/{bv}/"

        response = requests.get(url, headers=dic)#发送请求
        response.encoding = 'utf-8'

        result_title_findErro = obj_title_findErro.search(response.text)
        if result_title_findErro == None:
            result_title = obj_title_find.search(response.text)
            title = result_title.group("title")

        else:
            title = result_title_findErro.group("title_find1")

        if "出错啦!" in title or "视频去哪了呢？" in title:
            print("视频不存在或已被删除！")
            bv = input("请重新输入BV号：")
            reinput = "y"
            continue

        print("获取标题成功")
        # print("是否下载标题为：",title,"的视频？(y/n)")
        title_choice = input(f"是否下载标题为:《{title}》,的视频？(y/n):")

        while title_choice != "y" and title_choice != "n":
            title_choice = input("输入错误！请重新输入:")

        else:
            if title_choice == "n":# 选择不下载
                # print("视频不对？是否输入新的BV号？(y/n/e)，按y重新输入，按n直接下载已输入BV号视频，按e退出程序并退出命令行。")
                choice = input("视频不对？是否输入新的BV号？(y/n/e)，按y重新输入，按n直接下载已输入BV号视频，按e退出程序并退出命令行:")
                if choice == "y":
                    reinput = "y"
                    break
                
                if choice == "n":
                    reinput = "n"
                    break

                if choice == "e":
                    response.close() #关闭请求
                    print("程序已退出。")
                    exit()

            if title_choice == "y":
                reinput = "n"

    print("开始下载...")

    result_video = obj_video.search(response.text)
    result_audio = obj_audio.search(response.text)
    url_video = result_video.group("video")
    url_audio = result_audio.group("audio")
    # 获取视频链接和音频链接

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

    print("完成!")
    
    redanwload = input("是否继续下载视频？(y/n):")
    while redanwload != "n" and redanwload != "y":
        redanwload = input("输入错误！请重新输入:")
    else:
        if redanwload == "y":
            restart = "y"
        else:
            restart = "n"

    response.close() #关闭请求
    print("程序已退出。")