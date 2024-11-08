

while restart == "y":

    print("请输入视频号,如BVxxxxxxxxxx：")
    bv = input("请输入视频号：")
    
    # 处理用户输入的循环
    while True:
        if not obj_BV.match(bv):
            print("输入的视频号不符合格式！")
            bv = input("请重新输入视频号：")
            continue  # 继续上面的循环重新输入
        else:
            break  # 输入合法，跳出当前循环
        
    url = f"https://www.bilibili.com/video/{bv}/"
    
    response = requests.get(url, headers=dic)  # 发送请求
    response.encoding = 'utf-8'

    result_title_findErro = obj_title_findErro.search(response.text)
    if result_title_findErro == None:
        result_title = obj_title_find.search(response.text)
        title = result_title.group("title")
    else:
        title = result_title_findErro.group("title_find1")

    if "出错啦!" in title or "视频去哪了呢？" in title:
        print("视频不存在或已被删除！")
        continue  # 视频不可用时，直接回到输入 BV 的部分

    print("获取标题成功")
    title_choice = input(f"是否下载标题为:《{title}》,的视频？(y/n): ")

    if title_choice == "n":
        choice = input("视频不对？是否输入新的BV号？按y重新输入，按n直接下载已输入BV号视频，按e退出程序：")
        if choice == "y":
            continue  # 直接重新进入输入视频号的逻辑
        elif choice == "e":
            response.close()  # 关闭请求
            print("程序已退出。")
            exit()

    # 如果选择下载
    if title_choice == "y":
