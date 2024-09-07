print("叠数问题。求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制")
x=int(input("请输入一个数字"))
y=int(input("请输入加数个数"))
sum=0
z=x
for  i in range(y):
    sum = 10*sum+x
    z=z+sum
print("这几个数的叠数和为",z)