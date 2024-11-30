import sys
card = 10000  # 初始化银行卡余额
t = 3  # 初始化密码输入次数限制

print('欢迎光临！本机可提供以下服务：1、取款 2、存款 3、密码修改 4、退出')
print('------------------------------------------------------------------')

while t != 0:  # 循环结构，最多3次输入密码
    password = int(input('请输入密码（6位数字）：'))
    
    if password == 123456:  # 分支结构，判断密码正确，进入操作选项选择
        choice = int(input('请输入你的服务选择：1、取款 2、存款 3、密码修改 4、退出 ——>'))

        while choice != -1:  # 循环结构，重复进行各项ATM机操作
            if choice == 1:  # 分支结构，进行取款操作(取款后显示余额，如余额不足，不能取款显示余额不足),继续输入其他选项
                que = int(input("请输入取款金额："))
                while que > card:
                    que = int(input("余额不足,请重新输入取款金额："))
                else:
                    print("取走", que, "元")
                    card = card - que
                    print("您的余额为", card, "元")
                choice = int(input('请输入你的服务选择：1、取款 2、存款 3、密码修改 4、退出 ——>'))

            elif choice == 2:  # 分支结构，进行存款操作(存款张数不能多于100张，可重复存款，存款后显示余额),继续输入其他选项
                cun = int(input("请放入纸币（张）"))
                while cun > 100:
                    cun = int(input("存款张数不能多于100张,请重新输入存款张数："))
                else:
                    print("放入纸币", cun, "张")
                    card = card + 100 * cun
                    print("您的余额为", card, "元")
                choice = int(input('请输入你的服务选择：1、取款 2、存款 3、密码修改 4、退出 ——>'))

            elif choice == 3:  # 分支结构，进行密码修改操作(正确密码输入两次，可以修改，两次不匹配不能修改)
                xinmima1 = int(input("请输入新的密码"))
                xinmima2 = int(input("再次输入新的密码"))
                while xinmima2 != xinmima1:
                    xinmima2 = int(input("两次输入不正确，请重新输入第二次密码"))
                else:
                    password = xinmima2
                    print("密码修改成功")
                choice = int(input('请输入你的服务选择：1、取款 2、存款 3、密码修改 4、退出 ——>'))

            elif choice == 4:  # 分支结构，选项4，退出操作
                print("欢迎下次光临！")
                sys.exit()

            else:  # 选项不是1、2、3、4，提示输入选项错误
                print("选项不是1、2、3、4，输入选项错误，请重新输入")
                choice = int(input('请输入你的服务选择：1、取款 2、存款 3、密码修改 4、退出 ——>'))

    else:  # 分支结构，判断输入密码不正确
        t = t - 1

else:  # 3次密码输入错误，提示取卡退出程序
    print("次密码输入错误，请取卡退出程序")