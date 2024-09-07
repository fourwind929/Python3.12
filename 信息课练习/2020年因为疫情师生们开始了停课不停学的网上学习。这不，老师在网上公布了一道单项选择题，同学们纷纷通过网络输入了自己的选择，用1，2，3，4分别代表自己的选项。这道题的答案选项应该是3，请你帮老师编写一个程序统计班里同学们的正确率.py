count=0
x=int(input("提交答案的同学一共有（名）"))
for i in range(x):
    a=int(input("该名同学提交的答案是"))
    if a==3:
        count=count+1
    else:
        count=count

y=count/x
print("同学们的正确率是",y)
        
