import requests

url = 'http://httpbin.org/post'

s = input('请输入要发送的数据：')    # 输入要发送的数据

dat = {
    'name': 'zhangxw', 'age': s
}    # 要发送的数据

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

response = requests.post(url=url, headers=dic, data=dat)    # 发送post请求

print(response.json())    # 打印响应内容 

response.close()    # 关闭响应