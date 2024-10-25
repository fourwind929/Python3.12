import requests
import re
from moviepy.editor import *
import os

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")

obj_path = re.compile(r'^[A-Za-z]:\$[^\\:*?"<>|]+\$*[^\\:*?"<>|]*$')
print("欢迎使用BV号下载B站视频！")
print("tips:")
print("不可下载分P视频，只下载单P视频。")
print("本程序不含cookie，请先登录B站并复制cookie内容写入一个文本文件，文件名为<B站cookie.txt>，并保存到Documents文件夹。")
print("如果程序无法获取cookie，则程序会自动下载清晰度最低的视频。")
print("————————————————————————————————————————————————————————————————————————————————————————————————————")
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

# 获取用户的文稿路径
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
cookie_file_path = os.path.join(documents_folder, "B站cookie.txt")

# 检查文件是否存在
if os.path.exists(cookie_file_path):
    # 读取文件内容
    with open(cookie_file_path, 'r', encoding='utf-8') as file:
        cookie = file.read().strip()  # 去除头尾空白字符
    # print(cookie)
else:
    cookie = ""

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"cookie":"buvid4=86705F0E-94A1-4BC8-7377-4E8B8E8D3BD284330-023082108-nStoKVDpV6TWmkr8NXd3WtSxKnyqevuExi3ulVPy6uBib7oNdvXzGA%3D%3D; header_theme_version=CLOSE; buvid_fp_plain=undefined; LIVE_BUVID=AUTO2616959926194049; enable_web_push=DISABLE; DedeUserID=1292515807; DedeUserID__ckMd5=4304e455feb2ad9a; blackside_state=0; CURRENT_BLACKGAP=0; FEED_LIVE_VERSION=V8; PVID=1; balh_server_inner=__custom__; balh_is_closed=; buvid3=11D252E5-4F95-36FE-718C-2804E3AABA9872508infoc; b_nut=1724132572; _uuid=D9E682B2-82BF-4EE4-10F52-49621E66CCA773430infoc; CURRENT_FNVAL=4048; hit-dyn-v2=1; rpdid=0zbfvRPVul|VGkZ0byE|PTA|3w1SZR0r; fingerprint=8c54690999a2ce2631d7c96a147b98e2; buvid_fp=8c54690999a2ce2631d7c96a147b98e2; bp_t_offset_1292515807=990231025357422592; home_feed_column=5; browser_resolution=1432-816; b_lsid=D6B10C739_192C3F5A903; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzAxMjM3MTMsImlhdCI6MTcyOTg2NDQ1MywicGx0IjotMX0.bub-Bqpqu-bq4giiS3qm_6uq_tC3y6XJz-U8J3WoUV8; bili_ticket_expires=1730123653; SESSDATA=73624c07%2C1745416515%2Ca46e5%2Aa1CjAdaOasbc0V61RYpN__XYY_PX5qSzeG_xsi76nPXiWckWMi6y7muAIo9GFb_JBe3HISVjR2WjlhcDR6VU1YbTJMWWc2VTZRUmhSWnVHbXB2N3NpWFFhZEYtcTFNdTVWQ3dOU3FXck54WVpaSTZYczFjLTRfS0xmczhNTFpRTC0wS21fVkpMbkFBIIEC; bili_jct=ae31c52925e6ef238ac425922f86b146; sid=55njneex; CURRENT_QUALITY=80"# 请自行替换cookie
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

    print(obj_video.search(response.text).group("video"))
    print(obj_audio.search(response.text).group("audio"))

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