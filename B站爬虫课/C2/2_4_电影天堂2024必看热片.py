# 2_4_电影天堂2024必看热片.py
from calendar import c
from tokenize import cookie_re
import requests
import re
import csv

domain = "https://www.dytt89.com/"

headers = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}#请求头

# requests.packages.urllib3.disable_warnings()
response = requests.get(url=domain,verify=False,headers=headers)#请求网页
response.encoding = "gb2312"
# print(response.text)

# 定义正则表达式
obj1 = re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3 = re.compile(r'◎片　　名(?P<moviename>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_magnet>.*?)">',re.S)

child_href_list = []#子链接列表

result1 = obj1.finditer(response.text)

print("取得父链接成功")
for i in result1:
    ul = i.group('ul')
    # print(ul)
    
    result2 = obj2.finditer(ul) 
    for itt in result2:
        # print(itt.group('href')) 
        child_href = domain + itt.group('href').strip("/")#拼接子链接
        child_href_list.append(child_href)#添加子链接到列表

print("取得子链接列表成功")
#print(child_href_list)
f = open("电影天堂2024必看热片.csv","w",encoding="utf-8")
writer = csv.writer(f)
print("打开csv文件成功")

print("开始爬取子链接")
for href in child_href_list:
    print("取得单个链接成功")
    child_response = requests.get(url=href,verify=False,headers=headers)#请求网页
    child_response.encoding = "gb2312"
    # print(child_response)
    result3 = obj3.search(child_response.text)
    
    print("开始写入csv文件")
    # print(result3.group('moviename'))
    # print(result3.group('download_magnet'))
    # print("打印成功")
    writer.writerow([result3.group('moviename'),result3.group('download_magnet')])
    print("写入成功")

print("爬取完成")
response.close() 