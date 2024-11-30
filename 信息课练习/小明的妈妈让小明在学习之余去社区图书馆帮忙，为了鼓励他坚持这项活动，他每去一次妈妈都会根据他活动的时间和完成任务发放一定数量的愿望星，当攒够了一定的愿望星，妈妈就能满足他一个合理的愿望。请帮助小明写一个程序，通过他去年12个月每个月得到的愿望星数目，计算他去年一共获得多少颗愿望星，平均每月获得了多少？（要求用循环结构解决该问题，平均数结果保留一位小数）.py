print("12个月每个月得到的愿望星数目分别为")
x=12
sum=0
for i in range(x):
    a = int(input())
    sum = sum + a
y=sum/x
print("愿望星总数为",sum)
print("平均每月愿望星数目是",y)
