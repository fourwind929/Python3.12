x=int(input("请输入当天健步走的步数"))
sum=0
if x<2000:
    sum=1
else:
    
    sum=(x//2000)*10
print("此用户当天积分为",sum)
