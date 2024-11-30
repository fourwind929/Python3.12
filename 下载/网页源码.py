import requests
import os

url = input("请输入要爬取的网页的url：")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
#第一个cookie是B站的cookie


response = requests.get(url, headers=headers)

# print(response.text)     # 打印网页源码 

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
folder = download_folder  +  "/网页源码"

if not os.path.exists(folder):   # 如果路径不存在，则创建路径,存在则不创建，并切换到该路径下
    os.makedirs(folder)
os.chdir(folder)

# 保存网页源码到本地文件
with open(f"{url.split('/')[2]}.html", "w", encoding="utf-8") as f:   # 保存网页源码到本地文件
    f.write(response.text)

response.close()