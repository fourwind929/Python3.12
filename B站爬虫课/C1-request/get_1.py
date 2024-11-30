import requests

x = input("请输入要搜索的内容：")
url = f"https://www.sogou.com/web?query={x}"  

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}

response = requests.get(url=url, headers=dic)

print(response.text)

# with open("sogou.html", "w", encoding="utf-8") as f:
#     f.write(response.text)

response.close()