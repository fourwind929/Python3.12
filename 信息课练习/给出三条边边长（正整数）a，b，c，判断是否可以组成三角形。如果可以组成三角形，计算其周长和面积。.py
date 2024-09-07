a=int(input("请输入第一条边长"))
b=int(input("请输入第二条边长"))
c=int(input("请输入第三条边长"))
if a+b>c:
    print("这三边可以组成一个三角形")
    z=a+b+c
    p=(a+b+c)/2
    s=(p*(p-a)*(p-b)*(p-c))**0.5
    print("这三边的周长是",z,"，面积是",s)
else:
    print("这三边不可以组成一个三角形")
