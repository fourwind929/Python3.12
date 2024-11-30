
#只单纯修改时间，每天使用时需先启动greenhub，然后再执行次代码


import os

# 定义要搜索的文件名
file_name = "config.json"

# 定义搜索的起始目录（通常是用户的主目录）
start_directory = os.path.expanduser("~")

# 定义一个函数来递归搜索文件
def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

# 调用函数搜索文件
file_path = find_file(file_name, start_directory)

print("文件路径：", file_path)


# 导入json模块

import json

# 定义文件路径
# file_path = "/Users/zhangxw/Library/Application Support/GreenHub/config.json"# 注意修改路径，修改为自己的路径

# 读取JSON文件
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 修改today-use-minute中的minutes值
data["today-use-minute"]["minutes"] = 1440

# 将修改后的数据写回JSON文件
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("文件已更新")
