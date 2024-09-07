a=int(input("请输入心跳数a"))
b=int(input("请输入心跳数b"))
r=(a-b)/10
if r>=3:
    print("心脏恢复率为",r,"良好")
else:
    print("心脏恢复率为",r,"不佳")
 
