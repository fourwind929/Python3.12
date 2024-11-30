import requests
import re
import csv

url = "https://movie.douban.com/top250"

dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头

response = requests.get(url=url,headers=dic)

page_content = response.text

#提取电影名称
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
                 r'</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<numberevaluate>.*?)人评价</span>',re.S) 

result = obj.finditer(page_content)

f = open("豆瓣电影排行.csv","w",encoding="utf-8")
writer = csv.writer(f)

for i in result:
    # print(i.group("name"))
    # print(i.group("year").strip(),"年")
    # print(i.group("score"),"分")
    # print(i.group("numberevaluate"),"人评价")
    # print("----------------------------")
    dic = i.groupdict()
    dic["year"] = dic["year"].strip()
    writer.writerow([dic["name"],dic["year"],dic["score"],dic["numberevaluate"]])
    print("写入成功")

    
response.close() 
print("爬取完成")