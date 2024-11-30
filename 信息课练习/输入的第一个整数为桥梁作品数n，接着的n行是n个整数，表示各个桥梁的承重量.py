n=int(input("桥梁作品数量是"))
max=int(input("该桥梁的称重量为"))
for i in range(n-1):
    x=int(input("该桥梁的称重量为"))
    if x>max:
        max=x
print("最大称重量为",max)
