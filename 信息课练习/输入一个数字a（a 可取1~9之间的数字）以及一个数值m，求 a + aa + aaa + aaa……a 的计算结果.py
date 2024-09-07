import math
a=int(input("输入重复的数字"))
m=int(input("输入循环次数"))
s = 0
for i in range(m):
    s=s+(a+a*pow(10, i))
print("结果是",s-1)
