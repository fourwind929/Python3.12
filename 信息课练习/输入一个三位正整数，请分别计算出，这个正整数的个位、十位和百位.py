x=int(input("输入一个三位正整数"))
a=x//100
b=(x-100*a)//10
c=(x-100*a-10*b)//1
print("这个三位数的百位、十位、个位数字是")
print("百位",a)
print("十位",b)
print("个位",c)
