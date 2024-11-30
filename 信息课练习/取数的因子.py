x=int(input("请输入房间的编号："))
for i in range(1,x+1):
    if x % i == 0:
        print(i,end=" ")
