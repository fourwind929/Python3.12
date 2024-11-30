from DrissionPage import SessionPage
import requests

song_id = input("请输入歌单ID:")
download_url = f"http://music.163.com/song/media/outer/url?id={song_id}.mp3"
# 获取最终响应
response = requests.get(download_url, allow_redirects=True)
# 创建页面对象
down_page = SessionPage()
# 访问网页获取歌曲名称
down_page.get(download_url)
# 执行下载
down_page.download(response.url, rename='音乐1.mp3')