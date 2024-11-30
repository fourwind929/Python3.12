x=int(input("请输入数字："))
y=0
for i in range(1,x+1):
    if i % 7 == 0 or i % 10 ==7:
        print(i,end=" ")
        y=y+1
print("共有",y,"个")

