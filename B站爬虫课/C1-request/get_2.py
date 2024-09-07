import requests

# x = input("请输入要搜索的内容：")
url = "https://movie.douban.com/j/chart/top_list?"#豆瓣电影排行榜

param = {
    "type": "24",#电影类型
    "interval_id": "100:90",#时间跨度
    "action": "",#排序方式
    "start": 0,#开始的位置
    "limit": 20,#每页显示的条数
}#请求参数

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头

response = requests.get(url=url, params=param, headers=dic)#发送请求

print(response.json())#页面源代码

response.close() 