# 2_4_电影天堂2024必看热片.py
import requests
import re
import csv

domain = "https://www.dytt89.com/"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}  # 请求头

try:
    response = requests.get(url=domain, headers=headers)  # 请求网页，默认验证SSL证书
    response.encoding = "gb2312"
    # print(response.text)

    # 正则表达式
    obj1 = re.compile(r"2024必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
    obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)
    obj3 = re.compile(r'◎片　　名(?P<moviename>.*?)<br />.*?'
                      r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_magnet>.*?)">', re.S)

    child_href_list = []  # 子链接列表

    result1 = obj1.finditer(response.text)

    for i in result1:
        ul = i.group('ul')
        # print(ul)

        result2 = obj2.finditer(ul)
        for itt in result2:
            # print(itt.group('href'))
            child_href = domain + itt.group('href').strip("/")  # 拼接子链接
            child_href_list.append(child_href)  # 添加子链接到列表

    # print(child_href_list)
    with open("dytt89.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)

        for href in child_href_list:
            try:
                child_response = requests.get(url=href, headers=headers)  # 请求网页，默认验证SSL证书
                child_response.encoding = "gb2312"
                # print(child_response.text)
                result3 = obj3.search(child_response.text)
                if result3:
                    dic = result3.groupdict()
                    writer.writerow(dic.values())
            except Exception as e:
                print(f"请求子链接 {href} 失败: {e}")

except Exception as e:
    print(f"请求主域名 {domain} 失败: {e}")
