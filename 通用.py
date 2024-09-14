# 通用代码
#—------------------------------#
# 1：
#请求头:
dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    ,"cookie":"xxx"
    ,"referer":"xxx"
}

#—------------------------------—------------------------------—------------------------------#
# 2：
#自动将文件下载到下载文件夹中的“示例文件夹”文件夹中
#且若无“示例文件夹”文件夹，则自动创建“示例文件夹”文件夹
#记得import os并修改”示例文件夹“的路径

import os
download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
folder = download_folder
folder = download_folder  +  "/示例文件夹"
if not os.path.exists(folder):   # 如果路径不存在，则创建路径
    os.makedirs(folder)
os.chdir(folder)

