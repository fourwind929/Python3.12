import os

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
