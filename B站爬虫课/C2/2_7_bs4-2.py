import re
import requests
from bs4 import BeautifulSoup
import os
import time

#单个子页面中如果是图集，此程序会趋势！！！
#如这个页面：https://www.umeituku.com/bizhitupian/weimeibizhi/204681.htm

url = 'https://www.umeituku.com/bizhitupian/weimeibizhi/'

#请求头:
dic = {
    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    # ,"cookie":"__51vcke__KSHU1VNqce379XHB=e2d5e8e9-ef05-5edd-9cac-7149be0a7205; __51vuft__KSHU1VNqce379XHB=1725097450942; __vtins__KSHU1VNqce379XHB=%7B%22sid%22%3A%20%22184f38a8-33a0-5bad-9bd2-3d87efd67d63%22%2C%20%22vd%22%3A%201%2C%20%22stt%22%3A%200%2C%20%22dr%22%3A%200%2C%20%22expires%22%3A%201725119999999%2C%20%22ct%22%3A%201725119341589%7D; __51uvsct__KSHU1VNqce379XHB=3; Hm_lvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725097452,1725119342; HMACCOUNT=1589301F85258CBA; Hm_lvt_0113b461c3b631f7a568630be1134d3d=1725097452,1725119342; Hm_lvt_8e745928b4c636da693d2c43470f5413=1725097452,1725119342; Hm_lpvt_0113b461c3b631f7a568630be1134d3d=1725121061; Hm_lpvt_93b4a7c2e07353c3853ac17a86d4c8a4=1725121061; Hm_lpvt_8e745928b4c636da693d2c43470f5413=1725121061"
    ,"referer":""
}

response = requests.get(url=url, headers=dic)
response.encoding = 'utf-8'

main_page = BeautifulSoup(response.text, 'html.parser')

#获取图片链接
alist = main_page.find_all('div', {'class': 'TypeList'})[0].find_all('a')

for a in alist:
    href = a.get('href')
    # print(href)

    child_page_response = requests.get(url=href, headers=dic)
    child_page_response.encoding = 'utf-8'

    child_page = BeautifulSoup(child_page_response.text, 'html.parser')
 
    #获取图片链接
    div = child_page.find('div', attrs={'class': 'ImageBody'})
    p = div.find('p')
    img = p.find('img')
    img_name = img.get('alt')
    img_url = img.get('src')


    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    folder = download_folder
    folder = download_folder  +  "/示例文件夹"
    if not os.path.exists(folder):   # 如果路径不存在，则创建路径
        os.makedirs(folder)
    os.chdir(folder)

    #下载图片
    img_response = requests.get(img_url, headers=dic)
    with open(f"{img_name}.jpg", 'wb') as f:
        f.write(img_response.content)
    print(f"图片{img_name}下载完成")
    time.sleep(5)

response.close()
print("全部图片下载完成")