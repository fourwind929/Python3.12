x=int(input("请输入当月用电量："))
sum=0
if x<=300:
    sum=x*0.5
else:
    sum=300*0.5+(x-300)*0.7
print("本月电费为：",sum)

