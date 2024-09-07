import requests

x = input("请输入抖音/快手视频链接：")

url = f"{x}"

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头

response = requests.get(url,headers=dic)

open("video.mp4","wb").write(response.content)
