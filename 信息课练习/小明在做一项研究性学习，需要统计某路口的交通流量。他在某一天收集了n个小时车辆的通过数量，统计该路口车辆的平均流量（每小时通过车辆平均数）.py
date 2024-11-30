print("--------------------统计该路口车辆的平均流量-------------------")
x=int(input("观察所用时间为（小时）"))
sum=0
print("每小时通过车辆分别为")
for i in range(x):
    a = int(input())
    sum = sum + a
y=sum/x
print("该路口车辆的平均流量为",y,"辆/每小时")
