# 使用BeautifulSoup解析网页，爬取绿果网蔬菜报价表

import requests
from bs4 import BeautifulSoup
import csv

dict = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

f = open('蔬菜报价表.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['时间','生产地','类别','品种及市场趋势','联系方式'])

url = 'http://www.shucai123.com/price/'

response = requests.get(url=url, headers=dict) # 发送请求，获取响应

# print(response.text)

page = BeautifulSoup(response.text, 'html.parser')# 解析网页,注意:第二个参数解析器"html.parser"使bs4能够解析网页

table = page.find('table',attrs={'class':'bjtbl'}) #class是python关键字,可用class_代替class，或使用attrs={'class':'xxxxx'}
# print(table)

trs = table.find_all('tr')[1:] # 取出第二行开始的所有行
for tr in trs:
    tds = tr.find_all('td')# 取出每一行的td
    # print(td)
    time = tds[0].text.strip() # 取出报价时间
    producer = tds[1].text.strip() # 取出生产地
    type = tds[2].text.strip() # 取出菜品类别
    Varieties_market_trends = tds[3].text.strip() # 取出品种及市场趋势
    contacts = tds[4].text.strip() # 取出联系方式
    csv_writer.writerow([time,producer,type,Varieties_market_trends,contacts])
response.close()
f.close()
print('爬取完成')