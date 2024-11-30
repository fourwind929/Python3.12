import random
a=random.randint(1,10)
b=int(input("输入猜数"))
while b!=a:
    if b>a:
        print("猜大了")
        b=int(input("输入猜数"))
    else:
        print("猜小了")
        b=int(input("输入猜数"))
else:
    print("猜对了")
    
        



