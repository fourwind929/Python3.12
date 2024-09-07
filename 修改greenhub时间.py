import json

# 定义文件路径
file_path = "/Users/zhangxw/Library/Application Support/GreenHub/config.json"

# 读取JSON文件
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 修改today-use-minute中的minutes值
data["today-use-minute"]["minutes"] = 1440

# 将修改后的数据写回JSON文件
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("文件已更新")
