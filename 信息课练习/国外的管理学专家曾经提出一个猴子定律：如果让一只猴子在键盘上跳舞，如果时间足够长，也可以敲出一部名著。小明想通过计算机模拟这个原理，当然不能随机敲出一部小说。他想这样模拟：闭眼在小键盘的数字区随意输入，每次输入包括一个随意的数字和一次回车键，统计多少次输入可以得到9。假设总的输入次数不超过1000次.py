import random
count=0
x=0
while x != 9:
    x=random.randint(0,10)
    print(x)
    count=count + 1
else:
    print("猜了",count,"次" )
