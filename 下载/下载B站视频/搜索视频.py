import requests
import os
import re

download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
folder = download_folder  +  "/示例文件夹"
if not os.path.exists(folder):   # 如果路径不存在，则创建路径
    os.makedirs(folder)
os.chdir(folder)

print("请输入你要搜索的关键字：")
keyword = input()
url = "https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=" + keyword    # 构造搜索视频的url

# 获取用户的文稿路径
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
cookie_file_path = os.path.join(documents_folder, "B-cookie.txt")

# 检查文件是否存在
if os.path.exists(cookie_file_path):
    # 读取文件内容
    with open(cookie_file_path, 'r', encoding='utf-8') as file:
        cookie = file.read().strip()  # 去除头尾空白字符
    # print(cookie)
else:
    cookie = ""

dic = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"
    ,"cookie":f"{cookie}"
    ,"referer":"https://www.bilibili.com/"
}  

response = requests.get(url, headers=dic)    # 发送请求
response.encoding = 'utf-8'

obj_search_title = re.compile(r'')    # 匹配搜索结果的标题和链接
obj_search_rul = re.compile(r'')    # 匹配搜索结果的封面、标题和链接






with open("search_result.html", "w", encoding="utf-8") as f:    # 保存搜索结果
    f.write(response.text)