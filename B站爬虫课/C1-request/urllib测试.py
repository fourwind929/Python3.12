from urllib.request import urlopen

url = "http://www.baidu.com"
response = urlopen(url)

# print(response.read().decode('utf-8'))

with open('local_baidu.html', mode='w',encoding='utf-8') as f:
    f.write(response.read().decode('utf-8'))  # 将网页内容写入文件

response.close()  # 关闭response对象